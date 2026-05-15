# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| latest (main) | :white_check_mark: |

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.**

If you discover a security vulnerability in this project, please report it privately via one of the following methods:

1. **GitHub Private Advisory** — Go to [Security > Advisories](https://github.com/ivarunsharma/crewai-trip-planner/security/advisories/new) and click "Report a vulnerability". This is the preferred method.
2. **Email** — Send details to **contact4varun@gmail.com** with the subject line: `[SECURITY] crewai-trip-planner`

### What to include in your report

- A description of the vulnerability and its potential impact
- Steps to reproduce the issue
- Any proof-of-concept code or screenshots (if applicable)
- Your suggested fix (optional but appreciated)

### Response timeline

| Action | Target time |
|--------|-------------|
| Initial acknowledgement | Within 48 hours |
| Triage and severity assessment | Within 5 business days |
| Fix or mitigation shipped | Within 30 days for critical issues |

You will be credited in the release notes unless you prefer to remain anonymous.

## Known Security Considerations

### API Keys

This project requires API keys (`AZURE_OPENAI_API_KEY`, `SERPER_API_KEY`). Follow these practices:

- **Never** commit `.env` files or hardcode API keys in source code.
- Store secrets in a `.env` file (already listed in `.gitignore`).
- Rotate any key that you suspect has been exposed.
- Use environment-scoped keys (dev vs. prod) where your provider allows it.

### Dependency Security

- We recommend running `pip audit` regularly to check for known vulnerabilities in dependencies.
- Dependabot is enabled on this repo to automatically flag outdated or vulnerable packages.

## Security Best Practices for Contributors

- Do not log or print API keys, tokens, or personal data.
- Validate and sanitize all user-supplied inputs before passing them to external APIs or executing expressions (e.g., the calculator tool).
- Avoid using `eval()` or `exec()` on untrusted input.
- Keep dependencies pinned to specific versions in `requirements.txt` and update them deliberately.

## Scope

The following are **in scope** for vulnerability reports:

- API key or secret leakage via the application
- Remote code execution via the calculator or search tools
- Prompt injection attacks that alter agent behavior in unintended ways
- Dependency vulnerabilities with a direct exploit path

The following are **out of scope**:

- Vulnerabilities in upstream services (Azure OpenAI, Serper, CrewAI library)
- Social engineering attacks
- Issues that require physical access to a user's machine

Thank you for helping keep this project and its users safe.
