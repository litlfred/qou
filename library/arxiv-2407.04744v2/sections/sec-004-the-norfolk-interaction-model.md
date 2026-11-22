---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods"
section_id: sec-004-the-norfolk-interaction-model
section_title: "The Norfolk interaction model"
section_number: null
pages: 3-4
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.984
doc_brief: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods — 26 sections: Magnetic structure of A 10 nuclei ; Introduction; Theory"
---
[]{#sec:nv23 label="sec:nv23"}

We base our calculations on electromagnetic many-body currents [@Pastore:2008ui; @Pastore:2009is; @Schiavilla:2018udt; @Gnech:2022vwr] derived consistently with the Norfolk two- and three-body (NV2+3) nuclear interactions [@Piarulli:2014bda; @Piarulli:2016vel; @Piarulli:2017dwd; @Baroni:2018fdn; @Piarulli:2019cqu]. The Norfolk two-body potential (NV2) is a fully local interaction -- hence suitable to be utilized within QMC methods -- and includes terms up to N3LO in the $\chi$EFT expansion. To this order, the NV2 consists of one- (OPE) and two-pion-exchange (TPE) contributions, as well as contact interactions with strengths specified by unknown low-energy constants (LECs). Non-localities emerging from the contact terms entering at N3LO have been eliminated by i) leveraging Fierz transformations to develop a minimally non-local interaction to order N3LO [@Piarulli:2014bda]; and ii) constraining the LECs associated with the leftover N3LO non-local terms to vanish [@Piarulli:2016vel]. This choice is motivated by the consideration that the LECs associated with the non-local terms are of natural size, as opposed to those associated with the local isovector and isotensor operators required to obtain good agreement with nucleon-nucleon ($N\!N$) scattering data.

<figure id="fig:currn2lo">
<div class="center">
<embed src="em2_current.pdf" style="width:1.2in" />
</div>
<figcaption>Diagrams illustrating the contributions to the electromagnetic current up to N2LO. Nucleons, <span class="math inline"><em>Δ</em></span>-isobars, pions, and external fields are denoted by solid, thick-solid, dashed, and wavy lines, respectively. The square in panel (d) represents relativistic corrections to the LO current. Figure from Ref. <span class="citation" data-cites="Schiavilla:2018udt"></span>.</figcaption>
</figure>

Schematically, the NV2 interaction can be broken down into three parts as $$v_{12} = v_{12}^L + v_{12}^S + v_{12}^{\rm EM}\, ,$$ where $v_{12}^L$ is the long-range term consisting of OPE and TPE contributions to order N2LO, $v_{12}^S$ is the short-range term consisting of contact interactions, and $v^{\rm EM}_{12}$ is an electromagnetic contribution. The electromagnetic term retains second-order Coulomb, Darwin-Foldy, vacuum polarization, and magnetic moment interaction terms [@Wiringa:1994wb].

The radial functions in $v_{12}^L$ have ${\sim} 1/r^n$ (with $n\le6$) singularities at the origin that are regulated with the function $$C_{R_L}(r) =  1 - \frac{1}{(r/R_L)^6e^{2(r-R_L)/R_L} + 1 },$$ where $R_L$ is the long-range cutoff. The short-range regulator comes from a Gaussian smearing of the $\delta$-functions in coordinate space, expressed as $$C_{R_S}(r) = \frac{1}{\pi^{3/2}R_S^3}e^{-(r/R_S)^2}\, ,$$ where $R_S$ is the Gaussian parameter governing the width of the smearing. Consequently, two regulator parameters need to be specified in the model.

Embedded within $v_{12}^S$ are 26 unknown LECs that parameterize the strengths of the contact terms, adjusted to fit $N\!N$ scattering data [@Perez:2013jpa; @Perez:2013oba; @Perez:2014yla]. There are four classes of models for the NV2. Model classes denoted by I (II) are fit to $N\!N$ scattering data up to 125 (200) MeV with a $\chi^2/{\rm datum}\approx 1.1~(1.4)$. For model classes denoted by a (b), the regulators used in the potential are $[R_L,R_S]=[1.2~{\rm fm},0.8~{\rm fm}]$ ($[R_L,R_S]=[1.0~{\rm fm},0.7~{\rm fm}]$).

In addition to the NV2, the Norfolk models incorporate a three-body force (NV3) [@vanKolck:1994yi; @Epelbaum:2002vt] that requires the determination of two additional LECs; namely, $c_D$ and $c_E$. These are fit either to the triton ground state energy and $nd$ doublet scattering length [@Piarulli:2017dwd] or to the triton ground state energy and Gamow-Teller matrix element for $\beta$-decay [@Baroni:2018fdn]. The latter fitting procedure corresponds to the model classes denoted with a star, which are the ones used in this work.
