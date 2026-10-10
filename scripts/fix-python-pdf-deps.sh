#!/usr/bin/env bash
# Repair the Python PDF-ingestion dependency chain so `pypdf` imports cleanly.
#
# WHY THIS SCRIPT EXISTS
# ----------------------
# `folio-assistant/scripts/pdf-structure.py` (the PDF ingestion tool, corpus
# path uploads/ -> library/) does `from pypdf import PdfReader`. `pypdf` in turn
# imports `cryptography` for its AES crypt-provider, and `cryptography`'s pyo3
# `_rust` extension needs `_cffi_backend` (the `cffi` C extension).
#
# In the Claude-Code-on-the-web sandbox the base image ships:
#   * `cryptography` 41.0.7 as the APT copy under /usr/lib/python3/dist-packages
#     (RECORD-less, so pip cannot uninstall it), and
#   * NO `cffi` at all.
# So `import cryptography.hazmat.bindings._rust` panics with
#   ModuleNotFoundError: No module named '_cffi_backend'
#   pyo3_runtime.PanicException: Python API call failed
# and every `from pypdf import PdfReader` dies. Agents have been shimming around
# this with PyMuPDF instead of fixing it.
#
# THE FIX
# -------
# Install consistent manylinux wheels for `cffi` + `cryptography` + `pypdf` with
# pip. They land in a site-packages dir that PRECEDES /usr/lib/python3/dist-
# packages in sys.path (--user -> ~/.local wins outright), so the working pip
# `cryptography` shadows the broken APT one and its bundled `_rust` matches the
# freshly-installed `_cffi_backend`. `--ignore-installed` is required because the
# APT `cryptography` has no RECORD file and pip's uninstall step aborts on it.
#
# IDEMPOTENT: guarded by an import check, so it is a no-op once the chain works.
# EPHEMERAL host: the install lives in the session container and dies when the
# container is reclaimed, which is why this is wired into the SessionStart hooks
# (.claude/settings.json) — a fresh session re-runs it and re-establishes the fix.
set -uo pipefail

# Already working? Then do nothing (idempotent no-op on a healthy session).
if python3 -c "from pypdf import PdfReader" >/dev/null 2>&1; then
  echo "[fix-python-pdf-deps] pypdf imports cleanly — nothing to do."
  exit 0
fi

echo "[fix-python-pdf-deps] pypdf import broken — installing cffi + cryptography + pypdf wheels"
# --user  -> ~/.local/lib/pythonX.Y/site-packages, which is first on sys.path,
#            so it shadows the RECORD-less APT cryptography outright.
# --ignore-installed -> do not try to uninstall the APT cryptography (no RECORD;
#            pip's uninstall aborts on it).
pip install --user --force-reinstall --no-cache-dir --ignore-installed \
  cffi cryptography pypdf \
  || { echo "[fix-python-pdf-deps] ERROR: pip install failed (network? proxy?)" >&2; exit 1; }

export PATH="$HOME/.local/bin:$PATH"

# Verify the real target, not just the wheels.
if python3 -c "from pypdf import PdfReader; print('[fix-python-pdf-deps] pypdf OK')"; then
  echo "[fix-python-pdf-deps] done — folio-assistant/cat-harness/scripts/pdf-structure.py can run."
else
  echo "[fix-python-pdf-deps] ERROR: pypdf still fails to import after install" >&2
  exit 1
fi
