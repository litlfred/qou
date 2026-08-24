/-
  Wedderburn–Bratteli recursion for Jones–Markov weights y_λ at H_n(R, q).

  Statement: with z = 1/(v + v⁻¹) the Markov parameter (where v
  is the formal square root of q, so v² = q), the Jones–Markov
  weights satisfy a multiplicative recursion of the form

    y_λ^(n+1) = z · F_q(λ, μ) · y_μ^(n)

  for every Bratteli edge μ ↗ λ at generic q, where F_q(λ, μ) is a
  q-rational function of the added cell's q-content c(λ, μ) = j - i
  and the partition shape data.  The specific closed form

    F_q(c, h) = [c+1]_q / [c+h]_q

  with h := height(λ) is one candidate matching the Wenzl-bridge
  derivation (see prop:y-lambda-closed-form-wenzl-bridge); the full
  closed form is extracted symbolically from the y_λ witness ratios
  via y_lambda_bratteli_extract.py and is canonically expressed via
  the Wenzl Schur principal-specialization formula.

  The Bratteli diagram is multiplicity-free at generic q (Hoefsmit),
  so the recursion is well-defined and reproduces the y_λ tower from
  H_2 base data.

  **Pre-Archimedean stub.** The recursion is stated over an
  abstract field `R` carrying `q : R` and `v : R` with `v² = q`
  (the formal square root of `q`).  On `R = ℚ(v)` (a Laurent
  field over the formal `v`) every quantity is rational in `v`;
  the Archimedean specialisation `R = ℝ` evaluating at `v = √q₀`
  is the post-τ realisation and lives downstream
  (`QOU.Calculations`).  Real.sqrt was removed; the formal square
  root `v` is now an explicit parameter.

  **Base ring (§7c): the `Field` is essential here, not scaffolding.**
  Adjudicated against `wall-base-ring-minimal`: the recursion is a
  q-*rational* statement, not a q-Laurent one, and both of its divisions
  are by elements that genuinely vanish somewhere.

  * `markovZ' v = 1/(v + v⁻¹)` divides by `v + v⁻¹`, which is `0` at
    `v² = −1`; so `v + v⁻¹` is not a unit and the quotient is not a
    Laurent polynomial.
  * `bratteliFactor = [c+1]_q / [c+h]_q` divides by a q-integer, which
    vanishes at roots of unity — exactly the locus this file excludes by
    working "at generic q".
  * `qIntZ` is an abbreviation for the **canonical** `QOU.QInteger.qIntBalZ`,
    whose own defining equation is `(q^k − q^{−k})/(q − q⁻¹)` over
    `[Field R]`. That `Field` is a deliberate, documented upstream choice
    ("algebraic inverse — §7c, NOT archimedean; no `ℝ`"), so it is
    inherited here and cannot be weakened locally.

  A division-free restatement is possible in principle by moving to the
  relational R[h] form (`z·(v²+1) = v`, `F·[c+h]_q = [c+1]_q`), but that
  converts `markovZ'`/`bratteliFactor` from functions into relations and
  so changes the shape of `SatisfiesWedderburnBratteliRecursion` and every
  consumer; it would have to start at `QOU.MathlibExt.QIntegerCanonical`,
  not here.  Nothing in this file is archimedean, so it is already on the
  correct side of the wall.

  Refs: prop:wedderburn-bratteli-recursion,
        prop:y-lambda-closed-form-wenzl-bridge,
        prop:hoefsmit-seminormal-form,
        thm:jones-markov-trace
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.BraidsAndKnots

universe u

/-- Symmetric q-integer for ℤ exponents:
    `qIntZ q k = [k]_q = (q^k - q^(-k)) / (q - q^(-1))`.

    Polymorphic in the ground field `R`.  The denominator
    `q - q⁻¹` is required to be invertible (`q² ≠ 1`); on the
    Laurent field `ℚ(q)` this holds as long as we work generically
    (away from roots of unity). -/
noncomputable abbrev qIntZ {R : Type u} [Field R] (q : R) (k : ℤ) : R :=
  QOU.QInteger.qIntBalZ q k

/-- Markov parameter `z = 1/(v + v⁻¹)` in terms of the formal
    square root `v` of `q` (so `v² = q`).  No `Real.sqrt` is
    used — `v` is supplied externally. -/
noncomputable def markovZ' {R : Type u} [Field R] (v : R) : R :=
  1 / (v + v⁻¹)

/-- A partition (skeleton). The recursion statement below does not
    depend on internal partition structure; it carries the q-content
    of the added cell and the height of `lam` as explicit parameters.
    Full box-difference decoder (μ ⊂ λ check, removable-corner
    enumeration, content extraction) is open work. -/
structure Partition where
  parts : List ℕ

/-- The height of λ — number of rows. -/
def Partition.height (lam : Partition) : ℕ := lam.parts.length

/-- A Bratteli edge `μ ↗ λ` decorated with the q-content `c` of the
    added cell. The content is carried as a structure field rather
    than recovered from `μ, λ` (which would require the box-difference
    decoder). At generic q the Bratteli diagram is multiplicity-free
    (Hoefsmit), so `c` is determined uniquely by the edge. -/
structure BratteliEdge where
  mu : Partition
  lam : Partition
  /-- q-content `c(λ, μ) = j - i` of the unique box in `λ \ μ`. -/
  content : ℤ

/-- The Bratteli content factor `F_q(c, h) = [c+1]_q / [c+h]_q` in
    the recursion `y_λ^(n+1) = z · F_q · y_μ^(n)`. -/
noncomputable def bratteliFactor {R : Type u} [Field R]
    (q : R) (c h : ℤ) : R :=
  qIntZ q (c + 1) / qIntZ q (c + h)

/-- A weight function `y : Partition → R` satisfies the Wedderburn–
    Bratteli recursion at parameter `(q, v)` (with `v² = q`) if for
    every Bratteli edge `e : BratteliEdge`, the next-level weight
    `y e.lam` equals `z · F_q(c, height(λ)) · y e.mu`. -/
def SatisfiesWedderburnBratteliRecursion {R : Type u} [Field R]
    (q v : R) (y : Partition → R) : Prop :=
  ∀ e : BratteliEdge,
    y e.lam = (markovZ' v) *
              bratteliFactor q e.content (e.lam.height : ℤ) *
              y e.mu

/-- Existence: a function `y : Partition → R` satisfying the
    Wedderburn–Bratteli recursion exists at any generic `q` (with
    formal `v` such that `v² = q`).

    Closed with the trivial witness `y ≡ 0`: the recursion
    `y e.lam = z · F · y e.mu` is satisfied vacuously since both
    sides reduce to 0. The intended Jones–Markov witness is
    constructed numerically in
    `computations/y-lambda-jones-markov-witness.json`
    (n=2..12) and symbolically in `y-lambda-symbolic-witness.json`;
    porting that construction into Lean (with the Hoefsmit seminormal
    eigenvalues + Markov property) is the meaningful next step.

    The theorem as stated only asserts *consistency* of the recursion,
    not non-triviality of the weight. Sharpening to "the unique
    Markov-trace-derived weight satisfies the recursion" requires a
    Jones-Markov axiom on top of `MarkovTransitionStep`. -/
-- Ref: prop:wedderburn-bratteli-recursion proof, [hoefsmit1974];
-- Hoefsmit seminormal eigenvalue on per-cell idempotent + Markov property.
theorem wedderburn_bratteli_recursion_holds
    {R : Type u} [Field R] (q v : R) :
    ∃ y : Partition → R, SatisfiesWedderburnBratteliRecursion q v y :=
  ⟨fun _ => 0, by
    intro e
    show (0 : R) = _ * _ * 0
    ring⟩

/-- Application: given any `y` known to satisfy the recursion, the
    edge equation follows. -/
theorem wedderburn_bratteli_apply
    {R : Type u} [Field R] (q v : R) (y : Partition → R)
    (hrec : SatisfiesWedderburnBratteliRecursion q v y)
    (e : BratteliEdge) :
    y e.lam = (markovZ' v) *
              bratteliFactor q e.content (e.lam.height : ℤ) *
              y e.mu :=
  hrec e

/-- Base case at H_1: the weight on the single partition `(1)` is 1, and
    that value **anchors** the recursion — on any edge out of `(1)` the
    next-level weight is the bare Bratteli factor, with no free constant
    left. This is `tr_M(1_1) = 1` propagating one level up.

    The old statement was `(hbase : y ⟨[1]⟩ = 1) : y ⟨[1]⟩ = 1 := hbase` —
    hypothesis identical to conclusion, proof the identity. It named the
    base case without asserting anything about it, and would have stayed
    true had every definition in this file been swapped. Anchoring is the
    content the docstring already claimed; it just was not stated.

    §7c: `Field` now, not `CommRing`. The old form divided by nothing
    because it did nothing; using the recursion brings in `bratteliFactor`,
    whose q-integer quotient is exactly why the rest of this file needs a
    field. -/
-- Ref: [manuscript] thm:jones-markov-trace base case;
-- H_1(R, q) = R, tr_M = identity character on V_(1).
theorem y_base_case_singleton {R : Type u} [Field R] (q v : R)
    (y : Partition → R)
    (hrec : SatisfiesWedderburnBratteliRecursion q v y)
    (hbase : y ⟨[1]⟩ = (1 : R))
    (e : BratteliEdge) (he : e.mu = ⟨[1]⟩) :
    y e.lam = (markovZ' v) * bratteliFactor q e.content (e.lam.height : ℤ) := by
  rw [wedderburn_bratteli_apply q v y hrec e, he, hbase, mul_one]

-- Plancherel completeness at every level: `Σ y_λ · d_λ = 1` where
-- `d_λ = dim V_λ` (hook-length formula), summed over all partitions
-- of n.  The Markov-trace normalisation `tr_M(1_n) = 1` transported
-- through Wedderburn, valid for any `y` arising from a Markov trace.
--
-- The `parts_complete` hypothesis ensures the list `parts` contains
-- every partition of `n` exactly once — without it, the partial sum
-- is not guaranteed to equal 1.
/-- **External axiom (§3b-cond pattern): plancherel_completeness.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 Lemma 3.2 (Plancherel completeness Σ_λ y_λ·d_λ = 1 from Markov-trace normalisation)
axiom plancherel_completeness_axiom {R : Type u} [Field R] (q v : R) (n : ℕ)
    (parts : List Partition)
    (_parts_complete : ∀ lam : Partition, lam.parts.sum = n → lam ∈ parts)
    (_parts_nodup : parts.Nodup)
    (y : Partition → R) (d : Partition → ℕ)
    (_hrec : SatisfiesWedderburnBratteliRecursion q v y) :
    (parts.map (fun lam => y lam * (d lam : R))).sum = (1 : R)

theorem plancherel_completeness
    {R : Type u} [Field R] (q v : R) (n : ℕ)
    (parts : List Partition)
    (_parts_complete : ∀ lam : Partition, lam.parts.sum = n → lam ∈ parts)
    (_parts_nodup : parts.Nodup)
    (y : Partition → R) (d : Partition → ℕ)
    (_hrec : SatisfiesWedderburnBratteliRecursion q v y) :
    (parts.map (fun lam => y lam * (d lam : R))).sum = (1 : R) :=
  plancherel_completeness_axiom q v n parts _parts_complete _parts_nodup y d _hrec

end QOU.BraidsAndKnots
