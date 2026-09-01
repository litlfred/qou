# Sparse Magnus-sign probe: measured optimization impact + the A-scaling ceiling

**Date:** 2026-08-30
**Context:** owner asked to "make use of all symmetry", "check impact of each
potential optimization", and warned "we may need to go much higher than 4" for
the Magnus Ω₂ sign-vs-A map (A=2 deuteron `qou-dp32`, A=3 triton #6107, A=4 ⁴He
#6183). This records what each optimization actually buys — **measured, not
estimated** — and where the method's ceiling is.

The quantity: `P(A) = Σ_{λ⊢3A} y_λ · tr(ρ_λ Ω₂_λ)`, `y_λ = d_q(λ)²/[n]_q!`,
`Ω₂ = ½Σ_{i<j}[A_{g_i},A_{g_j}]`, germ `A_g = q·∂_qσ_g·σ_g⁻¹`, `ρ = ∏σ_{g_i}`,
word `atom_braid_word_3A(Z,N)` (3 strands/nucleon ⇒ n = 3A strands, H_n).

## Measured impact of each optimization

| optimization | what it buys | measured | status |
|---|---|---|---|
| **Block-diagonal generators + germ** (Young seminormal is a ⊕ of 1×1/2×2 blocks; the germ inherits the blocks; exact 2×2 inverse) | avoids the dense `mp.zeros(dim,dim)` allocation and the O(dim³) `mp.inverse` | at H₁₂ the biggest block is 7700² ≈ 9 GB **per generator dense** → **<10 MB sparse**; dense OOM-crashes before any arithmetic | **THE enabler** — makes A=4 possible at all |
| **Matrix-free trace** (`ρ` never materialized; `tr(ρΩ₂)=Σ_k Σ_i Ω₂[k,i](ρe_k)[i]` via sparse mat-vec chains) | O(dim) memory instead of a dense dim×dim `ρ` | same OOM avoidance; time stays O(dim²·L) | **enabler** (memory) |
| **Far-commutativity** (`[A_a,A_b]=0` for `|a−b|≥2`) | fewer commutators in Ω₂ assembly | He4 word: **1081 crossing-pairs → 145 kept (13.4%)**; only **10 distinct** commutators to build; triton 595→106, 7 distinct | real **~7.5×** on Ω₂ **assembly** — but assembly is not the bottleneck (the trace loop is), so end-to-end effect is small |
| **Biggest-partition-first parallelism** (4 procs) | wall-clock | **4×** (4 cores); LPT-optimal makespan | in use |
| **Correctness gate** (sparse≡dense on λ⊢4..7; reproduce committed triton P_total) | correctness, not speed | matched triton to **rel 9.3e-61**, sign −1 | in use |

## Measured DEAD ENDS (tested, do not pursue)

- **Conjugate-partition (transpose) symmetry λ↔λ′ — REFUTED (0×).** Hoped for a
  clean `tr_{λ′} = ±tr_λ` (a rigorous 2×). Measured on the committed triton
  per-partition data: **14/14 conjugate pairs show no ±1 relation** (ratios
  −0.002, +0.024, −0.78, −4.85, …). The specific braid-word density ρ breaks the
  q→−q⁻¹ transpose covariance of χ_λ. scope-(a) negative: not transpose-covariant
  for this quantity.
- **Canonical-trace / Ocneanu-recursion collapse — DOES NOT APPLY.** It was
  claimed mid-session that `P = τ(ρΩ₂)` with τ the canonical symmetrizing trace
  (which would give a matrix-free `T_e`-coefficient route). **Tested and false:**
  `Σ_λ y_λ·dim_λ = 1,452,540.8 ≠ 1`, so `y_λ = d_q(λ)²/[n]_q!` is the
  **Wedderburn/Frobenius** weight (squared q-dimension), not the canonical-trace
  weight (τ(1)=1). P is a genuine d_q²-weighted Wedderburn sum with **no trivial
  collapse**; it is also not the regular-rep trace (that carries the ordinary-dim
  weight f^λ, not d_q²). The matrix-free-per-partition structure already in the
  probe is the right shape; there is no scalar shortcut around the partitions.

## The A-scaling ceiling (why "much higher than 4" needs a new method)

Per-partition trace cost is O(dim²·L) and `Σ_{λ⊢n} dim² = n!` (n = 3A). So the
flat-partition method's total cost scales as **n! = (3A)!**:

| A | nucleus | n=3A | #partitions | max dim (S_n) | Σdim² = n! | feasibility |
|---|---|---|---|---|---|---|
| 2 | ²H | 6 | 11 | 16 | 720 | trivial |
| 3 | ³H | 9 | 30 | 216 | 362,880 | ~min (#6107) |
| 4 | ⁴He | 12 | 77 | 7,700 | 4.8e8 | ~2 h, 4 cores (#6183) |
| 5 | ⁶Li | 15 | 176 | 2.0e5 | 1.3e12 | ~2700× A=4 — days–weeks, at the edge |
| 6 | — | 18 | 385 | 5.4e6 | 6.4e15 | **infeasible flat** |
| 8 | — | 24 | 1575 | ~10⁹ | 6.2e23 | **hopeless flat** |

**A=4 is the last atom feasible by flat-partition enumeration.** A=5 is already
~2700× A=4 (edge of feasible with the branching tower below; hopeless without).
A≥6 is out of reach for any method that enumerates S_n irreps.

### The only route to A≫4: the branching-basis tower

Do **not** enumerate λ⊢3A. Work in the iterated branching
`H_{3A} ↓ H_{3(A-1)} × H_3 ↓ … ↓ (H_3)^{×A}` (the machinery
`sublemma_2_1_h12_he4_branching.py` already uses for characters), so the full
dim-2e5+ rep is **never formed** — only small H_3-block pieces and the branching
coefficients. Two structural facts make this efficient and are the "all symmetry"
the word actually has:

1. **Nucleon-block structure of the word.** `atom_braid_word_3A` is A disjoint
   3-strand nucleon words (generators within `{3k, 3k+1}`) connected only by the
   inter-nucleon links `σ_2, σ_5, σ_8, …` (each multiplicity 1). So ρ is
   **nearly block-diagonal across nucleons** — it factors through the branching
   with only A−1 linking crossings mixing blocks. This is the "chained iterative
   factorization" via the GS/production pathway.
2. **Far-commutativity + the germ's locality.** A_g touches only strands g, g+1;
   Ω₂ keeps adjacent pairs only. In the branching basis these are local operators
   on adjacent H_3 blocks, so tr(ρΩ₂) becomes a **transfer-matrix contraction
   along the nucleon chain** — cost linear in A, not (3A)!.

This is a substantial new implementation (not a constant-factor tweak), and it is
the prerequisite for A=5 and the only path to A≥6. It is **not** started here.

## Bottom line for the author

- **A=4 is running** (#6183) and is the last flat-feasible atom.
- **Constant-factor tricks won't reach higher A.** Batched mat-vec (~2–3×,
  unmeasured) and precision drop (~1.4×) help this run, not the A-ceiling.
- **The transpose symmetry and the canonical-trace shortcut are measured dead
  ends** — no 2×, no scalar collapse.
- **To go "much higher than 4" the investment is the branching-basis transfer-
  matrix tower** (nucleon-chain contraction), seeded by
  `sublemma_2_1_h12_he4_branching.py`. That is the next build if A≥5 is wanted.
