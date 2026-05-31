#!/bin/bash
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
MOCK_DIR="$PROJECT_DIR/mock-server"

echo "=== AI电商客服系统 启动脚本 ==="

if ! command -v java &> /dev/null; then
    echo "错误: 未找到Java，请安装JDK 17+"
    exit 1
fi

if ! command -v mvn &> /dev/null; then
    echo "错误: 未找到Maven，请安装Maven"
    exit 1
fi

echo "正在启动Java Mock服务..."
cd "$MOCK_DIR"
mvn spring-boot:run -q &
MOCK_PID=$!
echo "Mock服务 PID: $MOCK_PID"

echo "等待Mock服务启动..."
for i in $(seq 1 30); do
    if curl -s http://localhost:8080/api/products > /dev/null 2>&1; then
        echo "Mock服务启动成功！"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "Mock服务启动超时"
        kill $MOCK_PID 2>/dev/null
        exit 1
    fi
    sleep 1
done

echo "正在启动Python客服服务..."
cd "$PROJECT_DIR"
python3 main.py &
PYTHON_PID=$!
echo "Python服务 PID: $PYTHON_PID"

echo ""
echo "=== 启动完成 ==="
echo "Mock API: http://localhost:8080"
echo "客服界面: http://localhost:7860"
echo ""
echo "按Ctrl+C停止所有服务"

cleanup() {
    echo "正在停止服务..."
    kill $MOCK_PID 2>/dev/null
    kill $PYTHON_PID 2>/dev/null
    echo "服务已停止"
    exit 0
}

trap cleanup SIGINT SIGTERM

wait
