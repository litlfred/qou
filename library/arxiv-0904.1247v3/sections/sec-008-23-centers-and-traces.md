---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-008-23-centers-and-traces
section_title: "Centers and traces"
section_number: 2.3
pages: 18-20
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.978
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
[]{#defining centers label="defining centers"}

We briefly review the theory of Hochschild (co)homology of associative algebra objects in closed symmetric monoidal $\infty$-categories, following [@BFN] to which we refer for more details. This is an $\infty$-categorical version of the approach to topological Hochschild homology developed in [@EKMM; @shipley; @THH].

Let $\mathcal S$ be a closed symmetric monoidal $\infty$-category, and $A\in \mathcal S$ an associative algebra object. Then we have internal hom objects [@HA 6.1], and given $A\otimes A^{op}$-modules $M,N$, we can consider the $A\otimes A^{op}$-linear morphism object ${\mathcal Hom}_{A\otimes A^{op}}(M, N)\in \mathcal S$. Likewise, given left and right $A\otimes A^{op}$ modules $M,N\in\mathcal S$ we have a pairing $M\otimes_{A\otimes A^{op}} N\in \mathcal S$ defined by the two-sided bar construction [@HA 4.3.4] over $A\otimes A^{op}$.

::: definition
[]{#def center label="def center"} Let $A$ be an associative algebra object in a closed symmetric monoidal $\infty$-category $\mathcal S$, and $B$ an $A$-bimodule in $\mathcal S$.

1.  The Hochschild cohomology (or derived center) $\operatorname{Z}(A)=\mathop{\mathrm{HH}}^*(A)\in \mathcal S$ is the endomorphism object ${\mathcal End}_{A\otimes
      A^{op}}(A)$ of $A$ as an $A$-bimodule. More generally, the Hochschild cohomology of the bimodule $B$ is $$\mathop{\mathrm{HH}}^*(A,B)=\mathop{\mathrm{Hom}}_{A\otimes A^{op}}(A,B).$$

2.  The Hochschild homology (or derived trace) $\operatorname{Tr}(A)=\mathop{\mathrm{HH}}_*(A)\in \mathcal S$ is the pairing object ${A\otimes_{A\otimes A^{op}}
      A}$ of $A$ with itself as an $A$-bimodule. More generally, the Hochschild homology of the bimodule $B$ is $$\mathop{\mathrm{HH}}_*(A,B)=A\otimes_{A\otimes A^{op}}B.$$
:::

::: example
Taking $B=M_A\otimes{}_A N$ for a left $A$-module ${}_A N$ and a right $A$-module $M_A$, we find the relative tensor product $$\mathop{\mathrm{HH}}_*(A,M_A\otimes{}_A N)=M\otimes_A N,$$ while taking $B=\mathop{\mathrm{Hom}}({}_A M,{}_A N)$ the Hom object in $\mathcal S$ between two left $A$-modules $M,N$, we find the $A$-module Hom $$\mathop{\mathrm{HH}}^*(A,\mathop{\mathrm{Hom}}({}_A M,{}_A N))=\mathop{\mathrm{Hom}}_A(M,N).$$
:::

In general, the center $\operatorname{Z}(A)$ is again an associative algebra object in $\mathcal S$. Furthermore, $\operatorname{Z}(A)$ comes with a canonical central morphism $$\xymatrix{
\mathfrak z:\operatorname{Z}(A)
\ar[r] &
A 
&&
F\ar@{|->}[r]
& 
F(1_A)
}$$ while the trace $\operatorname{Tr}(A)$ comes with a canonical trace morphism $$\xymatrix{
\mathfrak {tr}:A 
\ar[r] &
\operatorname{Tr}(A)
}$$ coequalizing left and right multiplication.

### Cyclic bar construction {#hochschild complexes}

For an associative algebra object $A$ in a symmetric monoidal $\infty$-category $\mathcal S$, there is a natural simplicial object $\mathbf{N}^{cyc}_*(A)$ and cosimplicial object $\mathbf{N}_{cyc}^*(A)$ such that the geometric realization $\mathop{\mathrm{colim}}\mathbf{N}^{cyc}_*(A)$ calculates $\mathop{\mathrm{HH}}_*(A)=\operatorname{Tr}(A)$ and the totalization $\lim \mathbf{N}_{cyc}^*(A)$ calculates $\mathop{\mathrm{HH}}^*(A)=\operatorname{Z}(A)$.

We construct the simplicial object $\mathbf{N}^{cyc}_*(A)$ and cosimplicial object $\mathbf{N}_{cyc}^*(A)$ as follows. The $A$-bimodule $A$ has a canonical free simplicial resolution $C_*(A)$ as an $A$-bimodule with terms $$C_{n}(A)\simeq A^{\otimes n+2}$$ It is defined using the usual formalism of cotriple resolutions as in [@BFN]. The face maps come from the multiplication on $A$, and the degeneracies from the unit of $A$. The $A$-bimodule structure is the obvious action on the left and right extreme factors.

Now recall that the trace $\mathop{\mathrm{HH}}_*(A,B)$ is defined by the pairing $A\otimes_{A\otimes A^{op}}B$. Since the tensor product commutes with colimits, in particular geometric realizations, we calculate $$\mathop{\mathrm{HH}}_*(A,B) = A\otimes_{A\otimes A^{op}}B \simeq |C_*(A)|\otimes_{A\otimes A^{op}}B
\simeq |B\otimes_{A\otimes A^{op}} C_*(A)|.$$ Thus the geometric realization of $C_*(A)\otimes_{A\otimes A^{op}} B$ calculates the trace $\mathop{\mathrm{HH}}_*(A,B)$.

We write $\mathbf{N}^{cyc}_*(A)$ for the simplicial object $A\otimes_{A\otimes A^{op}} C_*(A)$ and refer to it as the Hochschild simplicial object. We can evaluate the terms of the Hochschild simplicial object $$\mathbf{N}^{cyc}_n(A) = A\otimes_{A\otimes A^{op}} C_n(A)
\simeq
A\otimes_{A\otimes A^{op}} A^{\otimes n+2} \simeq A^{\otimes n+1}$$ In particular, there are equivalences $\mathbf{N}^{cyc}_0(A) \simeq A$ and $\mathbf{N}^{cyc}_1(A) \simeq A\otimes A$, and the two simplicial maps $A\otimes A \rightarrow A$ are the multiplication and the opposite multiplication of $A$.

Similarly, recall that the center $\mathop{\mathrm{HH}}^*(A,B)$ is defined by the hom object ${\mathcal Hom}_{A\otimes A^{op}}(A,B)$. Since morphisms take colimits in the domain to limits, in particular geometric realizations to totalizations, we calculate $$\mathop{\mathrm{HH}}^*(A,B) = {\mathcal Hom}_{A\otimes A^{op}}(A,B)
\simeq  {\mathcal Hom}_{A\otimes A^{ op}}(|C_*(A)|, B)
\simeq \lim {\mathcal Hom}_{A\otimes A^{ op}}(C_*(A), B)$$ Thus the totalization of ${\mathcal Hom}_{A\otimes A^{ op}}(C_*(A), B)$ calculates the center $\mathop{\mathrm{HH}}^*(A,B)$.

We write $\mathbf{N}_{cyc}^*(A)$ for the cosimplicial object ${\mathcal Hom}_{A\otimes A^{ op}}(C_*(A), A)$ and refer to it as the Hochschild cosimplicial object.

As before, we can evaluate the terms of the Hochschild cosimplicial object $$\mathbf{N}_{cyc}^n(A) = {\mathcal Hom}_{A\otimes A^{ op}}(C_n(A), A)
\simeq
{\mathcal Hom}_{A\otimes A^{ op}}(A^{\otimes n+2}, A)
\simeq
{\mathcal Hom}(A^{\otimes n}, A).$$ In particular, there are equivalences $\mathbf{N}_{cyc}^0(A) \simeq A$ and $\mathbf{N}_{cyc}^1(A) \simeq {\mathcal Hom}(A, A)$, and the two cosimplicial maps $A\to {\mathcal Hom}(A, A)$ are induced by the left and right multiplication of $A$.

### Transposed Hochschild object {#transposed HH}

Let us now suppose that $A\in \mathcal S$ is dualizable, with dual $A'$. In that case the simplicial object $C_*(A)$ defines a dual cosimplicial object $C_*(A)^t$ with cosimplices $$C_{n}(A)^t\simeq A'^{\otimes n+2}$$ and face and degeneracies given as the transposes of those of $C_*(A)$. In this case, we can describe the center of a bimodule as a colimit $$\begin{aligned}
\mathop{\mathrm{HH}}^*(A,B) &\simeq &  \lim {\mathcal Hom}_{A\otimes A^{ op}}(C_*(A), B)\\
&\simeq & | C_*(A)' \otimes_{A\otimes A^{op}} B|
\end{aligned}$$
