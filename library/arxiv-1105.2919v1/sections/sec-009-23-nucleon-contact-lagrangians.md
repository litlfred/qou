---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-009-23-nucleon-contact-lagrangians
section_title: "Nucleon contact Lagrangians"
section_number: 2.3
pages: 15-15
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.989
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Two-nucleon contact interactions consist of four nucleon
fields (four nucleon legs) and no meson fields.
Such terms are needed to renormalize
loop integrals, to make results reasonably independent
of regulators, and to parametrize the 
unresolved short-distance dynamics of the nuclear
force. For more on the role of contact terms,
see Section~\ref{sec_ct}.

Because of parity, nucleon contact interactions come only
in even powers of derivatives, thus,
\begin{equation}
\label{eq_LNN}
\widehat{\cal L}_{NN} =
\widehat{\cal L}^{(0)}_{NN} +
\widehat{\cal L}^{(2)}_{NN} +
\widehat{\cal L}^{(4)}_{NN} + \ldots
\end{equation}

The lowest order (or leading order) $NN$ Lagrangian has no derivatives 
and reads~\cite{Wei90,Wei91}

\begin{equation}
\label{eq_LNN0}
\widehat{\cal L}^{(0)}_{NN} =
-\frac{1}{2} C_S \bar{N} N \bar{N} N 
-\frac{1}{2} C_T (\bar{N} \vec \sigma N) \cdot (\bar{N} \vec \sigma N) \, ,
\end{equation}

where $N$ is the heavy baryon nucleon field ($\bar{N}=N^\dagger$).
$C_S$ and $C_T$ are unknown constants which are determined
by a fit to the $NN$ data.
The second order $NN$ Lagrangian can be stated as
follows~\cite{ORK96}
\begin{eqnarray}
\label{eq_LNN2}
\widehat{\cal L}^{(2)}_{NN} &=&
-C'_1 \left[(\bar{N} \vec \nabla N)^2+ (\overline{\vec \nabla N} N)^2 \right]
-C'_2 (\bar{N} \vec \nabla N)\cdot (\overline{\vec \nabla N} N)

-C'_3 \bar{N} N \left[\bar N \vec \nabla^2 N+\overline{\vec \nabla^2 N} N \right]
\nonumber \\ &&
-i C'_4 \left[
\bar N \vec \nabla N \cdot 
(\overline{\vec \nabla N} \times \vec \sigma N) +
\overline{(\vec \nabla N)} N \cdot 
(\bar N \vec \sigma \times \vec \nabla N) \right]
\nonumber \\ &&
-i C'_5 \bar N N(\overline{\vec \nabla N} \cdot \vec \sigma \times \vec \nabla N)
-i C'_6 (\bar N \vec \sigma N)\cdot (\overline{\vec \nabla N} \times \vec \nabla N)
\nonumber \\ &&
-\left(C'_7 \delta_{ik} \delta_{jl}+C'_8 \delta_{il} \delta_{kj}
+C'_9 \delta_{ij} \delta_{kl}\right)

\left[\bar N \sigma_k \partial_i N \bar N \sigma_l \partial_j N +
\overline{\partial_i N} \sigma_k N \overline{\partial_j N} \sigma_l N \right]
\nonumber \\ &&
-\left(C'_{10} \delta_{ik} \delta_{jl}+C'_{11} \delta_{il} \delta_{kj}+C'_{12} \delta_{ij} \delta_{kl}\right)
\bar N \sigma_k \partial_i N \overline{\partial_j N} \sigma_l N
\nonumber \\ &&
-\left(\frac{1}{2} C'_{13} (\delta_{ik} \delta_{jl}+
\delta_{il} \delta_{kj}) 

+C'_{14} \delta_{ij} \delta_{kl} \right)
\left[\overline{\partial_i N} \sigma_k \partial_j N + \overline{\partial_j N} \sigma_k \partial_i N\right]
\bar N \sigma_l N \, .
\end{eqnarray}
For a thorough discussion of second order contact Lagrangians, see Refs.~\cite{Epe00,Gir10}. 

Similar to $C_S$ and $C_T$ of Eq.~(\ref{eq_LNN0}), the $C'_i$ of Eq.~(\ref{eq_LNN2}) are unknown constants 
which are fixed in a fit to the $NN$ data.
Obviously, these contact Lagrangians blow up quite a bit
with increasing order, which is why we do not give
$\widehat{\cal L}^{(4)}_{NN}$
explicitly here.
The $NN$ contact potentials that emerge from these Lagrangians
are given in Section~\ref{sec_ct}.

Besides the above contact Lagrangians involving two nucleons,
there exist contact interactions among three or more nucleons
representing nuclear many-body forces 
(cf.\ last term of Eq.~(\ref{eq_LD1}), below, and Section~\ref{sec_manyNF}).
