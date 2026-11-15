---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-003-211-torsion-of-a-chain-complex
section_title: "Torsion of a chain complex"
section_number: 2.1.1
pages: 4-6
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.991
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Let $F$ be a field and $C_*=(C_*,\partial)$ a chain complex of finite dimensional $F$-vector spaces: $$C_d\xrightarrow{\partial} C_{d-1} \xrightarrow{\partial}\cdots 
\xrightarrow{\partial} C_0.$$ The subspaces of boundaries and cycles are denoted by $B_i=\operatorname{Im}(C_{i+1}
\xrightarrow{\partial} C_i)$ and $Z_i=\ker(C_{i}
\xrightarrow{\partial} C_{i-1} )$ respectively, the homology is denoted by by $H_i=Z_i/B_i$. Assume $$c_i=\{c_{i,1},\ldots,c_{i,j_i}\}$$ is an $F$-basis for $C_i$ and $$h_i=\{h_{i,1},\ldots,h_{i,r_i}\},$$ is a basis for $H_i$, if nonzero. For the definition of torsion, a basis $$b_i=\{b_{i,1},\ldots,b_{i,r_i} \}$$ for $B_i$ is also required. Using the exact sequences: $$\begin{gathered}
\label{eqn:cycle} 0\to Z_i\to C_i \xrightarrow{\partial} B_{i-1}\to 0 \\
\label{eqn:homology}  0\to B_i\to Z_i\to H_i\to 0,
\end{gathered}$$ lift $b_{i-1}$ to $\tilde b_{i-1}\subset C_i$ in [\[eqn:cycle\]](#eqn:cycle){reference-type="eqref" reference="eqn:cycle"} and $h_i$ to $\tilde h_i\subset Z_i\subset C_ i$ in [\[eqn:homology\]](#eqn:homology){reference-type="eqref" reference="eqn:homology"} and construct a new basis for $C_i$: $$b_i\sqcup \tilde  b_{i-1}\sqcup \tilde h_i ,$$ where $\sqcup$ denotes the disjoint union. The bases are compared with the determinant of the corresponding matrix. Given two bases $\alpha=\{\alpha_1,\ldots,\alpha_r\}$ and $\beta=\{\beta_1,\ldots,\beta_r\}$ for $F^r$, if $(\eta_{ij})\in 
\operatorname{M}_n(F)$ is the matrix that relates the bases, i.e. if $\alpha_i= \sum_j 
\eta_{ij}\beta_j$, set $$\label{eqn:det}
[\alpha,\beta]=\det(\eta_{ij})\in F^*.$$

::: definition
[]{#def:torsionchain label="def:torsionchain"} The torsion of the chain complex $C_*$ with bases $\{c_i\}$ and bases $\{h_i\}$ for $H_i$ is: $$\label{eqn:torcplx}
  \operatorname{tor}(C_*,\{c_i\},\{h_i\})= \prod_{i=0}^{d} [ b^i\sqcup \tilde  b_{i-1}\sqcup 
\tilde h_i, c_i] ^{(-1)^{i+1}}\in F^*/\{\pm 1\}.$$
:::

As it is an alternated product, it is easy to see that it does not depend on the choice of $b_i$, the basis for $B_i$, and it is also straightforward that it does not depend on the lifts $\tilde b_{i-1}$ and $\tilde h_{i}$.

::: remark
[]{#rem:convention label="rem:convention"} In the alternated product defining the torsion of a complex [\[eqn:torcplx\]](#eqn:torcplx){reference-type="eqref" reference="eqn:torcplx"}, may authors use ${(-1)^{i}}$ instead of ${(-1)^{i+1}}$. Definition [\[def:torsionchain\]](#def:torsionchain){reference-type="ref" reference="def:torsionchain"} follows the convention of [@Turaev01; @Turaev02; @Turaev86; @Milnor62; @Kitano96] for instance, but opposite to [@Milnor66; @Dubois05] and all papers on analytic torsion [@Cheeger79; @Muller93] and quantum invariants [@Witten89; @BNW91; @DK07; @GM08; @DG11; @HM11; @Murakami13; @DG13; @OT15; @DuboisG16]. I followed this convention in [@Memoirs] but not in [@MFP14]. This convention is better suited for polynomials, also for functions on the deformation space; the opposite one is more useful for the interpretation of the torsion as a volume form.

We follow a different definition for the torsion of a cocomplex, which gives a nonstandard statement of Lemma [\[lemma:dual\]](#lemma:dual){reference-type="ref" reference="lemma:dual"} (in the standard version it is corrected by a power $(-1)^n$).
:::

There is a formula of change of bases. For different choices $c'_i$ and $h'_i$ of bases for $C_i$ and $H_i$ we have $$\label{eqn:change}
 \frac{ \operatorname{tor}(C_*,\{c_i'\},\{h_i'\} )}{ \operatorname{tor}(C_*,\{c_i\},\{h_i\}) } =
 \prod_{i=0}^{d}  \left(\frac{[c'_i,c_i ]}{ [h'_i,h_i ]}\right)^{(-1)^i}.$$ The proof is straightforward, see [@Milnor66; @Memoirs; @Nicolaescu] for details.

::: definition
[]{#def:cochain label="def:cochain"} Let $C^*=(C^*,\delta)$ be a *cochain complex* with bases $\{c^i\}$, and cohomology bases $\{h^i\}$, by constructing the $b^i$ in a similar way, its torsion is defined as $$\label{eqn:cohom}
 \operatorname{tor}(C^*,\{c^i\},\{h^i\})=\prod_{i=0}^{d} [ b^i\sqcup \tilde  b^{i-1}\sqcup 
\tilde h^i, c_i] ^{(-1)^{i}}\in F^*/\{\pm 1\}.$$
:::

The convention of powers $(-1)^{i}$ and $(-1)^{i+1}$ has been changed in this definition, for the purpose of Lemma [\[lemma:dual\]](#lemma:dual){reference-type="ref" reference="lemma:dual"}.

::: lemma
Let $(C_i)^ \star=\hom_F(C_i,F)$ be the dual cocomplex, with coboundary $\delta: 
C_i^\star\to C^\star_{i-1}$ defined by $\delta(\theta)=\theta\circ d$. If $(h_i)^\star$ is dual to $h_i$, then []{#lemma:dual label="lemma:dual"} $$\operatorname{tor}(C_*,\{h_i\}) =\operatorname{tor}((C_*)^\star, \{ (h_i)^\star\}).$$
:::

Notice that this lemma uses Definition [\[def:cochain\]](#def:cochain){reference-type="ref" reference="def:cochain"} of a cochain complex. If instead of the cocomplex one considers the dual complex, one must re-index the dimension $i$ by $d-i$, then the torsion of the complex is replaced by its $(-1)^{d+1}$-power! Then, one may see [@Franz37; @Milnor62] for a proof with this version of Lemma [\[lemma:dual\]](#lemma:dual){reference-type="ref" reference="lemma:dual"}.
