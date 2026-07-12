**Proof.** Write $\mathcal{B}$ for Bring's curve over $\mathbb{F}_q$, of genus $g = 4$, and let $N_n = |\mathcal{B}(\mathbb{F}_{q^n})|$ denote the point count over the degree-$n$ extension. By the definition of the [local $q$-zeta function](#local-q-zeta-function), the numerator $P(t) = \prod_{i=1}^{2g}(1 - \alpha_i t)$ encodes the point counts through

$$
N_n = q^n + 1 - \sum_{i=1}^{2g} \alpha_i^n ,
$$

obtained by taking the logarithmic derivative of $Z(\mathcal{B}, t) = P(t)/\bigl((1-t)(1-qt)\bigr)$ and comparing coefficients. The proof bounds $N_n - (q^n + 1)$ by intersection theory on the self-product and then converts the point-count bound into the eigenvalue bound; this is Weil's argument \cite{weil1948}, in the form given by \cite{rosen2002} (Ch. 5) and \cite{milne2013} (§27).

**Step 1: Intersection numbers on $\mathcal{B} \times \mathcal{B}$.** Work on the smooth projective surface $S = \mathcal{B} \times \mathcal{B}$. Let $h = \mathcal{B} \times \{\mathrm{pt}\}$ and $v = \{\mathrm{pt}\} \times \mathcal{B}$ be the horizontal and vertical fibre classes, so that

$$
h \cdot h = 0, \qquad v \cdot v = 0, \qquad h \cdot v = 1 .
$$

Let $\Delta \subset S$ be the diagonal and $\Gamma_n \subset S$ the graph of the $n$-th power Frobenius $\mathrm{Fr}_q^n : \mathcal{B} \to \mathcal{B}$. Their intersection numbers with the fibre classes are

$$
\Delta \cdot h = \Delta \cdot v = 1, \qquad
\Gamma_n \cdot v = 1, \qquad
\Gamma_n \cdot h = \deg(\mathrm{Fr}_q^n) = q^n ,
$$

since $\Gamma_n$ meets a vertical fibre $\{x\} \times \mathcal{B}$ in the single reduced point $(x, \mathrm{Fr}_q^n x)$, while its scheme-theoretic intersection with a horizontal fibre $\mathcal{B} \times \{c\}$ is the fibre $(\mathrm{Fr}_q^n)^{-1}(c)$, of degree $q^n$. The self-intersections are the standard graph formulas: the diagonal has $\Delta^2 = \deg T_{\mathcal{B}} = 2 - 2g$, and for a morphism $f : \mathcal{B} \to \mathcal{B}$ of degree $\deg f$ the graph satisfies $\Gamma_f^2 = (\deg f)(2 - 2g)$, so

$$
\Delta^2 = 2 - 2g, \qquad \Gamma_n^2 = q^n (2 - 2g) .
$$

Finally, $\Delta \cdot \Gamma_n$ counts the fixed points of $\mathrm{Fr}_q^n$, which are exactly the $\mathbb{F}_{q^n}$-rational points. Every such fixed point is transverse: the differential of Frobenius vanishes identically, so $1$ is not an eigenvalue of $d(\mathrm{Fr}_q^n)$ at any fixed point and each fixed point carries intersection multiplicity one. Hence

$$
\Delta \cdot \Gamma_n = N_n .
$$

**Step 2: The Castelnuovo--Severi inequality from the Hodge index theorem.** Let $D$ be any divisor class on $S$ and set $d_h = D \cdot h$, $d_v = D \cdot v$. The class $D' = D - d_v h - d_h v$ is orthogonal to both $h$ and $v$:

$$
D' \cdot h = d_h - d_v (h \cdot h) - d_h (v \cdot h) = 0,
\qquad
D' \cdot v = d_v - d_v (h \cdot v) - d_h (v \cdot v) = 0 .
$$

In particular $D'$ is orthogonal to the ample class $h + v$, so the Hodge index theorem on the surface $S$ gives $D'^2 \leq 0$. Expanding $D = d_v h + d_h v + D'$ and using $h^2 = v^2 = 0$, $h \cdot v = 1$:

$$
D^2 = 2 d_h d_v + D'^2 \leq 2\,(D \cdot h)(D \cdot v) .
$$

This is the Castelnuovo--Severi inequality on $\mathcal{B} \times \mathcal{B}$.

**Step 3: The point-count bound.** Fix $n \geq 1$ and apply Step 2 to $D = r\Delta + s\Gamma_n$ for arbitrary integers $r, s$. From Step 1,

$$
D^2 = r^2(2-2g) + 2rs\,N_n + s^2 q^n (2-2g),
\qquad
D \cdot h = r + s q^n,
\qquad
D \cdot v = r + s ,
$$

and the inequality $D^2 \leq 2(D \cdot h)(D \cdot v)$ becomes, after expanding the right side as $2r^2 + 2rs(1 + q^n) + 2s^2 q^n$ and cancelling,

$$
2rs\,\bigl(N_n - (q^n + 1)\bigr) \;\leq\; 2g\,\bigl(r^2 + s^2 q^n\bigr)
\qquad \text{for all } r, s \in \mathbb{Z} .
$$

Choosing the sign of $rs$ to match the sign of $N_n - (q^n+1)$ gives $|rs| \cdot |N_n - (q^n+1)| \leq g\,(r^2 + s^2 q^n)$. Both sides are homogeneous of degree $2$ in $(r,s)$, so the inequality extends from integers to all rational ratios $x = r/s$ and, by continuity, to all real $x > 0$:

$$
\bigl|N_n - (q^n + 1)\bigr| \;\leq\; g \cdot \frac{x^2 + q^n}{x} .
$$

The right side is minimized at $x = q^{n/2}$, where it equals $2g\,q^{n/2}$. Therefore

$$
\bigl|N_n - (q^n + 1)\bigr| \;\leq\; 2g\,q^{n/2}
\qquad \text{for every } n \geq 1 .
$$

**Step 4: From the point-count bound to $|\alpha_i| \leq q^{1/2}$.** By the trace formula stated at the outset, the bound of Step 3 reads $\bigl|\sum_{i=1}^{2g} \alpha_i^n\bigr| \leq 2g\,q^{n/2}$ for all $n \geq 1$. Consider the rational function

$$
f(t) \;=\; \sum_{n=1}^{\infty} \Bigl(\sum_{i=1}^{2g} \alpha_i^n\Bigr) t^n
\;=\; \sum_{i=1}^{2g} \frac{\alpha_i t}{1 - \alpha_i t} .
$$

The coefficient bound forces the power series to converge absolutely on the open disc $|t| < q^{-1/2}$, so $f$ is holomorphic there. Grouping equal eigenvalues, each distinct value $\alpha$ among the $\alpha_i$, occurring with multiplicity $m_\alpha \geq 1$, contributes a simple pole of $f$ at $t = 1/\alpha$ with residue $-m_\alpha/\alpha \neq 0$; poles at distinct locations cannot cancel. Hence no $1/\alpha_i$ lies in the disc $|t| < q^{-1/2}$, i.e.

$$
|\alpha_i| \;\leq\; q^{1/2} \qquad \text{for all } i .
$$

**Step 5: The functional equation forces equality.** The zeta function of a smooth projective curve satisfies the functional equation

$$
P(t) \;=\; q^g\, t^{2g}\, P\!\Bigl(\frac{1}{qt}\Bigr),
$$

a consequence of the Riemann--Roch theorem on $\mathcal{B}$ \cite{rosen2002} (Ch. 5, Thm. 5.9). Comparing root sets on both sides, the involution $\alpha \mapsto q/\alpha$ permutes the multiset $\{\alpha_1, \ldots, \alpha_{2g}\}$. Applying Step 4 to the eigenvalue $q/\alpha_i$ gives $|q/\alpha_i| \leq q^{1/2}$, i.e. $|\alpha_i| \geq q^{1/2}$. Combined with Step 4 itself,

$$
|\alpha_i| \;=\; q^{1/2} \qquad \text{for all } i = 1, \ldots, 2g .
$$

Since $g = 4$ for Bring's curve, this is the asserted bound on all eight fundamental eigenvalues. $\square$
