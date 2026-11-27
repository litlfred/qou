/-
  # Gauge intents, flux-threading intents, and closed-loop holonomy

  Part 3 of `docs/audits/2026-11-27-observer-intent-outer-automorphisms.md`.

  Edge variables on a graph with vertex set `V` take values in a group `G`
  (`U x y` is the transport along the oriented edge `x → y`). The holonomy of a walk
  `x, v₁, …, v_k` is the ordered product of its edge variables.

  * A **gauge intent** acts by a vertex 0-cochain `g : V → G`,
    `U x y ↦ g x · U x y · (g y)⁻¹`. Along any walk the inner factors telescope
    (`hol_gauge`), so on a closed walk the holonomy is conjugated
    (`hol_gauge_closed`) and every class function of it is unchanged.
  * A **flux-threading intent** acts by an integer 1-cochain `ω` and a central `z`,
    `U x y ↦ z^{ω x y} · U x y`. Along any walk it multiplies the holonomy by
    `z^{∮ω}` (`hol_flux`).
  * Hence (`flux_not_gauge`): if `∮_γ ω` is such that a class function `χ`
    separates `W(γ)` from `z^{∮ω}·W(γ)`, no gauge intent equals the flux intent.

  **Scope (stated in the audit).** Nothing here uses locality, a radius, or the
  half-systole of Bring's `{5,4}` map: a *global* vertex gauge preserves holonomy
  just as a local one does. The obstruction separating the flux intent from gauge
  intents is the class of `ω` modulo coboundaries, not locality. And a one-edge
  flux (`ω` supported on a single edge, a radius-0 operation) also changes the
  holonomy (`hol_flux` with that `ω`), so "changes a systole holonomy" does not by
  itself certify "not a cellular automaton". A correct non-CA statement must
  restrict the CA class to curvature-preserving gates (`dω = 0` on every face);
  that restriction is the content the owner discussion left implicit.

  Generic: any `Group G`, any type `V`; no ring, no `ℝ`.

  -- Ref: [leitner2026] def:observation, rem:two-observer-parallelogram
-/
import Mathlib.Algebra.Group.Commute.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Group.Conj
import Mathlib.Tactic.Group

set_option autoImplicit false

namespace QOU.IntentHolonomy

variable {V G : Type*} [Group G]

/-- Holonomy of the walk starting at `x` and visiting the listed vertices in order. -/
def hol (U : V → V → G) : V → List V → G
  | _, [] => 1
  | x, y :: rest => U x y * hol U y rest

/-- Endpoint of the walk. -/
def last : V → List V → V
  | x, [] => x
  | _, y :: rest => last y rest

/-- Gauge intent by a vertex 0-cochain. -/
def gauge (g : V → G) (U : V → V → G) : V → V → G := fun x y => g x * U x y * (g y)⁻¹

/-- Flux-threading intent by an integer 1-cochain `ω` and an element `z`. -/
def flux (ω : V → V → ℤ) (z : G) (U : V → V → G) : V → V → G := fun x y => z ^ ω x y * U x y

/-- `∮ ω` along the walk. -/
def wsum (ω : V → V → ℤ) : V → List V → ℤ
  | _, [] => 0
  | x, y :: rest => ω x y + wsum ω y rest

/-- **Telescoping.** A gauge intent conjugates the holonomy of every walk by its
endpoint values. -/
theorem hol_gauge (g : V → G) (U : V → V → G) :
    ∀ (x : V) (l : List V), hol (gauge g U) x l = g x * hol U x l * (g (last x l))⁻¹
  | x, [] => by simp [hol, last]
  | x, y :: rest => by
      simp only [hol, last, gauge, hol_gauge g U y rest]
      group

/-- On a closed walk a gauge intent conjugates the holonomy. -/
theorem hol_gauge_closed (g : V → G) (U : V → V → G) (x : V) (l : List V)
    (hc : last x l = x) : hol (gauge g U) x l = g x * hol U x l * (g x)⁻¹ := by
  rw [hol_gauge, hc]

/-- Every class function of a closed-walk holonomy is gauge invariant. -/
theorem classFun_gauge_invariant {K : Type*} (χ : G → K) (hχ : ∀ a b, χ (a * b * a⁻¹) = χ b)
    (g : V → G) (U : V → V → G) (x : V) (l : List V) (hc : last x l = x) :
    χ (hol (gauge g U) x l) = χ (hol U x l) := by
  rw [hol_gauge_closed g U x l hc, hχ]

/-- **Flux threading.** For central `z`, the flux intent multiplies the holonomy of
every walk by `z^{∮ω}`. -/
theorem hol_flux (ω : V → V → ℤ) {z : G} (hz : ∀ a : G, Commute z a) (U : V → V → G) :
    ∀ (x : V) (l : List V), hol (flux ω z U) x l = z ^ wsum ω x l * hol U x l
  | x, [] => by simp [hol, wsum]
  | x, y :: rest => by
      simp only [hol, wsum, flux, hol_flux ω hz U y rest, zpow_add]
      have hc : Commute (z ^ wsum ω y rest) (U x y) := (hz (U x y)).zpow_left _
      rw [mul_assoc, ← mul_assoc (U x y), ← hc.eq]
      group

/-- **The flux intent is not a gauge intent** whenever a class function separates the
closed-walk holonomy `W` from `z^{∮ω}·W`. -/
theorem flux_not_gauge {K : Type*} (χ : G → K) (hχ : ∀ a b, χ (a * b * a⁻¹) = χ b)
    (ω : V → V → ℤ) {z : G} (hz : ∀ a : G, Commute z a) (U : V → V → G)
    (x : V) (l : List V) (hc : last x l = x)
    (hsep : χ (z ^ wsum ω x l * hol U x l) ≠ χ (hol U x l)) :
    ¬ ∃ g : V → G, gauge g U = flux ω z U := by
  rintro ⟨g, hg⟩
  apply hsep
  rw [← hol_flux ω hz U x l, ← hg, classFun_gauge_invariant χ hχ g U x l hc]

/-- A coboundary flux `ω = δf` (`ω x y = f y − f x`) is a gauge intent: take
`g x = z^{−f x}`. So only the class of `ω` modulo coboundaries can obstruct. -/
theorem flux_coboundary_is_gauge (f : V → ℤ) {z : G} (hz : ∀ a : G, Commute z a)
    (U : V → V → G) :
    flux (fun x y => f y - f x) z U = gauge (fun x => z ^ (-f x)) U := by
  funext x y
  simp only [flux, gauge]
  have hc : Commute (z ^ (-f x)) (U x y) := (hz (U x y)).zpow_left _
  calc z ^ (f y - f x) * U x y = U x y * z ^ (f y - f x) := ((hz _).zpow_left _).eq
    _ = U x y * (z ^ (-f x) * (z ^ (-f y))⁻¹) := by
        rw [← zpow_neg, ← zpow_add]; congr 2; ring
    _ = z ^ (-f x) * U x y * (z ^ (-f y))⁻¹ := by rw [← mul_assoc, hc.eq]

end QOU.IntentHolonomy
