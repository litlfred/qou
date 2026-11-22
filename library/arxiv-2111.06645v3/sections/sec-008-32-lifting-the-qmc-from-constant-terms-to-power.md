---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-008-32-lifting-the-qmc-from-constant-terms-to-power
section_title: "Lifting the QMC from constant terms to power series"
section_number: 3.2
pages: 16-18
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.995
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.QMCwithh label="sub.QMCwithh"}

In the previous subsection, we generalized the original QMC by replacing the Kashaev invariant $J^{(K)}$ by the generalized Kashaev invariants $J^{(K,\sigma)}$ for any $\sigma\in\mathcal P_K$. This in turn will be further refined in Section [\[sec.RQMC\]](#sec.RQMC){reference-type="ref" reference="sec.RQMC"} by adding terms of exponentially lower order to the right-hand side of the asymptotic formula. Here we discuss instead a different refinement.

Our starting point, just as in Section [\[sub.GQMC\]](#sub.GQMC){reference-type="ref" reference="sub.GQMC"}, is that the Kashaev invariant $J^{(K)}(\alpha)$ is equal to the constant term of the power series as defined in Section [\[sec.Phi\]](#sec.Phi){reference-type="ref" reference="sec.Phi"}, so that the original QMC [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"} can be rewritten as $$\Phi_{\gamma X} ^{(\sigma_0)}(0)
 \sim  (cX+d)^{3/2} \Phi_{X} ^{(\sigma_0)}(0)
 \widehat\Phi_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)$$ for $X$ tending to infinity with fixed fractional part or with bounded denominator. (Here we again omit the knot $K$ from the superscripts when it is not varying to avoid cluttering up the notations. Recall also that $c>0$.) It is then natural to ask whether this asymptotic formula can be lifted to a corresponding statement for the full series  rather than just its constant term. The answer is affirmative, but with a little twist, $$\label{GQMCh}
\Phi_{\gamma X} ^{(\sigma_0)}(h^*)  \sim (cX+d)^{3/2}
\Phi_{X} ^{(\sigma_0)}(h) \widehat\Phi_{a/c}\left(\frac{2\pi {\rm i}}{c(cx+d)}\right) ,$$ where $x=X-\hbar$ with $\hbar$ as in [\[UnifPhih\]](#UnifPhih){reference-type="eqref" reference="UnifPhih"} and .

Let us explain what the asymptotic expansion [\[GQMCh\]](#GQMCh){reference-type="eqref" reference="GQMCh"} means in the simplest case of the figure 8 knot. Recall that where $\mathcal J(q)=\mathcal J^{(4_1)}(q)$ is the element of the Habiro ring given by [\[Hab41\]](#Hab41){reference-type="eqref" reference="Hab41"}, related to $J(X)=J^{(4_1)}(X)$ by $J(X)=\mathcal J(\mathbf{e}(X))$. Since the Habiro ring is closed under the operator $q {\rm d}/{\rm d}q$, it contains the function $\mathcal J'$ defined by $$\label{41Jderiv}
\mathcal J'(q) := q \frac {\rm d}{{\rm d}q} \mathcal J(q)
= \sum_{n=1}^\infty \big(q^{-1};q^{-1}\big)_n (q,q)_n
\sum_{k=1}^nk \frac{1+q^k}{1-q^k} .$$ We then define the formal derivative $J'\colon \mathbb Q/\mathbb Z\to2\pi {\rm i} \overline{\mathbb Q}$ by $J'(X)=2\pi {\rm i}\mathcal J'(\mathbf{e}(X))$. Then the statement of [\[GQMCh\]](#GQMCh){reference-type="eqref" reference="GQMCh"} in this case is $$\label{CheckDeriv}
\frac1{(cX+d)^2}
\frac{J'\bigl(\frac{aX+b}{cX+d}\bigr)}{J\bigl(\frac{aX+b}{cX+d}\bigr)}
 - \frac{J'(X)}{J(X)} \approx 
 - \frac{2\pi {\rm i}}{(cX+d)^2}
\frac{\widehat\Phi'_{a/c}
 \bigl(\frac{2\pi {\rm i}}{c(cX+d)}\bigr)}{\widehat\Phi_{a/c}\bigl(\frac{2\pi {\rm i}}{c(cX+d)}\bigr)}
 ,$$ interpreted in the following sense. The left-hand side of [\[CheckDeriv\]](#CheckDeriv){reference-type="eqref" reference="CheckDeriv"} is $2\pi {\rm i}$ times an algebraic number belonging to some fixed cyclotomic field for each fixed element $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)$ and bound on the denominator of $X$, while the right-hand side is defined only as a divergent power series in $(cX+d)^{-1}$. The claim is then that when we compute both sides of [\[CheckDeriv\]](#CheckDeriv){reference-type="eqref" reference="CheckDeriv"} for fixed $\gamma$ and for $X$ tending to infinity with bounded denominator, using [\[41Jderiv\]](#41Jderiv){reference-type="eqref" reference="41Jderiv"} to compute the terms $J'(X)$ and $J'(\gamma X)$ as exact algebraic numbers, the two expressions agree numerically to all orders in $1/X$, and this is the statement that we verified numerically for several elements $\gamma$ and sequences of large rational numbers $X$. Note that [\[CheckDeriv\]](#CheckDeriv){reference-type="eqref" reference="CheckDeriv"} is almost what we would get if we differentiated the original QMC formula [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"} logarithmically (which of course we are not allowed to do since it is only an asymptotic statement valid for large rational numbers $X$ with fixed denominator and hence is rigid), except that then we would have an extra term which is in fact not present because equation [\[GQMCh\]](#GQMCh){reference-type="eqref" reference="GQMCh"} contains $(cX+d)^{3/2}$ rather than $(cx+d)^{3/2}$.

All of this was for the trivial connection $\sigma_0$. If we consider instead an arbitrary element $\sigma$ of $\mathcal P_K$, then what we find is the obvious combination of [\[GQMC\]](#GQMC){reference-type="eqref" reference="GQMC"} (which was only for the constant terms $\Phi(0)$) and [\[GQMCh\]](#GQMCh){reference-type="eqref" reference="GQMCh"} (which gave the "twist" needed to include $h$), namely $$\label{GQMChh}
(cX+d)^{-\kappa(\sigma)} {\rm e}^{-v(\sigma)  \lambda_\gamma(X)}  \Phi_{\gamma X} ^{(\sigma)}(h^*)
  \sim  \Phi_X^{(\sigma)}(h) \widehat\Phi_{a/c}\left(\frac{2\pi {\rm i}}{c(cx+d)}\right) ,$$ with $x=X-\hbar$ and $h^*=h/(cx+d)(cX+d)$ as in [\[GQMCh\]](#GQMCh){reference-type="eqref" reference="GQMCh"}.

Equation [\[GQMChh\]](#GQMChh){reference-type="eqref" reference="GQMChh"} differs in two notable ways from the original QMC [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"}: the appearance of the "tweaking factor" ${\rm e}^{-v(\sigma)\lambda_\gamma(X)}$ and the change of infinitesimal variable from $h$ to $h^*$. In fact, the first is explained very simply by replacing the two power series $\Phi^{(\sigma)}$ in [\[GQMChh\]](#GQMChh){reference-type="eqref" reference="GQMChh"} by their completions as defined in [\[UnifPhih\]](#UnifPhih){reference-type="eqref" reference="UnifPhih"}, because a short calculation shows that the number $\lambda_\gamma(X)$ defined in [\[tweakdef\]](#tweakdef){reference-type="eqref" reference="tweakdef"} is equal to the difference between $1/\mathrm{den}(X)^2\hbar$ and $1/\mathrm{den}(\gamma X)^2\hbar^*$ with ${\hbar^*:=\hbar^*/2\pi {\rm i}=\hbar/(cx+d)(cX+d)}$, so that [\[GQMChh\]](#GQMChh){reference-type="eqref" reference="GQMChh"} becomes simply $$\label{GQMChhh}
\widehat\Phi_{\gamma X} ^{(K,\sigma)}(h^*)  \sim (cx+d)^{-\kappa(\sigma)} \widehat\Phi_X^{(K,\sigma)}(h)
 \widehat\Phi^{(K,\sigma_1)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cx+d)}\right) ,$$ where we have now again included the complete labels of the $\widehat\Phi$ series for clarity. In this version both the tweaking factor ${\rm e}^{-v(\sigma)\lambda_\gamma(X)}$ and the automorphy factor $(cX+d)^{3/2}$ have been absorbed into the completed power series, but then producing a new automorphy factor ${(cx+d)^{-3/2}}$. Finally, the "twisting" from $h$ to $h^*$ is partly motivated by the calculation just given and the simplifications in [\[GQMChhh\]](#GQMChhh){reference-type="eqref" reference="GQMChhh"}, but more conceptually by observing that $x=X-\hbar$ implies ${\gamma x=\gamma X-\hbar^*}$. Equation [\[GQMChhh\]](#GQMChhh){reference-type="eqref" reference="GQMChhh"} will then take on an even more natural form in terms of the notion of "functions near $\mathbb Q$" that will be introduced in Section [\[sec.Matrix\]](#sec.Matrix){reference-type="ref" reference="sec.Matrix"}.
