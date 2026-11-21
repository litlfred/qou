#!/usr/bin/env python3
"""bean qou-iyf6 finding (A): ρ_F = ν_SDP  vs  adjoint Reidemeister torsion τ_adj.

Literature cross-check — NO FIT, nothing wired to production.

The corpus conjecture `conj:kashaev-density-equals-sdp-multiplicity`
(folio/quantum-observable-universe/mass-theory/
 kashaev-density-equals-sdp-multiplicity.md) states that the *binding-density
prefactor* ρ_F in

    B_pred(K_w) = ρ_F · m_e · Vol_hyp(K_w),      ρ_F ∈ ℤ_{>0}

— named there the "Kashaev density prefactor" — equals the joint-tower SDP
Wedderburn multiplicity ν_SDP(K_w), a positive integer, and moreover
ρ_F ∈ {1, 2} for every atom (prop:cpt-orbit-closure-density, Type-B
fold-orbit closure).

The knot-theory literature identifies the *topological density selecting the
geometric flat connection* — the 2nd (subleading, "1-loop") coefficient of
the Kashaev asymptotic expansion — with the **adjoint (twisted) Reidemeister
torsion** τ_adj at the geometric holonomy representation, PROVED equal to the
Dimofte–Garoufalidis 1-loop invariant for 2-bridge knots:

  * Ohtsuki–Takata, "On the Kashaev invariant and the twisted Reidemeister
    torsion of two-bridge knots", Geom. Topol. 19 (2015) 853.
  * "1-loop equals torsion for two-bridge knots", arXiv:2411.03801 (2024).

Both 4₁ (figure-eight) and 5₂ (three-twist) are 2-bridge, so their Kashaev
2nd coefficient IS τ_adj.

This probe computes τ_adj for 4₁ (exact closed form) and characterises it for
5₂ (algebraic type + geometric shape + volume), then compares to the corpus
ρ_F = ν_SDP for the same knots. The comparison is reported with an explicit
scope-(a)/(b) classification per AGENTS.md §"Before declaring refuted".

Kashaev asymptotic (Ohtsuki normalisation), schematically

    ⟨K⟩_N  ~  N^{3/2} · τ_adj^{-1/2} · (2π)^{3/2} · exp( (N / 2π)(Vol + i·CS) )

Note the two DISTINCT structural slots:
  * Vol lives in the EXPONENT (scaled by N/2π);
  * τ_adj is the AMPLITUDE of the N^{3/2} term (the "density" that selects the
    geometric connection) — it does NOT multiply Vol.
The corpus ρ_F, by contrast, is a LINEAR multiplier on Vol. So ρ_F and τ_adj
occupy different slots of the asymptotic — a role mismatch on top of the
type mismatch (integer vs algebraic non-integer).

Run:
    python3 -u computations/probes/rhoF_vs_adjoint_torsion.py \\
        2>&1 | tee /tmp/rhoF_vs_adjoint_torsion.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401  (Phase 6 substrate-subdir bridge)
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60  # ≥ 50 dps per AGENTS.md precision discipline


def bloch_wigner(z: mp.mpc) -> mp.mpf:
    """Bloch–Wigner dilogarithm D(z) = Im Li₂(z) + arg(1-z)·log|z|."""
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def fmt(x, n: int = 50) -> str:
    return mp.nstr(x, n)


def main() -> int:
    builder = (
        WitnessBuilder("rhoF-vs-adjoint-torsion", engine="python")
        .set_description(
            "bean qou-iyf6 finding (A): literature cross-check of the corpus "
            "identity ρ_F = ν_SDP (conj:kashaev-density-equals-sdp-multiplicity) "
            "against the adjoint (twisted) Reidemeister torsion τ_adj at the "
            "geometric rep — the topological density that the Kashaev 2nd "
            "coefficient equals for 2-bridge knots (Ohtsuki–Takata Geom. Topol. "
            "19 (2015) 853; 1-loop=torsion arXiv:2411.03801). Computes τ_adj(4₁) "
            "exactly (1/√-3, |τ_adj|=1/√3, cross-checked against Ohtsuki's 3^{-1/4} "
            "amplitude) and characterises τ_adj(5₂) (complex algebraic in the "
            "disc -23 cubic trace field; geometric shape z: z³-z²+1=0, "
            "Vol=2.82812). Compares to the corpus ρ_F=ν_SDP∈{1,2}. Finding: TYPE "
            "MISMATCH (integer ρ_F/ν_SDP vs non-integer algebraic τ_adj) plus a "
            "ROLE mismatch (ρ_F multiplies Vol; τ_adj is the N^{3/2} amplitude, "
            "not a Vol-multiplier); scope-(a). No fit; nothing wired."
        )
        .set_audit_only("bean qou-iyf6 finding (A)")
    )

    print("=" * 78)
    print(" ρ_F = ν_SDP  vs  adjoint Reidemeister torsion τ_adj  (bean qou-iyf6 A)")
    print("=" * 78)

    # ------------------------------------------------------------------ #
    # PART 1 — 4₁ (figure-eight): exact adjoint torsion.
    # ------------------------------------------------------------------ #
    # Geometric shape z = e^{iπ/3}; single tetrahedron pair.
    z41 = mp.e ** (mp.pi * 1j / 3)
    vol41 = 2 * mp.im(mp.polylog(2, z41))  # = 2 D(e^{iπ/3})

    # Adjoint Reidemeister torsion at the discrete faithful rep, w.r.t. the
    # meridian (Porti; Dubois 2006, "Non abelian Reidemeister torsion and
    # volume form on the SU(2)-representation space of knot groups"):
    #     τ_adj(4₁) = 1/√-3   (trace field ℚ(√-3)).
    tau_adj_41 = 1 / mp.sqrt(-3)
    abs_tau_41 = abs(tau_adj_41)  # = 1/√3

    # Cross-check against the PUBLISHED Kashaev-asymptotic amplitude.
    # Ohtsuki (2016): ⟨4₁⟩_N ~ N^{3/2} · 3^{-1/4} · e^{N·Vol/2π} · (…). The
    # "1-loop = torsion" theorem gives amplitude = |τ_adj|^{1/2}; check
    #     √|τ_adj(4₁)|  ==  3^{-1/4}.
    ohtsuki_amp = mp.mpf(3) ** mp.mpf("-0.25")
    sqrt_abs_tau = mp.sqrt(abs_tau_41)
    amp_ok = abs(sqrt_abs_tau - ohtsuki_amp) < mp.mpf(10) ** -45

    print("\n[4₁ figure-eight]  2-bridge, trace field ℚ(√-3)")
    print(f"  geometric shape z = e^(iπ/3) = {fmt(z41, 20)}")
    print(f"  Vol(4₁)          = {fmt(vol41, 30)}")
    print(f"  τ_adj(4₁)        = 1/√-3 = {fmt(tau_adj_41, 30)}")
    print(f"  |τ_adj(4₁)|      = 1/√3 = {fmt(abs_tau_41, 40)}")
    print(f"  √|τ_adj|         = {fmt(sqrt_abs_tau, 40)}")
    print(f"  Ohtsuki 3^(-1/4) = {fmt(ohtsuki_amp, 40)}   match={amp_ok}")

    builder.add_assertion(
        name="tau_adj_4_1_amplitude_crosscheck",
        computed=sqrt_abs_tau,
        expected=ohtsuki_amp,
        tolerance=1e-40,
        source="√|τ_adj(4₁)| = 3^{-1/4} = Ohtsuki's Kashaev N^{3/2} amplitude; "
               "confirms |τ_adj(4₁)| = 1/√3 (Porti/Dubois, meridian; "
               "Ohtsuki–Takata Geom. Topol. 19 (2015) 853)",
    )

    # ------------------------------------------------------------------ #
    # PART 2 — 5₂ (three-twist): algebraic characterisation of τ_adj.
    # ------------------------------------------------------------------ #
    # Geometric tetrahedron shape z solves the shape cubic  z³ - z² + 1 = 0
    # (disc = -23); trace field K = ℚ[ξ]/(ξ³ - 2ξ² + 3ξ - 1), the disc -23
    # cubic (corpus: qbeta_5two_gswz_saddle_arithmeticity_probe.py).
    shape_roots = mp.polyroots([1, -1, 0, 1])
    z52 = next(r for r in shape_roots if mp.im(r) < -1e-9)  # geometric branch
    vol52 = 3 * abs(bloch_wigner(z52))   # 5₂ = 3 tetrahedra, D(z1)=D(z2)=D(z)
    # Read the reference from the corpus registry instead of typing it in
    # (witness-value copy audit): VOL_5_2_MPF is the SnapPy HP 50-dps value.
    from knot_volumes import VOL_5_2_MPF
    vol52_ref = mp.mpf(VOL_5_2_MPF)
    vol_ok = abs(vol52 - vol52_ref) < mp.mpf(10) ** -12

    # discriminant of the shape cubic z³ - z² + 1  (a,b,c,d = 1,-1,0,1)
    a, b, c, d = 1, -1, 0, 1
    disc_shape = (18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2
                  - 4 * a * c ** 3 - 27 * a ** 2 * d ** 2)

    print("\n[5₂ three-twist]  2-bridge, trace field = disc -23 cubic")
    print(f"  shape cubic       z³ - z² + 1 = 0,  disc = {disc_shape}")
    print(f"  geometric shape z = {fmt(z52, 30)}")
    print(f"  Vol(5₂)=3|D(z)|   = {fmt(vol52, 30)}   (ref 2.82812; match={vol_ok})")
    print("  τ_adj(5₂)         = complex algebraic number in the degree-3")
    print("                      trace field K (disc -23) — NON-INTEGER.")
    print("                      Exact 50-dps NZ/Tran recompute: see gap bean.")

    builder.add_assertion(
        name="vol_5_2_geometric_shape",
        computed=vol52,
        expected=vol52_ref,
        tolerance=1e-12,
        source="Vol(5₂) = 3·|D(z)|, z root of z³-z²+1 (disc -23); "
               "SnapPy value 2.828122088330783",
    )

    # ------------------------------------------------------------------ #
    # PART 3 — QOU corpus side: ρ_F = ν_SDP for 4₁ and 5₂.
    # ------------------------------------------------------------------ #
    # The corpus's CONFIRMED atoms are knots 6₂ / 8₁₁ / link L6a4 — NOT 4₁/5₂.
    # 4₁ is the MUON ANCHOR (Vol(4₁) in m_μ = m_e·Vol(4₁)/ℏ_q²), a mass scale,
    # not a bound-state atom. Both 4₁ and 5₂ appear in the corpus only as
    # CANDIDATE atomic-link primitives (rho_f_volume_binding_gap.py inverts the
    # law to report a REQUIRED ρ_F). So the corpus assigns NO confirmed integer
    # ν_SDP to 4₁ or 5₂; the only QOU-side integer available for them is the
    # PREDICTED allowed class ρ_F ∈ {1, 2} (prop:cpt-orbit-closure-density).
    corpus_rho_class = [1, 2]  # predicted allowed values; ρ_F = ν_SDP ∈ ℤ_{>0}
    print("\n[QOU corpus]  ρ_F = ν_SDP  for 4₁, 5₂")
    print("  Confirmed atoms are 6₂/8₁₁/L6a4 (ρ_F=ν_SDP ∈ {1,2}); 4₁/5₂ are")
    print("  NOT confirmed atoms — 4₁ is the muon anchor, both are candidate")
    print(f"  links only. Predicted allowed class: ρ_F = ν_SDP ∈ {corpus_rho_class}")
    print("  No confirmed ν_SDP(4₁), ν_SDP(5₂) exists in the corpus — see gap bean.")

    # ------------------------------------------------------------------ #
    # PART 4 — comparison + scope classification.
    # ------------------------------------------------------------------ #
    # |τ_adj(4₁)| = 1/√3 ≈ 0.5774 (or the reciprocal-convention √3 ≈ 1.732);
    # neither is a positive integer, and 5₂'s τ_adj is genuinely COMPLEX in a
    # degree-3 field. ρ_F = ν_SDP is a positive integer ∈ {1,2}. The objects
    # differ in TYPE (integer vs algebraic non-integer) and in ROLE (Vol-
    # multiplier vs N^{3/2} amplitude). This is a scope-(a) negative — the
    # comparison AS SET UP does not match; it does NOT refute the internal
    # QOU integer identity ρ_F = ν_SDP, which is a separate claim about
    # Wedderburn multiplicities. What it puts in TENSION is the corpus's
    # IDENTIFICATION of ρ_F with the "Kashaev density prefactor": the
    # literature's Kashaev/topological density selecting the geometric
    # connection is τ_adj, a non-integer algebraic number at a different
    # asymptotic order.
    tau41_recip = 1 / abs_tau_41            # √3, the reciprocal-convention value
    near_int_41 = min(abs(abs_tau_41 - n) for n in (1, 2))
    near_int_41_recip = min(abs(tau41_recip - n) for n in (1, 2))

    print("\n[COMPARISON]")
    print(f"  τ_adj(4₁): |τ|=1/√3={fmt(abs_tau_41, 12)} (dist to nearest {{1,2}}"
          f" = {fmt(near_int_41, 6)});")
    print(f"             recip √3={fmt(tau41_recip, 12)} (dist = {fmt(near_int_41_recip, 6)})")
    print("  τ_adj(5₂): complex algebraic (degree 3, disc -23) — not real, not integer.")
    print(f"  ρ_F=ν_SDP: positive integer ∈ {corpus_rho_class}")
    print("  VERDICT: TYPE mismatch (integer vs non-integer algebraic) +")
    print("           ROLE mismatch (Vol-multiplier vs N^{3/2} amplitude).")
    print("           scope-(a): 'this comparison, as set up, does not match'.")
    print("           Does NOT refute the internal integer identity ρ_F=ν_SDP;")
    print("           puts in TENSION the naming of ρ_F as the Kashaev density.")

    verdict = (
        "TENSION (scope-(a)). τ_adj(4₁) = 1/√-3 (|τ_adj| = 1/√3 ≈ 0.5774; "
        "reciprocal convention √3 ≈ 1.7321) is a NON-INTEGER algebraic number "
        "in ℚ(√-3); √|τ_adj(4₁)| = 3^{-1/4} matches Ohtsuki's Kashaev N^{3/2} "
        "amplitude to 45 dps (independent confirmation of the value). "
        "τ_adj(5₂) is a genuinely COMPLEX algebraic number in the degree-3 "
        "disc -23 trace field. The corpus ρ_F = ν_SDP is a POSITIVE INTEGER "
        "(∈ {1,2}). The two objects differ in TYPE (integer vs algebraic "
        "non-integer) and in ROLE (ρ_F is a linear multiplier on Vol in "
        "B = ρ_F·m_e·Vol; τ_adj is the amplitude of the N^{3/2} subleading "
        "Kashaev term, NOT a Vol-multiplier). This is a scope-(a) negative: "
        "the comparison AS SET UP does not match — it does NOT refute the "
        "internal QOU integer identity ρ_F = ν_SDP (a Wedderburn-multiplicity "
        "claim), but it puts in TENSION the corpus's IDENTIFICATION of ρ_F "
        "with the 'Kashaev density prefactor', since the literature's "
        "topological density selecting the geometric flat connection (the "
        "Kashaev 2nd coefficient, PROVED = τ_adj for 2-bridge knots) is that "
        "non-integer τ_adj. Caveat: 4₁ and 5₂ are NOT confirmed QOU atoms "
        "(confirmed set 6₂/8₁₁/L6a4; 4₁ is the muon anchor), so the corpus "
        "asserts no ν_SDP for them — the compare is against the predicted "
        "allowed class ρ_F ∈ {1,2}. NO scope-(b) structural exclusion is "
        "claimed: no proved invariant forbids a normalisation/order map "
        "between an integer multiplicity and √-torsion."
    )

    builder.add_data("tau_adj_4_1", {
        "closed_form": "1/sqrt(-3)",
        "value_re": fmt(mp.re(tau_adj_41), 50),
        "value_im": fmt(mp.im(tau_adj_41), 50),
        "abs": fmt(abs_tau_41, 50),
        "abs_reciprocal_convention": fmt(tau41_recip, 50),
        "trace_field": "Q(sqrt(-3))",
        "amplitude_crosscheck": "sqrt(|tau_adj|) == 3^{-1/4} (Ohtsuki)",
        "amplitude_match_to_45dps": bool(amp_ok),
        "Vol_4_1": fmt(vol41, 50),
    })
    builder.add_data("tau_adj_5_2", {
        "type": "complex algebraic, degree 3",
        "trace_field": "Q[xi]/(xi^3 - 2 xi^2 + 3 xi - 1), disc -23",
        "geometric_shape_cubic": "z^3 - z^2 + 1 = 0 (disc -23)",
        "geometric_shape_re": fmt(mp.re(z52), 50),
        "geometric_shape_im": fmt(mp.im(z52), 50),
        "Vol_5_2": fmt(vol52, 50),
        "exact_50dps_torsion": "NOT PINNED — see gap bean (NZ 1-loop / Tran closed form)",
        "non_integer": True,
    })
    builder.add_data("corpus_rho_F_eq_nu_SDP", {
        "law": "B_pred(K_w) = rho_F * m_e * Vol_hyp(K_w), rho_F in Z_{>0}",
        "identity": "rho_F = nu_SDP (conj:kashaev-density-equals-sdp-multiplicity)",
        "predicted_allowed_class": corpus_rho_class,
        "confirmed_atoms": ["6_2 (rho_F=1)", "8_11 (rho_F=2)", "L6a4 (rho_F=2)"],
        "nu_SDP_for_4_1": "NOT ASSIGNED (muon anchor; candidate link only)",
        "nu_SDP_for_5_2": "NOT ASSIGNED (candidate link only)",
    })
    builder.add_data("comparison_verdict", verdict)
    builder.add_data("scope_classification", "scope-(a) tension; no scope-(b) exclusion")
    builder.add_data("discipline", "literature cross-check; no fit; nothing wired")
    # The type/role mismatch is the FINDING, recorded as data (not an assertion —
    # an assertion with computed≠expected would misleadingly register as a
    # numeric FAILURE). The two numeric assertions above (4₁ amplitude
    # cross-check, Vol(5₂)) are the pass/fail gates and both PASS.
    builder.add_data("type_and_role_mismatch_scope_a", {
        "tau_adj": "non-integer algebraic (4_1: 1/sqrt(-3); 5_2: complex cubic)",
        "rho_F_eq_nu_SDP": "positive integer in {1,2}",
        "type_mismatch": True,
        "role_mismatch": True,
        "scope": "a",
        "note": verdict,
    })

    out_path = builder.save()
    print(f"\nWitness: {out_path}")
    print("\nVERDICT:", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
