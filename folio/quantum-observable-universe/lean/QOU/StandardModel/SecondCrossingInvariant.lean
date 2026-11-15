import Mathlib.CategoryTheory.Groupoid
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
# The second crossing invariant for the hypercharge gap (formalize-first scaffold)

The `HyperchargeInvariant` conjecture (2026-06-02 audit, PR #1683; Lean
`sm-hypercharge-invariant.lean`) reduced the electroweak `U(1)` gap to a
single precise object: a **second invariant on the state groupoid,
independent of the writhe `w`**, from which the weak hypercharge `Y` is
read via the Gell-Mann–Nishijima relation `Q = I₃ + Y/2`.  The writhe was
DERIVED to carry `I₃` (sign+ratio across the nucleon doublet, `c = 1/2`
fixed by `def:coulomb-charge`) but FALSIFIED as a `Y`-map (proton and
neutron share `Y = +1` while their writhes differ).

This file (branch `claude/hypercharge-second-invariant-2026-08-02`) is the
formalize-first artifact for the *identity* of that second invariant.  The
candidate identified by the corpus-grep survey is the **Milnor triple
linking number `μ̄₁₂₃`** of the three color-tube components:

* The canonical baryon is the **Borromean link `𝓑₃`** of three color-tube
  unknots (`borromean-quark.md`): "no two components link, yet all three
  together remain inseparable" — i.e. *all pairwise linkings vanish* while
  the *triple* invariant is nonzero.  The framework explicitly rejects the
  Hopf link (pairwise linking) because it would permit diquarks.
* On this baryon the intra-braid **writhe is `0`** (`β_Bor = (σ₁⁻¹σ₂)³`,
  three `+` and three `−` crossings — s5-so3 audit 2026-06-01) and every
  pairwise linking is `0`.  So **every degree-1 crossing invariant**
  (writhe, self-linking, framing phase `q^{w·c}`, pairwise linking)
  *vanishes on the baryon* and cannot supply `Y`.
* The first non-vanishing finite-type invariant of a 3-component Brunnian
  (Borromean) link is `±μ̄₁₂₃ = ±1` at degree `2(A−1)` (the existing
  `QOU.KnotTheory.Vassiliev.BrunnianVassilievBridge` conjecture class;
  Habegger–Masbaum 2000).  Because the pairwise linkings vanish, `μ̄₁₂₃`
  has **no indeterminacy** (Milnor 1954: well-defined mod gcd of pairwise
  linkings; here the gcd is `0`), so it is an unambiguous integer on the
  baryon.  It equals the **baryon number `B`** (`+1` for the confined
  triple, `0` for a 2-tube meson), and on the non-strange sector `Y = B`.

This file states — as a **content-bearing primary conjecture class with no
instance** (§3b-tax) — that such a `Y = a·w + b·B` (ℤ-linear in the writhe
and the second invariant, `b ≠ 0`) realizes Gell-Mann–Nishijima and does
not factor through the writhe; and it **proves, sorry-free**, the abstract
reductions that make this the right shape: (i) any invariant not factoring
through `w` supplies the writhe-degenerate separating pair the conjecture
needs, (ii) the concrete baryon/vacuum pair (both `w = 0`, `B = 1` vs `0`)
is such a pair, and (iii) on the writhe-`0` baryon sector `Y = 2Q` — the
writhe contributes nothing, so `Y` is carried entirely by the second
invariant.

**Symbol disambiguation — two `μ̄`s in the corpus (do not conflate).**
`QOU.MassTheory.MilnorExactCoefficient` (landed upstream) carries
`mubarMeasured A = (3/4)·(−2)^{A−3}`, whose `A = 3` value is `3/4`, *not*
`±1`.  That object is the **trace-normalised leading coefficient** of the
A-component Brunnian Markov-trace deficit `1 − τ_A`, empirically extracted
and explicitly *not* proved equal to the topological invariant (its own
docstring: "that is the open Milnor μ̄(12…A) content, Route A").  The `μ̄₁₂₃`
in *this* file is the **topological** Milnor triple linking number, which is
`±1` on the Borromean rings.  Same glyph, different objects and different
normalisations — per AGENTS.md §"Attributes do not transfer across
overloaded symbols", no property of either transfers to the other.

Relevant upstream negative: `cyclic_trace_kills_iterCommTower` proves a
cyclic (Markov) trace annihilates the Lie iterated-commutator tower, so the
leading coefficient is *not* recoverable from that tower via a trace.  This
does not bear on the conjecture below — nothing here extracts `μ̄₁₂₃` from a
trace — but it is why the exact-order law remains open upstream.

**Honesty scope (AGENTS.md anti-laundering).** No instance is provided and
no coefficient is fitted.  The class is OPEN.  The physics claim
`μ̄₁₂₃ = B = Y` is a *conjecture*: `Y = B` closes only the non-strange
sector, and the full `Y = B + S` (strangeness) and the relative `U(1)`
coupling normalization that `sin²θ_W` needs both inherit the open
SU(3)-flavor problem.  What is *proved* here is only the abstract
group-theoretic reduction, not the identification.

## References

- [leitner2026] Appendix: Toward the Standard Model; hypercharge audit
  `docs/audits/2026-06-02-u1-hypercharge-assignment.md`.
- [milnor1954] μ̄ triple-linking invariant; indeterminacy mod gcd of
  pairwise linkings.
- [habegger-masbaum2000] Milnor = leading Vassiliev for Brunnian links.
-/

namespace QOU.StandardModel

open CategoryTheory

universe u v

/-- **Reduction lemma (proved).** If a candidate invariant `B` does *not*
factor through the writhe `w`, then there is a **writhe-degenerate pair**
of states — equal writhe, distinct `B` — exactly the object the
hypercharge conjecture requires.  This is the constructive converse of
`HyperchargeInvariant.exists_writhe_degenerate_pair`: a genuine second
invariant automatically discharges the non-factorization clause. -/
theorem secondInvariant_gives_separating_pair {S : Type*}
    (B : S → ℚ) (w : S → ℤ)
    (hB : ¬ ∃ f : ℤ → ℚ, ∀ X, B X = f (w X)) :
    ∃ X X' : S, w X = w X' ∧ B X ≠ B X' := by
  by_contra h
  push_neg at h
  -- `h : ∀ X X', w X = w X' → B X = B X'`; build the factoring map by choice.
  apply hB
  classical
  refine ⟨fun z => if hz : ∃ X, w X = z then B hz.choose else 0, fun X => ?_⟩
  have hex : ∃ X', w X' = w X := ⟨X, rfl⟩
  simp only [dif_pos hex]
  exact (h hex.choose X hex.choose_spec).symm

/-- **Concrete Borromean/vacuum separating pair (proved).** The canonical
baryon (`w = 0`, `B = 1`: Borromean triple linking `μ̄₁₂₃ = 1`) and the
vacuum/meson (`w = 0`, `B = 0`: no triple) are a writhe-degenerate pair
separated by the second invariant.  This realizes, with the framework's own
objects, the pair whose *existence* the hypercharge conjecture asserts. -/
theorem baryon_vacuum_separating {S : Type*}
    (w : S → ℤ) (B : S → ℚ) (baryon vacuum : S)
    (hbw : w baryon = 0) (hvw : w vacuum = 0)
    (hbB : B baryon = 1) (hvB : B vacuum = 0) :
    w baryon = w vacuum ∧ B baryon ≠ B vacuum := by
  refine ⟨by rw [hbw, hvw], ?_⟩
  rw [hbB, hvB]
  norm_num

/-- **Writhe-`0` sector lemma (proved).** On any state whose writhe is `0`
(the Borromean baryon, per the s5-so3 audit), the writhe reading
`I₃ = w/2` vanishes, so Gell-Mann–Nishijima forces `Y = 2Q`: the *entire*
hypercharge is carried by the second invariant, not the writhe.  This is
the sharp reason the writhe alone cannot supply `Y` on the baryon.

Stated in **cleared (division-free)** form -- `2·I₃ = w` and
`2Q = 2I₃ + Y` rather than `I₃ = w/2` and `Q = I₃ + Y/2` -- so it holds over
an arbitrary `CommRing R` with **no characteristic hypothesis**.  Note the
proof never needs `I₃ X = 0`, only `2·I₃ X = 0`, which is why no invertible
`2` is required.  Matches the formulation in
`QOU/StandardModel/HyperchargeBatteryReduction.lean`. -/
theorem writheZero_Y_eq_twoQ {S : Type*} {R : Type*} [CommRing R]
    (w : S → ℤ) (I3 Q Y : S → R)
    (hI3 : ∀ X, 2 * I3 X = (w X : R))
    (hgmn : ∀ X, 2 * Q X = 2 * I3 X + Y X)
    (X : S) (hw : w X = 0) :
    Y X = 2 * Q X := by
  have h1 : 2 * I3 X = 0 := by rw [hI3 X, hw]; norm_num
  have h2 := hgmn X
  rw [h1, zero_add] at h2
  exact h2.symm

/-- The rational statement is recovered from the cleared one: over `ℚ` the
familiar `I₃ = w/2`, `Q = I₃ + Y/2` hypotheses imply the cleared ones, so
no content is lost by generalising. -/
theorem writheZero_Y_eq_twoQ_rat {S : Type*}
    (w : S → ℤ) (I3 Q Y : S → ℚ)
    (hI3 : ∀ X, I3 X = (w X : ℚ) / 2)
    (hgmn : ∀ X, Q X = I3 X + Y X / 2)
    (X : S) (hw : w X = 0) :
    Y X = 2 * Q X :=
  writheZero_Y_eq_twoQ w I3 Q Y
    (fun X => by rw [hI3 X]; ring)
    (fun X => by rw [hgmn X]; ring)
    X hw

/-- **Conjecture class (primary): the second crossing invariant.**  Over a
groupoid `S` of topological states with a derived charge `Q`, the writhe
reading `I₃` and the writhe `w`, there is an integer-valued gauge-invariant
**second invariant `B`** (intended: the Milnor triple linking `μ̄₁₂₃` of the
three color-tube components) and integers `a, b` with `b ≠ 0` such that the
weak hypercharge

  `Y = a·w + b·B`

is a genuine ℤ-linear combination (the `b·B` piece is present) realizing
Gell-Mann–Nishijima `Q = I₃ + Y/2`, and — the sharp clause — `Y` does
**not** factor through the writhe.

Intended instantiation: `S` = knot-state groupoid; `Q = w/2` the Coulomb
charge, `I₃ = w/2` the writhe reading (both 2026-06-02 audit), `B = μ̄₁₂₃`
the Borromean baryon-number invariant, `a = 0`, `b = 1` (so `Y = B`) on the
non-strange sector.  **Open:** no instance — the identification `B = μ̄₁₂₃`,
its GMN normalization, and the strangeness/`sin²θ_W` extension are not
derived. -/
class SecondCrossingInvariant (S : Type u) [Groupoid.{v} S]
    (Q I3 : S → ℚ) (w : S → ℤ) : Prop where
  /-- There is an integer-valued gauge-invariant second invariant `B`
  (intended: Milnor `μ̄₁₂₃`, an integer because the Borromean pairwise
  linkings vanish) and integers `a, b` with `b ≠ 0` such that
  `Y = a·w + b·B` realizes Gell-Mann–Nishijima `Q = I₃ + Y/2`, with `I₃`
  the writhe reading `w/2`, and does **not** factor through the writhe. -/
  exists_second_invariant :
    ∃ (B : S → ℤ) (a b : ℤ),
      b ≠ 0 ∧
      (∀ ⦃X X' : S⦄, (X ⟶ X') → B X = B X') ∧
      (∀ X, I3 X = (w X : ℚ) / 2) ∧
      (∀ X, Q X = I3 X + ((a * w X + b * B X : ℤ) : ℚ) / 2) ∧
      ¬ ∃ f : ℤ → ℚ, ∀ X, ((a * w X + b * B X : ℤ) : ℚ) = f (w X)

/-- **(Conditional on `SecondCrossingInvariant`.)** Any second crossing
invariant forces a writhe-degenerate pair separated by the hypercharge
`Y = a·w + b·B`.  Proved from the reduction lemma; the only unproved input
is the class instance (§3b-cond).  This checks the conjecture is *coherent*:
its hypotheses genuinely deliver the object the `HyperchargeInvariant`
conjecture demands. -/
theorem SecondCrossingInvariant.exists_writhe_degenerate_pair
    {S : Type u} [Groupoid.{v} S] {Q I3 : S → ℚ} {w : S → ℤ}
    [inst : SecondCrossingInvariant S Q I3 w] :
    ∃ (Y : S → ℚ) (X X' : S), w X = w X' ∧ Y X ≠ Y X' := by
  obtain ⟨B, a, b, _, _, _, _, hnf⟩ := inst.exists_second_invariant
  exact ⟨fun X => ((a * w X + b * B X : ℤ) : ℚ),
    secondInvariant_gives_separating_pair _ w hnf⟩

end QOU.StandardModel
