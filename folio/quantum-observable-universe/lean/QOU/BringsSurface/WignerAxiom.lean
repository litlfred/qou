import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.Algebra.Module.Submodule.Range

/-!
# The Wigner axiom — `conj:wigner-axiom`

The content block `def:skein-resolution-obstruction` and the theorem
`thm:qou-obstruction-reduction` need the classical-limit obstruction space of
the substrate (the Hochschild cohomology `HH²(𝒰_q, Ad)` of
`def:classical-limit-obstruction`) to be **one-dimensional**, and its generator
to have an archimedean image that integrates to the Euler characteristic of the
base curve.  Until 2026-09-15 the corpus presented the first clause as a
*theorem* of the QOU axioms ("observability kills `HH⁰`, Frobenius–Poincaré
duality gives `HH² ≅ (HH¹)^∨`, Drinfeld rigidity gives `dim HH¹ = 1`").  That
derivation does not hold: the duality of Brown–Zhang is cohomology-to-HOMOLOGY
with a Nakayama twist, the "unique deformation direction `q`" is a class in
`HH¹`, not `HH²`, and at `q = 1` Whitehead's lemma gives `HH²(U(𝔤), M) = 0` for
`𝔤` semisimple — so one-dimensionality is not a consequence of the axioms.
See `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.4.

On the owner's instruction (2026-09-15) the hypothesis is therefore stated as an
**axiom**, named for Wigner's Courant lecture of 11 May 1959 (*The unreasonable
effectiveness of mathematics in the natural sciences*, Comm. Pure Appl. Math.
13 (1960) 1–14): the substrate is *assumed* to be governed by a single scalar
obstruction, and the Millennium-problem blocks downstream are conditional on
it.  Per AGENTS.md §3b it is a **primary conjecture class** — its signature
binds no other conjecture class — with content-bearing fields, and **no
instance is supplied** (the honest open state).

## What the two clauses say

* **(W1)** `Module.finrank k Obs = 1`: the obstruction space is a line.
* **(W2)** the Euler class `euler` of the tangent bundle of the base lies in
  the image of the archimedean realisation `realise : Obs →ₗ[k] H`, and is
  non-zero.  So a generator of the line maps ONTO the Euler class, whose
  integral over the base is `χ_eu(M₀) = 2 − 2g` (Poincaré–Hopf, cited, not
  formalised here: the pairing enters the theorem below as a hypothesis).

## Why (W2) has this shape and not another

The measured `S₅`-equivariance of Bring's surface leaves no other target
(`QOU.Brings.S5Char.hochschild_invariants_of_base`, sorry-free): the
`S₅`-invariant part of the base curve's Hochschild theory is `k²` in `HH₀`
(spanned by `H⁰(𝒪)` and `H¹(K) = H²(M₀; k)`) and `k` in `HH⁰`, and is ZERO
in `HH²(M₀) = H¹(T_{M₀}) = [4,1] ⊕ [3,2]`.  An equivariant image of a
one-dimensional obstruction space in the base's deformations is therefore
zero, and the only invariant line that can carry the `−6` is `H²(M₀; k)`,
where the Euler class lives.  The axiom is stated with that target and no
other.

## What would refute it

A computation of `HH²(𝒰_q(𝔰𝔩₂), Ad)` at generic `q` with dimension `≠ 1`
refutes (W1); an equivariant realisation whose image of the obstruction line
is `0 ∈ H²(M₀; k)` refutes (W2).  Neither computation exists in the corpus.

Companion blocks: `conj:wigner-axiom` (this class), `thm:qou-obstruction-reduction`
(conditional on it, proved below as `pairing_of_generator`),
`rem:three-euler-characteristics`.
-/

namespace QOU.AlgebraicSubstrate

open Module

/-- **The Wigner axiom** (`conj:wigner-axiom`).  `Obs` is the classical-limit
obstruction space (`HH²(𝒰_q, Ad)` of `def:classical-limit-obstruction`) as a
`k`-vector space, `H` is the archimedean receiving space (`H²(M₀; k)` for the
base curve), `realise` is the tower comparison map and `euler` is the Euler
class of the tangent bundle of the base.

(W1) the obstruction space is one-dimensional; (W2) the Euler class is a
non-zero element of the image of `realise`.  No instance is provided. -/
-- Ref: [wigner1960] https://doi.org/10.1002/cpa.3160130102
-- Ref: [leitner2026] stochastic-mechanics/wigner-axiom
class WignerAxiom (k : Type*) [Field k]
    (Obs : Type*) [AddCommGroup Obs] [Module k Obs]
    (H : Type*) [AddCommGroup H] [Module k H]
    (realise : Obs →ₗ[k] H) (euler : H) : Prop where
  /-- (W1) the classical-limit obstruction space is a line. -/
  finrank_obs_eq_one : Module.finrank k Obs = 1
  /-- (W2a) the Euler class of the base is realised by an obstruction class. -/
  euler_mem_range : euler ∈ LinearMap.range realise
  /-- (W2b) and it is not zero — the base curve is not a torus. -/
  euler_ne_zero : euler ≠ 0

variable {k : Type*} [Field k]
  {Obs : Type*} [AddCommGroup Obs] [Module k Obs]
  {H : Type*} [AddCommGroup H] [Module k H]
  (realise : Obs →ₗ[k] H) (euler : H)

/-- Under the axiom there is a non-zero obstruction class `w` whose archimedean
image is the Euler class. -/
theorem WignerAxiom.exists_generator [WignerAxiom k Obs H realise euler] :
    ∃ w : Obs, w ≠ 0 ∧ realise w = euler := by
  obtain ⟨w, hw⟩ :=
    LinearMap.mem_range.mp (WignerAxiom.euler_mem_range (realise := realise) (euler := euler))
  refine ⟨w, ?_, hw⟩
  rintro rfl
  rw [map_zero] at hw
  exact WignerAxiom.euler_ne_zero (realise := realise) (euler := euler) hw.symm

/-- Under (W1) every obstruction class is a scalar multiple of any non-zero one:
the obstruction is "a single scalar". -/
theorem WignerAxiom.eq_smul_of_ne_zero [WignerAxiom k Obs H realise euler]
    {w : Obs} (hw : w ≠ 0) (v : Obs) : ∃ c : k, c • w = v :=
  (finrank_eq_one_iff_of_nonzero' w hw).mp
    (WignerAxiom.finrank_obs_eq_one (realise := realise) (euler := euler)) v

/-- **Part (a) of `thm:qou-obstruction-reduction`, conditional on the axiom.**
Let `pair : H →ₗ[k] k` be integration over the base and suppose
`pair euler = χ` (Poincaré–Hopf: `χ = 2 − 2g`, supplied as a hypothesis).
Then a generator of the obstruction line pairs to `χ`, and every obstruction
class pairs to a multiple of `χ`. -/
theorem WignerAxiom.pairing_of_generator [WignerAxiom k Obs H realise euler]
    (pair : H →ₗ[k] k) (χ : k) (hχ : pair euler = χ) :
    ∃ w : Obs, w ≠ 0 ∧ pair (realise w) = χ ∧
      ∀ v : Obs, ∃ c : k, pair (realise v) = c * χ := by
  obtain ⟨w, hw0, hw⟩ := WignerAxiom.exists_generator realise euler
  refine ⟨w, hw0, by rw [hw, hχ], fun v => ?_⟩
  obtain ⟨c, hc⟩ := WignerAxiom.eq_smul_of_ne_zero realise euler hw0 v
  exact ⟨c, by rw [← hc, map_smul, map_smul, smul_eq_mul, hw, hχ]⟩

end QOU.AlgebraicSubstrate
