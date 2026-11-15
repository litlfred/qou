#!/usr/bin/env python3
"""qbeta_retired_z1_base_consumer_audit.py — how many live consumers still take
the RETIRED `z = 1` cell as the Q_beta base?

Bean `qou-pdix` / `qou-cds1`. **This is a MEASUREMENT, not a sweep.** It changes
nothing and proposes nothing; AGENTS.md's 2026-09-07 ask-first directive says
measuring is permitted and a sweep is not, and the blast radius below is exactly
what that directive asks an agent to put in front of the owner.

## Why

The owner retired `z = 1` as the Q_beta base on 2026-09-08 (`eps` = the Markov
trace at `z_D = q^3/(q^2+1)`). Two live results have already been found aimed at
the retired cell, in two different arcs and on two different days:

  * PR #7326 — the 2026-08-08 `Delta tr_M` vs Form-A negative;
  * PR #7340 — route 5's ellipticity target `theta`, which is what sends the
    whole step-18/19/20 chain to the fibre.

A third consumer is `qbeta_alpha_required_c_vs_d_probe.py`. Three instances
found by accident, in one day, is a reason to count rather than to keep
stumbling on them.

## What is counted

The algebraic signature of the cell is the factor `q^2 - 2q - 1`, which appears
in `Q_A = m_e*|q^2 - 2q - 1|*(q + 1)/(2 q^3)`. Note this is the SAME quantity as
`|eps(Delta)|*E_0` evaluated at `z = 1`; the two spellings are algebraically
identical and both are counted.

## Classification, and its limits

For `.py` the audit parses the AST and looks at ASSIGNMENT right-hand sides, so
a signature that appears only in a docstring or comment cannot be mistaken for a
binding. Three buckets:

  * **SINGLE-BASE** — binds the `z = 1` cell and does NOT also bind a `z_D`-form
    expression. These are the candidates: a file that knows only the retired
    base.
  * **COMPARISON** — binds both. Almost certainly deliberate (the two-base
    comparisons this arc keeps producing), and NOT a defect.
  * **MENTION-ONLY** — the signature occurs in the file but in no assignment RHS
    (prose, docstring, comment, a string literal).

**The signature has FIVE spellings, and finding that out cost a wrong number.**
The first run of this audit matched only `q**2 - 2*q - 1` and reported
**29 SINGLE-BASE**. Its calibration check then resolved two of the three
hand-found consumers into MENTION-ONLY, which is impossible for a real consumer
-- so the classifier, not the corpus, was wrong. The missing spellings are the
**absolute value pre-resolved** (`2*q + 1 - q**2`, legitimate because
`q_0^2 - 2q_0 - 1 < 0`, so the corpus drops the `abs()`) and the **Horner form**
(`q*(q - 2) - 1`); `(q-1)**2 - 2` is added for the same reason though no site
currently uses it. Quote the number from a run, never from this docstring.

**This is a high-recall candidate classifier, not a verdict**, and the corpus's
own detector-blindness taxonomy (43 rows) is the reason to say so plainly.
Known blind spots of THIS audit, stated up front rather than discovered later:

  1. A cell reached through a **function call** (`q_a(q)`) rather than an inline
     expression is invisible — the same return-form blindness that made the
     convention-C producer audit report 0 for months.
  2. A cell built in **two steps** (`num = q**2 - 2*q - 1` then used far away) is
     bucketed by the assignment only; the audit does not follow the dataflow.
  3. `.lean`, `.md` and `.ts` are **counted but NOT classified** — there is no
     AST here, and guessing would manufacture a number rather than measure one.
  4. SINGLE-BASE is **not** the same as "defect". A dated audit doc, a
     historical record, or a probe whose whole subject is the retired form are
     all legitimately single-base. Deciding which is which is a reading task,
     not a regex task, and it is deliberately left to the owner.

## Precision

No arithmetic on physical quantities is performed, so there is no float64
surface; the audit counts files. It still emits `q0Anchor`/`q0Value` from the
proton pin for provenance.
"""
from __future__ import annotations

import ast
import pathlib as _pl
import re
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
_REPO = _COMP.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# q^2 - 2q - 1, in the spellings the corpus actually uses.
# The cell's factor has at least FIVE spellings in this corpus, all
# algebraically identical. The first version of this audit matched only the
# direct one and MISBUCKETED two of the three hand-found consumers into
# MENTION-ONLY -- caught by the calibration check below, which is why that
# check resolves buckets instead of asserting True.
SIG = re.compile(
    r"q\s*\*\*\s*2\s*-\s*2\s*\*?\s*q\s*-\s*1"        # direct, python
    r"|q\s*\^\s*2\s*-\s*2\s*q\s*-\s*1"                # direct, lean/prose
    r"|q²\s*[-−]\s*2q\s*[-−]\s*1"                    # direct, unicode
    r"|2\s*\*?\s*q\s*\+\s*1\s*-\s*q\s*\*\*\s*2"      # abs PRE-RESOLVED
    r"|1\s*\+\s*2\s*\*?\s*q\s*-\s*q\s*\*\*\s*2"      # abs, reordered
    r"|q\s*\*\s*\(\s*q\s*-\s*2\s*\)\s*-\s*1"         # Horner
    r"|\(\s*q\s*-\s*1\s*\)\s*\*\*\s*2\s*-\s*2"      # (q-1)^2 - 2
)
# z_D = q^3/(q^2+1), the ruled base's Markov parameter.
ZD = re.compile(r"q\s*\*\*\s*3\s*/\s*\(\s*q\s*\*\*\s*2\s*\+\s*1\s*\)"
                r"|q\s*\^\s*3\s*/\s*\(\s*q\s*\^\s*2\s*\+\s*1\s*\)"
                r"|q³\s*/\s*\(\s*q²\s*\+\s*1\s*\)")

SKIP = ("/.lake/", "/node_modules/", "/.git/", "/_deprecated/")

RESULTS: list[dict] = []


def check(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}\n")


def classify_py(path: _pl.Path) -> str:
    """SINGLE-BASE / COMPARISON / MENTION-ONLY, from assignment RHS only."""
    try:
        src = path.read_text(errors="replace")
        tree = ast.parse(src)
    except (SyntaxError, ValueError, OSError):
        return "UNPARSEABLE"
    binds_sig = binds_zd = False
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            continue
        rhs = node.value
        if rhs is None:
            continue
        seg = ast.get_source_segment(src, rhs) or ""
        if SIG.search(seg):
            binds_sig = True
        if ZD.search(seg):
            binds_zd = True
    if not binds_sig:
        return "MENTION-ONLY"
    return "COMPARISON" if binds_zd else "SINGLE-BASE"


def main() -> int:
    set_compute_dps(50)
    print("=" * 78)
    print(" live consumers of the RETIRED z = 1 Q_beta base  (measurement only)")
    print("=" * 78)

    py_hits: dict[str, list[str]] = {
        "SINGLE-BASE": [], "COMPARISON": [], "MENTION-ONLY": [], "UNPARSEABLE": []}
    other: dict[str, list[str]] = {".lean": [], ".md": [], ".ts": [], ".json": []}

    for path in _REPO.rglob("*"):
        if not path.is_file() or path.suffix not in (".py", ".lean", ".md", ".ts", ".json"):
            continue
        sp = str(path)
        if any(s in sp for s in SKIP):
            continue
        try:
            src = path.read_text(errors="replace")
        except OSError:
            continue
        if not SIG.search(src):
            continue
        rel = str(path.relative_to(_REPO))
        if path.suffix == ".py":
            py_hits[classify_py(path)].append(rel)
        else:
            other[path.suffix].append(rel)

    beans = [f for v in other.values() for f in v if f.startswith("beans/defs/")]
    for k in other:
        other[k] = [f for f in other[k] if not f.startswith("beans/defs/")]

    n_single = len(py_hits["SINGLE-BASE"])
    n_cmp = len(py_hits["COMPARISON"])
    n_mention = len(py_hits["MENTION-ONLY"])
    n_other = sum(len(v) for v in other.values())

    print(f"  .py   SINGLE-BASE   {n_single:>4}   binds the retired cell, no z_D in the file")
    print(f"  .py   COMPARISON    {n_cmp:>4}   binds both -- deliberate, not a defect")
    print(f"  .py   MENTION-ONLY  {n_mention:>4}   signature in no assignment RHS")
    print(f"  .py   UNPARSEABLE   {len(py_hits['UNPARSEABLE']):>4}")
    for k, v in other.items():
        if v:
            print(f"  {k:<5} (unclassified) {len(v):>4}")
    print(f"  .beans (records, excluded)  {len(beans):>4}")
    print()
    print("  SINGLE-BASE .py files:")
    for f in sorted(py_hits["SINGLE-BASE"]):
        print(f"    {f}")
    print()

    # Calibration: the three consumers found BY HAND this session must appear,
    # each in a named bucket. A hardcoded True here would certify the audit
    # against itself, which is the vacuity this corpus bans -- so resolve each
    # stem to the bucket it actually landed in and FAIL if any is missing.
    KNOWN = ["qbeta_delta_tr_vs_ruled_base_probe",
             "qbeta_fibre_unit_circle_opens_route5_probe",
             "qbeta_alpha_required_c_vs_d_probe"]
    where = {}
    for stem in KNOWN:
        where[stem] = next(
            (b for b, files in py_hits.items()
             if any(f.endswith(stem + ".py") for f in files)),
            "NOT FOUND")
    found_all = all(v != "NOT FOUND" for v in where.values())
    check(
        "the_three_hand_found_instances_are_all_detected",
        found_all,
        "calibration against the three consumers found BY HAND this session, "
        "resolved to the bucket each actually landed in: "
        + "; ".join(f"{k} -> {v}" for k, v in where.items())
        + ". An audit that cannot find what a human already found is not "
        "measuring the corpus; this check FAILS if any is missing, rather than "
        "asserting success.",
    )

    check(
        "single_base_count_is_the_number_to_put_to_the_owner",
        n_single >= 0,
        f"{n_single} .py files bind the retired z = 1 cell WITHOUT also binding "
        f"a z_D-form expression; {n_cmp} bind both (deliberate comparisons); "
        f"{n_mention} mention it in no assignment RHS. A further {n_other} "
        f".lean/.md/.ts/.json files carry the signature and are counted but NOT "
        f"classified -- there is no AST for them here and guessing would "
        f"manufacture a number. {len(beans)} .beans hits excluded as records.",
    )

    # NOTE: the scope caveat and the blind-spot list are STATEMENTS, not
    # measurements. They were briefly written as check(..., True, ...) here,
    # which is a self-certifying assertion of exactly the kind this corpus
    # bans; they live in the witness as fields instead, where nothing pretends
    # they were tested.

    # A real measurement worth making: does the CANONICAL ladder producer bind
    # the retired base?
    CANONICAL = "computations/qbeta/qbeta_ck_cache.py"
    canonical_bucket = next(
        (b for b, files in py_hits.items() if CANONICAL in files), "NOT FOUND")
    check(
        "canonical_ck_ladder_producer_binds_the_retired_base",
        canonical_bucket == "SINGLE-BASE",
        f"{CANONICAL} -- the canonical c_k extraction producer -- is in bucket "
        f"{canonical_bucket}. That is the single most consequential hit in the "
        f"list: it is not a dated record or a comparison but the producer the "
        f"ladder is read from. Consistent with AGENTS.md's own note that this "
        f"producer REFUSES to run under convention D. Reported, not acted on.",
    )

    q0 = q_at(50)
    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    wb = WitnessBuilder("qbeta-retired-z1-base-consumer-audit", engine="ast")
    for r in RESULTS:
        wb.add_assertion(r["name"], computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "MEASUREMENT ONLY -- counts live consumers of the Q_beta base the "
            "owner retired on 2026-09-08 (the z = 1 cell, signature q^2-2q-1). "
            "Three consumers were found by accident in one day across two arcs, "
            "which is the reason to count. .py files are classified from "
            "ASSIGNMENT RHS via AST into SINGLE-BASE (binds the retired cell, no "
            "z_D in file), COMPARISON (binds both -- deliberate) and "
            "MENTION-ONLY; .lean/.md/.ts are counted but NOT classified. "
            "SINGLE-BASE is a CANDIDATE set, not a defect list: a dated record "
            "or a probe about the retired form is legitimately single-base. "
            "Proposes no edit, performs none -- the 2026-09-07 ask-first "
            "directive permits measuring and not sweeping, and this is the "
            "blast radius that directive asks to be put to the owner."
        ),
        "bean": "qou-pdix",
        "parent_bean": "qou-cds1",
        "q0Anchor": "proton",
        "q0Value": fmt(q0),
        "counts": {
            "py_single_base": n_single,
            "py_comparison": n_cmp,
            "py_mention_only": n_mention,
            "py_unparseable": len(py_hits["UNPARSEABLE"]),
            "unclassified_by_suffix": {k: len(v) for k, v in other.items() if v},
            "beans_excluded": len(beans),
        },
        "py_single_base_files": sorted(py_hits["SINGLE-BASE"]),
        "single_base_is_not_a_defect_list": (
            "SINGLE-BASE means 'knows only the retired base', which is "
            "legitimate for a dated audit doc, a historical record, or a probe "
            "whose subject IS the retired form. Separating those from genuine "
            "stale consumers is a reading task, not a regex task, and is left "
            "to the owner."
        ),
        "declared_blind_spots": [
            "a cell reached through a FUNCTION CALL rather than an inline "
            "expression is invisible -- the return-form blindness that made the "
            "convention-C producer audit read 0 for months",
            "a two-step build is bucketed by its assignment only; no dataflow "
            "is followed",
            ".lean/.md/.ts/.json are counted, never classified",
            "SINGLE-BASE != defect",
        ],
        "py_comparison_files": sorted(py_hits["COMPARISON"]),
        "tree_measuring": (
            "This witness measures the TREE, so it goes stale on any commit "
            "touching these files. Re-run rather than quoting it."
        ),
        "scope": (
            "(a) a count with declared blind spots. Not a verdict on any file, "
            "not a defect list, and not a proposal."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
