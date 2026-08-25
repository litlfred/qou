import Mathlib.Tactic

/-!
# QOU.Eightfold.GellMannOkuboSecondOrder — what a second-order term can and cannot carry

Bean `qou-bhfg`. Sequel to `QOU.Eightfold.GellMannOkuboIdentity`, which proves
Gell-Mann–Okubo vanishes **identically** in the first-order octet ansatz and so
has zero discriminating power.

## The question this answers

If GMO is content-free at first order, the testable content is its **deviation**
(≈ 6 %), and likewise the decuplet equal-spacing deviation (≈ 9.2 %). The
framework derives no second-order term, so it currently predicts **0** for both.
Before anyone fits a term to those numbers, it is worth knowing *which*
second-order structures can carry them at all — a formalize-first prune
(AGENTS.md §"Formalize-first probe discipline").

## The ansatz

First order is `m = a + b·Y + c·d` with `d = I(I+1) − Y²/4`. At second order the
three structures quadratic in the breaking are `Y²`, `d²` and `Y·d`, with
coefficients `e`, `f`, `g`. Everything is scaled by 16 and written through
`fourD = 4·I(I+1) − Y²` so that no denominator ever appears; the scaling is
uniform and cancels from every statement below.

## What is proved

| declaration | content |
|---|---|
| `gmo_second_order` | the GMO combination is `16·(4e − 3f)` |
| `gmo_blind_to_Yd` | **GMO cannot see `g` at all** — the `Y·d` structure is odd in `Y` and dies in the hypercharge-averaged kaon |
| `decuplet_second_differences_equal` | the two decuplet second differences stay **exactly equal** |
| `decuplet_second_order` | each is `8·(4e + 9f + 6g)` |
| `gmo_zero_decuplet_nonzero` / `decuplet_zero_gmo_nonzero` | the two constraints are **independent** — witnesses both ways |

## What it means, stated carefully

Two consequences, and neither is a derivation of anything:

1. **`Y·d` is invisible to GMO.** Not "small" — *exactly* zero, by parity in `Y`.
   A GMO-deviation fit therefore cannot constrain `g` even in principle.
2. **Two measurements, three unknowns.** GMO constrains `4e − 3f`; the decuplet
   constrains `4e + 9f + 6g`. Those are not proportional, so the two deviations
   are independent — and they under-determine `(e, f, g)` by one. **Reproducing
   both numbers is therefore not a prediction**: a one-parameter family of
   second-order terms fits any pair of values. A third independent observable is
   needed before a second-order account has content.

The equal-spacing result is worth stating precisely, because it is easy to
over-read. At second order the decuplet is **not** equally spaced — each second
difference is `8·(4e + 9f + 6g) ≠ 0` in general. What survives is that the two
second differences remain *equal to each other*: the failure is uniform, so the
decuplet masses go from linear to exactly quadratic in the ladder position, with
no cubic residue. That is a real constraint on any second-order account, and it
is testable against the observed spacings independently of their common size.

**Scope.** This is a statement about the standard `(I, Y)` octet/decuplet mass
ansatz, consumed as given — the same ansatz `GellMannOkuboIdentity` uses. It
derives no value for `e`, `f`, `g`, predicts neither deviation, and says nothing
about whether QOU produces such a term. Coleman–Glashow is deliberately **not**
included: it is an electromagnetic/isospin-breaking relation, not an
`SU(3)`-breaking one on this ansatz, and folding it in here would be the
overloaded-symbol error this branch has already had to correct once.

-- Ref: [okubo1962] (the octet mass formula and its `SU(3)`-breaking expansion).
-/

namespace QOU.Eightfold.GellMannOkuboSecondOrder

variable {R : Type*} [CommRing R]

/-- `16 ×` the mass of a state, with first-order coefficients `a, b, c` and
second-order `e` (`Y²`), `f` (`d²`), `g` (`Y·d`).

`fourD = 4·I(I+1) − Y²`, i.e. `4d`. The `16 ×` and the `fourD` parametrisation
between them clear every denominator; both scalings are uniform across states
and cancel from every combination below. -/
def m16 (a b c e f g : R) (fourD Y : R) : R :=
  16 * a + 16 * b * Y + 4 * c * fourD + 16 * e * Y ^ 2 + f * fourD ^ 2 + 4 * g * Y * fourD

section Meson
variable (a b c e f g : R)

/-- Pion: `I = 1, Y = 0` ⇒ `fourD = 8`. -/
def pion : R := m16 a b c e f g 8 0
/-- Eta: `I = 0, Y = 0` ⇒ `fourD = 0`. -/
def eta : R := m16 a b c e f g 0 0
/-- Kaon at `Y = +1`: `I = 1/2` ⇒ `fourD = 2`. -/
def kaonPlus : R := m16 a b c e f g 2 1
/-- Kaon at `Y = −1`. -/
def kaonMinus : R := m16 a b c e f g 2 (-1)

/-- The GMO combination `4·⟨m²_K⟩ − 3·m²_η − m²_π`, doubled so the hypercharge
average over the kaon doublet needs no division. -/
def gmoCombination : R := 2 * (kaonPlus a b c e f g + kaonMinus a b c e f g)
  - 3 * eta a b c e f g - pion a b c e f g

/-- **GMO at second order is `16·(4e − 3f)`.** It vanishes identically in the
first-order parameters `a, b, c` — recovering `GellMannOkuboIdentity` — and
picks up exactly one combination of the second-order ones. -/
theorem gmo_second_order : gmoCombination a b c e f g = 16 * (4 * e - 3 * f) := by
  unfold gmoCombination kaonPlus kaonMinus eta pion m16; ring

/-- **GMO is blind to the `Y·d` structure.** Changing `g` freely leaves the
combination unchanged — it is odd in `Y` and cancels in the kaon average. So a
fit to the GMO deviation cannot constrain `g`, even in principle. -/
theorem gmo_blind_to_Yd (g' : R) :
    gmoCombination a b c e f g = gmoCombination a b c e f g' := by
  rw [gmo_second_order, gmo_second_order]

end Meson

section Decuplet
variable (a b c e f g : R)

/-- Δ: `I = 3/2, Y = 1` ⇒ `fourD = 14`. -/
def delta : R := m16 a b c e f g 14 1
/-- Σ*: `I = 1, Y = 0` ⇒ `fourD = 8`. -/
def sigmaStar : R := m16 a b c e f g 8 0
/-- Ξ*: `I = 1/2, Y = −1` ⇒ `fourD = 2`. -/
def xiStar : R := m16 a b c e f g 2 (-1)
/-- Ω: `I = 0, Y = −2` ⇒ `fourD = −4`. -/
def omega : R := m16 a b c e f g (-4) (-2)

/-- Upper second difference `Ω − 2Ξ* + Σ*`; zero iff the top three are equally
spaced. -/
def spacingUpper : R := omega a b c e f g - 2 * xiStar a b c e f g + sigmaStar a b c e f g
/-- Lower second difference `Ξ* − 2Σ* + Δ`. -/
def spacingLower : R := xiStar a b c e f g - 2 * sigmaStar a b c e f g + delta a b c e f g

/-- **The equal-spacing rule fails at second order** — each second difference is
`8·(4e + 9f + 6g)`, nonzero in general. -/
theorem decuplet_second_order :
    spacingUpper a b c e f g = 8 * (4 * e + 9 * f + 6 * g) := by
  unfold spacingUpper omega xiStar sigmaStar m16; ring

/-- **But the failure is uniform.** The two second differences remain *exactly*
equal, so the decuplet goes from linear to exactly quadratic in the ladder
position with no cubic residue — a constraint testable independently of the
common size of the deviation. -/
theorem decuplet_second_differences_equal :
    spacingUpper a b c e f g = spacingLower a b c e f g := by
  unfold spacingUpper spacingLower omega xiStar sigmaStar delta m16; ring

end Decuplet

/-! ## Independence — two measurements cannot fix three coefficients -/

/-- A second-order term with **zero** GMO deviation and a **nonzero** decuplet
one. -/
theorem gmo_zero_decuplet_nonzero :
    gmoCombination (0:ℤ) 0 0 3 4 0 = 0 ∧ spacingUpper (0:ℤ) 0 0 3 4 0 ≠ 0 := by
  constructor
  · rw [gmo_second_order]; decide
  · rw [decuplet_second_order]; decide

/-- And one with a **nonzero** GMO deviation and **zero** decuplet one. So the
two relations constrain genuinely different combinations, and together they
still leave a one-parameter family: reproducing both observed deviations is a
fit, not a prediction. -/
theorem decuplet_zero_gmo_nonzero :
    spacingUpper (0:ℤ) 0 0 3 (-4) 4 = 0 ∧ gmoCombination (0:ℤ) 0 0 3 (-4) 4 ≠ 0 := by
  constructor
  · rw [decuplet_second_order]; decide
  · rw [gmo_second_order]; decide

end QOU.Eightfold.GellMannOkuboSecondOrder
