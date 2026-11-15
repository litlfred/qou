---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-009-26-further-terminology
section_title: "Further terminology"
section_number: 2.6
pages: 6-7
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.866
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{defns}

In this section we gather some terminology for describing BPS structures of various special kinds.

\begin{defn}
\label{la}
We say that a BPS structure $(Z,\Gamma,\Omega)$ is
\begin{itemize}
\item[(a)] finite, if there are only finitely many active classes $\gamma\in \Gamma$;

\item[(b)] ray-finite, if for any ray $\ell\subset \bC^*$ there are only finitely many active classes $\gamma\in \Gamma$ for which $Z(\gamma)\in \ell$;

\item[(c)] convergent, if for some $R>0$
\begin{equation}\label{concon}\big.\sum_{\gamma\in \Gamma} |\Omega(\gamma)|\cdot e^{-R|Z(\gamma)|}<\infty.\end{equation}
\end{itemize}
\end{defn}

An equivalent condition to \eqref{concon} already appears in the work of Gaiotto, Moore and Neitzke \cite[Appendix C]{GMN1}. The same condition also plays a prominent role in the work of Barbieri and Stoppa \cite[Definition 3.5]{BSt}. 


\begin{defn}
\label{gob}
We say that a BPS structure $(Z,\Gamma,\Omega)$ is
\begin{itemize}
\item[(a)] {uncoupled}, if  for any two active classes $\gamma_1,\gamma_2\in \Gamma$  one has
 $\<\gamma_1,\gamma_2\>=0$;

\item[(b)] generic, if for any two active classes $\gamma_1,\gamma_2\in \Gamma$ one has 
\[\bR_{>0} \cdot Z(\gamma_1)=\bR_{>0} \cdot Z(\gamma_2) \implies \< \gamma_1, \gamma_2\>=0.\]
\item[(c)] integral, if the BPS invariants $\Omega(\gamma)\in \bZ$ are all integers.
\end{itemize}
\end{defn}

The  uncoupled condition ensures that the Hamiltonian flows for any pair of functions on $\bT$ of the form $\DT(\gamma)\cdot x_\gamma$ commute. This situation corresponds to the case of  `mutually local corrections'  in \cite{GMN1}.  Genericity is the weaker condition that all such flows for which $Z(\gamma)$ lies on a given fixed ray $\ell\subset \bC^*$ should commute.
