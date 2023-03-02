python setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*
gh release create v1.1.0.4 ./dist/* --generate-notes