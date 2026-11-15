import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Complex.Basic

/-!
# Route-B step 2: order-difference periodicity for the Faddeev rigidity

The meromorphic reformulation of `PentagonRigidity.uniqueUpToScalar` (bean
`qou-2cvs`, route B). The true `Φ_b` is *meromorphic* (zeros on the `b`-lattice,
poles on the dual lattice), so the idealized entire-nowhere-zero scaffold does not
apply; rigidity must be restated over `MeromorphicOn`/divisors. The keystone is
that two solutions of the *same* first-order q-difference equation `f(·+c) = P·f`
have the **same divisor**, so their ratio is entire and nowhere zero.

This file proves **route-B step 2 in full** (sorry-free):

* `meromorphicOrderAt_comp_add` — **brick (a)**, translation invariance of the
  meromorphic order: `ord (g∘(·+c)) x = ord g (x+c)`. Proved from the
  `eq_top_iff` / `eq_int_iff` characterizations, transporting the local
  representation across the `z ↦ z+c` homeomorphism (`AnalyticAt.comp`,
  punctured-nhds `Tendsto`). No longer a Mathlib gap.
* `meromorphicOrderAt_sharedPrefactor_balance` — the prefactor `P`'s order
  cancels: `ord(P·Ψ) + ord Φ = ord(P·Φ) + ord Ψ`.
* `meromorphicOrderAt_orderDiff_periodic` — **the step-2 conclusion,
  unconditional**: two solutions of the same equation `f(·+c)=P·f` have
  `ord Ψ − ord Φ` preserved by one `c`-shift. Brick (a) discharges the
  translation input; nothing is assumed.

Applied to both quasi-periods `ib, i/b`, this makes the order-difference
`ord Ψ − ord Φ` **doubly periodic** — equivalently, the divisor of the ratio
`r = Ψ/Φ` is `⟨ib, i/b⟩`-periodic (`r` is `c`-periodic for each `c`, so `r` is
an **elliptic function**).

**Honest scope correction (2026-07-19).** Double periodicity does **not** force
`ord Φ = ord Ψ`. A doubly-periodic meromorphic ratio can be a *nonconstant*
elliptic function (Weierstrass ℘), so the two solutions need **not** share a
divisor from the equations alone — there is genuine elliptic freedom. Hence
"same divisor ⇒ ratio entire" is an **independent analytic input** (the
Φ_b-specific characterization pinning the ratio to have no elliptic freedom),
NOT a consequence of steps 1–2. Route B closes `uniqueUpToScalar` only with that
extra input (≡ brick (c)'s premise); step 2 supplies the periodicity, not the
constancy.

**Build note.** `Mathlib.Analysis.Meromorphic.*` is outside the QOU library's
usual import cone; verified `lean`-direct after building the Meromorphic cone from
the pinned mathlib source (github egress; the release-server cache is
network-blocked but the source build is not). CI has full mathlib. Sorry-free.

**Remaining route-B bricks (honest, not axiomatized):** lattice ⇒ order-diff
`0` ⇒ same divisor; empty divisor ⇒ ratio `AnalyticOnNhd` + nonvanishing;
assembly into `uniqueUpToScalar`.
-/

open Filter Topology
open scoped Classical

/-- Translation `z ↦ z + c` tends within punctured neighborhoods:
`𝓝[≠] x → 𝓝[≠] (x + c)`. -/
theorem tendsto_add_right_nhdsWithin_ne (x c : ℂ) :
    Tendsto (fun z => z + c) (𝓝[≠] x) (𝓝[≠] (x + c)) := by
  rw [tendsto_nhdsWithin_iff]
  refine ⟨((continuous_id.add continuous_const).continuousAt).mono_left nhdsWithin_le_nhds, ?_⟩
  filter_upwards [self_mem_nhdsWithin] with z hz
  simp only [Set.mem_compl_iff, Set.mem_singleton_iff] at hz ⊢
  exact fun h => hz (add_right_cancel h)

/-- Meromorphy is preserved by the translation `z ↦ z + c`. -/
theorem meromorphicAt_comp_add {g : ℂ → ℂ} {x c : ℂ}
    (hg : MeromorphicAt g (x + c)) : MeromorphicAt (fun z => g (z + c)) x := by
  obtain ⟨n, hn⟩ := hg
  refine ⟨n, ?_⟩
  have hshift : AnalyticAt ℂ (fun z : ℂ => z + c) x := by fun_prop
  have hcomp : AnalyticAt ℂ (fun z : ℂ => ((z + c) - (x + c)) ^ n • g (z + c)) x :=
    AnalyticAt.comp (g := fun w : ℂ => (w - (x + c)) ^ n • g w)
      (f := fun z : ℂ => z + c) hn hshift
  have hfun : (fun z : ℂ => (z - x) ^ n • g (z + c))
      = (fun z : ℂ => ((z + c) - (x + c)) ^ n • g (z + c)) := by
    funext z; congr 2; ring
  rw [hfun]
  exact hcomp

/-- Meromorphy transported both ways under `z ↦ z + c`. -/
theorem meromorphicAt_comp_add_iff {g : ℂ → ℂ} {x c : ℂ} :
    MeromorphicAt (fun z => g (z + c)) x ↔ MeromorphicAt g (x + c) := by
  constructor
  · intro hF
    have h := meromorphicAt_comp_add (g := fun z => g (z + c)) (x := x + c) (c := -c)
      (by simpa using hF)
    simpa using h
  · exact meromorphicAt_comp_add

/-- **Brick (a): translation invariance of the meromorphic order.**
`meromorphicOrderAt (g ∘ (·+c)) x = meromorphicOrderAt g (x+c)`. -/
theorem meromorphicOrderAt_comp_add (g : ℂ → ℂ) (x c : ℂ) :
    meromorphicOrderAt (fun z => g (z + c)) x = meromorphicOrderAt g (x + c) := by
  by_cases hg : MeromorphicAt g (x + c)
  · have hFm : MeromorphicAt (fun z => g (z + c)) x := meromorphicAt_comp_add hg
    rcases eq_or_ne (meromorphicOrderAt g (x + c)) ⊤ with htop | hfin
    · rw [htop, meromorphicOrderAt_eq_top_iff]
      rw [meromorphicOrderAt_eq_top_iff] at htop
      exact (tendsto_add_right_nhdsWithin_ne x c).eventually htop
    · obtain ⟨n, hn⟩ := WithTop.ne_top_iff_exists.mp hfin
      rw [← hn, meromorphicOrderAt_eq_int_iff hFm]
      obtain ⟨G, hGan, hGne, hGeq⟩ := (meromorphicOrderAt_eq_int_iff hg).mp hn.symm
      refine ⟨fun z => G (z + c), ?_, ?_, ?_⟩
      · exact AnalyticAt.comp (g := G) (f := fun z => z + c) hGan (by fun_prop)
      · exact hGne
      · have h2 := (tendsto_add_right_nhdsWithin_ne x c).eventually hGeq
        filter_upwards [h2] with z hz
        show g (z + c) = (z - x) ^ n • G (z + c)
        rw [hz]
        have hb : (z + c) - (x + c) = z - x := by ring
        rw [hb]
  · rw [meromorphicOrderAt_of_not_meromorphicAt (mt meromorphicAt_comp_add_iff.mp hg),
        meromorphicOrderAt_of_not_meromorphicAt hg]

/-- **Shared-prefactor order balance** (route-B step 2). For meromorphic
`Φ, Ψ, P` at `x`, the prefactor `P`'s order cancels between the two shifted
solutions: `ord(P·Ψ) + ord Φ = ord(P·Φ) + ord Ψ`. -/
theorem meromorphicOrderAt_sharedPrefactor_balance
    {Φ Ψ P : ℂ → ℂ} {x : ℂ}
    (hΦ : MeromorphicAt Φ x) (hΨ : MeromorphicAt Ψ x) (hP : MeromorphicAt P x) :
    meromorphicOrderAt (P * Ψ) x + meromorphicOrderAt Φ x
      = meromorphicOrderAt (P * Φ) x + meromorphicOrderAt Ψ x := by
  rw [meromorphicOrderAt_mul hP hΨ, meromorphicOrderAt_mul hP hΦ]
  abel

/-- **Route-B step 2 (conclusion, UNCONDITIONAL): order-difference periodicity.**
Two solutions `Φ, Ψ` of the *same* first-order q-difference equation `f(·+c) = P·f`
have their order-difference preserved by one `c`-shift:
`ord Ψ (x+c) + ord Φ x = ord Φ (x+c) + ord Ψ x`. Discharges the translation input
via brick (a) `meromorphicOrderAt_comp_add`; nothing is axiomatized. -/
theorem meromorphicOrderAt_orderDiff_periodic
    {Φ Ψ P : ℂ → ℂ} {x c : ℂ}
    (hΦ : MeromorphicAt Φ x) (hΨ : MeromorphicAt Ψ x) (hP : MeromorphicAt P x)
    (hΦeq : ∀ z, Φ (z + c) = P z * Φ z) (hΨeq : ∀ z, Ψ (z + c) = P z * Ψ z) :
    meromorphicOrderAt Ψ (x + c) + meromorphicOrderAt Φ x
      = meromorphicOrderAt Φ (x + c) + meromorphicOrderAt Ψ x := by
  have eΦ : (fun z => Φ (z + c)) = P * Φ := funext hΦeq
  have eΨ : (fun z => Ψ (z + c)) = P * Ψ := funext hΨeq
  rw [← meromorphicOrderAt_comp_add Ψ x c, ← meromorphicOrderAt_comp_add Φ x c, eΨ, eΦ]
  exact meromorphicOrderAt_sharedPrefactor_balance hΦ hΨ hP
