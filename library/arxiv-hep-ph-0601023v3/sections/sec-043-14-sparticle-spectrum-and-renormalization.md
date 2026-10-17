---
doc_id: arxiv-hep-ph-0601023v3
doc_title: "arXiv:hep-ph/0601023v3 23 Apr 2007"
section_id: sec-043-14-sparticle-spectrum-and-renormalization
section_title: "Sparticle spectrum and renormalization"
section_number: 14
pages: 168-174
source_pdf: 0601023v3.pdf
source_sha256: 875ab040b50487a1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.889
---
In this appendix we exhibit the sparticle mass matrices 
that enter in the analysis of the dressings of the 
dimension five operators. The matrices are given at the 
electroweak scale, and they are the most general ones including CP phases. 
We list all relevant renormalization group equations at the 
one-loop level for the soft parameters in the MSSM. As discussed already
in Sec.(4.2), in MSSM the superpotential is given by
\beq
W = \hat{U}^C Y_u \hat{Q} \hat{H}_u + \hat{D}^C Y_d \hat{Q} \hat{H}_d + \hat{E}^C Y_e \hat{L} \hat{H}_d + \mu \hat{H}_u \hat{H}_d
\eeq
where $Y_{u,d,e}$ are matrices in family space. The soft SUSY-breaking 
Lagrangian contains scalar couplings
\beq
{\cal L}_{soft} \owns \tilde{u}^C h_u \tilde{Q} H_u + \tilde{d}^C h_d \tilde{Q} H_d 
+ \tilde{e}^C h_e \tilde{L} H_d + B H_u H_d + h.c. 
\eeq
where $h_{u,d,e}$ are $3 \times 3$ matrices. There are also scalar masses
\beq
{\cal L}_{soft} \owns m_{H_u}^2 H_u^{\dagger} H_u + m_{H_d}^2 H_d^{\dagger} H_d 
+ \tilde{Q}^{\dagger} M_{\tilde Q}^2 \tilde{Q} 
+ \tilde{L}^{\dagger} M_{\tilde L}^2 \tilde{L} \nonumber\\
\eeq
\beq 
+ \tilde{u}^{C \dagger} m_{\tilde u}^2 \ \tilde{u}^C + 
\tilde{d}^{C \dagger} m_{\tilde d}^2 \ \tilde{d}^C + 
\tilde{e}^{C \dagger} m_{\tilde e}^2 \ \tilde{e}^C
\eeq 

Here again $M_{\tilde Q}^2$, $M_{\tilde L}^2$, $m_{\tilde u}^2$, 
$m_{\tilde d}^2$, and $m_{\tilde e}^2$ are $3 \times 3$ matrices 
in family space.
The renormalization group equations for the gauge couplings are:

\beq
\frac{d g_a}{dt}=\frac{g_a^3}{16 \pi^2} B_a^{(1)} + \nonumber\\ 
\frac{g_a^3}{(16 \pi^2)^2} \left(  \sum_{b=1}^3 B_{ab}^{2} g_b^2 - \sum_{x=u,d,e} C_a^x Tr (Y_x^{\dagger} Y_x) \right)
\eeq
with $B_a^{(1)}= (33/5, 1, -3)$ for $U(1)_Y$, $SU(2)_L$ 
and $SU(3)_C$, respectively.

\begin{equation}
B_{ab}^{(2)}=\left(
\begin{array}{ccc}
  \frac{199}{25} & \frac{27}{5} & \frac{88}{5} \\ \\
  \frac{9}{5} & 25 & 24 \\ \\
  \frac{11}{5} & 9 & 14 \\ \\
\end{array}\right)
\end{equation}

\begin{equation}
C_{a}^{u,d,e}=\left(
\begin{array}{ccc}
  \frac{26}{5} & \frac{14}{5} & \frac{18}{5} \\ \\
  6 & 6 & 2 \\ \\
  4 & 4 & 0 \\ \\
\end{array}\right)
\end{equation}

The one-loop renormalization group equations 
for the three gaugino mass parameters are~\cite{Martin:1993zk}:

\beq
\frac{d M_a}{dt}= \frac{2 g_a^2}{16 \pi^2} B_a^{(1)} M_a
\eeq
while for the $\mu$ term, and the Yukawa couplings one has:
\beq
\frac{d \mu}{dt}= \frac{\beta_{\mu}^{(1)}}{16 \pi^2}
\eeq
\beq
\frac{d Y_{u,d,e}}{dt} = \frac{\beta_{Y_{u,d,e}}^{(1)}}{16 \pi^2}
\eeq
where
\beq
\beta_{\mu}^{(1)}=\mu \left(  Tr (3 Y_u Y_u^{\dagger} + 3 Y_d Y_d^{\dagger} + Y_e Y_e^{\dagger}) -3 g_2^2 - \frac{3}{5} g_1^2 \right)
\eeq
\beq
\beta_{Y_u}^{(1)}= Y_u \left(  3 Tr(Y_u Y_u^{\dagger}) + 3 Y_u^{\dagger} Y_u + Y_d^{\dagger} Y_d - 
\frac{16}{3} g_3^2 - 3 g_2^2 - \frac{13}{15} g_1^2 \right)
\eeq
\beq
\beta_{Y_d}^{(1)}= Y_d \left( Tr(3 Y_d Y_d^{\dagger} + Y_e Y_e^{\dagger}) + 
3 Y_d^{\dagger} Y_d + Y_u^{\dagger} Y_u - \frac{16}{3}g_3^2 -3 g_2^2 - \frac{7}{15} g_1^2 \right)
\eeq
\beq
\beta_{Y_e}^{(1)}= Y_e \left(  Tr( 3 Y_d Y_d^{\dagger} + Y_e Y_e^{\dagger}) + 
3 Y_e^{\dagger} Y_e - 3 g_2^2 - \frac{9}{5} g_1^2 \right)
\eeq
For the trilinear terms the RG equations are
\beq
\frac{d h_{u,d,e}}{dt}= \frac{{\beta_{h_{u,d,e}}}^{(1)}}{16 \pi^2}
\eeq
where:
\begin{displaymath}
\beta_{h_{u}}^{(1)}= h_u \left(  3 Tr (Y_u Y_u^{\dagger}) + 5 Y_u^{\dagger} Y_u + Y_d^{\dagger} Y_d 
- \frac{16}{3} g_3^2 - 3 g_2^2 - \frac{13}{15} g_1^2 \right) + \nonumber
\end{displaymath}
\beq
+ Y_u \left( 6 Tr(h_u Y_u^{\dagger}) + 4 Y_u^{\dagger} h_u + 2 Y_d^{\dagger}h_d + 
\frac{32}{3} g_3^2 M_3 + 6 g_2^2 M_2 + \frac{26}{15} g_1^2 M_1   \right)
\eeq
\begin{displaymath}
\beta_{h_{d}}^{(1)}= h_d \left( Tr( 3 Y_d Y_d^{\dagger} + Y_e Y_e^{\dagger}) 
+ 5 Y_d^{\dagger} Y_d + Y_u^{\dagger} Y_u - \frac{16}{3}g_3^2 -3 g_2^2 - \frac{7}{15} g_1^2 \right) + \nonumber
\end{displaymath}
\beq
Y_d \left( Tr( 6 h_d Y_d^{\dagger} + 2 h_e Y_e^{\dagger})+ 4 Y_d^{\dagger} h_d 
+ 2 Y_u^{\dagger} h_u + \frac{32}{3} g_3^2 M_3 + 6 g_2^2 M_2 + \frac{14}{15}g_1^2 M_1 \right)
\eeq
\begin{displaymath}
\beta_{h_{e}}^{(1)}= h_e \left( Tr( 3 Y_d Y_d^{\dagger} + Y_e Y_e^{\dagger}) + 5 Y_e^{\dagger} Y_e - 3 g_2^2 
- \frac{9}{5}g_1^2 \right) +
\end{displaymath}
\beq
Y_e \left( Tr( 6 h_d Y_d^{\dagger} + 2 h_e Y_e^{\dagger}) + 4 Y_e^{\dagger} h_e + 6 g_2^2 M_2 + \frac{18}{5} g_1^2 M_1 \right)
\eeq
The renormalization group equation for the B-term is given by

\beq
\frac{d B}{dt}= \frac{\beta_{B}^{(1)}}{16 \pi^2}
\eeq
where 
\begin{displaymath}
\beta_B^{(1)}=B \left( Tr(3 Y_u Y_u^{\dagger} + 3 Y_d Y_d^{\dagger} + Y_e Y_e^{\dagger})- 3 g_2^2 - \frac{3}{5}g_1^2\right)+
\end{displaymath}
\beq
\mu \left( Tr( 6 h_u Y_u^{\dagger} + 6 h_d Y_d^{\dagger} + 2 h_e Y_e^{\dagger})+ 6 g_2^2 M_2 + \frac{6}{5} g_1^2 M_1 \right)
\eeq
while the RG equations for the soft masses are
\beq
\frac{d}{dt}m^2 = \frac{\beta_{m^2}^{(1)}}{16 \pi^2}
\eeq
where 
\begin{displaymath}
\beta_{m_{H_u}^2}^{(1)}= 6 Tr\left( (m_{H_u}^2 + M_{\tilde Q}^2 ) Y_u^{\dagger} Y_u 
+ Y_u^{\dagger} m_{\tilde u}^2 Y_u + h_u^{\dagger} h_u \right)
- 6 g_2^2 |M_2|^2 - \frac{6}{5} g_1^2 |M_1|^2 
\end{displaymath}
\beq
+ \frac{3}{5} g_1^2 S
\eeq
\begin{displaymath}
\beta_{m_{H_d}^2}^{(1)}= Tr ( 6 (m_{H_d}^2 + M_{\tilde Q}^2 ) Y_d^{\dagger} Y_d 
+ 6 Y_d^{\dagger} m_{\tilde d}^2 Y_d + 
2 (m_{H_d}^2 + M_{\tilde L}^2) Y_e^{\dagger} Y_e + 2 Y_e^{\dagger} m_{\tilde e}^2 Y_e 
\end{displaymath}
\beq
+ 6 h_d^{\dagger} h_d + 2 h_e^{\dagger} h_e ) - 6 g_2^2 |M_2|^2 - \frac{6}{5} |M_1|^2 - \frac{3}{5}g_1^2 S
\eeq
\beq
\beta_{M_{\tilde Q}^2}^{(1)}=(M_{\tilde Q}^2 + 2 m_{H_u}^2) Y_u^{\dagger} Y_u + 
(M_{\tilde Q}^2 + 2 m_{H_d}^2)Y_d^{\dagger} Y_d + 
(Y_u^{\dagger} Y_u + Y_d^{\dagger} Y_d) M_{\tilde Q}^2  + 2 Y_u^{\dagger} m_{\tilde u}^2 Y_u
\eeq
\begin{displaymath}
\beta_{M_{\tilde L}^2}^{(1)}=(M_{\tilde L}^2 + 2 m_{H_d}^2) Y_e^{\dagger} Y_e + 
2 Y_e^{\dagger} m_{\tilde e}^2 Y_e + Y_e^{\dagger} Y_e M_{\tilde L}^2 
+2 h_e^{\dagger} h_e -
\end{displaymath}
\beq
- 6 g_2^2 |M_2|^2 -\frac{6}{5} g_1^2 |M_1|^2 - \frac{3}{5} g_1^2 S
\eeq
\begin{displaymath}
\beta_{m_{\tilde u}^2}^{(1)}=( 2 m_{\tilde u}^2 + 4 m_{H_u}^2) Y_u Y_u^{\dagger} 
+ 4 Y_u M_{\tilde Q}^2 Y_u^{\dagger} + 2 Y_u Y_u^{\dagger} m_{\tilde u}^2 + 
\end{displaymath}
\beq
+ 4 h_u h_u^{\dagger} - \frac{32}{3} g_3^2 |M_3|^2 -\frac{32}{15} g_1^2 |M_1|^2 -\frac{4}{5}g_1^2 S 
\eeq
\begin{displaymath}
\beta_{m_{\tilde d}^2}^{(1)}= ( 2 m_{\tilde d}^2 + 4 m_{H_d}^2) Y_d Y_d^{\dagger} 
+ 4 Y_d M_{\tilde Q}^2 Y_d^{\dagger} + 2 Y_d Y_d^{\dagger} m_{\tilde d}^2 + 4 h_d h_d^{\dagger}-
\end{displaymath}
\beq
-\frac{32}{3} g_3^2 |M_3|^2 - \frac{8}{15} g_1^2 |M_1|^2 + \frac{2}{5} g_1^2 S
\eeq
\begin{displaymath}
\beta_{m_{\tilde e}^2}^{(1)}= ( 2 m_{\tilde e}^2 + 4 m_{H_d}^2) Y_e Y_e^{\dagger} 
+ 4 Y_e M_{\tilde L}^2 Y_e^{\dagger} + 2 Y_e Y_e^{\dagger} m_{\tilde e}^2 
+ 4 h_e h_e^{\dagger}-
\end{displaymath}
\beq
-\frac{24}{5} g_1^2 |M_1|^2 + \frac{6}{5} g_1^2 S
\eeq
and where  
\beq
S= m_{H_u}^2 - m_{H_d}^2 + Tr \left( M_{\tilde Q}^2 - M_{\tilde L}^2 - 2 m_{\tilde u}^2 
+ m_{\tilde d}^2 + m_{\tilde e}^2 \right)
\eeq
The full two loop RG equations can be founds in Refs.\cite{Machacek:1983tz,Martin:1993zk}.
Now, let us list the mass matrices for the sparticles in the MSSM.
The chargino mass matrix was already given in Eq.(\ref{chmatrix}). 
For the  neutralino mass matrix one has 

\begin{displaymath}
M_{{\tilde \chi}^0}=\left(\matrix{M_1 & 0 & -M_Z s_W  c_\beta    & M_Z    s_W  s_\beta \cr
                 0  & M_2 & M_Z c_W   c_\beta & -M_Z c_W  s_\beta \cr
		 -M_Z s_W  c_\beta &  M_Z c_W c_\beta & 0 & -\mu \cr
		 M_Z s_W s_\beta  & -M_Z  c_W s_\beta & -\mu & 0}
			\right) \nonumber 
\end{displaymath}
\beq
\eeq
where $\theta_W$ is the weak angle, $s_W=\sin \theta_W$, $s_\beta= \sin\beta$, 
$c_\beta = \cos \beta$, and $s_\beta=\sin \beta$. 
The squark $(mass)^2$  matrix 
for $\tilde{u}$  at the electroweak scale is given by

\begin{displaymath}
M_{\tilde{u}}^2=\left(\matrix{M_{\tilde{Q}}^2+m{_u}^2 + M_{Z}^2(\frac{1}{2}-Q_u
s^2_W)\cos2\beta & m_u(A_{u}^{*} - \mu \cot\beta) \cr
   	          	m_u(A_{u} - \mu^{*} \cot\beta) & 
m_{\tilde{u}}^2+m{_u}^2 + M_{Z}^2 Q_u s^2_W \cos2\beta}
		\right) \nonumber
\end{displaymath}
\beq
\eeq
where $Q_u=\frac{2}{3}$,  and  the squark $(mass)^2$  matrix 
for $\tilde{d}$   is given by

\begin{displaymath}
M_{\tilde{d}}^2=\left(\matrix{M_{\tilde{Q}}^2+m{_d}^2-M_{Z}^2(\frac{1}{2}+Q_d
s^2_W)\cos2\beta & m_d(A_{d}^{*} - \mu \tan\beta) \cr
                        m_d(A_{d} - \mu^{*} \tan\beta) & m_{\tilde{d}
}^2+m{_d}^2+M_{Z}^2 Q_d s^2_W \cos2\beta}
                \right) \nonumber
\end{displaymath}
\beq
\eeq
We note that here we are using the relations $h_{u,d,e}=Y_{u,d,e} A_{u,d,e}$ 
for the trilinear terms. $Q_d=-\frac{1}{3}$. 
Finally, the slepton mass matrix is given by 

\begin{displaymath}
M_{\tilde {\it l}}^2=\left(\matrix{ M_{\tilde L}^2+m_{e}^2 -M_Z^2(\frac{1}{2}
- s^2_W)\cos 2\beta & m_{e}(A_{e}^* - \mu\tan\beta)\cr
m_{e}(A_{e} - \mu^*\tan\beta) &  m_{\tilde e}^2 + m_{e}^2 -M_Z^2 s^2_W
	\cos 2\beta  }
            \right)\nonumber
\end{displaymath}
\beq
\eeq
Further details of supersymmetry phenomenology can be found in 
Refs.~\cite{applied,Nilles:1983ge,Haber:1984rc,recent_susy}.


\section{Renormalization of the $d=5$ and $d=6$ operators} 

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
