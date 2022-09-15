rm dist/*
python3 setup.py sdist
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
pip3 install --upgrade gooblerpkg
pip3 install --upgrade gooblerpkg