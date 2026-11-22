---
doc_id: arxiv-1011.1343v1
doc_title: "Chiral symmetry, nuclear forces and all that"
section_id: sec-008-5-flash-forward-combining-nuclear-eft-with-latti
section_title: "Flash forward: Combining nuclear EFT with lattice simulations"
section_number: 5
pages: 13-15
source_pdf: 1011.1343v1.pdf
source_sha256: 7d50e5e28e695191
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.988
doc_brief: "Chiral symmetry, nuclear forces and all that — 11 sections: Front matter; The early days at Stony Brook; A first step: Studying pion-nucleo"
---
<figure id="fig:nuclat">
<embed src="phasediagram.eps" style="width:60.0%" />
<embed src="NuclLatt.eps" style="width:35.0%" />
<figcaption><span id="fig:nuclat" label="fig:nuclat"></span> Left panel: Euclidean space-time lattice with point-like nucleons on the lattice sites and a typical lattice spacing of <span class="math inline"><em>a</em> = 2</span> fm. Right panel: Nuclear phase diagram as accessible by lattice QCD and by nuclear lattice EFT. Figure courtesy of Dean Lee. </figcaption>
</figure>

Having now constructed nuclear forces between two, three and four nucleons, one has a new tool to address the nuclear many-body problem. One venue is to combine standard many-body techniques with these forces, as exemplified by the NCSM calculation shown in Sec. [\[sec:three\]](#sec:three){reference-type="ref" reference="sec:three"} or the discussion of nuclear matter in Sec. [\[sec:nucmat\]](#sec:nucmat){reference-type="ref" reference="sec:nucmat"} (see also the contribution by Josef Speth, Siegfried Krewald and Frank Grümmer to this Festschrift). Here, I briefly want to outline a very different and novel approach that combines the chiral EFT for the forces with the method of Monte Carlo simulations, that are so successfully utilized in the lattice approach to QCD. The basic idea is to formulate the chiral EFT on a Euclidean space-time lattice as depicted in the left panel of Fig. [1](#fig:nuclat){reference-type="ref" reference="fig:nuclat"} - here, the lattice spacing serves as an UV regulator and has to be chosen such that the nucleons - which are treated as non-relativistic point-like particles on the lattice sites - do not overlap. A lattice spacing of $a = 2\,$fm entails an UV cut-off $\Lambda = \pi/a \simeq 300\,$MeV. The pion and nucleon propagators as well as the one- and two-pion exchanges and the multi-nucleon contact interactions are written in terms of lattice variables, making use of Hubbard-Stratonovich fields to bring the 4- and 6-nucleon interactions into a quadratic form (for more details, see [@Borasoy:2006qn] and references therein as well as the nice review by Dean Lee [@Lee:2008fa]). Given this Euclidean formulation of the action, the generating functional of the theory can then be evaluated with stochastic methods, such as the hybrid Monte Carlo approach. It is important to stress that the approximate Wigner SU(4) symmetry of the nuclear interactions strongly suppresses the sign oscillations and thus makes such nuclear lattice simulations easier to handle than lattice QCD calculations. Within this scheme, a systematic study of nuclei up to $A \simeq 40$ will be possible using petascale computing as long as the total spin and isospin of the nucleus under consideration is zero. Also, the nuclear phase diagram can be studied for a wide range of temperatures and densities, as indicated in the right panel of Fig. [1](#fig:nuclat){reference-type="ref" reference="fig:nuclat"}.

<figure id="fig:c12">
<div class="center">
<embed src="carbon12.eps" style="width:11cm" />
</div>
<figcaption><span id="fig:c12" label="fig:c12"></span> Ground-state energy of <span class="math inline"><sup>12</sup></span>C as a function of Euclidean time. For details, see <span class="citation" data-cites="Epelbaum:2009pd"></span>.</figcaption>
</figure>

The state-of-the-art of these simulations is the calculation of the ground-state energy of $^6$Li and $^{12}$C [@Epelbaum:2009pd]. In these works, for the first time the contributions from the Coulomb interaction between protons and strong isospin-breaking effects were included. A parameter-free prediction for the energy difference between the triton and $^3$He could be given, $$E(^3{\rm H}) - E(^3{\rm He}) = 0.78(5)~{\rm MeV}~,$$ in good agreement with the empirical value of $0.76$ MeV. The ground-state energies of $^6$Li and $^{12}$C are calculated as $-32.9(9)$ MeV and $-99(2)$ MeV, respectively, not far from the empirical values of $-32.0$ and $-92.2$ MeV, cf. also Fig. [2](#fig:c12){reference-type="ref" reference="fig:c12"}. This accuracy is comparable to other so-called ab initio calculations (like the NCSM or Greens function Monte Carlo), that often are based on a less consistent formulation of the underlying nuclear forces.

Taking $^{12}$C as the benchmark, it is interesting to estimate the required computing time and storage needed for the calculation of larger nuclei[^1]. With an improved algorithm, the required CPU time for the $^{12}$C simulation on a BlueGene/P architecture and the necessary storage to make the configurations (about 3500) available is $$X_{^{12}C}^{\rm CPU} = 5 \times 10^{-5}~{\rm PFlop-yr}~,~~~~
X_{^{12}C}^{\rm storage} = 0.14~{\rm TB}~.$$ For a nucleus with $A$ nucleons and with total spin $S$ and isospin $I$ the required CPU time and data storage place can be estimated as $$\begin{aligned}
X^{\rm CPU} &\approx& X_{^{12}C}^{\rm CPU} \times \left(
  \frac{A}{12}\right)^{3.2}\exp[0.10(A-12) + 3(S~{\rm mod}~2) +4I]~,
\nonumber \\
X^{\rm storage} &\approx& X_{^{12}C}^{\rm storage} \times \left(
  \frac{A}{12}\right)^{2}\exp[0.10(A-12) + 3(S~{\rm mod}~2) +4I]~,
\end{aligned}$$ so that e.g. the calculation of the ground-states energies of the magnesium isotopes $^{24,25,26}$Mg would require $0.002, 0.064, 0.131$ PFlop-yr and one would need $1.9, 73.8, 145.5$ TB to store the configurations for the calculation of matrix elements for these nuclei. In many cases, neutron scattering off nuclei can also be calculated making use of Lüscher's formula that relates the continuum phase shift to the finite energy shift measured on the lattice. The CPU and storage requirements for neutron scattering of the isotopes $^{24,26}$Mg would be $0.064, 5.43$ PFlop-yr and $73.8,  5473$ TB, respectively. All this work remains to be done but bears a lot of promise. The possibilities that would be offered in a future exascale era are simply breath-taking.

[^1]: I am grateful to Dean Lee for providing me with these estimates.
