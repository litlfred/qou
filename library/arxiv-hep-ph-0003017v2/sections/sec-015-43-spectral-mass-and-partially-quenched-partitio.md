---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-015-43-spectral-mass-and-partially-quenched-partitio
section_title: "Spectral Mass and Partially Quenched Partition Function"
section_number: 4.3
pages: 26-31
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.987
---
[]{#SpectralMass label="SpectralMass"}

The Dirac spectrum can be obtained from the resolvent $$\Sigma(z) =\left\langle \frac 1V\: \Tr \frac 1{{\cal D}+z} \right
  \rangle\:,$$ were the spectral mass $z$ is an independent complex variable that does not occur in the average. With purely imaginary eigenvalues the spectral density is given by the discontinuity of the resolvent across the imaginary axis, $$\frac {\rho(\lambda)}V = \lim_{\epsilon\to0}\frac 1{2\pi}
  [ \Sigma(i\lambda +\epsilon) - \Sigma(i\lambda -\epsilon)]\:.
  \label{discon}$$ This follows immediately upon writing the trace as a sum over the eigenvalues of ${\cal D}$. The generating function for the resolvent can be written down easily [@Vminn], $$Z^{\rm sp} = \left \langle \frac {{\det}^{N_f}({\cal D}+m)
      \det({\cal D}+z)}{\det({\cal D}+z')} \right \rangle_{\rm YM}\:,
  \label{Zsp}$$ where we have explicitly displayed the fermion determinant in the measure. The resolvent is then given by $$\Sigma(z) = \left. \frac 1V \partial_z Z^{\rm sp}(z,z')\right|_{z'=z}.
  \label{resol}$$ In QCD, this method was first introduced in order to derive the quenched strong coupling expansion [@Morel]. In nuclear physics and condensed matter physics, this method is known as the supersymmetric method or Efetov method for quenched disorder [@Brezin; @Efetov; @VWZ].

The determinants in the numerator can be written as fermionic integrals whereas the determinant in the denominator can be written as a bosonic integral. The partition function ([\[Zsp\]](#Zsp){reference-type="ref" reference="Zsp"}) is thus invariant under flavor symmetries that mix commuting and anticommuting degrees of freedom. More precisely, for $m=z=z'=0$ the partition function is invariant under the supergroup ${\rm
  Gl}_R(N_f+1|1) \times {\rm Gl}_L(N_f+1|1)$. In order to obtain a consistent effective theory, it is essential to extend the unitary symmetry to the general linear group Gl. We expect, as for the QCD vacuum, that chiral symmetry is spontaneously broken to the diagonal subgroup ${\rm Gl}_{\rm V}(N_f+1|1)$. The mass term explicitly breaks the full symmetry to this subgroup as well.

The effective partition function can be derived in the same way as the regular chiral Lagrangian with one complication. To obtain finite integrals, we must make sure that the integration manifold is Riemannian. This is why we have extended the flavor symmetry to the full general linear group. The integration manifold is then given by the maximum Riemannian submanifold of ${\rm
  Gl}_{\rm A}(N_f+1|1)$. In plain language, this means that we compensate the extra minus sign in the supertrace by complexifying the group parameters. The generating function is thus given by [@OTV] $$\label{zspect}
  Z^{\rm pq}=\hspace*{-17pt}\int\limits_{U\in {\hat {\rm Gl}}(N_f+1|1)} 
  \hspace*{-17pt} DU e^{\int d^4x \left[-\frac
      {F^2}4 \Str \partial_\mu U \partial_\mu U^{-1} -
      \frac{F^2m_0^2}{12}\left(\frac{\sqrt 2 \Phi_0}F  
        - \theta \right )^2 + \frac{ \Sigma}2\:
      \Str (MU + M^\dagger U^{-1})\right]}\:, \nonumber \\$$ where $i\sqrt 2\Phi_0/F = {\rm Str} \log U$. This partition function is also known as the partially quenched effective partition function. It has been used to obtain a better understanding of quenched lattice QCD results [@Maarten; @Sharpe]. The hat on Gl denotes the maximum Riemannian submanifold of ${\rm Gl}(N_f+1|1)$, and Str stands for the supertrace. An example of an explicit parameterization of $U$ will be given in the next subsection. The parameter $m_0^2$ is proportional to the topological susceptibility and results in a mass for the singlet channel that does not vanish in the chiral limit.

The perturbative formulation of this partition function was first given by Bernard and Golterman [@Maarten], and a perturbative calculation of the dependence of the condensate on the spectral mass was first performed in Ref. [@Leung]. In that case, it is acceptable to ignore the convergence properties of the effective partition function and integrate over the unitary supergroup instead.

An alternative generating function would be obtained by replacing the ratio of the two determinants by ${\det}^n({\cal D}+z)$ and putting $n
\rightarrow 0$ after having calculated the resolvent. This procedure, known as the replica trick [@edwards], successfully reproduces the asymptotic expansions of the spectral correlation functions [@asympt; @pourep]. There have been recent claims that it is possible to derive truly nonperturbative results by means of the replica trick [@kamenev; @yurk; @kanrep]. We do not believe that this can be done in general [@critique; @zirnrep; @dalmazi]. As mentioned, because of the compact/noncompact structure of the final answer, the supersymmetric formulation is the natural approach to this problem.

## Domains of the Partially Quenched Effective Theory {#sec:domains}

The Goldstone fields can be written as $$\label{Ufields}
  U = e^{i\sqrt 2\Pi/F}\:.$$ To second order in the fields, the effective Lagrangian in momentum space is given by $${\cal L} = \frac 1V \sum_a\sum_k  (k^2 + M_a^2) \Pi_a^2(k)\:,
  \label{L2}$$ where the sum is over the momenta in a box of length $L$ (including the zero-momentum state) and the masses of the Goldstone bosons are denoted by $M_a$. The sum over $a$ is over the different Goldstone modes. In addition to the usual Goldstone modes with mass $$\label{Gmass1}
  M_{mm}^2 = \frac{2m\Sigma}{F^2}\:,$$ there are both fermionic and bosonic Goldstone bosons with mass $$M_{mz}^2 = \frac{(m+z)\Sigma}{F^2}$$ and fermionic and bosonic Goldstone bosons with mass $$\label{Gmass3}
  M_{zz}^2 = \frac{2z\Sigma}{F^2}\:.$$ In the Lagrangian ([\[L2\]](#L2){reference-type="ref" reference="L2"}), one can distinguish the zero-momentum modes from the nonzero-momentum modes. The magnitude of the fluctuations of the nonzero-momentum modes is of order $1/(k^2+M^2_a)$, whereas the magnitude of the fluctuations of the zero-momentum modes is of order $1/M_a^2$. Since the smallest nonzero momenta are of order $1/L$, the fluctuations of the zero-momentum modes are dominant if $$\label{compton}
  M_a^2 \ll \frac 1{L^2}\:.$$ This means that the Compton wavelength of the "pion" is much larger than the size of the box. For nonzero quark masses of order $O(L^0)$, the inequality ([\[compton\]](#compton){reference-type="ref" reference="compton"}) is never satisfied. However, the spectral mass $z$ is a free parameter, and the inequality can be rewritten as [@Verb96; @Trento] $$z \ll E_c\equiv\frac {F^2}{\Sigma L^2}\:.
  \label{spectralrange}$$ We sometimes refer to the quantity $E_c$ as the Thouless energy for reasons that will become clear in Sec. [\[sec:anderson\]](#sec:anderson){reference-type="ref" reference="sec:anderson"}. In the domain of Eq. ([\[spectralrange\]](#spectralrange){reference-type="ref" reference="spectralrange"}), the dominant contributions to the resolvent are from the zero-momentum modes. Thus, the partially quenched effective partition function ([\[zspect\]](#zspect){reference-type="ref" reference="zspect"}) can be reduced to the partition function in the zero-momentum sector [@OTV; @Damg99], $$\label{static}
  Z= \int_{U\in {\hat{\rm Gl}}(N_f+1|1)} DU e^{\frac12 
    V\Sigma\:\Str(MU + M^\dagger U^{-1})}\:.$$ The microscopic spectral density and the spectral correlations computed from Eq. ([\[static\]](#static){reference-type="ref" reference="static"}) are identical to those obtained in chRMT [@Verb96; @Trento]. Let us show this by an explicit calculation of the dependence of the chiral condensate on the spectral mass $z$. To cover the complete range ([\[spectralrange\]](#spectralrange){reference-type="ref" reference="spectralrange"}), the integral over $U$ has to be done nonperturbatively. This is a straightforward superintegral that can be evaluated using standard methods. The calculation of the integration measure requires an explicit parameterization of the integration manifold. For example, in the quenched limit, $N_f = 0$, a possible choice is $$U = \mat e^{i\phi} & \alpha \\ \beta & e^s \emat$$ with $\alpha$ and $\beta$ Grassmann variables, $\phi \in [0, 2\pi]$, and $s \in (-\infty, \infty)$. A characteristic feature of the integration manifold is that it consists of a compact and a noncompact component. The valence-quark mass dependence of this partition function and its generalization to arbitrary topological charge coincide with the valence quark mass dependence of the chUE partition function. We merely quote the final result for the resolvent for $N_f$ massless flavors in the sector of topological charge $\nu$ [@Verb96], $$\label{valk}
  \frac{\Sigma(u)}{\Sigma} = u\left[I_{a}(u)K_{a}(u) 
    +I_{a+1}(u)K_{a-1}(u)\right]+\frac{|\nu|}{u}\:,$$ where $a= N_f+|\nu|$ and $u= zV\Sigma$. The compact/noncompact symmetries are reflected in the appearance of the $I_a/K_a$-Bessel functions and are thus a natural ingredient of the underlying integration manifold. This result was first obtained from chRMT by integrating the microscopic spectral density in Eq. ([\[micro2\]](#micro2){reference-type="ref" reference="micro2"}) as follows, $$\frac{\Sigma(u)}{\Sigma} = \int_0^\infty d\zeta 
 \frac{2u}{\zeta^2+u^2}\rho_s(\zeta)\:.$$ Alternatively, the microscopic spectral density can be obtained by taking the discontinuity of $\Sigma(u)$ according to Eq. ([\[discon\]](#discon){reference-type="ref" reference="discon"}). By integrating back, we find that the mass dependence of the zero-momentum partially quenched partition function coincides with that of the chRMT partition function for $\beta=2$.

Figure [1](#fig:domains){reference-type="ref" reference="fig:domains"} presents a schematic picture of the different domains in the Dirac spectrum. There are other non-QCD theories that can be reduced to the same partially quenched partition function. Probably the best known example is the instanton liquid model of QCD [@instantonl]. Another example, more closely related to disordered condensed matter systems, is the random-flux model [@simons-altland], which is in essence quenched lattice QCD with Kogut-Susskind fermions but without the phase factors due to the $\gamma$-matrices. Related examples are so-called two-sublattice models with disorder [@Gade], and disordered lattice models with the chiral and flavor symmetries of QCD [@Takahashi; @Guhr-Wilke-Weidi].

<figure id="fig:domains">
<div class="center">

</div>
<figcaption>Diagram illustrating the different domains in the QCD Dirac spectrum. Here, pqChPT denotes partially quenched chiral perturbation theory, and chRMT stands for chiral random matrix theory.</figcaption>
</figure>

In the range $$E_c \ll z \ll \Lambda\:,
  \label{dom1}$$ the effective action ([\[zspect\]](#zspect){reference-type="ref" reference="zspect"}) is still valid but chiral random matrix theory no longer applies. In this range, the $U$ fields can be expanded to second order in the pion fields, and the spectral mass dependence of the chiral condensate can be obtained to one loop order. The spectral density follows by taking the discontinuity of $\Sigma(z)$ across the imaginary axis. This calculation can be performed both for the partition function of Eq. ([\[zspect\]](#zspect){reference-type="ref" reference="zspect"}) and the effective partition functions for $\beta =1$ and $\beta =4$. The result for the slope of the spectral density at zero, valid for $N_f\ge2$, reads [@Smilstern; @Toub99] $$\frac{\rho'(0)}{\rho(0)} =
  \frac {(N_f-2)(N_f+\beta)}
  {16\pi \beta N_f }\frac{\Sigma }{F^4}\:.$$ The result for $\beta =2$ was first derived by Smilga and Stern [@Smilstern] from the scalar susceptibility in standard chiral perturbation theory. We emphasize that this is an exact result for the QCD Dirac spectrum that is valid in the thermodynamic limit. The vanishing of the slope for $N_f =2$ has been confirmed by instanton liquid simulations [@Acta].

The two-point correlation function can also be obtained from a supersymmetric generating function with, in this case, two different spectral masses and two bosonic superpartners [@OTV]. Again the zero-momentum contribution coincides with the chUE result. Let us consider the perturbative expansion of the two-point correlation function. Generalizing Eq. ([\[discon\]](#discon){reference-type="ref" reference="discon"}), we obtain a relation between the two-point level correlation function and the pion susceptibility [@OTV; @carter], $$\langle \rho(\lambda) \rho(\lambda') \rangle^C =
  \frac 1{4\pi^2}\frac {\Sigma^2}{F^4}\left . {\rm Disc}
  \right |_{z = i\lambda, z'=i\lambda'}\sum_q\frac 1{(q^2 +M^2)^2},$$ where the meson mass is given by $M^2=(\sqrt{z^2}+\sqrt{z'^2})\Sigma/F^2$ and the superscript $C$ denotes the connected part of the two-point function. By taking the discontinuities of the zero-momentum contribution, we find the two-point correlation function [@OTV] $$\langle \rho(\lambda) \rho(\lambda') \rangle^C \sim
  -\frac 1{2\pi^2} \left [\frac 1{(\lambda-\lambda')^2}
  + \frac 1{(\lambda+\lambda')^2}\right ]\:,$$ which is the correct asymptotic result for the chUE.
