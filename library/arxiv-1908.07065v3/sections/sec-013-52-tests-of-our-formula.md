---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-013-52-tests-of-our-formula
section_title: "Tests of our formula"
section_number: 5.2
pages: 31-36
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.912
latex_coverage_ratio: 0.996
---
We will now test the expression (\ref{sd}) in several ways. 

A first simple test is that the zeros of $\Xi(E)$ give the correct spectrum of the modified Mathieu operator. This should be expected 
from the general results of \cite{gm3}, but it is instructive to check it explicitly. 
The zeros correspond to the vanishing of the $\cosh$ in (\ref{sd}), and by using 
(\ref{abpe}) we find,

\be 
\label{eqref} \partial_{a}F_{\rm NS}(a,\hbar)= \hbar  \pi  \left( n+{1\over 2} \right), 
\ee

which is the exact quantization condition obtained from the conjecture in \cite{ns}, subsequently proved in \cite{kt2}. 

 
 Another check can be obtained by comparing our expression to the asymptotics of Fredholm determinants obtained in \cite{voros,voros-zq,voros-quartic} 
 by using the all-orders WKB method. This asymptotic expansion is valid when $E<0$, where the Fredholm determinant is not oscillatory. In order to write down 
 the asymptotics, we need some ingredients. Let 

\be
G(E) =\sum_{n =0}^\infty {1\over E-E_n}
\ee

be the trace of the resolvent, and 

\be
T(E)=  {1\over 2} \int_\IR {\rd x \over {\sqrt{2\Lambda^2 \cosh(x)-E}}} 
\ee

the transit time. We also need the formal power series in $\hbar$ 

\be
\label{aewkb}
b(E) =  \exp \left\{  \ri \sum_{n\ge 1} \hbar^{2n-1} \int_\IR p_{2n} (x, E) \rd x \right\}, 
\ee

where the functions $p_{2n}(x,E)$ are the ones appearing in the solution to the all-orders WKB method in \eqref{ricwkb}. 
Let us now define $\kappa=-E$, which will be taken to be positive. It is convenient to introduce the functions

\be
\widetilde G(\kappa)= G(-\kappa), \qquad \widetilde \Xi(\kappa)= \Xi(-\kappa), \qquad \widetilde b(\kappa) =b(-\kappa), \qquad \widetilde T(\kappa)= T(-\kappa).
\ee

Then, one has the following small $\hbar$ asymptotics,  
 
 \be
 \label{xi-as}
\widetilde \Xi(\kappa)\sim  \widetilde b(\kappa) \exp\left\{ {1\over \hbar} \int_0^\kappa \widetilde T(\kappa') \rd \kappa' - \int_0^\infty  \left( \widetilde G(\kappa') +{1\over \hbar} \widetilde T(\kappa') \right) \rd \kappa' \right\}.   
 \ee
 
The second term in the exponent is independent of $\kappa$ but depends on $\hbar$. We note that all the integrals involved in this expression are well 
defined precisely because 
$E$ is negative. The very first terms in the asymptotics can be easily worked out, and one finds\footnote{This agrees with an unpublished calculation of 
Y. Hatsuda, who obtained the same result by considering the semiclassical expansion of the spectral traces.} 

\be
\label{wkb-sd}
\log\Xi(-\kappa) \sim - {\ri \over 2 \hbar} \Pi_B^{(0)}(\kappa)+{\ri \hbar \over 2}\Pi_B^{(1)}(\kappa)+ \cdots,  \qquad \kappa>0, 
\ee

up to $\kappa$-independent terms. Note that the sign in the subleading correction is the opposite one to what one finds in the WKB expansion of the quantum $B$ period. 

 Let us now compare this result to the exact expression for the spectral determinant \eqref{sd}, which can be written as
 
 \be
 \label{alt-sd}
 \Xi(E)=A (\hbar) \left( \sinh\left(\frac{\pi a}{\hbar }\right) \right)^{-1} \cos\left( {1\over \hbar} {\partial F_{\rm NS} \over \partial a} \right).\
 \ee
 
From the explicit expression (\ref{aseries}) it is easy to see that,
when $E$ is negative, $a$ is purely imaginary. More precisely, one has


\be
\label{aminus}
a(-\kappa, \hbar)= \ri \alpha, \qquad \alpha= a(\kappa, \ri\hbar),  
\ee

and we take $\alpha>0$ for definiteness. In addition,

\be
\label{fminus}
\partial_a F^{\rm inst} _{\rm NS} (a, \hbar)= \ri \partial_\alpha F^{\rm inst}_{\rm NS} (\alpha, \ri\hbar).  
\ee

By using the explicit expression (\ref{gammadef}) and standard
identities for the $\Gamma$ function, we find

\be
\ba
{\Xi(-\kappa)\over A(\hbar)}&={1\over 2 \pi} \Gamma\left( 1+{\alpha \over \hbar} \right)  \Gamma\left( {\alpha \over \hbar} \right) \exp \left[ {\alpha \over \hbar} \log\left( {\hbar^2 \over \Lambda^2} \right) + {1\over \hbar} \partial_\alpha F^{\rm inst}_{\rm NS} (\alpha, \ri\hbar) \right]
\\& +{1\over 2 \pi} \Gamma\left(1-{\alpha \over \hbar} \right)  \Gamma\left(-{\alpha \over \hbar} \right) \exp \left[ -{\alpha \over \hbar} \log\left( {\hbar^2 \over \Lambda^2} \right) - {1\over \hbar} \partial_\alpha F^{\rm inst}_{\rm NS} (\alpha, \ri\hbar) \right]. 
\ea
\ee

The term in the second line gives an exponentially small correction to
the leading asymptotics. The small $\hbar$ asymptotics of the quantity
in the first line is given by 

\be
\ba
&\log \left[ {1\over 2 \pi} \Gamma\left( 1+{\alpha \over \hbar} \right)  \Gamma\left( {\alpha \over \hbar} \right) \right]+ {\alpha \over \hbar} \log\left( {\hbar^2 \over \Lambda^2} \right) + {1\over \hbar} \partial_\alpha F^{\rm inst}_{\rm NS} (\alpha, \ri\hbar) 
\\&\sim  -{\ri \over 2 \hbar} \sum_{n \ge 0} (-1)^n \Pi_B ^{(n)}(\kappa) \hbar^{2n}.  
\ea
\ee

We have used that, due to (\ref{aminus}) and (\ref{fminus}), the
quantum period is evaluated at $-E$, where $E=-\kappa<0$, and we have
to change  $\hbar\rightarrow \ri\hbar$. The result is in agreement with
the WKB asymptotics obtained in (\ref{wkb-sd}).


A more precise test of (\ref{sd}) can be made by comparing the analytical formulae for the spectral traces with numerical results. These are obtained 
by calculating the spectrum of $\mH$ with standard techniques. An example of such a comparison is shown in Table \ref{tbx1}. 
\begin{table}[h!] 
\centering
   \begin{tabular}{l l l}
  \\
 $N_b$& $Z_2$  \\
\hline

2 &  \underline{0.004794786}11468342466\\

 4 & \underline{0.004794786073913}81196\\ 

 6 &                 0.00479478607391375025           \\  
 \hline
Num &  0.00479478607391375025    \\
\end{tabular}    \\
\caption{ The second spectral trace $Z_2$ as computed from  \eqref{tr2} for $\hbar=3\pi$ and $\Lambda=1$. The number $N_b$ means that we truncate the series \eqref{inst}  at order $\Lambda^{4 N_b}$. The last line gives the numerical result obtained from the spectrum of $\mH$. }
   \label{tbx1}
 
 
 \end{table}

We finally note that $\Xi(E)$ is an entire function of $E$. In particular, the would-be singularities due to the denominator of (\ref{alt-sd}) or to 
the Gamma functions in (\ref{gammadef}) must cancel in the end. This leads in turn to constraints on the form of the singularities of $F_{\rm NS}^{\rm inst}$, 
which might be testable against the results in \cite{gorsky-bands} (see also \cite{beccaria}). 


\subsection{Comparison to Zamolodchikov's TBA equation}

\label{comp-zamo}
An additional test of our formula (\ref{sd}) comes from a comparison
with \cite{post-zamo}.  Inspired by the ODE/IM correspondence
\cite{dt,ddt}, Zamolodchikov found in \cite{post-zamo} a TBA equation
which computes precisely the spectral determinant \eqref{sd}. Let us
state the main result of \cite{post-zamo}, referring to Appendix
\ref{appendixzamo} for more details. Let $\epsilon(\theta, P)$ be a
solution of the TBA equation \eqref{eq:cTBA-0} but with the boundary
condition at $\theta \rightarrow -\infty$ given by

\begin{equation}
  \label{zamobc}\epsilon (\theta,P) \sim 8 P \theta-2C(P), \qquad \theta \to
   -\infty, \quad P>0,
 \end{equation}
 
where $C(P)$ is written down in (\ref{CP}). 
Let us now introduce the function 

\be X(\mu, P)=\exp\left[-\epsilon(\theta, P)/2\right], 
\ee

where $\mu$ is related to $\theta$ by

\be
\label{mutheta}
\mu=  \re^{2 \theta}\left(\frac{\Gamma \left(\frac{1}{4}\right)^2}{16 \sqrt{\pi }}\right)^2. 
\ee

Then, according to \cite{post-zamo}, the spectral determinant of the modified Mathieu operator (\ref{eq:schrodinger}) is given by 
\be  
\Xi (E)= {X(\mu, P) \over X(\mu, 0)},
\ee

where the parameters $\Lambda$, $E$ and $\hbar$ of the operator are related to the parameters appearing in $X(\mu, P)$ by

\be \label{diczo} \mu=  \Lambda^2 \hbar^{-2}, \qquad P^2 =-E \hbar^{-2}.
 \ee 

   If we compare the result of \cite{post-zamo} with ours we should have (by using the dictionary \eqref{diczo}) 
   
 \be {X(\mu, P) \over X(\mu, 0)}=A (\hbar)\left( \sinh\left(\frac{ \Pi_A^{\rm ex}(E, \hbar)}{2 \hbar }\right) \right)^{-1} \cosh\left({1 \over 2\hbar} \Pi_B^{\rm ex}(E, \hbar)\right). 
 \ee
 
 In order to find the relation between the two normalization constants
 $X(\mu, 0)$ and $A (\hbar)$, it is useful to first derive the
 asymptotic behavior \eqref{zamobc} from our expression \eqref{sd}. We
 need to expand around small $\Lambda \hbar^{-1}$ and take $u<0$,
 which means that $a$ is imaginary, as discussed in (\ref{aminus}). In
 this regime, and by using \eqref{abpe}, we have
 
 \be 
 \ba
 &\label{asy} \left( \sinh\left(\frac{\pi a}{\hbar }\right) \right)^{-1} \cosh \left({\ri \over \hbar}\partial_{a}F_{\rm NS}(a, \hbar)\right)\\
 & \approx  2^{-1}\pi^{-1}\left(\left({\Lambda\over\hbar}\right)^{-2s }\Gamma(1+s)\Gamma(s)+\left({\Lambda\over\hbar}\right)^{2s }\Gamma(1-s)\Gamma(-s)\right),
 \ea
 \ee
 
 where 
 
 \be s=-\ri {a \over \hbar} = \frac{\alpha}{\hbar} > 0.
 \ee
 
By using \eqref{mmap} we have 

\be 
E \approx a^2/4 
\ee

and therefore 

 
 
 \be P =s/2 >0.
 \ee
Hence we can neglect the second term in the r.h.s. of \eqref{asy}. It follows from \eqref{diczo} that \eqref{asy} agrees precisely with \eqref{zamobc}. 
In particular this means that the two normalization constants are identified and we have

\be \label{IDtest} X(\mu, P)= \left( \sinh\left(\frac{ \Pi_A^{\rm ex}(E, \hbar)}{2 \hbar }\right) \right)^{-1} \cosh\left({1 \over 2\hbar} \Pi_B^{\rm ex}(E, \hbar)\right). 
  \ee
  
We test this equality by solving numerically the TBA equation \eqref{eq:cTBA-0} with the boundary condition \eqref{zamobc}. 
Some results  are given in Table \ref{TestTBA1}. We find perfect agreement. 


 \begin{table}[h!] 
\centering
   \begin{tabular}{l l l}
  \\
 $N_b$& $\log\left(\left( \sinh\left(\frac{\pi a}{\hbar }\right) \right)^{-1} \cosh\left({\ri \over \hbar}\partial_{a}F_{\rm NS}(a, \hbar)\right)\right)$  \\
\hline
 
 2 &\underline{11.360025}317439438\\
 
 4 &\underline{11.36002529911}2863\\ 

  6&11.360025299117259\\  
 \hline
TBA &  11.360025299117    \\
\end{tabular}    \\
\caption{ The un-normalized spectral determinant as computed 
by using instanton counting and 
by solving numerically  the TBA \eqref{eq:cTBA-0} with \eqref{zamobc}.  We use $P^2=-E=5$, $\mu=\Lambda^2=\left(\Gamma \left(1/4\right)^2/(16 \sqrt{\pi })\right)^2$, and $\hbar=1$. The number $N_b$ means that we truncate the series \eqref{inst}  at order $\Lambda^{4 N_b}$. }
 \label{TestTBA1}
 
 
 \end{table}
   

 An important spinoff of this comparison is that our result (\ref{sd})
 provides an analytic, closed form solution to the TBA equation of
 \cite{post-zamo}. This also has the following consequence.  When we
 derived the Fredholm determinant from the topological string
 perspective, and due to our regularization procedure, we generated an
 integration constant $A(\hbar)$ whose explicit expression is given in
 \eqref{ainst}.  Given the identity \eqref{IDtest} between our
 Fredholm determinant and the solution to the Zamolodchikov's TBA, we
 expect $A(\hbar)$ to be computed by the integral equation \eqref{eq:cTBA-0} at
 $P=u=0$.  More precisely we expect

\be \label{ccc} 2 \log A(\hbar) = \epsilon(\theta, P=0),
\ee

where we used the dictionary \eqref{diczo}.  For $P=0$ the asymptotic
condition \eqref{zamobc} does not make sense, strictly speaking.
Nevertheless, we can derive the appropriate asymptotic condition for
the TBA at $P=0$ by using our analytic expression \eqref{IDtest}.  We
find that, as $\theta \rightarrow -\infty$,





\begin{equation}\label{eps0}
  \epsilon(\theta, P=0) 
  \sim -2 \log \left(
    -\frac{2 (\theta +\gamma_{\rm Euler} )-\log \pi+4 \log\Gamma(5/4)}{\pi}
  \right).
\end{equation}

 This is precisely the boundary condition used in section~\ref{tbau0}, equation \eqref{eq:bdy-cor}. 
 One can now check \eqref{ccc} numerically.
  For instance, by solving the TBA of  section~\ref{tbau0} we find
  
 \be \epsilon(\theta,P=0)\Big|_{\theta=-1}=0.51888\cdots 
 \ee
 
 Likewise, by using instanton counting, and in particular \eqref{abpe} and \eqref{ainst}, we have ($\Lambda=1$)
 
 \be 2 \log\left(A \left(\frac{16 \re \sqrt{\pi }}{\Gamma \left(\frac{1}{4}\right)^2}\right)\right)=0.51887965286656 \cdots
 \ee
 
We have 5 matching digits which is consistent with the precision achieved with the TBA equation.

This discussion provides an additional result along the lines of what we obtained in section \ref{bo}. As we discussed in section 
\ref{tbau0}, the function $\epsilon(\theta)$ with the boundary condition (\ref{eq:bdy-cor}) computes the dyonic  period $\Pi_D(0,\hbar)$. As pointed out in Sec \ref{bo}, 
such period is Borel summable, and we can indeed test that its Borel resummation agrees with \eqref{ainst}, 
namely

\be  \label{bspd}\exp\left({1 \over 2 \hbar} s\left(\Pi_D\right)(0,\hbar)\right)={\sinh\left(\frac{\pi a}{\hbar }\right) \over \cosh\left({\ri \over \hbar}\partial_{a}F_{\rm NS}(a, \hbar)\right)}\bigg|_{a=a(0, \hbar)}=\frac{\sinh\left(\frac{1}{2 \hbar}  \Pi_A^{\rm ex}(0, \hbar)\right) }{ \cosh\left({1 \over 2\hbar} \Pi_B^{\rm ex}(0, \hbar)\right)}.
\ee

We have verified this identity numerically. In addition we have tested that \eqref{bspd} also holds for other values of $u$ in the strong coupling region, and we 
conjecture that, for $u\in [-1, 1]$, one has 

\be
 \label{bspd2}\exp\left({1 \over 2 \hbar} s\left(\Pi_D\right)(u,\hbar)\right)=\frac{\sinh\left(\frac{1}{2 \hbar}  \Pi_A^{\rm ex}(u, \hbar)\right) }{ \cosh\left({1 \over 2\hbar} \Pi_B^{\rm ex}(u, \hbar)\right)}.
\ee
