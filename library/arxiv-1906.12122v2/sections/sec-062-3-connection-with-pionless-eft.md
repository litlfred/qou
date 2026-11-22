---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-062-3-connection-with-pionless-eft
section_title: "Connection with Pionless EFT"
section_number: 3
pages: 49-50
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 1.0
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{subsubsection:conpiless}

Experience with Pionless
EFT~\cite{Bedaque:1997qi,vanKolck:1997ut,Kaplan:1998tg,Kaplan:1998we,
Bedaque:1998mb,vanKolck:1998bw} shows that the factors associated with reducible
loops are

\begin{subalign}[eq:ConnectionPionlessPC]
 \text{potential}
 &\sim 4\pi m_N^{-1} \Mlo^{-1}\left(Q \MQCD^{-1}\right)^{\mu} \,,
 \label{potsize} \\
 \text{nucleon prop.} &\sim m_N Q^{-2} \,, \\
 \text{reducible loop int.} &\sim (4\pi m_N)^{-1} Q^5 \,,
\end{subalign}

where the factor of {$(4\pi)^{{-}1}$} is typical of integrals involving
Schr\"odinger
propagators.  One iteration of the order-$\mu$ potential adds a
reducible loop and two nucleon propagators, or $(Q/\Mlo)(Q/\MQCD)^{\mu}$.  This
is an IR enhancement of $m_N/(4\pi Q)$ over the factor that arises from
Eqs.~\eqref{props} and~\eqref{loopintegral}.  As a consequence, the
{perturbative} series in
the LO potential ($\mu=0$) fails to converge for $Q\sim \Mlo$, while subleading
potentials ($\mu\ge 1$) should be amenable to perturbation theory.

The LO chiral potential~\eqref{OPE} has the form~\eqref{potsize} if $\MNN =
\OO(\Mlo)$.  Since bound states indicate a breakdown of perturbation theory,
one expects binding energies per nucleon

\begin{equation}
 \frac{B_A}{A}\sim \frac{\MNN^2}{\MQCD}\sim \frac{f_\pi}{4\pi} \sim 10~\MeV \,,
\label{B/A}
\end{equation}

which is in the right ballpark for heavy nuclei.  Thus chiral symmetry together
with this IR enhancement provides a natural explanation~\cite{Bedaque:2002mn}
for the shallowness of nuclei compared to $\MQCD$, $B_A/A\ll \MQCD$, long
considered a mystery.

The factor of $4\pi$ in the IR enhancement was not recognized before Pionless
EFT was developed, but it has implications for the natural size of few-body
forces.  Connecting an $aN$ potential to another nucleon to make it an $(a+1)N$
potential without changing $L$ or $\Delta$ involves an additional factor $4\pi
m_N^{-1} \Mlo^{-2}$ from the extra $2N$ interaction and the extra nucleon
propagator inside the $aN$ potential.  At the same time, it adds a reducible
loop and one nucleon propagator at the amplitude level, resulting in an overall
suppression by $Q/m_N$.  For $m_N=\OO(\MQCD)$---as dictated by NDA for
{$A=1$}, where it works well---this is the $n=1$ suppression of
\textcite{Friar:1996zw}.  In contrast, missing the $4\pi$ in the IR enhancement
would require $Q/m_N\sim Q^2/\MQCD^2$, as found in Sec.~\ref{subsubsec:nukepot}
for $n=2$~\cite{Weinberg:1991um,Ordonez:1992xp,Weinberg:1992yk,VanKolck:1993ee}.
Thus, counting factors of $4\pi$ in reducible loops leads to Friar's power
counting{, which, however, has not been widely tested so far.}
