---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-026-451-regularization-and-non-perturbative-renormal
section_title: "Regularization and non-perturbative renormalization"
section_number: 4.5.1
pages: 36-37
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 1.0
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Iteration of $\widehat V$ in the LS equation, Eq.~(\ref{eq_LS}),
requires cutting $\widehat V$ off for high momenta to avoid infinities.
This is consistent with the fact that ChPT
is a low-momentum expansion which
is valid only for momenta $Q \ll \Lambda_\chi \approx 1$ GeV.
Therefore, the potential $\widehat V$
is multiplied
with the regulator function $f(p',p)$,
\begin{equation}
{\widehat V}(\vec{ p}~',{\vec p})
\longmapsto
{\widehat V}(\vec{ p}~',{\vec p}) \, f(p',p) 
\end{equation}
with
\begin{equation}
f(p',p) = \exp[-(p'/\Lambda)^{2n}-(p/\Lambda)^{2n}] \,,
\label{eq_f}
\end{equation}
such that
\begin{equation}
{\widehat V}(\vec{ p}~',{\vec p}) \, f(p',p) 
\approx
{\widehat V}(\vec{ p}~',{\vec p})
\left\{1-\left[\left(\frac{p'}{\Lambda}\right)^{2n}
+\left(\frac{p}{\Lambda}\right)^{2n}\right]+ \ldots \right\} 
\,.
\label{eq_reg_exp}
\end{equation}
Typical choices for the cutoff parameter $\Lambda$ that
appears in the regulator are 
$\Lambda \approx 0.5 \mbox{ GeV} \ll \Lambda_\chi \approx 1$ GeV.

Equation~(\ref{eq_reg_exp}) provides an indication of the fact that
the exponential cutoff does not necessarily
affect the given order at which 
the calculation is conducted.
For sufficiently large $n$, the regulator introduces contributions that 
are beyond the given order. Assuming a good rate
of convergence of the chiral expansion, such orders are small 
as compared to the given order and, thus, do not
affect the accuracy at the given order.
In calculations, one uses, of course,
the exponential form, Eq.~(\ref{eq_f}),
and not the expansion Eq.~(\ref{eq_reg_exp}). On a similar note, we also
do not expand the square-root factors
in Eqs.~(\ref{eq_minrel1}-\ref{eq_minrel2})
because they are kinematical factors which guarantee
relativistic elastic unitarity.



It is pretty obvious that results for the $T$-matrix may
depend sensitively on the regulator and its cutoff parameter.
This is acceptable if one wishes to build models.
For example, the meson models of the past~\cite{Mac89,MHE87}
always depended sensitively on the choices for the
cutoff parameters which, in fact,
were important for the fit of the $NN$ data.
However, the EFT approach wishes to be fundamental
in nature and not just another model.

In field theories, divergent integrals are not uncommon and methods have
been developed for how to deal with them.
One regulates the integrals and then removes the dependence
on the regularization parameters (scales, cutoffs)
by renormalization. In the end, the theory and its
predictions do not depend on cutoffs
or renormalization scales.

So-called renormalizable quantum field theories, like QED,
have essentially one set of prescriptions 
that takes care of renormalization through all orders. 
In contrast, 
EFTs are renormalized order by order. 

The renormalization of {\it perturbative}
EFT calculations is not a problem. {\it The problem
is nonperturbative renormalization.}
This problem typically occurs in {\it nuclear} EFT because
nuclear physics is characterized by bound states which
are nonperturbative in nature.
EFT power counting may be different for nonperturbative processes as
compared to perturbative ones. Such difference may be caused by the infrared
enhancement of the reducible diagrams generated in the LS equation.

Weinberg's implicit assumption~\cite{Wei90,Wei09} was that the counterterms
introduced to renormalize the perturbatively calculated
potential, based upon naive dimensional analysis (``Weinberg counting''),
are also sufficient to renormalize the nonperturbative
resummation of the potential in the LS equation.
In 1996, Kaplan, Savage, and Wise (KSW)~\cite{KSW96}
pointed out that there are problems with the Weinberg scheme
if the LS equation is renormalized 
by minimally-subtracted dimensional regularization.
This criticism resulted in a flurry of publications on
the renormalization of the nonperturbative
$NN$ problem
\cite{FMS00,PBC98,FTT99,Bir06,Bea02,VA05-1,NTK05,VA05-2,VA07,EM06,VA08,Ent08,YEP07,LK08,BKV08,Val08,ME10}.
The literature is too comprehensive
to discuss all contributions.
Let us just mention some of the work that has particular relevance
for our present discussion.

If the potential $V$ consists of contact terms only (a.k.a.\
pion-less theory), then
the nonperturbative summation (\ref{eq_LS})
can be performed analytically and the power counting is explicit.
However, when pion exchange is included, then (\ref{eq_LS})
can be solved only numerically and the power counting
is less transparent.
Perturbative ladder diagrams of arbitrarily high order,
where the rungs of the ladder represent a potential made up from
irreducible pion exchange,
suggest that an infinite number of counterterms is needed to achieve
cutoff independence for all the terms of increasing order generated
by the iterations.
For that reason, 
Kaplan, Savage, and Wise (KSW)~\cite{KSW96} proposed 
to sum the leading-order contact interaction to all orders (analytically)
and to add higher-order contacts and
pion exchange perturbatively up to the given order. Unfortunately,
it turned out that the order by order convergence of 1PE 
is poor in the $^3S_1$-$^3D_1$ state~\cite{FMS00}. 
The failure was triggered by the $1/r^3$ singularity of the 1PE tensor
force when iterated to second order. Therefore, KSW counting is no
longer taken into consideration (see, however, \cite{BKV08}).  
A balanced discussion of possible
solutions is provided in \cite{Bea02}.

Some researchers decided to take
a second look at Weinberg's original proposal.
A systematic investigation of Weinberg counting in leading order
has been conducted by Nogga, Timmermans, and van Kolck~\cite{NTK05}
in momentum space, and by Valderrama and Arriola
at LO and higher orders in
configuration space~\cite{VA05-1,VA05-2,VA07}. A comprehensive
discussion of both approaches and their equivalence can be found
in Refs.~\cite{Ent08,Val08}.

The LO $NN$ potential is given in (\ref{eq_Vlo}) and consists
of 1PE plus two nonderivative contact terms that contribute
only in $S$ waves.
Nogga {\it et al.}~\cite{NTK05} find that the given counterterms renormalize
the $S$ waves (i.e., stable results are obtained for $\Lambda \rightarrow \infty$) and
the naively expected infinite number of counterterms
is not needed. This means that Weinberg power counting does actually work in
$S$ waves at LO (ignoring the $m_\pi$ dependence of the contact interaction
discussed in Refs.~\cite{KSW96,Bea02}).
However, there are problems with a particular class of higher partial waves,
namely those  
in which the tensor force from 1PE is attractive. The first few cases
of this kind  of low angular momentum are
$^3P_0$, $^3P_2$, and $^3D_2$, which need a counterterm for cutoff independence. 
The leading (nonderivative) counterterms do not contribute in
$P$ and higher waves, which is why Weinberg counting fails in these cases. 
But the second order contact potential provides counterterms
for $P$ waves. Therefore, the promotion
of, particularly, the $^3P_0$ and $^3P_2$ contacts from NLO to LO would
fix the problem in $P$ waves. To take care of the $^3D_2$ problem,
a N$^3$LO contact, i.e. a term from $V^{(4)}_{\rm ct}$, needs to be promoted to LO.
Partial waves with orbital angular momentum $L\geq 3$ may be calculated in Born
approximation with sufficient accuracy and, therefore, do not pose renormalization
problems.
In this way, one arrives at a scheme
of `modified Weinberg counting'~\cite{NTK05} for the leading order 
two-nucleon interaction.
