---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-012-33-bar-constructions
section_title: "Bar constructions"
section_number: 3.3
pages: 24-25
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.986
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
Recall that $C_*(A)$ denotes the canonical simplicial resolution of $A$ as an $A$-bimodule, i.e., the monadic bar construction for the algebra $A$. Let $C_*(A)^{tr}$ denote the cosimplicial object obtained by passing to transposes, i.e., the comonadic cobar construction for the coalgebra $(A',\mu^t)$. Likewise, let $C_*(A)^r$ denote the cosimplicial object obtained by passing to right adjoints, i.e., the comonadic cobar construction for $(A^r,\mu^r)$. Note however that unless $A$ is rigid, the right adjoint to the unit morphism is not continuous, hence this cosimplicial object is not a diagram of continuous functors. We use the term semi-cosimplicial object to refer to the diagram object obtained from such a cosimplicial object by forgetting its codegeneracies, see [@topos Notation 6.5.3.6]. By [@topos Lemma 6.5.3.7], the inclusion of the semisimplical $\infty$-category in the simplicial one is cofinal, so that we may calculate totalizations of cosimplicial objects as limits over the underlying semi-cosimplicial objects. The underlying semi-cosimplicial object of $C_*(A)^r$ is indeed a diagram of continuous functors. The following is an immediate corollary of the above proposition:

::: cor
[]{#reversing arrows label="reversing arrows"} If $A\in  Alg(St_\mathbb C)$ is a semi-rigid monoidal category, then the semi-cosimplicial objects underlying $C_*(A)^r$ and $C_*(A)^{tr}$ are canonically equivalent. (If in addition $A$ is rigid, the cosimplicial objects $C_*(A)^r$ and $C_*(A)^{tr}$ are canonically equivalent.) In fact, there is a natural equivalence of diagrams of $A$-bimodules $$\xymatrix{ C_*(A)^r_{LL} \ar[r]^-{R} &C_*(A)^{tr}}$$ where the right $A$-action on $C_*(A)^r$ is twisted by the monoidal automorphism $LL$.
:::

Recall from Section [\[transposed HH\]](#transposed HH){reference-type="ref" reference="transposed HH"} that the cosimplicial diagram $C_*(A)^{tr}$ can be used to calculate Hochschild cohomology of $A$-bimodules. The cosimplicial object $C_*(A)^r$ can likewise be used to calculate Hochschild homology, so that Corollary [\[reversing arrows\]](#reversing arrows){reference-type="ref" reference="reversing arrows"} results in a general identification of traces and centers:

::: prop
[]{#reversing hh label="reversing hh"} Let $A\in  Alg(St_\mathbb C)$ be a semi-rigid monoidal category.

1.  For any $A$-bimodule, we have an equivalence between a twist of the center and the trace: $$\mathop{\mathrm{HH}}_*(A,B)\simeq \mathop{\mathrm{HH}}^*(A,{}_{LL} B).$$

2.  In particular, for $M$ a dualizable left $A$-module with dual $M'$ and $N$ an arbitrary left $A$-module, there is a canonical equivalence $$\mathop{\mathrm{Hom}}_A(M,{}_{LL}N) \simeq M' \otimes_A N$$ between a twist of the relative $\mathop{\mathrm{Hom}}$ and the relative tensor product of the dual of $M$ with $N$.
:::

::: proof
*Proof.* Recall the description of Hochschild homology via the bar resolution, $$\mathop{\mathrm{HH}}_*(A,B) = A\otimes_{A\otimes A^{op}}B \simeq \mathop{\mathrm{colim}}C_*(A)\otimes_{A\otimes A^{op}}B.$$ By Section [\[reversing diagrams\]](#reversing diagrams){reference-type="ref" reference="reversing diagrams"}, this colimit can be identified with the limit over the corresponding cosimplicial diagram, obtained by taking right adjoints (note that the simplicial object $C_*(A)\otimes_{A\otimes A^{op}} B$, the relative tensor product of a diagram of continuous functors by $B$, is a diagram of continuous functors). This adjoint cosimplicial diagram is naturally identified with $C_*(A)^r\otimes_{A\otimes A^{op}} B$, i.e., can be calculated by taking right adjoints in $C_*(A)$. Hence by Corollary [\[reversing arrows\]](#reversing arrows){reference-type="ref" reference="reversing arrows"}, we find $$\begin{aligned}
\mathop{\mathrm{HH}}_*(A,B) & \simeq& \mathop{\mathrm{colim}}C_*(A)\otimes_{A\otimes A^{op}}B\\
&\simeq& \lim C_*(A)^r \otimes_{A\otimes A^{op}} B\\
&\simeq& \lim C_*(A)^t_{RR} \otimes_{A\otimes A^{op}} B\\
&\simeq& \lim C_*(A)^t\otimes_{A\otimes A^{op}} {}_{LL} B\\
&\simeq& \mathop{\mathrm{HH}}^*(A,{}_{LL} B).
\end{aligned}$$

The second assertion follows immediately from the special case $B=N\otimes M'$. ◻
:::

::: prop
[]{#bimodule dual label="bimodule dual"} For $A$ semi-rigid and $M$ an $A$-module, $M$ is $A$-dualizable if and only if $M$ is dualizable in $St_\mathbb C$. In this case, the $A$-dual is canonically identified with the twisted naive dual $M'_{RR}$ as right $A$-modules.

In particular, the canonical pivotal structure on $A^e= A\otimes A^{op}$ induces an identification of the $A^e$-dual and $St_\mathbb C$-duals of $A$ (or any $A$-bimodule).
:::

::: proof
*Proof.* Suppose $M$ is dualizable in $\mathcal S$. We first apply Proposition [\[reversing hh\]](#reversing hh){reference-type="ref" reference="reversing hh"} and find $$\begin{aligned}
\mathop{\mathrm{Hom}}_{A}(M,A)&\simeq& M' \otimes_A {}_{LL} A\\
 &\simeq& M'_{RR}. 
 
\end{aligned}$$

On the other hand $$\begin{aligned}
 M'_{RR} \otimes_{A} M &\simeq& M' \otimes_{A} {}_{LL}M\\
 &\simeq& \mathop{\mathrm{Hom}}_{A}(M,M).
 
\end{aligned}$$

We can now realize $M'_{RR}$ as the $A$-dual of $M$ by taking the canonical evaluation and coevaluation maps $$\xymatrix{
M\otimes M'_{RR} \simeq M\otimes \mathop{\mathrm{Hom}}_{A}(M,A)\ar[r]^-{ev} &  A
&
\operatorname{Vect}_\mathbb C\ar[r] &  \mathop{\mathrm{Hom}}_{A}(M,M)\simeq M'_{RR}\otimes_{A} M
}$$

Similarly, if $M$ is $A$-dualizable with dual $\widetilde{M}$, we can explicitly exhibit a duality in $St_\mathbb C$ between $M$ and $M'=\widetilde{M}_{LL}$. ◻
:::
