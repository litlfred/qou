---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-015-322-trefoil
section_title: "Trefoil"
section_number: 3.2.2
pages: 34-36
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.976
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
Our next task is to derive refined recursion relations for the trefoil. Similarly as in the unknot case, we will be able to determine these relations from the structure of the $sl(2)$ specialization $P_{n}(T^{2,3};q,t)$ of the colored superpolynomial. For general $(2,2p+1)$ torus knots, we found an explicit expression for this homological invariant in ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}), which for the present purpose of deriving recursion relations we write in the form[^1]

$$P_{n}(T^{2,3}; q,t) \; = \; \sum_{k=0}^{n-1} P(n,k) \,,    \label{Pn-single}$$ where each $P(n,k)$ has a product structure $$P(n,k) = q^{n-1+n k} t^{2k} \prod_{i=1}^k \frac{(1 - q^{n-i})(1 + q^i t)}{1 - q^i}.  \label{Pnk}$$ In particular $$P(n,0) = q^{n-1}, \qquad P(n,n) = 0.$$ Note that for $t=-1$ simplifications occur and only one set of products remains in ([\[Pnk\]](#Pnk){reference-type="ref" reference="Pnk"}).

To derive recursion relations let us write down the following ratios, which is immediate due to the product structure of $P(n,k)$: $$\begin{aligned}
\frac{P(n+1,k)}{P(n,k)} & = & q^{k+1} \frac{1-q^n}{1-q^{n-k}}, \label{ratioA}\\
\frac{P(n,k+1)}{P(n,k)} & = & q^{n} t^2 \frac{(1-q^{n-k-1})(1+q^{k+1}t)}{1-q^{k+1}}, \label{ratioB}  \\
\frac{P(n+1,k+1)}{P(n,k)} & = & q^{n+k+2} t^2 \frac{(1-q^n)(1+q^{k+1}t)}{1-q^{k+1}}.
  \label{ratioC}  
\end{aligned}$$ These equations are equivalent to the following ones (obtained by clearing the denominators): $$\begin{aligned}
q^k P(n+1,k) - q^n P(n+1,k) & = & (1-q^n) q^{2k+1} P(n,k),   \label{recA} \\
q^k P(n,k+1) - q^{n+k} t^2 (1 - q^n t) P(n,k) &  & \nonumber \\
= -q^{2n-1} t^2 P(n,k) &  + & q^{2k+1}\Big(P(n,k+1) + t^3 q^n P(n,k)  \Big), \label{recB} \\
P(n+1,k+1) - t^3 q^{n+2k+3} (1 - q^n) P(n,k) &  &  \nonumber \\
= q^{k+1} \Big(P(n+1,k+1) & + & t^2 q^{n+1}(1-q^n) P(n,k)  \Big).    \label{recC}
\end{aligned}$$ These are linear equations in $P(n,k)$ (possibly with shifted arguments $n$ or $k$). Therefore, ideally, we would like to perform the sum over $k$ as in ([\[Pn-single\]](#Pn-single){reference-type="ref" reference="Pn-single"}) to transform them into equations for various $P_n$ (possibly with shifted $n$'s). However such summation cannot be directly performed because of $k$-dependent factors $q^k$ and $q^{2k}$. Nonetheless, we can take these factors into account at the expense of introducing auxiliary quantities: $$R_n = \sum_{k=0}^{n-1} q^k P(n,k),   \quad \qquad S_n  = \sum_{k=0}^{n-1} q^{2k} P(n,k).    \label{RnSn}$$ Now resummation of ([\[recA\]](#recA){reference-type="ref" reference="recA"})-([\[recC\]](#recC){reference-type="ref" reference="recC"}) can be performed and the answer written in terms of $P_n$, $R_n$, and $S_n$. Note that because of shifts in $n$ we need to take care of some boundary terms arising in various cases for $k=0$ or $k=n$. However all such boundary terms ultimately cancel and we get the following system of equations: $$\begin{aligned}
R_{n+1} + a P_{n+1} & = & b S_n,   \label{recAbis} \\
c R_n + d P_n & = & e S_n, \label{recBbis} \\
P_{n+1} - R_{n+1} + f R_n & = & g S_n,   \label{recCbis}
\end{aligned}$$ where $$a = -q^n, \quad b = q(1-q^n), \quad c = q^{-1} - t^2q^n(1-q^n t),\quad d = t^2 q^{2n-1},$$ $$e = q^{-1} + t^3 q^{n+1},\quad f = -t^2 q^{n+2} (1-q^n), \quad g = t^3 q^{n+3} (1-q^n).$$ Now we can determine $S_n$ from the first equation and substitute to the remaining two equations. This gives a system of two equations, which allows to determine $R_n$ and $R_{n+1}$ in terms of $P_n$ and $P_{n+1}$: $$\begin{aligned}
R_n & = & \frac{-d(b+g) P_n + (1 + a) e P_{n+1}}{b c - e f + c g}, \\
R_{n+1}  & = & \frac{-b d f P_ n + (b c  + a e f - a c g) P_{n+1}}{b c - e f + c g}.
\end{aligned}$$ Finally we notice that $R_n$ is related to $R_{n+1}$ simply by a shift of $n$ by one unit. Therefore, shifting the second equation above and comparing with the first one we get a homogeneous, 3-term recursion relation $$\boxed{\phantom{\int^1}
\alpha P_{n-1} + \beta P_n + \gamma P_{n+1} \; = \; 0 \,,
\phantom{\int^1}}
\label{RefineRecursion}$$ where $$\begin{aligned}
\alpha & = & \frac{q^{3 n-1} (q^n - q) t^4}{(q + q^{2 n} t^3) (1 +
   q^{n+1} t^3)}, \label{A}  \\
\beta & = & -\frac{t^2}{q^{-2 n} + q t^3} -
\frac{ q - q^{n+1} t^2 + q^{4 n} t^6 +
  q^{2 n} t^2 (1 + t + q t)}{(q + q^{2 n} t^3) (1 + q^{n+1} t^3)},  \label{B}  \\
\gamma & = & \frac{1}{q + q^{2 n+2} t^3} .   \label{C}
\end{aligned}$$ We can also rewrite the above relation in the operator form ([\[VCquantref\]](#VCquantref){reference-type="ref" reference="VCquantref"}a): $$\widehat A^{\text{ref}} (\widehat x, \widehat y; q,t) P_n (T^{2,3};q,t) \; = \; 0 \,.$$

Here, as in [\[xyactionP\]](#xyactionP){reference-type="eqref" reference="xyactionP"}, $\widehat{y}$ acts as a shift operator $P_n \to P_{n+1}$ and $\widehat{x}$ acts by multiplication by $q^n$, so that $\widehat x$ and $\widehat y$ obey the commutation relation $\widehat{y} \widehat{x} = q \widehat{x}\widehat{y}$. Then, the relation ([\[RefineRecursion\]](#RefineRecursion){reference-type="ref" reference="RefineRecursion"}) can be expressed in terms of the refined quantum $A$-polynomial $$\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t) \; =  \; \alpha \widehat{y}^{-1} + \beta + \gamma\widehat{y} \,,   \label{trefoil-Aqt}$$ with $$\begin{aligned}
\alpha & = & \frac{x^3 (x - q) t^4}{q (q + x^2 t^3) (1 +
   x q t^3)} \,,   \\
\beta & = & -\frac{t^2 x^2}{1 + x^2 q t^3} -
\frac{ q - x q t^2 + x^{4} t^6 +
  x^{2} t^2 (1 + t + q t)}{(q + x^{2} t^3) (1 + x q t^3)} \,,    \\
\gamma & = & \frac{1}{q + x^2 q^{2} t^3} \,.
\end{aligned}$$ In what follows we analyse various limits of this relation. In particular, we study the classical limit $q=1$ and the associated asymptotic structure of the $sl_2$ colored polynomial, and generalize these results to other $(2,2p+1)$ torus knots. The classical refined $A$-polynomials which we find for other values of $p$ provide an important guidance in generalizing the full quantum relations ([\[trefoil-Aqt\]](#trefoil-Aqt){reference-type="ref" reference="trefoil-Aqt"}) to other torus knots.

[^1]: The equivalence between this expression and ([\[refined_SU(2)\]](#refined_SU(2)){reference-type="ref" reference="refined_SU(2)"}) can be easily verified to sufficiently large $n$. Plus, both expressions enjoy the structural properties discussed in [\[sec:homological\]](#sec:homological){reference-type="ref" reference="sec:homological"}.
