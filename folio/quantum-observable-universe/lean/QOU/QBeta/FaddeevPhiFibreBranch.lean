/-
# Fibre-branch (root-of-unity) Faddeev-Φ-analog discharge (Φ_b workplan result L3)

This is the **payoff** of the Φ_b combinatorial workplan (bean `qou-lgpb`,
PR #3768): a *genuine, sorry-free* discharge of a Faddeev-Φ-style shift structure
on the `|q| = 1` **root-of-unity fibre branch**, complementing
`QOU.MathlibExt.PhiBProd`'s discharge on the `Im b² > 0` **substrate branch**.
Together the two branches close gap **G2** (fibre-regime construction) of
`docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`.

## What is proved

Building on **L1** (`cyclotomic_collapse`) and **L2**
(`QOU.QBeta.CyclicQuantumDilog`, in particular the proved boundary-trade
`cyclicDenom_shift_factor` and the root-of-unity periodicity `cyclicDenom_shift`),
this file:

1. Defines the fibre-branch analog class `CyclicFaddeevPhi ζ N D`, carrying the
   *multiplicative* shift laws that **actually hold** on the cyclic branch as its
   defining fields — the finite **boundary-trade** law and the exact
   **N-periodicity** — in the same spirit as `FaddeevPhi b Φ` carries its two
   additive `q`-difference equations.
2. **Discharges it unconditionally**: `cyclicFaddeevPhi_cyclic` proves the finite
   q-Pochhammer denominator `x ↦ (x;ζ)_N` is a genuine `CyclicFaddeevPhi` instance
   at every primitive `N`-th root of unity `ζ` (`N > 0`), sorry-free, from L2's
   proved shifts. This is the fibre-branch existence-with-shift-equations — the
   direct analog of `PhiBProd.faddeevPhi_phiBProd_substrate`.
3. Derives consequences (iterated periodicity, the polynomial collapse of the
   carrier, guard-free dilog periodicity) purely from the class fields / L2.

## Honest scope: the parametrization mismatch (no ℂ-`FaddeevPhi` bridge theorem)

The exact `QOU.MathlibExt.FaddeevQuantumDilogarithm.FaddeevPhi` class is
**additive-analytic over ℂ**: its `shift_b` is
`Φ(z − ib/2) = (1 + e^{2πbz})·Φ(z + ib/2)`, an equation on `ℂ → ℂ` with the
`(1 + e^{2πbz})` multiplier *present*. The cyclic-branch object here is
**multiplicative-algebraic** in `x` over a generic field at `ζ = ζ_N`: its
defining shift is the **exact N-periodicity** `D(ζ·x) = D(x)`, in which the
multiplier is **absorbed** by the cyclic wrap-around (L2 §docstring: `1 − x·ζ^N =
1 − x` at `ζ^N = 1`, so top and bottom boundary factors cancel).

Under the intended change of variable `x = e^{2πbz}` the multiplicative shift
`x ↦ ζ·x` is the additive shift `z ↦ z + ib/2` (with `ζ = e^{iπb²}`), so the two
*shapes* correspond — but the multipliers do **not**: FaddeevPhi keeps
`(1 + e^{2πbz})`, the cyclic branch degenerates it to `1`. Forcing `D(ζx) = D(x)`
into `shift_b` would require `1 + e^{2πbz} = 1`, i.e. `e^{2πbz} = 0`, which is
impossible for any `z`. **There is therefore no honest sorry-free bridge that
makes the cyclic dilog an instance of the exact ℂ-`FaddeevPhi` class**, and none
is asserted here — the correspondence is a genuine *degeneration* of the
functional equation at the root of unity, recorded in this docstring rather than
faked as a theorem. The defensible deliverable is precisely the faithful
fibre-branch class `CyclicFaddeevPhi` and its unconditional discharge below.

All results are generic over a field `K` (never specialised to `ℂ`), per §7c.

-- Ref: [faddeev1995] Faddeev, "Discrete Heisenberg–Weyl group and modular
--        group", Lett. Math. Phys. 34 (1995) 249. https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md
-/
import QOU.QBeta.CyclicQuantumDilog

namespace QOU.QBeta.FaddeevPhiFibreBranch

open Finset
open QOU.QBeta.CyclicQuantumDilog

variable {K : Type*} [Field K]

/-- **Fibre-branch Faddeev-Φ shift structure** (the root-of-unity / `|q| = 1`
analog of `QOU.MathlibExt.FaddeevQuantumDilogarithm.FaddeevPhi`).

A carrier `D : K → K` (think `D x = (x;ζ)_N`, the finite q-Pochhammer
denominator) at a primitive `N`-th root of unity `ζ` satisfies the two
*multiplicative* shift laws that genuinely hold on the cyclic branch:

* `shift_factor` — the **finite boundary-trade** law, the honest finite analog of
  the Faddeev shift `Φ(q²x) = (1 + qx)Φ(x)`: scaling the argument by `ζ` trades
  the bottom boundary factor `(1 − x)` for the top factor `(1 − x·ζ^N)`.
* `periodic` — the **exact N-periodicity** `D(ζ·x) = D(x)`, in which the
  `(1 + qx)`-type multiplier of the *infinite* Faddeev shift is **absorbed** by
  the cyclic wrap-around (`ζ^N = 1` makes the top and bottom boundary factors
  cancel).

Both fields carry genuine content (neither is `True` or an empty marker), per
the §3b-tax "carrier must assert something" rule. The class is discharged
unconditionally by `cyclicFaddeevPhi_cyclic` below. -/
class CyclicFaddeevPhi (ζ : K) (N : ℕ) (D : K → K) : Prop where
  /-- `N > 0` (the cyclic order is positive — the fibre analog of `FaddeevPhi`'s
  `0 < b.re`, i.e. a nondegenerate modular parameter). -/
  hN : 0 < N
  /-- `ζ` is a primitive `N`-th root of unity — the `|q| = 1` fibre datum. -/
  hζ : IsPrimitiveRoot ζ N
  /-- Finite boundary-trade shift law (finite analog of the Faddeev
  `Φ(q²x) = (1 + qx)Φ(x)` shift). -/
  shift_factor : ∀ x : K, (1 - x) * D (ζ * x) = (1 - x * ζ ^ N) * D x
  /-- Exact N-periodicity at the root of unity: the infinite-shift multiplier is
  absorbed by the cyclic wrap-around. -/
  periodic : ∀ x : K, D (ζ * x) = D x

variable {ζ : K} {N : ℕ} {D : K → K}

/-- **Iterated periodicity**: `D(ζ^j·x) = D(x)` for every `j`. The single
`ζ`-shift `periodic` iterated `j` times — the "closes as a finite N-step
recursion" statement (indeed period `1` in the `ζ`-scaling). Derived purely from
the class fields. -/
theorem cyclicFaddeevPhi_periodic_pow [h : CyclicFaddeevPhi ζ N D] (x : K) (j : ℕ) :
    D (ζ ^ j * x) = D x := by
  induction j with
  | zero => simp
  | succ n ih =>
    have e : ζ ^ (n + 1) * x = ζ * (ζ ^ n * x) := by ring
    rw [e, h.periodic, ih]

/-- **Discharge of the fibre-branch shift structure** (the payoff, closing G2).

At *every* primitive `N`-th root of unity `ζ` (`N > 0`), the finite q-Pochhammer
denominator `x ↦ (x;ζ)_N = ∏_{k<N}(1 − x·ζ^k)` is a genuine `CyclicFaddeevPhi`
instance: it satisfies the finite boundary-trade shift law
(`cyclicDenom_shift_factor`, L2) and the exact N-periodicity
(`cyclicDenom_shift`, L2). Unconditional, sorry-free — the fibre-branch analog of
`PhiBProd.faddeevPhi_phiBProd_substrate`. -/
theorem cyclicFaddeevPhi_cyclic (hN : 0 < N) (hζ : IsPrimitiveRoot ζ N) :
    CyclicFaddeevPhi ζ N (fun x => cyclicDenom ζ x N) where
  hN := hN
  hζ := hζ
  shift_factor x := cyclicDenom_shift_factor ζ x N
  periodic x := cyclicDenom_shift hN hζ x

/-- The discharged carrier is concretely the finite polynomial `1 − x^N`
(L1/L2 collapse `cyclicDenom_eq`) — evidence the fibre object is non-vacuous:
`CyclicFaddeevPhi` is realised by an honest, explicitly-computable function, not a
formal placeholder. -/
theorem cyclicFaddeevPhi_cyclic_carrier_eq (hN : 0 < N) (hζ : IsPrimitiveRoot ζ N)
    (x : K) : (fun x => cyclicDenom ζ x N) x = 1 - x ^ N :=
  cyclicDenom_eq hN hζ x

/-- **Bonus — guard-free periodicity of the cyclic dilog** `Φ(x) = (x;ζ)_N⁻¹`:
`Φ(ζ·x) = Φ(x)` (L2 `cyclicDilog_shift`, the reciprocal of the denominator's
periodicity). The full reciprocal boundary-trade law carries
nonzero-denominator guards, so the dilog is not made a complete
`CyclicFaddeevPhi` instance here; periodicity is its guard-free half, and it is
the closest form to the *invariance* the infinite Faddeev shift would want. -/
theorem cyclicFaddeevPhi_dilog_periodic (hN : 0 < N) (hζ : IsPrimitiveRoot ζ N)
    (x : K) : cyclicDilog ζ (ζ * x) N = cyclicDilog ζ x N :=
  cyclicDilog_shift hN hζ x

end QOU.QBeta.FaddeevPhiFibreBranch
