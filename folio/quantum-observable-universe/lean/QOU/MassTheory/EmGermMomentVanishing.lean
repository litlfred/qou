import Mathlib.Tactic

/-!
# QOU.MassTheory.EmGermMomentVanishing — where the EM germ moment vanishes, and where it blows up

Bean `qou-rrgk` (the *germ-viability* bean — see the ID note below).

The 2026-08-29 germ-viability probe
(`computations/alpha_em_germ_viability_probe.py`, audit
`docs/audits/2026-08-29-alpha-em-germ-viability-live.md`) computed the EM-singlet
moment of the germ curvature `F_q = [δq₁, δq₂]` in the fundamental
representation and found the closed form

  `m_F = qTr(E · F_q · E) / qTr(E) = −(q² − 1)/(q² + 1) = −h/[2]_q`,

with `h = q − q⁻¹` bar-odd and `[2]_q = q + q⁻¹` bar-even. That result is a
**probe computation and is taken here as given** — this file does not re-derive
it from the Hecke representation, and nothing below should be cited as doing so
("conditional-proved ≠ premise-established"). What this file adds is the
structure of the closed form, which is where its meaning lives.

## The point: one formula, both distinguished loci

A bar-odd numerator over a bar-even denominator has two special loci, and the
corpus already cares about **both** of them for separate reasons:

* **`q² = 1`** — the moment **vanishes** (`emMoment_eq_zero_iff`). This is the
  classical / self-dual point, and it is exactly the locus where the braiding
  becomes symmetric: `QOU.MassTheory.TraceSignFlipRegime.trace_sign_flip_iff_symmetric`
  gives `tr σ⁻¹ = tr σ ↔ q² = 1` from the same factor `h`. So germ sterility in
  the EM singlet channel and symmetric braiding are **the same condition**
  (`sterile_iff_bar_fixed`), not two coincidences. The germ is non-sterile
  *because* the braiding is non-symmetric.
* **`q² = −1`** — the normalisation `[2]_q` **degenerates**
  (`qInt2_eq_zero_iff`), so the moment is not defined there. The measure wall's
  stated obstruction (`docs/audits/2026-08-02-moc-gauss-manin-not-derivable.md`,
  epic `08a2`) is that *"the discrete `q = i` F-construction shadow supplies no
  germ"* — and `q = i` is a root of `q² = −1`.

  **Stated as a coincidence of loci, not as a derivation.** That `[2]_q`
  vanishes at `q = i` is the theorem; that this *is why* the discrete shadow
  supplies no germ is an interpretation this file does not prove and does not
  claim. It is recorded because the two loci agreeing is checkable and was not
  previously written down.

## Scope

Everything is algebraic over a `Field R` — no ordering, no `Real.sqrt`, no
archimedean construct (§7c), so the statements hold at the categorical/fibre
level and specialise to `ℝ` or `ℂ` on demand. Nothing here derives the measure
`1/(8π)`, which stays phase-4; nothing is wired.

## A note on the bean ID

Two distinct beans carry the ID `qou-rrgk` on `main`:
`qou-rrgk--germ-viability-probe-...` (this one) and
`qou-rrgk--drain-329-stale-q-0-anchors-...`. `beans show qou-rrgk` resolves to
the *drain* bean, so the germ bean is unreachable from the CLI by ID. Cite it by
filename.

-- Ref: [leitner2026] rem:two-observer-parallelogram
-/

namespace QOU.MassTheory.EmGermMomentVanishing

variable {R : Type*} [Field R]

/-- The bar-odd generator `h = q − q⁻¹`. Vanishes exactly on the bar-fixed
locus `q² = 1`. -/
-- NAMED `barOddGen`, NOT `hbar` (bean `qou-u87j`). Everywhere else in the
-- corpus `hbar` / `hbar_q` / `hbarQ` is the quantum Planck constant
-- ℏ_q = 1 - q⁻¹. This is the Hecke structure constant of AGENTS.md §7a,
-- q - q⁻¹ — a different quantity, 2.11x larger at the substrate anchor
-- (0.2090602988 against 0.0990817160 at q₀ = 1.1099785827513808). The
-- docstring always said `h`; only the identifier read as ℏ.
def barOddGen (q : R) : R := q - q⁻¹

/-- The bar-even quantum integer `[2]_q = q + q⁻¹`. -/
def qInt2 (q : R) : R := q + q⁻¹

/-- The EM-singlet moment of the germ curvature, in the closed form the probe
measured: `m_F = −h/[2]_q`. -/
def emMoment (q : R) : R := -(barOddGen q / qInt2 q)

/-! ### The two spellings agree -/

/-- `h = (q² − 1)/q`. -/
theorem barOddGen_eq (q : R) (hq : q ≠ 0) : barOddGen q = (q ^ 2 - 1) / q := by
  simp only [barOddGen]; field_simp

/-- `[2]_q = (q² + 1)/q`. -/
theorem qInt2_eq (q : R) (hq : q ≠ 0) : qInt2 q = (q ^ 2 + 1) / q := by
  simp only [qInt2]; field_simp

/-- The audit's two spellings of the moment are the same object:
`−h/[2]_q = −(q² − 1)/(q² + 1)`. -/
theorem emMoment_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    emMoment q = -((q ^ 2 - 1) / (q ^ 2 + 1)) := by
  have hq2 : qInt2 q ≠ 0 := by
    rw [qInt2_eq q hq]; exact div_ne_zero h2 hq
  rw [emMoment, neg_inj, div_eq_div_iff hq2 h2]
  simp only [barOddGen, qInt2]
  field_simp

/-! ### Bar-oddness -/

/-- `h` is bar-odd: `h(q⁻¹) = −h(q)`. -/
theorem barOddGen_inv (q : R) : barOddGen q⁻¹ = -barOddGen q := by
  simp [barOddGen]

/-- `[2]_q` is bar-even: `[2]_{q⁻¹} = [2]_q`. -/
theorem qInt2_inv (q : R) : qInt2 q⁻¹ = qInt2 q := by
  simp [qInt2, add_comm]

/-- **The moment is bar-odd**: `m_F(q⁻¹) = −m_F(q)`. Bar-odd over bar-even is
bar-odd, so the moment reverses under `q ↦ q⁻¹` — the signature of a genuine
`q`-motion rather than a static invariant. -/
theorem emMoment_bar_odd (q : R) : emMoment q⁻¹ = -emMoment q := by
  simp [emMoment, barOddGen_inv, qInt2_inv, neg_div]

/-! ### Locus 1 — sterility at the self-dual point -/

/-- `h = 0` exactly on the bar-fixed locus. -/
theorem barOddGen_eq_zero_iff (q : R) (hq : q ≠ 0) : barOddGen q = 0 ↔ q ^ 2 = 1 := by
  rw [barOddGen_eq q hq, div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · linear_combination h
    · exact absurd h hq
  · intro h; left; linear_combination h

/-- **The moment vanishes exactly at `q² = 1`.** Away from the degenerate locus
`[2]_q = 0`, the germ's EM-singlet channel is sterile precisely at the
classical / self-dual point and nowhere else — so non-sterility is generic, not
a lucky sample point. -/
theorem emMoment_eq_zero_iff (q : R) (hq : q ≠ 0) (h2 : qInt2 q ≠ 0) :
    emMoment q = 0 ↔ q ^ 2 = 1 := by
  rw [emMoment, neg_eq_zero, div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · exact (barOddGen_eq_zero_iff q hq).mp h
    · exact absurd h h2
  · intro h; left; exact (barOddGen_eq_zero_iff q hq).mpr h

/-- **Sterility and symmetric braiding are the same condition.** The moment
vanishes iff `h = 0`, which is the very factor whose vanishing makes
`tr σ⁻¹ = tr σ` in `TraceSignFlipRegime.trace_sign_flip_iff_symmetric`. So the
EM germ is non-sterile *because* the braiding is non-symmetric — the two facts
are one fact, and the deuteron's single-generator sterility is a genuinely
different mechanism (abelian transport), not this one. -/
theorem sterile_iff_bar_fixed (q : R) (hq : q ≠ 0) (h2 : qInt2 q ≠ 0) :
    emMoment q = 0 ↔ barOddGen q = 0 := by
  rw [emMoment_eq_zero_iff q hq h2, barOddGen_eq_zero_iff q hq]

/-! ### Locus 2 — the normalisation degenerates at `q² = −1` -/

/-- **`[2]_q` vanishes exactly at `q² = −1`.** In particular `[2]_i = 0`, so the
moment is undefined at the discrete `q = i` point rather than merely small
there. Recorded as a coincidence of loci with the measure wall's stated
`q = i` no-germ obstruction; the identification is not proved here. -/
theorem qInt2_eq_zero_iff (q : R) (hq : q ≠ 0) : qInt2 q = 0 ↔ q ^ 2 = -1 := by
  rw [qInt2_eq q hq, div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · linear_combination h
    · exact absurd h hq
  · intro h; left; linear_combination h

/-- The two distinguished loci are **distinct** whenever `2 ≠ 0`: the moment
cannot vanish and degenerate at the same `q`. So "sterile" and "undefined" are
genuinely different failure modes of the germ. -/
theorem loci_disjoint (q : R) (h2 : (2 : R) ≠ 0) :
    ¬(q ^ 2 = 1 ∧ q ^ 2 = -1) := by
  rintro ⟨h1, hm1⟩
  exact h2 (by linear_combination hm1 - h1)

end QOU.MassTheory.EmGermMomentVanishing
