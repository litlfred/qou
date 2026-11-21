---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-035-the-generation-of-counter-terms
section_title: "The generation of counter terms"
section_number: null
pages: 52-54
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.943
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
Before discussing the power-counting problem and its solution, let us briefly recall the principles of the renormalization procedure which will then allow us to set up a consistent power counting. At the beginning, the Lagrangian is written down in terms of bare, i.e., unrenormalized parameters and fields. In order to illustrate the procedure let us discuss ${\cal L}_{\pi N}^{(1)}$ of Eq. ([\[4:1:2:l1pin\]](#4:1:2:l1pin){reference-type="ref" reference="4:1:2:l1pin"}) and consider the free part in combination with the $\pi N$ interaction term with the smallest number of pion fields, $${\cal L}_{\pi N}^{(1)}=\bar \Psi_B \left( i\gamma^\mu
\partial_\mu -m_B -\frac{1}{2}\frac{{\texttt{g}_A}_B}{F_B}
\gamma^\mu
\gamma_5 \partial_\mu {\phi_i}_B  \tau_i \right) \Psi_B +\cdots,
\label{4:2:1:pieceoflolagr}$$ where the subscript $B$ denotes bare quantities. The renormalization is performed by expressing all the bare parameters and bare fields of the effective Lagrangian in terms of renormalized quantities (see, e.g., Refs. [@Collins:xc], [@Weinberg:1995mt] for details). Introducing the renormalized fields through $$\label{4:2:1:renf}
\Psi=\frac{\Psi_B}{\sqrt{Z_\Psi}},\quad
\phi_i=\frac{{\phi_i}_B}{\sqrt{Z_\phi}},$$ we express the field redefinition constants $\sqrt{Z_\Psi}$ and $\sqrt{Z_\phi}$ and the bare quantities in terms of renormalized parameters: $$\begin{aligned}
Z_\Psi&=& 1+\delta Z_\Psi\left(m,\texttt{g}_A, g_i, \nu \right),\nonumber\\
Z_{\phi}&=&1+\delta Z_\phi\left(m,\texttt{g}_A, g_i, \nu \right),\nonumber \\
m_B &=&m(\nu)+\delta m\left(m,\texttt{g}_A, g_i, \nu \right),\nonumber \\
{\texttt{g}_A}_B&=&\texttt{g}_A(\nu)+\delta \texttt{g}_A\left(m,\texttt{g}_A, g_i, \nu \right),
\label{4:2:1:bare}
\end{aligned}$$ where $g_i$, $i=1,\cdots, \infty$, collectively denote all the renormalized parameters which correspond to bare parameters ${g_i}_B$ of the full effective Lagrangian of Eq. ([\[4:2:full_lagrangian\]](#4:2:full_lagrangian){reference-type="ref" reference="4:2:full_lagrangian"}). The parameter $\nu$ indicates the dependence on the choice of the renormalization condition. We emphasize that the usual choice $m(\nu)=m$, where $m$ is the nucleon pole mass in the chiral limit, is only one among an infinite number of possibilities. Substituting Eqs. ([\[4:2:1:renf\]](#4:2:1:renf){reference-type="ref" reference="4:2:1:renf"}) and ([\[4:2:1:bare\]](#4:2:1:bare){reference-type="ref" reference="4:2:1:bare"}) into Eq. ([\[4:2:1:pieceoflolagr\]](#4:2:1:pieceoflolagr){reference-type="ref" reference="4:2:1:pieceoflolagr"}), we obtain $$\label{4:2:1:bct}
{\cal L}_{\pi N}^{(1)}={\cal L}_{\rm basic}+{\cal L}_{\rm ct}+\cdots$$ with the so-called basic and counter-term Lagrangians, respectively, $$\begin{aligned}
\label{4:2:1:lbasic}
{\cal L}_{\rm basic}&=&
\bar \Psi \left( i\gamma^\mu\partial_\mu - m
-\frac{1}{2} \frac{\texttt{g}_{A}}{F}\gamma^\mu\gamma_5\partial_\mu \phi_i\tau_i\right) \Psi,\\
\label{4:2:1:lcounterterm}
{\cal L}_{\rm ct}&=&\delta Z_\Psi \bar \Psi i\gamma^\mu\partial_\mu
\Psi
-\delta\{m\}\bar{\Psi}\Psi
-\frac{1}{2}\delta\left\{\frac{\texttt{g}_{A}}{F}\right\}
\bar{\Psi}\gamma^\mu \gamma_5  \partial_\mu \phi_i  \tau_i\Psi,
\end{aligned}$$ where we introduced the abbreviations $$\begin{aligned}
\delta\{m\}&\equiv&\delta Z_\Psi m+Z_\Psi\delta m,\\
\delta\left\{\frac{\texttt{g}_{A}}{F}\right\}&\equiv&
\delta Z_\Psi \frac{\texttt{g}_{A}}{F}\sqrt{Z_\pi}
+Z_\Psi\left(\frac{{\texttt{g}_{A}}_B}{F_B}-
\frac{\texttt{g}_{A}}{F}
\right)\sqrt{Z_\phi}
+\frac{\texttt{g}_{A}}{F}(\sqrt{Z_\phi}-1).
\end{aligned}$$ In Eq. ([\[4:2:1:lbasic\]](#4:2:1:lbasic){reference-type="ref" reference="4:2:1:lbasic"}), $m$, $\texttt{g}_A$, and $F$ denote the chiral limit of the physical nucleon mass, the axial-vector coupling constant, and the pion-decay constant, respectively. Expanding the counter-term Lagrangian of Eq. ([\[4:2:1:lcounterterm\]](#4:2:1:lcounterterm){reference-type="ref" reference="4:2:1:lcounterterm"}) in powers of the renormalized coupling constants generates an infinite series. By adjusting the expansion coefficients suitably, the individual terms are responsible for the subtractions of loop diagrams. For example, the divergences occurring in dimensionally regularized one-loop calculations involving vertices of ${\cal L}_2$ are absorbed in the renormalization of the bare coefficients $L_i$ \[see Eq. ([\[3:3:1:lihi\]](#3:3:1:lihi){reference-type="ref" reference="3:3:1:lihi"})\].
