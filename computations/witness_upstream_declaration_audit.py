#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit, emits no numeric physics.
"""Which producers read an upstream witness without declaring it?

Owner directive: NO FLOAT64 — this is the *staleness* half of the same
discipline. A number computed from a witness that has since moved is wrong in
a way no precision audit can see.

## The defect

`witness_dependency_drift.py` walks `data.upstream_witness_hashes`, which
`WitnessBuilder.add_upstream(path)` populates. A producer that reads its
upstream with a plain `json.load` records nothing, so the edge does not exist
as far as the detector is concerned:

```python
per_block = builder.add_upstream(upstream_path)     # declared   — visible
y_data    = json.load(open(_pb.witness_path("y-lambda-at-q0.witness.json")))
                                                    # undeclared — invisible
```

That is not hypothetical. `qbeta-per-block-paper-closed-forms.witness.json`
moved at the 8th digit on regeneration *before any source change*: its upstream
`y-lambda-at-q0.witness.json` had moved and nothing re-ran it. The gate was
green throughout.

This audit finds the same shape everywhere else. It is deliberately a
*reporting* tool and not a fixer: `add_upstream` changes witness content (it
records the upstream's hash), so adopting it is a regeneration wave, not an
edit — see the caveat under `--list`.

## What counts

A **producer** is a module that builds a witness: it constructs a
`WitnessBuilder`, calls `WitnessBuilder.wrap_legacy`, or stamps metadata with
`stamp_staleness_metadata`.

An **undeclared upstream** is a `*.witness.json` filename that provably reaches
a *read* sink in that module and is not among the filenames passed to
`add_upstream`. Sinks are asymmetric, exactly inverted from
`witness_provenance_audit`: `read_text` / `json.load(open(p))` / a bare
`open(p)` count as reads; `write_text` and `open(p, "w")` do not.

Path resolution is shared with `witness_provenance_audit` rather than
reimplemented, so both tools understand the same idioms (`Path(x)`, `HERE / x`,
`os.path.join`, `p.with_name`, `_pb.witness_path`, and values reached through
a variable). A filename this resolver cannot follow is simply not reported —
the count is a **floor**, never an accusation of completeness.

Usage:
    python3 computations/witness_upstream_declaration_audit.py
    python3 computations/witness_upstream_declaration_audit.py --list
    python3 computations/witness_upstream_declaration_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from witness_provenance_audit import (  # noqa: E402
    _DYNAMIC, _assignments, _is_write_mode, _resolve, written_filenames,
)

_READ_METHODS = {"read_text", "read_bytes"}


def _is_producer(tree: ast.AST) -> bool:
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if getattr(f, "id", "") == "WitnessBuilder":
            return True
        if isinstance(f, ast.Attribute) and f.attr in {
            "wrap_legacy", "stamp_staleness_metadata"
        }:
            return True
    return False


def _collect(node, assigns: dict, out: set) -> None:
    for lit in _resolve(node, assigns):
        if ".witness.json" in lit and not lit.startswith(_DYNAMIC):
            out.add(lit)


def read_filenames(tree: ast.AST) -> set:
    """Witness filenames that provably reach a READ in this module.

    The mirror image of `witness_provenance_audit.written_filenames`. A
    filename that reaches only a write is not an upstream — that is the module
    producing its own output, not consuming someone else's.
    """
    assigns = _assignments(tree)
    out: set = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if isinstance(f, ast.Attribute) and f.attr in _READ_METHODS:
            _collect(f.value, assigns, out)              # p.read_text()
        elif isinstance(f, ast.Attribute) and f.attr == "open":
            if not _is_write_mode(n):
                _collect(f.value, assigns, out)          # p.open()
        elif getattr(f, "id", "") == "open" and n.args:
            if not _is_write_mode(n, mode_index=1):
                _collect(n.args[0], assigns, out)        # open(p) / open(p,"r")
        elif isinstance(f, ast.Attribute) and f.attr in {"load", "loads"}:
            for a in n.args[:1]:
                _collect(a, assigns, out)                # json.load(p) — rare
    return out


def declared_upstreams(tree: ast.AST) -> set:
    """Filenames passed to `add_upstream`, however they are spelled."""
    assigns = _assignments(tree)
    out: set = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr == "add_upstream" and n.args:
            for lit in _resolve(n.args[0], assigns):
                out.add(lit)
            # A non-literal argument means the module DOES declare upstreams,
            # just not resolvably. Recording the sentinel keeps it out of the
            # undeclared list: the honest answer is "cannot tell", and this
            # audit must not manufacture work.
            if not list(_resolve(n.args[0], assigns)):
                out.add(_DYNAMIC)
    return out


def audit_source(source: str) -> dict | None:
    """None when the module is not a producer; otherwise its upstream state."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    if not _is_producer(tree):
        return None
    declared = declared_upstreams(tree)
    # A file this module also WRITES is its own output, not an upstream. The
    # incremental-cache producers (`per_irrep_pole_atom`, the chi caches) read
    # a partial result, extend it, and write it back; counting that as an
    # undeclared dependency would be pure noise — and it was, at 3x the true
    # figure, before this line existed.
    reads = read_filenames(tree) - written_filenames(tree)
    if _DYNAMIC in declared:
        return {"declared": sorted(declared - {_DYNAMIC}),
                "undeclared": [], "opaque": True}
    return {"declared": sorted(declared),
            "undeclared": sorted(reads - declared), "opaque": False}


def scan(root: Path) -> list[dict]:
    out: list[dict] = []
    for p in sorted((root / "computations").rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if ".witness.json" not in src:
            continue
        r = audit_source(src)
        if r is None:
            continue
        r["file"] = p.relative_to(root).as_posix()
        out.append(r)
    return out


CASES = [
    ("plain read, no add_upstream — invisible to the drift detector",
     'WitnessBuilder("mine")\n'
     'y = json.loads((HERE / "y-lambda-at-q0.witness.json").read_text())',
     ["y-lambda-at-q0.witness.json"]),
    ("declared via add_upstream",
     'b = WitnessBuilder("mine")\n'
     'y = b.add_upstream(HERE / "y-lambda-at-q0.witness.json")',
     []),
    ("one declared, one not — the per-block shape exactly",
     'b = WitnessBuilder("mine")\n'
     'p = b.add_upstream(HERE / "q-pinning-50-digit.witness.json")\n'
     'y = json.loads((HERE / "y-lambda-at-q0.witness.json").read_text())',
     ["y-lambda-at-q0.witness.json"]),
    ("its own OUTPUT is not an upstream",
     'WitnessBuilder("mine")\n'
     'out = HERE / "mine.witness.json"\nout.write_text(j)',
     []),
    # The incremental-cache shape: read your own partial result, extend it,
    # write it back. Not an upstream, and the single largest false positive.
    ("reads AND writes the same file — its own cache, not an upstream",
     'WitnessBuilder("mine")\n'
     'cache = HERE / "chi-proton-h3.witness.json"\n'
     'if cache.exists():\n    d = json.loads(cache.read_text())\n'
     'cache.write_text(json.dumps(d))',
     []),
    ("read via _pb.witness_path",
     'WitnessBuilder("mine")\n'
     'd = json.loads(_pb.witness_path("up.witness.json", HERE).read_text())',
     ["up.witness.json"]),
    ("read via open(p) with no mode",
     'WitnessBuilder("mine")\n'
     'd = json.load(open(HERE / "up.witness.json"))',
     ["up.witness.json"]),
    ("open(p, 'w') is a write, not an upstream",
     'WitnessBuilder("mine")\n'
     'f = open(HERE / "mine.witness.json", "w")',
     []),
    ("add_upstream with a computed path: opaque, never accused",
     'b = WitnessBuilder("mine")\n'
     'for nm in names:\n    b.add_upstream(HERE / nm)\n'
     'y = json.loads((HERE / "y.witness.json").read_text())',
     []),
    ("not a producer at all — out of scope",
     'y = json.loads((HERE / "y-lambda-at-q0.witness.json").read_text())',
     None),
    ("hand-rolled producer via stamp_staleness_metadata",
     'WitnessBuilder.stamp_staleness_metadata(w, script_path=__file__)\n'
     'y = json.loads((HERE / "up.witness.json").read_text())',
     ["up.witness.json"]),
]


def self_test() -> int:
    fails = 0
    for label, src, want in CASES:
        got = audit_source(src)
        got_u = None if got is None else got["undeclared"]
        ok = got_u == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}\n"
              f"          want {want}, got {got_u}")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--list", action="store_true",
                    help="list every producer with an undeclared upstream")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    rows = scan(Path(a.root).resolve())
    undecl = [r for r in rows if r["undeclared"]]
    declared_only = [r for r in rows if not r["undeclared"] and r["declared"]]
    opaque = [r for r in rows if r["opaque"]]
    edges = sum(len(r["undeclared"]) for r in undecl)

    print("witness-upstream-declaration: producers that consume a witness\n")
    print(f"  undeclared (invisible to drift) : {len(undecl):>4}"
          f"   ({edges} edges)")
    print(f"  fully declared via add_upstream : {len(declared_only):>4}")
    print(f"  declares, but via a computed path: {len(opaque):>4}"
          f"   (not counted either way)")

    if a.list:
        print("\n--- undeclared upstream edges ---")
        for r in undecl:
            print(f"  {r['file']}")
            for u in r["undeclared"]:
                print(f"      reads {u}")
        print("\nAdopting add_upstream REWRITES the witness (it records the "
              "upstream hash),\nso each of these is a re-run, not an edit. Port "
              "in batches you can regenerate\nand verify, never in one sweep.")
    else:
        print("\n  --list for the per-producer detail.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
