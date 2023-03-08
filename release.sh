rm dist/*.*
black .
python setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*
gh release create v2.0.0b dist/* --generate-notes