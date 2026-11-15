---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "arXiv:nucl-th/0103005v2 6 Mar 2001"
section_id: sec-004-5-energy-results
section_title: "ENERGY RESULTS"
section_number: 5
pages: 20-27
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.972
doc_brief: "arXiv:nucl-th/0103005v2 6 Mar 2001 — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear Hamiltonians that"
---
There are a number of accurate many-body methods for evaluating the binding energy of the s-shell nuclei, $^3$H, $^3$He, and $^4$He, using realistic nuclear forces. These include Faddeev in configuration space [@FPSS93] (FadR), Faddeev and Faddeev-Yakubovsky in momentum space [@NKG00] (FadQ), and hyperspherical harmonics [@HH] (HH), correlated hyperspherical harmonics [@VKR95] (CHH) and pair-correlated hyperspherical harmonics [@KVR93] (PHH). Some results of these methods for the AV18 and AV18/UIX Hamiltonians are shown in Table [1](#tab:s-shell){reference-type="ref" reference="tab:s-shell"}. We observe that the VMC upper bounds are generally 1.5--2.0% above the GFMC energies, which in turn are 0.25--1.0% above the Faddeev results. The disagreement between GFMC and the other methods may be attributable to the fact that GFMC is propagated with an $H'$ and a small piece of the Hamiltonian is computed in perturbation. At this fine level of comparison, one needs to worry about how features such as $T=\case{3}{2}$ admixtures and $n-p$ mass differences in the trinucleon ground state are treated in each calculation.

Table [1](#tab:s-shell){reference-type="ref" reference="tab:s-shell"} also shows the necessity of including (at least) a three-nucleon potential in the Hamiltonian in order to reproduce the A=3,4 experimental binding energies. This is true for all the other modern $N\!N$ potentials, as shown in Refs. [@FPSS93; @NKG00]. The local potentials AV18, Reid93, and Nijm II, give very similar results, while the slightly nonlocal Nijm I gives 1--3% more binding, and the more nonlocal CD-Bonn gives 5--8% more binding, or about halfway between the local potential values and experiment. At present, no two- plus three-nucleon potential combination gives an exact fit to both trinucleon and $^4$He energies, but several combinations, like AV18/UIX, come quite close. It also appears that it may be easier to fit $^3$He and $^4$He simultaneously, rather than $^3$H and $^4$He, perhaps because of the better data constraints on the $pp$ interaction compared to the $nn$ interaction [@NKG00]. In principle, there should also be four-body forces, but their contribution must be quite small, and it is impossible to unambiguously identify a need for such terms until a more thorough survey of possible three-nucleon potentials is made and the discrepancies between the various many-body methods are resolved.

::: {#tab:s-shell}
  ------------- --------- ------------ ------------ --------- -------- --------- -------- --
  Hamiltonian   nucleus            VMC         GFMC      FadQ     FadR        HH    Expt. 
  AV18          $^3$H        --7.50(1)    --7.61(1)   --7.623   --7.62   --7.618    8.482 
                $^4$He      --23.72(3)   --24.07(4)   --24.28            --24.18   28.296 
  AV18/UIX      $^3$H        --8.32(1)    --8.46(1)   --8.478            --8.475    8.482 
                $^4$He      --27.78(3)   --28.33(2)   --28.50             --28.1   28.296 
                                                                                          
  ------------- --------- ------------ ------------ --------- -------- --------- -------- --

  : Energies of $^3$H and $^4$He in MeV, computed by VMC and GFMC compared to momentum-space Faddeev [@NKG00], configuration-space Faddeev [@FPSS93] and various hyperspherical harmonics methods [@kievsky]. The HH column values are PHH for $^3$H; HH for $^4$He, AV18; and CHH for $^4$He, AV18/UIX
:::

Figure [1](#fig:vmc-gfmc-exp){reference-type="ref" reference="fig:vmc-gfmc-exp"} compares VMC (using the full $\Psi_V$ of Eq.([\[eq:bestpsiv\]](#eq:bestpsiv){reference-type="ref" reference="eq:bestpsiv"})) and GFMC calculations for the AV18/UIX Hamiltonian, and also shows experimental energies. All GFMC energies in this review are from Ref. [@PPWC01]; VMC energies are from Refs. [@WPCP00; @PPCPW97]. All particle-stable or narrow-width ($\Gamma<150$ keV) states for $4\leq{A}\leq8$ are shown, except isobaric analogs. We see that the VMC calculations get progressively worse in the p-shell compared to the s-shell, being on the order of 10--15% above the final GFMC results, for nuclei with $N \sim Z$. In absolute terms, $\Psi_V$ misses roughly an extra 1.5 MeV of binding for each p-shell nucleon that is added. The VMC results also fail to reproduce important qualitative features of the GFMC calculations; for example $^6$Li is stable against breakup into $\alpha$+d for this Hamiltonian but the VMC calculation shows it unbound by $\sim$<!-- -->2 MeV (the black dashed lines show the indicated thresholds computed using the sub-cluster energies appropriate to each calculation or experiment). Clearly, there is some significant feature of light p-shell nuclei that is not yet included in the trial wave functions.

<figure id="fig:vmc-gfmc-exp">

<figcaption>VMC and GFMC energies using AV18/UIX compared to experiment. Black dashed lines show the indicated breakup thresholds for each method. The Monte Carlo statistical errors are shown by the light blue and yellow bands.</figcaption>
</figure>

Table [2](#tab:energy){reference-type="ref" reference="tab:energy"} shows the GFMC energy values for several Hamiltonians. The table and Fig. [1](#fig:vmc-gfmc-exp){reference-type="ref" reference="fig:vmc-gfmc-exp"} show that the AV18/UIX Hamiltonian, which gives excellent energies, compared to experiment, for the s-shell nuclei, significantly underbinds the p-shell nuclei. The Li isotopes are stable against breakup into subclusters with AV18/UIX, but progressively more underbound as $A$ increases. There is also an isospin problem, in that the He isotopes are even further off from the experimental values, and in fact do not show stability against breakup into subclusters.

::: {#tab:energy}
  ------------------------- ---------------------- ---------------------- ---------------------- ------------------
                                     AV18                 AV18/UIX               AV18/IL2          Expt.
  $^3$H($\case{1}{2}^+$)      $-$<!-- -->7.61(1)     $-$<!-- -->8.46(1)     $-$<!-- -->8.43(1)    $-$<!-- -->8.48
  $^4$He(0$^+$)              $-$<!-- -->24.07(4)    $-$<!-- -->28.33(2)    $-$<!-- -->28.37(3)   $-$<!-- -->28.30
  $^6$He(0$^+$)              $-$<!-- -->23.9(1)     $-$<!-- -->28.1(1)     $-$<!-- -->29.4(1)    $-$<!-- -->29.27
  $^6$Li(1$^+$)              $-$<!-- -->26.9(1)     $-$<!-- -->31.1(1)     $-$<!-- -->32.3(1)    $-$<!-- -->31.99
  $^7$He($\case{3}{2}^-$)    $-$<!-- -->21.2(2)     $-$<!-- -->25.8(2)     $-$<!-- -->29.2(3)    $-$<!-- -->28.82
  $^7$Li($\case{3}{2}^-$)    $-$<!-- -->31.6(1)     $-$<!-- -->37.8(1)     $-$<!-- -->39.6(2)    $-$<!-- -->39.24
  $^8$He(0$^+$)              $-$<!-- -->21.6(2)     $-$<!-- -->27.2(2)     $-$<!-- -->31.3(3)    $-$<!-- -->31.41
  $^8$Li(2$^+$)              $-$<!-- -->31.8(3)     $-$<!-- -->38.0(2)     $-$<!-- -->42.2(2)    $-$<!-- -->41.28
  $^8$Be(0$^+$)              $-$<!-- -->45.6(3)     $-$<!-- -->54.4(2)     $-$<!-- -->56.6(4)    $-$<!-- -->56.50
  $^7$n($\case{1}{2}^-$)     $-$<!-- -->33.47(5)    $-$<!-- -->33.2(1)     $-$<!-- -->35.8(2)    
  $^8$n(0$^+$)               $-$<!-- -->39.21(8)    $-$<!-- -->37.8(1)     $-$<!-- -->41.1(3)    
                                                                                                 
  ------------------------- ---------------------- ---------------------- ---------------------- ------------------

  : GFMC and experimental energies of $A$=3--8 ground states in MeV. Energies of artificially confined 7- and 8-neutron drops are also shown. The experimental values are from Refs. [@TUNL3; @TUNL4; @AS88].
:::

The new Illinois three-nucleon potentials were constructed to solve the p-shell binding problems. Figure [2](#fig:av18-il2-exp){reference-type="ref" reference="fig:av18-il2-exp"} and Table [2](#tab:energy){reference-type="ref" reference="tab:energy"} compare GFMC calculations for AV18 with no $V_{ijk}$ and AV18/IL2 to the same experimental energies shown in Fig. [1](#fig:vmc-gfmc-exp){reference-type="ref" reference="fig:vmc-gfmc-exp"}. The AV18/IL2 Hamiltonian does a good job of reproducing these energies; the rms deviation from experiment for these levels is only 360 keV, while it is 2.3 MeV for AV18/UIX. The AV18 values with no $V_{ijk}$ show the large contribution that three-nucleon potentials make to these binding energies; for $A=8$ the IL2 increases the binding energy by more than 10 MeV.

<figure id="fig:av18-il2-exp">

<figcaption>GFMC energies using AV18 and AV18/IL2 compared to experiment.</figcaption>
</figure>

Table [3](#tab:sosplit){reference-type="ref" reference="tab:sosplit"} shows some splittings for states that in a simple shell-model picture have the same $L$ and $S$ but different total $J$. In all cases the lowest state for each $J$ is used. Some of the states, particularly the $^5$He states, have large experimental widths; calculations such as those described in Sec. [\[sec:scat\]](#sec:scat){reference-type="ref" reference="sec:scat"} would be more reliable. The splittings are computed for the AV18, AV18/UIX, and AV18/IL2 Hamiltonians and are compared to experimental values. The AV18 with no $V_{ijk}$ significantly underpredicts all the splittings except the $\case{1}{2}^- - \case{3}{2}^-$ doublet in $^7$Li; however in this case the relatively large statistical error for the small splitting makes any conclusion difficult (the computed splittings are the difference of two independent GFMC calculations whose statistical errors must be added in quadrature). The AV18/UIX Hamiltonian substantially improves the $^5$He splitting, and a VMC study showed that an earlier Urbana $V_{ijk}$ significantly increased the computed splitting in $^{15}$N, resulting in much better agreement with experiment [@PP93]. However the other splittings in the table are still underpredicted with AV18/UIX. The AV18/IL2 results in good predictions of all the splittings except for the 1$^+-2^+$ doublet in $^8$Li which is overpredicted.

::: {#tab:sosplit}
  -------- --------------------------------- ----- --------------- --------- ---------- ---------- -------
                                              $L$        $S$         AV18     AV18/UIX   AV18/IL2   Expt.
  $^5$He    $\case{1}{2}^- - \case{3}{2}^-$    1    $\case{1}{2}$   0.6(1)     1.1(2)     1.3(2)    1.20
  $^6$Li              2$^+ - 3^+$              2          1         0.8(1)     0.9(1)     2.2(2)    2.12
  $^7$Li    $\case{1}{2}^- - \case{3}{2}^-$    1    $\case{1}{2}$   0.5(2)     0.3(2)     0.6(3)    0.47
  $^7$Li    $\case{5}{2}^- - \case{7}{2}^-$    3    $\case{1}{2}$   0.7(2)     0.8(2)     2.2(3)    2.05
  $^8$Li              1$^+ - 2^+$              1          1         0.2(4)     0.6(2)     1.7(4)    0.98
  $^7$n     $\case{3}{2}^- - \case{1}{2}^-$    1    $\case{1}{2}$   1.65(7)    1.5(1)     2.8(3)   
                                                                                                   
  -------- --------------------------------- ----- --------------- --------- ---------- ---------- -------

  : GFMC and experimental [@AS88; @TUNL567] splittings of states with the same $L$ and $S$ but different $J$, in MeV.
:::

A detailed breakdown of the GFMC ground-state energies for AV18/IL2 into kinetic, two- and three-nucleon interactions is given in Table [4](#tab:gfmc){reference-type="ref" reference="tab:gfmc"}. Because of the extrapolation of the mixed expectation values, Eq.([\[eq:pc_gfmc\]](#eq:pc_gfmc){reference-type="ref" reference="eq:pc_gfmc"}), these components are not as accurate as the total energy, and do not add up to the full amount; indeed the sum of the individual kinetic and potential energies differs from $\langle H \rangle$ by the same amount that the GFMC has improved the $\Psi_T$ energy. Nevertheless, they give a good idea about the relative size of the different terms involved. There is a big cancellation between the kinetic and two-body potential terms. Consequently, while $V_{ijk}$ is less than 8% of $v_{ij}$ in magnitude, its expectation value is up to 50% of the net binding (however the net effect of the IL2 $V_{ijk}$, defined as the difference of the binding energies computed without and with $V_{ijk}$, is at most 30%, as can be seen in Table [2](#tab:energy){reference-type="ref" reference="tab:energy"}). This difference between expectation value and net effect is due to the large change that $V_{ijk}$ induces in $\langle K+v_{ij} \rangle$.

::: {#tab:gfmc}
  -------- ---------- --------------------- -------------------- ------------------- --------------------- -------------------- ---------------------
              $K$           $v_{ij}$             $V_{ijk}$        $v^{\gamma}_{ij}$     $v^{\pi}_{ij}$       $V^{2\pi}_{ijk}$      $V^{3\pi}_{ijk}$
  $^3$H      51.        $-$<!-- -->59.        $-$<!-- -->1.5            0.04           $-$<!-- -->45.        $-$<!-- -->3.0       0.18(1)
  $^4$He    115.(1)    $-$<!-- -->136.(1)     $-$<!-- -->8.4(1)         0.86          $-$<!-- -->105.       $-$<!-- -->16.3(1)    0.63(1)
  $^6$He    147.(2)    $-$<!-- -->171.(2)    $-$<!-- -->11.5(3)         0.87          $-$<!-- -->127.(1)    $-$<!-- -->20.3(4)  $-$<!-- -->0.91(6)
  $^6$Li    160.(2)    $-$<!-- -->187.(2)    $-$<!-- -->11.1(3)         1.73          $-$<!-- -->150.(1)    $-$<!-- -->19.8(4)  $-$<!-- -->0.44(5)
  $^7$He    175.(3)    $-$<!-- -->199.(3)    $-$<!-- -->16.3(4)         0.89          $-$<!-- -->145.(2)    $-$<!-- -->25.(1)   $-$<!-- -->3.1(1)
  $^7$Li    199.(3)    $-$<!-- -->232.(3)    $-$<!-- -->14.5(4)         1.80          $-$<!-- -->178.(2)    $-$<!-- -->25.6(6)  $-$<!-- -->1.1(1)
  $^8$He    190.(3)    $-$<!-- -->218.(3)    $-$<!-- -->16.3(5)         0.89          $-$<!-- -->153.(1)    $-$<!-- -->25.6(6)  $-$<!-- -->4.0(1)
  $^8$Li    242.(2)    $-$<!-- -->278.(2)    $-$<!-- -->20.6(4)         1.93          $-$<!-- -->211.(1)    $-$<!-- -->34.2(5)  $-$<!-- -->3.8(1)
  $^8$Be    256.(4)    $-$<!-- -->303.(3)    $-$<!-- -->21.(1)          3.32          $-$<!-- -->234.(2)    $-$<!-- -->38.5(9)  $-$<!-- -->0.9(2)
  $^7$n     105.(1)     $-$<!-- -->59.(1)     $-$<!-- -->3.6(3)         0.07           $-$<!-- -->10.        $-$<!-- -->0.1(1)  $-$<!-- -->5.4(3)
  $^8$n     122.(1)     $-$<!-- -->73.(1)     $-$<!-- -->3.0(3)         0.09           $-$<!-- -->12.              0.3(1)       $-$<!-- -->5.9(4)
                                                                                                                                
  -------- ---------- --------------------- -------------------- ------------------- --------------------- -------------------- ---------------------

  : Kinetic, $K$, and potential energy contributions in MeV. Shown are the total NN and NNN potential energies, $v_{ij}$ and $V_{ijk}$; the electromagnetic, $v^{\gamma}_{ij}$, and one-pion, $v^{\pi}_{ij}$, parts of $v_{ij}$; and the two- and three-pion parts of $V_{ijk}$.
:::

Among the subcomponents of $v_{ij}$, the one-pion exchange dominates, being 70--80% of the total $v_{ij}$ for $A\geq3$ nuclei. Similarly, the two-pion exchange is the dominant component of $V_{ijk}$. The three-pion exchange term is small and repulsive in s-shell nuclei, but attractive in the p-shell nuclei, which have $T=\case{3}{2}$ triples. It is this term which results in the large improvement of the Illinois models over the Urbana models for p-shell nuclei; however its contributions are always less than 15% of the two-pion $V_{ijk}$. Finally, we note that the electromagnetic $v^\gamma_{ij}$ is dominated by the Coulomb interaction between protons, but about 17% (8%) of its total contribution comes from the magnetic moment and other terms in He (Li) isotopes.

::: {#tab:analog}
  ---------------------- ----------- -------------- ---------------- ------------------ ---------- -------
  $a_n(A,T)$              $K^{CSB}$    $v_{C1}(pp)$  $v^{\gamma,R}$   $v^{CSB}+v^{CD}$    Total      Expt.
  $a_1(3,\case{1}{2})$       14              649(1)        29              64(0)           757(1)      764
  $a_1(6,1)$                 16             1091(5)        18              47(1)          1172(6)     1173
  $a_2(6,1)$                                 166(1)        19             107(13)          293(13)     223
  $a_1(7,\case{1}{2})$       22             1447(6)        40              79(2)          1588(7)     1644
  $a_1(7,\case{3}{2})$       18             1337(6)        12              52(1)          1420(8)     1373
  $a_2(7,\case{3}{2})$                       137(1)         7              36(6)           180(7)      175
  $a_1(8,1)$                 23             1686(5)        24              76(1)          1810(6)     1770
  $a_2(8,1)$                                 141(1)         4         $-$<!-- -->3(8)      143(8)      128
  $a_1(8,2)$                 18             1528(7)        17              59(1)          1622(8)     1659
  $a_2(8,2)$                                 136(1)         6              38(5)           180(5)      153
                                                                                                   
  ---------------------- ----------- -------------- ---------------- ------------------ ---------- -------

  : GFMC isovector and isotensor energy coefficients, $a_n(A,T)$, \[Eq. ([\[eq:isoexpand\]](#eq:isoexpand){reference-type="ref" reference="eq:isoexpand"})\] computed using AV18/IL2, in keV. The contributions shown are kinetic energy, $K^{CSB}$; Coulomb potential, $v_{C1}(pp)$; other electromagnetic, $v^{\gamma,R}$; and nuclear potential, $v^{CSB}+v^{CD}$. The experimental value for $a_2(8,1)$ is extracted using 16.80 MeV as the excitation of the pure $T=1$ isobaric analog state in $^8$Be [@B66].
:::

Energy differences among isobaric analog states are probes of the charge-indepen-dence-breaking parts of the Hamiltonian. The understanding of these "Nolen-Schiffer energies" has been a theoretical problem for 30 years [@NS69]. The energies for a given isomultiplet of states can be expanded as $$E_{A,T}(T_z) = \sum_{n\leq 2T} a_n(A,T) Q_n(T,T_z) \ ,
\label{eq:isoexpand}$$ where $Q_0=1$, $Q_1=T_z$, and $Q_2=\case{1}{2}(3T_z^2-T^2)$ are isoscalar, isovector, and isotensor terms [@P60]. The isovector and isotensor coefficients $a_n(A,T)$, and various contributions to them, are given in Table [5](#tab:analog){reference-type="ref" reference="tab:analog"}. These were calculated as expectation values in the $T_z=-T$ GFMC wave functions for AV18/IL2. The individual terms are: 1) the effect of the neutron-proton mass difference on the kinetic energy, $K^{CSB}$; 2) the proton-proton Coulomb potential, including the AV18 form factor, $v_{C1}(pp)$; 3) all other electromagnetic terms such as vacuum polarization and magnetic-moment terms, $v^{\gamma,R}$; and 4) the strong-interaction contributions, $v^{CSB}$ which contributes to the isotensor coefficients and $v^{CD}$ which contributes to the isovector coefficients.

The $^3$H--$^3$He mass difference is 757 keV with the AV18/IL2 Hamiltonian, in excellent agreement with the experimental value of 764 keV. The bulk of the difference is the $pp$ Coulomb energy, but 108 keV comes from the other terms. Because of its very long range, the $v_{C1}(pp)$ dominates the $a_1(A,T)$ of heavier nuclei even more and small errors in the rms radius of the nucleus can result in changes in the $v_{C1}(pp)$ contribution that can totally mask the effects of the other, much smaller, terms.

::: {#table:mixing}
  ----------- ----------- -------------- ---------------- ----------- ---------- -------
  $J^{\pi}$    $K^{CSB}$   $v_{C1}(pp)$   $v^{\gamma,R}$   $v^{CSB}$   $E_{01}$   Expt.
  $^+$             2            62              19            26        109(4)     149
  1$^+$            1            39              0             15         55(2)     120
  3$^+$            1            33              15            13         62(2)      63
                                                                                 
  ----------- ----------- -------------- ---------------- ----------- ---------- -------

  : VMC isospin-mixing matrix elements for $^8$Be in keV computed using AV18/UIX. Experimental values are from Ref. [@B66]
:::

[]{#table:mixing label="table:mixing"}

Two (2$^+$;0+1) states occur very close together in the spectrum of $^8$Be at 16.6 and 16.9 MeV excitation; these isospin-mixed states come from blending the (2$^+$;1) isobaric analog of the $^8$Li ground state with the second (2$^+$;0) excited state. There are also fairly close (1$^+$;0,1) and (3$^+$;0,1) pairs at slightly higher energies in the $^8$Be spectrum. The isospin-mixing matrix elements that connect these pairs of states, $$E_{01}(J) = \langle \Psi(J^+;0) | H | \Psi(J^+;1) \rangle \ ,$$ have been computed using VMC wave functions for the AV18/UIX Hamiltonian. Results for the $E_{01}(J)$ are given in Table [6](#table:mixing){reference-type="ref" reference="table:mixing"}. The experimental values are determined from the observed decay widths and energies [@B66]. The dominant contribution, from the Coulomb potential, typically accounts for less than half of the matrix element. We see that the remaining part of the electromagnetic interaction and the strong CSB interaction can provide a significant boost, although the experimental mixing is still underpredicted by $\sim$<!-- -->20%. It appears that these mixing elements are a more sensitive test of the small CSB components of the Hamiltonian than are the isobaric analog energy differences.
