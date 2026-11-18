/-
# The substrate's complexity bound loosens with `A`, so it cannot select a link

The nucleus→link assignments for `²H`, `³H`, `³He` are an admitted census fit:
the search criterion is proximity of `Vol` to `B_AME / (ρ · m_e)`
(`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md`). That audit measured
where the apparent selectivity comes from — **0** census manifolds beat `6₂`
inside the tabulated low-crossing links, **796** beat it without that
restriction — and closed by asking whether the substrate independently supplies
the restriction.

`computations/probes/substrate_complexity_bound_probe.py` measures what it does
supply. The canonical atom word on `A` nucleons has exactly `10 * A - 2` genuine
braid letters and uses exactly `3 * A` strands, so the substrate bounds any
closure by

  `crossings ≤ 10 * A - 2`   and   `braid index ≤ 3 * A`.

This file proves the consequence: **both bounds are strictly increasing in `A`,
and admissibility is monotone** — a link admissible at `A` is admissible at every
larger `A`. So the admissible class is a strictly increasing chain. Two links
distinct in crossing number are admissible together at every `A ≥ 1`, and the
slack above any fixed link grows without bound.

The reading is a *caution*, not a refutation: the derived bound is real and the
assigned knots satisfy it, but it never narrows, so it cannot be the source of a
selection. A census search at larger `A` is strictly freer than the `A = 2`
search, which is already 796-fold degenerate.

**Scope (a)** for the census route. Nothing here excludes a derived nucleus→link
map; it excludes recovering one by volume-matching inside the class the
substrate actually cuts out.

No `sorry`. Everything is over `ℕ`; `omega` discharges the truncated
subtraction, so `10 * A - 2` needs no side conditions beyond those stated.
-/
-- `omega` is a Lean core tactic, so no tactic import is needed; this import is
-- only for the `ℕ` notation. `Mathlib.Tactic.Omega` is deliberately NOT imported
-- — its olean is absent from the restored cache, and pulling it in would make
-- this file unverifiable in a sandbox for no gain.
import Mathlib.Data.Nat.Basic

namespace QOU.Mass.SubstrateComplexityBound

/-- Crossing bound the substrate supplies at mass number `A`: the number of
genuine braid letters in the canonical atom word, measured as `10 * A - 2`. -/
abbrev crossingBound (A : ℕ) : ℕ := 10 * A - 2

/-- Braid-index bound the substrate supplies at mass number `A`: the atom
occupies three strands per nucleon, so its closure has braid index at most
`3 * A`. -/
abbrev braidIndexBound (A : ℕ) : ℕ := 3 * A

/-- The data a complexity bound can see about a link. -/
structure LinkData where
  crossings : ℕ
  braidIndex : ℕ
  deriving DecidableEq

/-- A link is admissible at `A` when it satisfies both substrate bounds. -/
def Admissible (A : ℕ) (L : LinkData) : Prop :=
  L.crossings ≤ crossingBound A ∧ L.braidIndex ≤ braidIndexBound A

/-- Admissibility spelled out as plain arithmetic, so `omega` can be handed the
goal directly rather than being asked to see through a projection. -/
theorem admissible_iff (A : ℕ) (L : LinkData) :
    Admissible A L ↔ L.crossings ≤ 10 * A - 2 ∧ L.braidIndex ≤ 3 * A := Iff.rfl

/-- The crossing bound is strictly increasing once `A ≥ 1` (below that the
truncated subtraction flattens it, and no nucleus has `A = 0`). -/
theorem crossingBound_lt_of_lt {A B : ℕ} (hA : 1 ≤ A) (h : A < B) :
    crossingBound A < crossingBound B := by
  show 10 * A - 2 < 10 * B - 2
  omega

/-- The braid-index bound is strictly increasing. -/
theorem braidIndexBound_lt_of_lt {A B : ℕ} (h : A < B) :
    braidIndexBound A < braidIndexBound B := by
  show 3 * A < 3 * B
  omega

/-- **Admissibility only grows.** A link admissible at `A` stays admissible at
every larger mass number, so the substrate bound never removes a candidate. -/
theorem admissible_mono {A B : ℕ} (h : A ≤ B) {L : LinkData}
    (hL : Admissible A L) : Admissible B L := by
  obtain ⟨hc, hb⟩ := (admissible_iff A L).mp hL
  exact (admissible_iff B L).mpr ⟨by omega, by omega⟩

/-- **The bound is never selective.** At every `A ≥ 1` there are two links with
different crossing numbers that are both admissible, so no `A` singles one out.
-/
theorem not_selective (A : ℕ) (hA : 1 ≤ A) :
    ∃ L₁ L₂ : LinkData, L₁ ≠ L₂ ∧ Admissible A L₁ ∧ Admissible A L₂ :=
  -- `omega` will not reduce a projection out of a structure literal, so each
  -- component is `show`n as plain arithmetic first.
  ⟨⟨0, 0⟩, ⟨1, 1⟩, by simp,
    (admissible_iff A _).mpr
      ⟨by show (0 : ℕ) ≤ 10 * A - 2; omega, by show (0 : ℕ) ≤ 3 * A; omega⟩,
    (admissible_iff A _).mpr
      ⟨by show (1 : ℕ) ≤ 10 * A - 2; omega, by show (1 : ℕ) ≤ 3 * A; omega⟩⟩

/-- **The slack above any fixed link is unbounded.** For every link and every
`N` there is a mass number at which the crossing bound exceeds that link's
crossing number by at least `N` — the fit gets freer as `A` grows, not tighter.
-/
theorem slack_unbounded (L : LinkData) (N : ℕ) :
    ∃ A : ℕ, 1 ≤ A ∧ L.crossings + N ≤ crossingBound A :=
  ⟨L.crossings + N + 1, by omega, by
    show L.crossings + N ≤ 10 * (L.crossings + N + 1) - 2
    omega⟩

/-- The three registry assignments, as the bound sees them: `6₂` at `A = 2`,
`8₁₁` and `L6a4` at `A = 3`. Each is admissible — the bound is satisfied, which
is exactly why it carries no information about which was chosen. -/
example : Admissible 2 ⟨6, 3⟩ ∧ Admissible 3 ⟨8, 5⟩ ∧ Admissible 3 ⟨6, 3⟩ := by
  refine ⟨?_, ?_, ?_⟩ <;> rw [admissible_iff] <;> exact ⟨by decide, by decide⟩

/-- Step monotonicity of `Admissible`: any link admissible at `A` is admissible at `A + 1`. -/
theorem admissible_succ (A : ℕ) {L : LinkData} (hL : Admissible A L) :
    Admissible (A + 1) L :=
  admissible_mono (Nat.le_succ A) hL

end QOU.Mass.SubstrateComplexityBound
