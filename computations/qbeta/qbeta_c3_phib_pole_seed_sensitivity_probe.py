#!/usr/bin/env python3
"""qbeta_c3_phib_pole_seed_sensitivity_probe.py — measure the SENSITIVITY of
the Φ_q-pole-seeded Newton map at the physical anchors. EXPLORATORY
MEASUREMENT — no fit, no wiring.

Context. `thurston-relaxation.md` (conj:algebraic-geometric-dilog-equivalence)
specifies the q₀ → geometry map as Newton iteration on Thurston's gluing
equations for 4₁, *seeded by the Φ_q q-Pochhammer poles* x_k = q₀^{-(2k+1)}
(the Φ_b integral supplies a canonical imaginary offset +iδ — the contour
shift of `phi_b_evaluator.log_phi_b`, δ = half-distance to the first sinh
pole). Rounds 1-2 (this PR + #3562) showed any S-producing map needs
amplification |d·/dq| ~ 1e7 (the u³-lever class). This probe measures where
that amplification could live in the pole-seeded Newton mechanism:

  P1 BASIN FATE per pole seed (k = 0..19, both anchors): Newton on the
     COMPLETE-structure gluing polynomial z²(z−1)² = 1 from z₀ = q₀^{-(2k+1)}
     + iδ. Fates: the two geometric (complex, z(z−1) = −1, e^{±iπ/3}) vs the
     two golden (real, z(z−1) = +1) roots. If every seed's fate is identical
     at both anchors AND far from a basin boundary, the complete-structure
     seeding map is locally constant in q₀ — anchor-BLIND — and the S
     anchor-dependence must enter through the m-DEFORMED equations instead
     (a mechanism-locating result, scope-(a)).
  P2 BASIN-BOUNDARY DISTANCE: for each adjacent seed pair with different
     fates, bisect to the boundary; report min distance from any seed to a
     boundary, in units of the anchor-induced seed shift
     |dz₀/dq|·Δq (Δq = q_p − q_μ). Amplification = seed-shift / distance:
     lever-class sensitivity requires a seed within ~1e-8 of a boundary.
  P3 JACOBIAN CONDITIONING at the geometric root: |d(gluing)/dz|⁻¹ along the
     converged path — rules in/out near-singular Newton steps as the
     amplification source at the complete structure.

Run: python3 -u computations/qbeta/qbeta_c3_phib_pole_seed_sensitivity_probe.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_pole_seed_sensitivity.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from phi_b_substrate_regime import b_substrate  # noqa: E402

set_compute_dps()

Z_GEOM = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)          # geometric root e^{iπ/3}
PHI_GOLD = (1 + mp.sqrt(5)) / 2                       # golden roots 1±… of z(z−1)=1


def newton_fate(z0, maxit=200):
    """Newton on g(z) = z²(z−1)² − 1 (complete structure, m = 1).
    Returns ('geom', z) for the complex-conjugate geometric pair,
    ('gold', z) for the real golden pair, ('none', z) on no convergence."""
    z = mp.mpc(z0)
    for _ in range(maxit):
        g = z ** 2 * (z - 1) ** 2 - 1
        dg = 2 * z * (z - 1) * (2 * z - 1)
        if mp.fabs(dg) < mp.mpf("1e-60"):
            break
        step = g / dg
        z -= step
        if mp.fabs(step) < mp.mpf(10) ** (-mp.mp.dps + 10):
            break
    for root, tag in ((Z_GEOM, "geom"), (mp.conj(Z_GEOM), "geom"),
                      (mp.mpc(PHI_GOLD), "gold"), (mp.mpc(1 - PHI_GOLD), "gold")):
        if mp.fabs(z - root) < mp.mpf("1e-20"):
            return tag, z
    return "none", z


def main() -> int:
    from qou_substrate.constants import q_at, q_muon_at

    anchors = {"proton": q_at(50), "muon": q_muon_at(50)}
    dq = anchors["proton"] - anchors["muon"]
    NSEEDS = 20

    wb = WitnessBuilder("qbeta-c3-phib-pole-seed-sensitivity", engine="mpmath")
    wb.set_description(
        "Sensitivity of the Phi_q-pole-seeded Newton map (thurston-relaxation "
        "/ conj:algebraic-geometric-dilog-equivalence) at the physical "
        "anchors: basin fate per pole seed q0^-(2k+1)+i*delta on the "
        "complete-structure 4_1 gluing polynomial, basin-boundary distances "
        "in units of the anchor-induced seed shift, and Newton-Jacobian "
        "conditioning. Locates (or excludes) the u^3-lever amplification in "
        "the seeding stage. Exploratory; no fit; no c_k wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" Φ_q-pole-seeded Newton sensitivity at the anchors (4₁ complete structure)")
    print("=" * 78)

    # canonical +iδ from the Φ_b contour (half-distance to first sinh pole)
    delta = {}
    for a, q in anchors.items():
        b = b_substrate(q, +1)
        delta[a] = min(mp.im(mp.mpc(0, 1) * mp.pi / b),
                       mp.im(mp.mpc(0, 1) * mp.pi * b)) / 2
    print(f"  canonical iδ (contour shift): proton {mp.nstr(delta['proton'], 8)}")

    # ---- P1: basin fates ----
    fates = {}
    for a, q in anchors.items():
        fates[a] = []
        for k in range(NSEEDS):
            z0 = q ** (-(2 * k + 1)) + mp.mpc(0, 1) * delta[a]
            tag, _ = newton_fate(z0)
            fates[a].append(tag)
    same = fates["proton"] == fates["muon"]
    n_geom = fates["proton"].count("geom")
    n_gold = fates["proton"].count("gold")
    print(f"\n[P1] fates (proton anchor, k=0..{NSEEDS-1}): "
          f"{n_geom} geometric / {n_gold} golden / "
          f"{fates['proton'].count('none')} non-converged")
    print(f"     fate vector: {''.join('G' if f == 'geom' else ('g' if f == 'gold' else '.')  for f in fates['proton'])}")
    print(f"     anchors agree seed-by-seed: {same}")
    wb.add_data("P1_fates", {"proton": fates["proton"], "muon": fates["muon"],
                             "identical_across_anchors": bool(same)})
    wb.add_assertion("p1_fates_anchor_identical",
                     computed=float(1.0 if same else 0.0), expected=1.0,
                     tolerance=0.1,
                     source="seed fates identical across anchors => seeding map "
                            "locally constant at the anchor separation")

    # ---- P2: basin-boundary distance vs anchor-induced seed shift ----
    q_p = anchors["proton"]
    min_bd = mp.inf
    boundaries = []
    fp = fates["proton"]
    for k in range(NSEEDS - 1):
        if fp[k] != fp[k + 1] and "none" not in (fp[k], fp[k + 1]):
            lo = q_p ** (-(2 * k + 1))
            hi = q_p ** (-(2 * (k + 1) + 1))
            tag_lo = fp[k]
            for _ in range(80):  # bisection on the real part of the seed
                mid = (lo + hi) / 2
                tag_mid, _ = newton_fate(mid + mp.mpc(0, 1) * delta["proton"])
                if tag_mid == tag_lo:
                    lo = mid
                else:
                    hi = mid
            boundaries.append((k, (lo + hi) / 2))
            # distance from each neighbor seed to this boundary
            for kk in (k, k + 1):
                d = mp.fabs(q_p ** (-(2 * kk + 1)) - (lo + hi) / 2)
                min_bd = min(min_bd, d)
    # anchor-induced shift of seed k: |d(q^-(2k+1))/dq|·Δq, max over k
    shift_max = max(mp.fabs((2 * k + 1) * q_p ** (-(2 * k + 2)) * dq)
                    for k in range(NSEEDS))
    amp = float(shift_max / min_bd) if min_bd != mp.inf else 0.0
    print(f"\n[P2] basin boundaries found between seed indices: "
          f"{[b[0] for b in boundaries] or 'none'}")
    if min_bd != mp.inf:
        print(f"     min seed→boundary distance = {mp.nstr(min_bd, 6)}")
    print(f"     max anchor-induced seed shift = {mp.nstr(shift_max, 6)}")
    print(f"     amplification (shift/distance) = {amp:.3e}"
          f"   (lever class needs ~1; smooth-blind is ≪ 1)")
    wb.add_data("P2_boundary", {
        "n_boundaries": len(boundaries),
        "min_seed_to_boundary": mp.nstr(min_bd, 12) if min_bd != mp.inf else None,
        "max_anchor_seed_shift": mp.nstr(shift_max, 12),
        "amplification": amp})
    wb.add_assertion("p2_seeding_stage_is_anchor_blind",
                     computed=float(1.0 if amp < 1e-3 else 0.0), expected=1.0,
                     tolerance=0.1,
                     source="amplification << 1 => the complete-structure "
                            "pole-seeding stage CANNOT carry the u^3-lever "
                            "anchor swing; scope-(a): the S anchor-dependence "
                            "must enter via the m-DEFORMED gluing equations")

    # ---- P3: Jacobian conditioning at the geometric root ----
    dg_geom = 2 * Z_GEOM * (Z_GEOM - 1) * (2 * Z_GEOM - 1)
    cond = float(1 / mp.fabs(dg_geom))
    print(f"\n[P3] |g'(z_geom)|⁻¹ = {cond:.4f}  (O(1) ⇒ Newton at the complete "
          f"structure is well-conditioned; no amplification here)")
    wb.add_data("P3_jacobian", {"inv_abs_dg_at_geom_root": cond})
    wb.add_assertion("p3_newton_well_conditioned",
                     computed=cond, expected=0.5, tolerance=0.5,
                     source="|g'(e^{i pi/3})|^-1 = O(1): no near-singular Newton "
                            "step at the complete structure")

    ok = all(a.passed for a in wb.assertions)
    wb.add_data("verdict", (
        "Pole-seeded Newton sensitivity at the anchors (complete structure, "
        "NZ frame): seed fates are identical across anchors, the minimum "
        "seed-to-basin-boundary distance exceeds the anchor-induced seed "
        "shift by orders of magnitude, and the Newton Jacobian is O(1)-"
        "conditioned. MECHANISM-LOCATING RESULT (scope-(a)): the u^3-lever "
        "amplification required for the S anchor-swing does NOT live in the "
        "Phi_q-pole seeding stage of conj:algebraic-geometric-dilog-"
        "equivalence at the complete structure; it must enter through the "
        "m-deformed gluing system (the m(q0) assignment itself), consistent "
        "with #3543's near-singular q0->m diagnosis. No ingredient excluded; "
        "no fit; nothing wired."
        if ok else "INCONCLUSIVE — an assertion failed; re-examine before citing."))
    wb.save()
    print("\nwitness -> computations/qbeta/qbeta-c3-phib-pole-seed-sensitivity.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
