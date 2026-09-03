# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the Charlier–Claeys / CDI upload — the sine-kernel Toeplitz tool is now in-corpus and its constant is verified; the variance rate is still the open RH step

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bulk-rate-derivation-2026-08-29` · **Tier:**
literature ingestion + primary-source mapping + a verified determinant-level brick (piece 2) ·
**Discipline:** no fake closure; these two papers move the gap materially but do **not** close it, and
this note states exactly why. **Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

Per the owner's directive to *do the derivation* and the two supplied papers: ingest, map to the gap
with exact theorem/equation numbers, lay one more rigorous brick, and flag the irreducible step
honestly.

## The two papers (ingested this branch)

- **`charlier-claeys2015`** = Charlier & Claeys, *"Asymptotics for Toeplitz determinants: perturbation
  of symbols with a gap"* (arXiv `1409.0435v2`, `library/arxiv-1409.0435v2/`, 28 pp / 14 sections).
- **`corwin-deift-its2022`** = Corwin, Deift & Its, *"Harold Widom's work in random matrix theory"*
  (arXiv `2201.05665v1`, `library/arxiv-2201.05665v1/`, 16 pp / 8 sections).

Both registered in [`content/schema/references.ts`](../../content/schema/references.ts) with library
docids.

## What Charlier–Claeys gives, precisely (exact statements)

1. **Widom's arc-Toeplitz asymptotic** (their eq (1.3), attributed to Widom [22]). For the
   arc-indicator symbol `f = 1` on `[−θ₀,θ₀]`, `0` else (`s=0`, `W=0`):
   `ln D_n = n² ln sin(θ₀/2) − (1/4) ln n − (1/4) ln cos(θ₀/2) + c + o(1)`, with
   **`c = (1/12) ln 2 + 3ζ′(−1)`** — the des Cloizeaux–Mehta / Dyson / Widom constant.
2. **The double-scaling extension** (Theorem 1.1): the same Widom asymptotic persists for
   `0 ≤ s ≤ e^{−x_c n}`, with error **`O(n^{−1/2} e^{x_c n} s)`** (their eq (1.9)).
3. **The sine-kernel Fredholm determinant** (Application 2, eqs (1.23)–(1.29)): in the double-scaling
   limit `θ₀ = π(1 − 2y/n)`, `D_n → det(1 − (1−s)K_y)` with `K_y` the **continuous** sine kernel
   `sin π(x−t)/π(x−t)` on `(−y,y)`, and
   `ln det(1 − (1−s)K_y) = −π²y²/2 − (1/4) ln πy + c + O(y^{−1})`, **same `c`**.
4. **The rate mechanism**: the RH steepest-descent analysis matches a **local (modified Bessel)
   parametrix** to the **global parametrix** with `P = (I + O(n^{−1})) P^{(∞)}` (their eq (4.22)). The
   `O(n^{−1})` there is the structural origin of the sub-leading correction.

`corwin-deift-its2022` is the **survey** that pins Widom's sine-kernel-determinant references (the
bulk emptiness-formation probability "answering Dyson") and lays out the **sine (bulk) vs Airy (edge)**
regime split — context, not a primary rate computation.

## Piece 2 — the Widom/CC constant is verified at the Toeplitz level (rigorous brick)

[`wlambda_covariance_epic_M1_widom_arc_toeplitz_constant_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_widom_arc_toeplitz_constant_probe.py)
computes the **actual** finite-`n` arc-indicator Toeplitz determinant `D_n(0, π/2, 0)` by Cholesky
(the matrix is PSD; `f_k = sin(kθ₀)/(kπ)`, `f_0 = θ₀/π`), NO float64, `dps=60`, and forms
`ĉ(n) = ln D_n − n² ln sin(θ₀/2) + (1/4) ln n + (1/4) ln cos(θ₀/2)`.

| n | ĉ(n) | ĉ(n) − c | n²·(ĉ−c) | slope p |
|---|---|---|---|---|
| 16 | −0.4384393 | 6.18e−5 | 0.01583 | — |
| 32 | −0.4384859 | 1.53e−5 | 0.01568 | 2.009 |
| 48 | −0.4384944 | 6.79e−6 | 0.01565 | 2.003 |
| 64 | −0.4384973 | 3.82e−6 | 0.01564 | 2.002 |

`ĉ(n) → c = −0.438501166…` monotonically, confirming **`c = (1/12) ln 2 + 3ζ′(−1)`** to ~6 digits at
the determinant level — an independent, self-contained verification of the tool cited as
`charlier-claeys2015`, with no quadrature or discrete↔continuous normalisation to launder.

**Measured, and worth stating:** the residual decays as **`n^{−2}`** (slope `p → 2.002`,
`n²·(ĉ−c) → 0.0156`), NOT `n^{−1}` — the odd `n^{−1}` term cancels by the even-symbol symmetry
`f(e^{iθ}) = f(e^{−iθ})`. (My first pass wrote `~1/n`; the measurement corrected it.)

## Why this does NOT close the gap (the honest reason)

The quantity `qou-k5r5` needs is `V_A(θ) = Var_Planch(Σ|c|)/θ² → 8/π²` **with its rate** — a
**linear-statistic variance** of the **Plancherel** descent DPP. Charlier–Claeys and the CDI survey
are about:

| | Charlier–Claeys / CDI | what qou-k5r5 needs |
|---|---|---|
| **ensemble** | CUE arc-counting / continuous sine kernel | Plancherel descent DPP / discrete Bessel kernel (BOO) |
| **functional** | Fredholm/Toeplitz **determinant** (gap probability, MGF of a counting statistic in the large-deviation `s→0` regime) | **linear-statistic variance** `Var(Σ|c|)` (a `∂²_λ` at `λ=0`, the smooth/Szegő regime) |
| **sub-leading rate** | `n^{−2}` (symmetric arc, measured above) or `O(y^{−1})` (sine det) | `θ^{−1}` (measured, `qou-tvok`) |

They are the **right kernel neighbourhood** (both limit to the sine kernel) and the **right method**
(RH double-scaling, `O(n^{−1})` parametrix matching), and they now put the **rigorous sine-kernel
determinant + its constant in-corpus and verified**. But the variance of `Σ|c|` is a **different
(adjacent) functional** of the **Plancherel** kernel, and its rate constant is not any quantity these
papers state. The `n^{−2}` measured above vs the `θ^{−1}` of the variance is the numerical
fingerprint of that functional mismatch.

## The one remaining rigorous step (unchanged in kind, better equipped)

Write the DPP linear-statistic variance `V_g(θ) = ½ Σ_{x≠y}(g(x)−g(y))² J(x,y;θ)²` with `J` the BOO
discrete Bessel kernel, split into bulk (`J → S`, the sine kernel, now with the CC/Widom rate tool)
+ edge (Airy, BDJ) + tail (proved, Johansson 3.9), and carry out the **summation-by-parts /
stationary-phase cancellation** of the bulk cross-term `2 Σ S·E` (the `qou-tvok` `θ^{−1}`) with an
explicit constant. This is the original Riemann–Hilbert computation. It is now backed by a verified,
in-corpus determinant-level tool and constant — but the constant for **this** functional is not
handed over by any cited paper, and per the anti-laundering discipline it will not be fabricated.

## Status of `qou-k5r5`

Gap **OPEN**. Inventory after this upload: leading margin **proved** (ρ_P = 2√6/5, rigorous V_D
ceiling); tail **proved** (Johansson 3.9); de-Poissonization **cited**; leading variance `8/π²`
**cited** (IO); Debye bulk tool **verified** (piece 1, #6002); **Widom/CC sine-kernel Toeplitz constant
verified** (piece 2, this note) with the sine-kernel determinant machinery now in-corpus and citable.
The open piece is the Plancherel linear-statistic variance **rate constant** — the RH cross-term
cancellation — a different functional than any cited paper computes.

## Compute + sources

- [`wlambda_covariance_epic_M1_widom_arc_toeplitz_constant_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_widom_arc_toeplitz_constant_probe.py) (exit 0; NO float64; `c` verified, residual `~n^{−2}`).
- `charlier-claeys2015` = `library/arxiv-1409.0435v2/` (Thm 1.1, Application 2, eq (4.22)).
- `corwin-deift-its2022` = `library/arxiv-2201.05665v1/` (sine-kernel determinant survey).

## Cross-references

- Piece 1 (Debye bulk tool): [`2026-08-29-covariance-kernel-M1-k5r5-research-piece1-debye-verified.md`](2026-08-29-covariance-kernel-M1-k5r5-research-piece1-debye-verified.md)
- Regime structure (BDJ = edge): [`2026-08-29-covariance-kernel-M1-k5r5-regime-structure-BDJ-is-the-edge.md`](2026-08-29-covariance-kernel-M1-k5r5-regime-structure-BDJ-is-the-edge.md)
- Cited-inputs Lean class: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/M1DescentDPPConvergence.lean`
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
