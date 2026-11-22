# Sidecar review: mass-theory (2026-11-15, main `b2b349f36`)

Scope: 159 Lean-backed statement blocks and 154 `prf:` blocks in
`folio/quantum-observable-universe/mass-theory/`, grouped into 208 review units.
Each unit was read side by side (statement `.md`, the Lean the `.ts` names plus any sibling `.lean`,
narrative proof), following `reviewer-brief.md` and the pilot's standard. Algebra checks used exact
sympy / `Fraction` only. **No verdict has been written to a sidecar yet.**

- Per-batch tables (pilot shape): `2026-11-15-sidecar-review-mass-theory/findings-batch-{1..4}.md`
- Machine-readable verdicts (ready for `qa-agent-entry.ts`): `2026-11-15-sidecar-review-mass-theory/verdicts-batch-{1..4}.jsonl`
- Findings split by owning thread: `2026-11-15-sidecar-review-mass-theory/route-{lean,binding,exposition,other}.md`

## Tally (312 verdict rows)

| column | pass | warn | fail | under open PR (note only) |
|---|---|---|---|---|
| S↔L `proof-narrative-lean-equiv` (159) | 9 | 13 | 128 | 9 |
| S↔P `da-non-sequitur` (153 incl. n/a rows excluded) | 18 | 27 | 101 | 7 |

Routing: lean 126, binding 54, other 42, exposition 23 (rows that fail or carry a PR note).

## Critical findings (false statements or inconsistent axioms), each with an exact witness

Second-reviewer re-check (coordinating thread, exact arithmetic or direct reading of the Lean):
confirmed 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 22.
- 4: G(qx)=RG gives qⁿBₙ = Σ r_k B_{n−k}; the coefficients carry qⁿ, so the recurrence is not constant-coefficient (item 1 of the statement), as the block's own "P-recursive" wording admits.
- 13: `DemazureModel` leaves `demazureCharacter` free (only `schur_nonzero`); instances with constant 1 and constant 2 (Partition := fun _ => Unit) both satisfy it, and the axiom equates both to one opaque value ⇒ False. Not yet run in Lean.
- 16: Hankel determinants of the moments Σ q^{cr(π)} at q = 11/10 computed exactly for N ≤ 6: 1, 1, 21/10, 145971/10000, … all > 0 (= ∏[k]_q!). Super-exponential growth is true but does not preclude a measure.
- 18: Σ_λ d_λ e_λ at β = 1 in H₃ is 1 + e_(2,1).
- 20: (1ⁿ) is one-dimensional, so χ_(1ⁿ) of an invertible element is non-zero.
Not independently re-checked: 15 (knot-factor-spectral-derivation), 17 (eigenvalue-product-expansion), 21 (operator-selection-lp; its own proof carries a caveat that the all-H_n statement is false since G is singular).

1. **em-spectral-completeness** item 4: w₊+w₋ = ([3]²+1)/[2] ≠ 1 (457/40 at q=2).
2. **corrected-markov-trace**: tr_M(σ₀σ₁σ₀) = hz²+z, not z³; Lean takes the false step as `h_reduce2`. The corpus contradicts itself (explicit-alpha-k-h3, markov-trace-product say hz²+z).
3. **hecke-markov-transition (iv)**, **markov-trace-product**: tr_M = ∏V̂ᵢ fails for adjacent generators (same witness).
4. **binding-genfun-qdifference**: q-difference eq. does not give a constant-coefficient recursion.
5. **full-pole-structure-mass-trace**: tr_M(σ₁)=q³/(q²+1) is not Habiro; at q=i, 0=−i.
6. **frobenius-codim-universal**, **t-beta-markov-frobenius-collapse(-general)**, **frobenius-self-duality-forces-lp-dual-extraction**: rely on τ non-degenerate / PSD; under D, τ(p_(1³)²)=0 and τ((E₁₂−E₂₁)²) = −2/[2]².
7. **nuclear-knot-classification**: (1−h²)ⁿ → 0, not 1.
8. **unit-modulus-eigenvalue**: σ₁² has eigenvalues q^{±2}; χ_(2,1)(β_Bor) = 2−3h⁴−h⁶.
9. **s4-s3-half-symmetric-projection**: Borromean complement = 2 ideal octahedra, not 8.
10. **feynman-classical-limit**: z_D(1)=1/2, not 0; Lean ref never asserted.
11. **wenzl-qmn-synergy**: tr_M(T_w)=z^ℓ(w) false at w=s₁s₂s₁ (class field).
12. **binding-scale-catalan**: closure of (σ₀σ₁σ₂)² ∈ B₄ is T(4,2) (2 components), not Borromean; Catalan = Cl₂(π/2).
13. **demazure-fiber-markov-trace**: axiom over all instances vs one opaque constant ⇒ 1 = 2 (suspected inconsistent).
14. **jucys-murphy-central-elements-qou**: J₁ = 0; at n=2 eigenvalues are 1, −q⁻².
15. **knot-factor-spectral-form**: β=1 gives 1 = Σw_λ ≠ 1.
16. **q-gaussian-obstruction-at-q0**: Hankel dets ∏[k]^{N−k} > 0, so the measure exists; statement false.
17. **eigenvalue-product-expansion**: T=|Z−N|/2 wrong sign for N>Z (³H: −0.09347 vs 0.11521).
18. **gram-determinant-plancherel-ratio**: β = Σχ_λ e_λ false (β=1 in H₃ gives 1+e_(2,1)).
19. **habiro-precision-ladder-equivalence**: tr_M(σ₁)=u⁶/(u⁴+1) is not a finite ℤ[u] Habiro sum.
20. **knot-factor-shell-closed**: ββ* invertible, cannot be a multiple of e_(n).
21. **operator-selection-lp**: displayed dual violates weak duality (x free ⇒ equality constraints); exact H₃ witness at q=11/10.
22. **tmli-constituent-composite-agreement**: tr_M(σ₁σ₂σ₁σ₂) − tr_M(σ₁²)² = −(q⁴+q²+1)/(q²+1)² ≠ 0 (re-checked by hand).

## Cross-cutting patterns

- **Convention-C remnants** in proofs under the convention-D statement (wedderburn-bratteli, wenzl-bridge, y-lambda-cyclotomic, explicit-alpha-k-h4, skein-polynomial-transfer-matrix, interface-knot-markov-z `markovParam_le_half`).
- **Non-degeneracy of τ under D** is assumed in at least four blocks; D kills ℓ(λ) ≥ 3.
- **Vertex-product factorisation** of tr_M is assumed by several blocks; false for adjacent generators.
- **Lean S↔L fails** are dominated by self-assuming class fields, claimed value as a def / `rfl`, single-instance (n=3, n=4, q=1) proofs, `:= True` carriers, vacuous uninstantiable classes, and refs to empty modules.
- **Empirical content inside propositions** (CODATA/AME/PDG comparisons, fitted or scanned choices): about 20 blocks.

## Under open PRs (finding notes, no verdict)

#7915 (confinement-categorical, habiro-expansion-atomic, hecke-markov-transition, mass-tower-deeper-fillers,
unified-curvature-rank-mass-formula; its `.ts` ref is still a def that takes the decomposition as its definition),
#7946 (archimedean-functor-uniqueness), #7551 (markov-trace-product, mass-coefficient-shadow-price),
#8003 (markov-trace-frobenius-selection .ts and three other .ts). PR #7218 edits a `content/` path that no longer exists.
