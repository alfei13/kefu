def test_import():
    import kefu
    assert kefu is not None

def test_config():
    from kefu.config import Config
    config = Config()
    assert config.dashscope_model == "qwen-plus"
