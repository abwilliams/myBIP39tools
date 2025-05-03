# Template for python project

 
    python                      # project root directory
    ├── venv                    # virtual environmnent directory 
    ├── main.py                 # entry point for program 
    ├── modules                 # modules directory
    │   ├── __init__.py         # package file for modules
    │   ├── module1.py          # example module
    │   └── module2.py
    ├── tests                   # unit test directory
    │   ├── __init__.py
    │   ├── test_module1.py     # example unit test module
    │   └── test_module2.py
    ├── README.md               # documentation file
    └── requirements.txt        # list of python packages
 

    Call unit tests with :
        $ python -m unittest discover -s tests

    Call python program with :
        $ python main.py 

    Create 'requirements.txt' with :
        $ point freeze > requirements.txt

    Install requirements with :
        $ pip install -r requirements.txt 

    Create virtual environmnent :
        $ python -m venv venv

    Activate virtual environmnent
        $ source venv/bin/activate

    All calls made from the project root directory python/


