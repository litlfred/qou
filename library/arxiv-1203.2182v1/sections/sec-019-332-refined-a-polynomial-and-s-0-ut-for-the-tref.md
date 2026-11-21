---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-019-332-refined-a-polynomial-and-s-0-ut-for-the-tref
section_title: "Refined $A$-polynomial and $S_0 (u,t)$ for the trefoil"
section_number: 3.3.2
pages: 40-42
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.993
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
The next example is naturally the trefoil knot $T^{2,3} = {\bf 3}_1$. First, let us discuss the structure of its refined $A$-polynomial and the associated free energy $S_0(u,t)$ from the viewpoint of the quantum $A$-polynomial given in ([\[trefoil-Aqt\]](#trefoil-Aqt){reference-type="ref" reference="trefoil-Aqt"}). The refined $A$-polynomial can be determined by setting $q = 1$ in ([\[trefoil-Aqt\]](#trefoil-Aqt){reference-type="ref" reference="trefoil-Aqt"}): $$A_{T^{2,3}}^{\text{ref}}(x,y;t) = y^2 -\frac{1 - x t^2 + x^3 t^5 + x^4 t^6 + 2 x^2 t^2 (t+1)}{1
+ x t^3} y + \frac{(x-1) x^3 t^4}{1 + x t^3} \; = \; 0 \,.
\label{deformed_A-poly_trefoil}$$ We stress that for generic values of $t$ this form does not factorize, as the discriminant $$\Delta = \Big(\frac{1 + x^2 t^3}{1 + x t^3}\Big)^2 \big(1 - 2 t^2 x + (4 t^2 + 2 t^3 + t^4) x^2 + 2 t^5 x^3 + t^6 x^4\big)$$ is not a complete square. This means that the abelian branch -- represented by a factor $y-1$ in the classical, unrefined $A$-polynomial -- is "mixed" in together with the non-abelian branch for generic values of $t \ne -1$. Indeed, the value $t=-1$ is very special because the discriminant factorizes $$\Delta_{(t=-1)} \; = \; (1+x^3)^2 \,,$$ and, as a result, the $A$-polynomial also factorizes $$A^{\text{ref}}_{T^{2,3}}(x,y;t=-1) \; = \; (y-1) (y + x^3) \,.
\label{A31nonref}$$ In the latter expression, $y-1$ represents the abelian branch, while the "interesting" factor $y+x^3$ is what sometimes referred to as the reduced $A$-polynomial for the trefoil knot. We see that for generic values of $t$ such a factorization does not occur, and the "character variety" $A^{\text{ref}} (x,y;t)=0$ is irreducible, with only one component. For $t=-1$ it becomes reducible and splits into two (or, in general, several) components.

Once we found the refined curve, we can easily compute $S_0(u,t)=\int \log y \frac{dx}{x}$ using [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"}. For the trefoil knot there is no compact expression for this integral, but one can write it as a Taylor series in $(t+1)$. Namely, by solving the quadratic equation $A^{\text{ref}}_{T^{2,3}}(x,y;t)=0$, we find $$\begin{aligned}
y & = & \frac{1 - x t^2 + x^3 t^5 + x^4 t^6 + 2 x^2 t^2 (t+1)}{2(1 + x t^3)} - \frac{1}{2}\sqrt{\Delta} = \nonumber \\
& =& -x^3 + (t+1) x^3
\frac{(x-2) (3 x^2 -2x +2) }{(x-1) (1 - x + x^2)} + \mathcal{O}\big((t+1)^2\big)
\end{aligned}$$ The first term $-x^3$ corresponds to the non-abelian branch in ([\[A31nonref\]](#A31nonref){reference-type="ref" reference="A31nonref"}). Then, expanding the integrand $\log y \frac{dx}{x}$ in powers of $(t+1)$ and integrating term by term we find the following structure $$S_0(u,t) \; = \; S_0(u) + (t+1) S_0^{(1)}(u) + \sum_{k=2}^{\infty} (t+1)^k S_0^{(k)}(u),$$ where $S_0(u)$ is the ordinary Chern-Simons action of the flat $SL(2,{\mathbb C})$ connection on the trefoil knot complement: $$\begin{aligned}
S_0(u) & = & \frac{1}{6}\Big(\log (-x^3)\Big)^2, \nonumber\\
S_0^{(1)}(u) & = & \log\frac{(1-x)^3}{x^4 (1-x+x^2)}, \nonumber \\
S_0^{(2)}(u) & = & \frac{1}{2} S_0^{(1)}(u) + \frac{-8x^4 +9x^3 -12x^2 + 5x -3}{2( x-1 ) (1 -x +x^2)^2}, \nonumber \\
& \vdots & \nonumber\\
S_0^{(k)}(u) & = & \frac{1}{k} S_0^{(1)}(u) + \frac{1}{k!} \frac{R_k(x)}{( x-1 )^k (1 -x +x^2)^{2k-2}} \nonumber
\end{aligned}$$ In other words, the $k$-th order term $S_0^{(k)}(u)$ includes $\frac{1}{k} S_0^{(1)}(u)$ and also a rational function with $k! ( x-1 )^k (1 -x +x^2)^{2k}$ in the denominator and a certain polynomial $R_k(x)$ in the numerator. In particular, we can sum over all $S_0^{(1)}(u)$ contributions, so that $$S_0(u,t) \; = \; \frac{1}{6}\Big(\log (-x^3)\Big)^2 - \log(- t) \log\frac{(1-x)^3}{x^4 (1-x+x^2)} + R(x,t) \,,
\label{S0ut-trefoil}$$ where $R(x)$ is certain (complicated) function, whose $(t+1)^k$ coefficient is $\frac{1}{k!} \frac{R_k(x)}{( x-1 )^k (1 -x +x^2)^{2k}}$. We note that for $t=-1$ all $t$-dependent terms vanish. In the next subsection we will confirm that the same refined $A$-polynomial and the same $S_0(u,t)$ arise from the analysis of the asymptotic expansion of the colored superpolynomials ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}).

Let us point out that the curve [\[deformed_A-poly_trefoil\]](#deformed_A-poly_trefoil){reference-type="eqref" reference="deformed_A-poly_trefoil"} also factorizes in the $t=0$ limit: $$A^{\text{ref}}_{T^{2,3}}(x,y;t=0) \; = \; y(y-1) \,,$$ and there is an associated singularity in $S_0(u,t)$ when $t\to 0$. It would be interesting to understand this singularity better.
