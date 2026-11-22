---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-046-112-properties
section_title: "Properties."
section_number: 11.2
pages: 94-95
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.984
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:6.2}  

\begin{thm}\label{thm:6.2.1} The period mapping $\mathcal{P}$ is etale. Its image lies in the period domain $\mathcal{D}$. 


\end{thm}
The first assertion reduces, via an infinitesimal criterion of
etaleness, to the ``essential surjectivity part'' of the
Grothendieck-Messing theorem (\ref{thm:3.3.3}), in the case of an ideal
of square zero, \cf \cite[5.17]{psfpg}.  It corresponds to what is called
the ``local Torelli property'' in the complex case.


The second assertion is a
consequence of a theorem of B. Totaro on the equivalence of semi-stability and ``weak admissibility'' \cite{tpipht}.
The second assertion may be viewed as a
$p$-adic analogue of the ``Riemann relations'' (\ref{para:1.1.3}).

\begin{cor}\label{cor:6.2.2} $\mathcal{M}$ is smooth, and any component
 $\mathcal{M}^0$ is a connected $p$-adic manifold in the sense of
 I.\ref{para:p-adic-manifold}.
\end{cor}
\begin{para}\label{para:6.2.3}
 It is very likely that $\mathcal{P}$, viewed as a mapping
 $\mathcal{M}\rightarrow \mathcal{D}$, is surjective.  This is closely
 related to Fontaine's conjecture on the realizability of filtered
 Dieudonn\'e modules by $p$-divisible groups. Although recent work by
 C. Breuil \cite{breuil99:_repres}, \cite{breuil00:_group} settles the
 Fontaine conjecture at least for 
 finite residue fields of characteristic $\neq 2$ (and in other cases),
 it is not clear to the author to which extent the surjectivity
 conjecture is now established.


 On the other hand, the fibers of the period mapping are relatively
 well-understood, \cf \cite[5.37]{psfpg}. 
\end{para}

\begin{para}\label{para:6.2.4}
 The argument in the proof of \ref{lem:6.1.3} shows a little more. Recall from
 \ref{para:3.6.7} (ii) that the analytic vector bundle
 $(\D(\udl{\Lambda})_{\mathfrak{M}})^{\mathrm{an}}$ on $\mathcal{M}$ comes
 together with an integrable connection $\nabla_{\mathrm{GM}}$ (the Gauss-Manin
 connection).
\end{para}

 \begin{lem}\label{lem:6.2.5} The trivialization 
  \begin{equation*}
   (\D(\udl{\Lambda})_{\mathfrak{M}})^{\mathrm{an}}\cong
   V_p^{\C_p}\otimes_{\C_p}\mathcal{O}_\mathcal{M}
  \end{equation*}
  of \ref{lem:6.1.3} induces a trivialization of the Gauss-Manin connection:  
  \begin{equation*}
   \bigl(
    (\D(\udl{\Lambda})_{\mathfrak{M}})^{\mathrm{an}}
    \bigr)^{\nabla_{\mathrm{GM}}} 
    \cong V_p^{\C_p}.
  \end{equation*}

  The point is that the convergent isocrystal
  $\D(\Lambda\times_{\mathfrak{M}}{\mathfrak{M}}_{\mathrm{red}})$ is constant, 
  since it comes by base change, from $\D(\ovl{\Lambda})_\Q$.
 \end{lem}
 This useful lemma will allow us to give explicit expression of the
 period mapping in terms of quotients of solutions of differential
 equations, as in the complex case.
