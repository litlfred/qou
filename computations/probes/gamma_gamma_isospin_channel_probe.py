#!/usr/bin/env python3
"""
qou-ales x qou-kj4v — combine the gamma-gamma-selected interface bond with the isospin
projectors, and see whether the channel label T fixes the two-nucleon ordering.

OWNER ASK (2026-10-11, "try 1"): combine the gamma-gamma-selected bond with the isospin
projectors to fix the two-nucleon ordering.

THE TWO INGREDIENTS (both on `main`, cited, not re-derived)
-----------------------------------------------------------
* The gamma-gamma bond. The owner ruling (bean qou-ales) selects bonds by gamma-gamma pair
  production plus confinement-SDP reading 3. On the H_6 interface it selects
  G^3 = (s2 s3^-1)^3 (steps 6-7), and under B = E_0 ln(tr_M(W_free)/tr_M(W_atom)) the
  diproton is UNBOUND by 4.469 keV (step 3; closed form step 10). Step 11: the response is
  ONE-BODY at every placement -- it depends only on the nucleon the vertex borrows a
  generator from, by connected-sum multiplicativity across the single shared strand.
* The isospin projectors of the interface generator s2 (eigenvalues q, -1/q):
      P+ = (s2 + q^-1)/(q + q^-1)   T = 1   (pp, nn, pn-singlet)
      P- = (q - s2)/(q + q^-1)      T = 0   (the deuteron)
  P+ + P- = 1 (InterfaceScalar.proj_add_eq_one), so mu+ + mu- = 1 and both channels bind
  (bean qou-kj4v).

NO CORPUS COMPOSITION EXISTS
----------------------------
A grep of docs/audits, beans/defs and computations/probes for the gamma-gamma bond together
with the projectors finds no composition rule. So every natural composition is computed and
reported, and NONE is chosen by agreement with nature:

  free reference W = W_L W_R (disjoint-union, no bond):
    C1  atom = W . G . P_T          the bond letter becomes "gamma-gamma bond, projected"
    C2  atom = W . P_T . G          same, opposite order
    C3  atom = W . P_T . G . P_T    the bond compressed into channel T
  free reference W . P_T (the channel is part of the free state; G is the only bond):
    C4  atom = W . G . P_T
    C5  atom = W . P_T . G
    C6  atom = W . P_T . G . P_T
  and, as the consistency baseline, C0: atom = W . P_T, free = W  (the projector alone).

Each over the four interface vertices of step 11 (V1 = s2 s3^-1 canonical; V2 = V1^-1;
V3 = s1 s2^-1; V4 = V3^-1), G = V^3, and the four ordered species (pp, pn, np, nn). By
linearity every composition is a combination of the six traces
    tr(W), tr(W s2), tr(W G), tr(W G s2), tr(W s2 G), tr(W s2 G s2).

## Precision
Exact sympy over Q(q), convention-D weights solved symbolically; mpmath at 60 dps for the
MeV values. No float64 anywhere. AME2020 values appear ONLY as a labelled comparison column
and feed nothing.

## Cost
72 symbolic H_6 traces (4 live blocks each), ~10-20 min on 4 cores.
"""
from __future__ import annotations

import sys
import time
from multiprocessing import Pool
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python"):
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
VERTICES = {
    "V1": [(2, "sigma"), (3, "sigma_inv")],   # canonical (GammaGammaH6Interface.interfaceBond)
    "V2": [(3, "sigma"), (2, "sigma_inv")],
    "V3": [(1, "sigma"), (2, "sigma_inv")],
    "V4": [(2, "sigma"), (1, "sigma_inv")],
}
PAIRS = ("pp", "pn", "np", "nn")


def nucleon(kind: str, g0: int) -> list[tuple[int, str]]:
    """The canonical 11-letter nucleon element on generators (g0, g0+1) (as step 11)."""
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
    for pair in PAIRS:
        W = nucleon(pair[0], 0) + nucleon(pair[1], 3)
        jobs.append((pair, "W", W))
        jobs.append((pair, "W.s", W + S2))
        for v, vw in VERTICES.items():
            G = vw * 3
            jobs.append((pair, f"W.G[{v}]", W + G))
            jobs.append((pair, f"W.G.s[{v}]", W + G + S2))
            jobs.append((pair, f"W.s.G[{v}]", W + S2 + G))
            jobs.append((pair, f"W.s.G.s[{v}]", W + S2 + G + S2))
    return jobs


def compositions(t: dict, v: str, T: int):
    """Return {label: (tr_atom, tr_free)} as exact rational functions of Q."""
    qi = 1 / Q
    s = 1 / (Q + qi)
    # P_T as (a, b): P_T = a*1 + b*s2
    a, b = ((s * qi, s) if T == 1 else (s * Q, -s))
    W, Ws = t["W"], t["W.s"]
    WG, WGs = t[f"W.G[{v}]"], t[f"W.G.s[{v}]"]
    WsG, WsGs = t[f"W.s.G[{v}]"], t[f"W.s.G.s[{v}]"]
    WP = a * W + b * Ws
    WGP = a * WG + b * WGs
    WPG = a * WG + b * WsG
    WPGP = a * a * WG + a * b * (WGs + WsG) + b * b * WsGs
    return {
        "C0_P_only": (WP, W),
        "C1_G.P_over_W": (WGP, W),
        "C2_P.G_over_W": (WPG, W),
        "C3_P.G.P_over_W": (WPGP, W),
        "C4_G.P_over_W.P": (WGP, WP),
        "C5_P.G_over_W.P": (WPG, WP),
        "C6_P.G.P_over_W.P": (WPGP, WP),
        "Gbare_over_W": (WG, W),
    }


# Channel assignments: T = 1 for pp, nn and the pn singlet; T = 0 for the pn deuteron.
CHANNELS = [("pp", 1), ("nn", 1), ("pn", 1), ("np", 1), ("pn", 0), ("np", 0)]
AME_COMPARISON = {  # labelled comparison only; feeds nothing
    ("pn", 0): "deuteron B = +2.224566 MeV (bound)",
    ("pp", 1): "diproton unbound (no bound state)",
    ("nn", 1): "dineutron unbound (no bound state)",
}


def main() -> int:
    t0 = time.time()
    q = Q_MP
    # Same straddle as two_nucleon_binding_law_comparison_probe: the mpmath side is
    # Q_MP (70 digits) and this sympy side was the 50-digit string, a 2.13e-50 gap
    # inside one computation. Owner ruling option D, 2026-11-21.
    with mp.workdps(DPS + 15):
        qv = sp.Rational(mp.nstr(Q_MP, DPS + 10, strip_zeros=False))
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - 1 / q
    c_q = 1 / (q - 1)
    E0 = me * c_q ** 2 * hbar_q / (1 - hbar_q ** 2)
    print(f"gamma-gamma x isospin channel probe (proton pin, {DPS} dps)")
    print(f"  q_0 = {mp.nstr(q, 20)};  E_0^full = {mp.nstr(E0, 12)} MeV")

    jobs = build_jobs()
    with Pool(4, initializer=_init) as pool:
        t: dict[str, dict[str, sp.Expr]] = {p: {} for p in PAIRS}
        for i, (pair, key, expr) in enumerate(pool.imap_unordered(_job, jobs), 1):
            t[pair][key] = expr
            print(f"  [{i:>2}/{len(jobs)}] {pair} {key:<16} {time.time() - t0:7.1f}s", flush=True)

    def num(e):
        return mp.mpf(str(sp.N(e.subs(Q, qv), DPS + 15)))

    # --- checks ---------------------------------------------------------------------------
    checks = {}
    # step-3 reproduction: pp, V1, bare ratio
    r_pp = num(t["pp"]["W.G[V1]"] / t["pp"]["W"])
    checks["step3_ratio_reproduced"] = fmt(r_pp)
    # C0 is nucleon-blind and equals (z+1/q)/(q+1/q), (q-z)/(q+1/q)
    z = Q ** 3 / (Q ** 2 + 1)
    s = 1 / (Q + 1 / Q)
    mu_plus_th = sp.cancel(s * (z + 1 / Q))
    mu_minus_th = sp.cancel(s * (Q - z))

    results = {}
    identities = {}
    print(f"\n  step-3 pp ratio (V1, no projector) = {mp.nstr(r_pp, 20)}  (expect 1.00105775254515984)")
    for v in VERTICES:
        comp = {pair: {T: compositions(t[pair], v, T) for T in (0, 1)} for pair in PAIRS}
        for label in comp["pp"][1]:
            mus = {}
            for pair, T in CHANNELS:
                ta, tf = comp[pair][T][label]
                mus[(pair, T)] = sp.cancel(ta / tf)
            # exact identities
            ci = sp.simplify(mus[("pp", 1)] - mus[("nn", 1)]) == 0
            blind = all(sp.simplify(mus[(p, 1)] - mus[("pp", 1)]) == 0 for p in ("nn", "pn", "np"))
            pn_np_T1 = sp.simplify(mus[("pn", 1)] - mus[("np", 1)]) == 0
            pn_np_T0 = sp.simplify(mus[("pn", 0)] - mus[("np", 0)]) == 0
            identities[f"{v}/{label}"] = {
                "pp_eq_nn_exact": ci, "T1_nucleon_blind": blind,
                "pn_eq_np_T1": pn_np_T1, "pn_eq_np_T0": pn_np_T0,
                "pp_eq_np_T1": sp.simplify(mus[("pp", 1)] - mus[("np", 1)]) == 0,
                "nn_eq_pn_T1": sp.simplify(mus[("nn", 1)] - mus[("pn", 1)]) == 0,
            }
            row = {}
            for (pair, T), mu in mus.items():
                if label == "Gbare_over_W" and T == 0:
                    continue  # no channel label without a projector
                ta, tf = comp[pair][T][label]
                tav, tfv = num(ta), num(tf)
                muv = tav / tfv
                B = E0 * mp.log(abs(tfv) / abs(tav))
                row[f"{pair}_T{T}"] = {
                    "tr_atom": fmt(tav), "tr_free": fmt(tfv), "ratio": fmt(muv),
                    "B_MeV": fmt(B), "sign": "bound" if B > 0 else ("unbound" if B < 0 else "zero"),
                    "trace_signs": f"{'+' if tav > 0 else '-'}/{'+' if tfv > 0 else '-'}",
                }
            results[f"{v}/{label}"] = row
        if v == "V1":
            c0 = {pair: sp.cancel(comp[pair][1]["C0_P_only"][0] / comp[pair][1]["C0_P_only"][1])
                  for pair in PAIRS}
            c0m = {pair: sp.cancel(comp[pair][0]["C0_P_only"][0] / comp[pair][0]["C0_P_only"][1])
                   for pair in PAIRS}
            checks["C0_T1_equals_mu_plus_all_pairs"] = all(
                sp.simplify(c0[p] - mu_plus_th) == 0 for p in PAIRS)
            checks["C0_T0_equals_mu_minus_all_pairs"] = all(
                sp.simplify(c0m[p] - mu_minus_th) == 0 for p in PAIRS)
            # C1 sum rule: mu+(C1) + mu-(C1) = mu_G (bare)
            checks["C1_sum_rule_mu_plus_plus_mu_minus_eq_mu_G"] = all(
                sp.simplify(sp.cancel(comp[p][1]["C1_G.P_over_W"][0] / t[p]["W"])
                            + sp.cancel(comp[p][0]["C1_G.P_over_W"][0] / t[p]["W"])
                            - sp.cancel(t[p]["W.G[V1]"] / t[p]["W"])) == 0 for p in PAIRS)

    # --- printout ---------------------------------------------------------------------------
    for key, row in results.items():
        print(f"\n  {key}   identities: {identities[key]}")
        for ch, d in row.items():
            print(f"     {ch:>6}  ratio {mp.nstr(mp.mpf(d['ratio']), 14):>20}  "
                  f"B = {mp.nstr(mp.mpf(d['B_MeV']), 10):>16} MeV  {d['sign']:<8} traces {d['trace_signs']}")
    print(f"\n  checks: {checks}")
    print(f"  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-isospin-channel-probe", engine="python", start_time=t0)
    w.set_description(
        "Owner ask 'try 1': combine the gamma-gamma-selected interface bond G = V^3 (qou-ales) "
        "with the isospin projectors P+/P- of the interface generator s2 (qou-kj4v). No corpus "
        "composition rule exists, so six natural compositions (C1-C3 against the bare free word "
        "W, C4-C6 against the channel-projected free word W.P_T) over four vertices and four "
        "ordered species are all computed exactly over Q(q), convention D, and none is chosen "
        "by agreement with nature. B = E_0^full ln(|tr_free|/|tr_atom|). AME values appear only "
        "as a labelled comparison.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_parameter("E_0_register_name", "E_0^full = m_e c_q^2 hbar_q/(1-hbar_q^2)")
    w.add_parameter("projectors", "P+ = (s2 + 1/q)/(q+1/q) [T=1]; P- = (q - s2)/(q+1/q) [T=0]")
    w.add_parameter("vertices", {k: str(v) for k, v in VERTICES.items()})
    w.add_data("results", results)
    w.add_data("identities", {k: {kk: bool(vv) for kk, vv in d.items()} for k, d in identities.items()})
    w.add_data("checks", {k: (v if isinstance(v, str) else bool(v)) for k, v in checks.items()})
    w.add_data("ame_comparison_labelled_only", {f"{p}_T{T}": s_ for (p, T), s_ in AME_COMPARISON.items()})
    w.add_assertion(name="step3_pp_ratio_reproduced", computed=checks["step3_ratio_reproduced"][:22],
                    expected="1.00105775254515984365"[:22], tolerance="0",
                    source="gamma_gamma_h3_psd_selector_probe pp G^3 row")
    for k in ("C0_T1_equals_mu_plus_all_pairs", "C0_T0_equals_mu_minus_all_pairs",
              "C1_sum_rule_mu_plus_plus_mu_minus_eq_mu_G"):
        w.add_assertion(name=k, computed=str(int(bool(checks[k]))), expected="1", tolerance="0",
                        source="exact symbolic identity over Q(q)")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
