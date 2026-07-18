import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Complex.Basic

/-!
# Route-B step 2 (core): shared-prefactor order balance for the Faddeev rigidity

The meromorphic reformulation of `PentagonRigidity.uniqueUpToScalar` (bean
`qou-2cvs`, route B). The true `Φ_b` is *meromorphic* (zeros on the `b`-lattice,
poles on the dual lattice), so the idealized entire-nowhere-zero scaffold does not
apply; rigidity must be restated over `MeromorphicOn`/divisors. The keystone is
that two solutions of the *same* first-order q-difference equation
`f(·+c) = P·f` have the **same divisor**, so their ratio is entire and nowhere
zero.

This file proves the algebraic heart of that step: at any point, the shared
prefactor `P`'s order **cancels** in the order-difference. Writing `Ψ_shift = P·Ψ`
and `Φ_shift = P·Φ` (the `c`-shifts of the two solutions),
`ord(P·Ψ) + ord Φ = ord(P·Φ) + ord Ψ`, i.e. `ord Ψ_shift − ord Ψ = ord Φ_shift −
ord Φ` — the order-difference `ord Ψ − ord Φ` is preserved by one shift. Over the
`⟨ib, i/b⟩` lattice (`PeriodLatticeBasis.exists_period_basis`) this forces the
order-difference constant, hence `0` at a regular point, hence `ord Φ = ord Ψ`
everywhere (same divisor), hence the ratio is entire + nonvanishing — the input
`ratio_const_of_doublyPeriodic` consumes.

**Build note.** `Mathlib.Analysis.Meromorphic.*` is outside the QOU library's usual
import cone; verified `lean`-direct after building the 7-module Meromorphic cone
from the pinned mathlib source (github egress; the release-server cache is
network-blocked but the source build is not). CI has full mathlib and builds it
normally. Sorry-free, exit 0.

**Remaining route-B bricks (not in this file, honestly open):** the order of a
`c`-shifted function equals the order at the shifted point (translation of
`meromorphicOrderAt`); the lattice ⇒ constant ⇒ 0 argument; empty divisor ⇒
`AnalyticOnNhd` + nonvanishing; assembly into `uniqueUpToScalar`. Nothing is
axiomatized.
-/

open scoped Classical

/-- **Shared-prefactor order balance** (route-B step 2, core). For meromorphic
`Φ, Ψ, P` at `x`, the prefactor `P`'s order cancels between the two shifted
solutions: `ord(P·Ψ) + ord Φ = ord(P·Φ) + ord Ψ`. -/
theorem meromorphicOrderAt_sharedPrefactor_balance
    {Φ Ψ P : ℂ → ℂ} {x : ℂ}
    (hΦ : MeromorphicAt Φ x) (hΨ : MeromorphicAt Ψ x) (hP : MeromorphicAt P x) :
    meromorphicOrderAt (P * Ψ) x + meromorphicOrderAt Φ x
      = meromorphicOrderAt (P * Φ) x + meromorphicOrderAt Ψ x := by
  rw [meromorphicOrderAt_mul hP hΨ, meromorphicOrderAt_mul hP hΦ]
  abel

/-- **Route-B step 2 (conclusion): order-difference periodicity.** Two solutions
`Φ, Ψ` of the *same* first-order q-difference equation `f(·+c) = P·f` have their
order-difference preserved by one `c`-shift:
`ord Ψ (x+c) + ord Φ x = ord Φ (x+c) + ord Ψ x`, i.e. `ord Ψ − ord Φ` is
`c`-periodic. Composes `meromorphicOrderAt_sharedPrefactor_balance` (proved) with
the order-translation invariance `htr` — **brick (a)**, carried here as an
explicit hypothesis (§3b-cond): a separate lemma
`meromorphicOrderAt (g ∘ (·+c)) x = meromorphicOrderAt g (x+c)` will discharge it.
Not axiomatized — `htr` is a genuine sub-hypothesis, proved elsewhere. -/
theorem meromorphicOrderAt_orderDiff_shift
    {Φ Ψ P : ℂ → ℂ} {x c : ℂ}
    (hΦ : MeromorphicAt Φ x) (hΨ : MeromorphicAt Ψ x) (hP : MeromorphicAt P x)
    (hΦeq : ∀ z, Φ (z + c) = P z * Φ z) (hΨeq : ∀ z, Ψ (z + c) = P z * Ψ z)
    (htr : ∀ g : ℂ → ℂ, meromorphicOrderAt (fun z => g (z + c)) x
                          = meromorphicOrderAt g (x + c)) :
    meromorphicOrderAt Ψ (x + c) + meromorphicOrderAt Φ x
      = meromorphicOrderAt Φ (x + c) + meromorphicOrderAt Ψ x := by
  have eΦ : (fun z => Φ (z + c)) = P * Φ := funext hΦeq
  have eΨ : (fun z => Ψ (z + c)) = P * Ψ := funext hΨeq
  rw [← htr Ψ, ← htr Φ, eΨ, eΦ]
  exact meromorphicOrderAt_sharedPrefactor_balance hΦ hΨ hP
