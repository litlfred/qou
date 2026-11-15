---
doc_id: arxiv-hep-ph-0601023v3
doc_title: "Proton Stability in Grand Unified Theories, in Strings and in Branes"
section_id: sec-055-15-renormalization-of-the-d5-and-d6-operators
section_title: "Renormalization of the $d=5$ and $d=6$ operators"
section_number: 15
pages: 173-174
source_pdf: 0601023v3.pdf
source_sha256: 875ab040b50487a1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.949
doc_brief: "Proton Stability in Grand Unified Theories, in Strings and in Branes — A broad overview of the current status of proton stability in uni- ﬁed models of particle interactions is given which includes"
---
In this appendix we  discuss the renormalization effects for the 
$d=5$ and $d=6$ operators for proton decay. Typically
the $d=5$ effective operators are obtained at the GUT scale, once we integrate out 
the colored triplets. Before we dress those operators at the electroweak 
scale to obtain the $d=6$ effective operators, we have 
to run them from the GUT scale to the electroweak scale. After the dressing, 
we have to compute their coefficients at the proton decay scale $1$ GeV, 
and then use the Chiral Lagrangian technique to compute the lifetime for the 
different decay channels.    

The superpotential for the $d=5$ operators is 
\begin{eqnarray}
W_5 &=& \frac{1}{M_T} C_{L}^{ijkl} 
\ \epsilon_{abc} \ \epsilon_{\alpha \beta} \ \epsilon_{\gamma \delta} 
\ \hat{Q}_k^{a \alpha} \ \hat{Q}_l^{b \beta} \ 
\hat{Q}_i^{c \gamma} \ \hat{L}_{j}^{\delta} \ \nonumber\\
&+& \
\frac{1}{M_T} C_{R}^{ijkl} \ \epsilon_{abc} \ \hat{E}^C_k \ 
\hat{U}^C_{la} \ \hat{U}^C_{ib} \ \hat{D}^C_{jc} 
\end{eqnarray}   
where a, b, and c are the color indices. The coefficients $C_{L}$ 
and $C_{R}$ are functions of the Yukawa couplings and fermionic 
mixings at the GUT scale. Therefore in each model we have to find 
their expressions and values at the GUT scale and carry out the  RG 
evolution from the GUT scale down to the SUSY breaking scale~\cite{Goto:1998qg}. 

\begin{eqnarray}
(4 \pi)^2 \mu \frac{d}{d\mu} C_{L}^{ijkl} &=& 
(-8 g_3^2 -6 g_2^2 - \frac{2}{3} g_1^2) C_{L}^{ijkl} \nonumber\\
&+& C_{L}^{mjkl} (Y_D Y_D^{\dagger} + Y_U Y_U^{\dagger})^i_m \ + \
C_{L}^{imkl} (Y_L^{\dagger} Y_L)^j_m \nonumber\\
&+& C_{L}^{ijml} ( Y_D Y_D^{\dagger} + Y_U Y_U^{\dagger})^k_m 
\nonumber\\
&+& C_{L}^{ijkm} (Y_D Y_D^{\dagger} + Y_U Y_U^{\dagger})^l_m
\end{eqnarray}
and
\begin{eqnarray}
(4 \pi)^2 \mu \frac{d}{d\mu} C_{R}^{ijkl} &=& (-8 g_3^2 - 4 g_1^2) 
C_{R}^{ijkl} \ +\ C_{R}^{mjkl} ( 2 Y_U^{\dagger} Y_U)^i_m \ + \ \nonumber\\
&+&  C_{R}^{imkl} (2 Y_D^{\dagger} Y_D)^j_m \ + \ C_{R}^{ijml} 
(2 Y_L Y_L^{\dagger})^k_m \nonumber\\
&+& C_{R}^{ijkm} (2 Y_U^{\dagger} Y_U)^l_m
\end{eqnarray}
where $\mu$ is the renormalization scale, $Y_i$, and $g_i$ are the 
Yukawa matrices and gauge couplings.

Once we know  $C_{L}$ and $C_{R}$ at the electroweak scale, we can 
dress the $d=5$ operators. In order to estimate 
the value of the effective operators at the proton decay scale, we have 
to consider the long-range renormalization factor due to the QCD 
interaction between the SUSY scale ($m_{SUSY} \approx m_Z$) 
and the proton decay scale of 1 GeV. This factor is given by~\cite{Hisano:2000dg}:

\begin{equation}
A_L = \left(\frac{\alpha_s ( \mu_{had})}{ \alpha_s (m_b)}\right)^{6/25} 
\times 
\ \left(\frac{\alpha_s (m_b)}{\alpha_s (m_Z)}\right)^{6/23} \approx 1.4 
\end{equation} 

\\
\\
Long range effects  also  receive important  two loop QCD corrections 
which have  been computed  in ~\cite{Nihei:1994tx}. The reader is 
referred to this work for further details. 
In Sec.(3) we discussed  the most generic predictions 
for nucleon decay from the gauge $d=6$ operators. In this case 
proton decay is mediated by superheavy gauge bosons with mass $M_V$. 
Those effective operators are obtained at the GUT scale 
once the gauge bosons are integrated out. Since we have to 
compute the lifetime of the proton at 1 GeV, 
we have to carry out the RG evolution of these operators from the GUT scale 
to the electroweak scale and from the $M_Z$ scale to 1 GeV. In this case 
the effective $d=6$ operator will be multiply by a factor 
$A_R = A_R^{SD} A_L$, where the coefficient $A_{R}^{SD}$ is the 
short-distance renormalization factor which at one-loop 
(neglecting the flavour dependence of those operators) 
is given by~\cite{Hisano:2000dg}: 

\begin{equation}
A_R^{SD} = \left(\frac{\alpha_3 (m_Z)}{\alpha_{GUT}}\right)^{\frac{4}{3b_3}} \times
\left( \frac{\alpha_2 (m_Z)}{\alpha_{GUT}}\right)^{\frac{3}{2 b_2}} 
\end{equation}
where $b_3 = 9-2 n_g$ and $b_2 = 5- 2 n_g$ with $n_g$ is the number of 
families. $A_R^{SD} \approx 2.0$ if SUSY is the low energy effective 
theory below the GUT scale.
