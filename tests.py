import os, pathlib
import pytest

os.chdir( pathlib.Path.cwd() / 'tests' )
print(pathlib.Path.cwd())
pytest.main()