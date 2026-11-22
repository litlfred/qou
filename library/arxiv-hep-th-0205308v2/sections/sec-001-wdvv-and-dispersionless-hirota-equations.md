---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-001-wdvv-and-dispersionless-hirota-equations
section_title: "WDVV and dispersionless Hirota equations"
section_number: null
pages: 3-5
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.943
doc_brief: "WDVV Equations as Functional Relations — 6 sections: Front matter; Introduction; WDVV and dispersionless Hirota equ"
---
The WDVV equations usually follow from the crossing relations $$\label{crossing}
\sum_k C^k_{\ ij}C^n_{\ kl} = \sum_k C^k_{\ il}C^n_{\ kj}$$ for the structure constants of some algebra $$\label{alg}
\phi_i\circ\phi_j =\sum_k  C^k_{\ ij}\phi_k.$$ It is useful also to write ([\[crossing\]](#crossing){reference-type="ref" reference="crossing"}) in the matrix form $$\label{crossmatr}
{\sf C}_i\cdot {\sf C}_j = {\sf C}_j\cdot {\sf C}_i,\qquad \forall i,j
\qquad  ({\sf C}_i)\sp{l}_{\ m} = C_{\ im}\sp{l}.$$ Equations ([\[crossing\]](#crossing){reference-type="ref" reference="crossing"}) are algebraic relations and they turn into the WDVV system of nonlinear differential equations after expressing the structure constants in terms of the third derivatives of some function ${\cal F}(a\sp1,\dots,a\sp{N})$ $$\label{cf}
C_{\ ij}^k = \eta^{kl}{\cal F}_{ijl}.$$ Generically the matrix $\eta$ can be an arbitrary linear combination with time dependent coefficients $\eta = \sum_j \alpha\sp{j}({\bf a}){\sf F}_j$, but for simplicity we will mostly consider $\eta={\sf F}_1$. Then $\eta_{rs}=\iota_\alpha dT_{rs}$.

Various rewritings of the WDVV equations are possible. In the Frobenius manifold setting there is a pencil of flat connections, while the general equations ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) are equivalent [@mor] to the commuting of matrix-valued vector fields: $$[\partial_i -({\sf F}_j)\sp{-1}{\sf F}_i\, \partial_j,
   \partial_k -({\sf F}_j)\sp{-1}{\sf F}_k\, \partial_j]=0$$ (with fixed $j$). For our purposes one may also rewrite ([\[crossing\]](#crossing){reference-type="ref" reference="crossing"}) as $$\label{crossF}
\sum_k C^k_{\ ij}{\cal F}_{kln} = \sum_k C^k_{\ il}{\cal F}_{kjn}.$$ With one form $C=\eta\sp{-1}dT$ ( i.e. $C_{\ ij}^k da\sp{i}= \eta^{kl}\partial_i T_{jl}da\sp{i}=
\eta^{kl}{\cal F}_{ijl}da\sp{i}$) we have $$\label{bilinear}
[{\sf C}_i, {\sf C}_j ]=0\Longleftrightarrow C\wedge C=0
\Longleftrightarrow dT\wedge \eta\sp{-1}dT=0.$$ Unfortunately the connection $C$ is unrelated to the various connections arising in the special Kähler geometry because of the (arbitrary) appearance of $\eta$ which is unrelated to the special Kähler metric. In general the curvature of $C$ is nonvanishing. (The curvature will, for example, vanish as a consequence of the WDVV equations if there is a symmetry ${\cal L}_\alpha dT=\mu dT$, for some matrix $\mu$.) The final form of ([\[bilinear\]](#bilinear){reference-type="ref" reference="bilinear"}) is reminiscent of the Hirota bilinear equations which may be interpreted in terms of Plücker formulae, but again the appearance of $\eta$ means the bilinear form in such formulae is not constant. Whatever, the final form shows that the WDVV equations impose relations on the period matrices $T$, and consequently restrict the associated Seiberg-Witten curves that can yield solutions of ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}).

An important observation was made recently in [@BMRWZ] where it was shown that in the case of dispersionless integrable hierarchies the WDVV equations maybe derived directly by differentiating corresponding Hirota algebraic relations. In particular, the solutions associated with the Landau-Ginzburg topological models can be constructed in this way. Below, we will reverse the arrow of this implication and demonstrate that the WDVV equations, if rewritten in terms of second derivatives, can be simply viewed as certain Hirota-like functional relations.

The dispersionless Hirota relations (see [@BMRWZ] and references therein about the details and their explicit form) for the second derivatives, which can be written as $$\label{hir}
{\cal F}_{ij} = T_{ij}({\mbox{\boldmath $\varphi$}})$$ where $T_{ij}$ are some *known* functions and $\{\varphi_i\}$ denote some restricted set (of cardinality $N$, the size of the matrices under consideration in the finite-dimensional situation) second derivatives, for example $$\label{vf}
\varphi_i = {\cal F}_{1i}({\bf a})$$ Without specifying form of the functions $T_{ij}$ in ([\[hir\]](#hir){reference-type="ref" reference="hir"}) this is just a *dimensional* statement that the *matrix* of second derivatives of any function can be expressed in terms of only a *vector* of variables.

Consider the "period" matrix ([\[pematr\]](#pematr){reference-type="ref" reference="pematr"}) which for any integrable system is a function of only $N$ variables. This means that in the "Siegel upper half-space" $\{ T_{ij}\}$ of dimension $\dfrac{N(N+1)}{2}$ we have a "submanifold" of dimension $N$ $$\label{hs1}
T_{ij} = T_{ij}(a\sp1,\dots,a\sp{N})$$ or codimension $\dfrac{N(N-1)}{2}$ given by defining equations $$\label{hs2}
f_A(T_{ij})=0
\quad
A=1,\dots,{N(N-1)\over 2}$$ Of course, on this submanifold (under a generic assumption of nonsingularity) one may choose new variables, say $$\label{defphi}
\varphi_i = T_{1i}({\bf a})$$ Consequently there exist functional relations $$T_{ij} = T_{ij}(\varphi_1,\dots,\varphi_N) = T_{ij}({\bf a}
(\varphi_1,\dots,\varphi_N))$$ between the matrix elements of the whole period matrix, exactly as one has in dispersionless Hirota's relations. In the case of ([\[defphi\]](#defphi){reference-type="ref" reference="defphi"}) all of the matrix elements of the period matrix would be expressed in terms of a single row or column. (We give an example of this in section [\[ss:eg\]](#ss:eg){reference-type="ref" reference="ss:eg"}.)

More generally, let us assume we can find coordinates $\varphi_k$ so that $$\label{defc}
dT_{ij}=C^k_{\ ij}\,d\varphi_k.$$ Using the definition ([\[cf\]](#cf){reference-type="ref" reference="cf"}) this means $$\label{defp}
d\varphi_k=\eta_{kl}d a\sp{l}.$$ Both ([\[defc\]](#defc){reference-type="ref" reference="defc"}) and ([\[defp\]](#defp){reference-type="ref" reference="defp"}) have the common integrability condition $$\label{integ}
d\eta_{kl}\wedge d a\sp{l}=0\Longleftrightarrow M\sp{i}_s {\cal F}_{irk}=
M\sp{i}_r {\cal F}_{isk} ,\qquad M\sp{i}_r=\dfrac{\partial\alpha\sp{i}}{\partial a\sp{r}},$$ where the $\alpha\sp{i}$'s were the coefficients defining $\eta$ above. These are certainly satisfied for constant $\alpha\sp{i}$. Thus the choice ([\[defphi\]](#defphi){reference-type="ref" reference="defphi"}) would correspond to $\eta={\sf F}_1$. Supposing the integrability condition ([\[integ\]](#integ){reference-type="ref" reference="integ"}) holds, our assumption ([\[defc\]](#defc){reference-type="ref" reference="defc"}) means that the structure constants can be *integrated*, i.e. defined as derivatives of the functions ([\[hir\]](#hir){reference-type="ref" reference="hir"}) $$\label{c}
C_{\ ij}^k = {\partial T_{ij}\over\partial\varphi_k}$$ and that $$\label{inthir}
T_{ij}({\mbox{\boldmath $\varphi$}}) = \int \sum_k C_{ij}^k d\varphi_k,$$ i.e. the structure constants determine the form of the Hirota-like relations ([\[hir\]](#hir){reference-type="ref" reference="hir"}).
