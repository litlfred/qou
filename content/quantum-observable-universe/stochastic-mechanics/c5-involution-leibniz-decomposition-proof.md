## Proof sketch

### Step 1: Bar involution and the averaged crossing

The Hecke algebra $H_n(q)$ carries the bar involution $\overline{\,\,}$, a $\mathbb{Z}$-linear anti-ring-automorphism defined by:

$$
\overline{q} = q^{-1}, \quad \overline{\sigma_i} = \sigma_i^{-1}.
$$

The Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ (where $h = q - q^{-1}$) gives $\sigma_i^{-1} = \sigma_i - h$. The bar-invariant projector is $P_{\text{avg}} = (1 + \overline{\,\,})/2$. Its action on $\sigma_i$ yields:

$$
P_{\text{avg}}(\sigma_i) \;=\; \frac{\sigma_i + \overline{\sigma_i}}{2}
\;=\; \frac{\sigma_i + \sigma_i^{-1}}{2}
\;=\; \frac{\sigma_i + \sigma_i - h}{2}
\;=\; \sigma_i - \frac{h}{2}.
$$

This is the averaged crossing operator $\sigma_{\text{avg}}$ used in the typed-$\mathbf{B}_3$ braid recipe.

### Step 2: Averaged crossings in the typed braid

From [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic), the typed-$\mathbf{B}_3$ proton braid uses one averaged $\sigma_1$:

$$
\mathcal{B}_p \;=\; \sigma_0 \cdot (\sigma_1 - \tfrac{h}{2}\mathbf{1})
\;=\; \sigma_0 \cdot \sigma_{1,\text{avg}}.
$$

The typed neutron braid uses two averaged crossings (at $\sigma_0$ and $\sigma_1$):

$$
\mathcal{B}_n \;=\; (\sigma_0 - \tfrac{h}{2}\mathbf{1}) \cdot (\sigma_1 - h\mathbf{1})
\;=\; \sigma_{0,\text{avg}} \cdot \sigma_1^{-1}.
$$

Each averaged crossing contributes a factor of $h/2 = 1/2$ at its respective position.

### Step 3: Leibniz propagation to higher rungs

The categorical Markov-trace expansion of the typed braid in powers of $h$ generates the single-wrap baseline (Form A) plus precision-ladder corrections. The $h/2$ contributions from averaged positions propagate via the Leibniz product expansion:

$$
\tau_M(\mathcal{B}_n - \mathcal{B}_p) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\; \frac{h^2}{2} - h
\;=\; \frac{h(h-2)}{2}.
$$

The $h^2/2$ term is the product of two averaged-crossing $h/2$ contributions (the neutron has two such positions). The $h/2$ generates the $1/2$ in $\Delta(\mathrm{net})$.

For higher rungs $N = k \geq 4$ of the precision ladder, the expansion of $\tau_M(T_\beta)$ in $b \cdot \hbar_q^2$ produces coefficients with two distinct categorical origins.

- **Pure-$\sigma$ contributions.** These arise from non-averaged positions in the braid. They factor through $\sigma^p \cdot b^{2m}$ combinatorics. At the silver ratio, these reduce to Pell-Lucas-clean rationals (via the Hecke quadratic [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null)).
- **Averaged-crossing contributions.** These arise from positions where $\sigma_{\text{avg}}$ acts. They acquire the $1/2$ fingerprint of $P_{\text{avg}}$. At the silver ratio, they produce rationals with a $1/2$ component that is Pell-Lucas-incompatible.

### Step 4: Rung-by-rung classification

Sequential extraction of $c_k$ via $R(q_0) = \prod_k (1 + c_k b^k \hbar_q^{2k})$ yields:

| $c_k$ | Closed form | Origin | At silver ratio |
|:----:|:-----------:|:-------|:-------|
| $c_3$ | $-2$ | $J_{\text{Hopf}}(q=1)$, pure inter-block | $-2$ (clean) |
| $c_4$ | $c_3 \cdot b^4$ | $\sigma^p \cdot b^{2m}$ pure | $-49/32 = -a_3^2/2^5$ (clean) |
| $c_5$ | $\boxed{-b^2 - 1/2}$ | $\sigma$ + averaging | $-11/8$ (1/2 OUTLIER) |
| $c_6$ | $c_3^2 \cdot b^2$ | $\sigma^p \cdot b^{2m}$ pure | $7/2 = a_3/2$ (clean) |
| $c_7$ | $c_3^3$ | pure $\sigma$ powers | $-8$ (clean integer) |

The $c_5$ outlier is structurally distinct. The $\sigma_{\text{avg}}$ contributions at rung $5$ dominate. At all other rungs in $[3, 7]$, the pure-$\sigma$ contributions dominate. □

## Proofs (Lean $\leftrightarrow$ paper bridge)

Every substantive Lean theorem in [`c5-involution-leibniz-decomposition.lean`](c5-involution-leibniz-decomposition.lean) has a narrative proof here and a `sorry`-free Lean proof.

### Hoefsmit–Quantum-2 identity

**Theorem (Lean: `hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`).** For all $q \neq 0$ in $\mathbb{R}$:

$$b^2(q) \;=\; \frac{q^4 + q^2 + 1}{(q^2 + 1)^2} \;=\; 1 - \frac{1}{[2]_q^2}.$$

*Proof.* Multiply both sides by $[2]_q^2 = (q + q^{-1})^2$. Then $(q^2 + 1)^2 = q^2 \cdot (q + q^{-1})^2$, so $b^2 = (q^4+q^2+1)/(q^2[2]_q^2)$. Multiply numerator and denominator by $1/q^2$ to obtain $b^2 = (q^2 + 1 + q^{-2})/[2]_q^2$. This equals $([2]_q^2 - 1)/[2]_q^2 = 1 - 1/[2]_q^2$. Lean tactic: `field_simp; ring`. $\square$

**Corollary (Lean: `c5_decomposition_via_quantum_two`).** $c_5(q) = -3/2 + 1/[2]_q^2$.
*Proof.* Substitute $b^2 = 1 - 1/[2]_q^2$ into $c_5 = -b^2 - 1/2$. $\square$

### Classical-QOU limit + Wedderburn identification

**Theorem (Lean: `c5_classical_limit_eq_neg_five_quarters`).** $c_5(q = 1) = -5/4$.
*Proof.* At $q = 1$, $[2]_q = 2$. Thus $[2]_q^2 = 4$ and $1/[2]_q^2 = 1/4$. Then $c_5(1) = -3/2 + 1/4 = -5/4$. By `norm_num`. $\square$

**Theorem (Lean: `c5_classical_eq_wedderburn_nonsign_dim_half`).** $c_5(1) = -(\dim V_{(3)} + \dim V_{(2,1)})/2 + 1/4 = -5/4$.
*Proof.* The Wedderburn decomposition of $\mathbb{C}[S_3]$ has irreps of dimensions $1$ ($V_{(3)}$), $2$ ($V_{(2,1)}$), and $1$ ($V_{(1,1,1)}$). The non-sign sum is $1 + 2 = 3$. Half is $3/2$. We substitute $-3/2 = -(\dim V_{(3)} + \dim V_{(2,1)})/2$. Combining this with $1/4 = 1/[2]_q^2$ at $q=1$ gives $-5/4$. $\square$

### Silver-ratio identity

**Lemma (Lean: `quantumTwo_at_silver_ratio_squared`).** $[2]_q^2 = 8$ at $q = 1 + \sqrt 2$.
*Proof.* $[2]_{1+\sqrt 2} = (1+\sqrt 2) + 1/(1+\sqrt 2) = (1+\sqrt 2) + (\sqrt 2 - 1) = 2\sqrt 2$. Thus $[2]_q^2 = 8$. Lean tactic:

```lean
field_simp; ring_nf; linarith [Real.mul_self_sqrt (by norm_num : (2:ℝ) ≥ 0)]
```

$\square$

**Theorem (Lean: `b_squared_at_silver_ratio`).** $b^2(1 + \sqrt 2) = 7/8$.
*Proof.* Apply the Hoefsmit–Quantum-2 identity. Then $b^2 = 1 - 1/[2]_q^2 = 1 - 1/8 = 7/8$. $\square$

**Corollary (Lean: `c5_at_silver_ratio_is_minus_11_over_8`).** $c_5(\mathrm{silver}) = -11/8$.
*Proof.* Apply the closed form. Then $c_5 = -3/2 + 1/8 = -12/8 + 1/8 = -11/8$. The numerator $11$ is inert in $\mathbb{Z}[1+\sqrt 2]$. This confirms the $c_5$ outlier fingerprint. $\square$

### $c_5$ in terms of Hecke skein $h$

**Lemma (Lean: `quantum_two_squared_eq_skein_squared_plus_four`).** For all $q \neq 0$:
$[2]_q^2 = h^2 + 4$ where $h = q - q^{-1}$.
*Proof.* $(q + q^{-1})^2 = q^2 + 2 + q^{-2}$ and $(q - q^{-1})^2 + 4 = (q^2 - 2 + q^{-2}) + 4 = q^2 + 2 + q^{-2}$. $\square$

**Theorem (Lean: `c5_as_function_of_skein`).** $c_5(q) = -3/2 + 1/(h^2 + 4)$ where $h = q - q^{-1}$.
*Proof.* Substitute the previous lemma into $c_5 = -3/2 + 1/[2]_q^2$. $\square$

### $c_5$ as a rational map over $\mathbb{R}$

**Proposition (Lean: `c5RationalMap_at_skein_eq_c5Decomposition`).** `c5RationalMap(h(q)) = c5Decomposition(q)`.
*Proof.* Direct rewrite via `c5_as_function_of_skein`. $\square$

**Proposition (Lean: `h_sq_plus_four_pos`, `h_sq_plus_four_ne_zero`).** $h^2 + 4 > 0$ over $\mathbb{R}$.
*Proof.* $h^2 \geq 0$. $\square$

**Proposition (Lean: `c5RationalMap_zero/two/one`).** Concrete evaluations: $c_5(h{=}0) = -5/4$, $c_5(h{=}2) = -11/8$, $c_5(h{=}1) = -13/10$.
*Proof.* Direct numerical computation via `norm_num`. $\square$

**Theorem (Lean: `c5RationalMap_even h`).** $c_5(-h) = c_5(h)$.
*Proof.* $(-h)^2 = h^2$. This captures the categorical content of bar-symmetry: $c_5$ is invariant under the bar action $h \to -h$. $\square$

**Theorem (Lean: `c5RationalMap_le_neg_five_quarters h`).** $c_5(h) \leq -5/4$ for all real $h$, with equality at $h = 0$.
*Proof.* $h^2 + 4 \geq 4$, so $1/(h^2 + 4) \leq 1/4$. Then $c_5 \leq -3/2 + 1/4 = -5/4$. $\square$

**Theorem (Lean: `c5RationalMap_gt_neg_three_halves h`).** $c_5(h) > -3/2$ for all real $h$.
*Proof.* $1/(h^2 + 4) > 0$. The bound is approached asymptotically as $|h| \to \infty$. $\square$

**Theorem (Lean: `c5RationalMap_strict_neg h`).** $c_5(h) < 0$ for all real $h$.
*Proof.* Combine bounds: $c_5 \leq -5/4 < 0$. $\square$

**Theorem (Lean: `c5RationalMap_max_at_zero h`).** $h = 0$ achieves the maximum of $c_5$.
*Proof.* Combine bounds with $c_5(0) = -5/4$. $\square$

**Theorem (Lean: `c5OfHSquared_antitone_on_nonneg`).** $c_5$ is monotonically decreasing in $h^2$ on the non-negative domain.
*Proof.* For $0 \leq x \leq y$, $1/(y+4) \leq 1/(x+4)$. Then $c_5(y) \leq c_5(x)$. $\square$

### Factorization through $h^2$

**Theorem (Lean: `c5RationalMap_factor h`).** $c_5(h) = c_5\text{OfHSquared}(h^2)$.
*Proof.* Both unfold to $-3/2 + 1/(h^2 + 4)$. $\square$

Categorical reading: $c_5$ factors as

$$h \xrightarrow{\text{squaring}} h^2 \xrightarrow{\text{rational fn}} c_5$$

The first arrow is the canonical anti-symmetric to symmetric projection (`IsBarSymmetric.of_mul_antisym`). The second is a bar-symmetric-preserving function. This manifests the bar-symmetric structure of $c_5$ at the level of function composition.

All 24 substantive Lean theorems in the sibling possess narrative proofs here. The Lean file is `sorry`-free.
