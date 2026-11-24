import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Two exact facts about the Q_β ladder phase, block-resolved

Companion to `computations/qbeta/qbeta_phase_block_resolution_probe.py` (18/18)
and `computations/qbeta/qbeta_alpha_commutator_floor_probe.py` (22/22), on bean
`qou-cds1` (re-derive the Q_β ladder under convention D).

Background, in one paragraph. The ladder's eigenphase satisfies the exact
identity `ε(Δ) − tr_M^z(Δ) = h(z−1) = 2α`, so `α` is half the gap between two
functionals on the neutron−proton normal-form difference

`Δ = (h²/2)·γ − (h/2)·σ₀ − (h/2)·σ₁` in the Gröbner–Shirshov basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]` of `H₃(q)`.

Resolving that gap per Wedderburn block gives

`2α(z) = Σ_λ [a_λ − y_λ(z)] · χ^λ(Δ) + net(d_C)`,

in which only `y_λ(z)` depends on the Markov parameter. This file pins the two
statements from that resolution that are ring identities rather than
computations in a specific representation.

## Base ring (AGENTS.md §7c)

Generic `[CommRing R]`. Nothing archimedean appears: no ordering, no `Real.*`.
The divisions the narrative writes are carried as invertible data — `⅟(2 : R)`
for the halves in `Δ`, and `q : Rˣ` for the bar involution `q ↦ q⁻¹` — which is
the `CommRing` analogue of the nonzero side conditions, and recovers the
field statements via `invertibleOfNonzero` / `Units.mk0`.
-/

namespace QOU.QBeta.PhaseBlockResolution

variable {R : Type*} [CommRing R]

/-! ### 1. The phase is blind to the 2-dimensional block -/

/-- Coordinates of `Δ = NF(n) − NF(p)` in the Gröbner–Shirshov basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]` of `H₃(q)`, with the Hecke parameter `h = q − q⁻¹`.
This is the vector the Q_β ansatz evaluates. -/
def deltaCoords [Invertible (2 : R)] (h : R) : Fin 6 → R :=
  ![h ^ 2 * ⅟(2 : R), -(h * ⅟(2 : R)), -(h * ⅟(2 : R)), 0, 0, 0]

/-- A linear functional on `H₃(q)` applied to a coordinate vector: the pairing
of its values on the six basis elements against the vector. -/
def pair (f v : Fin 6 → R) : R :=
  f 0 * v 0 + f 1 * v 1 + f 2 * v 2 + f 3 * v 3 + f 4 * v 4 + f 5 * v 5

/-- **The 2-dimensional block character annihilates `Δ`.**

The `λ = (2,1)` block of `H₃(q)` is two-dimensional and each generator `σᵢ` acts
there with eigenvalues `q` and `−q⁻¹`, hence with trace `h = q − q⁻¹`. Those two
facts alone force `χ^{(2,1)}(Δ) = 0`:

`(h²/2)·2 − (h/2)·h − (h/2)·h = h² − h²/2 − h²/2 = 0`.

Note what the statement does *not* need: the character's values on the three
longer basis elements are left completely free, because `Δ` has zero coordinate
there. So the vanishing is a property of `Δ`'s support together with the block's
dimension and generator trace — not of the block's full character table.

Consequence for the ladder: the eigenphase `α = (ε − tr_M)/2` is blind to the
2-dimensional block **in every convention**, since no Markov parameter enters
this identity. -/
theorem chi_two_one_delta_eq_zero [Invertible (2 : R)]
    (h : R) (chi : Fin 6 → R)
    (hdim : chi 0 = 2) (hs0 : chi 1 = h) (hs1 : chi 2 = h) :
    pair chi (deltaCoords h) = 0 := by
  simp only [pair, deltaCoords, Matrix.cons_val_zero, Matrix.cons_val_one,
    hdim, hs0, hs1, Matrix.cons_val]
  ring

/-! ### 2. The commutator floor is bar-even -/

/-- Numerator of the commutator floor `net(d_C) = −(q²−1)² / (q⁴+q²+1)`, the
`z`-free part of the ladder phase: the value of the coordinate sum on the
component of `Δ` lying in `[H,H]`, which every trace annihilates.

Written as a function of a bare ring element so that the bar involution can be
applied to it without leaving `CommRing`; `q` and its bar-image `q⁻¹` are then
related only by the hypothesis `q · q⁻¹ = 1`. -/
def floorNum (x : R) : R := -(x ^ 2 - 1) ^ 2

/-- Denominator of the commutator floor. -/
def floorDen (x : R) : R := x ^ 4 + x ^ 2 + 1

/-- **The commutator floor is bar-even.**

Stated division-free by cross-multiplication, and with the bar involution
`q ↦ q⁻¹` carried by the single hypothesis `u · v = 1`, so the statement needs
nothing beyond `CommRing`:

`floorNum v · floorDen u = floorNum u · floorDen v`.

The identity is not a tautology of the shape — over a general commutative ring
`floorNum v · floorDen u − floorNum u · floorDen v = 3(u²−v²)((uv)²−1)`, which
is nonzero in general and vanishes exactly on the bar-involution locus `uv = 1`.

Why it matters on `qou-cds1`. The sibling prune `MarkovWeightsConventionD` shows
both surviving convention-D Markov weights are bar-even, hence that no bar-odd
part can be assembled *from the weights*. The floor is not built from weights —
it is a non-trace functional evaluated on the very component every weight
annihilates — so that prune does not reach it. This says the trace-invisible
sector supplies no bar-odd material either, and the prune therefore extends
rather than breaking. -/
theorem floor_bar_even (u v : R) (huv : u * v = 1) :
    floorNum v * floorDen u = floorNum u * floorDen v := by
  simp only [floorNum, floorDen]
  linear_combination (3 * (u ^ 2 - v ^ 2) * (u * v + 1)) * huv

/-- The cross-multiplied identity is genuinely conditional on `u · v = 1`: off
that locus the two sides differ by `3(u²−v²)((uv)²−1)`. Recorded so the theorem
above is not mistaken for a `ring` tautology. -/
theorem floor_bar_defect (u v : R) :
    floorNum v * floorDen u - floorNum u * floorDen v
      = 3 * (u ^ 2 - v ^ 2) * ((u * v) ^ 2 - 1) := by
  simp only [floorNum, floorDen]; ring

/-- The bar-evenness in the form the narrative uses, with `q` a unit and its
bar-image the honest inverse. -/
theorem floor_bar_even_units (q : Rˣ) :
    floorNum (↑q⁻¹ : R) * floorDen (q : R)
      = floorNum (q : R) * floorDen (↑q⁻¹ : R) :=
  floor_bar_even _ _ q.mul_inv

end QOU.QBeta.PhaseBlockResolution
