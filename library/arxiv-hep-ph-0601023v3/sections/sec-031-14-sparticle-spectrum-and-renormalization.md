---
doc_id: arxiv-hep-ph-0601023v3
doc_title: "arXiv:hep-ph/0601023v3 23 Apr 2007"
section_id: sec-031-14-sparticle-spectrum-and-renormalization
section_title: "Sparticle spectrum and renormalization"
section_number: 14
pages: 168-184
source_pdf: 0601023v3.pdf
source_sha256: 875ab040b50487a1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.938
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



\section{Effective lagrangian for nucleon decay}


As discussed already in supersymmetric theories \bl ~violating 
dimension five operators must be  dressed by gluino, chargino 
and neutralino exchanges to produce dimension six operators. 
These operators are typically of two types: 
$\Delta S=0$ and $\Delta S=1$. 
The \bl violating  $\Delta S=0$ operators are:

\beqn
O_{RL}^{\nu_i}=\epsilon_{abc} \overline{(d_{Ra})^C} u_{Rb} \overline{(d_{Lc})^C} \nu_{iL} \nonumber\\
O_{LL}^{\nu_i}=\epsilon_{abc} \overline{(d_{La})^C} u_{Lb} \overline{(d_{Lc})^C} \nu_{iL} \nonumber\\
O_{RL}^{e_i}=\epsilon_{abc} \overline{(d_{Ra})^C} u_{Rb} \overline{(u_{Lc})^C}  e_{iL} \nonumber\\
O_{LR}^{e_i}=\epsilon_{abc} \overline{(d_{La})^C} u_{Lb} \overline{(u_{Rc})^C}  e_{iR} \nonumber\\
O_{LL}^{e_i}=\epsilon_{abc} \overline{(d_{La})^C} u_{Lb} \overline{(u_{Lc})^C}  e_{iL} \nonumber\\
O_{RR}^{e_i}=\epsilon_{abc} \overline{(d_{Ra})^C} u_{Rb} \overline{(u_{Rc})^C}  e_{iR} 
\label{sz}
\eeqn
In the above a,b,c =1,2,3 are the color indices, and i is the generation index. 
For the $|\Delta S|=1$ the \bl violating dimension six operators are:

\beqn
\tilde O_{RL1}^{\nu_i}=\epsilon_{abc} \overline{(s_{Ra})^C} u_{Rb} \overline{(d_{Lc})^C} \nu_{iL} \nonumber\\
\tilde O_{LL1}^{\nu_i}=\epsilon_{abc} \overline{(s_{La})^C} u_{Lb} \overline{(d_{Lc})^C} \nu_{iL} \nonumber\\
\tilde O_{RL}^{e_i}=\epsilon_{abc} \overline{(s_{Ra})^C} u_{Rb} \overline{(u_{Lc})^C}  e_{iL} \nonumber\\
\tilde O_{LR}^{e_i}=\epsilon_{abc} \overline{(s_{La})^C} u_{Lb} \overline{(u_{Rc})^C}  e_{iR} \nonumber\\
\tilde O_{LL}^{e_i}=\epsilon_{abc} \overline{(s_{La})^C} u_{Lb} \overline{(u_{Lc})^C}  e_{iL} \nonumber\\
\tilde O_{RR}^{e_i}=\epsilon_{abc} \overline{(s_{Ra})^C} u_{Rb} \overline{(u_{Rc})^C}  e_{iR}\nonumber\\ 
\tilde O_{RL2}^{\nu_i}=\epsilon_{abc} \overline{(d_{Ra})^C} u_{Rb} \overline{(s_{Lc})^C} \nu_{iL} \nonumber\\
\tilde O_{LL2}^{\nu_i}=\epsilon_{abc} \overline{(d_{La})^C} u_{Lb} \overline{(s_{Lc})^C} \nu_{iL} 
\label{s1}
\eeqn
 Eq.(\ref{sz}) and Eq.(\ref{s1}) contain all the possible type of dimension six operators, i.e., 
 of  chirality types  RRLL,  LLLL, LLRR, and  RRRR. 

In obtaining the above set of operators one uses a  Fierz reordering. This is best 
 accomplished by defining a set of 16 matrices as follows (see, e.g., ~\cite{Chattopadhyay:1998wb})
 \beq
\Gamma^A=\{1,\gamma^0,i\gamma^i,i\gamma^0\gamma_5,
\gamma^i\gamma_5,\gamma_5,i\sigma^{0i},\sigma^{ij}\}: ~~i,j=1-3
\eeq
which are normalized so that 
\beq
tr(\Gamma^A\Gamma^B)=4\delta^{AB}
\eeq
With the above definitions and normalizations,  the Fierz rearrangement formula 
takes on the  form
\beq
(\bar{u_1}\Gamma^Au_2)(\bar{u_3}\Gamma^Bu_4)=\sum_{C,D}F^{AB}_{CD}
(\bar{u_1}\Gamma^Cu_4)(\bar{u_3}\Gamma^Du_2)
\eeq
where   $u_j$ may be   Dirac or Majorana spinors and
\beq
F^{AB}_{CD}=
-(+)\frac{1}{16}tr(\Gamma^C\Gamma^A\Gamma^D\Gamma^B)
\eeq
In the above the  
+ve (-ve) sign is for commuting (anticommuting) u spinors.
 A -ve sign should be  chosen when  dealing with quantum Majorana 
 and Dirac fields in the Lagrangian. 
 
 The general Lagrangian with \bl ~violating dimension
 six operators will then have the form
 \begin{eqnarray}
 {\cal L_{BL}}&=& C_{RL}^{\nu_i} O_{RL}^{\nu_i} +  C_{LL}^{\nu_i}O_{LL}^{\nu_i} + C_{RL}^{e_i}O_{RL}^{e_i}
+ C_{LR}^{e_i} O_{LR}^{e_i} 
\nonumber\\
&+&  C_{LL}^{e_i}O_{LL}^{e_i}+ C_{RR}^{e_i} O_{RR}^{e_i} + \tilde C_{RL1}^{\nu_i} \tilde O_{RL1}^{\nu_i} 
\nonumber\\
&+& \tilde C_{LL1}^{\nu_i} \tilde O_{LL1}^{\nu_i} + \tilde C_{RL}^{e_i} \tilde O_{RL}^{e_i} + 
\tilde C_{LR}^{e_i} \tilde O_{LR}^{e_i} + \tilde C_{LL}^{e_i} \tilde O_{LL}^{e_i}+
\nonumber\\ 
&+& \tilde C_{RR}^{e_i} \tilde O_{RR}^{e_i} +\tilde C_{RL2}^{\nu_i} \tilde O_{RL2}^{\nu_i} + 
\tilde C_{LL2}^{\nu_i} \tilde O_{LL2}^{\nu_i} 
 \label{lagbl}
\end{eqnarray}
We note that in Eq.(\ref{lagbl}) the neutrinos $\nu_{i}$ are in mass diagonal state and hence are not
related by a simple $SU(2)_L$ symmetry to the corresponding operators with $e_{iL}$.
If we assume that the $\nu_i$ are flavor diagonal, then some of the co-efficients $C's$ and $\tilde C's$
can be related. Thus in this case $C_{RL}^{\nu_i}=-C_{RL}^{e_i}$, $C_{LL}^{\nu_i}=-C_{LL}^{e_i}$,
and $\tilde C_{RL1}^{\nu_i}=-\tilde C_{RL}^{e_i}$, $\tilde C_{LL1}^{\nu_i}=-\tilde C_{LL}^{e_i}$.
These reduce the number of independent couplings from six to four for the $\Delta S=0$ case
and from eight to six  for the $|\Delta S|=1$.
 The co-efficients $C_k^i, \tilde C_k^i$ are determined by the details of the underlying 
 GUT or string theory.  
 In trying to extract the physical implications of this interaction one uses the technique of 
 effective or  phenomenological Lagrangians~\cite{effec_lag}. Specifically 
 what one wishes to do is convert the above interaction which contains
 quarks and leptons into an interaction involving mesons, baryons and leptonic fields. 
 To this end it is useful to classify the operators according to their transformation properties
 under $SU(3)_L\times SU(3)_R$.  
While the analysis below follows closely the work of Ref.~\cite{Claudson:1981gh,Chadha:1983sj,Chadha:1983mh}
   it is more general.  First, we have not imposed any SU(2) symmetry on the operators in 
   Eq.(\ref{sz}) and Eq.(\ref{s1}) since one is below the electro-weak symmetry breaking 
scale where the  residual symmetry is only $SU(3)_C\times U(1)_{em}$. 
Secondly, in the analysis of Chadha and Daniel~\cite{Chadha:1983sj,Chadha:1983mh} only 
the chirality  LLLL type operators were considered in computing the decays. Specifically the
   LLRR and RRLL type operators were not fully included in the computation of proton decay rates.
   This was subsequently corrected in Ref.~\cite{Nath:1985ub}.
    In the following we will give  a full analysis including
   all four types  of operators, i.e., LLLL, RRLL, LLRR and RRRR (For a recent update 
see Ref.~\cite{Aoki:1999tw}). 
We give now the details of  the effective Lagrangian approach.  
  Noting that  $u_{La}, d_{La}$  transform like $3_L$, 
  $u_{Ra}, d_{Ra}$ transform like $3_R$, $3_L\times 3_L =3_L^* +6_L$, $3_L\times 3_L^*=8_L+ 1_L$ etc,
one finds the transformations of the operators  listed in Table (\ref{dim6trans}).  

 \begin{table}[h]
\begin{center}
\begin{tabular}{|r|r|r|}
\hline\hline
Dim 6 operator & Chirality type & Transformation \\
\hline
$ O_{RL}^{\nu_i}, O_{RL}^{e_i},
 \tilde O_{RL1}^{\nu_i}, \tilde O_{RL}^{e_i}, \tilde O_{RL2}^{\nu_i}$& RRLL &$ (3, 3^*)$\\
$ O_{LR}^{e_i}, \tilde O_{LR}^{e_i}$ &  LLRR & $(3^*, 3)$\\
$O_{LL}^{\nu_i}, O_{LL}^{e_i}, \tilde O_{LL1}^{\nu_i}, 
\tilde  O_{LL}^{e_i}, \tilde O_{LL2}^{e_i}$ & LLLL & (8,1)\\
$O_{RR}^{e_i}, \tilde O_{RR}^{e_i}$ & RRRR  & (1,8)\\
\hline
\hline
\end{tabular}
\end{center}
\caption{Properties  of the  dimension six operators  under $SU(3)_L\times SU(3)_R$.} 
\label{dim6trans}
\end{table}

To obtain the effective  Lagrangian for the operators  we  want to simulate  the transformations 
of Table (\ref{dim6trans}) using the baryon and  meson fields. For the baryons we introduce the
matrix
\begin{equation}
B=\sum_{a=1}^8\lambda_a B_a =\pmatrix{\offinterlineskip
 \frac{\Sigma^0}{\sqrt{2}}+\frac{\Lambda}{\sqrt{6}}&\Sigma^+&p\cr
\Sigma^-&     -\frac{\Sigma^0}{\sqrt{2}}+\frac{\Lambda}{\sqrt{6}}   &n\cr
\Xi^-& \Xi^0 & -\sqrt{\frac{2}{3}} \Lambda\cr}
\end{equation}
which transforms under $SU(3)_L\times SU(3)_R$ as  follows
\beqn
B'=UBU^{\dagger}
\eeqn
 while  the transformations of the pseudo-Goldstone  bosons are described as follows
 \beqn
 \xi'= L\xi U^{\dagger} =U\xi R^{\dagger}, ~~\xi =e^{iM/f}
 \eeqn
where
\beqn
M=    \sum_{a=1}^8 \lambda_a \phi_a=
\pmatrix{\offinterlineskip
 \frac{\pi^0}{\sqrt{2}}+\frac{\eta}{\sqrt{6}}&\pi^+&K^+\cr
\pi^-&     -\frac{\pi^0}{\sqrt{2}}+\frac{\eta}{\sqrt{6}}   &K^0\cr
K^-& \bar K^0 & -\sqrt{\frac{2}{3}} \eta\cr}
\eeqn 
Then under  $SU(3)_L\times SU(3)_R$ transformations we have:
\beqn
\xi B\xi \to L\xi B\xi R^{\dagger},~~
\xi^{\dagger}B\xi^{\dagger} \to R\xi^{\dagger} B \xi^{\dagger} L^{\dagger}\nonumber\\
\xi B \xi^{\dagger} \to L\xi B\xi^{\dagger} L^{\dagger},~~
\xi^{\dagger} B\xi \to R \xi^{\dagger} B\xi R^{\dagger}
\eeqn
The above transformations are of the type $(3,3^*)$, $(3^*,3)$, $(8,1)$, and $(1,8)$, 
respectively. However, we must use projection operators to precisely get 
the operators of type in Eq.(\ref{sz}) and Eq.(\ref{s1}). 
We can now  write the $O$  operators as follows~\cite{Claudson:1981gh,Chadha:1983sj}
\beqn
O_{RL}^{\nu_i}= \alpha\overline{(\nu_{iL})^C} Tr(P'\xi B_L \xi)\nonumber\\
O_{LL}^{\nu_i}= \beta\overline{(\nu_{iL})^C} Tr(P'\xi B_L \xi^{\dagger})\nonumber\\
O_{RL}^{e_i}= \alpha\overline{(e_{iL})^C} Tr(P\xi B_L \xi)\nonumber\\
O_{LR}^{e_i}=\alpha\overline{(e_{iR})^C} Tr(P\xi^{\dagger} B_R \xi^{\dagger})\nonumber\\
O_{LL}^{e_i}=\beta\overline{(e_{iL})^C} Tr(P\xi B_L \xi^{\dagger})\nonumber\\
O_{RR}^{e_i}=\beta\overline{(e_{iR})^C} Tr(P\xi^{\dagger} B_R \xi)
\eeqn
where
\beqn
P=\pmatrix{\offinterlineskip
 0 & 0&0\cr
 0 & 0& 0\cr
 1 & 0 & 0 \cr}, ~~
P'=\pmatrix{\offinterlineskip
 0 & 0&0\cr
 0 & 0& 0\cr
 0 & 1 & 0 \cr}
\eeqn 
and where $\alpha$ and $\beta$ are matrix elements of the three quark states between nucleon
and the vacuum state (see, e.g., Ref.~\cite{Aoki:1999tw})

\beqn
<0|\epsilon_{abc} \epsilon_{\alpha\beta}u^{\alpha}_{aR}d^{\beta}_{bR}u^{\gamma}_L|p>=\alpha  u^{\gamma}_L,\nonumber\\
<0|\epsilon_{abc} \epsilon_{\alpha\beta}u^{\alpha}_{aL}d^{\beta}_{bL}u^{\gamma}_L|p>=\beta u^{\gamma}_L
\label{matrixelements}
\eeqn 
$\alpha$ and $\beta$ are known to satisfy the constraint~\cite{Brodsky:1983st,Gavela:1988cp}
$|\alpha|=|\beta|$. 

Recent lattice QCD calculation of the proton decay matrix element by the CP-PACS and the
JLQCD Collaborations  gives~\cite{Tsutsui:2004qc}
\beqn
|\alpha|=0.0090(09)(^{+5}_{-19}) ~{\rm GeV}^3\nonumber\\
|\beta=0.0096(09)(^{+6}_{-20}) ~{\rm GeV}^3
\label{alphabeta}
\eeqn
where $\alpha$ and $\beta$ have a relatively opposite sign. In the above the first error  is statistical and the
second error systematic.   
The lattice analysis uses the quenched QCD calculation in the continuum limit  where the continuum operators
are defined in the naive dimensional regularization (NDR) with $\overline{MS}$ subtraction scheme.  
The evaluation of $\alpha$ and $\beta$ given above is at the scale $Q=2$ GeV.  
The result of Eq.(\ref{alphabeta}) is smaller the previous evaluation by the JLQCD Collaboration which 
gave~\cite{Aoki:1999tw} 
$|\alpha|=0.0151(1) ~{\rm GeV}^3$, 
$|\beta=0.014(1) ~{\rm GeV}^3$ 
where again the analysis is done using NDR and the evaluations are scale $Q=2.30(4)$ GeV. 
Further, one may compare the result of Eq.(\ref{alphabeta}) with the 
preliminary results of the RBC Collaboration at the scale $Q=1.23(5)$ GeV which gives
$|\alpha|=0.0061(1) ~{\rm GeV}^3$, 
$|\beta=0.007(1) ~{\rm GeV}^3$ and are about 30\% smaller than those of  Eq.(\ref{alphabeta}). 
The above difference cannot be accounted for by the renormalization group effects in going 
from the scale Q=1.23 GeV to the scale Q=2 GeV which gives  about 3.5\%  effect~\cite{Tsutsui:2004qc}.
It should be noted that the analysis of Eq.(\ref{alphabeta}) is about a factor of 3 larger than than
the early QCD calculations of these  matrix ~\cite{Donoghue:1982jm}.   Returning to 
the analysis of  Ref.~\cite{Tsutsui:2004qc} the relative sign 
between $\alpha$ and $\beta$ is important as it can affect very significantly 
the proton decay rates. Similarly we can write the $\tilde O$ operators as  follows 
\beqn
\tilde O_{RL1}^{\nu_i}=\alpha\overline{(\nu_{iL})^C} Tr( \tilde P'\xi B_L \xi)\nonumber\\
\tilde O_{LL1}^{\nu_i}=\beta\overline{(\nu_{iL})^C} Tr(\tilde P'\xi B_L \xi^{\dagger})\nonumber\\
\tilde O_{RL}^{e_i}=\alpha\overline{(e_{iL})^C} Tr(\tilde P\xi B_L \xi)\nonumber\\
\tilde O_{LR}^{e_i}=\alpha\overline{(e_{iR})^C} Tr( \tilde P\xi^{\dagger} B_R \xi^{\dagger})\nonumber\\
\tilde O_{LL}^{e_i}=\beta\overline{(e_{iL})^C} Tr(\tilde P\xi B_L \xi^{\dagger})\nonumber\\
\tilde O_{RR}^{e_i}=\beta\overline{(e_{iR})^C} Tr(\tilde P\xi^{\dagger} B_R \xi)\nonumber\\
\tilde O_{RL2}^{\nu_i}=\alpha\overline{(\nu_{iL})^C} Tr( \tilde P''\xi B_L \xi)\nonumber\\
\tilde O_{LL2}^{\nu_i}=\beta\overline{(\nu_{iL})^C} Tr(\tilde P''\xi B_L \xi^{\dagger})
\eeqn
where
\beqn
\tilde P=\pmatrix{\offinterlineskip
 0 & 0&0\cr
 -1 & 0& 0\cr
 0 & 0 & 0 \cr}, ~~
\tilde P'=\pmatrix{\offinterlineskip
 0 & 0&0\cr
 0 & -1& 0\cr
 0 & 0 & 0 \cr}, ~~
 \tilde P''=\pmatrix{\offinterlineskip
 0 & 0&0\cr
 0 & 0& 0\cr
 0 & 0 & 1 \cr}
\eeqn 
In extracting the \bl violating parts from Eq.(\ref{lagbl}) we must compute both the quadratic and
a cubic term. The quadratic part is easily extracted. It is  
 \begin{eqnarray}
 {\cal L_{BL}}^{(2)} &=& (\alpha C_{RL}^{\nu_i}+\beta C_{LL}^{\nu_i})\overline{(\nu_{iL})^C} n_L + 
 (\alpha C_{RL}^{e_i} + \beta C_{LL}^{e_i})\overline{(e_{iL})^C} p_L + 
\nonumber\\
&& (\alpha C_{LR}^{e_i}+\beta C_{RR}^{e_i})\overline{(e_{iR})^C} p_R 
+ (\alpha \tilde C_{RL1}^{\nu_i}+\beta \tilde C_{LL1}^{\nu_i})\overline{(\nu_{iL})^C} 
(\frac{\Sigma^0_L }{\sqrt 2} -\frac{\Lambda^0_L}{\sqrt 6})
\nonumber\\
 &-& (\alpha\tilde C_{RL}^{e_i}+\beta\tilde C_{LL}^{e_i})\overline{(e_{iL})^C}\Sigma_L^+ 
\nonumber\\
 &-& (\alpha\tilde C_{LR}^{e_i}+\beta\tilde C_{RR}^{e_i})\overline{(e_{iR})^C} \Sigma_R^+
-(\alpha\tilde C_{RL2}^{\nu_i}
+ \beta\tilde C_{LL2}^{\nu_i}) \sqrt {\frac{2}{3}} \overline{(\nu_{iL})^C}\Lambda_L^0 
\nonumber\\
\end{eqnarray}
while the \bl violating cubic interaction is
 \begin{eqnarray}
 {\cal L_{BL}}^{(3)} &=& \frac{i}{f}  \{
     \alpha C_{RL}^{\nu_i} ( \overline{(\nu_{iL})^C} p_L\pi^- 
 -  \overline{(\nu_{iL})^C} n_L( \frac{\pi^0}{\sqrt 2} + \frac{\eta}{\sqrt 6}) )  
\nonumber\\ 
&+&\beta C_{LL}^{\nu_i} 
 ( \overline{(\nu_{iL})^C} p_L\pi^- 
 +  \overline{(\nu_{iL})^C} n_L( -\frac{\pi^0}{\sqrt 2} + \frac{3}{\sqrt 6}\eta) )  
 \nonumber\\
 &+& \alpha  C_{RL}^{e_i} 
 ( \overline{(e_{iL})^C} n_L\pi^+ 
 +  \overline{(e_{iL})^C} p_L( \frac{\pi^0}{\sqrt 2} - \frac{1}{\sqrt 6}\eta) ) 
\nonumber\\ 
&-& \alpha C_{LR}^{e_i} 
 ( \overline{(e_{iR})^C} n_R\pi^+ 
 +  \overline{(e_{iR})^C} p_R( \frac{\pi^0}{\sqrt 2} - \frac{1}{\sqrt 6}\eta) ) 
 \nonumber\\
 &+& \beta C_{LL}^{e_i} 
 ( \overline{(e_{iL})^C} n_L\pi^+ 
 +  \overline{(e_{iL})^C} p_L( \frac{\pi^0}{\sqrt 2} + \frac{3}{\sqrt 6}\eta)  )
\nonumber\\ 
&-& \beta C_{RR}^{e_i} 
 ( \overline{(e_{iR})^C} n_R\pi^+ 
 +  \overline{(e_{iR})^C} p_R( \frac{\pi^0}{\sqrt 2} + \frac{3}{\sqrt 6}\eta)  )
\nonumber\\
 &+&  (-\alpha \tilde C_{RL1}^{\nu_i} +\beta \tilde C_{LL1}^{\nu_i})  \overline{(\nu_{iL})^C} n_L \bar K^0 
+ ( -\alpha \tilde C_{RL}^{e_i} 
\nonumber\\
&+& \beta \tilde C_{LL}^{e_i})  \overline{(e_{iL})^C} p_L \bar K^0
  + ( \alpha \tilde C_{LR}^{e_i} - \beta \tilde C_{RR}^{e_i})  \overline{(e_{iR})^C}p_R \bar K^0
 \nonumber\\
 &+& (\alpha\tilde C_{RL2}^{\nu_i} +\beta \tilde C_{LL2}^{\nu_i}) 
 ( \overline{(\nu_{iL})^C} n_L \bar K^0  + \overline{(\nu_{iL})^C} p_L  K^-) 
   \} + h.c. \nonumber\\
\end{eqnarray}

In addition there are baryon number conserving interactions. 
The relevant terms are~\cite{Chadha:1983sj}:
\begin{eqnarray}
 {\cal L_{BC}}&=& \frac{1}{2i} (D-F) Tr[ \bar B \gamma^{\mu} \gamma_5 B
 \{\partial_{\mu} \xi \xi^{\dagger} 
\nonumber\\
&-& \partial_{\mu}\xi^{\dagger} \xi\}]
- \frac{1}{2i} (D+F) Tr[ \bar B \gamma^{\mu} \gamma_5 
 \{\xi \partial_{\mu}\xi^{\dagger} - \xi^{\dagger} \partial_{\mu}\xi \}B]
\nonumber\\
&+& b_1 Tr[ \bar B \gamma_5(\xi^{\dagger} m\xi^{\dagger} -\xi  m\xi) B]
+b_2 Tr[ \bar B \gamma_5 B(\xi^{\dagger} m\xi^{\dagger} -\xi  m\xi) ]
\nonumber\\
\end{eqnarray}
where m is quark mass matrix  such that $ m=diag (m_u, m_d, m_s)$. 
In the above the terms with co-efficients ($D\pm F$) are invariant under $SU(3)_L\times SU(3)_R$
while the terms with co-efficients $b_1, b_2$ transform like $(3,3^*)+(3^*,3)$ and break 
$SU(3)_L\times SU(3)_R$ down to $SU(3)_V$. The matrix $\bar B$ is defined so that

\begin{equation}
\bar B=\pmatrix{\offinterlineskip
 \frac{\bar \Sigma^0}{\sqrt{2}}+\frac{\bar \Lambda}{\sqrt{6}}&\bar \Sigma^-&- \bar\Xi^-\cr
\bar\Sigma^+&     -\frac{\bar\Sigma^0}{\sqrt{2}}+\frac{\bar\Lambda}{\sqrt{6}}   & \bar \Xi^0\cr
\bar p & \bar n & -\sqrt{\frac{2}{3}} \bar\Lambda\cr}
\end{equation}
The relevant part of  $ {\cal L_{BC}} $ is 
\beqn
{\cal L_{BC}} = \left(  \frac{D-F}{\sqrt 2 f} \bar \Sigma^0 \gamma^{\mu} \gamma_5 p 
-\frac{D+3F}{\sqrt 6 f}  \bar \Lambda^0 \gamma^{\mu} \gamma_5 p
+\frac{D-F}{\sqrt 2 f} \bar \Sigma^- \gamma^{\mu} \gamma_5 n\right) \partial_{\mu}K^- 
\nonumber\\
+\left(\frac{D-F}{ f} \bar \Sigma^+ \gamma^{\mu} \gamma_5 p 
-\frac{D-F}{\sqrt 2 f}  \bar \Sigma^0 \gamma^{\mu} \gamma_5 n
-\frac{D+3F}{\sqrt 6 f} \bar \Lambda^0 \gamma^{\mu} \gamma_5 n\right) \partial_{\mu}\bar K^0 
\nonumber\\
+\frac{i}{f} (m_u+m_s) \left( \sqrt{\frac{2}{3}} (2b_1-b_2) \bar \Lambda^0\gamma_5p 
-\sqrt 2 b_2 \bar \Sigma^0\gamma_5 p +2b_2 \bar \Sigma^-\gamma_5 n \right)K^- 
\nonumber\\
+
\frac{i}{f} (m_d+m_s) \left(
 - 2b_2  \bar \Sigma^+\gamma_5p 
+\sqrt{\frac{2}{3}} (2b_1-b_2)  \bar \Lambda^0\gamma_5 n +
\sqrt 2 b_2 \bar \Sigma^0\gamma_5 n \right) \bar K^0  + h.c. \nonumber\\
\eeqn
The contribution of the $m_u, m_s$ terms is typically small and as is 
conventional we neglect them from here on. For simplicity we introduce the notation
\beqn
C_{RL}^{'\nu_i,e_i }=\alpha C_{RL}^{\nu_i,e_i}, ~C_{LL}^{'\nu_i,e_i}=\beta C_{LL}^{\nu_i,e_i},
~C_{LR}^{'e_i}=\alpha C_{LR}^{e_i}, ~C_{RR}^{'e_i}=\beta C_{RR}^{e_i},\nonumber\\
\tilde C_{RL1}^{'\nu_i}=\alpha C_{RL1}^{\nu_i}, 
~\tilde C_{LL1}^{'\nu_i}=\beta C_{LL1}^{\nu_i},
\tilde C_{RL}^{'e_i}=\alpha C_{R}^{e_i},
~\tilde C_{LR}^{'e_i}=\alpha \tilde C_{LR}^{e_i},
\nonumber\\
~\tilde C_{LL}^{'e_i}=\beta C_{LL}^{e_i},
~\tilde C_{RR}^{'e_i}=\beta \tilde C_{RR}^{e_i},
\tilde C_{RL2}^{'\nu_i}=\alpha C_{RL2}^{\nu_i}, 
~\tilde C_{LL2}^{'\nu_i} =\beta C_{LL2}^{\nu_i},
\label{cprime}
\eeqn

\noindent
We discuss now the decay widths for the various decay modes.

 \noindent
 (i) $\underline{p \to \bar\nu_i K^+}$  decay 

\begin{eqnarray}
\Gamma(p\to \bar\nu_i K^+) &= & (32\pi f^2 m_N^3)^{-1} (m_N^2-m_K^2)^2 
|(\tilde C_{LL2}^{'\nu_i}+\tilde C_{RL2}^{'\nu_i}) 
\nonumber\\
&+& \frac{m_N}{2m_{\Sigma^0}} ( \tilde C_{LL1}^{'\nu_i}+ 
\tilde C_{RL1}^{'\nu_i}) (D-F)
\nonumber\\
&+& \frac{m_N}{6m_{\Lambda}}  \{ \tilde C_{LL1}^{'\nu_i}+   \tilde C_{RL1}^{'\nu_i}+2 
(\tilde C_{LL2}^{'\nu_i}+\tilde C_{RL2}^{'\nu_i}) \} (D+3F)|^2 \nonumber\\
\end{eqnarray}
In the above and in the following the $C's$  
and  $\tilde C's$ are as defined in Eq.(\ref{cprime}).\\

\noindent
(ii) $\underline{n \to \bar\nu_i K^0}$ decay 
\begin{eqnarray}
\Gamma(n\to \bar\nu_i K^0) &=& (32\pi f^2 m_N^3)^{-1} (m_N^2-m_K^2)^2 
|( -\tilde C_{RL1}^{'\nu_i}+
\tilde C_{LL1}^{'\nu_i} +
\tilde C_{RL2}^{'\nu_i}+\tilde C_{LL2}^{'\nu_i})  
\nonumber\\
&-& \frac{1}{2} \frac{m_N}{m_{\Sigma^0}}  (\tilde C_{RL1}^{'\nu_i}+\tilde C_{LL1}^{'\nu_i})(D-F) 
+\frac{m_N}{6m_{\Lambda} }(\tilde C_{RL1}^{'\nu_i}+\tilde C_{LL1}^{'\nu_i}  
\nonumber\\
&+& 2\tilde C_{RL2}^{'\nu_i}+2\tilde C_{LL2}^{'\nu_i}) (D+3F) |^2
\end{eqnarray}
 
\noindent
 (iii) $\underline{p \to  l_i^+ K^0}$ decay
\begin{eqnarray}
\Gamma(p \to l_i^+ K^0) &=& (32\pi f^2 m_N^3)^{-1} (m_N^2-m_K^2)^2 
\{\frac{1}{2} [-\tilde  C_{RL}^{'e_i}+\tilde C_{LL}^{'e_i}+\tilde C_{LR}^{'e_i}
\nonumber\\
&-& \tilde C_{RR}^{'e_i} - \frac{m_N}{m_{\Sigma}} 
(\tilde C_{RL}^{'e_i} +\tilde C_{LL}^{'e_i} -\tilde C_{LR}^{'e_i} 
-\tilde C_{RR}^{'e_i})(D-F)]^2+
\nonumber\\
&+& \frac{1}{2} [-\tilde  C_{RL}^{'e_i}+\tilde C_{LL}^{'e_i}-\tilde C_{LR}^{'e_i}+\tilde C_{RR}^{'e_i} 
\nonumber\\
&-& \frac{m_N}{m_{\Sigma}} (\tilde C_{RL}^{'e_i} +\tilde C_{LL}^{'e_i} +\tilde C_{LR}^{'e_i} 
+\tilde C_{RR}^{'e_i})(D-F)]^2\} \nonumber\\
\end{eqnarray}

\noindent
(iv) $\underline{ p \to  \bar \nu_i \pi^+}$ decay
\beqn
\Gamma(p \to \bar \nu_i \pi^+) =(32\pi f^2 m_N^3)^{-1} (m_p^2-m_{\pi^+}^2)^2 
|C_{RL}^{'\nu_i} +C_{LL}^{'\nu_i}|^2(1+D+F)^2 \nonumber\\
\eeqn

\noindent
 (v) $\underline{ n \to  \bar\nu_i \pi^0}$  decay
\beqn
\Gamma(n\to \bar\nu_i \pi^0) =(32\pi f^2 m_N^3)^{-1} (m_n^2-m_{\pi^0}^2)^2 
 \frac{1}{2}  |C_{RL}^{'\nu_i} +C_{LL}^{'\nu_i}|^2
 (1+D+F)^2 \nonumber\\
\eeqn
Neglecting the  mass differences  of p and n and  of $\pi^+$ and $\pi^0$ we get
\beqn
\Gamma(n\to \bar \nu_i \pi^0)\simeq 0.5 \Gamma(p\to \bar \nu_i  \pi^+)
\eeqn


\noindent
(vi) $\underline{ n \to  \bar\nu_i \eta^0}$ decay
\beqn
\Gamma(n\to \bar\nu_i \eta^0) =(32\pi f^2 m_N^3)^{-1} (m_n^2-m_{\eta^0}^2)^2 \times
\nonumber\\
 \frac{3}{2}  | C_{RL}^{'\nu_i}(-\frac{1}{3} -\frac{D}{3}+F) +  
 C_{LL}^{'\nu_i} (1-\frac{D}{3} +F)|^2
\eeqn


\noindent
(vii) $\underline{p \to  e_i^+ \pi^0}$  decay
\beqn
\Gamma(p\to e_i^+ \pi^0) =(32\pi f^2 m_N^3)^{-1} (m_n^2-m_{\pi^0}^2)^2 \times
\nonumber\\
 \frac{1}{2}  \left(  | C_{RL}^{'e_i} +C_{LL}^{'e_i}|^2 +|C_{LR}^{'e_i}+C_{RR}^{'e_i}|^2  \right) 
(1+D+F)^2 \nonumber\\
\eeqn

\noindent
(viii)  $\underline{p \to  e_i^+ \eta^0}$   decay
\beqn
\Gamma(p\to e_i^+ \eta^0) =(32\pi f^2 m_N^3)^{-1} (m_n^2-m_{\eta^0}^2)^2 
\times
\nonumber\\
 \frac{3}{2}
 \{ [ C_{LL}^{'e_i}(1-\frac{D}{3} +F) +
 C_{RL}^{'e_i}(-\frac{1}{3}-\frac{D}{3} +F)]^2 
 \nonumber\\
  + [ C_{RR}^{'e_i}(1-\frac{D}{3} +F) +
 C_{LR}^{'e_i}(-\frac{1}{3}-\frac{D}{3} +F)]^2 \}
\eeqn

\noindent
 (ix) $\underline{n \to  e_i^+ \pi^-}$ decay   
\beqn
\Gamma(n\to e_i^+ \pi^-) =(32\pi f^2 m_N^3)^{-1} (m_n^2-m_{\pi^-}^2)^2 
 \times 
\nonumber\\
\frac{3}{2}
 \left( |C_{RL}^{'e_i}+C_{LL}^{'e_i}|^2+|C_{LR}^{'e_i}+C_{RR}^{'e_i}|^2 \right)  (1+D+F)^2 
 \eeqn
 Currently the effective lagrangian approach is the most reliable 
approach to the computation of proton decay amplitudes. 
Numerically $f=139$ MeV, while F and D can be gotten from a recent analysis  of  hyperon decays
which gives\cite{Cabibbo:2003cu} 
\beqn
F+D=1.2670\pm 0.0030, ~~F-D=-0.341\pm 0.016
\eeqn
As we already discussed, in order to compute the lifetime of the proton we have to take into account the renormalization effects from the GUT scale to 1 GeV. 
In the previous appendix we already discussed those effects for the $d=5$ and 
$d=6$ operators.


The chiral Lagrangian approach is currently the best available technique for the 
analysis of proton decay lifetime starting with the fundamental  Lagrangian  in terms of 
quark fields. The approach~\cite{effec_lag} had considerable success 
in the past but it has certain limitations. The technique works best in the so called 
soft pion approximation. In the present context,  the mesons  in  proton decay 
may have energies as large as 500 MeV so a certain extrapolation is 
necessary.  However, the technique  still remains the state of the art in the 
computation of proton decay life times.
