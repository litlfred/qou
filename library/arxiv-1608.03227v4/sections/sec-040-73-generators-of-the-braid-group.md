---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-040-73-generators-of-the-braid-group
section_title: "Generators of the braid group"
section_number: 7.3
pages: 41-42
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.979
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec:gens label="ssec:gens"}

When $n=2$ the potential is $\Wr(X,g,Y)=\Tr(X\Ad_g(Y))$ where $$g=\begin{bmatrix} g_{11}&g_{12}\\ g_{21}& g_{22}\end{bmatrix},\quad X=\begin{bmatrix} x_{11}&x_{12}\\ 0& x_{22}\end{bmatrix},\quad Y=\begin{bmatrix} 0& y_{12}\\0&0\end{bmatrix}$$ A direct computation shows that it factors: $$\Wr(X,g,Y)=y_{12}(g_{11}(x_{11}-x_{22})+g_{21}x_{12})g_{21}/\Delta,\quad \Delta=\det(g).$$

If $n=2$ then the unit matrix factorization from section [\[sec: unit\]](#sec: unit){reference-type="ref" reference="sec: unit"} is: $$\crX_{\parallel}=\Phi(\begin{bmatrix}g_{21}\Delta^{-1}& y_{12}(g_{11}(x_{11}-x_{22})+g_{21}x_{12})\end{bmatrix}),$$

Let also introduce the matrix factorizations $\crX_{+}$, $\crX_{\bullet}$: $$\SymbolPrint{\crX_{\bullet}}=\Phi(\begin{bmatrix}y_{12}\Delta^{-1}& g_{21}(g_{11}(X_{11}-X_{22})+g_{21}X_{12})\end{bmatrix}),$$ $$\label{eq: C+}
\SymbolPrint{\crX_{+}}=\Phi(\begin{bmatrix}g_{21}y_{12}\Delta^{-1}& (g_{11}(x_{11}-x_{22})+g_{21}x_{12})\end{bmatrix}).$$ The complex $\crX_+$, as we will see later, correspond to the positive crossing of two strands in the braid. To define the complex corresponding to the negative crossing we need to shift the weights of $B^2$ action on $\crX_+$.

Let $\chi_1,\chi_2$ be the generators of the group of characters of $B$: $$\SymbolPrint{\chi_1}\left(\begin{bmatrix}a&b\\0&c\end{bmatrix}\right)=a,\quad \SymbolPrint{\chi_2}\left(\begin{bmatrix}a&b\\0&c\end{bmatrix}\right)=c.$$ Bellow we use convention that $\calF\brwsh{\chi'}{\chi''}\in \MF_{B^2}(\calX_2(G_2),W)$ is obtained from the complex $\calF$ by twisting the action of the first factor in $B^2$ by the character $\chi'$ and the action of the second copy is twisted by the character $\chi''$. With these conventions in mind we have the following formula for the complex of negative crossing. $$\label{eq: C-}
 \SymbolPrint{\crX_-}:=\crX_+\brwsh{-\chi_1}{\chi_2}.$$

We postpone the description of the $T_{sc}$-equivariant structure of matrix factorizations from above till the section [\[sec: two str\]](#sec: two str){reference-type="ref" reference="sec: two str"}. In the section [\[sec: two str\]](#sec: two str){reference-type="ref" reference="sec: two str"} we show that the convolution of $\crX_{+}$ and $\crX_-$ is homotopic to $\crX_\parallel$.

To define the generators of $\Brgr_n$ for general $n$ we use our induction functor: $$\SymbolPrint{\crX_{\pm}^{(i)}}:=\Ind_{ii+1}(\crX_{\pm}),\quad \crX_{\parallel}^{(i)}:=\Ind_{ii+1}(\crX_\parallel).$$

It is elementary to check that $\crX_{\parallel}^{(i)}$ is independent of $i$ and is a unit in the convolution algebra (see next section for the proof). The main result of the first part of the paper is the following theorem

::: theorem
[]{#thm: braids label="thm: braids"} The complexes $\crX_{\pm}^{(i)}$ satisfy the braid relations $$\begin{gathered}
\crX_{+}^{(i)}\star\crX_{-}^{(i)}\sim\crX_\parallel,\label{eq: inverse}\\
\crX_{+}^{(i)}\star \crX_{+}^{(i+1)} \star \crX_{+}^{(i)}\sim \crX_{+}^{(i+1)}\star \crX_{+}^{(i)}\star \crX_{+}^{(i+1)},\label{eq: cubic}\\
\crX_{+}^{(i)}\star \crX_{+}^{(j)}\sim\crX_{+}^{(j)}\star \crX_{+}^{(i)},\quad |i-j|>1.\label{eq: commuting}
\end{gathered}$$ where $\sim$ is the homotopy equivalence.
:::

::: proof
*Proof.* The relation ([\[eq: inverse\]](#eq: inverse){reference-type="ref" reference="eq: inverse"}) is proven for two strand braids in lemma [\[thm: two strands\]](#thm: two strands){reference-type="ref" reference="thm: two strands"}. Hence by corollary [\[cor: ind\]](#cor: ind){reference-type="ref" reference="cor: ind"} the relation ([\[eq: inverse\]](#eq: inverse){reference-type="ref" reference="eq: inverse"}) holds in general. The equation ([\[eq: cubic\]](#eq: cubic){reference-type="ref" reference="eq: cubic"}) is proven for three strand braids in corollary [\[cor: cubic\]](#cor: cubic){reference-type="ref" reference="cor: cubic"}. Finally, the commuting relation ([\[eq: commuting\]](#eq: commuting){reference-type="ref" reference="eq: commuting"}) follows from the corollary [\[cor: commute\]](#cor: commute){reference-type="ref" reference="cor: commute"}. ◻
:::

For a given element $\beta=\sigma_{i_1}^{\epsilon_1}\cdots\sigma_{i_\ell}^{\epsilon_\ell}$ we introduce the following notations: $$\calC_\beta=\calC_{\epsilon_1}^{(i_1)}\star\dots \calC_{\epsilon_\ell}^{(i_\ell)},\quad \bcalC_\beta=\bcalC_{\epsilon_1}^{(i_1)}\bar{\star}\dots \bar{\star}\bcalC_{\epsilon_\ell}^{(i_\ell)}.$$
