#!/usr/bin/env python3
"""Spike: extended q-dilog / Bloch-Wigner search for λ_scale.

Follow-on to PR #923. Three open paths from the q-dilog spike audit:

  (a) Operator-valued V̂_S spectral coordinates from the canonical
      proton braid in H_3, evaluated through Li_2^q. Signed V̂ values
      are passed directly (not |V̂|) since Li_2^q is well-defined for
      any |z| < q.
  (b) Bloch-Wigner regulator D(z) at primitive n-th roots of unity
      for n covering the ℚ(ζ_60) trace-field tower. This is the
      1-variable basis; true 2-variable Bloch-Wigner / 5-term
      Rogers pentagon pairings are deferred (research-level
      extension noted in the companion audit doc).
  (c) Hyperbolic-knot volumes for the Tier-0 basis (matches
      bring_bloch_tier0_search.py).

PSLQ at 80 dps, max coefficient 10^30 (matching bring_bloch tier 5).
"""
from __future__ import annotations

import sys
import time
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
    For z = e^{iθ} on the unit circle, D(z) = Cl_2(θ) (Clausen function).
    """
    if z == 0:
        return mp.mpf(0)
    li2 = mp.polylog(2, z)
    z_arg = mp.arg(1 - z) if z != 1 else mp.mpf(0)
    z_log = mp.log(mp.fabs(z))
    return mp.im(li2) + z_arg * z_log


def main():
    t_start = time.monotonic()
    mp.mp.dps = 80

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Q0i = 1 / Q0
    h = Q0 - Q0i
    G = mp.catalan
    PI = mp.pi

    # Targets
    lambda_p = mp.mpf("2.4599527869")
    vol_eff = lambda_p * 8 * G  # ≈ 18.0259

    print(f"q_0 = {mp.nstr(Q0, 30)}")
    print(f"target λ_p = {mp.nstr(lambda_p, 12)}")
    print(f"target Vol_eff_p = {mp.nstr(vol_eff, 12)}")
    print()

    # ── (a) Operator-valued V̂_S spectral coordinates ────────────
    # Li_2^q(z) is well-defined for any |z| < q (positive or negative),
    # so we pass the signed V̂ values directly. The label is V̂_i^λ
    # (signed), not |V̂_i^λ|.
    print("Path (a): Li_2^q at V̂_i^λ (signed) for proton braid (H_3)")
    v_hat_basis: list[tuple[str, mp.mpf]] = []
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        V = per_irrep_V_hat(1, 0, shape)
        for i, v in enumerate(V):
            v_mp = mp.mpf(repr(v))
            # Li_2^q convergence radius is |z| < q ≈ 1.11
            if mp.fabs(v_mp) < Q0:
                val = li_2_q(v_mp, Q0, Q0i)
                v_hat_basis.append((f"Li2q(V̂[{shape},{i}]={float(v):+.3f})", val))
                print(f"  Li2q(V̂_{i}^{shape} = {float(v):+.4f}) = {mp.nstr(val, 10)}")
            else:
                print(f"  V̂_{i}^{shape} = {float(v):+.4f} (|V| ≥ q, skip)")
    print()

    # ── (b) Bloch-Wigner D at primitive ζ_n roots of unity ───────
    # This is the 1-variable Bloch-Wigner basis covering the
    # ℚ(ζ_60) trace-field tower. True 2-variable Bloch-Wigner /
    # 5-term Rogers pentagon pairings would expand this further;
    # deferred to companion audit doc's "still open" list.
    print("Path (b): D(ζ_n) at primitive n-th roots of unity")
    # Primitive ζ_n has argument 2π/n. We use exp(2πi/n) consistently.
    primitive_zeta_args = [
        (3, "ζ_3"),
        (4, "ζ_4 = i"),
        (5, "ζ_5"),
        (6, "ζ_6"),
        (8, "ζ_8"),
        (10, "ζ_10"),
        (12, "ζ_12"),
        (15, "ζ_15"),
        (20, "ζ_20"),
        (60, "ζ_60"),
    ]
    bw_basis: list[tuple[str, mp.mpf]] = []
    for n, label in primitive_zeta_args:
        z = mp.exp(mp.mpc(0, 2 * PI / n))
        d = bloch_wigner(z)
        bw_basis.append((f"D({label})", d))
        print(f"  D({label} = exp(2πi/{n})) = {mp.nstr(d, 10)}")
    print()

    # ── (c) Tier-0 hyperbolic-knot volumes ────────────────────
    # Matches bring_bloch_tier0_search.py basis exactly. Volumes
    # are SnapPy-canonical literals (no claimed structural identity
    # beyond the standard hyperbolic-volume calculation).
    print("Path (c): Tier-0 hyperbolic-knot volumes")
    knot_vols = [
        # Vol(4_1) = 2·Cl_2(π/3) is the Cl_2(π/3) closed-form identity
        # (Adams 1985); included here as a SnapPy-canonical anchor.
        ("Vol(4_1)", 2 * bloch_wigner(mp.exp(mp.mpc(0, PI/3)))),
        ("Vol(B_3)", 8 * G),
        ("Vol(5_2)", mp.mpf("2.828122088")),
        ("Vol(6_1)", mp.mpf("3.16396322")),
        ("Vol(7_4)", mp.mpf("5.13794120")),
        ("Vol(Whitehead)", mp.mpf("3.66386237")),
    ]
    knot_basis: list[tuple[str, mp.mpf]] = []
    for name, v in knot_vols:
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
    any_error = False
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
                results.append({"target": target_name, "outcome": "no_relation"})
                continue
            if rel[0] == 0:
                nonzero = [(name, int(a)) for (name, _), a in zip(full_basis, rel[1:]) if a != 0]
                print(f"  → basis-internal trivial relation (target coef 0):")
                for n, a in nonzero[:5]:
                    print(f"      {a:>+12d} · {n}")
                results.append({"target": target_name, "outcome": "trivial",
                                "basis_terms": nonzero})
                continue
            terms = [(name, int(a)) for (name, _), a in zip(full_basis, rel[1:]) if a != 0]
            print(f"  → relation: a0 = {rel[0]}; {len(terms)} non-zero basis terms")
            for n, a in terms[:8]:
                print(f"      {a:>+12d} · {n}")
            results.append({
                "target": target_name,
                "outcome": "nontrivial_relation",
                "a0": int(rel[0]),
                "terms": terms,
            })
        except Exception as e:
            print(f"  → PSLQ FAILED: {e}")
            results.append({"target": target_name, "outcome": "error", "error": str(e)})
            any_error = True
        print()

    # Witness — pass start_time so durationMs reflects real runtime
    w = WitnessBuilder("q-dilog-vhat-spike-lambda-scale", engine="mpmath",
                        start_time=t_start)
    w.set_description(
        "Extended spike for substrate-pure λ_scale: tests three paths "
        "left open by q-dilog-tower-spike (PR #923): (a) V̂_S spectral "
        "coords (signed) from canonical proton braid via Li_2^q, "
        "(b) Bloch-Wigner D at primitive ζ_n for n ∈ {3,4,5,6,8,10,12,15,20,60} "
        "(1-variable; 2-variable pairings deferred), "
        "(c) Tier-0 hyperbolic-knot volumes. PSLQ at 80 dps, "
        "maxcoeff 10^30, against λ_p / Vol_eff_p / Vol_eff_p - 8G. "
        "Companion to PR #888 + #904 + #923."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 80)
    # Store maxcoeff as string — int 10^30 exceeds JS safe-integer range
    w.add_parameter("pslq_maxcoeff", str(10**30))
    w.add_data("basis_path_a_size", len(v_hat_basis))
    w.add_data("basis_path_b_size", len(bw_basis))
    w.add_data("basis_path_c_size", len(knot_basis))
    w.add_data("basis_total_size", len(full_basis))
    w.add_data("results", [
        {"target": r["target"],
         "outcome": r["outcome"],
         "a0": r.get("a0"),
         "n_nonzero_terms": len(r.get("terms", [])) if r["outcome"] == "nontrivial_relation" else 0,
         "error": r.get("error")}
        for r in results
    ])
    any_nontrivial = any(r["outcome"] == "nontrivial_relation" for r in results)
    # Assertion fails (computed=0) if any target errored OR a non-trivial
    # relation was found — both warrant follow-up.
    w.add_assertion(
        "all_targets_searched_no_nontrivial_relation",
        computed=float(not any_nontrivial and not any_error),
        expected=1.0,
    )
    out = w.save()
    print(f"Witness: {out.name}")


if __name__ == "__main__":
    main()
