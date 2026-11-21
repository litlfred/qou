---
doc_id: arxiv-1301.6953v1
doc_title: "Chiral Perturbation Theory and Mesons"
section_id: sec-002-3-determining-low-energy-constants-in-the-contin
section_title: "Determining low-energy-constants in the continuum"
section_number: 3
pages: 5-7
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.981
doc_brief: "Chiral Perturbation Theory and Mesons — 7 sections: Front matter; Chiral Perturbation Theory; Introduction"
---
Lattice QCD has now reached the stage where they can start determining
the ChPT LECs. A review is the FLAG collaboration \cite{FLAG} and
talks at this conference that had results on LECS are \cite{Lellouch,Stolz,
Deuzeman,Bernard}.

For the two-flavour constants the status has not really changed much since
the previous chiral dynamics.
The constants $\bar l_1$ to $\bar l_4$
are determined from ChPT at order $p^6$ and the Roy equation analysis
in $\pi\pi$ and $F_S$ \cite{CGL}. A related talk is \cite{Rios}.
$\bar l_5$
and $\bar l_6$ come from $F_V$ and $\pi\to\ell\nu\gamma$
\cite{BCT,BT}
and from $\Pi_V-\Pi_A$ \cite{GPP}.
Some related work using similar sum rules is \cite{Dominguez}.
In conclusion:
\begin{align}
\label{valueli}
\bar l_1&=-0.4\pm 0.6\,,&
\bar l_2&= 4.3\pm0.1\,,&
\bar l_3&=2.9\pm2.4\,,
\nonumber\\
\bar l_4&=4.4\pm0.2\,,&
\bar l_5 &= 12.24\pm0.21\,,&
\bar l_6-\bar l_5& = 3.0\pm0.3\,,
\nonumber\\
\bar l_6 &= 16.0\pm0.5\pm0.7\,.
\nonumber
\end{align}
and $l_7\sim 5\cdot 10^{-3}$
from $\pi^0$-$\eta$ mixing \cite{GL1}.
In the two-flavour case the contribution from the order $p^6$ LECs was small
so the uncertainty on estimating those is not very important.

The uncertainty on estimates of the order $p^6$ LECs, the $C_i^r$, in the
three flavour case is much more important because $m_K^2,m_\eta^2\gg m_\pi^2$.
The larger $C_i^r$ dependent contributions make their estimates much more
relevant. Typically, if the term multiplying a particular $C_i^r$ leads
to a kinematical dependence it can be measured and the estimates tested.
But if it leads only to a higher order quark-mass dependence they lead
to experiment in a 100\% correlated way with the order $p^4$ LECs, the $L_i^r$.
Here we really need the lattice, typically the latter type of $C_i^r$
need scalars to estimate their values from resonance exchance and are thus 
intrinsically less well estimated. In addition, often the large $N_c$ suppressed
terms in the order $p^6$ lagrangian contribute with large coefficients as well
and all estimates so far of the LECs rely on large $N_c$ to a large extent.
One big question is thus whether we are really testing ChPT or simply
doing a phenomenological fit. 
In order to answer this question a systematic
search for relations that are independent of the $C_i^r$ was done
\cite{relations}. We found there 35 relations between 76 observables
and of these 13 had sufficient data to study their success.
There were 7 relations in $\pi\pi$ scattering which worked about the same for
two and three flavour ChPT. The two relations involving $a_3^-$ did not
work well in either case. Of the 5 extra relations involving
$\pi\pi$ and $\pi K$ scattering three worked well, one of the bad ones involved
$a_3^-$ and the last one had very large NNLO corrections. The final relation
involves $K_{\ell4}$ and did not work well probably because ChPT fails to
describe the quadratic slope in the $F$ form-factor \cite{Kl4,Stoffer}.
The quality of the relations is shown in Fig.~\ref{fig3}. The conclusion is
that three flavour ChPT ``sort of'' works taking into account that the
relations involve very large correlations and that thus the experimental or dispersive input errors might be underestimated.
\begin{figure}
\centerline{\includegraphics[angle=270,width=0.9\textwidth]{figrelations.ps}}
\caption{\label{fig3} The quality of the relations found in \cite{relations}.
Shown are the NLO and NNLO predictions for combinations of observables with vanishes NNLO LEC contributions as well as the experimental/dispersive results for the same combinations.}
\end{figure}

The previous major fit to determine the $L_i^r$ using NNLO formulas
dates back to 2001 \cite{oldfit}. Given that many more calculations
in three flavour ChPT at NNLO have been performed since and that
the experimental input used then has also changed, an update has become
necessary. This was done in \cite{newfit} and the main results are summarized in Tab.~\ref{tab2}.
\begin{table}
\centerline{\begin{tabular}{|l|c c c c |c|}
\hline
             &fit 10 iso    & NA48/2   & $F_K/F_\pi$ & All $\star$ &  All  \\
\hline
      & old data      &          &            & $\pi\pi$, $\pi K$, $\langle r_S^2\rangle$ & $m_s/\hat m$\\[2mm]
$10^3 L_1^r$ &$0.39\pm0.12$ &\framebox{$0.88$}    & $0.87$     &$0.89$  &$0.88\pm0.09$ \\
$10^3 L_2^r$ &$0.73\pm0.12$ & $0.79$    & $0.80$     &$0.63$  &$0.61\pm0.20$ \\
$10^3 L_3^r$ &$-2.34\pm0.37$& $-3.11$   &$-3.09$     &$-3.06$ &$-3.04\pm0.43$\\
$10^3 L_4^r$ &$\equiv0$     & $\equiv0$ & $\equiv0$  &\framebox{$0.60$} &$0.75\pm0.75$ \\
$10^3 L_5^r$ &$0.97\pm0.11$ & $0.91$     & \framebox{$0.73$}   &\framebox{$0.58$}  &$0.58\pm0.13$ \\
$10^3 L_6^r$ &$\equiv 0$    & $\equiv 0$& $\equiv 0$ & $0.08$ &\framebox{$0.29\pm0.85$}   \\
$10^3 L_7^r$ &$-0.30\pm0.15$& $-0.30$    &$-0.26$    &$-0.22$ &$-0.11\pm0.15$  \\
$10^3 L_8^r$ &$0.60\pm0.20$ & $0.59$     & $0.49$    &$0.40$  &$0.18\pm0.18$  \\ \hline
$\chi^2$  & $0.26$  &$0.01$  &$0.01$   &$1.20$  &$1.28$ \\
dof  & 1 & 1 & 1 & 4 & 4 \\
\hline
\end{tabular}}
\caption{\label{tab2} The main new fit of the $L_i^r$ of \cite{newfit}.
The various columns show the changes w.r.t. the old fit of \cite{oldfit}.}
\end{table}
The old programs in the isospin conserving versions were rewritten
in {C++} for this purpose.
The first column uses the old input values and reproduces the old
fit \cite{oldfit} which was done isospin violation included. The next columns
give the results from including the NA48/2 data on the form factors
\cite{NA482},
the new value of $F_K/F_\pi$, the inclusion of $\pi\pi$, $\pi K$ scattering
and the scalar radius and finally the new value of $m_s/\hat m$. The LEC
that changed most at each step is put in a box.
In the final result one note significant
values for the $N_c$-suppressed constants $L_4^r,L_6^r$, albeit with large errors
and the fact the the large $N_c$-relation $2L_1^r=L_2^r$ no longer holds well.

A large number of variations on the fit were tried in \cite{newfit} by letting
$\mu$ free and varying the input used for the $C_i^r$. All of these gave
similar values for the $L_i^r$. However, a problem occurred when including
the relation between the 2 and 3-flavour LECs of \cite{GHIS}. In order for
getting this relation to work well we needed nonzero values for at least some
$N_c$-suppressed $C_i^r$. In \cite{newfit} a large effort was done to find
reasonable looking $C_i^r$ that allowed to get good fits to all of the inputs.
Many were found but there is no good ground to prefer any of these.
More work especially in trying to include lattice results is definitely needed.
For now, fit All of Tab.~\ref{tab2} and \cite{newfit} should be regarded
as the standard values for the $L_i^r$.
