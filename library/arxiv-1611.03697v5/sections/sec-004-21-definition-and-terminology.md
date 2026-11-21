---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-004-21-definition-and-terminology
section_title: "Definition and terminology"
section_number: 2.1
pages: 3-4
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
The following definition  is a special case of the notion of stability data on a graded Lie algebra \cite[Section 2.1]{KS1}. It was also studied by Stoppa and his collaborators \cite[Section 3]{BSt}, \cite[Section 2]{FGS}.


\begin{defn}
A BPS structure  consists of \begin{itemize}
\item[(a)] A finite-rank free abelian group $\Gamma\isom \bZ^{\oplus n}$, equipped with a skew-symmetric form \[\<-,-\>\colon \Gamma \times \Gamma \to \bZ,\]

\item[(b)] A homomorphism of abelian groups
$Z\colon \Gamma\to \bC$,\smallskip

\item[(c)] A map of sets
$\Omega\colon \Gamma\to \bQ,$
\end{itemize}

satisfying the following properties:

\begin{itemize}
\item[(i)] Symmetry: $\Omega(-\gamma)=\Omega(\gamma)$ for all $\gamma\in \Gamma$,\smallskip
\item[(ii)] Support property: fixing a norm  $\|\cdot\|$ on the finite-dimensional vector space $\Gamma\tensor_\bZ \bR$, there is a constant $C>0$ such that 
\begin{equation}
\label{support}\Omega(\gamma)\neq 0 \implies |Z(\gamma)|> C\cdot \|\gamma\|.\end{equation}
\end{itemize}
\end{defn}


The lattice $\Gamma$ will be  called the charge lattice, and the form $\<-,-\>$ is the intersection form. The group homomorphism $Z$ is  called the central charge. The rational numbers $\Omega(\gamma)$ are called BPS invariants. A class $\gamma\in \Gamma$ will be called active if $\Omega(\gamma)\neq 0$.
