---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-007-5-discussion
section_title: "Discussion"
section_number: 5
pages: 25-26
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.932
---
## Connection with $\beta = 2$ initial conditions

We have calculated exact formulas for the dynamical distribution function ([\[2.c\]](#2.c){reference-type="ref" reference="2.c"}) in the case of $\beta = 1$ and $\beta = 4$ initial conditions, with the final state corresponding to a $\beta = 2$ equilibrium. If in these formulas we take the limit $t_{X},
t_{Y} \rightarrow \infty$ with $t_{X} - t_{Y}$ fixed, then we would expect no memory of the initial state to be retained, but rather the distribution functions corresponding to a $\beta = 2$ initial condition (i.e. the equilibrium state) to result.

Consider first the hard edge. Inspection of ([\[3.20\'\]](#3.20'){reference-type="ref" reference="3.20'"}), ([\[m.2\]](#m.2){reference-type="ref" reference="m.2"}), ([\[m.3\]](#m.3){reference-type="ref" reference="m.3"}) and ([\[m.4\]](#m.4){reference-type="ref" reference="m.4"}) shows that in this limit $$\begin{aligned}
\lefteqn{S_{1}^{\rm{hard}}(X, Y; t_{X}, t_{Y}) \sim
S_{4}^{\rm{hard}}(X, Y,;t_{X}, t_{Y})} \nonumber \\
& &  \sim
S_{2}^{\rm{hard}}(X, Y,;t_{X}, t_{Y})
:= \frac{1}{4}\int_{0}^{1}J_{a}\left(\sqrt{uX}\right)
J_{a}\left(\sqrt{uY}\right)\, e^{-u(t_{X} - t_{Y})}
\,  du  \,  ,
\label{5.1} \\
\lefteqn{\tilde{S}_{1}^{\rm{hard}}(X, Y; t_{X}, t_{Y}) \sim
\tilde{S}_{4}^{\rm{hard}}(X, Y,;t_{X}, t_{Y})} \nonumber \\
& &  \sim
\tilde{S}_{2}^{\rm{hard}}(X, Y,;t_{X}, t_{Y})
:= -\frac{1}{4}\int_{1}^{\infty}
J_{a}\left(\sqrt{uX}\right)
J_{a}\left(\sqrt{uY}\right)\, e^{-u(t_{X} - t_{Y})}
\,  du   \,  ,
\label{5.2}
\end{aligned}$$ while from ([\[3.22\]](#3.22){reference-type="ref" reference="3.22"}), ([\[3.35\]](#3.35){reference-type="ref" reference="3.35"}), ([\[3.23\]](#3.23){reference-type="ref" reference="3.23"}) and ([\[3.38\]](#3.38){reference-type="ref" reference="3.38"}) we see that $$\begin{aligned}
& & e^{(t_{X} + t_{Y})}\, \tilde{I}_{1}^{\rm{hard}}(X, Y; t_{X}, t_{Y})
 \sim e^{(t_{X} + t_{Y})}\, \tilde{I}_{4}^{\rm{hard}}(X, Y; t_{X}, t_{Y})
\sim 0  \,  ,
\label{5.3} \\
& & e^{-(t_{X} + t_{Y})}\, {D}_{1}^{\rm{hard}}(X, Y; t_{X}, t_{Y})
 \sim e^{-(t_{X} + t_{Y})}\, {D}_{4}^{\rm{hard}}(X, Y; t_{X}, t_{Y})
\sim 0  \,   .
\label{5.4}
\end{aligned}$$ Substituting these values in ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) and then using ([\[2.1b\]](#2.1b){reference-type="ref" reference="2.1b"}), and the formula $$\rm{Pf}(ZX) = (\rm{det}(ZX))^{1/2},$$ we see by interchanges of particular rows and columns that $ZX$ is equivalent to a block matrix of the form $$\begin{aligned}
\left(\begin{array}{cc}
 0_{n+m} & A  \\
-A & 0_{n+m}  \end{array} \right) \, ,
\nonumber 
\end{aligned}$$ where $$\begin{aligned}
A  =  \left[  \begin{array}{cc}
\left[S_{2}^{\rm{hard}}\left(
X_{j}^{(1)}, X_{k}^{(1)}; t_{1}, t_{1}\right)\right]_{n \times n}
 & \left[\tilde{S}_{2}^{\rm{hard}}\left(
X_{j}^{(1)}, X_{k}^{(2)}; t_{1}, t_{2}\right)\right]_{n \times m}
 \\
\left[\tilde{S}_{2}^{\rm{hard}}\left(
X_{j}^{(2)}, X_{k}^{(1)}; t_{2}, t_{1}\right)\right]_{m \times n}
& \left[S_{2}^{\rm{hard}}\left(
X_{j}^{(2)}, X_{k}^{(2)}; t_{2}, t_{2}\right)\right]_{m \times m}
\end{array} \right]  \,    .
\label{5.5}
\end{aligned}$$ Thus the limiting form of the dynamical distribution is given by $$\begin{aligned}
\rho_{(n+m)}\left(x_{1}^{(1)}, \ldots , x_{n}^{(1)}; \tau_{1};
x_{1}^{(2)}, \ldots , x_{m}^{(2)}; \tau_{2} \right) = \rm{det} \,A \,  .
\label{5.6}
\end{aligned}$$

The analysis in the soft edge case is very similar. The formulas ([\[5.3\]](#5.3){reference-type="ref" reference="5.3"}) and ([\[5.4\]](#5.4){reference-type="ref" reference="5.4"}) again apply, as do the formulas ([\[5.1\]](#5.1){reference-type="ref" reference="5.1"}) and ([\[5.2\]](#5.2){reference-type="ref" reference="5.2"}) with $S_{2}^{\rm{hard}}$, $\tilde{S}_{2}^{\rm{hard}}$ replaced by $$\begin{aligned}
S_{2}^{\rm{soft}}(X, Y; t_{X}, t_{Y}) &:=&
\int_{0}^{\infty}{\rm Ai}(X+v){\rm Ai}(Y+v)e^{-v(t_{Y}-t_{X})}dv \,  ,
\label{5.7} \\
\tilde{S}_{2}^{\rm{soft}}(X, Y; t_{X}, t_{Y}) &:=&
-\int_{-\infty}^{0}{\rm Ai}(X+v){\rm Ai}(Y+v)e^{-v(t_{Y}-t_{X})}dv \,  .
\label{5.8}
\end{aligned}$$ We remark that in the case $n = m =1$, the resulting formula for $\rho_{(n+m)}$ implied by ([\[5.6\]](#5.6){reference-type="ref" reference="5.6"}) and ([\[5.5\]](#5.5){reference-type="ref" reference="5.5"}) in both the hard and soft edge theories agrees with that computed by Mâcedo [@Ma1; @Ma296].
