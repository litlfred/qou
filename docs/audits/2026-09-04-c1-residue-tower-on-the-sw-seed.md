# The C1 residue tower on the actual Σ seed — a scope-(a) negative, and an underdetermination count

**Date:** 2026-09-04 · **Bean:** `qou-an6y` · follows `qou-col1` (#6628), `qou-w0tx` (#6610), `qou-33hb` (#6582)
**Probe:** [`c1_residue_tower_sw_seed_probe.py`](../../computations/probes/c1_residue_tower_sw_seed_probe.py) (mpmath 80 dps for the algebraic seed; exact sympy for the counting; no float64)
**Lean backbone:** `QOU.Mass.C1KernelLevelReading.twoOp_c1RecFrom_two_iff` (#6628) — this tranche adds a measurement against it, not new Lean.

## What was asked

#6628 established, sorry-free, that for a derivative-only two-term tower
`D = c₂(e)S₂ + c₁(e)S₁` the residues `r_n = (Dⁿ X)(−2)` satisfy the C1 recurrence
`[n+2]_q r_{n+2} = r_{n+1} + r_n` from level 2 **iff** the tower's `t¹`-coefficients
`s_m = (Dᵐ X)(1)` satisfy `[m+4]_q s_{m+2} = s_{m+1} + s_m`, and its probe measured that
the level-`m` constraint reads seed slots `a_{m+3}..a_{2m+5}` only. With a generic seed
the recurrence is therefore always satisfiable by choosing the tail — so whatever
content the conjecture's "symbol = `L_K`" has on the level axis sits in the **seed**,
which the geometry fixes. Two questions follow, and both are finite computations:

1. On the seed Σ actually supplies, do the two concrete derivative-only candidates
   (#6474's admissible class — Jackson `[e+1]_q σ` + q-`d/dz` `[e+2]_q σ²`) have a
   residue tower satisfying C1 from level 2?
2. With the seed fixed and the weights `c₁(e), c₂(e)` left free, is the level-axis
   identification a constraint on the weights at all?

## The seed

`X = X₀ + Σ_{k≥1} a_k t^k` is the Puiseux expansion of the colour cubic
`P(X,z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)` at `z = z_c + t²`, with `z_c` a root
of `disc_X P` and `X₀` the colliding double root — the same simple branch
[`zgeometric_ramification_parity_probe.py`](../../computations/probes/zgeometric_ramification_parity_probe.py)
uses. Coefficients by the order-by-order Newton step
`a_k = −[t^{k+1}] P(X₀ + S_{k−1}, z_c + t²) / (P_XX(X₀,z_c)·a₁)`, `a₁² = −2P_z/P_XX`.

| | value (12 digits shown; 80 dps carried) |
|---|---|
| `z_c` | `−0.974815532978 + 0.223012727585 i` |
| `X₀` | `−0.0720852069059 − 0.638326735148 i` |
| `a₁` (sheet +) | `0.709379325 − 0.709379325 i` |
| `a₂` | `−0.5720852069 + 0.2586289424 i` (sheet-independent) |
| `|P_X(X₀,z_c)|` after refinement | `1.05e−81` |
| re-substitution `|P(X(t), z_c+t²)|` through `t²²` | `1.02e−79` |

**One numerical trap, caught by the probe's own thresholds.** A double root returned
by `mp.polyroots` is determined only to *half* the working precision — measured
`|P_X| = 3.3e−41` at 80 dps, and the re-substitution residual sat at `6e−40`. Refining
`(X₀, z_c)` jointly by Newton on the nonsingular 2×2 system `P = P_X = 0` recovers
full precision (`1e−81`). The zgeometric probe's `|P_X| ≈ 6e−21` at its working
precision is the same effect one precision level down; its parity conclusions do not
depend on it, but any future exact use of that seed should refine first.

## Result 1 — scope-(a) negative: the two candidates fail on this seed

`d_n := [n+2]_q r_{n+2} − r_{n+1} − r_n`, `n = 2..6`, normalised by `max_{2≤n≤8} |r_n|`:

| convention | sheet | `q = 11/10` | `q = 3/2` | `q = 2` | `q = q₀` (proton) |
|---|---|---|---|---|---|
| balanced | + | 8.77 | 30.7 | 171 | 8.94 |
| balanced | − | 8.78 | 30.7 | 171 | 8.94 |
| geometric | + | 11.4 | 49.3 | 255 | 11.9 |
| geometric | − | 11.4 | 49.3 | 255 | 11.9 |

The defect is of order **1 to 100** relative to the residues themselves, at every `q`,
on both sheets, in both conventions. A C1 identity in `q` would vanish at each tested
`q` to 80 digits; this is not a precision artefact. `r_0 = r_1 = 0` as #6628 proves
(derivative-like shift 2 on a power-series seed), and `r_2 = κ a₁` with
`κ = c₁(−2)c₂(−1)` — `−1` balanced, `−1/q` geometric — as its `twoOp_residueSeq_add_two`
says.

**Scope (a).** This is *these two candidates, on this seed, alone*. It does not
exclude a derivative-only `D_q` with geometry-supplied weights, nor a `D_q` with a
non-derivative component (which #6582's level-0 argument says the conjecture needs
anyway if the recurrence is demanded from level 0). No invariant is cited, so no
scope-(b) claim is made.

## Result 2 — with free weights the constraint is underdetermined

Exact sympy, generic symbolic seed `a₀..a₁₅` and generic weights (`c₁(−1) = c₂(−2) = 0`
imposed, the derivative-only condition):

| level `m` | weight values in constraint `m` | of which new | enter linearly |
|---|---|---|---|
| 0 | 6 | 6 | yes |
| 1 | 10 | 4 | yes |
| 2 | 14 | 4 | yes |
| 3 | 18 | 4 | yes |

Each level introduces **at least four new weight unknowns**, all entering linearly,
against **one** constraint. So the level-axis identification "residues satisfy `L_K`"
places no constraint on a two-term derivative-only tower whose weights are free: for
any seed there are weight choices satisfying it at every level. The content of the
conjecture, on this axis, is entirely in *where the weights come from* — which is
wall W1 (`qou-d8de`, construct `D_q` from Σ), restated as a counting fact.

## What this says about the conjecture, and what it does not

- It does **not** refute `conj:qdifference-kernel-prolongation-symbol`. It refutes
  the cheapest way to satisfy it: taking the two textbook q-derivative towers as
  `D_q` and hoping the geometry's seed makes their residues C1. It does not.
- Combined with #6628: a derivative-only tower cannot carry C1 from level 0 at all
  (`r_0 = r_1 = 0`); from level 2 it can only if its weights are tuned, and the two
  natural untuned weightings fail. So on the level axis, "symbol = `L_K`" is a
  statement about `D_q`'s weights, and the weights are exactly what is not derived.
- The counting result is a *prune* for future work: do not fit weights to satisfy
  the recurrence — the count says a fit always exists, so a fit is evidence of nothing.

## Scope note added

One sentence-group appended to the level-reading paragraph of
`mass-theory/qdifference-kernel-prolongation-symbol.md`, scope-(a) labelled.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/c1_residue_tower_sw_seed_probe.py
```
