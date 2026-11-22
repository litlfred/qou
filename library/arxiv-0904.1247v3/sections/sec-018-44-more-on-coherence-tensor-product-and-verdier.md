---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-018-44-more-on-coherence-tensor-product-and-verdier
section_title: "More on coherence, tensor product, and Verdier duality"
section_number: 4.4
pages: 29-30
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.927
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
Since $f^!$ for a smooth morphism $f:X\to Y$ preserves coherence, one may define coherent ${\mathcal D}$-modules on a stack by requiring coherence locally on smooth covers. We denote by $\mathcal D_{coh}(X)\subset {\mathcal D}(X)$ the full subcategory of coherent ${\mathcal D}$-modules.

By [@finiteness Theorem 8.1.1], for any stack $X$, the category ${\mathcal D}(X)$ is compactly generated and all compact objects are coherent. However, it is not necessarily true that all coherent ${\mathcal D}$-modules are compact. For example, the object $\mathbb C_X \in {\mathcal D}(X)$ representing the de Rham cohomology functor $\Gamma_{dR}$ is coherent (and in fact holonomic) but not in general compact. The case of the classifying space $X=BG$ of an affine group $G$ is illuminating and worked out in detail in [@finiteness Section 7.2]. In this case, $\Gamma_{dR}$ calculates equivariant cohomology, which is not continuous even when $G$ is the multiplicative group. More generally, finite rank vector bundles with flat connection on a smooth stack are coherent (and in fact holonomic) but not necessarily compact.

In general, there is the notion of *safe* stacks characterized by the assumption that coherent ${\mathcal D}$-modules are compact. In [@finiteness Section 10.2], the following conditions are shown to be equivalent:

$\bullet$ all coherent ${\mathcal D}$-modules on $X$ are compact,

$\bullet$ the object $\mathbb C_X$ is compact, i.e., the functor $\Gamma_{dR}$ is continuous,

$\bullet$ the identity component of the automorphism group of any geometric point of $X$ is unipotent.

For example, any Deligne-Mumford stack is safe.

More generally, there is the relative notion of safe morphism $f:X\to Y$ of stacks characterized by the assumption that $f_*$ is continuous. It guarantees familiar properties such as the projection formula hold.

We will make repeated use of [@finiteness Corollary 8.3.4] which asserts that for any stacks (in fact, for any prestacks), external tensor product provides a natural equivalence $$\xymatrix{
\boxtimes:{\mathcal D}(X)\otimes {\mathcal D}(Y)\ar[r]^-\sim &  {\mathcal D}(X\times Y)
}$$

There is a resulting symmetric monoidal structure on ${\mathcal D}(X)$ whose multiplication can be calculated locally with respect to smooth covers.

One can extend Verdier duality to ${\mathcal D}$-modules on stacks by applying it locally, intertwining the realizations of ${\mathcal D}$-modules in terms of descent under $!$- and $*$-pullbacks. Moreover, Verdier duality restricts to compact objects, where as in equation [\[Verdier\]](#Verdier){reference-type="eqref" reference="Verdier"}, it is characterized by a functorial equivalence $$\label{Verdierstacks}
\xymatrix{
\mathop{\mathrm{Hom}}_{{\mathcal D}(X)}(\mathbb D_X(\mathfrak M),\mathfrak N)\simeq  \mathop{\mathrm{Hom}}_{{\mathcal D}(X)}(\mathbb C_X, \mathfrak M\otimes\mathfrak N) 
& \mathfrak M, \mathfrak N\in {\mathcal D}(X)_{cpt}
}$$ Here as elsewhere we write ${\mathcal D}(X)_{cpt}$ for the compact objects of ${\mathcal D}(X)$. Its continuous extension to all ${\mathcal D}$-modules provides a canonical self-duality $$\xymatrix{\mathbb D_X:{\mathcal D}(X)' \ar[r]^-{\sim}& {\mathcal D}(X) }$$ Note that equation [\[Verdierstacks\]](#Verdierstacks){reference-type="eqref" reference="Verdierstacks"} does not necessarily hold for arbitrary $\mathfrak M, \mathfrak N\in{\mathcal D}(X)$. The left hand side is continuous in each, but $\mathbb C_X\in {\mathcal D}(X)$ may not be compact and hence the right hand side may not be continuous.
