#!/usr/bin/env python3
"""qbeta_h_frame_rungs_probe.py — the Q_β ladder's rungs in the h frame,
exactly, and the identity that says what a u-rung IS in that frame.

Bean `qou-cwin` T1. Companion to `QOU/QBeta/LadderFrameChange.lean`, which
proves the algebra below sorry-free over a generic field.

WHAT THIS ESTABLISHES

1. **The frame change is an IDENTITY, not an asymptotic.** The relation
   normally written "u ∼ h² near q = 1" is exact at every q:

       ℏ_q · (q + 1) = h              since ℏ_q = (q−1)/q, h = (q²−1)/q
       u = b · h² / (q + 1)²          since u = b·ℏ_q²

   The conversion factor is b/(q+1)² — at the proton anchor ≈ 0.19488, which
   is why u/h² measures 0.194875 and NOT the √3/8 ≈ 0.21651 its q → 1 limit
   would suggest. Using the limit as the conversion is a ~10 % error.

2. **Every u-rung is an even h-rung: uᵏ = (b/(q+1)²)ᵏ · h²ᵏ.** So a u-ladder
   places weight only on EVEN h-orders. Odd h-orders are not unpopulated by
   choice — they are outside the span of any u-ladder whatsoever. This is the
   exact form of a fact previously stated as "half-integer powers appear when
   the u-expansion is pushed past its analytic range".

3. **The odd orders are not empty.** Expanding cos(α − u/2) in h gives a
   nonzero, purely-irrational h³ rung. No u-ladder can carry it.

WHAT THIS DOES NOT ESTABLISH. Nothing physical. It is a change of variable:
no c_k value, no derivation of α (un-derived in both frames), and no accuracy
improvement — the cross-anchor instability is 2.3748 % in BOTH frames because
it lives in the residual, not the coordinate
(`qbeta_h_vs_u_frame_stability_probe`). Do not cite this as progress on the
ladder; cite it for what a rung means when the frame changes.

Anchors: proton (experimental, default per the 2026-08-07 directive) and muon.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

N_ORDERS = 8


def h_frame_series():
    """Exact h-series of cos(α − u/2), via series reversion of h(s), s = q−1.

    Reversion rather than a direct substitution because h = q − 1/q is not
    invertible in closed polynomial form; undetermined coefficients give the
    exact ℚ(√3) rungs without ever going numerical.
    """
    s = sp.Symbol('s', positive=True)
    q = 1 + s
    hh = q - 1 / q
    hbar = (q - 1) / q
    b = sp.sqrt((hh ** 2 + 3) / (hh ** 2 + 4))
    u = b * hbar ** 2
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    alpha = (z - 1) * hh / 2

    M_s = sp.series(sp.cos(alpha - u / 2), s, 0, N_ORDERS).removeO()
    H_s = sp.series(hh, s, 0, N_ORDERS).removeO()

    hsym = sp.Symbol('h')
    a = sp.symbols(f'a1:{N_ORDERS + 1}')
    ser = sum(a[i] * hsym ** (i + 1) for i in range(N_ORDERS - 1))
    eq = sp.series(H_s.subs(s, ser), hsym, 0, N_ORDERS).removeO() - hsym
    sol = sp.solve([sp.expand(eq).coeff(hsym, k)
                    for k in range(1, N_ORDERS)], a, dict=True)[0]
    M_h = sp.series(sp.expand(ser.subs(sol)), hsym, 0, N_ORDERS)  # touch
    M_h = sp.series(M_s.subs(s, sp.expand(ser.subs(sol))), hsym, 0,
                    N_ORDERS).removeO()
    P = sp.Poly(sp.expand(M_h), hsym)
    return [sp.nsimplify(sp.radsimp(sp.simplify(P.coeff_monomial(hsym ** k))))
            for k in range(N_ORDERS)]


def main() -> int:
    print("=" * 78)
    print(" T1 — the Q_β ladder's rungs in the h frame (h = q − 1/q)")
    print("=" * 78)

    # ── 1. the frame-change identity, verified symbolically ──────────────
    q = sp.Symbol('q', positive=True)
    h_s, hbar_s = q - 1 / q, (q - 1) / q
    b_s = sp.sqrt(((q - 1 / q) ** 2 + 3) / ((q - 1 / q) ** 2 + 4))
    id1 = sp.simplify(hbar_s * (q + 1) - h_s)
    id2 = sp.simplify(b_s * hbar_s ** 2 - b_s * h_s ** 2 / (q + 1) ** 2)
    print(f"\n  ℏ_q·(q+1) − h                = {id1}   (0 ⇒ identity)")
    print(f"  u − b·h²/(q+1)²              = {id2}   (0 ⇒ identity)")
    if id1 != 0 or id2 != 0:
        raise AssertionError("frame-change identity failed symbolically")

    # ── 2. the conversion factor is NOT its q→1 limit ────────────────────
    rows = []
    for qv, label in ((q_at(), "proton"), (q_muon_at(), "muon")):
        s = substrate_ladder_quantities(qv)
        conv = s["b"] / (qv + 1) ** 2
        rows.append({"anchor": label, "q": qv, "b": s["b"],
                     "conversion_b_over_qp1_sq": conv,
                     "u_over_h_sq": s["u"] / s["h"] ** 2})
    lim = mp.sqrt(3) / 8
    print(f"\n  conversion factor b/(q+1)², vs its q→1 limit √3/8 = {float(lim):.8f}")
    print(f"\n  {'anchor':>8} {'b/(q+1)²':>14} {'u/h²':>14} {'vs √3/8':>12}")
    print("  " + "-" * 52)
    for r in rows:
        print(f"  {r['anchor']:>8} {float(r['conversion_b_over_qp1_sq']):>14.9f} "
              f"{float(r['u_over_h_sq']):>14.9f} "
              f"{float((r['conversion_b_over_qp1_sq'] - lim) / lim):>11.2%}")

    # ── 3. the exact h-frame rungs ───────────────────────────────────────
    coeffs = h_frame_series()
    print(f"\n  cos(α − u/2) expanded in h — exact rungs in ℚ(√3):\n")
    print(f"  {'order':>7} {'exact':>34} {'numeric':>16} {'reachable':>11}")
    print("  " + "-" * 72)
    rung_rows = []
    for k, c in enumerate(coeffs):
        reach = "even ✓" if k % 2 == 0 else "ODD ✗"
        # Evaluate the exact ℚ(√3) coefficient at COMPUTE precision.  This used
        # to go through `float(c)` and then re-promote with `mp.mpf(...)`, which
        # collapsed the exact value to float64 and then serialized 50 digits of
        # it — fake precision, caught by the float64-padding ratchet.  sympy's
        # `N(c, 60)` keeps the value exact to well past the 50-dps serialization
        # width; `float(c)` survives only for the aligned console column.
        mval = mp.mpf(str(sp.N(c, 60)))
        print(f"  {'h^' + str(k):>7} {str(c):>34} {float(c):>16.10f} {reach:>11}")
        rung_rows.append({"order": k, "exact": str(c), "numeric": fmt(mval),
                          "reachable_from_u_ladder": (k % 2 == 0)})

    odd_nonzero = [k for k, c in enumerate(coeffs) if k % 2 == 1 and c != 0]
    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  The frame change is an IDENTITY: u = b·h²/(q+1)², exact at every q. So
  uᵏ = (b/(q+1)²)ᵏ·h²ᵏ, and a u-rung of order k lands at h-order exactly 2k.

  A u-ladder therefore spans ONLY the even h-orders. The odd orders are not
  unpopulated by choice — they are unreachable, whatever coefficients are
  chosen. Nonzero odd rungs present in the model: h^{odd_nonzero}.
  h³ = −√3/64 is nonzero and purely irrational; no u-ladder carries it.

  The conversion factor b/(q+1)² is ~0.1949 at both anchors, NOT the
  √3/8 ≈ 0.2165 of its q→1 limit — using the limit is a ~10% error, which is
  what makes the identity worth having over the asymptotic.

  Nothing here is physical: no c_k value, no derivation of α, no accuracy
  gained. The instability is 2.3748% in both frames.
""")

    wb = WitnessBuilder("qbeta-h-frame-rungs", engine="sympy+mpmath")
    wb.set_description(
        "T1 of bean qou-cwin. Establishes that the u→h frame change is an "
        "exact identity (u = b·h²/(q+1)², from ℏ_q(q+1) = h) rather than the "
        "asymptotic 'u ∼ h² near q=1', and derives the consequence that "
        "uᵏ = (b/(q+1)²)ᵏ·h²ᵏ — so a u-rung of order k lands at h-order 2k and "
        "a u-ladder spans only EVEN h-orders. Odd h-orders are unreachable by "
        "any choice of u-coefficients, and the model's h³ rung (−√3/64) is "
        "nonzero and purely irrational. Also records the exact ℚ(√3) h-frame "
        "rungs through h⁷, and that the conversion factor b/(q+1)² ≈ 0.1949 "
        "differs from its q→1 limit √3/8 ≈ 0.2165 by ~10%. Companion to the "
        "sorry-free Lean in QOU/QBeta/LadderFrameChange.lean. No physical "
        "claim: no c_k value, no derivation of α, no accuracy improvement — "
        "the cross-anchor instability is 2.3748% in both frames."
    )
    wb.add_data("ladder_frame_source", "u")
    wb.add_data("ladder_frame_target", "h")
    wb.add_data("h_frame_rungs", rung_rows)
    wb.add_data("odd_orders_with_nonzero_rung", odd_nonzero)
    wb.add_data("anchors", [
        {k: (fmt(v) if isinstance(v, mp.mpf) else v) for k, v in r.items()}
        for r in rows
    ])
    wb.add_data("conversion_q_to_1_limit_sqrt3_over_8", fmt(lim))

    wb.add_assertion(
        name="frame_change_is_an_exact_identity",
        computed=str(int(id1 == 0 and id2 == 0)), expected="1", tolerance=0,
        source="sympy: ℏ_q(q+1) − h and u − b·h²/(q+1)² both simplify to 0 "
               "identically in q. Proved over a generic field in "
               "QOU.QBeta.hbar_mul_succ_eq_h / u_eq_b_mul_h_sq_div.",
    )
    wb.add_assertion(
        name="model_has_a_nonzero_ODD_h_rung_unreachable_from_u",
        computed=str(int(len(odd_nonzero) > 0)), expected="1", tolerance=0,
        source=f"nonzero odd-order rungs at h^{odd_nonzero}; h³ = −√3/64 is "
               "purely irrational. Since uᵏ ∝ h²ᵏ "
               "(QOU.QBeta.u_pow_eq_even_h_pow), no u-ladder can produce any "
               "of them — this is the exact form of 'odd rungs are "
               "structurally unrepresentable in u'.",
    )
    wb.add_assertion(
        name="conversion_factor_is_not_its_q_to_1_limit",
        computed=str(int(
            mp.fabs((rows[0]["conversion_b_over_qp1_sq"] - lim) / lim) > mp.mpf("0.05"))),
        expected="1", tolerance=0,
        source=f"b/(q+1)² = {mp.nstr(rows[0]['conversion_b_over_qp1_sq'], 10)} at the "
               f"proton anchor vs √3/8 = {mp.nstr(lim, 10)}, a "
               f"{float((rows[0]['conversion_b_over_qp1_sq'] - lim) / lim):.1%} difference. "
               "Using the q→1 limit as the conversion is a ~10% error, which "
               "is why the exact identity matters rather than the asymptotic.",
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
