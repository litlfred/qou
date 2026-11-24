#!/usr/bin/env python3
# polynomial_q_not_applicable: static cross-package precision audit; emits no numeric physics.
"""tools_qou_mass_precision_audit.py — static precision gate for `tools/` and `qou-mass/` (bean `qou-4w77`).

Closes the cross-package coverage gap identified in `qou-psjm` / `qou-4w77`
without modifying or re-stamping any of the contended `computations/` audit
witnesses (`qou-v0t8`):

  1. `mpf_float_source`: flags `mpf(<non-dyadic float literal>)` DEFECTs and
     unparseable `.py` files across `tools/` and `qou-mass/` (`mpf_float_source_audit`
     previously scanned `computations/` and `tools/`, omitting `qou-mass/`).
  2. `module_const_precision`: flags LOSSY module-scope `mpf(<literal>)`
     constants built before working precision is raised across `tools/` and
     `qou-mass/` (complementing `module_const_precision_audit.py`, now also
     extended to `computations/`, `tools/`, and `qou-mass/`).
  3. `never_raises_dps`: flags runnable witness-emitting scripts under `tools/`
     and `qou-mass/` that construct `mpmath` values without raising `mp.dps`
     (`never_raises_dps_audit.py` scans `computations/` only).
  4. `mpf_mixed_arithmetic`: flags `float64`-tainted `mpmath` formatting sinks
     under `qou-mass/` using the full cross-repo function-return registry over
     `computations/`, `tools/`, and `qou-mass/` (`mpf_mixed_arithmetic_audit.py`
     previously scanned `computations/` and `tools/`, omitting `qou-mass/`).

Supports `--scan-root <dir>` (repeatable), `--strict`, `--no-witness`, and
`--self-test`. Wired into `scripts/precision-gates.sh` with `--strict --no-witness`
so CI/preflight runs never dirty tracked witness files.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401, E402
import module_const_precision_audit as _mcp  # noqa: E402
import mpf_float_source_audit as _mfs  # noqa: E402
import mpf_mixed_arithmetic_audit as _mma  # noqa: E402
import never_raises_dps_audit as _nrd  # noqa: E402

DEFAULT_SCAN_ROOTS: tuple[str, ...] = ("tools", "qou-mass")
SKIP_PARTS: frozenset[str] = frozenset({
    "_deprecated", "fsh-guts", "__pycache__", ".venv", "venv",
    "target", "build", "dist", "node_modules",
})


def collect_py_files(root: Path, scan_roots: list[str]) -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for d in scan_roots:
        base = Path(d) if Path(d).is_absolute() else (root / d)
        base = base.resolve()
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            if p in seen or (set(p.parts) & SKIP_PARTS):
                continue
            seen.add(p)
            out.append(p)
    return out


def _audit_mpf_float_file(p: Path, root: Path) -> list[dict]:
    prev = _mfs.ROOT
    try:
        _mfs.ROOT = root
        return _mfs.audit_file(p)
    finally:
        _mfs.ROOT = prev


def run_audit(root: Path, scan_roots: list[str]) -> dict:
    root = root.resolve()
    py_files = collect_py_files(root, scan_roots)

    mfs_defects: list[dict] = []
    mfs_blind: list[dict] = []
    mcp_lossy: list[dict] = []
    nrd_defects: list[dict] = []

    for p in py_files:
        for r in _audit_mpf_float_file(p, root):
            if r["class"] == "DEFECT":
                mfs_defects.append(r)
            elif r["class"] in ("unparseable", "unreadable"):
                mfs_blind.append(r)

        try:
            rel = p.relative_to(root).as_posix()
        except ValueError:
            rel = p.as_posix()

        try:
            src = p.read_text(encoding="utf-8")
        except Exception as exc:
            mfs_blind.append({"file": rel, "line": 0, "class": "unreadable", "source": str(exc)})
            continue

        for h in _mcp.find_early_constants(src, rel):
            if h["tier"] == "LOSSY":
                mcp_lossy.append(h)

        if _nrd.emits_witness(src):
            try:
                tree = ast.parse(src)
            except SyntaxError:
                continue
            if _nrd.is_runnable(tree) and not _nrd.raises_precision(tree) and _nrd.mp_value_calls(tree):
                if not _nrd.raises_via_import(p, tree):
                    nrd_defects.append({"file": rel, "mp_calls": len(_nrd.mp_value_calls(tree))})

    # Mixed-arithmetic check over qou-mass/ (and any non-computations scan_root)
    # using full cross-repo registry so -> float annotations from computations/ and tools/ propagate.
    reg_files = collect_py_files(root, list(dict.fromkeys(["computations", *scan_roots])))
    registry = _mma.build_registry(reg_files)
    mma_qou_mass_candidates: list[dict] = []
    for p in py_files:
        try:
            rel_parts = p.relative_to(root).parts
        except ValueError:
            rel_parts = p.parts
        if "tools" in rel_parts and "qou-mass" not in rel_parts:
            # tools/ is already in mpf_mixed_arithmetic_audit.SEARCH_ROOTS and baselined there.
            continue
        prev_mma_root = _mma.ROOT
        try:
            _mma.ROOT = root
            mma_rows = _mma.audit_file(p, registry)
        finally:
            _mma.ROOT = prev_mma_root
        for r in mma_rows:
            if r["class"] == "CANDIDATE":
                mma_qou_mass_candidates.append(r)

    return {
        "scan_roots": list(scan_roots),
        "scanned_py_files": len(py_files),
        "mpf_float_source_defects": mfs_defects,
        "unparseable_or_unreadable": mfs_blind,
        "module_const_lossy": mcp_lossy,
        "never_raises_dps_producers": nrd_defects,
        "qou_mass_mixed_arithmetic_candidates": mma_qou_mass_candidates,
        "blocking_total": (
            len(mfs_defects)
            + len(mfs_blind)
            + len(mcp_lossy)
            + len(nrd_defects)
            + len(mma_qou_mass_candidates)
        ),
    }


def self_test() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        troot = Path(td)
        qm = troot / "qou-mass"
        qm.mkdir()
        (qm / "bad.py").write_text(
            'import mpmath as mp\n'
            'LOSSY = mp.mpf("1.1099785827513808079")\n'
            'BAD_FLOAT = mp.mpf(0.1)\n',
            encoding="utf-8",
        )
        res_bad = run_audit(troot, ["qou-mass"])
        if len(res_bad["mpf_float_source_defects"]) != 1 or len(res_bad["module_const_lossy"]) != 1:
            print(f"SELF-TEST FAILED on bad fixture: {res_bad}")
            return 1

        (qm / "bad.py").write_text(
            'import mpmath as mp\n'
            'mp.mp.dps = 95\n'
            'GOOD = mp.mpf("1.1099785827513808079")\n',
            encoding="utf-8",
        )
        res_good = run_audit(troot, ["qou-mass"])
        if res_good["blocking_total"] != 0:
            print(f"SELF-TEST FAILED on clean fixture: {res_good}")
            return 1

    print("SELF-TEST PASSED — bad fixture caught (mpf(0.1) + early module const), clean fixture 0.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument(
        "--scan-root",
        action="append",
        dest="scan_roots",
        default=None,
        help="directory to scan (repeatable; default: tools, qou-mass)",
    )
    ap.add_argument("--strict", action="store_true", help="exit 1 if blocking_total > 0")
    ap.add_argument("--no-witness", action="store_true", help="do not write witness file")
    ap.add_argument("--self-test", "--selftest", dest="selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return self_test()

    roots = args.scan_roots if args.scan_roots else list(DEFAULT_SCAN_ROOTS)
    summary = run_audit(Path(args.root).resolve(), roots)

    print("=" * 74)
    print(f"TOOLS & QOU-MASS PRECISION AUDIT (bean qou-4w77) — roots={roots}")
    print("=" * 74)
    print(f"  scanned .py files                      : {summary['scanned_py_files']}")
    print(f"  mpf(<non-dyadic float>) defects        : {len(summary['mpf_float_source_defects'])}")
    print(f"  module-const LOSSY (<15 dps at import) : {len(summary['module_const_lossy'])}")
    print(f"  never-raises-dps witness producers     : {len(summary['never_raises_dps_producers'])}")
    print(f"  qou-mass mixed-arithmetic candidates   : {len(summary['qou_mass_mixed_arithmetic_candidates'])}")
    print(f"  unparseable / unreadable blind spots   : {len(summary['unparseable_or_unreadable'])}")
    print(f"  blocking_total                         : {summary['blocking_total']}")

    if not args.no_witness:
        from qou_substrate.witness import WitnessBuilder as _WB

        out = HERE / "tools-qou-mass-precision-audit.witness.json"
        payload = {
            "schema": "witness/v1",
            "name": "tools-qou-mass-precision-audit",
            "scriptFile": os.path.basename(__file__),
            "description": (
                "Static precision audit extending mpf(<float>), module-const "
                "import-time dps, never-raises-dps, and mixed-arithmetic checks "
                "to tools/ and qou-mass/ (bean qou-4w77) without touching "
                "contended computations/ audit witnesses."
            ),
            "data": summary,
            "assertions": [
                {
                    "name": "tools_and_qou_mass_zero_blocking_precision_defects",
                    "computed": summary["blocking_total"],
                    "expected": 0,
                    "passed": summary["blocking_total"] == 0,
                    "source": "tools/ + qou-mass/ static precision scan (bean qou-4w77)",
                }
            ],
            "allPassed": summary["blocking_total"] == 0,
        }
        _WB.stamp_staleness_metadata(
            payload, script_path=__file__, engine="python-stdlib", q0_anchor=False
        )
        out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote {out.relative_to(ROOT)}")

    return 1 if (args.strict and summary["blocking_total"] > 0) else 0


if __name__ == "__main__":
    sys.exit(main())
