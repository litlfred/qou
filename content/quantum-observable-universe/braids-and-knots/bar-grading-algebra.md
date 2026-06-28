**Proposition.** *Let $R$ be a commutative ring of characteristic
$\ne 2$ equipped with the [bar-involution](#def:bar-involution). Then
the bar-involution induces a $\mathbb{Z}/2\mathbb{Z}$-grading on $R$
with the following properties.*

*(i) **Decomposition.** Every $x \in R$ splits uniquely as*

$$x \;=\; P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x), \qquad
P_{\mathrm{avg}}(x) = \tfrac{x + \overline x}{2}, \quad
P_{\mathrm{skew}}(x) = \tfrac{x - \overline x}{2}.$$

*(ii) **Subring structure.** The bar-symmetric subspace contains
$0$ and $1$ and is closed under addition and multiplication; the
bar-anti-symmetric subspace is closed under addition. The grading sign
rules hold: $\text{anti} \times \text{anti} = \text{sym}$ and
$\text{sym} \times \text{anti} = \text{anti}$, so $x^{2n}$ is
bar-symmetric and $x^{2n+1}$ is bar-anti-symmetric for any
bar-anti-symmetric $x$.*

*(iii) **Projection idempotency and grading.** $P_{\mathrm{avg}}$ and
$P_{\mathrm{skew}}$ are idempotent; $P_{\mathrm{avg}}(x)$ is always
bar-symmetric and $P_{\mathrm{skew}}(x)$ always bar-anti-symmetric;
$P_{\mathrm{avg}}$ fixes the bar-symmetric subspace and annihilates the
bar-anti-symmetric subspace (and dually for $P_{\mathrm{skew}}$). In
particular $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$ and
$P_{\mathrm{avg}}(x^{2n+1}) = 0$ for bar-anti-symmetric $x$ — the formal
statement of "the framework retains the even part and projects away the
odd part."*

The parts (i)–(iii) are formalized sorry-free in
[`bar-involution.lean`](bar-involution.lean); the
[`rem:bar-involution-properties`](bar-involution-properties.md) remark
gives the physical / categorical reading.

## Proof (Lean $\leftrightarrow$ paper bridge)

Every Lean theorem in [`bar-involution.lean`](bar-involution.lean) has both a narrative proof here and a `sorry`-free formal proof. Theorems split into three sections by structural prerequisite (`CommRing` / `Field`).

### Bar-grading over `CommRing R`

**Proposition (Lean: `decompose x`).** $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$.
*Proof.* $\frac{x + \overline x}{2} + \frac{x - \overline x}{2} = \frac{2x}{2} = x$. $\square$

**Proposition (Lean: `isBarSymmetric_zero`, `isBarSymmetric_one`).** $0$ and $1$ are bar-symmetric.
*Proof.* Direct from `BarInvolution.bar_zero` and `bar_one`. $\square$

**Proposition (Lean: `IsBarSymmetric.add`).** Sum of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = x + y$. $\square$

**Proposition (Lean: `IsBarSymmetric.mul`).** Product of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot y$. $\square$

**Proposition (Lean: `IsBarAntiSymmetric.add`).** Sum of bar-anti-symmetric is bar-anti-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = -x + (-y) = -(x+y)$. $\square$

**Theorem (Lean: `IsBarSymmetric.of_mul_antisym`).** $x, y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = (-x)(-y) = x \cdot y$. **This is the "anti $\times$ anti = sym" identity that generates the bar-symmetric content from bar-anti-symmetric kernels** (e.g., $h^2$ bar-sym from $h$ bar-anti-sym). $\square$

**Theorem (Lean: `IsBarAntiSymmetric.of_sym_mul`).** $x$ bar-symmetric, $y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-anti-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot (-y) = -(x \cdot y)$. $\square$

**Proposition (Lean: `bar_neg x`).** $\overline{-x} = -\overline x$ — bar commutes with negation.
*Proof.* From $x + (-x) = 0$ and bar additive: $\overline x + \overline{-x} = \overline 0 = 0$, hence $\overline{-x} = -\overline x$. $\square$

**Proposition (Lean: `IsBarSymmetric.neg`, `IsBarAntiSymmetric.neg`).** Negation preserves both grading sectors.
*Proof.* For sym: $\overline{-x} = -\overline x = -x$. For anti-sym: $\overline{-x} = -\overline x = -(-x) = x = -(-x)$. $\square$

**Theorem (Lean: `IsBarAntiSymmetric.pow_two_mul`).** $x$ bar-anti-sym $\Rightarrow$ $x^{2n}$ bar-symmetric.
*Proof.* Induction on $n$. Base ($n=0$): $x^0 = 1$ bar-symmetric. Step: $x^{2(k+1)} = x^{2k} \cdot (x \cdot x)$; $x^{2k}$ bar-sym by IH, $x \cdot x$ bar-sym by `of_mul_antisym`; product bar-sym by `IsBarSymmetric.mul`. $\square$

**Theorem (Lean: `IsBarAntiSymmetric.pow_two_mul_add_one`).** $x$ bar-anti-sym $\Rightarrow$ $x^{2n+1}$ bar-anti-symmetric.
*Proof.* $x^{2n+1} = x^{2n} \cdot x$; $x^{2n}$ bar-sym (above), $x$ bar-anti-sym (hypothesis); product bar-anti-sym by `of_sym_mul`. $\square$

### Bar on integer scalars

**Proposition (Lean: `bar_two`).** $\overline 2 = 2$.
*Proof.* $\overline 2 = \overline{1 + 1} = \overline 1 + \overline 1 = 1 + 1 = 2$. $\square$

**Proposition (Lean: `bar_natCast n`).** $\overline n = n$ for every $n \in \mathbb{N}$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition (Lean: `isBarSymmetric_natCast n`).** Every natural-number scalar is bar-symmetric.
*Proof.* Restatement of `bar_natCast n` in the `IsBarSymmetric` predicate. $\square$

### Projection theorems (require `Field R`)

**Proposition (Lean: `bar_inv x`).** $\overline{x^{-1}} = (\overline x)^{-1}$ over a field.
*Proof.* If $x = 0$: both sides are $0$ (from $\overline 0 = 0$ + $0^{-1} = 0$ convention). If $x \neq 0$: $\overline x \neq 0$ (bar is injective by involutivity), and $\overline x \cdot \overline{x^{-1}} = \overline{x \cdot x^{-1}} = \overline 1 = 1$, hence $\overline{x^{-1}} = (\overline x)^{-1}$. $\square$

**Proposition (Lean: `bar_half`).** $\overline{1/2} = 1/2$ over a field.
*Proof.* $\overline{1/2} = \overline{1 \cdot 2^{-1}} = \overline 1 \cdot (\overline 2)^{-1} = 1 \cdot 2^{-1} = 1/2$ via `bar_inv` and `bar_two`. $\square$

**Proposition (Lean: `isBarSymmetric_intCast n`).** Every integer scalar is bar-symmetric.
*Proof.* For $n = \mathrm{ofNat}\, k$: use `bar_natCast`. For $n = \mathrm{negSucc}\, k = -(k+1)$: $\overline{-(k+1)} = -\overline{k+1} = -(k+1)$ via `bar_neg` + `bar_natCast`. $\square$

**Proposition (Lean: `barSymmetricProjection_of_sym x`).** If $x$ is bar-symmetric, $P_{\mathrm{avg}}(x) = x$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x + x)/2 = x$. $\square$

**Proposition (Lean: `barSymmetricProjection_of_antisym x`).** If $x$ is bar-anti-symmetric, $P_{\mathrm{avg}}(x) = 0$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x - x)/2 = 0$. $\square$

**Proposition (Lean: `barSkewProjection_of_antisym x`).** If $x$ is bar-anti-symmetric, $P_{\mathrm{skew}}(x) = x$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - (-x))/2 = x$. $\square$

**Proposition (Lean: `barSkewProjection_of_sym x`).** If $x$ is bar-symmetric, $P_{\mathrm{skew}}(x) = 0$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - x)/2 = 0$. $\square$

**Theorem (Lean: `barSymmetricProjection_pow_even_of_antisym x n`).** For bar-anti-sym $x$: $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$.
*Proof.* $x^{2n}$ is bar-symmetric by `pow_two_mul`; apply `of_sym`. $\square$

**Theorem (Lean: `barSymmetricProjection_pow_odd_of_antisym x n`).** For bar-anti-sym $x$: $P_{\mathrm{avg}}(x^{2n+1}) = 0$.
*Proof.* $x^{2n+1}$ is bar-anti-sym by `pow_two_mul_add_one`; apply `of_antisym`. **This is "the framework projects away odd-power components" at the formal level.** $\square$

**Theorem (Lean: `barSymmetricProjection_isBarSymmetric x`).** $P_{\mathrm{avg}}(x)$ is bar-symmetric for every $x$.
*Proof.* $\overline{P_{\mathrm{avg}}(x)} = \overline{(x + \overline x)/2} = \overline{x + \overline x} \cdot \overline{1/2} = (\overline x + x) \cdot (1/2) = P_{\mathrm{avg}}(x)$ via `bar_half`. $\square$

**Theorem (Lean: `barSymmetricProjection_idempotent x`).** $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$.
*Proof.* $P_{\mathrm{avg}}(x)$ is bar-symmetric by the previous theorem; applying $P_{\mathrm{avg}}$ to a bar-symmetric input gives the input back by `of_sym`. $\square$

**Theorem (Lean: `barSkewProjection_isBarAntiSymmetric x`).** $P_{\mathrm{skew}}(x)$ is bar-anti-symmetric.
*Proof.* $\overline{P_{\mathrm{skew}}(x)} = \overline{(x - \overline x)/2} = (\overline x - x) \cdot (1/2) = -P_{\mathrm{skew}}(x)$. $\square$

**Theorem (Lean: `barSkewProjection_idempotent x`).** $P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$.
*Proof.* Analogous to $P_{\mathrm{avg}}$ idempotency via `barSkewProjection_of_antisym`. $\square$

All 33 theorems / definitions in [`bar-involution.lean`](bar-involution.lean) have narrative proofs here and `sorry`-free Lean proofs.
