---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-010-34-asymptotics-of-the-coefficients
section_title: "Asymptotics of the coefficients"
section_number: 3.4
pages: 20-22
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.994
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.CoeffA label="sub.CoeffA"}

The third interrelationship between the series $\Phi^{(\sigma)}_\alpha$ for different elements $\sigma$ of $\mathcal P_K$ arises via the asymptotics of their coefficients.

For both theoretical and numerical purposes, we need to be able to compute the "values" of the divergent series for very small $h$, and for this we need to know how their coefficients grow. We will write for the coefficient of $h^n$ in .

As usual, we start with the simplest example $K=4_1$, $\sigma=\sigma_1$ (geometric representation), and  $\alpha=0$, where is just the series [\[as41\]](#as41){reference-type="eqref" reference="as41"}. Let us write just $A(n)$ for its $n$-th coefficient (so $A(0)=3^{-1/4}$, $A(1)=11 A_0/72\sqrt{-3}$). Calculating many coefficients and using a standard numerical extrapolation method that is recalled in Part II, we find that $A(n)$ grows factorially like $(n-1)! \lambda^{-n} \big(c_0+c_1n^{-1}+c_2n^{-2}+\cdots\big)$ for some constants $\lambda$ and $c_i$. The numbers $\lambda$ and $c_0$ are easily recognized to be $2\mathbf V(K)=2{\rm i} \mathrm{Vol}(K)$ and $3A(0)/2\pi$, respectively, but the further coefficients $c_i$ have more and more complicated expressions. It turns out that a much more convenient representation for the asymptotics is as a sum of shifted factorials $(n-1-\ell)!$ rather than of terms $n!/n^\ell$, because in this version we find the expansion $$\label{AnFirst}
A(n) \sim \frac3{2\pi}
\sum_{\ell\ge0} (-1)^\ell A(\ell) \frac{(n-\ell-1)!}{(2\mathbf V(4_1))^{n-\ell}}$$ with easily recognizable coefficients to all orders. If we now recall that equals and hence , then we can recognize [\[AnFirst\]](#AnFirst){reference-type="eqref" reference="AnFirst"} as one of a pair of coupled asymptotic expansions $$A^{(\sigma_1)}_0(n) \sim \frac3{2\pi {\rm i}}
\sum_{\ell\ge0} A^{(\sigma_2)}_0(\ell) \frac{(n-1-\ell)!}{(2\mathbf V(4_1))^{n-\ell}} ,
\qquad A^{(\sigma_2)}_0(n) \sim
\frac{-3}{2\pi {\rm i}}
\sum_{\ell\ge0} A^{(\sigma_1)}_0(\ell) \frac{(n-\ell-1)!}{(-2\mathbf V(4_1))^{n-\ell}} .$$ This already looks quite nice, but the picture becomes even clearer when we consider also the coefficients $B(0)=1$, $B(1)=0$, $B(2)=-1$, $\dots$ of the third series $\Phi_0^{\sigma_0}$ as given in [\[41HabAt0\]](#41HabAt0){reference-type="eqref" reference="41HabAt0"}. Since the $B(n)$ vanish for $n$ odd, it would first seem that one has to give separate asymptotic formulas according to the parity of $n$, but a better way is to write as a sum of *two* asymptotic expansions labelled by the two other elements $\sigma_1$ and $\sigma_2$ of $\mathcal P_K$: $$\label{BnFirst}
B(n) \sim \sqrt{2\pi} \sum_{\ell\ge0}
A^{(\sigma_1)}_0(\ell) \frac{\Gamma\big(n-\ell+\frac32\big)}{(-\mathbf V(4_1))^{n-\ell+3/2}}
 - \sqrt{2\pi} \sum_{\ell\ge0}
A^{(\sigma_2)}_0(\ell) \frac{\Gamma\big(n-\ell+\frac32\big)}{\mathbf V(4_1)^{n-\ell+3/2}} .$$ Here we observe that the expressions $2\mathbf V(4_1)$, $-2\mathbf V(4_1)$, $-\mathbf V(4_1)$ and $\mathbf V(4_1)$ occurring in the denominators of the last two formulas can be written in a uniform way as $\mathbf V(\sigma_1)-\mathbf V(\sigma_2)$, $\mathbf V(\sigma_2)-\mathbf V(\sigma_1)$, $\mathbf V(\sigma_0)-\mathbf V(\sigma_1)$ and $\mathbf V(\sigma_0)-\mathbf V(\sigma_2)$, respectively. Exactly analogous asymptotic statements turn out to hold for the coefficients of the series also for $\alpha\ne0$, with the same coefficients, leading for this knot to the uniform conjectural statement $$\label{CoeffAsymp}
A_\alpha^{(K,\sigma)}(n) \sim (2\pi)^{\kappa_\sigma-1} 
\sum_{\sigma'\ne\sigma}M_K(\sigma,\sigma') \sum_{\ell\ge0} A^{(\sigma')}_\alpha(\ell)
\frac{\Gamma(n-\ell+\kappa_\sigma)}{\bigl(\mathbf V(\sigma)-\mathbf V(\sigma')\bigr)^{n-\ell+\kappa_\sigma}} ,$$ for all elements $\sigma\in\mathcal P_K$ and all $\alpha\in\mathbb Q$, where $\kappa_\sigma$ is defined as in [\[Defwsigma\]](#Defwsigma){reference-type="eqref" reference="Defwsigma"} and where the coefficients $M_K(\sigma,\sigma')$ are integers independent on $\alpha$, given for $K=4_1$ by $$M_{4_1} =
\begin{pmatrix} 0 & 1 & -1 \\ 0 & 0 & -3 \\ 0 & 3 & \hphantom{-}0 \end{pmatrix} .$$ Experiments with our other two standard sample knots $5_2$ and $(-2,3,7)$ reveal the same asymptotic behavior [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"}, with the matrix $M_K$ given in these two cases by $$M_{5_2} = \begin{pmatrix}
 0 & \hphantom{-}1 & 1 & -1 \\
 0 & \hphantom{-}0 & 4 & -3 \\
 0 & -4 & 0 & -3 \\
 0 & \hphantom{-}3 & 3 & \hphantom{-}0 \end{pmatrix} ,
\qquad
M_{(-2,3,7)} =
\begin{pmatrix} 0 & \hphantom{-}0 & \hphantom{-}0 & 1 & 0 & 0 & 0 \\
 0 & \hphantom{-}0 & \hphantom{-}0 & 1 & 2 & 2 & 2 \\
 0 & \hphantom{-}0 & \hphantom{-}0 & 1 & 2 & 2 & 2 \\
 0 & -1 & -1 & 0 & 0 & 0 & 0 \\
 0 & -2 & -2 & 0 & 0 & 0 & 0 \\
 0 & -2 & -2 & 0 & 0 & 0 & 0 \\
 0 & -2 & -2 & 0 & 0 & 0 & 0 \end{pmatrix} .$$

We end this subsection by making a number of remarks about the asymptotic formula [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"} and the matrices $M_K$.

**1.** The coefficients of the matrices $M_K$ are much simpler invariants of $K$ than the coefficients of the power series , because they are rational integers rather than algebraic numbers and also do not depend on $\alpha$. It would be of considerable interest to have an direct topological definition of these numbers rather than just an indirect one in terms of the (still conjectural) asymptotic formula [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"}. One possibility in Section [\[sec.Phi\]](#sec.Phi){reference-type="ref" reference="sec.Phi"} is that they are related to the counting of flow lines in Floer homology. They are also presumably the same as the skew-symmetric matrices of "Stokes indices" as recently introduced by Kontsevich [@MaximTalks].

**2.** The different forms of the asymptotics of the coefficients of $\Phi^{(\sigma)}_\alpha$ for $\sigma=\sigma_0$ and $\sigma\ne\sigma_0$ are directly related to the different weights and different completions of these series as given in equation [\[UnifPhih\]](#UnifPhih){reference-type="eqref" reference="UnifPhih"}.

**3.** A different asymmetry between the trivial and non-trivial representations is seen in the fact that $M_K(\sigma,\sigma_0)$ always vanishes but $M_K(\sigma_0,\sigma)$ does not, meaning that the large-index coefficients of the $\Phi^{(\sigma_0)}$ series "see" the small-index coefficients of the $\Phi^\sigma$ series for $\sigma\ne\sigma_0$ but not vice versa. It is interesting to note that similar "one-way phenomenon" regarding the matrices appearing in  [@Witten:continuation], see also Gukov et al. [@Gukov:resurgence; @Gukov:BPS].

**4.** In all three examples given above, we further observe that apart from their first column, which vanishes, and first row, which does not, the matrices $M_K$ are skew-symmetric, i.e., ${M_K(\sigma,\sigma')=-M_K(\sigma',\sigma)}$ for $\sigma, \sigma'\ne\sigma_0$. This phenomenon, which we expect to hold for all knots, will be shown below to be a formal consequence of the quadratic relation [\[quadrel\]](#quadrel){reference-type="eqref" reference="quadrel"}.

**5.** We also observe that the lower $4\times4$ block of the matrix $M_{(-2,3,7)}$ vanishes identically. In view of the numbering of the indices, this means that $M_K(\sigma,\sigma')$ vanishes whenever $\sigma$ and $\sigma'$ are both real and distinct from $\sigma_0$. This in fact holds for all knots and is a special case of the more general identity $M_K\big(\overline{\sigma\vphantom I},\overline{\sigma'}\big)=-M_K(\sigma,\sigma')$ for all $\sigma, \sigma'\ne\sigma_0$, which we can prove easily (assuming that the expansion [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"} is correct) simply by taking the complex conjugate of [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"} and noting that $\mathbf V(\overline\sigma)$ and are the complex conjugates of $\mathbf V(\sigma)$ and , respectively (and, of course, that the coefficients of $M_K$ are real). The minus sign arises from the pure imaginary prefactor $(2\pi {\rm i})^{-1}$ in [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"}.

**6.** A corollary of [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"} is the growth estimate $$A_\sigma^{(\sigma)}(n)= O\bigl(n^{\kappa_\sigma-1}n! \Delta(\sigma)^{-n}\bigr) ,$$ where $$\Delta(\sigma)=\Delta(K,\sigma) = \min_{M_K(\sigma,\sigma')\ne0}\bigl|\mathbf V(\sigma)-\mathbf V(\sigma')\bigr| .$$ This estimate will be important for the optimal truncation that is used in the next section and discussed in more detail in Section [\[sec.compKash\]](#sec.compKash){reference-type="ref" reference="sec.compKash"} and in [@GZ:optimal].

**7.** We should also mention that there is still some sign ambiguity in the definition of the matrix $M_K$. At the moment, even assuming the validity of the various conjectures presented in the next two sections, we can only normalize the power series up to the ambiguity of a sign $\varepsilon_\sigma\in\{\pm1\}$ independent of $\alpha$ but depending on $\sigma$, and making this change would multiply $M_K(\sigma,\sigma')$ by $\varepsilon_\sigma\varepsilon_{\sigma'}$ (which would not affect either of the properties mentioned in **3** and **4** above). Similarly, when $\sigma=\sigma_0$ the formula defining $M_K(\sigma,\sigma')$ has an inherent ambiguity coming from the choice of sign of square-root of $V_\sigma-V_{\sigma'}=-V_{\sigma'}$ in [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"} (only in the first term; the choices for the other terms are then determined in the obvious way), so that each of the matrix entries $M_K(\sigma_0,\sigma')$ is actually only well defined up to sign. Of course, it is possible that there is some canonical way to normalize everything to eliminate these ambiguities, but we do not yet know how to do this.

**8.** Actually, however, there is a problem with all of these statements that we have glossed over so far but that does need to be addressed. This is that the right-hand side of [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"} does not really make sense as it stands, since the terms on the right-hand side are given by divergent series and hence can be computed only up to some level of precision, but at the same time have exponentially different orders of growth, so that it is not a priori clear what it means to add them. In the case of $4_1$, we did not see this problem, because there is only one term in [\[CoeffAsymp\]](#CoeffAsymp){reference-type="eqref" reference="CoeffAsymp"}. This point will be discussed briefly in Section [\[sub.optimal\]](#sub.optimal){reference-type="ref" reference="sub.optimal"} and in detail in [@GZ:optimal].
