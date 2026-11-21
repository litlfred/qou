---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-014-43-some-knot-complements
section_title: "Some knot complements"
section_number: 4.3
pages: 28-31
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.674
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:knots label="sec:knots"}

A well-studied class of 3-manifolds are the complements of knots in the 3-sphere. One forms a knot complement $M_K$ by slightly thickening a knot $K\in S^3$ into a solid torus $N_K$, and then cutting it out,

$$M_K = S^3\backslash N_K\,.$$

With the single exception of the unknot complement, all knot complements seem to admit

[^1]

ideal triangulations that can be used to define the index $\mathcal{I}_{M_K}$, a topological invariant of $M_K$.

::: wrapfigure
r3in ![image](LM){width="2.8in"}
:::

The boundary of a knot complement is a torus $T^2$, and its phase space $\mathcal{P}_{T^2}$ has a canonical polarization $\Pi$. To define it, one first identifies the so-called meridian and longitude cycles on the boundary: the meridian $\mu$ is a small loop linking the knot $K$, which would be contractible in the thickened knot neighborhood $N_K$; and the longitude $\lambda$ is a loop running parallel to $K$ that has zero linking number with $K$ and is null-homologous in $M_K$ (Figure [\[fig:lm\]](#fig:lm){reference-type="ref" reference="fig:lm"}). The orientation of $M_K$ induces a relative orientation on these cycles. The eigenvalues of the $SL(2,{\mathbb C})$ holonomies along $\lambda$ and $\mu$, typically denoted $\ell$ and $m$, then provide ${\mathbb C}^*$ coordinates for the boundary phase space (see *e.g.* [@gukov-2003]):

$$\mathcal{P}_{\partial M} \;=\; \big({\mathbb C}^*\times {\mathbb C}^*\big)\big/\raisebox{-.1cm}{${\mathbb Z}_2$} \;=\; \{(\ell,m)\}\big/\raisebox{-.1cm}{$(\ell,m)\sim(\ell^{-1},m^{-1})$}\;\;. \label{PT2}$$

Finally, we take the canonical position coordinate

[^2]

to be $U\equiv 2\log(m)$ and its conjugate momentum to be $v\equiv \log(-\ell)$. These logarithmic coordinates are periodic, and have an identification $(U,v)\sim (-U,-v)$.

The coordinates $U$ and $v$ are easily expressed as sums and differences of edge parameters of tetrahedra in a triangulation of $M_K$ [@Thurston-1980; @NZ], and thus fit nicely into the general combinatorial framework of Section [\[sec:rules\]](#sec:rules){reference-type="ref" reference="sec:rules"} for constructing theories $T_{M_K}$ and indices $\mathcal{I}_{M_K}$. In particular, any knot complement theory $T_{M_K}$ has a single $U(1)$ flavor symmetry, with twisted mass parameter $U$. Therefore, the index $\mathcal{I}_{M_K}(m,e)$ depends on a single electric charge $e$ and magnetic flux $m$. We expect that the manifest $U(1)$ symmetry is actually enhanced to $SU(2)$, allowing knot complement theories to couple to the 4d theory $T[\partial M_K]=T[T^2]$, which is $\mathcal{N}=4$ $SU(2)$ super-Yang-Mills. A classical indication of this enhancement appears in the ${\mathbb Z}_2$ Weyl symmetry of the phase space [\[PT2\]](#PT2){reference-type="eqref" reference="PT2"}. The enhancement would also imply that the index satisfies

$$\mathcal{I}_{M_K}(m,e;q) = \mathcal{I}_{M_K}(-m,-e;q)\,, \label{indZ2}$$

which can be considered a quantum version of symmetry in the phase space.

We now give a few examples.

### Figure-eight from two tetrahedra

![The standard triangulation of the figure-eight knot complement](fig8cusp){#fig:fig8cusp width="6in"}

The standard triangulation of the figure-eight ($\mathbf{4_1}$) knot complement has two ideal tetrahedra, say $\Delta_Z$ and $\Delta_W$. All tetrahedron faces are glued together pairwise, and the $T^2$ boundary is made up from small, truncated ideal vertices of the tetrahedra (Figure [1](#fig:fig8cusp){reference-type="ref" reference="fig:fig8cusp"}). We find a meridian $U = Z-W''$ and a longitude $v= Z''-Z$. There are two internal edge coordinates, but only one of them is independent, and we can take it to be $C = 2Z''+Z'+2W''+W'$. Finally, the conjugate momentum to $C$ can be defined as (say) $\Gamma = -W''$. The change of polarization from $\Pi_Z\times \Pi_W$ to $\widetilde\Pi$ then becomes

$$\begin{pmatrix} U\\ C\\v\\\Gamma \end{pmatrix}
 = \begin{pmatrix} Z-W'' \\ 2Z''+Z'+2W''+W' \\ Z''-Z\\ -W'' \end{pmatrix}
 = \begin{pmatrix} 1&0&0&-1 \\ -1&-1&1&1  \\ -1&0&1&0 \\ 0&0&0&-1 \end{pmatrix}\begin{pmatrix} Z \\ W \\ Z'' \\ W''\end{pmatrix} + \begin{pmatrix} 0 \\ 2\pi i+\hbar \\ 0 \\ 0 \end{pmatrix}\,.$$

Correspondingly, the product index $\mathcal{I}_{\Delta_Z}(m_1,e_1)\mathcal{I}_{\Delta_W}(m_2,e_2)$ gets transformed by the affine $Sp(4,{\mathbb Z})$ action above to

$$\mathcal{I}_{\{\Delta_i\},\tilde\Pi}(m_1,m_2,e_1,e_2) = \big(-q^{\frac12}\big)^{-2e_2}\mathcal{I}_\Delta(m_1-e_2,m_1+e_1-e_2)\,\mathcal{I}_\Delta(-m_2+e_1-e_2,-e_2)\,,$$

and then after breaking the $U(1)$ symmetry associated to the internal edge $C$ we obtain

$$\begin{aligned}
 \mathcal{I}_{\mathbf{4_1}}(m,e) &= \sum_{e_2\in {\mathbb Z}}\mathcal{I}_\Delta(m-e_2,m+e-e_2)\,\mathcal{I}_\Delta(e-e_2,-e_2)\,. \label{ind41}
\end{aligned}$$

It can be checked for any charges $(m,e)$ and to any order in $q$ that

$$\mathcal{I}_{\mathbf{4_1}}(m,e) = \mathcal{I}_{\mathbf{4_1}}(-m,e) = \mathcal{I}_{\mathbf{4_1}}(m,-e) = \mathcal{I}_{\mathbf{4_1}}(-m,-e)\,.$$

For example,

$$\mathcal{I}_{\mathbf{4_1}}(1,1)=\mathcal{I}_{\mathbf{4_1}}(1,-1)= -q-q^2+2q^3+7q^4+11q^5+11q^6+3q^7+\dots\,,$$

*etc.* Thus, in addition to the Weyl symmetry [\[indZ2\]](#indZ2){reference-type="eqref" reference="indZ2"}, there is a parity-like symmetry that inverts the sign of a single charge. Geometrically, this is a result of the fact that the figure-eight knot complement is amphicheiral (*i.e.* is equivalent to its mirror image).

[^1]: All ideal triangulations of the unknot have a univalent ("peripherally homotopic") edge. Otherwise, it has been proven that all hyperbolic knot complements have non-univalent triangulations [@Tillmann-def], and the same seems to hold even for non-hyperbolic knots [@Segerman-def].

[^2]: The factor of $2$ in the definition of $U$ ensures that $U$ and $v$ are canonically conjugate. The minus sign in $v=\log(-\ell)$ is merely convenient when dealing with combinatorics of triangulations, to avoid unwanted factors of $i\pi$. Geometrically, this sign is correlated with the lift from $PSL(2)$ to $SL(2)$ holonomy on a knot complement.
