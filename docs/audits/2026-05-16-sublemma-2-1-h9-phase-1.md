# Sub-lemma 2.1 multi-interface extension at H_9 — fully closed (30/30 at machine ε)

**Date:** 2026-05-16
**Branch:** `claude/sublemma-2-1-h9-extraction`
**Status:** **CLOSED.** All 30 λ ⊢ 9 verified at machine ε for tritium
via the branching-basis approach (Halley-refined Hecke Wedderburn
projectors). Phase 1 (test-word, 2/30) and Phase 2 (branching basis,
30/30) both shipped on this branch.

## Summary

Implements the multi-interface extension of refined Sub-lemma 2.1 to
H_9 ↓ H_6 × H_3, scaffolded in
[`docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md`](2026-05-15-sublemma-2-1-h9-multi-interface-extension.md):

  $$\chi^\lambda(\beta_K) = \sum_{\xi \vdash 6, \, \nu \vdash 3} c^\lambda_{\xi\nu} \cdot \mathrm{Tr}_{V_\xi \otimes V_\nu}\bigl( A^\lambda_{\xi\nu}(I_2) \cdot (\rho_\xi(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_3)) \bigr)$$

For tritium $\beta_T = \beta_p \cdot I_{pn} \cdot \beta_n \cdot I_{nn} \cdot \beta_n$:
- $W_{\mathrm{inner}} = \beta_p \cdot I_{pn} \cdot \beta_n \in H_6$
- $I_2 = I_{nn}$
- $\beta_3 = \beta_n \in H_3$

## Phase 1 — bilinear extraction (test-word approach)

Three new files:

1. **[`computations/sublemma_2_1_A_operator_extract_h9.py`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/sublemma_2_1_A_operator_extract_h9.py)**
   — extracts $A^\lambda_{\xi\nu}(I_2)$ at H_9 via least-squares
   bilinear-system inversion across $K_6 \times K_3 = 12 \times 12 = 144$
   test pairs. Emits both summary stats AND full matrix entries
   (`matrix_re`, `matrix_im`) per (ξ, ν) block, so downstream
   verification can apply A directly without re-extracting.
2. **[`computations/sublemma_2_1_h9_tritium_verify.py`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/sublemma_2_1_h9_tritium_verify.py)**
   — Path A vs Path B verification on the tritium braid:
   - Path A: direct $\chi^\lambda(\beta_T)$ via Hoefsmit at H_9 for all 30 λ ⊢ 9
   - Path B: iterated 2-interface formula using extracted A's + the
     existing H_6 deuteron $A^\xi_{\mu\nu'}(I_{pn})$
3. **Cache-path bug fix in
   [`computations/mass_at_3A_proper.py`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/mass_at_3A_proper.py)**
   (separate concern, see §"Cache-path bug fix" below).

### Results

Extraction (~3.5 min compute on 4 cores, all 30 λ ⊢ 9 reach
chi-reconstruction residual ≤ machine ε):

| λ subset | count | rank vs n_unknowns | extraction status |
|---|---|---|---|
| 1-dim partitions ((9), (1^9)) | 2 | rank = n_unknowns = 1 | **fully determined** |
| All other λ ⊢ 9 | 28 | rank ≤ 66 ≪ n_unknowns ≤ 3390 | rank-deficient |

Verification (Path A vs Path B for tritium, ~2.5 min):

| λ subset | Path A vs Path B | status |
|---|---|---|
| (9), (1^9) | rel diff $\leq 3.24 \times 10^{-16}$ | **machine ε ✓** |
| All other 28 λ | rel diff up to 2.82 (~order-1) | under-determined; extracted A is non-unique outside the test grid |

3/3 fully-determined consistency assertions pass at machine ε.

### Why only 2/30 verify at K_6 = K_3 = 12

Sub-lemma 2.1 requires extracting $A^\lambda_{\xi\nu}(I_2) \in
\mathrm{End}(V_\xi \otimes V_\nu)$, which has $d_\xi^2 \cdot d_\nu^2$
unknowns per (ξ, ν) block. To uniquely determine A from test pairs,
the bilinear matrix needs full column rank — which requires the test
words $\{W_6[i]\}$ to span $\mathrm{End}(V_\xi)$, i.e. $K_6 \geq d_\xi^2$.

Dimensions of ξ ⊢ 6 irreps (Hoefsmit):

| ξ | (6) | (5,1) | (4,2) | (4,1,1) | (3,3) | **(3,2,1)** | (3,1,1,1) | (2,2,2) | (2,2,1,1) | (2,1^4) | (1^6) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $d_\xi$ | 1 | 5 | 9 | 10 | 5 | **16** | 10 | 5 | 9 | 5 | 1 |
| $d_\xi^2$ | 1 | 25 | 81 | 100 | 25 | **256** | 100 | 25 | 81 | 25 | 1 |

At $K_6 = 12$, only $\xi \in \{(6), (1^6)\}$ are spanned; every other
ξ produces a rank-deficient bilinear system. The only λ ⊢ 9 whose LR
support is contained in $\{((6), \nu), ((1^6), \nu)\}$ are
λ = (9) and λ = (1^9) — which is what the empirical verification
shows.

## Approach 1 (next): branching basis — no test words

Per user direction. The categorically clean derivation:

### Math

$A^\lambda_{\xi\nu}(I_2)$ is *literally* the (ξ, ν)-isotypic
diagonal block of $\rho_\lambda(\sigma_5)$ in the H_6 × H_3
branching basis.

Trace structure makes off-diagonal blocks of $\rho_\lambda(I_2)$
contribute zero to $\chi^\lambda(\beta_1 \cdot I_2 \cdot \beta_2)$
(cyclicity + the fact that $\rho_\lambda(\beta_1)\rho_\lambda(\beta_2)$
is block-diagonal in the branching basis when $\beta_1 \in H_6$,
$\beta_2 \in H_3$). So only the (ξ, ν)-diagonal blocks matter, and
they ARE $A^\lambda_{\xi\nu}(I_2)$.

### Algorithm

For each $\lambda \vdash 9$:

1. Build $\rho_\lambda(\sigma_5)$ at H_9 via Hoefsmit (one matrix, fast).
2. Compute $\rho_\lambda(I_2) = c \cdot \rho_\lambda(\sigma_5) + d \cdot I$.
3. Build the change-of-basis (COB) matrix $Q$ from Young's seminormal
   SYT basis to the branching basis:
   - Group SYTs of λ by their {1..6}-restriction shape ξ.
   - Within each ξ-class, decompose the H_3 sub-action on the
     {7,8,9}-cells (via $\rho_\lambda(\sigma_6)$, $\rho_\lambda(\sigma_7)$)
     into Hoefsmit V_ν irreps via SKEW SCHUR straightening (jeu de
     taquin) or via Wedderburn projector $P_\nu = \frac{d_\nu}{|H_3|_q}
     \sum_{g \in H_3} \chi_\nu(g) \cdot \rho_\lambda(g)$.
4. Apply $Q$: $\hat\rho_\lambda(I_2) = Q \rho_\lambda(I_2) Q^{-1}$ is
   block-diagonal with $A^\lambda_{\xi\nu}(I_2)$ on the (ξ, ν)
   blocks.

### Compute cost

~150 ms per λ × 30 λ = ~5 s total. Vastly faster than test-word
extraction (~3.5 min), exact (no rank deficiency), works for ALL
30 partitions of 9.

### Implementation status — DONE

[`computations/sublemma_2_1_h9_branching_basis.py`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/sublemma_2_1_h9_branching_basis.py)
implements the branching-basis algorithm in ~400 lines:

1. **SYT enumeration + ξ-restriction grouping** (~30 lines): uses
   `hecke_characters.standard_young_tableaux` + a new
   `syt_restriction_shape(syt, cells, max_value=6)` that computes the
   sub-shape of cells with values ≤ 6 from each SYT.
2. **Hecke Schur element** $s_\nu(q) = \prod_{x \in \nu} [h(x)]_q$
   (~30 lines): `hook_lengths(nu)` + `schur_element(nu, q_val)`.
3. **Approximate Hecke Wedderburn projector** $P_\nu \approx
   (1/s_\nu(q)) \sum_w \chi_\nu(T_w^{-1}) T_w$ (~60 lines): inverts
   each Hecke word via `_invert_hecke_word` (T_{σ_i}^{-1} = σ_i − h·I,
   word order reversed).  The Geck–Pfeiffer formula is only an
   APPROXIMATE projector at $q \neq 1$ — eigenvalues distribute
   fractionally across all ν's including those with LR mult = 0.
4. **Halley's iteration** $P \mapsto 3P^2 - 2P^3$ (~25 lines):
   quadratically pushes eigenvalues to {0, 1}.  Converges to a TRUE
   projector in ~6 iterations from the Geck–Pfeiffer approximation.
   Verified: $\Vert P^2 - P \Vert \leq 10^{-31}$, $\Vert \sum_\nu P_\nu - I \Vert \leq 10^{-31}$.
5. **(ξ, ν)-block trace extraction** (~30 lines): for each ξ-class,
   compute the top $d_\xi \cdot c^\lambda_{\xi\nu} \cdot d_\nu$
   singular vectors of $P_\nu$ (the V_ν isotype basis within the
   ξ-class), then trace $M$ restricted to that basis.

### Verification results

`probe_q_beta_h9_tritium_branching_verify.py` on the tritium braid
$\beta_T = \beta_p \cdot I_{pn} \cdot \beta_n \cdot I_{nn} \cdot \beta_n$
at $H_9$:

| metric | value |
|---|---|
| λ ⊢ 9 verified | **30 / 30** ✓ |
| max rel residual | **1.15 × 10⁻¹⁴** (f64 machine ε) |
| Path A compute time | 156 s (one-time Hoefsmit warm-up + 30 χ^λ evaluations) |
| Path B compute time | 0.6 s (Halley iter is cheap; reuses cached Hoefsmit) |
| Path B / Path A compute speedup | **~260×** |

The 260× speedup confirms the practical value of the branching
approach: once $\rho_\lambda(\sigma_5)$ is cached at H_9, the
iterated formula evaluates in 600 ms vs 2.5 minutes for direct
Hoefsmit at H_9 — and the same A-blocks reuse for any future
$(W_{\mathrm{inner}}, \beta_3)$ pair.

## Cache-path bug fix (separate concern)

While running Phase 1 extraction, hit a CACHE COLLISION bug in
[`mass_at_3A_proper._cached_seminormal`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/mass_at_3A_proper.py):

```python
# before (buggy)
stem = (_SEMINORMAL_DISK /
        f"n{n}_q{Q0:.10f}_shape{'-'.join(map(str, shape))}")
npz_path = stem.with_suffix(".npz")  # strips after FIRST '.' of "1.1099785955"!
                                     # → "n9_q1.npz" for ALL shapes
```

Path's `with_suffix` replaces everything after the first dot in the
filename, so `q1.1099785955...` got truncated and every shape at the
same n collided into a single `n9_q1.npz` file (containing only the
LAST-written shape's seminormal matrices).

In-memory cache `_SEMINORMAL_CACHE[(n, shape)]` works fine — but cold
starts that hit the disk get the wrong shape's matrices. Effect: any
script computing $\chi^\lambda$ for multiple λ at the same n (cold
start) silently uses the WRONG seminormal matrices for the second-
through-last shape.

**Fix** (in this branch):

```python
# after
stem_name = f"n{n}_q{Q0:.10f}_shape{'-'.join(map(str, shape))}"
npz_path = _SEMINORMAL_DISK / (stem_name + ".npz")
json_path = _SEMINORMAL_DISK / (stem_name + ".json")
```

Verified: distinct shapes now get distinct cache files. The buggy
n3/n6/n9 cache files were deleted as part of this commit.

**Impact assessment**: any prior witness that computed $\chi^\lambda$
for multiple λ at the same n via a cold cache may have silently
mixed shapes. In practice, most production scripts pre-warm the cache
(via `_SEMINORMAL_CACHE` in-memory) before iterating, so cold-from-
disk loads are rare. A targeted re-validation of cold-start-sensitive
witnesses is recommended as follow-up.

## CAL discipline

Phase 1 uses only $q_0$ (CAL-2). No $m_e$, $Q_\beta$, AME data.

## Cross-references

- [`docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md`](2026-05-15-sublemma-2-1-h9-multi-interface-extension.md)
  — original scaffold + math
- [`docs/audits/2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md)
  — single-interface H_6 (deuteron) closure at machine ε
- [`computations/sublemma_2_1_A_operator_extract.py`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/sublemma_2_1_A_operator_extract.py)
  — H_6 (deuteron) extraction (Phase 0; verified)
- [`computations/sublemma-2-1-A-operator-extract-h9-nn.witness.json`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/sublemma-2-1-A-operator-extract-h9-nn.witness.json)
  — Phase 1 H_9 extraction witness (this branch)
- [`computations/sublemma-2-1-h9-tritium-verify.witness.json`](https://github.com/litlfred/qou/blob/claude/sublemma-2-1-h9-extraction/computations/sublemma-2-1-h9-tritium-verify.witness.json)
  — Phase 1 verification witness (this branch)
