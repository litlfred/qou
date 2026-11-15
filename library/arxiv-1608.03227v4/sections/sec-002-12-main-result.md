---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-002-12-main-result
section_title: "Main result"
section_number: 1.2
pages: 4-5
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.965
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
We consider a 'non-commutative analog' of the nested Hilbert scheme defined as a quotient $\SymbolPrint{\Hilb_{1,n}^{free}}=\SymbolPrint{\widetilde{\Hilb}_{1,n}^{free}}/\SymbolPrint{B}$, where $$\widetilde{\Hilb}_{1,n}^{free} = \{
 (X,Y,v)\in \frb\times\frn\times V\,|\,\CC\langle X,Y\rangle v=\SymbolPrint{V}
 \}$$ is an open subset of the product $\frn\times\frb\times V$ ($\frn,\frb\subset\mathfrak{gl}_n(\SymbolPrint{V})$ being the nilpotent radial and Borel subalgebra), the Borel subgroup $B\subset\mathrm{GL}_n$ acts on the first two factors by conjugation and $V$ is its fundamental representation.

Denote a flag $V_\bullet=(V_1\subset\cdots \subset V_{n-1}\subset V_n=V)\in \mathrm{Fl}$ and denote a point in the cotangent bundle $T^*\mathrm{Fl}$ as a pair $(Y,V_\bullet )$, where $Y$ is a nilpotent matrix preserving the flag: $Y V_i\subset V_{i-1}$.

In order to avoid a quotient by a non-reductive group $B$ we can define $\Hilb^{free}_{1,n}$ equivalently as a GIT $\mathrm{GL}_n$-quotient of

the space of quadruples $(X,Y,V_\bullet,v)\in \frg\times T^*\mathrm{Fl}\times V$ such that $\CC\langle X,Y\rangle v=V$ and $X V_\bullet\subset V_\bullet$. The fact that these definitions match follows from covering $\widetilde{\Hilb}_{1,n}$ by affine charts with free $B$-action, for details see proposition [\[prop: aff cover\]](#prop: aff cover){reference-type="ref" reference="prop: aff cover"}. The affine cover also provides a \"hands on\" description of the algebraic structure of the quotient manifold.

Let us denote by $\SymbolPrint{\calB^\vee}$ the trivial vector bundle over $\widetilde{\Hilb}_{1,n}^{free}$ with the fiber $V$, we use the same notation for its descent to the $B$-quotient. Respectively, $\SymbolPrint{\calB}$ is the vector bundle dual to $\calB^\vee$.

The two-dimensional torus $\SymbolPrint{\Tsc}=\CC^*\times\CC^*$ acts on $\Hilb_{1,n}^{free}$ by scaling $X,Y$: an element $(\lambda,\mu)\in T_{sc}$ turns a pair of matrices $(X,Y)$ into $(\lambda^{-2}X,\lambda^2 \mu^2Y)$. We refer to the weights of this action as $q$-degree and $t$-degree. The torus $T_{sc}$ acts on the space $V$ by $(\lambda,\mu)\cdot v=\lambda v$, that is the vectors of $V$ have degree $t$. We use notation $\SymbolPrint{  \mathsf{q}^k  \mathsf{t}^l}$ for the shift of the $T_{sc}$-action: $$(\lambda,\mu)(  \mathsf{q}^k  \mathsf{t}^l\cdot x)=\lambda^k\mu^l (\lambda,\mu)\cdot x.$$

We denote by $\SymbolPrint{D^{per}_{T_{sc}}(\Hilb_{1,n}^{free})}$ the derived category of two-periodic complexes on $\Hilb_{1,n}^{free}$ which are $T_{sc}$-equivariant. Let $\Brgrn$ denote a braid group with $n$ strands and let $\SymbolPrint{\xwr(\beta)}$ denote the writhe of a braid $\beta$ defined as the difference between the positive and negative crossings. Our main result is the construction of the object $$\SymbolPrint{\bbS_\beta}\in D^{per}_{T_{sc}}(\Hilb_{1,n}^{free}),$$ such that the hypercohomology of the complex $$\SymbolPrint{\mathbb{H}^k(\beta)}:=\mathbb{H}(\bbS_\beta\otimes \wedge^k\calB)$$ defines an isotopy invariant of $L(\beta)$. To simplify notations we assume $\mathbb{H}^k(\dots)=0$ for $k\notin \{0,1,\dots,n\}$.

::: theorem
[]{#thm: intro main label="thm: intro main"} For any $\beta\in \Brgr_n$ the triply graded space: $$\SymbolPrint{\mathcal{H}(\beta)}:=\oplus_{k\in\mathbb{Z} }\SymbolPrint{\mathcal{H}^k(\beta)},$$ with $\mathcal{H}^k(\beta)$ doubly graded defined by $$\calH^k(\beta):=  \mathsf{q}^{-\xwr(\beta)+n}\cdot\mathbb{H}^{(k-\xwr(\beta)+n-1)/2}(\beta),$$ is an isotopy invariant of the braid closure $L(\beta)$.
:::

Let us also introduce a notation for the graded pieces of $\calH^k$: $\SymbolPrint{\calH^{i,j,k}}\subset \calH^k$ is the subspace of vectors that are of weight $q^it^j$. We show that our invariant categorifies HOMFLY-PT polynomial.

::: theorem
[]{#thm:HOMFLY label="thm:HOMFLY"} The bi-graded Euler characteristic of $\calH^k(\beta)$ is equal to the HOMFLY-PT polynomial of the link $L(\beta)$: $$P\bigl(L(\beta)\bigr) =\sum_{i,j,k\in\mathbb{Z} } (-1)^j q^i a^k\dim  \calH^{i,j,k}(\beta).$$
:::

The first categorification of HOMFLY-PT polynomial was discovered by Khovanov and Rozansky [@KhR] and it is natural to expect that the homology theory from this paper coincides with one from [@KhR]. We do not have a proof for a match of these theories.
