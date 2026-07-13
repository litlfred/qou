# Piece A: Corner-Removal Induction

This file provides the narrative counterpart to the corner-removal induction route for Piece A.

**Lemma (Lean: `colLen_corner`).** For a corner $(r,s)$ where $s = \lambda_r - 1$, the column length of $s$ is exactly $r + 1$.
*Proof.* This follows since row $r$ reaches column $s$, but row $r+1$ is strictly shorter. Thus the column length is $r+1$. □

**Lemma (Lean: `hook_r_j`).** For a corner row $r$ and $j < \lambda_r - 1$, the arm contribution to the hook simplifies to $(\lambda_r - 1 - j) + (\text{colLen}(j) - r)$.
*Proof.* By definition, the hook length is $h(r,j) = (\lambda_r - j) + (\text{colLen}(j) - r) - 1$. Algebraically rearranging yields the simplified form. □

**Lemma (Lean: `hook_i_s`).** For a corner column $s = \lambda_r - 1$ and $i < r$, the leg contribution to the hook simplifies to $(\lambda_i - s) + (r - i)$.
*Proof.* By definition, $h(i,s) = (\lambda_i - s) + (\text{colLen}(s) - i) - 1$. Substituting $\text{colLen}(s) = r + 1$ (by Lean: `colLen_corner`) yields the result. □

**Lemma (Lean: `sum_hook_r`).** The sum of $2h(r,j) - 1$ along the row $r$ up to $s$ satisfies:
$$ \sum_{j=0}^{s-1} (2h(r,j) - 1) = 2 \sum_{j=0}^{s-1} \text{colLen}(j) + s^2 - 2rs $$
*Proof.* Substitute the simplification from Lean: `hook_r_j` into the sum. The sum over $j$ evaluates via standard arithmetic series identities, grouping the column length terms together. □

**Lemma (Lean: `sum_hook_s`).** The sum of $2h(i,s) - 1$ along the column $s$ up to $r$ satisfies:
$$ \sum_{i=0}^{r-1} (2h(i,s) - 1) = 2 \sum_{i=0}^{r-1} \lambda_i + r^2 - 2sr $$
*Proof.* Substitute the simplification from Lean: `hook_i_s` into the sum. The sum over $i$ evaluates analogously to the row sum, leaving a term involving the sum of row lengths. □

**Lemma (Lean: `sz_decomposition`).** The total number of cells $n$ decomposes relative to the corner $(r,s)$ as:
$$ n = \sum_{i=0}^{r-1} \lambda_i + \sum_{j=0}^{s-1} \text{colLen}(j) - rs + 1 $$
*Proof.* The total size $n$ can be broken into the cells in rows strictly above $r$, the cells in columns strictly to the left of $s$, the overlap between these two regions (which is a rectangle of size $r \times s$), and the corner cell itself. Summing these regions with the inclusion-exclusion principle yields the identity. □

**Theorem (Lean: `corner_removal_obligation`).** The change in the hook sum obligation when a corner at $(r,s)$ with $s = \lambda_r - 1$ is removed evaluates to:
$$ 1 + \sum_{j=0}^{s-1} (2h(r,j) - 1) + \sum_{i=0}^{r-1} (2h(i,s) - 1) = (s - r)^2 + 2n - 1 $$
*Proof.* Summing the results from Lean: `sum_hook_r` and Lean: `sum_hook_s` alongside the isolated corner cell gives an expression involving $2 \sum \text{colLen}(j) + 2 \sum \lambda_i$. By applying Lean: `sz_decomposition` to rewrite these sums in terms of $n$ and algebraically expanding $(s-r)^2$, the terms exactly cancel to match the right-hand side. □
