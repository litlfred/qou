---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "arXiv:nucl-th/0103005v2 6 Mar 2001"
section_id: sec-003-4-greens-function-monte-carlo
section_title: "GREEN'S FUNCTION MONTE CARLO"
section_number: 4
pages: 15-20
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.984
doc_brief: "arXiv:nucl-th/0103005v2 6 Mar 2001 — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear Hamiltonians that"
---
The GFMC method [@C87; @C88] projects out the exact lowest-energy state, $\Psi_{0}$, for a given set of quantum numbers, using $\Psi_0 = \lim_{\tau \rightarrow \infty} \exp [ - ( H - E_0) \tau ] \Psi_T$, where $\Psi_{T}$ is an initial trial function. If the maximum $\tau$ actually used is large enough, the eigenvalue $E_{0}$ is calculated exactly while other expectation values are generally calculated neglecting terms of order $|\Psi_{0}-\Psi_{T}|^{2}$ and higher [@PPCPW97]. In contrast, the error in the variational energy, $E_{V}$, is of order $|\Psi_{0}-\Psi_{T}|^{2}$, and other expectation values calculated with $\Psi_{T}$ have errors of order $|\Psi_{0}-\Psi_{T}|$. In the following we present a brief overview of modern nuclear GFMC methods; much more detail may be found in Refs. [@PPCPW97; @WPCP00].

We start with the $\Psi_{T}$ of Eq.([\[eq:psitgfmc\]](#eq:psitgfmc){reference-type="ref" reference="eq:psitgfmc"}) and define the propagated wave function $\Psi(\tau)$ $$\begin{aligned}
   \Psi(\tau) = e^{-({H}-E_{0})\tau} \Psi_{T}
              = \left[e^{-({H}-E_{0})\triangle\tau}\right]^{n} \Psi_{T} \ ,
\end{aligned}$$ where we have introduced a small time step, $\tau=n\triangle\tau$; obviously $\Psi(\tau=0) =  \Psi_{T}$ and $\Psi(\tau \rightarrow \infty) = \Psi_{0}$. The $\Psi (\tau)$ is represented by a vector function of $\bf R$ using Eq.([\[eq:psivec\]](#eq:psivec){reference-type="ref" reference="eq:psivec"}), and the Green's function, $G_{\alpha\beta}({\bf R},{\bf R}^{\prime})$ is a matrix function of $\bf R$ and ${\bf R}^{\prime}$ in spin-isospin space, defined as $$G_{\alpha\beta}({\bf R},{\bf R}^{\prime})= \langle {\bf
R},\alpha|e^{-({H}-E_{0})\triangle\tau}|{\bf R}^{\prime},\beta\rangle \ .
\label{eq:gfunction}$$ It is calculated with leading errors of order $(\triangle\tau)^{3}$. Omitting the spin-isospin indices $\alpha$, $\beta$ for brevity, $\Psi({\bf R}_{n},\tau)$ is given by $$\Psi({\bf R}_{n},\tau) = \int G({\bf R}_{n},{\bf R}_{n-1})\cdots G({\bf
R}_{1},{\bf R}_{0})\Psi_{T}({\bf R}_{0})d{\bf R}_{n-1}\cdots d{\bf R}_{1}d{\bf
R}_{0} \ ,
\label{eq:gfmcpsi}$$ with the integral being evaluated stochastically.

The short-time propagator should allow as large a time step $\triangle\tau$ as possible, because the total computational time for propagation is proportional to $1/\triangle\tau$. Earlier calculations [@PPCW95; @C87; @C88] used the propagator obtained from the Feynman formulae in which the kinetic and potential energy terms of $H$ are separately exponentiated. The main error in this approximation to $G_{\alpha,\beta}$ comes from terms in $e^{-{H}\triangle\tau}$ having multiple $v_{ij}$, like $v_{ij}Kv_{ij}(\triangle\tau)^{3}$, where $K$ is the kinetic energy, which can become large when particles $i$ and $j$ are very close due to the large repulsive core in $v_{ij}$. This requires a rather small $\triangle\tau \sim 0.1$ GeV$^{-1}$.

It has been found in studies of bulk helium atoms [@C95] that including the exact two-body propagator allows much larger time steps. This short-time propagator is $$\begin{aligned}
G_{\alpha\beta}({\bf R},{\bf R}^{\prime}) &=& G_{0}({\bf R},{\bf
R}^{\prime})\langle\alpha|\left[{\cal S}\prod_{i<j}\frac{g_{ij}({\bf
r}_{ij},{\bf r}_{ij}^{\prime})}{g_{0,ij}({\bf r}_{ij},{\bf r}_{ij}^{\prime})}
\right] |\beta\rangle \ ,
\end{aligned}$$ where $$\begin{aligned}
G_{0}({\bf R},{\bf R}^{\prime}) &=& \langle {\bf R}|e^{-{K}\triangle\tau}|{\bf
R}^{\prime}\rangle =  \left[ \sqrt{\frac{m}
{2\pi\hbar^{2} \triangle\tau}}\, \right]^{3A}\exp\left[\frac{-({\bf R}-{\bf
R}^{\prime})^2}{2\hbar^{2}\triangle\tau/m}\right] \ ,
\label{eq:propagator2}
\end{aligned}$$ $g_{ij}$ is the exact two-body propagator, $$\begin{aligned}
g_{ij}({\bf r}_{ij},{\bf r}_{ij}^{\prime}) = \langle{\bf
r}_{ij}|e^{-H_{ij}\triangle\tau}|{\bf r}_{ij}^{\prime}\rangle \ ,
\label{eq:gij}
\end{aligned}$$ and $g_{0,ij}$ is the free two-body propagator. All terms containing any number of the same $v_{ij}$ and $K$ are treated exactly in this propagator, as we have included the imaginary-time equivalent of the full two-body scattering amplitude. It still has errors of order $(\triangle\tau)^{3}$, however they are from commutators of terms like $v_{ij}Kv_{ik}(\triangle\tau)^{3}$ which become large only when both pairs $ij$ and $ik$ are close. Because this is a rare occurrence, a five times larger time step, $\triangle\tau \sim 0.5$ GeV$^{-1}$, can be used [@PPCPW97].

Including the three-body forces and the $E_{0}$ in Eq.([\[eq:gfunction\]](#eq:gfunction){reference-type="ref" reference="eq:gfunction"}), the complete propagator is given by $$\begin{aligned}
G_{\alpha\beta}({\bf R},{\bf R}^{\prime})& = &e^{E_{o}\triangle\tau}G_{0}({\bf
R},{\bf R}^{\prime})\exp[{- \sum (V^{R}_{ijk}({\bf R})+ V^{R}_{ijk}({\bf
R^{\prime}}))\frac{\triangle\tau}{2}}] \nonumber \\
& & \langle\alpha|I_{3}({\bf R})|\gamma\rangle\langle\gamma|\left[{\cal
S}\prod_{i<j}\frac{g_{ij}({\bf r}_{ij},{\bf r}_{ij}^{\prime})}
{g_{0,ij}({\bf r}_{ij},{\bf r}_{ij}^{\prime})} \right] 
|\delta\rangle\langle\delta|I_{3}({\bf
R}^{\prime})|\beta\rangle~,
\label{eq:fullprop}
\end{aligned}$$ where $$\begin{aligned}
I_{3}({\bf R}) = \left[1 - \frac{\triangle\tau}{2}\sum V^{\pi}_{ijk}({\bf
R})\right]~.
\end{aligned}$$ and $V^{\pi}_{ijk}=V^{2\pi}_{ijk}+V^{3\pi}_{ijk}$ represents, in general, all non-central $V_{ijk}$ terms. With the exponential of $V^{\pi}_{ijk}$ expanded to first order in $\triangle\tau$, there are additional error terms of the form $V^{\pi}_{ijk}V^{\pi}_{i'j'k'}(\triangle\tau)^{2}$. However, they have negligible effect because $V^{\pi}_{ijk}$ has a magnitude of only a few MeV.

Quantities of interest are evaluated in terms of a "mixed" expectation value between $\Psi_T$ and $\Psi(\tau)$: $$\begin{aligned}
\langle O \rangle_{\rm Mixed} & = & \frac{\langle \Psi_{T} | O |
\Psi(\tau)\rangle}{\langle \Psi_{T} | \Psi(\tau)\rangle} \nonumber \\
& = & \frac{ \int d {\bf P}_n
\Psi_{T}^{\dagger}({\bf R}_{n}) O G({\bf R}_{n},{\bf
R}_{n-1})\cdots G({\bf R}_{1},{\bf R}_{0})\Psi_{T}({\bf R}_{0})}
{\int d{\bf P}_{n} \Psi_{T}^{\dagger}
({\bf R}_{n})G({\bf R}_{n},{\bf R}_{n-1}) \cdots G({\bf
R}_{1},{\bf R}_{0})\Psi_{T}({\bf R}_{0})}~,
\label{eq:expectation}
\end{aligned}$$ where ${\bf P}_{n} = {\bf R}_{0},{\bf R}_{1},\cdots,{\bf R}_{n}$ denotes the 'path', and $d{\bf P}_{n} = d{\bf R}_{0} d{\bf R}_{1}\cdots d{\bf R}_{n}$ with the integral over the paths being carried out stochastically. The desired expectation values would, of course, have $\Psi(\tau)$ on both sides; by writing $\Psi(\tau) = \Psi_{T} + \delta\Psi(\tau)$ and neglecting terms of order $[\delta\Psi(\tau)]^2$, we obtain the approximate expression $$\begin{aligned}
\langle O (\tau)\rangle =
\frac{\langle\Psi(\tau)| O |\Psi(\tau)\rangle}
{\langle\Psi(\tau)|\Psi(\tau)\rangle}
\approx \langle O (\tau)\rangle_{\rm Mixed}
     + [\langle O (\tau)\rangle_{\rm Mixed} - \langle O \rangle_T] ~,
\label{eq:pc_gfmc}
\end{aligned}$$ where $\langle O \rangle_T$ is the variational expectation value. More accurate evaluations of $\langle O (\tau)\rangle$ are possible [@K67], essentially by measuring the observable at the mid-point of the path. However, such estimates require a propagation twice as long as the mixed estimate and require separate propagations for every $\langle O \rangle$ to be evaluated. The nuclear calculations published to date use the approximation of Eq.([\[eq:pc_gfmc\]](#eq:pc_gfmc){reference-type="ref" reference="eq:pc_gfmc"}).

A special case is the expectation value of the Hamiltonian. The $\langle{H}(\tau)\rangle_{\rm Mixed}$ can be re-expressed as [@CK79] $$\begin{aligned}
\langle{H}(\tau)\rangle_{\rm Mixed} = \frac{\langle \Psi_{T} |
e^{-({H}-E_{0})\tau /2}{H} e^{-({H}-E_{0})\tau /2} |
\Psi_{T}\rangle}{\langle \Psi_{T} |e^{-({H}-E_{0})\tau /2}
e^{-({H}-E_{0})\tau /2}| \Psi_{T}\rangle} \geq E_{0}~,
\end{aligned}$$ since the propagator $\exp [ - (H - E_0) \tau ]$ commutes with the Hamiltonian. Thus $\langle{H}(\tau)\rangle_{\rm Mixed}$ approaches $E_{0}$ in the limit $\tau\rightarrow\infty$, and the expectation value obeys the variational principle for all $\tau$.

The AV18 interaction contains terms that are quadratic in orbital angular momentum, $L$. These terms are, in essence, state- and position-dependent modifications of the mass of the nucleons. If they are included in the calculation of $g_{ij}$, then the ratio $g_{ij}/g_{0,ij}$ in Eq.([\[eq:propagator2\]](#eq:propagator2){reference-type="ref" reference="eq:propagator2"}) becomes unbounded for large $|{\bf r}_{ij}|$ or $|{\bf r}_{ij}^{\prime}|$ and the Monte Carlo statistical error will also be unbounded. Hence the GFMC propagator is constructed with a simpler isoscalar interaction, $H^{\prime}$, with a $v^{\prime}_{ij}$ that has only eight operator terms, $[1, \boldsigma_{i}\cdot\boldsigma_{j}, S_{ij}, {\bf L\cdot S}]\otimes
[1, \boldtau_{i}\cdot\boldtau_{j}]$, chosen such that it equals the CI part of the full interaction in all S- and P-waves and in the deuteron. The $v^{\prime}_{ij}$ is a little more attractive than $v_{ij}$, so a $V^{\prime}_{ijk}$ adjusted so that $\langle H^{\prime} \rangle \approx \langle H \rangle$ is also used. This ensures the GFMC algorithm will not propagate to excessively large densities due to overbinding. Consequently, the upper bound property applies to $\langle{H}^{\prime}(\tau)\rangle$, and $\langle H-H^{\prime} \rangle$ must be evaluated perturbatively.

Another complication that arises in the GFMC algorithm is the "fermion sign problem". This arises from the stochastic evaluation of the matrix elements in Eq.([\[eq:expectation\]](#eq:expectation){reference-type="ref" reference="eq:expectation"}). The $G({\bf R}_{i},{\bf R}_{i-1})$ is a local operator and can mix in the boson solution. This has a (much) lower energy than the fermion solution and thus is exponentially amplified in subsequent propagations. In the final integration with the antisymmetric $\Psi_T$, the desired fermionic part is projected out, but in the presence of large statistical errors that grow exponentially with $\tau$. Because the number of pairs that can be exchanged grows with $A$, the sign problem also grows exponentially with increasing $A$. For $A{\geq}8$, the errors grow so fast that convergence in $\tau$ cannot be achieved.

For simple scalar wave functions, the fermion sign problem can be controlled by not allowing the propagation to move across a node of the wave function. Such "fixed-node" GFMC provides an approximate solution which is the best possible variational wave function with the same nodal structure as $\Psi_T$. However, a more complicated solution is necessary for the spin- and isospin-dependent wave functions of nuclei. In the last few years a suitable "constrained path" approximation has been developed and extensively tested, first for condensed matter systems [@ZCG95] and more recently for nuclei [@WPCP00]. The basic idea of the constrained-path method is to discard those configurations that, in future generations, will contribute only noise to expectation values. If the exact ground state $| \Psi_0 \rangle$ were known, any configuration for which $$\Psi({\bf P}_n)^\dagger \Psi_0({\bf R}_n) = 0 \ ,
\label{eq:gfmc:const_config}$$ where a sum over spin-isospin states is implied, could be discarded. Here ${\bf P}_n$ designates the complete path, $({\bf R}_0, ..., {\bf R}_n)$ that has led to ${\bf R}_n$. The sum of these discarded configurations can be written as a state $| \Psi_d \rangle$, which obviously has zero overlap with the ground state. The $\Psi_d$ contains only excited states and should decay away as $\tau \rightarrow \infty$, thus discarding it is justified. Of course the exact $\Psi_0$ is not known, and so configurations are discarded with a probability such that the average overlap with the trial wave function, $$\langle \Psi_d | \Psi_T \rangle = 0 \ .$$ Many tests of this procedure have been made [@WPCP00] and it usually gives results that are consistent with unconstrained propagation, within statistical errors. However a few cases in which the constrained propagation converges to the wrong energy (either above or below the correct energy) have been found. Therefore a small number, $n_u=10$ to 20, unconstrained steps are made before evaluating expectation values. These few unconstrained steps, out of typically 400 total steps, appear to be enough to damp out errors introduced by the constraint, but do not greatly increase the statistical error.

<figure id="fig:8be-e_of_tau">

<figcaption>GFMC <span class="math inline"><em>E</em>(<em>τ</em>)</span> using AV18/UIX for various states of <span class="math inline"><sup>8</sup></span>Be. Averages with their standard errors are shown by the solid and dashed lines.</figcaption>
</figure>

Figure [1](#fig:8be-e_of_tau){reference-type="ref" reference="fig:8be-e_of_tau"} shows the progress with increasing $\tau$ of typical constrained GFMC calculations, in this case for various states of $^8$Be. The values shown at $\tau=0$ are the VMC values using $\Psi_T$; VMC values with the best known $\Psi_V$ are about 1.5 MeV below these. The GFMC very rapidly makes a large improvement on these energies; by $\tau=0.01$ MeV$^{-1}$, the $\Psi_T$ energies have been reduced by 6.5 to 8 MeV. This rapid improvement corresponds to the removal of small admixtures of states with excitation energies $\sim~1$ GeV from $\Psi_T$. Averages over typically the last nine $\tau$ values are used as the GFMC energy. The standard deviation, computed using block averaging, of all of the individual energies for these $\tau$ values is used to compute the corresponding statistical error. The solid lines show these averages; the corresponding dashed lines show the statistical errors. The g.s., $1^+$, and $3^+$ states of $^8$Be have widths less than 250 keV and their $E(\tau)$ appear to be converged and constant over the averaging regime. The $2^+$ state has a width of 1.5 MeV and the $4^+$ state's width is 3.5 MeV; the $E(\tau)$ for the $2^+$ state might be converged, but that of the $4^+$ state is clearly steadily decreasing. Reliable estimates of the energies of broad resonances requires the use of scattering-state boundary conditions (see Sec. [\[sec:scat\]](#sec:scat){reference-type="ref" reference="sec:scat"}) which have not yet been implemented for more than five nucleons.

Tests with different $\Psi_T$ as starting points for the GFMC calculation are described in Ref. [@PPCPW97]. The most crucial aspect in choosing $\Psi_T$ is that it have the correct mix of spatial symmetries, i.e., the $\beta_{LS[n]}$ admixtures. This is because the limited propagation time is not sufficient for the GFMC algorithm to filter out low-lying excitations with the same quantum numbers. This issue is unimportant in $^4$He, where the first 0$^+$ excited state is near 20 MeV, but in $^6$Li, the first 1$^+$ excited state is at only 5.65 MeV; other $p$-shell nuclei have similar low-lying excitations. Otherwise, the GFMC algorithm is able to rapidly correct for some very poor $\Psi_T$ whose variational energies are actually positive. However, a good $\Psi_T$ helps to keep the error bars small at larger $\tau$. The most efficient balance between speed of construction of $\Psi_T$ and smallest number of samples needed to achieve a given error bar seems to be given by Eq.([\[eq:psitgfmc\]](#eq:psitgfmc){reference-type="ref" reference="eq:psitgfmc"}). A number of other tests of the GFMC algorithm and its ability to determine nuclear radii are described in Refs. [@PPCPW97; @WPCP00].

The calculations described here are computationally intense, and would not have been possible without the advent of parallel supercomputers. The initial studies [@PPCW95] of $^6$Li required $\sim 2,000$ node hours on an IBM SP1 to propagate 10,000 configurations to $\tau$ = 0.06 MeV$^{-1}$. Today, with improvements in the algorithm and after much effort to optimize the computer codes, the same calculation requires about 15 node hours on a third generation IBM SP. However, a present calculation for $^8$Li, requiring 10,000 configurations to get a reasonable error bar, takes 1,000 node hours, so forefront computer resources remain essential for this program.
