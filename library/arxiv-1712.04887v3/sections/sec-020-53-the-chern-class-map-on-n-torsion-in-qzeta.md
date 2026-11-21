---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-020-53-the-chern-class-map-on-n-torsion-in-qzeta
section_title: "The Chern class map on n-torsion in Qzeta"
section_number: 5.3
pages: 28-31
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.958
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#subsection:speculative label="subsection:speculative"}

The following section contains a speculative digression and is not used elsewhere in the paper. We have proved that the maps $c_\zeta$ and $R_\zeta$ agree up to an invertible element of $\mathbf Z^{\times}_p$. To determine the value of this ratio, we need to compute the images of specific elements of the Bloch group. More specifically, as explained in the introduction, we need the two statements [\[CompRz\]](#CompRz){reference-type="eqref" reference="CompRz"} and [\[Compcz\]](#Compcz){reference-type="eqref" reference="Compcz"}. The first of these will be proved below (Theorem [\[thm.eta\]](#thm.eta){reference-type="ref" reference="thm.eta"}). Here we want to show that the second is not pure fancy. We shall give a heuristic justification of why the image of the Chern class map on $\eta_{\zeta}$ should be $\zeta$ --- at least up to a sign and a small power of $2$ in the exponent. We hope that the arguments of this section could, with care, be made into a precise argument. However, since the main conjecture of this section is somewhat orthogonal to the main purpose of this paper, and correctly proving everything would (at the very least) involve establishing that several diagrams relating the cohomology of $\mathrm{SL}_2$ and $\mathrm{PSL}_2$ and $\mathrm{GL}_2$ and $\mathrm{PGL}_2$ commute up to precise signs and factors of $2$, we content ourselves with a sketch, and enter the happy land where all diagrams commute.

The first subtle point is that the relation between $K_3(F)$ and $B(F)$ as established by Suslin is not an isomorphism. There is always an issue with $2$-torsion coming from the image of Milnor $K_3$. However, even for primes $p$ away from $2$, there is an exact sequence of Suslin ([@Suslintwo], Theorem 5.2; here $F$ is a number field so certainly infinite): $$0 \rightarrow  \mathrm{Tor}_1(\mu_F,\mu_F) \otimes \mathbf Z[1/2] \rightarrow K_3(F) 
\otimes \mathbf Z[1/2] \rightarrow B(F) \otimes \mathbf Z[1/2] \rightarrow 0,$$ and hence when $p | w_F = |\mu_F|$, the comparison map is not an isomorphism. (This is one of the headaches which required us to assume that $\zeta\notin F$ when computing the Chern class map on $B(F)$.) This issue arises in the following way. Over the field $\mathbf Q(\zeta)$, the Bott element provides a direct relationship between $K_1(F,\mathbf Z/n\mathbf Z)$ and $K_3(\mathbf Z,\mathbf Z/n\mathbf Z)$. This suggests we should push forward $\eta_{\zeta}$ to $\mathbf Q(\zeta)$ and compute the Chern class there. However, since in $B(\mathbf Q(\zeta))$, the class $\eta_{\zeta}$ may (and indeed does) become trivial, we instead consider $\eta_{\zeta}$ as an element of $K_3(\mathbf Q(\zeta))$, and then compute the Chern class map directly in $K$-theory.

By Theorem 4.10 of Dupont--Sah [@DS], the diagonal map $$x \rightarrow \left( \begin{matrix} x& 0 \\
0 & x^{-1} \end{matrix} \right)$$ induces an injection $$\mu_{\mathbf C} \simeq H_3(\mu_{\mathbf C},\mathbf Z) \rightarrow H_3(\mathrm{SL}_2(\mathbf C),\mathbf Z)$$ whose image is precisely the torsion subgroup. (We shall be more precise about this first isomorphism below.) Let $n$ be odd, and let $\zeta$ be a primitive $n$th root of unity, let $E = \mathbf Q(\zeta)$, and let $E^{+} = \mathbf Q(\zeta)^{+}$. If $\mu_E$ is the group of $n$th roots of unity, the map $\mu_E \rightarrow \mathrm{SL}_2(E)$ is conjugate to a map $$\mu_E \rightarrow \mathrm{SL}_2(E^{+})$$ as follows; send $\zeta$ to $$t = A \left( \begin{matrix} \zeta^{-1} & 0 \\
0 & \zeta \end{matrix} \right) A^{-1},
\quad \text{where} \  A =  \left(\begin{matrix} \zeta & \zeta^{-1} \\
1 & 1 \end{matrix} \right) \,.$$ The cohomology of $\mu_E$ with coefficients in $\mathbf Z/n\mathbf Z$ is (non-canonically) isomorphic to $\mathbf Z/n\mathbf Z$ in all degrees. More precisely, there is a canonical isomorphism $$H_1(\mu_E,\mathbf Z) = H_1(\mu_E,\mathbf Z/n\mathbf Z) = \mu_E \,,$$ we have $H_2(\mu_E,\mathbf Z) = 0$, and thus via the Bockstein map $H_2(\mu_E,\mathbf Z/n\mathbf Z) = H_1(\mu_E,\mathbf Z)[n] = \mu_E$. A choice of $\zeta$ leads to a choice of element $\beta \in H_2(\mu_E,\mathbf Z/n\mathbf Z)  
= \mu_E$, and hence to an isomorphism $$\mu_E  = H_1(\mu_E,\mathbf Z/n\mathbf Z)  \stackrel{* \beta}{\longrightarrow}  
H_3(\mu_E,\mathbf Z/n \mathbf Z) = H_3(\mu_E,\mathbf Z)$$ where the isomorphism is given by the Pontryagin product of $\mu_E$ with $\beta \in H_2(\mu_E,\mathbf Z/n\mathbf Z)$. These choices induce a map

$$\displaystyle{\mu_E \rightarrow  H_3(\mu_E,\mathbf Z) \rightarrow 
H_3(\mathrm{SL}_2(E^{+}),\mathbf Z) \rightarrow K_3(E^{+}) \rightarrow B(E^{+})}$$ which sends $\zeta$ to $\eta_{\zeta}$. That the image of $\zeta$ is $\eta_{\zeta}$ follows (for example) by §8.1 of [@Zickert]). Implicit in this statement also is that the Pontryagin product of $1 \in \mathbf Z/n\mathbf Z= H_1(\mathbf Z/n\mathbf Z,\mathbf Z/ n \mathbf Z)$ with $1 \in H_2(\mathbf Z/n\mathbf Z,\mathbf Z/n \mathbf Z)$ is exactly the class constructed in Proposition 3.25 of Parry and Sah [@PS]. (The maps above are only properly defined modulo $2$-torsion, since $\mu$ has odd order this issue can safely be ignored). Denote by $\eta_{E^{+}}$ the corresponding element in $K_3(E^{+})$.

The Chern class maps are compatible with base change, so to compute $c(\eta_{E^{+}})$ it suffices to compute $c(\eta_{E})$ where $\eta_E \in K_3(E)$ is the image of $\eta_{E^{+}}$ under the map $K_3(E^{+}) \rightarrow K_3(E)$. The Chern class map on $K_1(E) = E^{\times}$ canonically sends $\zeta \in E^{\times}$ to $\zeta$; we would like to directly connect the Chern class map on $K_1$ with the one on $K_3$ using the Bott element. The Bott element $\beta \in K_2(E;\mathbf Z/n\mathbf Z)$ is defined as follows. There is an isomorphism: $$\mu_E  = \ker \left(E^{\times} \stackrel{n}{\longrightarrow} E^{\times} \right) 
= \pi_2(E^{\times};\mathbf Z/n\mathbf Z) \,.$$ The element $\beta$ is defined as the image of $\zeta$ under the composition $$\pi_2(\mathrm{BGL}_1(E);\mathbf Z/n\mathbf Z) \rightarrow \pi_2(\mathrm{BGL}(E);\mathbf Z/n\mathbf Z)
\rightarrow \pi_2(\mathrm{BGL}(E)^{+};\mathbf Z/n\mathbf Z) = K_2(E;\mathbf Z/p\mathbf Z) \,.$$ The Bott element induces an isomorphism: $$\beta: K_1(E;\mathbf Z/n\mathbf Z) \rightarrow K_3(E;\mathbf Z/n\mathbf Z) \,.$$ Hence there is, given our choice of $\zeta \in E$, a canonically defined map: $$\begin{diagram}
K_3(E)&   & E^{\times}/E^{\times n} \\
\dTo & \ruTo^{c_{\zeta}} & \dEquals \\
K_3(E;\mathbf Z/n\mathbf Z) & & \\
\dEquals^{\beta^{-1}} & & \\
K_1(E,\mathbf Z/n\mathbf Z) & \rTo^{c} & E^{\times}/E^{\times n}
\end{diagram}$$ Here $c_{\zeta}$ is the composition of the Chern class map to $H^1(E,\mathbf Z/n\mathbf Z(2))$ which can be identified with $E^{\times}/E^{\times n}$ after a choice of $\zeta\in E$. Note that the definition of $\beta$ also requires a similar choice. Thus it makes sense to make the following:

::: assumption
[]{#assump label="assump"} The diagram above commutes.
:::

Using Assumption [\[assump\]](#assump){reference-type="ref" reference="assump"}, we would like to show that $c_{\zeta}(\eta_E) = \zeta$, and hence that $c_{\zeta}(\eta_{E^{+}})$ and thus $c_{\zeta}(\eta_{\zeta})$ are also both equal to $\zeta$. This will follow if, under the Bott element, the class $\eta_E$ corresponds to $\zeta\in K_1(E;\mathbf Z/n\mathbf Z)$. To prove this, one roughly has to show that the following square commutes: $$\begin{diagram}
\mu_E  = H_1(\mu_E,\mathbf Z/n\mathbf Z) & \rTo^{* \beta} & H_3(\mu_E,\mathbf Z/n \mathbf Z) \\
\dTo & & \dTo \\
E^{\times}/E^{\times n} =  K_1(E,\mathbf Z/n\mathbf Z) & \rTo^{\beta} & K_3(E;\mathbf Z/n\mathbf Z).
\end{diagram}$$ The top line comes from the Pontryagin product structure of $H_1(\mu_E,\mathbf Z/n\mathbf Z) = \mu_E$ with $$H_2(\mu_E,\mathbf Z/n\mathbf Z) = \ker(\mu_E 
\stackrel{[n]}{\longrightarrow} \mu_E) \,,$$ and the bottom line comes from Pontryagin product with the Bott element $\beta$ coming via the Bockstein map from $$\ker(E^{\times} \stackrel{[n]}{\longrightarrow} E^{\times}) \,.$$ We conveniently denote both maps by essentially the same letter in order to be more suggestive. One caveat is that the maps from $E^{\times} \rightarrow \mathrm{GL}_2(E)$ and $\mu_E \rightarrow \mathrm{SL}_2(E)$ considered above differ slightly in that $x$ is sent to $\left( \begin{matrix} x & 0 \\ 0 & 1 \end{matrix} \right)$ and $\left( \begin{matrix} x & 0 \\ 0 & x^{-1} \end{matrix} \right)$ respectively; since $n$ is odd such maps can be compared by comparing the cohomologies of $\mathrm{GL}$, $\mathrm{PGL}$, $\mathrm{SL}$, and $\mathrm{PSL}$ respectively; it is quite possible that such comparisons might require that the maps above include a factor of $2$ or $-1$ at some point.

The above discussion above makes the conjectured Equation [\[Compcz\]](#Compcz){reference-type="eqref" reference="Compcz"} plausible.
