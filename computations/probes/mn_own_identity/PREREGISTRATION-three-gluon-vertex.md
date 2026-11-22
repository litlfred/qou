# Braid-level analogue of the three-gluon (and four-gluon) colour vertex: pre-registration (2026-11-22)

Written and committed **before** `mn_three_gluon_vertex_probe.py` is written or run. Item 2 of the
parent's list. Algebra only: no dynamics, no coupling, no selection of a gluon (owner ruling
2026-11-22: the gluon of step 4 of `def:derived-atom` stays open).

## Hypothesis under test (not assumed)

In 't Hooft double-line language a strand is a colour line and a crossing is one-gluon exchange
`Ω = Σ_a T^a ⊗ T^a`. The non-abelian `ggg` vertex `f^{abc}` would then be the defect of two
crossings sharing a strand, i.e. the commutator `[Ω₁₂, Ω₂₃]`, and the braid relation would
"carry" it.

## Corpus already held (corpus-grep, this session)

- `QOU/Mass/InfinitesimalPureBraid.lean` — sorry-free: for any Lie algebra and invariant `Ω`,
  `[Ω_ij, Ω_ik + Ω_jk] = 0`, `[Ω_ij, Ω_kl] = 0` (disjoint), and flatness of the KZ connection.
  It does **not** state the value of `[Ω₁₂, Ω₂₃]` itself.
- Library: `kohno1987-aif`, `drinfeld1991-quasitriangular` (Drinfeld–Kohno), `cherednik1991-kz-dunkl`.
- `QOU/QBeta/GluonVertexPsdParity.lean`: a different object (PSD parity of `σ₀^k` in `H₂`).
- 't Hooft double-line notation: **not found** in `folio/`, `docs/audits/` (only 't Hooft's
  cellular-automaton papers are cited). So the colour-line reading is introduced here, not held.

## Exact construction

`V = ℚ(q)³` (basis e₁,e₂,e₃), `T^a = λ^a/2` (Gell-Mann), `f^{abc}`, `d^{abc}` from
`[T^a,T^b] = i f^{abc}T^c`, `{T^a,T^b} = δ^{ab}/3 + d^{abc}T^c`. Define on `V^{⊗3}`
`F := i f^{abc} T^a⊗T^b⊗T^c`, `D := d^{abc} T^a⊗T^b⊗T^c`; on `V^{⊗4}`
`G := f^{abe} f^{cde} T^a⊗T^b⊗T^c⊗T^d`.

Jimbo braided R-matrix (convention of `NucleonWeightSpaceTraces.lean`, extended to sl₃):
`Ř(e_i e_i) = q e_i e_i`; for `i<j`: `Ř(e_i e_j) = e_j e_i`, `Ř(e_j e_i) = e_i e_j + h e_j e_i`,
`h = q − q⁻¹`. `R := P Ř`. σ₀ ↦ Ř₁₂, σ₁ ↦ Ř₂₃ (σ₂ ↦ Ř₃₄).

Expansion: `q = e^ħ`, normalised `R̃ = q^{-1/3} R = 1 + ħ r + ħ² r⁽²⁾ + …`; `r = 2Ω + r_a`,
`r_a` antisymmetric (`r_a + r_a²¹ = 0`). All exact (sympy rationals / series); no float.

"f-part / d-part" of an operator X: first its HS-orthogonal projection onto the classical SU(3)
commutant (= Haar average, exact via the Gram matrix of permutation operators), then its
coordinates in a basis containing F and D. In H₃(q) (abstract Hecke algebra) the analogue is the
coefficient of `σ₀σ₁ − σ₁σ₀` in the basis {1, σ₀±σ₁, σ₀σ₁±σ₁σ₀, σ₀σ₁σ₀}, antisymmetric part under
the Dynkin flip σ₀↔σ₁.

## Measurements and predictions

- **M1** `[Ω₁₂, Ω₂₃]` vs F, D. Prediction (standard Lie algebra): `= ±F` exactly, D-coefficient 0,
  and F is a multiple of `C − C²` (antisymmetrised 3-cycle) on `V^{⊗3}`.
- **M2** YBE `R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂` exactly; at order ħ² this is CYBE(r) = 0. Decompose:
  CYBE(2Ω) alone is a nonzero multiple of F; prediction: the `r_a` terms cancel it exactly, so the
  braid relation encodes F only as a **cancellation** (modified CYBE), not as a surviving term.
  Coefficient of F in CYBE(2Ω) measured.
- **M3** order-ħ² term of `R̃₁₂R̃₂₃` and of `Ř₁₂Ř₂₃Ř₁₂`, projected: F- and D-coefficients.
  Prediction: R̃₁₂R̃₂₃ has nonzero F-coefficient at ħ² (from ½[r₁₂,r₂₃]); Ř₁₂Ř₂₃Ř₁₂ (= P₁₃·…,
  flip-symmetric) has zero F-coefficient at every order.
- **M4 (QOU-specific)** the photon chiral letter σ₀σ₁⁻¹ and the Borromean core V³ = (σ₀σ₁⁻¹)³:
  exact F- and D-coefficients (classical-commutant projection, all q) and the H₃ commutator
  coefficient. Prediction: σ₀σ₁⁻¹ already carries F at order ħ⁰ (it is a 3-cycle at q = 1);
  H₃ commutator coefficient of σ₀σ₁⁻¹ is exactly ½. V³: no prediction for sign/size.
- **M5 (four strands)** G vs nested commutator `[[Ω₁₂,Ω₂₃],Ω₃₄]`; whether G lies in the span of
  degree-≤2 Ω-monomials (projected); lowest ħ order of `R̃₁₂R̃₂₃R̃₃₄` with a component outside that
  span. Prediction: `[[Ω₁₂,Ω₂₃],Ω₃₄] = c·G`, c ≠ 0; G not in the degree-≤2 span; first appears at ħ³.

## Decision rule

The hypothesis "ggg = two crossings sharing a strand" is **supported at the algebra level** if M1
gives ±F with zero D and M3 gives a nonzero F-coefficient at ħ². It is **not** a statement about
the braid relation unless M2 shows a surviving F term; a pure cancellation is reported as
"the YBE contains F only through the modified CYBE". M1/M2 are standard mathematics
(Drinfeld–Kohno, Belavin–Drinfeld); only M4 is QOU-specific.

## Honesty clause

Every number is reported, including predictions that fail. No object is chosen because its
coefficient looks like QCD. Nothing here identifies a gluon, a coupling, or a vertex strength;
"F-coefficient" is a projection, not a Feynman rule. Negatives are scope (a).
