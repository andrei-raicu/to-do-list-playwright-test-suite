# Description

This project showcases the use of Playwright and Pytest to automate an E2E UI test suite.
The Application Under Test is https://todolist.james.am/#/.

# Dependencies

The code in this repository uses the following Python version `3.10.4`. Please make sure to have either this or the [latest version of Python](https://www.python.org/downloads/) on your machine before attempting to run this test suite.

- [Windows installation guide](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
- [Mac installation guide using brew](https://docs.brew.sh/Homebrew-and-Python)

# Test project setup

Make sure you are inside the test project folder.

Inside the project, create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) using the [venv](https://docs.python.org/3/library/venv.html) module to manage dependency packages locally:

`$ python -m venv venv`

Activate the virtual environment. On macOS or Linux, use the following command:

`$ source venv/bin/activate`

The equivalent command for a Windows command line is:

`> venv\Scripts\activate.bat`

Install the dependencies using this command:

`pip install -r requirements.txt`

After the Python packages are installed, we need to install the browsers for Playwright. The playwright install command installs the latest versions of the three browsers that Playwright supports: Chromium, Firefox, and WebKit:

`$ playwright install`

Run tests (headless by default):

`python -m pytest tests`

Run tests in headed mode:

`python -m pytest tests --headed`

Slow down test execution:

`python -m pytest tests --headed --slowmo 400`

For more information with regards to CLI arguments please consult the [playwright pytest plugin documentation](https://playwright.dev/python/docs/test-runners)

## Extras

Run tests in parallel:

`python -m pytest tests -n auto`

> Note:
> With auto pytest will spawn a number of workers processes equal to the number of available CPUs. You can also set as many number of workers you want ie. `python -m pytest tests -n 4`
>
> For more information please consult the [pytest-xdist documentation](https://pytest-xdist.readthedocs.io/en/stable/)

Re-run all failures

`python -m pytest tests --reruns 3`

> Note:
> For more information please consult the [pytest-rerunfailures documentation](https://pypi.org/project/pytest-rerunfailures/)
