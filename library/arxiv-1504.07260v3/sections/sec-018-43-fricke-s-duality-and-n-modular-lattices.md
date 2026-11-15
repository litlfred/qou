---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-018-43-fricke-s-duality-and-n-modular-lattices
section_title: "Fricke S-duality and N-modular lattices"
section_number: 4.3
pages: 29-30
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.985
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
[]{#s:Nmodular label="s:Nmodular"}

In the previous section, we derived the lattice $\Lambda_{em}$ of electric-magnetic charges of a CHL model, in the case $\lambda=1$. Suppose that the CHL model is in case 1 of section [\[s:Sdual\]](#s:Sdual){reference-type="ref" reference="s:Sdual"}, i.e. the symmetry $g$ has balanced cycle shape. In this case, the Fricke S-duality connects two different points in the moduli space of the same CHL model. In particular, the moduli $S_{\text{het}},T_{\text{het}},U_{\text{het}}$ of the dual theories are related as in [\[hetmodSdual\]](#hetmodSdual){reference-type="eqref" reference="hetmodSdual"} and the electric and magnetic charges as in [\[emcharges\]](#emcharges){reference-type="eqref" reference="emcharges"}. This implies that the lattice of magnetic charges $\Lambda_m$ of a $\mathbb{Z}_N$ self-dual CHL model is an integral $N$-modular lattice $$\Lambda_m^*(N)\cong \Lambda_m\ .$$ This prediction can be verified in detail. By [\[electLattsimpl\]](#electLattsimpl){reference-type="eqref" reference="electLattsimpl"}, we have $$\Lambda_m^*(N)=(\Gamma_{K3}^g)^*(N)\oplus \langle \frac{u}{\sqrt{N}}, \sqrt{N}u^*\rangle \oplus \Gamma_{\tilde S^1}(N)\ .$$The summands $\langle \frac{u}{\sqrt{N}}, \sqrt{N}u^*\rangle$ and $\Gamma_{\tilde S^1}(N)$ are $\mathbb{Z}^2$ lattices with quadratic forms, respectively $$\begin{pmatrix}
0 & 1 \\ 
1 & 0 \end{pmatrix}\qquad \qquad \begin{pmatrix}
 0 & N\\
 N & 0
\end{pmatrix}\ .$$On the other hand, the summands $\langle N u^*, u\rangle$, $\Gamma_{\tilde S^1}\subset \Lambda_m$ are $\mathbb{Z}^2$ lattices with quadratic forms, respectively $$\begin{pmatrix}
0 & N \\ 
N & 0 \end{pmatrix}\qquad \qquad \begin{pmatrix}
 0 & 1\\
 1 & 0
\end{pmatrix}\ .$$ Therefore, the lattices $\langle \frac{u}{\sqrt{N}}, \sqrt{N}u^*\rangle\oplus \Gamma_{\tilde S^1}(N)$ and $\langle N u^*, u\rangle$, $\Gamma_{\tilde S^1}\subset \Lambda_m$ are isomorphic, as expected, but the isomorphism requires the exchange of the winding-momentum charges related to the circle $S^1$ with the ones related to $\tilde S^1$. This is compatible with the non-trivial action of the S-duality transformation [\[hetmodSdual\]](#hetmodSdual){reference-type="eqref" reference="hetmodSdual"} on the complex structure modulus $U_{\text{het}}$.

$N$-modularity of the summands $\langle N u^*, u\rangle$, $\Gamma_{\tilde S^1}$ actually holds for every CHL model (with $\lambda=1$), independently of the model being self-dual or not. What is peculiar to self-dual CHL models is the $N$-modularity property of the orthogonal complements $$(\Gamma_{K3}^g)^*(N)\cong \Gamma_{K3}^g\ .$$We have verified this property directly by deriving the quadratic forms of the lattices $\Gamma_{K3}^g$ for all possible Frame shapes of $g$ (see tables [\[t:case1\]](#t:case1){reference-type="ref" reference="t:case1"},[\[t:case2\]](#t:case2){reference-type="ref" reference="t:case2"},[\[t:case3\]](#t:case3){reference-type="ref" reference="t:case3"} in appendix [\[s:lattices\]](#s:lattices){reference-type="ref" reference="s:lattices"}). It turns out that the lattice $\Gamma_{K3}^g$ is $N$-modular if and only if the Frame shape of $g$ is balanced (table [\[t:case1\]](#t:case1){reference-type="ref" reference="t:case1"}). This conclusion extends to the cases $\lambda>1$, as described in section [\[s:genlatticeem\]](#s:genlatticeem){reference-type="ref" reference="s:genlatticeem"}. A highly non-trivial example is provided by the Frame shape $1^82^8$, which corresponds on the type IIA side to a symplectic automorphism of order $2$ of the K3 manifold (Nikulin involution), and on the $E_8\times E_8$ heterotic side to the involution exchanging the two $E_8$ factors. In this case, one obtains $$\Gamma_{K3}^g= \Gamma^{4,4}\oplus E_8(-2)\ ,$$and $$(\Gamma_{K3}^g)^*= \Gamma^{4,4}\oplus E_8(-1/2)\ .$$S-duality, in this case, predicts the existence of an isomorphism $$\Gamma^{4,4}(2)\oplus E_8(-1)\cong \Gamma^{4,4}\oplus E_8(-2)\ .$$This isomorphism can be verified by first checking that the lattices on both sides are in the same genus, and then noting that the genus has only one isomorphism class (as follows from theorem 1.14.2 of [@Nikulin]).

In case 2, S-duality relates pairs of distinct CHL models, related to symmetries $g, g'\in O(\Gamma_{K3})$ of the same order but different Frame shape, and we have (table [\[t:case3\]](#t:case3){reference-type="ref" reference="t:case3"}) $$(\Gamma_{K3}^g)^*(N)\cong \Gamma_{K3}^{g'}\ .$$

Finally, for case 3, i.e. when the orbifold of the type IIA K3 model by $g$ is a sigma model on $T^4$, one has $$(\Gamma_{K3}^g)^*(N)\cong (\Gamma^{4,4})^{g'}\ ,$$where $\Gamma^{4,4}$ is the lattice of even D-brane charges on a non-linear sigma model on $T^4$ and $g'\in O(\Gamma^{4,4})$ is a symmetry of this model preserving the (small) $\mathcal{N}=(4,4)$ superconformal algebra [@Volpato:2014zla] (see table [\[t:case2\]](#t:case2){reference-type="ref" reference="t:case2"} in appendix [\[s:lattices\]](#s:lattices){reference-type="ref" reference="s:lattices"}).
