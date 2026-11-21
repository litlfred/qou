---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-007-21-notations-conventions
section_title: "Notations, conventions"
section_number: 2.1
pages: 8-8
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
### 

Let us fix the following notations for the groups that appear in our work: $$\SymbolPrint{G_n}=\mathrm{GL}_n,\quad \SymbolPrint{T_n}\subset B_n\subset G_n.$$

We use gothic script for the Lie algebras of the respective groups. Whenever the rank of the group is obvious from the context of the paper we omit the subscripts. Let $U_n=[B_n,B_n]$ and $\frn_n=\textup{Lie}(U_n)$. We also denote the Lie algebra of $T_n$ as $\SymbolPrint{\mathfrak{h}_n}$.

Let us also fix the notations for the projections on the upper and the lower triangular parts of the matrix: for a given square matrix $X$ we denote by $\SymbolPrint{X_+}$ and $\SymbolPrint{X_{++}}$ the upper-triangular and the strictly upper-triangular part of $X$: $$(X_{++})_{ij}=\begin{cases} X_{ij},& i<j\\
                            0,&i \ge j
                          \end{cases},\quad (X_{+})_{ij}=\begin{cases} X_{ij},&i\le j\\
                            0,&i>j
                          \end{cases}$$ respectively $X_-:=X-X_{++}$ and $X_{--}:=X-X_+$ are the lower-triangular and strictly lower-triangular parts of $X$.

The main geometric object in our study is the ($G_n\times B_n^\ell$)-space $\calX_\ell=\frg_n\times (G_n\times \frn_n)^\ell$ with the following action of the group: $$(b_1,\dots,b_\ell)\cdot (X,g_1,Y_1,\dots,g_\ell, Y_\ell)=(X,g_1\cdot b_1^{-1},\Ad_{b_1}(Y_1),\dots,g_\ell\cdot b_\ell^{-1},\Ad_{b_\ell}(Y_\ell)),$$ $$h\cdot (X,h\cdot g_1,Y_1,\dots,g_\ell, Y_\ell)=(\Ad_h(X),h\cdot g_1,Y_1,\dots,h\cdot g_\ell,Y_\ell).$$

The space $\calX_2$ is the enlarged version of the space $\calXr_2(G_n)$, that was discussed in the introduction. Sometimes we use notation $\calX_2(G_n)$ for $\calX_2$.
