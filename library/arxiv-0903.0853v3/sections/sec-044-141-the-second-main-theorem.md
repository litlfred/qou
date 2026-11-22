---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-044-141-the-second-main-theorem
section_title: "The second main theorem"
section_number: 14.1
pages: 70-73
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.853
latex_coverage_ratio: 0.963
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:thesecondmaintheorem label="subsection:thesecondmaintheorem"}

Before going on, let us make some preliminary remarks. Let $M_{0} := P_{1} \oplus \cdots \oplus P_{k}$ be a pure module. Represent it by a matrix $A_0$ with the same form as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"}. Assume moreover that $A_{0}$ is in Birkhoff-Guenther normal form as found in [\[subsection:BGNF\]](#subsection:BGNF){reference-type="ref" reference="subsection:BGNF"}.\
We saw in proposition [\[prop:groupeformelsuranalytique\]](#prop:groupeformelsuranalytique){reference-type="ref" reference="prop:groupeformelsuranalytique"} that there is a natural bijective mapping between ${\mathcal{F}}(M_0) = {\mathcal{F}}(P_{1},\ldots,P_{k})$ and the quotient ${\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})/{\mathfrak{G}}({{\mathbf C}(\{z\})})$. It also follows from the first part of [\[subsection:computnormalform\]](#subsection:computnormalform){reference-type="ref" reference="subsection:computnormalform"} that this, in turn, is equal to ${\mathfrak{G}}^{A_{0}}({{\mathbf C}[[z]]})/{\mathfrak{G}}({{\mathbf C}\{z\}})$. Last, the inclusion ${\mathfrak{G}}\subset {\text{GL}}_n$ induces a bijection from ${\mathfrak{G}}^{A_{0}}({{\mathbf C}[[z]]})/{\mathfrak{G}}({{\mathbf C}\{z\}})$ to the quotient ${\text{GL}}^{M_0}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$, where we take []{#not56 label="not56"} ${\text{GL}}^{M_0}_n\bigl({{\mathbf C}[[z]]}\bigr)$ to denote the set of those formal gauge transformation matrices that send $A_{0}$ into ${\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$.

::: theo
[]{#theo:secondqMalgrangeSibuya label="theo:secondqMalgrangeSibuya"} Let $M_0$ be a pure module represented by a matrix $A_{0}$ in Birkhoff-Guenther normal form. There is a natural bijective mapping: $${\text{GL}}^{M_0}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
\rightarrow H^1\bigl({\mathbf{E}_{q}};\Lambda_I(M_0)\bigr),$$ whence a natural bijective mapping: $${\mathcal{F}}(M_0) \rightarrow H^1\bigl({\mathbf{E}_{q}};\Lambda_I(M_0)\bigr).$$
:::

::: proof
*Proof.* [*The map $\lambda$*]{.underline}

Let ${\mathfrak{U}}:=(U_i)_{i\in I}$ be a good open covering of ${\mathbf{E}_{q}}$.

Let $\hat F \in {\text{GL}}^{M_0}_n \subset {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$; by definition there exists an unique $A \in {\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$ such that $\hat F[A_0] = A$.

For all $i\in I$, there exists $g_i \in {\text{GL}}_n\bigl({\mathcal
A}(U_i)\bigr)$ asymptotic to $\hat F$ on $U_i$ (*cf.* theorem [\[theo:TFESA\]](#theo:TFESA){reference-type="ref" reference="theo:TFESA"}). The coboundary $(g_{ij})$ of the cochain $(g_i)$ belongs to $Z^1({\mathfrak{U}},\Lambda_I(M_0))$ (the reason for that is lemma [\[lemm:cocyclasympt\]](#lemm:cocyclasympt){reference-type="ref" reference="lemm:cocyclasympt"} which can be applied because the condition of good covering implies that the open sets are adequate); it does not change if we multiply $\hat F$ on the right by an element of ${\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$. If we change the representatives $g_i$, we get another cochain in $Z^1({\mathfrak{U}},\Lambda_I(M_0))$ inducing the same element of $H^1({\mathfrak{U}},\Lambda_I(M_0))$. We thus get a natural map: $$\lambda:{\text{GL}}^{M_0}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
\rightarrow H^1\bigl({\mathbf{E}_{q}};\Lambda_I(M_0)\bigr).$$ This map is injective.

[*Surjectivity of $\lambda$*]{.underline} Let ${\mathfrak{U}}:=(U_i)_{i\in I}$ be a good open covering of ${\mathbf{E}_{q}}$; assume moreover that the compact covering $(\overline U_i)_{i\in I}$ is good and that the $U_i$ are small parallelograms.

Let $\gamma \in H^1({\mathbf{E}_{q}};\Lambda_I(M_0))$; we can represent it by an element $g \in Z^1({\mathfrak{U}};\Lambda_I(M_0)$, ${\mathfrak{U}}=(U_i)_{i\in I}$ being a good open covering of ${\mathbf{E}_{q}}$. Moreover we can choose ${\mathfrak{U}}$ such that the compact covering $(\overline U_i)_{i\in I}$ is good and such that the $U_i$ are small parallelograms.

As in section [\[subsection:glue\]](#subsection:glue){reference-type="ref" reference="subsection:glue"}, using $g$, we can build a germ of analytic manifold ${\mathbf M}_g$ and a holomorphic fibration $\pi:{\mathbf M}_g\rightarrow ({\mathbf C},0)$. But now there is a new ingredient: we have a holomorphic automorphism $\Theta_0:({\mathbf C},0)\times{\mathbf C}^n\rightarrow ({\mathbf C},0)\times{\mathbf C}^n$ of the trivial bundle $\bigl(({\mathbf C},0)\times{\mathbf C}^n,\pi_0,({\mathbf C},0)\bigr)$ defined by: $$(z,X)\mapsto (qz,A_0 X).$$ It induces, for all $i\in I$ a holomorphic automorphism of fibre bundles $\Theta_{0,i}: U_i\times{\mathbf C}^n\rightarrow U_i$.

By definition the $g_{ij}\in \Lambda_I(M_0)(U_{ij})$ commute with $\Theta_0$, therefore the automorphisms $\Theta_{0,i}$ glue together into a holomorphic automorphism $\Psi$ of the germ of fibered manifold $\bigl({\mathbf M}_g,\pi, ({\mathbf C},\{ 0\})\bigr)$. The map $\Psi$ is linear on the fibers and the map on the basis is the germ of $z\mapsto qz$.

We choose a holomorphic trivialisation $H$ of the germ of fiber bundle $\bigl({\mathbf M}_g,\pi,({\mathbf C},0)\bigr)$: $\pi_0\circ H = \pi$. The map $\Phi :=H\circ\Psi\circ H^{-1}$ is a holomorphic automorphism of the germ of trivial bundle $\bigl(({\mathbf C},0)\times{\mathbf C}^n,\pi_0,({\mathbf C},0)\bigr)$, it corresponds to an element $A\in {\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$. Using the results and notations of section [\[subsection:glue\]](#subsection:glue){reference-type="ref" reference="subsection:glue"}, we see that there exists an element $\hat{\varphi} \in {\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)$ such that $g \mapsto \hat{\varphi}^{-1}$ induces the inverse of the natural map ${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/ {\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)\rightarrow
H^1\bigl({\mathbf{E}_{q}};\Lambda_I\bigr)$. If we set $\hat F := \hat\varphi^{-1}$, it is easy to check that $\hat F[A_0]=A$. We have $\hat F \in {\text{GL}}^{M_0}_n$ and $\lambda(\hat F)=g$, therefore $\lambda$ is surjective. ◻
:::

# Summation and asymptotic theory {#chapter:asymptotictheory}

To find analytic solutions having a given formal solution as asymptotic expansion is a rather old subject in the theory of $q$-difference equations: see for instance the paper [@Tr] by Trjitzinsky in 1933. The first author had already suggested in [@RamisPanorama] the use of the gaussian function to formulate a $q$-analogue for Laplace transform; this allowed to find in [@zh1] the $Gq$-summation, a $q$-analog of the exponential summation method of Borel-Laplace. In [@MarotteZhang], the $Gq$-summation was extended to the case of multiple levels, and it was shown that any formal power series solution of a linear equation with analytic coefficients is $Gq$-multisummable, and thus can be seen as the asymptotic expansion of an analytical solution in a sector with infinite opening in the Riemann surface of the logarithm. The work in [@rz] [@RSZ2], [@zh2], [@zh3] was undertaken with the goal of obtaining a summation over the elliptic curve, or a finite covering of it[^1].

[^1]: To be more precise: note [@RSZ2] can be seen as an abridged version of the present chapter. It summarizes and completes [@rz], the departure point, which announces the first part of [@zh3]. These first works dealt with divisors supported at a single point, and [@zh2] started the extension to more general divisors (and more slopes).
