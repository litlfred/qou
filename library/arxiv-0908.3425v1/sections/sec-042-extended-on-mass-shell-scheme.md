---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-042-extended-on-mass-shell-scheme
section_title: "Extended on-mass-shell scheme"
section_number: null
pages: 62-64
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.984
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
In the following, we will concentrate on yet another solution which has been motivated in Ref. [@Gegelia:1999gf] and has been worked out in detail in Ref. [@Fuchs:2003qc]. The central idea of the extended on-mass-shell (EOMS) scheme consists of performing additional subtractions beyond the $\widetilde{\rm MS}$ scheme such that renormalized diagrams satisfy the power counting. Terms violating the power counting are analytic in small quantities and can thus be absorbed in a renormalization of counter terms.

In order to illustrate the approach, let us consider a simplified version of the integral $H$, namely its value in the chiral limit, $$H(p^2,m^2,0;n)= -i\int \frac{\mbox{d}^n k}{(2\pi)^n}
\frac{1}{[(k-p)^2-m^2+i0^+](k^2+i0^+)},$$ where $$\Delta=\frac{p^2-m^2}{m^2}={\cal O}(q)$$ is a small quantity. Applying the power-counting rules of Sec. [\[subsection_pcrd\]](#subsection_pcrd){reference-type="ref" reference="subsection_pcrd"}, we want the renormalized integral to be of order $D=n-1-2=n-3$. Introducing $C(z,\Delta)=z^2-\Delta\, z(1-z)-i0^+$, we obtain $$\label{Hcl}
H(p^2,m^2,0;n)=\kappa(m;n)\int_0^1 \mbox{d}z\, [C(z,\Delta)]^{\frac{n}{2}-2},$$ where $\kappa(m;n)$ is given in Eq. ([\[4:3:3:kappan\]](#4:3:3:kappan){reference-type="ref" reference="4:3:3:kappan"}). For the purpose of evaluating the integral of Eq. ([\[Hcl\]](#Hcl){reference-type="ref" reference="Hcl"}) we write $$\int_0^1 \mbox{d}z\, [C(z,\Delta)]^{\frac{n}{2}-2}=
(-\Delta)^{\frac{n}{2}-2}\int_0^1 \mbox{d}z\, z^{\frac{n}{2}-2}
\left(1-\frac{1+\Delta}{\Delta}z\right)^{\frac{n}{2}-2}$$ and apply Eqs. 15.3.1 and 15.3.4 of Ref. [@Abramowitz] to obtain $$\label{Hclresult}
H(p^2,m^2,0;n)=\kappa(m;n)\frac{\Gamma\left(\frac{n}{2}-1\right)}{\Gamma
\left(\frac{n}{2}\right)}F\left(1,2-\frac{n}{2};\frac{n}{2};\frac{p^2}{m^2}
\right),$$ where $F(a,b;c;z)$ is the hypergeometric function [@Abramowitz]. In order to discuss the power-counting properties of $H$ (in the chiral limit) in terms of $\Delta$, we make use of Eq. 15.3.6 of Ref. [@Abramowitz] to re-write Eq. ([\[Hclresult\]](#Hclresult){reference-type="ref" reference="Hclresult"}) as $$\begin{aligned}
\label{4:3:4:j0dircalcrewr}
H(p^2,m^2,0;n)&=&\frac{m^{n-4}}{(4\pi)^\frac{n}{2}}\left[
\frac{\Gamma\left(2-\frac{n}{2}\right)}{n-3}
F\left(1,2-\frac{n}{2};4-n;-\Delta\right)\right.\nonumber\\
&&\left.+(-\Delta)^{n-3}\,\Gamma\left(\frac{n}{2}-1\right)
\Gamma(3-n)F\left(\frac{n}{2}-1,n-2;n-2;-\Delta\right)\right].
\end{aligned}$$ Making use of $$\label{fexpansion}
F(a,b;c;z)=1+\frac{ab}{c}z+\frac{a(a+1)b(b+1)}{c(c+1)}\frac{z^2}{2}+\cdots$$ for $|z|<1$ and the fact that $\Delta$ counts as a small quantity of ${\cal O}(q)$, we immediately see that the first term of Eq. ([\[4:3:4:j0dircalcrewr\]](#4:3:4:j0dircalcrewr){reference-type="ref" reference="4:3:4:j0dircalcrewr"}) contains a contribution which does not satisfy the above power counting, i.e., which is not proportional to ${\cal O}(q)$ as $n\to 4$. Using the expansion of Eq. ([\[fexpansion\]](#fexpansion){reference-type="ref" reference="fexpansion"}) together with $\Gamma(1+x)=x\Gamma(x)$ we obtain, as $n\to 4$, $$H=\frac{m^{n-4}}{(4\pi )^{\frac{n}{2}}}
\left[\frac{\Gamma \left(2-\frac{n}{2}\right)}{n-3}
+\left( 1-{p^2\over m^2}\right)\ln \left( 1-{p^2\over m^2}
\right)+
\left( 1-{p^2\over m^2}\right)^2\ln \left( 1-{p^2\over m^2}\right)
+\cdots\right],
\label{j0dircalcisolated}$$ where $\cdots$ refers to terms which are at least of ${\cal O}(q^3)$ or $O(n-4)$. Note that we count a term of the type $-\Delta \ln(-\Delta)$ as ${\cal O}(q)$. If we subtract $$\label{subtraction}
\frac{m^{n-4}}{(4\pi )^{\frac{n}{2}}}
\frac{\Gamma \left( 2-\frac{n}{2}\right)}{n-3}
\label{subtrterm}$$ from Eq. ([\[j0dircalcisolated\]](#j0dircalcisolated){reference-type="ref" reference="j0dircalcisolated"}) we obtain as the renormalized integral $$H_R(p^2,m^2,0;n)={m^{n-4}\over (4\pi )^{n/2}}\left[ \left( 1-{p^2\over m^2}
\right)
\ln \left( 1-{p^2\over m^2}\right)+
\left( 1-{p^2\over m^2}\right)^2\ln \left( 1-{p^2\over m^2}\right)
+\cdots\right].
\label{j0ren}$$ The subtracted term of Eq. ([\[subtrterm\]](#subtrterm){reference-type="ref" reference="subtrterm"}) is local in the external momentum $p$, i.e., it is a *polynomial*  in $p^2$ and can thus be obtained by a finite number of counter terms in the most general effective Lagrangian.

We have seen in Eq. ([\[4:3:4:j0dircalcrewr\]](#4:3:4:j0dircalcrewr){reference-type="ref" reference="4:3:4:j0dircalcrewr"}) that the one-loop integral is of the type $$H\sim F(n,\Delta)+\Delta^{n-3}G(n,\Delta),$$ where $F$ and $G$ are hypergeometric functions and are analytic in $\Delta$ for any $n$. The observation central for the setting up of a systematic method is the fact that the part proportional to $F$ can be obtained by first expanding the integrand in small quantities and *then* performing the integration for each term [@Gegelia:1994zz] (see Sec. [\[section_dimensional_counting_analysis\]](#section_dimensional_counting_analysis){reference-type="ref" reference="section_dimensional_counting_analysis"} for an illustration of the general method). We now apply a conventional renormalization prescription which allows us to identify those terms which we subtract from a given integral without *explicitly* calculating the integral beforehand. In essence we work with a modified integrand which is obtained from the original integrand by subtracting a suitable number of counter terms. The meaning of suitable in the present context will be explained in a moment. To that end we consider the series $$\begin{aligned}
\label{4:3:4:series}
\lefteqn{
\sum_{l=0}^\infty \frac{(p^2-m^2)^l}{l!}\left[
\left(\frac{1}{2p^2}p_\mu\frac{\partial}{\partial p_\mu}\right)^l
\frac{1}{[k^2-2k\cdot p+(p^2-m^2)+i0^+](k^2+i0^+)}\right]_{p^2=m^2}}\nonumber\\
&=&\left.\frac{1}{(k^2-2k\cdot p+i0^+)(k^2+i0^+)}\right|_{p^2=m^2}\nonumber\\
&&+(p^2-m^2)\left[\frac{1}{2m^2}\frac{1}{(k^2-2k\cdot p+i0^+)^2}
-\frac{1}{2m^2}\frac{1}{(k^2-2k\cdot p+i0^+)(k^2+i0^+)}\right.\nonumber\\
&&\left. -\frac{1}{(k^2-2k\cdot p+i0^+)^2(k^2+i0^+)}
\right]_{p^2=m^2}+\cdots,
\end{aligned}$$ where $[\cdots ]_{p^2=m^2}$ means that we consider the *coefficients* of $(p^2-m^2)^l$ only for four-momenta $p^\mu$ satisfying the on-mass-shell condition. Although the coefficients still depend on the direction of $p^\mu$, after integration of this series with respect to the loop momentum $k$ and evaluation of the resulting coefficients for $p^2=m^2$, the integrated series is a function of $p^2$ only. In fact, as was shown in Ref. [@Gegelia:1994zz], the integrated series exactly reproduces the first term of Eq. ([\[4:3:4:j0dircalcrewr\]](#4:3:4:j0dircalcrewr){reference-type="ref" reference="4:3:4:j0dircalcrewr"}). At this point we stress that $$\left.
-i\int \frac{\mbox{d}^n k}{(2\pi)^n}
\frac{1}{(k^2-2k\cdot p+i0^+)(k^2+i0^+)}\right|_{p^2=m^2}$$ and $$\left[-i\int \frac{\mbox{d}^n k}{(2\pi)^n}
\frac{1}{(k^2-2k\cdot p+p^2-m^2+ i0^+)(k^2+i0^+)}\right]_{p^2=m^2}$$ are not the same for $n\leq 3$.

The formal definition of the EOMS renormalization scheme is then as follows: we subtract from the integrand of $H(p^2,m^2,0;n)$ those terms of the series of Eq. ([\[4:3:4:series\]](#4:3:4:series){reference-type="ref" reference="4:3:4:series"}) which violate the power counting. These terms are always analytic in the small parameter and do not contain infrared singularities. In the above example we only need to subtract the first term. All the higher-order terms contain infrared singularities. For example, the last term of the second coefficient would generate a behavior $k^3/k^4$ of the integrand for $n=4$. The integral of the first term of Eq. ([\[4:3:4:series\]](#4:3:4:series){reference-type="ref" reference="4:3:4:series"}) is given by Eq. ([\[subtraction\]](#subtraction){reference-type="ref" reference="subtraction"}), and we end up with Eq. ([\[j0ren\]](#j0ren){reference-type="ref" reference="j0ren"}) for the renormalized integral: $$H_R=H-H_{\rm subtr}={\cal O}(q^{n-3}).$$ Since the subtraction point is $p^2=m^2$, the renormalization condition is denoted "extended on-mass-shell" (EOMS) scheme in analogy with the on-mass-shell renormalization scheme in renormalizable theories. In the general case including the pion mass, one would consider the series $$\begin{aligned}
&& \left.\frac{1}{\left( k^2-2 k\cdot p+i 0^+ \right)\left( k^2+i
0^+\right)}\right|_{p^2=m^2}+(p^2-m^2)\left[ \frac{1}{2 m^2} \frac{1}{\left( k^2-2 k\cdot p+i
0^+
\right)^2}+\cdots \right]_{p^2=m^2}\\
&&+M^2 \left. \frac{1}{\left( k^2-2 k\cdot p+i 0^+
\right)\left( k^2+i 0^+\right)^2 }\right|_{p^2=m^2}+\cdots
\end{aligned}$$ instead of Eq. ([\[4:3:4:series\]](#4:3:4:series){reference-type="ref" reference="4:3:4:series"}). However, it would still be only the contribution resulting from the first term that were to be subtracted.

Within the EOMS framework it is straightforward to obtain a consistent power counting in manifestly Lorentz-invariant baryon ChPT including, e.g., vector mesons [@Fuchs:2003sh] or the $\Delta(1232)$ resonance [@Hacker:2005fh] as explicit degrees of freedom. Moreover, the infrared regularization of Becher and Leutwyler can be reformulated in a form analogous to the EOMS renormalization scheme and can thus be applied straightforwardly to multi-loop diagrams with an arbitrary number of particles with arbitrary masses [@Schindler:2003xv] (see also Refs. [@Lehmann:2001xm], [@Bruns:2004tj], [@Bruns:2008ub]). The application of both infrared and extended on-mass-shell renormalization schemes to multi-loop diagrams was explicitly demonstrated by means of a two-loop self-energy diagram [@Schindler:2003je].
