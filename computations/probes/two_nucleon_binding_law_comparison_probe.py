#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational arithmetic at the rational q0, then mpmath at 60 dps.
"""Two-nucleon binding: every candidate LAW evaluated on the SAME channel data.

Owner ask (2026-10-11, "explore all", item 3 "the binding law"). EXPLORE ONLY: no
producer, dashboard or content block is touched, and no law is chosen here.

The working law `B = E_0 ln(tr_free/tr_atom)` is tagged POSITED by the dashboard
(`mass_binding_dashboard.py`: "no block in the corpus licenses alpha*ln(ratio) as an
energy"). This probe asks a narrower question than "which law is right": on the
existing two-nucleon data, WHICH conclusions depend on the law at all?

Laws evaluated (status in the corpus in brackets):

  L_log    B = E_0 ln(tr_free/tr_atom)           [POSITED; B_sym / binding_log_free_energy]
  L_mayer  B = E_0 (1 - mu),  mu = tr_atom/tr_free [two-body term of the multiplicative
                                                    assembly W = 1 - prod f; UrsellPartitionFunctionB3]
  L_diff   B = E_0 (tr_free - tr_atom)            [CONJECTURE: conj:knot-factor-frobenius-pairing]
  L_frob   B = m_e (Phi(free) - Phi(atom)),
           Phi(X) = sum_lam y_lam chi^lam(X) Delta_lam,
           Delta_lam = (-1)^{n(lam)} dim V_lam    [Delta value PROVED (dtEuler_eq_deltaLambda_
                                                    unconditional); the LAW B = m_e sum y chi Delta
                                                    is posited — delta-lambda-witness caveat:
                                                    "value_only ... NOT a binding energy"]
  L_frob_direct  B = m_e Phi(P_T)  (n = 2 only)   [the other reading of the same formula]

Data (convention D, proton pin, exact over Q at the rational q0):

  D1  the n = 2 interface projectors P_+ [T=1], P_- [T=0] (bean qou-kj4v)
  D2  the H_6 template letters sigma_2 + d, d in {0 (pp), -h/2 (pn), -h (nn)}
  D3  the gamma-gamma bond G^3 = (vertex)^3, bare, vertices V1..V4
  D4  the six gamma-gamma x projector compositions C0..C6 of
      gamma_gamma_isospin_channel_probe.py, vertex V1, channels pp/nn/pn/np (T=1), pn/np (T=0)

Every trace is recomputed here from chi^lam and cross-checked against the committed
witnesses (`gamma-gamma-isospin-channel-probe.witness.json`,
`gamma-gamma-nn-pn-selection-probe.witness.json`). AME appears only as a labelled
comparison and feeds nothing.

Lean companion: QOU/Mass/BindingLawClassInvariants.lean.
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
from gamma_gamma_isospin_channel_probe import VERTICES, nucleon  # noqa: E402

DPS = 60
set_compute_dps(DPS)
# BOTH LAYERS MUST CARRY THE SAME q. This was `sp.Rational(Q_50_DIGIT_STR)` while the
# mpmath side below is `Q_MP` (70 digits) -- so the probe computed its H_6 characters and
# Markov weights at one q and its `laws()` arithmetic at another, a 2.13e-50 internal
# straddle. That gap is exactly what broke the three 1e-50 cross-witness checks
# (H6_traces / D2_log / D4_ratios): the values agreed to 48 digits and the tolerance asks
# for 51. Fixed at the producer per the owner's ruling (option D, 2026-11-21), not by
# widening the tolerance -- a bound sized to its own miss is a fit.
with mp.workdps(DPS + 15):
    QV = sp.Rational(mp.nstr(Q_MP, DPS + 10, strip_zeros=False))
S2 = [(2, "sigma")]
PAIRS = ("pp", "pn", "np", "nn")
HERE = Path(__file__).resolve().parent


def to_mp(x) -> mp.mpf:
    num, den = sp.fraction(sp.nsimplify(x) if not isinstance(x, sp.Rational) else x)
    return mp.mpf(int(num)) / mp.mpf(int(den))


def hook_dim(lam) -> int:
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    return factorial(n) // prod


def n_of(lam) -> int:
    return sum(i * r for i, r in enumerate(lam))


def delta(lam) -> int:
    return (-1) ** n_of(lam) * hook_dim(lam)


def _job(args):
    pair, key, word, lam = args
    return pair, key, lam, sp.Rational(q_character_on_braid_word(lam, tuple(word), QV))


def build_words():
    words = []
    for pair in PAIRS:
        W = nucleon(pair[0], 0) + nucleon(pair[1], 3)
        words += [(pair, "W", W), (pair, "W.s", W + S2)]
        for v, vw in VERTICES.items():
            G = vw * 3
            words.append((pair, f"W.G[{v}]", W + G))
            if v == "V1":
                words += [(pair, "W.G.s[V1]", W + G + S2), (pair, "W.s.G[V1]", W + S2 + G),
                          (pair, "W.s.G.s[V1]", W + S2 + G + S2)]
    return words


def laws(tf, ta, pf, pa, E0, me):
    """B under each law; None where a log of a non-positive ratio would be needed."""
    out = {}
    out["L_log"] = E0 * mp.log(tf / ta) if (tf > 0 and ta > 0) else None
    out["L_mayer"] = E0 * (1 - ta / tf)
    out["L_diff"] = E0 * (tf - ta)
    out["L_frob"] = me * (pf - pa)
    return out


def sign(x):
    if x is None:
        return "undefined"
    return "bound" if x > 0 else ("unbound" if x < 0 else "marginal")


#: Relative width below which two law values are reported as TIED rather than ordered.
#: DERIVED from the probe's own arithmetic (DPS = 60, less a 10-digit guard), NOT sized to
#: any observed miss -- a bound sized to its own miss is a fit. The two margins bracket it
#: by a wide gap in both directions, which is what makes it safe:
#:   * the spurious gaps it must absorb are ~1e-61 (round-off),      11 orders BELOW it;
#:   * the smallest genuine gap in this probe is 0.0132 (D3 V3),     48 orders ABOVE it.
#: So no choice inside ~1e-13..1e-58 changes any verdict here.
ORDER_TIE_REL = mp.mpf(10) ** -(DPS - 10)


def order_desc(d):
    """Descending order of the law values, with TIES MADE EXPLICIT as `a = b`.

    The strict-order version of this function made the `log_and_mayer_orders_identical`
    check decide on round-off. At D3 vertices V1 and V2 the `nn` and `pn` values are
    mathematically EQUAL; the committed 50-digit witness had both laws carrying a ~6.6e-61
    residual that happened to point the SAME way, so the check passed by coincidence.
    Closing the Q_MP/sympy straddle left `L_log` with a 3.3e-61 residual while `L_mayer`'s
    became exactly 0.0, so one law broke the tie and the other did not, and the check
    failed -- also by coincidence. A verdict decided at the 61st digit is not a verdict.

    Same class as detector-blindness taxonomy row 59 (a tie-sorted list permuted by a
    precision change at digit ~60), one level up: there the TIE moved, here it is the
    ORDERING OVER a tie that is being compared.
    """
    items = sorted(((k, v) for k, v in d.items() if v is not None), key=lambda kv: -kv[1])
    if not items:
        return ""
    groups = [[items[0]]]
    for k, v in items[1:]:
        ref = groups[-1][0][1]
        scale = max(abs(ref), abs(v))
        if scale == 0 or abs(ref - v) <= ORDER_TIE_REL * scale:
            groups[-1].append((k, v))
        else:
            groups.append([(k, v)])
    return " > ".join(" = ".join(sorted(k for k, _ in g)) for g in groups)


def main() -> int:
    t0 = time.time()
    q = Q_MP
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - 1 / q
    c_q = 1 / (q - 1)
    E0 = me * c_q ** 2 * hbar_q / (1 - hbar_q ** 2)
    z = q ** 3 / (q ** 2 + 1)
    h = q - 1 / q
    s = 1 / (q + 1 / q)
    print(f"two-nucleon binding-law comparison (proton pin, convention D, {DPS} dps)")
    print(f"  q0 = {mp.nstr(q, 20)}  E_0 = {mp.nstr(E0, 15)} MeV  m_e = {mp.nstr(me, 12)} MeV")

    results: dict = {}
    checks: dict = {}

    # ---------------- D1: n = 2 projectors -----------------------------------
    # H_2 characters: chi^(2)(a + b sigma) = a + b q ; chi^(1,1)(a + b sigma) = a - b/q.
    # Markov weights at n = 2: y2 + y11 = 1, q y2 - y11/q = z.
    y2 = (z + 1 / q) / (q + 1 / q)
    y11 = (q - z) / (q + 1 / q)
    mu_p, mu_m = y2, y11       # tr(P_+), tr(P_-)
    phi = {"1": y2 * 1 - y11 * 1}       # Delta_(2) = +1, Delta_(1,1) = -1
    phi["P+"] = y2 * (s / q + s * q) - y11 * (s / q - s / q)
    phi["P-"] = y2 * (s * q - s * q) - y11 * (s * q + s / q)
    D1 = {}
    for name, T, mu, P in (("T1 (P+)", 1, mu_p, "P+"), ("T0 (P-)", 0, mu_m, "P-")):
        L = laws(mp.mpf(1), mu, phi["1"], phi[P], E0, me)
        L["L_frob_direct"] = me * phi[P]
        D1[name] = {"mu": fmt(mu), **{k: fmt(v) for k, v in L.items()},
                    "signs": {k: sign(v) for k, v in L.items()}}
    results["D1_n2_projectors"] = D1
    checks["D1_mu_plus"] = fmt(mu_p)
    checks["D1_mu_sum_is_one"] = bool(abs(mu_p + mu_m - 1) < mp.mpf(10) ** (-55))
    checks["D1_phi_Pplus_eq_y2"] = bool(abs(phi["P+"] - y2) < mp.mpf(10) ** (-55))
    checks["D1_phi_Pminus_eq_minus_y11"] = bool(abs(phi["P-"] + y11) < mp.mpf(10) ** (-55))

    # ---------------- H_6 characters ------------------------------------------
    Y6s = solve_y_lambda(6)
    support = sorted((lam for lam in Y6s if sp.cancel(Y6s[lam]) != 0), key=len)
    y6 = {lam: sp.Rational(sp.cancel(Y6s[lam]).subs(Q, QV)) for lam in support}
    words = build_words()
    jobs = [(p, k, w, lam) for (p, k, w) in words for lam in support]
    print(f"  {len(words)} words x {len(support)} blocks = {len(jobs)} characters ...", flush=True)
    chi: dict = {}
    with Pool(4) as pool:
        for i, (p, k, lam, val) in enumerate(pool.imap_unordered(_job, jobs), 1):
            chi.setdefault(p, {}).setdefault(k, {})[lam] = val
            if i % 20 == 0:
                print(f"    {i}/{len(jobs)}  {time.time() - t0:.0f} s", flush=True)
    tr = {p: {k: to_mp(sum(y6[l] * c[l] for l in support)) for k, c in d.items()} for p, d in chi.items()}
    ph = {p: {k: to_mp(sum(y6[l] * c[l] * delta(l) for l in support)) for k, c in d.items()}
          for p, d in chi.items()}
    results["H6_delta_lambda_on_support"] = {str(l): delta(l) for l in support}

    # cross-checks against committed witnesses
    wi = json.loads((HERE / "gamma-gamma-isospin-channel-probe.witness.json").read_text())
    wn = json.loads((HERE / "gamma-gamma-nn-pn-selection-probe.witness.json").read_text())
    tol = mp.mpf(10) ** (-50)
    ok = True
    for p in PAIRS:
        ok &= abs(tr[p]["W"] - mp.mpf(wn["data"]["binding_with_selected_bond_m3"]["V1"][p]["tr_free"])) < tol
        for v in VERTICES:
            ok &= abs(tr[p][f"W.G[{v}]"]
                      - mp.mpf(wn["data"]["binding_with_selected_bond_m3"][v][p]["tr_atom"])) < tol
    checks["H6_traces_match_nn_pn_witness"] = bool(ok)

    # ---------------- D2: template letters -----------------------------------
    dlet = {"pp": mp.mpf(0), "pn": -h / 2, "np": -h / 2, "nn": -h}
    D2 = {}
    for p in PAIRS:
        tf, pf = tr[p]["W"], ph[p]["W"]
        ta = tr[p]["W.s"] + dlet[p] * tf
        pa = ph[p]["W.s"] + dlet[p] * pf
        L = laws(tf, ta, pf, pa, E0, me)
        D2[p] = {"letter_d": fmt(dlet[p]), "mu": fmt(ta / tf), "mu_minus_z_minus_d": fmt(ta / tf - z - dlet[p]),
                 **{k: fmt(v) for k, v in L.items()}, "signs": {k: sign(v) for k, v in L.items()}}
    D2["order_desc"] = {law: order_desc({p: mp.mpf(D2[p][law]) for p in ("pp", "pn", "nn")})
                        for law in ("L_log", "L_mayer", "L_diff", "L_frob")}
    tmpl = wn["data"]["template_binding_reference_MeV"]
    checks["D2_log_matches_template_witness"] = bool(all(
        abs(mp.mpf(D2[p]["L_log"]) - mp.mpf(tmpl[p])) < tol for p in PAIRS))
    results["D2_template_letters"] = D2

    # ---------------- D3: bare gamma-gamma G^3 -------------------------------
    D3 = {}
    for v in VERTICES:
        D3[v] = {}
        for p in PAIRS:
            tf, ta = tr[p]["W"], tr[p][f"W.G[{v}]"]
            pf, pa = ph[p]["W"], ph[p][f"W.G[{v}]"]
            L = laws(tf, ta, pf, pa, E0, me)
            D3[v][p] = {"mu": fmt(ta / tf), **{k: fmt(vv) for k, vv in L.items()},
                        "signs": {k: sign(vv) for k, vv in L.items()}}
        D3[v]["order_desc"] = {law: order_desc({p: (mp.mpf(D3[v][p][law]) if D3[v][p][law] is not None else None)
                                                 for p in ("pp", "pn", "nn")})
                               for law in ("L_log", "L_mayer", "L_diff", "L_frob")}
    results["D3_gamma_gamma_bare"] = D3

    # ---------------- D4: compositions C0..C6, vertex V1 ----------------------
    def comps(t, T):
        a, b = ((s / q, s) if T == 1 else (s * q, -s))
        W, Ws = t["W"], t["W.s"]
        WG, WGs, WsG, WsGs = t["W.G[V1]"], t["W.G.s[V1]"], t["W.s.G[V1]"], t["W.s.G.s[V1]"]
        WP = a * W + b * Ws
        WGP = a * WG + b * WGs
        WPG = a * WG + b * WsG
        WPGP = a * a * WG + a * b * (WGs + WsG) + b * b * WsGs
        return {"C0_P_only": (WP, W), "C1_G.P_over_W": (WGP, W), "C2_P.G_over_W": (WPG, W),
                "C3_P.G.P_over_W": (WPGP, W), "C4_G.P_over_W.P": (WGP, WP),
                "C5_P.G_over_W.P": (WPG, WP), "C6_P.G.P_over_W.P": (WPGP, WP)}

    channels = [("pp", 1), ("nn", 1), ("pn", 1), ("np", 1), ("pn", 0), ("np", 0)]
    D4 = {}
    match_isospin = True
    for (p, T) in channels:
        ct, cp = comps(tr[p], T), comps(ph[p], T)
        for c in ct:
            ta, tf = ct[c]
            pa, pf = cp[c]
            L = laws(tf, ta, pf, pa, E0, me)
            D4.setdefault(c, {})[f"{p}_T{T}"] = {"mu": fmt(ta / tf), **{k: fmt(v) for k, v in L.items()},
                                                 "signs": {k: sign(v) for k, v in L.items()}}
            ref = wi["data"]["results"].get(f"V1/{c}", {}).get(f"{p}_T{T}")
            if ref is not None:
                match_isospin &= abs(ta / tf - mp.mpf(ref["ratio"])) < tol
    checks["D4_ratios_match_isospin_witness"] = bool(match_isospin)
    results["D4_compositions_V1"] = D4

    # ---------------- law-class invariants (the Lean statements, measured) ---
    # For L_log and L_mayer (both strictly decreasing functions of mu vanishing at mu = 1)
    # the sign is sign(1 - mu) and the channel order is the reverse order of mu.
    agree = True
    for ds in (D2, *D3.values()):
        for p in PAIRS:
            r = ds[p]
            if r["L_log"] is None:
                continue
            for law in ("L_log", "L_mayer"):
                agree &= (r["signs"][law] == r["signs"]["L_log"])
    for c, d in D4.items():
        for k, r in d.items():
            if r["L_log"] is not None:
                agree &= r["signs"]["L_mayer"] == r["signs"]["L_log"]
    checks["log_and_mayer_signs_identical_everywhere"] = bool(agree)
    same_order = all(D2["order_desc"]["L_log"] == D2["order_desc"][l] for l in ("L_mayer",)) and all(
        D3[v]["order_desc"]["L_log"] == D3[v]["order_desc"]["L_mayer"] for v in VERTICES)
    checks["log_and_mayer_orders_identical"] = bool(same_order)
    # under C0 (pure projector decomposition) does ANY law give an unbound channel?
    c0_unbound = {law: [k for k, r in D4["C0_P_only"].items() if r["signs"][law] == "unbound"]
                  for law in ("L_log", "L_mayer", "L_diff", "L_frob")}
    c0_unbound["L_frob_direct(n=2)"] = [k for k, r in D1.items() if r["signs"]["L_frob_direct"] == "unbound"]
    c0_unbound["L_frob(n=2)"] = [k for k, r in D1.items() if r["signs"]["L_frob"] == "unbound"]
    results["unbound_channels_under_pure_projector_decomposition"] = c0_unbound

    # ---------------- print -------------------------------------------------
    def row(lbl, r):
        return (f"    {lbl:<10} mu={mp.nstr(mp.mpf(r['mu']), 12):<16}"
                + "  ".join(f"{k}={mp.nstr(mp.mpf(r[k]), 8) if r[k] is not None else 'undef'}"
                            for k in ("L_log", "L_mayer", "L_diff", "L_frob")))
    print("\n  D1 n=2 projectors [MeV]")
    for k, r in D1.items():
        print(row(k, r) + f"  L_frob_direct={mp.nstr(mp.mpf(r['L_frob_direct']), 8)}")
    print("\n  D2 template letters [MeV]")
    for p in PAIRS:
        print(row(p, D2[p]))
    print(f"    order: {D2['order_desc']}")
    print("\n  D3 bare G^3 [MeV]")
    for v in VERTICES:
        for p in PAIRS:
            print(row(f"{v} {p}", D3[v][p]))
        print(f"    order: {D3[v]['order_desc']}")
    print("\n  D4 compositions, V1 [MeV]")
    for c, d in D4.items():
        print(f"   {c}")
        for k, r in d.items():
            print(row(k, r))
    print(f"\n  unbound under pure projector decomposition: {c0_unbound}")
    print(f"  checks: {checks}")
    print(f"  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("two-nucleon-binding-law-comparison-probe", engine="python", start_time=t0)
    w.set_description(
        "Owner ask 'explore all' item 3: every candidate two-nucleon binding law (log-ratio, "
        "Mayer two-body, trace difference, Delta_lambda-weighted Frobenius functional) evaluated on "
        "the same exact channel data (n=2 projectors, H_6 template letters, bare gamma-gamma G^3 at "
        "four vertices, the six gamma-gamma x projector compositions). Convention D, proton pin. No law "
        "is chosen; AME is not used.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_parameter("m_e_MeV", fmt(me))
    w.add_parameter("laws", {
        "L_log": "E_0 ln(tr_free/tr_atom) [POSITED]",
        "L_mayer": "E_0 (1 - tr_atom/tr_free) [two-body term of W = 1 - prod f]",
        "L_diff": "E_0 (tr_free - tr_atom) [conj:knot-factor-frobenius-pairing]",
        "L_frob": "m_e (Phi(free) - Phi(atom)), Phi = sum y chi Delta [Delta proved; law posited]",
        "L_frob_direct": "m_e Phi(P_T), n = 2 only"})
    w.add_data("results", results)
    w.add_data("checks", {k: (v if isinstance(v, str) else bool(v)) for k, v in checks.items()})
    w.add_data("ame_comparison_labelled_only", {"B_2H_MeV": "2.224566", "pp": "unbound", "nn": "unbound"})
    for k, v in checks.items():
        if isinstance(v, bool):
            w.add_assertion(name=k, computed=str(int(v)), expected="1", tolerance="0",
                            source="exact recomputation at the rational q0")
    out = w.save()
    print(f"  witness -> {out}")
    return 0 if all(v for v in checks.values() if isinstance(v, bool)) else 1


if __name__ == "__main__":
    sys.exit(main())
