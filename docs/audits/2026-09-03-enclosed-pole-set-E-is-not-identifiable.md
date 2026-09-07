# The enclosed pole set `E` is not identifiable — and the branch locus is bar-symmetric

**Date:** 2026-09-03 · **Bean:** `qou-qx7j` · continues `qou-6v5l` (PR #6067) and `qou-u8oy`
**Lean:** `QOU.Brings.ColourCubicBranchLocus` (sorry-free) ·
**Probe:** [`colour_cubic_branch_locus_and_residue_vanishing_probe.py`](../../computations/probes/colour_cubic_branch_locus_and_residue_vanishing_probe.py) (exact, exit 0)

## The question

PR #6067 corrected `prop:sw-period-residue-sum` to range its residue sum over an
**enclosed subset `E`** of the branch points rather than over all of them — since
summing over every pole of a meromorphic 1-form on a compact surface gives zero —
and named identifying `E` as the open geometric content of the keystone
`a_D^(n) = lw(n−1)`.

**The answer is that the question is empty.** Under the classical-jet
prolongation there is nothing to enclose: every residue vanishes individually, so
every subset `E` gives period zero.

## 1. The branch locus is bar-symmetric — new, and exact

The colour cubic `f(X,z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)` has

```
Δ(z) = −(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)
```

whose coefficient list `[16, 24, 35, 50, 35, 24, 16]` is **palindromic**. The
corpus has had this polynomial written out exactly since
[`bring_cubic_monodromy_probe.py`](../../computations/probes/bring_cubic_monodromy_probe.py)
(its fact A1: degree 6, `gcd(Δ, Δ′) = 1`, six distinct simple branch points) and
**had never recorded that it is self-reciprocal**.

Consequences, all exact:

| fact | how it is established |
|---|---|
| `z⁶ Δ(1/z) = Δ(z)`, so the locus is invariant under `z ↦ 1/z` | exact identity; `branchLocus_inv_mem` |
| `w = z + 1/z` sends `Δ/z³` to `16w³ + 24w² − 13w + 2` | exact back-substitution; `w_cubic_of_palindromic` |
| that cubic has discriminant `−80000 < 0` ⟹ one real root, one conjugate pair | `sp.discriminant` over `ℚ` |
| the real root lies in `(−2, −1)` | `C(−2) = −4 < 0 < 23 = C(−1)`, IVT on **integer** evaluations; `w_real_root_mem_Ioo` |
| no rational root ⟹ irreducible over `ℚ` | rational-root test |
| a real `w` with `w² < 4` gives `\|z\| = 1` **exactly** | `\|z\|² = (w² + (4−w²))/4 = 1`; `normSq_root_eq_one` |

So the six branch points split **2 + 4**:

- **two bar-fixed points, exactly on the unit circle** — at `e^{±iθ}` with
  `2cos θ = w₀`, a cubic irrationality;
- **one bar-orbit of four**, two strictly inside and two strictly outside, with
  reciprocal moduli (measured: `0.9430955890717590` and `1.06033790380066254`,
  product `1.000000000000000000000000`).

`z ↦ 1/z` is the Hecke bar-involution. So the pole locus of `λ_SW^(n)` carries
the bar-involution, with the on-circle pair as its fixed points.

### The one natural contour is excluded

**The unit circle is not an admissible contour: it passes through two branch
points.** That is exactly the candidate the corpus's own `∮_{S_c}` notation
suggests, and it is ruled out on the geometry.

## 2. No residue survives — so no `E` works

`QOU.Brings.RamificationParityMonodromy` already carries the right local model:
at a simple ramification point `z = z_c + t²` it represents a Laurent expansion
by its coefficient function `f : ℤ → R` and defines

```
ddz f = fun e => ((e + 2 : ℤ) : R) • f (e + 2)
```

the coefficient form of `d/dz = (1/(2t)) d/dt`, with its exponent shift of
exactly `−2`. That file uses the shift's **evenness** (to show `ddz` commutes
with the covering monodromy `t ↦ −t`). This audit uses the **multiplier**, at the
one exponent where it vanishes:

```
(ddz f)(−2) = ((−2) + 2) • f 0 = 0 • f 0 = 0        for every f
```

The `t^{−2}` coefficient of a `z`-derivative is always zero, because the only
input that could reach it is the **constant** term, and differentiating a
constant kills it. Since `λ_SW^(n) = X^(n) dz = X^(n) · 2t dt`, the residue at a
simple branch point *is* that coefficient up to the nonzero factor `2`.

**Hence every residue of `λ_SW^(n)` vanishes, at every branch point, for every
`n ≥ 1`, independently of the Puiseux data.** `ddz_residue_slot_eq_zero` depends
on `[propext]` alone.

Nothing here rebuilds `ddz` — the result is about the corpus's own operator. The
general-`n` bookkeeping form, `∏_{i<n}(2n−2−2i) = 0`, is kept as
`chain_factor_eq_zero` because the probe tabulates it.

**Non-vacuity.** `ddz` is not identically zero
(`ddz (monomialCoeff 2) 0 = 2` over `ℤ`), and the Puiseux coefficients the chain
factor kills are themselves nonzero (measured at 60 dps: `a₀ = X_k =
−0.07208520691 + 0.6383267351i` at the first branch point, whose two colliding
roots agree to `4.1e-31`). So the vanishing is caused by the operator's parity,
not by the absence of a term.

## This is a third route, not a discovery

The conclusion is one the corpus already holds. Recorded plainly because the
corpus-grep found it before any of this was written up as new:

| route | assumes | driven by | scope |
|---|---|---|---|
| `prop:sw-classical-jet-exactness` | `λ_SW^(n) = d(X^(n−1))` is exact, so each residue vanishes | a **global primitive** | classical-jet reading |
| `QOU.Brings.period_eq_zero_of_total_residue_vanishes` (#6067) | only the **total** residue vanishes | the **ambient compact surface** | any reading summing over all poles |
| `ddz_residue_slot_eq_zero` (here) | nothing beyond the local model | the **parity of `(1/2t)d/dt`** | any reading, per-point |

The third assumes least and is local: it needs neither a global primitive nor
the surface. All three leave the q-difference prolongation untouched.

## What this re-scopes

**Identifying `E` is not the open problem.** The open problem is upstream of it:
*which prolongation*. Under the classical-jet rule the `E`-question has no
content, and `prop:sw-period-residue-sum`'s enclosed-subset formulation — correct
as far as it goes — cannot be completed within that rule.

This does not weaken the keystone `a_D^(n) = lw(n−1)`, which remains a §3b class
with no instance, and it does not touch the q-difference prolongation, where
`RamificationParityMonodromy` already locates the missing structure (its walls
W1–W3: q-jet-bundle / q-D-module symbol calculus, absent from Mathlib and the
corpus).

> 🛑 **Scope correction (2026-09-06, bean `qou-p6m1`).** The claim above bundles two objects. The **q-D-module symbol calculus is PRESENT** — `QOU.Machinery.QuantumTorusSymbol` (QDM-1/2, 19 decls, sorry-free, on `main` by 2026-07-24) and `QOU.Mathlib.RamifiedShiftCalculus` (the same calculus at the ramified pole `z = z_c + t²`, sorry-free, 2026-09-03, and it *imports* `RamificationParityMonodromy`, the file that declared it absent). Only the **q-jet bundle over `Σ`** is absent. **W1 (construct `D_q` from `Σ`) still stands** — this is a scoping split, not a downgrade.


## Two defects found in passing

- **`sw_period_growth_probe.py` does not run on `main`.** It exits 1 before any
  of its own output, on `mpmath` `NoConvergence`: `polyroots` is called at a
  branch point with the default `maxsteps=50`, and two roots collide there — the
  probe's own subject breaks its solver. It also pushed the discriminant's exact
  integer coefficients through `complex(c)`, i.e. float64. Both fixed here;
  the sheet gap now resolves to `4.072e-36` and the probe exits 0.
- **Its closing claim is withdrawn.** It reported the verdict "CONFIRMED two
  ways: branch-point Puiseux (here) AND the corpus residue sum
  (`prop:sw-period-residue-sum`: residues = per-block Wedderburn `dim_q` = lw)".
  The second route is gone: those residues are not merely mis-summed, they are
  individually zero, so they are not the per-block `dim_q` and that leg confirms
  nothing. The branch-point Puiseux argument for super-exponential growth, and
  the lw/#1765 verdict, are untouched — the finding is kept and only its support
  corrected.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/colour_cubic_branch_locus_and_residue_vanishing_probe.py
PYTHONPATH=computations python3 -u computations/sw_period_growth_probe.py
```
