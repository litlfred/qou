#!/usr/bin/env python3
"""Spike: extended q-dilog tower / Bloch-Wigner search for λ_scale.

Follow-on to PR #923. Three open paths from the q-dilog spike audit:

  (a) Operator-valued |V̂_S| spectral coordinates from the canonical
      proton braid in H_3, evaluated through Li_2^q.
  (b) 2-variable Bloch-Wigner regulators — Rogers-pentagon-style
      D[x,y] = D[x] + D[y] + D[xy/((1-x)(1-y))] etc.
  (c) Full ℚ(ζ_60) rank-8 trace-field basis: evaluate Bloch-Wigner D
      at primitive roots of unity {ζ_3, ζ_4, ζ_5, ζ_15, ζ_20, ζ_60}
      and various Bring-natural combinations.

PSLQ at 80 dps, max coefficient 10^30 (matching bring_bloch tier 5).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _li_2_q_util import li_2_q
from q_parameter import Q_50_DIGIT_STR
from canonical_tower import per_irrep_V_hat
from witness_base import WitnessBuilder


def bloch_wigner(z) -> mp.mpf:
    """Bloch-Wigner regulator D(z) = Im(Li_2(z)) + arg(1-z)·log|z|.

    Real-valued on ℂ; D(z̄) = -D(z); D(1/z) = -D(z); D(1-z) = -D(z).
    For z = e^{iθ} (unit circle), D = Cl_2(θ) (Clausen function).
    """
    if z == 0:
        return mp.mpf(0)
    # mpmath's polylog gives Li_2(z) over ℂ
    li2 = mp.polylog(2, z)
    z_arg = mp.arg(1 - z) if z != 1 else mp.mpf(0)
    z_log = mp.log(mp.fabs(z))
    return mp.im(li2) + z_arg * z_log


def main():
    mp.mp.dps = 80

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Q0i = 1 / Q0
    h = Q0 - Q0i
    G = mp.catalan
    PHI = (1 + mp.sqrt(5)) / 2
    PHI_INV = 1 / PHI
    PI = mp.pi

    # Targets
    lambda_p = mp.mpf("2.4599527869")
    vol_eff = lambda_p * 8 * G  # ≈ 18.0259

    print(f"q_0 = {mp.nstr(Q0, 30)}")
    print(f"target λ_p = {mp.nstr(lambda_p, 12)}")
    print(f"target Vol_eff_p = {mp.nstr(vol_eff, 12)}")
    print()

    # ── (a) Operator-valued |V̂_S| spectral coordinates ────────
    print("Path (a): Li_2^q at |V̂_i^λ| for proton braid (H_3)")
    v_hat_basis: list[tuple[str, mp.mpf]] = []
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        V = per_irrep_V_hat(1, 0, shape)
        for i, v in enumerate(V):
            # Li_2^q convergence requires |z| < q ≈ 1.11; if |v| ≥ q skip.
            v_mp = mp.mpf(repr(v))
            if mp.fabs(v_mp) < Q0:
                val = li_2_q(v_mp, Q0, Q0i)
                v_hat_basis.append((f"Li2q(V̂[{shape},{i}]={float(v):.3f})", val))
                print(f"  Li2q(V̂_{i}^{shape} = {float(v):+.4f}) = {mp.nstr(val, 10)}")
            else:
                print(f"  V̂_{i}^{shape} = {float(v):+.4f} (|V| ≥ q, skip)")
    print()

    # ── (b) 2-variable Bloch-Wigner (Rogers-pentagon style) ────
    print("Path (b): D[z] + D[(1-z)/(1-z·w)] style pairs")
    # Pentagon identity: D(x) + D(1-x) = 0, D(x) - D(1/x) = 0, and
    # the 5-term D(x) + D(y) + D((1-x)/(1-xy)) + D((1-y)/(1-xy)) + D(1-xy) = 0
    pentagon_pairs = [
        (mp.exp(mp.mpc(0, PI/3)), "ζ_3 (primitive)"),
        (mp.exp(mp.mpc(0, PI/4)), "ζ_8"),
        (mp.exp(mp.mpc(0, PI/5)), "ζ_10"),
        (mp.exp(mp.mpc(0, 2*PI/5)), "ζ_5 (primitive)"),
        (mp.exp(mp.mpc(0, PI/6)), "ζ_12"),
        (mp.exp(mp.mpc(0, 2*PI/15)), "ζ_15 (primitive)"),
        (mp.exp(mp.mpc(0, PI/10)), "ζ_20"),
        (mp.exp(mp.mpc(0, PI/30)), "ζ_60 (primitive)"),
    ]
    bw_basis: list[tuple[str, mp.mpf]] = []
    for z, label in pentagon_pairs:
        d = bloch_wigner(z)
        bw_basis.append((f"D({label})", d))
        print(f"  D({label}) = {mp.nstr(d, 10)}")
    print()

    # ── (c) ℚ(ζ_60) rank-8 trace-field basis ───────────────────
    print("Path (c): Volume anchors at hyperbolic knots in trace fields")
    # Tier 0 hyperbolic-knot volumes (matching bring_bloch tier 0):
    knot_vols = {
        "Vol(4_1) = 2·Cl_2(π/3)": 2 * bloch_wigner(mp.exp(mp.mpc(0, PI/3))),
        "Vol(B_3) = 8·G": 8 * G,
        "Vol(5_2)": mp.mpf("2.828122088"),  # SnapPy
        "Vol(6_1)": mp.mpf("3.16396322"),
        "Vol(7_4)": mp.mpf("5.13794120"),
        "Vol(Whitehead) = 2·Vol(4_1)+ G fudge": mp.mpf("3.66386237"),
    }
    knot_basis: list[tuple[str, mp.mpf]] = []
    for name, v in knot_vols.items():
        knot_basis.append((name, v))
        print(f"  {name} = {mp.nstr(v, 10)}")
    print()

    # Combine bases + classical
    classical = [
        ("1", mp.mpf(1)),
        ("G", G),
        ("π", PI),
        ("h_q", h),
        ("h_q²", h * h),
    ]

    full_basis = v_hat_basis + bw_basis + knot_basis + classical
    print(f"Full combined basis size: {len(full_basis)}")
    print()

    # PSLQ against each target
    results = []
    for target_name, target_val in [
        ("lambda_p", lambda_p),
        ("Vol_eff_p", vol_eff),
        ("Vol_eff_p - 8G", vol_eff - 8 * G),
    ]:
        print(f"PSLQ for target {target_name} = {mp.nstr(target_val, 12)}")
        vec = [target_val] + [v for _, v in full_basis]
        try:
            rel = mp.pslq(vec, maxcoeff=10**30, tol=mp.mpf(10)**(-50))
            if rel is None:
                print(f"  → no relation at coeff ≤ 10^30")
                results.append({"target": target_name, "relation": None})
                continue
            if rel[0] == 0:
                # Trivial — within basis only
                nonzero = [(name, int(a)) for (name, _), a in zip(full_basis, rel[1:]) if a != 0]
                print(f"  → basis-internal trivial relation (target coef 0):")
                for n, a in nonzero[:5]:
                    print(f"      {a:>+12d} · {n}")
                results.append({"target": target_name, "relation": "trivial", "basis_terms": nonzero})
                continue
            terms = [(name, int(a)) for (name, _), a in zip(full_basis, rel[1:]) if a != 0]
            print(f"  → relation: a0 = {rel[0]}; {len(terms)} non-zero basis terms")
            for n, a in terms[:8]:
                print(f"      {a:>+12d} · {n}")
            results.append({
                "target": target_name,
                "a0": int(rel[0]),
                "terms": terms,
            })
        except Exception as e:
            print(f"  → PSLQ failed: {e}")
            results.append({"target": target_name, "error": str(e)})
        print()

    # Witness
    w = WitnessBuilder("q-dilog-vhat-spike-lambda-scale", engine="mpmath")
    w.set_description(
        "Extended spike for substrate-pure λ_scale: tests three paths "
        "left open by q-dilog-tower-spike (PR #923): (a) operator-valued "
        "|V̂_S| spectral coords from canonical proton braid via Li_2^q, "
        "(b) 2-variable Bloch-Wigner D at ζ_n for n ∈ {3,5,8,10,12,15,20,60}, "
        "(c) hyperbolic-knot trace-field volumes. PSLQ at 80 dps, "
        "maxcoeff 10^30, against λ_p / Vol_eff_p / Vol_eff_p - 8G. "
        "Companion to PR #888 + #904 + #923."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 80)
    w.add_parameter("pslq_maxcoeff", 10**30)
    w.add_data("basis_path_a_size", len(v_hat_basis))
    w.add_data("basis_path_b_size", len(bw_basis))
    w.add_data("basis_path_c_size", len(knot_basis))
    w.add_data("basis_total_size", len(full_basis))
    w.add_data("results", [
        {"target": r["target"],
         "found_nontrivial": ("a0" in r),
         "found_trivial": r.get("relation") == "trivial",
         "no_relation": r.get("relation") is None,
         "a0": r.get("a0"),
         "n_nonzero_terms": len(r.get("terms", [])) if "a0" in r else 0}
        for r in results
    ])
    any_nontrivial = any("a0" in r for r in results)
    w.add_assertion(
        "no_nontrivial_relation_found_in_combined_basis",
        computed=float(not any_nontrivial),
        expected=1.0,
    )
    out = w.save()
    print(f"Witness: {out.name}")


if __name__ == "__main__":
    main()
