---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-045-111-construction
section_title: "Construction."
section_number: 11.1
pages: 94-94
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.966
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:6.1} 

\begin{para}\label{para:6.1.1} The construction of the $p$-adic period
 mapping is parallel to the complex case: one 
 attaches to a point $s\in \mathcal{M}$ representing a pair $(\Lambda,
 \rho)$ the point $\mathcal{P}(s)$ of $\mathcal{D}^\vee$ 
which parametrizes the notch $F^1$ of the Hodge filtration of the
 Dieudonn\'e module of $\Lambda$. The idea of the construction is
 already present in Grothendieck's talk
 \cite{grothendieck70:_group_barsot_tate}.
\end{para}

\begin{para}\label{para:6.1.2} More precisely, notation being as in
 \ref{para:4.1.1}--\ref{para:4.3.1}, let us consider the universal object 
 $(\udl{\Lambda},\udl{\rho})$ on the moduli formal scheme
 $\mathfrak{M}$, and the Dieudonn\'e crystal $\D(\udl{\Lambda})$. Its
 evaluation $\D(\udl{\Lambda})_{\mathfrak{M}}$ on $\mathfrak{M}$ is a
 vector bundle on $\mathfrak{M}$.
\end{para}

\begin{lem}\label{lem:6.1.3} The quasi-isogeny $\udl{\rho}$ induces a
 trivialization of the associated analytic vector bundle on
$\mathcal{M}={\mathfrak{M}}^{\mathrm{an}}_{\C_p} $:
\begin{equation*}
 (\D(\udl{\Lambda})_{\mathfrak{M}})^{\mathrm{an}}\cong
 V_p^{\C_p}\otimes_{\C_p}\mathcal{O}_\mathcal{M}
\end{equation*}


\end{lem}

\begin{proof}
 $\rho$ is a quasi-isogeny between $\udl{\Lambda}
 \times_{\mathfrak{M}}{\mathfrak{M}}_{\mathrm{red}}$ and
 $\ovl{\Lambda}\times_{\ovl{\F}_p}{\mathfrak{M}}_{\mathrm{red}}$. According to
 \ref{para:3.6.7} (i), by the rigidity of convergent isocrystals, it induces a
 canonical isomorphism $(\D(\udl{\Lambda})_{\mathfrak{M}})^{\mathrm{an}}\cong
 \bigl(\D(\ovl{\Lambda}\times_{\ovl{\F}_p}
 {\mathfrak{M}}_{\mathrm{red}})_{\mathfrak{M}}\bigr)^{\mathrm{an}}.$
 On the other hand, since the formation of $\D(\Lambda)$ commutes with
 base change (\ref{para:3.2.2}), we have
 \begin{equation*}
 \bigl(\D(\ovl{\Lambda}\times_{\ovl{\F}_p}
 {\mathfrak{M}}_{\mathrm{red}})_{\mathfrak{M}}\bigr)^{\mathrm{an}} =
 \D(\ovl{\Lambda})\otimes_W 
 \mathcal{O}_\mathcal{M}=V_p\otimes_{\Q_p}\mathcal{O}_\mathcal{M}.
 \end{equation*}
\end{proof}

\begin{para}\label{para:6.1.4}
 On the other hand, we have a locally direct summand
 $F^1=(\omega_{\udl{\Lambda}})^{\mathrm{an}}$ in
 $(\D(\udl{\Lambda})_{\mathfrak{M}})^{\mathrm{an}}\cong
 V_p\otimes_{\Q_p}\mathcal{O}_\mathcal{M}$ (\ref{para:3.3.1}). This
 determines an 
 $\mathcal{M}$-point of the flag space $\mathcal{D}^\vee$, \ie an
 analytic mapping 
 \begin{equation*}
  \mathcal{P}:\mathcal{M}\;\longrightarrow \;\mathcal{D}^\vee
 \end{equation*}

 This is called the {\it period mapping} for the moduli problem
 (decorated or not). It is clear from the construction that $\mathcal{P}$ is
 $J$-{\it equivariant}.


 If $\mathcal{M}^0$ is any connected component of $\mathcal{M}$, it is
 stable under $J'\subset J$, hence the induced period mapping
 $\mathcal{P}:\;\mathcal{M}^0\;\longrightarrow \;\mathcal{D}^\vee\;$ is
 $J'$-equivariant (the $J'$-action factors through ${J'}^{\mathrm{ad}}$).
\end{para}
