---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-008-5-large-n-analysis-of-partition-function-an-alte
section_title: "Large N analysis of partition function : an alternate proof of the limit shape theorem"
section_number: 5
pages: 15-16
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.879
latex_coverage_ratio: 1.0
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:largek}

The large $N$ analysis of partition function (\ref{eq:GCPF2}) was explicitly done in \cite{duttagopakumar}. We briefly review the procedure for the readers not familiar with matrix model techniques (for a more comprehensive treatment of matrix models, see \cite{Marino:2005sj,Eynard:2015aea,eynard_book}). To analyse the partition function (\ref{eq:GCPF3}) we  denote a valid Young diagram of symmetric group $S_k$ by a set of numbers $\{n_i\}_{i=1}^N$ where $n_i$ denotes the number of boxes in $i^{th}$ row. 

\begin{figure}[h]
	\begin{center}
		\includegraphics[width=9cm,height=5.5cm]{YDEng.pdf}
			\caption{A generic Young diagram in English notation. Here $N$ is an arbitrary positive integer. The number of boxes in the first column is less than or equal to $N$. In general, $\exists$ a number $0<M\leq N$ such that $n_i=0$ for $i=M+1, \cdots, N.$}
			\label{fig:YD-english}
	\end{center}
\end{figure}

$N$ is an arbitrary positive integer greater than or equal to the height of the first column. See figure \ref{fig:YD-english}. The dimension of a representation $\lambda_k$ of $S_k$ is given by \cite{hamermesh}

\ben\label{eq:dimY}
\text{dim} \lambda_k = \frac{k!}{h_1! h_2! \cdots h_N!} \prod_{i=1\atop i<j }^{N}(h_i-h_j)
\een

where,

\ben\label{eq:hook}
h_i = n_i + N -i
\een

is the hook length of the first box in $i^{th}$ row. 

We consider the large $N$ limit of the partition function (\ref{eq:GCPF3}). In this limit the hook numbers $h_i \sim N$ (\ref{eq:hook}). Therefore we define the following continuous functions to describe Young diagrams at large $N$

\ben
n(x) = \frac{n_{i}}{N}, \quad h(x) = \frac{h_i}{N}, \quad \where \quad x=\frac{i}{N},\quad x\in[0,1].
\een

The function $n(x)$ or $h(x)$ captures the distribution of boxes in a large $k$ Young diagram. The relation between $n(x)$ and $h(x)$ follows from equation (\ref{eq:hook}) and is given by

\be\label{eq:hook2}
h(x) = n(x)+1-x.
\ee

The number of boxes in a Young diagram in the large $N$ limit is given by

\be
k = \sum_{i=1}^{N} n_i \longrightarrow N^2 \lB \int_0^1 dx \lb h(x)+1-x \rb\rB = N^2 \lB \int_0^1 dx h(x)-\frac12 \rB = N^2 k'
\ee

where

\be
k' =  \int_0^1 dx h(x)-\frac12\
\ee

is the renormalised box number and is an ${\cal O}(1)$ quantity. Thus we see that the number of boxes in a Young diagram in the large $N$ limit goes as $\sim {\cal O}(N^2)$ and hence $N\sim {\cal O}(\sqrt{k})$. The partition function (\ref{eq:GCPF3}) in $N \ra \infty$ limit is given by,

\ben
	\cQ_{\cY} = \int [Dh(x)] e^{-N^2 \seff{h(x)}} 
\een

where

\ben 
-\seff{h(x)}  = \int_0^1 dx\Xint-_0^1 dy \ln|h(x)-h(y)| -2 \int_0^1 dx h(x) \ln h(x) +k' \ln (z k') +k'+1.
\een

Therefore, the dominant contribution to the partition function comes from the extrema of $\seff{h(x)}$. Varying $\seff{h(x)}$ with respect to $h(x)$ we get the saddle point equation

\ben\label{eq:saddeq2}
\Xint- \frac{u(h')dh'}{h-h'} = \ln \lb \frac{h}{\xi}\rb, \quad \where \quad \xi^2 = z k'
\een

where the Young diagram density $u(h)$ is given by

\ben\label{eq:uhdef}
u(h)=-\frac{\partial x}{\partial h}.
\een

Monotonicity of $h(x)$ implies $0 \leq u(h) \leq 1$. $u(h)$ also satisfies two conditions

\ben\label{eq:uhcond}
\int dh\, u(h) =1, \quad \tand \quad \int h\, u(h)\, dh = k'+\frac12.
\een

We solve the saddle point equation (\ref{eq:saddeq2}) to find Young diagram density that satisfies the constraints (\ref{eq:uhcond}).
