rm dist/*
python3 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
pip install --upgrade gooblerpkg
pip install --upgrade gooblerpkg