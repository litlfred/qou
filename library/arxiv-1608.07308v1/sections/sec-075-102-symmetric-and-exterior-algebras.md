---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-075-102-symmetric-and-exterior-algebras
section_title: "Symmetric and exterior algebras"
section_number: 10.2
pages: 72-73
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.873
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
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
