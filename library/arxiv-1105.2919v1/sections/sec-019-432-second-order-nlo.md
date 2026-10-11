---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-019-432-second-order-nlo
section_title: "Second order (NLO)"
section_number: 4.3.2
pages: 32-35
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
text_source: latex
latex_prose_ratio: 0.799
latex_coverage_ratio: 0.983
---
The contact Lagrangian
$\widehat{\cal L}^{(2)}_{NN}$,
Eq.~(\ref{eq_LNN2}), 
which is part of 
$\widehat{\cal L}^{\Delta=2}$,
Eq.~(\ref{eq_LD2}), 
generates the following $NN$ contact potential
\be
V_{\rm ct}^{(2)}(\vec{p'},\vec{p}) &=&
C_1 \, q^2 +
C_2 \, k^2 
\nonumber 
\\ &+& 
\left(
C_3 \, q^2 +
C_4 \, k^2 
\right) \vec{\sigma}_1 \cdot \vec{\sigma}_2 
\nonumber 
\\
&+& C_5 \left( -i \vec{S} \cdot (\vec{q} \times \vec{k}) \right)
\nonumber 
\\ &+& 
 C_6 \, ( \vec{\sigma}_1 \cdot \vec{q} )\,( \vec{\sigma}_2 \cdot 
\vec{q} )
\nonumber 
\\ &+& 
 C_7 \, ( \vec{\sigma}_1 \cdot \vec{k} )\,( \vec{\sigma}_2 \cdot 
\vec{k} ) \,.
\label{eq_ct2}
\ee
The coefficients $C_i$ used here in the contact potential
are, of course, related to the coefficients $C_i'$
that occur in the Lagrangian
$\widehat{\cal L}^{(2)}_{NN}$,
Eq.~(\ref{eq_LNN2}).
The relation, which is unimportant for our purposes,
can be found in Refs.~\cite{ORK96,EGM98}.

There are many ways to perform the partial-wave decomposition
of the above potential.
We perceive the method presented 
by Erkelenz, Alzetta, and Holinde~\cite{EAH71} as the
most elegant one.
Thus, one obtains
\be
V_{\rm ct}^{(2)}(^1 S_0)          &=&  C_{^1 S_0} ( p^2 + {p'}^2 ) 
\nonumber \\
V_{\rm ct}^{(2)}(^3 P_0)          &=&  C_{^3 P_0} \, p p'
\nonumber \\
V_{\rm ct}^{(2)}(^1 P_1)          &=&  C_{^1 P_1} \, p p' 
\nonumber \\
V_{\rm ct}^{(2)}(^3 P_1)          &=&  C_{^3 P_1} \, p p' 
\nonumber \\
V_{\rm ct}^{(2)}(^3 S_1)          &=&  C_{^3 S_1} ( p^2 + {p'}^2 ) 
\nonumber \\
V_{\rm ct}^{(2)}(^3 S_1- ^3 D_1)  &=&  C_{^3 S_1- ^3 D_1}  p^2 
\nonumber \\
V_{\rm ct}^{(2)}(^3 D_1- ^3 S_1)  &=&  C_{^3 S_1- ^3 D_1}  {p'}^2 
\nonumber \\
V_{\rm ct}^{(2)}(^3 P_2)          &=&  C_{^3 P_2} \, p p' 
\label{eq_ct2_pw}
\ee
with
\be
C_{^1 S_0} 
&=&
4\pi\, \left( C_1 + \frac{1}{4} C_2 - 3 C_3 - \frac{3}{4} C_4 - 
C_6 - \frac{1}{4} C_7 \right)
\nonumber 
\\
C_{^3 P_0} 
&=&
4\pi\, \left( -\frac{2}{3} C_1 + \frac{1}{6} C_2 - \frac{2}{3} C_3 
+ \frac{1}{6} C_4 - \frac{2}{3} C_5
+ 2 C_6 - \frac{1}{2} C_7 \right)
\nonumber 
\\
C_{^1 P_1} 
&=&
4\pi\, \left( -\frac{2}{3} C_1 + \frac{1}{6} C_2 + 2 C_3 
- \frac{1}{2} C_4 
+ \frac{2}{3} C_6 - \frac{1}{6} C_7 \right)
\nonumber 
\\
C_{^3 P_1} 
&=&
4\pi\, \left( -\frac{2}{3} C_1 + \frac{1}{6} C_2 - \frac{2}{3} C_3 
+ \frac{1}{6} C_4 - \frac{1}{3} C_5
- \frac{4}{3} C_6 + \frac{1}{3} C_7 \right)
\nonumber 
\\
C_{^3 S_1} 
&=&
4\pi\, \left( C_1 + \frac{1}{4} C_2 + C_3 + \frac{1}{4} C_4 + 
\frac{1}{3} C_6 + \frac{1}{12} C_7 \right)
\nonumber 
\\
C_{^3 S_1- ^3 D_1} 
&=&
4\pi\, \left( -\frac{2\sqrt{2}}{3} C_6 - \frac{\sqrt{2}}{6} 
C_7 \right)
\nonumber 
\\
C_{^3 P_2} 
&=&
4\pi\, \left( -\frac{2}{3} C_1 + \frac{1}{6} C_2 - \frac{2}{3} C_3 
+ \frac{1}{6} C_4 + \frac{1}{3} C_5 \right) \,.
\label{eq_ct2_pwcoef}
\ee




\subsubsection{Fourth order (N$^3$LO)}

The contact potential of order four reads
\be
V_{\rm ct}^{(4)}(\vec{p'},\vec{p}) &=&
D_1 \, q^4 +
D_2 \, k^4 +
D_3 \, q^2 k^2 +
D_4 \, (\vec{q} \times \vec{k})^2 
\nonumber 
\\ &+& 
\left(
D_5 \, q^4 +
D_6 \, k^4 +
D_7 \, q^2 k^2 +
D_8 \, (\vec{q} \times \vec{k})^2 
\right) \vec{\sigma}_1 \cdot \vec{\sigma}_2 
\nonumber 
\\ &+& 
\left(
D_9 \, q^2 +
D_{10} \, k^2 
\right) \left( -i \vec{S} \cdot (\vec{q} \times \vec{k}) \right)
\nonumber 
\\ &+& 
\left(
D_{11} \, q^2 +
D_{12} \, k^2 
\right) ( \vec{\sigma}_1 \cdot \vec{q} )\,( \vec{\sigma}_2 
\cdot \vec{q})
\nonumber 
\\ &+& 
\left(
D_{13} \, q^2 +
D_{14} \, k^2 
\right) ( \vec{\sigma}_1 \cdot \vec{k} )\,( \vec{\sigma}_2 
\cdot \vec{k})
\nonumber 
\\ &+& 
D_{15} \left( 
\vec{\sigma}_1 \cdot (\vec{q} \times \vec{k}) \, \,
\vec{\sigma}_2 \cdot (\vec{q} \times \vec{k}) 
\right) .
\label{eq_ct4}
\ee
The rather lengthy partial-wave expressions of this order
are relegated to \ref{app_ct}.




\subsection{Definition of $NN$ potential
\label{sec_pot}}

We have now rounded up everything needed for a realistic
nuclear force---long, intermediate, and short ranged 
components---and so we can finally proceed to the lower
partial waves. However, here we encounter another problem.
The two-nucleon system at low angular momentum, particularly,
in $S$ waves, is characterized by the
presence of a shallow bound state (the deuteron)
and large scattering lengths.
Thus, perturbation theory does not apply.
In contrast to $\pi$-$\pi$ and $\pi$-$N$,
the interaction between nucleons is not suppressed
in the chiral limit ($Q\rightarrow 0$).
Weinberg~\cite{Wei90,Wei91} showed that the strong enhancement of the
scattering amplitude arises from purely nucleonic intermediate
states (``infrared enhancement''). He therefore suggested to use perturbation theory to
calculate the $NN$ potential (i.e., the irreducible graphs) and to apply this potential
in a scattering equation 
to obtain the $NN$ amplitude. We will follow
this prescription and discuss potential problems in the next subsection.

Since the irreducible diagrams that make up the potential
are calculated using
covariant perturbation theory (cf.~Section~\ref{sec_pi}), 
it is consistent to
start from the covariant
Bethe-Salpeter (BS) equation~\cite{SB51} describing
two-nucleon scattering.
In operator notation, the BS equation reads
\begin{equation}
T = {\cal V+V\,G} \,T
\label{eq_BS}
\end{equation}
where $T$ denotes the invariant T-matrix ($T=i{\cal M}$ with ${\cal M}$ the invariant
amplitude) for the two-nucleon scattering process,
${\cal V}$ the sum of all connected two-particle irreducible diagrams, and 
${\cal G}$ is $(-i)$ times the relativistic two-nucleon propagator. 
The BS equation
is equivalent to a set of two equations
\begin{eqnarray}
{T}&=&{V}+{V} \, g \, {T}
\label{eq_bbs}
\\
{V}&=&{\cal V + V\,(G}-g)\,{V} 
\label{eq_BS2}
\\
   &=& {\cal V} + {\cal V}_{1\pi}\,({\cal G}-g)\,{\cal V}_{1\pi} 
    + \ldots \, ,
\label{eq_BS3}
\end{eqnarray}
where $g$ is a covariant three-dimensional propagator
which preserves relativistic elastic unitarity.
We choose the propagator $g$ proposed by 
Blankenbecler and Sugar (BbS)~\cite{BS66}
(for more details on relativistic three-dimensional
reductions of the BS equation, see Ref.~\cite{Mac89}). 
The ellipsis in Eq.~(\ref{eq_BS3}) stands for 
terms of irreducible $3\pi$ and higher pion exchanges
which we neglect.

Note that when we speak of covariance in conjunction with
(heavy baryon) ChPT, we are not referring to manifest
covariance. Relativity and relativistic off-shell
effects are accounted for in terms of
a $Q/M_N$ expansion up to the given order
and up to the number of pions we take into consideration.
Thus, Eq.~(\ref{eq_BS3}) is evaluated in the following way,
\begin{eqnarray}
V  & \approx &
 \:  {\cal V} (\mbox{\rm on-shell}) \: + \:
 {\cal V}_{1\pi}\,{\cal G}\,{\cal V}_{1\pi}-{V}_{1\pi}\,{g}\,{V}_{1\pi} 
\\
 & \approx & 
 \; V_{1\pi} \; + \; \widetilde{V}_{2\pi} \; + \:
 {\cal V}_{1\pi}\,{\cal G}\,{\cal V}_{1\pi}-{V}_{1\pi}\,{g}\,{V}_{1\pi} 
\\
 & = & 
 \; V_{1\pi} \; + \; V_{2\pi}'
\,,
\label{eq_BS4}
\end{eqnarray}
where
${\cal V}_{1\pi}$
denotes the relativistic (off-shell) 1PE, while
$V_{1\pi}$ is the on-shell 1PE given 
in Eq.~(\ref{eq_1pe}).
$\widetilde{V}_{2\pi}$  stands for the
irreducible $2\pi$ exchanges calculated (on-shell) in Section~\ref{sec_2pi},
{\it but without the covariant planar box diagram}, 
which in the above equations is given by
${\cal V}_{1\pi}\,{\cal G}\,{\cal V}_{1\pi}$.
Furthermore,
${V}_{1\pi}\,{g}\,{V}_{1\pi}$
is the iterated 1PE discussed in 
Section~\ref{sec_2piit}.
Thus, the term
$({\cal V}_{1\pi}\,{\cal G}\,{\cal V}
_{1\pi}-{V}_{1\pi}\,{g}\,{V}_{1\pi})$
represents the irreducible part of the
box diagram contribution. Finally,
$V_{2\pi}'$ subsumes all $2\pi$ exchanges without the iterated
$V_{1\pi}$ and is, therefore, also known as the irreducible 2PE.
Since all contributions are calculated on shell, the potential
has no energy dependence.

Adding the short-range contact terms $V_{\rm ct}$ to the above,
yields the full $NN$ potential, 
\begin{equation}
V = V_{1\pi} + V_{2\pi}' + V_{\rm ct} 
\,.
\label{eq_pot1}
\end{equation}
Notice that the pion-exchange part of this potential
differs from the perturbative amplitude, Eq.~(\ref{eq_tall}),
by the absence of the iterative 2PE. The latter is generated
automatically when the potential is inserted into a Schroedinger
or Lippmann-Schwinger equation (see below).
We also note that adding the contact interactions to the
pion interactions will generate loop corrections
of the contact terms. This leads to a $m_\pi$-dependent renormalization
of the contact parameters and can be ignored if $m_\pi$-dependence
is not an issue.

As discussed, the irreducible 2PE, $V_{2\pi}'$, is organized
according to increasing orders,
\begin{equation}
V_{2\pi}' = 
V_{2\pi}^{'(2)} +
V_{2\pi}^{'(3)} +
V_{2\pi}^{'(4)} 
+ \ldots 
\,,
\end{equation}
and was calculated in Section~\ref{sec_2pi}:
$V_{2\pi}^{'(2)}$
is given by the contributions of
Eqs.~(\ref{eq_2C}) and (\ref{eq_2T}),
$V_{2\pi}^{'(3)}$
is made up from
Eqs.~(\ref{eq_3C})-(\ref{eq_3EM4}), and
$V_{2\pi}^{'(4)}$
is contained in \ref{app_N3LO}.

The contact potentials come in even orders,
\begin{equation}
V_{\rm ct} =
V_{\rm ct}^{(0)} + 
V_{\rm ct}^{(2)} + 
V_{\rm ct}^{(4)} 
+ \ldots
\,,
\end{equation}
and were presented in Section~\ref{sec_ct}.

In summary, the $NN$ potential $V$, calculated 
to certain orders,
is given by:
\begin{eqnarray}
V_{\rm LO} &=& V_{1\pi} + V_{\rm ct}^{(0)} 
\label{eq_Vlo} \\
V_{\rm NLO} &=& V_{\rm LO} + V_{2\pi}^{'(2)} + V_{\rm ct}^{(2)} 
\label{eq_Vnlo} \\
V_{\rm NNLO} &=& V_{\rm NLO} + V_{2\pi}^{'(3)} 
\label{eq_Vnnlo} \\
V_{{\rm N}^3{\rm LO}} &=&
 V_{\rm NNLO} + V_{2\pi}^{'(4)} + V_{\rm ct}^{(4)}
\label{eq_Vn3lo}
\end{eqnarray}

The potential $V$ satisfies the relativistic
BbS equation, Eq.~(\ref{eq_bbs}), which reads explicitly,
\begin{equation}
{T}({\vec p}~',{\vec p})= {V}({\vec p}~',{\vec p})+
\int \frac{d^3p''}{(2\pi)^3} \:
{V}({\vec p}~',{\vec p}~'') \:
\frac{M_N^2}{E_{p''}} \:  
\frac{1}
{{ p}^{2}-{p''}^{2}+i\epsilon} \:
{T}({\vec p}~'',{\vec p}) 
\label{eq_bbs2}
\end{equation}
with $E_{p''}\equiv \sqrt{M_N^2 + {p''}^2}$.
The advantage of using a relativistic scattering equation is that it automatically
includes relativistic corrections to all orders. Thus, in the scattering equation,
no propagator modifications are necessary when raising the order to which the
calculation is conducted.

Defining
\begin{equation}
\widehat{V}({\vec p}~',{\vec p})
\equiv 
\frac{1}{(2\pi)^3}
\sqrt{\frac{M_N}{E_{p'}}}\:  
{V}({\vec p}~',{\vec p})\:
 \sqrt{\frac{M_N}{E_{p}}}
\label{eq_minrel1}
\end{equation}
and
\begin{equation}
\widehat{T}({\vec p}~',{\vec p})
\equiv 
\frac{1}{(2\pi)^3}
\sqrt{\frac{M_N}{E_{p'}}}\:  
{T}({\vec p}~',{\vec p})\:
 \sqrt{\frac{M_N}{E_{p}}}
\,,
\label{eq_minrel2}
\end{equation}
where the factor $1/(2\pi)^3$ is added for convenience,
the BbS equation collapses into the usual, nonrelativistic
Lippmann-Schwinger (LS) equation,
\begin{equation}
 \widehat{T}({\vec p}~',{\vec p})= \widehat{V}({\vec p}~',{\vec p})+
\int d^3p''\:
\widehat{V}({\vec p}~',{\vec p}~'')\:
\frac{M_N}
{{ p}^{2}-{p''}^{2}+i\epsilon}\:
\widehat{T}({\vec p}~'',{\vec p}) \, .
\label{eq_LS}
\end{equation}
Since 
$\widehat V$ 
satisfies Eq.~(\ref{eq_LS}), 
it can be used like a usual nonrelativistic potential, and 
$\widehat{T}$ 
may be perceived as the conventional nonrelativistic 
T-matrix.
In applications, it is more convenient to use the K-matrix instead
of the T-matrix and to have the LS equation
decomposed into partial waves: all these technical issues
are explained in detail in Appendix A of Ref.~\cite{Mac01} where also 
the formulas for the calculation of $np$ and $pp$ (the latter with Coulomb) phase shifts
are provided.
The partial wave decomposition of the operators by which the potential
is represented can be found in section~4 of Ref.~\cite{EAH71}, and numerical methods
for solving the LS equation are explained in Ref.~\cite{Mac93}.
