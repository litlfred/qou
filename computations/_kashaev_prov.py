"""Minimal witness-provenance stamper for the Kashaev/Whitehead audit-only
producers — adds the `engine`/`scriptFile`/`commitSha` triple (plus
`computedAt`/`auditOnly`/`engineVersion`) required by
`computations/audits/witness_provenance_audit.py`."""
from __future__ import annotations

import os
import platform
import subprocess
from datetime import datetime, timezone


def add_provenance(w: dict, script_file: str, engine: str = "python") -> dict:
    here = os.path.dirname(os.path.abspath(script_file))
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=here, stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        sha = None
    w["engine"] = engine
    w["engineVersion"] = platform.python_version()
    w["scriptFile"] = os.path.basename(script_file)
    w["commitSha"] = sha
    w["computedAt"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    w["auditOnly"] = True
    return w
