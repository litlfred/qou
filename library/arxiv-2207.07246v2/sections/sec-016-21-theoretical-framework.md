---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-016-21-theoretical-framework
section_title: "Theoretical Framework"
section_number: 2.1
pages: 24-29
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.988
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#TheoFrame label="TheoFrame"} PIMC directly calculates the expectation value of an operator $\langle \hat{O} \rangle$ as $$\langle \hat{O} \rangle= \frac{  \langle \Psi_T| e^{-H \tau_1}  \hat{O} e^{-H \tau_2 } | \Psi_T \rangle  }
{\langle \Psi_T| e^{-H \tau} | \Psi_T \rangle}, \label{PIMCopexp}$$ where $\tau_i$ is an imaginary time and the total imaginary time $\tau=\tau_1+\tau_2$. $\Psi_T$ is a trial wave function and it can serve as the initial state of the system. $H$ is the Hamiltonian of the system, $$H=T+V, \label{HTV}$$ where $T$ and $V$ are kinetic and potential energy operators. Since the operator $\hat{O}$ is Hermitian, the numerator and denominator in Eq.([\[PIMCopexp\]](#PIMCopexp){reference-type="ref" reference="PIMCopexp"}) are real, so in PIMC it is actually calculated as, $$\langle \hat{O} \rangle
= \frac{ Re  \langle \Psi_T| e^{-H \tau_1}  \hat{O} e^{-H \tau_2 } | \Psi_T \rangle  }
{ Re \langle \Psi_T| e^{-H \tau} | \Psi_T \rangle} .
\label{PIMCopexpdetail}$$

On the one hand, if $\tau_i=0$, Eq.([\[PIMCopexp\]](#PIMCopexp){reference-type="ref" reference="PIMCopexp"}) becomes, $$\langle \hat{O} \rangle  = \frac{ \langle \Psi_T | \hat{O}   | \Psi_T  \rangle }   { \langle \Psi_T | \Psi_T  \rangle  }
=\frac{ Re \langle \Psi_T | \hat{O}   | \Psi_T  \rangle }   { Re \langle \Psi_T | \Psi_T  \rangle  } , \label{VMCoexp}$$ so PIMC becomes VMC which gives an upper bound to the true ground state energy.

On the other hand, the trial state $| \Psi_T \rangle$ can be written as the linear combination of the eigenstates $|\Phi_n\rangle$ of the Hamiltonian whose eigenvalues are $E_n$, and with corresponding amplitude $a_n$ such that, $$|\Psi_T \rangle = \sum_{n=0}^{\infty} a_n |\Phi_n\rangle .
\label{PsiTexpansion}$$ After operating with the propagator $e^{-H \tau_1}$, $| \Psi_T \rangle$ becomes, $$e^{-H \tau_1} |\Psi_T \rangle =
a_0e^{-E_0 \tau_1}
\left[   | \Phi_0 \rangle  + \sum_{i=1}^{\infty}\frac{a_i}{a_0}e^{-(E_i-E_0) \tau_1} | \Phi_i \rangle \right].
\label{eHPsiT}$$

Therefore, if $\tau_i$ is big enough, the factor $e^{-(E_i-E_0) \tau_1}$ will make all the excited states negligible compared with the ground state $| \Phi_0 \rangle$, and we find that, $$\lim_{\tau_i \rightarrow \infty } e^{-H \tau_i} | \Psi_T  \rangle \propto | \Phi_0 \rangle.$$

So, $e^{-H \tau_i} | \psi_T \rangle$ project out the ground state $| \Phi_0 \rangle$. In this case Eq.([\[PIMCopexp\]](#PIMCopexp){reference-type="ref" reference="PIMCopexp"}) will become the ground state expectation value of $\hat{O}$, $$\langle \hat{O} \rangle  = \frac{ \langle \Phi_0 | \hat{O}   | \Phi_0  \rangle }   { \langle \Phi_0 | \Phi_0  \rangle  }
=\frac{ Re \langle \Phi_0 | \hat{O}   | \Phi_0  \rangle }   { Re \langle \Phi_0 | \Phi_0  \rangle  }. \label{PIMCopgndexp}$$

In all kinds of calculations, however, it is usually not easy to directly sample the whole exact propagator $e^{-H \tau_i}$. Instead, we break $\tau_i$ into $N_i$ pieces of time step $\Delta \tau$ such that $\tau_i=N_i \Delta \tau$, and the whole propagator can be written as a product of $N_i$ short-time propagator $e^{-H \Delta \tau}$, $$e^{-H \tau_i}=  (e^{-H \Delta \tau})^{N_i} . \label{wholepropagator}$$

Typically we approximate $e^{-H \Delta \tau}$ using a Trotter breakup ([@SchmidtLee95a]), $$e^{-H \Delta \tau}  \approx e^{-\frac{V}{2} \Delta \tau}e^{- T \Delta \tau}e^{- \frac{V}{2} \Delta \tau} ,
\label{Trotter}$$ where each of the terms $e^{-\frac{V}{2} \Delta \tau}$ and $e^{- T \Delta \tau}$ can be calculated exactly or well approximated, as shown later.

If we want to calculate ground state properties, we need to use a sufficiently large $\tau_i$ first such that $e^{-H \tau_i}$ can project out the ground state $|\Phi_0\rangle$, then we choose a proper $N_i$ to make sure $\Delta \tau$ is small enough such that time step error are negligible for the quantity we want to calculate. However, if $\Delta \tau$ is too small it can cost an unnecessary large amount of computational resources, because then we need a very big $N_i$ which means many short-time propagators $e^{-H \Delta \tau}$. Therefore, time step $\Delta \tau$ should be set at a reasonable point between accuracy and computational cost.

Once $\tau_i$, $\Delta \tau$ and $N_i$ are chosen, then we apply Eq.([\[wholepropagator\]](#wholepropagator){reference-type="ref" reference="wholepropagator"}) in Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}) such that we accurately multiply the $N_i$ short-time propagators $e^{-H \Delta \tau}$ together to replace $e^{-H \tau_i}$, and therefore the sampling of Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}) will be equivalent with Eq.([\[PIMCopgndexp\]](#PIMCopgndexp){reference-type="ref" reference="PIMCopgndexp"}) the ground state calculation. So we calculate Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}) by choosing a sufficiently large $\tau_1$ and $\tau_2$ first (usually we set $\tau_1=\tau_2$), then replacing $e^{-H \tau_1}$ and $e^{-H \tau_2}$ with corresponding $(e^{-H \Delta \tau})^{N_1}$ and $(e^{-H \Delta \tau})^{N_2}$ such that, $$\langle \hat{O} \rangle
= \frac{ Re  \langle \Psi_T| e^{-H \Delta \tau}...e^{-H \Delta \tau} \hat{O} e^{-H \Delta \tau} ...e^{-H \Delta \tau}| \Psi_T \rangle  }
{ Re \langle \Psi_T| e^{-H \Delta \tau}...e^{-H \Delta \tau} e^{-H \Delta \tau} ...e^{-H \Delta \tau} | \Psi_T \rangle} .
\label{PIMCopexpdetailshorttime}$$

Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}) is basically how PIMC works. As we can see from Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}), a PIMC calculation not only depends on the operator $\hat{O}$, but also depends on the Hamiltonian $\hat{H}$, the trial wave function $\Psi_T$ and the short-time propagator $e^{-H \Delta \tau}$. All of them will be introduced one by one in the following sections.

As to the operator $\hat{O}$, on the one hand, it may commute with the Hamiltonian. In this case, $\hat{O}$ can be moved to the leftmost or the rightmost position, and Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}) can then be written as the average of the two, $$\langle \hat{O} \rangle
= \frac{
\frac{1}{2}  Re \! \left( \!   \langle \Psi_T| \hat{O} e^{-H \tau}  | \Psi_T \rangle
\! + \!
 \langle \Psi_T|  e^{-H \tau} \hat{O} | \Psi_T \rangle
\! \right)
 }
{  Re \langle \Psi_T| e^{-H \tau} | \Psi_T \rangle}
.
\label{PIMCopexpdetailOH}$$ This is useful when the application of the operator on the trial wave function is simpler than its application directly on the propagator $e^{-H \tau}$, or has lower variance.

On the other hand, however, the operator $\hat{O}$ can also be other operators which do not commute with $H$. In fact, a big advantage of PIMC is that it can directly deal with operators which do not commute with $H$, while diffusion based QMC methods like GFMC and AFDMC cannot easily do so without tradeoff.

Because, fundamentally speaking, unlike Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}), all the diffusion based QMC are trying to use a large enough total imaginary time $\tau_d$ in $e^{-H \tau_d }$ to project out the ground state and calculate the following quantity, $$\langle \hat{O} \rangle
= \frac{ Re  \langle \Psi_T| \hat{O} e^{-H \tau_d } | \Psi_T \rangle  }
{ Re \langle \Psi_T| e^{-H \tau_d} | \Psi_T \rangle}
=\frac{ Re  \langle \Psi_T| \hat{O} | \Phi_0 \rangle  }
{ Re \langle \Psi_T | \Phi_0 \rangle},
\label{DMCopexpdetail}$$ which is called mixed estimator[^1]. It works fine as long as $\hat{O}$ commutes with $H$. However if $\hat{O}$ does not commute with $H$, diffusion based QMC cannot directly calculate the ground state of $\langle \hat{O} \rangle$, and often the mixed estimator along with extrapolation of the errors ([@HammondMCbook]) are used instead. However, the extrapolated mixed estimator is not as accurate as the true ground state estimator Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}). And in fact, a lot of operators do not commute with $H$, and they can only be accurately and directly calculated by PIMC (or higher variance forward walking additions to diffusion methods). That is one of the main reasons to choose PIMC.

<figure id="rhopimcdmc">
<embed src="Figures/rhopimcdmc.eps" />
<figcaption>Comparison between PIMC and DMC 4-particle calculations for one-particle number density <span class="math inline"><em>ρ</em>(<em>r</em>)</span> using 3 different trial wave function (<span class="citation" data-cites="ZABOLITZKY1981114"></span>) and with Malfliet-Tjon interaction (<span class="citation" data-cites="MALFLIET1969161"></span>).</figcaption>
</figure>

Fig. [1](#rhopimcdmc){reference-type="ref" reference="rhopimcdmc"} is an example to illustrate the advantage of PIMC. The one-particle number density operator $\hat{O}=\hat{\rho}(r)$ whose definition is Eq.([\[rhordef\]](#rhordef){reference-type="ref" reference="rhordef"}) does not commute with $H$, therefore straightforward DMC can only calculate the mixed estimator of $\rho(r)$ which is different from the exact $\rho(r)$. As one can see from Fig. [1](#rhopimcdmc){reference-type="ref" reference="rhopimcdmc"}, in the 4-particle system, using three different trial wave function $\Psi_T$ marked as Nr.1, Nr.2 and Nr.3, the extrapolated estimator $\rho(r)$ from DMC are different with each other and none of them is the true ground state expectation value[^2]. However, no matter which of the 3 trial wave functions $\Psi_T$ are used, the $\rho(r)$ projected out by PIMC are the same within error bar, which means they are the true ground state $\rho(r)$. Obviously the PIMC results are more reliable than the DMC in this case.

It needs to be pointed out that, due to the fact that $T$ and $V$ do not commute with each other as well as $V$ is usually non-trivial, we use approximated short-time propagator $U(\Delta \tau) \approx e^{-H \Delta \tau}$ in the calculation instead of $e^{-H \Delta \tau}$. And $U(\Delta \tau)$ and $e^{-H \Delta \tau}$ are different by a time step $\Delta \tau$ error, $$U(\Delta \tau) = e^{-H \Delta \tau} + \mathcal{O}(\Delta \tau^l),$$ where different choices of $U(\Delta \tau)$ will give different integer $l$, and the error between the approximate short-time propagator $U(\Delta \tau)$ and exact short-time propagator $e^{-H \Delta \tau}$ is of $\Delta \tau^l$ order.

Therefore, what we really calculate in PIMC is $\langle O(\Delta \tau) \rangle$, which is an approximation of the true expectation value $\langle O \rangle$ in Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}), $$\langle \hat{O} (\Delta \tau) \rangle
= \frac{ Re  \langle \Psi_T| [U(\Delta \tau)]^{N_1} \hat{O} [U(\Delta \tau)]^{N_2}| \Psi_T \rangle  }
{ Re \langle \Psi_T| [U(\Delta \tau)]^{N_1+N_2} | \Psi_T \rangle} .
\label{PIMCopexpdetailshorttimeapprox}$$ In the limit of the time step $\Delta \tau$ becomes zero, $\langle O(\Delta \tau) \rangle$ will be the same as $\langle O \rangle$, $$\lim_{\Delta \tau \rightarrow 0}\langle \hat{O} (\Delta \tau) \rangle
= \langle O \rangle .$$ So we need to calculate $\langle O(\Delta \tau) \rangle$ for different time step $\Delta \tau$, then extrapolate the $\langle O(\Delta \tau) \rangle$ at $\Delta \tau=0$ in order to find the true expectation value $\langle O \rangle$. If the operator $\hat{O}$ in Eq.([\[PIMCopexpdetailshorttimeapprox\]](#PIMCopexpdetailshorttimeapprox){reference-type="ref" reference="PIMCopexpdetailshorttimeapprox"}) is placed exactly at the middle of the path such that $N_1=N_2$, the PIMC will essentially be equivalent with VMC whose trial function is $[U(\Delta \tau)]^{\frac{N}{2}}| \Psi_T \rangle$, in this case $\langle O(\Delta \tau) \rangle$ will be the upper bound of the true expectation $\langle O \rangle$.

[^1]: It can be seen from Eq.([\[DMCopexpdetail\]](#DMCopexpdetail){reference-type="ref" reference="DMCopexpdetail"}) that the DMC total imaginary time $\tau_d$ can be just half of the PIMC total imaginary time $\tau$, $\tau_d=0.5 \tau$, because DMC project out the ground state only from one side while PIMC does so from both sides.

[^2]: the DMC results are obtained by using the extrapolated estimator Eq.([\[Apest\]](#Apest){reference-type="ref" reference="Apest"}).
