---
doc_id: arxiv-hep-ph-9308276v1
doc_title: "The Electroweak Chiral Lagrangian for the Standard Model with a heavy Higgs"
section_id: sec-026-5-conclusions
section_title: "Conclusions"
section_number: 5
pages: 16-20
source_pdf: 9308276v1.pdf
source_sha256: 498931b15afb3f65
doc_brief: "The Electroweak Chiral Lagrangian for the Standard Model with a heavy Higgs — The most general chiral Lagrangian for electroweak interac tions with the complete set of SU (2)L × U (1)Y invariant"
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.989
---
In this paper, we have considered the electroweak chiral Lagrangian that parametrizes electroweak interactions in the case of a heavy Higgs boson. This Lagrangian has been obtained as the low energy effective theory of the standard model when the Higgs particle is integrated out to one--loop order. In particular, we have analyzed the subset of effective operators that contribute to the two-- and three--point Green's functions for gauge bosons. The leading contributions of a heavy Higgs to these operators, including logarithms of the Higgs mass plus finite (non-logarithmic) terms, have been explicitely calculated.

The electroweak chiral Lagrangian provides a general framework to analyze the effects of alternative dynamics of the Higgs sector in low energy observables. Therefore, it is interesting to determine the parameters in the case of a heavy Higgs, since they serve as reference values to be compared with those coming from other models of symmetry breaking. The chiral parameters are directly related to different observables in scattering processes and in precision electroweak measurements, and therefore can be used to constrain the underlying dynamics from experimental data.

# Aknowledgments

We would like to thank A.Dobado and D.Espriu for reading the manuscript and for useful discussions. A special thank goes to C.P.Martı́n for many stimulating discussions, his interesting comments on the manuscript and for his valuable help and patience in explaining us the large-m techniques developed in [@CAR; @O]. We are also indebted to C.Quimbay who participated in the very early stages of this work. M.J.H. aknowledges partial finantial support from the Ministerio de Educacion y Ciencia (Spain) (CICYT AEN90-272). E.R.M. aknowledges support from Dpto. de Matemáticas at UAM and thanks the SLAC theory group for their hospitality.

# Appendix A

The complete expression for $\fpnl$ containing terms up to $O(c c \pi \pi )$ is: $$\begin{aligned}
\fpnl & = & c_0^{\dagger} \left[-\nabla^2 -g'\left( \frac{g' v \xi_B}{2}
\right)
\left[\frac{v}{2}-\frac{1}{6 v}(\pi_1^2 + \pi_2^2) + ...\right] \right]
c_0 \nonumber\\
& & +\sum_{i\ne j \ne k = 1}^3 c_i^{\dagger} \left[-\nabla^2 -g\left(
\frac{g
 v \xi_W}{2} \right)
\left[\frac{v}{2}-\frac{1}{6 v}(\pi_j^2 + \pi_k^2) + ...\right] \right]
c_i \nonumber\\
& & + ( g'\xi_B c^{\dagger}_0 c_1 + g\xi_W c^{\dagger}_1 c_0)
\left(\frac{\sqrt{g g'} v}
{2} \right) \left[ \frac{- \pi_2}{2} + \frac{1}{6 v} \pi_3 \pi_1 + ...\right]
\nonumber\\
& & + ( g'\xi_B c^{\dagger}_0 c_2 + g \xi_W c^{\dagger}_2 c_0)
\left(\frac{\sqrt{g g'} v}
{2} \right) \left[ \frac{ \pi_1}{2} + \frac{1}{6 v} \pi_3 \pi_2 + ...\right]
\nonumber\\
& & + ( g' \xi_B c^{\dagger}_0 c_3 + g \xi_W c^{\dagger}_3 c_0)
\left(\frac{\sqrt{g g'} v}
{2} \right) \left[ \frac{v}{2} - \frac{1}{6 v}(\pi_1^2 + \pi_2^2) + ...\right]
\nonumber\\
& & + (c^{\dagger}_1 c_2 - c^{\dagger}_2 c_1) \left[ - g \partial^\mu
W^3_\mu + g \left(\frac{g v \xi_W}{2}\right) \frac{\pi_3}{2} \right]
\nonumber\\
& & + (c^{\dagger}_1 c_3 - c^{\dagger}_3 c_1) \left[  g \partial^\mu
W^2_\mu - g \left(\frac{g v \xi_W}{2}\right) \frac{\pi_2}{2} \right]
\nonumber\\
& & + (c^{\dagger}_2 c_3 - c^{\dagger}_3 c_2) \left[ - g \partial^\mu
W^1_\mu + g \left(\frac{g v \xi_W}{2}\right) \frac{\pi_1}{2} \right]
\nonumber\\
& & + (c^{\dagger}_1 c_2 + c^{\dagger}_2 c_1) g \left(\frac{g v
\xi_W}{2}\right)
\left(\frac{-1}{6 v}\right) \pi_1 \pi_2 +...\nonumber\\
& & + (c^{\dagger}_1 c_3 + c^{\dagger}_3 c_1) g \left(- \frac{g v
\xi_W}{2}\right)
\left(\frac{+1}{6 v}\right) \pi_1 \pi_3 +...\nonumber\\
& & + (c^{\dagger}_2 c_3 + c^{\dagger}_3 c_2) g \left(\frac{g v
\xi_W}{2}\right)
\left(\frac{-1}{6 v}\right) \pi_2 \pi_3 +...\nonumber
\end{aligned}$$

# Appendix B

In this appendix, we give the different contributions to the one loop Green's functions appearing in the matching equations ([\[PM\]](#PM){reference-type="ref" reference="PM"},[\[VM\]](#VM){reference-type="ref" reference="VM"}). In these formulas, we have not written explicitely the counterterm in the bare $a_i$ coefficients for brevity; therefore the replacement $a_i \rightarrow a_i^{\msb}(\mu)
+ \delta a_i^{\msb}$ has to be understood. The rest of fields and parameters are renormalized quantities.

## Two point functions

The differences in the tree level plus counterterm contributions to the two point functions from the SM and the EChL are given by:

$$\begin{aligned}
-i \Pi^{WW}_{(0+{\rm C}) \mu\nu}+i \widehat{\Pi}^{WW}_{(0+{\rm C})
\mu\nu}&=&
i g_{\mu\nu} \frac{g^2 v^2}{4}
\left[
\Delta Z_\pi -
2 \frac{\Delta g}{g} - 2 \frac{\Delta v}{v} \right]
\nonumber \\[2mm]
& & -i \left( g_{\mu\nu} q^2 - q_\mu q_\nu \right) \Delta Z_W
+ i q_\mu q_\nu \left[\frac{1}{\xi_W} (\Delta\xi_W-\Delta Z_W )
+ g^2 a_{11}\right] \nonumber \\[4mm]

-i \Pi^{ZZ}_{(0+{\rm C}) \mu\nu} +i \widehat{\Pi}^{ZZ}_{(0+{\rm C})
\mu\nu}&=&
i g_{\mu\nu}\frac{(g^2+g'^2) v^2}{4}
\left[\Delta Z_\pi-
2c_{\rm w}^2\frac{\Delta g}{g}-2s_{\rm w}^2\frac{\Delta g'}{g'}
-2\frac{\Delta v}{v}+2a_0\right] \nonumber \\[2mm]
& & -i \left( g_{\mu\nu} q^2 - q_\mu q_\nu \right)
\left[ c_{\rm w}^2 \Delta Z_W
+ s_{\rm w}^2 \Delta Z_B \frac{}{}\right. \nonumber\\[2mm]
& & \left. - c_{\rm w}^2 g^2 a_8 - 2 s_{\rm w}^2 g^2 a_1
- (g^2+g'^2) a_{13} \frac{}{} \right] \nonumber\\[2mm]
& &  +i q_\mu q_\nu \left[ \frac{c_{\rm w}^2}{\xi_W} \left(
\Delta \xi_W - \Delta Z_W \right) + \frac{s_{\rm w}^2}{\xi_B}
\left( \Delta \xi_B - \Delta Z_B \right) \right. \nonumber\\[2mm]
& & \left. + \left(g^2 + g'^2 \right) \left( a_{11} - 2 a_{12} +
a_{13} \right) \frac{}{}\right] \nonumber\\[4mm]

-i \Pi^{\gamma\gamma}_{(0+{\rm C}) \mu\nu} +i
\widehat{\Pi}^{\gamma\gamma}_{(0+{\rm C}) \mu\nu}&=&
-i \left( g_{\mu\nu} q^2 - q_\mu q_\nu \right) \left[
s_{\rm w}^2 \Delta Z_W +
c_{\rm w}^2 \Delta Z_B -
s_{\rm w}^2 g^2 (a_8 - 2 a_1)\frac{}{}\right]\nonumber \\[2mm]
& &+i q_\mu q_\nu \left[ \frac{s_{\rm w}^2}{\xi_W} \left(
\Delta \xi_W - \Delta Z_W \right) + \frac{c_{\rm w}^2}{\xi_B}
\left( \Delta \xi_B - \Delta Z_B \right) \right] \nonumber\\[4mm]

-i \Pi^{\gamma Z}_{(0+{\rm C}) \mu\nu} +i \widehat{\Pi}^{\gamma
Z}_{(0+{\rm C}) \mu\nu}&=&i g_{\mu\nu}  \frac{g g' v^2}{4}
 \left[ \frac{\Delta g'}{g'} - \frac{\Delta g}{g}
\right] \nonumber\\[2mm]
& & -i \left( g_{\mu\nu} q^2 - q_\mu q_\nu \right) \left[
s_{\rm w} c_{\rm w} \Delta Z_W -
s_{\rm w} c_{\rm w} \Delta Z_B \frac{}{}\right.\nonumber\\[2mm]
& & \left. - s_{\rm w} c_{\rm w} g^2 a_8 +
 (c_{\rm w}^2 - s_{\rm w}^2) g g' a_1 \frac{}{}\right] \nonumber\\[2mm]
& & +i q_\mu q_\nu s_{\rm w} c_{\rm w} \left[ \frac{1}{\xi_W} \left(
\Delta \xi_W - \Delta Z_W \right) - \frac{1}{\xi_B}
\left( \Delta \xi_B - \Delta Z_B \right) \right] \nonumber
\end{aligned}$$

In the expressions above, the $\Delta$ quantities represent the standard model counterterms minus the corresponding counterterms in the EChL, that is

$\hspace{1cm}\Delta Q \equiv \delta Q - \widehat{\delta Q}, \hspace{8mm}
{\rm with} \hspace{8mm} Q = Z_{\pi},\; Z_B,\; Z_W,\; \xi_B,\; \xi_W,\;
g,
\; g'\;\;
{\rm and} \;\; v.$

On the other hand, the one loop contributions wich do not cancel among both sides of the matching condition ([\[PM\]](#PM){reference-type="ref" reference="PM"}) are the following: $$\begin{aligned}
-i \Pi^{WW}_{{\rm L} \mu\nu} +i \widehat{\Pi}^{WW}_{{\rm L} \mu\nu}
& = & i g_{\mu \nu} \frac{g^2}{16 \pi^2} \left[  \frac{3}{4} M_H^2
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{7}{6} \right)
\right. \nonumber\\[2mm]
& & \left. - \frac{g^2 v^2}{4} \frac{3}{4}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{5}{6} \right)
\right] \nonumber\\[2mm]
& & - i \left( g_{\mu\nu} q^2 - q_\mu q_\nu \right) \frac{g^2}{16 \pi^2}
\frac{1}{12}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{5}{6} \right)
\nonumber\\[2mm]
& & + i q_\mu q_\nu \; \frac{g^2}{16 \pi^2} \frac{1}{24} \nonumber  \\[4mm]

-i \Pi^{ZZ}_{{\rm L} \mu\nu} +i \widehat{\Pi}^{ZZ}_{{\rm L} \mu\nu}
& = & i g_{\mu \nu} \frac{(g^2 + g'^2)}{16 \pi^2} \left[
\frac{3}{4}  M_H^2 \left( \Delta_\epsilon
- \log\frac{M_H^2}{\mu^2} + \frac{7}{6} \right) \right. \nonumber\\[2mm]
& & \left. - \frac{(g^2 + g'^2) v^2}{4} \frac{3}{4}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{5}{6} \right)
\right] \nonumber\\[2mm]
& & - i \left( g_{\mu\nu} q^2 - q_\mu q_\nu \right)
\frac{(g^2 + g'^2)}{16 \pi^2}\frac{1}{12}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{5}{6} \right)
\nonumber\\[2mm]
& & + i q_\mu q_\nu \frac{(g^2 + g'^2)}{16 \pi^2}  \frac{1}{24}
\nonumber\\[4mm]

-i \Pi^{\gamma\gamma}_{{\rm L} \mu\nu} +i \widehat{\Pi}^{\gamma\gamma}_
{{\rm L} \mu\nu} & = & 0 \nonumber\\[4mm]

-i \Pi^{\gamma Z}_{{\rm L} \mu\nu} +i \widehat{\Pi}^{\gamma Z}_
{{\rm L} \mu\nu}
& = & 0 \nonumber
\end{aligned}$$

## Three point functions

The differences in the tree level plus counterterm contributions to the $\gamma$WW and ZWW 1PI Green's functions from the SM and the EChL are given by: $$\begin{aligned}
-i V^{\gamma WW}_{(0+{\rm C}) \lambda\mu\nu}
+i \widehat{V}^{\gamma WW}_{(0+{\rm C}) \lambda\mu\nu}
& = & -i g s_{\rm w} T^\gamma_{\lambda\mu\nu}
\left[
\Delta Z_W - \frac{\Delta g}{g}
\right] \nonumber \\[2mm]
& &  - i g^3 s_{\rm w} \left( p_{1 \mu} g_{\lambda \nu} - p_{1 \nu}
g_{\lambda \mu}
\right) \left[ a_1 - a_2 + a_3 - a_8 + a_9 \frac{}{}\right] \nonumber\\[2mm]
& & -i g^3 s_{\rm w}  \left( p_{2 \mu} g_{\lambda \nu} - p_{3 \nu}
g_{\lambda \mu}
 \right) a_{11} \nonumber\\[4mm]

-i V^{ZWW}_{(0+{\rm C}) \lambda\mu\nu}
+i \widehat{V}^{ZWW}_{(0+{\rm C}) \lambda\mu\nu} & = &
-i g c_{\rm w} T^Z_{\lambda\mu\nu}
\left[
\Delta Z_W - \frac{\Delta g}{g}
+ \frac{g^2}{c_{\rm w}^2} a_3
\right]\nonumber \\[2mm]
& &  - i g c_{\rm w} \left( p_{1 \mu} g_{\lambda \nu} - p_{1 \nu}
g_{\lambda \mu}
\right) \left[ g'^2 ( a_2 - a_1 - a_3 - a_{13} ) \frac{}{} \right.
\nonumber\\[2mm]
& & \left.+ g^2 ( a_9 - a_8 - a_{13} ) \frac{}{}\right] \nonumber\\[2mm]
& &  - i g c_{\rm w} \left( p_{2 \mu} g_{\lambda \nu} - p_{3 \nu}
g_{\lambda\mu}
\right) \left[ -g'^2 a_{11} + \frac{g^2}{c_{\rm w}^2} a_{12} \right]\nonumber
\end{aligned}$$

where $\Delta Z_W$ and $\Delta g$ are defined as in the two point functions case. The convention for momenta and indexes in the three point functions are defined by the tensor associated to the tree level vertex

$T^{V}_{\lambda\mu\nu} \equiv \left( V_\lambda(p_1),
W^{-}_\mu(p_2), W^+_\nu(p_3) \right) = \left[ (p_1-p_3)_\mu
g_{\lambda\nu} + (p_3-p_2)_\lambda g_{\mu\nu} + (p_2-p_1)_\nu
g_{\lambda\mu} \right]$

and $V = \gamma$ or $Z$. All the momenta are taken incoming.

The one loop contributions which enter the matching equations ([\[VM\]](#VM){reference-type="ref" reference="VM"}) are the following: $$\begin{aligned}
-i V^{\gamma WW}_{{\rm L} \lambda\mu\nu}
+i \widehat{V}^{\gamma WW}_{{\rm L} \lambda\mu\nu}
& = & -i g s_{\rm w} T^\gamma_{\lambda\mu\nu} \frac{g^2}{16 \pi^2} \frac{1}{12}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{5}{6}
\right) \nonumber\\[2mm]
& &  + i g s_{\rm w} \left( p_{1 \mu} g_{\lambda \nu} - p_{1 \nu}
g_{\lambda \mu} \right)  \frac{g^2}{16 \pi^2} \frac{-1}{6} \nonumber\\[2mm]
& & +i g s_{\rm w}  \left( p_{2 \mu} g_{\lambda \nu} - p_{3 \nu}
g_{\lambda \mu} \right)  \frac{g^2}{16 \pi^2} \frac{-1}{24} \nonumber\\[4mm]

-i V^{ZWW}_{{\rm L} \lambda\mu\nu}
+i \widehat{V}^{ZWW}_{{\rm L} \lambda\mu\nu}
& = & -i g c_{\rm w} T^{Z}_{\lambda\mu\nu} \left[
\frac{g^2}{16 \pi^2} \frac{1}{12}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{5}{6}\right) \right.
\nonumber\\[2mm]
& & \left. + \frac{(g^2+g'^2)}{16 \pi^2 } \frac{1}{24}
\left( \Delta_\epsilon - \log\frac{M_H^2}{\mu^2} + \frac{17}{6} \right)
\right] \nonumber\\[2mm]
& &  + i g c_{\rm w} \left( p_{1 \mu} g_{\lambda \nu} - p_{1 \nu}
g_{\lambda \mu} \right)  \frac{g'^2}{16 \pi^2} \frac{1}{6}\nonumber\\[2mm]
& & +i g c_{\rm w}  \left( p_{2 \mu} g_{\lambda \nu} - p_{3 \nu}
g_{\lambda \mu} \right)  \frac{g'^2}{16 \pi^2} \frac{1}{24} \nonumber
\end{aligned}$$

These are all the necessary contributions to solve the matching equations ([\[PM\]](#PM){reference-type="ref" reference="PM"}, [\[VM\]](#VM){reference-type="ref" reference="VM"}).

# Figure Captions

Fig.1

:   **1.a** One-loop diagrams contributing to the $WW$ self- energy in the standard model (left side) and in the effective EChL theory (right side).\
    **1.b** Same as 1.a for the $ZZ$ self-energy.

Fig.2

:   One-loop diagrams contributing to the $\gamma WW$ 1LPI Green's function in the standard model that differ from those in the EChL.

Fig.3

:   Same as Fig.2 for the $ZWW$ three point function.
