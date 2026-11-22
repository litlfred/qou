---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-044-44-euclidean-response-functions
section_title: "Euclidean Response Functions"
section_number: 4.4
pages: 110-116
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.988
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#SECresponse label="SECresponse"}

Response functions are important quantities ([@Carlson92a; @Benhar1994book; @Carlson94a; @Carlson02a; @sick2003meson; @Lovato13a; @Lovato15a]) and the related operators do not commute with $H$. Using PIMC to calculate the response functions thus has a natural advantage over diffusion methods.

In an electron-nucleus scattering experiment, the response of a weakly coupled external probe can be written as the function $S(k,\omega)$ which can be expanded in the energy eigenstates ([@Carlson94a]), as $$\begin{aligned}
S(k,\omega)=\frac{\sum_n \langle \Phi_0 | \rho^\dagger(\bm{k}) | \Phi_n \rangle \langle \Phi_n | \rho(\bm{k})| \Phi_0 \rangle  \delta(\omega+E_0-E_n)  }{\langle \Phi_0 | \Phi_0 \rangle} ,
\label{Skwdef}
\end{aligned}$$ where $\bm{k}$ is the momentum transfer between the final and initial momentum of the nucleus, and $\omega$ is the energy transfer which is the difference between the final and initial energy of the nucleus. $(k,\omega)$ is the four-momentum carried by the virtual photon ([@Bacca2014JPG]) which is exchanged between the electron and the nucleus. $E_n$ is eigenenergy of the excited states $|\Phi_n \rangle$, and the $\rho(\bm{k})$ is the coupling operator.

The $S(k,\omega)$ in Eq.([\[Skwdef\]](#Skwdef){reference-type="ref" reference="Skwdef"}) is called the response function. It is useful because it is related with the scattering cross section therefore directly connects theory and experiment. For different scattering processes the couplings of the probe to the nucleus gives different $\rho(\bm{k})$ operators. However, it is not easy to directly calculate the response function itself. Instead, we calculate the Euclidean response function $E(k,\tau)$ of $S(k,\omega)$ by using QMC, and then find ways ([@GShen2012PRC; @Lovato15a]) to invert $E(k,\tau)$ to $S(k,\omega)$.

The Euclidean response function $E(k,\tau)$ is related to $S(k,\omega)$ by the following Laplace transform, $$\begin{aligned}
E(k,\tau) &=
\int_{0}^{\infty} e^{-\tau(\omega-\omega_{qe})} S(k,\omega) d\omega \nonumber \\
&= \frac{e^{\omega_{qe}\tau} \sum_n \langle \Phi_0 | \rho^\dagger(\bm{k}) e^{-H \tau}  | \Phi_n \rangle \langle \Phi_n | \rho(\bm{k})| \Phi_0 \rangle   }
{ e^{-E_0 \tau} | \langle \Phi_0 | \Phi_0 \rangle} \nonumber \\
&=\frac{ e^{\omega_{qe}\tau} \langle \Phi_0| \rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k}) | \Phi_0 \rangle}{\langle \Phi_0| e^{-H\tau} | \Phi_0 \rangle} \nonumber \\
&=\frac{ e^{\omega_{qe}\tau} \langle \Psi_T | e^{-H \tau_1}
\left[\rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k})\right]
e^{-H \tau_1} | \Psi_T \rangle}
{\langle \Psi_T | e^{-H \tau_1} e^{-H\tau} e^{-H \tau_1} | \Psi_T \rangle},
\label{Ektauresponse}
\end{aligned}$$ where $\omega_{qe}=k^2/2m$ is the quasielastic energy transfer ([@lovato2020ab]) and $\tau_1$ is chosen to be large enough to project out the ground state $\Phi_0$.

In this work, we calculate the $^4$He Euclidean response functions that correspond to several different single-nucleon couplings $\rho(\bm{k})$, which are similar to those in Carlson and Schiavilla's 1994 paper ([@Carlson94a]). Those include the nucleon coupling $\rho_N (\bm{k})$ , proton coupling $\rho_p (\bm{k})$, isovector coupling $\rho_\tau (\bm{k})$, spin-longitudinal coupling $\rho_{\sigma \tau L} (\bm{k})$ and spin-transverse coupling $\rho_{\sigma \tau T} (\bm{k})$. They are defined as, $$\begin{aligned}
\rho_N (\bm{k}) & = \sum_{i=1}^{A} e^{i \bm{k} \cdot \bm{r}_i } , \\
\rho_p (\bm{k}) & = \sum_{i=1}^{A} e^{i \bm{k} \cdot \bm{r}_i } \frac{1+\tau_{iz}}{2} , \\
\rho_\tau (\bm{k}) & = \sum_{i=1}^{A} e^{i \bm{k} \cdot \bm{r}_i } \tau_{iz} , \\
\rho_{\sigma \tau L} (\bm{k}) & = \sum_{i=1}^{A} e^{i \bm{k} \cdot \bm{r}_i } (\bm{\sigma}_i \cdot \hat{\bm{k}}) \tau_{iz} , \\
\rho_{\sigma \tau T} (\bm{k}) & = \sum_{i=1}^{A} e^{i \bm{k} \cdot \bm{r}_i } (\bm{\sigma}_i \times \hat{\bm{k}}) \tau_{iz} .
\end{aligned}$$

Note that $\tau_{iz}$ is the difference between the proton and neutron projection operators, so it is related with the difference between protons and neutrons. $\bm{\sigma}_i \cdot \hat{\bm{k}}$ and $\bm{\sigma}_i \times \hat{\bm{k}}$ can be related with different mesons including pion, EM scattering, magnetic fields, etc ([@CarlsonRMP1998]).

In diffusion QMC such as GFMC and AFDMC, it is often $\langle \Psi_T |\rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k}) |\Phi_0 \rangle$ that is calculated. Since the operator $\rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k})$ does not commute with the Hamiltonian, $\langle \Psi_T |\rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k}) |\Phi_0 \rangle$ is mostly a mixed estimator (although forward walking extrapolation can improve this) instead of the true ground state estimator $\langle \Phi_0 |\rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k}) |\Phi_0 \rangle$. This disadvantage of diffusion QMC is exactly the advantage of PIMC method, because PIMC can project out the ground state $\Phi_0$ from both $\langle \Psi_T |$ and $| \Psi_T \rangle$ by using the projection operator $e^{-H \tau_1}$ with the short-time approximation. PIMC really calculates the ground state estimator $\langle \Phi_0| \rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k}) | \Phi_0 \rangle$, whether $\rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k})$ commutes with the Hamiltonian or not.

<figure id="PIMCBeadsResponse">
<embed src="Figures/PIMCBeadsResponse.eps" />
<figcaption>Illustration of <span class="math inline"><em>g</em><sub><em>l</em><em>r</em>, <em>M</em></sub><sup><em>V</em></sup>(ℛ)</span> in Eq.(<a href="#gVRlrresponse" data-reference-type="ref" data-reference="gVRlrresponse">[gVRlrresponse]</a>) for Euclidean response functions.</figcaption>
</figure>

The calculations of $E(k,\tau)$ in PIMC is straightforward. Eq.([\[Ektauresponse\]](#Ektauresponse){reference-type="ref" reference="Ektauresponse"}) can be recast into the form of Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}. As illustrated in Fig. [1](#PIMCBeadsResponse){reference-type="ref" reference="PIMCBeadsResponse"}, we can denote the total imaginary time as $\tau_{\textrm{tot}}=N\Delta \tau$, and $\tau_1=L \Delta \tau$, $L=N-M$, $\tau=(M-L)\Delta \tau =(2M-N) \Delta \tau$. We just need to place the operator $\rho^\dagger(\bm{k})$ at bead $L$, and place $\rho (\bm{k})$ at bead $M$, and $g^V_{lr,M}(\mathcal{R})$ can be written as, $$g^V_{lr,M}(\mathcal{R}) = e^{\omega_{qe}\tau}   \langle \psi^l_{L\!-\!1}  (\mathcal{R}) |
 e^{\frac{- \mathcal{V}_L  \Delta \tau }{2}} \rho^\dagger(\bm{k}) e^{-V\tau} \rho(\bm{k}) e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}}
 | \psi^r_{M\!+\!1} (\mathcal{R}) \rangle ,
\label{gVRlrresponse}$$ where $e^{-V\tau}$ is defined as, $$\begin{aligned}
e^{-V\tau} \! \equiv
 e^{\frac{- \mathcal{V}^\dagger_L  \Delta \tau }{2}} \bm{\mathcal{G}}
 \left(e^{\frac{- \mathcal{V}_{L+1}  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_{L+1}  \Delta \tau }{2}}\right) \bm{\mathcal{G}} ~...~
 \bm{\mathcal{G}} \left(e^{\frac{- \mathcal{V}_{M-1}  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_{M-1}  \Delta \tau }{2}} \right)\bm{\mathcal{G}}
 e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}}  .
\label{eVtaudef}
\end{aligned}$$ All the other functions and calculations are the same as those in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}.

The ground state of $^4$He has total isospin and its z component both 0, and it is a spherically symmetric object. Therefore the response functions do not depend on the direction of $\bm{k}$. So when calculating the $E(k,\tau)$, the momentum $\bm{k}$ can be averaged over all the directions. The angle averaged response functions are not calculated on the fly because they are relatively more time-consuming comparing with other quantities, so they are calculated after we have enough paths stored on the storage systems. For a given amount of computation time, the angle averaged $E(k,\tau)$ have less variance than the non angle averaged $E(k,\tau)$. The angle averaged $E(k,\tau)$ is calculated as, $$\begin{aligned}
E(k,\tau) = \frac{ e^{\omega_{qe}\tau} \langle \Psi_T | e^{-H \tau_1}
\left[\frac{1}{4\pi}\int \rho^\dagger(\bm{k}) e^{-H\tau} \rho(\bm{k}) d\Omega\right]
e^{-H \tau_1} | \Psi_T \rangle}
{\langle \Psi_T | e^{-H \tau_1} e^{-H\tau} e^{-H \tau_1} | \Psi_T \rangle},
\label{Ektauresponseave}
\end{aligned}$$ so that the correspondingly $g^V_{lr,M}(\mathcal{R})$ is calculated as[^1], $$\begin{aligned}
\!\! g^V_{lr,M}(\mathcal{R}) = e^{\omega_{qe}\tau}   \langle \psi^l_{L\!-\!1}  (\mathcal{R}) | \bm{\mathcal{G}}  e^{\frac{- \mathcal{V}_L  \Delta \tau }{2}}
 \left[ \frac{  \int \rho^\dagger(\bm{k}) e^{-V\tau} \rho(\bm{k})  d \Omega}{4\pi} \right]
 e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}} \bm{\mathcal{G}}
 | \psi^r_{M\!+\!1} (\mathcal{R}) \rangle,
\label{gVRlrresponseave}
\end{aligned}$$ where $e^{-V\tau}$ is defined in Eq.([\[eVtaudef\]](#eVtaudef){reference-type="ref" reference="eVtaudef"}). For any operator $\hat{O}$ which is independent of $\bm{k}$, e.g., $\hat{O}$ can be $e^{-H\tau}$ or $e^{-V\tau}$ as defined in Eq.([\[eVtaudef\]](#eVtaudef){reference-type="ref" reference="eVtaudef"}).

<figure id="response">
<embed src="Figures/response.eps" />
<figcaption>Angle averaged Euclidean response functions of <span class="math inline"><sup>4</sup></span>He at <span class="math inline"><em>k</em> = 350 MeV/c</span> for the AV6’ interaction.</figcaption>
</figure>

<figure id="responseN2LO">
<embed src="Figures/responseN2LO.eps" />
<figcaption>Angle averaged Euclidean response functions of <span class="math inline"><sup>4</sup></span>He at <span class="math inline"><em>k</em> = 350 MeV/c</span> for the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction.</figcaption>
</figure>

Fig. [2](#response){reference-type="ref" reference="response"} and Fig [3](#responseN2LO){reference-type="ref" reference="responseN2LO"} shows all the angle averaged Euclidean response functions $E_\alpha$ for each $\rho_\alpha$ defined in this work. Fig. [2](#response){reference-type="ref" reference="response"} is for the AV6' interaction and Fig [3](#responseN2LO){reference-type="ref" reference="responseN2LO"} is for the local chiral N$^2$LO interaction. Each of the $E_\alpha$ has been normalized such that $\lim_{k\rightarrow \infty} E_\alpha(k,\tau=0)=1$. Our calculations are done in the center of mass frame, but we have converted our results to the lab frame[^2]. We calculate our response functions in the center of mass frame first because it can give lower variance compare with lab frame. We then multiply our results by $e^{- 16.3\tau}$ (the 16.3 MeV is the center of mass energy for this $k=350\textrm{ MeV/c}$) in order to compare with the results in Carlson and Schiavilla's paper ([@Carlson94a]) which are digitized as the red dots in Figs. [2](#response){reference-type="ref" reference="response"} and [3](#responseN2LO){reference-type="ref" reference="responseN2LO"}. The small difference between ours and theirs comes from several sources. First, we use PIMC, they use GFMC. Second, the interactions are somewhat different, they used the Argonne $v8$ interaction combined with the Urbana model-. Third, we use $\tau_{iz}$ in stead of $\tau_+(i)$ for the isovector, spin-longitudinal and spin-transverse couplings, this is suggested in their paper when dealing with an isoscalar target like the ground state $^4$He, and with interactions that conserve the number of protons and neutrons. The small difference can also indicate our results are more accurate because in PIMC we do not need forward walking as DMC does.

[^1]: The detailed angle averaged calculations of $\int \rho^\dagger(\bm{k}) \hat{O} \rho(\bm{k}) d \Omega/4\pi$ for each response function can be found in Appendix [\[secAngleAveResponse\]](#secAngleAveResponse){reference-type="ref" reference="secAngleAveResponse"}.

[^2]: See Appendix [\[secResconvert\]](#secResconvert){reference-type="ref" reference="secResconvert"} for the conversion process.
