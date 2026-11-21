---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-014-53-comparison-to-zamolodchikovs-tba-equation
section_title: "Comparison to Zamolodchikov's TBA equation"
section_number: 5.3
pages: 33-36
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.994
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
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
