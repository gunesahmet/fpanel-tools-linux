# fpanel-tools-linux

FPanel helper scripts and service configuration templates for Linux.

Secret values in templates are replaced with `ENTER_SECRET_KEY` / `ENTER_API_KEY`; set real values on the server.

## Branch workflow

- `main` and `dev` are protected: nobody pushes to them directly.
- Create your own branch from `dev` (for example `feature/short-name` or `fix/short-name`).
- Push your branch and open a pull request into `dev`.
- A pull request needs one approval before it can be merged.
- `dev` is merged into `main` through a pull request for releases.
