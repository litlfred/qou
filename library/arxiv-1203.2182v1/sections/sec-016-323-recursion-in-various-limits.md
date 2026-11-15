---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-016-323-recursion-in-various-limits
section_title: "Recursion in various limits"
section_number: 3.2.3
pages: 36-38
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 1.0
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

[^1]: Note that for general $t$ it is not possible to solve for combinations $q^k P(n,k)$ directly, which is why we had to sum over $k$ first using auxiliary $R_n$ and $S_n$, to get 3-term homogeneous relation.
