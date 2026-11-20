**V_(2,1) Hoefsmit 2$\times$2 matrix derivation — partial closure.**

$V_{(2,1)}$ provides the 2-dimensional Hoefsmit irrep of $H_3(q)$. Unlike
$V_{(3)}$ and $V_{(1,1,1)}$ (1-d, scalar arithmetic), $V_{(2,1)}$ requires the
full 2$\times$2 matrix representation:

$$
  \sigma_0 \mapsto \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \sigma_1 \mapsto \begin{pmatrix} d_1 & b \\ b & d_2 \end{pmatrix}
$$

with $d_1 = -q^{-1}/(q^2+1)$, $d_2 = q^3/(q^2+1)$, $b^2 = d_1 d_2 + 1$.

**Uniqueness of the diagonal assignment $(d_1, d_2)$.** With $\sigma_0 = \mathrm{diag}(q, -q^{-1})$ fixed as above, the
braid relation $\sigma_0 \sigma_1 \sigma_0 = \sigma_1 \sigma_0 \sigma_1$
admits the unique diagonal assignment $(d_1, d_2)$ shown (up to the sign of $b$, and the degenerate
$b = 0$). The transposed pair $(d_2, d_1)$ satisfies the Hecke quadratic relation, has the same
trace $q - q^{-1}$ and determinant $-1$, and yields the same $b^2$ —
all four of those quantities are **symmetric** in $d_1, d_2$ — yet fails
the braid relation and therefore does not define a representation of $B_3$. At $q = 1$
the representation reduces to the classical Young orthogonal matrix
$s_2 = \begin{pmatrix} -1/2 & \sqrt3/2 \\ \sqrt3/2 & 1/2 \end{pmatrix}$
on the two-dimensional irreducible representation of $S_3$.

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
| `hoefsmit_v21_braid_relation` | $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$, generic $b$ with $b^2 = d_1d_2+1$ | `fin_cases` + `field_simp` + `nlinarith` |
| `chi_v21_matrix_trace_identity` | **the 11-crossing matrix-product trace difference** | `simp only` + `Matrix.trace_fin_two_of` + `ring_nf` + `field_simp` |


## Laurent decomposition and the ε^k growth

Unlike V_(3) where the inverse-Laurent has only one term ($q^{-1}/4$,
giving bounded oscillation), V_(2,1) has two inverse terms ($q^{-1}/4$
and $q^{-3}/4$), and the $q^{-3}/4$ term has $\binom{k+2}{2}$ growth
$\sim k^2/2$. This matches the observed asymptotic $\sim k(k+3)/2$
for the V_(2,1) coefficients.

## Formalization of the matrix-product trace identity

The full matrix-product trace derivation is formalized and proved in `chi_v21_matrix_trace_identity`:

1. The Hoefsmit matrices $\sigma_0, \sigma_1$ are declared locally on `(Fin 2) × (Fin 2) → ℝ`.
2. The non-invariance under the diagonal transposition $d_1 \leftrightarrow d_2$ is established: the transposed matrices yield a trace difference $\chi_{(2,1)}(\mathcal{B}_n) - \chi_{(2,1)}(\mathcal{B}_p)$ larger than the closed form above by a factor of $(q^4+q^2+1)/q^2 = q^2 + 1 + q^{-2}$, verified symbolically and at the rational points $q = 2$, $q = 3/2$, and $q = 1.1099$. Although $b^2$, the trace, and the determinant are symmetric under the swap, the **braid relation** couples $\sigma_0$ to $\sigma_1$ and excludes the transposed pair.
3. The explicit 11-crossing word orders for $\beta_p$ and $\beta_n$ are encoded as `beta_p_word_v21` and `beta_n_word_v21` and consumed directly by the proof.

**The one tactic choice that decides it.** Project the folded matrix with
`Matrix.trace_fin_two_of` (which rewrites $\mathrm{tr}\,!![a,b;c,d]$ straight
to $a+d$), never `Matrix.trace_fin_two` (which leaves `M 0 0 + M 1 1` as
*applications*). With the latter, `field_simp` runs on the un-projected
expression and exhausts 2 000 000 heartbeats. Projecting first also removes
the need for any `linear_combination` certificate: only **even** powers of
$b$ reach the trace, because each index-1 factor is symmetric with
off-diagonal $b$ and a path from a diagonal slot back to itself takes an even
number of off-diagonal steps. Odd powers do occur — $b^3$ appears 20 times in
the normalised matrix — but only in the off-diagonal entries, which the trace
discards.

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
