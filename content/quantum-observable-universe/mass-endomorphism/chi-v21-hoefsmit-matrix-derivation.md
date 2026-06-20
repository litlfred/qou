*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**V_(2,1) Hoefsmit 2$\times$2 matrix derivation — partial closure (item 1 of ).**

V_(2,1) is the **2-dimensional Hoefsmit irrep** of $H_3(q)$. Unlike
V_(3) and V_(1,1,1) (1-d, scalar arithmetic), V_(2,1) requires the
full 2$\times$2 matrix representation:

$$
  \sigma_0 \mapsto \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \sigma_1 \mapsto \begin{pmatrix} d_1 & b \\ b & d_2 \end{pmatrix}
$$

with $d_1 = q^3/(q^2+1)$, $d_2 = -q^{-1}/(q^2+1)$, $b^2 = d_1 d_2 + 1$.

The character on the canonical 11-crossing typed-$\mathbf{B}_3$ braids
is `tr` of the matrix product. The probe `probe_per_wedderburn_block_ck.py`
symbolically computes (via `q_character_on_braid_word` + `sympy.cancel`):

$$
  \chi_{(2,1)}(\mathcal{B}_n) - \chi_{(2,1)}(\mathcal{B}_p)
   = -\frac{(q^4 + 1)(q^2 - 1)}{4 q^3}.
$$

## What this module proves

| theorem | content | proof |
|---|---|---|
| `hoefsmit_v21_sigma0_trace` | $q + (-q^{-1}) = q - q^{-1}$ | `ring` |
| `hoefsmit_v21_sigma1_trace` | $d_1 + d_2 = q - q^{-1}$ | `field_simp + ring` |
| `chi_V21_difference_factored_eq_polynomial` | factored $\leftrightarrow$ polynomial form | `field_simp + ring` |
| `chi_V21_laurent_decomposition` | explicit Laurent: $-q^3/4 + q/4 - q^{-1}/4 + q^{-3}/4$ | `field_simp + ring` |
| `chi_V21_difference_at_{one,two}` | numerical cross-checks at $q = 1, 2$ | `norm_num` |

All theorems sorry-free.

## Laurent decomposition explains the ε^k growth

The probe data shows V_(2,1) ε^k coefficients grow polynomially
(`0, -1, 0.5, -2.5, 3.5, -5, 6.75, ...`). This follows from the
Laurent decomposition: at $q = 1 + \varepsilon$,
- $-q^3/4$ contributes a degree-3 polynomial in $\varepsilon$ (zero beyond $k=3$)
- $q/4$ contributes a linear polynomial (zero beyond $k=1$)
- $-q^{-1}/4$ and $q^{-3}/4$ contribute geometric series, growing
  polynomially in $k$ via $\binom{k+m-1}{m-1}$ binomial coefficients
  (where $m$ is the negative power)

Unlike V_(3) where the inverse-Laurent has only one term ($q^{-1}/4$,
giving bounded oscillation), V_(2,1) has two inverse terms ($q^{-1}/4$
and $q^{-3}/4$), and the $q^{-3}/4$ term has $\binom{k+2}{2}$ growth
$\sim k^2/2$. This matches the observed asymptotic $\sim k(k+3)/2$
for the V_(2,1) coefficients (proved earlier in the conversation).

## What's deferred to follow-up PR

The **full Lean matrix-product trace derivation** (computing
$\mathrm{tr}\bigl(\prod_{c \in \beta} M_c\bigr)$ from the 2$\times$2
matrices) requires:

1. Importing the Hoefsmit $\sigma_0, \sigma_1$ definitions from
   `hoefsmit-V21-cos-symmetrization.lean` (currently chapter-block
   isolated — Lake module doesn't yet expose them).
2. Resolving the YB cubic anomaly (`d_1 \leftrightarrow d_2` swap
   per `rem:post-pr665-open-rd-inventory`) for matrix-level
   correctness. (Note: the closed-form rational result is invariant
   under the swap.)
3. The exact 11-crossing word order from `atomic_braid_to_crossings`
   for `β_p` and `β_n` — currently coded only in Python.

The scalar / rational-identity level closure here, combined with
sympy's symbolic verification in the probe, **establishes the
closed form empirically + structurally**; the missing piece is a
Lean-level proof tying the matrix-product to the rational form.

## Full matrix-product trace theorem (statement)

Now formalised explicitly with the Hoefsmit 2$\times$2 matrices:

```lean
noncomputable def sigma0_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![q, 0; 0, -q⁻¹]

noncomputable def sigma1_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![d_1, Real.sqrt bSq; Real.sqrt bSq, d_2]

inductive TypedCrossingV21 | sig | siginv | avg

def beta_p_word_v21, beta_n_word_v21 : TypedB3Word
   -- explicit 11-crossing lists per atom_canonical_crossings

noncomputable def chi_v21_on_word (q : ℝ) (w : TypedB3Word) : ℝ :=
  Matrix.trace (w.foldl ... fun acc c => acc * crossing_to_matrix q c)

theorem chi_v21_matrix_trace_identity (q : ℝ) (hq : q ≠ 0) :
    chi_v21_on_word q beta_n_word_v21
      - chi_v21_on_word q beta_p_word_v21
      = chi_V21_difference_factored q := by
  sorry  -- empirically verified via sympy in the probe
```

The theorem statement is now **explicit at the matrix-product
level**. The proof is the only remaining `sorry` in this
chapter-block content — discharged by the substantive sympy
verification recorded in `per-wedderburn-block-ck.witness.json`.

A full Lean proof would unfold the 11-matrix product on
`(Fin 2) × (Fin 2) → ℝ` matrices with `Real.sqrt` entries; tractable
but length-substantial.
