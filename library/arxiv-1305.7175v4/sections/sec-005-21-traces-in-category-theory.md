---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-005-21-traces-in-category-theory
section_title: "Traces in category theory"
section_number: 2.1
pages: 7-9
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.582
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
We highlight structures arising in the general theory of dualizable objects in symmetric monoidal higher categories (see also [@doldpuppe; @may; @PS]). For legibility, we suppress all $\oo$-categorical notations and complications from the introduction. We rely on [@GR] for the theory of symmetric monoidal $(\oo,2)$-categories, though only the formal outline of the theory is in fact needed for this paper. See [@TV; @HSS] for thorough treatments of the theory of traces in higher category theory.

The basic notion in the theory is that of *dimension* of a dualizable object of a symmetric monoidal category $\cA$. By definition, for such an object $A$ there exists another $A^\vee$ together with a coevaluation map $\eta_A$ and evaluation map $\epsilon_A$ satisfying standard identities. By definition, the dimension of $A$ is the endomorphism of the the unit $1_\cA$ given by the composition $$\xymatrix{ 1_\cA\ar[rr]^-{\eta_A}\ar@/_2pc/^-{\dim(A)}[rrrr] &&
  A\ot A^\vee \ar[rr]^-{\epsilon_A}&& 1_\cA}$$

::: example
For $V$ a vector space, $V^\vee =\Hom_k(V, k)$ is the vector space of functionals, $\epsilon_V: V\otimes V^\vee \to k$ is the usual evaluation of functionals, $\eta_V:k\to \End(V)\simeq V\ot V^\vee$ is the identity map (which exists only for $V$ finite-dimensional), and $\dim(V)$ can be regarded as an element of the ground field (by evaluating it on the multiplicative unit).
:::

::: remark
It is a useful technical observation that the notion of dualizability in the setting of $\oo$-categories is a "naive\" one: it is a property of an object that can be checked in the underlying homotopy category. As a result, all of the categorical and 2-categorical calculations in this paper are similarly naive and explicit (and analogous to familiar unenriched categorical assertions), involving only small amounts of data that can be checked by hand.
:::

The notion of dimension is a special case of the *trace* of an endomorphism $\Phi$ of a dualizable object $A$. By definition, the trace of $\Phi$ is the endomorphism of the unit $1_\cA$ given by the composition $$\xymatrix{1_{\cA}\ar[r]^-{\eta_A}\ar@/_2pc/^-{\Tr(\Phi)}[rrrr]& A \otimes A^\vee\ar[rr]^-{\Phi \otimes \id_{A^\vee}} &&  A\ot A^{\vee}
\ar[r]^-{\epsilon_A}& 1_\cA}$$ which recovers the dimension for $\Phi = \id_{A}$.

A key feature of dimensions and traces is their *cyclicity*, which at the coarsest level is expressed by a canonical equivalence $$\xymatrix{m(\Phi,\Psi):\Tr(\Phi\circ\Psi)\ar[r]^-{\sim}& \Tr(\Psi\circ\Phi),}$$ see Proposition [\[cyclic trace\]](#cyclic trace){reference-type="ref" reference="cyclic trace"}. At a much deeper level, an important corollary of the cobordism hypothesis [@TFT] is the existence of an $S^1$-action on $\dim(A)$ for any dualizable object $A$ (and an analogous structure for general traces, see Remark [\[full trace\]](#full trace){reference-type="ref" reference="full trace"}).

::: remark
[]{#dim local label="dim local"} It is useful for applications to note that the notion of dualizability and the definition of dimension and are local in the category $\cA$. Namely, they only require knowledge of the objects $1_{\cA},A,A^\vee, A\ot A^{\vee}$, the morphisms $\eta_A,\epsilon_A$, and standard tensor product and composition identities among them. Likewise, the notion of trace only requires the additional endomorphism $\Phi$ along with a handful of additional identities.
:::
