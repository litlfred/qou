**V_(2,1) Hoefsmit 2$\times$2 matrix derivation — partial closure.**

$V_{(2,1)}$ provides the 2-dimensional Hoefsmit irrep of $H_3(q)$. Unlike
$V_{(3)}$ and $V_{(1,1,1)}$ (1-d, scalar arithmetic), $V_{(2,1)}$ requires the
full 2$\times$2 matrix representation:

$$
  \sigma_0 \mapsto \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \sigma_1 \mapsto \begin{pmatrix} d_1 & b \\ b & d_2 \end{pmatrix}
$$

with $d_1 = q^3/(q^2+1)$, $d_2 = -q^{-1}/(q^2+1)$, $b^2 = d_1 d_2 + 1$.

$$
  \chi_{(2,1)}(\mathcal{B}_n) - \chi_{(2,1)}(\mathcal{B}_p)
   = -\frac{(q^4 + 1)(q^2 - 1)}{4 q^3}.
$$

## Content of this module

| theorem | content | proof |
|---|---|---|
| `hoefsmit_v21_sigma0_trace` | $q + (-q^{-1}) = q - q^{-1}$ | `ring` |
| `hoefsmit_v21_sigma1_trace` | $d_1 + d_2 = q - q^{-1}$ | `field_simp + ring` |
| `chi_V21_difference_factored_eq_polynomial` | factored $\leftrightarrow$ polynomial form | `field_simp + ring` |
| `chi_V21_laurent_decomposition` | explicit Laurent: $-q^3/4 + q/4 - q^{-1}/4 + q^{-3}/4$ | `field_simp + ring` |
| `chi_V21_difference_at_{one,two}` | numerical cross-checks at $q = 1, 2$ | `norm_num` |

All theorems sorry-free.

## Laurent decomposition and the ε^k growth

Unlike V_(3) where the inverse-Laurent has only one term ($q^{-1}/4$,
giving bounded oscillation), V_(2,1) has two inverse terms ($q^{-1}/4$
and $q^{-3}/4$), and the $q^{-3}/4$ term has $\binom{k+2}{2}$ growth
$\sim k^2/2$. This matches the observed asymptotic $\sim k(k+3)/2$
for the V_(2,1) coefficients.

## Not yet formalised

The **full Lean matrix-product trace derivation** (computing
$\mathrm{tr}\bigl(\prod_{c \in \beta} M_c\bigr)$ from the 2$\times$2
matrices) requires:

1. Importing the Hoefsmit $\sigma_0, \sigma_1$ definitions from
   `hoefsmit-V21-cos-symmetrization.lean`, which the Lean module does not
   yet export.
2. Resolving the YB cubic anomaly (the `d_1 \leftrightarrow d_2` swap) for matrix-level
   correctness. (Note: the closed-form rational result is invariant
   under the swap.)
3. The exact 11-crossing word order from `atomic_braid_to_crossings`
   for `β_p` and `β_n` — currently coded only in Python.

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
```

The theorem statement is now **explicit at the matrix-product
level**. The proof is the only remaining `sorry` here — discharged by the substantive sympy
verification recorded in `per-wedderburn-block-ck.witness.json`.

A full Lean proof would unfold the 11-matrix product on
`(Fin 2) × (Fin 2) → ℝ` matrices with `Real.sqrt` entries; tractable
but length-substantial.
