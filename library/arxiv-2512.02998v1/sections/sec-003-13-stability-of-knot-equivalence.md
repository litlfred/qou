---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-003-13-stability-of-knot-equivalence
section_title: "Stability of knot equivalence"
section_number: 1.3
pages: 3-4
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.914
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
As an immediate consequence of Theorem~\ref{thm:isomorphic} in combination with
part (iii) of Theorem~\ref{thm:gordon-luecke} we obtain a simple
sufficient geometric criterion for knot equivalence.
\begin{corollary}[Knot equivalence via local distortion]
\label{cor:equiv-knots}
Two tame knots $\g_i\in C^0(\R/\Z,\R^3)$ with local 
distortion 
 $\delta(\g_i(\R/\Z),r_{\g_i})<g_3$
at scales $r_{\g_i}>0$
for $i=1,2$, and
$\dist_{\HH}(\g_1(\R/\Z),\g_2(\R/\Z))$
$<\frac 14 \min\{r_{\g_1},r_{\g_2}\}$, are equivalent.
\end{corollary}

Notice that a small Hausdorff-distance, even an arbitrarily
small $L^\infty$-distance $\|\g_1-\g_2\|_{L^\infty}$
\emph{alone} does not guarantee knot equivalence:
One can insert small knotted arcs at any scale to produce highly complex
knots arbitrarily close to the round circle. Essential 
is the combination of controlled local
distortion at some scales and  
the Hausdorff-distance bounded in terms of these scales.
With Corollary \ref{cor:equiv-knots} we can prove 
the following stability of knot equivalence in the 
Lipschitz category.


\begin{corollary}[Lipschitz stability of knot equivalence]\label{cor:lipschitz-stability}
Let $\g:\R/\Z\to\R^3$ be an arclength parametrized tame 
knot with 
local distortion $\delta(\g(\R/\Z),r_\g)< g_3$
at scale $r_\g>0$. Then for all $h\in C^{0,1}(\R/\Z,\R^3)$
there exists $\epsilon_{\g,h}>0$ such that $\g_\epsilon:=\g+\epsilon h$ is
an immersed knot equivalent to $\g$ for all $|\epsilon| \le \epsilon_{\g,h}$.
\end{corollary}
Note that Lipschitz continuous curves are differentiable a.e., and we call such curves
\emph{immersed} if $v_\g:=\essinf_{u\in\R/\Z}|\g'(u)|>0$.

For $C^1$-knots $\g$ one has, of course, $\delta(\g(\R/\Z),r)\to 1 $ as $r\to 0$, so that
one finds a scale $r_\g$ sufficiently small so that $\g$ has 
local distortion strictly below $g_3$.
In fact, this observation implies a weaker version of Theorem~\ref{thm:C1-stability} where ambient isotopy is replaced by knot equivalence.
But we will prove here
that a fractional Sobolev regularity (below $C^1$) suffices, 
which leads to the following fractional stability result for knot equivalence.
\begin{corollary}[Fractional stability of knot equivalence]
\label{cor:fractional-stability}
For any arclength parametrized knot $\g\in W^{\frac32,2}(\R/\Z,\R^3)$ there exists
$\epsilon_\g>0$ such that every arclength parametrized
curve $\eta\in B_{\epsilon_\g}(\g)\subset
W^{\frac32,2}(\R/\Z,\R^3)$ is a knot equivalent to $\g$.
\end{corollary}
The preceding statement can be shown to hold true also
if $\g$ and
$\eta$ are only immersed and not necessarily arclength
parametrized, but we will not discuss the details here.
Open at this point, however, is if the bound on local 
distortion in Corollaries \ref{cor:equiv-knots} and 
\ref{cor:lipschitz-stability} already
implies tameness of the knots, or some improved regularity.
