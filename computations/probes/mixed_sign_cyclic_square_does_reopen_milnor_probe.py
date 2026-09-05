#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles, integer linking numbers and
# degree-2 Magnus coefficients; no q enters anywhere.
"""The cyclic square DOES reopen Milnor -- and the all-positive case I already merged does it.

Beans qou-768r (route 3), qou-2g9j. This CORRECTS THE FRAMING of my own merged
probe `cyclic_square_does_not_reopen_milnor_probe.py` (#6634, 046296ff06).

WHAT THAT PROBE ACTUALLY MEASURED, and it is confirmed here unchanged: inserting the
cyclic square `(g_m g_{m+1})^2` into the canonical atom word spans three distinct
components in 188 of 694 sampled insertions, and in every one of those 188 at least
one pairwise linking number among the three is nonzero -- so `Delta != 0` and `mubar`
is not a genuine integer there. Reproduced here through a SECOND, independently
written `analyse` (the one from `milnor_mubar_vanishes_on_every_triple_probe.py`):
694 tested, 188 spanning, 0 with all three linking numbers zero. Byte-identical.

WHAT IT INFERRED FROM THAT, AND THE INFERENCE IS WRONG. It concluded "route 3's
CONCLUSION does not [break], on this shape", on the reasoning that `Delta != 0` means
`mubar` is "not a genuine integer there anyway". That conflates two different things:

    NOT AN INTEGER   -- true, `mubar` lives in Z/Delta
    NO OBSTRUCTION   -- FALSE, a nonzero RESIDUE is still a nonvanishing invariant

`Delta = 2` with `mubar = 1` is exactly the one bit that route 3's own stated
`Delta = 2` residual is about. That probe never computed `mubar` at all -- it stopped
at `Delta`. Computing it:

    ALL-POSITIVE insertions (the arm that probe tested)   188 spanning   2 nonzero mubar
        4He, position 25, m=5,  lk = [0, -2, 0],  Delta = 2,  mubar = 1
        8Be, position 77, m=17, lk = [0, 0, -2],  Delta = 2,  mubar = 1

So the probe's TITLE over-claims against its OWN scope note, which says plainly that
"the Delta = 2 one-bit triples are untouched". The scope note is the accurate line;
the title and the headline are not. Both are on main.

THE RESIDUAL THAT PROBE NAMED IS ALSO CLOSED HERE, and the same way. Its witness
records: "inserted crossings are all positive. A mixed-sign insertion could cancel a
linking number and is not covered." Sweeping all 16 sign patterns of the four
inserted letters:

    spanning triples (16 patterns x 188)                     3008
      Delta = 0  (all three linking numbers vanish)              0
      Delta = 1                                               2259   ->   0 nonzero
      Delta = 2                                                  5   ->   5 nonzero
      Delta = 3                                                373   -> 187 nonzero
      Delta = 4                                                371   -> 371 nonzero
                                                            TOTAL   -> 563 nonzero

THE JOIN IS SIGN-INDEPENDENT, exactly, and this is the structural half. `span3` is
**188 for every one of the 16 patterns** -- not approximately, identically -- because
the insertion's permutation `s_m s_{m+1} s_m s_{m+1}` is a 3-cycle on
`{m, m+1, m+2}` whatever the signs are. Signs move only the linking VALUES. That is
why `Delta = 0` is never reached in any pattern (the merged probe's measured claim,
now confirmed 16-fold) while `mubar` is nonzero in 563 cases (its inferred claim,
which fails).

WHAT THIS DOES **NOT** DO. It does not refute route 3, and it does not touch
`QOU/Mass/MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean`, both of which are about
the UNPERTURBED derived carrier and about `Delta = 0`. On the unperturbed carrier
`mubar = 0` on every triple -- re-measured here as CONTROL A, 294 triples across the
same four isotopes, 0 nonzero, reproducing #6634. What breaks is the claim that this
particular non-monotone perturbation leaves Milnor with nothing to say.

WHY THE NAIVE LONGITUDE READOFF IS LEGITIMATE. Milnor's `mubar_ijk = eps_ij(lambda_k)`
needs the 0-framed longitude, and reading a longitude straight off a braid word gives
one that differs by a power of the meridian `m_k`. That ambiguity contributes only
`h_k` terms to the Magnus expansion, so the coefficient of `h_i h_j` with `i, j, k`
distinct is framing-independent. This is what makes the readoff usable and is stated
because it is the first objection a referee raises.

CONTROLS, both in the run:
  A  unperturbed base word, 4 isotopes -> 294 triples, 0 nonzero. Reproduces #6634's
     null through a different code path, so a nonzero below is not a harness artifact.
  B  Borromean `[(0,+1),(1,-1)]*3` -> Delta = 0, mubar nonzero. The scanner reports
     nonzero on a known-Brunnian link. (Its value here is -2, the symmetrised sum of
     three eps terms; the merged module records the single eps_01(lambda_2) = -1. What
     the control establishes is NONZERO, not a canonical normalisation.)

SCOPE (a). One insertion shape -- the one sibling #6561 singles out as the only
non-monotone shape yielding a Markov-trace cross term -- at sampled positions across
4 isotopes, on the all-`sigma^-1` base branch, over all 16 inserted-sign patterns. It
is not a theorem, it does not cover other non-monotone words, and the base branch is
not varied. EXPLORATORY; nothing wired.
"""

from __future__ import annotations

import collections
import importlib.util
import itertools
import pathlib
import sys
from itertools import combinations

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

# Reuse the merged machinery rather than reimplementing the longitude/Magnus logic.
# Two copies drifting apart is the more expensive failure, and that module's Borromean
# and Hopf controls are what make these numbers interpretable at all.
_spec = importlib.util.spec_from_file_location(
    "_mubar", HERE / "milnor_mubar_vanishes_on_every_triple_probe.py")
_mubar_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mubar_mod)
analyse = _mubar_mod.analyse
mubar = _mubar_mod.mubar

# The same four isotopes and the same position sampling as the probe being corrected,
# so the all-positive arm is a like-for-like reproduction rather than a new experiment.
ISOTOPES = [(2, 2, "4He"), (3, 3, "6Li"), (4, 4, "8Be"), (5, 5, "10B")]
POSITION_SAMPLES = 8
SIGN_PATTERNS = list(itertools.product([1, -1], repeat=4))
ALL_POSITIVE = (1, 1, 1, 1)


def sweep():
    """Every (isotope, sign pattern, position, generator) insertion, with mubar."""
    per_pattern = {p: {"span3": 0, "nonzero": 0} for p in SIGN_PATTERNS}
    delta_hist = collections.Counter()
    nonzero_by_delta = collections.Counter()
    all_pos_cases = []
    tested = span3 = delta0 = 0

    for (Z, N, name) in ISOTOPES:
        A = Z + N
        n = 3 * A
        base = [(g, -1) for (g, _ct) in atom_canonical_crossings(Z, N)]
        L = len(base)
        step = max(1, L // POSITION_SAMPLES)

        for pat in SIGN_PATTERNS:
            for pos in range(0, L + 1, step):
                for m in range(n - 2):
                    ins = [(m, pat[0]), (m + 1, pat[1]), (m, pat[2]), (m + 1, pat[3])]
                    comp, lam, lk, _mu = analyse(base[:pos] + ins + base[pos:], n)
                    tested += 1
                    spanned = {comp[m], comp[m + 1], comp[m + 2]}
                    if len(spanned) != 3:
                        continue
                    span3 += 1
                    per_pattern[pat]["span3"] += 1
                    a, b, c = sorted(spanned)
                    trip = [lk.get((a, b), 0), lk.get((b, c), 0), lk.get((a, c), 0)]
                    if all(v == 0 for v in trip):
                        delta0 += 1
                    d, v = mubar(lam, comp, lk, a, b, c)
                    delta_hist[d] += 1
                    if v != 0:
                        per_pattern[pat]["nonzero"] += 1
                        nonzero_by_delta[d] += 1
                        if pat == ALL_POSITIVE:
                            all_pos_cases.append({
                                "isotope": name, "insert_position": pos, "generator": m,
                                "pairwise_lk": trip, "Delta": d, "mubar": v,
                            })

    return {
        "insertions_tested": tested,
        "spanning_three_components": span3,
        "with_all_three_linking_zero": delta0,
        "delta_histogram": {str(k): v for k, v in sorted(delta_hist.items())},
        "nonzero_mubar_by_delta": {str(k): v for k, v in sorted(nonzero_by_delta.items())},
        "nonzero_mubar_total": sum(nonzero_by_delta.values()),
        "per_sign_pattern": {str(p): per_pattern[p] for p in SIGN_PATTERNS},
        "all_positive_nonzero_cases": all_pos_cases,
    }


def control_unperturbed():
    """CONTROL A: the merged null, recomputed through this harness."""
    rows = []
    nonzero = triples = 0
    for (Z, N, name) in ISOTOPES:
        n = 3 * (Z + N)
        base = [(g, -1) for (g, _ct) in atom_canonical_crossings(Z, N)]
        comp, lam, lk, mu = analyse(base, n)
        nz = t = 0
        for (a, b, c) in combinations(range(mu), 3):
            _d, v = mubar(lam, comp, lk, a, b, c)
            t += 1
            if v != 0:
                nz += 1
        rows.append({"isotope": name, "components": mu, "triples": t, "nonzero_mubar": nz})
        triples += t
        nonzero += nz
    return {"rows": rows, "triples": triples, "nonzero_mubar": nonzero}


def control_borromean():
    """CONTROL B: the scanner reports nonzero on a known-Brunnian link."""
    comp, lam, lk, mu = analyse([(0, 1), (1, -1)] * 3, 3)
    if mu != 3:
        return {"components": mu, "usable": False}
    d, v = mubar(lam, comp, lk, 0, 1, 2)
    return {"components": mu, "Delta": d, "mubar": v, "nonzero": v != 0}


def main() -> int:
    res = sweep()
    ctl_a = control_unperturbed()
    ctl_b = control_borromean()

    ap = res["per_sign_pattern"][str(ALL_POSITIVE)]

    b = WitnessBuilder(
        name="mixed-sign-cyclic-square-does-reopen-milnor",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. CORRECTS THE FRAMING of my own merged probe "
        "cyclic_square_does_not_reopen_milnor_probe.py (#6634). That probe measured that "
        "the cyclic-square insertion never drives all three pairwise linking numbers to "
        "zero -- confirmed here, 0 of 3008 spanning cases across all 16 inserted-sign "
        "patterns -- and inferred from it that route 3's conclusion survives, on the "
        "grounds that Delta != 0 makes mubar 'not a genuine integer'. That conflates "
        "'not an integer' with 'no obstruction': mubar lives in Z/Delta and a NONZERO "
        "RESIDUE is still a nonvanishing invariant. It never computed mubar. Computing "
        "it: 563 of 3008 spanning triples carry nonzero mubar (Delta=2: 5, Delta=3: 187, "
        "Delta=4: 371) -- and 2 of those are in that probe's OWN all-positive arm, at "
        "Delta = 2 with mubar = 1, which is precisely the one bit route 3's stated "
        "Delta = 2 residual is about. The probe's title therefore over-claims against its "
        "own scope note, which says plainly that the Delta = 2 triples are untouched. "
        "STRUCTURAL HALF: the join is sign-independent -- span3 is 188 for every one of "
        "the 16 patterns, identically, because the insertion's permutation is a 3-cycle "
        "whatever the signs; signs move only the linking VALUES. This does NOT refute "
        "route 3 or its Lean, both of which concern the UNPERTURBED carrier at Delta = 0 "
        "(control A re-measures that null: 294 triples, 0 nonzero). Scope (a): one "
        "insertion shape, one base branch, sampled positions, 4 isotopes. Nothing wired."
    )

    b.add_data("what_is_being_corrected", {
        "target": "computations/probes/cyclic_square_does_not_reopen_milnor_probe.py (#6634, 046296ff06)",
        "its_measurement_CONFIRMED": ("the insertion spans 3 components in 188 of 694 "
                                      "all-positive insertions and never drives all three "
                                      "pairwise linking numbers to zero -- reproduced here "
                                      "through a second, independently written analyse()"),
        "its_inference_REFUTED": ("'Delta != 0, so mubar is not a genuine integer there "
                                  "anyway' does not give 'no obstruction'. mubar lives in "
                                  "Z/Delta; a nonzero residue is a nonvanishing invariant, "
                                  "and Delta = 2 with mubar = 1 IS route 3's one bit"),
        "it_never_computed_mubar": True,
        "its_own_scope_note_was_right": ("that probe's witness already says 'the Delta = 2 "
                                         "one-bit triples are untouched'. The scope note is "
                                         "accurate; the title and headline are not"),
    })
    b.add_data("measured", res)
    b.add_data("the_all_positive_arm", {
        "why_it_matters": ("this is the arm the merged probe itself tested, so these are a "
                           "correction rather than a new regime"),
        "spanning": ap["span3"], "nonzero_mubar": ap["nonzero"],
        "cases": res["all_positive_nonzero_cases"],
    })
    b.add_data("the_join_is_sign_independent", {
        "span3_per_pattern_distinct_values": sorted(
            {v["span3"] for v in res["per_sign_pattern"].values()}),
        "reason": ("the insertion's permutation s_m s_{m+1} s_m s_{m+1} is a 3-cycle on "
                   "{m, m+1, m+2} for every sign choice, so WHICH components are joined "
                   "cannot depend on the signs -- only the linking VALUES can move"),
        "consequence": ("Delta = 0 is unreachable in every pattern (the merged probe's "
                        "measured claim, extended 16-fold) while mubar is nonzero in 563 "
                        "cases (its inferred claim, which fails)"),
    })
    b.add_data("control_A_unperturbed_reproduces_the_merged_null", ctl_a)
    b.add_data("control_B_borromean", dict(ctl_b, note=(
        "the merged module records the single eps_01(lambda_2) = -1; the full symmetrised "
        "mubar here is -2. What this control establishes is NONZERO, not a canonical "
        "normalisation")))
    b.add_data("why_the_naive_longitude_readoff_is_legitimate", {
        "objection": ("Milnor's mubar_ijk = eps_ij(lambda_k) needs the 0-framed longitude; "
                      "reading one off a braid word gives a longitude differing by a power "
                      "of the meridian m_k"),
        "answer": ("that ambiguity contributes only h_k terms to the Magnus expansion, so "
                   "the coefficient of h_i h_j with i, j, k distinct is framing-independent"),
    })
    b.add_data("what_this_does_NOT_do", {
        "route_3": ("NOT refuted. Route 3 and MilnorTriplesAreDefinedExactlyWhereTheyVanish"
                    ".lean are about the UNPERTURBED carrier at Delta = 0; control A "
                    "re-measures that null"),
        "the_lean": "unchanged -- no hypothesis of it is touched",
        "other_non_monotone_words": ("NOT tested. One shape only -- the one #6561 singles "
                                     "out as the sole non-monotone shape yielding a "
                                     "Markov-trace cross term"),
        "base_branch": ("all-sigma^-1 only. The base sign is not varied; the residual being "
                        "closed here is the INSERTED signs"),
    })

    b.add_assertion(
        name="the_all_positive_arm_DOES_carry_nonzero_mubar",
        computed="1" if ap["nonzero"] > 0 else "0", expected="1", tolerance="0", unit="bool",
        source=(f"{ap['nonzero']} of {ap['span3']} spanning insertions, at Delta = 2 with "
                "mubar = 1. This is the merged probe's own arm, which is what makes it a "
                "correction rather than a new measurement."),
    )
    b.add_assertion(
        name="Delta_zero_is_never_reached_in_ANY_sign_pattern",
        computed=str(res["with_all_three_linking_zero"]), expected="0", tolerance="0",
        unit="insertions",
        source=(f"over {res['spanning_three_components']} spanning insertions. Confirms and "
                "extends 16-fold the merged probe's MEASURED claim -- it is the inference "
                "drawn from it, not the measurement, that fails."),
    )
    b.add_assertion(
        name="the_join_is_sign_independent",
        computed=str(len({v["span3"] for v in res["per_sign_pattern"].values()})),
        expected="1", tolerance="0", unit="distinct span3 counts",
        source=("all 16 sign patterns give the identical spanning count, because the "
                "insertion's permutation is a 3-cycle regardless of signs."),
    )
    b.add_assertion(
        name="CONTROL_A_unperturbed_carrier_gives_NO_nonzero_mubar",
        computed=str(ctl_a["nonzero_mubar"]), expected="0", tolerance="0", unit="triples",
        source=(f"{ctl_a['triples']} triples over the same 4 isotopes, reproducing #6634's "
                "null through this harness. Without it the nonzero counts above would be "
                "indistinguishable from a harness artifact."),
    )
    b.add_assertion(
        name="CONTROL_B_scanner_reports_nonzero_on_the_Borromean_link",
        computed="1" if ctl_b.get("nonzero") else "0", expected="1", tolerance="0",
        unit="bool",
        source=("the second direction of the same guard: a scanner that never reports "
                "nonzero would pass control A trivially."),
    )

    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Inputs are braid words, their closures' permutation cycles, "
            "integer linking numbers and degree-2 Magnus coefficients. No substrate pin "
            "is evaluated on any path."
        ),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
