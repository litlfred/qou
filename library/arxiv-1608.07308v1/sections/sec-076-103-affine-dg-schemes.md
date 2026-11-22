---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-076-103-affine-dg-schemes
section_title: "Affine dg schemes"
section_number: 10.3
pages: 73-74
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.947
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:affine dg schemes label="sub:affine dg schemes"}

Dg schemes can be defined as spectra of dg algebras with respect to the étale topology, as detailed in [@B]. We will not need the full theory, and instead follow the original definition of Kontsevich.

::: definition
[]{#def:dg scheme label="def:dg scheme"}

If $X$ is an scheme with structure sheaf $\mathcal{O}_X$, an **affine dg** scheme supported on $X$ is a sheaf $\mathcal{A}$ of dg algebras, concentrated in non-positive degrees, such that $\mathcal{O}_X = H^0(\mathcal{A})$.
:::

We will write $\mathrm{Spec}\ \mathcal{A}$ for the affine dg scheme associated to $\mathcal{A}$, to match this situation with that of usual schemes. Philosophically, the approach of Definition [\[def:dg scheme\]](#def:dg scheme){reference-type="ref" reference="def:dg scheme"} can be summarized by saying that we ignore topological subtleties of dg schemes, and simply endow them with the topology coming from $\mathcal{O}_X$. The natural definition of quasi-coherent sheaves is: $$\mathrm{QCoh}(\mathrm{Spec}\ \mathcal{A}) = \mathcal{A}\text{--Mod} = \frac {\Big\{ \mathcal{P}\in \mathrm{QCoh}(X) \text{ endowed with a dg module structure for }\mathcal{A}\Big\}}{\text{quasi--isomorphism}}$$ All of the dg schemes in this paper will be of finite type, meaning that $\mathcal{A}$ is finitely generated over $\mathcal{O}_X = H^0(\mathcal{A})$. Since this is the case, it is natural to define coherent-sheaves as the full subcategory: $$\mathcal{A}\text{--mod} = \mathrm{Coh}(\mathrm{Spec}\ \mathcal{A}) \subset \mathrm{QCoh}(\mathrm{Spec}\ \mathcal{A})$$ consisting of dg modules whose cohomology groups are coherent sheaves over $\mathcal{O}_X = H^0(\mathcal{A})$.

::: example
[]{#ex:koszul label="ex:koszul"}

Suppose that $\mathcal{A}= S_X[\mathcal{N}\stackrel{s}\rightarrow \mathcal{O}_X]$ is the Koszul complex associated to a coherent sheaf $\mathcal{N}$ and a co-section $s$. Explicitly, we have: $$\mathcal{A}= \left[ ... \stackrel{d_s}\longrightarrow \wedge^2 \mathcal{N}\stackrel{d_s}\longrightarrow \mathcal{N}\stackrel{d_s}\longrightarrow \mathcal{O}_X \right]$$ The structure sheaf $\mathcal{O}_X$ situated in degree 0, as in Example [\[ex:important\]](#ex:important){reference-type="ref" reference="ex:important"}, upgraded to the situation of modules. If the co-section $s$ is regular, then it is well-known that the Koszul complex is acyclic, and the dg algebra $\mathcal{A}$ becomes isomorphic to the usual commutative algebra $\mathcal{O}_X/s$. In this case, the dg scheme is simply the subscheme of $X$ cut out by the section $s$.

However, in general it may be that the section $s$ is not regular (for example, $s$ could be 0). In this case, the dg algebra $\mathcal{A}= \wedge^\bullet \mathcal{N}$ has 0 differential but non-trivial grading. Explicitly: $$\mathcal{A}\text{--mod} = \frac {\Big\{\text{graded coherent }\mathcal{O}_X \curvearrowright \mathcal{P}^\bullet \text{ together with } \mathcal{N}\otimes \mathcal{P}^\bullet \stackrel{\lambda}\rightarrow \mathcal{P}^{\bullet-1} \text{ such that } \lambda \circ \lambda = 0\Big\}}{\text{quasi--isomorphism}}$$ In particular, if $\mathcal{N}\cong \mathcal{O}_X^{\oplus n}$ is a free module, the choice of the datum $\lambda$ corresponds to $n$ commuting degree $-1$ endomorphisms of $\mathcal{P}$.
:::

::: example
[]{#ex:affine dg label="ex:affine dg"}

In general, the affine dg schemes we will encounter will combine the previous example with the case of polynomial rings over ordinary algebras. Specifically, we will have: $$\mathcal{A}= S_X[\mathcal{M}\stackrel{s}\longrightarrow \mathcal{N}] = \left[ ... \stackrel{d_s}\longrightarrow \wedge^2 \mathcal{M}\otimes S_X\mathcal{N}\stackrel{d_s}\longrightarrow \mathcal{M}\otimes S_X\mathcal{N}\stackrel{d_s}\longrightarrow S_X\mathcal{N}\right]$$ where $\mathcal{M}\stackrel{s}\rightarrow \mathcal{N}$ is a map of coherent sheaves of $X$. The differential $d_s$ is given by [\[eqn:ds\]](#eqn:ds){reference-type="eqref" reference="eqn:ds"}, and the grading has $\wedge^i\mathcal{M}\otimes S\mathcal{N}$ sitting in degree $-i$. But note that there is an extra grading on the algebra $\mathcal{A}$, given by placing $\wedge^i \mathcal{M}\otimes S^j \mathcal{N}$ in degree $i+j$. We will write this as: $$\mathcal{A}^{\bullet,*} = \bigoplus_{i,j \geq 0} \mathcal{A}^{-i,i+j} = \bigoplus_{i,j \geq 0} \wedge^i \mathcal{M}\otimes S^j \mathcal{N}$$ Since the $* = i+j$ grading is preserved by the differential $d_s$, it descends to a grading on the cohomology groups. For example, when the morphism $s$ is regular (i.e. when the Koszul complex $\mathcal{A}$ is acyclic in negative degrees), the $\bullet$ grading collapses, and the $*$ grading matches the usual polynomial grading on the symmetric power $S^*_X (\mathcal{N}/\mathcal{M})$.
:::
