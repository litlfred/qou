import Mathlib.Tactic

/-!
# QOU.BraidKnot.knot_factor_spectral_derivation — `a_𝒦` as Plancherel-weighted character pairing

**Proposition** ([`prop:knot-factor-spectral-derivation`](../../../mass-theory/knot-factor-spectral-derivation.md)).

*Let `𝒦` be a knot with braid representative `β_𝒦 ∈ B_n` and mirror
`β_𝒦*`, working over `A = H_n(R, q)`.  The knot factor `a_𝒦` in the
unified mass formula is the normalised chirality Gram pairing*

```
  a_𝒦 = G_{β_𝒦, β_𝒦*} / G_{𝟙, 𝟙}
      = Σ_{λ ⊢ n} w_λ · χ_λ(β_𝒦) · χ_λ(β_𝒦*) / χ_λ(𝟙)²
```

*with Plancherel weights `w_λ = dim_q²(V_λ) / [n]_q!` summing to 1.
The identity is exact in `R`.*

## 2026-09-03 — the 2026-08-30 pass removed the sibling and left this one

That pass deleted `plancherelWeight_sum_eq_one` (body
`ctx.claim_plancherel_sum_one`) and recorded the disposition as *"drop the
pseudo-theorem and project the field at use sites"*, on the ground that

> *"The content stays in the class field each declaration projected, which
> asserts the same proposition **under the same hypotheses**."*

**That ground does not hold here, and it is worth being explicit about why**,
because the same sentence would justify leaving every carrier in the drain
alone.  `KnotFactorSpectralContext` carried `q`, `Partition`, `partitions`,
`plancherelWeight`, `chi_beta`, `chi_beta_mirror`, `chi_one` and
`knotFactor` as **data fields** — ten fields, of which only two were claims.
So the instance chose every quantity the claim is about, and a
`[KnotFactorSpectralContext n]` binder assumed nothing about anything a
caller supplied.  A field is a hypothesis only when it constrains the
class's *parameters*; here the sole parameter was `n`, which the identity
never mentions.  (This carrier is why *"is the class parameterised?"* fails
as a triage discriminator — see `scripts/sap-carrier-shape.py`.)

The pass also left `knot_factor_spectral_derivation` itself: a `def` whose
type is the identity and whose body was `ctx.claim_knot_factor_spectral` —
the projection, in the one declaration that could not simply be dropped
because the block's `lean.ref` resolves to it.  A `def` returning a proof is
a theorem in disguise besides (AGENTS.md §1a).

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

Both propositions are now **`Prop`-valued definitions over caller-supplied
data**, and the class is gone.  A caller with actual Hecke characters and
Plancherel weights supplies them and takes these as hypotheses, and they
constrain the caller because the data are theirs.

Naming recovers real content here — it is not the
`six_term_mass_formula_complete` case — because the two named propositions
**combine into a theorem**: `knotFactor_eq_one_of_trivial_braid` derives
`a_𝒦 = 1` for a braid whose character equals that of the identity, from the
spectral formula plus the normalisation `Σ_λ w_λ = 1`.  That is the
proposition's own consistency check (the unknot carries knot factor 1) and it
is proved sorry-free, using the non-vanishing `χ_λ(𝟙) ≠ 0` that the old class
carried as `chi_one_ne_zero`.

## What is still unencoded

Everything upstream of the identity: `H_n(R, q)`, the braid `β_𝒦` and its
mirror, the irreducible characters `χ_λ`, the Gram pairing
`G_{β_𝒦, β_𝒦*}`, and the definition `w_λ = dim_q²(V_λ) / [n]_q!` that makes
the weights *Plancherel* rather than arbitrary reals summing to one.  The
`q`-dependence is gone with the class field `q`, which the identity never
used.  So what is named is the shape of the pairing, not its derivation from
Wedderburn.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/knot-factor-spectral-derivation.md
-/

namespace QOU.BraidKnot

/-- **Plancherel normalisation**: the weights sum to `1` (the Wedderburn
trace identity).

Named over caller-supplied data.  Note this says nothing about the weights
being `dim_q²(V_λ) / [n]_q!` — only that they are normalised. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/knot-factor-spectral-derivation.md
def PlancherelNormalised {P : Type} (partitions : Finset P)
    (plancherelWeight : P → ℝ) : Prop :=
  (partitions.sum fun lam => plancherelWeight lam) = 1

/-- **Knot-factor spectral formula** ([`prop:knot-factor-spectral-derivation`]):

`a_𝒦 = Σ_λ w_λ · χ_λ(β_𝒦) · χ_λ(β_𝒦*) / χ_λ(𝟙)²`.

**Named, not asserted** — see the module docstring for why neither a
projection nor a `sorry` is the honest form here. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/knot-factor-spectral-derivation.md
def knot_factor_spectral_derivation {P : Type} (partitions : Finset P)
    (plancherelWeight chi_beta chi_beta_mirror chi_one : P → ℝ)
    (knotFactor : ℝ) : Prop :=
  knotFactor = partitions.sum
    fun lam => plancherelWeight lam * chi_beta lam * chi_beta_mirror lam
             / (chi_one lam) ^ 2

/-- **The unknot consistency check, derived.**

If the braid and its mirror have the character of the identity on every
irrep — `χ_λ(β_𝒦) = χ_λ(β_𝒦*) = χ_λ(𝟙)` — then the spectral formula and the
Plancherel normalisation together force `a_𝒦 = 1`.

Each summand collapses to `w_λ` because `χ_λ(𝟙) ≠ 0`, which is the
non-vanishing the old class carried as `chi_one_ne_zero`; the sum is then
the normalisation.

This is why naming the two propositions recovers content rather than only a
schema: they combine into a theorem about the caller's data. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/knot-factor-spectral-derivation.md
theorem knotFactor_eq_one_of_trivial_braid {P : Type} (partitions : Finset P)
    (plancherelWeight chi_one : P → ℝ)
    (hne : ∀ lam ∈ partitions, chi_one lam ≠ 0)
    (hsum : PlancherelNormalised partitions plancherelWeight)
    (knotFactor : ℝ)
    (h : knot_factor_spectral_derivation partitions plancherelWeight
          chi_one chi_one chi_one knotFactor) :
    knotFactor = 1 := by
  have hterm : ∀ lam ∈ partitions,
      plancherelWeight lam * chi_one lam * chi_one lam / (chi_one lam) ^ 2
        = plancherelWeight lam := by
    intro lam hlam
    have h0 := hne lam hlam
    field_simp
  calc knotFactor
      = partitions.sum (fun lam => plancherelWeight lam * chi_one lam
          * chi_one lam / (chi_one lam) ^ 2) := h
    _ = partitions.sum (fun lam => plancherelWeight lam) :=
        Finset.sum_congr rfl hterm
    _ = 1 := hsum

/-- **The formula is refutable at freely-chosen data**, which is why it is
named rather than carried as a `sorry`.

With no partitions the sum is empty, so `a_𝒦 = 1` reads `1 = 0`.  Recorded
as a theorem so a later attempt to "finish" this file with a `sorry` fails
against a standing counterexample. -/
theorem not_knot_factor_spectral_derivation_of_free_data :
    ¬ knot_factor_spectral_derivation (∅ : Finset ℕ)
        (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => 1) 1 := by
  simp [knot_factor_spectral_derivation]

end QOU.BraidKnot
