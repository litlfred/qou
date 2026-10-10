---
doc_id: arxiv-math-0403224v1
doc_title: "Difference equation of the colored Jones polynomial for torus knot"
section_id: sec-005-3-a-p-olynomial
section_title: "A-P olynomial"
section_number: 3
pages: 4-6
source_pdf: 0403224v1.pdf
source_sha256: c25ccba77da375ad
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.544
doc_brief: "Difference equation of the colored Jones polynomial for torus knot — We prove that the N-colored Jones polynomial for the torus knot Ts, t satisﬁes the second order diﬀerence equation, which reduces"
---
In Ref.  the "AJ conjecture" is proposed; the *homogeneous* difference equation of the colored Jones polynomial $J_\mathcal{K}(N)$ for knot $\mathcal{K}$ gives the A-polynomial $A_\mathcal{K}(L,M)$ for knot $\mathcal{K}$. More precisely we rewrite the difference equation of the colored Jones polynomial, $\sum_{k\geq 0} a_k \, J_{\mathcal{K}}(N+k)=0$, into a form, $\mathcal{A}_\mathcal{K}(E,Q;q) \, J_\mathcal{K}(N)
\equiv
\sum_{k\geq 0}   a_k(Q,q)  \, E^k
\, J_{\mathcal{K}}(N)=0$, where the operators $Q$ and $E$ act on $J_\mathcal{K}(N)$ as $$\begin{align*}
  E \, J_\mathcal{K}(N)
  & = J_\mathcal{K}(N+1)
  \\[2mm]
  Q \, J_\mathcal{K}(N)
  & = q^N \, J_\mathcal{K}(N)
\end{align*}$$ Then a claim of Ref.  is that the A-polynomial $A_\mathcal{K}(L,M)$ coincides with $$\begin{equation}
  \label{AJ_identity}
  A_\mathcal{K}(L,M)
  =
  \mathcal{A}_\mathcal{K}(L,M^2; q=1)
\end{equation}$$ This AJ conjecture was checked with a help of `Mathematica` package for trefoil, figure-eight knots [@SGarou03b], and for $5_2$, $6_1$ knots [@TTakata04a].

For our case of the torus knot $\mathcal{T}_{s,t}$, we can easily check that applying above procedure the difference equations [\[difference_Jones\]](#difference_Jones){reference-type="eqref" reference="difference_Jones"} and [\[torus_difference\]](#torus_difference){reference-type="eqref" reference="torus_difference"} reproduce the A-polynomial for the torus knots given in Ref.  (see also Refs. ); $$\begin{equation*}
  A_{\mathcal{T}_{s,t}}(L, M)
  =
  \begin{cases}
    (L-1) \, (- 1 + L^2 \, M^{2 s t} ) 
    &
    \text{for $s,t>2$}
    \\[2mm]

    (L-1 ) \, ( 1 + L \,  M^{2(2m+1)} ) 
    &
    \text{for $(s,t)=(2,2m+1)$}
  \end{cases}
\end{equation*}$$

We can thus conclude that

::: theorem
[]{#thm:AJ_torus label="thm:AJ_torus"} AJ conjecture [\[AJ_identity\]](#AJ_identity){reference-type="eqref" reference="AJ_identity"} proposed in Ref.  is true for the torus knots $\mathcal{K}=\mathcal{T}_{s,t}$.
:::
