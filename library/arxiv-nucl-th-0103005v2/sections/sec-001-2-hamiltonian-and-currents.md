---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "arXiv:nucl-th/0103005v2 6 Mar 2001"
section_id: sec-001-2-hamiltonian-and-currents
section_title: "HAMILTONIAN AND CURRENTS"
section_number: 2
pages: 4-8
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.971
doc_brief: "arXiv:nucl-th/0103005v2 6 Mar 2001 — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear Hamiltonians that"
---
The Hamiltonian used in this review use includes nonrelativistic kinetic energy, the AV18 $N\!N$ potential [@WSS95] and either the Urbana IX [@PPCW95] or one of the new Illinois series of $N\!N\!$ potential [@PPWC01]: $$H = \sum_{i} K_{i} + \sum_{i<j} v_{ij} + \sum_{i<j<k} V_{ijk} \ .
\label{eq:H}$$ The kinetic energy operator has charge-independent (CI) and charge-symmetry-breaking (CSB) components, the latter due to the difference between proton and neutron masses, $$K_{i} = K^{CI}_{i} + K^{CSB}_{i} \equiv -\frac{\hbar^2}{4}
     (\frac{1}{m_{p}} + \frac{1}{m_{n}}) \nabla^{2}_{i}
    -\frac{\hbar^2}{4} (\frac{1}{m_{p}} - \frac{1}{m_{n}})\tau_{zi}
     \nabla^{2}_{i} ~,$$ where $\boldtau_{i}$ is the isospin of nucleon $i$.

The AV18 potential is written as a sum of electromagnetic and one-pion-exchange terms and a shorter-range phenomenological part, $$v_{ij} = v^{\gamma}_{ij} + v^{\pi}_{ij} + v^{R}_{ij} \ .$$ The electromagnetic terms include one- and two-photon-exchange Coulomb interaction, vacuum polarization, Darwin-Foldy, and magnetic moment terms, all with appropriate proton and neutron form factors. The one-pion-exchange part of the potential includes the charge-dependent (CD) terms due to the difference in neutral and charged pion masses. It can be written as $$v^{\pi}_{ij} = f^{2} \left(\frac{m}{m_{s}}\right)^{2} \case{1}{3}
                 mc^{2} \left[ X_{ij} \boldtau_{i} \cdot \boldtau_{j}
                      + \tilde{X}_{ij} T_{ij} \right] \ ,
\label{eq:vpi}$$ where $T_{ij} = 3\tau_{zi}\tau_{zj}-\boldtau_{i}\cdot\boldtau_{j}$ is the isotensor operator and $$\begin{aligned}
   && X_{ij} = \case{1}{3} \left( X^{0}_{ij} + 2 X^{\pm}_{ij} \right) , \\
   && \tilde{X}_{ij} = \case{1}{3} \left( X^{0}_{ij} - X^{\pm}_{ij}
                                      \right) , \\
   && X^{m}_{ij} =  \left[ Y(mr_{ij}) \boldsigma_{i} \cdot \boldsigma_{j} +
                           T(mr_{ij}) S_{ij}  \right] \ .
\end{aligned}$$ Here $Y(x)$ and $T(x)$ are the normal Yukawa and tensor functions: $$\begin{aligned}
Y(x) &=& \frac{e^{-x}}{x} \  \xi_Y(r) \ ,
\label{eq:yij}   \\
T(x) &=& \left( \frac{3}{x^2} + \frac{3}{x} + 1 \right) Y(x) \  \xi_T(r) \ .
\label{eq:tij}
\end{aligned}$$ with short-range cutoff functions $\xi_Y(r)$ and $\xi_T(r)$, and the $X^{\pm,0}$ are calculated with $m = m_{\pi^{\pm}}$ and $m_{\pi^{0}}$. The coupling constant in Eq.([\[eq:vpi\]](#eq:vpi){reference-type="ref" reference="eq:vpi"}) is $f^2 = 0.075$ and the scaling mass $m_s = m_{\pi^{\pm}}$.

The remaining terms are of intermediate (two-pion-exchange) and short range, with some 40 adjustable parameters. The one-pion-exchange and the remaining phenomenological part of the potential can be written as a sum of eighteen operators, $$v^{\pi}_{ij} + v^{R}_{ij} = \sum_{p=1,18} v_{p}(r_{ij}) O^{p}_{ij} \ .$$ The first fourteen are CI operators, $$\begin{aligned}
O^{p=1,14}_{ij} = [1, \boldsigma_{i}\cdot\boldsigma_{j}, S_{ij},
{\bf L\cdot S},{\bf L}^{2},{\bf L}^{2}(\boldsigma_{i}\cdot\boldsigma_{j}),
({\bf L\cdot S})^{2}]\otimes[1,\boldtau_{i}\cdot\boldtau_{j}] ~,
\label{eq:op14}
\end{aligned}$$ while the last four, $$O^{p=15,18}_{ij} = [1, \boldsigma_{i}\cdot\boldsigma_{j},
S_{ij}]\otimes T_{ij} \ ,  {\rm and} \ (\tau_{zi}+\tau_{zj}) \ ,$$ are CD and CSB terms. The potential was fit directly to the Nijmegen $N\!N$ scattering data base [@SKRS93] containing 1787 $pp$ and 2514 $np$ data in the range 0--350 MeV, to the $nn$ scattering length, and to the deuteron binding energy, with a $\chi^2$ per datum of 1.09.

While the CD and CSB terms are small, there is a clear need for their presence. The Nijmegen group studied many $N\!N$ potentials from the 1980s and before, and found that potentials fit to $np$ data in $T=1$ states did not fit $pp$ data well even after allowing for standard Coulomb effects, and vice versa [@SS93-95]. All five modern $N\!N$ potentials, Reid93, Nijm I and II [@SKTS94], CD Bonn [@MSS96], and AV18, which fit $pp$ and $np$ scattering data with a $\chi^2/$point near 1, have CD components. The CSB term is required to fit the difference between the $pp$ and $nn$ scattering lengths, and is consistent with the mass difference between $^3$H and $^3$He, as shown below. The identification of the proper CI, CD, and CSB $N\!N$ force components is important in setting the proper baseline for the introduction of $N\!N\!N$ forces, which are required to fit the $^3$H and $^3$He binding energies as a primary constraint.

<figure id="fig:vijk">

<figcaption>Three-body force Feynman diagrams: a is the Fujita-Miyazawa or two-pion P-wave, b is two-pion S-wave, c and d are three-pion rings with one <span class="math inline"><em>Δ</em></span> in intermediate states.</figcaption>
</figure>

The Urbana series of three-nucleon potentials is written as a sum of two-pion-exchange P-wave and remaining shorter-range phenomenological terms, $$V_{ijk} = V^{2\pi,P}_{ijk} + V^{R}_{ijk} ~.$$ The structure of the two-pion P-wave exchange term with an intermediate $\Delta$ excitation (Fig. [1](#fig:vijk){reference-type="ref" reference="fig:vijk"}a) was originally written down by Fujita and Miyazawa [@FM57]; it can be expressed simply as $$V^{2\pi,P}_{ijk} = \sum_{cyc} \left( A^P_{2\pi}
     \{X^{\pi}_{ij},X^{\pi}_{jk}\}
     \{\boldtau_{i}\cdot\boldtau_{j},\boldtau_{j}\cdot\boldtau_{k}\}
   + C^P_{2\pi} [X^{\pi}_{ij},X^{\pi}_{jk}]
     [\boldtau_{i}\cdot\boldtau_{j},\boldtau_{j}\cdot\boldtau_{k}] \right ) \ ,$$ where $X^{\pi}_{ij}$ is constructed with an average pion mass, $m_{\pi}=\case{1}{3}m_{\pi^0}+\case{2}{3}m_{\pi^{\pm}}$, and $\sum_{cyc}$ is a sum over the three cyclic exchanges of nucleons $i,j,k$. For the Urbana models $C^P_{2\pi} = \case{1}{4}A^P_{2\pi}$, as in the original Fujita-Miyazawa model [@FM57], while other potentials like the Tucson-Melbourne [@TM] and Brazil [@Brazil] models, have a ratio slightly larger than $\case{1}{4}$. The shorter-range phenomenological term is given by $$V^{R}_{ijk} = \sum_{cyc} A_R T^2(m_{\pi}r_{ij}) T^2(m_{\pi}r_{jk}) \ .
\label{eq:vrijk}$$ For the Urbana IX (UIX) model, the parameters were determined by fitting the binding energy of $^3$H and the density of nuclear matter in conjunction with AV18.

As shown below, while the combined AV18/UIX Hamiltonian reproduces the binding energies of s-shell nuclei, it does not do so well for light p-shell nuclei. Recently a new class of $N\!N\!N$ potentials, called the Illinois models, has been developed to address this problem [@PPWC01]. These potentials contain the Urbana terms and two additional terms, resulting in a total of four coupling constants that can be adjusted to fit the data.

One term, $V^{2\pi,S}_{ijk}$, is due to $\pi N$ S-wave scattering as illustrated in Fig. [1](#fig:vijk){reference-type="ref" reference="fig:vijk"}b. It has been included in a number of $N\!N\!N$ potentials like the Tucson-Melbourne [@TM] and Brazil [@Brazil] models. The Illinois models use the form recommended in the latest Texas model [@Texas], where chiral symmetry is used to constrain the structure of the interaction. However, in practice, this term is much smaller than the $V^{2\pi,P}_{ijk}$ contribution and behaves similarly in light nuclei, so it is difficult to establish its strength independently just from calculations of energy levels.

A more important addition is a simplified form for three-pion rings containing one or two deltas (Fig. [1](#fig:vijk){reference-type="ref" reference="fig:vijk"}c,d). As discussed in Ref. [@PPWC01], these diagrams result in a large number of terms, the most important of which are used to construct the Illinois models: $$V^{3\pi,\Delta R}_{ijk} = \Athpi \left[ \case{50}{3}S^I_{\tau}S^I_{\sigma}+
\case{26}{3}A^I_{\tau}A^I_{\sigma} \right] \ .$$ Here the $S^I_x$ and $A^I_x$ are operators that are symmetric or antisymmetric under any exchange of the three nucleons, and the subscript $x=\sigma$ or $\tau$ indicates that the operators act on, respectively, spin and space or just isospin degrees of freedom.

The $S^I_\tau$ is a projector onto isospin-$\case{3}{2}$ triples: $$S^I_{\tau} = 2 + \case{2}{3}\left(\boldtau_i \cdot \boldtau_j 
+\boldtau_j \cdot \boldtau_k + \boldtau_k \cdot \boldtau_i \right) 
= 4 P_{T=3/2}  \ .  
\label{eq:sitau}$$ To the extent isospin is conserved, there are no such triples in the s-shell nuclei, and so this term does not affect them. It is also zero for $Nd$ scattering. However, the $S^I_{\tau}S^I_{\sigma}$ term is attractive in all the p-shell nuclei studied. The $A^I_\tau$ has the same structure as the isospin part of anticommutator part of $V^{2\pi,P}$, but the $A^I_{\tau}A^I_{\sigma}$ term is repulsive in all nuclei studied so far. In p-shell nuclei, the magnitude of the $A^I_{\tau}A^I_{\sigma}$ term is smaller than that of the $S^I_{\tau}S^I_{\sigma}$ term, so the net effect of the $V^{3\pi,\Delta R}_{ijk}$ is slight repulsion in s-shell nuclei and larger attraction in p-shell nuclei. The reader is referred to Ref. [@PPWC01], and its appendix, for the complete structure of $V^{3\pi,\Delta R}_{ijk}$.

Relativistic corrections to the Hamiltonian of Eq.([\[eq:H\]](#eq:H){reference-type="ref" reference="eq:H"}) have been studied in three- and four-body nuclei [@CPS93; @FPCS95; @FPA99]. We only briefly outline the results here. If a square-root kinetic energy, $$K^{rel}_i = \sqrt{ p^2_i + m^2_i } - m_i \ ,$$ where $p_i$ is the momentum of nucleon $i$, is introduced into the Hamiltonian, then the $N\!N$ potential must be readjusted to refit the $N\!N$ data. This can be done for AV18 with only small adjustments of the parameters, to produce a $v^{rel}$. VMC calculations show that the resulting $\langle K^{rel}+v^{rel} \rangle \sim \langle K+v \rangle$ for $^3$H and $^4$He; thus the square-root kinetic energy may be neglected in light nuclei.

A second relativistic correction, the so-called "boost correction," arises from the fact that the two-nucleon interaction $v_{ij}$ depends both on the relative momentum ${\bf p} = ({\bf p}_i - {\bf p}_j)/2$ and the total momentum ${\bf P} = {\bf p}_i + {\bf p}_j$ of the interacting nucleons, $$v_{ij}({\bf p},{\bf P}) = \tvij({\bf p}) + \dvij({\bf p},{\bf P}) \ ,
\label{eq:tvdv}$$ where $\delta v_{ij}({\bf p},{\bf P}=0)=0$. Fitting the two-body potential to two-nucleon scattering data determines only $\tvij$. The $\dvij$ can be determined from $\tvij$; a suitable approximation [@FPA99; @FPF95; @F75] is $$\delta{v_{ij}}({\bf P})=-\frac{P^2}{8m^2}\tvij+\frac{1}{8m^2}\,\left[\ {\bf P}
\cdot{\bf r}\;{\bf P}\cdot\mbox{\boldmath$\nabla$}, \tvij\ \right] \ ,
\label{eq:friar}$$ where only the first six terms (the static terms) of $\tvij$ are retained and the gradient operators do not act on $\tvij$. The $\dvij$ is meant to be used only in first-order perturbation in a non-relativistic wave function. Its expectation values in light nuclei are nearly proportional to $\langle V^R_{ijk} \rangle$ [@PPWC01], and thus one can consider that part of $A_R$, Eq.([\[eq:vrijk\]](#eq:vrijk){reference-type="ref" reference="eq:vrijk"}), comes from $\dvij$. This proportionality does not, however, extend to nuclear matter or pure neutron systems. There one must use a reduced $A_R^*$ that does not contain the part ascribable to $\dvij$, and explicitly evaluate $\langle \dvij \rangle$; doing so results in a softer equation of state for dense matter.
