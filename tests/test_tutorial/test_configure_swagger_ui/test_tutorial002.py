from fastapi.testclient import TestClient

from docs_src.configure_swagger_ui.tutorial002 import app

client = TestClient(app)


def test_swagger_ui():
    response = client.get("/docs")
    assert response.status_code == 200, response.text
    assert '"syntaxHighlight": false' not in response.text, (
        "not used parameters should not be included"
    )
    assert '"syntaxHighlight": {"theme": "obsidian"}' in response.text, (
        "parameters with middle dots should be included in a JSON compatible way"
    )
    assert '"dom_id": "#swagger-ui"' in response.text, (
        "default configs should be preserved"
    )
    assert "presets: [" in response.text, "default configs should be preserved"
    assert "SwaggerUIBundle.presets.apis," in response.text, (
        "default configs should be preserved"
    )
    assert "SwaggerUIBundle.SwaggerUIStandalonePreset" in response.text, (
        "default configs should be preserved"
    )
    assert '"layout": "BaseLayout",' in response.text, (
        "default configs should be preserved"
    )
    assert '"deepLinking": true,' in response.text, (
        "default configs should be preserved"
    )
    assert '"showExtensions": true,' in response.text, (
        "default configs should be preserved"
    )
    assert '"showCommonExtensions": true,' in response.text, (
        "default configs should be preserved"
    )


def test_get_users():
    response = client.get("/users/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello foo"}
