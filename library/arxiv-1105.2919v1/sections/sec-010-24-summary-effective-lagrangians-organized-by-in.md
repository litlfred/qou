---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-010-24-summary-effective-lagrangians-organized-by-in
section_title: "Summary: Effective Lagrangians organized by interaction index"
section_number: 2.4
pages: 15-16
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.76
latex_coverage_ratio: 0.986
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
To summarize, the effective Lagrangian needed to derive nuclear
forces includes the following parts:
\begin{equation}
{\cal L_{\rm eff}} 
=
{\cal L}_{\pi\pi} 
+
{\cal L}_{\pi N} 
+
{\cal L}_{NN} 
+ \ldots ,
\end{equation}
where the ellipsis stands for terms that involve two nucleons plus
pions and three or more
nucleons with or without pions, relevant for nuclear
many-body forces 
(cf.\ last two terms of Eq.~(\ref{eq_LD1}), below, and Section~\ref{sec_manyNF}).

In previous sections, we organized the Lagrangians by the number
of derivatives or pion-mass insertions. This is 
the standard way, appropriate particularly for
considerations of $\pi$-$\pi$ and $\pi$-$N$ scattering.
As it turns out (cf.\ Section~\ref{sec_chpt}), 
for interactions among nucleons,
it is sometimes useful to also consider the so-called
index of the interaction,
\begin{equation}
\Delta  \equiv   d + \frac{n}{2} - 2  \, ,
\label{eq_Delta}
\end{equation}
where $d$ is the number of derivatives or pion-mass insertions 
and $n$ the number of nucleon field operators (nucleon legs).
We will now re-write the HB Lagrangian in terms
of increasing values of the parameter $\Delta$.

The leading-order Lagrangian reads,
\begin{eqnarray}
\widehat{\cal L}^{\Delta=0} &=&
	\frac{1}{2} 
	\partial_\mu \mbox{\boldmath{$\pi$}} \cdot 
	\partial^\mu \mbox{\boldmath{$\pi$}}
     -  \frac{1}{2} m_\pi^2 \mbox{\boldmath{$\pi$}}^2
\nonumber \\ &&
     +  \frac{1-4\alpha}{2f_\pi^2} 
        (\mbox{\boldmath{$\pi$}} \cdot \partial_\mu \mbox{\boldmath{$\pi$}})
        (\mbox{\boldmath{$\pi$}} \cdot \partial^\mu \mbox{\boldmath{$\pi$}})
     -  \frac{\alpha}{f_\pi^2} 
        \mbox{\boldmath{$\pi$}}^2
	\partial_\mu \mbox{\boldmath{$\pi$}} \cdot 
	\partial^\mu \mbox{\boldmath{$\pi$}}
     +\;  \frac{8\alpha-1}{8f_\pi^2} 
        m_\pi^2 \mbox{\boldmath{$\pi$}}^4
\nonumber \\ &&
+ \bar{N} \left[ 
i \partial_0 
- \frac{g_A}{2f_\pi} \; \mbox{\boldmath $\tau$} \cdot 
 ( \vec \sigma \cdot \vec \nabla ) \mbox{\boldmath $\pi$} 
- \frac{1}{4f_\pi^2} \; \mbox{\boldmath $\tau$} \cdot 
 ( \mbox{\boldmath $\pi$}
\times \partial_0 \mbox{\boldmath $\pi$})
\right] N
\nonumber \\ &&
+ \bar{N} \left\{
 \frac{g_A(4\alpha-1)}{4f_\pi^3} \;
(\mbox{\boldmath $\tau$} \cdot 
\mbox{\boldmath $\pi$}) 
\left[ \mbox{\boldmath $\pi$} \cdot 
 ( \vec \sigma \cdot \vec \nabla )
\mbox{\boldmath $\pi$} \right]
+ \frac{g_A\alpha}{2f_\pi^3} \;
\mbox{\boldmath $\pi$}^2 
\left[ \mbox{\boldmath $\tau$} \cdot 
 ( \vec \sigma \cdot \vec \nabla )
\mbox{\boldmath $\pi$} 
\right]
\right\} N 
\nonumber \\ &&
-\frac{1}{2} C_S \bar{N} N \bar{N} N 
-\frac{1}{2} C_T (\bar{N} \vec \sigma N) \cdot (\bar{N} \vec \sigma N) 
\; + \; \ldots \,,
\label{eq_LD0}
\end{eqnarray}
and subleading Lagrangians are,
\begin{eqnarray}
\widehat{\cal L}^{\Delta=1} &=&
 \bar{N} \left\{
 \frac{{\vec \nabla}^2}{2M_N} 
-\frac{ig_A}{4M_Nf_\pi} 
\mbox{\boldmath $\tau$} \cdot 
\left[
\vec \sigma \cdot
\left( \stackrel{\leftarrow}{\nabla} 
\partial_0 \mbox{\boldmath $\pi$}
 -
\partial_0 \mbox{\boldmath $\pi$}
\stackrel{\rightarrow}{\nabla} \right)
\right]
\right.
\nonumber \\ &&
\left.
- \frac{i}{8M_N f_\pi^2}
\mbox{\boldmath $\tau$} \cdot 
\left[
\stackrel{\leftarrow}{\nabla} 
\cdot
( \mbox{\boldmath $\pi$} \times \vec\nabla \mbox{\boldmath $\pi$} )
   -   
( \mbox{\boldmath $\pi$} \times \vec\nabla \mbox{\boldmath $\pi$} )
\cdot
\stackrel{\rightarrow}{\nabla} 
\right]
\right\} N 
\nonumber \\ &&
+ \bar{N} \left[
 4c_1m_\pi^2
-\frac{2 c_1}{f_\pi^2} \, m_\pi^2\, \mbox{\boldmath $\pi$}^2 
\, + \, 
\left( c_2 - \frac{g_A^2}{8M_N}\right) 
\frac{1}{f_\pi^2}
(\partial_0 \mbox{\boldmath{$\pi$}} \cdot 
 \partial_0 \mbox{\boldmath{$\pi$}})
\right.  \nonumber \\ &&  \left.
 + \, \frac{c_3}{f_\pi^2}\,
(\partial_\mu \mbox{\boldmath{$\pi$}} \cdot 
\partial^\mu \mbox{\boldmath{$\pi$}})

 - \, \left( c_4 + \frac{1}{4M_N} \right) 
\frac{1}{2f_\pi^2}
\epsilon^{ijk} \epsilon^{abc} \sigma^i \tau^a
(\partial^j \pi^b) (\partial^k \pi^c)
 \right] N 
\nonumber \\ &&
- \frac{D}{4f_\pi} (\bar{N}N) \bar{N} \left[ 
\mbox{\boldmath $\tau$} 
\cdot ( \vec \sigma \cdot \vec \nabla )
\mbox{\boldmath $\pi$} 
\right] N
-\frac12 E
(\bar{N}N)
(\bar{N}
\mbox{\boldmath $\tau$} 
N)
\cdot
(\bar{N}
\mbox{\boldmath $\tau$} 
N)
\; + \; \ldots \,,
\label{eq_LD1}
\\
\widehat{\cal L}^{\Delta=2} &=&
\; {\cal L}^{(4)}_{\pi\pi} \; +
\; \widehat{\cal L}^{(3)}_{\pi N} \; + \; \widehat{\cal L}^{(2)}_{NN}
\; + \; \ldots \,,
\label{eq_LD2}
\\
\widehat{\cal L}^{\Delta=4} &=&
\; \widehat{\cal L}^{(4)}_{NN}
\; + \; \ldots \,,
\label{eq_LD4}
\end{eqnarray}
where the ellipses represent terms that are irrelevant
for the derivation of nuclear forces up to fourth
order.




\section{Nuclear forces from EFT: Overview
\label{sec_overview}}

In the beginning of Section~\ref{sec_EFT},
we listed the steps we have to take for carrying out
the EFT program of a derivation of nuclear forces.
So far, we discussed steps one to three.
What is left are steps four (low-momentum expansion) and
five (Feynman diagrams).
In this section, we will say more about the expansion
we are using and
give an overview of the Feynman diagrams that arise
order by order.
