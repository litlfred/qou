---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-054-102-symmetric-and-exterior-algebras
section_title: "Symmetric and exterior algebras"
section_number: 10.2
pages: 72-74
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.81
---
[]{#sub:sym ext label="sub:sym ext"}

There will be two main examples of dg algebras, both associated to a vector space $V$. The first is the **symmetric algebra**: $$\label{eqn:symm}
S V = \bigoplus_{d=0}^\infty S^d V$$ concentrated in degree 0 and with trivial differential, and the **exterior algebra**: $$\label{eqn:ext}
\wedge V = \bigoplus_{d=0}^\infty \wedge^d V$$ situated in degrees $...,-2,-1,0$ and with trivial differential. By definition, the spaces [\[eqn:symm\]](#eqn:symm){reference-type="eqref" reference="eqn:symm"} and [\[eqn:ext\]](#eqn:ext){reference-type="eqref" reference="eqn:ext"} are quotients of the tensor algebra of $V$ by the relations $v\otimes v' \mp v' \otimes v$. Therefore, they are both particular cases of the symmetric algebra of a dg vector space: $$\label{eqn:symm ext}
S V^\bullet := \left(\bigoplus_{n=0}^\infty V^\bullet \otimes ... \otimes V^\bullet \right) \Big/ \left( v \otimes v' - (-1)^{(\deg v)(\deg v')} v' \otimes v \right)$$ which inherits the differential from $V^\bullet$: $$d(v_1 \otimes ... \otimes v_k) = \sum_{i=1}^k (-1)^{\deg v_1 + ... + \deg v_{i-1}} \cdot v_1 \otimes ... \otimes v_{i-1} \otimes d(v_i) \otimes v_{i+1} \otimes ... \otimes v_k$$ By the very definition, [\[eqn:symm ext\]](#eqn:symm ext){reference-type="eqref" reference="eqn:symm ext"} is a commutative dg algebra, which is concentrated in non-positive degrees as long as the original dg vector space $V^\bullet$ is. In particular, when the dg vector space is concentrated in degree 0 (respectively -1), we obtain [\[eqn:symm\]](#eqn:symm){reference-type="eqref" reference="eqn:symm"} (respectively [\[eqn:ext\]](#eqn:ext){reference-type="eqref" reference="eqn:ext"}.

::: example
[]{#ex:important label="ex:important"}

A particularly important case of the construction [\[eqn:symm ext\]](#eqn:symm ext){reference-type="eqref" reference="eqn:symm ext"} is when: $$V^\bullet = \left[ M \stackrel{s}\longrightarrow N \right]$$ is concentrated in degrees $-1$ and 0. Then we have: $$S V^\bullet = \left[ ... \stackrel{d_s}\longrightarrow \wedge^2 M \otimes S N \stackrel{d_s}\longrightarrow M \otimes S N \stackrel{d_s}\longrightarrow S N \right]$$ in degrees $...,-2,-1,0$, with differential given by: $$\label{eqn:ds}
d_s(m_1 \wedge... \wedge m_k \otimes n) = (-1)^{k-1} \sum_{i=0}^k m_1 \wedge ... \wedge m_{i-1} \wedge m_{i+1} \wedge ... \wedge m_k \otimes s(m_i)n$$ for all $m_1,...,m_k \in M$ and $n \in S N$.
:::

More generally, suppose that $A$ is a dg algebra and $M$ is a dg module for $A$. Define: $$S_{A} M^\bullet = SM^\bullet \Big/ \left( am \otimes m' - m \otimes a m' \right)$$ which will also be a dg module for $A$. The formalism above, as well as Example [\[ex:important\]](#ex:important){reference-type="ref" reference="ex:important"}, apply.

## Affine dg schemes {#sub:affine dg schemes}

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
