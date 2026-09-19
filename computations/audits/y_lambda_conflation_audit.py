#!/usr/bin/env python3
"""`y_lambda` naming a weight that is NOT the Wenzl y_λ.

AGENTS.md is explicit that the three partition-weight families y_λ / w_λ / w̃_λ
are DISTINCT at q ≠ 1 and must never be conflated. This audit is the mechanical
half of that rule: it finds places where the name `y_lambda` / `y_λ` is attached
to the **quantum Plancherel** measure `d_q(λ)² / [n]_q!` instead.

WHY IT EXISTS — the conflation was not cosmetic, and nothing caught it
--------------------------------------------------------------------
The three Magnus Ω₂ sign probes aggregated with the Plancherel measure while
calling it `y_λ` in every docstring, in the `pairing` field of every witness,
and in the `y_lambda` column of every `per_partition` row (bean `qou-za3q`).
Two costs followed, and only the second was noticed:

  1. A corpus grep keying on the name `y_lambda` could not tell those witnesses
     apart from the production Markov weight.
  2. Re-weighting the SAME committed traces with the real Wenzl bridge flips the
     sign of P_total at A=3 and A=4 (Plancherel −,+,+ over A=2,3,4; Wenzl
     −,−,−). The programme's target A-dependent sign change is exhibited under
     one name and absent under the other. So the two families are not a
     rescaling, and a mislabelled weight is a mislabelled RESULT.

Not one existing detector fired. Checked before writing this: the whole
`computations/audits` tree greps for value/precision/staleness defects, and the
naming rule lived only in AGENTS.md prose. `qou-9yt9`'s docstring-claims-gap
sweep also missed it, because the docstring and the code AGREED — both said
`y_λ`; both were wrong about which y_λ.

WHAT IT FLAGS
-------------
A. **Textual identification.** Source, doc, or witness text that writes the
   equation `y_λ = d_q(λ)²/[n]_q!` (in any of the spellings the corpus uses).
   This is the forbidden statement itself, so it is flagged wherever it appears.

B. **Structural mislabelling (AST).** A value produced by a function that
   DECLARES itself the quantum Plancherel measure — its docstring says so — and
   then stored under a name or dict key containing `y_lambda`. This is the shape
   the sign probes had: `wedderburn_weight()` (docstring: "**quantum
   Plancherel** measure") written into a `"y_lambda"` row key.

C. **A Plancherel producer named `y_lambda`.** A function whose docstring
   declares the Plancherel measure while its own name says `y_lambda`.

D. **Undeclared witness column.** A witness JSON carrying a `y_lambda` key
   inside a per-partition array, in a `results`/`data` object that declares no
   `weight_family`. A consumer reading that column has no way to know which
   family it holds — which is exactly how the number travelled.

NOT FLAGGED, deliberately
-------------------------
  * A `y_lambda` fed from the Wenzl bridge (`y_lambda_wenzl_bridge*`), which is
    the correct use of the name.
  * A witness column that DOES declare `weight_family` — declaring it is the
    remedy this audit asks for, so a declared column is clean whichever family
    it names. (D is a labelling gate, not a family preference.)
  * Prose that CONTRASTS the two families, e.g. text containing "NOT the Wenzl"
    or naming both — describing the conflation is how it gets fixed, and the
    fix must not trip the detector that motivated it.
  * `library/` — external literature; not ours to relabel.

Exit 0 when clean, 1 otherwise. `--self-test` runs the fixture pair only.

-- Ref: [manuscript] AGENTS.md "uses[] and interprets are the EDITORIAL relation"
-- Ref: [manuscript] docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md
"""
from __future__ import annotations

import ast
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"__pycache__", "node_modules", ".git", ".lake", "library",
             "_deprecated", "data"}

#: This file quotes the forbidden equation in its docstring and its fixtures.
#: A detector that fires on its own definition of the defect is noise.
SELF = os.path.abspath(__file__)

#: Check D's standing backlog. D is a RATCHET, not a pass/fail gate: 48 tracked
#: witness columns already carry an undeclared `y_lambda`, and per this
#: repo's own doctrine (scripts/precision-gates.sh: "a gate that is red on
#: arrival gets skipped, which is how a checker goes quiet") a detector that
#: cannot be green cannot be a gate. A/B/C are pass/fail — they were all zero
#: after the qou-za3q/qou-q2q7 fixes, so they can only fire on a regression.
#: THE BASELINE DRAINS, NEVER GROWS. Re-baselining upward to go green defeats
#: the mechanism; declare `weight_family` at the producer instead.
#:
#: IT READ 55 UNTIL 2026-09-14, AND SEVEN OF THOSE WERE NOT CORPUS FILES. The
#: walk counted gitignored chi caches (`.gitignore:230`), so the number moved
#: whenever a sibling regenerated one — it went 55 -> 56 within a day of this
#: audit landing, on a file no other machine has. `tracked_only()` now filters
#: to what git tracks. THE 55 -> 48 DROP IS A SCOPE CORRECTION, NOT SEVEN
#: FIXES: the seven were `chi-{deuteron,dineutron,diproton,helium-3,neutron,
#: proton,tritium}-*-at-q<hex>-50dps.witness.json`, all still undeclared, just
#: not part of the corpus. Nothing was declared to earn it.
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "y-lambda-undeclared-column-baseline.json")

#: A docstring that says this is the Plancherel measure. Matching on the
#: DECLARATION rather than on the arithmetic keeps the detector honest: a
#: producer that renames itself without changing what it computes still trips,
#: and one that genuinely switches family stops tripping when it says so.
_PLANCHEREL_DECL = re.compile(r"quantum\s+Plancherel", re.I)

#: The forbidden identification, in the spellings the corpus actually uses:
#: `y_λ = d_q(λ)²/[n]_q!`, `y_lambda = d_q(lambda)^2 / [n]_q!`, and the
#: `d_q²/[n]_q!` short form.
_CONFLATION = re.compile(
    r"y_(?:λ|lambda)\s*[=:]\s*d_?q\s*(?:\((?:λ|lambda)\))?\s*(?:²|\^2|\*\*2)"
    r"\s*/\s*\[?\s*n\s*\]?_?q\s*!",
    re.I,
)

#: Prose that is ABOUT the distinction rather than asserting the identity. A
#: line carrying one of these is discussing the two families, so the equation
#: in it is a quotation, not a claim.
_CONTRAST = re.compile(
    r"NOT the Wenzl|not the wenzl|forbids conflat|conflation|"
    r"quantum Plancherel|names the WENZL weight only|weight famil",
    re.I,
)

_NAME_IS_Y = re.compile(r"y_(?:lambda|λ)", re.I)
_WENZL_SOURCE = re.compile(r"wenzl|markov", re.I)

TEXT_EXT = {".py", ".md", ".ts", ".lean", ".json"}


def tracked_only() -> set[str] | None:
    """Tracked-file filter for check D — see `_tracked_corpus` for why.

    Shared with `intra_ordering_structural_assembly_audit` rather than copied:
    this audit's sibling exists precisely because the corpus transcribes shared
    one-liners instead of calling them.
    """
    from _tracked_corpus import tracked_files          # noqa: PLC0415
    return tracked_files(ROOT, verify=SELF)


def _iter_files(root: str):
    tracked = tracked_only()
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in sorted(files):
            if os.path.splitext(fn)[1] not in TEXT_EXT:
                continue
            p = os.path.join(dirpath, fn)
            if tracked is not None and os.path.abspath(p) not in tracked:
                continue
            yield p


# ---------------------------------------------------------------- check A ----
def scan_text(path: str, src: str | None = None) -> list[dict]:
    """A. the forbidden identification written out, outside contrast prose."""
    if src is None:
        try:
            src = open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            return []
    out = []
    for i, line in enumerate(src.splitlines(), 1):
        if _CONFLATION.search(line) and not _CONTRAST.search(line):
            out.append({"check": "A", "path": os.path.relpath(path, ROOT),
                        "line": i, "detail": line.strip()[:150]})
    return out


# ------------------------------------------------------------- checks B/C ----
def _plancherel_producers(tree: ast.AST) -> set[str]:
    """Functions whose own docstring declares them the Plancherel measure."""
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node) or ""
            if _PLANCHEREL_DECL.search(doc):
                names.add(node.name)
    return names


def _callee(node: ast.AST) -> str | None:
    if not isinstance(node, ast.Call):
        return None
    f = node.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return None


def scan_python(path: str, src: str | None = None) -> list[dict]:
    if src is None:
        try:
            src = open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            return []
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    rel = os.path.relpath(path, ROOT)
    producers = _plancherel_producers(tree)
    out = []

    # C — a Plancherel producer whose own name says y_lambda.
    for name in sorted(producers):
        if _NAME_IS_Y.search(name):
            out.append({"check": "C", "path": rel, "line": 0,
                        "detail": f"def {name}() declares the quantum Plancherel "
                                  f"measure but is named y_lambda"})

    if not producers:
        return out

    # B — a Plancherel producer's value stored under a y_lambda name or key.
    for node in ast.walk(tree):
        target_names: list[tuple[str, ast.AST]] = []
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    target_names.append((t.id, node.value))
        elif isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and isinstance(k.value, str):
                    target_names.append((k.value, v))
        for nm, val in target_names:
            if not _NAME_IS_Y.search(nm):
                continue
            call = _callee(val)
            # A cast around the call (fmt(...), str(...), mp.nstr(...)) is the
            # usual serialisation shape; look one level in before giving up.
            if call is not None and call not in producers and isinstance(val, ast.Call):
                for a in val.args:
                    inner = _callee(a)
                    if inner in producers:
                        call = inner
                        break
            if call in producers and not _WENZL_SOURCE.search(nm):
                out.append({"check": "B", "path": rel,
                            "line": getattr(val, "lineno", 0),
                            "detail": f"`{nm}` <- {call}(), which declares itself "
                                      f"the quantum Plancherel measure"})
    return out


# ---------------------------------------------------------------- check D ----
def _per_partition_arrays(obj, path=()):
    """Yield (container, array) for every list-of-dicts under a results-ish key."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if (isinstance(v, list) and v
                    and all(isinstance(e, dict) for e in v)):
                yield obj, k, v
            yield from _per_partition_arrays(v, path + (k,))
    elif isinstance(obj, list):
        for e in obj:
            yield from _per_partition_arrays(e, path)


def scan_witness(path: str, doc=None) -> list[dict]:
    if doc is None:
        try:
            doc = json.load(open(path, encoding="utf-8"))
        except (OSError, ValueError, UnicodeDecodeError):
            return []
    if not isinstance(doc, dict):
        return []
    rel = os.path.relpath(path, ROOT)
    out = []
    # One finding per (file, column). `_per_partition_arrays` walks the whole
    # document, so a witness holding the same array under several parents — or
    # several sibling arrays of the same name — reported the same column many
    # times over. That inflates the count a ratchet is measured against.
    seen: set[str] = set()
    for container, key, arr in _per_partition_arrays(doc):
        if not any(_NAME_IS_Y.fullmatch(k or "") for e in arr for k in e):
            continue
        if any(k == "weight_family" for k in container):
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append({"check": "D", "path": rel, "line": 0,
                    "detail": f"`{key}[].y_lambda` with no `weight_family` "
                              f"declared beside it"})
    return out


def scan_file(path: str) -> list[dict]:
    if os.path.abspath(path) == SELF:
        return []
    ext = os.path.splitext(path)[1]
    out = scan_text(path)
    if ext == ".py":
        out += scan_python(path)
    elif ext == ".json" and path.endswith(".witness.json"):
        out += scan_witness(path)
    return out


# ----------------------------------------------------------------- tests -----
_FIRES_PY = '''
def wedderburn_weight(shape, q):
    """**quantum Plancherel** measure d_q^2/[n]_q!."""
    return 1

def y_lambda_planch(shape, q):
    """the **quantum Plancherel** measure."""
    return 1

def go():
    rows = []
    rows.append({"lambda": (1,), "y_lambda": wedderburn_weight((1,), 2)})
'''

_QUIET_PY = '''
def wedderburn_weight(shape, q):
    """**quantum Plancherel** measure d_q^2/[n]_q!."""
    return 1

def go():
    rows = []
    # correctly named, and the Wenzl arm keeps its own key
    rows.append({"lambda": (1,), "w_planch": wedderburn_weight((1,), 2),
                 "y_lambda_wenzl": 0})
'''

_FIRES_TXT = "  pairing  P = sum_lam y_lambda tr(rho Om2), y_lambda = d_q(lambda)^2/[n]_q!\n"
_QUIET_TXT = ("  the `y_lambda` column holds the quantum Plancherel measure "
              "y_lambda = d_q(lambda)^2/[n]_q!, NOT the Wenzl y_lambda\n")

_FIRES_W = {"results": {"per_partition": [{"lambda": [2], "y_lambda": "0.5"}]}}
_QUIET_W = {"results": {"per_partition": [{"lambda": [2], "y_lambda": "0.5"}],
                        "weight_family": "quantum_plancherel_dq2_over_n_factorial"}}


def _selftest() -> None:
    cases = [
        ("py fires", len(scan_python("<t>", _FIRES_PY)), 2),
        ("py quiet", len(scan_python("<t>", _QUIET_PY)), 0),
        ("txt fires", len(scan_text("<t>", _FIRES_TXT)), 1),
        ("txt quiet", len(scan_text("<t>", _QUIET_TXT)), 0),
        ("witness fires", len(scan_witness("<t>", _FIRES_W)), 1),
        ("witness quiet", len(scan_witness("<t>", _QUIET_W)), 0),
    ]
    bad = [(n, got, want) for n, got, want in cases if got != want]
    if bad:
        for n, got, want in bad:
            print(f"  SELFTEST FAIL {n}: expected {want}, got {got}", file=sys.stderr)
        raise SystemExit(2)


def _load_baseline() -> set[str]:
    try:
        with open(BASELINE, encoding="utf-8") as fh:
            return set(json.load(fh).get("undeclared_columns", []))
    except (OSError, ValueError):
        return set()


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    _selftest()
    if "--self-test" in argv:
        print("  selftest: PASS (3 must-fire, 3 must-stay-quiet)")
        return 0
    rebaseline = "--rebaseline" in argv
    argv = [a for a in argv if a != "--rebaseline"]

    findings: list[dict] = []
    # The check-D ratchet compares against a whole-tree baseline, so it is only
    # meaningful on a whole-tree scan. In --files mode the unscanned files look
    # drained: the first run of this audit against a single file reported
    # "drained: 55" and invited a --rebaseline that would have erased a real
    # backlog. Partial scans therefore report A/B/C only.
    partial = bool(argv and argv[0] == "--files")
    if partial:
        for a in argv[1:]:
            if os.path.exists(a):
                findings += scan_file(os.path.abspath(a))
    else:
        for p in _iter_files(ROOT):
            findings += scan_file(p)
    if partial and rebaseline:
        print("  REFUSED: --rebaseline needs a whole-tree scan; drop --files.")
        return 2
    findings.sort(key=lambda r: (r["check"], r["path"], r["line"]))

    abc = [f for f in findings if f["check"] in "ABC"]
    d_keys = sorted({f"{f['path']}::{f['detail'].split('[')[0].strip('`')}"
                     for f in findings if f["check"] == "D"})

    if rebaseline:
        with open(BASELINE, "w", encoding="utf-8") as fh:
            json.dump({
                "_comment": "Check-D ratchet. DRAINS, NEVER GROWS — declare "
                            "weight_family at the producer instead of adding "
                            "an entry here. See the module docstring.",
                "count": len(d_keys),
                "undeclared_columns": d_keys,
            }, fh, indent=1)
            fh.write("\n")
        print(f"  rebaselined check D at {len(d_keys)} undeclared columns -> {BASELINE}")
        return 0

    base = _load_baseline()
    d_new = [k for k in d_keys if k not in base]
    d_fixed = [] if partial else sorted(base - set(d_keys))

    print("=" * 78)
    print(" y_lambda NAMING A WEIGHT THAT IS NOT THE WENZL y_λ")
    print("=" * 78)
    by = {c: sum(1 for f in findings if f["check"] == c) for c in "ABC"}
    print(f"  A  forbidden identification in text            : {by['A']}   (blocking)")
    print(f"  B  Plancherel value under a y_lambda name/key  : {by['B']}   (blocking)")
    print(f"  C  Plancherel producer named y_lambda          : {by['C']}   (blocking)")
    print(f"  D  witness y_lambda column, no weight_family   : {len(d_keys)}"
          f"  (ratchet, baseline {len(base)})")
    if partial:
        print("     partial scan (--files): D reports new entries only; the "
              "drain count needs a whole-tree run")
    print(f"     new since baseline : {len(d_new)}"
          f"{'' if partial else f'      drained : {len(d_fixed)}'}")
    print("  selftest : PASS (3 must-fire, 3 must-stay-quiet)")
    if tracked_only() is None:
        print("     ⚠ git unavailable — scanning the WORKING DIRECTORY, so "
              "untracked artifacts are counted and D is not reproducible")

    if abc:
        print()
        for f in abc:
            loc = f"{f['path']}:{f['line']}" if f["line"] else f["path"]
            print(f"  [{f['check']}] {loc}")
            print(f"        {f['detail']}")
    if d_new:
        print()
        print("  NEW undeclared y_lambda columns (this is what the ratchet blocks):")
        for k in d_new:
            print(f"  [D] {k}")
    if d_fixed:
        print()
        print(f"  {len(d_fixed)} baseline entries no longer fire — run with "
              f"--rebaseline to lower the ratchet.")
    if abc or d_new:
        print()
        print("  FIX AT THE PRODUCER. Name the family (`w_planch`, or the Wenzl")
        print("  bridge for the Markov weight) and declare `weight_family` beside")
        print("  any y_lambda column. Renaming the audit's pattern, or widening")
        print("  the baseline, defeats the rule AGENTS.md states.")
    return 1 if (abc or d_new) else 0


if __name__ == "__main__":
    sys.exit(main())
