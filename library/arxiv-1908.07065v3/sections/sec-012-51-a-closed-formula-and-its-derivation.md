---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-012-51-a-closed-formula-and-its-derivation
section_title: "A closed formula and its derivation"
section_number: 5.1
pages: 30-31
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.979
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{deri}

By using the approach of \cite{ghm,gm3} we find the following expression 
for the spectral determinant of \eqref{eq:schrodinger}\footnote{While presenting these 
results at the conference {\it Irregular singularities in Quantum Field Theory} (http://irregular.rd.ciencias.ulisboa.pt/conference),   	
S. Lukyanov informed us that he had independently derived this result \cite{PCL} by using completely different methods. }

\be 
\label{sd}\Xi(E)=A (\hbar) \left( \sinh\left(\frac{ \Pi_A^{\rm ex}(E, \hbar)}{2 \hbar }\right) \right)^{-1} \cosh\left({1 \over 2\hbar} \Pi_B^{\rm ex}(E, \hbar)\right), 
\ee

where $\Pi_{A,B}^{\rm ex} (E, \hbar)$ are given by (\ref{abpe}) and $A(\hbar) $ is an $u$-independent constant which can be fixed from $\Xi(0)=1$, namely, 

 \be\label{ainst} A(\hbar) =  \sinh\left(\frac{ \Pi_A^{\rm ex}(0, \hbar)}{2 \hbar }\right)  \left(\cosh\left({1 \over 2\hbar} \Pi_B^{\rm ex}(0, \hbar)\right)\right)^{-1}.\ee
 
From this expression we can read off explicit formulae for the spectral traces. We find for instance 

\be \label{tr1} Z_1=-{1\over 2 \hbar}\left(\partial_E\Pi_B^{\rm ex}(0, \hbar) \tanh \left( {\Pi_B^{\rm ex}(0, \hbar)}\over 2 \hbar\right)-  \coth \left(\frac{\Pi_A^{\rm ex}(0, \hbar)}{2 \hbar }\right)   \partial_E \Pi_A^{\rm ex}(0, \hbar)\right)      ,\ee

as well as

\be \ba \label{tr2} 4 \hbar^2 Z_2= & 2 \hbar \partial_E^2\Pi_A^{\rm ex}(0,\hbar) \coth \left(\frac{\Pi_A^{\rm ex}(0,\hbar)}{2 \hbar }\right)-(\partial_E\Pi_A^{\rm ex}(0,\hbar))^2 \text{csch}^2\left(\frac{\Pi_A^{\rm ex}(0,\hbar)}{2 \hbar }\right)\\
&-\text{sech}^2\left(\frac{\Pi_B^{\rm ex}(0,\hbar)}{2 \hbar }\right) \left(\hbar  \partial_E^2 \Pi_B^{\rm ex}(0,\hbar) \sinh \left(\frac{\Pi_B^{\rm ex}(0,\hbar)}{\hbar }\right)
+(\partial_E \Pi_B^{\rm ex}(0,\hbar))^2\right). 
\ea
 \ee
 
 Note that in order to calculate $\Pi_A^{\rm ex}(0,\hbar)$ we have to use (\ref{inta}) or (\ref{a-char}), so the above formula tests as well the analytic continuation of instanton calculus beyond the semiclassical region\footnote{In evaluating the derivative of the periods w.r.t.~$E$, we used the quantum Matone relation (\ref{mmap}) and instanton 
 calculus. }.  









The explicit formula (\ref{sd}) can be extended to the family of operators considered in \cite{gm3}, see Appendix \ref{asun} for more details. 


Let us now explain how to
derive \eqref{sd} from the TS/ST correspondence of \cite{ghm,cgm}. The relevant CY geometry is the
canonical bundle over $\IF_0$, also known as resolved $Y^{2,0}$
singularity.  The corresponding quantum mirror curve is

\begin{equation}
\mO-\kappa=(R \Lambda)^2(\re^{\mathsf x}+\re^{-\mathsf
    x})-\kappa+\re^{\mathsf p}+\re^{-\mathsf p},  \quad [\mathsf x,
  \mathsf p]=\ri  \hbar.
\end{equation}

According to the TS/ST correspondence we have

\begin{equation}
  \label{tsst} \det (1-\kappa \mO^{-1})=\sum_{ { m}
    \in \IZ} \exp\left[\mJ ( {\mu+\ri \pi+2 \pi \ri m},R\Lambda,
    \hbar)\right], \quad \kappa=\re^{\mu},
\end{equation}

where $\mJ ( {\mu},\xi, \hbar)$ is the grand potential of the resolved $Y^{2,0}$ singularity as defined in \cite{gm3}, section~5.1.

The expression  \eqref{sd}  is obtained by implementing  the geometric engineering limit \cite{selfdual,kkv} in \eqref{tsst}. 
More precisely, we consider the limit 

\be\label{4dlimit} p\to R p, \quad\hbar\to R\hbar, \quad \kappa=2+E R^2+\mathcal{O}(R^3), \quad R\to 0.\ee

This has to be done carefully since both sides of \eqref{tsst} diverge, therefore they need to be properly regularized. 
For that it is convenient to study the trace of the resolvent

\be 
G_\mO (\kappa)={\rd \over \rd \kappa} \log \det (1-\kappa \mO^{-1})={\rm Tr} \left({1\over \kappa- \mO}\right), 
 \ee

rather than the spectral determinant. It is easy to see that in the limit \eqref{4dlimit} one has

\be  G_\mO (\kappa) \to {1\over R^2} G(E), \qquad G(E)= \Tr\left({1\over E-\mH}\right),
\ee

where $\mH$ is the modified Mathieu operator in (\ref{eq:schrodinger}). 

Likewise the limit \eqref{4dlimit} can be implemented on the r.h.s~of \eqref{tsst} in a quite 
straightforward way by following \cite{gm3}, section~5.2 and by using the identity (3.9) in \cite{bgt}. 
The overall divergent piece $R^{-2}$ cancels and we find

\be 
\ba 
G(E)=-{\partial_E a \over \hbar}\left(\partial_a^2 F_{\rm NS}\tanh\left({\partial_a F_{\rm NS}\over \hbar}\right)+\pi \coth\left({a\pi\over \hbar}\right)\right).
\ea\ee

 By integrating w.r.t.~$E$ we obtain \eqref{sd}, where $A(\hbar)$ is an integration constant.
