import importlib, os
def test_app_mode_default(monkeypatch):
    monkeypatch.delenv("APP_MODE", raising=False)
    cfg = importlib.import_module("src.calculator.config")
    assert cfg.APP_MODE == "prod"

def test_app_mode_env(monkeypatch):
    monkeypatch.setenv("APP_MODE", "dev")
    cfg = importlib.import_module("src.calculator.config")
    importlib.reload(cfg)
    assert cfg.APP_MODE == "dev"
