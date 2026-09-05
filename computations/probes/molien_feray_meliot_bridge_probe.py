#!/usr/bin/env python3
"""Is the corpus's Molien weight the SAME OBJECT as Feray-Meliot's `M_{n,q}`?

Bean `qou-j7ef`. This is the load-bearing question for rehoming
`prop:q-plancherel-asymptotic-skeleton`: clause 2 cites `feray2010`, whose
theorems are stated for `M_{n,q}`, while the block pushes forward
`w_lambda = dim_q^2/[n]_q!`. Those two are NOT one normalisation apart, so the
citation does not transfer. The proposed repair is to restate the skeleton
over the family that Feray-Meliot actually proved it for -- but only if the
corpus already HAS that family under another name.

A NOTE ON THE ARGUMENT, because it changes a number already in the corpus.
`prop:q-plancherel-asymptotic-skeleton` records the w-vs-M separation as
`0.158/0.320/0.575/0.951/3.53/12.6` at n = 3,4,5,6,9,12. That is M evaluated at
`Q = q0` -- the raw Definition-1 argument. But the family the corpus actually
holds is `M_{n,q0^2}` (that is the whole content of T1 below), and the
separation from THAT is `0.368/0.870/1.84/3.78/41.8/978`. Both are measured
here (T5) and both are reported, because the earlier figure is not wrong about
its own quantity -- it is just not the distance to the object in the corpus.
The conclusion is unchanged and strengthened: 12.6 already ruled out a
rescaling, 978 rules it out by two more orders of magnitude.

It does. Feray-Meliot Definition 1 (asymmetric q-integers {k}_Q = (Q^k-1)/(Q-1)):

    M_{n,Q}(lam) = Q^{b(lam)} * f^lam / prod_{x in lam} {h(x)}_Q,   b(lam) = n(lam)

The corpus's Molien / fake-degree weight (Lean `MolienFakeDegreeGeneralN.molienSum`,
balanced q-integers [k] = (q^k - q^-k)/(q - q^-1)):

    Mol_n(lam) = f^lam * q^{-kappa_lam} * dim_q(lam) / [n]_q!,   kappa_lam = contentSum(lam)

CLAIM UNDER TEST:  Mol_n(lam)  ==  M_{n,q^2}(lam)   for every lam and every q.

The algebra, so a reader can check the test rather than trust it. With Q = q^2,
{k}_Q = (q^2k - 1)/(q^2 - 1) = q^{k-1}[k]_q, so

    prod_x {h(x)}_Q = q^{(sum_x h) - n} * prod_x [h(x)]_q,
    dim_q(lam)      = [n]_q! / prod_x [h(x)]_q        (q-hook-length formula)

hence  M_{n,q^2}(lam) = q^{2 n(lam) - sum_x h(x) + n} * f^lam * dim_q(lam) / [n]_q!.
The exponent collapses by the standard hook identity sum_x h(x) = n(lam) + n(lam') + n:

    2 n(lam) - (n(lam) + n(lam') + n) + n  =  n(lam) - n(lam')  =  -contentSum(lam)

since contentSum(lam) = sum_x (j - i) = n(lam') - n(lam). So the corpus's kappa is
forced -- it is not a convention someone picked, it is what the Q = q^2 substitution
produces.

WHY THIS IS TESTED AND NOT ASSERTED. Every step above is one I could have got
backwards, and two of them have a sign I have personally inverted before in this
arc (bean qou-7o7h recorded a scaling law tested upside down). So the test is:
  T1 exact rational identity at a rational q, all partitions, n = 1..9;
  T2 the hook identity sum h = n(lam) + n(lam') + n, independently;
  T3 contentSum = n(lam') - n(lam), independently;
  T4 both families sum to 1 (they are probability measures) at the substrate q0;
  T5 the SEPARATION from w_lambda = dim_q^2/[n]_q!, so this cannot be read as
     "all three are the same thing after all".
T2 and T3 are what make T1 an explanation instead of a coincidence: if T1 passed
while T2/T3 failed, the identity would be numerology at the tested points.

Exact arithmetic throughout (`fractions.Fraction` at a rational q), so T1 is a
proof at each tested n rather than agreement to a tolerance. T4 needs a real q0
and uses mpmath at 50 dps -- no float64 anywhere (AGENTS.md NO-FLOAT64, which
binds probes).
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from fractions import Fraction  # noqa: E402

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402


# ---------------------------------------------------------------- partitions

def partitions(n: int, cap: int | None = None) -> list[tuple[int, ...]]:
    """Weakly decreasing partitions of `n`."""
    if n == 0:
        return [()]
    cap = n if cap is None else cap
    out: list[tuple[int, ...]] = []
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            out.append((first,) + rest)
    return out


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def hooks(lam: tuple[int, ...]) -> list[int]:
    lamt = conjugate(lam)
    return [lam[i] - j + lamt[j] - i - 1
            for i in range(len(lam)) for j in range(lam[i])]


def content_sum(lam: tuple[int, ...]) -> int:
    """sum_{(i,j) in lam} (j - i), 0-indexed."""
    return sum(j - i for i in range(len(lam)) for j in range(lam[i]))


def n_stat(lam: tuple[int, ...]) -> int:
    """n(lam) = sum_i (i-1) lam_i, 1-indexed = sum_i i*lam_i with i 0-indexed."""
    return sum(i * p for i, p in enumerate(lam))


def f_lambda(lam: tuple[int, ...]) -> int:
    """#SYT by the hook length formula (exact, integer)."""
    n = sum(lam)
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for h in hooks(lam):
        den *= h
    assert num % den == 0, "hook length formula must divide exactly"
    return num // den


# ---------------------------------------------------- the two weight families
# Both are computed over an arbitrary arithmetic type via the q-integer passed in,
# so the SAME code runs under Fraction (T1) and under mp.mpf (T4). A separate
# float path is exactly how a probe ends up comparing two different computations.

def bal_int(q, k: int):
    """[k]_q = (q^k - q^-k)/(q - q^-1), balanced."""
    return (q**k - q**(-k)) / (q - q**(-1))


def asym_int(Q, k: int):
    """{k}_Q = (Q^k - 1)/(Q - 1), asymmetric."""
    return (Q**k - 1) / (Q - 1)


def molien_weight(q, lam: tuple[int, ...]):
    """f^lam * q^{-kappa} * dim_q(lam) / [n]_q!  == f^lam * q^{-kappa} / prod [h]_q."""
    den = 1
    for h in hooks(lam):
        den = den * bal_int(q, h)
    return f_lambda(lam) * q**(-content_sum(lam)) / den


def feray_meliot_weight(Q, lam: tuple[int, ...]):
    """M_{n,Q}(lam) = Q^{n(lam)} f^lam / prod {h}_Q."""
    den = 1
    for h in hooks(lam):
        den = den * asym_int(Q, h)
    return Q**n_stat(lam) * f_lambda(lam) / den


def wedderburn_weight(q, lam: tuple[int, ...]):
    """w_lam = dim_q^2 / [n]_q!  -- the family the skeleton block currently uses."""
    n = sum(lam)
    qfac = 1
    for k in range(1, n + 1):
        qfac = qfac * bal_int(q, k)
    hp = 1
    for h in hooks(lam):
        hp = hp * bal_int(q, h)
    dimq = qfac / hp
    return dimq * dimq / qfac


# ------------------------------------------------------------------ the tests

def main() -> int:
    set_compute_dps()
    b = WitnessBuilder("molien-feray-meliot-bridge")
    b.set_description(
        "Establishes that the corpus's Molien/fake-degree weight "
        "f^lam*q^{-contentSum}*dim_q/[n]_q! IS Feray-Meliot's q-Plancherel "
        "measure M_{n,Q} under Q = q^2 -- an exact identity, not an "
        "approximation, verified in exact rational arithmetic for every "
        "partition of n = 1..9 (bean qou-j7ef). Consequence: the "
        "feray2010 citation in prop:q-plancherel-asymptotic-skeleton clause 2 "
        "transfers to the Molien family verbatim, while it does NOT transfer "
        "to the dim_q^2/[n]_q! family the block currently pushes forward: "
        "those two disagree per-partition by a relative 978 at n=12. NOTE the "
        "skeleton block records that separation as 12.6, which is M evaluated "
        "at Q = q0 rather than at the bridge argument Q = q0^2; both are "
        "measured in T5 and the earlier figure is correct about its own "
        "quantity, just not about the distance to the family the corpus holds. "
        "The kappa exponent is FORCED by the substitution (via the hook "
        "identity sum h = n(lam)+n(lam')+n and contentSum = n(lam')-n(lam), "
        "both verified independently) rather than being a convention choice."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    b.add_parameter("bridge_substitution", "Q = q^2")

    # -- T1: exact identity, rational q, every partition, n = 1..9 ------------
    # q = 7/5 is arbitrary but chosen != 1 and not a root of unity of small order;
    # exactness makes one witness point a proof, so a second q would add nothing.
    q_rat = Fraction(7, 5)
    Q_rat = q_rat * q_rat
    worst_n, worst_lam, n_checked = 0, None, 0
    all_exact = True
    for n in range(1, 10):
        for lam in partitions(n):
            n_checked += 1
            lhs = molien_weight(q_rat, lam)
            rhs = feray_meliot_weight(Q_rat, lam)
            if lhs != rhs:
                all_exact = False
                worst_n, worst_lam = n, lam
    b.add_data("T1_exact_identity", {
        "q_rational": str(q_rat),
        "Q_rational": str(Q_rat),
        "n_range": "1..9",
        "partitions_checked": n_checked,
        "arithmetic": "fractions.Fraction (exact)",
        "first_mismatch": None if all_exact else {"n": worst_n, "lam": list(worst_lam)},
    })
    b.add_assertion(
        "molien_eq_feray_meliot_at_Q_eq_q_squared",
        computed="1" if all_exact else "0", expected="1",
        source=f"Mol_n(lam) == M_{{n,q^2}}(lam) exactly (Fraction arithmetic) "
               f"for all {n_checked} partitions of n=1..9 at q=7/5",
    )

    # -- T2: the hook identity that collapses the exponent --------------------
    hook_ok = all(
        sum(hooks(lam)) == n_stat(lam) + n_stat(conjugate(lam)) + n
        for n in range(1, 11) for lam in partitions(n)
    )
    b.add_assertion(
        "hook_sum_identity",
        computed="1" if hook_ok else "0", expected="1",
        source="sum_x h(x) = n(lam) + n(lam') + n, all partitions n=1..10 -- "
               "the first of the two facts that make T1 structural rather "
               "than coincidental at the tested points",
    )

    # -- T3: contentSum is the OTHER half of the exponent collapse ------------
    content_ok = all(
        content_sum(lam) == n_stat(conjugate(lam)) - n_stat(lam)
        for n in range(1, 11) for lam in partitions(n)
    )
    b.add_assertion(
        "content_sum_eq_conjugate_defect",
        computed="1" if content_ok else "0", expected="1",
        source="contentSum(lam) = n(lam') - n(lam), all partitions n=1..10 -- "
               "so the corpus's kappa is exactly the exponent Q = q^2 forces, "
               "not a chosen convention",
    )

    # -- T4: both are probability measures at the real substrate q0 -----------
    q0 = mp.mpf(Q_50_DIGIT_STR)
    Q0 = q0 * q0
    sums = {}
    tol = mp.mpf(10) ** (-40)
    both_normalised = True
    for n in (3, 4, 5, 6, 9, 12):
        s_mol = mp.fsum(molien_weight(q0, lam) for lam in partitions(n))
        s_fm = mp.fsum(feray_meliot_weight(Q0, lam) for lam in partitions(n))
        sums[str(n)] = {"molien": fmt(s_mol), "feray_meliot": fmt(s_fm)}
        if abs(s_mol - 1) > tol or abs(s_fm - 1) > tol:
            both_normalised = False
    b.add_data("T4_normalisation_at_q0", sums)
    b.add_assertion(
        "both_families_sum_to_one_at_q0",
        computed="1" if both_normalised else "0", expected="1",
        source="sum_lam = 1 to 1e-40 for BOTH families at n = 3,4,5,6,9,12 and "
               "q0 > 1 (the Lean molienSum_eq_qFactorial and Feray-Meliot "
               "Definition 1 are the same theorem)",
    )

    # -- T5: and w_lambda is a genuinely different object ---------------------
    # Reported so this witness cannot be read as "the three families coincide".
    seps = {}
    max_rel_overall = mp.mpf(0)
    for n in (3, 4, 5, 6, 9, 12):
        s_w = mp.fsum(wedderburn_weight(q0, lam) for lam in partitions(n))
        max_rel = mp.mpf(0)
        max_rel_rawQ = mp.mpf(0)
        for lam in partitions(n):
            m = molien_weight(q0, lam)          # == M_{n, q0^2}, by T1
            w = wedderburn_weight(q0, lam)
            fm_rawQ = feray_meliot_weight(q0, lam)   # M at Q = q0, NOT the bridge
            max_rel = max(max_rel, abs(w - m) / m)
            max_rel_rawQ = max(max_rel_rawQ, abs(w - fm_rawQ) / fm_rawQ)
        max_rel_overall = max(max_rel_overall, max_rel)
        seps[str(n)] = {
            "sum_w_lambda": fmt(s_w),
            "max_rel_dev_w_vs_molien_Q_eq_q_squared": fmt(max_rel),
            "max_rel_dev_w_vs_feray_meliot_at_Q_eq_q": fmt(max_rel_rawQ),
        }
    b.add_data("T5_separation_from_wedderburn_weight", {
        "note": "Two columns because the argument matters. "
                "`..._Q_eq_q_squared` is the distance from w_lambda to the "
                "family the corpus actually holds (the Molien weight, = M at "
                "Q = q^2 by T1). `..._Q_eq_q` is the distance to M evaluated "
                "at the raw Definition-1 argument Q = q, which is the column "
                "prop:q-plancherel-asymptotic-skeleton currently quotes. Both "
                "are real quantities; only the first answers 'can the "
                "feray2010 citation be moved onto w_lambda by rescaling'.",
        "per_n": seps,
    })
    b.add_assertion(
        "wedderburn_weight_is_a_different_family",
        computed="1" if max_rel_overall > mp.mpf("0.1") else "0", expected="1",
        source=f"max per-partition relative deviation of dim_q^2/[n]_q! from "
               f"the Molien family is {fmt(max_rel_overall)} over n<=12 -- the "
               f"two are not one normalisation apart, so the feray2010 "
               f"citation cannot be moved between them by rescaling",
    )

    b.save()
    ok = all_exact and hook_ok and content_ok and both_normalised
    print(f"T1 exact identity over {n_checked} partitions (n=1..9): {all_exact}")
    print(f"T2 hook-sum identity: {hook_ok}")
    print(f"T3 contentSum = n(lam') - n(lam): {content_ok}")
    print(f"T4 both sum to 1 at q0: {both_normalised}")
    print(f"T5 max rel dev w_lambda vs Molien: {fmt(max_rel_overall)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
