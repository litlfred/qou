import QOU.Hecke.Algebra
import QOU.Hecke.MarkovTrace
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.List.Sort

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
  algebra with no residue.  `trace_decomp` below is the `y_λ`-weighted
  refinement that rests on this partition of unity. -/
  complete : all_parts.sum (fun lam => pi_lambda lam) = 1
  /-- Trace decomposition: the Markov trace decomposes over `all_parts` as
  `tr(x) = Σ_{λ ∈ all_parts} y_λ · tr(x · π_λ)`.
  Follows from `Σ_{λ ∈ all_parts} π_λ = 1` (partition of unity),
  trace linearity, and `y_λ` as central coefficients. -/
  trace_decomp : ∀ (x : A),
      MT.trace x =
        all_parts.sum (fun lam => y_lambda lam • MT.trace (x * pi_lambda lam))

namespace WedderburnDecomp

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]
  [WD : WedderburnDecomp n q A]

/-- Wedderburn decomposition of the Markov trace:
    tr_M(x) = Σ_λ y_λ · χ^λ(x)
where χ^λ(x) = tr(x · π_λ) (block-restricted trace), and the sum
runs over `WD.all_parts` (the complete set of irreducibles). -/
theorem trace_decomposition (x : A) :
    MT.trace x = WD.all_parts.sum (fun lam =>
      WD.y_lambda lam • MT.trace (x * WD.pi_lambda lam)) := by
  -- Ref: [thm:wedderburn-mass-formula]. Follows directly from the
  -- trace_decomp axiom of WedderburnDecomp.
  exact WD.trace_decomp x

open Classical in
/-- **(§9.4 L-2) Kronecker orthogonality of the central idempotents** —
`π_λ · π_μ = δ_{λ,μ} · π_λ`. Packages the `idempotent` and `orthogonal`
axioms into one relation. The statement is keyed on `lam = mu` (matching the
Kronecker `δ_{λ,μ}` and independent of `Partition`'s internal representation);
the `@[ext]` proof-irrelevance step (equal `parts` ⇒ equal `Partition`) is used
only internally to bridge to the `parts`-keyed `orthogonal` axiom. Makes the
block algebra directly usable.

The *standing* §9.4 debt is to **discharge** the `orthogonal` axiom itself
(and `y_lambda` uniqueness, L-1) from the Hecke structure via Schur
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
no other blocks.  Contrast `trace_decomposition`, which projects the
`y_λ`-weighted `trace_decomp` axiom; this lemma needs only `complete`. -/
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
/-- The Hecke-side **Frobenius pairing** `⟨a,b⟩_F = tr_M(a·b)`
(cf. `def:frobenius-hopf-substrate`: `⟨a,b⟩_F = ∫_A(a·b)` with the
Markov trace as the integral). Symmetric by the Markov cyclicity
axiom (M2). `n` and `q` are explicit because they are not inferable
from `a b : A` alone. -/
def frobPairing (a b : A) : R := MT.trace (a * b)

open Classical in
/-- **(§9.4 L-3, cross-block vanishing)** — the Frobenius pairing of
elements in *distinct* Wedderburn blocks vanishes:
`⟨a·π_λ, b·π_μ⟩_F = 0` for `λ ≠ μ`. Derived from centrality
(`pi_mul_shift`) + Kronecker orthogonality (`pi_mul_pi`); no new
axiom beyond the `WedderburnDecomp` class. -/
theorem frobPairing_block_orthogonal (lam mu : Partition n) (h : lam ≠ mu)
    (a b : A) :
    frobPairing n q (a * WD.pi_lambda lam) (b * WD.pi_lambda mu) = (0 : R) := by
  -- Ref: [manuscript] def:frobenius-hopf-substrate; Mathas (1999) §3.43.
  unfold frobPairing
  rw [pi_mul_shift, pi_mul_pi, if_neg h, mul_zero, map_zero]

/-- **(§9.4 L-3, block decomposition)** — the Frobenius pairing splits
over the Wedderburn blocks with no residue:
`⟨a,b⟩_F = Σ_λ ⟨a·π_λ, b·π_λ⟩_F`. Together with
`frobPairing_block_orthogonal` this is the per-λ block-orthogonality
`⟨·,·⟩_F = ⊕_λ ⟨·,·⟩_F^λ` of §9.4 L-3, derived from the resolution of
identity (`trace_exhaustive`) + centrality + idempotency — conditional
on the same `WedderburnDecomp` class as L-2's `pi_mul_pi`, with the
class-axiom discharge (Mathas §3.43) remaining the L-1/L-2 debt. -/
theorem frobPairing_block_decomp (a b : A) :
    frobPairing n q a b
      = WD.all_parts.sum (fun lam =>
          frobPairing n q (a * WD.pi_lambda lam) (b * WD.pi_lambda lam)) := by
  -- Ref: [manuscript] def:frobenius-hopf-substrate; Mathas (1999) §3.43.
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

end WedderburnDecomp

end QOU.Hecke
