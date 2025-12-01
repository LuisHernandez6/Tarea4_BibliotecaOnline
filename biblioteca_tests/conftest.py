import pytest
import os
import base64
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    driver = getattr(item.instance, "driver", None)

    if driver and rep.when == "call":
        try:
            # Crear carpeta para screenshots
            os.makedirs("screenshots", exist_ok=True)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_file = os.path.join("screenshots", f"{item.name}_{now}.png")

            # Guardar screenshot
            driver.save_screenshot(screenshot_file)

            # Convertir a base64
            with open(screenshot_file, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")

            # Obtener plugin de pytest-html
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(encoded, mime_type="image/png"))
                rep.extra = extra

        except Exception as e:
            print(f"No se pudo tomar screenshot: {e}")
