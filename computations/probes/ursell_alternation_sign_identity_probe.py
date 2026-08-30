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

WHAT THIS DOES NOT ESTABLISH. The Boltzmann identification `f_corpus = e^{-v}`
is NOT derived anywhere in the corpus -- the framework's bond factors are Markov
factors built from `z`, and nothing identifies them with an exponentiated
potential. Measurement 1 is a pure algebraic identity and needs no such reading;
measurements 2 and 3 need only that `f_corpus` lies in `(0,1)`, which is
measured. But calling `g = f_corpus - 1` "a Mayer function of a repulsive
potential" is an INTERPRETATION, and the physical conclusion inherits it.

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

set_compute_dps()

# AME2020, the same three values MayerThreeBodySign's probe uses.
AME = {"D": mpf("2.224566"), "3H": mpf("8.481798"), "3He": mpf("7.718043")}

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


def main() -> int:
    ident = check_identity()
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

    assertions = [
        {"name": "corpus b3 == -phi^T_3 exactly, on every random non-uniform triple",
         "passed": ident["n3_identity_holds"]},
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
        "framework_evaluation": evals,
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(a). Does NOT refute MayerThreeBodySign -- every statement there "
            "remains true of the object it is about. What is established is that "
            "that object differs from the classical one by a sign the classical "
            "theory does not carry. The Boltzmann identification f_corpus = e^{-v} "
            "is NOT derived in the corpus; the algebraic identity needs no such "
            "reading, but the physical conclusion inherits it."),
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
