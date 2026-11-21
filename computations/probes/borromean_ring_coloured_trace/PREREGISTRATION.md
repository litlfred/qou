# Pre-registration — ring-coloured trace on the Borromean nucleon `V³`

Bean `qou-99qc`. Owner question 2026-11-21: *"Why are you not doing a trace on the Borromean ring
with the strands?"* Written before any number at `q₀` is computed. Disclosure: the symbolic
closed forms (diagonal entries of `V³` on the weight spaces, and the change of those entries under
conjugation by `σ₁²`) were computed in sympy while writing this file. No value at `q₀`, no `E₀`
and no CODATA figure had been computed.

## Object

`V = K²`, basis `u = e₁` (`K u = q u`), `d = e₂`. Level-2 Jimbo braiding on `V^{⊗3}` (the matrices
of `NucleonWeightSpaceTraces.lean`). `β_Bor = V³ = (σ₁σ₂⁻¹)³`, a pure braid; its closure is the
Borromean rings, one component per strand. For a colouring `c : Fin 3 → {u, d}`, `P_c = P_{c₀}⊗P_{c₁}⊗P_{c₂}`
is rank one, so

  `τ_c(b) = Tr(K^{⊗3} P_c ρ(b)) / [2]_q³ = q^{2T³(c)} · ⟨c|ρ(b)|c⟩ / [2]_q³`.

The normalisation `[2]_q³` is the one the corpus fixes (whole-space trace = convention-D Markov
trace, `qtrace_crossing_eq_zD`). It is also the Reshetikhin–Turaev normalisation that gives each
component the quantum dimension `[2]_q` of `V`. No other normalisation is introduced.

## Hypotheses, each with its test

* **H1 (well-definedness).** `τ_c` is a link invariant of the coloured closure: unchanged under
  conjugation by a pure braid. Test: `σ₁²` and `σ₂²` on both weight spaces. Expected from the
  symbolic run: **fails** (the `h·E⊗F` W-exchange term of `ChargedCurrentW` changes a strand's
  flavour, so flavour is not constant along a component). If it fails, `τ_c` is reported as a
  boundary-condition amplitude of the open braid, not as a ring colouring, and is not scored.
* **H2 (class constancy).** `τ_c` is constant on the one-`u` class and on the two-`u` class.
* **H3 (flip).** `u ↔ d` sends `ρ(σ)` to `ρ(σ⁻¹)` at `q⁻¹` and `K` to `K⁻¹`, so
  `τ_{flip c}(V³; q) = τ_c(mirror V³; q⁻¹)`.
* **H4 (class sums).** `Σ_{c ∈ class} τ_c` equals the already-scored `ε_p`, `ε_n` of
  `FlavourWeightSplit`, and `ε_p = q² ε_n`.
* **H5 (W-free strict colouring).** Keeping only the flavour-preserving part `R₀` of each
  strand-tracked crossing (each component keeps its flavour), the amplitude is
  `Π q^{±[c_i = c_j]} = q^{2 Σ_{same-flavour pairs} lk(i,j)}`. Borromean pairwise linking
  numbers are 0, so the prediction is `τ^{strict}_c = q^{2T³(c)}/[2]³` with the braid dropping out.
* **Two-term.** Per colouring, the covariant all-pairs insertion `Q₁₂+Q₂₃+Q₁₃` and the
  non-covariant adjacent insertion `Q₁₂+Q₂₃` (labelled comparison), raw and connected.

## Numbers (only after all checks)

70 dps, proton `q₀` (`q_parameter.Q_50_DIGIT_STR`), mpmath only. For every invariant class
difference `Δ`, `Q = |Δ|·E₀` with BOTH `qbeta_e0.canonical` (tower-summed, the scored cell's
form) and `qbeta_e0.order_zero`, labelled. Then the CODATA column. No colouring, insertion, sign or
`E₀` form is chosen by the CODATA column; per-colouring values that fail H1 are not turned into
`Q_β` candidates.
