---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-013-42-new-elements-of-the-habiro-ring
section_title: "New elements of the Habiro ring"
section_number: 4.2
pages: 23-25
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.4.2 label="sub.4.2"}

For the knot $K=5_2$ the set $\mathcal P_K$ has four elements: the Habiro one, the geometric and antigeometric ones, and the one corresponding to the real embedding of the cubic field $F_K=\mathbb Q(\xi)$. However, it has only three distinct real volumes: the geometric volume $\operatorname{Im} \mathbf V(\sigma_1)=\mathrm{Vol}(K)$ (with the numerical value $2.82812\dots$), the anti-geometric volume $\operatorname{Im} \mathbf V(\sigma_2)=-\mathrm{Vol}(K)$, and 0 for both ${\sigma=\sigma_0}$ and $\sigma=\sigma_3$, and consequently only three distinct orders of growth (one exponentially large, one exponentially small, and two of polynomial growth) of the corresponding $\widehat\Phi$-functions $\widehat\Phi^{(K,\sigma)}(h)$. (For simplicity we concentrate for the moment only on $\alpha=0$ and omit it from the notations.) This means that in the analogue of [\[FirstRQMC\]](#FirstRQMC){reference-type="eqref" reference="FirstRQMC"} there is only one term that is too small to be seen numerically when we replace the $\Phi$-series by their optimal truncation, so that here one can hope to see *three* distinct terms on the right. To test this, we take the same values ${N=100}$, $h=2\pi {\rm i}/N$ as before. Then $J^{(K)}\bigl(-\frac1N\bigr)$ is of the order of magnitude of $10^{22}$ and the difference is of the order of 1 just as before, but now when we divide this difference by $\widehat\Phi^{(K,\sigma_3)}\bigl(h\bigr)^{{\rm opt}}$ we obtain $2 + (1.22-5.23{\rm i})\cdot10^{-9}$, strongly suggesting that the limiting value of this difference as $X$ tends to infinity through integers exists and is equal to 2. Further experiments for non-integral values of $X$ and for other matrices $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)$ then lead to the new conjectural asymptotic statement $$\begin{aligned}
 (cX+d)^{-3/2} J^{(5_2)}\left(\frac{aX+b}{cX+d}\right) \overset?\approx{}&  J^{(5_2)}(X) \widehat\Phi^{(5_2,\sigma_1)}_{a/c}
 \left(\frac{2\pi {\rm i}}{c(cX+d)}\right)
 + \widehat\Phi^{(5_2,\sigma_0)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)\nonumber\\
& + Q^{(5_2)}(X) \widehat\Phi^{(5_2,\sigma_3)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)
 \label{52WeakRQMC}
\end{aligned}$$ for all $\gamma$ and all $X$ tending to infinity with bounded denominator, where $Q^{(5_2)}(x)$ (which is a temporary notation, only for this knot) is a function that is independent of $\gamma$ but that, unlike the constant coefficient 1 of the Habiro term $\widehat\Phi^{(K,\sigma_0)}(h)$, is not independent of $x$. Instead, $Q^{(5_2)}(x)$ is numerically found to be a periodic function of period 1 taking on simple algebraic values, the first few being $$\begin{gathered}
Q^{(5_2)}(0)=2,\qquad Q^{(5_2)}\big(\tfrac12\big)=8, \qquad
Q^{(5_2)}\bigl(\pm\tfrac13\bigr)=\frac{37\pm3\sqrt{-3}}2,
\qquad Q^{(5_2)}\bigl(\pm\tfrac14\bigr)=29\pm13{\rm i} .
\end{gathered}$$ (These values were found experimentally, using a Chinese-remainder-type interpolation, and the existence of such functions for all knots is not known.) Looking at more values (specifically, for all $x$ with denominator up to 200), we find that $Q^{(5_2)}(x)$ belongs to $\mathbb Z[\mathbf{e}(x)]$ and is Galois-invariant, so we can write it as $\mathcal{Q}^{(5_2)}(\mathbf{e}(x))$ where $\mathcal{Q}^{(5_2)}(q)$ is an element of $\mathbb Z[q]$ for every root of unity $q$, the first values being given by

::: center
           Ord($q$)           $1$    2       3         4                5                6      
  -------------------------- ----- ----- --------- ---------- --------------------- ----------- --
   $\mathcal{Q}^{(5_2)}(q)$   $2$   $8$   $20+3q$   $29+13q$   $69+27q+37q^2+2q^3$   $-46+69q$  
:::

This suggests that $q\mapsto\mathcal{Q}^{(5_2)}(q)$ might be an element of the Habiro ring $\mathcal H$ defined in [\[HabDef\]](#HabDef){reference-type="eqref" reference="HabDef"}, just as we know is the case for the coefficient $J^{(5_2)}(X)$ of the first $\widehat\Phi$-term in [\[52WeakRQMC\]](#52WeakRQMC){reference-type="eqref" reference="52WeakRQMC"}. This hypothesis can be tested numerically, because a well-known property of any element $\mathcal{Q}\in\mathcal H$ (originally observed by Ohtsuki [@Oh] in the context of the WRT-invariants of integer homology spheres even before the Habiro ring had been formalized) is that it satisfies an infinite number of congruences, the simplest of which is that $\mathcal{Q}(\zeta_p)$ for every prime number $p$ should be congruent modulo $p$ to , where $\pi_p=\zeta_p-1$ is the prime dividing $p$ in $\mathbb Q(\zeta_p)$ and where the $c_i$ are rational integers independent of $p$. This means in our case that the coefficient of $x^i$ in the polynomial $Q_p(1+x)\in\mathbb Z[x]$ should be congruent modulo $p$ to a *fixed* integer $c_i\in\mathbb Z$ for all primes $p>i+1$, and testing this for the numerically obtained polynomials $Q_n$, we find that it is indeed true, with $Q_p(\zeta_p)\equiv\text{Oh}(\pi_p)\!\pmod p$ for a power series $\text{Oh}(x)\in\mathbb Z[[x]]$ beginning $$\text{Oh}(x) = 2 - 3x + 8x^2 - 28x^3 + 120x^4 - 614x^5 + 3669x^6 - 25125x^7 + O\big(x^8\big) .$$

In fact, later we were able to guess an explicit formula, given below in Section [\[sub.qholo\]](#sub.qholo){reference-type="ref" reference="sub.qholo"}, that is manifestly in the Habiro ring and that reproduces the values of the polynomials $Q_n(q)$ and power series $\text{Oh}(x)$ as given above. But in many other cases, including the $(-2,3,7)$ knot discussed below, we cannot give even conjectural explicit formulas of the required kind, and in such cases it is important to be able to have a numerical test of the Habiro-ness of a periodic function.

Notice that the right-hand side of [\[52WeakRQMC\]](#52WeakRQMC){reference-type="eqref" reference="52WeakRQMC"} contains only three of the four completed power series $\widehat\Phi_{a/c}^{5_2,\sigma}$. Just as for the $4_1$ knot, this is not because the last one isn't really there, but because our approximate evaluations are not accurate enough at this point to detect the remaining term, which is exponentially small. We will correct this in Section [\[sub.4.3\]](#sub.4.3){reference-type="ref" reference="sub.4.3"}.

We were able to carry out similar calculations for the $(-2,3,7)$ pretzel knot, though the numerical analysis required here was much more arduous due to the larger number of series involved. Recall that this knot has rank 6, so that $\mathcal P_K$ contains seven elements. What makes the calculation feasible at all is that five of these seven elements are real (the Habiro one and the ones corresponding to the real embedding of $\mathbb Q(\xi)$ and to all three embeddings of $\mathbb Q(\eta)$), so that only one of the seven $\widehat\Phi$-functions is exponentially small and hence invisible with optimal truncation. (Actually, the fact that the other terms apart from the geometric one are of the order of 1 is not quite enough: one also has to verify by using the formulas of Section [\[sub.CoeffA\]](#sub.CoeffA){reference-type="ref" reference="sub.CoeffA"} and the numerical values of the complex volumes $v(K,\sigma_i)$ that the absolute error made in calculating the exponentially large dominant term $\widehat\Phi^{(K,\sigma_1)}(h)$ using optimal truncation is exponentially small.) We find a formula exactly analogous to [\[52WeakRQMC\]](#52WeakRQMC){reference-type="eqref" reference="52WeakRQMC"}, but now with six terms on the right, namely $$\label{237WeakRQMC}
(cX+d)^{-3/2} J^{(-2,3,7)}\left(\frac{aX+b}{cX+d}\right)  \overset?\approx
\sum_{\substack{0\le j\le 6\\j\ne2}}
Q^{(-2,3,7)}_j(X)
\widehat\Phi^{((-2,3,7),\sigma_j)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right) ,$$ where $j=2$ is omitted for the same reason as in [\[52WeakRQMC\]](#52WeakRQMC){reference-type="eqref" reference="52WeakRQMC"} (viz., that the corresponding term is too small to see at this stage) and where , and , and the four new periodic functions take values in $\mathbb Z[\mathbf{e}(x)]$ just as before, the first values (for $j\ne0,2$) being

::: center
             Ord($q$)                    $1$                 2                      3                 4                     5                     6        
  ------------------------------- ----------------- -------------------- ----------------------- ------------ ----------------------------- -------------- --
   $\mathcal{Q}^{(-2,3,7)}_1(q)$   $\hphantom{-}1$    $\hphantom{-1}1$          $-5+6 q$           $17-8 q$      $-21-27 q-5 q^2+4 q^3$      $-107+108 q$  
   $\mathcal{Q}^{(-2,3,7)}_3(q)$        $-4$               $-12$               $-15 - 10q$        $-16 - 2q$   $-36 - 20q - 29q^2 - 24q^3$    $23 + 14q$   
   $\mathcal{Q}^{(-2,3,7)}_4(q)$   $\hphantom{-}2$         $-10$               $-16 - 12q$          $-46q$     $-8 - 44q - 38q^2 - 48q^3$    $116 - 24q$   
   $\mathcal{Q}^{(-2,3,7)}_5(q)$        $-2$         $\hphantom{1}{-}6$        $-14 - 6q$         $8 - 10q$       $32q - 4q^2 - 10q^3$       $-82 + 122q$  
   $\mathcal{Q}^{(-2,3,7)}_6(q)$   $\hphantom{-}2$    $\hphantom{-1}2$    $\hphantom{-1}4 - 8q$   $10 - 12q$   $-4 - 36q - 44q^2 - 34q^3$    $136 - 16q$   
:::

Just as with the $5_2$ knot, we can verify the Ohtsuki property for these functions to a large number of terms and thus convince ourselves that each one belongs to the Habiro ring, even though in this case we do not know an explicit formula that makes this property manifest.
