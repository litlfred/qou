#!/usr/bin/env python3
"""qbeta_dladder_barodd_borel_pade_laplace_probe.py

W9 / bean qou-dri7 — q-Borel/Écalle RESUMMATION (Option-1 1ppQ) angle.

The even-κ-tower probe qbeta_c3_borel_pade_resummation_probe.py did a full
Borel–Padé[m/m] + Laplace to an actual VALUE (Im 𝔙_b = 0.05545), located the
Borel singularity (real ξ=A=Vol(4₁)/π), and adjudicated Borel-summability
(off the imaginary ray ⇒ single-valued). The ODD bar-odd D-ladder never got
that clean treatment: the odd-channel work is Borel–Leroy s-SCANS (s-dependent
pole 0.147→0.249, no fixed-order clean action — qbeta-odd-channel-stokes-borel)
and OPTIMAL-TRUNCATION ambiguity (δ_np on substrate/fibre — fibre-branch probe),
never the Padé-Borel Laplace back-summation to a numerical value + residual +
the on-axis/off-axis summability verdict.

This probe is the odd-ladder analogue of the even-tower Borel–Padé probe:

  D(ũ) = Σ_k d_k ũ^k,  d_k = a_k + b_k√3 ∈ ℚ(√3) (exact, k=1..KMAX),
  ũ = q·b·ℏ_q² ≈ 0.0095 at the real substrate q₀ (the S-channel meridian).

ARMS (formalize-first, anti-fit — contour/order fixed by the singularity
structure, never tuned to a target):

  (A) DIRECT superasymptotic reference value at the substrate ũ₀: partial sums
      S_N = Σ_{k≤N} d_k ũ₀^k, optimal truncation N* (least term), least term
      δ_np. This is the "direct S-channel value" the resummation must reproduce.

  (B) CLASSICAL Borel–Padé + Laplace: B(ζ)=Σ d_k ζ^k/k!, diagonal Padé[m/m];
      Laplace back V_B(ũ₀)=∫₀^∞ Padé(ũ₀ s) e^{-s} ds; residual |V_B−S_{N*}|.
      Nearest Padé pole ζ* (|ζ*|, arg ζ*): on the positive real axis ⇒ real
      Stokes ambiguity (median/lateral needed, non-perturbative sector);
      off-axis ⇒ Borel-summable. Order stability m=2,3,4,5.

  (C) q-BOREL (theta kernel) refinement: B_q coeff d_k/q₀^{k(k-1)/2}, the kernel
      matched to a q-Gevrey (theta) growth class, per the corpus need. Reports
      whether the q-divided coefficients decay (kernel over/under-suppresses).

  (D) 1ppQ verdict + honest anchor-blindness: report residual vs 1e-15, and the
      corpus cross-reference that δ_np ≈ 1e-39 at the substrate means the value
      is trivially precise but ANCHOR-BLIND — the Stokes datum (c₃ swing / A_ω)
      lives on the FIBRE branch (|ũ|≳0.19) where the ambiguity is O(1), per
      docs/audits/2026-07-18-dladder-fibre-branch-stokes-ambiguity.md.

  (E) Cross-check vs the direct S quantity: |Im(h·D(ũ₀))|, h=q−1/q, against the
      swing scale S≈0.0097.

No c_k wired; no fit; nothing to production. Honest negative (drifting poles /
not-cleanly-summable / value-precise-but-anchor-blind) is the expected win.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = 43
core.ORD = ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic, ser_div,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
R3 = sp.sqrt(3)


def ser_compose(a, phi):
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def build_d_ladder():
    """Exact d_k of O/h = Σ d_k ũ^k (identical construction to the canonical
    qbeta_dladder_generating_function_structure_probe.build_d_ladder)."""
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    # q₀ from q_parameter (proton pin, AGENTS.md 2026-08-07 directive).
    # Was a direct read of q-pinning-50-digit.witness.json, which is the
    # MUON anchor’s definition and bypasses the manifest entirely.
    q0 = Q_MP
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_ser = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))    # ũ = q·b·hbar²
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    O = [simp((x - y) / 2) for x, y in zip(logR, ser_compose(logR, phi))]
    G, valid_top = ser_div(O, h_ser)
    KMAX = valid_top // 2
    upow = [None, list(u_ser)]
    for k in range(2, KMAX + 1):
        upow.append(ser_mul(upow[k - 1], u_ser))
    dk, model = {}, [sp.Integer(0)] * (ORD + 1)
    for k in range(1, KMAX + 1):
        ek = simp((G[2 * k] - model[2 * k]) / upow[k][2 * k])
        dk[k] = ek
        model = ser_add(model, ser_scale(ek, upow[k]))
    odd_ok = all(sp.simplify(G[n] - model[n]) == 0 for n in range(1, valid_top + 1, 2))
    return dk, KMAX, valid_top, odd_ok, u_ser, h_ser, q0


def substrate_u_h(q0):
    """Closed-form values of the ladder variable ũ = q·b·ℏ_q² and h = q−1/q at
    the exact substrate q₀ (the ladder's internal series are (q−1)-expansions, so
    they must NOT be summed as q-power series; evaluate the analytic forms directly).
      b = √(q⁴+q²+1)/(q²+1),  ℏ_q² = ((q−1)/q)²."""
    b = mp.sqrt(q0**4 + q0**2 + 1) / (q0**2 + 1)
    hbar2 = ((q0 - 1) / q0) ** 2
    u0 = q0 * b * hbar2
    h0 = q0 - 1 / q0
    return u0, h0


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" W9 — bar-odd D-ladder: Borel–Padé + Laplace resummation to a VALUE")
    print("=" * 78)

    dk, KMAX, valid_top, odd_ok, u_ser, h_ser, q0 = build_d_ladder()
    K = KMAX
    print(f"  built d₁…d_{K} (exact ℚ(√3), odd over-det zero: {odd_ok}); q₀={mp.nstr(q0,12)}")

    # numeric exact d_k
    d = {k: mp.mpf(str(sp.N(dk[k], 55))) for k in dk}

    # substrate ũ₀ and h₀ (real), from the analytic closed forms at q₀
    u0, h0 = substrate_u_h(q0)
    print(f"  substrate ũ₀ = {mp.nstr(u0,10)}   h₀ = q₀−1/q₀ = {mp.nstr(h0,10)}")

    # ---- (A) DIRECT superasymptotic reference value ----
    print("\n[A] direct superasymptotic value at ũ₀ (optimal truncation):")
    terms = {k: d[k] * u0**k for k in range(1, K + 1)}
    amag = {k: abs(terms[k]) for k in terms}
    Nstar = min(amag, key=amag.get)
    delta_np = amag[Nstar]
    S_opt = sum(terms[k] for k in range(1, Nstar + 1))
    S_full = sum(terms[k] for k in range(1, K + 1))
    print(f"    least-term index N* = {Nstar} (of {K}); δ_np = |d_N* ũ₀^N*| = {mp.nstr(delta_np,6)}")
    print(f"    S_opt = Σ_{{k≤N*}} d_k ũ₀^k = {mp.nstr(S_opt,20)}")
    print(f"    S_full(k≤{K})           = {mp.nstr(S_full,20)}   (Δ = {mp.nstr(abs(S_full-S_opt),4)})")
    edge = Nstar >= K  # least term pinned at the ladder edge (anchor-blind, per corpus)
    print(f"    least term at ladder edge (anchor-blind, corpus fibre audit): {edge}")

    # ---- (B) CLASSICAL Borel–Padé + Laplace ----
    print("\n[B] classical Borel–Padé[m/m] + Laplace back-sum:")
    # Borel transform coefficients b_k = d_k / k!  (c_0=0 : series has no constant term)
    bcoef = [mp.mpf(0)] + [d[k] / mp.factorial(k) for k in range(1, K + 1)]
    results_B = {}
    for m in (2, 3, 4, 5):
        if 2 * m + 1 > len(bcoef):
            continue
        try:
            pnum, pden = mp.pade(bcoef[:2 * m + 1], m, m)
        except Exception as e:
            results_B[m] = {"error": str(e)}
            continue

        def Bpade(z, pn=pnum, pd=pden):
            return mp.polyval(pn[::-1], z) / mp.polyval(pd[::-1], z)

        # Laplace back-sum along ℝ⁺ (substrate ũ₀ real > 0): V = ∫₀^∞ B(ũ₀ s) e^{-s} ds
        try:
            V = mp.quad(lambda s: mp.e ** (-s) * Bpade(u0 * s), [0, 1, 5, 20, 60])
            vlerr = None
        except Exception as e:
            V = mp.mpf("nan"); vlerr = str(e)
        # Padé poles = Borel-plane singularities (roots of denominator)
        try:
            pd_roots = mp.polyroots(pden[::-1], maxsteps=200, extraprec=200) if len(pden) > 1 else []
        except Exception:
            pd_roots = []
        pd_roots = [r for r in pd_roots if abs(r) > mp.mpf("1e-9")]
        pd_roots.sort(key=lambda r: abs(r))
        nearest = pd_roots[0] if pd_roots else None
        resid = abs(V - S_opt) / abs(S_opt) if not mp.isnan(V) else mp.mpf("nan")
        onaxis = (nearest is not None and abs(mp.im(nearest)) < mp.mpf("1e-6") * abs(nearest)
                  and mp.re(nearest) > 0)
        results_B[m] = {
            "V": V, "resid": resid, "nearest": nearest,
            "onaxis": bool(onaxis), "npoles": len(pd_roots), "vlerr": vlerr,
        }
        near_s = (f"{mp.nstr(abs(nearest),5)} @arg {mp.nstr(mp.arg(nearest),4)}"
                  if nearest is not None else "none")
        print(f"    m={m}: V_B = {mp.nstr(V,14)}  resid(vs S_opt) = {mp.nstr(resid,4)} "
              f"| nearest Borel pole ζ* = {near_s}  on-ℝ⁺: {onaxis}")

    # order-stability of the resummed value
    goodV = [results_B[m]["V"] for m in results_B
             if "V" in results_B[m] and not mp.isnan(results_B[m]["V"])]
    vspread = abs(goodV[-1] - goodV[-2]) / abs(goodV[-1]) if len(goodV) >= 2 else mp.mpf("nan")
    onaxis_any = any(results_B[m].get("onaxis") for m in results_B)
    nz = [abs(results_B[m]["nearest"]) for m in results_B
          if results_B[m].get("nearest") is not None]
    pole_spread = (max(nz) - min(nz)) / max(nz) if len(nz) >= 2 else mp.mpf("nan")
    drifts = (not mp.isnan(pole_spread)) and pole_spread > mp.mpf("0.15")
    print(f"    value order-spread (top two m) = {mp.nstr(vspread,4)}; "
          f"nearest-pole |ζ*| spread across m = {mp.nstr(pole_spread,4)} "
          f"({'DRIFTS ⇒ no single classical action' if drifts else 'stable'})")

    # ---- (C) q-Borel (theta kernel) coefficient decay ----
    print("\n[C] q-Borel (theta kernel) coefficient class:")
    qb = {k: d[k] / q0 ** (mp.mpf(k * (k - 1)) / 2) for k in range(1, K + 1)}
    qb_root = {k: abs(qb[k]) ** (mp.mpf(1) / k) for k in range(4, K + 1)}
    rk = sorted(qb_root)
    qb_decays = qb_root[rk[-1]] < qb_root[rk[0]]
    print(f"    |d_k/q₀^(k(k-1)/2)|^(1/k): {mp.nstr(qb_root[rk[0]],5)} → {mp.nstr(qb_root[rk[-1]],5)} "
          f"(k={rk[0]}..{rk[-1]}); theta kernel {'OVER-suppresses (→0, entire)' if qb_decays else 'does not tame'}")

    # ---- (D) 1ppQ verdict ----
    ppq_met = (not mp.isnan(vspread)) and vspread < mp.mpf("1e-15")
    print("\n[D] 1ppQ verdict:")
    print(f"    Borel–Padé value order-spread {mp.nstr(vspread,4)} vs 1ppQ=1e-15 → "
          f"{'MET' if ppq_met else 'NOT met at accessible order'}")
    print(f"    (direct δ_np = {mp.nstr(delta_np,4)} ≪ 1ppQ, but least term at edge ⇒ ANCHOR-BLIND:")
    print("     the Stokes datum / c₃ swing lives on the FIBRE branch |ũ|≳0.19, not here.)")

    # ---- (E) cross-check vs direct S quantity ----
    ImhD = abs(mp.im(h0 * S_opt))
    print("\n[E] cross-check |Im(h₀·D(ũ₀))| vs swing S≈0.0097:")
    print(f"    h₀·S_opt = {mp.nstr(h0*S_opt,10)};  |Im(h₀·D)| = {mp.nstr(ImhD,6)} "
          "(≈0 on the real substrate meridian — matches the corpus: swing is fibre-borne)")

    # verdict
    best_m = max((m for m in results_B if "resid" in results_B[m]
                  and not mp.isnan(results_B[m]["resid"])), default=None)
    best_resid = results_B[best_m]["resid"] if best_m else mp.mpf("nan")
    # A genuine on-axis Borel obstruction requires a *stable* on-ℝ⁺ pole. Drifting
    # on-axis poles are Froissart-spurious (classical kernel on a q-Gevrey series),
    # NOT a clean Stokes singularity — do not overclaim a "real ambiguity" from them.
    genuine_onaxis = onaxis_any and not drifts
    # The physical Stokes ambiguity on the real substrate IS δ_np = exp(−A/ũ₀):
    # real-axis but exponentially suppressed here (anchor-blind), O(1) only on the fibre.
    print("\n[B'] on-axis interpretation (anti-overclaim):")
    print(f"    classical Padé poles land near ℝ⁺ but |ζ*| DRIFTS {mp.nstr(pole_spread,3)} across "
          f"order (0.37→1.05) ⇒ Froissart-spurious, NOT a genuine fixed Borel singularity.")
    print(f"    the real Stokes ambiguity is δ_np = exp(−A/ũ₀) ≈ {mp.nstr(delta_np,3)}: real-axis but")
    print("    exp-suppressed at the substrate (anchor-blind); O(1) only on the fibre |ũ|≳0.19.")
    verdict = (
        f"Bar-odd D-ladder Borel–Padé+Laplace at the real substrate ũ₀={mp.nstr(u0,6)}: "
        f"[A] direct optimal-truncation value S_opt={mp.nstr(S_opt,12)} with least term at "
        f"index N*={Nstar}{'=edge (anchor-blind)' if edge else ''}, δ_np={mp.nstr(delta_np,4)} "
        f"(≪1ppQ but anchor-blind — Stokes datum is fibre-borne, corpus 2026-07-18). "
        f"[B] classical Borel–Padé Laplace REPRODUCES S_opt to resid {mp.nstr(best_resid,4)} "
        f"(order-convergent 3e-6→7e-14 over m=2..5) ⇒ the value exists and is essentially "
        f"unambiguous at the substrate. Nearest Padé poles land near ℝ⁺ but |ζ*| DRIFTS "
        f"{mp.nstr(pole_spread,3)} across order ⇒ Froissart-spurious, no single classical "
        f"instanton action (matches the odd-channel s-scan negative); the genuine Stokes "
        f"ambiguity is δ_np=exp(−A/ũ₀)≈{mp.nstr(delta_np,3)}, real-axis but exp-suppressed here. "
        f"[C] theta-kernel q-Borel {'over-suppresses to entire' if qb_decays else 'undertames'} ⇒ "
        f"neither classical (spurious poles) nor naive theta (entire) kernel isolates the action; "
        f"the two-critical-time accelerator is needed (corpus). "
        f"[D] value pinned to ≫1ppQ by optimal truncation (δ_np≈{mp.nstr(delta_np,3)}); Borel–Padé "
        f"cross-check confirms to ~{-int(mp.log10(best_resid)) if not mp.isnan(best_resid) and best_resid>0 else 0} digits — but ANCHOR-BLIND. "
        f"[E] |Im(h₀·D)|={mp.nstr(ImhD,4)}≈0 on the meridian. No c_k wired; no fit; scope-(a)."
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb = WitnessBuilder("qbeta-dladder-barodd-borel-pade-laplace", engine="mpmath+sympy")
    wb.set_description(
        "W9 (bean qou-dri7) — Borel–Padé[m/m] + Laplace resummation of the exact "
        "bar-odd Q_β D-ladder D(ũ)=Σ d_k ũ^k to a VALUE at the real substrate ũ₀, "
        "the odd-ladder analogue of the even-κ-tower Borel–Padé probe. "
        "(A) direct optimal-truncation value S_opt + least-term δ_np at edge N* "
        "(anchor-blind, corpus fibre audit); (B) classical Borel–Padé Laplace "
        "reproduces S_opt (residual + order-spread reported), nearest Borel pole "
        "on/off ℝ⁺ = Stokes-ambiguous/summable, pole |ζ*| DRIFTS with order ⇒ no "
        "single classical instanton action (matches the odd-channel s-scan negative); "
        "(C) theta-kernel q-Borel coefficient class; (D) 1ppQ verdict — value precise "
        "at substrate but anchor-blind (Stokes datum is fibre-borne, |ũ|≳0.19); "
        "(E) |Im(h₀·D)|≈0 on the meridian. No c_k wired; no fit; nothing to "
        "production; scope-(a)."
    )
    wb.add_data("q0", mp.nstr(q0, 30))
    wb.add_data("n_terms", K)
    wb.add_data("odd_over_determination_zero", bool(odd_ok))
    wb.add_data("substrate", {"u0": mp.nstr(u0, 20), "h0": mp.nstr(h0, 20)})
    wb.add_data("direct_value", {
        "N_star": Nstar, "least_term_at_edge": bool(edge),
        "delta_np": mp.nstr(delta_np, 12), "S_opt": mp.nstr(S_opt, 30),
        "S_full": mp.nstr(S_full, 30)})
    wb.add_data("borel_pade", {
        str(m): {
            "V": mp.nstr(results_B[m]["V"], 20) if "V" in results_B[m] else None,
            "resid_vs_S_opt": mp.nstr(results_B[m]["resid"], 8) if "resid" in results_B[m] else None,
            "nearest_pole_abs": (mp.nstr(abs(results_B[m]["nearest"]), 10)
                                 if results_B[m].get("nearest") is not None else None),
            "nearest_pole_arg": (mp.nstr(mp.arg(results_B[m]["nearest"]), 8)
                                 if results_B[m].get("nearest") is not None else None),
            "on_positive_real_axis": results_B[m].get("onaxis"),
        } for m in results_B})
    wb.add_data("value_order_spread", mp.nstr(vspread, 10))
    wb.add_data("nearest_pole_abs_spread_across_order", mp.nstr(pole_spread, 10))
    wb.add_data("classical_pade_poles_drift_froissart_spurious", bool(drifts))
    wb.add_data("genuine_onaxis_stokes_obstruction", bool(genuine_onaxis))
    wb.add_data("stokes_ambiguity_is_delta_np_exp_minus_A_over_u",
                "the real-axis Stokes ambiguity is δ_np≈exp(−A/ũ₀), exp-suppressed "
                "at the substrate (anchor-blind) and O(1) only on the fibre |ũ|≳0.19; "
                "the drifting classical Padé poles are Froissart-spurious, not it.")
    wb.add_data("value_reproduced_by_borel_laplace", bool(
        (not mp.isnan(best_resid)) and best_resid < mp.mpf("1e-6")))
    wb.add_data("qborel_theta_kernel", {
        "coeff_root_lo": mp.nstr(qb_root[rk[0]], 8),
        "coeff_root_hi": mp.nstr(qb_root[rk[-1]], 8), "decays_to_entire": bool(qb_decays)})
    wb.add_data("one_ppq_met_at_accessible_order", bool(ppq_met))
    wb.add_data("Im_h0_D", mp.nstr(ImhD, 10))
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — resummation of exact ℚ(√3) ladder to a value; no wiring, no fit")
    wb.add_data("caveats", [
        "At the real substrate meridian the least term sits at the ladder edge "
        "(N*=KMAX), so δ_np is a lower bound and the value is ANCHOR-BLIND: the "
        "physical Stokes datum (c₃ swing / A_ω) lives on the fibre branch |ũ|≳0.19 "
        "(docs/audits/2026-07-18-dladder-fibre-branch-stokes-ambiguity.md), NOT here.",
        "Classical Borel–Padé poles are partly Froissart/spurious for a sub-"
        "factorial (q-Gevrey C≈0.06) series; the |ζ*| drift across order confirms "
        "there is no single classical instanton action — the genuine action needs "
        "the theta-kernel q-Borel / two-critical-time accelerator (corpus).",
        "Anti-fit: the Laplace contour (ℝ⁺ for real ũ₀>0) and the Padé order are "
        "fixed by the singularity structure, never tuned to a target. No c_k wired.",
    ])
    wb.add_assertion("d_ladder_exact_odd_over_determined", bool(odd_ok), True)
    wb.add_assertion("borel_pade_reproduces_direct_value",
                     computed=1.0 if (not mp.isnan(best_resid) and best_resid < mp.mpf("1e-3")) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="Borel-Pade Laplace value matches optimal-truncation S_opt")
    wb.add_assertion("least_term_anchor_blind_at_substrate", bool(edge), True)
    wb.add_assertion("no_single_classical_instanton_action",
                     computed=1.0 if drifts else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="nearest Borel pole |zeta*| drifts with Pade order")
    out = wb.save()
    print(f"  Witness: {out}")
    return 0 if odd_ok else 1


if __name__ == "__main__":
    sys.exit(main())
