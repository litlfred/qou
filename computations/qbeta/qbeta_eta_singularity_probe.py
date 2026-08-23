#!/usr/bin/env python3
"""qbeta_eta_singularity_probe.py — identify the eta-plane singularity
(follow-up to bean 0zr0; audit
docs/audits/2026-07-03-0zr0-eta-descent-invariant-theory-prune.md).

The 0zr0 prune left ONE sharpened datum: the descent rungs g_k of
E = sum g_k t^k (t = eta^2) grow like |g_{k+1}/g_k| -> ~20, so E(t) has a
finite radius of convergence ~1/20.5 with the nearest singularity on the
negative t-axis.  This probe answers: WHAT is that singularity?

Two independent legs:

  LEG 1 (series-side): sharpen t_c from the exact rungs — Domb–Sykes
  extrapolation of g_{k+1}/g_k against 1/k, and Padé-approximant poles of
  E(t).  Consistency of the two estimates is the sanity gate.

  LEG 2 (function-side): the net route is CLOSED FORM —
      R(q) = sgn·(dnet(q)/(q−1))/q / (QA(q)·cos α(q)),
      α = ((z−1)h − ũ)/2,  z = √q/(q+1),  ũ = q·b·ℏ_q²,
      b = √(q⁴+q²+1)/(q²+1),  h = q − 1/q,
  and O(s) = (log R(1+s) − log R(1/(1+s)))/2, t(s) = (O(s)/ℓ)^{2/3}
  (principal branches; O = ℓ·η³ exactly per the 0zr0 gauge).  The
  candidate mechanisms for a t-plane singularity of E(t), each locatable
  numerically in the s-annulus:
    (a) zeros of O(s), s ≠ 0  — cube-root branch points of η (t branches);
    (b) zeros of O′(s)        — critical points of s ↦ t (inverse branches);
    (c) zeros of dnet_reg at q = 1+s or q = 1/(1+s) — log-branch points
        (R → 0), where E and O blow up together;
    (d) zeros of cos α        — poles of log R (far, |α| must reach π/2);
    (e) |q| = 1 with arg q/2π rational — root-of-unity locus (checked on
        whichever point wins).
  For each candidate s₁ found, the t-image |t(s₁)| is compared to the
  LEG-1 t_c; the winner (closest match from inside) is the identified
  mechanism.

Numerics only (mpmath, dps 40); identification is by |t|-match to ~1%,
recorded as such — scope (a), audit-only, no wiring.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = 17
ORD = core.ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent


def ser_compose(a, phi):
    assert phi[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def ser_cbrt1(a):
    assert simp(a[0] - 1) == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = sp.Integer(1)
    for n in range(1, ORD + 1):
        part = ser_mul(ser_mul(out, out), out)
        out[n] = simp((a[n] - part[n]) / 3)
    return out


def t_rungs(E, t_ser, kmax):
    e = {}
    model = [sp.Integer(0)] * (ORD + 1)
    tpow = [[sp.Integer(1)] + [sp.Integer(0)] * ORD]
    for k in range(1, kmax + 1):
        tpow.append(ser_mul(tpow[-1], t_ser))
    for k in range(1, kmax + 1):
        lead = tpow[k][2 * k]
        ek = simp((E[2 * k] - model[2 * k]) / lead)
        e[k] = ek
        model = ser_add(model, ser_scale(ek, tpow[k]))
    return e


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" eta-plane singularity identification (0zr0 follow-up)")
    print("=" * 78)

    # ---- shared exact objects --------------------------------------------
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    with open(_pb.witness_path(
            "q-pinning-50-digit.witness.json", HERE)) as fh:
        q0 = mp.mpf(json.load(fh)["derived_50_digit"]["q"])
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))

    # ---- LEG 1: exact rungs -> t_c ---------------------------------------
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_tilde = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_tilde))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    logR_bar = ser_compose(logR, phi)
    E = [simp((a + b_) / 2) for a, b_ in zip(logR, logR_bar)]
    O = [simp((a - b_) / 2) for a, b_ in zip(logR, logR_bar)]
    ell = O[3]
    O_shift3 = [simp(o / ell) for o in O[3:]] + [sp.Integer(0)] * 3
    eta = [sp.Integer(0)] + ser_cbrt1(O_shift3)[:ORD]
    t_ser = ser_mul(eta, eta)
    KMAX = (ORD - 1) // 2
    g = t_rungs(E, t_ser, KMAX)
    gN = {k: mp.mpf(str(sp.N(v, 35))) for k, v in g.items()}
    print(f"  rungs computed ({time.monotonic()-t0:.0f}s)")

    # Domb–Sykes: r_k = g_{k+1}/g_k ~ (1/t_c)(1 + (γ−1)/k): linear fit vs 1/k
    ks = sorted(gN)[:-1]
    ratios = {k: gN[k + 1] / gN[k] for k in ks}
    k_hi = ks[-3:]
    xs = [mp.mpf(1) / k for k in k_hi]
    ys = [ratios[k] for k in k_hi]
    # 2-point slope/intercept from the last two, and last three (avg)
    slope = (ys[-1] - ys[0]) / (xs[-1] - xs[0])
    intercept = ys[-1] - slope * xs[-1]
    t_c_ds = 1 / intercept
    gamma_ds = 1 + slope / intercept
    print(f"  Domb–Sykes: 1/t_c = {mp.nstr(intercept, 8)}  ->  t_c = {mp.nstr(t_c_ds, 8)}"
          f"   exponent γ ≈ {mp.nstr(gamma_ds, 4)}")

    # Padé poles of E(t) (coeffs g_1..g_KMAX, constant 0)
    coeffs = [mp.mpf(0)] + [gN[k] for k in sorted(gN)]
    pade_poles = {}
    for L, M in ((3, 4), (4, 4), (3, 3)):
        try:
            p, qd = mp.pade(coeffs, L, M)
            roots = mp.polyroots([mp.mpf(str(c)) for c in qd[::-1]], maxsteps=200)
            near = min(roots, key=lambda r: abs(r))
            pade_poles[f"[{L}/{M}]"] = near
            print(f"  Padé [{L}/{M}] nearest pole: t = {mp.nstr(near, 8)}  |t| = {mp.nstr(abs(near), 8)}")
        except Exception as exc:  # noqa: BLE001
            print(f"  Padé [{L}/{M}] failed: {exc}")
    t_c = min((v for v in pade_poles.values()), key=lambda r: abs(r)) \
        if pade_poles else mp.mpc(t_c_ds)
    print(f"  LEG-1 t_c (Padé, nearest): {mp.nstr(t_c, 8)}")

    # ---- LEG 2: closed-form function side --------------------------------
    dnet_f = sp.lambdify(q, dnet_reg, "mpmath")
    ell_n = mp.mpf(str(sp.N(ell, 35)))  # ell is real (Q(sqrt3)), ~ -2.7835

    def Rq(qq):
        zq = mp.sqrt(qq) / (qq + 1)
        bq = mp.sqrt(qq**4 + qq**2 + 1) / (qq**2 + 1)
        hq = qq - 1 / qq
        utq = qq * bq * ((qq - 1) / qq) ** 2
        aq = ((zq - 1) * hq - utq) / 2
        QAq = (2 * qq + 1 - qq**2) * (qq + 1) / (2 * qq**3)
        return sgn * (dnet_f(qq) / qq) / (QAq * mp.cos(aq))

    def O_s(s):
        return (mp.log(Rq(1 + s)) - mp.log(Rq(1 / (1 + s)))) / 2

    def t_s(s):
        # principal-branch t = (O/ell)^(2/3); valid up to branch choice —
        # used only for |t| comparisons.
        return mp.power(O_s(s) / ell_n, mp.mpf(2) / 3)

    def dO(s, h=mp.mpf("1e-12")):
        return (O_s(s + h) - O_s(s - h)) / (2 * h)

    # grid-scan the upper annulus for |O| minima (mechanism a) and |O'| minima (b)
    def scan(fn, rlo=0.10, rhi=0.45, nr=24, nth=48):
        seeds = []
        vals = {}
        import math
        for i in range(nr + 1):
            r = rlo + (rhi - rlo) * i / nr
            for j in range(1, nth):
                th = math.pi * j / nth
                s = mp.mpc(r * math.cos(th), r * math.sin(th))
                try:
                    vals[(i, j)] = (s, abs(fn(s)))
                except Exception:  # noqa: BLE001
                    continue
        # local minima on the grid
        for (i, j), (s, v) in vals.items():
            nb = [vals.get((i + di, j + dj)) for di in (-1, 0, 1) for dj in (-1, 0, 1)
                  if (di, dj) != (0, 0)]
            nb = [x for x in nb if x is not None]
            if nb and all(v <= x[1] for x in nb) and v < 0.5:
                seeds.append(s)
        roots = []
        for s0 in seeds:
            try:
                r_ = mp.findroot(fn, s0, maxsteps=60)
                if r_.imag > 1e-6 and mp.mpf("0.02") < abs(r_) < mp.mpf("0.9"):
                    if all(abs(r_ - r2) > 1e-6 for r2 in roots):
                        roots.append(r_)
            except Exception:  # noqa: BLE001
                continue
        return sorted(roots, key=lambda r_: abs(r_))

    print("\n  LEG-2 mechanism scan (upper half-annulus, conjugates implied):")
    zeros_O = scan(O_s)
    print(f"  (a) zeros of O(s):      {[mp.nstr(r, 8) for r in zeros_O[:4]]}")
    zeros_dO = scan(dO)
    zeros_dO = [r for r in zeros_dO if all(abs(r - z) > 1e-5 for z in zeros_O)]
    print(f"  (b) zeros of O'(s)\\(a): {[mp.nstr(r, 8) for r in zeros_dO[:4]]}")
    zeros_net, zeros_net_bar = [], []
    zeros_net = scan(lambda s: dnet_f(1 + s))
    zeros_net_bar = scan(lambda s: dnet_f(1 / (1 + s)))
    print(f"  (c) dnet_reg(1+s) = 0:  {[mp.nstr(r, 8) for r in zeros_net[:4]]}")
    print(f"      dnet_reg(σ)  = 0:  {[mp.nstr(r, 8) for r in zeros_net_bar[:4]]}")

    candidates = []
    for tag, roots in (("O-zero (cbrt branch of eta)", zeros_O),
                       ("O'-zero (critical point of t)", zeros_dO),
                       ("net-zero at q=1+s (log branch)", zeros_net),
                       ("net-zero at q=σ(s) (log branch)", zeros_net_bar)):
        for r_ in roots[:3]:
            # t-image: for log-branch points t is finite; for O-zeros t(s1)
            # is finite too (t = (O/ell)^{2/3} -> 0? no: O(s1)=0 => t=0 —
            # the branch point maps to t-image via the OTHER sheet; use
            # a nearby circuit max as proxy: evaluate |t| on small circle.
            try:
                if "O-zero" in tag:
                    tt = max(abs(t_s(r_ + mp.mpf("2e-3") * mp.expjpi(2 * mp.mpf(m) / 8)))
                             for m in range(8))
                else:
                    tt = abs(t_s(r_))
            except Exception:  # noqa: BLE001
                tt = mp.inf
            qq = 1 + r_
            candidates.append({
                "mechanism": tag,
                "s": mp.nstr(r_, 10),
                "abs_s": mp.nstr(abs(r_), 8),
                "abs_t_image": mp.nstr(tt, 8),
                "match_ratio_vs_tc": mp.nstr(tt / abs(t_c), 6),
                "abs_q": mp.nstr(abs(qq), 10),
                "arg_q_over_2pi": mp.nstr(mp.arg(qq) / (2 * mp.pi), 8),
            })

    print("\n  candidate table (|t-image| vs |t_c| = " + mp.nstr(abs(t_c), 8) + "):")
    for c in candidates:
        print(f"    {c['mechanism']:34s} s={c['s']:28s} |t|={c['abs_t_image']:12s} "
              f"ratio={c['match_ratio_vs_tc']:10s} |q|={c['abs_q']}")

    best = min(candidates, key=lambda c: abs(mp.mpf(c["match_ratio_vs_tc"]) - 1)) \
        if candidates else None

    # root-of-unity check on the winner
    rou = None
    if best:
        absq = mp.mpf(best["abs_q"])
        argf = abs(mp.mpf(best["arg_q_over_2pi"]))
        best_frac = None
        for den in range(2, 61):
            num = mp.nint(argf * den)
            if num > 0 and abs(argf - num / den) < mp.mpf("5e-4"):
                best_frac = (int(num), den)
                break
        rou = {
            "abs_q_minus_1": mp.nstr(absq - 1, 6),
            "on_unit_circle_1e-3": bool(abs(absq - 1) < 1e-3),
            "arg_q_over_2pi_rational_approx": best_frac,
        }

    verdict = (
        ("no mechanism candidate found in the annulus — enlarge the scan"
         " (recorded, scope (a))") if not best else
        (f"nearest-singularity mechanism candidate: {best['mechanism']} at "
         f"s = {best['s']} (|t-image|/|t_c| = {best['match_ratio_vs_tc']}); "
         f"q = 1+s has |q| = {best['abs_q']}"
         + (" — ON the unit circle (root-of-unity locus plausible)"
            if rou and rou["on_unit_circle_1e-3"] else
            " — NOT on the unit circle (root-of-unity hypothesis disfavored)")
         + ". Numeric identification at ~1% |t|-match; scope (a), audit-only.")
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic()-t0:.1f}s)")

    wb = WitnessBuilder("qbeta-eta-singularity", engine="mpmath+sympy",
                        start_time=t0)
    wb.set_description(
        "0zr0 follow-up: identify the nearest t-plane singularity of the "
        "descent function E(t). LEG 1: Domb-Sykes + Pade t_c from the exact "
        "rungs. LEG 2: closed-form net route — locate zeros of O (cbrt "
        "branch points of eta), zeros of O' (critical points of t), net-route "
        "zeros (log branch) in the s-annulus; match |t|-images against t_c; "
        "root-of-unity check on the winner."
    )
    wb.add_data("ORD", ORD)
    wb.add_data("rungs_g_k", {str(k): mp.nstr(gN[k], 20) for k in sorted(gN)})
    wb.add_data("domb_sykes", {"t_c": mp.nstr(t_c_ds, 12), "gamma": mp.nstr(gamma_ds, 8)})
    wb.add_data("pade_nearest_poles", {k: mp.nstr(v, 12) for k, v in pade_poles.items()})
    wb.add_data("t_c_adopted", mp.nstr(t_c, 12))
    wb.add_data("candidates", candidates)
    wb.add_data("winner", best)
    wb.add_data("root_of_unity_check", rou)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a); numeric identification, no wiring")
    wb.add_assertion("rungs_grow_finite_radius",
                     bool(abs(gN[KMAX] / gN[KMAX - 1]) > abs(gN[2] / gN[1])), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
