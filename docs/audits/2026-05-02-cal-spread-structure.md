# cal/m_e spread investigation — structural variable analysis

**Pair:** [`per_braid_tower_hybrid.py`](../../computations/per_braid_tower_hybrid.py)
+ jet-extension result memo
[`2026-05-02-a3-jet-extension-result.md`](2026-05-02-a3-jet-extension-result.md).

The A.3 jet-extension scaffold's q-Plancherel-descent lift only
shrank the per-atom cal/$m_e$ spread from 1.06% → 1.00% — a
**negative result**. The audit memo proposed two follow-up paths:
plot cal/$m_e$ against structural variables ($A$, $|N-Z|$, shell
structure) to find the spread's actual driver, and check the
$H_3$-at-$H_{3A}$ weight approximation. This memo lands the first.

## Per-atom data (level-0 hybrid + tail bound at $N_\text{jet} = 0$)

| atom | $A$ | $|N-Z|$ | cal/$m_e$ | (c − mean)/mean (ppm) |
|------|----:|-------:|---------:|------------------------:|
| D    |  2  | 0 | 0.991807 | **+5198** |
| 3He  |  3  | 1 | 0.989969 | +3335 |
| 3H   |  3  | 1 | 0.990156 | +3524 |
| 4He  |  4  | 0 | 0.985360 | **−1336** |
| 6Li  |  6  | 0 | 0.987319 | +649 |
| 7Li  |  7  | 1 | 0.987012 | +337 |
| 9Be  |  9  | 1 | 0.985700 | −992 |
| 12C  | 12  | 0 | 0.984378 | −2332 |
| 16O  | 16  | 0 | 0.983760 | −2958 |
| 40Ca | 40  | 0 | 0.981325 | **−5426** |

Mean cal/$m_e$ = 0.98668. Spread (max − min)/mean = **1.06%**.

## Single-variable fit: $\log A$ dominates

$$
  \mathrm{cal}/m_e \;\approx\; 0.99308 - 0.00334 \log A
$$

residual $\sigma \approx 1100$ ppm, max $|$residual$|$ = **3087 ppm at 4He**.

$1/A$ and linear-$A$ fits are worse ($\sigma$ = 1230, 1850 ppm
respectively). $|N-Z|/A$ and parity-of-$A$ correlations with the
$\log A$ residual are weak (0.34 and 0.31).

## Outlier-excluding fit collapses the spread

Refit **excluding D and 4He** (the two smallest, structurally
special atoms — D = simplest bound state, 4He = doubly-magic
$Z=N=2$):

$$
  \mathrm{cal}/m_e \;\approx\; 0.99366 - 0.00349 \log A
$$

| atom | $A$ | residual ppm |
|------|----:|-------------:|
| 6Li  |  6  | −82 |
| 7Li  |  7  | +149 |
| 9Be  |  9  | −284 |
| 12C  | 12  | −601 |
| 16O  | 16  | −214 |
| 40Ca | 40  | +554 |

Residual $\sigma$ = **345 ppm**, max = **601 ppm**. Bulk of the
spread is gone — and the headline 4He residual jumps to **−3458
ppm** (from a -1336 ppm "deviation from mean" → −3458 ppm
"deviation from log-A trend").

## Interpretation

**The 1.06% spread is dominated by 4He**, with D a small secondary
outlier. The remaining 8 atoms follow a clean $\log A$ scaling
with ~345 ppm scatter — about 16× the 22 ppb calibration floor
but vastly tighter than the headline number suggests.

Why 4He overpredicts:

1. **Doubly-magic, hardest to compute.** $Z = N = 2$ has the
   smallest partition count of any closed-shell atom; the
   $H_3$-at-$H_{3A}$ weight approximation (P2.2a in workplan)
   is most pronounced here.
2. **Descended $q$-Hecke contribution is non-negligible at A=4.**
   The descended trace decays as $e^{-A}$ (4He: $6 \times 10^{-7}$,
   12C: $10^{-46}$). At small $A$, the q-Hecke descended is
   ~$10^{-7}$ of the tower, so weight error in that channel
   matters more.
3. **Jet-tower truncation effect on shell structure.** Closed
   shells have the strongest binding; the level-0 hybrid sees
   only level-0 $\Phi_q$ contributions, missing the n≥1 shell-
   correction terms.

D's smaller +567 ppm residual (from the log-A trend excluding
itself) is consistent with the same explanation: smallest atom,
weight-approximation residual is largest.

## Why $\log A$?

A $\log A$ trend is structurally significant. Three candidate
origins (not mutually exclusive):

- **Finite-size / level-counting**. The number of jet levels
  needed to converge grows with $A$; the level-0 truncation error
  scales as $\log A$ if the per-level corrections are
  $\propto 1/n$.
- **q-Plancherel weight error**. The $H_3$-at-$H_{3A}$
  approximation introduces a per-strand error that compounds as
  $\log[3A]_q!$; the leading large-$A$ behaviour is $\propto A
  \log A$, matching the trend after the per-atom normalisation
  divides by $A$.
- **Coulomb-like A-dependence**. The cal/$m_e$ ratio is the
  binding-energy-per-nucleon discount; the SEMF Coulomb term is
  $-a_C Z(Z-1)/A^{1/3} \sim A^{2/3}$, but the **per-nucleon**
  Coulomb is $\sim A^{-1/3}$ — at log scale this is a slowly-
  varying contribution.

## Recommended next step

**Implement the $H_3$-at-$H_{3A}$ weight fix (P2.2a)**. Per the
existing workplan and `schur_weyl_symbolic.markov_trace_schur_weyl_eval`
infrastructure (already landed), switching the level-0 hybrid's
weight from $w_\lambda^{(H_3)}$ to $w_\lambda^{(H_{3A})}$ should
specifically improve 4He (where the weight error is largest).
If the resulting 4He residual drops by >2000 ppm, that closes
the dominant spread component.

Secondary investigation: jet-tower n=1 with **shell-structure-
aware correction** (not the universal q-Plancherel scaffold).
The level-1 contribution should grow at closed shells; if a
shell-aware level-1 lowers 4He's predicted mass by ~3500 ppm,
that closes the residual without needing to re-do the weight
calculation.

## Status

Spread investigation: **dominant variable is $\log A$; primary
outlier is 4He (doubly-magic)**. The "1.06% spread" headline is
misleading — most atoms agree to within ~350 ppm of a $\log A$
trend. The actionable fix is P2.2a (proper $H_{3A}$ weights),
not deeper jet-prolongation work.
