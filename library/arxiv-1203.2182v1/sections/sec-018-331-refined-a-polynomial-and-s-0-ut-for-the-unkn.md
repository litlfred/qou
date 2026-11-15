---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-018-331-refined-a-polynomial-and-s-0-ut-for-the-unkn
section_title: "Refined $A$-polynomial and $S_0 (u,t)$ for the unknot"
section_number: 3.3.1
pages: 39-40
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.98
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
We start our analysis with the example of the unknot. This example is quite instructive: being relatively simple, it captures all essential ingredients which arise for more complicated knots. Recall, that we already determined the quantum refined curve in ([\[qAt-unknot\]](#qAt-unknot){reference-type="ref" reference="qAt-unknot"}), and its classical limit reads ([\[At-unknot\]](#At-unknot){reference-type="ref" reference="At-unknot"}): $$A^{\text{ref}}_{{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}}(x,y;t) \; = \;
(1 + t^3 x) ( - t^{-3})^{1/2} - (1 - x) y  = 0 \,.   \label{Atunknot2}$$ We would like to verify our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a) and to confirm that the same curve controls the asymptotic expansion of the $n$-colored homological invariants ([\[Pnunkot\]](#Pnunkot){reference-type="ref" reference="Pnunkot"}): $$\begin{aligned}
P_{n} ({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; q,t) & = &
 q^{-\frac{n-1}{2}} (-t^{-3})^{\frac{n-1}{2}} \frac{(-q^2 t^3;q)_{n-1}}{(q;q)_{n-1}} = \nonumber  \\
& = & (-t^{-3})^{\frac{n-1}{2}} q^{1/2} x^{-1/2} \frac{(-q^2 t^3;q)_{\infty}}{(-q^2 t^3 x;q)_{\infty}}
\frac{(x;q)_{\infty}}{(q;q)_{\infty}},
\end{aligned}$$ where we introduced $x=e^u=q^n$. Now we can use the expansion of the quantum dilogarithm function, see *e.g.* [@DGLZ; @Kirillov], $$\begin{aligned}
\log (x;q)_{\infty} \; = \; \frac{1}{\hbar}{\rm Li}_2(x)
+\frac{1}{2}\log(1-x)-\sum_{k=1}^{\infty}\frac{B_{2k}}{(2k)!}
\frac{U_{2k-1}(x)\hbar^{2k-1}}{(1-x)^{2k-1}} \,,
\label{q-dlog_exp}
\end{aligned}$$ where $q=e^{\hbar}$ and $U_k(x)$ is a polynomial of degree $k$ satisfying $$\begin{aligned}
U_k(x) \; = \; (x-x^2)U^{\prime}_{k-1}(x)+kxU_{k-1}(x) \,, \quad U_0=1 \,.
\end{aligned}$$ From this expansion we find the asymptotics $$P_n({\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}; q,t) = \exp \frac{1}{\hbar}\Big(\log x\, \log(-t^{-3})^{1/2} + \textrm{Li}_2(x) - \textrm{Li}_2(-t^3 x)  + \textrm{Li}_2(-t^3) - \frac{\pi^2}{6} + \mathcal{O}(\hbar) \Big),$$ so that we identify $$S_0(u,t) \; = \;  \log x\, \log(-t^{-3})^{1/2} + \textrm{Li}_2(x) - \textrm{Li}_2(-t^3 x)  + \textrm{Li}_2(-t^3) - \frac{\pi^2}{6} \,.
\label{S0unknot}$$ Computing the derivative of this result and using the relation ([\[yS0prim\]](#yS0prim){reference-type="ref" reference="yS0prim"}) we finally obtain $$y = e^{S'_0(u,t)} = (-t^{-3})^{1/2} \frac{1 + t^3 x}{1 - x},$$ which is clearly equivalent to the refined $A$-polynomial ([\[Atunknot2\]](#Atunknot2){reference-type="ref" reference="Atunknot2"}).

Let us also stress an interesting feature of the leading order free energy ([\[S0unknot\]](#S0unknot){reference-type="ref" reference="S0unknot"}). In the unrefined limit, $t=-1$, this free energy vanishes: $$S_0(u, t=-1) \; = \; 0 \,,$$ which is consistent with the form of the unrefined $A$-polynomial $A_{{\,\raisebox{-.08cm}{\includegraphics[width=.37cm]{unknot}}\,}}(x,y) = (1-x)(1-y)$ given in ([\[Aunknot1x1y\]](#Aunknot1x1y){reference-type="ref" reference="Aunknot1x1y"}). The factor $(1-y)$ in this classical, unrefined $A$-polynomial is a universal factor associated with abelian flat connections connections. Usually, it does not lead to an interesting contribution to the free energy, as the integral ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}) is trivial in this case. Therefore, our result ([\[S0unknot\]](#S0unknot){reference-type="ref" reference="S0unknot"}) could be interpreted as a contribution of a "refined" abelian flat connection, which becomes non-trivial once $t \ne -1$.

In what follows we use similar methods to analyze more interesting knots.
