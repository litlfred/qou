---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-057-73-eigenobjects
section_title: "Eigenobjects"
section_number: 7.3
pages: 53-54
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.933
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:eigenobjects label="sub:eigenobjects"}

In Definition [\[def:EH1\]](#def:EH1){reference-type="ref" reference="def:EH1"} we have recalled the categorical version of eigenvalues. In [@EH], the authors complete the picture by categorifying eigenvectors:

::: definition
[]{#def:EH3 label="def:EH3"} If for some $P \in \mathcal{C}$ the arrow: $$\label{eqn:eigenobject}
\alpha \otimes \mathop{\mathrm{Id}}_P : \lambda\cdot P \stackrel{\cong}\longrightarrow F\otimes P$$ is an isomorphism, then we call $P$ an **eigenobject** for the datum of Definition [\[def:EH1\]](#def:EH1){reference-type="ref" reference="def:EH1"}.
:::

In the decategorified world, the eigenvectors of the operator of multiplication by $[F]$ of [\[eqn:charpoly\]](#eqn:charpoly){reference-type="eqref" reference="eqn:charpoly"} can be computed explicitly, essentially by the Lagrange interpolation formula: $$\label{eqn:idempotent0}
[P_i] := \prod_{0\leq j \neq i \leq n} \frac {\lambda_j - [F]}{\lambda_j-\lambda_i}$$ The reason why we divide by $\lambda_j-\lambda_i$ is to ensure that the elements $[P_i]$ are idempotents. However, this comes at the cost of enlarging the algebra to account for such denominators. One of the main constructions in [@EH] is the categorify formula [\[eqn:idempotent0\]](#eqn:idempotent0){reference-type="eqref" reference="eqn:idempotent0"} in a way which keeps track of the eigenmaps.

The main difficulty, which we will shortly address, is how to lift the denominators of [\[eqn:idempotent0\]](#eqn:idempotent0){reference-type="eqref" reference="eqn:idempotent0"} from the Grothendieck group to the category $\mathcal{C}$. The idea spelled out in [@EH] is that in [\[eqn:idempotent0\]](#eqn:idempotent0){reference-type="eqref" reference="eqn:idempotent0"} one should expand: $$\frac {\lambda_j - [F]}{\lambda_j-\lambda_i} = \left(1 - \frac {[F]}{\lambda_j} \right)\left(1 + \frac {\lambda_i}{\lambda_j} + \frac {\lambda_i^2}{\lambda_j^2} + ... \right)$$ if $j<i$ and: $$\frac {\lambda_j - [F]}{\lambda_j-\lambda_i} = \left(\frac {[F]}{\lambda_i} - \frac {\lambda_j}{\lambda_i} \right)\left(1 + \frac {\lambda_j}{\lambda_i} + \frac {\lambda_j^2}{\lambda_i^2} + ... \right)$$ if $j>i$. To understand the above as an expansion of geometric series, we assume that there exists a distinguished subtorus $\mathbb{C}^* \subset T$ which we will be called **homological**, such that: $$\label{eqn:increasing}
\lambda_0|_{\mathbb{C}^*} > ... > \lambda_n|_{\mathbb{C}^*}$$ To categorify these geometric series, [@EH] replace the category $\mathcal{C}$ by its **homological completion** $\mathcal{C}^{\uparrow}$, as in Section [\[def:cat\]](#def:cat){reference-type="ref" reference="def:cat"}.

::: theorem
([@EH]) []{#thm:EH diagonalization label="thm:EH diagonalization"} Let $F$ be a diagonalizable object, with eigenmaps $\alpha_i$ and eigenvalues $\lambda_i$ satisfying [\[eqn:increasing\]](#eqn:increasing){reference-type="eqref" reference="eqn:increasing"}. Then there exist a collection of eigenobjects $P_i$ as in [\[eqn:eigenobject\]](#eqn:eigenobject){reference-type="eqref" reference="eqn:eigenobject"}, explicitly given by: $$\label{eqn:idempotent}
\includegraphics{7_7.png}$$ The objects should be added $\oplus$ along columns, with differentials according to the arrows. The collection $\{P_0,...,P_n\}$ yields a semi-orthogonal decomposition of $\overline{\mathcal{C}}$: $$\label{eqn:semi orthogonal}
\mathbf{1} \cong \Big[P_0 \oplus ... \oplus P_n, \text{ a certain differential} \Big]$$ and $\mathop{\mathrm{Hom}}_{\overline{\mathcal{C}}}(P_i,P_j)=0$ if $i>j$. Furthermore, $P_i\otimes P_j\simeq 0$ for $i\neq j$ and $P_i\otimes P_i\simeq P_i$.
:::

The main application of [@EH] is when $\mathcal{C}= K^b(\mathrm{SBim}_n)$ is replaced by $\overline{\mathcal{C}}= K^-(\mathrm{SBim}_n)$, and the homological $\mathbb{C}^*$ action is by homological degree of chain complexes. We may generalize this particular case to the following setup.
