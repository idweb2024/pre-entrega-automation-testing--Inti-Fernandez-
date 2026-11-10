import subprocess
import sys

import pytest


def correr_behave(tag, nombre_reporte):
    """Ejecuta Behave filtrando por un tag y genera reporte JSON + salida pretty."""
    comando = [
        sys.executable, '-m', 'behave',
        '-t', tag,
        '-f', 'json', '-o', f'reports/{nombre_reporte}.json',
        '-f', 'pretty',
    ]
    return subprocess.run(comando)


@pytest.mark.bdd
@pytest.mark.smoke
def test_behave_smoke():
    resultado = correr_behave('@smoke', 'behave_smoke')
    assert resultado.returncode == 0, "Fallaron escenarios @smoke de Behave"


@pytest.mark.bdd
@pytest.mark.regression
def test_behave_regression():
    resultado = correr_behave('@regression', 'behave_regression')
    assert resultado.returncode == 0, "Fallaron escenarios @regression de Behave"