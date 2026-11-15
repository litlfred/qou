---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-037-91-algebraic-number-theory-aspects
section_title: "Algebraic number theory aspects"
section_number: 9.1
pages: 63-65
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.996
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.field label="sub.field"}

A detailed study of the power series (or more generally ) reveals several interesting algebraic number theoretical aspects, especially concerning the field of definition, transformation under the action of the Galois group, and above all the appearance of non-trivial algebraic units.

We begin by looking in more detail at the series because this example is quite illuminating. The first few terms of the series were given in [@Za:QMF p. 670], as $$\begin{aligned}
\Phi^{(4_1,\sigma_1)}_{a/5}(h)
={}&\sqrt[4]3\sqrt[10]{E^{(a)}}
\big(\bigl(2-E^{(a)}_1+E^{(a)}_2+2E^{(a)}_3\bigr)\nonumber \\ &
+ \frac{2678-943E^{(a)}_1+1831E^{(a)}_2+2990E^{(a)}_3}{2^3 3^2 5^2
\sqrt{-3}} h +\cdots\bigg) ,\label{at5}
\end{aligned}$$ where $E^{(a)}_k=2\cos\bigl(\frac{2\pi(6a-5)k}{15}\bigr)$ and $E^{(a)}=E^{(a)}_2/\bigl(E^{(a)}_1\bigr)^3E^{(a)}_3$, except that the formula was given there in terms of $\log\Phi$, which introduced spurious denominators in all terms of the expansion. Actually, this is one of the first insights from the numerical calculations: earlier papers had always worked with the logarithm, which is what one sees if one does a Feynman diagram expansion and looks at the contribution of connected graphs only, but (as in many other combinatorial problems) one gets much simpler numbers by looking at the exponentiated sum, corresponding to summing over all graphs rather than just the connected ones. In the case at hand, this meant that the coefficients of $h$ and $h^2$ in [@Za:QMF] contained mysterious powers of the prime $$\pi_{29}^{(a)} = 2-E^{(a)}_1+E^{(a)}_2+2E^{(a)}_3$$ of $\mathbb Q\bigl(\cos\bigl(\frac{2\pi}{15}\bigr)\bigr)$, which simply disappear as soon as one goes from the logarithm of the series to the series itself. But the few terms of given in [\[at5\]](#at5){reference-type="eqref" reference="at5"} also suffice to illustrate several other key arithmetic points:

-   The most striking feature of [\[at5\]](#at5){reference-type="eqref" reference="at5"} is the appearance of the 10th root of the algebraic unit $E^{(a)}$ as a prefactor. From this and the corresponding numbers found for other values of $\alpha$ and for other knots we were led to conjecture the existence of algebraic units in cyclotomic extensions of any number field determined by elements of the Bloch group of this field, a prediction that was then confirmed in the joint paper [@CGZ] with Frank Calegari.

-   The case of the $4_1$ knot has the somewhat misleading special property that the Kashaev invariant [\[J0for41\]](#J0for41){reference-type="eqref" reference="J0for41"} is always positive, so that we seem to be seeing elements in the real part ${\mathbb Q\bigl(\cos\bigl(\frac{2\pi}{15}\bigr)\bigr)}$ of the cyclotomic extension $F(\zeta_5)=\mathbb Q(\zeta_{15})$ of the trace field $F=F_{4_1}=\mathbb Q\big(\sqrt{-3}\big)$ rather than in this cyclotomic extension itself. In particular, as was not observed in [@Za:QMF], the unit is, up to sign, the *square* of an element of $F(\zeta_5)$, so that its 10 root is, up to a root of unity, in fact a fifth root of a unit in this larger field. Specifically, we have $$\sqrt{-E^{(a)}}=\big(\zeta_{15}^{(a)}- \big(\zeta_{15}^{(a)}\big)^{-1}\big) E^{(a)}_2/E^{(a)}_1,$$ permitting us to rewrite [\[at5\]](#at5){reference-type="eqref" reference="at5"} in the form [\[as41at5\]](#as41at5){reference-type="eqref" reference="as41at5"} given in Section [\[sec.QMCK\]](#sec.QMCK){reference-type="ref" reference="sec.QMCK"}. This, too, turned out to be true for the general case studied in [@CGZ], where one associates to a number field $F$ and an element of its Bloch group the $c$-th root of a unit (or at least $S$-unit for a finite set of primes $S$ independent of $c$) in $F(\zeta)$ for every primitive $c$-th root of unity $\zeta$, and not a $(2c)$-th root. This unit, for $F=F_\sigma$ and $\zeta=\mathbf{e}(\alpha)$, is expected to appear as a prefactor in  for every $K$, $\sigma$, and $\alpha$.

-   Apart from the unit prefactor (which equals in the notation of [\[as41at5\]](#as41at5){reference-type="eqref" reference="as41at5"}), there is a further prefactor $3^{1/4}$ that coincides with the torsion up to a root of unity and an element of $F_{4_1}$.

-   After we remove these factors, the remaining power series has coefficients in the cyclotomic extension $F(\zeta_5)$ of the trace field.

-   The denominators of this remaining power series, when we calculate it to many more terms using the methods described in Section [\[sub.comp2\]](#sub.comp2){reference-type="ref" reference="sub.comp2"}, have powers of $3$ (the ramified prime already occurring in (c)) and $D_n$, where $$\label{Dn}
    D_n = 2^{3n + v_2(n!)} \prod_{\substack{\text{$p$ prime} \\ p>2}}
     p^{ \sum_{i\ge0}[n/p^i(p-2)]} .$$ (Note that the exponent $v_p(D_n)$ of $p >2$ in $D_n$ can be written as $r+v_p(r!) = v_p((p r)!)$ where $r=[n/(p-2)]$.) We will return to this point in the next subsection.

-   The unit $\varepsilon_{a/5}$ occurring in (a) and (b), the term under the square-root sign in (c), and the coefficients of the "remaining power series" as defined in (d) are not only in $F(\zeta_5)$, but transform under the Galois group of $F(\zeta_5)/F$ in the "obvious" way, i.e., each of these numbers is a polynomial in $\zeta={\rm e}^{2\pi{\rm i}a/5}$ whose coefficients lie in $F_{4_1}$ and are independent of $a$.

-   Finally, the unit $\varepsilon_{a/5}$ of $F(\zeta_5)$, considered in the quotient $F(\zeta_5)^\times/F(\zeta_5)^{\times 5}$, transforms under the action of the Galois group $\text{Gal}(F(\zeta_5)/F)=(\mathbb Z/5\mathbb Z)^\times$ in two different ways: $$\label{cunit}
    \underline\sigma_r(\varepsilon_{a/5}) = \varepsilon_{ar/5} = (\varepsilon_{a/5})^{1/r}, \qquad r\in(\mathbb Z/5\mathbb Z)^\times,$$ where $\underline\sigma_r$ is the Galois automorphism defined by $\underline\sigma_r(\zeta_5)=\zeta_5^{ r}$.

We conjecture that these properties (a)--(g) hold for all hyperbolic knots $K$, all representations $\sigma$ in $\mathcal P_K$ and all roots of unity $\zeta_\alpha$, with $F$ replaced by the trace field $F_\sigma$ and 5 by the denominator of $\alpha$, as well as a few other small modifications (in particular, that instead of a unit one may get an $S$-unit for small finite set $S$ of primes, essentially the ones occurring in the shape parameters of a triangulation of $S^3\smallsetminus K$, which was empty for $4_1$). In other words, the power series can be written in the form $$\label{Phiprec2}
\Phi_\alpha^{(K,\sigma)}(h) =\mu_{\sigma,\alpha}\cdot(\varepsilon_{\sigma,\alpha})^{1/c}
\cdot \delta_\sigma^{-1/2} \sum_{n=0}^\infty \widetilde A^{(K,\sigma)}_{\alpha,n} h^n ,
\qquad \widetilde A^{(K,\sigma)}_{\alpha,n} \in F_\sigma(\zeta_\alpha)$$ (so that is the product of an algebraic number independent of $n$ and the coefficient denoted in Section [\[sub.CoeffA\]](#sub.CoeffA){reference-type="ref" reference="sub.CoeffA"}), where $F_\sigma$ is defined as in Section [\[sec.Phi\]](#sec.Phi){reference-type="ref" reference="sec.Phi"}, $\mu_{\sigma,\alpha}$ is an $(8c)$-th root of unity, and $\varepsilon_{\sigma,\alpha} \in F_\sigma(\zeta_\alpha)^\times$ is a near-unit, canonically defined only up to $c$-th powers, that transforms up to $c$-th powers as in [\[cunit\]](#cunit){reference-type="eqref" reference="cunit"} (with 5 replaced everywhere by $c$) and that conjecturally depends only on the element of the Bloch group $B(F_\sigma)$ determined by $\sigma$ and in fact coincides with the near-unit that was constructed in [@CGZ], and with the same denominator bound $D_n$ as in [\[Dn\]](#Dn){reference-type="eqref" reference="Dn"}, independent of $K$, $\sigma$ and $\alpha$.
