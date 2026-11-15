---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-017-5-the-matrix-valued-cocycle-associated-to-a-knot
section_title: "The matrix-valued cocycle associated to a knot"
section_number: 5
pages: 30-31
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.993
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sec.Matrix label="sec.Matrix"}

Let us define, for a fixed knot $K$ (suppressed from the notation as usual), matrix $\gamma\in\mathrm{SL}_2(\mathbb Z)$ and number $x\in\mathbb Q\smallsetminus\big\{\gamma^{-1}(\infty)\big\}$, an $(r+1)\times (r+1)$ matrix $W_\gamma(x)$ by $$\label{Wdef}
W_\gamma(x) = \mathbf{J}(\gamma x)^{-1} \widetilde{\mathbf{j}}_\gamma(x)  \mathbf{J}(x)  ,$$ where $\widetilde{\mathbf{j}}$ is the automorphy factor defined in [\[autofactor\]](#autofactor){reference-type="eqref" reference="autofactor"}. (This formula makes sense because the matrix $\mathbf{J}$ is conjecturally invertible, and even unimodular, as discussed in [\[Orthogonality1\]](#Orthogonality1){reference-type="eqref" reference="Orthogonality1"} below.) This function has remarkable properties. On the one hand, the refined quantum modularity conjecture as presented above can now be rewritten as the asymptotic statement $$\label{WRQMC}
W_\gamma(X) \approx \mathbf{\widehat\Phi}_{a/c}{\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)}^{^{-1}}$$ for $X\in\mathbb Q$ tending to infinity with bounded denominator. In particular, unlike the completely discontinuous function $\mathbf{J}(x)$ in terms of which it is defined, $W_\gamma(X)$ has an asymptotic behavior at infinity that depends only on $X$ as a real number and not on its numerator and denominator separately, and in Section [\[sub.lift\]](#sub.lift){reference-type="ref" reference="sub.lift"} we will present very strong evidence that this is true not only asymptotically at infinity, but also for finite values of the argument, so that $W_\gamma(x)$ becomes a smooth (and in fact real analytic) function of its argument away from the singularity at ${x=\gamma^{-1}(\infty)}$. On the other hand, the cocycle property [\[jcoc\]](#jcoc){reference-type="eqref" reference="jcoc"} of $\widetilde{\mathbf{j}}$ immediately implies that the function $\gamma\mapsto W_\gamma(\cdot)$ is a cocycle for the group $\mathrm{PSL}_2(\mathbb Z)$ acting on the multiplicative group of almost-everywhere-defined invertible matrix-valued functions on $\mathbb P^1(\mathbb Q)$, meaning that it satisfies $$\begin{gathered}
\label{cocycle}
W_{\gamma\gamma'}(x) = W_\gamma(\gamma' x)  W_{\gamma'}(x)
\end{gathered}$$ for all $\gamma$ and $\gamma'$ in $\mathrm{PSL}_2(\mathbb Z)$. But this cocycle property then immediately extends by continuity to imply that $W_\gamma$ on $\mathbb R$ is also a $\mathrm{PSL}_2(\mathbb Z)$-cocycle, but now in the space of piecewise smooth matrix-valued functions on $\mathbb P^1(\mathbb R)$. We can then use the smoothness to define a canonical lift of each of the formal power series to an actual function of $h$, simply by requiring [\[WRQMC\]](#WRQMC){reference-type="eqref" reference="WRQMC"} to be an exact rather than merely an asymptotic equality.

These various properties will be described in detail in this section. The first subsection treats the elementary properties (behavior under complex conjugation, determinant, and inverse) of the matrices $\mathbf{J}(x)$ and $W_\gamma(x)$. The discussion of the smoothness properties and the lifting of the perturbative series to well-defined functions of $h$ will be given in Section [\[sub.lift\]](#sub.lift){reference-type="ref" reference="sub.lift"}, while the brief final subsection treats the expected equality between the cocycle $W_\gamma(x)$ and the cocycle constructed in the companion paper [@GZ:qseries] using state integrals, which gives the real explanation for its smoothness and even analyticity.
