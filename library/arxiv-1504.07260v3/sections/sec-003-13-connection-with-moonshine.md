---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-003-13-connection-with-moonshine
section_title: "Connection with moonshine"
section_number: 1.3
pages: 9-10
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.994
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Monstrous moonshine relates representations of the monster group $\mathbb{M}$ with modular forms, Borcherds-Kac-Moody algebras and conformal field theory. To each element $g\in \mathbb{M}$ one associates a modular form $T_g(\tau)$ (McKay-Thompson series), whose Fourier coefficients are characters of the monster group. The basic conjecture of Conway-Norton, later proven by Borcherds, was that the McKay-Thompson series $T_g(\tau)$ should be invariant under a certain genus zero subgroup $\Gamma_g\subset SL(2,\mathbb{R})$. For some elements $g$, the invariance group $\Gamma_g$ contains a Fricke involution $\tau \to -1/(N\tau)$, analogously to our Fricke S-duality ([\[Fricke\]](#Fricke){reference-type="ref" reference="Fricke"}).

The relation with moonshine goes in fact much deeper than this simple analogy. In recent years a new moonshine phenomenon has been discovered, dubbed Mathieu moonshine, which relates the representation theory of the Mathieu group $M_{24}$ with weak Jacobi forms and superstring theory on $K3$-surfaces [@Eguchi:2010ej; @Cheng:2010pq; @Gaberdiel:2010ch; @Taormina:2010pf; @Gaberdiel:2010ca; @Eguchi:2010fg; @Gaberdiel:2011fg; @Govindarajan:2011em; @Taormina:2011rr; @Cheng:2011ay; @Eguchi:2011aj; @Cheng:2012tq; @Gaberdiel:2012gf; @Gannon:2012ck; @Gaberdiel:2013nya; @Taormina:2013mda; @Cheng:2013wca; @Harrison:2013bya; @Creutzig:2013mqa; @Gaberdiel:2013psa; @Persson:2013xpa]. The role of the McKay-Thompson series is here played by the so called *twining genera* $\phi_g(\tau, z)$, which are weak Jacobi forms with respect to subgroups of $SL(2,\mathbb{Z})$. In our previous work [@Persson:2013xpa] (generalising the earlier results [@Cheng:2010pq; @2012arXiv1208.3453R]), we defined a class of infinite-products, labelled by *commuting pairs* $g,h$ of elements in $M_{24}$: $$\begin{aligned}
\label{infprod} \Phi_{g,h}(\sigma,\tau,z):= p q^{\frac{1}{N}} y\prod_{(d,m,\ell)>0}\prod_{t=0}^{M-1}(1-e^{\frac{2\pi it}{M}}q^{\frac{m}{N}}y^\ell p^d)^{\hat c_{g,h}(d,m,\ell ,t)},
\end{aligned}$$ where the first product runs over $$d,m\in\mathbb{Z}_{\ge 0}\quad \text{and} \quad \begin{cases} \ell\in\mathbb{Z},\ \ell<0, & \text{if }m=0=d\ ,\\
 \ell\in\mathbb{Z}, & \text{otherwise.}
\end{cases}$$ We proved that the functions $\Phi_{g,h}(\sigma,\tau,z)$ are Siegel modular forms with respect to certain discrete subgroups $\Gamma_{g,h}^{(2)}\subset Sp(4;\mathbb{R})$. The automorphic properties of $\Phi_{g,h}(\sigma,\tau,z)$ imply, in particular, that they satisfy the relation: $$\label{Sduality} 
\Phi_{g,h}(\sigma,\tau,z)=\Phi_{g,h'}(\frac{\tau}{N},N\sigma,z)\ ,$$ where we note that $h$ and $h'$ may not be in the same conjugacy class of $M_{24}$. For the case $(g,h)=(e,e)$ one obtains the famous Igusa cusp form $\Phi_{10}$, whose inverse is the generating function of 1/4 BPS-states in $\mathcal{N}=4$ string theory. In this case, ([\[Sduality\]](#Sduality){reference-type="ref" reference="Sduality"}) reduces to ordinary electric-magnetic duality. It was conjectured in [@Persson:2013xpa] that $\Phi_{g,h}^{-1}$ similarly count twisted dyons in the CHL model obtained through orbifolding by $g$. We therefore conclude that whenever these functions have a physical interpretation, the associated CHL model should exhibit a generalization of electric-magnetic dual which acts on the vector of electric-magnetic charges $(Q,P)$ in the following way: $$\left(\begin{array}{c} Q \\ P \end{array}\right) \longmapsto \left(\begin{array}{c} -\frac{1}{\sqrt{N}} P \\ \phantom{-}\sqrt{N} Q \end{array}\right).$$ This electric-magnetic duality precisely corresponds to the $N$-modularity of the associated charge lattices. Thus, the results of the present paper show that this modular property is a consequence of the fact that CHL models satisfy Fricke S-duality. []{#sec:moonshine label="sec:moonshine"}
