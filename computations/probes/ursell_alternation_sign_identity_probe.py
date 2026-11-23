#!/usr/bin/env python3
"""The 3-body sign obstruction is a missing (-1)^(n-1), not a physical bound.

`MayerThreeBodySign` proves that the multiplicative assembly `W = 1 - PROD f`
forces `b3 < 0` while `fpn <= 2/3`, and the framework's own `fpn = z_D` is below
it. That has been read as a physical obstruction. This probe measures what the
classical cluster expansion does with the SAME data, and the answer inverts the
reading.

Definitions are taken verbatim from Jansen & Kolesnikov, *Cluster Expansions:
Necessary and Sufficient Convergence Conditions*, J. Stat. Phys. 189:33 (2022),
`library/s10955-022-02992-6/` -- Mayer's f function `f(x,y) = e^{-v(x,y)} - 1`,
the graph weight `w(G) = PROD_{{i,j} in E(G)} f(x_i,x_j)`, and the n-th Ursell
function `phi^T_n = SUM_{G connected on [n]} w(G)`.

THREE MEASUREMENTS.

1. THE IDENTITY. Under the Boltzmann identification `f_corpus = e^{-v}`, so that
   the Mayer variable is `g = f_corpus - 1`, the corpus's connected 3-body
   cumulant is EXACTLY minus the third Ursell function:

       b3_corpus(f12,f13,f23)  ==  - phi^T_3(f12-1, f13-1, f23-1)

   Checked in exact rational arithmetic on random non-uniform triples. It also
   holds trivially at n = 2 (`W(2) = 1 - f = -(f-1) = -phi^T_2`) and it FAILS at
   n = 4 -- the corpus's `b4` is neither `+phi^T_4` nor `-phi^T_4`. So this is a
   low-order identity of the `1 - PROD f` form, not a general correspondence,
   and it is reported as such.

2. THE ALTERNATION. In the purely repulsive class (`v >= 0`, i.e. `g` in
   `(-1,0)`, i.e. `f_corpus` in `(0,1)` -- which is where every framework bond
   factor lives) the Ursell functions ALTERNATE: `(-1)^(n-1) phi^T_n >= 0`.
   So `phi^T_2 <= 0` and `phi^T_3 >= 0`.

   NOTE ON THE SOURCE. The paper's Eq. (3.1) reads `(-1)^n` in the OCR of
   `library/s10955-022-02992-6/`. That is inconsistent with the paper's own
   Corollary 3.3, which gives sign `(-1)^k` for `psi_{n,n+k}` together with
   `psi_{1,1+k} = phi^T_{1+k}`, i.e. sign `(-1)^(m-1)` for `phi^T_m`. This probe
   settles it by direct computation from the definitions rather than from the
   scanned superscript: at n = 2, `phi^T_2 = g <= 0`, so `(-1)^n` would be wrong
   and `(-1)^(n-1)` is right. Treat the OCR'd exponent as a scanning artifact.

3. THE CONSEQUENCE. The corpus carries a UNIFORM minus sign: `b_n = -phi^T_n` at
   both n = 2 and n = 3. At n = 2 that is correct -- binding is positive and
   `phi^T_2` is negative. At n = 3 the Ursell function has already flipped sign
   on its own, so the uniform minus INVERTS the physical answer. Restoring the
   alternation, `b_n = (-1)^(n-1) phi^T_n`, gives `b3 = +phi^T_3 > 0` -- positive
   for every `f` in `(0,1)`, with no threshold, no `fpn > 2/3`, and no attractive
   component required.

   The probe reports the resulting `b3` in MeV against the AME targets, so the
   magnitude claim is measured rather than asserted.

4. THE BOLTZMANN IDENTIFICATION IS DERIVED, NOT ASSUMED -- and by the corpus.
   An earlier version of this probe flagged `f_corpus = e^{-v}` as an
   unestablished interpretation. It is not: it is
   `docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
   Sec.10a read backwards. That section derives, from trace multiplicativity over
   bonds (`tr_atom = tr_free * PROD_bonds mu_k`, verified to 1.2e-31) plus energy
   extensivity, that the bond energy is `B = -alpha * ln mu` -- the Cauchy
   functional equation, "the log form is forced". Inverting, `mu = e^{-B/alpha}`:
   the corpus's bond factor IS the Boltzmann factor of the corpus's own derived
   bond energy, with `v := B/alpha`.

   And it is the SAME object: Sec.10b's `mu_pn = z - h(1/2 - delta/4)` is
   character-for-character the `fpn` of `MayerThreeBodySign`'s probe-2 typing.

   This probe checks the chain numerically in both conventions: `mu in (0,1)`,
   `v > 0`, and `e^{-v} == mu` to 1e-40.

   NAMING CAVEAT, so nobody reads physics out of a convention. In the Mayer
   convention `v > 0` is called "repulsive", and here `v = B/alpha` is the
   BINDING energy, which is positive. The classical alternation theorem holds on
   `f in (0,1)`, which is where the corpus sits; calling the corresponding
   `v = -ln mu > 0` "repulsive" is bookkeeping and asserts NOTHING about the
   nuclear force.

WHAT THIS DOES NOT ESTABLISH. The normalisation of the cluster expansion's
n-body term is not fixed here. Sec.10a gives `B = -alpha * ln(trace)`, and the
standard cluster expansion gives `ln Xi = SUM_n (z^n/n!) INT phi^T_n`, so the
connected n-body part of `B` should be `alpha` times the n-th Ursell term up to
a combinatorial factor this probe does not derive. The SIGN is settled; the
magnitude is reported under two scale conventions that differ by ~10%, and
pinning the normalisation is the remaining work.

Scope-(a). This does not refute `MayerThreeBodySign` -- every one of its
statements remains true of the object it is about. What is established is that
the object it is about differs from the classical one by a sign the classical
theory does not carry.

`-- Ref:` [jansen2022cluster] https://doi.org/10.1007/s10955-022-02992-6
Bean `qou-rwhv`; audit
`docs/audits/2026-08-30-ursell-alternating-sign-and-the-b3-obstruction.md`.
"""
from __future__ import annotations

import datetime
import json
import os
import random
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

set_compute_dps()

# AME2020, the same three values MayerThreeBodySign's probe uses.
AME = {"D": AME_B_DEUTERON_MEV_VALIDATION, "3H": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION}

N_TRIALS_N3 = 400
N_TRIALS_N4 = 200
RANDOM_SEED = 11


# ---------------------------------------------------------------- exact layer
# Measurement 1 is an ALGEBRAIC identity, so it is checked over Fraction, not
# mpmath: an exact identity should be verified exactly, and a tolerance here
# would be reporting the arithmetic rather than the mathematics.

def _prod(it):
    r = Fraction(1)
    for x in it:
        r *= x
    return r


def connected_edge_subsets(n):
    """Every connected graph on [n], as an edge list. C_n in the paper's notation."""
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        E = [edges[i] for i in range(len(edges)) if mask >> i & 1]
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for i, j in E:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[ri] = rj
        if len({find(v) for v in range(n)}) == 1:
            yield E


def ursell(n, g):
    """phi^T_n = SUM_{G in C_n} PROD_{{i,j} in E(G)} g_ij  (Jansen-Kolesnikov p.5)."""
    return sum((_prod(g[e] for e in E) for E in connected_edge_subsets(n)),
               Fraction(0))


def W(f, S):
    """The corpus's multiplicative assembly on a sub-cluster: 1 - PROD f over its bonds."""
    return 1 - _prod(f[e] for e in combinations(sorted(S), 2))


def corpus_b3(f):
    """QOU.Mass.PairwiseCumulantVanishing.b3 with the multiplicative binding."""
    return W(f, {0, 1, 2}) - sum(W(f, {i, j}) for i, j in combinations(range(3), 2))


def corpus_b4(f):
    """QOU.Mass.PairwiseCumulantVanishing.b4 = quad - pairSum - b3Sum."""
    pair_sum = sum(W(f, {i, j}) for i, j in combinations(range(4), 2))
    b3_sum = sum(
        W(f, set(T)) - sum(W(f, {i, j}) for i, j in combinations(sorted(T), 2))
        for T in combinations(range(4), 3)
    )
    return W(f, {0, 1, 2, 3}) - pair_sum - b3_sum


def check_identity():
    rng = random.Random(RANDOM_SEED)
    mism3 = 0
    for _ in range(N_TRIALS_N3):
        f = {e: Fraction(rng.randint(1, 9999), 10000)
             for e in combinations(range(3), 2)}
        if corpus_b3(f) != -ursell(3, {e: f[e] - 1 for e in f}):
            mism3 += 1
    mism4_neg = mism4_pos = 0
    for _ in range(N_TRIALS_N4):
        f = {e: Fraction(rng.randint(1, 9999), 10000)
             for e in combinations(range(4), 2)}
        phi4 = ursell(4, {e: f[e] - 1 for e in f})
        b4 = corpus_b4(f)
        if b4 != -phi4:
            mism4_neg += 1
        if b4 != phi4:
            mism4_pos += 1
    return {
        "n3_trials": N_TRIALS_N3,
        "n3_mismatches_vs_minus_phi": mism3,
        "n3_identity_holds": mism3 == 0,
        "n4_trials": N_TRIALS_N4,
        "n4_mismatches_vs_minus_phi": mism4_neg,
        "n4_mismatches_vs_plus_phi": mism4_pos,
        "n4_identity_holds_either_sign": mism4_neg == 0 or mism4_pos == 0,
        "arithmetic": "exact (fractions.Fraction); no tolerance, no float",
    }


def check_alternation():
    """(-1)^(n-1) phi^T_n >= 0 for g in (-1,0), against the OCR'd (-1)^n."""
    rng = random.Random(RANDOM_SEED + 1)
    rows = []
    for n in (2, 3, 4, 5):
        ok_alt = ok_ocr = 0
        trials = 60 if n <= 4 else 20
        for _ in range(trials):
            g = {e: Fraction(-rng.randint(1, 9999), 10000)
                 for e in combinations(range(n), 2)}
            phi = ursell(n, g)
            if (-1) ** (n - 1) * phi >= 0:
                ok_alt += 1
            if (-1) ** n * phi >= 0:
                ok_ocr += 1
        rows.append({
            "n": n,
            "trials": trials,
            "holds_minus_one_to_n_minus_1": ok_alt,
            "holds_minus_one_to_n_as_ocrd": ok_ocr,
        })
    return rows


# ------------------------------------------------------------ framework layer
# Measurement 3 evaluates at the framework's own bond factors, so it is mpmath
# at the compute dps, carried end to end; floats appear nowhere.

def framework_bond_factors():
    q = mpf(Q_50_DIGIT_STR)
    z = markov_z(q)                       # convention D, canonical (R1 2026-08-15)
    h = hecke_h(q)
    delta = flavor_split_leading(q)
    return {
        "q0": q,
        "z_D": z,
        "h": h,
        "f_pp": z,
        "f_nn": z - h,
        "f_pn_probe2": z - h * (mpf(1) / 2 - delta / 4),
        "f_pn_chi": z,
    }


def ursell_mp(n, g):
    """phi^T_n over mpmath, same definition as `ursell` above."""
    tot = mpf(0)
    for E in connected_edge_subsets(n):
        w = mpf(1)
        for e in E:
            w *= g[e]
        tot += w
    return tot


def evaluate_at_framework(fpn):
    """Uniform-bond evaluation at the framework's own f_pn, in W-units and MeV."""
    f = {e: fpn for e in combinations(range(3), 2)}
    g = {e: fpn - 1 for e in combinations(range(3), 2)}

    b2_W = 1 - fpn                                   # = -phi^T_2
    phi2 = ursell_mp(2, {(0, 1): fpn - 1})
    phi3 = ursell_mp(3, g)
    b3_corpus_W = (1 - fpn ** 3) - 3 * (1 - fpn)     # = -phi^T_3
    b3_alternating_W = phi3                          # = (-1)^(3-1) phi^T_3

    scale = AME["D"] / b2_W                          # MeV per W-unit, pinned at D
    ame_b3_avg = (AME["3H"] + AME["3He"]) / 2 - 3 * AME["D"]
    ame_b3_triton = AME["3H"] - 3 * AME["D"]

    b3_pred = scale * b3_alternating_W
    return {
        "f_pn": mp.nstr(fpn, 20),
        "b2_W_units": mp.nstr(b2_W, 20),
        "phi_T_2": mp.nstr(phi2, 20),
        "b2_equals_minus_phi2": bool(abs(b2_W + phi2) < mpf(10) ** (-40)),
        "phi_T_3": mp.nstr(phi3, 20),
        "b3_corpus_W_units": mp.nstr(b3_corpus_W, 20),
        "b3_corpus_equals_minus_phi3": bool(
            abs(b3_corpus_W + phi3) < mpf(10) ** (-40)),
        "b3_alternating_W_units": mp.nstr(b3_alternating_W, 20),
        "MeV_per_W_unit": mp.nstr(scale, 20),
        "b3_alternating_MeV": mp.nstr(b3_pred, 20),
        "ame_b3_isospin_avg_MeV": mp.nstr(ame_b3_avg, 12),
        "ame_b3_triton_MeV": mp.nstr(ame_b3_triton, 12),
        "ratio_to_isospin_avg": mp.nstr(b3_pred / ame_b3_avg, 12),
        "ratio_to_triton": mp.nstr(b3_pred / ame_b3_triton, 12),
    }


def check_boltzmann_chain():
    """Measurement 4: mu is the Boltzmann factor of the SEC.10a-derived bond energy.

    Sec.10a: B = -alpha * ln mu, alpha = m_e / (q0 (q0 - 1)).  Inverting gives
    mu = e^{-v} with v := B/alpha, so the Mayer variable g = mu - 1 is not an
    imported analogy. Checked in both conventions -- D is canonical (R1
    2026-08-15); C is what the 2026-08-08 audit itself used, so its row is the
    cross-check that this reproduces that audit's own number.
    """
    q = mpf(Q_50_DIGIT_STR)
    h = hecke_h(q)
    d = flavor_split_leading(q)
    # NO SILENT FALLBACK. A hardcoded m_e differs from the package's
    # M_E_MEV = 0.51099895069 at the 10th digit, which silently shifts alpha and
    # every energy below it by ~1.35e-9 relative -- invisible in a conclusion,
    # wrong in every digit past the 9th that this probe prints. Fail loudly.
    from qou_substrate.constants import M_E_MEV as _ME  # noqa: E402
    me = mpf(_ME)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    ame_d = AME["D"]

    rows = []
    for label, z in (("D_canonical", markov_z(q)),
                     ("C_as_used_by_the_2026_08_08_audit",
                      1 / (mp.sqrt(q) + 1 / mp.sqrt(q)))):
        mu = z - h * (mpf(1) / 2 - d / 4)
        B = -alpha * mp.log(mu)
        v = B / alpha
        rows.append({
            "convention": label,
            "z": mp.nstr(z, 20),
            "mu_pn": mp.nstr(mu, 20),
            "mu_in_unit_interval": bool(0 < mu < 1),
            "B_2H_MeV": mp.nstr(B, 12),
            "B_2H_over_AME": mp.nstr(B / ame_d, 10),
            "v_eq_B_over_alpha": mp.nstr(v, 20),
            "v_positive": bool(v > 0),
            "exp_minus_v_equals_mu": bool(abs(mp.e ** (-v) - mu) < mpf(10) ** (-40)),
        })
    return {"alpha_MeV": mp.nstr(alpha, 20), "rows": rows}


def main() -> int:
    ident = check_identity()
    boltz = check_boltzmann_chain()
    alt = check_alternation()
    bf = framework_bond_factors()

    evals = {
        "chi_typing_f_pn_eq_z_D": evaluate_at_framework(bf["f_pn_chi"]),
        "probe2_typing_f_pn": evaluate_at_framework(bf["f_pn_probe2"]),
    }

    print("1. IDENTITY  corpus b3 == -phi^T_3(f-1), exact rational arithmetic")
    print(f"     n=3: {ident['n3_trials'] - ident['n3_mismatches_vs_minus_phi']}"
          f"/{ident['n3_trials']} agree   (mismatches "
          f"{ident['n3_mismatches_vs_minus_phi']})")
    print(f"     n=4: b4 vs -phi^T_4 mismatches {ident['n4_mismatches_vs_minus_phi']}"
          f"/{ident['n4_trials']};  vs +phi^T_4 mismatches "
          f"{ident['n4_mismatches_vs_plus_phi']}/{ident['n4_trials']}")
    print("          -> the identity is a LOW-ORDER property, it does not extend to n=4")

    print("\n2. ALTERNATION  in the repulsive class g in (-1,0)")
    print(f"     {'n':>3}{'trials':>8}{'(-1)^(n-1) phi >= 0':>22}{'(-1)^n phi >= 0':>20}")
    for r in alt:
        print(f"     {r['n']:>3}{r['trials']:>8}"
              f"{r['holds_minus_one_to_n_minus_1']:>22}"
              f"{r['holds_minus_one_to_n_as_ocrd']:>20}")
    print("          -> (-1)^(n-1) is the law; the OCR'd (-1)^n in Eq. (3.1) fails at n=2")

    print("\n3. AT THE FRAMEWORK'S OWN BOND FACTORS (uniform, convention D)")
    for name, e in evals.items():
        print(f"     {name}")
        print(f"       f_pn                    {e['f_pn']}")
        print(f"       corpus b3   (W-units)   {e['b3_corpus_W_units']}")
        print(f"       phi^T_3     (W-units)   {e['phi_T_3']}")
        print(f"       b3 with alternation     {e['b3_alternating_W_units']}")
        print(f"       -> in MeV               {e['b3_alternating_MeV']}")
        print(f"          AME isospin avg      {e['ame_b3_isospin_avg_MeV']}"
              f"   ratio {e['ratio_to_isospin_avg']}")
        print(f"          AME triton           {e['ame_b3_triton_MeV']}"
              f"   ratio {e['ratio_to_triton']}")

    print("\n4. THE BOLTZMANN IDENTIFICATION IS SEC.10a READ BACKWARDS")
    print(f"     alpha = m_e/(q0(q0-1)) = {boltz['alpha_MeV']} MeV")
    for r in boltz["rows"]:
        print(f"     {r['convention']}")
        print(f"       mu_pn = {r['mu_pn']}   in (0,1)? {r['mu_in_unit_interval']}")
        print(f"       B(2H) = -alpha ln mu = {r['B_2H_MeV']} MeV"
              f"   / AME = {r['B_2H_over_AME']}")
        print(f"       v = B/alpha = {r['v_eq_B_over_alpha']}   > 0? {r['v_positive']}"
              f"   e^-v == mu? {r['exp_minus_v_equals_mu']}")

    assertions = [
        {"name": "corpus b3 == -phi^T_3 exactly, on every random non-uniform triple",
         "passed": ident["n3_identity_holds"]},
        {"name": "mu is the Boltzmann factor of the Sec.10a bond energy: "
                 "mu in (0,1), v = B/alpha > 0, and e^-v == mu, in BOTH conventions",
         "passed": all(r["mu_in_unit_interval"] and r["v_positive"]
                       and r["exp_minus_v_equals_mu"] for r in boltz["rows"])},
        {"name": "the identity does NOT extend to n=4 under either sign",
         "passed": not ident["n4_identity_holds_either_sign"]},
        {"name": "(-1)^(n-1) phi^T_n >= 0 holds for every n and trial in the repulsive class",
         "passed": all(r["holds_minus_one_to_n_minus_1"] == r["trials"] for r in alt)},
        {"name": "the OCR'd (-1)^n law FAILS at n=2, which is how the exponent is settled",
         "passed": next(r for r in alt if r["n"] == 2)["holds_minus_one_to_n_as_ocrd"] == 0},
        {"name": "at both typings the corpus b3 is negative and phi^T_3 is positive",
         "passed": all(mpf(e["b3_corpus_W_units"]) < 0 < mpf(e["phi_T_3"])
                       for e in evals.values())},
        {"name": "restoring the alternation gives b3 > 0, the sign AME has",
         "passed": all(mpf(e["b3_alternating_MeV"]) > 0 for e in evals.values())},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The corpus's 3-body cumulant is exactly minus the classical third "
            "Ursell function under the Boltzmann identification g = f - 1. The "
            "classical Ursell functions ALTERNATE in the repulsive class, "
            "(-1)^(n-1) phi^T_n >= 0, while the corpus carries a uniform minus "
            "at n=2 and n=3. The uniform minus is correct at n=2 and inverts the "
            "physical sign at n=3, so MayerThreeBodySign's b3 < 0 is a missing "
            "(-1)^(n-1) rather than a physical obstruction. The identity is "
            "low-order: it does not extend to n=4 under either sign."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "convention": "D (z = q^3/(q^2+1)), canonical per owner ruling R1 2026-08-15",
        "identity": ident,
        "alternation": alt,
        "boltzmann_chain": boltz,
        "framework_evaluation": evals,
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(a). Does NOT refute MayerThreeBodySign -- every statement there "
            "remains true of the object it is about. What is established is that "
            "that object differs from the classical one by a sign the classical "
            "theory does not carry. The Boltzmann identification f = e^{-v} IS "
            "derived, by the corpus's own Sec.10a log form read backwards (see "
            "boltzmann_chain). What is NOT fixed here is the normalisation of the "
            "cluster expansion's n-body term: the sign is settled, the magnitude "
            "is reported under two scale conventions differing by ~10%."),
        "source": (
            "Jansen & Kolesnikov, J. Stat. Phys. 189:33 (2022), "
            "library/s10955-022-02992-6/ -- definitions on p.5, sign property "
            "in section 3.1. The OCR of Eq. (3.1) reads (-1)^n and is "
            "inconsistent with the paper's own Corollary 3.3; settled here by "
            "computation from the definitions, not from the scanned superscript."),
        "lean": "QOU/MassTheory/MayerThreeBodySign.lean, QOU/Mass/PairwiseCumulantVanishing.lean",
        "bean": "qou-rwhv",
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "ursell-alternation-sign-identity.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
