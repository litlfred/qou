# H9b result: exact q-form and the general photon pair, folded wall, mirror summed (2026-11-21)

Pre-registration: `h9b_preregistration.md`. Scripts: `h9b_folded_exact_probe.py` and
`h9b_folded_not_hecke_check.out.txt` (the check is inline in the result below). Exact.

## 1. Exact D(q) for the braid word V³

- `D(q)` is a degree-26/27 rational function, given in the output. It reproduces H9 at q = 3/2, 2 and
  q₀ (0.95835983113265780026), so the consistency gate passes.
- The closed ratio is `T_p/T_n = q²`.
- The denominator has real roots at q ≈ 1.55627 and 1.64762. That explains H9's swing between 3/2
  and 2; q₀ is far from both.

## 2. The general photon pair

- **At q = 1, `D = 1` for every φ.** The folded wall is a pure q-deformation effect for every
  photon pair.
- **At q₀, `D` depends on φ.** For example 0.958055 at the V³ point and 0.941050 at φ ≡ 1. So with
  the ruled photon the wall's effect is not a single number until the photon parameters are fixed.

## 3. A structural finding: folding breaks the bulk Hecke relation

**The check failed.** The photon product `γ(0,0,qh)·γ(0,0,−q⁻¹h)` does not give the same `D` as the
braid word V³ in the folded model: 0.958055 against 0.958360 at q₀.

The reason is exact (`h9b_folded_not_hecke_check.out.txt`). A folded bulk generator
`σ̂ᵢ = σ_{3+i}σ_{3−i}` is a product of two commuting crossings. Its eigenvalues are `{q², −1, q⁻²}`,
and it satisfies the cubic `(σ̂ − q²)(σ̂ + 1)(σ̂ − q⁻²) = 0`, not the Hecke quadratic. So folding
represents the braid group, but not the Hecke algebra `H₃(q)` in which the photon is defined. Hecke
identities, such as `V³ = γγ`, fail after folding.

So the braid-level folding **derives the wall's Hecke relation and breaks the bulk's**. Under the
photon ruling (γ ∈ H₃(q)), a model that keeps the bulk in `H₃(q)` is needed.

## 4. The Hecke-level version already exists: H8 N1

A type-B Hecke representation with **equal parameters** keeps every bulk `σᵢ` Hecke and gives the
wall the same eigenvalues `{q, −q⁻¹}` as a crossing. On `V^{⊗3}` that is H5's reflection solution with
`x = q`, `y = −q⁻¹`, so `s = h`. This is H8's N1: `D(q₀) = 0.93995737184425521828`, with `D = 1` at
q = 1.

"Equal parameters" is the Hecke-level reading of folding. It is not stated in the corpus (it would sit
under `conj:type-b-folding-cpt`).

## Verdict

Not a hit. Two folding readings now exist, and they differ:

| level | bulk Hecke? | wall Hecke? | D(q₀), V³ |
|---|---|---|---|
| braid-level folding (H9, summed) | **no** (cubic) | yes | 0.958360 (braid word) / 0.958055 (photon product) |
| Hecke-level equal parameters (H8 N1) | yes | yes | 0.939957 |

Both give `D = 1` at q = 1. Only the Hecke-level one is consistent with the photon ruling.
