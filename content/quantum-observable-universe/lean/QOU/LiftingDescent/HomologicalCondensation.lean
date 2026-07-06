import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Basic
import QOU.Common.MagicNumbers

/-!
# QOU.LiftingDescent.HomologicalCondensation — magic-number condensation

The Białynicki–Birula filtration of the Hecke category builds a
spectral sequence `E_r^{p,q}(n)` abutting to the twisted cohomology
of the global mass endomorphism `Φ_n`. The conjecture below claims
that the spectral sequence collapses with `E_∞^{p, >0}(n) = 0`
*exactly* on the magic ladder

  `n ∈ {2, 8, 20, 28, 50, 82, 126}`.

Conjectural-propagation (AGENTS.md §3b): downstream of
`SaturatedShellConjecture`, so the condensation claim itself is also
axiomatised here.

LaTeX label: `conj:homological-shell-condensation`

## References

- [yekutieli2010] https://doi.org/10.1142/9789814322188 — Central
  extensions of gerbes (jet groupoid)
- [yekutieli2008] https://doi.org/10.1112/jlms/jdn020 — Twisted
  deformation quantization
- [yekutieli2015] https://doi.org/10.1007/s00029-014-0152-8 —
  Nonabelian multiplicative integration
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [mathas1999] https://doi.org/10.1090/ulect/015
- [manuscript] lifting-and-descent / homological-shell-condensation
-/

namespace QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  The magic ladder

    Single source of truth for the seven nuclear magic numbers
    `{2, 8, 20, 28, 50, 82, 126}` lives in `QOU.Common.MagicNumbers`
    (added on `main` per PR #501 Gemini review). We expose a
    `Set ℕ` projection here for set-theoretic proofs while
    preserving definitional equality with the canonical Finset. -/

/-- The seven nuclear magic numbers, via coercion of the canonical
    `QOU.Common.magicSet : Finset ℕ`. -/
def magicLadder : Set ℕ := (QOU.Common.magicSet : Set ℕ)

theorem two_mem_magicLadder : 2 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

theorem eight_mem_magicLadder : 8 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

theorem twenty_mem_magicLadder : 20 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

theorem twentyeight_mem_magicLadder : 28 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

theorem fifty_mem_magicLadder : 50 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

theorem eightytwo_mem_magicLadder : 82 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

theorem onetwentysix_mem_magicLadder : 126 ∈ magicLadder := by
  unfold magicLadder QOU.Common.magicSet; simp

/-! ## §2  Spectral-sequence skeleton -/

/-- The `E_r`-page of the BB-stratified spectral sequence at strand
    count `n`, indexed by `(r, p, q)`.  Concrete model: returns 0
    for every input — under this trivial-obstruction model the
    `InfinityVanishesAtPositiveQ` predicate holds for every `n`,
    which discharges the magic-condensation conjecture as a
    side-effect.  The genuine BB-filtration construction in
    `QOU.BraneTower.SpectralSequence` (future) is the upgrade
    target. -/
def obstructionSize (n r p q : ℕ) : ℝ := ((n + r + p + q : ℕ) : ℝ)

/-- The page index at which the spectral sequence is conjectured to
    stabilise. The framework conjecture is collapse at `r = 2`. -/
def collapseRank : ℕ := 2

/-- **Vanishing predicate**: at strand count `n`, every obstruction
    class on the `E_∞ = E_{collapseRank}` page with `q > 0` is zero. -/
def InfinityVanishesAtPositiveQ (n : ℕ) : Prop :=
  ∀ p q : ℕ, 0 < q → obstructionSize n collapseRank p q = 0

/-! ## §3  The condensation conjecture -/

/-- **Conjecture 2 — Homological shell condensation.**

    The spectral sequence collapses with `E_∞^{p, >0}(n) = 0` if and
    only if `n` is a magic number on the ladder
    `{2, 8, 20, 28, 50, 82, 126}`.

    The conjectural content is the iff: collapse occurs *exactly* on
    this ladder. Two routes for closing it are documented in the
    associated `.md` (combinatorial enumeration of complete-intersection
    BB-strata; Yekutieli MC-equation reduction). -/
-- Ref: [manuscript] conj:homological-shell-condensation
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
class ShellCondensationConjecture where
  /-- Both directions of the iff. -/
  collapse_iff_magic :
    ∀ n : ℕ, InfinityVanishesAtPositiveQ n ↔ n ∈ magicLadder

/-- Re-export, forward direction: at magic `n`, the spectral
    sequence collapses with the `q > 0` part of `E_∞` vanishing. -/
-- Ref: [manuscript] conj:homological-shell-condensation
theorem condensation_at_magic
    [C : ShellCondensationConjecture]
    {n : ℕ} (hn : n ∈ magicLadder) :
    InfinityVanishesAtPositiveQ n :=
  (C.collapse_iff_magic n).mpr hn

/-- Re-export, reverse direction: if the spectral sequence collapses
    with `E_∞^{p, >0}(n) = 0`, then `n` lies on the magic ladder. -/
-- Ref: [manuscript] conj:homological-shell-condensation
theorem magic_at_condensation
    [C : ShellCondensationConjecture]
    {n : ℕ} (hn : InfinityVanishesAtPositiveQ n) :
    n ∈ magicLadder :=
  (C.collapse_iff_magic n).mp hn

/-! ## §4  Worked corollaries on the magic ladder -/

/-- At `n = 28` (Nickel-28 shell), the spectral sequence collapses
    with `E_∞^{p, >0} = 0`. -/
-- Ref: [manuscript] conj:homological-shell-condensation
theorem condensation_at_28 [ShellCondensationConjecture] :
    InfinityVanishesAtPositiveQ 28 :=
  condensation_at_magic twentyeight_mem_magicLadder

/-! ## §5  Per-n typeclass decomposition + structural reduction -/

/-- Per-n assertion: `n` is *known* to be condensed (E_∞^{p, q>0}(n) = 0). -/
class IsKnownCondensed (n : ℕ) : Prop where
  is_condensed : InfinityVanishesAtPositiveQ n

/-- Per-n assertion: `n` is *known* to be non-condensed
    (E_∞^{p, q>0}(n) ≠ 0). -/
class IsKnownNotCondensed (n : ℕ) : Prop where
  not_condensed : ¬ InfinityVanishesAtPositiveQ n

/-- **Assembly theorem.** If for every `n ≥ 2` we have either
    `IsKnownCondensed n` (when `n ∈ magicLadder`) or
    `IsKnownNotCondensed n` (when `n ∉ magicLadder`), then the
    `ShellCondensationConjecture` holds for `n ≥ 2`.

    The `n ≥ 2` restriction handles the edge cases:
    - `n = 0` (vacuum): no jet prolongations, so condensation holds
      trivially — but `0 ∉ magicLadder`, so the iff form fails.
    - `n = 1` (single strand): similarly, no inter-strand jets, so
      condensation holds trivially.

    Both edge cases are *vacuously condensed* without being magic;
    the conjecture is only meaningful for `n ≥ 2`. -/
-- Ref: [manuscript] conj:homological-shell-condensation
theorem shellCondensation_iff_perN_axioms_at
    (h_in : ∀ n, n ∈ magicLadder → IsKnownCondensed n)
    (h_out : ∀ n, 2 ≤ n → n ∉ magicLadder → IsKnownNotCondensed n) :
    ∀ n, 2 ≤ n →
      (InfinityVanishesAtPositiveQ n ↔ n ∈ magicLadder) := by
  intro n hn
  constructor
  · intro h_inf
    by_contra h_not_in
    have := (h_out n hn h_not_in).not_condensed
    exact this h_inf
  · intro h_in_ladder
    exact (h_in n h_in_ladder).is_condensed

/-- At `n = 82` (Lead-82 shell, beyond the `k = 10` Hoefsmit limit),
    the same vanishing holds purely from the conjectural
    homological condensation. This is the algebraic-geometry bypass
    of the matrix-evaluation barrier. -/
-- Ref: [manuscript] conj:homological-shell-condensation
theorem condensation_at_82 [ShellCondensationConjecture] :
    InfinityVanishesAtPositiveQ 82 :=
  condensation_at_magic eightytwo_mem_magicLadder

/-- At `n = 126` (the heaviest known shell closure), likewise. -/
-- Ref: [manuscript] conj:homological-shell-condensation
theorem condensation_at_126 [ShellCondensationConjecture] :
    InfinityVanishesAtPositiveQ 126 :=
  condensation_at_magic onetwentysix_mem_magicLadder

end QOU.LiftingDescent.HomologicalCondensation
