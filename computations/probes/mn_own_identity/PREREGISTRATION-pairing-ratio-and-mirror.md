# Pre-registration: nucleon/electron pairing ratio, and the mirror Frobenius relation

Written 2026-11-21, before any computation below. Owner: "3" (both).

## A. Nucleon/electron ratio of matter pairings

**Premise under test (hypothesis, not established).** `m_e` is the electron's matter pairing in
the same two-term Lagrangian. The production constant is `12 m_e`, so the nucleon's constant over
the electron's should be `12`.

**Scale removal.** A pure state `ψ` normalised against the shared form (`ψ* ψ = 1`) gives a
scale-free expectation `⟨X⟩ = φ X ψ / φ ψ`. The sector-averaged (mixed) state gives
`⟨X⟩ = tr(K X) / tr(K)` on the sector: a ratio of closed traces, also scale-free. Pure states need a
choice of vector, which would be selection, so **only the mixed-state version is computed**.

**The class, fixed now (no other variants will be run):**
- Representation: Jimbo `Ř` on `V^{⊗3}`, `V = ℚ(q)²`, `K = diag(q, q⁻¹)`, `K^{⊗3}`.
- Electron: `X_e = ρ(σ₀σ₁σ₀)`. Nucleon: `X_N = ρ((σ₀σ₁⁻¹)³)` (Borromean core).
- Sectors: E1 the whole 8-dim space for both; E2 nucleon on the proton weight space `(2 up, 1 down)`,
  electron on the whole space. (The electron has no weight sector fixed by the ruling; the whole
  space is the only choice not made by us.)
- Ratio `r(q) = ⟨X_N⟩ / ⟨X_e⟩` in exact `ℚ(q)`.

**Pass criterion:** `r(q) = 12` identically in `q`. Also reported: `r(1)`, and the neutron
version. Anything else is a scope-(a) negative for this class only.

## B. Does the mirror Frobenius relation follow from the axioms?

**Question.** The left snake identity for `λ = ε` needs `μ ≫ Δ = (A ◁ Δ) ≫ α⁻¹ ≫ (μ ▷ A)`, which
is not an axiom. Is it implied by the others?

**Test, fixed now.** Search for a counterexample in `Vect_ℚ` with symmetric braiding:
`A = ℚ[x]/(x²)` (commutative), antipode `S = id`, `Δ(a) = t·(1 ⊗ a)` for `t = Δ(1) ∈ A ⊗ A`
(this makes the stated Frobenius relation hold by construction), `ε` arbitrary. Impose all
`FrobeniusHopfData` laws that are polynomial in `(t, ε)` (counit laws, coassociativity,
`S` laws with `S = id`: these need `Δ` cocommutative), and solve exactly with sympy.

**Outcomes:** a solution violating the mirror relation shows it does not follow (in this setting).
No solution in this class proves nothing beyond this class.
