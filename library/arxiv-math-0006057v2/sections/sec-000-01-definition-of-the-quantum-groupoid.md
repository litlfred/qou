---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-000-01-definition-of-the-quantum-groupoid
section_title: "Definition of the quantum groupoid"
section_number: 0.1
pages: 3-4
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.929
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
By *quantum groupoids* or *weak Hopf algebras* we understand the objects introduced in [@BNSz], [@BSz1] as a generalization of ordinary Hopf algebras.

::: definition
[]{#finite quantum groupoid label="finite quantum groupoid"} A *(finite) quantum groupoid* over $k$ is a finite dimensional $k$-vector space $H$ with the structures of an associative algebra $(H,\,m,\,1)$ with multiplication $m:H\otimes_k H\to H$ and unit $1\in H$ and a coassociative coalgebra $(H,\,\Delta,\,\varepsilon)$ with comultiplication $\Delta:H\to H\otimes_k H$ and counit $\varepsilon:H\to k$ such that:

1.  The comultiplication $\Delta$ is a (not necessarily unit-preserving) homomorphism of algebras such that $$(\Delta \otimes \mbox{id}) \Delta(1) =
    (\Delta(1)\otimes 1)(1\otimes \Delta(1)) =
    (1\otimes \Delta(1))(\Delta(1)\otimes 1),
    \label{Delta 1}$$

2.  The counit is a $k$-linear map satisfying the identity: $$\varepsilon(fgh) = \varepsilon(fg_{(1)})\, \varepsilon(g_{(2)}h) = \varepsilon(fg_{(2)})\, \varepsilon(g_{(1)}h),
    \label{eps m}$$ for all $f,g,h\in H$.

3.  There is a linear map $S: H \to H$, called an *antipode*, such that, for all $h\in H$, $$\begin{aligned}
    m(\mbox{id}\otimes S)\Delta(h) &=&(\varepsilon\otimes\mbox{id})(\Delta(1)(h\otimes 1)),
    \label{S epst} \\
    m(S\otimes \mbox{id})\Delta(h) &=& (\mbox{id}\otimes \varepsilon)((1\otimes h)\Delta(1)),
    \label{S epss} \\
    m(m\otimes id)(S\otimes \mbox{id}\otimes S)(\Delta\otimes id)\Delta(h) &=& S(h).
    \label{S id S}
    \end{aligned}$$
:::

A quantum groupoid is a Hopf algebra if and only if the comultiplication is unit-preserving if and only if the counit is a homomorphism of algebras.

A *morphism* between quantum groupoids $H_1$ and $H_2$ is a map $\alpha : H_1 \to H_2$ which is both algebra and coalgebra homomorphism preserving unit and counit and which intertwines the antipodes of $H_1$ and $H_2$, i.e., $\alpha\circ S_1 = S_2\circ \alpha$. The image of a morphism is clearly a quantum groupoid. The tensor product of two quantum groupoids is defined in an obvious way.
