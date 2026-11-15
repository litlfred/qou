---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-015-42-stability-implies-negative-association
section_title: "Stability Implies Negative Association"
section_number: 4.2
pages: 24-25
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.982
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s-sna}

The main argument in the proof of the following theorem goes back to 
Feder-Mihail \cite{feder} although the proof of the full theorem is scattered 
over the literature \cite{DJR,Lyons,Lyons-Peres,W}. 

\begin{theorem}\label{FM}
Let $\mathcal{S}$ be a class of probability measures satisfying: 
\begin{enumerate}
\item Each $\mu \in \mathcal{S}$ is a measure on $2^{E}$, where $E$ is a 
finite subset of $\{1,2,\ldots\}$ depending on $\mu$; 
\item $\mathcal{S}$ is closed under conditioning; 
\item For each $\mu \in \mathcal{S}$ the variables $X_e$, $e \in E$, 
are pairwise negatively correlated; 
\item Each $\mu \in \mathcal{S}$ has a homogeneous generating polynomial.  
\end{enumerate} 
Then all measures in $\mathcal{S}$ are $\CNA$ (conditionally negatively 
associated).
\end{theorem}







The homogeneity condition in (4) above is essential and ensures 
the existence of
a variable of so-called ``positive influence'' \cite{DJR} (various 
notions of ``influence'' have been studied by Bourgain {\em et al} in 
\cite{BKKKL}). 

A sketch of the proof of Theorem~\ref{FM} is as follows.  
Recall from \S \ref{s21} the definition of an increasing event. Since any 
increasing function depending on a set $E_0$ can be written as a positive 
linear 
combination of characteristic functions, $\chi_{\mathcal{A}}$, of increasing 
events $\mathcal{A}$ depending on $E_0$, it is enough to prove the theorem for 
such characteristic functions. The proof of negative association in the case
when 
$F =\chi_{\mathcal{A}}$ and $G = X_e$ in Definition~\ref{d-na} are such that
$\cA$ does not depend on $e$ is recovered from Feder-Mihail's proof 
\cite{feder,Lyons-Peres}. The general case -- when
$F =\chi_{\mathcal{A}_1}$ and $G = \chi_{\mathcal{A}_2}$ in 
Definition~\ref{d-na} are such that $\cA_1$ and $\cA_2$ depend on disjoint
sets of variables -- then follows from the proof of \cite[Theorem 6.5]{Lyons}. 

Using Theorem~\ref{FM} we can establish the following result.

\begin{theorem}\label{stab-NA}
If $\mu\in \fP_n$ is strongly Rayleigh then it is $\CNA+$. 
\end{theorem}

\begin{proof}
Let $\mathcal{S}$ be the class of all probability measures $\mu$ such that 
\begin{itemize} 
\item each $\mu \in \mathcal{S}$ is a measure on $2^{E}$, where $E$ is a 
finite subset of $\{1,2,\ldots\}$ depending on $\mu$, and 
\item $\mu$ has a stable homogeneous generating polynomial.  
\end{itemize}
Since stable homogeneous polynomials are pairwise negatively correlated and
are also closed under conditioning (cf.~\S \ref{s21}), the class 
$\mathcal{S}$ satisfies all the hypotheses required in Theorem~\ref{FM}.
Therefore, all the measures in $\mathcal{S}$ are negatively associated. Let 
further $\widehat{\mathcal{S}}$ 
be the class of all probability measures $\mu$ such that 
\begin{itemize} 
\item each $\mu \in \widehat{\mathcal{S}}$ is a measure on $2^{E}$, where 
$E$ is a 
finite subset of $\{1,2,\ldots\}$ depending on $\mu$, and 
\item $\mu$ has a stable generating polynomial.  
\end{itemize}
Now by Theorem~\ref{SH} every measure in $\widehat{\mathcal{S}}$ is the 
projection of a measure in 
$\mathcal{S}$. Since negative association is closed under projections and 
the strongly Rayleigh property is closed under conditioning and external 
fields, the theorem follows.
\end{proof}

Note that since the Rayleigh/h-NLC+ property is also closed under conditioning,
projections, and external fields, Theorem~\ref{FM} and slight modifications of
the above arguments actually yield the following stronger version of 
Theorem~\ref{stab-NA}.

\begin{theorem}\label{PHR-NA}
If $\mu\in \fP_n$ is $\PHR$ then it is $\CNA+$. 
\end{theorem}

Since homogeneous Rayleigh polynomials need not be stable, 
strongly Rayleigh $\Rightarrow$ PHR strictly. As we will see in 
\S \ref{s-countex}, one also has PHR $\Rightarrow$ CNA+ strictly.
