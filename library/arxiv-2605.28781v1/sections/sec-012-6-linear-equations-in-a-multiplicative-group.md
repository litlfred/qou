---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-012-6-linear-equations-in-a-multiplicative-group
section_title: "Linear equations in a multiplicative group"
section_number: 6
pages: 12-14
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.757
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
[]{#sec-linear label="sec-linear"} Let $\Gamma\leq \mathbb{C}^\times$ be a multiplicative group. A natural question is how many solutions the equation $$\begin{equation}
\label{eq-sunit}
x_1+\cdots+x_k=1
\end{equation}$$ can have with $x_i\in \Gamma$. We are concerned only with non-degenerate solutions, which are those such that $\sum_{i\in I}x_i\neq 0$ for every non-empty $I\subseteq \{1,\ldots,k\}$. Building on a sequence of earlier results, Evertse, Schlickewei, and Schmidt [@ESS02] proved the following.

::: theorem
[]{#th-ess label="th-ess"} If $\Gamma\leq \mathbb{C}^\times$ is a multiplicative group of rank $d$ then, for any $k\geq 2$, the number of non-degenerate solutions to [\[eq-sunit\]](#eq-sunit){reference-type="eqref" reference="eq-sunit"} is at most $$\exp(C_kd)$$ for some constant $C_k>0$ depending only on $k$.
:::

They gave $C_k$ as an explicit function of $k$, which has been improved (most recently by Amoroso and Viada [@AmVi09], and is now polynomial in $k$), but here we are most concerned with the dependence on the rank $d$.

Erdős, Stewart, and Tijdeman [@EST88] constructed,[^1] for any $k\geq 2$ and large enough $d$, multiplicative groups $\Gamma\leq \mathbb{Q}^\times$ of rank $d$ in which the number of non-degenerate solutions to [\[eq-sunit\]](#eq-sunit){reference-type="eqref" reference="eq-sunit"} is at least $$\exp\mathopen{}\left(  c_k \mathopen{}\left( \frac{d}{\log d} \mathclose{}\right)^{1-\frac{1}{k}} \mathclose{}\right)$$ for some $c_k>0$. This has been improved in some regimes by Konyagin and Soundararajan [@KoSo07] (again for $\Gamma\leq \mathbb{Q}^\times$).

It has been conjectured (see, for example, [@ESS02]) that the dependence on $d$ in Theorem [\[th-ess\]](#th-ess){reference-type="ref" reference="th-ess"} can be improved, perhaps to $\exp(C_kd^{1-c_k})$ for some $c_k>0$. Our construction is also able to disprove this, and shows that the linear dependence on $d$ in the exponent is the best possible. Again, we stress that our construction makes heavy use of algebraic number fields of large degree, and so it remains possible that the dependence on $d$ in the upper bound can be improved if $\Gamma\leq \mathbb{Q}^\times$, for example.

::: theorem
There is an absolute constant $C>0$ such that the following holds. Let $k\geq C$ be any integer. There exist infinitely many $d\geq 2$ and multiplicative groups $\Gamma\leq\mathbb{R}^\times$ of rank $\leq d$ such that there are at least $$\exp((C^{-1}k\log k)d)$$ many non-degenerate solutions to [\[eq-sunit\]](#eq-sunit){reference-type="eqref" reference="eq-sunit"}.
:::

::: proof
*Proof.* Let $K$ be a totally real number field of degree $d$ with $\Delta_K\leq C^d$ for some constant $C>0$, as provided by Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"}. Let $A$ be constructed as in Lemma [\[lem-mainmult\]](#lem-mainmult){reference-type="ref" reference="lem-mainmult"} (so it is a ball of lattice points in the multiplicative unit lattice of $K$), viewed as a subset of $\mathbb{R}$. Note that the unit group has rank $d-1$. Losing only a factor of $2$ in $\mathopen{}\left| A\mathclose{}\right|$ we can assume that $a>0$ for all $a\in A$. We therefore obtain, for any $Y\geq 2$, infinitely many $d$ with accompanying $A$ (contained in a multiplicative group of rank $d-1$) such that $\mathopen{}\left| A\mathclose{}\right|\geq (cY)^{d-1}$ and $$\mathopen{}\left| kA\mathclose{}\right|\leq (Cke^Y)^d$$ for some constants $c,C>0$. By the pigeonhole principle there exists some $x\in kA$ such that $$a_1+\cdots+a_k=x$$ has at least $$\frac{\mathopen{}\left| A\mathclose{}\right|^k}{\mathopen{}\left| kA\mathclose{}\right|}\geq\frac{(cY)^{k(d-1)}}{(Cke^Y)^d}\geq Y^{-k}\left(\frac{(cY)^k}{Cke^Y}\right)^d$$ many solutions. Letting $z_i=a_i/x$, and expanding the group of units with the generator $x$, we achieve at least this many solutions to [\[eq-sunit\]](#eq-sunit){reference-type="eqref" reference="eq-sunit"} in a multiplicative group of rank at most $d$. Furthermore, since $z_i>0$, all of these solutions are automatically non-degenerate.

The conclusion then follows from taking $Y=k$. ◻
:::

A related question is to bound the number of solutions to [\[eq-sunit\]](#eq-sunit){reference-type="eqref" reference="eq-sunit"} in the group of units $\mathcal{O}_K^\times$. Evertse [@Ev83] proved that the number of solutions to $x_1+x_2=1$ with $x_1,x_2\in \mathcal{O}_K^\times$ is at most $3\cdot 7^{3d}$, where $d$ is the degree of $K$. (Such $x_i$ are often called 'exceptional units'.) Niklasch [@Ni97] considered this question further and in particular, generalising a conjecture of Stewart (see [@EGST88 p.120]), conjectured [@Ni97 Conjecture 4.2] the sub-exponential upper bound of $$\exp(d^{2/3+o(1)}).$$ We are able to prove that if we consider the analogous question with $2$ variables replaced by a sufficiently large (but still a constant) number of variables, the analogous conjecture is false, and in fact there are exponentially in $d$ many solutions.

::: theorem
[]{#th-unitlower-body label="th-unitlower-body"} There exists an integer $k\geq 2$ and an absolute constant $C>1$ such that, for infinitely many $d$, there exists a number field $K$ of degree $d$ such that there are at least $C^d$ non-degenerate solutions to [\[eq-sunit\]](#eq-sunit){reference-type="eqref" reference="eq-sunit"} with $x_i\in \mathcal{O}_K^\times$.
:::

This is, in hindsight, a simple consequence of the fact that units of bounded height still have small height after $O(1)$ many sums, and so the size of their $k$-fold sumset is small. To highlight the simplicity of the example we will present the construction from first principles, at the cost of some slight repetition of earlier arguments.

::: proof
*Proof.* Let $C>0$ be the constant provided by Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"}, and let $K$ be a number field of degree $d$ and discriminant $\Delta_K\leq C^d$. Let $Y\geq 1$ be some constant to be chosen later, and let $A=B^\times(Y)\subset \mathcal{O}_K^\times$, so that by Lemma [\[lem-regbound\]](#lem-regbound){reference-type="ref" reference="lem-regbound"} and Lemma [\[lem-ball-mult\]](#lem-ball-mult){reference-type="ref" reference="lem-ball-mult"} $$\mathopen{}\left| A\mathclose{}\right|\geq Y^{d-1}d^{-1/2}C^{-d}.$$ Since $B^\times(Y)\subseteq B^+(e^Y)$, $kA\subseteq B^+(ke^Y)$, and hence by Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"} $$\mathopen{}\left| kA\mathclose{}\right|\leq (2ke^Y+1)^d\leq (3ke^Y)^d,$$ say. By the Cauchy-Schwarz inequality it follows that $$\#\{x_1+\cdots+x_k=y_1+\cdots+y_k : x_i,y_i\in A\}\geq \frac{\mathopen{}\left| A\mathclose{}\right|^{2k}}{\mathopen{}\left| kA\mathclose{}\right|}\geq \mathopen{}\left| A\mathclose{}\right|^{3k/2},$$ say, provided we first choose $Y$ to be some large constant depending on $C$, and then $k$ some larger constant depending on $Y$. By Hölder's inequality (see, for example, the proof of [@ABP25 Lemma 5]) the left-hand side is at most $$C^{k^2}\mathopen{}\left| A\mathclose{}\right|^k+X$$ for some constant $C>1$, where $X$ counts the number of solutions to $x_1+\cdots-y_k=0$ in which no subsum on the left-hand side vanishes. Hence $X\geq \mathopen{}\left| A\mathclose{}\right|^{k/4}$, say, provided $d$ is sufficiently large, which concludes the proof (using that $-1\in \mathcal{O}_K^\times$ and dilating by some fixed $y_k\in A$). ◻
:::

[^1]: In [@EST88] they just address the case $k=2$, but this is straightforward to generalise to arbitrary $k\geq 2$ as indicated in [@ESS02].
