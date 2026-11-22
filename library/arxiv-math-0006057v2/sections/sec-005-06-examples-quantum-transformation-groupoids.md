---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-005-06-examples-quantum-transformation-groupoids
section_title: "Examples : quantum transformation groupoids"
section_number: 0.6
pages: 8-8
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
It is known that any group action on a set (i.e., on a commutative algebra of functions) gives rise to a groupoid [@R]. Extending this construction, we associate a quantum groupoid with any action of a Hopf algebra on a separable algebra ("finite quantum space").

Namely, let $H$ be a Hopf algebra and $B$ be a separable (and, therefore, finite dimensional and semisimple [@P]) right $H$-module algebra with the action $b\otimes h \mapsto b\cdot h$, where $b\in B,h\in H$. Then $B^{op}$, the algebra opposite to $B$, becomes a left $H$-module algebra via $h\otimes a \mapsto 
h\cdot a = a\cdot S_H(h)$. One can form a *double crossed product algebra* $B^{op}{>\!\!\!\triangleleft}H{\triangleright\!\!\!<}B$ on the vector space $B^{op}\otimes H \otimes B$ with the multiplication $$(a\otimes h\otimes b)(a'\otimes h'\otimes b') =
(h_{(1)}\cdot a')a \otimes h_{(2)}{h'}_{(1)} \otimes (b\cdot {h'}_{(2)}) b',$$ for all $a,a'\in B^{op},\, b,b'\in B,$ and $h,h'\in H$.

Assume that $k$ is algebraically closed and let $e$ be the separability element of $B$ (note that $e$ is an idempotent when considered in $B\otimes B^{op}$). Let $\omega\in B^*$ be uniquely determined by $(\omega\otimes \mbox{id})e = (\mbox{id}\otimes \omega)e = 1$.

One can check that $\omega$ is the trace of the left regular representation of $B$ and verifies the following identities: $$\omega((h\cdot a)b) = \omega(a (b\cdot h)), \qquad
e^{(1)}\otimes (h\cdot e^{(2)})  = (e^{(1)}\cdot h) \otimes e^{(2)},$$ where $a\in B^{op}, b\in B$, and $e =e^{(1)}\otimes e^{(2)}$.

The structure of a quantum groupoid on $B^{op}{>\!\!\!\triangleleft}H{\triangleright\!\!\!<}B$ is given by $$\begin{aligned}
\Delta(a\otimes h\otimes b) &=& 
(a\otimes h_{(1)} \otimes e^{(1)})\otimes ((h_{(2)}\cdot e^{(2)})\otimes h_{(3)} \otimes b),\\
\varepsilon(a\otimes h\otimes b) &=& \omega(a(h\cdot b)) = \omega(a(b\cdot S(h))),\\
S(a\otimes h\otimes b) &=& b\otimes S(h)\otimes a.
\end{aligned}$$
