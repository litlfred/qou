**Proof.** Define $\overline p(X) := p(-X)$ for $p \in R[X]$ over any commutative ring $R$.

### Core ring-involution axioms

**Proposition.** $\overline X = -X$ and $\overline{-X} = X$.
*Proof.* Evaluating the substitution $X \mapsto -X$ on $X$ gives $-X$, and on $-X$ gives $-(-X) = X$. $\square$

**Proposition.** For every scalar $c \in R$, $\overline{c} = c$.
*Proof.* Constant polynomials are invariant under substitution of $-X$ for $X$. $\square$

**Proposition.** For all $p, q \in R[X]$, $\overline{p+q} = \overline p + \overline q$, $\overline{p \cdot q} = \overline p \cdot \overline q$, $\overline 1 = 1$, and $\overline 0 = 0$.
*Proof.* Polynomial evaluation at $-X \in R[X]$ is a unital ring endomorphism of $R[X]$. $\square$

**Proposition.** $\overline{\overline p} = p$ for every $p \in R[X]$.
*Proof.* Associativity of polynomial composition gives $\overline{\overline p}(X) = p(-(-X)) = p(X)$. $\square$

### Power and scalar identities

**Proposition.** $\overline{X^2} = X^2$, and more generally $\overline{X^n} = (-1)^n X^n$ for all $n \in \mathbb{N}$; in particular $\overline{X^{2n}} = X^{2n}$ and $\overline{X^{2n+1}} = -X^{2n+1}$.
*Proof.* By induction on $n$: $\overline 1 = 1$, and $\overline{X^{k+1}} = \overline{X}\,\overline{X^k} = (-X)(-1)^k X^k = (-1)^{k+1} X^{k+1}$. Specialising to $2n$ and $2n+1$ gives $(-1)^{2n} = 1$ and $(-1)^{2n+1} = -1$. $\square$

**Proposition.** Every natural-number scalar $n \cdot 1 \in R[X]$ is bar-fixed, and $\overline{p - q} = \overline p - \overline q$, $\overline{-p} = -\overline p$.
*Proof.* Natural-number scalars are fixed by induction from $\overline 0 = 0$ and $\overline 1 = 1$. Since $p - q = p + (-1)q$ and $\overline{-1} = -1$, subtraction and negation commute with $\overline{(\cdot)}$. $\square$

### Concrete bar-symmetric polynomials

**Proposition.** $\overline{4 + X^2} = 4 + X^2$.
*Proof.* Combine $\overline 4 = 4$ and $\overline{X^2} = X^2$ by additivity. $\square$

**Proposition.** In $\mathbb{R}[X]$, the truncated sixth-order polynomials
$$c_5^{[6]}(X) := -\tfrac{5}{4} - \tfrac{X^2}{16} + \tfrac{X^4}{64} - \tfrac{X^6}{256}, \qquad \cos^{[6]}(X) := 1 - \tfrac{X^2}{2} + \tfrac{X^4}{24} - \tfrac{X^6}{720}, \qquad \cosh^{[6]}(X) := 1 + \tfrac{X^2}{2} + \tfrac{X^4}{24} + \tfrac{X^6}{720}$$
are all bar-symmetric under the same involution $X \mapsto -X$.
*Proof.* Each term has the form $c\,X^{2k}$ with a bar-fixed scalar $c$ and a bar-fixed even power $X^{2k}$; sums and differences of bar-symmetric polynomials remain bar-symmetric, placing the series, phase, and gain truncations in the same invariant subring $\mathbb{R}[X^2]$. $\square$

### Pre-archimedean generic versions

**Theorem.** Over any commutative ring $R$ (with no field or archimedean structure invoked), for any $n \in \mathbb{N}$ and coefficients $c_k \in R$, the even polynomial $P_n(X) := \sum_{k=0}^{n-1} c_k X^{2k}$ is bar-symmetric (in particular $c_0 + c_1 X^2 + c_2 X^4 + c_3 X^6$ is bar-symmetric), and any odd-power sum $\sum_{k=0}^{n-1} c_k X^{2k+1}$ is bar-anti-symmetric.
*Proof.* By induction on $n$: the empty sum $0$ satisfies both conditions, each term $c_k X^{2k}$ is fixed while each term $c_k X^{2k+1}$ negates under $X \mapsto -X$, and additivity preserves both eigenspaces. $\square$

### Concrete evaluations

**Proposition.** $c_5^{[6]}(0) = -5/4$ and $c_5^{[6]}(1) = -333/256$.
*Proof.* At $X = 0$ all positive-degree terms vanish, leaving $-5/4$. At $X = 1$, $-5/4 - 1/16 + 1/64 - 1/256 = (-320 - 16 + 4 - 1)/256 = -333/256$, which approximates the exact value $c_5(1) = -13/10 = -332.8/256$ to relative error $\approx 0.06\%$ (consistent with the $O(X^8/4^4)$ Taylor remainder at $X = 1$). Extending from $R[X]$ to rational functions and formal power series over $R$ embeds the closed form $-3/2 + 1/(X^2 + 4)$ and the untruncated series in the same involution framework. $\square$
