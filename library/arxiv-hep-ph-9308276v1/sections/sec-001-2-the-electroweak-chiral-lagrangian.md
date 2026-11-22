---
doc_id: arxiv-hep-ph-9308276v1
doc_title: "The Electroweak Chiral Lagrangian for the Standard Model with a heavy Higgs"
section_id: sec-001-2-the-electroweak-chiral-lagrangian
section_title: "The electroweak chiral Lagrangian"
section_number: 2
pages: 3-8
source_pdf: 9308276v1.pdf
source_sha256: 498931b15afb3f65
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.994
doc_brief: "The Electroweak Chiral Lagrangian for the Standard Model with a heavy Higgs — The most general chiral Lagrangian for electroweak interactions with the complete set of SU(2)L × U(1)Y invariant"
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

[^1]: There is an extra term $\cl_{14}$ proportional to $\epsilon^{\mu
    \nu\alpha\beta}$ that is CP conserving but C and P violating [@F; @AW]. It is not relevant in case of absence of fermion contributions and will not be considered here.

[^2]: The relation with Longhitano's notation is the following: $a_0=g^2\beta_1\;;\;a_1=\frac{g}{g'}\alpha_1\;;\;
    a_2=\frac{g}{g'}\alpha_2\;;\;a_3=-\alpha_3\;;\;a_i=\alpha_i\;,
    i=4,5,6,7\;;\;a_8=-\alpha_8\;;\;a_9=-\alpha_9\;;\;
    a_{10}=\alpha_{10}/2\;;\;a_{11}=\alpha_{11}\;;\;
    a_{12}=\alpha_{12}/2\;;\;a_{13}=\alpha_{13}$.

[^3]: A recent discussion on regularization methods in Chiral Perturbation Theory has been done in [@EM]
