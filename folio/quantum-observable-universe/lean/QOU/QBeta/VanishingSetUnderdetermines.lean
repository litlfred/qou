import QOU.QBeta.WenzlWeightVanishing

/-!
# The vanishing set does not determine the Ocneanu weights

`WenzlWeightVanishing` axiomatises Wenzl (1988) as
`IsOcneanuWeightSystem Q z r y`, whose second field is a **weight identity**
`y μ = schurPrincipal r Q μ / Z`. A proposed cheaper discharge route
(`2026-08-16-ocneanu-weight-axiomatisation.md` §"Is there a cheaper route?")
would replace that field by the **vanishing set** `y μ = 0 ↔ r < μ.colLen 0`,
on the stated grounds that the vanishing set is all the corpus consumes.

This file measures the gap between those two hypotheses, so that the trade is
made against a proved statement rather than against an impression.

## Results

* `ocneanuWeight_eq_bot_smul_schurPrincipal` — **rigidity**: the class pins `y`
  completely, up to the single scalar `y ⊥`. Two weight systems agreeing at the
  empty diagram are equal everywhere.
* `vanishingSet_not_determines_weights` — **the gap is real**: rescaling a
  genuine weight system at one surviving diagram preserves the vanishing set
  exactly and destroys the class. So the vanishing-set hypothesis is *strictly*
  weaker, and a consumer of weight **values** is not served by it.

Neither result discharges Wenzl's theorem, and neither is a step toward
discharging it; both are measurements of what a proposed weaker hypothesis
would and would not supply. The route's viability is assessed in
`docs/audits/2026-08-21-wenzl-discharge-tln-route-scoping.md`.

Base ring: generic `{R : Type*} [Field R]` throughout — no ordering, no `ℝ`, no
archimedean construct (AGENTS.md §7c).
-/

namespace QOU.QBeta.WenzlWeight

variable {R : Type*} [Field R]

/-! ### The empty diagram -/

/-- `schurPrincipal` at the empty diagram is `1`: the cell product is empty and
`n(⊥) = 0`. This is the normalisation point that gives the rigidity lemma below
a canonical scalar to be stated against. -/
@[simp] theorem schurPrincipal_bot (r : ℕ) (Q : R) :
    schurPrincipal r Q (⊥ : YoungDiagram) = 1 := by
  simp [schurPrincipal, nPart]

/-! ### Rigidity: the class pins the weights up to one scalar -/

/-- **The value at the empty diagram is never zero.**

Proved from the class fields rather than from the vanishing criterion, so that
it does not inherit the genericity hypothesis: `y ⊥ = 1 / Z` with `Z ≠ 0`. -/
theorem ocneanuWeight_bot_ne_zero {Q z : R} {r : ℕ} {y : YoungDiagram → R}
    [hw : IsOcneanuWeightSystem Q z r y] : y (⊥ : YoungDiagram) ≠ 0 := by
  obtain ⟨Z, hZ, hy⟩ := hw.weight_eq_schurPrincipal
  rw [hy, schurPrincipal_bot]
  exact one_div_ne_zero hZ

/-- **Rigidity — the class determines `y` up to the single scalar `y ⊥`.**

`y μ = y ⊥ · s_μ`. The normaliser `Z` of the class is not a free parameter once
`y ⊥` is known: it is `1 / y ⊥`.

This is what `IsOcneanuWeightSystem` supplies *beyond* a vanishing set, and it
is the whole of the difference — a weight system carries one scalar's worth of
freedom, whereas the vanishing set leaves a nonzero scalar free at *every*
surviving diagram independently (`vanishingSet_not_determines_weights`). -/
theorem ocneanuWeight_eq_bot_smul_schurPrincipal {Q z : R} {r : ℕ}
    {y : YoungDiagram → R} [hw : IsOcneanuWeightSystem Q z r y]
    (μ : YoungDiagram) :
    y μ = y (⊥ : YoungDiagram) * schurPrincipal r Q μ := by
  obtain ⟨Z, hZ, hy⟩ := hw.weight_eq_schurPrincipal
  rw [hy, hy, schurPrincipal_bot]
  field_simp

/-- **Two weight systems at the same `(Q, r)` agreeing at `⊥` agree everywhere.**

An immediate corollary of rigidity, recorded because it is the form in which the
uniqueness is wanted below: the class has no room for two genuinely different
solutions once the normalisation is fixed. -/
theorem ocneanuWeight_unique_of_bot_eq {Q z z' : R} {r : ℕ}
    {y y' : YoungDiagram → R} [hw : IsOcneanuWeightSystem Q z r y]
    [hw' : IsOcneanuWeightSystem Q z' r y']
    (hbot : y (⊥ : YoungDiagram) = y' (⊥ : YoungDiagram)) : y = y' := by
  funext μ
  rw [ocneanuWeight_eq_bot_smul_schurPrincipal (hw := hw) μ,
    ocneanuWeight_eq_bot_smul_schurPrincipal (hw := hw') μ, hbot]

/-! ### The gap: the vanishing set is strictly weaker -/

open Classical in
/-- The one-point rescaling of a weight function: multiply the value at `μ₀` by
`c` and leave every other value alone.

`YoungDiagram` carries no `DecidableEq` instance, so this is classical and
`noncomputable`; nothing below evaluates it. -/
noncomputable def rescaleAt (μ₀ : YoungDiagram) (c : R) (y : YoungDiagram → R) :
    YoungDiagram → R :=
  fun μ => if μ = μ₀ then c * y μ else y μ

@[simp] theorem rescaleAt_self {μ₀ : YoungDiagram} {c : R}
    {y : YoungDiagram → R} : rescaleAt μ₀ c y μ₀ = c * y μ₀ := by
  simp [rescaleAt]

theorem rescaleAt_of_ne {μ₀ μ : YoungDiagram} {c : R} {y : YoungDiagram → R}
    (h : μ ≠ μ₀) : rescaleAt μ₀ c y μ = y μ := by
  simp [rescaleAt, h]

/-- **A one-point rescaling preserves the vanishing set exactly.**

For `c ≠ 0`, `rescaleAt μ₀ c y` vanishes at precisely the diagrams where `y`
does. So a vanishing-set hypothesis cannot tell the two apart. -/
theorem rescaleAt_eq_zero_iff {μ₀ : YoungDiagram} {c : R} (hc : c ≠ 0)
    {y : YoungDiagram → R} (μ : YoungDiagram) :
    rescaleAt μ₀ c y μ = 0 ↔ y μ = 0 := by
  by_cases h : μ = μ₀
  · subst h; simp [rescaleAt, hc]
  · simp [rescaleAt_of_ne h]

/-- **The vanishing set does not determine the weights.**

Given *any* genuine Ocneanu weight system `y`, and any diagram `μ₀ ≠ ⊥` that `y`
does not annihilate, the one-point rescaling `rescaleAt μ₀ c y` (with `c ≠ 0`,
`c ≠ 1`):

* has **exactly** the same vanishing set as `y` — so it satisfies every
  vanishing-set hypothesis that `y` does; and
* is **not** an Ocneanu weight system at `(Q, z', r)` for any `z'`.

Hence replacing `weight_eq_schurPrincipal` by a vanishing-set field yields a
*strictly weaker* hypothesis. A downstream consumer of weight **values** — as
opposed to the vanishing set alone — is not served by the weaker class.

The proof is rigidity: `rescaleAt μ₀ c y` still agrees with `y` at `⊥` (since
`μ₀ ≠ ⊥`), so if it were a weight system it would have to equal `y` everywhere
by `ocneanuWeight_unique_of_bot_eq`; but it differs at `μ₀` because `c ≠ 1` and
`y μ₀ ≠ 0`. Delete `ocneanuWeight_eq_bot_smul_schurPrincipal` and the argument
does not go through: nothing else forces the value at `μ₀`.

`z` is explicit: it appears in the hypothesis but not in the conclusion, so
typeclass resolution cannot recover it (the same convention as
`ocneanuWeight_eq_zero_iff_of_wenzl`). -/
theorem vanishingSet_not_determines_weights {Q : R} (z : R) {r : ℕ}
    {y : YoungDiagram → R} [hy : IsOcneanuWeightSystem Q z r y]
    {μ₀ : YoungDiagram} (hμ₀ : μ₀ ≠ ⊥) (hy₀ : y μ₀ ≠ 0)
    {c : R} (hc0 : c ≠ 0) (hc1 : c ≠ 1) :
    (∀ μ, rescaleAt μ₀ c y μ = 0 ↔ y μ = 0) ∧
      ∀ z' : R, ¬ IsOcneanuWeightSystem Q z' r (rescaleAt μ₀ c y) := by
  refine ⟨fun μ => rescaleAt_eq_zero_iff hc0 μ, fun z' hw' => ?_⟩
  -- The rescaling agrees with `y` at `⊥`, since `μ₀ ≠ ⊥`.
  have hbot : rescaleAt μ₀ c y (⊥ : YoungDiagram) = y (⊥ : YoungDiagram) :=
    rescaleAt_of_ne (fun h => hμ₀ h.symm)
  -- So rigidity forces the two functions to be equal everywhere …
  have heq : rescaleAt μ₀ c y = y :=
    ocneanuWeight_unique_of_bot_eq (hw := hw') (hw' := hy) hbot
  -- … but they differ at `μ₀`.
  have hmul : c * y μ₀ = y μ₀ := by
    have h := congrFun heq μ₀
    rwa [rescaleAt_self] at h
  exact hc1 (mul_right_cancel₀ hy₀ (by rw [one_mul]; exact hmul))

/-! ### The gap is inhabited, not merely stated

`vanishingSet_not_determines_weights` carries three side conditions
(`μ₀ ≠ ⊥`, `y μ₀ ≠ 0`, and a scalar `c ∉ {0, 1}`) on top of the class. A
theorem whose hypotheses are never jointly met proves nothing, so they are met
here concretely rather than argued for. -/

/-- **A concrete function with the right vanishing set that is not an Ocneanu
weight system.**

Take the level-2 weights at `Q = 2` over `ℚ` — the satisfiability witness
`isOcneanuWeightSystem_schurPrincipal` — and double the value on the two-row
diagram `(2,1)`, the block PR #5185 measured at `y₍₂,₁₎ = q²/(q²+1)² ≠ 0`. The
result annihilates exactly the same diagrams (in particular it still kills
`(1³)` and still spares `(2,1)`), yet it is **not** a weight system at any
Markov parameter.

So a vanishing-set hypothesis admits this function and the genuine one alike,
while `IsOcneanuWeightSystem` separates them. This is the concrete form of the
gap, on the same two blocks `discriminates_at_n_three` uses. -/
theorem rescaled_two_one_not_weight_system :
    (∀ μ : YoungDiagram,
        rescaleAt (YoungDiagram.ofRowLens [2, 1] (by decide)) (2 : ℚ)
            (fun ν => schurPrincipal 2 (2 : ℚ) ν / 1) μ = 0
          ↔ schurPrincipal 2 (2 : ℚ) μ / 1 = 0) ∧
      ∀ z' : ℚ, ¬ IsOcneanuWeightSystem (2 : ℚ) z' 2
        (rescaleAt (YoungDiagram.ofRowLens [2, 1] (by decide)) (2 : ℚ)
          (fun ν => schurPrincipal 2 (2 : ℚ) ν / 1)) := by
  haveI : IsOcneanuWeightSystem (2 : ℚ)
      ((2 : ℚ) ^ 2 * (1 - 2) / (1 - (2 : ℚ) ^ 2)) 2
      (fun ν => schurPrincipal 2 (2 : ℚ) ν / 1) :=
    isOcneanuWeightSystem_schurPrincipal 2 (by norm_num)
  -- `(2,1)` is not the empty diagram: its first column has length `2`, not `0`.
  have hbot : (⊥ : YoungDiagram).colLen 0 = 0 := by simp [YoungDiagram.colLen]
  have hne : YoungDiagram.ofRowLens [2, 1] (by decide) ≠ (⊥ : YoungDiagram) := by
    intro h
    have h2 := colLen_ofRowLens_two_one
    rw [h, hbot] at h2
    exact absurd h2 (by norm_num)
  exact vanishingSet_not_determines_weights
    ((2 : ℚ) ^ 2 * (1 - 2) / (1 - (2 : ℚ) ^ 2))
    (y := fun ν => schurPrincipal 2 (2 : ℚ) ν / 1)
    hne discriminates_at_n_three.2 (by norm_num) (by norm_num)

end QOU.QBeta.WenzlWeight
