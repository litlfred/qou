---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-024-61-derivation-based-connections-first-definition
section_title: "Derivation-based connections. First definition"
section_number: 6.1
pages: 30-30
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.977
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
Let $J$ be a unital Jordan algebra with center (= centroid) $Z(J)$ and let ${\mbox{Der}}(J)$ be the Lie algebra and $Z(J)$-module of derivations of $J$. A *(derivation-based) connection* $\nabla$ on a unital $J$-module $M$ is a linear mapping $X\mapsto \nabla_X$ of ${\mbox{Der}}(J)$ into the linear endomorphisms of $M$ such that $$\left\{
 \begin{array}{l}
 \nabla_X(xm)=X(x)m +x\nabla_X(m)\\
 \\
 \nabla_{zX}(m)=z\nabla_X(m)
 \end{array}
 \right.
  \label{covder}$$ for any $m\in M$, $x\in J$ and $z\in Z(J)$.\
It follows from this definition that the difference $\nabla-\nabla'$ between 2 connections on $M$ is a $Z(J)$-linear mapping of ${\mbox{Der}}(J)$ into the $Z(J)$-module of all the $J$-module endomorphisms of $M$.\
It also follows that $$R_{X,Y}=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$$ satisfies $$\left\{
 \begin{array}{l}
 R_{X,Y}(xm)=x R_{X,Y}(m)\\
 \\
 R_{zX,Y}(m)=z R_{X,Y}(m)
 \end{array}
 \right.
 \label{curv}$$ in other words that $R$ is a $Z(J)$-linear mapping of $\wedge^2_{Z(J)}{\mbox{Der}}(J)$ into the $Z(J)$-module of all the $J$-module endomorphism of $M$ which will be referred to as the *curvature* of $\nabla$.\
It is clear that if ${\mathfrak g}$ is a Lie subalgebra and a $Z(J)$-submodule of ${\mbox{Der}}(J)$, the restriction of ([\[covder\]](#covder){reference-type="ref" reference="covder"}) to ${\mathfrak g}$, i.e. for $X\in{\mathfrak g}$, makes sense and the corresponding notion will be referred to as a *derivation-based ${\mathfrak g}$-connection* on $M$.
