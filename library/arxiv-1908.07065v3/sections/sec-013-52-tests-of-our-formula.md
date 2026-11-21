---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-013-52-tests-of-our-formula
section_title: "Tests of our formula"
section_number: 5.2
pages: 31-33
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.989
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
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
