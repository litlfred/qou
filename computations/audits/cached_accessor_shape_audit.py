#!/usr/bin/env python3
# polynomial_q_not_applicable: validator, not a q-series compute.
"""Find accessors with the "matches the package constant => serve the cache" shape.

WHY. AGENTS.md §"q0 anchor convention" closes its layer-straddle rule with a
general instruction: *"Audit any other cached-witness accessor with the same
'matches the package constant => serve the cache' shape."* The named instance,
`wedderburn_jones_markov.y_lambda_at`, no longer has it -- the cache path moved
into `_y_lambda_at_convention_C_HISTORICAL` when convention C was excised on
2026-08-09 (bean qou-vu19). The general instruction still stands, and nobody had
measured it.

THE SHAPE is: a function that returns PRECOMPUTED data when the caller's q
happens to match the value the cache was built at. It is dangerous because the
gate is satisfied TRIVIALLY when the caller passes the package constant itself,
so an ideal-layer cache reaches an experimental-layer caller with no signal that
a boundary was crossed. Measured cost of one instance: 11.54 ppb, the mu-p
tension itself, in the mu_3 Frechet probe.

HOW IT IS DETECTED, and why not by name. Two earlier versions of this detector
returned 0 and BOTH were wrong:

  v1  required a tolerance literal and a ".witness.json" string in the same
      function. 1 hit, and it was the INVERSE shape -- cross_check_trM_1ppb
      reads the pin and RAISES if the runtime constant disagrees. A guard.

  v2  keyed the `if` test on a list of q-constant names (Q, Q_MP,
      Q_50_DIGIT_STR, ...). It missed the known positive, because that one
      compares against `_Y_LAMBDA_AT_Q0_WITNESS_Q0` -- a module-private name no
      list would have guessed. Keying on how a thing is SPELLED is the failure
      mode the convention-C detector-blindness taxonomy catalogues; this is
      another entry in it.

v3 keys on PROVENANCE instead. A name is cache-derived if it is assigned from a
file/JSON read -- at module level, or inside a function that declares it
`global` and performs such a read. Then the shape is: an `if` whose test
mentions a cache-derived name, whose body returns. No name list, so a producer
cannot evade it by choosing a different identifier.

The known positive is asserted, not hoped for: --selftest fails if
`_y_lambda_at_convention_C_HISTORICAL` is not among the hits.

Usage:
    python3 cached_accessor_shape_audit.py
    python3 cached_accessor_shape_audit.py --selftest
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SKIP = (".git", ".claude", "_deprecated", "node_modules", "__pycache__")
LOAD_CALLS = {"load", "loads", "read_text", "read_bytes", "open",
              "record_upstream", "witness_path"}
KNOWN_POSITIVE = "_y_lambda_at_convention_C_HISTORICAL"


def _names(node: ast.AST) -> set[str]:
    out: set[str] = set()
    for x in ast.walk(node):
        if isinstance(x, ast.Name):
            out.add(x.id)
        elif isinstance(x, ast.Attribute):
            out.add(x.attr)
    return out


def _performs_load(node: ast.AST) -> bool:
    for x in ast.walk(node):
        if isinstance(x, ast.Call):
            f = x.func
            nm = (f.id if isinstance(f, ast.Name)
                  else f.attr if isinstance(f, ast.Attribute) else None)
            if nm in LOAD_CALLS:
                return True
        if isinstance(x, ast.Constant) and isinstance(x.value, str) \
                and x.value.endswith(".witness.json") \
                and not x.value.startswith(("-", ".", "*")):
            # A leading "-" or "." means this is a SUFFIX pattern, not a path.
            # Without this guard, `AUDIT_SUFFIXES = ("-audit.witness.json", …)`
            # reads as cache-derived, and every `if name.endswith(suf)` gate
            # over it looks like the shape. That was 2 of 4 hits.
            return True
    return False


def cache_derived_names(tree: ast.Module) -> set[str]:
    """Names whose value traces to a file/JSON read.

    Two bindings, and the second is the one a name-list misses: a module-level
    cache is typically DECLARED at module scope (often `= None`) and ASSIGNED
    inside a loader that declares it `global`.
    """
    out: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Assign) and _performs_load(node.value):
            out |= {t.id for t in node.targets if isinstance(t, ast.Name)}
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not _performs_load(fn):
            continue
        globals_here: set[str] = set()
        for x in ast.walk(fn):
            if isinstance(x, ast.Global):
                globals_here |= set(x.names)
        if not globals_here:
            continue
        for x in ast.walk(fn):
            if isinstance(x, ast.Assign):
                out |= {t.id for t in x.targets
                        if isinstance(t, ast.Name) and t.id in globals_here}
    return out


def scan() -> list[tuple[str, str, int, list[str]]]:
    hits: list[tuple[str, str, int, list[str]]] = []
    for p in sorted(REPO.rglob("*.py")):
        if any(x in p.parts for x in SKIP):
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        derived = cache_derived_names(tree)
        if not derived:
            continue
        for fn in ast.walk(tree):
            if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for node in ast.walk(fn):
                if not isinstance(node, ast.If):
                    continue
                touched = _names(node.test) & derived
                if not touched:
                    continue
                # The gate must involve a CALLER ARGUMENT. Without this the
                # scan returns 34, and the great majority are plain
                # memoisation -- `if _CACHE is not None: return _CACHE` -- or
                # an existence check, `if PATH.exists(): return load(PATH)`.
                # Those are benign: they hand back the same data whoever asks,
                # with no claim that it matches the caller's q. What makes the
                # shape dangerous is precisely that the cache is served ON THE
                # STRENGTH OF A COMPARISON against something the caller passed,
                # so a caller passing the package constant satisfies it
                # trivially. The known positive tests
                # `abs(float(q_val) - _Y_LAMBDA_AT_Q0_WITNESS_Q0) < tol`,
                # where `q_val` is a parameter.
                params = {a.arg for a in fn.args.args} | \
                         {a.arg for a in fn.args.kwonlyargs}
                if fn.args.vararg:
                    params.add(fn.args.vararg.arg)
                if fn.args.kwarg:
                    params.add(fn.args.kwarg.arg)
                gated_on_arg = _names(node.test) & params
                if not gated_on_arg:
                    continue
                body = ast.Module(body=node.body, type_ignores=[])
                if any(isinstance(r, ast.Return) and r.value is not None
                       for r in ast.walk(body)):
                    hits.append((str(p.relative_to(REPO)), fn.name,
                                 node.lineno,
                                 sorted(touched) + [f"arg:{a}" for a in sorted(gated_on_arg)]))
    return hits


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true",
                    help="fail unless the known positive is detected")
    args = ap.parse_args(argv)

    hits = scan()
    if args.selftest:
        found = [h for h in hits if h[1] == KNOWN_POSITIVE]
        if not found:
            print(f"SELFTEST FAIL: {KNOWN_POSITIVE} not detected — a scan that "
                  "cannot find the known positive is measuring itself.")
            return 1
        print(f"SELFTEST PASS: known positive detected at {found[0][0]}:"
              f"{found[0][2]} via {found[0][3]}")
        return 0

    print("=" * 72)
    print('accessors with the "q matches the cache\'s q => serve the cache" shape')
    print("=" * 72)
    for path, fn, line, via in hits:
        print(f"  {path}::{fn}  (if at line {line})")
        print(f"      gated on cache-derived name(s): {via}")
    print(f"\n  total: {len(hits)}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
