/-
# No antisymmetric-column Casimir carries three-body content — for any `SU(N)`

`QOU.Mass.SU4CasimirIsAffineInPairCount` showed that the Wigner `SU(4)` Casimir
of the fully antisymmetric `[1^n]` is affine in the pair count, so a two-body
`SU(4)`-invariant interaction contributes a constant per pair and gives `b₃ = 0`.

**That was not an `SU(4)` accident.** This file proves the same for every `N`,
which is what turns a one-off refutation into a closed *family* — and the family
includes `SU(3)`, the eightfold way's own flavour group.

## The general identities

For the fully antisymmetric `[1^n]` of `SU(N)`,

    C₂([1^n]) = (N+1)·n·(N−n) / (2N),     C₂(fund) = (N²−1) / (2N)

Clearing denominators (`casimirAntisymX2N` is `2N·C₂([1^n])`, `pairSumX4N` is
`4N·S`, `pairCountX2` is `2·C(n,2) = n(n−1)`):

* `casimir_affine` —

      2N·C₂([1^n]) = (N+1)(N−1)·n − (N+1)·n(n−1)

  the Casimir is **affine in `{n, C(n,2)}` for every `N`**.

* `pairSum_eq` — the two-body sum `S(n) = ½(C₂([1^n]) − n·C₂(fund))` satisfies

      2N·S(n) = −(N+1)·C(n,2)      i.e.   S(n) = −[(N+1)/(2N)]·C(n,2)

  **exactly proportional to the pair count, for every `N` and every `n`.**

## What that closes

`S` is what a two-body `SU(N)`-invariant interaction contributes summed over the
antisymmetric `A`-body state. Being exactly proportional to the pair count, it
contributes a *constant per pair*: constant coordination weight, `b₃ = 0`. So
**no antisymmetric-column Casimir of any `SU(N)` can produce a connected
three-body cumulant.**

Specialisations worth naming, since each has been proposed at some point:

| `N` | group | `S(n)/C(n,2)` | what it was proposed for |
|---|---|---|---|
| 2 | spin | `−3/4` | spin-only pairing |
| **3** | **flavour — the eightfold way** | **`−2/3`** | the `SU(3)` route |
| 4 | Wigner spin-isospin | `−5/8` | the merged `SU4Casimir…` result |
| 6 | spin-flavour with strangeness | `−7/12` | large-`N_c` extensions |

## Scope

This closes *antisymmetric-column quadratic Casimirs*. It does **not** touch:
the cubic and higher Casimirs, which are not affine in the pair count in general;
representations of mixed symmetry (relevant only outside the `s`-shell, `A ≥ 5`);
`6j` symbols and other recoupling data, which are genuinely three-object; or the
**support** bound `dim[1^n] = 0` for `n > N`, which locates the turnover and uses
the vanishing of the representation rather than its Casimir.

Base ring is a generic `CommRing`; the content is two polynomial identities.

Bean `qou-edt7`. Generalises `QOU.Mass.SU4CasimirIsAffineInPairCount`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.Mass.AntisymmetricCasimirIsTwoBody

variable {R : Type*} [CommRing R]

/-- `2N · C₂([1^n])` for the fully antisymmetric representation of `SU(N)`,
whose Casimir is `(N+1)n(N−n)/(2N)`. Scaled to stay in a ring. -/
def casimirAntisymX2N (n N : R) : R := (N + 1) * n * (N - n)

/-- `2N · C₂(fund) = N² − 1`. -/
def casimirFundX2N (N : R) : R := N ^ 2 - 1

/-- `2 · C(n,2) = n(n−1)`. -/
def pairCountX2 (n : R) : R := n * (n - 1)

/-- `4N · S(n)` where `S(n) = ½(C₂([1^n]) − n·C₂(fund))` is the sum a two-body
`SU(N)`-invariant interaction contributes over the antisymmetric `n`-body state. -/
def pairSumX4N (n N : R) : R := casimirAntisymX2N n N - n * casimirFundX2N N

/-- **The Casimir is affine in the pair count, for every `N`.** -/
theorem casimir_affine (n N : R) :
    casimirAntisymX2N n N = (N + 1) * (N - 1) * n - (N + 1) * pairCountX2 n := by
  unfold casimirAntisymX2N pairCountX2
  ring

/-- **The two-body sum is exactly proportional to the pair count, for every `N`.**
`2N·S(n) = −(N+1)·C(n,2)`, stated here as `4N·S = −(N+1)·2C(n,2)`.

This is the load-bearing statement: such an interaction contributes a constant
per pair, hence a constant coordination weight, hence `b₃ = 0`. No
antisymmetric-column Casimir of any `SU(N)` can carry three-body content. -/
theorem pairSum_eq (n N : R) :
    pairSumX4N n N = -((N + 1) * pairCountX2 n) := by
  unfold pairSumX4N casimirAntisymX2N casimirFundX2N pairCountX2
  ring

/-- Proportionality in the form that shows no `n`-dependence survives for a
coordination weight to inherit: the two-body sum plus `(N+1)` times the pair
count vanishes identically. -/
theorem pairSum_add_eq_zero (n N : R) :
    pairSumX4N n N + (N + 1) * pairCountX2 n = 0 := by
  rw [pairSum_eq]; ring

/-- `SU(4)`, recovering the merged `SU4CasimirIsAffineInPairCount` result:
`4·4·S = −5·2·C(n,2)`, i.e. `S = −(5/8)·C(n,2)`. -/
theorem pairSum_su4 (n : R) : pairSumX4N n 4 = -(5 * pairCountX2 n) := by
  rw [pairSum_eq]; norm_num

/-- `SU(3)` — **the eightfold way's own flavour group** — falls to the same
identity: `S = −(4/6)·C(n,2) = −(2/3)·C(n,2)`. The eightfold way cannot supply a
three-body cumulant either. -/
theorem pairSum_su3 (n : R) : pairSumX4N n 3 = -(4 * pairCountX2 n) := by
  rw [pairSum_eq]; norm_num

/-- `SU(2)`, spin alone: `S = −(3/4)·C(n,2)`. -/
theorem pairSum_su2 (n : R) : pairSumX4N n 2 = -(3 * pairCountX2 n) := by
  rw [pairSum_eq]; norm_num

end QOU.Mass.AntisymmetricCasimirIsTwoBody
