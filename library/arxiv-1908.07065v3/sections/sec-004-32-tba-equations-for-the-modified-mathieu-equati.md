---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-004-32-tba-equations-for-the-modified-mathieu-equati
section_title: "TBA equations for the modified Mathieu equation"
section_number: 3.2
pages: 10-11
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.807
latex_coverage_ratio: 1.0
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{sc:SW-TBA}

Building on \cite{oper, ims}, we expect to have a general
correspondence between the mathematical description of BPS states in \cite{gmn,gmn2}, and the ``resurgent"
properties of the quantum periods associated to the corresponding SW curve. As noted in \cite{oper}, this correspondence involves the conformal limit of the 
TBA equations of \cite{gmn}, which is given by

\begin{equation}
  R\to 0 \ , \quad \zeta \to 0\ ,\quad  \zeta/R\;\; \text{finite} \ .
\end{equation}

In this correspondence, the classical limit of the WKB periods
$\Pi_\gamma ^{(0)}$ corresponds to the central charge $Z_\gamma$,
while the full quantum period is obtained as the logarithm of the
Coulomb branch coordinates $\chi_\gamma(\zeta)$ (in the conformal
limit). The Borel singularities of the Borel transforms
$\widehat \Pi_\gamma$ are closely related to the BPS spectrum of the
theory, and the Stokes discontinuities of the quantum periods are
closely related to the so-called Kontsevich--Soibelman
symplectomorphisms \cite{ks, gmn,gmn2}. This correspondence is
summarized in Table \ref{table-cor}, and it can be used to obtain
integral equations of the TBA type governing the quantum periods. We
will now apply this correspondence to obtain such equations for the
modified Mathieu operator.

\begin{table}
\begin{center}
\begin{tabular}{|l | r|}
\hline
Resurgence & BPS states \\ \hline\hline
WKB curve &  SW curve\\ \hline
classical limit $\Pi_\gamma^{(0)}$ & central charge $Z(\gamma)$  \\ \hline
quantum period $\Pi_\gamma$ &  cluster coordinate $\log \, \chi_\gamma$ \\\hline
Borel singularities  & BPS spectrum  \\\hline
Stokes discontinuities  & KS symplectomorphisms  \\\hline
\end{tabular}
\end{center}
\caption{Correspondence between the mathematical structures in the
  resurgent approach to the WKB method, and those in the theory of BPS
  states.}
\label{table-cor}
\end{table}



Let us then consider the SW theory \cite{sw}, i.e.\ pure $\CN=2$ SYM with
gauge group $SU(2)$. We will denote the charge by 

\begin{equation}
  \bs{\gamma}=\gamma=(n_e, n_m). 
\end{equation}

We will use the conventions of \cite{cdorey} for the symplectic product, 

\begin{equation}
  \langle \gamma, \gamma'\rangle = \langle (n_e, n_m), (n'_e, n'_m)
  \rangle= -n_e n_m'+ n_m n'_e.  
\end{equation}

We will denote

\begin{equation}
  \chi_{e} (\zeta)= \chi_{(1,0)} (\zeta), \qquad  \chi_{m} (\zeta)=
  \chi_{(0,1)} (\zeta), \qquad \chi_{d} (\zeta)= \chi_{(1,1)} (\zeta),  
\end{equation}

and because of (\ref{product}) we have

\begin{equation}
  \chi_{d} (\zeta)= \chi_{e} (\zeta) \chi_{m} (\zeta).
\end{equation}
 
We will write TBA equations for $ \chi_{e} (\zeta)$ and
$ \chi_{m} (\zeta)$, as in \cite{cdorey}. We have
 
\begin{equation}
  \label{su2tba}
  \ba
  \chi_e (\zeta)&=  \chi^{\rm sf}_{e} (\zeta)\exp\left[-{1\over 2 \pi
      \ri} \sum_{\gamma'} c_e(\gamma') \CI_{\gamma'}(\zeta) \right],\\ 
  \chi_m (\zeta)&=  \chi^{\rm sf}_{m} (\zeta)\exp\left[-{1\over 2 \pi
      \ri} \sum_{\gamma'} c_m(\gamma') \CI_{\gamma'}(\zeta)\right], 
  \ea
\end{equation}
  
where
  
\begin{equation}
  \label{cem}
  c_e(\gamma)= \Omega(\gamma; u) \langle (1,0), \gamma\rangle, \qquad
  c_m(\gamma)= \Omega(\gamma; u) \langle (0,1), \gamma\rangle. 
\end{equation}
  

In order to write the integral equations, we need to know the
structure of the BPS spectrum in SW theory. It is known that there is
a curve of marginal stability ${\cal C}$ in the Coulomb branch of the
SW theory, separating a strong coupling region or chamber ${\cal S}$
inside ${\cal C}$, from a weak coupling region or chamber ${\cal W}$
outside ${\cal C}$ \cite{sw,fb,selfdual}. As we move from the strong
coupling region to the weak coupling region, the spectrum of BPS
states changes drastically by the famous wall-crossing phenomenon. We
consider the two chambers in turn.
