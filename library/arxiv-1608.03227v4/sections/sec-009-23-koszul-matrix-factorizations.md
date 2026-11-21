---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-009-23-koszul-matrix-factorizations
section_title: "Koszul matrix factorizations"
section_number: 2.3
pages: 11-12
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.981
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: str eq Kosz label="ssec: str eq Kosz"} In this subsection we set notations for a particular type of matrix factorization that is ubiquitous in our work and in the previous work that relates matrix factorizations to knot invariants [@KR]. We need slightly more general setting than the one from [@KR] because we work with equivariant matrix factorizations. We state some simple properties of these factorizations that are used later in the paper.

Suppose $\calZ$ is a variety with the action of a group $G$ and $F$ is a $G$-invariant potential.

An object of the category $\MFs_{B^2}^{str}(\calZ,F)$ is a free $B^2$-equivariant $\Zt$-graded $\CC[\calZ]$-module $\xxM$ with the odd $G$-invariant differential $\xD$ such that $\xD^2 = F\xIdv{M}$. In particular, a free $G$-equivariant $\CC[\calZ]$-module $\xxV$ with two elements $\xdl\in\xxV$, $\xdr\in\xxV^*$ such that $(d_l,d_r)=F$, determines a Koszul matrix factorization $\SymbolPrint{\Kszvvv{\xxV}{\xdl}{\xdr}} = \bigwedge^{\bullet}\xxV$ with the differential $Dv = \xdl\wedge v + \xdr\cdot v$ for $v\in \bigwedge^{\bullet}\xxV$. We use a more detailed notation by choosing a basis $\ktht_1,\ldots,\ktht_n\in \xxV$ and presenting $\xdl$ and $\xdr$ in terms of components: $\xdl=a_1\ktht_1 +\cdots a_n\ktht_n$, $\xdr=b_1\ktht^*_1+\cdots + b_n\ktht^*_n$: $$\label{eq:kszm}
\Kszvvv{\xxV}{\xdl}{\xdr} = \kmtr{a_1 & b_1 &\ktht_1\\ \vdots & \vdots & \vdots \\
a_n & b_n & \ktht_n}$$ The structure of $G$-module is described by specifying the action of $G$ on the basis $\ktht_1,\ldots,\ktht_n$. In some cases when $G$-equivariant structure of the module $\xxM$ is clear from the context we omit the last columns from the notations. We call a matrix presenting Koszul matrix factorization Koszul matrix. For example,

if we change the basis $\theta_1,\dots, \theta_n$ to the basis $\theta_1,\dots,\theta_i+c\theta_j,\dots, \theta_j,\dots,\theta_n$ the $i$-th and $j$-th rows of the Koszul matrix will change: $$\begin{bmatrix}
a_i& b_i&\theta_i\\
a_j& b_j&\theta_j
\end{bmatrix}
\mapsto
\begin{bmatrix}
a_i+ca_j& b_i&\theta_i+c\theta_j\\
a_j& b_j-cb_i&\theta_j
\end{bmatrix}$$

Suppose $a_1,\dots,a_n\in \CC[\calZ]$ is a regular sequence and $F\in (a_1,\dots,a_n)$. We can choose $b_i$ such that $F=\sum_i a_i b_i$ and $\xdl$ and $\xdr$ are as above: $\xdl=a_1\ktht_1 +\cdots a_n\ktht_n$, $\xdr=b_1\ktht^*_1+\cdots + b_n\ktht^*_n$. In general, there is no unique choice for $b_i$ but all choices lead to homotopy equivalent Koszul matrix factorizations (in the non-equivariant case they would be simply isomorphic).

In other words, if $b'_i$ is a another collection of elements such that $F=\sum a_i b'_i$ and $\xdr'=b'_1\ktht^*_1+\cdots + b'_n\ktht^*_n$ then Lemma [\[lem: ext uniq\]](#lem: ext uniq){reference-type="ref" reference="lem: ext uniq"} implies that the complexes $\Kszvvv{\xxV}{\xdl}{\xdr}$ and $\Kszvvv{\xxV}{\xdl}{\xdr'}$ are homotopy equivalent.

Indeed, we need to apply Lemma [\[lem: ext uniq\]](#lem: ext uniq){reference-type="ref" reference="lem: ext uniq"} for $(C_\bullet,d^+_\bullet)=(\tilde{C}_\bullet,\tilde{d}_\bullet^+)=(\Lambda^\bullet V,\xdl)$. The elements $a_i$ form a regular sequence hence $\Lambda^\bullet V,\xdl$ is homotopic to $\mathcal{O}=\CC[Z]/I$, $I=(a_1,\dots,a_n)$ and we conclude that $\Hom_{d_+}^{<0}(C_\bullet,C_\bullet)=\Hom_{d_+}^{<0}(\mathcal{O},C_\bullet)=0$. Moreover, the differentials $\xdr$ and $\xdr'$ are homotopies between $F\in Hom_{d_+}^0(C_\bullet,C_\bullet)$ and $0$. Thus there is a homotopy between $\Kszvvv{\xxV}{\xdl}{\xdr}$ and $\Kszvvv{\xxV}{\xdl}{\xdr'}$ and from now on we use notation $\SymbolPrint{\mathrm{K}^F}(a_1,\dots,a_n)$ for such matrix factorization.
