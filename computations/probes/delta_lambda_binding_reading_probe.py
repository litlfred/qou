#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational arithmetic at the rational q0, then mpmath at 60 dps.
"""The Delta_lambda-weighted binding functional: which READING, and where pn != np comes from.

Owner pick (2026-10-11, "2"): investigate the Delta_lambda binding law — fix its reading and
the pn != np asymmetry. EXPLORE AND DERIVE ONLY: no producer, dashboard or content block is
touched, and no law or reading is selected by agreement with nature (AME is not used).

Functional:  Phi(X) = sum_lam y_lam chi^lam(X) Delta_lam,  Delta_lam = (-1)^{n(lam)} dim V_lam
             (value PROVED, dtEuler_eq_deltaLambda_unconditional; the LAW is posited —
             computations/delta-lambda-witness.json: "NOT a binding energy").

Three readings measured on the same words (convention D, proton pin, exact over Q):

  R_dir_corpus  B = - m_e Phi(B_K)              the corpus's own form: Binding(K) = m_e Phi(B_K)
                                                 is ADDED to the constituent mass
                                                 (recomputed-low-isotope-mass-table.md:14-15), so the
                                                 binding ENERGY is its negative
  R_dir_plus    B = + m_e Phi(B_K)              the sign used by the predecessor probe's L_frob_direct
  R_diff        B = m_e (Phi(free) - Phi(atom)) the difference form (no source block for Phi; the
                                                 corpus states the difference form only for tr_M,
                                                 conj:knot-factor-frobenius-pairing)

Structural facts measured (Lean companion: QOU/Mass/DeltaLambdaReadingAndExchange.lean):

  F1  Projector complement: for every word W, Phi(W) - Phi(W P_+) = Phi(W P_-) exactly, so
      R_diff(T) = m_e Phi(W P_{other}) = -R_dir_corpus(W P_{other}): the difference reading of
      a channel is the corpus-direct reading of the COMPLEMENTARY channel, negated.
  F2  Cyclicity: Phi(W s2) = Phi(s2 W) (Phi is a class function — each chi^lam is a trace).
  F3  Flip invariance: Phi(F(X)) = Phi(X), F: sigma_i -> sigma_{4-i} (conjugation by the half
      twist). F fixes the interface letter s2 and maps (p on left, n on right) to (n on left,
      p on right) with EACH nucleon word mirrored (its two generators swapped).
  F4  Hence Phi(W_pn s2) = Phi(W~_np s2), where ~ is the in-block mirror. pn = np would need
      Phi to be blind to the mirror of a nucleon word sitting next to the interface letter.
      tr_M is blind (Markov factorisation tr(W s2) = z tr(W)); Phi is not.
  F5  The free words are equal: Phi(W_pn) = Phi(W_np) (the blocks are conjugate by the block
      exchange), so the whole asymmetry lives in the bond term.
"""
from __future__ import annotations

import json
import sys
import time
from math import factorial
from multiprocessing import Pool
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_symbolic import Q  # noqa: E402
from hecke_character_symbolic import q_character_on_braid_word  # noqa: E402
from markov_weights_symbolic import solve_y_lambda  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from gamma_gamma_isospin_channel_probe import nucleon  # noqa: E402

DPS = 60
set_compute_dps(DPS)
QV = sp.Rational(Q_50_DIGIT_STR)
NGEN = 5          # H_6, generators 0..4; interface letter is generator 2
S2 = [(2, "sigma")]
PAIRS = ("pp", "pn", "np", "nn")


def to_mp(x) -> mp.mpf:
    num, den = sp.fraction(sp.Rational(x))
    return mp.mpf(int(num)) / mp.mpf(int(den))


def hook_dim(lam) -> int:
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    return factorial(n) // prod


def delta(lam) -> int:
    return (-1) ** sum(i * r for i, r in enumerate(lam)) * hook_dim(lam)


def flip(word):
    """Conjugation by the half twist: sigma_i -> sigma_{NGEN-1-i}."""
    return [(NGEN - 1 - g, t) for (g, t) in word]


def mirror_nucleon(kind, g0):
    """The nucleon word on (g0, g0+1) with its two generators swapped (in-block flip)."""
    a, b = g0, g0 + 1
    return [((b if g == a else a), t) for (g, t) in nucleon(kind, g0)]


def build_words():
    out = []
    for pair in PAIRS:
        W = nucleon(pair[0], 0) + nucleon(pair[1], 3)
        Wm = mirror_nucleon(pair[0], 0) + mirror_nucleon(pair[1], 3)
        out += [(pair, "W", W), (pair, "W.s", W + S2), (pair, "s.W", S2 + W),
                (pair, "F(W)", flip(W)), (pair, "F(W).s", flip(W) + S2),
                (pair, "Wmir", Wm), (pair, "Wmir.s", Wm + S2)]
    return out


def _job(args):
    pair, key, word, lam = args
    return pair, key, lam, sp.Rational(q_character_on_braid_word(lam, tuple(word), QV))


def main() -> int:
    t0 = time.time()
    q = Q_MP
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    z = q ** 3 / (q ** 2 + 1)
    s = 1 / (q + 1 / q)
    print(f"Delta_lambda binding reading probe (proton pin, convention D, {DPS} dps)")

    results: dict = {}
    checks: dict = {}
    tol = mp.mpf(10) ** (-50)

    # ---------- n = 2: the three readings on the bare projectors ----------
    y2 = (z + 1 / q) / (q + 1 / q)
    y11 = (q - z) / (q + 1 / q)
    phi1 = y2 - y11
    phiP = {1: y2, 0: -y11}                 # Phi(P_+) = y2, Phi(P_-) = -y11 (Delta_(2)=+1, Delta_(1,1)=-1)
    n2 = {}
    for T in (1, 0):
        n2[f"T{T}"] = {"R_dir_corpus": fmt(-me * phiP[T]), "R_dir_plus": fmt(me * phiP[T]),
                       "R_diff": fmt(me * (phi1 - phiP[T]))}
    results["n2_projectors_MeV"] = n2
    checks["n2_complement_Phi1_minus_PhiPplus_eq_PhiPminus"] = bool(abs(phi1 - phiP[1] - phiP[0]) < tol)

    # ---------- H_6 ----------
    Y6s = solve_y_lambda(6)
    support = sorted((lam for lam in Y6s if sp.cancel(Y6s[lam]) != 0), key=len)
    y6 = {lam: sp.Rational(sp.cancel(Y6s[lam]).subs(Q, QV)) for lam in support}
    words = build_words()
    jobs = [(p, k, w, lam) for (p, k, w) in words for lam in support]
    print(f"  {len(words)} words x {len(support)} blocks = {len(jobs)} characters", flush=True)
    chi: dict = {}
    with Pool(4) as pool:
        for i, (p, k, lam, val) in enumerate(pool.imap_unordered(_job, jobs), 1):
            chi.setdefault(p, {}).setdefault(k, {})[lam] = val
            if i % 16 == 0:
                print(f"    {i}/{len(jobs)}  {time.time() - t0:.0f} s", flush=True)
    tr = {p: {k: to_mp(sum(y6[l] * c[l] for l in support)) for k, c in d.items()} for p, d in chi.items()}
    ph = {p: {k: to_mp(sum(y6[l] * c[l] * delta(l) for l in support)) for k, c in d.items()}
          for p, d in chi.items()}
    results["support_delta"] = {str(l): delta(l) for l in support}
    results["Phi"] = {p: {k: fmt(v) for k, v in d.items()} for p, d in ph.items()}
    results["tr_M"] = {p: {k: fmt(v) for k, v in d.items()} for p, d in tr.items()}

    # F2 cyclicity, F3 flip invariance, F5 free equality
    checks["F2_cyclic_Phi"] = bool(all(abs(ph[p]["W.s"] - ph[p]["s.W"]) < tol for p in PAIRS))
    checks["F3_flip_invariant_Phi_W"] = bool(all(abs(ph[p]["W"] - ph[p]["F(W)"]) < tol for p in PAIRS))
    checks["F3_flip_invariant_Phi_Ws"] = bool(all(abs(ph[p]["W.s"] - ph[p]["F(W).s"]) < tol for p in PAIRS))
    checks["F5_free_pn_eq_np_Phi"] = bool(abs(ph["pn"]["W"] - ph["np"]["W"]) < tol)
    # F4: F(W_pn) is (mirrored n on the left, mirrored p on the right) = W~_np
    checks["F4_Phi_pn_bond_eq_mirrored_np_bond"] = bool(abs(ph["pn"]["W.s"] - ph["np"]["Wmir.s"]) < tol)
    checks["F4_Phi_np_bond_eq_mirrored_pn_bond"] = bool(abs(ph["np"]["W.s"] - ph["pn"]["Wmir.s"]) < tol)
    # tr_M Markov factorisation: tr(W s2) = z tr(W) for every pair (why tr_M is blind to the order)
    checks["trM_markov_factorises_Ws"] = bool(all(abs(tr[p]["W.s"] - z * tr[p]["W"]) < tol for p in PAIRS))
    checks["trM_bond_pn_eq_np"] = bool(abs(tr["pn"]["W.s"] - tr["np"]["W.s"]) < tol)
    checks["Phi_bond_pn_ne_np"] = bool(abs(ph["pn"]["W.s"] - ph["np"]["W.s"]) > mp.mpf(10) ** (-20))
    # Phi does NOT factorise: Phi(W s2) / Phi(W) is species-dependent
    ratios = {p: ph[p]["W.s"] / ph[p]["W"] for p in PAIRS}
    results["Phi_bond_ratio_Phi(Ws)/Phi(W)"] = {p: fmt(v) for p, v in ratios.items()}
    results["mirror_effect_Phi(W.s)-Phi(Wmir.s)"] = {p: fmt(ph[p]["W.s"] - ph[p]["Wmir.s"]) for p in PAIRS}

    # ---------- C0: P_T on the interface; the three readings ----------
    def proj(T):
        return (s / q, s) if T == 1 else (s * q, -s)

    C0 = {}
    for p in PAIRS:
        for T in (1, 0):
            if p in ("pp", "nn") and T == 0:
                continue
            a, b = proj(T)
            atom = a * ph[p]["W"] + b * ph[p]["W.s"]
            other = proj(1 - T)
            atom_c = other[0] * ph[p]["W"] + other[1] * ph[p]["W.s"]
            free = ph[p]["W"]
            row = {"R_dir_corpus": -me * atom, "R_dir_plus": me * atom,
                   "R_diff": me * (free - atom), "free_baseline_R_dir_corpus": -me * free}
            checks.setdefault("F1_diff_T_eq_Phi_complement_channel", True)
            checks["F1_diff_T_eq_Phi_complement_channel"] &= bool(abs((free - atom) - atom_c) < tol)
            C0[f"{p}_T{T}"] = {k: fmt(v) for k, v in row.items()}
    results["C0_MeV"] = C0
    # the S2-orbit average over the two block orders (labelled OPTION, not adopted)
    avg = {}
    for T in (1, 0):
        for rd in ("R_dir_corpus", "R_diff"):
            avg[f"pn_np_avg_T{T}_{rd}"] = fmt((mp.mpf(C0[f"pn_T{T}"][rd]) + mp.mpf(C0[f"np_T{T}"][rd])) / 2)
    results["C0_order_average_OPTION_not_adopted"] = avg

    # ---------- print ----------
    print("\n  n=2 projectors [MeV]")
    for k, r in n2.items():
        print(f"    {k}: " + "  ".join(f"{kk}={mp.nstr(mp.mpf(v), 10)}" for kk, v in r.items()))
    print("\n  H6 Phi, tr_M")
    for p in PAIRS:
        print(f"    {p}: Phi(W)={mp.nstr(ph[p]['W'], 12)} Phi(Ws)={mp.nstr(ph[p]['W.s'], 12)} "
              f"Phi(Wmir.s)={mp.nstr(ph[p]['Wmir.s'], 12)} tr(W)={mp.nstr(tr[p]['W'], 12)} "
              f"tr(Ws)/tr(W)={mp.nstr(tr[p]['W.s'] / tr[p]['W'], 12)}")
    print("\n  C0 [MeV]")
    for k, r in C0.items():
        print(f"    {k:<7} " + "  ".join(f"{kk}={mp.nstr(mp.mpf(v), 9)}" for kk, v in r.items()))
    print(f"\n  order-average OPTION: {avg}")
    print(f"  checks: {checks}")
    print(f"  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("delta-lambda-binding-reading-probe", engine="python", start_time=t0)
    w.set_description(
        "Owner pick '2': the Delta_lambda-weighted binding functional Phi = sum y chi Delta. Three "
        "readings (corpus direct with mass-defect sign, direct with + sign, difference) on the n=2 "
        "projectors and the H_6 gamma-gamma-free template with the interface letter; the structural "
        "source of pn != np (Phi is cyclic and flip-invariant but does not Markov-factorise, so it "
        "sees the in-block mirror of a nucleon word next to the interface). Convention D, proton pin. "
        "No reading is selected by agreement with nature; AME is not used.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("m_e_MeV", fmt(me))
    w.add_data("results", results)
    w.add_data("checks", {k: bool(v) for k, v in checks.items()})
    for k, v in checks.items():
        w.add_assertion(name=k, computed=str(int(bool(v))), expected="1", tolerance="0",
                        source="exact recomputation at the rational q0")
    out = w.save()
    print(f"  witness -> {out}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
