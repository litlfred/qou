# Pre-registration: γγ-vertex eigenvalues on H₆ (2026-11-22)

Owner, 2026-11-22: *"Also check H_6"*. Follows PREREGISTRATION-vertex-eigenvalues.md (H₃: all P1–P4
held; V = σ₀σ₁⁻¹ has eigenvalues e^{±iθ(q)} on (2,1), θ(1) = 2π/3, θ(q₀)/2π = 0.337380).
Written and committed before any H₆ computation.

**Method.** All eleven irreps of H₆(q) in seminormal (Hoefsmit) form, built from standard Young
tableaux, validated by the Hecke and braid relations. Eigenvalues by mpmath at 30 dps at
q₀ = 1.1099785827513808076 and at q = 1 + 10⁻²⁵. Phases reported as θ/2π.

**Words (fixed now, chosen by structure, not by outcome; V_i = σ_iσ_{i+1}⁻¹, all γγ words):**
- W1 = V₀ — one vertex.
- W2 = V₀V₃ — one vertex in each nucleon (disjoint strands 0–2, 3–5).
- W3 = V₀³V₃³ — two Borromean nucleons, unlinked.
- W4 = V₂³ — the γγ-selected interface bond G (qou-ales).
- W5 = V₀V₂V₄ — three vertices covering all six strands (connected).
- W6 = V₀³V₃³V₂³ — two nucleons then the bond.

**Predictions (derived in advance):**
- P1 (branching). W1, W4 lie in a parabolic H₃, so their spectra are ⊆ {1, λ^{±m}} with
  m = 1, 3: no new phases beyond H₃.
- P2 (commuting product). W2, W3 are products of commuting parabolic H₃ elements, so their
  phases are sums: ⊆ {0, ±θ, ±2θ} for W2 and {0, ±3θ, ±6θ} for W3. At q = 1: W2 ⊆ {0, ±1/3},
  W3 all 0.
- W5, W6: no prediction. They are the genuinely H₆ content.

**Readings.** Phase multisets per irrep; at q = 1 note which are thirds. No experimental number is
used; SM charges appear only as context. A negative: W5/W6 giving nothing beyond sums of H₃ phases.
