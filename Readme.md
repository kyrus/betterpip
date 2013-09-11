# Why

Because pip doesn't recursively install the requirements defined
in a package's requirements.txt file when it installs the package.

# Installation

    git clone https://github.com/kyrus/betterpip.git

    mkvirtualenv / workon <your virtualenv>

    pip install .

# Usage

    python -m betterpip install <any pip install args>

For example:

    python -m betterpip install nose

    python -m betterpip install -v nose

    python -m betterpip install -r requirements.txt

    python -m betterpip install --build build-dir -r requirements.txt
