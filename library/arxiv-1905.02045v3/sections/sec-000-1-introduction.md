---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.974
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM INVARIANTS OF HYPERBOLIC KNOTS — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
Among knot invariants, the colored Jones polynomials $\{J_{K,n}\}_{n\geq2}$ and the Kashaev invariants $\{\langle K\rangle_N\}_{N\geq 2}$ are of particular interest, by their relation to quantum field theory, and the geometry of hyperbolic manifolds [@Witten1994; @MurakamiMurakami2001]. We refer to *e.g.* [@MurakamiMurakami2001; @Yokota2011] for their definitions; by [@MurakamiMurakami2001], the two invariants are related by $\langle K\rangle_N=J_{K,N}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i /N})$. We refer to [@Jones; @Kashaev1995; @Champanerkar_etal] for more results and references on this topic.

The Kashaev invariant is extended to a function on roots of unity by setting, for $(h, k)=1$, $\mathcal{J}_{K,0}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i h/k}):=J_{K,k}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i h/k})$. For fixed $k$, the values $(J_{K,0}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i h/k}))_{(h, k)=1}$ are simply the Galois conjugates of $\langle K\rangle_N$ in $\mathbb{Q}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i / k})$. In the case of $K=4_1$, the simplest hyperbolic knot, we have explicitly $$\begin{aligned}
\label{jones41}
  \mathcal{J}_{4_1,0}(q)= \sum_{r=0}^{\infty} | (1-q)(1-q^2)\dotsb (1-q^r)|^2
\end{aligned}$$ for a root of unity $q$. In general, $\mathcal{J}_{K,0}(q)$ can be written as a series of this kind, involving a ratio of $q$-Pochhammer symbols of various indexes. See Section [\[sec:recip2-poch\]](#sec:recip2-poch){reference-type="ref" reference="sec:recip2-poch"} for some more examples and the precise definition of $\mathcal{J}_{K,0}(q)$ in the cases we will consider.

The *volume conjecture* [@MurakamiMurakami2001 Section 5] predicts that $$\label{eq:vc}
  \lim_{N\to\infty}\frac{\log |\langle K\rangle_N|}{N}=\lim_{N\to\infty}\frac{\log |\mathcal{J}_{K,0}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i /N})|}{N}=\frac{\mathopen{}\mathclose\bgroup\originalleft\|K\aftergroup\egroup\originalright\|}{2\pi} v_3,$$ where $\mathopen{}\mathclose\bgroup\originalleft\|K\aftergroup\egroup\originalright\|$ is related to the Gromov simplicial volumes of the complement of $K$, and $v_3$ is a suitable constant (the volume of the ideal regular tetrahedron in ${\mathbb H}^3$). All the knots we will refer to in this paper will be hyperbolic; in this case, the asymptotic formula [\[eq:vc\]](#eq:vc){reference-type="eqref" reference="eq:vc"} was conjectured by Kashaev [@Kashaev1997], and $\mathopen{}\mathclose\bgroup\originalleft\|K\aftergroup\egroup\originalright\|v_3 = \textnormal{Vol} (K)$, the hyperbolic volume of the complement of $K$ in the $3$-sphere. This is motivated by the analogy between the usual dilogarithm, which measures volumes of tetrahedra in the hyperbolic space, and the quantum dilogarithm, which are the building blocks of Kashaev's invariant.

This conjecture was extended in [@Gukov2005] to a full asymptotic expansion, referred to as the *arithmeticity conjecture* in [@CalegariGaroufalidisZagier], whereas the corresponding question for the imaginary part of the logarithm is conjectured to involve the Chern-Simons invariant $\mathop{\mathrm{cs}}(K)$ of $K$ [@MurakamiMurakamiEtAl2002; @Gukov2005]. The arithmeticity conjecture has been proved for all knots with up to seven crossings in [@AndersenHansen2006; @Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7]. We refer to [@DimofteGukovEtAl2009; @Murakami2017; @MurakamiYokota2018; @Murakami2011; @KashaevTirkkonen] and the references therein for more results and information on the volume conjecture.

In [@Zagier2010], Zagier studies several examples of what is called "quantum modular forms". Motivated by extensive numerical computations, he predicts that $\mathcal{J}_{K,0}$ satisfies an approximate modularity property which relates, in the limit as $x\to\infty$ among rationals of bounded denominator, $\mathcal{J}_{K,0}(\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i ({ax+b})/({cx+d})})$ with $\mathcal{J}_{K,0}(x)$ for any $(\begin{smallmatrix}a &b \\ c& d\end{smallmatrix})\in\textnormal{SL}(2,\mathbb{Z})$. More specifically, given a hyperbolic knot $K$, the following conjecture is made (cf. also [@Garoufalidis2018])

::: conj
[]{#conj:zagier label="conj:zagier"} For all $\gamma\in\textnormal{SL}_2(\mathbb{Z})$ such that[^1] $\alpha:= \gamma(\infty) \in\mathbb{Q}$, there exist $C_K(\alpha)\in\mathbb{C}$ and a sequence $(D_{K,n}(\alpha))_{n\geq 0}$ of complex numbers such that, for all $M\in\mathbb{N}$ and $x\in\mathbb{Q}$, with $x\to\infty$, there holds $$\label{eq:J0-approxmod}
    \frac{\mathcal{J}_{K,0}(\ifthenelse{\equal{\gamma(x))}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \gamma(x))\aftergroup\egroup\originalright)}{( \gamma(x)))}{( \gamma(x)))}{( \gamma(x)))}}}{\mathcal{J}_{K,0}(\ifthenelse{\equal{x}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  x\aftergroup\egroup\originalright)}{( x)}{( x)}{( x)}})} = \Big(\frac{2\pi}{\hbar}\Big)^{3/2}\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{i\frac{\mathop{\mathrm{Vol}}(K)-i\mathop{\mathrm{cs}}(K)}{\hbar}} C_K(\alpha)\Big(\sum_{0\leq n < M} D_{K,n}(\alpha) \hbar^{n} + O(\hbar^{M})\Big), \quad \hbar:=\frac{2\pi i}{x-\gamma^{-1}(\infty)},$$ where $\ifthenelse{\equal{x}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  x\aftergroup\egroup\originalright)}{( x)}{( x)}{( x)}}:=\ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}^{2\pi i x}$ and the implied constant depends at most on $\alpha$, on the denominator of $x$ and on $M$. Moreover, if $F_K$ is the invariant trace field of $K$, and $F_{K,\alpha}:=F_K(\ifthenelse{\equal{\alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \alpha\aftergroup\egroup\originalright)}{( \alpha)}{( \alpha)}{( \alpha)}})$, then:

-   $C_K(\alpha)$ is a product of rational powers of elements of $F_{K,\alpha}$;

-   $D_{K,n}(\alpha)\in F_{K,\alpha}$ for $n\geq0$.
:::

In the case $K = 4_1$, Garoufalidis and Zagier [@GaroufalidisZagier] announced a proof of Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"}, and also numerically investigated the conjecture for other knots. The case of the $4_1$ knot is special and rather simpler than that of other knots, due to the fact that in this case all the summands in the definition [\[jones41\]](#jones41){reference-type="eqref" reference="jones41"} of $\mathcal{J}_{4_1,0}$ are positive. One can then use Laplace's method to extract the asymptotic expansion [\[eq:J0-approxmod\]](#eq:J0-approxmod){reference-type="eqref" reference="eq:J0-approxmod"}. In general, this positivity is not present and there is a remarkable amount of cancellation among the terms.

Indeed, $\mathcal{J}_{K,0}(\ifthenelse{\equal{1/N}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  1/N\aftergroup\egroup\originalright)}{( 1/N)}{( 1/N)}{( 1/N)}})$ is typically exponentially smaller than the largest summands in its definition, and this prevents one from applying a direct estimation based on Laplace's method. We circumvent this serious obstacle by obtaining a new modularity relation, with a precise description of the holomorphic and periodic behaviour of the error terms, for the $q$-Pochhammer symbol. This symbol is of crucial importance in the theory of $q$-series and often appears in the theory of modular forms and combinatorics (see for example [@Berndt2010] and references therein).

For $r\in\mathbb{Z}_{\geq0}$, it is defined as $$\label{eq:def-Pochhammer} 
(q)_r:=\prod_{i=0}^r(1-q)^r,\qquad q\in\mathbb{C}.$$ When $|q|<1$, one can also take $r=+\infty$ and obtain the Dedekind $\eta$-function $\eta(z):=\ifthenelse{\equal{z/24}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  z/24\aftergroup\egroup\originalright)}{( z/24)}{( z/24)}{( z/24)}}(\ifthenelse{\equal{z}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  z\aftergroup\egroup\originalright)}{( z)}{( z)}{( z)}})_{\infty},$ an important example of a (half-integral weight) modular form. As such, $\eta$ satisfies the relation $$\eta(\gamma z)=\vartheta(\gamma)(cz+d)^\frac12\eta(z),\qquad \gamma=(\begin{smallmatrix}a &b \\ c& d\end{smallmatrix})\in\textnormal{SL}(2,\mathbb{Z}),$$ for a certain "multiplier system" $\vartheta$ (see [@Iwaniec1997 Section 2.8]). This modularity relation can be naturally extended to the partial product at root of unities. Indeed, in Theorem [\[th:Ir\]](#th:Ir){reference-type="ref" reference="th:Ir"} below we show that for $\alpha \in\mathbb{Q}$, $1\leq r< \textnormal{den}(\gamma \alpha)$ we have $$\label{eq:mro}
\ifthenelse{\equal{\tfrac {\gamma \alpha}{24}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tfrac {\gamma \alpha}{24}\aftergroup\egroup\originalright)}{( \tfrac {\gamma \alpha}{24})}{( \tfrac {\gamma \alpha}{24})}{( \tfrac {\gamma \alpha}{24})}}(\ifthenelse{\equal{\gamma \alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \gamma \alpha\aftergroup\egroup\originalright)}{( \gamma \alpha)}{( \gamma \alpha)}{( \gamma \alpha)}})_r= \vartheta(\gamma) \ifthenelse{\equal{\tfrac{\alpha}{24}}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \tfrac{\alpha}{24}\aftergroup\egroup\originalright)}{( \tfrac{\alpha}{24})}{( \tfrac{\alpha}{24})}{( \tfrac{\alpha}{24})}}(\ifthenelse{\equal{ \alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(   \alpha\aftergroup\egroup\originalright)}{(  \alpha)}{(  \alpha)}{(  \alpha)}})_{r'}\psi_\gamma(\alpha,r)$$ for some $1\leq r'< \textnormal{den}( \alpha)$ and where $\psi_\gamma(\alpha,r)$ is an explicit function with suitable holomorphicity properties. We refer to Section [\[repsec\]](#repsec){reference-type="ref" reference="repsec"} for the precise formulation of this reciprocity formula which we believe to be of independent interest. With this new tool, we can reduce Zagier's modularity conjecture to a slightly modified form of the arithmeticity conjecture, thus showing that the two conjectures are "morally equivalent". In particular, we are able to prove the conjecture for all hyperbolic knots $K\neq 7_2$ with at most seven crossings, since for these the arithmeticity conjecture is known by works of Andersen and Hansen [@AndersenHansen2006] (in the case $K=4_1$), Ohtsuki [@Ohtsuki52; @Ohtsuki7] (in the case $K=5_2$ and with $7$ crossings) and Ohtsuki and Yokota [@OhtsukiYokota6] (in the case of $6$ crossings).

::: theo
[]{#th:1 label="th:1"} Let $K\neq 7_2$ be a hyperbolic knot with at most $7$ crossings. Then Conjecture [\[conj:zagier\]](#conj:zagier){reference-type="ref" reference="conj:zagier"} holds for $K$. The constant $C_K(\alpha)$ has the shape $$C_K(\alpha) = \ifthenelse{\equal{}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \aftergroup\egroup\originalright)}{( )}{( )}{( )}}\Big(\frac{\nu_K}2 \mathop{\mathrm{s}}(\alpha)\Big) c^{\nu_K/2} \Lambda_{K, \alpha}^{1/c} \delta_K^{-1/2},\label{eq:expr-CK}$$ where $c$ is the denominator of $\alpha$, $\Lambda_{K, \alpha} \in F_{K,\alpha}$, $\nu_K\in\mathbb{Z}$, and $\delta_K \in F_K$, $\nu_K$ is given in Figure [\[fig:nuK\]](#fig:nuK){reference-type="ref" reference="fig:nuK"} below and $\mathop{\mathrm{s}}(\alpha)$ is the Dedekind sum (see [\[eq:def-dedekind\]](#eq:def-dedekind){reference-type="eqref" reference="eq:def-dedekind"}).
:::

::: remark
By the works [@OhtsukiTakata2015; @Ohtsuki52; @OhtsukiYokota6; @Ohtsuki7], the number $\pm 2i \delta_K^{-1}$ can be interpreted as the conjugate of a twisted Reidemeister torsion of $K$. Our method gives the constant term $C_K\cdot D_{K,0}$ as an explicit product of algebraic numbers; in Remark [\[c45\]](#c45){reference-type="ref" reference="c45"} in Section [\[pmt1\]](#pmt1){reference-type="ref" reference="pmt1"} we give as examples its value in the cases of $K=4_1$ and $K=5_1$.
:::

::: remark
Recently, Calegari, Garoufalidis and Zagier [@CalegariGaroufalidisZagier] made a more precise conjecture on $C_K(\alpha)$, predicting it naturally factors as $\mu_{K,8c}\cdot \varepsilon_K(\alpha)^{1/c}/\sqrt{\delta_K}$, where $c$ is the denominator of $\alpha$, $\mu_{K,8c}$ is a $8c$ root of unity, $\varepsilon_K(\alpha)$ is a unit of $F_{K,\alpha}$ and $\delta_K\in F_{K}$. We do not at present have such a precise description of $C_K(\alpha)$. This would presumably require a fine understanding of the congruence sums [\[defcs\]](#defcs){reference-type="eqref" reference="defcs"}.
:::

By the work of Ohtsuki [@Ohtsuki7], the arithmeticity conjecture is known also for $K=7_2$ and we expect that our method would give Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"} also in this case. However, the proof of this case is more involved, so we decided to exclude this case for simplicity. In any case, we want to stress again that the scope of our work is more general and suggests that any proof of the arithmeticity conjecture should be adaptable into a proof of the modularity conjecture via the use of the reciprocity relation [\[eq:mro\]](#eq:mro){reference-type="eqref" reference="eq:mro"}.

The modularity and the volume conjectures likely don't give the full picture on the symmetries of $\mathcal{J}_{K,0}$ nor on its values at roots of unity.

Indeed, in the case of $K=4_1$ we can show that Theorem [\[th:1\]](#th:1){reference-type="ref" reference="th:1"} can be complemented by a second reciprocity formula relating $X=\frac hk$ with $X'=\frac {\overline h}k$, where the overline indicates the multiplicative inverse modulo the denominator. This new reciprocity formula involves the "cotangent sum" (which appears also in the main term in the variation, effective for other ranges of the parameters, of the reciprocity formula given in Theorem [\[th:4\]](#th:4){reference-type="ref" reference="th:4"} below) $$\mathop{\mathrm{c_0}}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  h/k\aftergroup\egroup\originalright)}{( h/k)}{( h/k)}{( h/k)}:=-\sum_{m=1}^{k-1}\frac mk\cot\mathchoice{\mathopen{}\mathclose\bgroup\originalleft( \frac{\pi  mh}{k}\aftergroup\egroup\originalright)}{(\frac{\pi  mh}{k})}{(\frac{\pi  mh}{k})}{(\frac{\pi  mh}{k})},\qquad (h,k)=1,k\geq1,$$ which is itself a quantum modular form [@BettinConrey2013] and has been widely studied due to its connection to the Báez-Duarte-Nyman-Beurling criterion for the Riemann hypothesis (see, for example, [@Bagchi2006; @Baez-Duarte2003; @Baez-DuarteBalazardEtAl2005; @Vasyunin1995]).

::: theo
[]{#th:2 label="th:2"} Let $1\leq h\leq k$ with $(h,k)=1$. Then $$\label{eq:frf}
   \frac{\mathcal{J}_{4_1,0}\big(\ifthenelse{\equal{{\overline{h}}/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  {\overline{h}}/k\aftergroup\egroup\originalright)}{( {\overline{h}}/k)}{( {\overline{h}}/k)}{( {\overline{h}}/k)}}\big)}{\mathcal{J}_{4_1,0}\big(\ifthenelse{\equal{{\overline{k}/}h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  {\overline{k}/}h\aftergroup\egroup\originalright)}{( {\overline{k}/}h)}{( {\overline{k}/}h)}{( {\overline{k}/}h)}}\big) }=\exp\bigg( \frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi} \frac kh+\mathcal{E}( h,k)\bigg),$$ where $$\begin{aligned}
\label{eq:ber}
    \mathcal{E}( h,k) \ll 
    \frac1k \max_{0\leq r' <h}\Big|\sum_{\substack{1\leq n\leq r'}}\cot\Big(\pi\frac{n\overline k}h\Big)\frac{ n}{h}\Big|+\frac {1}{h}\Big|\mathop{\mathrm{c_0}}\Big(\frac{\overline k}h\Big)\Big|
    +\log \frac kh+\frac{k}{h^{2}}.
  
\end{aligned}$$
:::

This may be compared with [\[eq:J0-approxmod\]](#eq:J0-approxmod){reference-type="eqref" reference="eq:J0-approxmod"}. Note that $\mathop{\mathrm{cs}}(4_1) = 0$, so there is no corresponding contribution on the right-hand side of [\[eq:frf\]](#eq:frf){reference-type="eqref" reference="eq:frf"}.

In this case as well, the reciprocity formula [\[eq:frf\]](#eq:frf){reference-type="eqref" reference="eq:frf"} stems from a corresponding relation for the $q$-Pochhammer symbol (see Theorem [\[thp\]](#thp){reference-type="ref" reference="thp"} below). Notice that, despite not giving a full asymptotic expansion, [\[eq:frf\]](#eq:frf){reference-type="eqref" reference="eq:frf"} is completely uniform. In particular, it permits to be successfully iterated for "typical" roots of unity, allowing us to deduce the following law of large numbers for $\log \mathcal{J}_{4_1,0}$.

::: theo
[]{#theo:cfep label="theo:cfep"} For $\alpha\in\mathbb{Q}\cap(0,1)$ with continued fraction expansion $[0;b_1,\dots,b_r]$, $b_r>1$, let $$r(\alpha):=r,\qquad \Sigma(\alpha):=\sum_{\ell=1}^rb_\ell.$$ Then, as $\Sigma(\alpha)/r(\alpha)\to\infty$, we have $$\label{eq:cfef}\begin{aligned}
      \log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{\alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \alpha\aftergroup\egroup\originalright)}{( \alpha)}{( \alpha)}{( \alpha)}})&\sim \frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi} \Sigma(\alpha).
    \end{aligned}$$ In particular, for almost all roots of unity $q$ of order $n\leq N$, one has $$\label{eq:asy}
    \log \mathcal{J}_{4_1,0}(q) \sim  \frac{12 }{\pi^2}\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}\log n \log \log n$$ as $N\to\infty$.
:::

Equation [\[eq:asy\]](#eq:asy){reference-type="eqref" reference="eq:asy"} can be seen as a version of the volume conjecture [\[eq:vc\]](#eq:vc){reference-type="eqref" reference="eq:vc"} for typical roots of unity. Indeed, the volume conjecture provides the asymptotic behavior of $\log \mathcal{J}_{4_1,0}$ at the root of unity $\ifthenelse{\equal{1/N}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  1/N\aftergroup\egroup\originalright)}{( 1/N)}{( 1/N)}{( 1/N)}}$, whereas our result gives the asymptotic for almost all roots of unity of denominator $\leq N$. Notice then in both cases the leading constant involves the hyperbolic volume $\mathop{\mathrm{Vol}}(4_1)$, but the size of $\mathcal{J}_{4_1,0}$ changes dramatically.

Equation [\[eq:cfef\]](#eq:cfef){reference-type="eqref" reference="eq:cfef"} is stronger than [\[eq:asy\]](#eq:asy){reference-type="eqref" reference="eq:asy"}, which will be readily deduced by [@BettinDrappeau], and gives an asymptotic formula in most cases, e.g. when $\alpha$ is restricted to rational numbers with bounded $r(\alpha)$ as the denominator of $\alpha$ goes to infinity. In particular, it generalises the volume conjecture, which corresponds to the case $\alpha=1/N=[0;N]$. It is very likely that the assumption $\Sigma(\alpha)/r(\alpha)\to\infty$ cannot be removed in general. Indeed, if for example $\alpha_n=F_{n-1}/F_{n}$ with $F_n$ the $n$-th Fibonacci number so that $\Sigma(\alpha_n)=r(\alpha_n)+1=n-1$, then Theorem [\[eq:cfef\]](#eq:cfef){reference-type="ref" reference="eq:cfef"} would give $\log \mathcal{J}_{4_1,0}(\ifthenelse{\equal{\alpha_n}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \alpha_n\aftergroup\egroup\originalright)}{( \alpha_n)}{( \alpha_n)}{( \alpha_n)}})\sim C n$, with $C=\frac{\mathop{\mathrm{Vol}}(4_1)}{2\pi}\approx 0.323\dots$, whereas numerically it appears that $F(\alpha_n)$ grows like $C' n$, for $C'\approx 1.1$ (cf. also [@Zagier2010 Figure 6]).

Our proof of Theorems [\[theo:cfep\]](#theo:cfep){reference-type="ref" reference="theo:cfep"} depends crucially on the positivity of the summands in [\[jones41\]](#jones41){reference-type="eqref" reference="jones41"} which is missing if $K\neq 4_1$. Nonetheless, we expect a similar result holds for all hyperbolic knots. Also, since $\Sigma(\alpha)$ is distributed according to a stable law [@BettinDrappeau], we expect the same to hold for $\log |\mathcal{J}_{K,0}(\ifthenelse{\equal{\alpha}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \alpha\aftergroup\egroup\originalright)}{( \alpha)}{( \alpha)}{( \alpha)}})|$ for any hyperbolic knot $K$.

::: conj
[]{#conj:zagier2 label="conj:zagier2"} Let $K$ be a hyperbolic knot. There exists a constant $D_{K}\in\mathbb{R}$ such that for any interval $[a,b]\subset\mathbb{R}$ there holds $$\label{eq:conj}
    \begin{split}
      &|Q_N|^{-1}\Big|\Big\{q\in Q_N\  \Big | \bigg(\frac{ \log |\mathcal{J}_{K,0}(q)|}{\frac{\textnormal{Vol}(K)}{2\pi} \log N}-\frac{12 }{\pi^2 } \log \log N -D_{K}\bigg)\, \in [a,b]\Big\}\Big|\\
      & \qquad = \int_a^b f_1(x; \tfrac6\pi, 1, 0) \mathrm{d}x + o(1)
    \end{split}$$ as $N\to\infty$, where $Q_N$ is the set of roots of unity of order $\leq N$, and $c\mapsto f_1(c; \tfrac6\pi, 1, 0)$ is the density of the stable law $S_1(\tfrac6\pi,1,0)$. In particular, $$\log |\mathcal{J}_{K,0}(q)|\sim \frac{12 }{\pi^2 }\frac{\textnormal{Vol}(K)}{2\pi} \log n \log \log n$$ for almost all roots of unity $q$ of order $n\leq N$ as $N\to\infty$.
:::

In [@Zagier2010] Zagier discusses the continuity with respect to the real topology of $$H_{4_1}(h/k):=\log |\mathcal{J}_{4_1,0}(\ifthenelse{\equal{h/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  h/k\aftergroup\egroup\originalright)}{( h/k)}{( h/k)}{( h/k)}})|-\log |\mathcal{J}_{4_1,0}(\ifthenelse{\equal{k/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  k/h\aftergroup\egroup\originalright)}{( k/h)}{( k/h)}{( k/h)}})|$$ and suggests that $H_{4_1}$ is discontinuous but $\mathcal C^{\infty}$ from the right and the left at non-zero rationals[^2] and continuous but not differentiable as one approaches irrational numbers. Using Lebesgue's integrability condition and [@BettinDrappeau], one can easily show that this continuity condition together with a suitable continuity condition at zero implies Conjecture [\[conj:zagier2\]](#conj:zagier2){reference-type="ref" reference="conj:zagier2"}.

::: theo
[]{#th:pz label="th:pz"} Let $K$ be a hyperbolic knot. Assume the following:

-   $H_{K}(h/k):=\log |\mathcal{J}_{K,0}(\ifthenelse{\equal{h/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  h/k\aftergroup\egroup\originalright)}{( h/k)}{( h/k)}{( h/k)}})|-\log |\mathcal{J}_{K,0}(\ifthenelse{\equal{k/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  k/h\aftergroup\egroup\originalright)}{( k/h)}{( k/h)}{( k/h)}})|$ has a limit as $h/k$ tends to any positive irrational number,

-   $H_{K}(h/k)-\frac{\textnormal{Vol} (K)}{2\pi}\frac{k}h-\frac{3}2\log (k/h)$ is uniformly bounded.

Then Conjecture [\[conj:zagier2\]](#conj:zagier2){reference-type="ref" reference="conj:zagier2"} holds with $D_K = \frac{1-\gamma_0-\log 2}{\pi^2/12} + \frac{24}{\pi\textnormal{Vol}(K)}\int_0^1 \frac{H_{K}(1/t) - \frac{\textnormal{Vol}(K)}{2\pi t}}{1+t}\mathrm{d}t$, the function $H_{K}$ being extended to $\mathbb{R}_{>0}$ by taking limits over the rationals.
:::

::: remark
One could replace the second assumption in Theorem [\[th:pz\]](#th:pz){reference-type="ref" reference="th:pz"} with the assumption that $H_{K}(h/k)-\frac{\textnormal{Vol} (K)}{2\pi}\frac{k}h-\frac{3}2\log (k/h)$ is left and right continuous as $h/k$ approaches any rational number.
:::

In the case of torus knots, the invariant $\mathcal{J}_{K,0}$ can still be constructed and a formula of type [\[eq:J0-approxmod\]](#eq:J0-approxmod){reference-type="eqref" reference="eq:J0-approxmod"} is expected to hold with $\textnormal{Vol}(K)$ replaced by $0$. In this situation, the works [@BaladiVallee2005; @BettinDrappeau] would suggest that $\frac{\log |\mathcal{J}_{K,0}(q)|}{\sqrt{\log n}}$ becomes distributed according to a Gaussian law. In this case however, the conditions of Theorem [\[th:pz\]](#th:pz){reference-type="ref" reference="th:pz"} are not sufficient to conclude.

In view of Theorem [\[th:2\]](#th:2){reference-type="ref" reference="th:2"}, it is natural to wonder if also the function $H_{K}^*(h/k):=\log |\mathcal{J}_{K,0}(\ifthenelse{\equal{\overline h/k}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \overline h/k\aftergroup\egroup\originalright)}{( \overline h/k)}{( \overline h/k)}{( \overline h/k)}})|-\log |\mathcal{J}_{4_1,0}(\ifthenelse{\equal{\overline k/h}{}}{{\rm e}}{\operatorname{e}\mathchoice{\mathopen{}\mathclose\bgroup\originalleft(  \overline k/h\aftergroup\egroup\originalright)}{( \overline k/h)}{( \overline k/h)}{( \overline k/h)}})|$ could be regular at irrational points. We can answer this question in the negative in the case of $K=4_1$.

::: theo
[]{#concor label="concor"} For all $x\in[0,1]$ we have $\limsup_{y\to x^\pm,\, y\in\mathbb{Q}} |H^\ast_{4_1}(y)|=+\infty$.
:::

<figure id="fig:graph-global">
<table>
<tbody>
<tr class="odd">
<td style="text-align: center;"><img src="plot-g-full.png" style="width:40.0%" alt="image" /></td>
<td style="text-align: center;"><img src="plot-gstar-full.png" style="width:40.0%" alt="image" /></td>
</tr>
</tbody>
</table>
<figcaption>Global graph of <span class="math inline"><em>H</em><sub>4<sub>1</sub></sub></span> and <span class="math inline"><em>H</em><sub>4<sub>1</sub></sub><sup>*</sup></span></figcaption>
</figure>

<figure id="fig:graph-globalast">
<table>
<tbody>
<tr class="odd">
<td style="text-align: center;"><img src="plot-g-zoom.png" style="width:40.0%" alt="image" /></td>
<td style="text-align: center;"><img src="plot-gstar-zoom.png" style="width:40.0%" alt="image" /></td>
</tr>
</tbody>
</table>
<figcaption>Graph of <span class="math inline"><em>H</em><sub>4<sub>1</sub></sub></span> and <span class="math inline"><em>H</em><sub>4<sub>1</sub></sub><sup>*</sup></span> around <span class="math inline"><em>x</em> = 0.485</span></figcaption>
</figure>

[^1]: In what follows, a matrix in $\textnormal{SL}(2, \mathbb{R})$ acts on $\mathbb{C}$ by homography.

[^2]: This continuity property at rationals follows from the modularity conjecture but only when approaching a rational $h/k=[0;b_1,\dots,b_r]$ with fractions essentially of the form $[0;b_1,\dots,b_r,N]$ with $N\to\infty$; and not, for example, with $[0;b_1,\dots,b_r,N_1,N_2]$ with both $N_1,N_2\in\mathbb{N}$ going to infinity.
