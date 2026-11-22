---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-069-91-spectral-sequence-for-gln-homology
section_title: "Spectral sequence for glN homology"
section_number: 9.1
pages: 67-68
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.928
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:spectral diff label="sub:spectral diff"}

By [@RasDiff], for each $N$ there exists a spectral sequence starting at the HOMFLY-PT homology and converging to $\mathfrak{sl}_N$ homology of a given knot. More precisely, for a given braid $\sigma$ one can construct a complex of Soergel bimodules as described in Subsection [\[sub:khr\]](#sub:khr){reference-type="ref" reference="sub:khr"}. The Hochschild homology of this complex coincides with the HOMFLY-PT homology of the closure of $\sigma$. Given a polynomial $p \in \mathbb{C}[x]$, we can construct an additional differential $d_-$ which acts on Soergel bimodules, as we now describe.

Recall that the simple Soergel bimodule can be written as $B_i=R \otimes_{R^{i,i+1}} R$. Denote $u_j=x_j\otimes 1, v_j=1\otimes x_j$ for all $j$, and $$U_{i,i+1}:=\frac{\mathbb{C}[u_1,\ldots,u_n,v_1,\ldots,v_n]}{(u_i+u_{i+1}-v_i-v_{i+1},u_j-v_j,j\notin \{i,i+1\})},$$ then $$B_i\cong \left[U_{i,i+1}\xrightarrow{(v_i-u_i)(v_i-u_{i+1})}U_{i,i+1}\right].$$ Given a polynomial $p\in \mathbb{C}[x]$, consider the difference $$W_{i,i+1}:=p(u_i)+p(u_{i+1})-p(v_i)-p(v_{i+1})=p(u_i)+p(u_{i+1})-p(v_i)-p(u_i+u_{i+1}-v_i)\in U_{i,i+1}.$$ Remark that $W_{i,i+1}$ is divisible by $(v_i-u_i)(v_i-u_{i+1})$: indeed, $W_{i,i+1}$ vanishes if $v_i=u_i$ or $v_i=u_{i+1}$. Let $p_{i,i+1}=W_{i,i+1}/(v_i-u_i)(v_i-u_{i+1})$. We use $p_{i,i+1}$ to define an additional differential (denoted by $d_{-}$ in [@RasDiff]) which acts *backwards*: $$\label{bs with potential}
B_i^{(p)}:=\left[U_{i,i+1}\xtofrom[d_{-}:=p_{i,i+1}]{(v_i-u_i)(v_i-u_{i+1})}U_{i,i+1}\right].$$ Note that the total complex $(B_i^{(p)},d_++d_-)$ is not a chain complex but a matrix factorization with potential $W_{i,i+1}$.

It is proved in [@RasDiff] that this additional differential $d_{-}$ can be naturally extended to Bott-Samuelson bimodules (tensor products of $B_i$), and to Rouquier complexes. One can also prove [@Becker] that $d_{-}$ can be correctly defined on general Soergel bimodules as well. For $p'(x)=x^N$, this differential is usually denoted by $d_N$, and the homology of the total differential is isomorphic to $\mathfrak{gl}_N$ Khovanov-Rozansky homology [@KhR1]. The desired spectral sequence is then induced by $d_N$ on $\mathop{\mathrm{HHH}}(\sigma)$.

In the present section, we wish to present a more geometric viewpoint of this construction. Given $N$, we define the so-called $\mathfrak{sl}_N$ dg category $(\mathrm{SBim}_n,d_N)$, where the objects are Soergel bimodules equipped with the "internal differential" $d_N$. This is a subcategory of the category of matrix factorizations with potential $x^N$. There is a monoidal functor: $$K^b(\mathrm{SBim}_n) \to \left( K^b(\mathrm{SBim}_n), d_N \right)$$ which is given by endowing complexes of Soergel bimodules with the differential $d_N$.
