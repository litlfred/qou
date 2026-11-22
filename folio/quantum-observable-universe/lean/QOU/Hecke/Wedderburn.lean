import QOU.Hecke.Algebra
import QOU.Hecke.MarkovTrace
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.List.Sort
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Algebra.Hom
import QOU.BraidKnot.IdentityIContentDecomposition
import QOU.Mathlib.SYTHookGNW

open BigOperators

/-!
# Wedderburn–Artin decomposition of `H_n(q)`

Over a "generic" base ring `R` (containing `ℚ` and the `q-integers`),
the Hecke algebra splits as a direct sum of matrix algebras indexed
by partitions of `n`:

  `H_n(q) ≅ ⊕_{λ ⊢ n} M_{f^λ}(R)`

where `f^λ = #SYT(λ)` is the dimension of the Specht module
(equal to the hook-length formula `n! / Π hook(c)` for c in λ).

For each partition λ, the corresponding matrix block carries:
- A central idempotent π_λ ∈ Z(H_n(q));
- A faithful matrix representation ρ_λ : H_n(q) → M_{f^λ}(R).

The Markov trace decomposes as
  `tr_M(x) = Σ_λ y_λ · χ^λ(x)`
where `y_λ = tr_M(π_λ) / f^λ` is the *central coefficient*, and
`χ^λ(x) = tr(ρ_λ(x))` is the partition character.

## References

- [thm:wedderburn-mass-formula]
- [prop:y-lambda-recipe-from-partition]
- Mathas (1999), Theorem 3.43.
-/

namespace QOU.Hecke

universe u

/-- A partition `λ ⊢ n` represented as a non-increasing tuple of
positive integers summing to `n`. We use `List ℕ` with explicit
predicates for partition validity. -/
@[ext]
structure Partition (n : ℕ) where
  parts : List ℕ
  sum_eq : parts.sum = n
  positive : ∀ p ∈ parts, 0 < p
  decreasing : parts.Sorted (· ≥ ·)

/-- The hook-length formula: f^λ = n! / Π hook(c). The hook lengths
themselves are computed in `Mathlib.Combinatorics.YoungTableau` (or
re-derived locally); this is the abstract dimension predicate. -/
class SpechtDimension {n : ℕ} (lam : Partition n) where
  /-- Specht module dimension f^λ. -/
  dim : ℕ
  positive : 0 < dim

/-- **The block dimension `f^λ`, computed from the partition.**

`dimHLF` is the Frame–Robinson–Thrall hook-length dimension `n! / ∏_c h_c`
(`QOU.BraidKnot.IdentityI`). This is a plain function of `λ`, not a field: it is
what closes the last freedom the class had. Before 2026-08-30 `blockDim` was a
free `Partition n → ℕ`, so `y_λ` was pinned only *relative* to it and every
`1/d` remained realisable.

**This IS the SYT count, and that is a theorem here — not a commitment.**
Frame–Robinson–Thrall (`dimHLF λ = #SYT(λ)`) is proved in this corpus at general
`n`, sorry-free: `QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF`, via the
Greene–Nijenhuis–Wilf route (corner recursion + hook-summation identity, combined
by strong induction). `blockDim_eq_numSYT` below discharges it against a
`Partition n`, whose `decreasing` and `positive` fields supply exactly the two
hypotheses FRT needs, so nothing is left assumed.

**Corrected 2026-08-30.** An earlier version of this docstring said the general
theorem was "open here" and that the class committed to the FRT *formula* without
proving FRT. Both halves were false. The error came from trusting
`SYTHookFormulaRows.lean`'s header, which is itself stale and is fixed in the
same commit — the corpus, not a source file's status note, is the authority
(AGENTS.md §"Before declaring open"). -/
def blockDim {n : ℕ} (lam : Partition n) : ℕ :=
  QOU.BraidKnot.IdentityI.dimHLF lam.parts

/-- **The block dimension IS the number of standard Young tableaux of shape `λ`.**

`blockDim` is defined by the hook-length *formula*; this identifies it with the
combinatorial object that formula computes, via the corpus's sorry-free general
Frame–Robinson–Thrall theorem.

Both hypotheses FRT needs come free from the `Partition n` structure — `parts` is
weakly decreasing (`lam.decreasing`) and its entries are positive
(`lam.positive`) — so there is nothing left to assume. This is what upgrades
`blockDim` from a chosen formula to `f^λ`. -/
theorem blockDim_eq_numSYT {n : ℕ} (lam : Partition n) :
    blockDim lam = QOU.Mathlib.SYTEnum.numSYTenum lam.parts :=
  (QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF lam.parts lam.decreasing lam.positive).symm

/--
Wedderburn–Artin decomposition of `H_n(q)`. An instance asserts:
- For each partition λ ⊢ n, a central idempotent `pi_lambda λ`;
- The idempotents are mutually orthogonal and sum to 1;
- Each block `pi_lambda λ · A · pi_lambda λ` is isomorphic to
  `M_{f^λ}(R)` (matrix algebra of size f^λ);
- The Markov trace's restriction to each block is the matrix trace
  scaled by the central coefficient `y_λ`.

For brevity we store only the central idempotents + scalar
coefficients here; the matrix-algebra isomorphisms are captured
abstractly via a representation `rho_lambda`.
-/
class WedderburnDecomp
    {R : Type u} (n : ℕ) (q : R) (A : Type u)
    [CommRing R] [Inv R] [Ring A] [Algebra R A]
    [HeckeAlgebra R n q A] [MT : MarkovTrace n q A] where
  /-- Central idempotent for partition λ. -/
  pi_lambda : Partition n → A
  /-- Each pi_lambda is idempotent. -/
  idempotent : ∀ lam : Partition n, (pi_lambda lam) * (pi_lambda lam) = pi_lambda lam
  /-- Distinct idempotents are orthogonal. -/
  orthogonal : ∀ lam mu : Partition n, lam.parts ≠ mu.parts →
    pi_lambda lam * pi_lambda mu = 0
  /-- Each `π_λ` is **central**: `π_λ ∈ Z(H_n(q))`. This was always the
  claim of this class (see the docstring above: "central idempotent
  π_λ ∈ Z(H_n(q))") and of the §9.1 partition-respecting table
  ("Central idempotents π_λ (orthogonal, central) — asserted (class
  axiom)"); encoding it as a field closes the docstring-vs-fields gap
  (the `proof-claims-unencoded` pattern) and unlocks the L-3 per-λ
  Frobenius block-orthogonality below as *derived* theorems. Its
  discharge from the Hecke structure is the same Mathas (1999) §3.43
  debt as `orthogonal` (§9.4 L-2). -/
  central : ∀ (lam : Partition n) (a : A), pi_lambda lam * a = a * pi_lambda lam
  /-- Markov-trace central coefficient y_λ. By
  prop:y-lambda-recipe-from-partition this is a rational function
  in q given by `s_λ(1, Q, ..., Q^{r-1}) / Σ d_μ s_μ(...)`. -/
  y_lambda : Partition n → R
  /-- The complete set of partitions (all irreducible representations
  of `H_n(q)`, one for each partition `λ ⊢ n`). This equals the full
  set `{λ | λ ⊢ n}` of Young diagrams of `n`; by the Wedderburn–Artin
  theorem there are no other irreducibles over a generic base ring. -/
  all_parts : Finset (Partition n)
  /-- **Resolution of identity (completeness).** The central idempotents
  sum to `1`: `Σ_{λ ∈ all_parts} π_λ = 1`.  This is the machine-checked
  "we account for everything" — by Wedderburn–Artin the partitions of `n`
  index ALL irreducibles (Mathas 1999 §3.43), so the blocks exhaust the
  algebra with no residue.  `trace_exhaustive` below is the *derived*
  unweighted decomposition that rests on this partition of unity; the `y_λ`
  enter one level down, through `block_scaling`. -/
  complete : all_parts.sum (fun lam => pi_lambda lam) = 1
  /-- The `λ`-block representation `ρ_λ : A → M_{f^λ}(R)`, as an **algebra
  homomorphism**.

  This replaces a free field `chi_lambda : Partition n → A → R`, and the
  upgrade is the point: an `AlgHom` satisfies `ρ_λ 1 = 1`, so the block
  character has `χ^λ(1) = f^λ` forced. With `χ^λ` free, `block_scaling` was an
  equation on a product of two unknowns and pinned neither factor; with `ρ_λ`
  an algebra map it pins `y_λ` against `blockDim` (`yLambda_determined`). -/
  rho : (lam : Partition n) →
    A →ₐ[R] Matrix (Fin (blockDim lam)) (Fin (blockDim lam)) R
  /-- **Block scaling.** The Markov trace restricted to block `λ` is the block
  character scaled by the central coefficient: `tr_M(x · π_λ) = y_λ · χ^λ(x)`.

  This is the sentence in this class's header docstring — *"The Markov trace's
  restriction to each block is the matrix trace scaled by the central
  coefficient `y_λ`"* — which was prose and is now a field. It is where the
  `y_λ` actually enter, and it is a **hypothesis**, not the conclusion:
  `trace_decomposition` derives `tr_M(x) = Σ_λ y_λ · χ^λ(x)` from it together
  with `complete`, and neither input is that identity.

  It replaces a field `trace_decomp` that asserted the conclusion directly, over
  the terms `tr_M(x · π_λ)` rather than `χ^λ(x)` — applying `y_λ` on top of a
  quantity that already carries it. That field was not merely redundant with
  the derived `trace_exhaustive`: the two together forced `(1 − y_μ) · tr_M(π_μ)
  = 0` for every block, i.e. every weight trivial or its block trace zero.
  Machine-checked as `weights_inert` / `weight_one_or_block_trace_zero` in
  commit `9e8b712fa2`, which is where those two theorems can still be run; they
  are deleted here along with the field they were about. -/
  block_scaling : ∀ (x : A) (lam : Partition n),
      MT.trace (x * pi_lambda lam) = y_lambda lam * Matrix.trace (rho lam x)

namespace WedderburnDecomp

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]
  [WD : WedderburnDecomp n q A]

/-- The **block character** `χ^λ`, now *computed* as the matrix trace of the
block representation rather than carried as a free field. -/
def chi_lambda (lam : Partition n) (x : A) : R :=
  Matrix.trace (WD.rho lam x)

/-- `χ^λ(1) = f^λ`: the block character at the identity is the block dimension.

This is the rigidity the `AlgHom` upgrade buys, and the reason `y_λ` becomes
pinned below. A free `chi_lambda` field could take any value at `1`; an algebra
map cannot, because `ρ_λ 1 = 1` and the trace of an identity matrix is its
size. -/
theorem chi_lambda_one (lam : Partition n) :
    chi_lambda (WD := WD) lam 1 = (blockDim lam : R) := by
  change Matrix.trace (WD.rho lam 1) = (blockDim lam : R)
  have h1 : WD.rho lam 1 = 1 := map_one (WD.rho lam)
  rw [h1, Matrix.trace_one, Fintype.card_fin]

/-- **`y_λ` is determined.** `block_scaling` at `x = 1`, with `χ^λ(1) = f^λ`:

  `tr_M(π_λ) = y_λ · f^λ`.

The weight is no longer a free parameter: it is the block trace against the
block dimension. Contrast `RankOneDegeneracy`, where against the
previous class every nonzero rational was realisable as `y_λ` at every
partition. -/
theorem yLambda_determined (lam : Partition n) :
    MT.trace (WD.pi_lambda lam) = WD.y_lambda lam * (blockDim lam : R) := by
  have h := WD.block_scaling 1 lam
  rw [one_mul] at h
  rw [h, ← chi_lambda_one (WD := WD) lam]
  rfl

omit WD in
/-- **Uniqueness of the weight.** Two decompositions agreeing on the block
idempotent agree on `y_λ`, provided the block dimension is not a zero divisor.

The `blockDim` hypothesis the 2026-08-30 morning version of this theorem
carried is **gone**, and its absence is the content: `blockDim` is now a
function of `λ` alone, so two decompositions cannot disagree about it. What
remains is a hypothesis about `R` (no zero divisors) and about the value
`(f^λ : R)`, not about the decompositions. -/
theorem yLambda_unique [NoZeroDivisors R]
    (W W' : WedderburnDecomp n q A) (lam : Partition n)
    (hpi : W.pi_lambda lam = W'.pi_lambda lam)
    (hne : (blockDim lam : R) ≠ 0) :
    W.y_lambda lam = W'.y_lambda lam := by
  have h  := yLambda_determined (WD := W) lam
  have h' := yLambda_determined (WD := W') lam
  rw [← hpi] at h'
  exact mul_right_cancel₀ hne (h.symm.trans h')

open Classical in
/-- **(§9.4 L-2) Kronecker orthogonality of the central idempotents** —
`π_λ · π_μ = δ_{λ,μ} · π_λ`. Packages the `idempotent` and `orthogonal`
axioms into one relation. The statement is keyed on `lam = mu` (matching the
Kronecker `δ_{λ,μ}` and independent of `Partition`'s internal representation);
the `@[ext]` proof-irrelevance step (equal `parts` ⇒ equal `Partition`) is used
only internally to bridge to the `parts`-keyed `orthogonal` axiom. Makes the
block algebra directly usable.

The *standing* §9.4 debt is to **discharge** the `orthogonal` axiom itself
(and `y_lambda` uniqueness, L-1) from the algebra structure via
character-orthogonality — Mathas (1999) §3.43, not yet in Mathlib. This lemma
is the immediate consequence of the current axioms, not that discharge. -/
theorem pi_mul_pi (lam mu : Partition n) :
    WD.pi_lambda lam * WD.pi_lambda mu
      = if lam = mu then WD.pi_lambda lam else 0 := by
  by_cases h : lam = mu
  · rw [if_pos h, h, WD.idempotent]
  · rw [if_neg h]
    apply WD.orthogonal lam mu
    intro hp
    apply h
    ext1
    exact hp

/-- **Exhaustiveness of the Markov trace over the Wedderburn blocks** —
`tr_M(x) = Σ_λ tr_M(x · π_λ)`, with NO residue.  The machine-checked
"we account for everything": *derived* from the resolution of identity
`Σ_λ π_λ = 1` (`WD.complete`) via left-distributivity and `R`-linearity
of the trace — it does NOT re-assume a decomposition.  The sum runs over
the complete set `WD.all_parts` (the `p(n)` partitions of `n`); there are
no other blocks.  This lemma needs only `complete`; `trace_decomposition`
below adds `block_scaling` to it and gets the `y_λ`-weighted form. -/
theorem trace_exhaustive (x : A) :
    MT.trace x
      = WD.all_parts.sum (fun lam => MT.trace (x * WD.pi_lambda lam)) := by
  have hx : WD.all_parts.sum (fun lam => x * WD.pi_lambda lam) = x := by
    rw [← Finset.mul_sum, WD.complete, mul_one]
  calc
    MT.trace x
        = MT.trace (WD.all_parts.sum (fun lam => x * WD.pi_lambda lam)) := by
          rw [hx]
    _ = WD.all_parts.sum (fun lam => MT.trace (x * WD.pi_lambda lam)) :=
          map_sum MT.trace _ WD.all_parts

/-- **Block decomposition of the trace, derived**:
`tr_M(x) = Σ_λ y_λ · χ^λ(x)`, the sum running over `WD.all_parts` (the
complete set of irreducibles).

Two inputs, neither of them the conclusion: `complete` (via
`trace_exhaustive`, which contributes the unweighted sum) and `block_scaling`
(which contributes the weights, one block at a time). Note where each enters —
the `y_λ` are *not* a consequence of completeness, which is why assuming the
whole identity was never necessary, and they are *not* free either, which is
why the honest axiom is the block scaling. -/
theorem trace_decomposition (x : A) :
    MT.trace x = WD.all_parts.sum (fun lam =>
      WD.y_lambda lam * chi_lambda (WD := WD) lam x) := by
  -- Ref: [thm:wedderburn-mass-formula].
  rw [trace_exhaustive (WD := WD) x]
  exact Finset.sum_congr rfl (fun lam _ => WD.block_scaling x lam)

/-- Auxiliary product shift: `(a·π_λ)·(b·π_μ) = (a·b)·(π_λ·π_μ)`, from
centrality of the idempotents. The noncommutative bookkeeping behind both
L-3 theorems below. -/
theorem pi_mul_shift (lam mu : Partition n) (a b : A) :
    (a * WD.pi_lambda lam) * (b * WD.pi_lambda mu)
      = (a * b) * (WD.pi_lambda lam * WD.pi_lambda mu) := by
  simp only [mul_assoc]
  congr 1
  rw [← mul_assoc, WD.central lam b, mul_assoc]

variable (n) (q) in
/-- The algebra-side **bilinear trace pairing** `⟨a,b⟩_F = tr_M(a·b)`.
Symmetric by the cyclicity axiom (M2). `n` and `q` are explicit because
they are not inferable from `a b : A` alone. -/
def frobPairing (a b : A) : R := MT.trace (a * b)

open Classical in
/-- **(§9.4 L-3, cross-block vanishing)** — the bilinear trace pairing of
elements in *distinct* simple blocks vanishes:
`⟨a·π_λ, b·π_μ⟩_F = 0` for `λ ≠ μ`. Derived from centrality
(`pi_mul_shift`) + Kronecker orthogonality (`pi_mul_pi`). -/
theorem frobPairing_block_orthogonal (lam mu : Partition n) (h : lam ≠ mu)
    (a b : A) :
    frobPairing n q (a * WD.pi_lambda lam) (b * WD.pi_lambda mu) = (0 : R) := by
  -- Ref: [leitner2026] def:frobenius-hopf-substrate; Mathas (1999) §3.43.
  unfold frobPairing
  rw [pi_mul_shift, pi_mul_pi, if_neg h, mul_zero, map_zero]

/-- **(§9.4 L-3, block decomposition)** — the bilinear trace pairing splits
over the simple blocks with no residue:
`⟨a,b⟩_F = Σ_λ ⟨a·π_λ, b·π_λ⟩_F`. Together with
`frobPairing_block_orthogonal` this is the per-λ block-orthogonality
`⟨·,·⟩_F = ⊕_λ ⟨·,·⟩_F^λ` of §9.4 L-3, derived from the resolution of
identity (`trace_exhaustive`) + centrality + idempotency. -/
theorem frobPairing_block_decomp (a b : A) :
    frobPairing n q a b
      = WD.all_parts.sum (fun lam =>
          frobPairing n q (a * WD.pi_lambda lam) (b * WD.pi_lambda lam)) := by
  -- Ref: [leitner2026] def:frobenius-hopf-substrate; Mathas (1999) §3.43.
  unfold frobPairing
  have h : ∀ lam : Partition n,
      (a * WD.pi_lambda lam) * (b * WD.pi_lambda lam)
        = (a * b) * WD.pi_lambda lam := by
    intro lam
    rw [pi_mul_shift, WD.idempotent]
  calc MT.trace (a * b)
      = WD.all_parts.sum (fun lam => MT.trace ((a * b) * WD.pi_lambda lam)) :=
        trace_exhaustive (a * b)
    _ = WD.all_parts.sum (fun lam =>
          MT.trace ((a * WD.pi_lambda lam) * (b * WD.pi_lambda lam))) := by
        refine Finset.sum_congr rfl (fun lam _ => ?_)
        rw [h lam]

/-- **Dimension-weighted sum of `y_λ` (`qou-6dzi`).**
Evaluating `trace_decomposition` at `1` and substituting `chi_lambda_one`
gives `∑_{λ ∈ all_parts} y_λ · f^λ = tr_M(1)`. -/
theorem sum_yLambda_mul_blockDim :
    WD.all_parts.sum (fun lam => WD.y_lambda lam * (blockDim lam : R)) = MT.trace 1 := by
  have h := trace_decomposition (WD := WD) 1
  rw [h]
  refine Finset.sum_congr rfl (fun lam _ => ?_)
  rw [chi_lambda_one (WD := WD) lam]

/-- **Orthogonality excludes a unit idempotent alongside any non-zero block (`qou-6dzi`).**
If `π_λ = 1` for some partition `λ`, then every distinct partition `μ` (`λ.parts ≠ μ.parts`)
must have `π_μ = 0`. -/
theorem pi_lambda_eq_one_forces_other_zero {lam mu : Partition n}
    (h : lam.parts ≠ mu.parts) (h1 : WD.pi_lambda lam = 1) :
    WD.pi_lambda mu = 0 := by
  have horth := WD.orthogonal lam mu h
  rw [h1, one_mul] at horth
  exact horth

/-- **No trivial constant-unit block decomposition over a nontrivial algebra (`qou-6dzi`).**
In any nontrivial ring `A` (`(1 : A) ≠ 0`), two distinct partitions `λ.parts ≠ μ.parts`
cannot both be assigned the unit projector `1`, machine-certifying why the trivial instance's
`block_proj _ := 1` requires `Subsingleton` and fails on any nontrivial carrier. -/
theorem not_both_pi_lambda_eq_one [Nontrivial A] {lam mu : Partition n}
    (h : lam.parts ≠ mu.parts) :
    ¬ (WD.pi_lambda lam = 1 ∧ WD.pi_lambda mu = 1) := by
  rintro ⟨hlam, hmu⟩
  have hzero := pi_lambda_eq_one_forces_other_zero (WD := WD) h hlam
  rw [hmu] at hzero
  exact one_ne_zero hzero

end WedderburnDecomp

end QOU.Hecke
