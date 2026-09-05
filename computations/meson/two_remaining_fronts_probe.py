#!/usr/bin/env python3
"""The two fronts left after Addendum 22, worked. One closes; one does not.

Bean qou-6tcn. Addendum 22 closed the fixed-width cut entropy by a Lean-proved
invariant and named exactly two things it did NOT touch. Both are worked here.

FRONT 1 -- a cut whose WIDTH GROWS with A.  OPEN, and genuinely different.
=========================================================================
The Markov property that made the fixed-width entropy constant also gives the
growing case for free: the marginal on the first k strands IS the k-strand
Markov measure, so

    S(k) = - sum_{mu |- k, ell(mu) <= 2}  f^mu y^{(k)}_mu ln y^{(k)}_mu

with no Littlewood-Richardson needed.  Measured, this is a **VOLUME law**:

    S(k)/k  ->  ln [2]_q = 0.6985808...    (k = 24 .. 768)
    S(k)    =   k ln[2]_q - c + o(1)

i.e. an entropy density of exactly one `ln [2]_q` per strand -- the log of the
fundamental's quantum dimension, which is what a strand carries. So unlike the
fixed-width case this quantity IS extensive, and Addendum 22's theorem does not
reach it. That escape is real.

**But it does not match, and the reason it cannot be made to is instructive.**
For the balanced cut k = floor(3A/2):

    iso   A    E0*S(k)     B_AME      ratio     E0*S/A     B/A
    2H    2     4.3363     2.2246    1.9493x     2.1682   1.1123
    3H    3     6.8866     8.4818    0.8119x     2.2955   2.8273
    4He   4    11.9036    28.2957    0.4207x     2.9759   7.0739
    6Li   6    19.7479    31.9940    0.6172x     3.2913   5.3323
    12C  12    44.4404    92.1617    0.4822x     3.7034   7.6801
    16O  16    61.2108   127.6193    0.4796x     3.8257   7.9762

The ratio is not constant (4.63x over these, against 17.64x for the fixed cut),
and it settles near 0.48 -- an undershoot of about 2.1x. Asymptotically a cut
growing at `w` strands per nucleon gives `E_0 w ln[2]_q` per nucleon, so the
balanced choice `w = 1.5` yields 4.386 MeV/nucleon against an empirical
approach to ~8 MeV/nucleon.

**`w` is a free parameter, and that is the whole problem.** Matching would fix
`w ~ 2.9`, which is not derived from anything -- and at `w = 3`, the whole
nucleon, the cut is the entire system and the entropy is identically zero. So
this front is open in the sense that the OBJECT is extensive, and closed in the
sense that nothing in the framework selects the cut. Choosing `w` to match is a
fit, and is not done here.

FRONT 2 -- is `tr_M(beta_D)` reachable?  CLOSED, scope (b).
===========================================================
Addendum 21 established that even a perfectly concentrated cost needs
`tr_M(beta_D) >= sqrt(B_AME) = 1.491498`, against the measured 0.575172 -- a
factor 2.59. The corpus already proves the bound that settles this:
`atom-branch-convexity-bound` shows the atom is a CONVEX combination of its
branch closures (`sum_b |w_b| = 1`, every `w_b > 0`), so

    tr_M(atom) = sum_b w_b tr_M(beta_b)  <=  max_b tr_M(beta_b).

Measured over all 32 deuteron branches:

    min_b tr_M = 0.291552        max_b tr_M = 1.018275
    required   = 1.491498        max / required = 0.6827

**No reweighting of the branches reaches it.** And the ceiling is quadratic, so
even AT the convex maximum the best attainable objective is
`(max_b tr_M)^2 = 1.036884` against `B_AME = 2.224566` -- still **2.15x short**.

That is scope (b): the invariant is the convexity of the branch decomposition,
proved in the corpus and not fitted. It excludes reaching AME by any
redistribution over the branches of THIS word. It does NOT exclude a different
braid word, and says nothing about whether one exists or is derivable.

SCOPE -- (a) for front 1, (b) for front 2
=========================================
NOT claimed: that the growing cut IS the binding energy or appears in any
binding formula; that any value of `w` is correct; that a braid word with a
larger trace does not exist. Nothing here computes a binding contribution.

PRECISION NOTE
==============
Front 1 is exact (mpmath from the closed form; no LR, no float64). Front 2's
branch traces come through `binding_k_solver.per_block_evaluation`, which is
float64 -- so the branch control reproduces the committed `tr_M(atom)` to ~1e-9,
not exactly. The verdict turns on a 47 % gap, far above that resolution.
"""

from __future__ import annotations

import itertools
import pathlib
import sys
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
import binding_k_solver as bks  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    M_E_MEV,
    ame_binding_mev  # noqa: E402,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import HA_MP, Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 50)

Q = Q_MP
E0 = mp.mpf(str(M_E_MEV)) / (Q * (Q - 1))
H = HA_MP
TOL = mp.mpf("1e-9")
SUPPORT6 = [(6,), (5, 1), (4, 2), (3, 3)]


def hook_dim(lam):
    lam = tuple(x for x in lam if x)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def markov_weight(lam, k):
    j = lam[1] if len(lam) > 1 else 0
    return qint(k - 2 * j + 1) / qint(2) ** k


def S(k):
    """Entropy of the k-strand convention-D Markov measure = the k-strand
    marginal, by the Markov property.  Exact; no LR, no float64."""
    s = mp.mpf(0)
    for j in range(0, k // 2 + 1):
        lam = (k - j, j) if j else (k,)
        y = markov_weight(lam, k)
        if y > 0:
            s -= hook_dim(lam) * y * mp.log(y)
    return s


def slots(word):
    out = []
    for (_c, d, g) in word:
        t = -mp.mpf(str(d)) / H
        if abs(t) < TOL:
            out.append([(g + 1, mp.mpf(1))])
        elif abs(t - 1) < TOL:
            out.append([(-(g + 1), mp.mpf(1))])
        else:
            out.append([(g + 1, 1 - t), (-(g + 1), t)])
    return out


def main() -> int:
    wb = WitnessBuilder("two-remaining-fronts", engine="python-exact")
    wb.set_description(
        "Works the two fronts Addendum 22's theorem did not touch. FRONT 1, a "
        "growing-width cut: genuinely extensive, S(k) = k ln[2]_q - c, a volume "
        "law -- so the escape is real, but the cut width per nucleon is a free "
        "parameter and the balanced choice undershoots ~2.1x with a "
        "non-constant ratio. FRONT 2, whether tr_M can be 2.59x larger: CLOSED "
        "scope (b) by the corpus's proved convexity bound -- max over the 32 "
        "deuteron branches is 1.018275 against a required 1.491498, and even at "
        "the convex maximum the objective is 2.15x short.")

    ln2q = mp.log(qint(2))

    # ── FRONT 1 ───────────────────────────────────────────────────────────
    dens = {k: S(k) / k for k in (24, 96, 384, 768)}
    s3 = S(3)
    iso = [("2H", 1, 2), ("3H", 1, 3), ("3He", 2, 3), ("4He", 2, 4),
           ("6Li", 3, 6), ("7Li", 3, 7), ("12C", 6, 12), ("16O", 8, 16)]
    rows1, ratios = [], []
    for name, Z, A in iso:
        k = (3 * A) // 2
        s = S(k)
        B = ame_binding_mev(Z, A)
        r = E0 * s / B
        ratios.append(r)
        rows1.append({"isotope": name, "A": A, "k": k,
                      "S_k": mp.nstr(s, 20),
                      "E0_S_MeV": mp.nstr(E0 * s, 20),
                      "B_AME_MeV": mp.nstr(B, 20),
                      "ratio": mp.nstr(r, 20)})
    spread1 = max(ratios) / min(ratios)
    per_nucleon = E0 * mp.mpf("1.5") * ln2q

    # ── FRONT 2 ───────────────────────────────────────────────────────────
    sl = slots(atom_braid_word_3A(1, 1))
    y6 = {l: markov_weight(l, 6) for l in SUPPORT6}

    def trM(braid):
        pb = bks.per_block_evaluation(braid, 6, q=float(Q))["per_block"]
        tot = mp.mpf(0)
        for l in SUPPORT6:
            key = next(k for k in pb if tuple(k) == l or str(k) == str(l))
            chi = pb[key]["chi"]
            tot += y6[l] * mp.mpf(str(getattr(chi, "real", chi)))
        return tot

    vals, weighted = [], mp.mpf(0)
    for combo in itertools.product(*sl):
        w = mp.mpf(1)
        for _, wt in combo:
            w *= wt
        t = trM([g for g, _ in combo])
        vals.append(t)
        weighted += w * t
    max_b, min_b = max(vals), min(vals)
    committed = mp.mpf("0.5751722457697739")
    need = mp.sqrt(AME_B_DEUTERON_MEV_VALIDATION)
    reach = max_b / need
    ceil_at_max = max_b ** 2 / AME_B_DEUTERON_MEV_VALIDATION

    print(f"FRONT 1  ln[2]_q = {mp.nstr(ln2q, 12)}")
    for k, d in dens.items():
        print(f"   S({k})/{k} = {mp.nstr(d, 12)}")
    print(f"   balanced-cut ratio spread: {mp.nstr(spread1, 8)}x")
    print(f"   asymptotic E0*S/A = {mp.nstr(per_nucleon, 8)} MeV/nucleon\n")
    print(f"FRONT 2  branches {len(vals)}   min {mp.nstr(min_b, 10)}   "
          f"max {mp.nstr(max_b, 10)}")
    print(f"   required {mp.nstr(need, 10)}   max/required "
          f"{mp.nstr(reach, 8)}  -> NOT reachable")
    print(f"   objective even at the convex max: "
          f"{mp.nstr(ceil_at_max, 8)} of AME")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — FRONT 1: a volume law. Density approaches ln[2]_q from below.
    wb.add_assertion(
        name="growing_cut_entropy_density_approaches_ln_two_q",
        computed=mp.nstr(dens[768], 20), expected="0.6843894655",
        tolerance="1e-6", unit="nats per strand",
        source="S(768)/768; the limit is ln[2]_q = 0.6985808249")
    wb.add_assertion(
        name="control_density_is_bounded_by_ln_two_q",
        computed=repr(bool(all(d < ln2q for d in dens.values()))),
        expected="True", tolerance="0", unit="boolean",
        source="S(k)/k < ln[2]_q at k = 24, 96, 384, 768")

    # A2 — CONTROL tying this to the fixed-width probe: S(3) is that number.
    wb.add_assertion(
        name="control_S3_reproduces_the_fixed_width_result",
        computed=mp.nstr(s3, 20), expected="1.0359164340",
        tolerance="1e-9", unit="nats",
        source="cut_entropy_is_A_independent_probe reported 1.0359164340")

    # A3 — but the balanced cut does not track binding.
    wb.add_assertion(
        name="balanced_cut_ratio_is_not_constant",
        computed=mp.nstr(spread1, 20), expected="4.6338",
        tolerance="1e-3", unit="ratio",
        source="max/min of E_0*S(k)/B_AME over 2H..16O")

    # A4 — FRONT 2, THE RESULT: the convex maximum falls short.
    wb.add_assertion(
        name="ame_not_reachable_by_branch_reweighting",
        computed=mp.nstr(reach, 20), expected="0.68272",
        tolerance="1e-4", unit="ratio",
        source="max_b tr_M(beta_b) / sqrt(B_AME); < 1 means unreachable")

    # A5 — and quadratically so: even at the max the objective is short.
    wb.add_assertion(
        name="objective_short_even_at_the_convex_maximum",
        computed=mp.nstr(ceil_at_max, 20), expected="0.46611",
        tolerance="1e-4", unit="fraction of B_AME",
        source="(max_b tr_M)^2 / B_AME")

    # A6 — CONTROL: the convex decomposition is the committed atom. Without
    #      this, max_b would be about some other object entirely.
    wb.add_assertion(
        name="control_branch_average_reproduces_committed_trace",
        computed=mp.nstr(abs(weighted - committed), 20), expected="0",
        tolerance="1e-7", unit="dimensionless",
        source="sum_b w_b tr_M(beta_b) vs deuteron-real-sdp n_target "
               "(per_block_evaluation is float64)")

    # A7 — CONTROL: 32 branches, matching the committed convexity witness.
    wb.add_assertion(
        name="control_branch_count",
        computed=str(len(vals)), expected="32", tolerance="0", unit="count",
        source="atom-branch-convexity-bound deuteron branch count")

    # A8 — CONTROL against the vacuous reading "every branch is small": the
    #      branches genuinely spread, and the max is well above the atom's own.
    wb.add_assertion(
        name="control_branch_traces_spread_above_the_atom",
        computed=mp.nstr(max_b / committed, 20), expected="1.7704",
        tolerance="1e-3", unit="ratio",
        source="max_b tr_M / tr_M(atom); > 1 so the bound is not trivial")

    wb.add_data("front1_ln_two_q", mp.nstr(ln2q, 30))
    wb.add_data("front1_density", {str(k): mp.nstr(v, 24)
                                   for k, v in dens.items()})
    wb.add_data("front1_rows", rows1)
    wb.add_data("front1_asymptotic_MeV_per_nucleon", mp.nstr(per_nucleon, 24))
    wb.add_data("front2_branch_count", len(vals))
    wb.add_data("front2_min_branch_trace", mp.nstr(min_b, 24))
    wb.add_data("front2_max_branch_trace", mp.nstr(max_b, 24))
    wb.add_data("front2_required_trace", mp.nstr(need, 24))
    wb.add_caveat(
        "FRONT 1 is scope (a) and stays OPEN: the growing-width cut is a "
        "genuine volume law and Addendum 22's theorem does not reach it. But "
        "the cut width per nucleon is a FREE PARAMETER -- matching would fix "
        "w ~ 2.9, which nothing derives, and at w = 3 the cut is the whole "
        "system and the entropy is identically zero. No w is chosen here.")
    wb.add_caveat(
        "FRONT 2 is scope (b): the invariant is the convexity of the branch "
        "decomposition, proved in the corpus (atom-branch-convexity-bound) and "
        "not fitted. It excludes reaching AME by any redistribution over the "
        "branches of THIS braid word. It does NOT exclude a different word, and "
        "says nothing about whether one exists or is derivable.")
    wb.add_caveat(
        "Front 1 is exact mpmath from the closed form. Front 2's branch traces "
        "go through binding_k_solver.per_block_evaluation, which is float64, so "
        "the branch control reproduces the committed trace to ~1e-9 rather than "
        "exactly. The verdict turns on a 47 % gap, far above that resolution.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
