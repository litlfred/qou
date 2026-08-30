#!/usr/bin/env python3
"""Predict which bucket-A drains are DRAIN-NO-OPs, without running anything.

Bean `qou-p77d` splits the assertion-float64 tranche into bucket A (the
producer raises `mp.dps`, so the `float()` cast is the defect and removing it
recovers digits) and bucket B (the producer is float64-equivalent, so removing
the cast would launder).  The bean also records, as a trap, that this split is
a STATIC HEURISTIC keyed on the producer's dps call and cannot settle any
single producer.

This script measures the specific way that bites which the bean had not yet
recorded: **a bucket-A producer can still feed float64 VALUES into its
assertions.**  The dps raise is real; it simply does not reach the quantity
being asserted.  `he4_sdp_compositional_probe.py` is the worked case — it
calls `set_compute_dps()`, so the classifier files it A, but its assertion
values come from `lp_dual_solver` as Python floats.

Why that matters for the drain specifically: `_precision.fmt` **short-circuits
a Python `float` to `str(value)`** (its own docstring says so).  So the
prescribed repair on such a field changes the JSON type and nothing else —
`assertion_drain_verify.py` calls that DRAIN-NO-OP.  Running the producer
twice to discover it costs minutes; the shape is visible in the source.

The signal is the ORIGIN of the expression passed to `computed=` / `expected=`,
not the presence of a dps call:

  * a name bound from a numeric-solver result (`res.x_star[...]`,
    `res.duality_gap`, anything off an `np.` / `scipy.` / `linalg` call)
    is float64 whatever the producer's dps is;
  * `math.*` returns a float and silently DOWNCASTS an mpf argument
    (the bean records this for `math.log`);
  * `statistics.*` and a bare `sum()`/`min()`/`max()` over such values
    accumulate in float64.

This is a HEURISTIC over origins and is reported as such: it narrows which
producers to open, and never decides one.  A hit means "expect DRAIN-NO-OP,
look before you run"; a miss does not promise a gain.  Confirm with
`assertion_drain_verify.py` against a fresh baseline, which is the only thing
that actually settles a field.

Usage:
    assertion_value_provenance_audit.py [--list] [--selftest]
"""
from __future__ import annotations

import argparse
import ast
import collections
import glob
import json
import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FLOAT64_MODULES = {"np", "numpy", "scipy", "math", "statistics", "st", "cmath"}
FLOAT64_ATTRS = {"x_star", "y_star", "y0_star", "duality_gap", "primal_obj",
                 "dual_obj", "fun", "x", "eigenvalues", "eigenvals"}


def _root_name(node) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _float64_origin(expr, floaty: set) -> str | None:
    """Name why `expr` is float64-valued, or None."""
    for n in ast.walk(expr):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Attribute):
                mod = _root_name(f)
                if mod in FLOAT64_MODULES:
                    return f"{mod}.{f.attr}() returns float64"
            if isinstance(f, ast.Name) and f.id in ("float", "sum", "min", "max"):
                if f.id == "float":
                    continue  # the cast itself is the thing being removed
                return f"{f.id}() accumulates in float64"
        if isinstance(n, ast.Attribute) and n.attr in FLOAT64_ATTRS:
            return f".{n.attr} is a numeric-solver result (float64)"
        if isinstance(n, ast.Name) and n.id in floaty:
            return f"`{n.id}` was bound from a float64 source"
    return None


def scan(path: pathlib.Path) -> list[tuple[str, str]]:
    try:
        tree = ast.parse(path.read_text())
    except Exception:
        return []

    floaty: set = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            if _float64_origin(node.value, set()):
                floaty.add(node.targets[0].id)

    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        for kw in node.keywords:
            if kw.arg not in ("computed", "expected"):
                continue
            why = _float64_origin(kw.value, floaty)
            if why:
                hits.append((f"line {kw.value.lineno} {kw.arg}=", why))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    sys.path.insert(0, "computations/audits")
    import assertion_value_float64_triage as T
    index = T._producer_index()

    bucketA: dict[str, int] = collections.Counter()
    for p in glob.glob("computations/**/*.witness.json", recursive=True):
        if "_deprecated" in p:
            continue
        try:
            d = json.load(open(p))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        here = 0
        for asrt in d.get("assertions") or []:
            if not isinstance(asrt, dict):
                continue
            for k in ("computed", "expected"):
                v = asrt.get(k)
                if isinstance(v, bool) or not isinstance(v, float):
                    continue
                if not T.is_intlike(v):
                    here += 1
        if here and T.classify_producer(d.get("scriptFile"), index) == "A":
            bucketA[d.get("scriptFile")] += here

    flagged, clean, missing = {}, 0, 0
    for name, n in bucketA.items():
        paths = [q for q in glob.glob(f"computations/**/{name}", recursive=True)
                 if "_deprecated" not in q]
        if not paths:
            missing += 1
            continue
        hits = scan(pathlib.Path(paths[0]))
        if hits:
            flagged[paths[0]] = (n, hits)
        else:
            clean += 1

    print("bucket-A producers — predicted drain outcome (HEURISTIC)\n")
    print(f"  {'producers scanned':<44} {len(bucketA)}")
    print(f"  {'predicted DRAIN-NO-OP (float64-valued)':<44} {len(flagged)}"
          f"   [{sum(n for n, _ in flagged.values())} fields]")
    print(f"  {'no float64 origin found (drain may gain)':<44} {clean}")
    print(f"  {'producer file not found':<44} {missing}")

    if a.list and flagged:
        print("\n  predicted DRAIN-NO-OP — open these before spending a run:")
        for path, (n, hits) in sorted(flagged.items(), key=lambda kv: -kv[1][0]):
            print(f"    {n:>3}  {path}")
            for where, why in hits[:3]:
                print(f"           {where:<22} {why}")

    print("\n  This NARROWS which producers to open. It never settles one:")
    print("  confirm with assertion_drain_verify.py against a FRESH baseline.")
    return 0


def selftest() -> int:
    """Pin the predictor on the real worked case and on its opposite."""
    import tempfile
    ok = True

    # the confirmed DRAIN-NO-OP: an LP-solver result reaching an assertion
    src = ("w.add_assertion(name='a', computed=float(res.x_star[0]), "
           "expected=1.0)\n")
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(src); tmp = f.name
    hits = scan(pathlib.Path(tmp)); os.unlink(tmp)
    good = bool(hits)
    ok &= good
    print(f"  {'ok  ' if good else 'FAIL'}  solver-result value flagged   {hits}")

    # a genuine mpf value must NOT be flagged, or the audit is useless
    src2 = ("w.add_assertion(name='a', computed=float(abs(denom)), expected=1.0)\n")
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(src2); tmp2 = f.name
    hits2 = scan(pathlib.Path(tmp2)); os.unlink(tmp2)
    good = not hits2
    ok &= good
    print(f"  {'ok  ' if good else 'FAIL'}  plain mpf expression not flagged   {hits2}")

    # math.* downcasts an mpf silently — the bean records this for math.log
    src3 = ("x = math.log(q)\nw.add_assertion(name='a', computed=float(x), "
            "expected=1.0)\n")
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(src3); tmp3 = f.name
    hits3 = scan(pathlib.Path(tmp3)); os.unlink(tmp3)
    good = bool(hits3)
    ok &= good
    print(f"  {'ok  ' if good else 'FAIL'}  math.* downcast flagged via binding   {hits3}")

    print("\nselftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
