/-
Copyright (c) 2026 litlfred. All rights reserved.

# The color spectral curve is a q-integer curve (W1 structural handle)

Second concrete ingredient of the open W1 wall (bean `qou-d8de`: construct the
q-difference prolongation `D_q` on the color spectral curve `Σ`). Companion to
`QDiffProlongationBaseOperator` (the base q-shift operator): this records why the
q-shift acts *naturally* on `Σ`, by exhibiting `Σ` itself as a **q-integer object**.

The color spectral cubic (`ColorSpectralCubicGeometry`, `def:color-spectral-cubic`) is

  `C_z(X) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`.

Its coefficients are **exactly the quantum integers** `[k]_z = ∑_{i<k} z^i`:

  `C_z(X) = [1]_z·X³ + [2]_z·X² + [3]_z·X + [4]_z`   (`z+1 = [2]_z`, `z²+z+1 = [3]_z`,
  `z³+z²+z+1 = [4]_z`).

**Why this is the W1 handle.** The base operator brick showed the q-shift produces
`[n]_q` (`jackson_monomial_numerator`). Here the *curve* is built from `[k]_z` — so the
base q-shift `z ↦ q·z` acts on each coefficient through the q-integer functional
equations (`qInt_succ`: `[k+1]_z = [k]_z + z^k`), i.e. `Σ` carries a natural q-shift
structure. This is the structural reason a q-difference prolongation — not the
classical `d/dz` — is the geometrically-adapted operator on `Σ`, and it is computed
**from `Σ` itself**, independently of the C1 kernel (no circularity, no fit).

**Scope (structural identity, not the prolongation).** This proves the coefficient
identity only. It does **not** build the jet-tower lift `Jⁿ E → Jⁿ⁺¹ E` (the open W1
core), extract a symbol (W2, `qou-xufp`), or assert `symbol = C1` (W3, `qou-ailp`) —
those stay beaned, and no conjecture-class asserting the identification is defined
(anti-laundering). §7c: identity over generic `CommRing` (`geomSum_form`); `[k]_z`
naming over `Field` (`qInt_form`). Sorry-free. No fit; nothing wired.

-- Ref: [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1/G1)
-/
import QOU.MathlibExt.QIntegerFactorial

namespace QOU.Mass.ColorCurveQIntegerForm

open Finset
open QOU.MathlibExt

/-! ## Disambiguation (`qInt`)

`QOU.Mass.qInt` (`QHookDimension`) is the **balanced** q-integer
`∑_{i<n} q^{2i-(n-1)}`; the geometric `∑_{i<n} q^i` this file means is
`QOU.MathlibExt.qInt`. Lean resolves a bare name against the enclosing namespace
before an `open`ed one, so inside `namespace QOU.Mass.*` a bare `qInt` is the
**balanced** one however this file opens `QOU.MathlibExt`. Every reference below is
therefore fully qualified: the bare form compiled against the wrong convention from
`1646b5d6d3` until this was fixed, and a bare form reintroduced here would silently
mean different mathematics again. Bean `qou-lksc`. -/

/-- **The color spectral cubic** `C_z(X) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`
(`def:color-spectral-cubic`). -/
def colorSpectralCubic {R : Type*} [CommRing R] (z X : R) : R :=
  X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X + (z ^ 3 + z ^ 2 + z + 1)

/-- **q-integer form (over any `CommRing`).** The cubic's coefficients are the
truncated geometric sums `∑_{i<k} z^i` for `k = 1,2,3,4` — i.e. `C_z` is
`∑_{k=1}^{4} (∑_{i<k} z^i)·X^{4−k}`. -/
theorem colorSpectralCubic_geomSum_form {R : Type*} [CommRing R] (z X : R) :
    colorSpectralCubic z X
      = (∑ i ∈ range 1, z ^ i) * X ^ 3 + (∑ i ∈ range 2, z ^ i) * X ^ 2
        + (∑ i ∈ range 3, z ^ i) * X + (∑ i ∈ range 4, z ^ i) := by
  simp only [colorSpectralCubic, Finset.sum_range_succ, Finset.sum_range_zero]
  ring

/-- **q-integer form (named, over a `Field`).** `C_z(X) = [1]_z·X³ + [2]_z·X² +
[3]_z·X + [4]_z`, reusing the corpus quantum integer `QOU.MathlibExt.qInt z k = [k]_z` (the
geometric one — see the disambiguation note above). The color
spectral curve is a **q-integer curve** — the structural handle for lifting the base
q-shift to `Σ`. -/
theorem colorSpectralCubic_qInt_form {K : Type*} [Field K] (z X : K) :
    colorSpectralCubic z X
      = QOU.MathlibExt.qInt z 1 * X ^ 3 + QOU.MathlibExt.qInt z 2 * X ^ 2
        + QOU.MathlibExt.qInt z 3 * X + QOU.MathlibExt.qInt z 4 := by
  simpa [QOU.MathlibExt.qInt] using colorSpectralCubic_geomSum_form z X

/-- **Coefficient q-integer ladder.** Consecutive coefficients differ by a pure power
of `z`: `[k+1]_z = [k]_z + z^k` (`qInt_succ`). So the four coefficients
`[1]_z, [2]_z, [3]_z, [4]_z` form a q-integer ladder — the functional-equation
structure through which the base q-shift `z ↦ q·z` acts on `Σ`. -/
theorem colorSpectralCubic_coeff_ladder {K : Type*} [Field K] (z : K) (k : ℕ) :
    QOU.MathlibExt.qInt z (k + 1) = QOU.MathlibExt.qInt z k + z ^ k :=
  qInt_succ z k

end QOU.Mass.ColorCurveQIntegerForm
