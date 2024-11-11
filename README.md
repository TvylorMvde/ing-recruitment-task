# 🎯 Recruitment task
The project includes automated tests developed in [Python](https://www.python.org/) using the following testing frameworks: [Pytest](https://docs.pytest.org/en/stable/getting-started.html), [Behave](https://behave.readthedocs.io/en/latest/) and [Playwright](https://playwright.dev/python/docs/intro).

## 📂 Project structure
```
ING-RECRUITMENT-TASK
├─ features
│  ├─ steps
│  │  └─ cookies_steps.py
│  ├─ cookies.feature
│  └─ environment.py
├─ models
│  ├─ base
│  │  ├─ __init__.py
│  │  ├─ clickables.py
│  │  └─ page.py
│  └─ modals
│     ├─ __init__.py
│     └─ cookies.py
├─ tests
│  ├─ __init__.py
│  ├─ conftest.py
│  └─ test_cookies.py
├─ .gitignore
├─ azure-pipelines.yml
├─ logs.py
├─ README.md
└─ requirements.txt
```
#### Glossary:
* `features` - directory containing feature file, step definitions for [Behave](https://behave.readthedocs.io/en/latest/) (BDD testing framework) and `environment.py` module defining environmental controls (hooks).
* `models` - directory containing the UI models (e.g. page objects and modals) used by the test scripts.
* `tests` - directory holding the test-related files, including test cases and fixtures for [Pytest](https://docs.pytest.org/en/stable/getting-started.html).
* `.gitignore` - file that specifies which files and directories should not be tracked by version control system.
* `azure-pipelines.yml` - configuration file for setting up a CI/CD on [Azure DevOps Platform](https://azure.microsoft.com/pl-pl/products/devops).
* `logs.py` - python module responsible for configuring the custom logging messages during tests execution.
* `README.md` - markdown file containing the project documentation.
* `requirements.txt` - file that lists all the Python packages and dependencies required for the project.

## 🛠 Installation
Python 3.10 or newer is required.
#### Clone the repository:
```
git clone https://github.com/TvylorMvde/ing-recruitment-task.git
```
#### Navigate to the project's directory:
```
cd ing-recruitment-task
```
#### Set up the virtual environment:
```
python -m venv venv
```
#### Activate virtual environment:
* bash/zsh:
    ```
    source venv/bin/activate
    ```
* Windows (command line):
    ```
    venv\Scripts\activate.bat
    ```
* Windows (PowerShell):
    ```
    venv\Scripts\Activate.ps1
    ```
#### Install required packages:
```
pip install -r requirements.txt
```
#### Install Playwright browsers:
```
playwright install
```

## 🚀 Running tests
#### Run the tests using [Behave](https://behave.readthedocs.io/en/latest/) and [Playwright](https://playwright.dev/python/docs/intro) frameworks:
```
behave
```
#### Run the tests using [Pytest](https://docs.pytest.org/en/stable/getting-started.html) and [Playwright](https://playwright.dev/python/docs/intro) frameworks:
```
pytest -v -s
```
## 📝 Test reports
The results of the [Pytest](https://docs.pytest.org/en/stable/getting-started.html) and [Playwright](https://playwright.dev/python/docs/intro) test runs are stored in the `playwright-report` directory in the root of the project directory. Each test run generates a report file named according to the browser being used for the tests. The file is named in the following convention: `playwright-report-{browser_name}.zip`.
#### Viewing the reports:
You can view the Playwright test reports using [Playwright Trace Viewer](https://trace.playwright.dev/):

1. Go to [https://trace.playwright.dev/](https://trace.playwright.dev/)
2. Upload the `.zip` report file (e.g. `playwright-report-chromium.zip`)
3. Once uploaded, you can explore the test run in detail, view screenshots, network logs, and interact with the trace data to investigate issues.

## ⚙️ CI/CD
A dedicated `azure-pipeline.yml` YAML file is configured to run the tests across multiple browsers (Chrome and Firefox) on the [Azure DevOps Platform](https://azure.microsoft.com/pl-pl/products/devops). The pipeline performs the following steps:
1. Checkout the repository
2. Set up Python version
3. Install the required dependencies
4. Install browsers
5. Run the tests
6. Generate test reports