This remark records the $\mathbb{Z}/2\mathbb{Z}$ bar-grading algebra for the [bar-involution](#def:bar-involution): the bar-symmetric subring, the bar-anti-symmetric module, and the idempotent sector projections.

## Bar-grading over a commutative ring $R$

**Proposition (Additive decomposition).** $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$ whenever $2 \in R^\times$.
*Proof.* $\frac{x + \overline x}{2} + \frac{x - \overline x}{2} = \frac{2x}{2} = x$. $\square$

**Proposition (Additive and multiplicative identities).** $0$ and $1$ are bar-symmetric.
*Proof.* Direct from the ring-homomorphism properties $\overline 0 = 0$ and $\overline 1 = 1$. $\square$

**Proposition (Closure of bar-symmetric elements under addition).** The sum of bar-symmetric elements is bar-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = x + y$. $\square$

**Proposition (Closure of bar-symmetric elements under multiplication).** The product of bar-symmetric elements is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot y$. $\square$

**Proposition (Closure of bar-anti-symmetric elements under addition).** The sum of bar-anti-symmetric elements is bar-anti-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = -x + (-y) = -(x+y)$. $\square$

**Theorem (Product of two bar-anti-symmetric elements).** If $x$ and $y$ are bar-anti-symmetric, then $x \cdot y$ is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = (-x)(-y) = x \cdot y$. **This is the "anti $\times$ anti = sym" identity that generates bar-symmetric content from bar-anti-symmetric kernels** (for instance, $h^2$ is bar-symmetric whenever $h$ is bar-anti-symmetric). $\square$

**Theorem (Product of bar-symmetric and bar-anti-symmetric elements).** If $x$ is bar-symmetric and $y$ is bar-anti-symmetric, then $x \cdot y$ is bar-anti-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot (-y) = -(x \cdot y)$. $\square$

**Proposition (Commutation with negation).** $\overline{-x} = -\overline x$ --- the bar involution commutes with additive inversion.
*Proof.* From $x + (-x) = 0$ and additivity of the bar involution: $\overline x + \overline{-x} = \overline 0 = 0$, hence $\overline{-x} = -\overline x$. $\square$

**Proposition (Stability under negation).** Negation preserves both grading sectors.
*Proof.* For the symmetric sector: $\overline{-x} = -\overline x = -x$. For the anti-symmetric sector: $\overline{-x} = -\overline x = -(-x) = x = -(-x)$. $\square$

**Theorem (Even powers of bar-anti-symmetric elements).** If $x$ is bar-anti-symmetric, then $x^{2n}$ is bar-symmetric for every $n \in \mathbb{N}$.
*Proof.* Induction on $n$. Base ($n=0$): $x^0 = 1$ is bar-symmetric. Step: $x^{2(k+1)} = x^{2k} \cdot (x \cdot x)$; here $x^{2k}$ is bar-symmetric by the induction hypothesis and $x \cdot x$ is bar-symmetric by the product of two anti-symmetric elements, so their product is bar-symmetric. $\square$

**Theorem (Odd powers of bar-anti-symmetric elements).** If $x$ is bar-anti-symmetric, then $x^{2n+1}$ is bar-anti-symmetric for every $n \in \mathbb{N}$.
*Proof.* Write $x^{2n+1} = x^{2n} \cdot x$; the first factor $x^{2n}$ is bar-symmetric by the even-power theorem and $x$ is bar-anti-symmetric by hypothesis, so their product is bar-anti-symmetric. $\square$

## Bar action on integer scalars

**Proposition (Fixed point at $2$).** $\overline 2 = 2$.
*Proof.* $\overline 2 = \overline{1 + 1} = \overline 1 + \overline 1 = 1 + 1 = 2$. $\square$

**Proposition (Fixed points on natural-number scalars).** $\overline n = n$ for every $n \in \mathbb{N}$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition (Bar-symmetry of natural-number scalars).** Every natural-number scalar is bar-symmetric.
*Proof.* Immediate from $\overline n = n$. $\square$

## Sector projections over a field

**Proposition (Commutation with multiplicative inversion).** Over a field, $\overline{x^{-1}} = (\overline x)^{-1}$.
*Proof.* If $x = 0$, both sides vanish under the $0^{-1} = 0$ convention because $\overline 0 = 0$. If $x \neq 0$, then $\overline x \neq 0$ because the bar involution is injective, and $\overline x \cdot \overline{x^{-1}} = \overline{x \cdot x^{-1}} = \overline 1 = 1$, hence $\overline{x^{-1}} = (\overline x)^{-1}$. $\square$

**Proposition (Invariance of $1/2$).** Over a field of characteristic $\neq 2$, $\overline{1/2} = 1/2$.
*Proof.* $\overline{1/2} = \overline{1 \cdot 2^{-1}} = \overline 1 \cdot (\overline 2)^{-1} = 1 \cdot 2^{-1} = 1/2$ by commutation with inversion and $\overline 2 = 2$. $\square$

**Proposition (Bar-symmetry of integer scalars).** Every integer scalar is bar-symmetric.
*Proof.* For non-negative integers $n \ge 0$, apply natural-number invariance. For negative integers $-(k+1)$, commutation with negation and natural-number invariance give $\overline{-(k+1)} = -\overline{k+1} = -(k+1)$. $\square$

**Proposition (Symmetric projection on symmetric inputs).** If $x$ is bar-symmetric, then $P_{\mathrm{avg}}(x) = x$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x + x)/2 = x$. $\square$

**Proposition (Symmetric projection on anti-symmetric inputs).** If $x$ is bar-anti-symmetric, then $P_{\mathrm{avg}}(x) = 0$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x - x)/2 = 0$. $\square$

**Proposition (Skew projection on anti-symmetric inputs).** If $x$ is bar-anti-symmetric, then $P_{\mathrm{skew}}(x) = x$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - (-x))/2 = x$. $\square$

**Proposition (Skew projection on symmetric inputs).** If $x$ is bar-symmetric, then $P_{\mathrm{skew}}(x) = 0$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - x)/2 = 0$. $\square$

**Theorem (Symmetric projection of even powers).** For bar-anti-symmetric $x$, $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$.
*Proof.* The even power $x^{2n}$ is bar-symmetric, so $P_{\mathrm{avg}}$ fixes it. $\square$

**Theorem (Symmetric projection of odd powers).** For bar-anti-symmetric $x$, $P_{\mathrm{avg}}(x^{2n+1}) = 0$.
*Proof.* The odd power $x^{2n+1}$ is bar-anti-symmetric, so $P_{\mathrm{avg}}$ annihilates it. **Consequently, averaging under the bar involution projects away all odd-power components.** $\square$

**Theorem (Image of the symmetric projection).** $P_{\mathrm{avg}}(x)$ is bar-symmetric for every $x$.
*Proof.* $\overline{P_{\mathrm{avg}}(x)} = \overline{(x + \overline x)/2} = \overline{x + \overline x} \cdot \overline{1/2} = (\overline x + x) \cdot (1/2) = P_{\mathrm{avg}}(x)$ by invariance of $1/2$. $\square$

**Theorem (Idempotency of the symmetric projection).** $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$.
*Proof.* By the preceding theorem, $P_{\mathrm{avg}}(x)$ is bar-symmetric; applying $P_{\mathrm{avg}}$ to a bar-symmetric element returns that element unchanged. $\square$

**Theorem (Image of the skew projection).** $P_{\mathrm{skew}}(x)$ is bar-anti-symmetric for every $x$.
*Proof.* $\overline{P_{\mathrm{skew}}(x)} = \overline{(x - \overline x)/2} = (\overline x - x) \cdot (1/2) = -P_{\mathrm{skew}}(x)$. $\square$

**Theorem (Idempotency of the skew projection).** $P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$.
*Proof.* Since $P_{\mathrm{skew}}(x)$ is bar-anti-symmetric, applying $P_{\mathrm{skew}}$ a second time fixes it. $\square$
