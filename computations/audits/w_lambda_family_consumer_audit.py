#!/usr/bin/env python3
"""WHICH weight family does each live `w_lambda` consumer actually use?

Bean `qou-oots`, option C. A grep for `w_lambda` over `computations/` returns 43
live files, and that number was used to describe the blast radius of choosing a
canonical family for the depth-stratified functional Phi_k. It is the WRONG
number for that purpose, because `w_lambda` is a NAME shared by families that
are different objects:

  PLANCHEREL-family (the ones the qou-oots choice is between)
    dim_q^2/[n]_q!            historical, NOT normalised (scope-(b) cross-n)
    dim_q^2/D^2               Reshetikhin-Turaev / Verlinde
    f^lam*q^{-kappa}*dim_q    Molien == M_{n,q^2} (qou-j7ef)
  MARKOV family (NOT part of the choice)
    y_lambda                  the Frobenius pairing tr_M = SUM y_lam chi_lam
  NEITHER
    a local variable spelled w / w_lambda that is some other weight entirely

So this audit classifies each file rather than counting it. THE POINT IS TO
SHRINK A NUMBER I QUOTED, not to defend it: I told the author "43 live files
reference a w_lambda-named weight, and I have not established how many are this
family" — this establishes it.

METHOD, and its limits stated up front because a classifier that over-reports is
the failure mode this corpus catalogues at length (AGENTS.md detector-blindness
taxonomy, 34 rows). Classification is by SOURCE PATTERN, per file:

  - a file is PLANCHEREL if it contains a construction of one of the three
    Plancherel weights, or imports one from a module that does;
  - a file is MARKOV if it contains `y_lambda` / `y_lam` / `markov_weight`
    constructions and no Plancherel construction;
  - BOTH is reported separately and is the interesting bucket, since a file
    carrying both may be a deliberate comparison or an undeclared straddle;
  - NAME-ONLY means the token appears (a docstring, a dict key, a witness field)
    with no construction — these are the files a raw grep over-counts.

A source-pattern classifier CANNOT see a weight reached through an alias, a
factory, or a witness file read at runtime. So NAME-ONLY is a lower bound on
"does not compute a weight" and the three real buckets are lower bounds on their
own membership. Reported as measured, not as complete.

No float64: this audit computes no numbers, only counts of files.

CORRECTION 2026-09-05 — the first version of this audit UNDERCOUNTED, and the
instance was found by `qou-wapd` rather than by me.

`close_321_weinberg_gap.py:302` builds `w_lam = d_q_lam ** 2 / fact_n` -- the
dim_q^2/[n]_q! weight exactly -- and was filed NAME-ONLY, because the regex
alternative `d_?q\s*\*\*\s*2` requires the `**` to follow `d_q` immediately and
the local variable is `d_q_lam`. One underscore-suffix defeated the match. That
is row 17-and-counting of the detector-blindness class AGENTS.md catalogues, and
it is the same failure MODE as rows 1-16: keying a detector on how an author
SPELLED a quantity.

The repair is NOT another spelling. It is to key on PROVENANCE -- what the name
was assigned FROM -- following `cached_accessor_shape_audit.py`, which the same
document records as the working instrument for this class. The AST pass below
finds every `X ** 2 / Y` (and `X * X / Y`), then resolves `X` and `Y` back
through the file's assignments to the FUNCTION that produced them. `d_q_lam`
resolves to `dim_q`, `fact_n` to `q_factorial`, and the construction is seen
regardless of what the local was called. Function names are shared across the
corpus and stable; local variable names are ad hoc, which is exactly why keying
on the latter fails.

The regex families are RETAINED alongside it and the buckets are the union, so
no previously-found file can be lost by this change; `detector` on each record
says which pass fired, making the residual blindness of each visible instead of
merely absent. `--selftest` fails unless the known miss is detected, so a future
narrowing cannot quietly restore the undercount.
"""

from __future__ import annotations

import ast
import re
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.witness import WitnessBuilder  # noqa: E402

ROOT = _Path(__file__).resolve().parent.parent

# The token whose 43 hits prompted this.
NAME = re.compile(r'\bw_lambda\b|\bwPlanch\b|\bselfnorm_denominator\b')

# Constructions. Each is a SHAPE that builds a specific family, not a mention.
PLANCH = {
    "dimq2_over_qfact": re.compile(
        r'dim_?q\w*\s*\*\*\s*2\s*/|'
        r'dim_?q\w*\s*\*\s*dim_?q\w*\s*/|'
        r'd_?q\s*\*\*\s*2\s*/'),
    "dimq2_selfnorm": re.compile(r'selfnorm_denominator|/\s*D2\b|sum_dimq2|D_?sq\b'),
    "molien": re.compile(r'molien|fake_?degree|q\s*\*\*\s*\(?\s*-\s*(kappa|content)'),
}
MARKOV = re.compile(r'\by_lambda\b|\by_lam\b|markov_weight|y_lambda_at|y_lambda_su_n')

# -- provenance vocabulary -------------------------------------------------
# These match the name of the FUNCTION a quantity was produced by, not the name
# of the local it was stored in. That is the whole point of the AST pass: a
# producer name is shared corpus-wide and stable, a local is whatever the author
# typed. `d_q_lam` is invisible to a local-name pattern and resolves cleanly
# here, because it was assigned from `dim_q(...)`.
DIMQ_SRC = re.compile(r'(?i)dim_?q|q_?dim|quantum_?dim|\bd_?q\b')

# A q-dimension is often not CALLED but BUILT INLINE from q-integers, and that
# spelling defeated the vocabulary above -- the 13th blindness mode of this
# detector, found 2026-09-05 via the trace-convention registry.
# `two_quark_volume_weighted_clean.py` writes
#
#     d = q_int(3, q) * q_int(2, q);  return d * d / q_factorial(3, q)
#
# whose numerator provenance resolves to `q_int`, matching nothing in DIMQ_SRC.
#
# 🛑 A HIT ON THIS VOCABULARY IS "PLANCHEREL-SHAPED", NOT "A PLANCHEREL WEIGHT".
# The very files that motivated it are the proof: their `d` is the HOOK PRODUCT,
# and the q-dimension is its reciprocal times [n]_q! (`dim_q = [n]_q!/hook_prod`).
# Measured at q0 for lambda |- 3 the true weights are 0.1634 / 0.6607 / 0.1634
# and those files carry 6.1206 / 1.5136 = hook_prod^2/[3]_q!, matching to the
# digit -- so the shape matched while the quantity was INVERTED. Report the
# shape; never assert the family from it.
QINT_SRC = re.compile(r'(?i)q_?int\b|q_?integer|\bqi\b|q_?bracket|q_?num\b')
QFACT_SRC = re.compile(r'(?i)q_?factorial|qfact|\bfact\b|factorial')
SELFNORM_SRC = re.compile(r'(?i)selfnorm|sum_?dim|denominator|\bD2\b|\bD_?sq\b')


def _assign_map(tree: ast.AST) -> dict[str, list[ast.AST]]:
    """name -> every RHS ever assigned to it in this file.

    Deliberately flow-INSENSITIVE and scope-insensitive: a file that assigns the
    same local twice contributes both, and a match on either is enough. For an
    audit whose job is to avoid undercounting, over-collecting provenance is the
    safe direction; the cost is a possible false positive, which is reported
    with its line number and is cheap to check by eye.
    """
    out: dict[str, list[ast.AST]] = {}
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets, value = node.targets, node.value
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)) and node.value:
            targets, value = [node.target], node.value
        else:
            continue
        for t in targets:
            if isinstance(t, ast.Name):
                out.setdefault(t.id, []).append(value)
    return out


def _provenance(node: ast.AST, amap: dict[str, list[ast.AST]],
                depth: int = 0) -> set[str]:
    """Identifiers this expression's VALUE came from, chased through assignment.

    Depth-capped at 6: the chains here are two or three hops (`d_q_lam` <-
    `float(dim_q(...))`), and an unbounded chase would loop on `x = x + 1`.
    """
    if depth > 6:
        return set()
    names: set[str] = set()
    if isinstance(node, ast.Name):
        names.add(node.id)
        for rhs in amap.get(node.id, ())[:4]:
            names |= _provenance(rhs, amap, depth + 1)
    elif isinstance(node, ast.Attribute):
        names.add(node.attr)
        names |= _provenance(node.value, amap, depth + 1)
    elif isinstance(node, ast.Call):
        names |= _provenance(node.func, amap, depth + 1)
        # `float(dim_q(...))` / `mp.mpf(dim_q(...))`: the wrapper is not the
        # provenance, the wrapped expression is. Chase arguments too.
        for a in node.args[:3]:
            names |= _provenance(a, amap, depth + 1)
    elif isinstance(node, ast.Subscript):
        names |= _provenance(node.value, amap, depth + 1)
    elif isinstance(node, ast.BinOp):
        names |= _provenance(node.left, amap, depth + 1)
        names |= _provenance(node.right, amap, depth + 1)
    return names


def _is_square(node: ast.AST) -> ast.AST | None:
    """Return the base of `X ** 2` or `X * X`, else None."""
    if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow)
            and isinstance(node.right, ast.Constant) and node.right.value == 2):
        return node.left
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
        try:
            if ast.dump(node.left) == ast.dump(node.right):
                return node.left
        except (RecursionError, ValueError):
            return None
    return None


def ast_planch_hits(text: str) -> list[dict]:
    """Every `dim_q(lam)^2 / <normaliser>` in the file, found by provenance.

    Reports the LOCAL spellings alongside the resolved producers, so the surface
    a name-keyed detector would have missed is visible in the witness rather
    than merely absent from a count.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    amap = _assign_map(tree)
    hits: list[dict] = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
            continue
        base = _is_square(node.left)
        if base is None:
            continue
        num = _provenance(base, amap)
        num_why = sorted(n for n in num if DIMQ_SRC.search(n))
        shape_only = False
        if not num_why:
            # Fall back to the inline q-integer spelling, and MARK IT, so a
            # reader cannot mistake a shape match for a confirmed family.
            num_why = sorted(n for n in num if QINT_SRC.search(n))
            shape_only = bool(num_why)
        if not num_why:
            continue
        den = _provenance(node.right, amap)
        den_self = sorted(n for n in den if SELFNORM_SRC.search(n))
        den_fact = sorted(n for n in den if QFACT_SRC.search(n))
        if den_self:
            family, den_why = "dimq2_selfnorm", den_self
        elif den_fact:
            family, den_why = "dimq2_over_qfact", den_fact
        else:
            continue
        try:
            local = ast.unparse(node)
        except Exception:  # pragma: no cover - unparse is total in 3.9+
            local = "<unparse failed>"
        # Report the names that DECIDED the match, not an alphabetical prefix of
        # the provenance set. Caught here: `fact_n` resolves through a set whose
        # ninth member alphabetically is `q_factorial`, so a `sorted(...)[:8]`
        # sample recorded a provenance list not containing its own evidence --
        # a row that looks like a false positive while being a true one.
        hits.append({
            "line": getattr(node, "lineno", -1),
            "family": family + ("  [SHAPE-ONLY: numerator built from q-integers, "
                                "NOT confirmed to be a dim_q]" if shape_only else ""),
            "shape_only": shape_only,
            "source": local[:120],
            "matched_numerator": num_why,
            "matched_denominator": den_why,
            "numerator_provenance_sample": sorted(num)[:8],
            "denominator_provenance_sample": sorted(den)[:8],
        })
    return hits


def classify(text: str) -> str:
    p = any(rx.search(text) for rx in PLANCH.values()) or bool(ast_planch_hits(text))
    m = bool(MARKOV.search(text))
    if p and m:
        return "BOTH"
    if p:
        return "PLANCHEREL"
    if m:
        return "MARKOV"
    return "NAME-ONLY"


def main() -> int:
    b = WitnessBuilder("w-lambda-family-consumer-audit")
    b.set_description(
        "Bean qou-oots option C. Classifies every live (non-_deprecated) "
        "computations/ file that references a `w_lambda`-named weight by WHICH "
        "family it actually constructs: PLANCHEREL (the dim_q^2/[n]_q!, "
        "dim_q^2/D^2 or Molien families -- the ones the qou-oots canonical "
        "choice is between), MARKOV (y_lambda, NOT part of that choice), BOTH "
        "(a deliberate comparison or an undeclared straddle), or NAME-ONLY (the "
        "token appears with no construction -- the files a raw grep "
        "over-counts). Purpose is to replace the raw grep count of 43, which "
        "was quoted as a blast radius and is the wrong number for it because "
        "`w_lambda` names several different objects. LIMITS: classification is "
        "by source pattern, so a weight reached through an alias, a factory, or "
        "a witness read at runtime is invisible; every bucket is a LOWER BOUND "
        "on its own membership and NAME-ONLY is a lower bound on 'computes no "
        "weight'. Measured, not complete."
    )

    buckets: dict[str, list[str]] = {
        "PLANCHEREL": [], "MARKOV": [], "BOTH": [], "NAME-ONLY": []}
    # Files the AST provenance pass finds that the regex pass does not. This
    # list IS the measured blindness of the original detector; an empty list
    # would mean the two passes agree, not that either is complete.
    ast_only: dict[str, list[dict]] = {}
    # Files carrying a Plancherel-SHAPED construction that the `w_lambda` name
    # gate never even examines. The 13th blindness mode, and a SCOPE defect
    # rather than a pattern one.
    name_gate_missed: dict[str, list[dict]] = {}
    for f in sorted(ROOT.rglob("*.py")):
        rel = f.relative_to(ROOT).as_posix()
        # Exclude this file. It necessarily contains every pattern it searches
        # for, so it classifies itself BOTH and inflates the answer by one. A
        # self-matching detector is the cheapest kind of false positive and the
        # easiest to miss, since the row looks like all the others.
        if (rel == _Path(__file__).resolve().relative_to(ROOT).as_posix()
                or ("_deprecated" in rel or "fsh-guts" in rel) or "__pycache__" in rel):
            continue
        try:
            text = f.read_text(errors="replace")
        except OSError:
            continue
        # THE NAME GATE IS THE ONE THAT FAILS FIRST, so the AST pass runs BEFORE
        # it and over every file. `two_quark_volume_weighted_clean.py` builds the
        # weight under the name `y_3_sym` and contains the token `w_lambda`
        # nowhere, so under the old ordering it was never EXAMINED -- the
        # provenance repair of PR #6840 could not have helped, because the file
        # never reached it. Scoping a "which files does the ruling move?" audit
        # by a STRING asks which files use a NAME, not which compute the OBJECT.
        hits = ast_planch_hits(text)
        named = bool(NAME.search(text))
        if hits and not named:
            name_gate_missed[rel] = hits
        if not named:
            continue
        buckets[classify(text)].append(rel)
        if hits and not any(rx.search(text) for rx in PLANCH.values()):
            ast_only[rel] = hits

    total = sum(len(v) for v in buckets.values())
    b.add_data("name_gate_missed", {
        "count": len(name_gate_missed),
        "note": "Files carrying a Plancherel-SHAPED d^2/[n]_q! construction "
                "that contain NO `w_lambda`-family token, so the name gate "
                "never examined them at all. The 13th blindness mode, and a "
                "SCOPE defect rather than a pattern one: the PR #6840 "
                "provenance repair could not have helped because these files "
                "never reached it. 🛑 A ROW HERE IS NOT AUTOMATICALLY IN THE "
                "MOLIEN BLAST RADIUS -- do not add this count to the 11 and "
                "quote a total. Two spot-checks show the range: "
                "q_pinning_50_digit.py:169 computes dim_q^2/[n]_q! correctly "
                "and is a real consumer (in the ANCHOR-DEFINING producer), "
                "while mass_endomorphism.py:93 divides by the sum of its own "
                "weights and is therefore already self-normalised dim_q^2/D^2, "
                "which the ruling does not move. Read the construction, and "
                "check `shape_only` first.",
        "files": {k: v for k, v in sorted(name_gate_missed.items())},
    })
    b.add_data("ast_provenance_only", {
        "count": len(ast_only),
        "note": "Files carrying a dim_q^2/<normaliser> construction that the "
                "REGEX pass does not see, found by resolving the local name "
                "back to the function that produced it. This is the measured "
                "blindness of the original detector, whose undercount "
                "(4 of 36) was found by bean qou-wapd and not by this audit. "
                "An empty list would mean the two passes AGREE -- it would not "
                "mean either is complete.",
        "files": {k: v for k, v in sorted(ast_only.items())},
    })
    for k, v in buckets.items():
        b.add_data(f"files_{k.lower().replace('-', '_')}", {
            "count": len(v), "files": v})
    b.add_data("summary", {
        "raw_grep_total": total,
        "planchereL_family_affected_by_the_qou_oots_choice":
            len(buckets["PLANCHEREL"]) + len(buckets["BOTH"]),
        "note": "The second figure is what the qou-oots canonical choice can "
                "move. BOTH is included in it because a file carrying both "
                "families is affected whether it is a deliberate comparison or "
                "a straddle -- which of those it is has NOT been triaged here.",
    })
    # -- How much does the choice actually MOVE a consumer? -------------------
    # A count of affected files says nothing about the size of the effect, and
    # the naive reading here is wrong in a way worth recording. Every reported
    # candidate in `beta_ew_delta_I_321_and_wedderburn.py` is a RATIO of
    # w-weighted quantities at a fixed n = 6, so a lambda-INDEPENDENT rescaling
    # of w cancels exactly. That makes dim_q^2/[n]_q! -> dim_q^2/D^2 a no-op for
    # it: same numerator, constant factor. It does NOT make the Molien option a
    # no-op, because Molien's numerator f^lam*q^{-kappa}*d_q is lambda-DEPENDENT
    # relative to d_q^2 -- so the ratios do not cancel and every candidate moves.
    #
    # Measured at the substrate q0, over the 11 partitions of 6: the ratio
    # w_Molien/w_dimq2, normalised to its own mean, runs 0.156 at the single row
    # (6) to 3.566 at the single column (1^6) -- a spread of 22.88x, monotone in
    # the row/column direction, which is the q^{-kappa} factor doing exactly what
    # it should (kappa = n(lam')-n(lam) is extremal on those two shapes). A 22.9x
    # reweighting is not a perturbation of a hypothesis search; it is a different
    # search.
    ratio_spread = {}
    try:
        from mpmath import mp  # noqa: PLC0415
        from _precision import set_compute_dps, fmt  # noqa: PLC0415
        from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: PLC0415
        _sys.path.insert(0, str(ROOT / "probes"))
        import molien_feray_meliot_bridge_probe as MB  # noqa: PLC0415
        import plancherel_deformation_uniqueness_probe as PU  # noqa: PLC0415
        set_compute_dps()
        q0 = Q_MP
        for nn in (3, 6, 9):
            lams = MB.partitions(nn)
            rs = [MB.molien_weight(q0, lam)
                  / (PU.dim_q(q0, lam) ** 2 / PU.q_factorial(q0, nn))
                  for lam in lams]
            mean = mp.fsum(rs) / len(rs)
            vals = [r / mean for r in rs]
            ratio_spread[str(nn)] = {
                "max_over_min": fmt(max(vals) / min(vals)),
                "at_single_row": fmt(vals[0]),
                "at_single_column": fmt(vals[-1]),
            }
    except Exception as exc:  # pragma: no cover - reported, never swallowed
        ratio_spread = {"error": f"{type(exc).__name__}: {exc}"}
    b.add_data("molien_vs_dimq2_lambda_dependence", {
        "note": "Ratio w_Molien(lam)/w_dimq2(lam) at the substrate q0, "
                "normalised to its own mean over partitions of n. A value of "
                "1.0 everywhere would mean the two families differ by a "
                "lambda-INDEPENDENT constant, and every same-n ratio built from "
                "them would be invariant. They do not: the spread is large and "
                "monotone from the single row to the single column, which is "
                "the q^{-kappa} factor. So consumers whose reported quantities "
                "are same-n ratios -- which is ALL SIX candidates in "
                "beta_ew_delta_I_321_and_wedderburn.py -- are invariant under "
                "dim_q^2/[n]_q! -> dim_q^2/D^2 (same numerator) but are NOT "
                "invariant under the Molien option.",
        "per_n": ratio_spread,
    })

    b.add_assertion(
        "planchereL_subset_is_smaller_than_the_raw_grep",
        computed=str(len(buckets["PLANCHEREL"]) + len(buckets["BOTH"])),
        expected=str(total), tolerance=None,
        source="Files the qou-oots choice can move, vs the raw grep count that "
               "was quoted as the blast radius. These are EXPECTED TO DIFFER -- "
               "the assertion records both numbers side by side rather than "
               "testing equality; read the values, not the pass/fail.",
    )
    b.save()

    if "--selftest" in _sys.argv:
        # The known miss, kept as a live regression rather than as prose. A
        # narrowing of the provenance vocabulary that quietly restored the
        # undercount would pass every other check in this file.
        known = "close_321_weinberg_gap.py"
        src = (ROOT / known).read_text(errors="replace")
        hits = ast_planch_hits(src)
        ok = any(h["family"] == "dimq2_over_qfact" for h in hits)
        regex_saw = any(rx.search(src) for rx in PLANCH.values())
        print(f"selftest: {known} -> AST hits {len(hits)}, "
              f"dimq2_over_qfact {'FOUND' if ok else 'MISSED'}, "
              f"regex pass {'sees it' if regex_saw else 'BLIND (as recorded)'}")
        for h in hits[:4]:
            print(f"    L{h['line']}: {h['source']}   [{h['family']}]")
            print(f"        matched num <- {h['matched_numerator']}")
            print(f"        matched den <- {h['matched_denominator']}")
        if not ok:
            print("SELFTEST FAILED: the known qou-wapd miss is not detected.")
            return 1
        return 0

    print(f"raw grep over live computations/: {total} files")
    for k in ("PLANCHEREL", "BOTH", "MARKOV", "NAME-ONLY"):
        print(f"  {k:11s} {len(buckets[k]):3d}")
    print(f"\n=> the qou-oots choice can move "
          f"{len(buckets['PLANCHEREL']) + len(buckets['BOTH'])} of {total}")
    print("\nPLANCHEREL:")
    for x in buckets["PLANCHEREL"]:
        print("   ", x)
    print("BOTH (comparison or straddle — NOT triaged):")
    for x in buckets["BOTH"]:
        print("   ", x)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
