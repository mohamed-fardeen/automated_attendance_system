# Contributing Guidelines

## Branch Strategy

### Main branches
- `main`   – Production-ready code
- `develop` – Integration / staging

### Feature branches
- `feature/mobile-app`          – React Native student app
- `feature/backend`             – Node.js/Express API
- `feature/facial-recognition`  – Python/Flask ML service
- `feature/dashboard`           – React faculty dashboard

## Workflow

1. Checkout your feature branch from `develop`.
2. Make changes only in your area (folders assigned to your role).
3. Run tests locally.
4. Commit with a clear message.
5. Push and open a Pull Request into `develop`.
6. Wait for CI to pass and at least 1 review approval.
7. After approval, the Integration Lead merges the PR.

## Commit message format

`<type>: <short description>`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
- `feat: add login screen UI`
- `fix: handle empty attendance list`

## Code style

- Use ESLint for JavaScript/TypeScript code.
- Use Black/PEP8 style for Python code.
- Prefer meaningful names and small functions.
- Add comments only for non-obvious logic.

## Testing

- Add or update tests for every new feature or bugfix.
- All tests must pass before merge.
- Avoid committing broken code.

## Pull requests

- Keep PRs focused on one logical change.
- Update docs (README, API, SETUP) if behavior changes.
- Request review from the Integration Lead (Member 6).
