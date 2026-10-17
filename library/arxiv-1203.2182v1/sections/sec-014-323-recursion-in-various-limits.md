---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-014-323-recursion-in-various-limits
section_title: "Recursion in various limits"
section_number: 3.2.3
pages: 36-42
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.992
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
In order to understand better the refined recursion relation ([\[RefineRecursion\]](#RefineRecursion){reference-type="ref" reference="RefineRecursion"}), let us consider what happens in various special limits, when $t=-1$ or $q=\pm 1$. We begin with the unrefined limit $t=-1$, which is special for several reasons. First, a direct substitution $\boxed{t=-1}$ in ([\[RefineRecursion\]](#RefineRecursion){reference-type="ref" reference="RefineRecursion"}) gives rise to the following 3-term homogeneous relation $$\alpha_{(t=-1)} J_{n-1} \, + \, \beta_{(t=-1)} J_n \, + \, \gamma_{(t=-1)} J_{n+1} \; = \; 0 \,,    \label{RefineRecursiont1}$$ with the coefficients (rescaled by $q^2-q^{1-n}$ compared to ([\[A\]](#A){reference-type="ref" reference="A"})-([\[C\]](#C){reference-type="ref" reference="C"})) $$\begin{aligned}
\alpha_{(t=-1)} & = & \frac{q^{2 n} (q^n - q)}{q^{2 n} - q}, \\
\beta_{(t=-1)} & = & q \Big(1 + q^{-n} - q^n +
\frac{q - q^n}{q^{2 n} - q} - \frac{q^n - 1}{ q^{2 n+1} - 1}  \Big),  \\
\gamma_{(t=-1)} & = & \frac{q - q^{-n}}{1 - q^{2 n+1}}.
\end{aligned}$$ This is precisely the homogeneous relation found in [@Garoufalidis] by hand and obtained more systematically in the recent work [@Tudor; @abmodel] by quantizing $A(x,y)$.

Moreover, in the $t=-1$ limit, there is also an inhomogeneous 2-term relation, which does not exist for other values of $t$. To derive this inhomogeneous relation we again start from the ratios ([\[ratioA\]](#ratioA){reference-type="ref" reference="ratioA"})-([\[ratioC\]](#ratioC){reference-type="ref" reference="ratioC"}). The crucial point is that at $t=-1$ the factors $(1-q^{k+1})$ in the numerator and denominator cancel. As a result, equations ([\[ratioB\]](#ratioB){reference-type="ref" reference="ratioB"}) and ([\[ratioC\]](#ratioC){reference-type="ref" reference="ratioC"}) take the form $$\begin{aligned}
q^{n-1} q^{-k} J(n,k) & = & J(n,k) - q^{-n} J(n,k+1) \,, \\
q^{-k} J(n+1,k+1) & = & q^{n+2} (1 - q^n) J(n,k) \,,
\end{aligned}$$ and factors $q^{2k}$ do not appear.[^1] Moreover if we shift the indices $n$ and $k$ by one unit in the second equation, we can explicitly solve for the factor $q^{-k} P(n,k)$ to obtain a single relation $$J(n,k+1) \; = \; q^n J(n,k) - q^{3n-1} (1 - q^{n-1}) J(n-1,k-1) \,.$$ Performing the sum over $k$ and using the definition ([\[Pn-single\]](#Pn-single){reference-type="ref" reference="Pn-single"}), as well as taking care of the boundary terms, we get $$J_n = q^{n-1} \frac{1-q^{2n-1}}{1-q^n} - q^{3n-1} \frac{1-q^{n-1}}{1-q^n} J_{n-1}.   \label{trefoil2term}$$ This is the same 2-term inhomogeneous relation as presented in [@Garoufalidis]. In fact, the homogeneous relation ([\[RefineRecursiont1\]](#RefineRecursiont1){reference-type="ref" reference="RefineRecursiont1"}) also follows from ([\[trefoil2term\]](#trefoil2term){reference-type="ref" reference="trefoil2term"}): if we normalize ([\[trefoil2term\]](#trefoil2term){reference-type="ref" reference="trefoil2term"}) so that the inhomogeneous term is an $n$-independent constant, we get $${\rm const} \; = \; \delta_n J_n + \epsilon_n J_{n-1} \; = \; \delta_{n+1} J_{n+1} + \epsilon_{n+1} J_{n} \,,$$ or, equivalently, $$\epsilon_n J_{n-1} + (\delta_n - \epsilon_{n+1} ) J_n - \delta_{n+1} J_{n+1} \; = \; 0 \,.$$ It is not hard to check that this structure reproduces ([\[RefineRecursiont1\]](#RefineRecursiont1){reference-type="ref" reference="RefineRecursiont1"}), with $\alpha_{(t=-1)} \sim \epsilon_n$, $\beta_{(t=-1)} \sim (\delta_n - \epsilon_{n+1})$, and $\gamma_{(t=-1)} \sim - \delta_{n+1}$.

Other interesting limits of ([\[RefineRecursion\]](#RefineRecursion){reference-type="ref" reference="RefineRecursion"}) arise when $q$ takes special values. Thus, when $\boxed{q=1}$ the coefficients in ([\[A\]](#A){reference-type="ref" reference="A"})-([\[C\]](#C){reference-type="ref" reference="C"}) simplify and, up to an overall factor $1+t^3$, take the form $$\alpha_{(q=1)} = 0 \,,  \qquad   \beta_{(q=1)} = -(1+t^2+t^3) \,, \qquad  \gamma_{(q=1)} = 1 \,.$$ Vanishing of $\alpha_{(q=1)}$ means that the recursion reduces to the 2-term form: $$P_{n+1} \; = \; (1+t^2+t^3) P_n \,.$$ In fact, in the classical limit $q=1$, even the full-fledged superpolynomial [\[Superpolynomial_sym_refined\]](#Superpolynomial_sym_refined){reference-type="eqref" reference="Superpolynomial_sym_refined"}, without the specialization to $a=q^2$, enjoys a simple and elegant recursion relation, which for $(2,2p+1)$ torus knots looks like: $${\cal P}^{S^n} (T^{2,2p+1})

\; = \; a^p \left[ \frac{1 - t^{2p+2}}{1 - t^2} + a t^3 \frac{1 - t^{2p}}{1 - t^2} \right]  \; {\cal P}^{S^{n-1}} (T^{2,2p+1})

\,.$$

In the limit $\boxed{q=-1}$ there are also simplifications. However, the recursion [\[RefineRecursion\]](#RefineRecursion){reference-type="eqref" reference="RefineRecursion"} still involves 3 terms with $$\begin{aligned}
\alpha_{(q=-1)} & = & \big(1 + (-1)^n  \big)t^4,  \\
\beta_{(q=-1)} & = & (1+t^3)\big(-1+(-1)^nt^2 +t^3\big), \\
\gamma_{(q=-1)} & = & -1+(-1)^n t^3.
\end{aligned}$$

All these limits have a nice physical interpretation that follows from [\[theoryA\]](#theoryA){reference-type="eqref" reference="theoryA"} and will be discussed elsewhere. Basically, setting the parameters $q$ and $t$ to special values means that in the corresponding generating functions [\[ZrefdefP\]](#ZrefdefP){reference-type="eqref" reference="ZrefdefP"} -- [\[Zrefdefa\]](#Zrefdefa){reference-type="eqref" reference="Zrefdefa"} one ignores the dependence on either the spin $F$ or the D0-brane charge $P$.

## Refined $A$-polynomials and the refined "volume" $S_0 (u,t)$ {#sec:knotS0}

One next goal is to test the second new conjecture of the present paper -- namely, the refinement of the generalized volume conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a) -- in a large class of examples associated with $(2,2p+1)$ torus knots.

Specifically, in this section we derive the refined $A$-polynomials $A^{\text{ref}}(x,y;t)$ for $(2,2p+1)$ torus knots and analyze the refined "volume" $S_0 (u,t)$ that dominates the asymptotic behavior ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a), thereby verifying [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"}.

At a very practical level, the refined $A$-polynomials arise as the $q \to 1$ limit of $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$, as we explained earlier and illustrated in Figure [\[fig:AAAA\]](#fig:AAAA){reference-type="ref" reference="fig:AAAA"}. Therefore, if one knows the quantum operator $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$, say, as in the case of the unknot or the trefoil knot, then it is trivial to find its classical version, $A^{\text{ref}}(x,y;t)$. However, our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}) provides another way to look at the refined $A$-polynomial. Namely, according to [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"}, it determines the asymptotic behavior of the $n$-colored homological invariants $P_n (q,t)$ in the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"}. Our conjecture says that, in this limit, the homological invariants $P_n (q,t)$ exhibit exponential growth with the leading term $S_0(u,t)$, such that $$y = e^{S'_0(u,t)} \; = \; e^{\frac{d}{du} S_0(u,t)} \; = \; e^{x \frac{d}{dx} S_0(\log x,t)} \,.   \label{yS0prim}$$ This gives another way of expressing the dependence of $y$ on $x$, which is equivalent to the equation $A^{\text{ref}}(x,y;t)=0$. In other words, the leading order free energy $S_0(u,t)$ computed directly from the asymptotics of $P_n (q,t)$ must agree with the integral ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}) on an algebraic curve $A^{\text{ref}}(x,y;t) = 0$. In this section, we will test this equivalence and our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a). We also determine the refined $A$-polynomials even in those examples where the full quantum curve $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$ is not known at present!

In particular, for the unknot and for the trefoil knot, for which we already found $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$ in the previous section, we will show that their $q \to 1$ limits indeed agree with the refined $A$-polynomials computed from the asymptotics of the corresponding colored homological invariants. Furthermore, even for more general $(2,2p+1)$ torus knots, for which the full quantum $A$-polynomials are not known at present, we will find the refined $A$-polynomials by testing our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}). Impatient reader can skip directly to Table [\[table_A-poly4\]](#table_A-poly4){reference-type="ref" reference="table_A-poly4"}, where we list the explicit form of $A^{\text{ref}}_{T^{2,2p+1}} (x,y;t)$ for several small values of $p$. In section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"}, we will use analogous techniques to analyze the refined $A$-polynomials and asymptotic expansions in examples coming from refined BPS state counting.

### Refined $A$-polynomial and $S_0 (u,t)$ for the unknot

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

### Refined $A$-polynomial and $S_0 (u,t)$ for the trefoil

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

[^1]: Note that for general $t$ it is not possible to solve for combinations $q^k P(n,k)$ directly, which is why we had to sum over $k$ first using auxiliary $R_n$ and $S_n$, to get 3-term homogeneous relation.
