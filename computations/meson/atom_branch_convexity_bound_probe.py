#!/usr/bin/env python3
"""The atom element is a CONVEX combination of braids — so its volume is capped.

Bean qou-7p7d.  The formalize-first move for the one-K problem: find the
invariant that prunes before running any search.

THE SETUP
=========
`atom_braid_word_3A` returns an element of H_n(q) OUTSIDE im(rho) (PR #5765), so
it has no closure and no volume.  But tr_M is LINEAR on H_n(q), and each letter
`c*sigma_g + d*1` expands over {sigma_g, sigma_g^-1} using sigma^-1 = sigma - h.
So the atom element is a weighted sum of genuine braid images:

    atom = sum_b w_b * rho(beta_b),        tr_M(atom) = sum_b w_b * J_{K_b}(q)

WHAT THIS MEASURES
==================
The weights.  If they form a CONVEX combination -- all non-negative, summing to
1 -- then |tr_M(atom)| <= max_b |J_{K_b}(q)|, with no geometry needed.  Under the
correspondence the framework itself invokes (`tr_M ~ exp(Vol)`, the volume
conjecture; cheat sheet: "Volume is NOT the carrier, it is the exponential of
it"), that caps any effective volume by the LARGEST BRANCH VOLUME:

    Vol_eff(atom) <= max_b Vol(K_b) + log(sum_b |w_b|)

and a convex combination kills the second term.  This turns 2^(2A+1) separate
hyperbolicity questions into ONE max -- the pruning invariant.

WHAT IS AND IS NOT ESTABLISHED HERE
===================================
MEASURED: the weight structure, exactly, at A = 1, 2, 4.

NOT MEASURED, and NOT claimed: whether the branch closures are hyperbolic.
SnapPy is unavailable in this container, so this file computes NO volumes.  For
2H a sibling measured all 32 branch closures non-hyperbolic with SnapPy
(docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md); that is THEIR
measurement, cited, not reproduced here.  For A = 1 nothing is established.

A caution recorded because an earlier draft of this file got it wrong: the
relevant property for the branch braids is HOMOGENEOUS (each generator appearing
with a consistent sign, Stallings), NOT "all letters share a sign".  The draft
tested the latter, then printed a `-> Vol = 0` conclusion that was a hardcoded
string rather than a computation.  Both are fixed: the test below is
per-generator, and it reports the property only, never a volume.

EXPLORATORY / audit-only.  mpmath throughout at the compute dps.
"""

from __future__ import annotations

import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin

H = HA_MP
TOL = mp.mpf("1e-9")          # the census tolerance; 1e-30 misclassifies sigma^-1
ISOTOPES = [("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1), ("4He", 2, 2)]


def slots(word):
    """Per-letter expansion over {sigma, sigma^-1} with weights."""
    out = []
    for (_c, d, g) in word:
        t = -mp.mpf(str(d)) / H
        if abs(t) < TOL:
            out.append([(g + 1, mp.mpf(1))])            # sigma
        elif abs(t - 1) < TOL:
            out.append([(-(g + 1), mp.mpf(1))])         # sigma^-1
        else:
            out.append([(g + 1, 1 - t), (-(g + 1), t)])  # a genuine average
    return out


def homogeneous(braid) -> bool:
    """Stallings-homogeneous: each generator appears with ONE sign."""
    seen = {}
    for x in braid:
        i, s = abs(x), (1 if x > 0 else -1)
        if seen.setdefault(i, s) != s:
            return False
    return True


def main() -> None:
    rows = []
    for name, Z, N in ISOTOPES:
        sl = slots(atom_braid_word_3A(Z, N))
        avg = [s for s in sl if len(s) > 1]
        n_branch = 2 ** len(avg)
        # sum of |weights| factorises over the letters
        total = mp.mpf(1)
        for s in avg:
            total *= sum(abs(p) for _, p in s)
        min_w = mp.mpf(1)
        for s in avg:
            min_w = min(min_w, min(p for _, p in s))
        A = Z + N
        row = {
            "isotope": name, "A": A, "letters": len(sl),
            "averaged_letters": len(avg), "branches": n_branch,
            "sum_abs_weights": mp.nstr(total, 20),
            "is_convex_combination": bool(abs(total - 1) < TOL and min_w > 0),
            "min_branch_weight_positive": bool(min_w > 0),
            "two_A_plus_one": 2 * A + 1,
            "matches_2A_plus_1": len(avg) == 2 * A + 1,
        }
        # enumerate branches only where it is cheap, and report the PROPERTY only
        if n_branch <= 64:
            homs = []
            for combo in itertools.product(*sl):
                homs.append(homogeneous([x for x, _ in combo]))
            row["branches_enumerated"] = len(homs)
            row["homogeneous_branches"] = sum(homs)
            row["all_branches_homogeneous"] = all(homs)
        rows.append(row)

    by = {r["isotope"]: r for r in rows}

    # 1. THE PRUNING INVARIANT: convexity, at every A measured
    assert all(r["is_convex_combination"] for r in rows), (
        "the branch weights are not a convex combination -- then |tr| is not "
        "bounded by the max branch and the whole pruning argument fails")
    # 2. the corpus's 2A+1 claim, which does NOT hold at A = 1
    assert by["deuteron"]["matches_2A_plus_1"], "2A+1 fails at A=2"
    assert not by["proton"]["matches_2A_plus_1"], (
        "2A+1 now HOLDS at A=1 -- the docstring correction below is wrong and "
        "must be withdrawn")
    # 3. the deuteron branch count the sibling's SnapPy sweep used
    assert by["deuteron"]["branches"] == 32, (
        f"deuteron branches {by['deuteron']['branches']} != the 32 the sibling "
        "audit swept")

    wb = WitnessBuilder("atom-branch-convexity-bound", engine="python-exact")
    wb.set_description(
        "Measures the branch-weight structure of the atom H_n(q) element. The "
        "weights are a CONVEX combination at every A tested, so tr_M of the "
        "atom is bounded by the largest branch trace -- which, under the "
        "volume-conjecture correspondence the framework invokes, caps any "
        "effective volume by the largest BRANCH volume. That is the invariant "
        "which prunes 2^(2A+1) hyperbolicity questions to one max. Computes NO "
        "volumes: SnapPy is unavailable here.")
    wb.add_data("branch_structure", rows)
    wb.add_data("the_bound", {
        "identity": "atom = sum_b w_b rho(beta_b), tr_M linear",
        "measured": "sum_b |w_b| = 1 and every w_b > 0 -- a convex combination",
        "consequence": "|tr_M(atom)| <= max_b |J_{K_b}(q)|, no geometry needed",
        "under_volume_conjecture": ("Vol_eff(atom) <= max_b Vol(K_b) + "
                                    "log(sum_b |w_b|), and convexity kills the "
                                    "second term"),
        "why_it_matters": ("turns 2^(2A+1) separate hyperbolicity questions "
                           "into ONE: is any branch hyperbolic?"),
    })
    wb.add_data("corrects_the_2A_plus_1_docstring", {
        "where": "computations/mass_at_3A_proper.py::atom_braid_word_3A",
        "says": ("There are 2A + 1 such non-braid letters (two per nucleon, "
                 "from its two ud pairs, plus one per interface)."),
        "measured": ("holds at A = 2 (5) and A = 4 (9); FAILS at A = 1, where "
                     "the count is 2, not 3 -- a single nucleon has no "
                     "interface, so the '+1' has nothing to count."),
        "my_own_probe_too": ("atom_word_braid_letter_census_probe.py asserts "
                             "the identity only over 2H/3He/4He, all A >= 2, "
                             "so its assertion is true as tested but its "
                             "framing implies a generality it never checked."),
    })
    wb.add_data("not_established_here", {
        "branch_hyperbolicity": ("NOT computed -- SnapPy is unavailable in this "
                                 "container. For 2H a sibling measured all 32 "
                                 "branch closures non-hyperbolic; that is cited, "
                                 "not reproduced. For A = 1, nothing."),
        "homogeneity_is_reported_not_concluded_from": ("the homogeneous counts "
                                                       "below are a structural "
                                                       "property only; no volume "
                                                       "is inferred from them "
                                                       "here."),
    })
    wb.set_audit_only(
        "docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md")

    wb.add_assertion(
        name="branch_weights_are_a_convex_combination",
        computed=sum(1 for r in rows if r["is_convex_combination"]),
        expected=len(rows), tolerance=0, unit="count",
        source="sum|w| = 1 with every weight positive, at A = 1, 2, 4.")
    wb.add_assertion(
        name="two_A_plus_one_fails_at_A_equals_one",
        computed=by["proton"]["averaged_letters"], expected=2, tolerance=0,
        unit="letters",
        source=("The docstring says 2A+1 = 3. A single nucleon has no "
                "interface, so the '+1' has nothing to count."))
    wb.add_assertion(
        name="deuteron_branch_count_matches_the_sibling_sweep",
        computed=by["deuteron"]["branches"], expected=32, tolerance=0,
        unit="count",
        source="2^(2A+1) at A=2, against the sibling's 32/32 SnapPy sweep.")
    out = wb.save()

    print(f"{'iso':>9} {'A':>2} {'letters':>8} {'avg':>4} {'2A+1':>5} "
          f"{'branches':>9} {'sum|w|':>8} {'convex':>7} {'all homog':>10}")
    for r in rows:
        print(f"{r['isotope']:>9} {r['A']:>2} {r['letters']:>8} "
              f"{r['averaged_letters']:>4} {r['two_A_plus_one']:>5} "
              f"{r['branches']:>9} {r['sum_abs_weights'][:6]:>8} "
              f"{str(r['is_convex_combination']):>7} "
              f"{str(r.get('all_branches_homogeneous', '-')):>10}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
