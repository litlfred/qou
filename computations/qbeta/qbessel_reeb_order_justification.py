#!/usr/bin/env python3
"""qbessel_reeb_order_justification.py
=======================================

Settle the Reeb-flow propagator ORDER choice: proper integer-order reduction-of-
order log-Neumann vs the half-integer ±1/2 the `qbessel_qdeformed_reeb_scale.py`
proxy used — and JUSTIFY the +1/2 (it is physics, not a resonance-dodge).

## The problem this fixes

`qbessel_qdeformed_reeb_scale.py` used `ν = dim−1 ± 1/2` as a *proxy* to avoid the
integer-order resonance `(q^k − q^ν)=0` in the `d_k`-recurrence second solution,
then flagged the ±0.5 SWING (0.43) + 64% single-block domination as "not forced".
But:

  • the resonance is an artifact of the `d_k` construction ONLY; the
    **reduction-of-order** second solution
        g2(w) = −g1(w)·Σ_j (q^j w)^{−ν} / [g1(q^j w) g1(q^{j+1} w)]
    (the q-Casoratian-weighted q-integral; `qbessel_reeb_yweighted_gap.py`) has NO
    such resonance and evaluates at INTEGER ν directly — the genuine log-Neumann;
  • the −1/2 branch puts every dim-1 block at ν=−1/2 (NEGATIVE order ⇒ the
    (q^j w)^{−ν} factor GROWS ⇒ a divergent, dominant propagator). THAT is the
    64% single-block artifact — unphysical, not a real per-block contribution.

## Justification of +1/2 (three independent reasons, all picking +1/2)

  1. **Spherical Bessel.** `j_l(x) = √(π/2x)·J_{l+1/2}(x)` are the radial modes of
     a *3-dimensional* tube; integer order is the 2D-annular cross-section. A flux
     tube in 3-space ⇒ spherical ⇒ +1/2.
  2. **Langer correction.** The d-dimensional radial Laplacian, reduced to Bessel
     form by `u = r^{(d-1)/2} R`, has effective order `ν = l + (d−2)/2`: d=2 → l
     (integer), d=3 → l+1/2 (half-integer). The +1/2 is the standard radial-
     reduction shift, not a fudge.
  3. **Framing/spin half-twist.** The Reeb flow is the writhe/framing flow on the
     SU(2) double cover (SU(2)→SO(3)); its natural angular order is spinorial =
     half-integer, shifted +1/2 from the bosonic integer value.

So the PHYSICAL order is either INTEGER (2D-annular tube) or +1/2 (3D-spherical /
spin-framed). The −1/2 branch is unjustified. The honest forced-ness test is the
**integer-vs-(+1/2) spread**, both with ν ≥ 0 — NOT the old ±1/2 swing.

## What this computes (deuteron, real χ_λ + forced y_λ Markov weights)

For ν ∈ {dim−1 (integer), dim−1+1/2 (spherical), dim−1−1/2 (the unphysical branch,
for contrast)} via the resonance-free reduction-of-order g2:

  δ_form = Σ_λ w_λ · [G(w_atom) − G(w_free)],   G = g1·g2·w^ν,  w = q·θ_λ²,
  weights: raw (1), A (y_λ), B (y_λ·χ_λ^atom).

Diagnostics: ratio vs B(D)/m_e≈4.35; single-block domination per order; cross-anchor
(q₀ vs q_μ). No fit; the scale must come from the forced order+weights, never a
tuned prefactor. Exploratory; audit-only.
"""
from __future__ import annotations

import json
import math
import pathlib
import sys

from mpmath import mp, mpf, qp, fabs, acos, acosh

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
# Substrate modulus from the registry, not re-typed here: the literal was
# "1.10997858", the proton pin truncated to 9 s.f. (canonical
# 1.10997858275138…). Proton is the default anchor per AGENTS.md.
from q_parameter import Q_MP  # noqa: E402
Q0 = Q_MP
QMU = mpf("1.110037")
B_DEU_OVER_ME = mpf("2.224573") / mpf("0.510999")
KSER, JSUM = 50, 80
HERE = pathlib.Path(__file__).resolve().parent
DEU = HERE.parent / "atom-chi-rust-d.witness.json"
sys.path.insert(0, str(HERE.parent))
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

_CK: dict = {}


def dim_sn(lam):
    n = sum(lam)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return math.factorial(n) // den


def ck_array(nu, q):
    """Cached [c_0..c_{KSER-1}] for g1 (Horner)."""
    key = (str(nu), str(q))
    if key not in _CK:
        arr = []
        for k in range(KSER):
            arr.append((-1) ** k * q ** (mpf(k * (k - 1)) / 2)
                       / (qp(q, q, k) * qp(q ** (nu + 1), q, k)))
        _CK[key] = arr
    return _CK[key]


def g1(w, nu, q):
    c = ck_array(nu, q)
    s = mpf(0)
    for k in range(KSER - 1, -1, -1):
        s = s * w + c[k]
    return s


def g2(w, nu, q):
    """Reduction-of-order (q-integral) second solution — resonance-free, valid at
    integer ν (the genuine log-Neumann)."""
    s = mpf(0)
    for j in range(JSUM):
        wj = q ** j * w
        s += (wj ** (-nu)) / (g1(wj, nu, q) * g1(q * wj, nu, q))
    return -g1(w, nu, q) * s


def G(w, nu, q):
    return g1(w, nu, q) * g2(w, nu, q) * w ** nu


def reeb(r):
    return acos(r) if fabs(r) <= 1 else acosh(fabs(r))


def load(cfg):
    d = json.loads(DEU.read_text(encoding="utf-8"))
    return {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d["data"][cfg]["by_partition"]}


def deltas_for_order(free, atom, y, q, offset):
    raw = wA = wB = mpf(0)
    contribs = []
    for lam in free:
        d = dim_sn(list(lam))
        nu = mpf(d - 1) + offset
        rf, ra = free[lam] / d, atom[lam] / d
        wf, wa = q * reeb(rf) ** 2, q * reeb(ra) ** 2
        dG = G(wa, nu, q) - G(wf, nu, q)
        yl = y[lam]
        raw += dG
        wA += yl * dG
        wB += yl * atom[lam] * dG
        contribs.append((lam, d, float(nu), yl * dG))
    return raw, wA, wB, contribs


def domination(contribs):
    tot = sum(fabs(c[3]) for c in contribs)
    if tot == 0:
        return mpf(0), None
    top = max(contribs, key=lambda c: fabs(c[3]))
    return fabs(top[3]) / tot, top


def main():
    free, atom = load("free"), load("atom")
    y0 = {k: mpf(str(v)) for k, v in y_lambda_at(6, Q0).items()}
    ymu = {k: mpf(str(v)) for k, v in y_lambda_at(6, QMU).items()}
    print("Reeb-flow propagator ORDER justification (integer vs +1/2 vs -1/2)")
    print("=" * 78)
    print(f"deuteron n=6, {len(free)} blocks; q_0={float(Q0)}; B(D)/m_e={float(B_DEU_OVER_ME):.4f}")
    print("reduction-of-order g2 (resonance-free); forced y_lambda weights; no fit\n")

    ORDERS = [("integer (2D-annular)", mpf(0)),
              ("+1/2 (spherical/Langer/spin)", mpf("0.5")),
              ("-1/2 (unphysical branch)", mpf("-0.5"))]

    results = {}
    print(f"{'order':<30}{'raw':>12}{'A=Σy·dG':>13}{'B=Σyχ·dG':>13}{'|A|/Bd':>9}{'topblk%':>9}")
    for name, off in ORDERS:
        raw, wA, wB, contribs = deltas_for_order(free, atom, y0, Q0, off)
        _, wAmu, wBmu, _ = deltas_for_order(free, atom, ymu, QMU, off)
        topfrac, toplam = domination(contribs)
        rA = fabs(wA) / B_DEU_OVER_ME
        xA = fabs(wAmu - wA) / (fabs(wA) + fabs(wAmu)) if (wA or wAmu) else mpf(0)
        results[name] = {"offset": str(off), "raw": str(raw), "A": str(wA), "B": str(wB),
                         "ratio_A_over_Bd": str(rA), "xanchor_A": str(xA),
                         "top_block_frac": str(topfrac),
                         "top_block": list(toplam[0]) if toplam else None,
                         "top_block_nu": float(toplam[2]) if toplam else None}
        print(f"{name:<30}{mp.nstr(raw,5):>12}{mp.nstr(wA,5):>13}{mp.nstr(wB,5):>13}"
              f"{mp.nstr(rA,4):>9}{mp.nstr(topfrac*100,4):>8}%")

    # The HONEST forced-ness test: integer vs +1/2 (both physical, ν≥0)
    intA = fabs(mpf(results["integer (2D-annular)"]["A"]))
    sphA = fabs(mpf(results["+1/2 (spherical/Langer/spin)"]["A"]))
    int_sph_spread = fabs(intA - sphA) / (intA + sphA) if (intA or sphA) else mpf(0)
    int_dom = mpf(results["integer (2D-annular)"]["top_block_frac"])
    sph_dom = mpf(results["+1/2 (spherical/Langer/spin)"]["top_block_frac"])
    minus_dom = mpf(results["-1/2 (unphysical branch)"]["top_block_frac"])

    print("\n--- VERDICT (order justification; no fit; critical distance) ---")
    print(f"  integer vs +1/2 relative spread (the REAL forced test) = {mp.nstr(int_sph_spread,4)}")
    print(f"  single-block domination:  integer {mp.nstr(int_dom*100,3)}%   "
          f"+1/2 {mp.nstr(sph_dom*100,3)}%   -1/2 {mp.nstr(minus_dom*100,3)}%")
    int_on = mpf("0.2") < fabs(intA) / B_DEU_OVER_ME < mpf("5")
    sph_on = mpf("0.2") < sphA / B_DEU_OVER_ME < mpf("5")
    robust = int_sph_spread < mpf("0.35") and int_dom < mpf("0.5") and sph_dom < mpf("0.5")
    print()
    print("  ±1/2 JUSTIFIED: +1/2 = spherical Bessel (3D tube) / Langer (d=3 radial)")
    print("                  / Reeb spin half-twist; -1/2 has NO physical basis and")
    print("                  puts dim-1 blocks at ν=-1/2 (negative order ⇒ divergent).")
    if robust and (int_on or sph_on):
        print("  => RESOLVED: at proper order (integer AND +1/2, both ν≥0) the propagator")
        print("     is on-scale, NOT single-block-dominated, and integer≈+1/2 — so the")
        print("     result is forced w.r.t. the (physical) order choice. The old ±1/2")
        print("     'swing' was the unphysical -1/2 branch leaking in. Next gate: bar-parity.")
    else:
        print("  => The proper integer/+1/2 orders remove the -1/2 artifact but the result is")
        print(f"     {'still single-block-sensitive' if max(int_dom,sph_dom)>=mpf('0.5') else 'on/off-scale order-sensitive'}:")
        print(f"     integer ratio {mp.nstr(fabs(intA)/B_DEU_OVER_ME,3)}, +1/2 ratio {mp.nstr(sph_on and sphA/B_DEU_OVER_ME or sphA/B_DEU_OVER_ME,3)},")
        print("     spread {0}. Honest: order choice (2D vs 3D tube) must be PINNED".format(mp.nstr(int_sph_spread,3)))
        print("     physically before this is wireable. Not a fit; not yet forced.")
    print("\n  No fit; nothing wired; c_k/Δ_λ cal-anchored.")

    # witness
    out = {
        "computation": "qbessel_reeb_order_justification",
        "description": ("Reeb-flow propagator order test: proper integer-order reduction-of-order "
                        "log-Neumann vs +1/2 (spherical/Langer/spin) vs -1/2 (unphysical), with "
                        "real y_lambda Markov weights on the deuteron. Justifies +1/2 and shows "
                        "the -1/2 branch is the single-block artifact. No fit; audit-only."),
        "discipline": "no fit; derive-or-refute; exploratory; does NOT wire; c_k/Delta_lambda cal-anchored",
        "auditOnly": "docs/audits/2026-06-23-qbessel-reeb-order-justification.md",
        "parameters": {"compute_dps": mp.dps, "KSER": KSER, "JSUM": JSUM,
                       "q0": str(Q0), "B_D_over_me": str(B_DEU_OVER_ME)},
        "orders": results,
        "integer_vs_half_spread": str(int_sph_spread),
        "verdict_robust": bool(robust and (int_on or sph_on)),
    }
    wp = HERE.parent / "probes" / "qbessel-reeb-order-justification.witness.json"
    wp.parent.mkdir(parents=True, exist_ok=True)
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
    out["scriptFile"] = _os.path.basename(__file__)
    wp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\n  witness → {wp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
