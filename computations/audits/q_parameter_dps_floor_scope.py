#!/usr/bin/env python3
# polynomial_q_not_applicable: source-hygiene audit, no q-dependence.
"""Scope the blast radius of hoisting the 50-dps floor out of `q_parameter`'s
muon branch (bean `qou-zbws`).  MEASUREMENT ONLY — it lands no change.

WHAT IS BEING MEASURED
----------------------
`computations/substrate/q_parameter.py` sets

    _mp.mp.dps = max(_mp.mp.dps, 50)

at 8-space indent, i.e. INSIDE `if _anchor in ("ideal", "muon", "canonical")`.
On any other anchor that line never runs, and `qou_substrate/constants.py`
builds its `_MP` family inside `with _mp.workdps(_DPS_DEFAULT)`, which RESTORES
the ambient precision on exit.  So on the default (proton) anchor the cached
constants are genuine 50-digit mpf objects but every subsequent operation on
them runs at mpmath's default 15 dps.

Measured on this checkout (all three reproduce the bean's figures):

    QOU_Q0_ANCHOR unset   -> mp.dps == 15 after `import q_parameter`
    QOU_Q0_ANCHOR=proton  -> mp.dps == 15
    QOU_Q0_ANCHOR=muon    -> mp.dps == 50

    1/Q_MP @ ambient 15 : 0.9009182839557414723685724311508238315582
    1/Q_MP @ ambient 50 : 0.9009182839557414921608228824810939360147
                     |d| = 1.97923e-17     (float64 epsilon, same anchor)

Hoisting the floor is one line and renumbers every proton-anchor producer that
does not set its own precision.  This audit counts exactly which those are, so
the owner has the blast radius before deciding.  IT IS NOT A GATE and has no
baseline: it answers a one-off sequencing question.

WHY AST AND NOT `grep -rl`
--------------------------
Bare-name imports (`from q_parameter import Q`) are made resolvable by
`computations/_path_bridge`, which puts every cluster subdirectory of
`computations/` on `sys.path`.  A textual grep cannot follow that, cannot see
`import q_parameter as qp` followed by attribute access, and cannot compute the
TRANSITIVE cone — a producer that imports a helper that imports `q_parameter`
inherits the ambient precision just the same.

Measured here, and the grep is wrong in BOTH directions:

    grep -rlE '^\s*(from|import)\s+q_parameter(\.|\s|$)' --include=*.py .
        -> 1382       (excluding qou-mass/ and _deprecated/)
    this resolver
        -> 1403 direct importers

  * 3 of the grep's hits are `from q_parameter import Q` inside a DOCSTRING —
    `_path_bridge.py`, `q_mpmath.py`, `qou_mass_canonical_wiring_example.py`.
    None of them imports anything.
  * 24 real importers spell it `from substrate.q_parameter import …` (e.g.
    `computations/deltalambda/branching_tower.py:49`), which the anchored
    pattern cannot match.

Net −21, and neither error is visible from the count alone.

WHAT THIS RESOLVER CAN MISS (stated so the numbers are not read as exact)
------------------------------------------------------------------------
  * dynamic imports — `importlib.import_module(name)`, `__import__`, `exec`.
  * `.sage` producers: not Python-parseable, excluded entirely.
  * a bare-name import that collides across cluster dirs resolves here to
    EVERY candidate (over-approximating the cone) rather than to the single
    file `sys.path` order would pick.  Measured on this checkout: 10 colliding
    basenames over 33 files, and exactly 2 module names ever resolve to more
    than one file, so the inflation is negligible.
  * precision raised by a called helper rather than in the file itself — a
    module that assigns `mp.dps` at import IS followed (it is an edge in the
    cone), but a helper that raises dps inside a function the producer calls
    is not.  Such a producer is counted as "moves" and may not.
  * `setattr(mp.mp, "dps", 50)` and other reflective spellings.
  * subprocess invocation of another producer.

Usage:
    python3 computations/audits/q_parameter_dps_floor_scope.py
    python3 computations/audits/q_parameter_dps_floor_scope.py --json
    python3 computations/audits/q_parameter_dps_floor_scope.py --list moves_own_mp
    python3 computations/audits/q_parameter_dps_floor_scope.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent

SKIP_PARTS = {"__pycache__", "_deprecated", ".git", "node_modules",
              ".venv", "venv", ".lake", ".work", ".cache", "qou-mass"}

# Precision raisers.  `set_compute_dps` / `.dps` / `workdps` match
# computations/never_raises_dps_audit.py so the two audits agree on who is
# already protected; `extradps`/`workprec`/`extraprec` are the remaining
# mpmath context managers that raise working precision.
RAISERS = {"set_compute_dps", "workdps", "extradps", "extraprec", "workprec"}

# Calls that CONSTRUCT an mpmath value (copied from never_raises_dps_audit.py
# so "does mp arithmetic" means the same thing in both).
MP_VALUE_FUNCS = {
    "mpf", "mpmathify", "sqrt", "exp", "log", "log10", "pi", "power",
    "cos", "sin", "tan", "atan", "asin", "acos", "gamma", "zeta",
    "polylog", "hyper", "besselj", "erf", "mpc", "matrix", "mpmathify",
}


# ── file universe ────────────────────────────────────────────────────
def py_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.py")
                  if not (set(p.relative_to(ROOT).parts) & SKIP_PARTS))


def bare_roots() -> list[Path]:
    """Directories `_path_bridge` puts on sys.path for bare-name imports."""
    roots = [COMP]
    for child in sorted(COMP.iterdir()):
        if (child.is_dir() and not child.name.startswith(("_", "."))
                and (child / "__init__.py").is_file()):
            roots.append(child)
    return roots


def pkg_roots() -> list[Path]:
    return [ROOT / "tools" / "qou-substrate" / "python",
            ROOT / "tools" / "pyhecke" / "python",
            ROOT]


_UNIVERSE: set[Path] = set()


# ── import extraction ────────────────────────────────────────────────
def imported_modules(tree: ast.Module, path: Path) -> set[str]:
    """Every module name this file imports, at ANY nesting depth.

    `import a.b.c`      -> {"a", "a.b", "a.b.c"}   (a prefix package that
                            re-exports the target is still an edge)
    `from a.b import c` -> {"a", "a.b", "a.b.c"}   (c may be a submodule)
    `import x as y`     -> {"x"}                   (the alias is irrelevant:
                            the MODULE is what executes)
    Relative imports are tagged and resolved against the file's directory.
    """
    mods: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                for i in range(1, len(parts) + 1):
                    mods.add(".".join(parts[:i]))
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                mods.add(f"__rel{node.level}:{base}")
                for alias in node.names:
                    mods.add(f"__rel{node.level}:"
                             + (f"{base}.{alias.name}" if base else alias.name))
                continue
            if base:
                parts = base.split(".")
                for i in range(1, len(parts) + 1):
                    mods.add(".".join(parts[:i]))
                for alias in node.names:
                    mods.add(f"{base}.{alias.name}")
    return mods


def resolve(mod: str, path: Path, bares: list[Path],
            pkgs: list[Path]) -> list[Path]:
    """Every file in the universe that `mod` could name from `path`."""
    hits: list[Path] = []
    if mod.startswith("__rel"):
        level_s, _, rest = mod.partition(":")
        level = int(level_s[len("__rel"):])
        base = path.parent
        for _ in range(level - 1):
            base = base.parent
        roots = [base]
        parts = rest.split(".") if rest else []
    else:
        roots = pkgs + [path.parent] + bares
        parts = mod.split(".")
    if not parts:
        return []
    for r in roots:
        sub = r.joinpath(*parts)
        for c in (sub.with_suffix(".py"), sub / "__init__.py"):
            if c.is_file():
                hits.append(c.resolve())
    return [h for h in dict.fromkeys(hits) if h in _UNIVERSE]


# ── precision predicates ─────────────────────────────────────────────
def _is_prec_target(t: ast.expr) -> bool:
    return isinstance(t, ast.Attribute) and t.attr in {"dps", "prec"}


def raise_sites(tree: ast.AST) -> list[int]:
    """Lines where working precision is set/raised, at any nesting depth."""
    out: list[int] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            name = (f.attr if isinstance(f, ast.Attribute)
                    else f.id if isinstance(f, ast.Name) else None)
            if name in RAISERS:
                out.append(node.lineno)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                if _is_prec_target(t):
                    out.append(node.lineno)
        elif isinstance(node, ast.AnnAssign):
            if _is_prec_target(node.target):
                out.append(node.lineno)
    return sorted(set(out))


def raise_values(tree: ast.AST) -> list[int]:
    """Literal precisions this file sets, where they are literals."""
    vals: list[int] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if (isinstance(t, ast.Attribute) and t.attr == "dps"
                        and isinstance(node.value, ast.Constant)
                        and isinstance(node.value.value, int)):
                    vals.append(node.value.value)
        elif isinstance(node, ast.Call):
            f = node.func
            nm = (f.attr if isinstance(f, ast.Attribute)
                  else f.id if isinstance(f, ast.Name) else None)
            if nm in RAISERS and node.args:
                a0 = node.args[0]
                if isinstance(a0, ast.Constant) and isinstance(a0.value, int):
                    vals.append(a0.value)
    return sorted(set(vals))


def module_scope_raise_lines(tree: ast.Module) -> list[int]:
    out: list[int] = []
    for stmt in tree.body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        out.extend(raise_sites(stmt))
    return sorted(set(out))


def mp_value_lines(tree: ast.Module) -> list[int]:
    out: list[int] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        if (isinstance(f, ast.Attribute) and f.attr in MP_VALUE_FUNCS
                and isinstance(f.value, ast.Name) and f.value.id in {"mp", "mpmath"}):
            out.append(node.lineno)
        elif isinstance(f, ast.Name) and f.id in {"mpf", "mpmathify"}:
            out.append(node.lineno)
    return sorted(set(out))


def imports_mp_family(tree: ast.Module) -> bool:
    """Does the file pull an mpf-valued substrate name (`Q_MP`, `q_at`, …)?

    A producer can be moved by the floor without ever writing `mp.` itself, by
    importing the `_MP` family and doing plain `*` / `/` on it.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for a in node.names:
                if a.name.endswith("_MP") or a.name in {
                        "q_at", "q_str", "q_int_mp", "q_muon_at",
                        "vol_4_1_at", "q_muon_frozen_at", "Q_50_DIGIT_STR"}:
                    return True
    return False


def first_import_line(tree: ast.Module, names: set[str]) -> int | None:
    best = None
    for node in ast.walk(tree):
        hit = False
        if isinstance(node, ast.Import):
            hit = any(a.name in names or a.name.split(".")[0] in names
                      for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            hit = (node.module in names or node.module.split(".")[0] in names)
        if hit:
            best = node.lineno if best is None else min(best, node.lineno)
    return best


def emits_witness(src: str) -> bool:
    return "WitnessBuilder" in src or ".witness.json" in src


def is_runnable(tree: ast.Module) -> bool:
    for node in tree.body:
        if isinstance(node, ast.If):
            d = ast.dump(node.test)
            if "__name__" in d and "__main__" in d:
                return True
    return False


# ── scan ─────────────────────────────────────────────────────────────
def scan() -> dict:
    files = py_files()
    _UNIVERSE.update(f.resolve() for f in files)
    bares, pkgs = bare_roots(), pkg_roots()

    parsed: dict[Path, ast.Module] = {}
    srcs: dict[Path, str] = {}
    broken: list[dict] = []
    for p in files:
        try:
            src = p.read_text(encoding="utf-8")
            parsed[p.resolve()] = ast.parse(src)
            srcs[p.resolve()] = src
        except SyntaxError as exc:
            broken.append({"file": str(p.relative_to(ROOT)),
                           "kind": "syntax-error", "detail": str(exc)[:100]})
        except Exception as exc:  # noqa: BLE001
            broken.append({"file": str(p.relative_to(ROOT)),
                           "kind": "unreadable", "detail": str(exc)[:100]})

    fwd: dict[Path, set[Path]] = {}
    rev: dict[Path, set[Path]] = {}
    for p, tree in parsed.items():
        tgts = {h for m in imported_modules(tree, p)
                for h in resolve(m, p, bares, pkgs) if h != p}
        fwd[p] = tgts
        for t in tgts:
            rev.setdefault(t, set()).add(p)

    def close(seed: Path, graph) -> set[Path]:
        seen, dq = {seed}, deque([seed])
        while dq:
            for nxt in graph.get(dq.popleft(), ()):
                if nxt not in seen:
                    seen.add(nxt)
                    dq.append(nxt)
        seen.discard(seed)
        return seen

    qp = (COMP / "substrate" / "q_parameter.py").resolve()
    const = (ROOT / "tools" / "qou-substrate" / "python" / "qou_substrate"
             / "constants.py").resolve()
    cone_qp = close(qp, rev)
    cone_const = close(const, rev)
    direct_qp = rev.get(qp, set())

    manifest = json.loads((COMP / "q0_anchor_manifest.json").read_text())
    muon_stems = set(manifest.get("ideal_muon", []))
    proton_stems = set(manifest.get("physical_proton", []))
    amb_stems = set(manifest.get("ambiguous", []))

    # Does any file in p's forward cone build mpmath values — EXCLUDING the
    # substrate/serialisation infrastructure every witness producer imports?
    #
    # Without the exclusion this test is vacuously true for the whole corpus:
    # `qou_substrate/witness.py:190` builds `_mp.mpf(v)` inside the witness
    # serialiser and `constants.py` builds the whole `_MP` family, so "some
    # file in my import cone touches mpf" says nothing about whether the
    # PRODUCER's own arithmetic runs at the ambient precision.  `pyhecke` is
    # deliberately NOT excluded: a producer that calls its Hecke/Gram/Markov
    # kernels at ambient 15 dps really does move.
    def _is_infra(p: Path) -> bool:
        s = str(p)
        if "/tools/qou-substrate/" in s:
            return True
        return p.name in {"q_parameter.py", "_precision.py", "witness_base.py",
                          "_path_bridge.py", "q_mpmath.py"}

    _fc_cache: dict[Path, bool] = {}

    def cone_builds_mp(p: Path) -> bool:
        if p in _fc_cache:
            return _fc_cache[p]
        _fc_cache[p] = False           # cycle guard
        res = False
        for t in close(p, fwd):
            if t in parsed and not _is_infra(t) and mp_value_lines(parsed[t]):
                res = True
                break
        _fc_cache[p] = res
        return res

    def row(p: Path) -> dict:
        tree, src = parsed[p], srcs[p]
        rl = raise_sites(tree)
        own_mp = bool(mp_value_lines(tree)) or imports_mp_family(tree)
        r = {
            "file": str(p.relative_to(ROOT)),
            "stem": p.stem,
            "producer": emits_witness(src) and is_runnable(tree),
            "raises_dps": bool(rl),
            "raise_values": raise_values(tree),
            "module_scope_raise": module_scope_raise_lines(tree)[:1],
            "qp_import_line": first_import_line(
                tree, {"q_parameter", "qou_substrate"}),
            "muon_manifest": p.stem in muon_stems,
            "proton_manifest": p.stem in proton_stems,
            "ambiguous_manifest": p.stem in amb_stems,
            "own_mp": own_mp,
            "direct": p in direct_qp,
        }
        if r["producer"] and not r["raises_dps"] and not r["muon_manifest"]:
            r["bucket"] = ("moves_own_mp" if own_mp else
                           "moves_via_helper" if cone_builds_mp(p) else "no_mp")
        elif r["producer"] and r["raises_dps"]:
            r["bucket"] = "raises"
        elif r["producer"]:
            r["bucket"] = "muon_already_50"
        else:
            r["bucket"] = "not_a_producer"
        return r

    return {
        "files_scanned": len(files),
        "parsed": len(parsed),
        "broken": broken,
        "direct_importers_q_parameter": len(direct_qp),
        "cone_q_parameter": [row(p) for p in sorted(cone_qp)],
        "cone_constants_only": [row(p) for p in sorted(cone_const - cone_qp - {qp})],
    }


# ── witness attribution ──────────────────────────────────────────────
def witnesses_for(res: dict) -> dict:
    """Committed witnesses under `computations/`, bucketed by their producer.

    Attribution widens `gen_q0_anchor_manifest._producer_stem` (which looks
    only beside the witness and at `computations/`) with two more passes,
    because that lookup leaves ~46 % of the corpus unattributed:

      1. beside the witness, then `computations/`  (the manifest's own rule)
      2. a UNIQUE `<stem>.py` anywhere under `computations/`
      3. any producer whose SOURCE names the witness file literally

    Pass 3 is what catches a producer emitting a witness under a different
    stem from its own filename; it is applied last so 1-2 keep priority.
    """
    rows = res["cone_q_parameter"] + res["cone_constants_only"]
    by_file = {r["file"]: r for r in rows}

    stem_index: dict[str, list[Path]] = {}
    for p in COMP.rglob("*.py"):
        if set(p.relative_to(ROOT).parts) & SKIP_PARTS:
            continue
        stem_index.setdefault(p.stem, []).append(p)

    # literal witness-name mentions, producer source -> witness basenames
    literal: dict[str, str] = {}
    for p in COMP.rglob("*.py"):
        if set(p.relative_to(ROOT).parts) & SKIP_PARTS:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        for tok in src.split('"'):
            if tok.endswith(".witness.json") and "/" not in tok:
                literal.setdefault(tok, str(p.relative_to(ROOT)))
        for tok in src.split("'"):
            if tok.endswith(".witness.json") and "/" not in tok:
                literal.setdefault(tok, str(p.relative_to(ROOT)))

    counts: dict[str, int] = {}
    unattributed: list[str] = []
    total = 0
    for w in sorted(COMP.rglob("*.witness.json")):
        if set(w.relative_to(ROOT).parts) & SKIP_PARTS:
            continue
        total += 1
        stem = w.name[: -len(".witness.json")]
        prod = None
        for base in (w.parent, COMP):
            for cand in (stem.replace("-", "_"), stem):
                f = base / f"{cand}.py"
                if f.exists():
                    prod = str(f.relative_to(ROOT))
                    break
            if prod:
                break
        if prod is None:
            for cand in (stem.replace("-", "_"), stem):
                hits = stem_index.get(cand, [])
                if len(hits) == 1:
                    prod = str(hits[0].relative_to(ROOT))
                    break
        if prod is None:
            prod = literal.get(w.name)
        if prod is None:
            unattributed.append(str(w.relative_to(ROOT)))
            continue
        r = by_file.get(prod)
        b = r["bucket"] if r else "producer_outside_both_cones"
        counts[b] = counts.get(b, 0) + 1
    counts["_witness_files_total"] = total
    counts["_no_producer_found"] = len(unattributed)
    counts["_unattributed_sample"] = unattributed[:8]
    return counts


def summarise(res: dict) -> dict:
    def bucket(rows, label):
        b: dict[str, int] = {}
        for r in rows:
            b[r["bucket"]] = b.get(r["bucket"], 0) + 1
        prod = [r for r in rows if r["producer"]]
        return {
            "label": label,
            "in_cone": len(rows),
            "producers": len(prod),
            "raises": b.get("raises", 0),
            "muon_already_50": b.get("muon_already_50", 0),
            "moves_own_mp": b.get("moves_own_mp", 0),
            "moves_via_helper": b.get("moves_via_helper", 0),
            "no_mp_unaffected": b.get("no_mp", 0),
        }
    return {
        "q_parameter": bucket(res["cone_q_parameter"], "imports q_parameter"),
        "constants_only": bucket(
            res["cone_constants_only"],
            "imports qou_substrate.constants but NOT q_parameter"),
    }


def self_test() -> int:
    cases = [
        ("set_compute_dps() is a raise",
         "from _precision import set_compute_dps\nset_compute_dps()\n", True),
        ("mp.mp.dps assignment is a raise",
         "import mpmath as mp\nmp.mp.dps = 50\n", True),
        ("`from mpmath import mp` + mp.dps is a raise",
         "from mpmath import mp\nmp.dps = 60\n", True),
        ("workdps block is a raise",
         "import mpmath as mp\nwith mp.workdps(50):\n    pass\n", True),
        ("importing a raiser without calling it is NOT",
         "from _precision import set_compute_dps, fmt\nx = 1\n", False),
        ("plain mpf use is NOT a raise",
         "import mpmath as mp\nx = mp.mpf('1.5')\n", False),
    ]
    bad = 0
    for name, src, want in cases:
        if bool(raise_sites(ast.parse(src))) != want:
            print(f"  FAIL {name}")
            bad += 1
    imp_cases = [
        ("bare import", "import q_parameter\n", "q_parameter"),
        ("ALIASED import (the shape grep misses)",
         "import q_parameter as qp\nx = qp.Q\n", "q_parameter"),
        ("from-import", "from q_parameter import Q, HA\n", "q_parameter"),
        ("star import", "from q_parameter import *\n", "q_parameter"),
        ("dotted prefix pulls the package __init__",
         "import qou_substrate.constants\n", "qou_substrate"),
        ("function-scope import", "def f():\n    import q_parameter\n",
         "q_parameter"),
        ("from-package submodule",
         "from qou_substrate import witness\n", "qou_substrate.witness"),
    ]
    for name, src, want in imp_cases:
        mods = imported_modules(ast.parse(src), Path("x.py"))
        if want not in mods:
            print(f"  FAIL import {name}: {want!r} not in {sorted(mods)}")
            bad += 1
    mp_cases = [
        ("mp.mpf builds a value", "import mpmath as mp\nmp.mpf('1')\n", True),
        ("bare mpf builds a value", "from mpmath import mpf\nmpf('1')\n", True),
        ("mp.dps is a setting, not a value",
         "import mpmath as mp\nmp.dps = 50\n", False),
    ]
    for name, src, want in mp_cases:
        if bool(mp_value_lines(ast.parse(src))) != want:
            print(f"  FAIL mp {name}")
            bad += 1
    fam = imports_mp_family(ast.parse("from q_parameter import Q_MP, HA_MP\n"))
    if not fam:
        print("  FAIL _MP family import not detected")
        bad += 1
    if imports_mp_family(ast.parse("from q_parameter import Q, HA\n")):
        print("  FAIL float-only import wrongly flagged as _MP family")
        bad += 1
    n = len(cases) + len(imp_cases) + len(mp_cases) + 2
    if bad:
        print(f"SELF-TEST FAILED — {bad}/{n}")
        return 1
    print(f"SELF-TEST PASSED — {n} cases")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--list", choices=["moves_own_mp", "moves_via_helper",
                                       "raises", "muon_already_50", "no_mp"])
    ap.add_argument("--cone", choices=["q_parameter", "constants_only"],
                    default="q_parameter")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    res = scan()
    s = summarise(res)
    wq = witnesses_for(res)
    if a.json:
        print(json.dumps({"summary": s, "witnesses_by_bucket": wq,
                          "detail": res}, indent=2))
        return 0

    print("=" * 78)
    print("q_parameter 50-DPS FLOOR — BLAST RADIUS   (bean qou-zbws, measure only)")
    print("=" * 78)
    print(f"  python files scanned (excl. qou-mass/, _deprecated/) : "
          f"{res['files_scanned']}")
    print(f"  parsed                                              : {res['parsed']}")
    print(f"  DIRECT importers of q_parameter (AST)               : "
          f"{res['direct_importers_q_parameter']}")
    if res["broken"]:
        print(f"  ⚠ unparseable — NO claim is made about these        : "
              f"{len(res['broken'])}")
        for r in res["broken"][:10]:
            print(f"      {r['file']}  [{r['kind']}]")
    for key in ("q_parameter", "constants_only"):
        b = s[key]
        print(f"\n  ── {b['label']} ──")
        print(f"     files in transitive import cone       : {b['in_cone']}")
        print(f"     of which runnable witness producers   : {b['producers']}")
        print(f"       A. raise dps themselves  UNAFFECTED : {b['raises']}")
        print(f"       B. muon manifest, already 50        : {b['muon_already_50']}")
        print(f"       C. no dps raise, own mpmath values  : {b['moves_own_mp']}"
              f"      <- NUMBERS MOVE")
        print(f"       D. no dps raise, mp only via helper : "
              f"{b['moves_via_helper']}      <- probably move")
        print(f"       E. no dps raise, no mpmath anywhere : "
              f"{b['no_mp_unaffected']}      <- unaffected")

    print("\n  ── committed witnesses under computations/, by producer bucket ──")
    for k in ("moves_own_mp", "moves_via_helper", "no_mp", "raises",
              "muon_already_50", "not_a_producer",
              "producer_outside_both_cones", "_no_producer_found",
              "_witness_files_total"):
        if k in wq:
            print(f"     {k:28s} : {wq[k]}")

    if a.list:
        rows = res["cone_" + ("q_parameter" if a.cone == "q_parameter"
                              else "constants_only")]
        sel = sorted(r["file"] for r in rows if r["bucket"] == a.list)
        print()
        for f in sel:
            print(f"  {f}")
        print(f"  ({len(sel)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
