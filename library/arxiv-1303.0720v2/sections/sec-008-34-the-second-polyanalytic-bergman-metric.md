---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-008-34-the-second-polyanalytic-bergman-metric
section_title: "The second polyanalytic Bergman metric"
section_number: 3.4
pages: 6-6
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.98
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We turn to Bergman's second metric. The function $$L_q(z,z'):=\log\mathbf{E}_{\otimes2}[K_q](z,z';z,z')
\label{eq-Lfun1}$$ is basic to the analysis, where the expression on the right-hand side is as in [\[eq-bk4\]](#eq-bk4){reference-type="eqref" reference="eq-bk4"}. We think of $(z,\bar z')$ as holomorphic coordinates, and form the corresponding Bergman metric: $$\partial_z\bar\partial_{z}L_q(z,z')\vert\mathrm{d}z\vert^2
+\partial_z\partial_{z'}L_q(z,z')\mathrm{d}z\mathrm{d}z'+
\bar\partial_{z}\bar\partial_{z'}L_q(z,z') 
\mathrm{d}\bar z\mathrm{d}\bar z'+
\partial_{z'}\bar\partial_{z'}L_q(z,z')\vert\mathrm{d}z'\vert^2$$ Next, we write $z'=z+\epsilon$, so that $\mathrm{d}z'=\mathrm{d}z+\mathrm{d}\epsilon$; to simplify as much as possible, we restrict to $\mathrm{d}\epsilon=0$, so that $\mathrm{d}z'=\mathrm{d}z$. Then the above metric becomes $$(\varDelta_z+\varDelta_{z'})L_q(z,z')\vert\mathrm{d}z\vert^2
+2\mathop{\mathrm{Re}}[\partial_z\partial_{z'}L_q(z,z')(\mathrm{d}z)^2],$$ which after full implementation of the coordinate change becomes $$\begin{gathered}
\mathrm{d}s_{q,\omega,\epsilon}^{\text{\ding{175}}}(z)^2
:=(\varDelta_z+\varDelta_{z'})L_q(z,z')\vert\mathrm{d}z\vert^2
+2\mathop{\mathrm{Re}}[\partial_z\partial_{z'}L_q(z,z')(\mathrm{d}z)^2]\big|_{z'=:z+\epsilon}
\\
=(\varDelta_z+2\varDelta_{\epsilon}-\bar\partial_z\partial_\epsilon
-\partial_z\bar\partial_\epsilon)[L_q(z,z+\epsilon)]\vert\mathrm{d}z\vert^2
+2\mathop{\mathrm{Re}}\big\{(\partial_z\partial_{\epsilon}-
\partial_\epsilon^2)[L_q(z,z+\epsilon)](\mathrm{d}z)^2\big\}.
\label{eq-bpam2}
\end{gathered}$$ This gives us a metric parametrized by $\epsilon$, for $\epsilon$ close to $0$, which we may think of as Bergman's second polyanalytic metric. This metric [\[eq-bpam2\]](#eq-bpam2){reference-type="eqref" reference="eq-bpam2"} is, generally speaking, not isothermal. We note here that to a given $C^\infty$-smooth non-isothermal metric we may associate an appropriate quasiconformal mapping which maps the non-isothermal metric to an isothermal one.
