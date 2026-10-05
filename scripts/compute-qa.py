#!/usr/bin/env python3
"""compute-qa — run qou's compute-QA gates, one table, one verdict file each.

Story TOOLS T7 (bean `qou-4dj1`). The gates used to live as inline `run:`
blocks in four workflow files (`witness-staleness`, `lp-dual-gate`,
`probe-float64-gate`, `word-provenance-gate`). They are now one table here,
and `processes/tools/compute-qa.bpmn` is the process that orders them; each
workflow step calls `python3 scripts/compute-qa.py --gate <id>` and carries a
`# bpmn-node:` back-reference to its activity.

THE COMMANDS ARE UNCHANGED. Every entry below is the exact argv the workflow
ran, and the mode reproduces what the step did with its exit code:

  strict    a non-zero exit fails the gate (the step had no `|| true`)
  warn      always passes; the output is the report (`|| true` in the step)
  advisory  same as warn, for the "survey (informational, never fails)" steps

A gate whose script cannot even start (missing module, missing binary) is
UNKNOWN, never a pass. A self-test that fails fails the gate whatever its mode,
because a detector without a working known positive reports everything clean.

Verdicts go to `test/results/compute-qa/<gate>.json` (gitignored), which is
the layout `bun run qa:publish` reads, so they land on the `qa-reports` branch
and are never committed. With `GITHUB_STEP_SUMMARY` set, each gate appends the
same heading and first lines the workflow step used to.

    python3 scripts/compute-qa.py --list
    python3 scripts/compute-qa.py --gate q0-anchor-flip
    python3 scripts/compute-qa.py --gate probe-float64-diff --base origin/main
    python3 scripts/compute-qa.py --all            # every gate that needs no setup
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "test" / "results" / "compute-qa"
PY = "python3"


def g(gid, node, title, cmds, mode="strict", lines=14, selftest=None, diff=False, setup=None):
    return dict(id=gid, node=node, title=title, cmds=cmds, mode=mode, lines=lines,
                selftest=selftest, diff=diff, setup=setup)


# One row per former workflow step. `node` is the activity in compute-qa.bpmn.
GATES = [
    # ── witness-staleness.yml, job `staleness` ────────────────────────────────
    g("staleness-report", "Task_Staleness", "Witness staleness (warn-mode)",
      [[PY, "computations/witness_dependency_drift.py"]], mode="warn", lines=20),
    g("q0-anchor-flip", "Task_Staleness", "q0-anchor flip detector (strict)",
      [[PY, "computations/audits/q0_anchor_consistency_audit.py", "--strict"]]),
    g("mpf-float-source", "Task_Precision", "mpf(<float>) source audit (strict)",
      [[PY, "computations/mpf_float_source_audit.py", "--strict"]],
      selftest=[PY, "computations/mpf_float_source_audit.py", "--self-test"]),
    g("import-time-dps", "Task_Precision", "import-time dps ratchet",
      [[PY, "computations/mpf_import_time_dps_audit.py", "--strict"]], lines=16,
      selftest=[PY, "computations/mpf_import_time_dps_audit.py", "--self-test"]),
    g("never-raises-dps", "Task_Precision", "never-raises-dps ratchet",
      [[PY, "computations/never_raises_dps_audit.py", "--strict"]], lines=16,
      selftest=[PY, "computations/never_raises_dps_audit.py", "--self-test"]),
    g("float64-padding", "Task_Precision", "float64-padding ratchet",
      [[PY, "computations/witness_float64_padding_audit.py", "--strict"]],
      selftest=[PY, "computations/witness_float64_padding_audit.py", "--self-test"]),
    g("mpf-context-dps", "Task_Precision", "mp.dps no-op gate",
      [[PY, "computations/mpf_context_dps_audit.py", "--strict"]], lines=20,
      selftest=[PY, "computations/mpf_context_dps_audit.py", "--self-test"]),
    g("module-const", "Task_Precision", "module-const precision gate",
      [[PY, "computations/module_const_precision_audit.py", "--strict"]], lines=24,
      selftest=[PY, "computations/module_const_precision_audit.py", "--self-test"]),
    g("raw-float64", "Task_Precision", "raw-float64 ratchet",
      [[PY, "computations/witness_raw_float64_audit.py", "--strict"]],
      selftest=[PY, "computations/witness_raw_float64_audit.py", "--self-test"]),
    g("q0-value-drift", "Task_Staleness", "q0-value drift ratchet",
      [[PY, "computations/q0_value_drift_audit.py", "--strict"]]),
    g("no-free-parameter", "Task_Precision", "No-free-parameter certificate",
      [[PY, "computations/no_free_parameter_certificate.py", "--strict"]], mode="warn", lines=20,
      selftest=[PY, "computations/no_free_parameter_certificate.py", "--self-test"]),
    g("authors-note-coverage", "Task_Staleness", "Author-note Lean-coverage drift gate",
      [["bun", "run", "scripts/refresh-authors-note.ts", "--check"]],
      setup="./scripts/setup-folio-assistant.sh"),
    # ── lp-dual-gate.yml, job `gate` (needs the MPFR LP binary built first) ────
    g("lp-dual-backend", "Task_LpDual", "Confirm CI solves at 50 dps, not float64",
      [[PY, "scripts/lp-dual-backend-check.py"]],
      setup="cargo build --release --features clarabel-mpfr --bin clarabel-operator-selection-lp (in tools/hecke-engine)"),
    g("pyhecke-tests", "Task_LpDual", "Unit tests — provenance, the rescue, and every backend site",
      [[PY, "-m", "pytest", "tools/pyhecke/tests", "-q"]]),
    g("lp-dual-wired", "Task_LpDual", "Content-wired LP/SDP witnesses must report their duals",
      [[PY, "computations/lp_dual_witness_validator.py", "--strict-wired"]]),
    g("lp-dual-survey", "Task_LpDual", "LP-dual survey (informational)",
      [[PY, "computations/lp_dual_witness_validator.py"]], mode="advisory"),
    # ── probe-float64-gate.yml ────────────────────────────────────────────────
    g("probe-float64-diff", "Task_Probe", "Fail on new float64 entry points",
      [[PY, "scripts/probe-float64-guard.py", "--diff"]], diff=True),
    g("probe-float64-survey", "Task_Probe", "probe-float64 survey (informational)",
      [[PY, "scripts/probe-float64-guard.py"]], mode="advisory"),
    # ── word-provenance-gate.yml ──────────────────────────────────────────────
    g("word-provenance-selftest", "Task_Words", "Detector self-test (known positive)",
      [[PY, "scripts/word-provenance-gate.py", "--selftest"]]),
    g("word-provenance-diff", "Task_Words", "Fail on new hardcoded word literals",
      [[PY, "scripts/word-provenance-gate.py", "--diff"]], diff=True),
    g("word-provenance-survey", "Task_Words", "word-provenance survey (informational)",
      [[PY, "scripts/word-provenance-gate.py"]], mode="advisory"),
]
BY_ID = {x["id"]: x for x in GATES}


def tool_defs_json() -> str:
    """The gate table as the Tool layer reads it; generated, never hand-edited."""
    rows = [dict(id=x["id"], node=x["node"], title=x["title"], mode=x["mode"], diff=x["diff"],
                 setup=x["setup"], command=" ".join(x["cmds"][0])) for x in GATES]
    return json.dumps({"$comment": "GENERATED by scripts/compute-qa.py --write-tool-defs. Do not edit.",
                       "gates": rows}, indent=2, ensure_ascii=False) + "\n"


def changed_py(base: str) -> list[str]:
    p = subprocess.run(["git", "diff", "--name-only", "--diff-filter=d", f"{base}...HEAD", "--", "*.py"],
                       cwd=ROOT, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"git diff against {base} failed: {p.stderr.strip()}")
    return [f for f in p.stdout.split() if f]


def could_not_start(code: int, out: str) -> bool:
    """A command that never reached its own logic: not found, or a missing import."""
    if code == 127:
        return True
    tail = out[-2000:]
    return code != 0 and ("ModuleNotFoundError" in tail or "No such file or directory" in tail
                          and "Traceback" not in tail)


def run_gate(gate: dict, files: list[str] | None) -> dict:
    t0 = time.time()
    log: list[str] = []
    codes: list[int] = []
    verdict, reason = "pass", ""
    if gate["diff"] and not files:
        return dict(gate=gate["id"], node=gate["node"], verdict="pass", reason="no changed .py files",
                    mode=gate["mode"], seconds=0.0, output_sha256="", output_head="")
    steps = ([gate["selftest"]] if gate["selftest"] else []) + gate["cmds"]
    for i, argv in enumerate(steps):
        argv = argv + (files if gate["diff"] and i == len(steps) - 1 else [])
        p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        out = p.stdout + p.stderr
        log.append(out)
        codes.append(p.returncode)
        is_selftest = gate["selftest"] is not None and i == 0
        if could_not_start(p.returncode, out):
            verdict, reason = "unknown", f"`{' '.join(argv[:3])}` could not start (exit {p.returncode})"
            break
        if p.returncode != 0 and (is_selftest or gate["mode"] == "strict"):
            verdict = "fail"
            reason = f"{'self-test' if is_selftest else 'gate'} exited {p.returncode}"
            break
    body = "".join(log)
    return dict(gate=gate["id"], node=gate["node"], title=gate["title"], verdict=verdict, reason=reason,
                mode=gate["mode"], exit_codes=codes, seconds=round(time.time() - t0, 1),
                output_sha256=hashlib.sha256(body.encode()).hexdigest(),
                output_head="\n".join(body.splitlines()[: gate["lines"]]))


def emit(res: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{res['gate']}.json").write_text(json.dumps({"$schema": "qou-compute-qa/v1", **res}, indent=2) + "\n")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(f"## {res.get('title', res['gate'])} — {res['verdict']}\n```\n{res['output_head']}\n```\n")
    mark = {"pass": "✓", "fail": "✗", "unknown": "?"}[res["verdict"]]
    print(f"{mark} {res['gate']:<26} {res['verdict']:<8} {res['seconds']:>7}s  {res['reason']}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--gate", action="append", default=[], help="gate id (repeatable)")
    ap.add_argument("--all", action="store_true", help="every gate that needs no extra setup")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--base", default=None, help="diff base for the --diff gates (e.g. origin/main)")
    ap.add_argument("--files", nargs="*", default=None, help="explicit changed .py files for the --diff gates")
    ap.add_argument("--write-tool-defs", action="store_true", help="write tool-defs/compute-qa-gates.json from the table")
    ap.add_argument("--check-tool-defs", action="store_true", help="exit 1 when tool-defs/compute-qa-gates.json is stale")
    a = ap.parse_args()
    if a.write_tool_defs or a.check_tool_defs:
        text = tool_defs_json()
        path = ROOT / "tool-defs" / "compute-qa-gates.json"
        if a.check_tool_defs:
            ok = path.exists() and path.read_text() == text
            print("✓ tool-defs/compute-qa-gates.json is current" if ok else "✗ stale — run scripts/compute-qa.py --write-tool-defs")
            return 0 if ok else 1
        path.write_text(text)
        print(f"wrote {path.relative_to(ROOT)} ({len(GATES)} gates)")
        return 0
    if a.list:
        for x in GATES:
            print(f"{x['id']:<26} {x['mode']:<9} {x['node']:<15} {x['title']}" + (f"  [setup: {x['setup']}]" if x["setup"] else ""))
        return 0
    ids = a.gate or ([x["id"] for x in GATES if not x["setup"]] if a.all else [])
    if not ids:
        ap.error("give --gate <id>, --all, or --list")
    unknown_ids = [i for i in ids if i not in BY_ID]
    if unknown_ids:
        ap.error(f"no such gate: {', '.join(unknown_ids)} (see --list)")
    files = a.files
    if files is None and any(BY_ID[i]["diff"] for i in ids) and a.base:
        files = changed_py(a.base)
    worst = 0
    for i in ids:
        res = run_gate(BY_ID[i], files)
        emit(res)
        worst = max(worst, {"pass": 0, "unknown": 2, "fail": 1}[res["verdict"]] if res["verdict"] != "fail" else 3)
    return {0: 0, 2: 2, 3: 1}[worst]


if __name__ == "__main__":
    sys.exit(main())
