---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-001-11-the-wrt-invariant-for-integral-homology-spher
section_title: "The WRT invariant for integral homology spheres"
section_number: 1.1
pages: 1-4
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.954
---
[]{#sec:witt-resh-tura-1 label="sec:witt-resh-tura-1"}

Witten [@Witten] introduced the notion of Chern-Simons path integral which gives a quantum field theory interpretation of the Jones polynomial [@Jones1; @Jones2] and predicts the existence of $3$-manifold invariants. Using the quantum group $U_q(sl_2)$ at roots of unity, Reshetikhin and Turaev [@Reshetikhin-Turaev:invariants] gave a rigorous construction of $3$-manifold invariants, which are believed to coincide with the Chern-Simons path integrals. These invariants are called the Witten-Reshetikhin-Turaev (WRT) invariants.

In the present paper, we focus on the WRT invariant for integral homology spheres, i.e., closed $3$-manifolds $M$ with trivial first homology groups. If we fix such $M$, the WRT invariant $\tau _\zeta (M)\in \C$ is defined for each root of unity $\zeta$. (Unlike the case of general closed $3$-manifolds, one does not have to specify a fourth root of $\zeta$.) For an integer $r\ge 1$, $\tau _{\zeta _r}(M)$ for $\zeta _r=\exp\frac{2\pi \sqrt{-1}}{r}$ is also denoted by $\tau _r(M)$. In the literature, usually $\tau _1(M)$ is not defined, but for our purpose it is convenient to defined it as $1$. For integral homology spheres, the version $\tau '_r(M)$ introduced by Kirby and Melvin [@Kirby-Melvin] defined for odd $r\ge 3$ is equal to $\tau _r(M)$.

Let $\calZ\subset \C$ denote the set of all roots of unity. Define the *WRT function* of $M$ $$\tau (M)\zzzcolon \calZ\rightarrow \C,$$ by $\tau (M)(\zeta )=\tau _\zeta (M)$. The behavior of the function $\tau (M)$ is of interest here.

For $\tau _\zeta (M)$ with $\zeta$ roots of unity of *odd prime (power) orders*, there have been more extensive studies than for the other cases. Murakami [@Murakami1] proved that if $\zeta \in \calZ$ is of odd prime order, then $\tau _\zeta (M)\in \modZ [\zeta ]$, hence it is an algebraic integer. Ohtsuki [@Ohtsuki1] extracted from the $\tau _\zeta (M)$ for $\zeta$ of odd prime orders a power series invariant, known as the *Ohtsuki series* of $M$ $$\tau ^O(M)=1+\sum_{n=1}^\infty \lambda _n(M)(q-1)^n\in \modQ [[q-1]].$$ Lawrence [@Lawrence:integrality] conjectured, and Rozansky [@Rozansky] later proved, that $\tau ^O(M)\in \modZ [[q-1]]$ and that, for each $\zeta \in \calZ$ of odd prime power order $p^e$, $\tau ^O(M)|_{q=\zeta }$ converges $p$-adically to $\tau _\zeta (M)$. In this sense, the Ohtsuki series *unifies* the WRT invariants at roots of unity of odd prime power orders. (For generalizations of the above-mentioned results to rational homology spheres and to invariants associated to other Lie groups, see [@Le1; @Le2; @Masbaum-Roberts; @Masbaum-Wenzl; @Murakami2; @Ohtsuki2; @Takata-Yokota].)

The proofs of the above-mentioned results depends heavily on the fact that if $\zeta \in \calZ$ is of prime power order, then $\zeta -1$ is not a unit in the ring $\modZ [\zeta ]$. Otherwise, $\zeta -1$ is a unit in $\modZ [\zeta ]$, and expansions in powers of $\zeta -1$ do not work.

## The ring $\Zqh$ of analytic functions on the set of roots of unity {#sec:ring-zqh-cyclotomic}

The invariant $J_M$ of an integral homology sphere $M$ which we construct in the paper takes values in a completion $\Zqh$ of the polynomial ring $\modZ [q]$, which was introduced in [@H:rims2001] and studied in [@H:cyclotomic]. One of the simplest definitions of $\Zqh$ is $$\Zqh = \varprojlim_{n}\modZ [q]/((q)_n),$$ where we set $$(q)_n = (1-q)(1-q^2)\cdots(1-q^n).$$

The ring $\Zqh$ may be regarded as the ring of "analytic functions defined on the set $\calZ$ of roots of unity". This statement is justified by the following facts. (The following overlaps those in [@H:rims2001; @H:cyclotomic].)

First of all, *each element of $\Zqh$ can be evaluated at each root of unity*. That is, for each $\zeta \in \calZ$, the evaluation map $\mods _\zeta \zzzcolon \modZ [q]\rightarrow \modZ [\zeta ]$, $f(q)\mapsto f(\zeta )$, induces a (surjective) ring homomorphism $$\mods _\zeta \zzzcolon \Zqh\rightarrow \modZ [\zeta ],$$ since $\mods _\zeta ((q)_n)=0$ if $n\ge \ord(\zeta )$. It is often useful to write $f(\zeta )=\mods _\zeta (f(q))$ for $f(q)\in \Zqh$.

Second, *each element of $\Zqh$ can be regarded as a (set-theoretic) function on the set of roots of unity.* This means that each $f\in \Zqh$ is determined uniquely by the values $\mods _\zeta (f)\in \modZ [\zeta ]$ for all $\zeta \in \calZ$, or, equivalently, the function $$\label{e4}
  \mods _{\calZ}\zzzcolon \Zqh\rightarrow \prod_{\zeta \in \calZ}\modZ [\zeta ],\quad
  f(q)\mapsto (f(\zeta ))_{\zeta \in \calZ}.$$ is injective [@H:cyclotomic Theorem 6.3]. Here, in a natural way, $\prod_{\zeta \in \calZ}\modZ [\zeta ]$ can be regarded as a subring of the ring of $\C$-valued functions on $\calZ$.

Third, *each element of $\Zqh$ has a power series expansion in $q-\zeta$ for each root of unity, and any such power series determines $\Zqh$.* In fact, for each $\zeta \in \calZ$, the inclusion $\modZ [q]\subset \modZ [\zeta ][q]$ induces a ring homomorphism $$\label{e6}
  \iota _\zeta \zzzcolon \Zqh\rightarrow \modZ [\zeta ][[q-\zeta ]],$$ since, for each $i\ge 0$, $(q)_n$ is divisible by $(q-\zeta )^i$ in $\modZ [\zeta ][q]$ if $n\ge i\ord(\zeta )$. Since $\iota _\zeta$ is injective [@H:cyclotomic Theorem 5.2], each $f\in \Zqh$ is determined by the power series $\iota _\zeta (f)$. $\iota _\zeta (f)$ may be regarded as the Taylor expansion of $f$, see Section [\[sec:power-seri-expans-1\]](#sec:power-seri-expans-1){reference-type="ref" reference="sec:power-seri-expans-1"}.

Fourth, *each element of $\Zqh$ is completely determined by its values on a subset $\calZ'\subset \calZ$ if $\calZ'$ has a limit point. Otherwise, not completely.* To explain what this means, we introduce a topology on the set $\calZ$, which is different from the usual one induced by the topology of $\C$. Two elements $\zeta ,\xi \in \calZ$ are said to be *adjacent* if $\zeta \xi ^{-1}$ is of prime power order, or, equivalently, if $\zeta -\xi$ is not a unit in $\modZ [\zeta ,\xi ]$. A subset $\calZ'\subset \calZ$ is defined to be *open* if, for each $\zeta \in \calZ'$, all but finitely many elements adjacent to $\zeta$ is contained in $\calZ'$. In this topology, an element $\xi \in \calZ$ is a limit point of a subset $\calZ'\subset \calZ$ (i.e., $(U\setminus \{\xi \})\cap \calZ'\neq\emptyset$ for all neighborhood $U$ of $\xi$) if and only if there are infinitely many $\zeta \in \calZ'$ adjacent to $\xi$. We have the following.

::: proposition
[]{#r85 label="r85"} If $\calZ'\subset \calZ$ has a limit point, then the ring homomorphism $$\label{e61}
    \mods _{\calZ'}\zzzcolon \Zqh\rightarrow \prod_{\zeta \in \calZ'}\modZ [\zeta ],\quad
    f(q)\mapsto (f(\zeta ))_{\zeta \in \calZ},$$ is injective.
:::

If $\calZ'\subset \calZ$ has no limit point, then $\mods _{\calZ'}$ is not injective, i.e., there is a non-zero "analytic function" $f\in \Zqh$ vanishing on $\calZ'$, see Proposition [\[r56\]](#r56){reference-type="ref" reference="r56"}.

The above-explained properties of $\Zqh$ are closely related to the integrality of $\Zqh$. In fact, the completion $\Qqh =
\varprojlim_{n}\modQ [q]/((q)_n)$ does not behave like $\Zqh$, see [@H:cyclotomic Section 7.5].

## A unified WRT invariant $J_M$ with values in $\Zqh$ {#sec:unif-wrt-invar-1}

The following is the main result of the present paper, and follows from Theorems [\[thm:41\]](#thm:41){reference-type="ref" reference="thm:41"} and [\[thm:65\]](#thm:65){reference-type="ref" reference="thm:65"}.

::: theorem
[]{#r40 label="r40"} There is an invariant $J_M\in \Zqh$ of an integral homology sphere $M$ such that for any root of unity $\zeta$ we have $$\label{e56}
    \mods _\zeta (J_M) = \tau _\zeta (M).$$
:::

The properties of the ring $\Zqh$ explained in the last subsection implies that the WRT function $\tau (M)$ may be regarded as an analytic function defined on $\calZ$. Let us describe some corollaries to Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} and properties of the ring $\Zqh$. (Part of the discussion below overlaps those in [@H:rims2001; @H:cyclotomic].)

An immediate consequence of Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} is the following generalization of Murakami's integrality result.

::: corollary
[]{#r14 label="r14"} For any integral homology sphere $M$ and for $\zeta \in \calZ$, we have $\tau _\zeta (M)\in \modZ [\zeta ]$.
:::

Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} immediately implies *Galois equivariance* of $\tau _\zeta (M)$. Namely, we have $$\label{e67}
  \tau _{\alpha (\zeta )}(M)=\alpha (\tau _\zeta (M))$$ for $\alpha \in \Gal(\modQ ^{ab}/\modQ )$ and $\zeta \in \calZ$. Here $\modQ ^{ab}$ denotes the maximal abelian extension of $\modQ$, which is generated over $\modQ$ by all roots of unity. ($\Gal(\modQ ^{ab}/\modQ )$ can be identified with the automorphism group of the group $\calZ\cong\modQ /\modZ$.) It is well known that the Galois equivariance of $\tau _\zeta (M)$ is implied by Reshetikhin and Turaev's definition. Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} reexplains it in an apparent way.

Proposition [\[r85\]](#r85){reference-type="ref" reference="r85"} implies the following.

::: theorem
[]{#r48 label="r48"} The invariant $J_M$ is determined by the WRT function $\tau (M)$. (Thus $J_M$ and $\tau (M)$ have the same strength in distinguishing two integral homology spheres.) Moreover, both $J_M$ and $\tau (M)$ are determined by the values of $\tau _\zeta (M)$ for $\zeta \in \calZ'$, where $\calZ'\subset \calZ$ is any infinite subset with a limit point in the sense explained in Section [0.1](#sec:ring-zqh-cyclotomic){reference-type="ref" reference="sec:ring-zqh-cyclotomic"}.
:::

The invariant $J_M$ unifies not only the WRT invariants but also the Ohtsuki series $\tau ^O(M)$. Namely, we have (Theorem [\[r52\]](#r52){reference-type="ref" reference="r52"}) $$\label{e12}
  \iota _1(J_M)=\tau ^O(M).$$

Injectivity of $\iota _\zeta$ in [\[e6\]](#e6){reference-type="eqref" reference="e6"} for each $\zeta \in \calZ$ implies that the $J_M$ and hence $\tau (M)$ are determined by the power series expansion $\iota _\zeta (J_M)\in \modZ [\zeta ][[q-\zeta ]]$. In particular, $J_M$ is determined by $\tau ^O(M)$, in view of [\[e12\]](#e12){reference-type="ref" reference="e12"}. Thus $J_M$ and $\tau ^O(M)$ have the same strength in distinguishing integral homology spheres. As a consequence, the Le-Murakami-Ohtsuki invariant [@LMO] determines $J_M$ and $\tau (M)$, since it determines $\tau ^O(M)$ (see [@Ohtsuki4]).

For further properties of $J_M$, see Sections [\[sec12\]](#sec12){reference-type="ref" reference="sec12"} and [\[sec13\]](#sec13){reference-type="ref" reference="sec13"}.
