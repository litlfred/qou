---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-003-04-the-dual-quantum-groupoid
section_title: "The dual quantum groupoid"
section_number: 0.4
pages: 7-7
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.955
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
The set of axioms of Definition [\[finite quantum groupoid\]](#finite quantum groupoid){reference-type="ref" reference="finite quantum groupoid"} is self-dual. This allows to define a natural quantum groupoid structure on the dual vector space $\widehat H=\mbox{Hom}_k(H,k)$ by "reversing the arrows": $$\begin{aligned}
& & \langle\,h,\,\phi\psi \,\rangle= \langle\,\Delta(h),\,\phi\otimes\psi \,\rangle, \\
& & \langle\,h\otimes g,\,{\widehat\Delta}(\phi) \,\rangle=  \langle\,hg,\, \phi\,\rangle, \\
& & \langle\,h,\, {\widehat S}(\phi) \,\rangle= \langle\,S(h),\,\phi \,\rangle,
\end{aligned}$$ for all $\phi,\psi \in \widehat H,\, h,g\in H$. The unit $\widehat 1$ of $\widehat H$ is $\varepsilon$ and counit $\widehat\varepsilon$ is $\phi \mapsto \langle\,\phi,\, 1\,\rangle$.

In what follows we will use the Sweedler arrows, writing for all $h\in H,\phi\in \widehat H$ : $$h\rightharpoonup\phi = \phi_{(1)} \langle\,h,\, \phi_{(2)}\,\rangle,
\qquad
\phi\leftharpoonup h =\langle\,h,\,\phi_{(1)} \,\rangle\phi_{(2)}.$$ for all $h\in H,\phi\in \widehat H$.

The counital subalgebras of $\widehat H$ are canonically anti-isomorphic to those of $H$. More precisely, the map $H_t \ni z \mapsto (z\rightharpoonup\varepsilon) \in {\widehat H}_s$ is an algebra isomorphism with the inverse given by $\chi \mapsto (1 \leftharpoonup\chi)$. Similarly, the map $H_s \ni z \mapsto (\varepsilon\leftharpoonup z) \in {\widehat H}_t$ is an algebra isomorphism ([@BNSz], 2.6).

::: remark
[]{#opposite groupoid label="opposite groupoid"} The opposite algebra $H^{op}$ is also a quantum groupoid with the same coalgebra structure and the antipode $S^{-1}$. Indeed, $$\begin{aligned}
S^{-1}(h_{(2)})h_{(1)}
&=& S^{-1}(\varepsilon_s(h)) = S^{-1}(1_{(1)}) \varepsilon(h1_{(2)}) \\
&=& S^{-1}(1_{(1)}) \varepsilon(h S^{-1}(1_{(2)})) =\varepsilon(h1_{(1)})1_{(2)}, \\
h_{(2)} S^{-1}(h_{(1)})
&=& S^{-1}(\varepsilon_t(h)) = \varepsilon(1_{(1)}h) S^{-1}(1_{(2)}) \\
&=& \varepsilon( S^{-1}(1_{(1)})h)S^{-1}(1_{(2)}) = 1_{(1)}\varepsilon(1_{(2)}h),\\
S^{-1}(h_{(3)}) h_{(2)} S^{-1}(h_{(1)}) 
&=& S^{-1}(h_{(1)} S(h_{(2)}) h_{(3)}) = S^{-1}(h). 
\end{aligned}$$ Similarly, the co-opposite coalgebra $H^{cop}$ (with the same algebra structure as $H$ and the antipode $S^{-1}$) and $(H^{op/cop}, S)$ are quantum groupoids.
:::
