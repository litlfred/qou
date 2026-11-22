# Pre-registration: quark channels as eigenvalues of the γγ vertex (2026-11-22)

Owner, 2026-11-22: *"Try eigenvalues approach"* (option: u and d are the two channels of the γγ
vertex, not letters). Written and committed before any computation.

**Object.** V = σ₀σ₁⁻¹ (the ruled γγ pair-production vertex; Borromean 𝓑₃ = V³) in H₃(q),
convention D irrelevant (no trace taken). Blocks: (3): σ ↦ q; (1³): σ ↦ −q⁻¹; (2,1): Hoefsmit
σ₀ = diag(q, −q⁻¹), σ₁ = [[a, b],[b, a']], a = h/(1−q⁴), a' = h/(1−q⁻⁴), b² = 1 + a a'.
Computed exactly in sympy; q₀ = proton pin, 30 dps.

**Predictions, made in advance (structural, no experimental input):**
- P1. On (3) and (1³), V ↦ 1. On (2,1), det V = 1, so the eigenvalues are a pair λ, λ⁻¹.
- P2. At q = 1, V is the 3-cycle, so λ = e^{±2πi/3}: phases ±1/3.
- P3. For q near 1 (including q₀), tr V ∈ (−2, 2), so |λ| = 1 and λ = e^{±iθ(q)}, θ(1) = 2π/3.
- P4. V³ on (2,1) has eigenvalues e^{±3iθ}; at q = 1 this is 1 (consistent with §29).

**Readings fixed now (two, both reported, neither chosen by outcome):**
- R1. Charge = phase: Q_± = ±θ(q)/2π. At q = 1: ±1/3.
- R2. Charge = phase mod 1, representative in [0,1): {1/3, 2/3} at q = 1.
Both are compared to nothing experimental; the SM charges (+2/3, −1/3) are named only as context.
What would count as a negative: P1–P3 failing, or θ(q₀) not near 2π/3.

**No fitting.** Nothing is tuned; q₀ is the standing pin.
