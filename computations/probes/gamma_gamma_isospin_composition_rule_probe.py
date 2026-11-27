#!/usr/bin/env python3
"""
qou-ales x qou-kj4v, follow-up to gamma_gamma_isospin_channel_probe.py — does the corpus
DERIVE a composition rule for the isospin projector P_T and the gamma-gamma bond G?

OWNER ASK (2026-10-11, "explore all", item 1). The previous probe computed six compositions
C1..C6 of P_T and G = (s2 s3^-1)^3. Only C5 (W.P.G over W.P) gives the physical sign pattern,
and it differs from the inverted C4 (W.G.P over W.P) only in the order of P and G. Picking C5
for its signs would be selection against the target (AGENTS.md section NO FITTING). This probe
asks whether anything in the corpus fixes the order, the normalisation, or a symmetric form.

WHAT IS TESTED
--------------
1. Commutation. P_T = a + b s2 with b != 0, so [P_T, G] = b [s2, G]. tr(W [s2, G]) is computed
   for every species; if it vanished, every ordering would agree. (The 2x2 statement that
   [s2, G] != 0 in the (2,1) block is QOU/Mass/IsospinBondCompositionOrientation.lean.)
2. Orientation. The Markov trace is invariant under the word-reversal anti-automorphism
   iota (s_i -> s_i, products reversed): tr(iota x) = tr(x). With iota(P_T) = P_T and
   cyclicity this gives, exactly,
        tr(W P G) = tr(iota(W) iota(G) P)      tr(W P) = tr(iota(W) P)
   so  C5(W, G) = C4(iota W, iota G)  and  C1(W, G) = C2(iota W, iota G).
   The order of P and G is therefore the same choice as the READING ORIENTATION of the
   nucleon words and the vertex. The bare functional B = E0 ln(tr W / tr W G) is
   orientation-blind (tr(iota(W G)) = tr(G W) = tr(W G)); an asymmetric composition is not.
   Verified here by computing the reversed traces directly.
3. Candidate rules, all computed and none chosen:
     S1  (PG + GP)/2 over W          S2  (PG + GP)/2 over W.P
     C3  P G P over W                C6  P G P over W.P     (Lueders compression)
     K1  G P G^-1 over W             K2  G P G^-1 over W.P
     K3  G^-1 P G over W             K4  G^-1 P G over W.P
     K5  (G P G^-1 + G^-1 P G)/2 over W      K6  same over W.P
   and C1, C2, C4, C5 for reference. S1, S2, C3, C6, K5, K6 are iota-covariant: a rule R with
   R(W, G) = R(iota W, iota G), because iota fixes P and maps G P G^-1 to (iota G)^-1 P iota G.
   C1, C2, C4, C5, K1..K4 are not: under iota they map pairwise onto each other.

## Precision
Exact sympy over Q(q) (convention D, y_lambda solved symbolically); mpmath 60 dps for MeV.
No float64. AME2020 appears only as a labelled comparison and feeds nothing.

## Cost
52 symbolic H_6 traces, ~15 min on 4 cores.
"""
from __future__ import annotations

import sys
import time
from multiprocessing import Pool
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "computations/probes", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402
from markov_weights_symbolic import solve_y_lambda  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)

S2 = [(2, "sigma")]
V1 = [(2, "sigma"), (3, "sigma_inv")]        # canonical gamma-gamma vertex
V1_INV = [(3, "sigma"), (2, "sigma_inv")]    # group inverse = V2 of the previous probe
G = V1 * 3
GINV = V1_INV * 3
PAIRS = ("pp", "pn", "np", "nn")


def nucleon(kind: str, g0: int) -> list[tuple[int, str]]:
    """Canonical 11-letter nucleon element (identical to gamma_gamma_isospin_channel_probe)."""
    g1 = g0 + 1
    w: list[tuple[int, str]] = []
    for _ in range(3):
        w += [(g0, "sigma"), (g1, "sigma_inv")]
    if kind == "p":
        w += [(g0, "sigma"), (g0, "averaged"), (g1, "averaged")]
    else:
        w += [(g0, "averaged"), (g0, "averaged"), (g1, "sigma_inv")]
    w += [(g0, "sigma"), (g0, "sigma")]
    return w


def rev(word):
    """iota: reverse the word, keep every letter (s -> s, s^-1 -> s^-1, averaged -> averaged)."""
    return list(reversed(word))


_Y6 = None
_SUPPORT = None


def _init():
    global _Y6, _SUPPORT
    _Y6 = solve_y_lambda(6)
    _SUPPORT = sorted((lam for lam in _Y6 if sp.cancel(_Y6[lam]) != 0), key=len)


def _job(args):
    pair, key, word = args
    tot = sp.Integer(0)
    for lam in _SUPPORT:
        tot += sp.cancel(_Y6[lam] * sp.cancel(chi_lambda_symbolic(lam, word)))
    return pair, key, sp.cancel(sp.together(tot))


def build_jobs():
    jobs = []
    rG = rev(G)
    for pair in PAIRS:
        W = nucleon(pair[0], 0) + nucleon(pair[1], 3)
        rW = rev(W)
        words = {
            "W": W, "Ws": W + S2, "WG": W + G, "WGs": W + G + S2, "WsG": W + S2 + G,
            "WsGs": W + S2 + G + S2,
            "rW": rW, "rWs": rW + S2, "rWrG": rW + rG, "rWrGs": rW + rG + S2,
            "rWsrG": rW + S2 + rG,
            "WGsGi": W + G + S2 + GINV, "WGisG": W + GINV + S2 + G,
        }
        jobs += [(pair, k, w) for k, w in words.items()]
    return jobs


def main() -> int:
    t0 = time.time()
    q = Q_MP
    qv = sp.Rational(Q_50_DIGIT_STR)
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - 1 / q
    c_q = 1 / (q - 1)
    E0 = me * c_q ** 2 * hbar_q / (1 - hbar_q ** 2)
    print(f"gamma-gamma x isospin COMPOSITION-RULE probe (proton pin, {DPS} dps)", flush=True)
    print(f"  q_0 = {mp.nstr(q, 20)};  E_0^full = {mp.nstr(E0, 12)} MeV", flush=True)

    jobs = build_jobs()
    t: dict[str, dict[str, sp.Expr]] = {p: {} for p in PAIRS}
    with Pool(4, initializer=_init) as pool:
        for i, (pair, key, expr) in enumerate(pool.imap_unordered(_job, jobs), 1):
            t[pair][key] = expr
            print(f"  [{i:>2}/{len(jobs)}] {pair} {key:<7} {time.time() - t0:7.1f}s", flush=True)

    def num(e):
        return mp.mpf(str(sp.N(sp.sympify(e).subs(Q, qv), DPS + 15)))

    qi = 1 / Q
    s = 1 / (Q + qi)
    checks: dict[str, object] = {}
    results: dict[str, dict] = {}

    # --- structural checks -------------------------------------------------------------
    comm = {}
    orient = {}
    for pair in PAIRS:
        tt = t[pair]
        c = sp.cancel(tt["WsG"] - tt["WGs"])          # tr(W [s2, G])
        comm[pair] = c
        orient[pair] = {
            "tr_iotaW_eq_trW": sp.cancel(tt["rW"] - tt["W"]) == 0,
            "tr_iotaW_s_eq_trWs": sp.cancel(tt["rWs"] - tt["Ws"]) == 0,
            "tr_iota(WG)_eq_trWG": sp.cancel(tt["rWrG"] - tt["WG"]) == 0,
            # tr(W s G) = tr(iotaW iotaG s)   [=> C5(W,G) = C4(iotaW, iotaG)]
            "WsG_eq_rWrGs": sp.cancel(tt["WsG"] - tt["rWrGs"]) == 0,
            # tr(W G s) = tr(iotaW s iotaG)   [=> C1(W,G) = C2(iotaW, iotaG)]
            "WGs_eq_rWsrG": sp.cancel(tt["WGs"] - tt["rWsrG"]) == 0,
        }
    checks["commutator_trace_nonzero_all_pairs"] = all(c != 0 for c in comm.values())
    checks["commutator_trace_values"] = {p: fmt(num(c)) for p, c in comm.items()}
    checks["orientation_identities"] = {p: {k: bool(v) for k, v in d.items()}
                                        for p, d in orient.items()}

    # --- candidate rules ----------------------------------------------------------------
    for T in (1, 0):
        a, b = ((s * qi, s) if T == 1 else (s * Q, -s))
        for pair in PAIRS:
            tt = t[pair]
            W, Ws = tt["W"], tt["Ws"]
            WG, WGs, WsG, WsGs = tt["WG"], tt["WGs"], tt["WsG"], tt["WsGs"]
            WP = a * W + b * Ws
            WGP = a * WG + b * WGs
            WPG = a * WG + b * WsG
            WPGP = a * a * WG + a * b * (WGs + WsG) + b * b * WsGs
            WK1 = a * W + b * tt["WGsGi"]                 # tr(W G P G^-1)
            WK3 = a * W + b * tt["WGisG"]                 # tr(W G^-1 P G)
            rules = {
                "C1_G.P/W": (WGP, W), "C2_P.G/W": (WPG, W),
                "C4_G.P/W.P": (WGP, WP), "C5_P.G/W.P": (WPG, WP),
                "S1_(PG+GP)/2/W": ((WGP + WPG) / 2, W),
                "S2_(PG+GP)/2/W.P": ((WGP + WPG) / 2, WP),
                "C3_PGP/W": (WPGP, W), "C6_PGP/W.P": (WPGP, WP),
                "K1_GPGinv/W": (WK1, W), "K2_GPGinv/W.P": (WK1, WP),
                "K3_GinvPG/W": (WK3, W), "K4_GinvPG/W.P": (WK3, WP),
                "K5_symconj/W": ((WK1 + WK3) / 2, W), "K6_symconj/W.P": ((WK1 + WK3) / 2, WP),
            }
            for lab, (ta, tf) in rules.items():
                tav, tfv = num(ta), num(tf)
                B = E0 * mp.log(abs(tfv) / abs(tav))
                results.setdefault(lab, {})[f"{pair}_T{T}"] = {
                    "ratio": fmt(tav / tfv), "B_MeV": fmt(B),
                    "sign": "bound" if B > 0 else ("unbound" if B < 0 else "zero"),
                    "trace_signs": f"{'+' if tav > 0 else '-'}/{'+' if tfv > 0 else '-'}",
                }

    # physically-labelled channels only
    show = ["pp_T1", "nn_T1", "pn_T1", "np_T1", "pn_T0", "np_T0"]
    for lab, row in results.items():
        line = "  ".join(f"{ch}={mp.nstr(mp.mpf(row[ch]['B_MeV']) * 1000, 6):>9}" for ch in show)
        print(f"  {lab:<20} [keV] {line}")
    print(f"\n  checks: commutator nonzero = {checks['commutator_trace_nonzero_all_pairs']}")
    for p, d in checks["orientation_identities"].items():
        print(f"    {p}: {d}")
    print(f"  wall {time.time() - t0:.1f} s", flush=True)

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-isospin-composition-rule-probe", engine="python", start_time=t0)
    w.set_description(
        "Owner ask 'explore all' item 1: does the corpus derive a composition rule for the "
        "isospin projector P_T and the gamma-gamma bond G = (s2 s3^-1)^3? Tests (i) commutation "
        "(tr(W[s2,G]) per species), (ii) the word-reversal anti-automorphism iota, under which "
        "C5(W,G) = C4(iota W, iota G) and C1(W,G) = C2(iota W, iota G) exactly, and (iii) "
        "fourteen candidate rules incl. symmetric, compressed and conjugated forms, over both "
        "normalisations. None is chosen by agreement with nature. B = E_0^full ln(|tr_free|/"
        "|tr_atom|), convention D, proton pin, exact over Q(q).")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_parameter("vertex", "V1 = s2 s3^-1 ; G = V1^3 ; G^-1 = (s3 s2^-1)^3")
    w.add_parameter("projectors", "P+ = (s2 + 1/q)/(q+1/q) [T=1]; P- = (q - s2)/(q+1/q) [T=0]")
    w.add_data("results", results)
    w.add_data("checks", checks)
    w.add_data("ame_comparison_labelled_only", {
        "pn_T0": "deuteron B = +2.224566 MeV (bound)",
        "pp_T1": "diproton unbound", "nn_T1": "dineutron unbound"})
    w.add_assertion(name="commutator_trace_nonzero_all_pairs",
                    computed=str(int(bool(checks["commutator_trace_nonzero_all_pairs"]))),
                    expected="1", tolerance="0", source="exact symbolic over Q(q)")
    allor = all(all(d.values()) for d in orient.values())
    w.add_assertion(name="orientation_identities_hold_all_pairs", computed=str(int(allor)),
                    expected="1", tolerance="0", source="exact symbolic over Q(q)")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
