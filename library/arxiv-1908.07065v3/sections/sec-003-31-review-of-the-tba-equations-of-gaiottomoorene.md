---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-003-31-review-of-the-tba-equations-of-gaiottomoorene
section_title: "Review of the TBA equations of Gaiotto–Moore–Neitzke"
section_number: 3.1
pages: 9-11
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 1.0
---
The TBA equations we will obtain are conformal limits \cite{oper} of
the integral equations proposed by Gaiotto--Moore--Neitzke (GMN) in
\cite{gmn} to describe the hyperK\"ahler metric on the Coulomb branch
of $\CN=2$ theories compactified on $\IR^3 \times \IS^1_R$, where $R$
is the compactification radius. We will now review some basic aspects
of these equations which will be useful in the following.  The basic
ingredients in these equations are the central charges of the $\CN=2$
supersymmetric gauge theory
 
\begin{equation}
  Z(\bs{u})=\left(\bs{a},  \bs{a}_D \right), 
\end{equation}

where

\begin{equation}
  \bs{a}_D={\partial F_0 \over \partial \bs{a}}. 
\end{equation}

 
We define the period associated to a vector
$\bs{\gamma}\in\Gamma$ in the lattice of electromagnetic charges as


\begin{equation}
  Z_{\bs{\gamma}}= Z(\bs{u}) \cdot {\boldsymbol{\gamma}}.
\end{equation}

This is just a linear combination of $A$ periods and $B$ periods. 

To such a central charge we associate a ray

\begin{equation}
  \ell_{\bs{\gamma}}= \left\{ \zeta: {Z_{\bs{\gamma}}(\bs{u}) \over
      \zeta} \in \IR_-\right\}.  
\end{equation}







The {\it semiflat coordinate} on the Coulomb branch is given by

\begin{equation}
\chi_{\bs{\gamma}}^{\rm sf}(\zeta)= \exp\left[ \pi R \zeta^{-1}
  Z_{\bs{\gamma}} + \ri \theta_{\bs{\gamma}} + \pi R \overline \zeta
  Z_{\bs{\gamma}} \right],  
\end{equation}

where $R$ is the compactification radius, and 

\begin{equation}
 \theta_{\bs{\gamma}}= \boldsymbol{\theta} \cdot {\bs{\gamma}}
 \end{equation}
 
 is the angular coordinate on the fiber.  The semiflat coordinate is
 the ``uncorrected" or ``classical" coordinate, and it is corrected by
 exponentially small effects in the large $R$ limit. These
 effects are encoded in a non-linear, TBA-like integral equation,
 which reads as

\begin{equation}
\label{tba-equation}
\chi_{\bs{\gamma}}(\zeta)=\chi_{\bs{\gamma}}^{\rm sf}(\zeta)\exp\left[
  -{1\over2 \pi \ri} \sum_{\bs{\gamma}' \in \Gamma}  
\Omega(\bs{\gamma}'; \bs{u}) \langle \bs{\gamma}, \bs{\gamma}'\rangle
\CI_{\bs{\gamma}'} (\zeta) \right],  
\end{equation}

where $\Omega(\gamma;u)$ is the number of BPS states with
electromagnetic charge $\gamma$ at the point $u$ of the Coulomb branch, and

\begin{equation}
  \CI_{\bs{\gamma}}= \int_{\ell_{\bs{\gamma}}} {\rd \zeta' \over
    \zeta'} {\zeta '+\zeta \over \zeta'- \zeta} \log\left(1-
    \sigma(\bs{\gamma}) \chi_{\bs{\gamma}} (\zeta') \right).  
\end{equation}

Here, $\sigma(\bs{\gamma})$ is the quadratic refinement. It has been
argued in \cite{gmn2} that, for BPS hypermultiplets/vectormultiplets,
one has, respectively,

\begin{equation}
  \sigma(\bs{\gamma})=\mp 1. 
\end{equation}












We have used the normalization of \cite{cdorey}, which is more
appropriate for our normalization of charges/periods. An important
feature of \eqref{tba-equation} is that only those states whose charge
$\bs{\gamma'}$ has a non-vanishing Dirac pairing with $\bs{\gamma}$
contributes to the equation of $\chi_{\bs{\gamma}}(\zeta)$.  The
quantities $\chi_{\bs{\gamma}}(\zeta)$ characterize in a precise way
the hyperK\"ahler metric of the moduli space of the $\CN=2$ theory
compactified on $\IR^3 \times \IS^1_R$, and they can be realized as
cluster coordinates on this moduli space \cite{gmn2}. They satisfy the
property

\begin{equation}
  \label{product}
  \chi_{\bs{\gamma}+\bs{\gamma}'}(\zeta) =
  \chi_{\bs{\gamma}}(\zeta)\chi_{\bs{\gamma}'}(\zeta). 
\end{equation}

 
Very often we have both charges $\pm \bs{\gamma}$ appearing in the sum
in the r.h.s. of (\ref{tba-equation}). If $\theta_{\bs{\gamma}}=0$, we
have an extra symmetry \cite{oper},

\begin{equation}
\label{sym}
\chi_{\bs{\gamma}}(\zeta)=\chi_{-\bs{\gamma}}(-\zeta), 
\end{equation}

and we can combine
 
 \begin{equation}
   \ba
   \label{cintegral}
   \CC_{\bs{\gamma}}= \CI_{\bs{\gamma}} -\CI_{-\bs{\gamma}}
   &=
   \int_{\ell_{\bs{\gamma}}} {\rd \zeta' \over \zeta'} {\zeta '+\zeta
     \over \zeta'- \zeta} \log\left(1- \sigma(\bs{\gamma})
     \chi_{\bs{\gamma}} (\zeta') \right)-
   \int_{\ell_{-\bs{\gamma}}} {\rd \zeta' \over \zeta'} {\zeta '+\zeta
     \over \zeta'- \zeta} \log\left(1- \sigma(-\bs{\gamma})
     \chi_{-\bs{\gamma}} (\zeta') \right)\\
   &= \int_{\ell_{\bs{\gamma}}} {\rd \zeta' \over \zeta'} \left(
     {\zeta '+\zeta \over \zeta'- \zeta}-{\zeta '-\zeta \over \zeta'+
       \zeta} \right) \log\left(1- \sigma(\bs{\gamma})
     \chi_{\bs{\gamma}} (\zeta') \right)\\
   &=4 \zeta  \int_{\ell_{\bs{\gamma}}} {\rd \zeta' \over \left(
       \zeta' \right)^2-\zeta^2} \log\left(1- \sigma(\bs{\gamma})
     \chi_{\bs{\gamma}} (\zeta') \right).  
   \ea 
\end{equation}
 
In going from the first to the second line we have changed variables
$\zeta'\rightarrow -\zeta'$, and we used the symmetry (\ref{sym}).
 
In order to put the equations in a form similar to the TBA equations,
we will perform a change of variables akin to the one made in
\cite{gmn}. If
 
\begin{equation}
  Z_{\bs{\gamma}}= \re^{\ri \phi'} \left|  Z_{\bs{\gamma}} \right|
\end{equation}
 
then we change variables in (\ref{cintegral}) as follows:
 
\begin{equation}
  \zeta= -\re^{\ri \phi -\theta}, \qquad \zeta'=  -\re^{\ri \phi' -\theta'}, 
\end{equation}
 
and we obtain
 
\begin{equation}
  \CC_{\bs{\gamma}}= 2\int_\IR { \log\left(1- \sigma(\bs{\gamma})
      \chi_{\bs{\gamma}} (\theta') \right) \over \sinh(
    \theta-\theta'+ \ri \phi'-\ri \phi)} \rd \theta'.  
\end{equation}
 


\subsection{TBA equations for the modified Mathieu equation}
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
