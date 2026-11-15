---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-006-4-partition-function-for-young-lattice
section_title: "Partition Function for Young lattice"
section_number: 4
pages: 13-13
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.989
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:partitionfunction}


Following (\ref{eq:GCPF}, \ref{eq:CPF}) and \cref{eq:Plancherelmeasure}, the grand canonical partition function for $\cY$ can be written as,

\ben\label{eq:GCPF2}
\cQ_\cY = \sum_{k=0}^{\infty} z^k \sum_{\lambda_{k}} \frac{(\text{dim}\lambda_{k})^2}{k!} \delta(k-|\lambda_{k}|), \quad z>0.
\een

This partition function is related to \emph{Poissonised Plancherel measure} \cite{1999math.5032B}. The above ensemble sometimes is known as \emph{Meixner} ensemble in literature \cite{1999math.6120J,2010ArM.48.79J}.

The above partition function does not capture the growth process of Young diagrams as it can exactly be calculated using the normalization \cref{eq:dimRnormalization}

\be
\cQ_{\cY} = \frac{1}{1-z}.
\ee

However, to study the growth process through the partition function we regularise the sum by imposing a \emph{cut-off} on the Young diagrams in the summation over $\lambda_k$ in eq. (\ref{eq:GCPF2}). We introduce a large positive integer $N$ and constrain that the Young diagrams in lattice $\cY$ can not have more than $N$ rows. In presence of such a cut-off the summation over $\lambda_k$ for $k>N$ is not equal to unity anymore. The \emph{regularised} partition function is therefore given by

\ben\label{eq:GCPF3}
\cQ_\cY^N = \sum_{k=0}^{\infty} z^k \sum_{n_1,\cdots, n_N\geq 0} \frac{(\text{dim}\lambda_{k})^2}{k!} \delta\lb k-\sum_{i=1}^N n_i\rb, \quad \with \quad n_1\geq n_2\geq \cdots\geq n_N\geq 0. 
\een

This regularisation gives us a handle on the partition function to carry out a saddle point analysis of the problem. In the large $N$ limit, the partition function is dominated by a single Young diagram for a given value of $z$. It turns out that the shape of this dominant diagram falls into the automodel class of Kerov \cite{Kerov1}, paramatrised by $z$. For a particular value of the parameter $z$ it becomes the limit shape \cite{VerKer77,LogShe,Kerov1}. Before we present the calculation, we show that the partition function (\ref{eq:GCPF3}) is equivalent to the partition function of $SU(N)$ Gross-Witten-Wadia model and its cousins.
