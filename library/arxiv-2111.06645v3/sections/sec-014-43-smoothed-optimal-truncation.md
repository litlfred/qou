---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-014-43-smoothed-optimal-truncation
section_title: "Smoothed optimal truncation"
section_number: 4.3
pages: 25-27
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.4.3 label="sub.4.3"}

We already mentioned at the end of Section [\[sub.4.1\]](#sub.4.1){reference-type="ref" reference="sub.4.1"} that it would be natural to expect a third term in [\[FirstRQMC\]](#FirstRQMC){reference-type="eqref" reference="FirstRQMC"} involving the missing $\widehat\Phi$-function $\widehat\Phi^{(K,\sigma_2)}(h)$, and the same applies even more strikingly to the two knots discussed in Section [\[sub.4.2\]](#sub.4.2){reference-type="ref" reference="sub.4.2"}, where we were obliged to omit the $\sigma_2$-term in both [\[52WeakRQMC\]](#52WeakRQMC){reference-type="eqref" reference="52WeakRQMC"} and [\[237WeakRQMC\]](#237WeakRQMC){reference-type="eqref" reference="237WeakRQMC"} because it would have been absorbed in the error terms of the other $\widehat\Phi$'s and hence could not be seen numerically if these values were defined by naive optimal truncation. However, there is a more precise way of turning the divergent series $\Phi(h)=\Phi_\alpha^{\sigma}(h)$ into functions that are defined up to exponentially rather than merely polynomially small errors, but with a much better exponent than before, by replacing the naive optimal truncation $\Phi(h)^{{\rm opt}}$ by a *smoothed* version $\Phi(h)^{{\rm sm}}$. The details of the procedure to do this are somewhat complicated and play no role for the story we are telling here, so will be given in detail in a separate publication [@GZ:optimal] and described briefly in Section [\[sub.optimal\]](#sub.optimal){reference-type="ref" reference="sub.optimal"}, the only important point here being that the improvement is sufficiently good, at least for our three standard knots, that we can unambiguously identify the periodic coefficients of the missing $\widehat\Phi$-terms.

We start as usual with the knot $K=4_1$ and the series whose initial terms are given in [\[as41\]](#as41){reference-type="eqref" reference="as41"}. In Section [\[sub.4.1\]](#sub.4.1){reference-type="ref" reference="sub.4.1"}, we considered $X=100$, $h=\frac{2\pi {\rm i}}X$ and saw that the number  had an error of the order of $10^{-12}$, which was more than sufficient to identify its difference with unambiguously as $\widehat\Phi^{(\sigma_0)}(h)$ but not enough to see a possible contribution from the much smaller $\widehat\Phi^{(\sigma_2)}(h)$. If we replace optimal by smooth truncation, then the error in $\widehat\Phi(h)$ decreases from (approximately) $10^{-15}$ to $10^{-44}$ and the error in $\widehat\Phi^{(\sigma_0)}(h)$ from $10^{-15}$ to $10^{-42}$. We can therefore compute the difference of the left- and right-hand sides of [\[FirstRQMC\]](#FirstRQMC){reference-type="eqref" reference="FirstRQMC"} (for $X=100$, $\gamma=S$) to 42 digits, finding that it vanishes, and since the remaining $\widehat\Phi$-value $\widehat\Phi^{(\sigma_2)}(h)$ has the much larger order of $10^{-14}$, we see that this quantity, if it occurs at all, must have coefficient 0. But when we replace $X=100$ by $100\frac13$, we find that the difference no longer vanishes but instead is equal to $\widehat\Phi^{(\sigma_2)}\bigl(h\bigr)^{{\rm sm}}$ times $-1.732050807568877293527446341{\rm i}$, which coincides to this accuracy with $-\sqrt{-3}$. Doing the same for other large values of $X$ with small denominators and other $\gamma$, we find that [\[FirstRQMC\]](#FirstRQMC){reference-type="eqref" reference="FirstRQMC"} with all $\Phi$-values interpreted by smooth rather than optimal truncation can be improved to $$\label{41RQMC}
(cX+d)^{-3/2} J^{(4_1)}\left(\frac{aX+b}{cX+d}\right)
 \overset?\approx  \sum_{j=0}^2 Q^{(4_1)}_j(X)
\widehat\Phi^{(4_1,\sigma_j)}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right),$$ where, just as for the $(-2,3,7)$ pretzel knot, , and is a 1-periodic functions, the notations in each case being a shorthand for . The first few values of the periodic functions for $i=1$ and $2$ are given by

::: center
            Ord($q$)             $1$    2        3         4                    5                      6       
  ----------------------------- ----- ----- ----------- -------- ------------------------------- ------------- --
   $\mathcal{Q}^{(4_1)}_1(q)$    $1$   $5$     $13$       $27$           $44-4 q^2-4q^3$             $89$      
   $2\mathcal{Q}^{(4_1)}_2(q)$   $0$   $0$   $-2 - 4q$   $-14q$   $-15 - 30 q - 22 q^2 - 8 q^3$   $46 - 92 q$  
:::

Just as with the functions  and ($i=3,4,5,6$) found for the $5_2$ and $(-2,3,7)$ knots in the previous subsection, the function (whose values we found by the numerical procedure just outlined for all $x$ with denominators up to 200), multiplied by 2, turned out to always belong to $\mathbb Z[\mathbf{e}(x)]$ and to satisfy all of the necessary Ohtsuki-type congruences near 0 and $1/2$ required for it to be an element of the Habiro ring. In this case, following a tip by Campbell Wheeler, we were actually able to guess a formula that reproduced all of the numerically found values and (after multiplication by 2) was visibly in the Habiro ring, namely the following simple variant of equation [\[Hab41\]](#Hab41){reference-type="eqref" reference="Hab41"}: $$\label{Q0for41}
\mathcal{Q}^{(4_1)}_2(q)
= \frac12
\sum_{n=0}^\infty \big(q^{n+1}-q^{-n-1}\big) \big(q^{-1};q^{-1}\big)_n (q;q)_n .$$

When we recompute the examples of Section [\[sub.4.2\]](#sub.4.2){reference-type="ref" reference="sub.4.2"} with smooth rather than optimal truncation, the situation is exactly similar and we are able to add a term to the right-hand sides of both [\[52WeakRQMC\]](#52WeakRQMC){reference-type="eqref" reference="52WeakRQMC"} and [\[237WeakRQMC\]](#237WeakRQMC){reference-type="eqref" reference="237WeakRQMC"}, obtaining for both knots a conjectural approximate formula of the form $$\label{strongRQMC}
(cx+d)^{-3/2} J^{(K)}\left(\frac{aX+b}{cX+d}\right)  \overset?\approx
\sum_{\sigma\in\mathcal P_K}

Q^{(K)}_{\sigma}(X)
 \widehat\Phi^{(K,\sigma)}_{a/c}
\left(\frac{2\pi {\rm i}}{c(cX+d)}\right) ,$$ where and . In Sections [\[sub.qholo\]](#sub.qholo){reference-type="ref" reference="sub.qholo"} and [\[sec.arithmetic\]](#sec.arithmetic){reference-type="ref" reference="sec.arithmetic"}, we give more information about these numbers including a formula for as an element of the Habiro ring.
