**Proposition.** *Let $F$ be a field. Write $\mathcal{P}(F)$ for the pre-Bloch group: the free abelian group on symbols $[z]$, $z \in F \setminus \{0,1\}$, modulo the five-term relations*

$$
  [x] - [y] + \Bigl[\frac{y}{x}\Bigr] - \Bigl[\frac{1-x^{-1}}{1-y^{-1}}\Bigr] + \Bigl[\frac{1-x}{1-y}\Bigr] = 0 .
$$

*Write $\mathcal{B}(F) = \ker\bigl(\delta \colon \mathcal{P}(F) \to \textstyle\bigwedge^2_{\mathbb{Z}} F^\times\bigr)$ with $\delta[z] = z \wedge (1-z)$. Let*

$$
  T_m(q) \;=\; \prod_{j=1}^{m} (1-q^{j})(1-q^{-j})
$$

*be the $m$-th summand of the figure-eight Habiro series. Then:*

1. *$T_{m+1} = T_m \cdot (1-qX)(1-q^{-1}X^{-1})$ with $X = q^m$, so the Nahm equation of the summand is $(1-X)(1-X^{-1}) = 1$.*
2. *For $X \neq 0$, the Nahm equation holds if and only if $X^2 - X + 1 = 0$.*
3. *Every solution $X \in F$ gives $[X] \in \mathcal{B}(F)$, and $\delta[X] = 0$ already in $\bigwedge^2 F^\times$.*
4. *For $F = \mathbb{Q}(\zeta_6) = \mathbb{Q}(\sqrt{-3})$, the class $2[\zeta_6]$ lies in $\mathcal{B}(F)$.*

*Proof.* Item 1 is the last factor of the product. For item 2, multiply the Nahm equation by $X$. For item 3, $X^2 - X + 1 = 0$ gives $1 - X = X^{-1}$, so $\delta[X] = X \wedge X^{-1} = -(X \wedge X) = 0$. Item 4 is item 3 at the primitive sixth root of unity, which satisfies $\zeta_6^2 - \zeta_6 + 1 = 0$. $\square$

Every statement is algebraic over $F$; no limit, integral or numerical value enters. The archimedean step is separate. The Bloch–Wigner function $D$ is a homomorphism $\mathcal{B}(\mathbb{C}) \to \mathbb{R}$, and $D(e^{i\pi/3}) = \tfrac{1}{2}\mathrm{Vol}(4_1)$. That evaluation is the figure-eight case of [archimedean realisation compatibility](#conj:archimedean-realisation-volume-compatibility), not of this proposition. The identification of $2[\zeta_6]$ with the class of the hyperbolic structure on the figure-eight complement is the standard computation from its two regular ideal tetrahedra \cite{zagier-dilogarithm}; it is cited here, not proved. The scope is the figure-eight knot only.
