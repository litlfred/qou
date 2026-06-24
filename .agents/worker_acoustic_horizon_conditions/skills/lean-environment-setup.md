# Lean Environment Setup (Copied from local skill)

Refer to `.claude/skills/local/lean-environment-setup.md` for full instructions.

Key highlights:
- **Direct Lean verification**: Run `lean` directly with manual `LEAN_PATH` (or use the package's `./scripts/lean-verify.sh`) to avoid `lake build` wiping restored oleans or rebuilding mathlib from source.
- **Cache restoration**: Monolithic QOU cache or multi-package cache can be restored via `./scripts/lake-cache-fetch.sh` or `./scripts/lake-cache-fetch-multi.py`.
- **Sandbox environment**: Always check if elan/lean are on the PATH and restore oleans if needed.
