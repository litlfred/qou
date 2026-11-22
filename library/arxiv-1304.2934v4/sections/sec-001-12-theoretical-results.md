---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-001-12-theoretical-results
section_title: "Theoretical results"
section_number: 1.2
pages: 5-7
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.975
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
The goal of this paper is to prove that the framework of mod-$\phi$ convergence as described in Definition~\ref{def:modphi} is suitable to obtain {\em precise}  large and moderate deviation results for the sequence $(X_n)_{n \in \N}$
(throughout the paper, we call {\em precise deviation result} an equivalent of the deviation probability itself and not on its logarithm). Namely, our results are the following.\vspace{2mm}

\begin{itemize}
\item We give equivalents for the quantity $\proba[X_n \ge t_n x]$, where $x$ is a fixed positive real number (see  Theorem~\ref{thm:mainlattice} for a lattice distribution $\phi$ and Theorem~\ref{thm:mainnonlattice} for a non-lattice distribution). This can be viewed as an analog (or an extension, see Section \ref{subsect:OnInfDiv}) of Bahadur-Rao theorem \cite{BR60}.\vspace{2mm}

\item We also consider probabilities of the kind $\proba[X_n \in t_n B]$ where $B$ is a Borelian set, and we give upper and lower bounds on this probability which coincide at first order for a {\em nice} Borelian set $B$, see Theorem~\ref{thm:hyperellis}. This result is an analog of Ellis-G\"artner theorem \cite[Theorem 2.3.6]{DZ98} (see also the original papers \cite{Gar77,Ellis84}): we have stronger hypotheses than in Ellis-Gärtner theorem, but also a more precise conclusion (the bounds involve the probability itself, not its logarithm).\vspace{2mm}

\item Besides, we give an equivalent for the probability $\proba[X_n -\esper[X_n] \ge s_n t_n]$, where $s_n=o(1)$, covering all intermediate scales between central limit theorem and deviations of order $t_n$ (Theorem~\ref{thm:cltlattice} in the lattice case, and Theorem~\ref{thm:cltnonlattice} in the non-lattice case).
\end{itemize}    
We also address the question of {\em normality zone}, {\it i.e.} the scale up to which the Gaussian approximation 
(coming from the central limit theorem) for the tail of the distribution of $X_n$ is valid.
In particular, our methods provide us with a systematic way to detect it and also explains how this approximation breaks at the edge of this zone; see Section \ref{sec:cumulantechnic}. 
The problem of detecting the normality zone for sums of i.i.d. random variables has received some attention in the literature on limit theorems (origninally in \cite{Cramer38}, see also \cite{IL71}).
Our framework enables an extension of such results, going beyond the setting of independent random variables:\vspace{1mm}
\begin{itemize}
\item we cover more situations, {\em e.g.}~sums of dependent random variables with a sparse dependency graph, or integer valued random variables, such as random additive functions, satisfying mod-Poisson convergence;\vspace{1mm}
\item we describe the correction to the normal approximation needed at the edge of the normality zone.
\end{itemize}







\noindent An interesting fact in our deviation results is the appearance of the limiting function $\psi$ in deviations at scale $t_n$. This means that, at smaller scales, a sequence $X_n$ converging mod-$\phi$ behaves exactly as a sum of $t_n$ i.i.d.~variables with distribution $\phi$. However, at scale $t_n$, this is not true any more and the limiting function $\psi$ gives us exactly the correcting factor.\medskip

In particular, in the case of mod-Gaussian convergence, the scale $t_n$ is the first scale where the equivalent given by the central limit theorem is not valid anymore. In this case, one often observes a symmetry breaking phenomenon
which is explained by the appearance of function $\psi$; see Section \ref{subsec:normalityzone}.
\bigskip


A special case of mod-Gaussian convergence is the case where \eqref{eq:modphi} is proved using bounds on the cumulants of $X_n$ --- see Section \ref{subsec:modgaussfromcumulants}. This case is particularly interesting as:\vspace{2mm}
\begin{itemize}
    \item it contains a large class of examples, see below in Section \ref{subsec:applications};\vspace{2mm}
    \item in this setting, one can obtain deviation results at a scale larger that $t_n$ (typically, $o((t_n)^{5/4})$, see Proposition \ref{prop:largedeviationscumulants}).\vspace{2mm}
\end{itemize}


The arguments involved in the proofs of our deviation results are standard, but they nonetheless need to be carefully adapted to the framework of Definition \ref{def:modphi}: elementary complex analysis, the method of change of probability measure or tilting due to Cram\'er, or adaptations of Berry-Esseen type inequalities with smoothing techniques. 
\bigskip


\begin{remark}
    \label{rem:hwang}
    We should here mention the work of Hwang \cite{Hwa96}, with some similarities with ours. Hwang works with hypotheses similar to Definition~\ref{def:modphi}, except that the convergence takes place uniformly on all compact sets contained in a given disk centered at the origin (while we assume convergence in a strip; thus this is weaker than our hypothesis, see Remark~\ref{rem:diskorstrip} for a discussion on this point).
    Under this hypothesis (and an hypothesis of the convergence speed), Hwang obtains an equivalent of the probability $\proba[X_n -\esper[X_n] \ge s_n t_n]$ with $s_n=o(1)$, and even gives some asymptotic expansion of this probability. However, Hwang does not give any deviation result at the scale $t_n$ and hence, none of his results show the role of $\psi$ in deviation probabilities. Besides, he has no results in the multi-dimensional setting.
\end{remark}
\bigskip
