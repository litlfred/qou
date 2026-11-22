---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-012-223-measure
section_title: "Measure"
section_number: 2.2.3
pages: 28-30
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.983
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
The described theory possesses the following "topological" gauge symmetry: $$\delta  z(x)=\theta(x), \qquad
    \delta\bar{z} (x)=\bar{\theta}(x),
    \label{top.sym.}$$ where $\theta (x)$ and $\bar{\theta}(x)$ are arbitrary except at the boundary $\partial S$ where they vanish. The origin of the symmetry [\[top.sym.\]](#top.sym.){reference-type="ref" reference="top.sym."} will become clear when we convert the action [\[top.act.\]](#top.act.){reference-type="ref" reference="top.act."} into a line integral. Integrating by parts in Eq.[\[top.act.\]](#top.act.){reference-type="ref" reference="top.act."} and using the Abelian Stokes theorem we obtain $$S_{\rm{cl}}=i\oint_{\partial S}
\bar{z}D_iz\,dx^i,$$ or in a parametrized form $$S_{\rm{cl}}=i\oint_{\partial S} \bar{z}
D_t z\,dt  .$$ To covariantly quantize the theory we shall introduce the BRS operator $s$. According to the form of the topological gauge symmetry [\[top.sym.\]](#top.sym.){reference-type="ref" reference="top.sym."}, the operator $s$ is easily defined by $$s\,z =\phi,\qquad s\,\bar{ z}=\bar{\chi}, \qquad
s\phi =0, \qquad s\bar{\chi}=0,$$ $$s\bar{\phi}=\bar{\beta}, \qquad s\chi =\beta , \qquad
s\bar{\beta}=0,\qquad s\beta =0,$$ where $\phi$ and $\bar{\chi}$ are ghost fields in the representation $R$, associated to $\theta$ and $\bar{\theta
}$, respectively, $\bar{\phi}$ and $\chi$ are the corresponding antighosts, and $\bar{\beta}$, $\beta$ are Lagrange multipliers. All the fields possess a suitable Grassmann parity correlated with the parity of $\bar{z}$ and $z$. Obviously $s^2=0$, and we can gauge fix the action in Eq.[\[top.act.\]](#top.act.){reference-type="ref" reference="top.act."} in a BRS-invariant manner by simply adding the following $s$-exact term: $$\begin{aligned}
    S'&=& s\left( \int_{\cal S} \left( \bar{\phi}\triangle  z
    \pm \bar{ z}\triangle \chi\right) d^2 \sigma \right)
    \nonumber\\ 
    &=&
    \int_S \left( \bar{\beta} \triangle z
    \pm \bar{\phi}\triangle \phi \pm \bar{\chi}\triangle\chi
    +\bar{z} \triangle \beta \right) d^2 \sigma.
    \nonumber 
\end{aligned}$$ The upper (lower) sign stands for the fields $\bar{z}$, $z$ of bosonic (fermionic) statistics. Integration after the ghost fields yields some numerical factor and the quantum action $$S=S_{\rm{cl}}+\int_S \left(\bar{\beta}
    \triangle z +\bar{z}\triangle\beta\right)
    d^2\sigma.
    \label{Sq}$$ If necessary, one can insert $\sqrt{g}$ into the second term, which is equivalent to change of variables. Thus the partition function is given by $$Z=\int e^{iS}\,D\bar{z}\,Dz\,D\bar{\beta}\,D\beta ,$$ with the boundary conditions: $\bar{\beta}|_{\partial S}=
\beta |_{\partial S}=0$.

One can observe that the job the fields $\bar{\beta}$ and $\beta$ are supposed to do consists in eliminating a redundant integration inside $S$. The gauge-fixing condition following from Eq.[\[Sq\]](#Sq){reference-type="ref" reference="Sq"} imposes the following constraints $$\triangle  z =0, \qquad \triangle \bar{ z}=0.$$ Since values of the fields $z$ and $\bar{z}$ are fixed on the boundary $\partial S=C$, we deal with the two well-defined $2$-dimensional Dirichlet problems. The solutions of the Dirichlet problems fix values of $z$ and $\bar z$ inside $S$. Another, more singular gauge-fixing, is proposed in \[Bro92\].

The issue of the measure has been also discussed in \[HU00\].
