INSERT INTO product (id, name, category, price, stock, description, image_url) VALUES
(1, 'iPhone 15 Pro', '手机', 8999.00, 100, '苹果最新旗舰手机，A17 Pro芯片', 'https://example.com/iphone15.jpg'),
(2, 'MacBook Pro 14', '电脑', 14999.00, 50, 'M3芯片专业笔记本电脑', 'https://example.com/macbook14.jpg'),
(3, 'AirPods Pro 2', '耳机', 1899.00, 200, '主动降噪无线耳机', 'https://example.com/airpods2.jpg'),
(4, 'iPad Air', '平板', 4799.00, 80, 'M1芯片轻薄平板电脑', 'https://example.com/ipad-air.jpg'),
(5, 'Apple Watch Ultra 2', '手表', 6499.00, 60, '钛金属表壳极限运动手表', 'https://example.com/watch-ultra2.jpg'),
(6, 'Mac Mini M2', '电脑', 4499.00, 40, 'M2芯片迷你台式电脑', 'https://example.com/macmini.jpg');

INSERT INTO "order" (id, user_id, product_id, product_name, quantity, total_price, status, create_time) VALUES
(1, 'user001', 1, 'iPhone 15 Pro', 1, 8999.00, '已完成', '2025-05-01 10:30:00'),
(2, 'user001', 3, 'AirPods Pro 2', 2, 3798.00, '已发货', '2025-05-10 14:20:00'),
(3, 'user002', 2, 'MacBook Pro 14', 1, 14999.00, '待付款', '2025-05-15 09:00:00'),
(4, 'user002', 5, 'Apple Watch Ultra 2', 1, 6499.00, '已完成', '2025-05-08 16:45:00');

INSERT INTO coupon (id, code, user_id, discount, type, expire_date, used) VALUES
(1, 'SAVE100', 'user001', 100.00, '满减券', '2025-12-31', false),
(2, 'DISCOUNT20', 'user001', 0.80, '折扣券', '2025-06-30', false),
(3, 'WELCOME50', 'user002', 50.00, '满减券', '2025-09-30', false),
(4, 'VIP9', 'user002', 0.90, '折扣券', '2025-12-31', true);

INSERT INTO after_sale_request (id, order_id, user_id, reason, type, status, create_time) VALUES
(1, 1, 'user001', '手机屏幕有坏点', '退货', '处理中', '2025-05-05 11:00:00'),
(2, 2, 'user001', '左耳耳机有杂音', '换货', '已同意', '2025-05-12 15:30:00');
