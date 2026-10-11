---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-008-52-connection-between-the-soft-and-hard-edges
section_title: "Connection between the soft and hard edges"
section_number: 5.2
pages: 26-27
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.943
---
For the hard edge distribution function of the Laguerre ensemble at $\beta = 2$ and $\tau = 0$, it is known that by taking the limit $a \rightarrow \infty$ and introducing new scaled coordinates, the distribution function of the soft edge of the Gaussian ensemble results [@Fo93]. Specifically, the new scaled variable $x$ is related to the scaled variable $X$ of the hard edge by $$\begin{aligned}
X = a^{2} - 2\, a\, (a/2)^{1/3} \, x
\label{5.9}
\end{aligned}$$ and the distribution functions are related by $$\begin{aligned}
& & \lim_{a \rightarrow \infty} \left(-2a(a/2)^{1/3}\right)^{n}
\rho_{(n)}^{\rm hard}\left(a^{2}-2a(a/2)^{1/3}x_{1}, \ldots ,
a^{2}-2a(a/2)^{1/3}x_{n} \right)
\nonumber \\
& & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad
 =  \rho_{(n)}^{\rm soft}\left(x_{1}, \ldots , x_{n}\right)\, .
\label{5.10}
\end{aligned}$$ As noted in [@Fo93; @BFP98] this property should persist for general $\beta$. Further, with appropriate scaling of $\tau$, the result would be expected to generalize to the dynamical distributions.

Let us first check this latter point for the dynamical distribution with a $\beta = 2$ initial condition ([\[5.6\]](#5.6){reference-type="ref" reference="5.6"}). For this purpose we require the asymptotic expansion [@Wa] $$\begin{aligned}
J_{a}(x) \sim \left(\frac{2}{x}\right)^{1/3}
{\rm Ai}\left(\frac{2^{1/3}(a-x)}{x^{1/3}}\right)
\label{5.11}
\end{aligned}$$ valid for $a$ and $x$ large such that the argument of the Airy function is of order unity. Changing variables $u = 1 - w(2/a)^{2/3}$ in the integrals of ([\[5.1\]](#5.1){reference-type="ref" reference="5.1"}) and ([\[5.2\]](#5.2){reference-type="ref" reference="5.2"}) and introducing the scaled coordinates ([\[5.9\]](#5.9){reference-type="ref" reference="5.9"}), application of ([\[5.11\]](#5.11){reference-type="ref" reference="5.11"}) shows $$\begin{aligned}
J_{a}\left(\sqrt{ux}\right) \sim \left(\frac{2}{a}\right)^{1/3} {\rm Ai}
(x + w) \, .
\label{5.11'}
\end{aligned}$$ Thus if we also scale $t$ according to $$\begin{aligned}
t_{X} \mapsto (a/2)^{2/3} \,  t_{x}
\label{5.12}
\end{aligned}$$ then we see that $$\begin{aligned}
& & \left(-2a(a/2)^{1/3}\right) S_{2}^{\rm hard}\left(a^{2} - 2a(a/2)^{1/3}x,
a^{2} - 2a(a/2)^{1/3}y; (a/2)^{2/3}t_{x}, (a/2)^{2/3}t_{y} \right)
\nonumber \\
& & \quad \quad \quad \quad \quad \quad \quad \quad \quad
 \sim  e^{-(a/2)^{2/3}(t_{x} - t_{y})} S_{2}^{\rm soft}(x, y; t_{x}, t_{y})\, ,
\nonumber \\
& & \left(-2a(a/2)^{1/3}\right) 
\tilde{S}_{2}^{\rm hard}\left(a^{2} - 2a(a/2)^{1/
3}x,
a^{2} - 2a(a/2)^{1/3}y; (a/2)^{2/3}t_{x}, (a/2)^{2/3}t_{y} \right)
\nonumber \\
& & \quad \quad \quad \quad \quad \quad \quad \quad \quad
 \sim    
e^{-(a/2)^{2/3}(t_{x} - t_{y})} S_{2}^{\rm soft}(x, y; t_{x}, t_{y})\, .
\nonumber
\end{aligned}$$ Since, as seen from ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}), the factors $e^{-(a/2)^{2/3}(t_{x} - t_{y})}$ do not affect the value of $\rho_{(n+m)}$, we thus have the dynamical extension of ([\[5.10\]](#5.10){reference-type="ref" reference="5.10"}), $$\begin{aligned}
\lim_{a \rightarrow \infty}\left(-2a(a/2)^{1/3}\right)^{n+m} 
\rho_{(n+m)}^{\rm hard}\Big(a^{2} - 2a(a/2)^{1/3}x_{1},  \ldots ,
a^{2} - 2a(a/2)^{1/3}x_{n}; (a/2)^{2/3}t_{x}; && \nonumber \\
\qquad \qquad  a^{2} - 2a(a/2)^{1/3}y_{1}, \ldots , 
a^{2} - 2a(a/2)^{1/3}y_{m}; (a/2)^{2/3}t_{y} \Big ) && \nonumber \\ 
\qquad \qquad  =  \rho_{(n+m)}^{\rm hard}(x_{1}, \ldots, x_{n}; t_{x};
y_{1}, \ldots , y_{m}; t_{y}) \, . && 
\label{5.13}
\end{aligned}$$

Consider next $\beta = 1$ initial conditions. Inspection of ([\[3.20\'\]](#3.20'){reference-type="ref" reference="3.20'"}), ([\[m.2\]](#m.2){reference-type="ref" reference="m.2"}), ([\[3.22\]](#3.22){reference-type="ref" reference="3.22"}) and ([\[3.23\]](#3.23){reference-type="ref" reference="3.23"}) shows that the analysis used above for $\beta = 2$ initial conditions again suffices to establish the connection formula. For example, consider the formula ([\[3.22\]](#3.22){reference-type="ref" reference="3.22"}) for $\tilde{I}_{1}^{\rm hard}$. For large $a$ we see that $$\begin{aligned}
\lefteqn{\tilde{I}_{1}^{\rm hard}(X, Y; t_{X}, t_{Y})}
\nonumber \\
& \sim & \frac{a^{2}}{4}
\int_{1}^{\infty} s^{-1 + a/2} J_{a}\left(\sqrt{sY}\right)
e^{-st_{Y}} \int_{s}^{\infty} \frac{e^{-ut_{X}}}{u}
J_{a}\left(\sqrt{uX}\right) du - (X \leftrightarrow Y)  .
\label{5.14}
\end{aligned}$$ Use of the asymptotic expansion ([\[5.11\'\]](#5.11'){reference-type="ref" reference="5.11'"}) ( after making the appropriate change of variables in the integrals) shows $$\begin{aligned}
& & \left(-2a(a/2)^{1/3}\right) 
\tilde{I}_{1}^{\rm hard}\left(a^{2} - 2a(a/2)^{1
/3}x,
a^{2} - 2a(a/2)^{1/3}y; (a/2)^{2/3}t_{x}, (a/2)^{2/3}t_{y} \right)
\nonumber \\
& & \quad \quad \quad \quad \quad \quad \quad \quad \quad
 \sim   e^{-(a/2)^{2/3}(t_{x} + t_{y})} 
\tilde{I}_{1}^{\rm soft}(x, y; t_{x}, t_
{y}) \,  .
\nonumber
\end{aligned}$$ Similar formulas hold connecting $S_{1}^{\rm hard}$, $\tilde{S}_{1}^{\rm hard}$ and $D_{1}^{\rm hard}$ to $S_{1}^{\rm soft}$, $\tilde{S}_{1}^{\rm soft}$ and $D_{1}^{\rm soft}$ respectively, thus showing the formula ([\[5.13\]](#5.13){reference-type="ref" reference="5.13"}) holds for $\beta = 1$ initial conditions. Repeating the analysis for $\beta = 4$ initial conditions leads to the same conclusion.
