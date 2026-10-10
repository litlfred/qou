#!/usr/bin/env python3
"""shadowed_import_arity_audit.py — find calls that would raise TypeError
because the name was imported from the WRONG one of two modules that both
define it.

WHY THIS EXISTS
===============

`qfac` is defined twice in this corpus, with different signatures:

    q_mpmath.qfac(n)                    # reads a module global for q
    hecke_characters.qfac(n, q=None)    # takes the anchor explicitly

Two producers imported the first and called the second:

    computations/delta_lambda_full_variance_phase5e_1.py:145
    computations/atomic_chirality_residue.py:159

Both raised `TypeError: qfac() takes 1 positional argument but 2 were given`
on the first statement that reached the call, so NEITHER COULD RUN AT ALL --
and both had a committed `.witness.json` on `main`, so nothing downstream
noticed.  Found 2026-09-07 while draining raw-float64 (bean `qou-kfeg`); the
cause is almost certainly the `qou-wee5` anchor-pinning sweep, which added
explicit `q` arguments to `dim_q` / `qfac` call sites corpus-wide and did not
check which `qfac` each file had imported.

WHAT IT CHECKS
==============

1. Which top-level names are defined by more than one importable module under
   `computations/`, with DIFFERENT signatures.  A name defined identically in
   two places cannot produce this failure and is not reported.
2. For each `.py` file, which of those names it imports and from where.
3. Whether any call to such a name passes an argument count the IMPORTED
   binding cannot accept.

It is deliberately narrow.  It does not attempt general arity checking (that is
a type checker's job) -- it answers only "did an author write the call for the
other module's function?", which is the failure that actually happened here and
which no existing gate catches: the file imports cleanly, the call is
syntactically fine, and the producer's own witness sits in the tree looking
current.

WHAT IT DOES NOT CATCH
======================

- A shadow where the two signatures happen to be arity-compatible but the
  SEMANTICS differ (e.g. one symmetric and one non-symmetric q-integer).  Both
  `qfac`s here agree numerically -- verified, ratio exactly 1.0 at n = 6, 9, 12
  -- so that case did not arise, but a future collision could be silently wrong
  rather than loudly broken.  Nothing here would see it.
- `import module` followed by `module.name(...)`, which is unambiguous and
  cannot be shadowed.
- A call reached through a variable, a `getattr`, or `**kwargs`.

Usage:
    python3 computations/audits/shadowed_import_arity_audit.py [--selftest]
"""
from __future__ import annotations

import ast
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
REPO = COMPUTATIONS.parent

# Directories whose *.py are importable by bare name from a producer, because
# `_path_bridge` puts them on `sys.path`.  Only these can shadow each other.
_IMPORT_ROOTS = (COMPUTATIONS, COMPUTATIONS / "substrate", COMPUTATIONS / "hecke")


def _arity_from_ast(node: ast.FunctionDef | ast.AsyncFunctionDef):
    """(min_positional, max_positional or None for *args), read from the source.

    Read from the AST rather than by importing the module and calling
    `inspect.signature`.  That is not a style preference: `importlib` runs the
    module body, and in `computations/` a module body is a PRODUCER -- the first
    version of this audit imported every candidate and set several probes
    running (they printed their own PASS tables into this script's output) and
    could have had them write witnesses into the tree.  An audit must not be
    able to mutate what it audits.
    """
    a = node.args
    pos = list(a.posonlyargs) + list(a.args)
    hi = len(pos)
    lo = hi - len(a.defaults)
    if a.vararg is not None:
        return (lo, None)
    return (lo, hi)


def _imported_names() -> set[str]:
    """Names that appear in some `from <module> import <name>`.

    A name nothing imports cannot be shadowed at a call site, so this is the
    second half of the noise filter.  Without it the table is dominated by
    `main` (130 modules, every producer's entry point) and by local helpers
    called `run`, `verdict`, `scan` -- all genuine name collisions, none of
    them capable of the failure being audited.
    """
    names: set[str] = set()
    for path in COMPUTATIONS.rglob("*.py"):
        if ("_deprecated" in path.parts or "fsh-guts" in path.parts):
            continue
        try:
            tree = ast.parse(path.read_text())
        except (SyntaxError, UnicodeDecodeError):
            continue
        for n in ast.walk(tree):
            if isinstance(n, ast.ImportFrom):
                names.update(a.name for a in n.names)
    return names


def _imported_stems() -> set[str]:
    """Module stems that some OTHER file imports by bare name.

    Restricting to these cuts the collision table from 181 names to a handful.
    Nearly every `computations/*.py` is a producer script, and two producers
    happening to define a local `verdict()` with different arities is not a
    shadow -- nothing imports either one, so neither can ever mask the other.
    Only a module something imports is capable of the failure this audits.
    """
    imported: set[str] = set()
    for path in COMPUTATIONS.rglob("*.py"):
        if ("_deprecated" in path.parts or "fsh-guts" in path.parts):
            continue
        try:
            tree = ast.parse(path.read_text())
        except (SyntaxError, UnicodeDecodeError):
            continue
        for n in ast.walk(tree):
            if isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
                imported.add(n.module.split(".")[0])
            elif isinstance(n, ast.Import):
                for a in n.names:
                    imported.add(a.name.split(".")[0])
    return imported


def _module_defs() -> dict[str, dict[str, tuple]]:
    """module stem -> {top-level function name: arity}, library modules only."""
    out: dict[str, dict[str, tuple]] = {}
    importable = _imported_stems()
    for d in _IMPORT_ROOTS:
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.py")):
            if f.name.startswith("_") or f.name == "setup.py":
                continue
            if f.stem not in importable:
                continue
            try:
                tree = ast.parse(f.read_text())
            except (SyntaxError, UnicodeDecodeError):
                continue
            defs = {}
            for n in tree.body:          # TOP LEVEL only — a nested def is not importable
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                        and not n.name.startswith("_"):
                    defs[n.name] = _arity_from_ast(n)
            if defs:
                out.setdefault(f.stem, {}).update(defs)
    return out


def collisions() -> dict[str, dict[str, tuple]]:
    """name -> {module: arity} for names defined in >1 module with DIFFERENT arity."""
    imported = _imported_names()
    seen: dict[str, dict[str, tuple]] = {}
    for mod, defs in _module_defs().items():
        for name, a in defs.items():
            if name in imported:
                seen.setdefault(name, {})[mod] = a
    return {k: v for k, v in seen.items()
            if len(v) > 1 and len(set(v.values())) > 1}


def audit(coll: dict[str, dict[str, tuple]]) -> list[dict]:
    findings = []
    for path in sorted(COMPUTATIONS.rglob("*.py")):
        if ("_deprecated" in path.parts or "fsh-guts" in path.parts):
            continue
        try:
            tree = ast.parse(path.read_text())
        except (SyntaxError, UnicodeDecodeError):
            continue
        # LOCAL name -> (ORIGINAL name, source module).  Keyed on the local name
        # because that is what the call site writes, but carrying the original
        # because `from m import foo as bar` makes the two differ and `coll` is
        # keyed by the original.  The first version stored only the module and
        # looked `coll` up by the local name, which raised KeyError on the first
        # aliased import it met.
        bound: dict[str, tuple[str, str]] = {}
        for n in ast.walk(tree):
            if isinstance(n, ast.ImportFrom) and n.module:
                for a in n.names:
                    if a.name in coll and n.module in coll[a.name]:
                        bound[a.asname or a.name] = (a.name, n.module)
        if not bound:
            continue
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            local = getattr(n.func, "id", None)
            if local not in bound:
                continue
            fname, src = bound[local]
            lo, hi = coll[fname][src]
            npos = len(n.args)
            if any(isinstance(a, ast.Starred) for a in n.args):
                continue
            if hi is not None and npos > hi:
                other = {m: a for m, a in coll[fname].items()
                         if m != src and (a[1] is None or a[1] >= npos)}
                findings.append({
                    "file": str(path.relative_to(REPO)),
                    "line": n.lineno,
                    "name": fname if local == fname else f"{fname} as {local}",
                    "imported_from": src,
                    "accepts": hi,
                    "called_with": npos,
                    "would_fit": sorted(other),
                })
    return findings


def _selftest() -> int:
    """The two known instances are FIXED, so a selftest cannot assert them.

    It asserts the two things that can still regress: that `_arity` reads the
    optional-parameter case correctly (the whole check turns on `q=None` making
    `hecke_characters.qfac` accept 2 while `q_mpmath.qfac` accepts 1), and that
    the collision finder still sees `qfac` as a live collision.  If someone
    unifies the two `qfac`s, this test fails loudly rather than the audit
    quietly reporting a clean tree because it lost its only subject.
    """
    ok = True

    cases = [("def f(n): ...", (1, 1)),
             ("def f(n, q=None): ...", (1, 2)),
             ("def f(n, *rest): ...", (1, None)),
             ("def f(n, /, q, *, kw=1): ...", (2, 2))]
    for src, want in cases:
        got = _arity_from_ast(ast.parse(src).body[0])
        if got != want:
            print(f"  FAIL _arity_from_ast({src!r}) = {got}, want {want}")
            ok = False

    coll = collisions()

    # A POSITIVE case, synthesised, because the two real ones are fixed and the
    # audit therefore reports a clean tree.  "Zero hits" is not evidence a
    # detector works -- this reconstructs the exact shape that broke two
    # producers and asserts it is still flagged.  (Checked once against the
    # real pre-fix sources at `8f7e7829218`: both were detected, at
    # atomic_chirality_residue.py:159 and
    # delta_lambda_full_variance_phase5e_1.py:145.)
    src = "from q_mpmath import qfac\nx = qfac(12, q)\n"
    tree = ast.parse(src)
    bound = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module:
            for a in n.names:
                if a.name in coll and n.module in coll[a.name]:
                    bound[a.asname or a.name] = (a.name, n.module)
    flagged = False
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and getattr(n.func, "id", None) in bound:
            fn, mod = bound[n.func.id]
            _lo, hi = coll[fn][mod]
            if hi is not None and len(n.args) > hi:
                flagged = True
    if not flagged:
        print("  FAIL: the known-bad shape `from q_mpmath import qfac; qfac(n, q)` "
              "is NOT flagged. The detector has lost its only positive.")
        ok = False
    else:
        print("  ok: known-bad shape flagged")

    if "qfac" not in coll:
        print("  FAIL: `qfac` is no longer seen as a colliding name. Either the "
              "two definitions were unified (good -- retire this selftest and "
              "say so) or module discovery broke (bad).")
        ok = False
    else:
        print(f"  ok: qfac collision live -- {coll['qfac']}")
    print("  selftest PASS" if ok else "  selftest FAIL")
    return 0 if ok else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return _selftest()
    coll = collisions()
    print(f"colliding names (defined in >1 module, different arity): {len(coll)}")
    for name, mods in sorted(coll.items()):
        print(f"  {name}: " + ", ".join(f"{m}{a}" for m, a in sorted(mods.items())))
    findings = audit(coll)
    print(f"\nfiles calling a shadowed binding with the WRONG arity: {len(findings)}")
    for f in findings:
        print(f"  {f['file']}:{f['line']}  {f['name']}() imported from "
              f"{f['imported_from']} accepts {f['accepts']} positional, "
              f"called with {f['called_with']}"
              + (f" -- fits {f['would_fit']}" if f["would_fit"] else ""))
    if findings:
        print("\nThese raise TypeError at runtime. Import the binding that fits.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
