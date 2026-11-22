---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "arXiv:nucl-th/0103005v2 6 Mar 2001"
section_id: sec-005-6-density-and-momentum-distributions
section_title: "DENSITY AND MOMENTUM DISTRIBUTIONS"
section_number: 6
pages: 27-35
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.981
doc_brief: "arXiv:nucl-th/0103005v2 6 Mar 2001 — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear Hamiltonians that"
---
The one- and two-nucleon distributions of light $p$-shell nuclei are interesting in a variety of experimental settings. For example, the Borromean $^6$He and $^8$He nuclei are popular candidates for study as 'halo' nuclei whose last neutrons are weakly bound. In addition, the polarization densities of $^6$Li and $^7$Li are important because of possible applications in polarized targets.

::: {#tab:radii}
  -------- ------------------------------- ------- ----------- ---------
           $\langle r^2_p \rangle^{1/2}$           $Q$         
           GFMC                            Expt.   GFMC        Expt.
   $^3$H   1.59(0)                         1.60                
   $^3$He  1.76(0)                         1.77                
   $^4$He  1.45(0)                         1.47                
   $^6$He  1.91(1)                                             
   $^6$Li  2.39(1)                         2.43    --0.32(6)   --0.083
   $^7$Li  2.25(1)                         2.27    --3.6(1)    --4.06
   $^7$Be  2.44(1)                                 --6.1(1)    
   $^8$He  1.88(1)                                             
   $^8$Li  2.09(1)                                 \(1\)       \(5\)
   $^8$B   2.45(1)                                 \(1\)       \(2\)
                                                               
  -------- ------------------------------- ------- ----------- ---------

  : GFMC values for point proton rms radii (in fm) and quadrupole moments (in fm$^2$) in impulse approximation, computed with AV18/IL2. Experimental values are from Refs. [@rmsr-expt; @rmsr-3He; @TUNL567; @moments-A8]
:::

Point proton rms radii and quadrupole moments are shown in Table [1](#tab:radii){reference-type="ref" reference="tab:radii"}, as computed by GFMC for the AV18/IL2 model, along with experimental values. The experimental charge radii have been converted to point proton radii by removing the proton and neutron $\langle r^2 \rangle$ of 0.743 and --0.116 fm$^2$, respectively. The radii are in good agreement with experiment, thanks at least in part to the fact that the AV18/IL2 model reproduces the binding energies of these nuclei very well. The quadrupole moments have been calculated in impulse approximation; two-body charge contributions are expected to provide only a few percent correction. The agreement with experiment is again fairly good, with the exception of the $^6$Li quadrupole moment, which involves a delicate cancellation between the contributions from the deuteron quadrupole moment and the D-wave part of the $\alpha$+$d$ relative wave function. In general, quadrupole moments are difficult to calculate accurately with quantum Monte Carlo methods because they are dominated by the long-range parts of the wave functions, which contribute very little to the total energy that VMC and GFMC are both designed to optimize.

::: {#tab:mag-mom}
  --------------- --------------- ----------- ------- --------------------- ------------------
                         T          Isoscalar                     Isovector 
                                         GFMC   Expt.                  GFMC              Expt.
   $^3$He$-^3$H    $\case{1}{2}$     0.403(0)   0.426   $-$<!-- -->4.330(1)   $-$<!-- -->5.107
      $^6$Li             0           0.817(1)   0.822                       
   $^7$Be$-^7$Li   $\case{1}{2}$     0.894(1)   0.929   $-$<!-- -->3.93(1)    $-$<!-- -->4.654
   $^8$B$-^8$Li          1           1.276(1)   1.345              0.369(9)   $-$<!-- -->0.309
                                                                            
  --------------- --------------- ----------- ------- --------------------- ------------------

  : GFMC values for isoscalar and isovector magnetic moments (in $\mu_N$) in impulse approximation using AV18/IL2. Experimental values are from Refs. [@TUNL3; @TUNL4; @AS88; @moments-A8]
:::

Calculated and experimental isoscalar and isovector magnetic moments are shown in Table [2](#tab:mag-mom){reference-type="ref" reference="tab:mag-mom"}, as defined with the convention used in Eq.([\[eq:isoexpand\]](#eq:isoexpand){reference-type="ref" reference="eq:isoexpand"}); thus the isovector values for the $T=\case{1}{2}$ cases are $-$<!-- -->2 times those often quoted in the literature. (For the $A=8$, $T=1$ nuclei the experimental isoscalar and isovector moments are obtained from the sum and difference of the values for B and Li, since the magnetic moment of the $T=1$ $J^{\pi}=2^+$ state in Be is not measured.) The moments were calculated as expectation values in the GFMC wave functions with $T_z=-T$ in impulse approximation. These impulse isoscalar moments are quite close to experiment and it is expected that two-body current contributions are small [@SPR89]. For isovector moments, however, there can be significant corrections from meson-exchange contributions. We note that the corrections needed for the $A$=7,8 isovector moments are the same sign and magnitude as for $A$=3, so an exchange-current model that fixes the s-shell [@MRS98] is likely to work for the light p-shell nuclei also.

<figure id="fig:he-rho1">

<figcaption>Proton and matter densities in <span class="math inline"><sup>4</sup></span>He, <span class="math inline"><sup>6</sup></span>He, and <span class="math inline"><sup>8</sup></span>He. Analyses of <span class="math inline"><sup>6, 8</sup></span>He-proton scattering are shown by the dashed (Ref. <span class="citation" data-cites="Alkhazov"></span>) and dot-dashed (Ref. <span class="citation" data-cites="Al-Khalili"></span>) curves.</figcaption>
</figure>

In Fig. [1](#fig:he-rho1){reference-type="ref" reference="fig:he-rho1"}, we present proton and matter (proton$+$neutron) densities for the stable helium isotopes, as calculated with GFMC for AV18/IL2. Nucleon densities are calculated as simple $\delta$-function expectation values, with possible spin and/or isospin projectors: for example, the proton density is given by $$\rho_{p}(r) \ = \ \frac{1}{4 \pi r^2}
\langle \Psi | \sum_i \ 
\ \frac { 1 + \tau_{zi}}{2} \ \delta ( r - | {\bf r}_i - {\bf R}_{cm} | )
\ | \Psi \rangle \ .$$ The blue symbols and curves show results for $^6$He, red ones for $^8$He; open symbols give the proton distributions which are also interpreted as the alpha "core" density, full symbols are the total matter densities. It can be seen that, as more neutrons are added, the tails of the matter distributions broaden considerably because of the relatively weak binding of the p-shell neutrons. In addition, the central neutron and proton densities decrease rather dramatically. This effect does not necessarily require any changes to the $\alpha$ core, but can be understood at least partially from the fact that the $\alpha$ no longer sits at the center of mass of the entire system. The motion relative to the center of mass spreads out the mass distribution relative to that of $^4$He.

The figure also shows two attempts to extract the densities of $^{6,8}$He from scattering of beams of these short-lived nuclei from proton targets [@Alkhazov]. The analysis of Alkhazov, et al. (dashed curves) used Glauber theory and assumed proton (core) and matter density distributions which were varied to fit the measured cross sections. The later work of Al-Khalili and Tostevin [@Al-Khalili] (dot-dashed curves) improved on this by doing the Glauber theory using model wave functions which contained correlations between the valence neutrons. The GFMC calculations definitely prefer the latter analysis.

<figure id="fig:he-pp">

<figcaption>Proton-proton distribution functions in helium isotopes</figcaption>
</figure>

The proton-proton distribution function is defined by $$\rho_{pp} (r) = \frac{1}{4 \pi r^2}
\langle \Psi | \sum_{i<j} \ \frac{1 + \tau_{zi}}{2}
\ \frac { 1 + \tau_{zj}}{2} \ \delta ( r - |{\bf r}_i - {\bf r}_j|)|
\Psi \rangle \ .$$ These distributions are directly related to the Coulomb sum measured in inclusive longitudinal electron scattering; such measurements in $^3$He have been used to put constraints on the $\rho_{pp} (r_{ij})$, and realistic calculations agree with the experimental results[@SWC93]. The behavior of $\rho_{pp} (r)$ at short distances is largely determined by the repulsive core of the $N\!N$ potential and is nearly independent of the nucleus, but at larger distances it is determined by the size of the nucleus.

It is interesting to compare $\rho_{pp}$ for $^4$He to that of $^6$He and $^8$He. These distribution functions are shown in Fig. [2](#fig:he-pp){reference-type="ref" reference="fig:he-pp"}, again calculated with GFMC for the AV18/IL2 model. These nuclei each have just one $pp$ pair which presumably is in the "alpha core" of $^{6,8}$He. Unlike the one-body densities, these distributions are not sensitive to center of mass effects, and thus if the alpha core of $^{6,8}$He is not distorted by the surrounding neutrons, all three $\rho_{pp}$ distributions in the figure should be the same. We see that the $pp$ distribution spreads out slightly with neutron number in the helium isotopes, with an increase of the pair rms radius of approximately 4% in going from $^4$He to $^6$He, and 8% to $^8$He. While this could be interpreted as a swelling of the alpha core, it might also be due to the charge-exchange ($\tau_i \cdot \tau_j$) correlations which can transfer charge from the core to the valence nucleons. Since these correlations are rather long-ranged, they can have a significant effect on the $pp$ distribution. VMC calculations of $^4$He with wave functions modified to give $\rho_{pp}$ distributions close to those of $^{6,8}$He suggest that the alpha cores of $^{6,8}$He are excited by $\sim80$ and $\sim350$ keV, respectively.

In general, VMC calculations give one-body densities very similar to the GFMC results, although the two-body densities may differ by up to 10% in the peak, with the GFMC having a somewhat sharper structure. Because the VMC wave functions are simpler and less expensive to construct they have been used in a number of applications where the single-particle structure is dominant. All these calculations were carried out with wave functions for the AV18/UIX Hamiltonian, but we expect that GFMC calculations with the improved AV18/IL2 model will not qualitatively alter the results. (Remember that the VMC wave functions are constrained to reproduce available experimental rms radii.)

<figure id="fig:li6ff">

<figcaption>Calculated and experimental elastic and transition form factors in <span class="math inline"><sup>6</sup></span>Li. Experimental data are from Refs. <span class="citation" data-cites="Li71 Lap78 Ber82 Ran66 Deu79 Ber76 Ber75"></span>.</figcaption>
</figure>

VMC calculations of elastic and inelastic electromagnetic form factors for $^6$Li are shown in Fig. [3](#fig:li6ff){reference-type="ref" reference="fig:li6ff"}. These have been made in impulse approximation (IA) and with meson-exchange contributions (MEC) to the charge and density operators [@WS98]. The comparison with data for the elastic longitudinal form factor, $F_L(q^2)$, is excellent, as is the E2 transition to the 3$^+$ first excited state. The MEC corrections are small, but stand out noticeably in the first minimum where they significantly improve the fit to data. The elastic transverse form factor, $F_T(q^2)$, is good up to the first zero, but is a little too large in the region of the second maximum. The M1 transition to the 0$^+$ isobaric analog state is also reproduced reasonably well. This kind of quantitative agreement with data has not been achieved in the past with either shell model or $\alpha$+$d$ cluster wave functions. In fact, shell model calculations normally require the introduction of effective charges, typically adding a charge of $\sim 0.5e$ to both the proton and neutron, to obtain reasonable transition rates [@PWK67]. No effective charges are used in the VMC calculations.

<figure id="fig:pipip">

<figcaption>Differential cross sections for <span class="math inline"><sup>7</sup></span>Li<span class="math inline">(<em>π</em>,<em>π</em>′)</span> scattering at <span class="math inline"><em>E</em><sub><em>π</em></sub> = 164</span> MeV. Data are from Ref. <span class="citation" data-cites="Bol79"></span>.</figcaption>
</figure>

While electron scattering from nuclei is primarily sensitive to the proton distributions in nuclei, $\pi^-$ scattering is most sensitive to the neutron distributions. Pion inelastic scattering at medium energy ($80 \leq E_{lab} \leq 300$ MeV) is dominated by strong absorption due to excitation of the $\Delta$ resonance, and is well described in distorted-wave impulse approximation (DWIA). An analysis of meson factory data for p-shell nuclei based on the Cohen-Kurath shell model [@CK65] showed that reasonable agreement with data could be achieved if the quadrupole excitation operator was enhanced by a factor $\sim$ 1.75--2.5 [@LK80]. Figure [4](#fig:pipip){reference-type="ref" reference="fig:pipip"} shows a calculation of the differential cross sections for $^7$Li($\pi,\pi^\prime$) scattering to the first three excited states using VMC transition densities as input, with no enhancement factors [@LW01]. Solid red lines show the full results, which are in good agreement with the data, while the dashed blue lines give the contribution coming from protons only. Because of the strong isospin dependence of the $\pi N$ scattering $t$-matrix, this reaction can be a stringent test of the neutron densities predicted by the quantum Monte Carlo calculations.

<figure id="fig:he6p">

<figcaption>Experimental <span class="citation" data-cites="LWW99"></span> momentum distributions for the transitions to the ground state (circles) and first excited state (squares) in the reaction <span class="math inline"><sup>7</sup></span>Li<span class="math inline">(<em>e</em>,<em>e</em>′<em>p</em>)<sup>6</sup></span>He, compared to CDWIA calculations with the VMC wave functions (solid lines) for AV18/UIX. </figcaption>
</figure>

The VMC wave functions for the AV18/UIX model have also been used to calculate single-nucleon momentum distributions in many nuclei, and a variety of cluster-cluster overlap wave functions, such as $\langle d p | t \rangle$, $\langle d d | \alpha \rangle$, and $\langle
\alpha d | ^6{\rm Li} \rangle$ [@SPW86; @FPPWSA96]. Recently the overlaps $\langle^6{\rm He}(J^{\pi})+p(\ell_j)|^7{\rm Li}\rangle$ for all possible p-shell states in $^6$He were studied [@LWW99]. The spectroscopic factors obtained from these overlaps are 0.41 to the ground state of $^6$He and 0.19 to the 2$^+$ first excited state. These factors are significantly smaller than the predictions of the Cohen-Kurath shell model [@CK67], which gives values of 0.59 and 0.40, respectively. The CK shell model requires that the possible $^6$He$+p$ states sum to unity within the p-shell, whereas in the VMC calculation, the correlations in the wave function push significant strength to higher momenta that cannot be represented as a $^6$He state plus p-wave proton. The VMC overlaps were used as input to a Coulomb DWIA analysis of recent $^7$Li$(e,e^{\prime}p)^6$He data taken at NIKHEF [@LWW99] and found to give an excellent fit to the data, as shown in Fig. [5](#fig:he6p){reference-type="ref" reference="fig:he6p"}.

<figure id="fig:be8">

<figcaption>Calculated density contours of <span class="math inline"><sup>8</sup></span>Be in the lab frame (left) and the intrinsic frame (right), labeled with densities in fm<span class="math inline"><sup>−3</sup></span></figcaption>
</figure>

The VMC wave functions are based on one-body parts that have a shell-model structure, namely four nucleons in an $\alpha$ core coupled to $(A-4)$ one-body $\ell=1$ wave functions. However the low-lying states of $^8$Be exhibit a rotational spectrum and are believed to be well approximated as two $\alpha$'s rotating around their common center of mass. It is possible to recover this picture from the VMC wave functions by a modified Monte Carlo density calculation [@WPCP00].

The standard Monte Carlo method for computing one-body densities, $\rho({\bf r})$, is to make a random walk that samples $|\Psi({\bf r}_1,{\bf r}_2,\cdots,{\bf r}_A)|^2$ and to bin ${\bf r}_1,{\bf r}_2,\cdots,{\bf r}_A$ for each configuration in the walk. The density is then proportional to the number of samples in each bin. In the case of a $J$ = 0 nucleus, this "laboratory" density will necessarily be spherically symmetric.

The intrinsic density in body-fixed coordinates can be approximated by computing the moment of inertia matrix, ${\cal M}$, of the $A$ positions for each configuration. The eigenvalues and eigenvectors of ${\cal M}$, are found and a rotation to those principal axes is made. The resulting ${\bf r}_1^\prime,{\bf r}_2^\prime,\cdots,{\bf r}_A^\prime$ is then binned. The eigenvector with the largest eigenvalue is chosen as the ${\bf z}^\prime$ axis. This procedure will not produce a spherically symmetric distribution, even if there is no underlying deformed structure, because almost every random configuration will have principal axes of different lengths and the rotation will always orient the longest principal axis in the ${\bf z}^\prime$ direction. However no artificial structure is introduced [@WPCP00].

When the above procedure is applied to the three lowest $^8$Be states, a dramatic intrinsic structure is revealed, as shown in Fig. [6](#fig:be8){reference-type="ref" reference="fig:be8"} for the ground state. The figure shows contours of constant density plotted in cylindrical coordinates. The left side of the figure shows the standard, lab frame, density calculation. For the $J$ = 0 ground state, this is spherically symmetric as shown. The right side of the figure shows the intrinsic density. It is clear that the intrinsic density has two peaks, with the neck between them having only one-third the peak density; we regard these as two $\alpha$'s. This assignment is strengthened by making the same construction for the $J=2^+$ and $4^+$ states; although the laboratory densities for these states (in $M=J$ states) are quite different, the intrinsic densities are, within statistical errors, the same as the $J=0$ intrinsic density [@WPCP00].

If the $0^+$, $2^+$, and $4^+$ states are generated by rotations of a common deformed structure, then their electromagnetic moments and transition strengths should all be related to the intrinsic moments which can be computed by integrating over the projected body-fixed densities. This is explored in Ref. [@WPCP00] and a generally consistent picture is shown.
