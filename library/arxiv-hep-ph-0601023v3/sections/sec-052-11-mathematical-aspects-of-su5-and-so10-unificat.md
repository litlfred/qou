---
doc_id: arxiv-hep-ph-0601023v3
doc_title: "Proton Stability in Grand Unified Theories, in Strings and in Branes"
section_id: sec-052-11-mathematical-aspects-of-su5-and-so10-unificat
section_title: "Mathematical aspects of $SU(5)$ and $SO(10)$ unification"
section_number: 11
pages: 147-162
source_pdf: 0601023v3.pdf
source_sha256: 875ab040b50487a1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.935
doc_brief: "Proton Stability in Grand Unified Theories, in Strings and in Branes — A broad overview of the current status of proton stability in uni- ﬁed models of particle interactions is given which includes"
---
In this appendix we will give some technical details of group theory 
that will facilitate reading the main body of the report. 
We begin by discussing $SU(5)$ where a single generation of 
quarks and  leptons is placed in the $\bar 5$ and the 
$10$ plet of $SU(5)$. The particle decomposition of $\bar 5$ is

\begin{eqnarray}
{\overline {5}}= \left(\begin{array}{c}d_{ L a}^c\\
e^-_L\\  -\nu_{eL}
  \end{array}\right)
\end{eqnarray}
where  sub a is the color  index. For the 10 plet of $SU(5)$ we have

\begin{eqnarray}
10 =\left(\begin{array}{ccccc}0 & u_3^c &-u_2^c  &-u^1 &-d^1\\ -u_3^c &0
&u_1^c  &-u^2 &-d^2\\ u_2^c &-u_1^c &0  &-u^3 &-d^3 \\
 u^1 &u^2 &u^3  &0 &e^+ \\ d^1 &d^2 &d^3 &-e^+
&0
  \end{array}
 \right)_L
\end{eqnarray}
To recover the interaction of the Standard Model particles from their $SU(5)$ invariant couplings  
one needs to carry out their $SU(3)_C\times SU(2)_L\times U(1)_Y$ invariant reduction. 
 Here we will illustrate the basic technique for  the reduction of $SU(5)$
 tensors  into tensors which are  irreducible under 
  $SU(3)_C\times SU(2)_L\times U(1)_Y$. First  it  is useful to record  the tensorial  representations  of  
    irreducible representations of $SU(5)$ which commonly surface in model building based  on the 
    group $SU(5)$. As we  have seen the matter falls in the $SU(5)$ representations $\bar 5_M +10_M$
    while, the Higgs could be  in any of the fields $5_H, \bar 5_H, 10_H, \overline{10}_H, 24_H$,
    $45_H$, $\overline{45}_H$, 
    $50_H, \overline{50}_H$, $75_H$ etc.  The tensors representing these are  
    \beqn
    5^i, \bar 5_i, 10^{ij}, \overline{10}_{ij}, 24^i_j, 45^{ij}_k,
    \overline{45}^i_{jk},
      50^{ijk}_{lm}, \overline{50}^{ij}_{klm}, 
    75^{ij}_{kl}
    \eeqn
    where one has  anti-symmetry in all the sub indices and  in all the super indices.
    Further, the  $24^i_j$ is traceless, while the 50-plet, $\overline{50}$ plet,
    and the 75-plet satisfy the following constraints 
    \beqn
    \sum_{n=1}^{5} 45^{in}_{n}=0 = \sum_{n=1}^{5} \overline{45}^{n}_{in};~~    
    \sum_{n=1}^{5} 50^{in}_{jkn}=0 = \sum_{n=1}^{5} \overline{50}^{ijn}_{kn};~~
    \sum_{n=1}^{5} 75^{in}_{jn} =0
    \eeqn 
      The following decomposition is useful in the reduction of the $SU(5)$ irreducible tensors
      into irreducible  components
      under  $SU(3)_C\times SU(2)_L\times U(1)_Y$          
   \beqn
   \delta^i_j= \sum_{a=1}^{3} \delta^i_a\delta^a_j + \sum_{\alpha=4}^{5} \delta^i_{\alpha}
   \delta^{\alpha}_j
   \eeqn
     where $a=1,2,3$ is the color index and $\alpha =4,5$ is the $SU(2)$ index.  Thus consider
     the 24-plet which has  the  following 
$SU(3)_C\times SU(2)_L\times U(1)_Y$ decomposition
    \beqn
    24=(1,1,0)+ (1,3,0) +(8,1,0) + (3,2,-5/3) + (\bar 3,2,5/3) 
   \label{24rep}
    \eeqn  
     Using the above  technique $(1,1,0)$ takes  the form
     \beqn
     24^i_j(1,1,0)= \sqrt{\frac{2}{15}}
      (\sum_{a=1}^{3}\delta^i_a\delta^a_j -\frac{3}{2} 
      \sum_{\alpha =4}^{5}\delta^i_{\alpha}\delta^{\alpha}_j) \sigma_{(110)}
     \eeqn 
 where $\sigma_{(110)}$ is the $SU(3)_C\times SU(2)_L\times U(1)$ singlet field 
   and the other components in Eq.(\ref{24rep}) can be similarly gotten.    
     \\ 
  
 We now give some mathematical background relevant for the group $SO(10)$.
 For reasons of computation of $SO(10)$ couplings it is found useful to 
 decompose them in the more familiar $SU(5)$ representations. We  begin
 by defining the 45 generators of $SO(10)$ in the spinor representation 
 so that 
  \begin{equation}
 \Sigma_{\mu\nu}=\frac{1}{2i}[\Gamma_\mu,\Gamma_\nu]
 \end{equation}
 where  elements  $\Gamma_{\mu}$  ($\mu=1,2,...,10$) which satisfy Clifford algebra 
\begin{equation}
\{\Gamma_{\mu},\Gamma_{\nu}\}=2\delta_{\mu\nu}.
\end{equation}
It is convenient to define $\Gamma_{\mu}$ in terms of creation and destruction operators,
$b_i$ and $b_i^{\dagger}$ ($i=1,2,...,5$)~\cite{Mohapatra:1979nn,Wilczek:1981iz} so that 
\begin{equation}
\Gamma_{2i}= (b_i+ b_i^{\dagger});~~~ \Gamma_{2i-1}= -i(b_i-
b_i^{\dagger})
\end{equation}
where
\begin{equation}
\{b_i,b_j\}=0;~~~\{b_i,b_j^{\dagger}\}=\delta_{i}^j; ~~~\{b_i^{\dagger},b_j^{\dagger}\}=0
\end{equation}
and where the $SU(5)$ singlet state  $|0>$  satisfies $b_i|0>=0$.
One can define an $SO(10)$ chirality operator  $(1\pm \Gamma_0)/2$ where 
$\Gamma_0=i^5 \Gamma_1\Gamma_2...\Gamma_{10}$  so that the 
 32 plet spinor of $SO(10)$ can be split into semi-spinors 
 $\Psi_{(\pm)\acute{a}}$ ($\acute{a}=1,2,3$ is  the generation index) which are eigen -states of
 of $SO(10)$ chirality. 
 \beqn
 \Psi_{(\pm)\acute{a}}=  \frac{1}{2}[1\pm \Gamma_0] \Psi_{\acute{a}}
 \eeqn 
 Now $\Psi_{(\pm)\acute{a}}$
transforms as a 16($\overline{16}$)-dimensional irreducible
representation of $SO(10)$. They can be expanded in $SU(5)$ decomposition 
so that  $16=1+\overline{5}+10$($\overline{16}=1+5+\overline{10}$) and are given by
\begin{equation}
|16_{\acute{a}} >=|0>{1}_{\acute{a}}+\frac{1}{2}b_i^{\dagger}b_j^{\dagger}|0>{
10}_{\acute{a}}^{ij} +\frac{1}{24}\epsilon^{ijklm}b_j^{\dagger}
b_k^{\dagger}b_l^{\dagger}b_m^{\dagger}|0>{\bar 5}_{\acute{a}i}
\end{equation}

\begin{equation}
|\overline{16}_{\acute{a}}>=b_1^{\dagger}b_2^{\dagger}b_3^{\dagger}b_4^{\dagger}b_5^{\dagger}|0>{
1'}_{\acute{a}}+\frac{1}{12}\epsilon^{ijklm}b_k^{\dagger}b_l^{\dagger}b_m^{\dagger}|0>{
10'}_{\acute{a}ij}+b_i^{\dagger}|0>{5'}_{\acute{a}}^i
\end{equation}
One generation of quarks and leptons can be identified as residing in a single $16$ plet 
representation of $SO(10)$, i.e., in the $\bar 5$ and $10$ SU(5) multiplets, while
the $SU(5)$ singlet field is a right handed neutrino which is needed in generation of
neutrino masses in a See-Saw mechanism. 
One may also define   a charge conjugation operator in $SO(10)$ by 

\begin{equation}
B=\prod_{\mu =odd}\Gamma_{\mu}= -i\prod_{k=1}^5
(b_k-b_k^{\dagger})
\end{equation}
This operator is needed in forming the $SO(10)$ invariant interactions.\\


In building models using  $SO(10)$  grand unification, one needs
the explicit decomposition of the $SO(10)$ invariant couplings in terms of
the Standard  Model fields. This task in facilitated  by decomposition of the
$SO(10)$ invariant couplings in terms of the $SU(5)$ invariant couplings, since
$SU(5)$  invariant couplings can be  easily decomposed in terms of the Standard 
Model states. The decomposition of the $SO(10)$ invariant couplings in terms of
$SU(5)$ invariant couplings can be  easily achieved  by use of the so called
Basic Theorem~\cite{Nath:2001uw,Nath:2001yj,Syed:2005gd,Syed:2004if,Nath:2005bx} which we  explain  briefly 
below.
We note that an $SO(10)$ invariant vertex can be expanded in a specific set of $SU(5)$
reducible tensors ${\Phi}_{c_k}$ and ${\Phi}_{\overline c_k}$ defined as  follows:
${\Phi}_{c_k}\equiv{\Phi}_{2k}+i{\Phi}_{2k-1},~
{\Phi}_{\overline c_k}\equiv{\Phi}_{2k}-i{\Phi}_{2k-1}$.
We can extend the above easily to define the quantity $\Phi_{c_ic_j\bar c_k..}$
which has an arbitrary number of barred and unbarred indices where each
 $c$ index is defined  so that
${\Phi}_{c_ic_j\overline
c_k...}={\Phi}_{2ic_j\overline c_k...}+i{\Phi}_{2i-1c_j\overline
 c_k...}~$etc.
 The above implies  that  the quantity  $\Phi_{c_ic_j\overline
c_k...c_N}$ is a sum of
 $2^N$ terms gotten by expanding all the c indices.
$\Phi_{c_ic_j\overline c_k...c_n}$ is completely anti-symmetric in
the interchange of its c indices whether unbarred or barred:
 ${\Phi}_{c_i\overline c_jc_k...\overline c_n}=-{\Phi}_{c_k\overline c_jc_i...\overline c_n}$.
Further, $ {\Phi}^*_{c_i\overline c_jc_k...\overline
c_n}={\Phi}_{\overline c_ic_j\overline
  c_k...c_n}$ etc.
    It is now clear  that the quantity
$\Phi_{c_ic_j\overline c_k...c_n}$ transforms like a reducible
representation of $SU(5)$.  This reducible representation can be further
decomposed into a sum of irreducible tensors. Thus the procedure is that
one first computes the $SO(10)$ invariant couplings in terms of the $SU(5)$
reducible tensors  and then decomposes them further in terms of the
the irreducible tensors. The above procedure can be summarized in terms of 
the following result in a compact form: The $SO(10)$ invariant vertex 
$\Gamma_{\mu}\Gamma_{\nu}\Gamma_
{\lambda}..\Gamma_{\sigma}$ $\Phi_{\mu\nu\lambda ..\sigma}$, where
$\Phi_{\mu\nu\lambda ..\sigma}$ is a tensor field, 
can  be expanded as follows~\cite{Nath:2001uw} 
 
\begin{eqnarray}
\Gamma_{\mu}\Gamma_{\nu}\Gamma_{\lambda}..\Gamma_{\sigma}
\Phi_{\mu\nu\lambda ...\sigma}&=& b_i^{\dagger}
b_j^{\dagger}b_k^{\dagger}...b_n^{\dagger} \Phi_{c_ic_jc_k...c_n}
+ ( b_i b_j^{\dagger}b_k^{\dagger}...b_n^{\dagger}
\Phi_{\overline c_ic_jc_k...c_n} \nonumber\\  &+& ~perms )
+\left(b_i b_jb_k^{\dagger}...b_n^{\dagger} \Phi_{\overline
c_i\overline c_jc_{k}...c_n}+~perms\right)+ ...
+  \nonumber\\ & & \left(b_ib_jb_k...b_{n-1}b_n^{\dagger}\Phi_{\overline
c_i\overline c_j
\overline c_k...\overline c_{n-1}c_n}+~perms\right)\nonumber\\
&+& b_ib_jb_k...b_n \Phi_{\overline c_i\overline c_j\overline
c_k...\overline c_n}
\end{eqnarray}
The quantity $\Phi_{c_ic_j\overline c_k...c_n}$ transforms like a
reducible representation of $SU(5)$ and can  be further decomposed
into  irreducible $SU(5)$ parts. The above technique is easily extended
to the expansion of an $SO(2N)$ vertex in terms of $SU(N)$ vertices.

With the above technique the cubic couplings in the 
superpotential involving 16-plet of 
matter and the $10$, $120$ and $\overline{126}$ of Higgs fields, 
and cubic couplings in the Lagrangian involving the 16-plet of matter fields  and the
$45$ plet of gauge fields can be computed.  We give now the explicit computations.
 For the $16-16-10$ couplings one finds the following expansion in their $SU(5)$  decomposed
 form
 \begin{eqnarray}
  W^{(10)}=(2\sqrt 2 i)f^{(+)}_{ab}(10^{ij}_a\bar 5_{ib}\bar 5_{Hj}
  -1_{a}\bar 5_{ib}5_H^i + \frac{1}{8}\epsilon_{ijklm}10^{ij}_a10^{kl}_b 5_H^m)
\label{161610}
\end{eqnarray} 
where the 10-plet of $SO(10)$  Higgs fields is decomposed in $SU(5)$ representations so that
$10_H=5_H+\bar 5_H$. In Eq.(\ref{161610}) the Higgs fields are identified  with
the subscript H while the remaining fields are the matter fields. 
 In analyzing the 16-16-120 coupling in the superpotential in terms of 
 $SU(5)$ representations we note that the 120-plet representation can be  decomposed
 in $SU(5)$ representations as follows: $120=5+\bar 5$ + $10+\overline{10}$+$45 +\overline{45}$.
 Thus  one has 
 
 \begin{eqnarray}
W^{(120)}=i\frac{2}{\sqrt 3}f_{\acute{a}\acute{b}}^{(-)} [
2 (1_{\acute{a}} 5_{i\acute{b}}5_H^i) +
10^{ij}_{\acute {a}}1_{\acute{b}}10_{Hij}
+5_{i\acute a}5_{j\acute b}10_H^{ij}\nonumber\\
-10^{ij}_{\acute a}\bar 5_{i\acute b}\bar 5_{Hj}+  \bar 5_{i\acute a}10_{\acute b}^{jk}\bar 45^i_{Hjk}
-\frac{1}{4}\epsilon_{ijklm}10_{\acute a}^{ij}10_{\acute b}^{mn}45^{kl}_{Hn} ]  
\end{eqnarray}
 where the fields with subscripts H are the Higgs fields in $SU(5)$ representations. 
 In decomposing the vertex involving the $\overline{126}$ coupling  we  note that 
 the $\overline{126}$ and ${126}$ have the    $SU(5)$   decompositions: 
 $\overline{126}= 1+5  +\overline{10} + 15 +\overline{45} + 50$  while 
${126}= 1+\bar 5 +{10} +\overline{15} + {45} + \overline{50}$. 
 The $16-16-\overline{126}$ vertex can be expanded as follows
 \begin{eqnarray}
W^{(\bar{126})}&=& if_{\acute{a}\acute{b}}^{(+)} {\frac{\sqrt 2}{\sqrt {15}}[-\sqrt 2}
(1_{\acute a} 1_{\acute b}1_H) -\sqrt 3  (1_{\acute a} \bar 5_{i\acute b}5^i_H) 
+1_{\acute a}10^{ij}_{\acute b}10_{Hij}\nonumber\\
&-& \frac{1}{8\sqrt 3}10_{\acute a}^{ij}10_{\acute b}^{kl}5^m_H\epsilon_{ijklm} 
-\bar 5_{i\acute a}\bar 5_{j\acute b} 15^{ij}_{HS} 
+10^{ij}_{\acute a}\bar 5_{\acute{b}k}\overline{45}^k_{Hij} \nonumber\\
&-& \frac{1}{12\sqrt 2}\epsilon_{ijklm}10_{\acute a}^{lm}10_{\acute b}^{rs}  50^{ijk}_{Hrs}]
\end{eqnarray}
where again the Higgs fields have been displayed with a subscript H while the other fields 
 are matter fields. 
 
The SO(10) gauge invariant couplings involve  the couplings of the 45 plet of gauge  vector
 bosons with 16-plet of matter. The supersymmetric Yang-Mills part of the Lagrangian 
 in superfield notation is 
\begin{equation}
 \int d^2\theta~tr(W^{\alpha}W_{\alpha}))
+ \int d^2\bar{\theta}~
tr(\overline{W}_{\dot{\alpha}}\overline{W}^{\dot{\alpha}})  
\end{equation}
 where  $W_{\alpha}$ is the field strength
 chiral spinor superfield. Since we are interested in dimension six fermion operators
 arising from these interactions, such interactions  arise only from the elimination
 of gauge vector bosons. Thus we exhibit only the gauge vector boson interactions 
 of the 45 gauge vectors  $V_{A\mu\nu}$  where A is a Lorentz index (A=0,1-3)
\begin{equation}
{\mathsf L}^{(45)}=\frac{1}{i}\frac{1}{2!}g^{^{(45)}}_{\acute{a}\acute{b}}
<\Psi_{(+)\acute a}|\gamma^0\gamma^A
\Sigma_{\mu\nu}|\Psi_{(+)\acute b}>V_{A\mu\nu}
\end{equation}
Here $\gamma^A $ spans the Clifford algebra
associated with the Lorentz group,  and $g$ is the gauge coupling constant.
Now in $SU(5)$ decomposition the 45 plet of SO(10) can be decomposed as follows
\begin{equation}
45= 1+ 10 + \overline{10} + 24
\end{equation}
We exhibit the $16-\overline{16}-45$ couplings in the decomposed  form 

\begin{eqnarray}
{\mathsf L}^{(45)}&=&g^{^{(45)}}_{\acute{a}\acute{b}}[\sqrt 5\left(-\frac{3}{5}
\overline{\bar 5_{\acute a}}^i\gamma^A \bar 5_{\acute{b}i}+
\frac{1}{10}\overline{10}_{\acute{a}ij}
\gamma^A 10_{\acute b}^{ij}+
\overline{1_{\acute a}}\gamma^A 1_{\acute b}\right){\mathsf V}_{A} \nonumber\\
&+&{\frac{1} {\sqrt 2}}\left(\overline {1}_{\acute a} \gamma^{A} {10}_{\acute b}^{lm}
+{\frac{1}{2}}\epsilon^{ijklm}\overline {10}_{\acute{a}ij}\gamma^A{\bar 5}_{\acute{b}k}\right) 
{\mathsf V}_{Alm}\nonumber\\
&-&\frac{1}{\sqrt 2}\left(
{\overline{10}}_{\acute{a}lm}\gamma^A{1}_{\acute b} 
+ \frac{1}{2}\epsilon_{ijklm}
 {\overline{\bar 5}}_{\acute a}^i\gamma^A{10}_{\acute b}^{jk}\right){\mathsf
V}_A^{lm} \nonumber\\
&+&\sqrt{2}\left(\overline {10}_{\acute{a}ik}\gamma^A {10}_{\acute b}^{kj}+
{\overline{\bar 5}}_{\acute a}^j\gamma^A{\bar 5}_{\acute{b}i}\right){\mathsf V}_{Aj}^i]. 
\end{eqnarray}
where $V_A$, $V_A^{ij}$, $V_{Aij}$, $V^i_{Aj}$ are the 1, 10, 
$\overline{10}$, and 24 plets of SU(5). The same technique can be used to compute
the interactions involving Higgs fields lying in  representations  $10$, $45$, $54$, $120$, 
$\overline{126}$,  $210$ (For later works using different techniques, 
see~\cite{Aulakh:2002zr,Fukuyama:2004ps,Aulakh:2004hm,Bajc:2004xe}).

We discuss now briefly the vector-spinor $\overline{144} (144)$ which requires  special
care~\cite{Nath:2005bx}. The reason for this is that the $\overline{144} (144)$ arise  via a constraint
on the reducible vector spinor $\overline{160} (160)$. Thus the 
 ${\overline {160}}$ vector-spinors has an  expansion  in $SU(5)$ oscillator modes so that:
\begin{equation}\label{bar160spinor}
|\Psi_{(+)\acute{a}\mu}>=|0>{\bf
P}_{\acute{a}\mu}+\frac{1}{2}b_i^{\dagger}b_j^{\dagger}|0>{\bf
P}_{\acute{a}\mu}^{ij} +\frac{1}{24}\epsilon^{ijklm}b_j^{\dagger}
b_k^{\dagger}b_l^{\dagger}b_m^{\dagger}|0>{\bf P}_{\acute{a}i\mu}
\end{equation}
while the 
${\overline {160}}$ vector-spinor has an expansion in $SU(5)$ oscillator modes so that:

\begin{equation}\label{160spinor}
|\Psi_{(-)\acute{b}\mu}>=b_1^{\dagger}b_2^{\dagger}
b_3^{\dagger}b_4^{\dagger}b_5^{\dagger}|0>{\bf Q}_{\acute{b}\mu}
+\frac{1}{12}\epsilon^{ijklm}b_k^{\dagger}b_l^{\dagger}
b_m^{\dagger}|0>{\bf Q}_{\acute{b}ij\mu}+b_i^{\dagger}|0>{\bf
Q}_{\acute{b}\mu}^i
\end{equation}
where  $i,j,k,l,m,...=1,2,...,5$ are
$SU(5)$ indices, 
$\mu,\nu,\rho,...=1,2,...,10$ are $SO(10)$ indices, while $\acute{a}, \acute{b},
\acute{c}, \acute{d}=1,2,3$ are generation indices. 
The $SU(5)$
field content of $\overline{160}$ multiplet is
\begin{eqnarray}
\label{su5decompositionofbar160,160}
\overline{160} (\Psi_{(+)\mu})&=& 1({\bf {\widehat P}})+\bar 5({\bf
P}_{i})+5 ({\bf P}^i)+5({\bf {\widehat P}}^i)+{\overline
{10}}({\bf P}_{ij}) +{\overline {10}}({\bf {\widehat
P}}_{ij}) \nonumber\\
&+& {\overline {15}}({\bf P}_{ij}^{(S)})
+24 ({\bf P}^i_j)+{\overline {40}}({\bf { P}}_{jkl}^i)+45 ({\bf
P}^{ij}_k)
\end{eqnarray}
while the $SU(5)$
field content of $\overline{160}$ multiplet is

\begin{eqnarray}
160 (\Psi_{(-)\mu})&=& 1({\bf {\widehat Q}})+5({\bf Q}^{i})+\bar 5
({\bf Q}_i)+\bar 5({\bf {\widehat Q}}_i)+10({\bf Q}^{ij}) +10({\bf
{\widehat
Q}}^{ij}) \nonumber\\
&+& 15({\bf Q}^{ij}_{(S)})
+24 ({\bf Q}^i_j)+40({\bf { Q}}^{ijk}_l)+{\overline {45}} ({\bf
Q}_{jk}^i)
\end{eqnarray}
To get the $\overline{144}144$ multiplets these must be  subject to the
constraint
 \beqn \Gamma_{\mu} |{\Upsilon}_{(\pm)\mu}>=0
\label{144constraint} \eeqn
Imposing these  constraints on the $\overline {160}$ multiplet gives

\begin{eqnarray}
\Gamma_{\mu}|\Psi_{(+)\mu}>&=& b_1^{\dagger}b_2^{\dagger}
b_3^{\dagger}b_4^{\dagger}b_5^{\dagger}|0>{\widehat {\bf P}}
+\frac{1}{12}\epsilon^{ijklm}b_k^{\dagger}b_l^{\dagger}
b_m^{\dagger}|0>\left({\bf P}_{ij}+6{\widehat {\bf
P}}_{ij}\right) \nonumber\\
&+& b_i^{\dagger}|0>\left({\bf P}^{i}+{\widehat {\bf P}}^{i}\right)
\end{eqnarray}
Thus to get the $\overline {144}$ spinor,
$|\Upsilon_{(+)\mu}>$ the following constraints  must  be imposed
on the components  in $|\Psi_{(+)\mu}>$
\begin{eqnarray}\label{constraints}
{\widehat {\bf P}}=0,~~~{\widehat {\bf P}}^i=-{\bf
P}^i,~~~{\widehat
{\bf P}}_{ij}=-\frac{1}{6}{\bf P}_{ij}
\end{eqnarray}
Similarly to reduce the 160-plet $|\Upsilon_{(-)\mu}>$
to $144$-plet we need to impose the constraints  

\begin{eqnarray}
{\widehat {\bf Q}}=0,~~~{\widehat {\bf Q}}_i=-{\bf
Q}_i,~~~{\widehat {\bf Q}}^{ij}=-\frac{1}{6}{\bf Q}^{ij}
\end{eqnarray}

The $SO(10)$ invariant cubic couplings in the superpotential
 involving two  vector-spinors
and  the tensors 1, 10, 45, 120, 210, and ${\overline
{126}}$ plet of Higgs etc can be written analogous to the 
couplings of the 16-plet spinor. We display the couplings for the
1,45, 10 tensors. The couplings for these are

\begin{eqnarray}
{\mathsf
W}^{(1)}=h^{^{(1)}}_{\acute{a}\acute{b}}<\Upsilon^{*}_{(-)\acute{a}\mu}|B|\Upsilon_{(+)\acute{b}\mu}>\Phi,
\nonumber\\
{\mathsf
W}^{(10)}=h^{^{(10)}}_{\acute{a}\acute{b}}<\Upsilon^{*}_{(+)\acute{a}\mu}|B\Gamma_{\nu}|\Upsilon_{(+)\acute{b}\mu}>
\Phi_{\nu},
\nonumber\\
{\mathsf
W}^{(45)}=\frac{1}{2!}h^{^{(45)}}_{\acute{a}\acute{b}}<\Upsilon^{*}_{(-)\acute{a}\mu}|B\Sigma_{\rho\sigma}|\Upsilon_{(+)\acute{b}
\mu}>\Phi_{\rho\sigma}.
\end{eqnarray}
Here $\Phi$ is the 1-plet,  $\Phi_{\nu}$  is the 10 plet, and $\Phi_{\rho\sigma}$ is the 45-plet
Higgs field. A detailed computation of these
and other couplings is  given in Ref.~\cite{Nath:2005bx}.




\section{$d=5$ contributions to the decay of the proton}

In this Appendix we present the complete set of diagrams
responsible for $d=5$ nucleon decay in supersymmetric scenarios. 
In this case proton decay is mediated by scalar leptoquarks 
and their superpartners. The relevant interactions for proton 
decay are the following:

\begin{eqnarray}
W &=& \hat{Q} \ \underline{A} \ \hat{Q} \ \hat{T} \ + 
\ \hat{U}^C \ \underline{B} \ \hat{E}^C \ \hat{T} \ \\
& + & \ \hat{Q} \ \underline{C} \ L \ \hat{\overline{T}} \ + \ 
\hat{U}^C \ \underline{D} \ \hat{D}^C \  \hat{\overline{T}} \ + \ M_T \hat{T} \hat{\overline{T}}
\end{eqnarray}

where we use the conventional notation for all MSSM superfields. 
The superfields $\hat{T}$, and $\hat{\overline{T}}$ transform 
as $(\bf{3},1,-2/3)$, and $(\overline{\bf{3}},1,2/3)$, 
respectively~\cite{Bajc:2002bv}.

\vskip 0.5cm
\noindent
\begin{center}
{\bf \underline{ Decay Channels:}}
\end{center}
\vspace{0.2cm}
\begin{center}
$p \ \to \ (K^+,\pi^+,\rho^+) \ \bar\nu_i$, and 
$n \ \to \ (\pi^0,\rho^0,\eta,\omega,K^0) \ \bar\nu_i$, 
with $i=1,2,3$. 
\end{center}


\begin{equation}
\label{nw1}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde\tau$}
\def\spgor{$\tilde w^+$}
\def\spdol{$\tilde w^-$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{$\nu_i$}
\def\isti{$d_{2,1}$}

\propto\;\;\;\;\;
(D^T\underline A^S\tilde U)_{13,23}(\tilde U^\dagger D)_{32,31}
(N^T\tilde E^*)_{i3}(\tilde E^T\underline C^TU)_{31}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde\tau$}
\def\spgor{$\tilde w^+$}
\def\spdol{$\tilde w^-$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{$\nu_i$}
\def\isti{$d_{2,1}$}

\propto\;\;\;\;\;
(D^T\underline A^S U)_{11,21}(N^T\tilde E^*)_{i3}
(\tilde E^T\underline C^T\tilde U)_{33}(\tilde U^\dagger D)_{32,31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde w^+$}
\def\spdol{$\tilde w^-$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{$u$}
\def\isti{$d_{2,1}$}

\propto\;\;\;\;\;
(D^T\underline A^S \tilde U)_{13,23}(\tilde U^\dagger D)_{32,31}
(U^T\tilde D^*)_{13}(\tilde D^T\underline CN)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde w^+$}
\def\spdol{$\tilde w^-$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{$u$}
\def\isti{$d_{2,1}$}

\propto\;\;\;\;\;
(D^T\underline CN)_{1i,2i}(U^T\tilde D^*)_{13}
(\tilde D^T\underline A^S \tilde U)_{33}(\tilde U^\dagger D)_{32,31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde{\bar h}_-^\dagger$}
\def\spdol{$\tilde h_+^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar d}_{2,1}^c$}

\propto\;\;\;\;\;
(D^T\underline A^S \tilde U)_{13,23}(\tilde U^\dagger Y_D^*D_c^*)_{32,31}
(U_c^\dagger Y_U^\dagger\tilde D^*)_{13}(\tilde D^T\underline CN)_{3i}
\end{equation}

\begin{equation}
\label{nh2}
\def\tr{$\bar T$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde{\bar h}_-^\dagger$}
\def\spdol{$\tilde h_+^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar d}_{2,1}^c$}

\propto\;\;\;\;\;
(D^T\underline CN)_{1i,2i}(U_c^\dagger Y_U^\dagger\tilde D^*)_{13}
(\tilde D^T\underline A^S \tilde U)_{33}(\tilde U^\dagger Y_D^*D_c^*)_{32,31}
\end{equation}

\begin{equation}
\label{nh3}
\def\trgor{$\tilde T^\dagger$}
\def\trdol{$\tilde{\bar T}^\dagger$}
\def\sfgor{$\tilde\tau^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde{\bar h}_-$}
\def\spdol{$\tilde h_+$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar d}_{2,1}^c$}
\def\itri{$d_{1,2}$}
\def\isti{$\nu_i$}

\propto\;\;\;\;\;
(U_c^\dagger\underline B^*\tilde E_c^*)_{13}(\tilde E_c^TY_EN)_{3i}
(D^TY_U\tilde U_c)_{13,23}(\tilde U_c^\dagger\underline D^*D_c^*)_{32,31}
\end{equation}

\begin{equation}
\label{nh4}
\def\tr{$\bar T$}
\def\sfgor{$\tilde\tau^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde{\bar h}_-$}
\def\spdol{$\tilde h_+$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar d}_{1,2}^c$}
\def\itri{$d_{2,1}$}
\def\isti{$\nu_i$}

\propto\;\;\;\;\;
(U_c^\dagger\underline D^* D_c^*)_{11,12}(D^TY_U\tilde U_c)_{23,13}
(\tilde U_c^\dagger\underline B^*\tilde E_c^*)_{33}(\tilde E_c^TY_EN)_{3i}
\end{equation}

\begin{equation}
\label{nh01}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde h_0^\dagger$}
\def\spdol{$\tilde{\bar h}_0^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{${\bar d}_{2,1}^c$}
\def\isti{${\bar u}^c$}

\propto\;\;\;\;\;
(D^T\underline A^S \tilde U)_{13,23}(\tilde U^\dagger Y_U^*U_c^*)_{31}
(D_c^\dagger Y_D^\dagger\tilde D^*)_{23,13}(\tilde D^T\underline CN)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde{\bar h}_0^\dagger$}
\def\spdol{$\tilde h_0^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar d}_{2,1}^c$}

\propto\;\;\;\;\;
(D^T\underline CN)_{1i,2i}(U_c^\dagger Y_U^\dagger\tilde U^*)_{13}
(\tilde U^T\underline A^S \tilde D)_{33}(\tilde D^\dagger Y_D^*D_c^*)_{32,31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{$d_{2,1}$}
\def\isti{$u$}

\propto\;\;\;\;\;
(D^T\underline A^S \tilde U)_{13,23}(\tilde U^\dagger U)_{31}
(D^T\tilde D^*)_{23,13}(\tilde D^T\underline CN)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$d_{1,2}$}
\def\idva{$\nu_i$}
\def\itri{$d_{2,1}$}
\def\isti{$u$}

\propto\;\;\;\;\;
(D^T\underline CN)_{1i,2i}(D^T\tilde D^*)_{23,13}
(\tilde D^T\underline A^S \tilde U)_{33}(\tilde U^\dagger U)_{31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{$d_{2,1}$}
\def\isti{$\nu_i$}

\propto\;\;\;\;\;
(D^T\underline C\tilde N)_{13,23}(\tilde N^\dagger N)_{3i}
(D^T\tilde D^*)_{23,13}(\tilde D^T\underline A^S U)_{31}
\end{equation}

\begin{equation}
\label{nv4}
\def\tr{$T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$u$}
\def\idva{$d_{1,2}$}
\def\itri{$d_{2,1}$}
\def\isti{$\nu_i$}

\propto\;\;\;\;\;
(U^T\underline A^S D)_{11,12}(D^T\tilde D^*)_{23,13}
(\tilde D^T\underline C\tilde N)_{33}(\tilde N^\dagger N)_{3i}
\end{equation}

\begin{equation}
\label{nv5}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$d_{1,2}$}
\def\idva{$d_{2,1}$}
\def\itri{$u$}
\def\isti{$\nu_i$}

\propto\;\;\;\;\;
(D^T\underline C\tilde N)_{13,23}(\tilde N^\dagger N)_{3i}
(U^T\tilde U^*)_{13}(\tilde U^T\underline A^S D)_{32,31}
\end{equation}

\vskip 1cm

\noindent

\begin{center}
{\bf \underline{Decay Channels:}}
\end{center}

\vspace{0.5cm}

\begin{center}
$p \ \to \ (K^0,\pi^0,\eta,\rho^0,\omega) \ e_i^+$, and 
$n \ \to \ (K^-,\pi^-,\rho^-) \ e_i^+$ 
with $i=1,2$.
\end{center}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde w^+$}
\def\spdol{$\tilde w^-$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{$u$}
\def\isti{$e_i$}

\propto\;\;\;\;\;
(D^T\underline C\tilde N)_{13,23}(\tilde N^\dagger E)_{3i}
(U^T\tilde D^*)_{13}(\tilde D^T\underline A^S U)_{31}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde w^+$}
\def\spdol{$\tilde w^-$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{$u$}
\def\isti{$e_i$}

\propto\;\;\;\;\;
(D^T\underline A^S U)_{11,21}(U^T\tilde D^*)_{13}
(\tilde D^T\underline C\tilde N)_{33}(\tilde N^\dagger E)_{3i}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde w^-$}
\def\spdol{$\tilde w^+$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{$d_{1,2}$}
\def\isti{$u$}

\propto\;\;\;\;\;
(U^T\underline A^S \tilde D)_{13}(\tilde D^\dagger U)_{31}
(D^T\tilde U^*)_{13,23}(\tilde U^T\underline CE)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde w^-$}
\def\spdol{$\tilde w^+$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{$d_{1,2}$}
\def\isti{$u$}

\propto\;\;\;\;\;
(U^T\underline CE)_{1i}(D^T\tilde U^*)_{13,23}
(\tilde U^T\underline A^S \tilde D)_{33}(\tilde D^\dagger U)_{31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}^\dagger$}
\def\trdol{$\tilde T^\dagger$}
\def\sfgor{$\tilde t^c$}
\def\sfdol{$\tilde b^c$}
\def\spgor{$\tilde h_+$}
\def\spdol{$\tilde{\bar h}_-$}
\def\iena{${\bar e}_i^c$}
\def\idva{${\bar u}^c$}
\def\itri{$u$}
\def\isti{$d_{1,2}$}

\propto\;\;\;\;\;
(E_c^\dagger\underline B^\dagger\tilde U_c^*)_{i3}
(\tilde U_c^TY_U^TD)_{31,32}(U^TY_D\tilde D_c)_{13}
(\tilde D_c^\dagger\underline D^\dagger U_c^*)_{31}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde t^c$}
\def\sfdol{$\tilde b^c$}
\def\spgor{$\tilde h_+$}
\def\spdol{$\tilde{\bar h}_-$}
\def\iena{${\bar e}_i^c$}
\def\idva{${\bar u}^c$}
\def\itri{$u$}
\def\isti{$d_{1,2}$}

\propto\;\;\;\;\;
(E_c^\dagger\underline B^\dagger U_c^*)_{i1}(U^TY_D\tilde D_c)_{13}
(\tilde D_c^\dagger\underline D^\dagger\tilde U_c^*)_{33}
(\tilde U_c^TY_U^TD)_{31,32}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde h_+^\dagger$}
\def\spdol{$\tilde{\bar h}_-^\dagger$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{${\bar d}_{1,2}^c$}
\def\isti{${\bar u}^c$}

\propto\;\;\;\;\;
(U^T\underline A^S \tilde D)_{13}(\tilde D^\dagger Y_U^*U_c^*)_{31}
(D_c^\dagger Y_D^\dagger\tilde U^*)_{13,23}(\tilde U^T\underline CE)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde h_+^\dagger$}
\def\spdol{$\tilde{\bar h}_-^\dagger$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{${\bar d}_{1,2}^c$}
\def\isti{${\bar u}^c$}

\propto\;\;\;\;\;
(U^T\underline CE)_{1i}(D_c^\dagger Y_D^\dagger\tilde U^*)_{13,23}
(\tilde U^T\underline A^S \tilde D)_{33}(\tilde D^\dagger Y_U^*U_c^*)_{31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde{\bar h}_-^\dagger$}
\def\spdol{$\tilde h_+^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar e}_i^c$}

\propto\;\;\;\;\;
(D^T\underline C\tilde N)_{13,23}(\tilde N^\dagger Y_E^\dagger E_c^*)_{3i}
(U_c^\dagger Y_U^\dagger\tilde D^*)_{13}(\tilde D^T\underline A^S U)_{31}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde\nu$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde{\bar h}_-^\dagger$}
\def\spdol{$\tilde h_+^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar e}_i^c$}

\propto\;\;\;\;\;
(D^T\underline A^S U)_{11,21}(U_c^\dagger Y_U^\dagger\tilde
D^*)_{13}(\tilde D^T\underline C\tilde N)_{33}
(\tilde N^\dagger Y_E^\dagger E_c^*)_{3i}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde{\bar h}_0^\dagger$}
\def\spdol{$\tilde h_0^\dagger$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar d}_{1,2}^c$}

\propto\;\;\;\;\;
(U^T\underline A^S \tilde D)_{13}(\tilde D^\dagger Y_D^* D_c^*)_{31,32}
(U_c^\dagger Y_U^\dagger\tilde U^*)_{13}(\tilde U^T\underline CE)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde b$}
\def\spgor{$\tilde h_0^\dagger$}
\def\spdol{$\tilde{\bar h}_0^\dagger$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{${\bar d}_{1,2}^c$}
\def\isti{${\bar u}^c$}

\propto\;\;\;\;\;
(U^T\underline CE)_{1i}(D_c^\dagger Y_D^\dagger\tilde D^*)_{13,23}
(\tilde D^T\underline A^S \tilde U)_{33}(\tilde U^\dagger Y_U^*U_c^*)_{31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde t^c$}
\def\sfdol{$\tilde\tau^c$}
\def\spgor{$\tilde h_0$}
\def\spdol{$\tilde{\bar h}_0$}
\def\iena{${\bar d}_{1,2}^c$}
\def\idva{${\bar u}^c$}
\def\itri{${\bar e}_i$}
\def\isti{$u$}

\propto\;\;\;\;\;
(D_c^\dagger\underline D^\dagger\tilde U_c^*)_{13,23}
(\tilde U_c^TY_U^TU)_{31}(E^TY_E^T\tilde E_c)_{i3}
(\tilde E_c^\dagger\underline B^\dagger U_c^*)_{31}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde t^c$}
\def\sfdol{$\tilde\tau^c$}
\def\spgor{$\tilde h_0$}
\def\spdol{$\tilde{\bar h}_0$}
\def\iena{${\bar d}_{1,2}^c$}
\def\idva{${\bar u}^c$}
\def\itri{${\bar e}_i$}
\def\isti{$u$}

\propto\;\;\;\;\;
(D_c^\dagger\underline D^\dagger U_c^*)_{11,21}
(E^TY_E^T\tilde E_c)_{i3}(\tilde E_c^\dagger\underline B^\dagger
\tilde U_c^*)_{33}(\tilde U_c^TY_U^TU)_{31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde b^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde{\bar h}_0$}
\def\spdol{$\tilde h_0$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar e}_i^c$}
\def\itri{$u$}
\def\isti{$d_{1,2}$}

\propto\;\;\;\;\;
(U_c^\dagger\underline D^*\tilde D_c^*)_{13}
(\tilde D_c^TY_D^TD)_{31,32}(U^TY_U\tilde U_c)_{13}
(\tilde U_c^\dagger\underline B^* E_c^*)_{3i}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde t^c$}
\def\sfdol{$\tilde b^c$}
\def\spgor{$\tilde h_0$}
\def\spdol{$\tilde{\bar h}_0$}
\def\iena{${\bar e}_i^c$}
\def\idva{${\bar u}^c$}
\def\itri{$d_{1,2}$}
\def\isti{$u$}

\propto\;\;\;\;\;
(E_c^\dagger\underline B^\dagger U_c^*)_{i1}(D^TY_D\tilde D_c)_{13,23}
(\tilde D_c^\dagger\underline D^\dagger\tilde U_c^*)_{33}
(\tilde U_c^TY_U^TU)_{31}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde t$}
\def\sfdol{$\tilde\tau$}
\def\spgor{$\tilde h_0^\dagger$}
\def\spdol{$\tilde{\bar h}_0^\dagger$}
\def\iena{$d_{1,2}$}
\def\idva{$u$}
\def\itri{${\bar e}_i^c$}
\def\isti{${\bar u}^c$}

\propto\;\;\;\;\;
(D^T\underline A^S \tilde U)_{13,23}
(\tilde U^\dagger Y_U^*U_c^*)_{31}(E_c^\dagger Y_E^*\tilde E^*)_{i3}
(\tilde E^T\underline C^T U)_{31}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde\tau$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde{\bar h}_0^\dagger$}
\def\spdol{$\tilde h_0^\dagger$}
\def\iena{$u$}
\def\idva{$d_{1,2}$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar e}_i^c$}

\propto\;\;\;\;\;
(U^T\underline A^S D)_{11,12}
(U_c^\dagger Y_U^\dagger\tilde U^*)_{13}(\tilde U^T\underline
C\tilde E)_{33}(\tilde E^\dagger Y_E^\dagger E_c^*)_{3i}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T$}
\def\trdol{$\tilde{\bar T}$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{$u$}
\def\isti{$d_{1,2}$}

\propto\;\;\;\;\;
(U^T\underline A^S \tilde D)_{13}(\tilde D^\dagger D)_{31,32}
(U^T\tilde U^*)_{13}(\tilde U^T\underline CE)_{3i}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde b$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$u$}
\def\idva{$e_i$}
\def\itri{$u$}
\def\isti{$d_{1,2}$}

\propto\;\;\;\;\;
(U^T\underline CE)_{1i}(U^T\tilde U^*)_{13}
(\tilde U^T\underline A^S \tilde D)_{33}(\tilde D^\dagger D)_{31,32}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}$}
\def\trdol{$\tilde T$}
\def\sfgor{$\tilde\tau$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$u$}
\def\idva{$d_{1,2}$}
\def\itri{$u$}
\def\isti{$e_i$}

\propto\;\;\;\;\;
(U^T\underline C\tilde E)_{13}(\tilde E^\dagger E)_{3i}
(U^T\tilde U^*)_{13}(\tilde U^T\underline A^S D)_{31,32}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde\tau$}
\def\sfdol{$\tilde t$}
\def\spgor{$\tilde V_0$}
\def\spdol{$\tilde V_0$}
\def\iena{$u$}
\def\idva{$d_{1,2}$}
\def\itri{$u$}
\def\isti{$e_i$}

\propto\;\;\;\;\;
(U^T\underline A^S D)_{11,12}(U^T\tilde U^*)_{13}
(\tilde U^T\underline C\tilde E)_{33}(\tilde E^\dagger E)_{3i}
\end{equation}

\begin{equation}
\def\trgor{$\tilde{\bar T}^\dagger$}
\def\trdol{$\tilde T^\dagger$}
\def\sfgor{$\tilde b^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde V_0^\dagger$}
\def\spdol{$\tilde V_0^\dagger$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar e}_i^c$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar d}_{1,2}^c$}

\propto\;\;\;\;\;
(U_c^\dagger\underline D^*\tilde D_c^*)_{13}(\tilde D_c^T D_c^*)_{31,32}
(U_c^\dagger\tilde U_c)_{13}(\tilde U_c^\dagger\underline B^*E_c^*)_{3i}
\end{equation}

\begin{equation}
\def\tr{$T$}
\def\sfgor{$\tilde b^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde V_0^\dagger$}
\def\spdol{$\tilde V_0^\dagger$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar e}_i^c$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar d}_{1,2}^c$}

\propto\;\;\;\;\;
(U_c^\dagger\underline B^*E_c^*)_{1i}(U_c^\dagger\tilde U_c)_{13}
(\tilde U_c^\dagger\underline D^*\tilde D_c^*)_{33}
(\tilde D_c^TD_c^*)_{31,32}
\end{equation}

\begin{equation}
\def\trgor{$\tilde T^\dagger$}
\def\trdol{$\tilde{\bar T}^\dagger$}
\def\sfgor{$\tilde\tau^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde V_0^\dagger$}
\def\spdol{$\tilde V_0^\dagger$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar d}_{1,2}^c$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar e}_i^c$}

\propto\;\;\;\;\;
(U_c^\dagger\underline B^*\tilde E_c^*)_{13}(\tilde E_c^TE_c^*)_{3i}
(U_c^\dagger\tilde U_c)_{13}
(\tilde U_c^\dagger\underline D^*D_c^*)_{31,32}
\end{equation}

\begin{equation}
\def\tr{$\bar T$}
\def\sfgor{$\tilde\tau^c$}
\def\sfdol{$\tilde t^c$}
\def\spgor{$\tilde V_0^\dagger$}
\def\spdol{$\tilde V_0^\dagger$}
\def\iena{${\bar u}^c$}
\def\idva{${\bar d}_{1,2}^c$}
\def\itri{${\bar u}^c$}
\def\isti{${\bar e}_i^c$}

\propto\;\;\;\;\;
(U_c^\dagger\underline D^* D_c^*)_{11,12}
(U_c^\dagger\tilde U_c)_{13}
(\tilde U_c^\dagger\underline B^*\tilde E_c^*)_{33}
(\tilde E_c^T E_c^*)_{3i}
\end{equation}
\\
\\
\\
\\

where:

\beq
\underline{A}^S=\underline{A} + \underline{A}^T
\eeq
\\
\\
\\
\\
For the case when there are more than one pair of Higgs triplet and
anti-triplet, as is often the case in $SO(10)$ models, one must
go to the mass diagonal basis for these fields to compute the
dimension five operators generated by their elimination. 
 The preceding diagrammatic analysis exhibits 
that the baryon and lepton number violating $d=5$  operators 
 are quite model dependent and generic predictions are not possible. 
 Specifically the proton lifetime predictions depend on the structure of the 
Higgs sector, and on the mixing between the fermion and the sfermions. 
However,  calculations with greater predictivity are possible if the model is fully 
well defined, including the Higgs sector, and the supersymmetry
breaking sector is well defined as, for example, is the case for the minimal supergravity
  model (mSUGRA).
