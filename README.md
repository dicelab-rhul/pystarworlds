# pystarworlds

LOCAL INSTALL PROCEEDURE:

1. Clone the repository
2. Navigate to the pystarworlds directory (the one that contains setup.py) in terminal
3. pip install -e .


PIP UPLOAD

python3 setup.py sdist bdist_wheel
python -m twine upload dist/* 
