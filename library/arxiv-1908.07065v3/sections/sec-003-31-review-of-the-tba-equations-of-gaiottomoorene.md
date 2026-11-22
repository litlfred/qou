---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-003-31-review-of-the-tba-equations-of-gaiottomoorene
section_title: "Review of the TBA equations of Gaiotto–Moore–Neitzke"
section_number: 3.1
pages: 9-10
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
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
