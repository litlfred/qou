---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-037-512-next-to-next-to-leading-order
section_title: "Next-to-next-to-leading order"
section_number: 5.1.2
pages: 51-52
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The power $\nu=3$ (NNLO) is obtained when
there are no loops ($L=0$) and 
$\sum_i \Delta_i = 1$, i.e., 
$\Delta_i=1$ for one vertex 
while $\Delta_i=0$ for all other vertices.
There are three topologies which fulfill this condition,
known as the two-pion exchange (2PE), 1PE,
and contact graphs~\cite{Kol94,Epe02b}
(Fig.~\ref{fig_3nf_nnlo}).

Using the subleading vertices Eqs.~(\ref{eq_V2_3}) and (\ref{eq_V2_4}),
it  is straightforward to derive the 2PE 3N-potential to be
\begin{equation}
V^{\rm 3NF}_{\rm 2PE} = 
\left( \frac{g_A}{2f_\pi} \right)^2
\frac12 
\sum_{i \neq j \neq k}
\frac{
( \vec \sigma_i \cdot \vec q_i ) 
( \vec \sigma_j \cdot \vec q_j ) }{
( q^2_i + m^2_\pi )
( q^2_j + m^2_\pi ) } \;
F^{ab}_{ijk} \;
\tau^a_i \tau^b_j
\label{eq_3nf_nnloa}
\end{equation}
with $\vec q_i \equiv \vec{p_i}' - \vec p_i$, 
where 
$\vec p_i$ and $\vec{p_i}'$ are the initial
and final momenta of nucleon $i$, respectively, and
\begin{equation}
F^{ab}_{ijk} = \delta^{ab}
\left[ - \frac{4c_1 m^2_\pi}{f^2_\pi}
+ \frac{2c_3}{f^2_\pi} \; \vec q_i \cdot \vec q_j \right]
+ 
\frac{c_4}{f^2_\pi}  
\sum_{c} 
\epsilon^{abc} \;
\tau^c_k \; \vec \sigma_k \cdot [ \vec q_i \times \vec q_j] \; .
\label{eq_3nf_nnlob}
\end{equation}  
There are great similarities between this force and earlier derivations of
2PE 3NFs, notably the 50-year old Fujita-Miyazawa~\cite{FM57},
the Tucson-Melbourne (TM)~\cite{Coo79}, and the Brazil~\cite{CDR83}
forces. A thorough comparison between various 2PE 3NFs is conducted in
Ref.~\cite{FHK99} resulting in the recommendation to drop the so-called
``c-term'' from the TM force, since it does not have an equivalent in the
ChPT derived force, Eqs.~(\ref{eq_3nf_nnloa}), (\ref{eq_3nf_nnlob}), giving rise
to the construction of the TM' (or TM99) force~\cite{CH01}.


\begin{figure}[t]\centering
\vspace*{-4.0cm}

\scalebox{0.55}{\includegraphics{diag_3nf_nnlo.pdf}}
\vspace*{-10.0cm}
\caption{The three-nucleon force at NNLO.
From left to right: 2PE, 1PE, and contact diagrams.
Notation as in Fig.~\ref{fig_hi}.}
\label{fig_3nf_nnlo}
\end{figure}

Notice that Eq.~(\ref{eq_3nf_nnlob}) does not include a $c_2$-term.
Due to two time-derivatives, the contribution from the $c_2$ vertex is $(Q/M_N)^2$ suppressed and
demoted by two orders. Note also that
the 2PE 3NF does not contain any new parameters,
because the LECs $c_1$, $c_3$, and $c_4$ appear already  in the 2PE 2NF (Section~\ref{sec_NNLO}) and
are fixed by $\pi N$ and/or $NN$ data.

The other two 3NF contributions shown in Fig.~\ref{fig_3nf_nnlo}
are easily derived by taking the last two terms of the $\Delta=1$ Lagrangian, Eq.~(\ref{eq_LD1}),
into account. The 1PE contribution is
\begin{equation}
V^{\rm 3NF}_{\rm 1PE} = 
-D \; \frac{g_A}{8f^2_\pi} 
\sum_{i \neq j \neq k}
\frac{\vec \sigma_j \cdot \vec q_j}{
 q^2_j + m^2_\pi }
( \mbox{\boldmath $\tau$}_i \cdot \mbox{\boldmath $\tau$}_j ) 
( \vec \sigma_i \cdot \vec q_j ) 
\label{eq_3nf_nnloc}
\end{equation}
and the 3N contact potential reads
\begin{equation}
V^{\rm 3NF}_{\rm ct} = E \; \frac12
\sum_{j \neq k} 
 \mbox{\boldmath $\tau$}_j \cdot \mbox{\boldmath $\tau$}_k  \; .
\label{eq_3nf_nnlod}
\end{equation}
These 3NF terms involve the two new parameters $D$ and $E$, 
which do not appear in the 2N problem.
There are many ways to pin these two parameters down.
In Ref.~\cite{Epe02b},
the triton binding energy and the $nd$ doublet scattering
length $^2a_{nd}$ were used.
One may also choose the binding
energies of $^3$H and $^4$He~\cite{Nog06} or
an optimal over-all fit of the properties of light nuclei~\cite{Nav07}.
Exploiting the consistency of interactions and currents in ChPT~\cite{GP06},
the parameter $D$ of the $\pi NNNN$ vertex involved in the
1PE 3NF can be constrained by $p$-wave pion-production data~\cite{HKM00}
or electro-weak processes like the tritium $\beta$-decay~\cite{GQN09}
or proton-proton fusion ($p\,p \rightarrow d \, e^+ \, \nu_e$)~\cite{Nak08}.
Once $D$ and $E$ are fixed, the results for other
3N, 4N, etc.\  observables are predictions.

The 3NF at NNLO has been applied in
calculations of few-nucleon 
reactions~\cite{Epe02b,Erm05,Kis05,Wit06,Ley06,Ste07,KE07,Mar09,Kie10,Viv10},
structure of light- and medium-mass 
nuclei~\cite{Nog06,Nav07,Hag07,Ots09},
and nuclear and neutron matter~\cite{Bog05,HS09}
with a good deal of success.
Yet, the famous `$A_y$ puzzle' of nucleon-deuteron scattering
is not resolved~\cite{Epe02b,KE07}.
When only 2NFs are applied,
the analyzing power in $p$-$^3$He scattering
is even more underpredicted than in $p$-$d$~\cite{Fis06,DF07}. 
However, when the
NNLO 3NF is added, the $p$-$^3$He $A_y$ substantially 
improves (more than in $p$-$d$)~\cite{Viv10}---but a discrepancy remains.
Furthermore, the spectra of light nuclei leave room for improvement~\cite{Nav07}.

We note that there are further 3NF contributions at NNLO, namely, the
$1/M_N$ corrections of the NLO 3NF diagrams (Fig.~\ref{fig_3nf_nlo}). Some of these terms involve
the vertices Eqs.~(\ref{eq_V2_1}) and (\ref{eq_V2_2}), and the $1/M_N$
correction of the $c_4$ vertex, Eq.~(\ref{eq_V2_4}); others are due to higher order recoil corrections.
Several of those contributions
have been calculated by Coon and Friar in 1986~\cite{CF86}.
These corrections are believed to be very small.

To summarize, the 3NF at NNLO is a remarkable contribution: It represents the leading many-body force
within the scheme of ChPT; it includes terms that were advocated already some 50 years ago; and it
produces noticeable improvements in few-nucleon reactions and the structure of
light nuclei.
But unresolved problems remain. Moreover, in the case of the
2NF, we have seen that one has to proceed to N$^3$LO to achieve sufficient accuracy.
Therefore, the 3NF at N$^3$LO is needed for at least two reasons: 
for consistency with the 2NF and to hopefully resolve outstanding problems in microscopic structure
and reactions.


\begin{figure}[t]\centering
\vspace*{-0.5cm}

\scalebox{1.0}{\includegraphics{diag_3nf_n3lo.pdf}}
\vspace*{-0.75cm}
\caption{Leading one-loop 3NF diagrams at N$^3$LO.
We show one representative example for each of five topologies,
which are: (a) 2PE, (b) 1PE-2PE, (c) ring, (d) contact-1PE, (e) contact-2PE.
Notation as in Fig.~\ref{fig_hi}.}
\label{fig_3nf_n3lo}
\end{figure}
