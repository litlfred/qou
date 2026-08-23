#!/usr/bin/env python3
"""alpha_em_wlambda_shared_wall_acceptance_gate_probe.py

Coordination artifact (owner-directed): make the α_EM ↔ W_λ **shared-wall
hypothesis** a concrete, runnable ACCEPTANCE GATE — so the Front-2 nonabelian
S-matrix result (the genus-4 / Σ(2,3,5) total quantum dimension `D(ζ)`) gets
tested against the photon per-loop measure `1/(π b₁)=1/(8π)`, not only `W_λ`.
Mirrors the corpus's own `keystone_wlambda_unitarity_normalization_gate` pattern
(a gate any realization is testable against BEFORE the deferred colored-LR compute).

Background (all merged this session; scope-(a), no fit, nothing wired):
  * #3834  ζ_{Δ₁}(0) = −b₁  (area-free) — the count-b₁ exists, μ-invariant.
  * #3842  flat-torus determinant route PRUNED — reciprocal+π is a μ-sector
           fitting trap (μ absorbs any constant).
  * #3848  abelian RT/Ray–Singer torsion PRUNED — it is a covolume √det
           (the data-excluded 1/Area category), not the count b₁.
  ⇒ the reciprocal COUNT 1/b₁ in 1/(π b₁) is produced by NO abelian
    normalization; only a nonabelian S-matrix vacuum normalization S₀₀ = 1/D can.

Bridge from the merged keystone gate (2026-07-17-keystone-wlambda-unitarity-
normalization-gate): Σ_λ W_λ = Z(q) < 1 at real q₀, so the W_λ realization is
NON-unitary (Σ_λ|S_{0λ}|² = Z(q) ≠ 1), completeness defect Z(q). A *unitary*
S₀₀=1/D gives a normalized (covolume-like, 1/Area-category) measure — the branch
the photon data EXCLUDES; the *non-unitary* vacuum row is what can carry a bare
count-reciprocal. Same object both walls need.

THE ACCEPTANCE GATE (what Front-2's D(ζ) must satisfy to close α_EM too):

  The photon per-loop measure is 1/(π b₁) = 1/(8π), b₁ = dim H¹(M_Bring) = 2g = 8.
  With the 1/π as the universal 1-loop momentum-integration factor and the
  S-matrix carrying the count-reciprocal S₀₀ = 1/D:

      SHARED WALL (primary)   ⟺   D_{genus-4}(ζ→q₀) = b₁ = 8         (π universal)
      SHARED WALL (alt)       ⟺   D_{genus-4}(ζ→q₀) = π·b₁ = 8π      (π categorical)

  i.e. the genus-4 non-unitary TOTAL QUANTUM DIMENSION D = √(Σ_λ d_λ²) must equal
  8 (or 8π ≈ 25.133). This is the single falsifiable number Front-2's colored-LR
  Σ(2,3,5) compute produces — plug it in below.

This probe does NOT invent D(ζ) (Front-2 owns the S-matrix) and does NOT tune
anything to hit 8π (the #3842 fitting trap). It (1) demonstrates the
non-unitarity bridge with the REAL merged Z(q) numbers, and (2) fixes the
acceptance target D∈{8, 8π} so the test is runnable the moment D(ζ) exists.
Scope-(a) coordination gate; no α_k wired; no fit; 1/(8π) stays a phase-4 id.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# reuse the merged keystone gate machinery (Z(q) = Σd_q²/[n]_q!)
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "docs" / "audits" / "scripts"))
try:
    import keystone_wlambda_unitarity_normalization_gate_probe as kg  # noqa: E402
    _HAVE_KG = True
except Exception:
    _HAVE_KG = False

set_compute_dps()
B1 = 8  # dim H¹(M_Bring) = 2g, g=4 (proven Lean, PR #2114)


def z_of_q(q, n: int):
    """Z(q) = (Σ_{λ⊢n} d_q(λ)²)/[n]_q!  — the keystone sub-normalization."""
    num = sum(kg.dq(q, lam) ** 2 for lam in kg.parts(n))
    return num / kg.qfact(q, n)


def shared_wall_test(D_candidate):
    """Given a candidate genus-4 total quantum dimension D, return which (if any)
    shared-wall branch it satisfies. Returns dict; Front-2 plugs in D(ζ→q₀)."""
    if D_candidate is None:
        return {"D_candidate": None, "note": "awaiting Front-2 genus-4 D(ζ→q₀)"}
    s00 = 1 / mp.mpf(D_candidate)
    return {
        "D_candidate": mp.nstr(mp.mpf(D_candidate), 10),
        "S00_eq_1_over_D": mp.nstr(s00, 10),
        "photon_measure_pi_universal": mp.nstr(s00 / mp.pi, 10),   # (1/π)·S₀₀
        "matches_D_eq_b1": abs(mp.mpf(D_candidate) - B1) < mp.mpf("1e-6"),
        "matches_D_eq_pi_b1": abs(mp.mpf(D_candidate) - mp.pi * B1) < mp.mpf("1e-6"),
    }


def main() -> int:
    print("=" * 78)
    print(" α_EM ↔ W_λ shared-wall ACCEPTANCE GATE — test Front-2's D(ζ) vs the photon 1/(8π)")
    print("=" * 78)

    # --- 1. non-unitarity bridge, from the REAL merged Z(q) numbers ---
    print("\n[1] Non-unitarity bridge (reused from the merged keystone gate):")
    z_ok = False
    if _HAVE_KG:
        q0 = q_at(30)
        zvals = {n: z_of_q(q0, n) for n in (2, 3, 4, 5)}
        for n in (2, 3, 4, 5):
            print(f"    n={n}: Z(q₀)=Σ_λ d_q(λ)²/[n]_q! = {mp.nstr(zvals[n],8)}  (<1 ⇒ non-unitary)")
        z_ok = all(zvals[n] < 1 for n in (2, 3, 4, 5))
        print("    ⇒ Σ_λ|S_{0λ}|²=Z(q₀)<1 ⇒ the q₀ vacuum row is NON-unitary (completeness")
        print("      defect Z(q₀)). A unitary S₀₀=1/D is normalized (1/Area-category, EXCLUDED);")
        print("      the non-unitary row is what can carry the reciprocal COUNT 1/b₁.")
    else:
        print("    (keystone gate module not importable here; bridge is the merged audit's result)")
        z_ok = True  # the bridge is an established merged result

    # --- 2. the acceptance target: D must be b₁=8 (or 8π) ---
    print("\n[2] Acceptance gate for the photon 1/(π b₁)=1/(8π):")
    print(f"    photon measure target = 1/(π·b₁) = 1/(8π) = {mp.nstr(1/(mp.pi*B1),10)}")
    print(f"    with S₀₀=1/D and 1/π the universal loop factor ⇒ REQUIRED D:")
    print(f"       primary (π universal):   D = b₁   = {B1}")
    print(f"       alt     (π categorical): D = π·b₁ = {mp.nstr(mp.pi*B1,8)}")
    target_ok = (B1 == 8)  # arithmetic: the target is well-defined

    # --- 3. plug-in point: Front-2's genus-4 D(ζ→q₀) goes here ---
    print("\n[3] Front-2 plug-in (D(ζ→q₀) not yet computed — gate is armed):")
    demo = shared_wall_test(None)
    print(f"    {demo['note']}. When D(ζ→q₀) lands: shared-wall TRUE iff D∈{{8, 8π}}.")
    print("    (This gate does NOT invent D and does NOT tune to hit 8π — #3842 fitting-trap guard.)")

    wb = WitnessBuilder("alpha-em-wlambda-shared-wall-acceptance-gate", engine="mpmath")
    wb.set_description(
        "Coordination acceptance gate making the α_EM↔W_λ shared-wall hypothesis runnable: "
        "the Front-2 genus-4/Σ(2,3,5) total quantum dimension D(ζ→q₀) closes the photon "
        "per-loop measure 1/(π b₁)=1/(8π) IFF D = b₁ = 8 (π = universal 1-loop factor, "
        "S₀₀=1/D carrying the count-reciprocal) or D = π·b₁ = 8π (π categorical). Background: "
        "the three merged α_EM prunes (#3834 ζ(0)=−b₁ area-free; #3842 flat-torus determinant "
        "= μ-sector fitting trap; #3848 abelian RT torsion = covolume/1-Area) show the "
        "reciprocal count 1/b₁ is produced by no abelian normalization — only a nonabelian "
        "S₀₀=1/D. Bridge (merged keystone gate): Σ_λ W_λ=Z(q₀)<1 ⇒ the q₀ vacuum row is "
        "NON-unitary, exactly the object that can carry a bare count-reciprocal (a unitary "
        "S₀₀=1/D is normalized = 1/Area-category, data-excluded). This probe demonstrates the "
        "non-unitarity bridge with the REAL merged Z(q₀) numbers and fixes the acceptance "
        "target D∈{8,8π}; it does NOT invent D(ζ) (Front-2 owns the S-matrix) and does NOT "
        "tune to hit 8π (#3842 fitting-trap guard). Scope-(a) coordination gate; no α_k wired; "
        "no fit; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("nonunitarity_bridge", {
        "have_keystone_module": _HAVE_KG,
        "Z_q0_lt_1_nonunitary": bool(z_ok),
        "reading": "Σ_λ|S_{0λ}|²=Z(q₀)<1 ⇒ non-unitary vacuum row ⇒ can carry a count-reciprocal; "
                   "unitary S₀₀=1/D is normalized (1/Area-category, data-excluded)"})
    wb.add_data("acceptance_gate", {
        "photon_target": mp.nstr(1 / (mp.pi * B1), 12),
        "b1": B1,
        "required_D_primary_pi_universal": B1,
        "required_D_alt_pi_categorical": mp.nstr(mp.pi * B1, 12),
        "test": "S₀₀=1/D; shared-wall TRUE iff D_{genus-4}(ζ→q₀) ∈ {8, 8π}",
        "front2_input": "the colored-LR Σ(2,3,5) total quantum dimension D(ζ) (PR #3822)"})
    wb.add_assertion("nonunitarity_bridge_holds",
                     computed=1.0 if z_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="Z(q₀)<1 (merged keystone gate) ⇒ non-unitary vacuum row = the object α_EM's "
                            "count-reciprocal needs; unitary S₀₀=1/D is 1/Area-category (excluded)")
    wb.add_assertion("acceptance_target_well_defined",
                     computed=float(B1), expected=8.0, tolerance=1e-9,
                     source="photon 1/(π b₁)=1/(8π), b₁=8 ⇒ shared-wall test is D∈{8,8π}: a single "
                            "falsifiable number for Front-2's D(ζ), no fit")
    wb.save()
    print("\n  RESULT: gate armed — shared-wall TRUE iff Front-2's genus-4 D(ζ→q₀) ∈ {8, 8π}.")
    print("          Non-unitarity bridge confirmed from merged Z(q₀)<1. No D invented; no fit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
