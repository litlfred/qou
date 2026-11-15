#!/usr/bin/env python3
"""witness-parity — does a producer still reproduce its committed witness?

Story TOOLS T4 of the migration epic qou-k3er (2026-10-04). Wrapping a producer
as a folio-assistant Tool node must not change what it computes, and this is
the check every such story runs. It is a PARITY ORACLE, never a writer: the
committed witness is never modified, and a re-run is undone before exit.

Three verdicts, never two (the TOOLS analysis measured why, docs/audits/
2026-10-04-workplan-and-migration/TOOLS_report.md section 3):

  PASS     the re-run output equals the committed witness after masking
           qou_substrate.witness._EPHEMERAL_META_FIELDS, AND the current
           environment matches the witness's own `environment` block.
  FAIL     the environment matches but the output differs substantively.
  UNKNOWN  the environment cannot be matched (e.g. pyhecke_native or clarabel
           missing), or the producer could not be run. A difference measured
           in a different environment proves nothing: the committed
           chi-sym-alt-closed-form witness differs at the ~60th digit when
           re-run without pyhecke_native. UNKNOWN is never reported as PASS.

Static checks (always, no re-run): the script's current content hash against
the witness's `scriptHash`, and the environment comparison.

Usage:
  python3 scripts/witness-parity.py computations/<name>.witness.json          # static
  python3 scripts/witness-parity.py computations/<name>.witness.json --run    # re-run
  add --json for a machine-readable verdict.

Exit: 0 PASS (or static OK), 1 FAIL, 2 UNKNOWN / could not determine.

--run executes the witness's own `invocation.reproduce` command from the repo
root. It refuses unless the working tree is clean, and afterwards restores every
tracked file the producer touched (`git checkout --`) and removes every new
untracked file it created, so the tree is left exactly as it was found.
"""
from __future__ import annotations

import argparse
import importlib.metadata as md
import json
import platform
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import (  # noqa: E402
    _EPHEMERAL_META_FIELDS,
    _strip_ephemeral_fields,
    file_content_hash,
)

# Keys in `environment` that are not importable distributions.
_NON_PACKAGE_ENV_KEYS = {"python", "pyhecke_native_build"}


def installed_version(dist: str) -> str | None:
    for name in (dist, dist.replace("_", "-")):
        try:
            return md.version(name)
        except md.PackageNotFoundError:
            continue
    return None


def compare_environment(recorded: dict | None) -> list[str]:
    """Return human-readable mismatches; [] means the environment matches."""
    if not recorded:
        return ["witness records no `environment` block"]
    out = []
    for key, want in recorded.items():
        if key == "python":
            have = platform.python_version()
        elif key in _NON_PACKAGE_ENV_KEYS:
            # A build id cannot be read back from an installed wheel here;
            # it only matters when the package itself is present.
            continue
        else:
            have = installed_version(key)
        if have != str(want):
            out.append(f"{key}: witness {want}, here {have or 'absent'}")
    return out


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def rerun(witness_path: Path, witness: dict) -> tuple[dict | None, str]:
    cmd = (witness.get("invocation") or {}).get("reproduce")
    if not cmd:
        return None, "witness has no invocation.reproduce"
    if git("status", "--porcelain", "--untracked-files=all").strip():
        return None, "working tree not clean; refusing to run (the run is undone by git, which needs a clean start)"
    try:
        proc = subprocess.run(shlex.split(cmd), cwd=ROOT, capture_output=True, text=True, timeout=3600)
        rerun_witness = json.loads(witness_path.read_text()) if witness_path.exists() else None
        note = f"exit {proc.returncode}"
    finally:
        changed = [l[3:] for l in git("status", "--porcelain", "--untracked-files=all").splitlines()]
        tracked = [p for p in changed if git("ls-files", "--", p).strip()]
        untracked = [p for p in changed if p not in tracked]
        if tracked:
            git("checkout", "--", *tracked)
        for p in untracked:
            (ROOT / p).unlink(missing_ok=True)
    return rerun_witness, note


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("witness", type=Path)
    ap.add_argument("--run", action="store_true", help="re-run the producer (undone afterwards)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    wpath = (ROOT / a.witness).resolve() if not a.witness.is_absolute() else a.witness
    committed = json.loads(wpath.read_text())
    report: dict = {"witness": str(wpath.relative_to(ROOT)), "checks": {}}

    script = committed.get("scriptFile")
    spath = ROOT / "computations" / script if script else None
    if spath and spath.exists() and committed.get("scriptHash"):
        now = file_content_hash(str(spath), len(committed["scriptHash"]))
        report["checks"]["scriptHash"] = "same" if now == committed["scriptHash"] else f"changed ({committed['scriptHash']} -> {now})"
    else:
        report["checks"]["scriptHash"] = "unknown (script or hash missing)"

    env_mismatch = compare_environment(committed.get("environment"))
    report["checks"]["environment"] = env_mismatch or "matches"

    if not a.run:
        ok = report["checks"]["scriptHash"] == "same" and not env_mismatch
        report["verdict"] = "STATIC-OK" if ok else "UNKNOWN"
    else:
        produced, note = rerun(wpath, committed)
        report["checks"]["run"] = note
        if produced is None:
            report["verdict"] = "UNKNOWN"
        else:
            equal = _strip_ephemeral_fields(produced) == _strip_ephemeral_fields(committed)
            report["checks"]["substantiveEqual"] = equal
            report["verdict"] = "UNKNOWN" if env_mismatch else ("PASS" if equal else "FAIL")
    report["maskedFields"] = sorted(_EPHEMERAL_META_FIELDS)

    if a.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['verdict']}  {report['witness']}")
        for k, v in report["checks"].items():
            print(f"  {k}: {v}")
    return {"PASS": 0, "STATIC-OK": 0, "FAIL": 1}.get(report["verdict"], 2)


if __name__ == "__main__":
    sys.exit(main())
