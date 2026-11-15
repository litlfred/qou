---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-003-4-what-is-known
section_title: "What is known?"
section_number: 4
pages: 9-15
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.975
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
Having defined our basic object of study, we explain some important structural results.

## Non-abelian Hodge correspondence

The non-abelian Hodge correspondence, pioneered by Hitchin [@hitchin1987self] and developed by Simpson [@simpson1990harmonic; @simpson1991nonabelian; @simpson1992higgs], is a construction of a remarkable bijection between local systems and stable Higgs bundles, which induces a diffeomorphism between the character variety and the moduli space that parametrizes stable Higgs bundles.

To define Higgs bundles, we need to view the Riemann surface with punctures as a compact algebraic curve $C$ over $\mathbb C$ with marked points. Then a *Higgs bundle* is a pair $(\mathcal{E}, \theta)$, where $\mathcal{E}$ is an algebraic vector bundle on $C$ and $\theta$ a *Higgs field*, which is a twisted matrix-valued function on $C$ of a certain kind. More precisely, $\theta:\mathcal{E}\to\mathcal{E}\otimes\omega_C(D)$, where $D=\sum_{i=1}^k [t_i]$ is the divisor on $C$ corresponding to the marked points. Explicitly, this means that on an open subset of $C$ with a trivialization of $\mathcal{E}$ is trivial, $\theta$ is a matrix whose entries are algebraic differential forms on $C$ with simple residues at the marked points.

Furthermore, these Higgs bundles are required to be endowed with *parabolic structures* at the marked points. This is simply a choice of a partial flag at the fiber of $\mathcal{E}$ at each marked point, preserved by the residue $\mathop{\mathrm{res}}_{t_i} \theta$, which acts on that fiber by a linear transformation. The steps of the partial flag precisely match the dimensions of the generalized eigenspaces of the Jordan forms $J_i$. The data of a Higgs bundle with a parabolic structure has to satisfy a *stability condition*. The data of the eigenvalues and the Jordan blocks of $J_i$ translate into *parabolic weights* defining the stability condition, and into the Jordan form of $\mathop{\mathrm{res}}_{t_i} \theta$ acting on the subquotients of the flag. Details are given in [@simpson1990harmonic]. We summarize the features appearing on both sides of this correspondence in the table on Figure [1](#fig:nonabelian hodge){reference-type="ref" reference="fig:nonabelian hodge"}.

<figure id="fig:nonabelian hodge">
<table>
<thead>
<tr class="header">
<th style="text-align: center;">Local systems</th>
<th style="text-align: center;">Higgs bundles</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><em>π</em><sub>1</sub>(<em>C</em>) → GL<sub><em>n</em></sub>(ℂ)</span></td>
<td style="text-align: center;"><span class="math inline">(ℰ,<em>θ</em>)</span>: <span class="math inline">ℰ</span> algebraic vector bundle on <span class="math inline"><em>C</em></span>,</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math inline"><em>θ</em> : ℰ → ℰ ⊗ <em>ω</em><sub><em>C</em></sub></span> Higgs field</td>
</tr>
<tr class="odd">
<td style="text-align: center;">punctures, <span class="math inline"><em>J</em><sub><em>i</em></sub></span></td>
<td style="text-align: center;">parabolic structure, stability</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><em>X</em><sub><em>B</em></sub></span> “Betti” moduli space</td>
<td style="text-align: center;"><span class="math inline"> ≅ <em>X</em><sub><em>D</em></sub></span> “Dolbeault” moduli space</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;"><img src="hitchin.png" style="width:4.5cm" alt="image" /></td>
</tr>
<tr class="even">
<td style="text-align: center;">affine algebraic variety</td>
<td style="text-align: center;">Hitchin system <span class="math inline"><em>X</em><sub><em>D</em></sub> → ℂ<sup>dimension/2</sup></span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Cohomology ring <span class="math inline"><em>H</em><sup>*</sup>(<em>X</em><sub><em>B</em></sub>,ℂ)</span></td>
<td style="text-align: center;">the same ring</td>
</tr>
<tr class="even">
<td style="text-align: center;">Weight “W” filtration <span class="math inline"><em>W</em><sub>*</sub><em>H</em><sup>*</sup></span></td>
<td style="text-align: center;">perverse “P” filtration</td>
</tr>
</tbody>
</table>
<figcaption><span id="fig:nonabelian hodge" label="fig:nonabelian hodge"></span>Non-abelian Hodge correspondence</figcaption>
</figure>

## Generators of $H^*(X)$

Generators of the cohomology ring are known. There is a general argument in [@markman2002generators] concerning moduli spaces of sheaves on surfaces. With a little modification it can be applied to the situation of parabolic Higgs bundles. Basically speaking, certain Chern class of the complex of vector bundles on $X_D\times X_D$ computing the derived $\mathop{\mathrm{Hom}}$ between Higgs bundles is a multiple of the diagonal class. Moreover, there exists a compactification $\overline{X_D}\supset X_D$ such that the complex extends to $X_D\times \overline{X_D}$ and the Chern class remains a multiple of the diagonal class. Thus the identity map $H^*(X_D)\to H^*(X_D)$ can be written in terms of the tautological classes.

Consider the tautological bundle[^1] $\mathcal{E}\to X_D\times C$. For each $i\in\{0,1,2\}$, $\xi\in H^i(C)$ and $m\in\mathbb Z_{\geq 0}$ define $$\label{eq:definition e}
        e_m(\xi):=(\pi_X)_*( c_m(\mathcal{E}) \cup \xi)\in H^{2m+i-2}(X_D).$$ Here $c_m(\mathcal{E})\in H^{2m}(X_D\times C)$ is the Chern class and $\pi_{X}$ is the projection $X_D\times C\to X_D$. If we have a marked point $t_j$, then each point of $X_D$ gives a flag $0=F_{j0}\subset F_{j1} \subset\cdots\subset F_{j r_j} = \mathcal E(t_j)$. Each subquotient of the flag produces a vector bundle on $X_D$ and we take its Chern classes $c_{m,j,\ell} := c_m(F_{j \ell} / F_{j \ell-1})$.

::: theorem
The cohomology ring $H^*(X_D)$ is generated by the classes $e_m(\xi)$ and $c_{m,j,\ell}$.
:::

The cohomology ring of the Riemann surface $C$ has a basis $1\in H^0(C)$, $\mathrm{pt}\in H^2(C)$ and $\sigma_1,\ldots,\sigma_{2g}\in H^1(C)$ with the product structure given by $\sigma_i \sigma_{i+g} = -\sigma_{i+g}\sigma_i=\mathrm{pt}$, all other $\sigma_i \sigma_j$ being zero.

## Explicit relations of $H^*(X)$

are known for $n=2$, $k=1$, $J_1=-I$, arbitrary $g$ ([@hausel2003relations]). The cohomology is generated by certain elements $\varepsilon_1,\ldots,\varepsilon_{2g}\in H^1(X_D)$, $\alpha\in H^2(X_D)$, $\psi_1,\ldots,\psi_{2g}\in H^2(X_D)$ and $\beta\in H^4(X_D)$. These are certain multiples of $e_1(\sigma_i)$, $e_2(1)$, $e_2(\sigma_i)$ and $e_2(\mathrm{pt})$. The elements $\varepsilon_i$ generate a copy of the cohomology ring of the Jacobian of $C$ and we have $$H^*(X_D) = H^*(\mathop{\mathrm{Jac}}(C)) \otimes \bigoplus_{i=0}^g \wedge_0^i(\psi) \otimes \mathbb C[\alpha,\beta,\gamma] / J_{i}^{g-i},$$ where $J_{i}^{g-i}\subset \mathbb C[\alpha,\beta,\gamma]$ is the ideal generated by an explicit list of polynomials in $\alpha, \beta, \gamma$. Here $\gamma=-2 \sum_{i=1}^g \psi_i \psi_{i+g}$ and $\wedge_0^i(\psi)$ denotes the primitive part in the space of $i$-fold products of $\psi_j$-classes.

## Weight filtration

The weight filtration is very easily described in terms of the tautological generators. The following was shown in [@shende2016weights] in the case without parabolic points and in [@mellit2019cell] in a more general case:

::: theorem
Define the weight of the tautological generators $e_{m}(\xi)$ and $c_{m,j,\ell}$ to be $2 m$. Then $W_m H^*(X_B)$ is spanned by products of tautological generators of total weight $\leq m$.
:::

## The pure part

The *pure part* $H^*_{\mathrm{pure}}(X_B)=\bigoplus_i W_i H^i(X_B)$ is naturally a subring of $H^*(X_B)$. In [@hausel2011arithmetic] it was conjectured that the Poincaré polynomial of $H^*_{\mathrm{pure}}(X_B)$ matches that of the quiver variety associated to the corresponding comet-shaped quiver, see Figure [2](#fig:comet){reference-type="ref" reference="fig:comet"}.

![[]{#fig:comet label="fig:comet"} Comet-shaped quiver with $k$ legs and $g$ loops.](gloops-klegs.png){#fig:comet width=".5\\linewidth"}

## $\boldsymbol{P}=\boldsymbol{W}$

Computing the characteristic polynomial of $\theta:\mathcal E\to \mathcal E\otimes \omega_C(D)$ at all points of $C$ produces a well-defined polynomial map $X_D\to \mathbb C^{\dim_\mathbb CX/2}$ called the *Hitchin map*, which is known to be proper. This induces a filtration $P_* H^*(X_D)$ on $H^*(X_D)$ called the *perverse Leray filtration* ([@cataldo2009decomposition]). According to the recently proved $P=W$ conjecture ([@cataldo2012topology]), we have

::: theorem
$$P_i=W_{2i}.$$
:::

## $\boldsymbol{q}-\boldsymbol{t}$ symmetry

Recall the Mixed Hodge polynomial $q+t+4$ from Section [\[ssec:mixed hodge polynomial\]](#ssec:mixed hodge polynomial){reference-type="ref" reference="ssec:mixed hodge polynomial"}. Its symmetry in the variables $q$ and $t$ was called the *curious hard Lefschetz* property in [@hausel2011arithmetic], and it was expected to hold in general. Having $P=W$, it follows from the *relative hard Lefschetz theorem* on the $X_D$-side. We have

::: theorem
$H^*(X_B)$ satisfies curious hard Lefschetz: $$\omega^i: \mathrm{Gr}^W_{\dim_\mathbb CX-2i} H^j(X_B) \to \mathrm{Gr}^W_{\dim_\mathbb CX+2i} H^{j+2 i}(X_B)$$ is an isomorphism.
:::

In fact, the proof of $P=W$ from [@maulik2024pw] relies on this result. On the other hand, the proof of $P=W$ in [@hausel2022p] is independent of it, and therefore provides another proof of the curious hard Lefschetz.

Similar curious hard Lefschetz property holds for a certain version of the Khovanov homology of knots (conjectured in [@dunfield2006superpolynomial], proved in [@gorsky2024tautological]).

## Partition function

Perhaps the biggest problem in the field that still remains open is the conjectural formula for the generating function of the mixed Hodge polynomials of all character varieties given in [@hausel2011arithmetic] in terms of a partition function. Here $k$ (the number of marked points) and $g$ are fixed. For each $i=1,\ldots,k$ let $\mathbf{x}_i:=(x_{i1},x_{i2},\ldots)$ be an infinite sequence of variables. Suppose we have a sequence $\boldsymbol\mu_i:=(\mu_{i1},\mu_{i2},\ldots)$ of non-negative integers with $\sum_{j}\mu_{ij}=n$. To this we associate a conjugacy class $J_{\mu_i}$ of the diagonal matrix with eigenvalues having multiplicities $\mu_{i1},\mu_{i2},\ldots$. For a tuple of such sequences $\boldsymbol{\mu}=(\mu_1,\ldots,\mu_k)$ we choose the eigenvalues arbitrarily so that the conjugacy classes satisfy the genericity condition (Definition [\[def:generic\]](#def:generic){reference-type="ref" reference="def:generic"}) and consider the corresponding character variety $X_{g;J_{\mu_1},\cdots,J_{\mu_{k}}}$. We take its mixed Hodge polynomial (Section [\[ssec:mixed hodge polynomial\]](#ssec:mixed hodge polynomial){reference-type="ref" reference="ssec:mixed hodge polynomial"}) with weight $$\mathbf{x}^{\boldsymbol\mu}:=\prod_{i=1}^k \prod_j x_{ij}^{\mu_{ij}}.$$ The result is a symmetric function in each sequence of variables $\mathbf{x}_i$ whose coefficients are polynomials in $q$ and $t$: $$\mathrm{MH}_{g,k}(\mathbf{x}_1,\ldots,\mathbf{x}_k; q,t) :=
    \sum_{n=1}^\infty \sum_{ \mu_1, \dots, \mu_{k} \vdash n} \mathrm{MH}(X_{g;J_{\mu_1},\cdots,J_{\mu_{k}}};q,t) \; \mathbf{x}^{\boldsymbol\mu}.$$ On the other hand, we define the *partition function* $$\label{eq:partition function}
        \Omega_{g,k}(\mathbf{x}_1,\ldots,\mathbf{x}_{k}; q,t) 
        :=\sum_{n=0}^\infty \sum_{\lambda\vdash n} \tilde H_\lambda(\mathbf{x}_1;q,t) \cdots \tilde H_\lambda(\mathbf{x}_k;q,t)
        \prod_{\square\in\lambda}\frac{\left(q^{a(\square)+1/2} - t^{\ell(\square)+1/2}\right)^{2g}}{(q^{a(\square)} - t^{\ell(\square)+1})(q^{a(\square)+1} - t^{\ell(\square)})},$$ where $\lambda$ goes over all partitions (Young diagrams), $\tilde H_\lambda(\mathbf{x}_k;q,t)$ denotes the *modified Macdonald polynomial*, the product goes over the cells of the Young diagram, and $a,\ell$ denote the usual arms and legs statistics (see [@garsia1996remarkable]).

::: conjecture
[]{#conj:partition function conjecture label="conj:partition function conjecture"} $$\label{eq:partition function conjecture}
            \Omega_{g,k} = \mathop{\mathrm{Exp}}\;\left(-\frac{\mathrm{MH_{g,k}}}{(q-1)(t-1)}\right).$$
:::

Here $\mathop{\mathrm{Exp}}$ denotes the *plethystic exponential*. It can be defined for any expression involving some variables $a,b,c,\ldots$ as follows: $$\mathop{\mathrm{Exp}}(f(a,b,c,\ldots)) := \exp\left(\sum_{n=1}^\infty \frac{f(a^n,b^n,c^n,\ldots)}{n}\right).$$ If $a,b,c,\ldots$ are monomials in some variables, then we have $$\mathop{\mathrm{Exp}}(a+b+c+\cdots) = \frac{1}{1-a} \; \frac{1}{1-b} \; \frac{1}{1-c} \; \cdots,$$ so plethystic exponential can be thought of as the conversion between infinite sums and infinite products. There is an inverse operation $\mathop{\mathrm{Log}}$ called the *plethystic logarithm*. So if we focus on computing the mixed Hodge polynomials from [\[eq:partition function conjecture\]](#eq:partition function conjecture){reference-type="eqref" reference="eq:partition function conjecture"}, we can write $$\label{eq:partition function logarithm}
        \mathrm{MH_{g,k}} = -(1-q)(1-t) \mathop{\mathrm{Log}}\Omega_{g,k}.$$

## What is known?

Conjecture [\[conj:partition function conjecture\]](#conj:partition function conjecture){reference-type="eqref" reference="conj:partition function conjecture"} was motivated by a computation performed in [@hausel2011arithmetic]. It was shown that its implication for the number of $\mathbb{F}_q$ points is correct (see [\[eq:Fq points and mixed Hodge\]](#eq:Fq points and mixed Hodge){reference-type="eqref" reference="eq:Fq points and mixed Hodge"}), by counting representations $\pi_1(C)\to \mathrm{GL_n}(\mathbb{F}_q)$ using the character theory of the finite group $\mathrm{GL_n}(\mathbb{F}_q)$.

::: theorem
The number of points over $\mathbb{F}_q$ ($t=q^{-1}$) deduced from [\[eq:partition function conjecture\]](#eq:partition function conjecture){reference-type="eqref" reference="eq:partition function conjecture"} is correct.
:::

Initially, in the identity [\[eq:partition function logarithm\]](#eq:partition function logarithm){reference-type="eqref" reference="eq:partition function logarithm"} it was not at all clear that the right hand side has coefficients which are polynomials in $q$, $t$, which they should be because the mixed Hodge polynomials on the left hand side are polynomials by definition. Using a new identity in Macdonald polynomials combinatorics established in [@garsia2019five], the author first proved

::: theorem
The coefficients of $(q-1)(t-1)\; \mathrm{Log}\;\Omega$ are polynomials in $q$ and $t$.
:::

Then, together with an approach to count Higgs bundles over $\mathbb{F}_q$ by Schiffmann ([@schiffmann2016indecomposable], [@mozgovoy2020counting]) and a new relationship between the Macdonald polynomials and the affine Springer fibers, the author proved

::: theorem
[]{#thm:poincare label="thm:poincare"} The Poincaré polynomials ($t=1$) deduced from [\[eq:partition function conjecture\]](#eq:partition function conjecture){reference-type="eqref" reference="eq:partition function conjecture"} are correct.
:::

With the help of this theorem, there is a following line of attack on Conjecture [\[conj:partition function conjecture\]](#conj:partition function conjecture){reference-type="eqref" reference="conj:partition function conjecture"}. Suppose we managed to construct a "candidate model" $M$ for the cohomology ring of the character variety so that it comes with a surjective map $M\to H^*(X)$. Showing surjectivity of the map is plausible because the generators of $H^*(X)$ are known. If we furthermore manage to show that the dimension of $M$ is exactly as predicted by Conjecture [\[conj:partition function conjecture\]](#conj:partition function conjecture){reference-type="eqref" reference="conj:partition function conjecture"}, then by Theorem [\[thm:poincare\]](#thm:poincare){reference-type="ref" reference="thm:poincare"} the map $M\to H^*(X)$ will have to be an isomorphism. Partial progress in this direction is discussed in the next sections.

[^1]: In fact the tautological bundle often is not well-defined as a vector bundle. It is well-defined as a projective bundle, and the "determinant" $\det \mathcal E$ is also well-defined, but the determinant might have no $n$-th root and correspondingly $c_1(\det \mathcal E)\in H^2(X_D,\mathbb Z)$ may not be divisible by $n$. Since we are dealing with the cohomology with complex coefficients, this does not create a problem and all the Chern classes are still well-defined.
