---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-003-3-review-2-plancherel-growth-of-young-diagrams
section_title: "Review 2 : Plancherel Growth of Young diagrams"
section_number: 3
pages: 9-10
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.983
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:plancherel}

The Markovian growth process of large Young diagrams can be given a statistical interpretation described through a partition function. In order to achieve that we define a Young lattice \cite{Eynard:2008mt}

\be\label{eq:Ylattice}
\cY = \bigcup\limits_{k=0}^{\infty}  \cY_k.
\ee

All the members of $\cY_k$ have same number of boxes but different shapes. $\cY_k$ can be thought of as an ensemble of Young diagrams with the same macroscopic variable $k$. Hence, we can define a partition function for the grand canonical ensemble (\ref{eq:Ylattice})

\ben\label{eq:GCPF}
\cQ_\cY = \sum_{k=0}^{\infty}z^k  \cZ_{\cY_k} 
\een

where $z$ is called \emph{fugacity} ($z>0$) and $\cZ_{\cY_k}$ is the canonical partition function for $\cY_k$, given by

\be\label{eq:CPF}
 \cZ_{\cY_k} = \sum_{\lambda_k} \cP(\lambda_k)  \delta(k-|\lambda_k|).
\ee

$\cP(\lambda_k)$ is the probability associated with the ensemble member $\lambda_k$ - a Young diagram with $k$ number of boxes.

To make the growth process meaningful it is customary to assign a probability for each diagram at level $k$ in the Young lattice $\cY$. There is a natural way to assign probability to different diagrams. We count the total number of inequivalent paths one can follow to come to a particular diagram at level $k$ starting from $\emptyset$. See figure \ref{fig:younggrowth}. It turns out that the Plancherel measure is proportional to the square of that number. The proportionality constant is fixed by the normalization condition. To calculate the number of paths heading to a diagram $\lambda_k$ we look at growth of Young tableaux rather than Young diagrams. Starting from $\emptyset$ we keep on adding one box at each level with increasing number. Therefore the readers can easily convince themselves that at each level $k$ we have different Young tableaux and a particular tableaux can be reached from $\emptyset$ by a unique path only. Thus the number of paths available to reach a particular Young diagram $\lambda_k$ is equal to the number of standard Young tableaux $f_{\lambda_k}$ of that given shape. It is well known that \cite{hamermesh,fulton1991representation},

\be\label{eq:dimRnormalization}
\sum_{\lambda_k \in\cY_k} (f_{\lambda_k})^2=k!.
\ee

Hence we get the Plancherel measure $\cP(\lambda_k)$ for a diagram $\lambda_k$

\be\label{eq:Plancherelmeasure}
\cP(\lambda_k) =  \frac{f_{\lambda_k}^2}{k!}.
\ee

This definition of Plancherel probability is equivalent to what we defined in equation (\ref{eq:transmeasure}). One can show that

\ben
\cP(\lambda_k)=\sum_{\text{paths}}\prod_{i=0}^{k-1} \cP_{\text{transition}}(\lambda_i,\lambda_{i+1}).
\een


We use $\cP(\lambda_k)$ to write the partition function for the growth process. The number $f_{\lambda_k}$ is equal to the dimension of the representation $\lambda_k$, i.e.

\be
f_{\lambda_k} = \text{dim} \ \lambda_k.
\ee

and thus we have,

\be\label{eq:Plancherelmeasure2}
\cP(\lambda_k) =  \frac{(\text{dim} \ \lambda_k)^2}{k!}.
\ee

It was observed in \cite{LogShe,VerKer77} that a Young lattice equipped with Plancherel measure terminates to a universal class of diagram in the limit $k\ra \infty$ when the diagrams are scaled properly.
