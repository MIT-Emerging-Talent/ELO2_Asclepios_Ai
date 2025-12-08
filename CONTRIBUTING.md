# Contributing to Asclepios AI

Thank you for your interest in contributing to **Asclepios AI**!\
We welcome contributions that help improve the platform, documentation,
models, and code quality.

------------------------------------------------------------------------

## 🚀 How to Contribute

### 1. Fork the Repository

Click the **Fork** button at the top of the project repository to create
your own copy.

### 2. Clone Your Fork

``` bash
git clone git@github.com:MIT-Emerging-Talent/ELO2_Asclepios_Ai.git
cd asclepios-ai
```

### 3. Create a New Branch

Always create a feature or fix branch in your fork:

``` bash
git checkout -b feature/new-enhancement
```

------------------------------------------------------------------------

## 🧪 Development Setup

Install dependencies:

``` bash
pip install -r requirements.txt
```

Ensure you are using **Python 3.10+**.

------------------------------------------------------------------------

## 📝 Code Standards

To maintain consistency, contributors are expected to follow:

### ✔️ Python Standards

- Use **PEP8** formatting.

- Run linters before submitting a PR:

    ``` bash
    ruff check .
    ```

### ✔️ Markdown Standards

Markdown files are checked using: - `.markdownlint.yml`

Run markdown linting:

``` bash
markdownlint .
```

### ✔️ Folder & File Naming

We follow `.ls-lint.yml` rules for consistent file naming across the
project.

------------------------------------------------------------------------

## 🧪 Testing

Ensure all code added or modified includes tests where applicable.

Run tests:

``` bash
pytest
```

------------------------------------------------------------------------

## 🔄 Submitting a Pull Request (PR)

1. Commit your changes:

    ``` bash
    git commit -m "Add: new enhancement"
    ```

2. Push to your fork:

    ``` bash
    git push origin feature/new-enhancement
    ```

3. Create a Pull Request on GitHub.

**Include the following in your PR:** - Clear description of the
change - Related issue number (if applicable) - Screenshots (for
UI/visual tools) - Test results (if required)

------------------------------------------------------------------------

## 💬 Community Guidelines

- Be respectful and helpful.
- Use clear communication.
- Provide meaningful commit messages.
- Document major changes clearly.

------------------------------------------------------------------------

## 📄 License

By contributing, you agree that your contributions will be licensed
under the **MIT License**, included in this repository.

------------------------------------------------------------------------

Thank you for helping make **Asclepios AI** better!\
For questions or suggestions, feel free to open an issue.
