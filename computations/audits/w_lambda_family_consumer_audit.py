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
"""

from __future__ import annotations

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


def classify(text: str) -> str:
    p = any(rx.search(text) for rx in PLANCH.values())
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
    for f in sorted(ROOT.rglob("*.py")):
        rel = f.relative_to(ROOT).as_posix()
        # Exclude this file. It necessarily contains every pattern it searches
        # for, so it classifies itself BOTH and inflates the answer by one. A
        # self-matching detector is the cheapest kind of false positive and the
        # easiest to miss, since the row looks like all the others.
        if (rel == _Path(__file__).resolve().relative_to(ROOT).as_posix()
                or "_deprecated" in rel or "__pycache__" in rel):
            continue
        try:
            text = f.read_text(errors="replace")
        except OSError:
            continue
        if not NAME.search(text):
            continue
        buckets[classify(text)].append(rel)

    total = sum(len(v) for v in buckets.values())
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
        from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: PLC0415
        _sys.path.insert(0, str(ROOT / "probes"))
        import molien_feray_meliot_bridge_probe as MB  # noqa: PLC0415
        import plancherel_deformation_uniqueness_probe as PU  # noqa: PLC0415
        set_compute_dps()
        q0 = mp.mpf(Q_50_DIGIT_STR)
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
