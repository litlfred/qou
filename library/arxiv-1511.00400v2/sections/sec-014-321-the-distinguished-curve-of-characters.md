---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-014-321-the-distinguished-curve-of-characters
section_title: "The distinguished curve of characters"
section_number: 3.2.1
pages: 19-26
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.97
---
The variety of $\mathrm{SL}_2(\mathbb{C})$-representations of $M^3$ is the set $$\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C})),$$ which it is an affine algebraic set: if a generating set of $\pi_1M^3$ has $k$ elements, then $\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))$ embeds in $\mathrm{SL}_2(\mathbb{C})^k\subset  
\mathbb{C}^{4 k}$, by mapping a representation to the image of its generators. The algebraic equations are induced by the relations of the group.

The group $\mathrm{PSL}_2(\mathbb{C})$ acts on $\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))$ by conjugation, and the affine algebraic quotient is the variety of characters $$X(M^3):= X(M^3,\mathrm{SL}_2(\mathbb{C}))=  \hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))/\! /  \mathrm{PSL}_2(\mathbb{C}).$$ This is defined in terms of the invariant functions: $X( M^3,\mathrm{SL}_2(\mathbb{C}))$ is the algebraic affine set whose function ring $\mathbb{C}[  X(M^3,\mathrm{SL}_2(\mathbb{C})) ]$ is the ring of invariant functions $$\mathbb{C}[ \hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))]^{\mathrm{PSL}_2(\mathbb{C})}.$$

By [@ThurstonBook], see also [@BoileauPorti Appendix B] each component that contains the lift of the holonomy of $M^3$ is a curve.

::: definition
An irreducible component of $X(M^3,\mathrm{SL}_2(\mathbb{C}))$ that contains a lift of the holonomy is called a *distinguished component* and it is denoted by $X_0(M^3)$.
:::

For many manifolds, e.g. for 2-bridge knot exteriors, there is a unique distinguished component. A priori there could be more components, but the definition makes sense because they would be isomorphic. More precisely, there are two characters of the holonomy representation in $\mathrm{PSL}_2(\mathbb{C})$ that are complex conjugate from each other, that correspond to the different orientations. When lifting them to $\mathrm{SL}_2(\mathbb{C})$, this gives $2 \vert   H^1(M^3;\mathbb{Z}/2\mathbb{Z}) \vert$ characters, two for each spin structure. The corresponding components $X_0(M^3)$ are isomorphic by means of the natural action of $H^1(M^3;\mathbb{Z}/2\mathbb{Z})$ and complex conjugation.

Recently, Casella, Luo, and Tillmann [@CLT] have shown an example of hyperbolic manifold with one cusp $M^3$ such that the holonomy characters of the different orientations lie in different components of $X(M^3,\mathrm{PSL}_2(\mathbb{C}))$. To my knowledge, the following question is still open:

::: question
Once $M^3$ is *oriented*, are all the lifts of the oriented holonomy contained in a single irreducible component of $X(M^3,\mathrm{SL}_2(\mathbb{C}))$?
:::

The distinguished component $X(M^3,\mathrm{SL}_2(\mathbb{C}))$ is a curve and it was studied by Thurston in his proof of the hyperbolic Dehn filling theorem [@ThurstonBook]. More precisely, in a neighborhood of the holonomy of the complete structure of $M^3$, the representations are holonomies of incomplete structures, and in some cases the completion is a Dehn filling. This is discussed in Paragraph [0.0.2](#sec:Dehnfilling){reference-type="ref" reference="sec:Dehnfilling"}.

### Torsion on the distinguished curve of characters

We say that a character $\chi\in X(M^3)$ is trivial if it takes values in $\{\pm 2\}$, i.e. it is a lift or the trivial character in $\mathrm{PSL}_2(\mathbb{C})$.

An irreducible character is the character of a unique conjugacy class of representations. A reducible character can correspond to more conjugacy classes, but if the character is non-trivial, then either all representations with this character are acyclic, either none of them is (Lemma [\[lemma:acyclicorbit\]](#lemma:acyclicorbit){reference-type="ref" reference="lemma:acyclicorbit"}).

::: definition
Define the torsion function on $X_0(M^3)$ minus the trivial character: $$\label{eqn:torsionfunct2}
\mathbb{T}_M(\chi_\rho)=\left\{
\begin{array}{ll}
\operatorname{tor}(M^3,\rho) & \textrm{if }\rho\textrm{ is acyclic;} \\
0 &  \textrm{if } \chi_\rho \textrm{ is non-trivial and } \rho \textrm{ 
non-acyclic,}
\end{array}
\right.$$ where $\chi_\rho$ denotes the character of $\rho$.
:::

::: prop
[]{#prop:rational label="prop:rational"} For a hyperbolic oriented manifold with one cusp, the torsion defines a rational function on $X_0(M^3)$, $\mathbb{T}_M\in \mathbb{C}(X_0(M^3))$, which is regular away from the trivial character.

In particular, if the trivial character is not contained in $X_0(M^3)$ (e.g. if $b_1(M^3)=1$), then $\mathbb{T}_M\in \mathbb{C}[X_0(M^3)]$, i.e. it is holomorphic (with no poles) $$\mathbb{T}_M \colon X_0(M^3)\to \mathbb{C}.$$
:::

::: remark
We prove that the trivial representation cannot be approached by irreducible ones when $b_1(M^3)=1$ in Appendix [\[sec:notapprox\]](#sec:notapprox){reference-type="ref" reference="sec:notapprox"}. This is always the case when $M^3$ is a knot exterior.
:::

::: proof
*Proof.* The dimension of each cohomology group is upper semi-continuous on the representation (see [@Heusener-Porti2011 Lemma 3.2], this is a particular case of the semi-continuity theorem [@Hartshorne1977 Ch. III, Theorem 12.8]). With Lemma [\[lemma:acyclicorbit\]](#lemma:acyclicorbit){reference-type="ref" reference="lemma:acyclicorbit"}, we can conclude that acyclicity holds true in a dense open Zariski domain $U\subset  X_0(M^3)$, after removing the trivial character if required. The fact that the function $\mathbb{T}_M$ is algebraic on this domain is clear, as this is defined from polynomials on the entries of $\rho$. Invariance by conjugation is one of the properties of the torsion. Thus it remains to deal with the points where it is not acyclic. Recall that by Lemma [\[lemma:acyclicorbit\]](#lemma:acyclicorbit){reference-type="ref" reference="lemma:acyclicorbit"} a representation with nontrivial character is acyclic if and only all representations with the same character are.

First notice that $H^0(M^3;\rho)$ is trivial when the character $\chi_\rho$ is non-trivial, because this cohomology group is naturally isomorphic to the space of invariants $\mathbb{C}^{\rho(\pi_1 M^3)}$. More precisely, $\mathbb{C}^{\rho(\pi_1 M^3)}$ is non-trivial only when all elements in $\rho(\pi_1 M^3)$ have $1$ as eigenvalue, which means that their trace is $2$, i.e. $\chi_\rho$ is trivial. Thus by duality $H_0(M^3;\rho)=  0$ when $\chi_\rho$ is non-trivial.

Now fix a representation $\rho_1$ which is not acyclic and non-trivial. Non-acyclicity implies that $H_1(M^3;\rho_1)\neq 0$ and $H_2(M^3;\rho_1)\neq 0$, as $H_0(M^3;\rho_1) = 0$, the homotopical dimension of $M^3$ is $2$, and $\chi(M^3)=0$. Notice that $M^3$ has the simple homotopy type of a 2-complex (see [@Nicolaescu Page 54] for instance), that can be used to compute the torsion. Using the notation of Section [\[sec:comb\]](#sec:comb){reference-type="ref" reference="sec:comb"}, fix a basis $\{v_1,v_2\}$ for $\mathbb{C}^2$ and lifts of cells $\tilde e^i_j$ of a triangulation of $M^3$. Then define a family of basis $c_i(\rho)$ by varying the representation in $v_k\otimes_\rho \tilde e^i_j$. Now choose $\tilde b_1(\rho)=c_2(\rho)$ and $\tilde b_0(\rho)$, a linear combination of $c_1(\rho)$ with constant coefficients (though $c_1(\rho)$ changes with $\rho$), so that $\partial(\tilde b_0(\rho_1))=c_0(\rho_1)$. The function $$\label{eqn:ratiotau2}
\rho\mapsto [\partial \tilde b_1(\rho)\sqcup \tilde b_0(\rho),c_1(\rho) ]/[\partial \tilde b_0( \rho),c_0(\rho)]$$ is well defined in the set where its denominator does not vanish. This is a Zariski open set that contains $\rho_1$. On this set $\partial \tilde b_1(\rho)=\partial c_2(\rho)$ has maximal rank iff $\rho$ is acyclic, thus the function [\[eqn:ratiotau2\]](#eqn:ratiotau2){reference-type="eqref" reference="eqn:ratiotau2"} vanishes when $\rho$ is not acyclic, and when $\rho$ is acyclic [\[eqn:ratiotau2\]](#eqn:ratiotau2){reference-type="eqref" reference="eqn:ratiotau2"} is the torsion. ◻
:::

::: example
[]{#ex:fig8sl2 label="ex:fig8sl2"} For the figure eight knot, in [@Kitano94b] Kitano computes it: $$\mathbb{T}_M(\rho)=2-2\operatorname{tr}(\rho(m))=2-2\chi_\rho(m)\, ,$$ where $m$ denotes the meridian of the knot. Notice that here the function only depends on $\operatorname{tr}(\rho(m))$, namely the evaluation of the character at $m$, and one does not need to describe the variety of characters. In general, as $\operatorname{tr}(\rho(m))$ is a non-constant function on the curve $X_0(M^3)$, $\mathbb{T}_M(\rho)$ and $\chi_\rho(m)= \operatorname{tr}(\rho(m))$ are related by a polynomial equation; compare with [@DuboisG16].
:::

### Dehn filling space {#sec:Dehnfilling}

Again let $M^3$ be an oriented, finite volume hyperbolic manifold with one cusp. Consider the peripheral torus $T^2$, which is the boundary of a compact core of $M^3$. Choose a frame on the peripheral torus $T^2$, i.e. two simple closed curves that generate $\pi_1 T^2$, denote this frame by $\{m,l\}$. The notation suggests that the canonical choice for a knot exterior is the pair meridian-longitude.

A *Dehn filling* on $M^3$ is the result of gluing a solid torus $D^2\times S^1$ to a compact core $M^3$ along the boundary. Up to homeomorphism, this manifold depends only on the (unoriented) homology class in $T^2$ of the meridian, i.e. the curve $\partial D^2\times \{*\}$. This curve is written as $\pm (p\, m+q\, l)$, and the Dehn filling is denoted by $M^3_{p/q}$.

When $\vert p\vert +\vert q\vert$ is sufficiently large, by Thurston's theorem $M_{p/q}$ is hyperbolic. To prove it, he introduces the *Thurston's parameters* of the Dehn filling space, by writing, for representations close to the holonomy of the complete hyperbolic structure, $$\label{eqn:u}
\rho(m)=\pm \begin{pmatrix}
         e^{u/2} & 1 \\ 0 & e^{-u/2}
        \end{pmatrix}
        \qquad
 \rho(l)   =  \pm \begin{pmatrix}
         e^{v/2} & f(u) \\ 0 & e^{-v/2}
        \end{pmatrix}$$ with $u,v\in\mathbb{C}$ in a neighborhood of the origin. For the holonomy of the complete structure, $u=v=0$ and write $$\operatorname{cs}= \operatorname{cs}(l,m)=f(0)\in \mathbb{C}-\mathbb{R}.$$

::: definition
[]{#def:cs label="def:cs"} The parameter $u\in U \subset \mathbb{C}$ as above is called the *Thurston parameter* and $\operatorname{cs}= \operatorname{cs}(l,m)\in \mathbb{C}-\mathbb{R}$ the *cusp shape* of the complete structure.
:::

The Thurston parameter $u$ is in fact a parameter of a double branched covering of a neighborhood of the lift of the holonomy $\varrho$, as the local parameter of $X_0(M^3)$ is $\operatorname{tr}(\rho(m))= \pm 2 \cosh\frac{u}{2}$. For the complete structure, the peripheral group acts as a lattice on a horosphere, that we view as $\mathbb{C}$. Up to affine equivalence, this lattice is given by $m\mapsto 1$, $l\mapsto \operatorname{cs}$.

::: lemma
There exists a (standard) neighborhood of the origin $U\subset \mathbb{C}$ such that:

(a) The map $U\to X_0(M^3)$ such that $u\mapsto \chi_\rho$, where $\rho$ is as in [\[eqn:u\]](#eqn:u){reference-type="eqref" reference="eqn:u"} is a double branched covering of a neighborhood in $X_0(M^3)$ of the character of the holonomy of the complete structure.

(b) $v$ is an analytic odd function on $u$ that satisfies $$v(u)=\operatorname{cs}u+ O(u^3).$$

(c) $f(u)=\sinh(v)/\sinh(u)$.
:::

The *generalized Dehn filling coefficients* are the $(p,q)\in\mathbb{R}^2\cup\{\infty\}$ such that $$\label{eqn:pq}
p\,u+q\, v=2\pi i$$ when $u\neq 0$ and $\infty$ when $u=0$.

::: thm
[@ThurstonBook; @NZ85] The generalized Dehn filling coefficients define a homeomorphism between $U$ and a neighborhood of $\infty$ in $S^2=\mathbb{R}^2\cup\{\infty\}$. If a pair of coprime integers $(p,q)\in\mathbb{Z}^2$ lies in the image of this homeomorphism, then $M^3_{p/q}$ is hyperbolic, with holonomy whose restriction to $M^3$ satisfies [\[eqn:pq\]](#eqn:pq){reference-type="eqref" reference="eqn:pq"}.
:::

We are interested in properties of $M^3_{p/q}$.

::: thm
$$\operatorname{vol}(M^3_{p/q})=\operatorname{vol}(M^3)-\pi^2\frac{\operatorname{Im}(\operatorname{cs})}{|p+\operatorname{cs}q|^2}+ O\left(\frac{1}{|p+\operatorname{cs}q|^4 }\right).$$
:::

We are also interested in the complex length of the soul of the solid torus added by Dehn filling, which is a short geodesic. Let $r$ and $s$ be integers satisfying $p\, s-q\, r=1$, this complex length is $r\, u+s\, v$. A straightforward computation yields [@Memoirs]:

::: remark
[]{#rem:length label="rem:length"} The complex length of the core of the solid torus $M_{p/q}^3$ is $$r\, u+s\, v= 2\pi i\frac{r}{p}+ \frac{v}{p}= 2\pi i\frac{s}{q}+ \frac{u}{q}$$
:::

Given a spin structure $\sigma$ on $M^3$, it may extend or not to $M_{p,q}^3$. It is easy to give a characterization using the bijection of Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}.

::: lemma
[@MFP14] []{#lemma:extendspin label="lemma:extendspin"} A spin structure $\sigma$ on $M$ extends to $M_{p,q}$ iff the corresponding lift of the holonomy $\varrho_{\sigma}$ (for the complete structure on $M^3$) satisfies $$\operatorname{tr}(\varrho_{\sigma}( p\, m+ q\, l ))=-2.$$
:::

### Torsion for Dehn fillings

Let $\vert p\vert +\vert q\vert$ be sufficiently large and let $\sigma$ be a spin structure on $M^3$ extensible to $M_{p/q}^3$. Let $\rho_{p/q,\sigma}$ denote the lift of the holonomy of the restriction to $M^3$ of the hyperbolic structure on $M_{p/q}^3$, and $\chi_{p/q,\sigma}$ the corresponding character. Let $\lambda_{p/q}$ denote the complex length of the soul of the filling torus. There is a surgery formula:

::: prop
[]{#prop:SF label="prop:SF"} Let $M^3$ be as above. For $\vert p\vert +\vert q\vert$ sufficiently large: $$\tau(M_{p/q}^3,\sigma)=  \frac{\mathbb{T}_{M}(\chi_{p/q,\sigma} )}{ 2 
(1-\cosh(\lambda_{p/q}/2 ) ) }.$$
:::

This proposition can be proved using Mayer-Vietoris (Proposition [\[prop:MV\]](#prop:MV){reference-type="ref" reference="prop:MV"}) to the pair $(M^3, D^2\times S^1 )$. The proof can be found for instance in [@Kitano15] for the figure eight knot, and in [@Tran15] for twist knots, but it applies to every cusped manifold, and it is essentially done too in [@Memoirs Proposition 4.10]. The only computation required is the torsion of the solid torus added by Dehn filling, or its core geodesic, which is (by Example [\[ex:circle\]](#ex:circle){reference-type="ref" reference="ex:circle"}): $$\frac{1}{
\det \left( \begin{pmatrix}
            1 & 0 \\
            0 & 1
           \end{pmatrix}
           -
           \begin{pmatrix}
            e^{\lambda_{p/q}/2} & 0 \\
            0 & e^{-\lambda_{p/q}/2}
           \end{pmatrix}
      \right) }= \frac1{2 (1-\cosh(\lambda_{p/q}/2 ))}.$$

::: remark
[]{#rem:2pi label="rem:2pi"} The complex length $\lambda_{p/q}$ is defined up to addition of a term in $2\pi i \mathbb{Z}$. The spin structure (or equivalently a choice of lift of the holonomy) determines $\lambda_{p/q}$ up to $4\pi i\mathbb{Z}$, as the holonomy of this curve is conjugate to $$\begin{pmatrix}
 e^{\lambda_{p/q}/2} & 0 \\ 0 & e^{-\lambda_{p/q}/2}
\end{pmatrix}.$$
:::

::: cor
[]{#cor:differentspin label="cor:differentspin"} There exist closed hyperbolic manifolds $N^3$ with two spin structures $\sigma$ and $\sigma'$ so that $\tau(N^3,\sigma)\neq \tau(N^3,\sigma')$.
:::

::: proof
*Proof.* The manifolds are obtained by Dehn filling on the figure eight knot. Consider the sequence $p_n/ q_n= 2 n$ so that both spin structures on the figure eight knot exterior $M^3$ extend to $M^3_{p_n/q_n}$, i.e. $H_1(M^3_{2 n} ; \mathbb{Z}/2\mathbb{Z})\cong \mathbb{Z}/2\mathbb{Z}$. The corresponding lifts differ on the sign of the trace of the meridian. As the core of the solid torus is homologous to the meridian, the sign of the traces of these cores differ. Hence for one of the lifts the complex length (modulo $4\pi i\mathbb{Z}$) is $\lambda_{2n}$, for the other one it is $\lambda_{2n}+ 2\pi i$ by Remark [\[rem:2pi\]](#rem:2pi){reference-type="ref" reference="rem:2pi"}. By Remark [\[rem:length\]](#rem:length){reference-type="ref" reference="rem:length"}, one may approximate $$\label{eqn:approx}
 \lambda_{2n}=\frac{2\pi i}{2n}+ O\left(\frac{1}{n^2}\right).$$ The goal is to show that the limit $$\label{eqn:limit}
 \lim_{n\to+\infty} \frac{\vert \tau(M_{2 n},\sigma )\vert }{ \vert \tau(M_{2 n},\sigma' )\vert}$$ is not $1$. By Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"} it is the product of the limits: $$\label{eqn:limitlambdas}
 \lim_{n\to\infty}\frac{1-\cosh( \lambda_{2n}/2 ) }{ 1-\cosh( (\lambda_{2n} + 2\pi i)/2) }
=\lim_{n\to\infty}\frac{1-\cos\frac{\pi} {2n}}{1+\cos\frac{\pi} {2n}} = 0$$ (using the approximation [\[eqn:approx\]](#eqn:approx){reference-type="eqref" reference="eqn:approx"}) and $$\label{eqn:limitfunctions}
 \lim_{n\to\infty}  
 \frac{\mathbb{T}_M(\chi_{2n,\sigma} 
)}{\mathbb{T}_M(\chi_{2n,\sigma'} )}
=
\frac{\tau(M^3,\sigma)}{\tau(M^3,\sigma')}.$$ As for one of the spin structures the trace of the meridian is $2$ and for the other $-2$, by Example [\[ex:fig8sl2\]](#ex:fig8sl2){reference-type="ref" reference="ex:fig8sl2"}, the limit in [\[eqn:limitfunctions\]](#eqn:limitfunctions){reference-type="eqref" reference="eqn:limitfunctions"} is $(2-2\cdot(-2))/(2-2\cdot2)=-3$. Thus the limit [\[eqn:limit\]](#eqn:limit){reference-type="eqref" reference="eqn:limit"} vanishes, hence it is not $1$. ◻
:::

The previous argument applies to any knot exterior, the precise value of the torsion is not needed. Corollary [\[cor:differentspin\]](#cor:differentspin){reference-type="ref" reference="cor:differentspin"} holds true also for cusped manifolds, by applying an analogous formula for partial surgery.

::: cor
[]{#cor:dense label="cor:dense"} The set of modules of the torsions $\left\vert \tau(M^3_{p/q},\sigma)\right\vert$ obtained by Dehn filling on $M^3$, so that the spin structure $\sigma$ on $M^3$ extends to $M^3_{p/q}$, is dense in $$\left[\frac14{\vert \tau(M^3,\sigma)\vert},+\infty\right).$$
:::

::: proof
*Proof.* By the surgery formula, Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}, it suffices to show that $$\left\vert 1- \cosh( 
  {\lambda_{p/q}}/2)\right\vert$$ is dense in the interval $[0,2]$. Let $r, s\in\mathbb{Z}$ be such that $p s-q r = 1$, by Remark [\[rem:length\]](#rem:length){reference-type="ref" reference="rem:length"}, $\lambda_{p/q}= 2\pi i \frac{r}p+\frac up$ and $u\to 0$. Then the result follows from the density of $\cos(\pi \frac{r}{p})$ in $[-1,1]$. Notice that extendibility of $\sigma$ is just determined by a condition $a\, p + b\, q\equiv 0 \mod 2$, for $a, b\in \mathbb{Z}/2\mathbb{Z}$ depending on $\sigma$. ◻
:::

As the surgery formula shows, this density is a consequence of the contribution of the core geodesics. Notice that in Theorem [\[thm:BV\]](#thm:BV){reference-type="ref" reference="thm:BV"} the hypothesis require the length of geodesics to be bounded below away from zero.

### Branched coverings on the figure eight {#sssection:branched}

We next consider another family of examples. We consider it only for the figure eight knot, but it generalizes to other manifolds.

Consider $M_ n^3$ the n-th cyclic branched covering of $S^3$, branched along the figure eight knot. It is hyperbolic for $n\geq 4$. Its torsion may be computed by means of the twisted Alexander polynomial, by using the formula à la Fox, Proposition [\[prop:Fox\]](#prop:Fox){reference-type="ref" reference="prop:Fox"}, due to Turaev [@Turaev86], see also [@DY12; @Porti04; @SW02; @Raimbault12; @Yamaguchi12]. More precisely, this polynomial is $$p_{\chi}( t )=t^2-2\chi(m) t + 1,$$ by [\[eqn:tor82t\]](#eqn:tor82t){reference-type="eqref" reference="eqn:tor82t"}, cf. [@Kitano-Morifuji2012]. Notice that its value at $1$ agrees with Example [\[ex:fig8sl2\]](#ex:fig8sl2){reference-type="ref" reference="ex:fig8sl2"}. The holonomy of $M_ n^3$ extends to a holonomy of the quotient orbifold $M_ 
n^3/ 
(\mathbb{Z}/n\mathbb{Z})$ in $\mathrm{PSL}_2(\mathbb{C})$. It induces a representation of the exterior of the not $S^3-\mathcal K$ that lifts to $\mathrm{SL}_2(\mathbb{C})$, that we denote by $\rho_n$. Since a rotation of angle $2\pi /n$ has trace $\pm 2\cos ( \pi/n)$, we have $$\chi_{\rho_n}(m)= \operatorname{tr}(\rho_n(m))= \pm 2 \cos ( \pi/n).$$ Using Proposition [\[prop:Fox\]](#prop:Fox){reference-type="ref" reference="prop:Fox"}, if $\Sigma_n\subset M_n$ is the lift of the branching locus, then $$\operatorname{tor}(M_n^3-\Sigma_n,\sigma)=\prod_{k=0}^{n-1} p_{\chi_n}( e^{2\pi i\frac{k}{n}})  =
 \prod_{k=0}^{n-1} \left( e^{4\pi i\frac{k}{n}}\mp 4\cos({\pi}/{n} ) 
e^{2\pi i\frac{k}{n}}+1\right).$$ By the surgery formula (Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}) and knowing that the complex length of the core geodesic is $\approx  \frac{\sqrt{3}\,\pi}n + O\left(\frac{1}{n^3}\right)$ (Remark [\[rem:length\]](#rem:length){reference-type="ref" reference="rem:length"}), $$\label{eq:foxsurgery}
 \operatorname{tor}(M_n^3,\sigma)= \frac{1/2}{1-\cosh \left( \frac{\sqrt{3}\,\pi}n  + 
O\left(\frac{1}{n^3}\right) \right)} 
  \prod_{k=0}^{n-1} \left( e^{4\pi i\frac{k}{n}}\mp 4\cos( {\pi}/{n} ) 
e^{2\pi i\frac{k}{n}}+1\right).$$ In particular, $$\label{eqn:limlog/n}
\lim_{n\to\infty} \frac{\log\vert \operatorname{tor}(M_n^3,\sigma)\vert}{n}= 
 \lim_{n\to\infty} \frac{1}{n} \sum_{k=0}^{n-1} \log \left\vert  e^{4\pi 
i\frac{k}{n}}\pm 4\cos( {\pi}/{n} ) e^{2\pi i\frac{k}{n}}+1 \right\vert.$$ Here we used that $\lim_{x\to 0^+}  x\log x =0$ to get rid of the first term, outside the product, in [\[eq:foxsurgery\]](#eq:foxsurgery){reference-type="eqref" reference="eq:foxsurgery"}. As $t^2 \mp 4 t + 1$ has no roots in the unit circle, the limit [\[eqn:limlog/n\]](#eqn:limlog/n){reference-type="eqref" reference="eqn:limlog/n"} converges to $$\frac{1}{2\pi}\int_{\vert z\vert =1} \log\vert z^2\pm  4 z +1 \vert .$$ Thus by Jensen's formula $$\lim_{n\to\infty} \frac{\log\vert \operatorname{tor}(M_n^3,\sigma)\vert}{n}
 = \log\vert 2+\sqrt{3}\vert .$$

This approach uses the ideas on Mahler measure of [@SW02]. It applies to a hyperbolic knot provided that the torsion polynomial has no roots in the unit circle. It is easy to prove that the roots of the polynomial are not roots of the unity, but this does not discard roots in the unit circle. For the adjoint representation, the nonexistence of roots in the unit circle has been proved by Kapovich [@Kapovich98].

# Torsions for higher dimensional representations of hyperbolic three-manifolds {#sec:repsandtors}

This section is devoted to further Reidemeister torsions naturally associated to hyperbolic three-manifolds, those obtained by using the (finite dimensional and linear) representations of $\mathrm{SL}_2(\mathbb{C})$.
