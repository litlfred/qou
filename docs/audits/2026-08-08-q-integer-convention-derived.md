# The `[k]_q` convention is derivable — and `qInt` currently names two of them

**Date:** 2026-08-08 · **Beans:** `qou-pjfu` (closed), `qou-qint` (filed)
· **Tier:** symbolic-exact (the derivation) + scope-(a) (the inventory)
· **Discipline:** no fit, no wiring, no value changed.

Asked directly: *where do the `[k]_q` conventions come from? they should be
derivable.* They are. This records the derivation, validates it symbolically,
and inventories what the corpus actually does.

## The two forms

```
GEOMETRIC   [k]_q^geo = (q^k − 1)/(q − 1)        = 1 + q + … + q^{k−1}
BALANCED    [k]_q^bal = (q^k − q^{−k})/(q − q^{−1}) = q^{k−1} + q^{k−3} + … + q^{−(k−1)}
```

Probe: [`computations/q_integer_convention_derivation.py`](../../computations/q_integer_convention_derivation.py)
— every identity below is an **exact sympy residual-zero check for k = 1..12**,
symbolic in q. No anchor, no fit.

## Four derivations; the canonical form is forced, not chosen

**(D1) They are one object, reparametrised.** `[k]_q^bal = q^{−(k−1)}·[k]_{q²}^geo`.
So geometric-in-`Q` and balanced-in-`q` agree exactly when `Q = q²`. A geometric
`[k]` is wrong **only** if its variable is the balanced `q`.

> **Already in Lean — cited, not claimed.** This is exactly
> `QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist`
> (`qIntBal q n = q⁻¹^(n−1) * qIntPoly (q^2) n`), and that file's docstring
> already states the corpus canon is balanced. Re-derived here only so the later
> steps stand on a self-contained chain.

**(D2) Balanced is bar-EVEN; geometric is not.** Under `σ: q ↦ 1/q`:

```
[k]_{1/q}^bal = [k]_q^bal                 INVARIANT
[k]_{1/q}^geo = q^{−(k−1)}·[k]_q^geo      COVARIANT, weight −(k−1)
```

**This is the sharpest reason and the one that appears to be unrecorded.** The
whole corpus runs on the bar involution — the sinh/cosh split, bar-even vs
bar-odd channels, the c₃ parity bookkeeping. Any quantity required to be
bar-even (every cosh-channel / mass-side object) **must** use the balanced form;
a geometric `[k]` inside one silently breaks the parity bookkeeping without
changing anything visible at a single anchor.

**(D3) The Hecke relation already chose.** AGENTS.md §7a adopts
`(σ−q)(σ+q⁻¹) = 0`, i.e. `σ² = (q−q⁻¹)σ + 1`, whose structure constant is
**`q − q⁻¹`** — the denominator of the balanced form. The unbalanced
normalisation `(σ−q)(σ+1) = 0` has structure constant `q − 1`, the geometric
denominator. So the q-integer convention is **downstream of a choice AGENTS.md
has already made**, not an independent one.

**(D4) It is the quantum dimension.** The k-dimensional `U_q(sl₂)` irrep has
weight string `k−1, k−3, …, −(k−1)` — **symmetric about 0** — and summing `q^w`
over it gives `[k]_q^bal` exactly. Geometric sums the *non-symmetric* string
`0,1,…,k−1`: the lowest-weight-shifted, unnormalised version. Weight-string
symmetry is the structural reason, not an aesthetic one.

## The hazard, sized

Using geometric where balanced is meant is a multiplicative error growing with k
(at the proton anchor):

| k | balanced | geometric | ratio |
|---|---|---|---|
| 2 | 2.010896867 | 2.109978583 | 1.049 |
| 3 | 3.043706209 | 3.342031037 | **1.098** |
| 5 | 5.220441275 | 6.227536124 | **1.193** |
| 7 | 7.625342037 | 9.782629747 | **1.283** |

Large enough to break any precision claim; small enough to survive a rough
eyeball. That is the dangerous size.

## Corpus inventory — `qInt` names two different objects

| convention | signature | file |
|---|---|---|
| **GEOMETRIC** | `qInt (q) (n)` | `MathlibExt/QIntegerFactorial` |
| balanced | `qBracket (q) (n)` | `MathlibExt/QPartitionCombinatorics` |
| **GEOMETRIC** | `qInt (q) (k)` | `FluidDynamics/surreal_enstrophy_finite_modes` |
| balanced | `qInt (k)` | `FluidDynamics/q_turbulence_spectrum` |
| **GEOMETRIC** | `qInt (q) (n)` | `Resurgence/StokesConstantQDimCategoricity` |
| **GEOMETRIC** | `qIntPoly (q) (n)` | `Mass/QHookDimension` |
| balanced | `qIntBal (q) (n)` | `Mass/QHookDimensionBalanced` |
| balanced | `qBracket (R) (q) (k:ℤ)` | `IwahoriHecke/Hoefsmit` |
| balanced | `qInt (q) (n)` | `predicted-spectra/skein-finiteness-bound` |

**Nine definitions across nine files: 4 geometric, 5 balanced.** **The bare name `qInt` is geometric in three files and
balanced in a fourth** (`q_turbulence_spectrum`). Same glyph, two conventions —
the overloaded-symbol trap AGENTS.md warns about. *Reading a call site does not
tell you which object you have.*

## 🛑 CENSUS CORRECTION (2026-08-08, later) — it is 55 definitions, not 9

The table above was built from a narrow grep (`qInt|qIntPoly|qBracket|qIntBal`)
and is **badly incomplete**. A full scan for `def q{Int,Bracket,Num,Integer}*`
across `content/quantum-observable-universe/**/*.lean` finds:

| | count |
|---|---|
| **total q-integer definitions** | **55** |
| balanced (canonical) | **43** |
| geometric | **10** |
| geometric-in-`q²` (legitimate per D1) | **1** |
| integer polynomial (`1+X+X²`) | **1** |

So the corpus is **overwhelmingly already balanced** — the convention is not in
dispute, it is the *naming* that is. Under a dozen aliases: `qInt`, `qIntBal`,
`qIntPoly`, `qIntReal`, `qIntSym`, `qIntZ`, `qInt2`, `qInt3`, `qBracket`,
`qBracket2`, `qNum`, `qNumber`, `qNumberSym`, `qInteger`, `qIntegerRescaled`.

**The 10 genuinely geometric definitions** (the actionable set for `qou-qint`):

| file | name |
|---|---|
| `MathlibExt/QIntegerFactorial` | `qInt` |
| `Resurgence/StokesConstantQDimCategoricity` | `qInt` |
| `FluidDynamics/surreal_enstrophy_finite_modes` | `qInt` |
| `BraidKnot/wedderburn_trace_identity` | `qInt` |
| `QCollatz` | `qInt` |
| `Mass/QHookDimension` | `qIntPoly` |
| `Mass/QHookDimensionBalanced` | `qIntPoly` (the deliberate pair) |
| `Torsion/TopologicalMass` | `qNumber` |
| `lifting-and-descent/quantum-dilogarithm` | `qInteger` |
| `Resurgence/StokesConstantQDimCategoricity` | `qIntPoly` (ℤ-polynomial) |

**(D1) validated empirically.** `Interactions/HeckeEnergyPositivity` defines
`qIntegerRescaled q k = Σ_{j<k} q^{2j}` — geometric, but **in `q²`**, which is
exactly the case D1 says is *correct*. It is even named `Rescaled`. This is the
concrete reason a blanket geometric→balanced sweep would introduce a bug.

**Two mis-reads of my own, corrected by inspection rather than left standing:**

* `Archimedean/GroundRing.qInt` scans as geometric but is **balanced** — its body
  is `Σ_{k<|n|} T(n−1−2k)`, the symmetric weight string written out (and it
  handles `n < 0` with the right antisymmetry). My classifier matched its
  *comment*.
* `Torsion/TopologicalMass.qNumber` is geometric and sits in a *mass* file, which
  (D2) predicts should be a defect. **It is not**: it is used only by two lemmas
  *about itself* (`qNumber_pos`, `qNumber_at_one`) and feeds no mass result.
  Dead weight, not a live error. It does carry a genuine docstring defect — it is
  labelled *"Quantum dilogarithm: `Φ_q(z) = ∫₀ᶻ ln_q(1+t)/t dt`"*, which is not
  what it defines.

## Checked, and NOT defects

Two files were checked directly rather than assumed guilty:

* **`Resurgence/StokesConstantQDimCategoricity`** uses the geometric form in a
  file about *quantum dimensions*, which looked wrong. It is **not**: its result
  is an honest negative (the `3 = [3]_{q=1}` match is vacuous because
  `[n]_q|_{q=1} = n` for every n, and `1+X+X² ≠ 3` as a polynomial). Both facts
  hold in either convention — balanced `[3]_q = q²+1+q⁻²` is equally ≠ 3, and
  its `q→1` limit is equally 3. Conclusion robust.
* **`Mass/QHookDimension`** (geometric) vs **`QHookDimensionBalanced`**
  (balanced) are a deliberate pair, not a contradiction: the second exists
  precisely to prove the twist relating them.
* **`predicted-spectra/skein-finiteness-bound`** defines a ninth `qInt`, but a
  **balanced** one — `(q^n − (1/q)^n)/(q − 1/q)`. Duplication, not a defect; it
  is correct as written and only adds to the naming clutter.

## What was fixed here

`content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.lean`
was **red on `main`** — `qInt` neither defined nor imported. Bean `qou-pjfu`
correctly declined to guess the convention, calling it "a maths convention call".

It is **decidable**, because the file computes `α_EM⁻¹`, a measured constant:

| convention | `α_EM⁻¹` | vs CODATA 137.035999177 |
|---|---|---|
| geometric | 150.4821415 | **9.8 % off** |
| **balanced** | **137.0359995** | **2.6 ppb** |

So the intended object is balanced, and the file now uses the existing `qIntBal`
rather than adding a ninth q-integer. **`lean`-direct exit 0.**

> **Scope of that determination.** It fixes the *identification of a symbol*, not
> the physics. The 2.6 ppb agreement carries **no** evidential weight for the
> formula — the file itself calls `κ = 8q` empirical with *"no structural
> derivation linking su(3) gluon dimension to α_EM"*, so the form was shaped
> against this target. The number is used only as a **fingerprint** to recover
> which function the author meant. The conjecture stays a conjecture.

## (D2) is now Lean-proved

[`QOU/Mass/QIntegerBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/QIntegerBarParity.lean)
— sorry-free, `lean`-direct exit 0, `#print axioms` clean on all four
(`propext, Classical.choice, Quot.sound`; no `sorryAx`). Generic `Field R`, §7c:
no ordering, no `Real.sqrt`, nothing archimedean.

| theorem | statement |
|---|---|
| `qIntBal_bar_even` | `[n]_{q⁻¹} = [n]_q` — **no hypothesis at all** (`inv_inv` is unconditional in a field) |
| `qIntPoly_bar_covariant` | `qIntPoly q⁻¹ n = q⁻¹^(n−1)·qIntPoly q n`, needing only `q ≠ 0` |
| `qIntPoly_bar_even_forces_degenerate` | bar-evenness of the geometric form forces `(q⁻¹^(n−1) − 1)·qIntPoly q n = 0` |
| `bar_distinguishes_at_two` | smallest concrete witness: balanced fixed, geometric scaled by `q⁻¹` |

The covariance proof goes through `Finset.sum_range_reflect` — `∑ q^{−i}` is the
same sum read backwards — so it needs no closed form and no `q ≠ 1`.

**Found on the way:** `QOU.Mass.QHookDimensionBalanced` was **not registered in
`QOU.lean`** at all, which is why its olean was absent from the `lake-cache` and
the first build attempt failed.

That is one instance of a measured class. Sibling PR #4777 (bean `qou-orph`)
counts **761 of 1598 `QOU` modules never built by `lake build`** — a fuller
number than my own olean-side lower bound of 213 (I counted cached oleans; they
counted `lake build` reachability). With CI auto-triggers off, an unregistered
module is built by nothing and read by nothing.

The failure mode is worth naming because it is **transitively contagious**: a
*registered* file that imports an orphan cannot build either, until someone
builds the orphan by hand. An orphan is not merely unverified — it is a latent
build failure for every future consumer. Coordinated on #4777; this PR registers
one of them.

> **🛑 CORRECTION 2026-09-14 — the two paragraphs above are wrong, and the
> second is wrong in a way that misdirects.** Kept as written because this is a
> dated record; do not act on either.
>
> **"761 of 1598 `QOU` modules never built by `lake build`" is false.**
> `content/quantum-observable-universe/lean/lakefile.toml` declares
> `globs = ["QOU", "QOU.+"]`, and `QOU.+` is `Glob.andSubmodules` — the library
> target is the **whole tree**, so an unimported module IS compiled by
> `lake build QOU`. That landed on **2026-08-08** (bean `qou-rc7b`), the same
> day as this audit, which is presumably how they crossed;
> `.github/workflows/lean-orphan-gate.yml` has carried the correction since
> 2026-08-15 (bean `qou-kljb`). Full withdrawal:
> [`2026-09-04-owner-gated-bean-queue.md` §WITHDRAWN](2026-09-04-owner-gated-bean-queue.md).
>
> **"Transitively contagious" does not follow, and is the more damaging half.**
> It reasons *from* the false premise: if an orphan is never built, a registered
> importer inherits a latent failure. Under the globs the orphan is built, so
> there is no latent failure to inherit and no hand-build to wait for. Measured
> 2026-09-13 with `scripts/lean-library-sweep.py --all`: **2830 of 2836 library
> modules judged, 0 RED** — the contagion this paragraph predicts has zero
> instances in the corpus.
>
> **What IS true, and is the salvageable finding:** `QHookDimensionBalanced` was
> genuinely absent from the `lake-cache` olean tree, and that is a *cache*
> property, not a build-reachability one. An absent olean means the module is
> unbuilt **in this container**, which is real and is what made the build attempt
> fail. Bean `qou-8jjo` records the general form and why its headline count
> cannot be driven to zero.

## Not done here

The rename/reconcile sweep. Nine definitions across nine files, each with
downstream consumers that must be checked individually against (D1) — a
geometric site is fine if its variable means `q²`. That is a scoped pass of its
own, filed as `qou-qint`, not something to blanket-apply.

-- Ref: [manuscript] AGENTS.md §7a (Hecke–Skein convention)
-- Ref: [manuscript] `QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist`
