---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-064-213-explicit-computation
section_title: "Explicit computation"
section_number: 21.3
pages: 112-114
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.993
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:explicitcomputation label="subsection:explicitcomputation"}

We want to make more explicit theorem [\[theo:devissageH1\]](#theo:devissageH1){reference-type="ref" reference="theo:devissageH1"}.\
So we assume that $A,A'$ represent two classes in $H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta+1})$ having the same image in $H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta})$. Up to an analytic gauge transform, the situation just described can be made explicit as follows. Assume that $A,A'$ have graded part $A_{0}$ and are in Birkhoff-Guenther normal form. Assume moreover that they coincide up to level $\delta - 1$. Then the same is true for $\hat{F}_{A}$ and $\hat{F}_{A'}$; therefore, it is also true for $\hat{F}_{A,A'}$ and $I_{n}$, that is, $\hat{F}_{A,A'} \in {\mathfrak{G}}^{\geq \delta}({{\mathbf C}((z))})$. The first non-trivial upper diagonal of $\hat{F}_{A,A'}$ is at level $\delta$ and, as a divergent series, generically it actually has $q$-Gevrey level $\delta$; if it has level $< \delta$, then it is convergent. The classes of $A,A'$ in ${\mathcal{F}}_{\leq \delta}(M_{0}) = H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta+1})$ have the same image in ${\mathcal{F}}_{\leq \delta-1}(M_{0}) = H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta})$. After theorem [\[theo:devissageH1\]](#theo:devissageH1){reference-type="ref" reference="theo:devissageH1"}, there exists a unique element of $V^{(\delta)}$ which carries the class of $A$ to the class of $A'$. The Stokes matrices $S_{c,d} \hat{F}_{A} := \left(S_{c,d} \hat{F}_{A}\right)^{-1} S_{d} \hat{F}_{A}$ []{#not94 label="not94"} and $S_{c,d} \hat{F}_{A'} := \left(S_{c,d} \hat{F}_{A'}\right)^{-1} S_{d} \hat{F}_{A'}$ are congruent modulo $\Lambda^{\geq \delta}$, so that their quotient $S_{c,d} \hat{F}_{A,A'}$ is in $\Lambda^{\geq \delta}$. Its first non trivial upper diagonal is at level $\delta$; call it $f_{c,d}$ and consider it as an element of $\lambda^{(\delta)}$. This defines a cocycle, hence a class in $H^{1}({\mathbf{E}_{q}},\lambda^{(\delta)})$. This class is the element of $V^{(\delta)}$ we look for.

::: exem
[]{#exem:geometrythreeslopes label="exem:geometrythreeslopes"} Take $A_{0} := \begin{pmatrix} a & 0 & 0 \\ 
0 & b z & 0 \\ 0 & 0 & c z^{2} \end{pmatrix}$ and $A := \begin{pmatrix} a & u & v_{0} + v_{1} z \\ 
0 & b z & w z \\ 0 & 0 & c z^{2} \end{pmatrix}$ in Birkhoff-Guenther normal form, so that $u,v_{0},v_{1},w \in {\mathbf C}$. Here, the total space of classes $H^{1}({\mathbf{E}_{q}},\Lambda_I(M_0))$ has dimension $4$, while each of the components $H^{1}({\mathbf{E}_{q}},\lambda^{(1)})$ and $H^{1}({\mathbf{E}_{q}},\lambda^{(2)})$ has dimension $2$.\
To compute the class of $A$ in $H^{1}({\mathbf{E}_{q}},\Lambda_I(M_0))$ identified with $H^{1}({\mathbf{E}_{q}},\lambda^{(1)}) \oplus H^{1}({\mathbf{E}_{q}},\lambda^{(2)})$, we introduce the intermediate point $A' := \begin{pmatrix} a & u & 0 \\ 
0 & b z & w z \\ 0 & 0 & c z^{2} \end{pmatrix}$ and the intermediate gauge transforms $G := \begin{pmatrix} 1 & f & x \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix}$ such that $G[A_{0}] = A'$ and $H := \begin{pmatrix} 1 & 0 & g \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ such that $H[A'] = A$, so that $F := H G =
\begin{pmatrix} 1 & f & g + x \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix}$ is such that $F[A_{0}] = A$.\
The component in $H^{1}({\mathbf{E}_{q}},\lambda^{(1)})$ is computed by considering $G$ alone. Its coefficients satisfy the equations: $$b z \sigma_qf - a f = u \text{~and~} c z \sigma_qh - b h = w.$$ (The coefficient $x$ is irrelevant here.) We shall see in section [\[section:qEuler\]](#section:qEuler){reference-type="ref" reference="section:qEuler"} how to compute the corresponding cocycles $(f_{c,d})$ and $(h_{c,d})$, but what is clear here is that they are respectively linear functions of $u$ and of $w$. So in the end, the component of the class of $A$ in $H^{1}({\mathbf{E}_{q}},\lambda^{(1)})$ is $u L_{1}(a,b) + w L_{1}(b,c)$ for some explicit basic classes $L_{1}(a,b)$, $L_{1}(b,c)$ (the index $1$ is for the level).\
Similarly, the component in $H^{1}({\mathbf{E}_{q}},\lambda^{(2)})$ is computed by considering $H$ alone. Its coefficient satisfies the equation: $$c z^{2} \sigma_qg - a g = v_{0} + v_{1} z.$$ It is therefore clear that the component we look for is $v_{0} L_{2,0}(a,c) + v_{1} L_{2,1}(a,c)$ for some explicit base of classes $L_{2,0}(a,c),L_{2,1}(a,c)$.\
This example will be pursued in section [\[section:qEulersquare\]](#section:qEulersquare){reference-type="ref" reference="section:qEulersquare"}.
:::

## Various geometries on ${\mathcal{F}}(P_{1},\ldots,P_{k})$ {#subsection:variousgeometries}

In subsection [\[subsection:BGNF\]](#subsection:BGNF){reference-type="ref" reference="subsection:BGNF"}, we drawed from the Birkhoff-Guenther normal form an affine structure on ${\mathcal{F}}(M_{0})$. This structure is made explicit by the coordinates provided by proposition [\[prop:kintegralslopesspace\]](#prop:kintegralslopesspace){reference-type="ref" reference="prop:kintegralslopesspace"}. The dévissage above implies that it is the same as the affine structure on $H^{1}({\mathbf{E}_{q}},\Lambda_I(M_0))$ inherited from the vector space structures on the $H^{1}({\mathbf{E}_{q}},\lambda^{(\delta)})$ through corollary [\[coro:devissageH1\]](#coro:devissageH1){reference-type="ref" reference="coro:devissageH1"}. More precisely:

::: theo
The mapping from $\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ to $\bigoplus\limits_{\delta \geq 1} H^{1}({\mathbf{E}_{q}},\lambda^{(\delta)})$ coming from proposition [\[prop:kintegralslopesspace\]](#prop:kintegralslopesspace){reference-type="ref" reference="prop:kintegralslopesspace"}, corollary [\[coro:devissageH1\]](#coro:devissageH1){reference-type="ref" reference="coro:devissageH1"} and theorems [\[theo:secondqMalgrangeSibuya\]](#theo:secondqMalgrangeSibuya){reference-type="ref" reference="theo:secondqMalgrangeSibuya"} and [\[section:analyticclassificationCZ\]](#section:analyticclassificationCZ){reference-type="ref" reference="section:analyticclassificationCZ"} is linear.
:::

::: proof
*Proof.* The computations are in essence the same as in the example. Details will be written in [@JSmoduli]. ◻
:::

There is a third source for the geometry on ${\mathcal{F}}(M_{0})$, namely the identification with the space $\bigoplus E_{i,j,c,d}$ of all privileged cocycles (where $c,d$ are fixed arbitrary) found in subsection [\[subsection:privilegedcocycles\]](#subsection:privilegedcocycles){reference-type="ref" reference="subsection:privilegedcocycles"}. The corresponding geometry is the same, see *loc. cit.*.
