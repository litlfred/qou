This remark details the $\mathbb{Z}/2\mathbb{Z}$ bar-grading structure for the [bar-involution](#def:bar-involution): the subring and module structures and their associated proofs.

## Proofs

Theorems split into three sections by structural prerequisite (commutative ring or field).

### Bar-grading over commutative rings

**Proposition.** $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$.
*Proof.* $\frac{x + \overline x}{2} + \frac{x - \overline x}{2} = \frac{2x}{2} = x$. $\square$

**Proposition.** $0$ and $1$ are bar-symmetric.
*Proof.* Direct from the bar involution axioms. $\square$

**Proposition.** Sum of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = x + y$. $\square$

**Proposition.** Product of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot y$. $\square$

**Proposition.** Sum of bar-anti-symmetric is bar-anti-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = -x + (-y) = -(x+y)$. $\square$

**Theorem.** $x, y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = (-x)(-y) = x \cdot y$. This identity generates the bar-symmetric content from bar-anti-symmetric kernels (e.g., $h^2$ bar-symmetric from $h$ bar-anti-symmetric). $\square$

**Theorem.** $x$ bar-symmetric, $y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-anti-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot (-y) = -(x \cdot y)$. $\square$

**Proposition.** $\overline{-x} = -\overline x$ — bar commutes with negation.
*Proof.* From $x + (-x) = 0$ and bar additive: $\overline x + \overline{-x} = \overline 0 = 0$, hence $\overline{-x} = -\overline x$. $\square$

**Proposition.** Negation preserves both grading sectors.
*Proof.* For symmetric: $\overline{-x} = -\overline x = -x$. For anti-symmetric: $\overline{-x} = -\overline x = -(-x) = x = -(-x)$. $\square$

**Theorem.** $x$ bar-anti-symmetric $\Rightarrow$ $x^{2n}$ bar-symmetric.
*Proof.* Induction on $n$. Base ($n=0$): $x^0 = 1$ bar-symmetric. Step: $x^{2(k+1)} = x^{2k} \cdot (x \cdot x)$; $x^{2k}$ bar-symmetric by inductive hypothesis, $x \cdot x$ bar-symmetric; product bar-symmetric. $\square$

**Theorem.** $x$ bar-anti-symmetric $\Rightarrow$ $x^{2n+1}$ bar-anti-symmetric.
*Proof.* $x^{2n+1} = x^{2n} \cdot x$; $x^{2n}$ bar-symmetric (above), $x$ bar-anti-symmetric (hypothesis); product bar-anti-symmetric. $\square$

### Bar on integer scalars

**Proposition.** $\overline 2 = 2$.
*Proof.* $\overline 2 = \overline{1 + 1} = \overline 1 + \overline 1 = 1 + 1 = 2$. $\square$

**Proposition.** $\overline n = n$ for every $n \in \mathbb{N}$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition.** Every natural-number scalar is bar-symmetric.
*Proof.* Restatement of $\overline n = n$. $\square$

### Projection theorems (require field)

**Proposition.** $\overline{x^{-1}} = (\overline x)^{-1}$ over a field.
*Proof.* If $x = 0$: both sides are $0$ (from $\overline 0 = 0$ and $0^{-1} = 0$ conventions). If $x \neq 0$: $\overline x \neq 0$ (bar is injective by involutivity), and $\overline x \cdot \overline{x^{-1}} = \overline{x \cdot x^{-1}} = \overline 1 = 1$, hence $\overline{x^{-1}} = (\overline x)^{-1}$. $\square$

**Proposition.** $\overline{1/2} = 1/2$ over a field.
*Proof.* $\overline{1/2} = \overline{1 \cdot 2^{-1}} = \overline 1 \cdot (\overline 2)^{-1} = 1 \cdot 2^{-1} = 1/2$. $\square$

**Proposition.** Every integer scalar is bar-symmetric.
*Proof.* For $n = k \ge 0$: use $\overline k = k$. For $n = -(k+1)$: $\overline{-(k+1)} = -\overline{k+1} = -(k+1)$. $\square$

**Proposition.** If $x$ is bar-symmetric, $P_{\mathrm{avg}}(x) = x$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x + x)/2 = x$. $\square$

**Proposition.** If $x$ is bar-anti-symmetric, $P_{\mathrm{avg}}(x) = 0$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x - x)/2 = 0$. $\square$

**Proposition.** If $x$ is bar-anti-symmetric, $P_{\mathrm{skew}}(x) = x$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - (-x))/2 = x$. $\square$

**Proposition.** If $x$ is bar-symmetric, $P_{\mathrm{skew}}(x) = 0$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - x)/2 = 0$. $\square$

**Theorem.** For bar-anti-symmetric $x$: $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$.
*Proof.* $x^{2n}$ is bar-symmetric; apply the projection property. $\square$

**Theorem.** For bar-anti-symmetric $x$: $P_{\mathrm{avg}}(x^{2n+1}) = 0$.
*Proof.* $x^{2n+1}$ is bar-anti-symmetric; apply the projection property. This projects away odd-power components. $\square$

**Theorem.** $P_{\mathrm{avg}}(x)$ is bar-symmetric for every $x$.
*Proof.* $\overline{P_{\mathrm{avg}}(x)} = \overline{(x + \overline x)/2} = \overline{x + \overline x} \cdot \overline{1/2} = (\overline x + x) \cdot (1/2) = P_{\mathrm{avg}}(x)$. $\square$

**Theorem.** $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$.
*Proof.* $P_{\mathrm{avg}}(x)$ is bar-symmetric by the previous theorem; applying $P_{\mathrm{avg}}$ to a bar-symmetric input gives the input back. $\square$

**Theorem.** $P_{\mathrm{skew}}(x)$ is bar-anti-symmetric.
*Proof.* $\overline{P_{\mathrm{skew}}(x)} = \overline{(x - \overline x)/2} = (\overline x - x) \cdot (1/2) = -P_{\mathrm{skew}}(x)$. $\square$

**Theorem.** $P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$.
*Proof.* Analogous to $P_{\mathrm{avg}}$ idempotency. $\square$
