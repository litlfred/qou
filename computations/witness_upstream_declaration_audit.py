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
        if not isinstance(n, ast.Call) or not n.args:
            continue
        fname = (n.func.attr if isinstance(n.func, ast.Attribute)
                 else getattr(n.func, "id", ""))
        # `record_upstream(path, into)` is the module-level form, for the 290
        # producers that read their upstreams before a builder exists. It
        # declares just as much as the method does — the record simply lands in
        # a caller-owned list first.
        if fname in {"add_upstream", "record_upstream"}:
            for lit in _resolve(n.args[0], assigns):
                out.add(lit)
            # A non-literal argument means the module DOES declare upstreams,
            # just not resolvably. Recording the sentinel keeps it out of the
            # undeclared list: the honest answer is "cannot tell", and this
            # audit must not manufacture work.
            if not list(_resolve(n.args[0], assigns)):
                out.add(_DYNAMIC)
    return out


def declaration_reaches_witness(tree: ast.AST) -> tuple[str, int, tuple] | None:
    """Does a DECLARED upstream actually reach the witness?

    The audit above asks whether a producer declares its upstream at all. This
    asks the next question, and the answer is often no even when it declares:

      * ``ATTACHED_TOO_EARLY`` — ``add_upstream_records(_UPSTREAM_RECORDS)`` is
        called right after ``WitnessBuilder(...)``, which is the natural place
        and is wrong: the records are gathered LATER, by the loaders. It copies
        (``for r in records or []``) so it copies an empty list, and the
        upstreams appended afterwards never reach the builder. The comment on
        the offending line usually reads "declare upstreams read *before* this
        builder existed" — which describes the correct use while the placement
        contradicts it.
      * ``NEVER_ATTACHED`` — ``record_upstream`` populates a list that no
        ``add_upstream_records`` ever consumes.

    Both produce the same end state: the source declares, the witness carries
    no `data.upstream_witness_hashes`, and `witness_dependency_drift` cannot
    walk the edge. Measured cost of one instance:
    `averaged-block-swap-binding` sat 2.5 months at **65.6 %** wrong against
    the `binding_canonical` it names, while an assertion at tolerance 1e-9
    reported PASSED (bean `qou-nmza` / `qou-orb6`).

    THE FALSE POSITIVE TO AVOID, which halved the first count from 40 to 21:
    a helper that populates the list is not a "later populator" when it is the
    very function CONTAINING the ``add_upstream_records`` call. A module-level
    ``raise SystemExit(main())`` is trivially after every line inside ``main``,
    so without excluding the owner this flags every producer whose ``main``
    does both — including correct ones. `q_weighted_block_swap` was flagged
    that way and is fine.

    Validated 6/6 against witness ground truth: the four flagged carry no
    `upstream_witness_hashes`, the two controls do.
    """
    helper: dict[str, bool] = {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            helper[n.name] = any(
                isinstance(c, ast.Call)
                and (getattr(c.func, "id", None)
                     or getattr(c.func, "attr", None)) == "record_upstream"
                for c in ast.walk(n))

    rec, att = [], []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = getattr(n.func, "id", None) or getattr(n.func, "attr", None)
        if f == "record_upstream":
            rec.append(n.lineno)
        elif f == "add_upstream_records":
            att.append(n.lineno)

    if not rec and not att:
        return None
    if rec and not att:
        return ("NEVER_ATTACHED", min(rec), ())
    if not att:
        return None

    aur = min(att)
    owner = None
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            end = getattr(n, "end_lineno", n.lineno) or n.lineno
            if n.lineno <= aur <= end and (owner is None or n.lineno > owner[1]):
                owner = (n.name, n.lineno)

    later = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = getattr(n.func, "id", None)
        if not (f and helper.get(f)):
            continue
        if owner and f == owner[0]:          # not a populator of itself
            continue
        if getattr(n, "lineno", 0) > aur:
            later.append((n.lineno, f))
    if later:
        return ("ATTACHED_TOO_EARLY", aur, sorted(later)[0])
    return None


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
    # The module-level form, for producers that read before a builder exists.
    ("declared via record_upstream into a caller-owned list",
     '_UP = []\n'
     'y = record_upstream(HERE / "y-lambda-at-q0.witness.json", _UP)\n'
     'w = WitnessBuilder("mine").add_upstream_records(_UP)',
     []),
    ("record_upstream declares one, plain read leaves the other undeclared",
     '_UP = []\n'
     'a = record_upstream(HERE / "a.witness.json", _UP)\n'
     'b = json.loads((HERE / "b.witness.json").read_text())\n'
     'w = WitnessBuilder("mine").add_upstream_records(_UP)',
     ["b.witness.json"]),
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


# Cases for `declaration_reaches_witness`. The third is the one that matters:
# without the owner exclusion the first count was 40, of which 19 were this
# false positive — including a producer I had just verified as correct.
REACH_CASES = [
    ("attached before the loader populates the list",
     "def load():\n    return record_upstream(p, _U)\n"
     "def main():\n    b = WitnessBuilder('w')\n"
     "    b.add_upstream_records(_U)\n    x = load()\n",
     "ATTACHED_TOO_EARLY"),
    ("gathered but never handed to a builder",
     "def main():\n    r = record_upstream(p, _U)\n"
     "    b = WitnessBuilder('w')\n", "NEVER_ATTACHED"),
    # THE false positive: `main` both populates and attaches, in the right
    # order, and is then called from module level — trivially "after".
    ("the containing function is not a later populator of itself",
     "def main():\n    r = record_upstream(p, _U)\n"
     "    b = WitnessBuilder('w')\n    b.add_upstream_records(_U)\n"
     "raise SystemExit(main())\n", None),
    ("attached after the loader is called is correct",
     "def load():\n    return record_upstream(p, _U)\n"
     "def main():\n    x = load()\n    b = WitnessBuilder('w')\n"
     "    b.add_upstream_records(_U)\n", None),
    ("a module doing neither is silent",
     "def main():\n    return 0\n", None),
]


def self_test() -> int:
    fails = 0
    for label, src, want in REACH_CASES:
        got = declaration_reaches_witness(ast.parse(src))
        got_k = None if got is None else got[0]
        ok = got_k == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}\n"
              f"          want {want}, got {got_k}")
    for label, src, want in CASES:
        got = audit_source(src)
        got_u = None if got is None else got["undeclared"]
        ok = got_u == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}\n"
              f"          want {want}, got {got_u}")
    total = len(CASES) + len(REACH_CASES)
    print(f"\n{total - fails}/{total} passed")
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

    # The next question after "does it declare?": does the declaration REACH
    # the witness? Scanned over the same tree so both answers come from one run.
    broken = []
    for f in sorted(Path(a.root).resolve().rglob("*.py")):
        if {"_deprecated", "node_modules", ".lake", ".claude"} & set(f.parts):
            continue
        if f.name == "witness.py" and "qou_substrate" in f.parts:
            continue
        try:
            v = declaration_reaches_witness(ast.parse(f.read_text(encoding="utf-8")))
        except (SyntaxError, OSError):
            continue
        if v:
            broken.append((v[0], f, v[1], v[2]))
    if broken:
        n_early = sum(1 for k, *_ in broken if k == "ATTACHED_TOO_EARLY")
        n_never = len(broken) - n_early
        print(f"\n  declares, but the declaration CANNOT REACH the witness: "
              f"{len(broken):>3}")
        print(f"      ATTACHED_TOO_EARLY {n_early:>3}  (attached before the "
              f"loaders populate the list)")
        print(f"      NEVER_ATTACHED     {n_never:>3}  (gathered, never handed "
              f"to a builder)")
        print("      These declare in SOURCE and record nothing in the "
              "WITNESS, so the drift\n"
              "      detector cannot walk the edge — the same end state as "
              "not declaring at all.")
        for k, f, ln, l in sorted(broken, key=lambda r: (r[0], str(r[1]))):
            rel = f.relative_to(Path(a.root).resolve())
            extra = f"  (populated at {l[0]} by {l[1]}())" if l else ""
            print(f"        {k:20s} {rel}  @{ln}{extra}")

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
