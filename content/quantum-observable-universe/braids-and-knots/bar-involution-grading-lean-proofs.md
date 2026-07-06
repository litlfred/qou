This remark details the $\mathbb{Z}/2\mathbb{Z}$ bar-grading structure for the [bar-involution](#def:bar-involution), verifying the subring and module properties algebraically.

## Formal properties

We decompose elements into symmetric and anti-symmetric components over formal rings. 

### Bar-grading over commutative rings

**Proposition.** $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$.
*Proof.* $\frac{x + \overline x}{2} + \frac{x - \overline x}{2} = \frac{2x}{2} = x$. $\square$

**Proposition.** $0$ and $1$ are bar-symmetric.
*Proof.* Immediate from ring involution axioms. $\square$

**Proposition.** The sum of bar-symmetric elements is bar-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = x + y$. $\square$

**Proposition.** The product of bar-symmetric elements is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot y$. $\square$

**Proposition.** The sum of bar-anti-symmetric elements is bar-anti-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = -x + (-y) = -(x+y)$. $\square$

**Theorem.** If $x$ and $y$ are bar-anti-symmetric, their product $x \cdot y$ is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = (-x)(-y) = x \cdot y$. This identity generates bar-symmetric structures from bar-anti-symmetric kernels (e.g., $h^2$ is bar-symmetric because $h$ is bar-anti-symmetric). $\square$

**Theorem.** If $x$ is bar-symmetric and $y$ is bar-anti-symmetric, $x \cdot y$ is bar-anti-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot (-y) = -(x \cdot y)$. $\square$

**Proposition.** The bar involution commutes with negation: $\overline{-x} = -\overline x$.
*Proof.* $\overline x + \overline{-x} = \overline 0 = 0$, hence $\overline{-x} = -\overline x$. $\square$

**Proposition.** Negation preserves both grading sectors.
*Proof.* For a symmetric element, $\overline{-x} = -\overline x = -x$. For an anti-symmetric element, $\overline{-x} = -\overline x = -(-x) = x$. $\square$

**Theorem.** If $x$ is bar-anti-symmetric, $x^{2n}$ is bar-symmetric.
*Proof.* By induction. Base case $n=0$: $x^0 = 1$ is bar-symmetric. Step: $x^{2(k+1)} = x^{2k} \cdot x^2$; $x^2$ is bar-symmetric, and the product of bar-symmetric elements is bar-symmetric. $\square$

**Theorem.** If $x$ is bar-anti-symmetric, $x^{2n+1}$ is bar-anti-symmetric.
*Proof.* $x^{2n+1} = x^{2n} \cdot x$. Since $x^{2n}$ is symmetric and $x$ is anti-symmetric, their product is anti-symmetric. $\square$

### Integer scalars

**Proposition.** $\overline 2 = 2$.
*Proof.* $\overline 2 = \overline{1 + 1} = \overline 1 + \overline 1 = 1 + 1 = 2$. $\square$

**Proposition.** For every $n \in \mathbb{N}$, $\overline n = n$.
*Proof.* By induction. $\overline 0 = 0$. $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition.** Every integer scalar is bar-symmetric.
*Proof.* Positive integers are bar-symmetric by the preceding proposition. Negative integers follow because negation preserves symmetry. $\square$

### Projections over fields

**Proposition.** Over a field, $\overline{x^{-1}} = (\overline x)^{-1}$.
*Proof.* If $x = 0$, both sides are $0$. If $x \neq 0$, then $\overline x \neq 0$ by injectivity. Thus $\overline x \cdot \overline{x^{-1}} = \overline{x \cdot x^{-1}} = \overline 1 = 1$. $\square$

**Proposition.** $\overline{1/2} = 1/2$.
*Proof.* $\overline{1/2} = \overline{1 \cdot 2^{-1}} = \overline 1 \cdot (\overline 2)^{-1} = 1 \cdot 2^{-1} = 1/2$. $\square$

**Proposition.** For bar-symmetric $x$, $P_{\mathrm{avg}}(x) = x$ and $P_{\mathrm{skew}}(x) = 0$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x + x)/2 = x$. $P_{\mathrm{skew}}(x) = (x - x)/2 = 0$. $\square$

**Proposition.** For bar-anti-symmetric $x$, $P_{\mathrm{avg}}(x) = 0$ and $P_{\mathrm{skew}}(x) = x$.
*Proof.* $P_{\mathrm{avg}}(x) = (x - x)/2 = 0$. $P_{\mathrm{skew}}(x) = (x - (-x))/2 = x$. $\square$

**Theorem.** For bar-anti-symmetric $x$, $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$ and $P_{\mathrm{avg}}(x^{2n+1}) = 0$.
*Proof.* $x^{2n}$ is bar-symmetric, so it equals its average projection. $x^{2n+1}$ is bar-anti-symmetric, so its average projection vanishes. This mechanism formally filters out odd-power components. $\square$

**Theorem.** The projections are idempotent: $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$ and $P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$.
*Proof.* $P_{\mathrm{avg}}(x)$ is bar-symmetric since $\overline{(x + \overline x)/2} = (\overline x + x)/2 = P_{\mathrm{avg}}(x)$. Applying $P_{\mathrm{avg}}$ to a bar-symmetric input returns the input. Similarly for $P_{\mathrm{skew}}$. $\square$
