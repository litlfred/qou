---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic fields"
section_id: sec-005-51-yang-mills-potentials-of-a-vacuum-field-with
section_title: "Yang-Mills potentials of a vacuum field with non-vanishing winding number"
section_number: 5.1
pages: 7-8
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.97
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magnetic ﬁelds is presented."
---
An $SU(2)$ Yang-Mills vacuum field is now constructed on a time slice $\reals^3$ of $\reals^4$ using the mapping $g: \reals^3 \rightarrow SU(2)$ (see e.g. Frankel 1997, Itzykson and Zuber 1980) $$g(\bx) \,=\, \text{exp}\left[\frac{i\pi \; x^j \sigma_j}
                          {\sqrt{||\bx||^2 + \lambda^2}}\right].
                        \label{g-original}$$ Interpreted as a gauge transformation of an $SU(2)$ classical vacuum, i.e. with vanishing connection $\omega = 0$, $g(\bx)$ gives rise to the pure gauge connection $$\omega = g^{-1}(\bx)\d g(\bx),\label{pure-gauge-omega}$$ and the Yang-Mills potential one-form $A = \frac{i}{q}\omega$ reads $$A^j \sigma_j = \frac{i}{q}g^{-1}(\bx)\d g(\bx).
         \label{pure-gauge-omega-A}$$ At this point we want to remark that the vacuum winding number of $\omega$, which is defined to be the degree of the map $g$, is $W(g)=1$. An important consequence of this non-trivial winding number will be a non-trivial value of the invariant $H^{(3)}$, as can be seen in equations ([\[H-3-in-example\]](#H-3-in-example){reference-type="ref" reference="H-3-in-example"}) and ([\[H-3-and-W\]](#H-3-and-W){reference-type="ref" reference="H-3-and-W"}) below.

In order to explicitly calculate the one-form potential $A$ given by the last expression we use that $g(\bx)$, as an element of $SU(2)$, has the form $$\begin{aligned}
   g(\bx) = \exp\left(\frac{1}{2i}\sigma_j n^j \right)
          = \cos\left({\frac{f}{2}}\right) 
                  -i \sigma_j \hat{n}^j \sin\left({\frac{f}{2}}\right),
                  \label{g-in-exp-form}
\end{aligned}$$ where $\bn = f {\hat\bn}$ and where $\hat{\bn}$ is a unit vector in $\reals^3$ with coordinate components $\hat{n}^j = x^j/||\bx||$. A comparison with ([\[g-original\]](#g-original){reference-type="ref" reference="g-original"}) shows $$\begin{aligned}
   f &= - \frac{2 \pi \,||\bx||}{\sqrt{||\bx||^2 + \lambda^2}}. \label{definition-f}
\end{aligned}$$ Substituting ([\[g-in-exp-form\]](#g-in-exp-form){reference-type="ref" reference="g-in-exp-form"}) into ([\[pure-gauge-omega-A\]](#pure-gauge-omega-A){reference-type="ref" reference="pure-gauge-omega-A"}) we obtain after some calculation $$A^\indi =  \frac{1}{2q}\left[
               \hat{n}^\indi\,\d f + \d \hat{n}^\indi \,\sin{f} 
               +
               \epsilon_{\indi\indj\indk}\,\hat{n}^\indj\,\d\hat{n}^\indk 
               (\cos{f}-1)\right]. \label{Yang-Mills-potential-components}$$
