---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-006-322-weak-coupling-region
section_title: "Weak coupling region"
section_number: 3.2.2
pages: 15-18
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 1.0
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
Let us now consider the region outside the curve of marginal
stability. The spectrum consists of dyons with charge $\pm \gamma_n$,
where

\begin{equation}
  \gamma_n= (n,1), \qquad n \in \IZ, 
\end{equation}

and $W$ boson with charges $\pm \gamma_e$, where

\begin{equation}
  \gamma_e=(1,0). 
\end{equation}

From (\ref{cem}) we conclude that

\begin{equation}
  c_e(\gamma_n)=-1
\end{equation}

and

\begin{equation}
  c_m(\gamma_n)=n, \qquad c_m(\gamma_e)=2, 
\end{equation}

where we used the fact that 

\begin{equation}
\Omega(\gamma_e;u)=2
\end{equation}

in the weak coupling region.

As in \cite{cdorey}, we write the equations for $\chi_e$, $\chi_m$. We
find

\begin{equation}
  \ba
  \chi_m(\zeta)&= \chi_m^{\rm sf}(\zeta) \exp\left[ -{1\over  \pi \ri}
    \CC_{\gamma_e}(\zeta) -{1\over 2 \pi \ri} \sum_{n \in \IZ} n
    \CC_{\gamma_n}(\zeta) \right],\\ 
  \chi_e(\zeta)&=\chi_e^{\rm sf}(\zeta) \exp\left[ {1\over 2 \pi \ri}
    \sum_{n \in \IZ} \CC_{\gamma_n}(\zeta) \right].  
  \ea
\end{equation}

In this region we will write

\begin{equation}
  Z_m= \ri \re^{\ri \phi_m} |Z_m|, \qquad Z_e= \re^{\ri \phi_e} |Z_e|,
  \qquad Z_{\ell}=\re^{\ri \phi_\ell} |Z_\ell|,  
\end{equation}

where we have denoted $Z_\ell= Z_{\gamma_\ell}$ the central charge of
a dyon. This is chosen in such a way that, if $u$ is real, we have
$\phi_e=\phi_m=0$.  We now define 
\begin{equation}
  \ba
  \chi_e\left( -\re^{\ri \phi_e -\theta}\right)&=
  \exp\left(-\epsilon_e (\theta-\ri \phi_e) \right)=
  \exp\left(-\widetilde \epsilon_e (\theta) \right),\\ 
  \chi_m\left( -\ri \, \re^{\ri \phi_m -\theta}\right)&=
  \exp\left(-\epsilon_m (\theta-\ri \phi_m) \right)=
  \exp\left(-\widetilde \epsilon_m (\theta) \right), \\ 
  \chi_\ell \left( - \, \re^{\ri \phi_\ell -\theta}\right)&=
  \exp\left(-\epsilon_\ell (\theta-\ri \phi_\ell) \right)=
  \exp\left(-\widetilde \epsilon_\ell (\theta) \right),   
  \ea
\end{equation}
    
We then obtain the equations,

\begin{equation}\label{eq:cTBA-2}
  \ba
  \widetilde \epsilon_e(\theta)
  &=\pi |Z_e|  \re^\theta+{1\over \pi} \int_\IR {\widetilde L_m
    (\theta') \over \cosh(\theta-\theta'+\ri \phi_m- \ri \phi_e)} \rd
  \theta' 
  + 
  {1\over \pi \ri}  \sum_{\ell \not=0} \int_\IR {\widetilde
    L_\ell(\theta') \rd \theta' \over \sinh(\theta-\theta'+\ri
    \phi_\ell- \ri \phi_e)} , \\ 
  \widetilde \epsilon_m(\theta)&=\pi |Z_m|  \re^\theta-{2\over \pi}
  \int_\IR {\widetilde L_e (\theta')\rd \theta' \over
    \cosh(\theta-\theta'+\ri \phi_e- \ri \phi_m)}-{1\over \pi}
  \sum_{\ell \in \IZ} \ell \int_\IR {\widetilde L_\ell(\theta') \rd
    \theta' \over  \cosh(\theta-\theta'+\ri \phi_\ell- \ri \phi_m)} 
  \ea
\end{equation}

where

\begin{equation}
  \widetilde L_{e,m}(\theta) = \log\left(1\mp \re^{-\widetilde
      \epsilon_{e,m}(\theta)} \right), \qquad \widetilde
  L_{\ell}(\theta) = \log\left(1+ \re^{-\widetilde
      \epsilon_{\ell}(\theta)} \right). 
\end{equation}

Here we have assumed that

\begin{equation}
  \sigma(\gamma_e)=1, 
\end{equation}

since the $W$ boson is a vector multiplet \cite{gmn2}. In the equation
for $\widetilde \epsilon_e(\theta)$ we have written down explicitly
the term corresponding to the dyon with zero electric charge
$\gamma_{\ell=0}=\gamma_m$, which is the magnetic monopole.  We can
also deduce the TBA equation for $\widetilde \epsilon_{\ell}(\theta)$,
by combining the two equations above. We find

\begin{equation}
\label{dyon-eps}
\widetilde \epsilon_\ell (\theta)=\pi |Z_\ell|  \re^\theta+{2\over \pi
  \ri} \int_\IR {\widetilde L_e (\theta')  \rd \theta' \over
  \sinh(\theta-\theta'+\ri \phi_e- \ri \phi_\ell)} +  
{1\over \pi \ri}  \sum_{k\in \IZ} (\ell-k) \int_\IR {\widetilde
  L_k(\theta') \rd \theta' \over \sinh(\theta-\theta'+\ri \phi_k- \ri
  \phi_\ell)}.  
\end{equation}

It is useful to isolate the contribution from the magnetic monopole
$k=0$ explicitly in the last term, so that we obtain

\begin{equation}
  \ba
  \label{dyon-eps2}
  \widetilde \epsilon_\ell (\theta)&=\pi |Z_\ell|  \re^\theta+{2\over
    \pi \ri} \int_\IR {\widetilde L_e (\theta')  \rd \theta' \over
    \sinh(\theta-\theta'+\ri \phi_e- \ri \phi_\ell)}  +  
  {1\over \pi \ri}  \sum_{k\not=0} (\ell-k) \int_\IR {\widetilde
    L_k(\theta')  \rd \theta'\over \sinh(\theta-\theta'+\ri \phi_k-
    \ri \phi_\ell)}\\ 
  &-{\ell \over \pi}  \int_\IR {\widetilde L_m(\theta')  \rd
    \theta'\over \cosh(\theta-\theta'+\ri \phi_m- \ri \phi_\ell)}. 
  \ea
\end{equation}

The above equations have some interesting reality properties along the
real axis, where $\phi_e=\phi_m=0$. In that case, since

\begin{equation}
  Z_\ell= \ell |Z_e| + \ri |Z_m|, 
\end{equation}

one has that

\begin{equation}
  \phi_{\ell}+ \phi_{-\ell}= \pi, \qquad \ell\in \IZ. 
\end{equation}

It is then easy to see that the conjugation property
 
\begin{equation}
  \widetilde \epsilon_{-\ell} (\theta)= \widetilde \epsilon^*_{\ell} (\theta)
\end{equation}
 
is compatible with the TBA system. In addition,
$\epsilon_{e,m}(\theta)$ are real in this case.

In the weak coupling region, we propose the following
identification with quantum periods

\begin{equation}\label{eq:TBA-dict-2}
  \begin{aligned}
    \widetilde \epsilon_m\left(x+\ri\phi_m+\frac{\ri\pi}{2}\right) =
    &\frac{1}{\hbar}s(\Pi_B)(\hbar),\\
    \widetilde \epsilon_e(x+\ri\phi_e) =
    &\frac{1}{\hbar}s(\Pi_A)(\hbar),\\
    \widetilde \epsilon_\ell(x+\ri\phi_\ell) =
    &\frac{1}{\hbar}s(\Pi_\ell)(\hbar),
  \end{aligned}
\end{equation}

with 

\begin{equation}
  \hbar = \pi^{-1}\re^{-x} , \quad \Pi_{\ell}=\ell \Pi_A+ \Pi_B \ .
\end{equation}

The TBA equations \eqref{eq:cTBA-2} then imply that the Borel
transforms of $\Pi_A(\hbar), \Pi_B(\hbar)$ have branch points at the
central charges of the BPS states whose electromagnetic charges have
non-vanishing Dirac pairing with those of the W-boson and monopole,
respectively. For $\Pi_A(\hbar)$, these are the BPS states with
charges $\pm(\ell,\pm 1), \ell=0,1,2,\ldots$; for $\Pi_B(\hbar)$,
these are the BPS states with charges
$\pm(1,0), \pm(\ell,\pm 1), \ell=1,2,\ldots$. This explains the Borel
plane plots in Figure~\ref{fg:u4-bc} with $u=4$, well in the weak
coupling region. We also superimpose in the plots the central charges
of the contributing BPS states as red spots.

In addition, the TBA equations \eqref{eq:cTBA-2} also indicate the
following discontinuities for the resummed quantum periods $s(\Pi_A)(\hbar)$,
$s(\Pi_B)(\hbar)$ in the $\hbar$-plane. The resummed quantum $A$ period
$s(\Pi_A)$ is discontinuous

\begin{itemize}
\item across the rays
$\arg(\hbar) = \phi_m\pm\frac{\pi}{2}$ with the discontinuity
\begin{equation}\label{eq:disc-A2m}
  \text{disc}_{\phi_m\pm\frac{\pi}{2}}(\Pi_A)
  = -2\hbar \log(1+\re^{-\tfrac{1}{\hbar}s(\Pi_B)(\hbar)}) \ ;
\end{equation}

\item across the rays $\arg(\hbar) = \phi_\ell(+\pi)$
with the discontinuity

\begin{equation}\label{eq:disc-A2l}
  \text{disc}_{\phi_\ell(+\pi)}(\Pi_A)
  = 2\hbar \log(1+\re^{-\tfrac{1}{\hbar}s(\Pi_\ell)(\hbar)}) \ ,\quad
  \ell\in\IZ\ .
\end{equation}
\end{itemize}

On the other hand, the quantum $B$ period $s(\Pi_B)$ is discontinuous

\begin{itemize}
\item across the rays $\arg(\hbar) = \phi_e(+\pi)$ with the discontinuity
\begin{equation}\label{eq:disc-B2e}
  \text{disc}_{\phi_e(+\pi)}(\Pi_B)
  = -4\hbar \log(1-\re^{-\tfrac{1}{\hbar}s(\Pi_A)(\hbar)}) \ ;
\end{equation}

\item across the rays $\arg(\hbar) = \phi_\ell(+\pi)$ ($\ell\neq 0$)
  with the discontinuity
  
\begin{equation}\label{eq:disc-B2l}
  \text{disc}_{\phi_\ell(+\pi)}(\Pi_B)
  = -2\ell\hbar \log(1+\re^{-\tfrac{1}{\hbar}s(\Pi_\ell)(\hbar)}) \ ,\quad
  \ell\neq 0\ .
\end{equation}

\end{itemize}

To test these formulae, we consider the case of $u=1+4\ri$, where the
branch cuts of the Borel transform of quantum $A$ and $B$ periods are well
separated, as seen in Figure~\ref{fg:ucpx-bc}. We compute the discontinuity
via lateral Borel resummation for various rays and
find good agreement with the r.h.s.\ of the formulae
\eqref{eq:disc-A2m}--\eqref{eq:disc-B2l}, see
Tables~\ref{tb:disc-Aucpx},\ref{tb:disc-Bucpx}.


\begin{figure}
  \centering
  \subfloat[$\Pi_A$]{\includegraphics[width=0.4\linewidth,valign=c]
    {qPiaucpx}} 
  \hspace{4ex}
  \subfloat[$\Pi_B$]{\includegraphics[width=0.4\linewidth,valign=c]
    {qPiaDucpx}}
  \caption{Poles of the Borel--Pad\'e transforms, which would accumulate to branch
    cuts for the Borel transform of the quantum periods $\Pi_A(E,\hbar)$ (a) and
    $\Pi_B(E,\hbar)$ (b) at $u=1+4\ri$ and $\Lambda=1$. The red points
    are the central charges of the BPS states which contribute to the
    branch points, and their electromagnetic charges are labelled
    nearby.}\label{fg:ucpx-bc}
\end{figure}


\begin{table}
  \centering
  \resizebox{\linewidth}{!}{
  \begin{tabular}{c*{2}{>{$}l<{$}}}\toprule
    BPS state & (0,-1) & (1,1)\\\midrule
    lateral Borel sum
    & 1.77819420225\times 10^{-10}-\ri 4.0146843089\times 10^{-11}
    & 5.37838410\times 10^{-13}+\ri 3.166367886\times 10^{-12}\\\midrule
    r.h.s.\ of \eqref{eq:disc-A2m},\eqref{eq:disc-A2l}
    & 1.7781942022540\times 10^{-10}-\ri 4.014684308966\times 10^{-11}
    & 5.3783841037\times 10^{-13}+\ri 3.16636788673\times
      10^{-12}
    \\\bottomrule
  \end{tabular}}
\caption{Discontinuity of $\Pi_A(u=1+4\ri,\hbar=1)$ across the rays associated to BPS states $\gamma = (0,-1), (1,1)$, computed by
  lateral Borel resummation and by using
  \eqref{eq:disc-A2m},\eqref{eq:disc-A2l} with up to 193
  terms in the asymptotic series. Only stabilised digits are listed.}
  \label{tb:disc-Aucpx}
\end{table}

\begin{table}
  \centering
  \resizebox{\linewidth}{!}{
  \begin{tabular}{c*{2}{>{$}l<{$}}}\toprule
    BPS state & (1,1) & (1,0)\\\midrule
    lateral Borel sum
    & 5.37838\times 10^{-13}+\ri 3.166367\times 10^{-12}
    & 5.979\times 10^{-16}+\ri 4.701\times 10^{-16}\\\midrule
    r.h.s.\ of \eqref{eq:disc-B2e},\eqref{eq:disc-B2l}
    & 5.3783841\times 10^{-13}+\ri 3.16636788\times 10^{-12}
    & 5.97982\times 10^{-16}+\ri 4.70119\times
      10^{-16}
    \\\bottomrule
  \end{tabular}}
\caption{Discontinuity of $\Pi_B(u=1+4\ri,\hbar=1)$ across the rays associated to BPS states $\gamma = (1,1), (1,0)$, computed by
  lateral Borel resummation and by using
  \eqref{eq:disc-B2e},\eqref{eq:disc-B2l} with up to 193
  terms in the asymptotic series. Only stabilised digits are listed.}
  \label{tb:disc-Bucpx}
\end{table}




Finally, we would like to mention that different TBA-like equations
for the quantum periods of the modified Mathieu operator have been
proposed in \cite{ito-shu-unp} and more recently in \cite{h-neitzke}.
