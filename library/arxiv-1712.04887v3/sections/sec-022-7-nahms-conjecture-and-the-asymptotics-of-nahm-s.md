---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-022-7-nahms-conjecture-and-the-asymptotics-of-nahm-s
section_title: "Nahm's conjecture and the asymptotics of Nahm sums at roots of unity"
section_number: 7
pages: 33-37
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.986
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sec.nahm label="sec.nahm"}

In Section [\[sub.intro.nahm\]](#sub.intro.nahm){reference-type="ref" reference="sub.intro.nahm"} of the introduction, we saw that the $S$-units constructed in this paper from elements of the Bloch group appear naturally (although in general only conjecturally) in connection with the asymptotic properties of the Kashaev invariant of knots and its Galois twists. A second place where these units appear is in the radial asymptotics of so-called Nahm sums. This was shown in [@GZ:asymptotics] and is quoted (in a simplified form) in Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} below. In this section, we explain this and give two applications, the proof of Theorem [\[thm.eta\]](#thm.eta){reference-type="ref" reference="thm.eta"} and the proof of Nahm's conjecture relating the modularity of Nahm sums to the vanishing of certain elements in Bloch groups.

Nahm sums are special $q$-hypergeometric series whose summand involves a quadratic form, a linear form and a constant. They were introduced by Nahm [@Nahm] in connection with characters of rational conformal field theories, and led to his above-mentioned conjecture concerning their modularity. They have also appeared recently in quantum topology in relation to the stabilization of the coefficients of the colored Jones polynomial (see Garoufalidis-Le [@GL:Nahm]), and they are building blocks of the 3D-index of an ideally triangulated manifold due to Dimofte--Gaiotto--Gukov [@DGG1; @DGG2]. Further connections between quantum topological invariants and Nahm sums are given in [@GZ:qseries], where one sees once again the appearance of the units $R_\zeta(\xi)^{1/n}$.

In the first subsection of this section, we review Nahm sums and the Nahm conjecture and state Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} relating the asymptotics of Nahm sums at roots of unity to the near units of Theorem [\[thm.R\]](#thm.R){reference-type="ref" reference="thm.R"}. This is then applied in §[\[sub.ag\]](#sub.ag){reference-type="ref" reference="sub.ag"} to a particular Nahm sum (namely, the famous Andrews-Gordon generalization of the Rogers-Ramanujan identities) to prove Equation [\[CompRz\]](#CompRz){reference-type="eqref" reference="CompRz"} of the introduction (Theorem [\[thm.eta\]](#thm.eta){reference-type="ref" reference="thm.eta"}). In the final subsection, we use Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} together with Theorem [\[thm.R\]](#thm.R){reference-type="ref" reference="thm.R"} to give a proof of Nahm's conjecture.

## Nahm's conjecture and Nahm sums {#sub.nahm}

Nahm's conjecture gives a very surprising connection between modularity and algebraic $K$-theory. More precisely, it predicts that the modularity of certain $q$-hypergeometric series ("Nahm sums\") is controlled by the vanishing of certain associated elements in the Bloch group $B(\overline{\mathbf Q})$.

The definition of Nahm sums and the question of determining when they are modular were motivated by the famous Rogers-Ramanujan identities, which say that $$G(q)\,:=\,\sum_{n=0}^\infty\frac{q^{n^2}}{(q)_n}
 \,=\,\prod_{\substack{ n>0 \\ (\frac n5)=1}}\!\frac1{1-q^n},\qquad
H(q)\,:=\,\sum_{n=0}^\infty\frac{q^{n^2+n}}{(q)_n}
 \,=\,\prod_{\substack{ n>0 \\ (\frac n5)=-1}}\!\frac1{1-q^n}\,,$$ where $(q)_n=(1-q)\cdots(1-q^n)$ is the $q$-Pochhammer symbol or quantum $n$-factorial. These identities imply via the Jacobi triple product formula that the two functions $q^{-1/60}G(q)$ and $q^{11/60}H(q)$ are quotients of unary theta-series by the Dedekind eta-function and hence are modular functions. (Here and from now on we will allow ourselves the abuse of terminology of saying that a function $f(q)$ is modular if the function $\widetilde f(\tau)=f(e^{2\pi i\tau})$ is invariant under the action of some subgroup of finite index of $\mathrm{SL}(2,\mathbf Z)$.) To see how general this phenomenon might be, Nahm [@Nahm] considered the three-parameter family $$\label{eq.FABC1}
f_{A,B,C}(q) :=q^C f_{A,B}(q) := q^C
\sum_{m\ge0} \frac{q^{\frac A2m^2+Bm}}{(q)_m} \qquad(A\in\mathbf Q_{>0},\;B,\,C\in\mathbf Q)$$ These are formal power series with integer coefficients in some rational power of $q$, and are analytic in the unit disk $|q|<1$, but they are very seldom modular: apart from the two Rogers-Ramanujan cases $(A,B,C)=(2,0,-\frac1{60})$ or $(2,1,\frac{11}{60})$, only five further cases $(1,0,-\frac1{48})$, $(1,\pm\frac12,\frac1{24})$, $(\frac12,0,-\frac1{40})$ and $(\frac12,\frac12,\frac1{40})$ were known for which $f_{A,B,C}$ is modular, and it was later proved ([@Terhoeven], [@Zagier]) that these are in fact the only ones. Since this list of seven examples is not very enlightening, Nahm introduced also a higher-order version $$\label{eq.FABC}
f_{A,B,C}(q)  :=q^C f_{A,B}(q):= q^C
\sum_{m\in\mathbf Z_{\ge0}^r} \frac{q^{\frac12 m^tAm + Bm}}{(q)_{m_1}\cdots(q)_{m_r}}\,,$$ where $A=(a_{ij})$ is a symmetric positive definite $r \times r$ matrix with rational entries, $B \in \mathbf Q^r$ a column vector, and $C \in \mathbf Q$ a scalar, and asked for which triples $(A,B,C)$ the function $\widetilde f_{A,B,C}(\tau)=f_{A,B,C}(e^{2\pi i\tau})$ is modular. His conjecture gives a partial answer to this question.

To formulate this conjecture, Nahm made two preliminary observations.

\(i\) Let $X=(X_1,\dots,X_r)\in\mathbf C^r$ be a solution of *Nahm's equations* $$\label{NahmEq}
1 \,-\, X_i \;=\; \prod_{j=1}^r X_j^{a_{ij}} \qquad(1\le j\le r)$$ (or symbolically $1-X=X^A$), and let $F$ be the field they generate over $\mathbf Q$, which will typically be a number field since [\[NahmEq\]](#NahmEq){reference-type="eqref" reference="NahmEq"} is a system of $r$ equations in $r$ unknowns and generically defines a 0-dimensional variety. Then the element $[X]=[X_1]+\cdots[X_r]$ of $\mathbf Z[F]$ belongs to the kernel of the map [\[defd\]](#defd){reference-type="eqref" reference="defd"}, because $$d\bigl([X]\bigr) \;=\; \sum_i(X_i)\wedge(1-X_i) \;=\; 
\sum_{i,\,j} a_{ij}\,(X_i)\wedge(X_j)\;=\;0$$ by virtue of the symmetry of $A$. (This calculation makes sense as it stands if $A$ has integer entries; if the entries are only rational, we have to tensor everything with $\mathbf Q$.) Therefore $[X]$ determines an element of the Bloch group $B(F)\otimes\mathbf Q$ and it makes sense to ask whether this element vanishes. This is equivalent to the vanishing of the numbers $D(\sigma X)=\sum D(\sigma X_i)$ for all embeddings $\sigma:F\hookrightarrow\mathbf C$, where $D(x)$ is the Bloch-Wigner dilogarithm function, and this condition can be either tested numerically to any precision or else verified rigorously by writing a multiple of $[X]$ as a linear combination of 5-term relations.

\(ii\) The first observation is that if $A$ is a positive definite symmetric matrix, then there is a distinguished solution of the Nahm equations, namely the unique solution $X^A=(X_1^A,\dots,X_r^A)$ with $0<X_i^A<1$ for all $i$. We denote by $\xi_A$ the corresponding element $[X^A]$ of the Bloch group. Then since $X^A$ is real, we obtain a further characteristic property when this element is torsion, namely that the real number $\mathrm L(\xi_A)=\sum\mathrm L(X_i)$, where $\mathrm L(x)$ is the Rogers dilogarithm function as defined below, is a rational multiple of $\pi^2$. But it can be shown fairly easily that $f_{A,B,C}(e^{-h})$ has an asymptotic expansion as $\,e^{\mathrm L(\xi_A)/h+\text O(1)}$ as $h\to0^+$ for any $B$ and $C$ (in fact, a full asymptotic expansion of the form $\,e^{\mathrm L(\xi_A)/h+c_0+c_1h+\cdots}$ is given in [@Zagier]). Since a modular function must have an expansion $\,e^{c/h+\text O(1)}$ with $c\in\mathbf Q\pi^2$, this already gives a strong indication of a relation between the modularity of Nahm sums and the vanishing (up to torsion) of the associated elements of Bloch groups.

Based on these observations, one can consider the following three properties of a matrix $A$ as above:

1.  []{#nahma label="nahma"} The class $[X]\in B(\mathbf C)$ vanishes for all solutions $X$ of the Nahm equations [\[NahmEq\]](#NahmEq){reference-type="eqref" reference="NahmEq"}.

2.  []{#nahmb label="nahmb"} The special class $\xi_A\in B(\mathbf C)$ associated to the solution $X^A$ of [\[NahmEq\]](#NahmEq){reference-type="eqref" reference="NahmEq"} vanishes.

3.  []{#nahmc label="nahmc"} The function $f_{A,B,C}(q)$ is modular for some $B\in\mathbf Q^r$ and $C\in\mathbf Q$.

Trivially [\[nahma\]](#nahma){reference-type="ref" reference="nahma"} $\Rightarrow$ [\[nahmb\]](#nahmb){reference-type="ref" reference="nahmb"}. Nahm's conjecture (see [@Nahm] and [@Zagier]) says that [\[nahma\]](#nahma){reference-type="ref" reference="nahma"} $\Rightarrow$ [\[nahmc\]](#nahmc){reference-type="ref" reference="nahmc"} and [\[nahmc\]](#nahmc){reference-type="ref" reference="nahmc"} $\Rightarrow$ [\[nahmb\]](#nahmb){reference-type="ref" reference="nahmb"}. (The possible stronger hypothesis that [\[nahmb\]](#nahmb){reference-type="ref" reference="nahmb"} alone might already imply [\[nahmc\]](#nahmc){reference-type="ref" reference="nahmc"} was eliminated in [@Zagier] using the $2\times2$ matrix $A=(\begin{smallmatrix} 8 & 5 \\ 5 & 4\end{smallmatrix})$, and the other possible stronger assertion that [\[nahmc\]](#nahmc){reference-type="ref" reference="nahmc"} might require [\[nahma\]](#nahma){reference-type="ref" reference="nahma"} was shown to be false by Vlasenko and Zwegers [@VZ] with the counterexample $A=(\begin{smallmatrix} 3/2 & 1/2 \\ 1/2 & 3/2\end{smallmatrix})$.) This conjecture had a dual motivation: on the one hand, the above-mentioned fact that both [\[nahmb\]](#nahmb){reference-type="ref" reference="nahmb"} and [\[nahmc\]](#nahmc){reference-type="ref" reference="nahmc"} force the rationality of $L(\xi_A)/\pi^2$, which is most unlikely to happen "at random,\" and on the other hand, a large number of supporting examples coming from the characters of rational conformal field theories, which are always modular functions and where the condition in the Bloch group can also be verified in many cases. Here we are concerned with an extension of the first of these two aspects, namely the asymptotics of the Nahm sum $f_{A,B,C}(q)$ as $q$ tends radially to *any* root of unity, not just to 1.

In order to state the asymptotic formula, we need to define the Rogers dilogarithm. In our normalization (which is $\pi^2/6$ minus the standard one as given, for instance, in [@Zagier], §II.1A), this is the function defined on $\mathbf R\smallsetminus\{0,1\}$ by $$\label{normalization}
\mathrm L(x) \;=\; 
\begin{cases}
\frac{\pi^2}6 \,-\,\mathrm{Li}_2(x) \,-\,\frac12\,\log(x)\,\log(1-x) & \text{if $0<x<1$,}\\
\,-\,\mathrm L(1/x) & \text{if $x>1$,} \\  \frac{\pi^2}6 \,-\,\mathrm L(1-x) & \text{if $x<0$}
\end{cases}$$ (here $\mathrm{Li}_2(x)=\sum_{n=1}^\infty\frac{x^n}{n^2}$ is the standard dilogarithm) and extended by continuity to a function $\mathbf P^1(\mathbf R)\to\mathbf R/\frac{\pi^2}2\mathbf Z$ by sending the three points $0$, 1 and $\infty$ to $\frac{\pi^2}6$, 0, and $-\frac{\pi^2}6$. Its linear extension to $Z(\mathbf R)$ vanishes on the group $C(\mathbf R)$ as defined at the beginning of §[\[sub.intro.bloch\]](#sub.intro.bloch){reference-type="ref" reference="sub.intro.bloch"}.

We comment here that the specific choice of the definition of the Bloch group in

Definition [\[def.BF\]](#def.BF){reference-type="ref" reference="def.BF"}, which forces $3[0]=0$, $[X]+[1/X]=0$ and $[X]+[1-X]=[0]$ for any field $F$ and any element $X$ of $\mathbf P^1(F)$, was chosen precisely so that $L$ is well-defined on $B(\mathbf R)$ and takes values in the group $\mathbf R/\frac{\pi^2}2\mathbf Z$ rather than just its quotient $\mathbf R/\frac{\pi^2}6\mathbf Z$.

Specifically, let $A$, $B$ and $C$ be as above let $X=X^A$ be the distinguished solution of [\[NahmEq\]](#NahmEq){reference-type="eqref" reference="NahmEq"} as in (ii) and $F$ the corresponding number field, and for each integer $n$ choose a primitive $n$th root of unity $\zeta$, set $F_n=F(\zeta)$ and denote by $H=H_n$ the Kummer extension of $F_n$ obtained by adjoining the positive $n$th roots $x_i$ of the $X_i$. We are interested in the asymptotic expansion of $f_{A,B,C}(\zeta e^{-h/n})$ as $h\to0^+$. Strictly speaking, this only makes sense if $A$ has integral coefficients, $B$ is congruent to $\frac12\text{diag}(A)$ modulo $\mathbf Z^r$, and $C\in\mathbf Z$, since otherwise the quadratic function $q^{\frac12nAn^t+nB+C}$ occurring in the definition of $f_{A,B,C}$ is not uniquely defined. We get around this by picking a representation of $\zeta$ as $\mathbf{e}(a/n)$ for some $a\in\mathbf Z$ (where $\mathbf{e}(x)=e^{2\pi i x}$) and interpreting $f_{A,B,C}(\zeta e^{-h/n})$ as $\widetilde f_{A,B,C}\bigl(\frac{a+i\hbar}n\bigr)$, where $\hbar=\frac h{2\pi}$. The full asymptotic expansion of $f_{A,B,C}(\zeta e^{-h/n})$ as $h\to0^+$ was calculated in [@GZ:asymptotics] using the Euler--Maclaurin formula, generalizing an earlier result in [@Zagier] for the case $n=1$. We do not give the complete formula here, but only the simplified form as needed for the applications we will give. In the statement of the theorem we have abbreviated by $\Delta_X$ the diagonal matrix whose diagonal is a given vector $X$.

::: theorem
[@GZ:asymptotics Thm 3.1] []{#thm.nahmEM label="thm.nahmEM"}

Let $A \in M_r(\mathbf Q)$ and $B \in \mathbf Q^r$ be as above. Let $n$ be a positive integer coprime to the denominator of $A$ and $B$. Then for every primitive $n$th root of unity $\zeta$, we have $$\label{eq.nahmEM}
f_{A,B} \bigl(\zeta\,e^{-h/n}\bigr)  \;=\;  \mu \, \omega 
\,e^{\mathrm L(\xi_A)/nh}\, \bigl(\Phi_\zeta(h) \,+\, \text{O}(h^K)\bigr)$$ for all $K>0$ as $h\to0^+$, where $\omega^2 \in F^\times$, $\mu = \mathbf{e}(r(n-1)(n-2)/24 n)$, and $\Phi_\zeta(h)=\Phi_{A,B,\zeta}(h)$ is an explicit power series satisfying the two properties $\Phi_\zeta(h)^n\in F_n[[h]]$ and $$P_\zeta(\xi_A)^{1/n} {D_{\zeta}(1)^{r/n}} \,\Phi_\zeta(h)\in F_n[[h]].$$ Moreover, if $\Phi_\zeta(0)^n\neq 0$, then its image in $F_n^\times/F_n^{\times n}$ belongs to the $\chi^{-1}$ eigenspace.
:::

::: corollary
[]{#UnitCor label="UnitCor"} If $\Phi_\zeta(0) \neq 0$, then

the product of the power series $\Phi_\zeta(h)$ with $\varepsilon^{1/n}$ for any unit $\varepsilon$ representing $R_\zeta(\xi_A)$ belongs to $F_n[[h]]\,$.
:::

::: proof
*Proof.* Let $\varepsilon\in F_n^\times$ denote a representative of $R_\zeta(\xi_A)$. On the one hand, Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} and Remark [\[rem.effectiveR\]](#rem.effectiveR){reference-type="ref" reference="rem.effectiveR"} imply that $\Phi_\zeta(0) \varepsilon^{1/n} \in F_n^\times$. On the other hand, Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} and our assumption implies that $(\Phi_\zeta(h)/\Phi_\zeta(0))^n \in F_n[[h]]$. Since $\Phi_\zeta(h)/\Phi_\zeta(0)$ is a power series with constant term $1$, it follows that $\Phi_\zeta(h)/\Phi_\zeta(0) \in F_n[[h]]$. Combining both conclusions, it follows that $\varepsilon^{1/n} \Phi_\zeta(h) \in F_n[[h]]$. ◻
:::

::: remark
In the theorem, we do *not* assert that the power series $\Phi$ cannot vanish identically (which is why we wrote an equality sign and $\Phi(h)+\text O(h^K)$ in [\[eq.nahmEM\]](#eq.nahmEM){reference-type="eqref" reference="eq.nahmEM"} rather than writing an asymptotic equality sign and putting simply $\Phi(h)$ on the right), and indeed this often happens, for instance, when $f_{A,B,C}$ is modular and we are expanding at a cusp not equivalent to 0. Of course, the corollary is vacuous if $\Phi$ vanishes.
:::
