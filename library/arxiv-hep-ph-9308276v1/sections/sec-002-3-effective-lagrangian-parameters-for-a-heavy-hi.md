---
doc_id: arxiv-hep-ph-9308276v1
doc_title: "The Electroweak Chiral Lagrangian for the Standard Model with a heavy Higgs"
section_id: sec-002-3-effective-lagrangian-parameters-for-a-heavy-hi
section_title: "Effective Lagrangian parameters for a heavy Higgs"
section_number: 3
pages: 8-14
source_pdf: 9308276v1.pdf
source_sha256: 498931b15afb3f65
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "The Electroweak Chiral Lagrangian for the Standard Model with a heavy Higgs — The most general chiral Lagrangian for electroweak interactions with the complete set of SU(2)L × U(1)Y invariant"
---
As we have already said, the fundamental theory that we want to represent by the electroweak chiral Lagrangian is the standard model with a heavy Higgs particle. We start with the standard model Lagrangian $$\cl_{\rm SM} = (D_\mu \Phi)^\dagger (D^\mu \Phi) + \mu^2 \Phi^\dagger \Phi -
\lambda (\Phi^\dagger \Phi)^2 + \frac{1}{2} Tr \left( \wtd \wtu + \btd \btu
\right)
+ \cl_{\rm GF} + \cl_{\rm FP} ,$$ where $$\Phi  = \frac{1}{\sqrt 2}\left( \begin{array}{c}\phi_1 - i \phi_2 \\
     \sigma + i \chi \end{array}\right), \;\;\;\;\;
(\pi_1,\pi_2,\pi_3)  \equiv  (-\phi_2,\phi_1,-\chi) ,\;\;\;\;\;
 v=\sqrt{\frac{\mu^2}{\lambda}}
\nonumber$$ $$D_\mu \Phi  \equiv  ( \partial_\mu + \frac{1}{2} i g
\vec{W}_\mu\cdot\vec{\tau} +
\frac{1}{2} i g' B_\mu) \Phi .$$ $\wtd, \btd$ and $\cl_{\rm GF}$ are defined in eqs.(1), (8) and (9) and $\cl_{\rm FP}$ is the usual Faddeev--Popov term of the standard model.

The next step is to rescale the fields and parameters in $\cl_{\rm
SM}$, according to: $$\begin{aligned}
B_{\mu}^b & =& Z_B^{1/2} B_\mu \nonumber\\[2mm]
\vec{W}_\mu^b & = & Z_W^{1/2} \vec{W}_\mu \nonumber\\[2mm]
\vec{\pi}^b & =& Z_\pi^{1/2} \vec{\pi} \nonumber\\[2mm]
g^b & = & Z_W^{-1/2} ( g - \delta g ) \nonumber\\[2mm]
g'^b & = & Z_B^{-1/2} ( g' - \delta g' ) \nonumber\\[2mm]
v^b & = & Z_\pi^{1/2} ( v - \delta v )\nonumber\\[2mm]
\xi_B^b & = & \xi_B ( 1 + \delta \xi_B )\nonumber\\[2mm]
\xi_W^b & = & \xi_W ( 1 + \delta \xi_W )
\end{aligned}$$ We present here just the relevant parameters for the computation of the two and three point functions with external $\gamma, W$ and $Z$ particles that are what concerns us in this work. The effects from the renormalization of the $\lambda$ coupling and the Higgs mass on these two and three point functions are of higher order in perturbation theory and can be neglected from now on. This will not be the case for the four point functions where there are contributions from the Higgs particle already at tree level [@HR1].

From the computational point of view, the large $\mh$ limit means that one neglects the contributions to the one-light-particle irreducible (1LPI) Green's functions that depend on (p$/\mh)^2$ and/or (m$/\mh)^2$ and vanish when the formal $\mh \rightarrow \infty$ limit is taken. The 1LPI functions are, by definition, the Green's functions with only light particles in the external legs and where the graphs contributing to them cannot be disconnected by cutting a single light particle line.

When computing the renormalized Green's functions to one loop in the standard model and in the large $\mh$ limit,care must be taken since clearly the operations of making loop integrals and taking the large $\mh$ limit do not commute. Thus, one must first regulate the loop integrals by dimensional regularization, then perform the renormalization operation with some fixed prescription and at the end take the large $\mh$ limit, with $\mh$ being the renormalized Higgs mass. The large $\mh$ values must be bounded in practice to the range m$^2$, p$^2 \ll \mh^2 \lsim 1$ TeV$^2$ where p$^2$ represent the available external momenta and m$^2$ the light (renormalized) particle masses (m = M$_{\rm W}$ or M$_{\rm Z}$).

Finally, the renormalized 1LPI functions with external $\gamma$, W and Z particles are formally defined as $$\Gamma_{\rm R}^{\rm SM}(\mu) = \Gamma_0^{\rm SM} + \Gamma_{\rm C}^{\rm SM}
+ \Gamma_{\rm L}^{\rm SM}$$ where $\Gamma_0^{\rm SM}$ is the contribution from $\cl_{\rm
SM}$ at the tree level, $\Gamma_{\rm C}^{\rm SM}$ is the contribution from the counterterms $\delta Z_i = Z_i-1$ and $\Gamma_{\rm L}^{\rm SM}$ is the contribution from all the one loop graphs of the bosonic sector of the standard model with the heavy Higgs mass limit to be taken as explained above.

We now focus our attention on the matching condition for relating the two theories, the fundamental underlying theory and the effective one. We will impose here the strongest form of matching by requiring that all renormalized 1LPI functions with external light particles are the same in the two theories at scales $\mu \leq \mh$. This matching condition is equivalent to the equality of the light particle effective action in the two descriptions. In contrast, the weaker form of matching is established when the equality of the two theories is done at the physical amplitudes level. In this work we perform the matching of the two theories at the one loop level and we apply it to the complete set of 1LPI functions with external $\gamma, W$ and $Z$ particles. This matching procedure is summarized in the following simple condition: $$\Gamma_{\rm R}^{\rm SM}(\mu ) =\Gamma_{\rm R}^{\rm EChL}(\mu )
\; , \;\;\;\;\;\;\;\;\;\;\;\;\mu\leq \mh$$ where the large Higgs mass limit in the left-hand side must be understood throughout. This equation represents symbolically a whole system of tensorial coupled equations (as many as 1LPI functions) with several unknowns, namely the complete set of parameters $a_i(\mu)$ and counterterms that we are interested in determining.

In the following we will present the results for the two and three 1LPI functions with external gauge particles. The matching conditions are summarized by the following system of six tensorial equations: $$\begin{aligned}
\Pi^{ab}_{0 \mu\nu} + \Pi^{ab}_{{\rm C} \mu\nu} +
\Pi^{ab}_{{\rm L} \mu\nu} & = &
\widehat{\Pi}^{ab}_{0 \mu\nu} + \widehat{\Pi}^{ab}_{{\rm C} \mu\nu} +
\widehat{\Pi}^{ab}_{{\rm L} \mu\nu} \label{PM}\\[2mm]
V^{abc}_{0 \lambda\mu\nu} + V^{abc}_{{\rm C} \lambda\mu\nu} +
V^{abc}_{{\rm L}\lambda\mu\nu} & = &
\widehat{V}^{abc}_{0 \lambda\mu\nu} + \widehat{V}^{abc}_{{\rm C}
 \lambda\mu\nu} +\widehat{V}^{abc}_{{\rm L} \lambda\mu\nu} \label{VM}
\end{aligned}$$ where $ab = WW, ZZ, \gamma\gamma , \gamma Z$ and $abc = \gamma WW,
ZWW$ and the large Higgs mass limit in the left-hand side must be understood throughout. Here we have used the hat to denote the quantities in the effective theory, thus, the left hand side of the above equations refers to the standard model predictions and the right hand side to the EChL predictions.

The resulting expressions for the tree level plus counterterms contributions have been collected in Appendix B. The one loop contributions to the 1LPI functions are represented in figures 1, 2 and 3. As mentioned above, a 1LPI function does not include diagrams that can be disconnected by cutting a light particle line, namely, a non-Higgs particle line. We have included all the one-loop 1LPI diagrams and analized them one by one in the large $\mh$ limit and in a generic $R_\xi$--gauge. In order to study the large $\mh$ limit of the various one-loop Feynman integrals, we have used the techniques developed in [@CAR; @O]. Particularly useful is the application of the m-theorem [@CAR] and the Lebesgue dominated convergence theorem, that allows us to discard convergent integrals that vanish in the large $\mh$ limit. Thanks to these techniques, we have been able to perform a systematic computation in a generic $R_\xi$--gauge that otherwise would have been much more tedious.

We start by reporting the results on the two point functions. Fig.(1) shows a comparative list of the one-loop 1LPI diagrams both in the standard model and in the effective EChL theory for $WW$ and $ZZ$ two point functions. Among the whole set of diagrams, some of those coming from the purely light sector are exactly the same in the SM and the effective EChL. This is the case of diagrams in the first line of figs.(1.a) and (1.b), as for instance the two point diagrams with only gauge particles flowing in the loop, (i) = ($\hat{\rm i}$), (r) = ($\hat{\rm r}$). This subset of diagrams are represented symbolically by ellipsis in fig.(1) and their contribution can be simply dropped out from both sides of the matching condition ([\[PM\]](#PM){reference-type="ref" reference="PM"}). There are a second class of diagrams that also come from the purely light sector, but they are not the same in the two theories, as the case of diagrams with GB particles flowing in the loop. This is because some vertices in $\nll$, like those for two gauge bosons--two GB, are different from the standard model ones, as a consequence of the non-linear realization of the gauge symmetry. However, these long distance contributions drop out from the matching condition because the following identities hold in the large $\mh$ limit: (j) + (k) = 0, (s) + (t) = ($\hat{\rm s}$) and (u) + (v) = 0. The rest of the tadpole diagrams with a Higgs propagator attached to the gauge line not appearing explicitely in fig.(1) vanish in the large $\mh$ limit. Finally, there is a third class of diagrams in the SM that contain the Higgs particle in the loops and whose contributions to the matching equations in the large $\mh$ limit are the relevant ones. These are diagrams (l), (m), (n) and (o) of Fig.(1.a) and (w), (x), (y) and (z) of Fig.(1.b). The role being played by them in the SM is replaced by the $a_i$ terms in the effective theory. This is an important point, and is equivalent to saying that the difference between the Green's functions of the two theories is an analytic function, which for momenta much lower than the scale $\mh$ can be approximated by a polynomial whose coefficients are given by the $a_i$'s.

The matching conditions for the $\gamma \gamma$ and $\gamma$Z two point functions are easily fixed since in these two cases there are neither one-loop contributions from the Higgs particle nor any difference in the diagrams of the two theories from the light sector. Thus, the possible difference in the Green's functions of the two theories are summarized in the different tree level and counterterms contributions that can be found in Appendix B.

The final results for the loop contributions $\Pi^{ab}_{{\rm L} \mu\nu}$, $ab = WW, ZZ, \gamma\gamma, \gamma Z$, are summarized in Appendix B.

Finally, we report the results on the three point 1LPI functions. The diagrams contributing to the SM functions $V^{\gamma
WW}_{{\rm L} \lambda\mu\nu}$ and $V^{ZWW}_{{\rm L} \lambda\mu\nu}$ are shown in figs.(2) and (3) respectively. The diagrams from the purely light sector that are equal in the two theories are not shown explicitely. As in the case of the two point functions, these contributions will be dropped out from both sides of the matching equation ([\[VM\]](#VM){reference-type="ref" reference="VM"}). For the rest of the diagrams the situation is the following. In the case of $V^{\gamma WW}_{{\rm L} \lambda\mu\nu}$ in fig.(2), diagrams (b), (c), (d), (g), (h) and (i) vanish in the large $\mh$ limit. Besides, it turns out that (j) + (k) =0. We have checked that the corresponding diagram in the effective theory also vanish ($\hat{\rm
j}$)=0. In summary, we are left with three relevant diagrams, namely (a), (e) and (f) that we have evaluated in the large $\mh$ limit.

Regarding $V^{ZWW}_{{\rm L} \lambda\mu\nu}$ in fig.(3) the situation is quite similar. The diagrams vanishing in the large $\mh$ limit are the following: (b), (c), (d), (g), (h), (i), (j), (m), (n) and (o). There is again a cancellation among diagrams, (p) + (q) =0 and corresponds to the vanishing in the effective theory of the corresponding diagram ($\hat{\rm p}$) =0. The relevant diagrams that we have computed in the large $\mh$ limit are therefore (a), (e), (f), (k) and (l).

The final results for the loop contributions $V^{VWW}_{{\rm L} \lambda\mu\nu}$, $V=\gamma ,Z$ are summarized in Appendix B.

Having all the pieces entering in the matching eqs.([\[PM\]](#PM){reference-type="ref" reference="PM"},[\[VM\]](#VM){reference-type="ref" reference="VM"}) well defined, we now solve the system formed by these six tensorial equations. There is just one compatible solution and is given by a set of particular values of the $a_i$ parameters and counterterms. Obviously, the renormalized parameters $a_i(\mu)$ are scheme renormalization dependent. Here we have chosen the $\overline{MS}$ scheme by fixing the counterterms $\delta a_i$ to the particular values given below. From now on, we will use the short notation $a_i^\msb(\mu)$ for the renormalized parameters in the $\overline{MS}$ scheme. After some algebra we find the following final result: $$\begin{array}{rlrl}
a_0^\msb(\mu)  = & {\displaystyle g'^2  \frac{1}{16 \pi^2}
\frac{3}{8}\left( \frac{5}{6} - \log\frac{M_H^2}{\mu^2} \right)}, \;\;\;\;\;\;
\;\;\;\;& \delta a_0 = & {\displaystyle g'^2 \frac{1}{16 \pi^2} \frac{3}{8}
\Delta_\epsilon } \\[3mm]
a_1^\msb(\mu)  = & {\displaystyle \frac{1}{16 \pi^2}  \frac{1}{12}
\left( \frac{5}{6} - \log\frac{M_H^2}{\mu^2} \right)},
& \delta a_1 = & {\displaystyle \frac{1}{16 \pi^2} \frac{1}{12}
\Delta_\epsilon }\\[3mm]
a_2^\msb(\mu)  = & {\displaystyle \frac{1}{16 \pi^2} \frac{1}{24}
\left( \frac{17}{6} - \log\frac{M_H^2}{\mu^2} \right)},
& \delta a_2 = & {\displaystyle \frac{1}{16 \pi^2} \frac{1}{24}
\Delta_\epsilon }\\[3mm]
a_3^\msb(\mu)  = & {\displaystyle \frac{-1}{16 \pi^2} \frac{1}{24}
\left( \frac{17}{6} - \log\frac{M_H^2}{\mu^2} \right)},
& \delta a_3 = & {\displaystyle \frac{-1}{16 \pi^2} \frac{1}{24}
\Delta_\epsilon }\\[3mm]
a_8^\msb(\mu)  = & 0, & \delta a_8 = & 0\\[3mm] a_9^\msb(\mu)
= & 0, & \delta a_9 = & 0 \\[3mm] a_{11}^\msb(\mu)  = &{\displaystyle
\frac{-1}{16 \pi^2}\frac{1}{24}}, & \delta a_{11} = & 0 \\[3mm]
a_{12}^\msb(\mu)  = & 0, & \delta a_{12} = & 0 \\[3mm]
a_{13}^\msb(\mu)  = & 0, & \delta a_{13} = & 0 \\[3mm]
\end{array}
\label{aMH}$$ where $$\Delta_\epsilon  \equiv  \frac{2}{\epsilon} - \gamma_E + \log 4 \pi$$

The solution ([\[aMH\]](#aMH){reference-type="ref" reference="aMH"}) of the matching conditions reproduces some partial results obtained before by other authors with different methods. Firstly, we recover the values of the counterterms that were first computed by Longuitano in the non-linear sigma model [@L]. We obtain as well the proper logarithmic running with the scale of the renormalized parameters $a_i(\mu)$. This $\mu$-scale dependence can be summarized by the following set of renormalization group equations: $$\begin{aligned}
a_0(\mu) & = &a_0(\mu') + \frac{g'^2}{16 \pi^2} \frac{3}{8}
\log\frac{\mu^2}{\mu'^2}\nonumber\\[2mm]
a_1(\mu) & = &a_1(\mu') + \frac{1}{16 \pi^2} \frac{1}{12}
\log\frac{\mu^2}{\mu'^2}\nonumber\\[2mm]
a_2(\mu) & = &a_2(\mu') + \frac{1}{16 \pi^2} \frac{1}{24}
\log\frac{\mu^2}{\mu'^2}\nonumber\\[2mm]
a_3(\mu) & = &a_3(\mu') - \frac{1}{16 \pi^2} \frac{1}{24}
\log\frac{\mu^2}{\mu'^2}
\label{RGE}
\end{aligned}$$ The paremeters $a_8$, $a_9$, $a_{11}$, $a_{12}$ and $a_{13}$ are obviously $\mu$-independent.

It is important to stress at this point that the logarithmic running with the $\mu$-scale depends only on the form of the lowest order universal Lagrangian $\nll$ and therefore, it will be the same for any underlying theory having the electroweak chiral Lagrangian as low energy effective theory. The differences amongst alternative fundamental theories will come, at one loop level, in the finite contributions to the effective Lagrangian parameters.

The rest of $a_i$'s cannot be obtained from this computation since they do not contribute to the two and three pont functions for gauge fields. A completely analogous computation of the whole set of four point 1LPI functions must be performed to extract the values of $a_4, a_5, a_6, a_7$ and $a_{10}$ as well as the corresponding counterterms [@HR1].

As far as the gauge sector is concerned, the matching equations provide a set of consistency relations among the corresponding counterterms of the two theories. We get the following relations: $$\begin{aligned}
 \Delta Z_W & = & - \frac{g^2} {16\pi^2}
\frac{1}{12} \left(\Delta_\epsilon + \frac{5}{6}
- \log\frac{M_H^2}{\mu^2} \right)\nonumber\\[2mm]
 \Delta Z_B & = & - \frac{g'^2} {16\pi^2}
\frac{1}{12} \left(\Delta_\epsilon + \frac{5}{6}
- \log\frac{M_H^2}{\mu^2} \right)\nonumber\\[2mm]
\Delta\xi_W & = &\Delta Z_W\nonumber\\[2mm]
 \Delta\xi_B & = &\Delta Z_B\nonumber\\[2mm]
 \frac{\Delta g}{g} & = & 0\nonumber\\[2mm]
 \frac{\Delta g'}{g'} & = & 0\label{Zs}
\end{aligned}$$ where we have defined the differences of the conterterms as, $$\Delta Q \equiv \delta Q- \widehat{\delta Q},\;\;\;\;\;Q=Z_W,Z_B,\xi_W,
     \xi_B,g,g'\nonumber$$ The wave function renormalization constants are not the same in the two theories, a result that accounts for the fact that the effective theory must incorporate the additional logarithmic divergences that arise in the standard model only when $\mh\rightarrow \infty$. Our results of eq.([\[Zs\]](#Zs){reference-type="ref" reference="Zs"}) confirm those found by Longhitano in [@L] that referred just to the terms proportional to $\Delta_\epsilon$. The results in eqs.([\[Zs\]](#Zs){reference-type="ref" reference="Zs"}) give a set of constraints relating the renormalization prescriptions for the effective and the underlying theory. These equations tell us the way one must fix the wave functions and coupling constants renormalizations in the effective theory, once a particular prescription for the standard model counterterms has been assumed.

Finally, to end this section, we have performed a comparison between our results of eq.([\[aMH\]](#aMH){reference-type="ref" reference="aMH"}) and the chiral parameters found by Gasser and Leutwyler in the first paper in [@GL] for the case of the linear sigma model with spontaneously broken $SU(2)_{\rm L}\times
SU(2)_{\rm R}$ symmetry. Since in their case there is no custodial symmetry breaking our set of operators defined in eq.([\[Li\]](#Li){reference-type="ref" reference="Li"}) is larger and contains theirs. A simple exercise shows that the relation among the two sets of bare parameters is the following: $$L_{10}=a_1 ,\;\;\;\; L_9=a_3-a_2 ,\;\;\;\;L_1=a_5 ,\;\;\;\;L_2=a_4 .$$

After performing the renormalization operation in both the $\msb$ scheme and the Gasser and Leutwyler ($GL$) scheme which differ in a finite constant, we find: $$\begin{aligned}
L_{10}^{\rm GL}(\mu) & = & L_{10}^\msb(\mu) - \frac{1}{16\pi^2}
\frac{1}{12} = a_1^\msb(\mu) - \frac{1}{16\pi^2} \frac{1}{12}=
 \nonumber\\[2mm]
  &=&
\frac{-1}{16\pi^2}
\left(\frac{1}{72}+\frac{1}{12}\log \frac{M_H^2}{\mu^2}\right)
\nonumber\\[2mm]
L_9^{\rm GL}(\mu) & = & L_9^\msb(\mu) + \frac{1}{16\pi^2} \frac{1}{12}=
a_3^\msb(\mu) - a_2^\msb(\mu) + \frac{1}{16\pi^2} \frac{1}{12}=
\nonumber\\[2mm]
&=&
\frac{-1}{16\pi^2}
\left(\frac{11}{72}-\frac{1}{12}\log \frac{M_H^2}{\mu^2}\right)
\end{aligned}$$ These values agree with the results found by Gasser and Leutwyler in [@GL]. We find this a quite remarkable result since in their case there are no gauge particles in the loops because the gauge fields were considered as external sources. We believe that this result can be traced back to the fact that the contributions to the effective operators of dimension four that come from mixed gauge--scalar loops are subleading, in the large $\mh$ limit, as compared to the pure scalar loops contributions. On the other hand, since the custodial breaking operators are generated precisely by these mixed loops, one can conclude that the dimension four custodial breaking operators do not get contributions from the Higgs particle at one loop. However, this is not the case for dimension two operators. The custodial breaking operator corresponding to $a_0$ comes from mixed gauge-scalar loops in diagrams (m) in fig.(1.a) and (x) in fig.(1.b) which give a non-vanishing contribution to $a_0$ in the large $\mh$ limit.
