---
doc_id: arxiv-hep-ph-9308276v1
doc_title: "arXiv:hep-ph/9308276v1 14 Aug 1993"
section_id: sec-001-2-the-electroweak-chiral-lagrangian
section_title: "The electroweak chiral Lagrangian"
section_number: 2
pages: 2-14
source_pdf: 9308276v1.pdf
source_sha256: 498931b15afb3f65
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.894
---
We start by writing down the electroweak chiral Lagrangian that is $\gs$ invariant and contains the whole set of CP-invariant operators up to dimension four. We will use the notation of ref. [@F] that is closely related to Longhitano's notation, and will restrict our study to the bosonic sector of electroweak theory. The basic building blocks that are used in the construction of the Lagrangian are the following: $$\begin{aligned}
T & \equiv & U \tau^3 U^\dagger \nonumber\\[2mm] V_\mu & \equiv &
(D_\mu U) U^\dagger \nonumber\\[2mm] D_\mu U & \equiv & \partial_\mu
U - g \wh_\mu U + g' U \bh_\mu \nonumber\\[2mm]
\wtd & \equiv &  \partial_\mu \wh_\nu - \partial_\nu \wh_\mu -
g [\wh_\mu, \wh_\nu]\nonumber\\[2mm]
\btd & \equiv &  \partial_\mu \bh_\nu - \partial_\nu \bh_\mu,
\end{aligned}$$ where the light bosonic fields have been parametrized as $$\begin{aligned}
U & \equiv & \displaystyle{\exp\left( {i \;
\frac{\vec{\tau}\cdot\vec{\pi}}{v}}\right)},
\;\;\; v  = 246 \;{\rm GeV}, \;\;\; \vec{\pi} = (\pi^1,\pi^2,\pi^3),
\nonumber\\ \wh_\mu & \equiv & \frac{ -i}{2}\; \vec{W}_\mu \cdot
\vec{\tau},  \nonumber\\ \bh_\mu & \equiv & \frac{ -i}{2} \; B_\mu \;
\tau^3. 
\end{aligned}$$ Their transformation properties under $\gs$ are $$\begin{aligned}
\wh'_\mu & = & g_{\rm L} \wh_\mu g_{\rm L}^\dagger - \frac{1}{g} g_{\rm L}
\partial_\mu
g_{\rm L}^\dagger\nonumber\\[2mm]
\bh'_\mu & = &  \bh_\mu  - \frac{1}{g'} g_{\rm R}  \partial_\mu g_{\rm
R}^\dagger
\end{aligned}$$ where $$g_{\rm L} = e^{\displaystyle{ i \vec{\alpha}\cdot\vec{\tau} / 2}} \;\;\in
\; SU(2)_{\rm L} , \;\;\;\; g_{\rm R} = e^{\displaystyle{ i \beta \tau^3 / 2}}
\;\;\in \; U(1)_Y .$$ The would-be Goldstone boson fields $\vec{\pi}$ transform non-linearly whereas the $U$ field transforms linearly $$\begin{aligned}
U' & = & g_{\rm L} U g_{\rm R}^\dagger ,\nonumber\\[2mm]
\vec{\pi'} \cdot \vec{\tau} & = & \vec{\pi} \cdot \vec{\tau} +
 v  \vec{\alpha} \cdot \frac{\vec{\tau}}{2} - v \beta
\frac{\tau^3}{2} - (\vec{\alpha}\times\vec{\pi})\cdot
\frac{\vec{\tau}}{2} + \frac{\beta}{2}(\pi_2 \tau_1-\pi_1 \tau_2)+
\nonumber\\[2mm]
 & &
+\frac{1}{6v}[(\vec{\alpha}\cdot\vec{\pi})
(\vec{\pi}\cdot\vec{\tau})-(\vec{\alpha}\cdot\vec{\tau})
(\vec{\pi}\cdot\vec{\pi})]-\frac{\beta}{6v}
[\pi_3(\vec{\pi}\cdot\vec{\tau})-\tau_3(\vec{\pi}\cdot\vec{\pi})]
 + O(\pi^3) .
\end{aligned}$$ The physical gauge fields are defined as $$\begin{aligned}
W^\pm_\mu & = & \frac{W^1_\mu \mp i W^2_\mu}{\sqrt 2},
\nonumber\\[2mm] Z_\mu & = & c_{\rm w} W^3_\mu - s_{\rm w} B_\mu \nonumber,
\\[2mm] A_\mu & = & s_{\rm w} W^3_\mu + c_{\rm w} B_\mu,
\end{aligned}$$ where $c_{\rm w} = \cos \theta_{\rm w}, \; s_{\rm w} = \sin \theta_{\rm w}$ and the weak angle is defined by $\tan \theta_{\rm w} = g' / g$.

At tree level and to lowest order in the derivative expansion, the effective low energy theory for the standard model with a heavy Higgs is the well known Lagrangian of the gauged non-linear sigma model, given by [@L]: $$\begin{aligned}
 \nll & = & \frac{v^2}{4}\; Tr\left[ D_\mu U^\dagger D^\mu U
 \right] + \cl_{\rm G},
\label{NLL} \\[2mm]
\cl_{\rm G} & = & \frac{1}{2}\; Tr\left[ \wtd \wtu + \btd \btu \right] +
\cl_{\rm GF} + \fpnl.
\nonumber
\end{aligned}$$ We have chosen to work in an arbitrary R$_\xi$-covariant gauge with the following gauge fixing term $$\cl_{\rm GF} =-\frac{1}{2\xi_B}f_0^2-
\frac{1}{2\xi_W} \left( \sum_{i=1}^3 f_i^2 \right) ,$$ where $$\begin{aligned}
f_0 & = &   \partial_\mu B^\mu +
\frac{g' v \xi_B}{2} \ \pi_3 ,\nonumber \\[2mm]
f_i & = &   \partial_\mu W_i^\mu -
\frac{g v \xi_W}{2} \  \pi_i , \;\;\; i=1,2,3.
\end{aligned}$$ and the corresponding Faddeev--Popov ghost term is given by $$\fpnl =\sum_{a,b=0}^{3} c_a^\dagger (x) \frac{\delta f_a}{\delta
 \theta_b} c_b(x) ,$$ where $\theta_0 = \beta, \, \theta_i = \alpha_i, \, i=1,2,3$.

It is important to menction that $\fpnl$ does not coincide with the usual Faddeev--Popov Lagrangian of the standard model. Due to the non-linearity of the would-be Goldstone boson modes under infinitesimal $\gs$ transformations, new interactions with increasing number of GB will appear in $\fpnl$. An explicit expression for $\fpnl$ is given in Appendix A. The relevant result is that the couplings of the type two ghosts--one gauge boson and two ghosts--one GB remain the same as in the linear model; but in addition there are new couplings of the type two ghosts--two or more GB that replace the standard coupling two ghosts--one Higgs. Since all these new couplings are proportional to the $\xi$-parameter, it turns out that when the Landau gauge is chosen ($\xi=0$), the Faddeev--Popov terms in the EChL, $\fpnl$, and the standard model, $\fpl$, coincide.

The convenience of the Landau gauge choice in the context of the gauged non-linear sigma model was emphasized by Appelquist and Bernard in [@AB]. Since in this gauge there are no direct copulings of the GB to the ghosts, the non-renormalizability of the GB self-interactions in $\nll$ does not infect graphs with external ghosts. For this reason, the counterterms needed to cancel the divergences generated with $\nll$ at one loop are gauge invariant functions of the GB and gauge fields only. In other R$_\xi$--gauges, there will be also counterterms that are functions of the ghost fields and their structure will have to be determined by using the more general Becchi-Rouet-Stora invariance. This fact, of course, does not preclude the use of R$_\xi$--gauges, but rather establishes the Landau gauge as the easiest one in the context of chiral electroweak theories. Alternatively, if one calculates only Green's fuctions with external gauge particles $\gamma, W^\pm$ and $Z$ as in the present work, all the new required counterterms are manifestly gauge invariant local functions of the GB and gauge fields. This fact can be seen by computing the Green's functions in a generic R$_\xi$--gauge and by checking explicitely the independence of the new counterterms on the $\xi$ parameter.

The non-linear Lagrangian of eq.([\[NLL\]](#NLL){reference-type="ref" reference="NLL"}), when treated at tree level, reproduces correctly the low energy properties of the standard model at tree level and in the heavy Higgs mass limit. In particular, it leads to the proper low energy theorems for the scattering amplitudes of longitudinal vector bosons [@LE]. However, in order to incorporate in the low energy theory the effects of heavy particles beyond the tree level, new effective operators have to be considered. The complete electroweak chiral Lagrangian [@L] containing the whole set of $\gs$ and CP- invariant operators up to dimension four is the following[^1] $$\ecl = \cl_{\rm   NL} + \sum_{i=0}^{13} \cl_{i} ,\label{ECL}$$ where $\nll$ is given in eq.([\[NLL\]](#NLL){reference-type="ref" reference="NLL"}) and the new operators are[^2]: $$\begin{aligned}
\cl_{0} & = & a_0 \frac{v^2}{4} \left[ Tr\left( T V_\mu \right) \right]^2
\nonumber\\[2mm]
\cl_{1} & = & a_1 \frac{i g g'}{2} B_{\mu\nu}  Tr\left( T \wtu \right)
\nonumber\\[2mm]
\cl_{2} & = & a_2 \frac{i g'}{2} B_{\mu\nu} Tr\left( T [V^\mu,V^\nu ]
\right)
\nonumber\\[2mm]
\cl_{3} & = & a_3  g Tr\left( \wtd [V^\mu,V^\nu ]\right)
\nonumber\\[2mm]
\cl_{4} & = & a_4  \left[ Tr\left( V_\mu V_\nu \right) \right]^2
\nonumber\\[2mm]
\cl_{5} & = & a_5  \left[ Tr\left( V_\mu V^\mu \right) \right]^2
\nonumber\\[2mm]
\cl_{6} & = & a_6 Tr\left( V_\mu V_\nu \right) Tr\left( T V^\mu
\right) Tr\left( T V^\nu \right)\nonumber\\[2mm]
\cl_{7} & = & a_7 Tr\left( V_\mu V^\mu \right) \left[ Tr\left( T V^\nu \right)
\right]^2\nonumber\\[2mm]
\cl_{8} & = & a_8  \frac{g^2}{4} \left[ Tr\left( T \wtd \right) \right]^2
\nonumber\\[2mm]
\cl_{9} & = & a_9  \frac{g}{2} Tr\left( T \wtd \right) Tr\left( T [V^\mu,V^\nu
]
\right) \nonumber\\[2mm]
\cl_{10} & = & a_{10} \left[ Tr\left( T V_\mu \right) Tr\left( T V_\nu ]
\right)
\right]^2 \nonumber\\[2mm]
\cl_{11} & = & a_{11} Tr\left( ( D_\mu V^\mu )^2 \right) \nonumber\\[2mm]
\cl_{12} & = & a_{12} Tr\left( T D_\mu D_\nu V^\nu \right) Tr \left( T V^\mu
\right)\nonumber\\[2mm]
\cl_{13} & = & a_{13} \frac{1}{2} \left[ Tr \left( T D_\mu V_\nu \right)
\right]^2 \label{Li}
\end{aligned}$$ Making use of the equations of motion, the above list can be reduced to eleven independent operators. In particular, one could eliminate the 11, 12 and 13 terms by redefining the rest of the terms [@F]. However, since we will not restrict ourselves to calculate on-shell matrix elements, we keep the complete basis given in eq.([\[Li\]](#Li){reference-type="ref" reference="Li"}). Among all these 14 terms, only the first six are truly needed as counterterms to absorb the new divergent structures that appear when calculating to one loop with the non-renormalizable Lagrangian $\nll$ of eq.([\[NLL\]](#NLL){reference-type="ref" reference="NLL"}). However, we retain the complete set to parametrize all the effects of a heavy Higgs to one loop order including both finite and divergent contributions.

We will now give the prescription to compute finite renormalized 1PI Green's functions $\Gamma_{\rm R}^{\rm EChL}$, to one loop order with the effective chiral electroweak Lagrangian of eq.([\[ECL\]](#ECL){reference-type="ref" reference="ECL"}). We choose to regulate the divergences by means of the dimensional regularization method that preserves the Ward identities of the effective theory[^3].

Firstly, there will be contributions to $\Gamma_{\rm R}^{\rm EChL}$ from $\nll$ and the $\cl_i$ 's when used at tree level. These terms will also act as source of counterterms when we rescale the fields and parameters in $\ecl$ according to [@L]: $$\begin{aligned}
B_{\mu}^b & = & \widehat{Z}_B^{1/2} B_\mu \nonumber\\[2mm]
\vec{W}_\mu^b & = & \widehat{Z}_W^{1/2} \vec{W}_\mu
\nonumber\\[2mm] \vec{\pi}^b & =& \widehat{Z}_\pi^{1/2}
\vec{\pi} \nonumber\\[2mm] g^b & =& \widehat{Z}_W^{-1/2} ( g -
\widehat{\delta g} )\nonumber\\[2mm] g'^b & = &
\widehat{Z}_B^{-1/2} ( g' - \widehat{\delta g'} )\nonumber\\[2mm]
v^b & = & \widehat{Z}_\pi^{1/2} ( v -\widehat{ \delta v})\nonumber\\[2mm]
\xi_B^b & = & \xi_B ( 1 + \widehat{\delta \xi}_B)\nonumber\\[2mm]
\xi_W^b & = & \xi_W ( 1 + \widehat{\delta \xi}_W)
\end{aligned}$$ where $\widehat{Z}_i \equiv 1 + \widehat{\delta Z_i}$ and the superscript b denotes bare quantities. The fields and parameters appearing in the right hand side of eq.(13) are renormalized quantities. We have used the hatted notation to distinguish the counterterms of the effective theory from the corresponding quantities in the standard model, to be presented in the next section. Similarly, we rescale the $a_i$'s according to: $$a_i^b = a_i + \delta a_i$$ where the $a_i$'s in the right hand side are renormalized parameters.

Secondly, there will be contributions to $\Gamma_{\rm R}^{\rm EChL}$ from loops generated by $\nll$ and the $\cl_i$'s. The contributions from the $\cl_i$'s at one loop level are subleading with respect to the corresponding ones from $\nll$ because they are either of higher order in powers of the gauge couplings or of higher order in powers of the external momenta, so that they will be neglected from now on.

Finally the renormalized 1PI Green's functions with external gauge particles can be formally defined as $$\Gamma_{\rm R}^{\rm EChL}(\mu) = \Gamma_0^{\rm EChL} + \Gamma_{\rm C}^{\rm
EChL} + \Gamma_{\rm L}^{\rm EChL}$$ where $\Gamma_0^{\rm EChL}$ is the contribution from $\ecl$ at the tree level, $\Gamma_{\rm C}^{\rm EChL}$ is the contribution from the counterterms and $\Gamma_{\rm L}^{\rm EChL}$ is the contribution from the loops generated by $\nll$. The energy scale $\mu$ is the usual scale of dimensional regularization. The final result for $\Gamma_{\rm R}^{\rm EChL}$ must be expressed in terms of the renormalized parameters.

With this prescription at hand one is able to give a finite result for $\Gamma_{\rm R}^{\rm EChL}$. The new divergences generated by $\nll$ at one loop are absorbed into the redefinitions of the $a_i$'s such that the final result for $\Gamma_{\rm R}^{\rm EChL}$ is given in terms of the renormalized parameters $a_i(\mu) = a_i^b - \delta a_i$ that are, in general, $\mu$-scale and renormalization prescription dependent. These renormalized $a_i(\mu)$ parameters incorporate the effects of the heavy particles at one loop, and can be explicitely computed by the matching procedure when the underlying fundamental theory is known.

# Effective Lagrangian parameters for a heavy Higgs

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

[^1]: There is an extra term $\cl_{14}$ proportional to $\epsilon^{\mu
    \nu\alpha\beta}$ that is CP conserving but C and P violating [@F; @AW]. It is not relevant in case of absence of fermion contributions and will not be considered here.

[^2]: The relation with Longhitano's notation is the following: $a_0=g^2\beta_1\;;\;a_1=\frac{g}{g'}\alpha_1\;;\;
    a_2=\frac{g}{g'}\alpha_2\;;\;a_3=-\alpha_3\;;\;a_i=\alpha_i\;,
    i=4,5,6,7\;;\;a_8=-\alpha_8\;;\;a_9=-\alpha_9\;;\;
    a_{10}=\alpha_{10}/2\;;\;a_{11}=\alpha_{11}\;;\;
    a_{12}=\alpha_{12}/2\;;\;a_{13}=\alpha_{13}$.

[^3]: A recent discussion on regularization methods in Chiral Perturbation Theory has been done in [@EM]
