---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-5
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.997
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:intro}

For a linear space $W\subset \R^n$, $g\in W$  is an 
 \emph{elementary vector} if $g$ is a support minimal nonzero vector in $W$, that is, no $h\in W\setminus\{0\}$ exists such that $\supp(h)\subsetneq \supp(g)$, where $\supp$ denotes the support of a vector. 
 A \emph{circuit} in $W$ is the support of some elementary vector; these are precisely the circuits in the associated  linear matroid $\mathcal{M}(W)$. We let $\EE(W)\subseteq W$ and $\circuits_W\subseteq 2^n$
 denote the set of elementary vectors and circuits in the space $W$, respectively.

Elementary vectors were first studied in the 1960s by Camion \cite{camion1964}, Tutte \cite{Tutte1965}, Fulkerson \cite{Fulkerson1968}, and Rockafellar \cite{RockafellarTheEV}.
Circuits play a crucial role in matroid theory and have been extremely well studied.  
For regular subspaces (i.e., kernels of totally unimodular matrices), elementary vectors have $\pm 1$ entries; this fact has been at the heart of several arguments in network optimization since the 1950s. 

The focus of this paper is on various  \emph{circuit imbalance measures}. We give an overview of classical and recent applications, and their relationship with other condition measures. We will mainly focus on applications in linear programming, mentioning in passing also their relevance to integer programming. 

\paragraph{Three circuit imbalance measures}
There are multiple ways to quantify  how `imbalanced' elementary vectors of a subspace can be. We define three different measures that capture various fractionality and integrality properties.

We will need some simple definitions.
The linear spaces $\{0\}$ and  $\R^n$ will be called \emph{trivial} subspaces; all other subspaces are \emph{nontrivial}. A linear subspace of $\R^n$ is a \emph{rational linear space} if it admits a basis of rational vectors. Equivalently, a rational linear space can be represented as the image of a rational matrix.
For an integer vector $v\in\Z^n$, let $\lcm(v)$ denote the least common multiple of the entries $|v_i|$, $i\in [n]$.

For every $C\in \circuits_W$, the elementary vectors with support $C$ form a one-dimensional subspace of $W$. We pick a representative $g^{C,W}\in \EE(W)$ from this subspace.
If $W$ is not a rational subspace, we select $g^{C,W}$ arbitrarily. For rational subspaces, we select $g^{C,W}$ as an integer vector with the largest common divisor of the coordinates being 1;
this choice is unique up to multiplication by $-1$.  When clear from the context, we omit the index $W$ and simply write $g^C$.
We now define the fractional circuit imbalance measure and two variants of integer circuit imbalance measure. 

\begin{Def}[Circuit imbalances]\label{def:kappa} For a non-trivial linear subspace $W\subseteq \R^n$, let us define the following notions:
\begin{itemize}
    \item
The \emph{fractional circuit imbalance measure} of $W$ is
\[
\kappa_W:=\max\left\{\left|\frac{g^C_j}{g^C_i}\right|:\,C\in\circuits_W, i,j\in C\right\}\, .
\]
\item If $W$ is a rational linear space,  the \emph{lcm-circuit imbalance measure}  is
\[
\kd_W:=\lcm\left\{\lcm(g^C):\,C\in\circuits_W\right\}\, .
\]
\item If $W$ is a rational linear space, the 
 \emph{max-circuit imbalance measure}  is
\[
\bar\kappa_W:=\max\left\{\|g^C\|_\infty:\,C\in\circuits_W\right\}\, .
\]
\end{itemize}
For trivial subspaces $W$, we define $\Le_W=\kd_W=\bar\kappa_W=1$.
Further, we say that the rational subspace $W$ is \emph{anchored}, if every vector $g^C$, $C\in\circuits_W$ has a $\pm 1$ entry.
\end{Def} 
Equivalently, in an anchored subspace every elementary vector $g\in\EE(W)$ has a nonzero entry such that all other entries are integer multiples of this entry.

 The term \emph{`circuit imbalance measure'} will refer to the fractional measure $\kappa_W$.
Note that $1\le \kappa_W\le \bar\kappa_W\le\dot\kappa_W$ and $\kappa_W=1$ implies $\bar\kappa_W=\dot\kappa_W=1$. This case plays a distinguished role and turns out to be equivalent to $W$ being a regular linear space (see Theorem~\ref{thm:tu_iff_kappa_1}).

 Another important case is when $\dot\kappa_W=p^\alpha$ is a prime power. In this case, $W$ is anchored, and  $\kappa_W=\bar\kappa_W=\dot\kappa_W$.
The linear space will be often represented as $W=\ker(A)$ for a 
a matrix $A\in \R^{m\times n}$.
We will use  $\EE(A)$, $\circuits_A$, $\Le_A$, $\kd_A$, $\bar\Le_A$ to refer to the corresponding quantities in $\ker(A)$.

\medskip

An earlier systematic study of elementary vectors was done in
Lee's work ~\cite{Lee89}. He mainly focused on the max-circuit imbalance measure; we give a quick comparison to the results in Section~\ref{sec:basic}. The fractional circuit imbalance measure played a key role in the paper \cite{DHNV20} on layered-least-squares interior point methods; it turns out to be  a close proxy to the well-studied condition number $\bar\chi_W$. As far as the authors are aware, the lcm-circuit imbalance measure has not been explicitly studied previously.

\paragraph{Overview and contributions}
Section~\ref{sec:prelim} introduces some background and notation.
Section~\ref{sec:basic} gives an overview of fundamental properties of $\Le_W$ and $\kd_W$. In particular, Section~\ref{sec:subdet} relates circuit imbalances to subdeterminant bounds. 
We note that many extensions of totally unimodular matrices focus on matrices with bounded subdeterminants. Working with circuit imbalances directly can often lead to stronger and conceptually cleaner results.
Section~\ref{sec:HK} presents an extension of the Hoffman-Kruskal characterization of TU matrices. Section~\ref{sec:self-dual} shows an important self-duality property of $\Le_W$ and $\kd_W$. Section~\ref{sec:matrix} studies `nice' matrix representations of subspaces with given lcm-circuit imbalances.
Section~\ref{sec:triangle} proves a multiplicative triangle-inequality for $\Le_W$. Many of these results were previously shown by Lee~\cite{Lee89}, Appa and Kotnyek~\cite{Appa04}, and by Dadush et al.~\cite{DHNV20}. We present them in a unified framework, extend some of the results, and provide new proofs.

Section~\ref{sec:connections} reveals connections between $\Le_W$ and the well-studied condition numbers $\bar\chi$ studied in the context of interior point methods, and $\delta$ studied---among other topics---in the analysis of the shadow simplex method. In particular, we show that previous diameter bounds for polyhedra can be translated to strong diameter bounds in terms of the condition number $\Le_W$ (Theorem~\ref{thm:kappa-diameter}).

Section~\ref{subsec:def_chi_bar_star} studies the best possible values of $\Le_{W}$ that can be achieved by rescaling the variables. We present the algorithm and min-max characterization from \cite{DHNV20}. Further, we characterize when a subspace can be rescaled to a regular one; we also give a new proof of a theorem from~\cite{Lee89}.

Section~\ref{sec:hoffman} shows variants of Hoffman-proximity bounds in terms of $\Le_W$ that will be used in  subsequent algorithms. In Section~\ref{sec:only-A}, we study algorithms for linear programming whose running time only depends on the constraint matrix $A$, and reveal the key role of $\Le_A$ in this context. Section~\ref{sec:black-box} shows how the Hoffman-proximity bounds can be used to obtain a black-box algorithm with $\Le_A$-dependence as in \cite{DadushNV20}, and Section~\ref{sec:LLS} discusses layered least squares interior point methods \cite{DHNV20,Vavasis1996}.

Section~\ref{sec:augment} gives an overview of circuit diameter bounds and circuit augmentation algorithms, a natural class of LP algorithms that work directly with elementary vectors. As a new result, we present an improved iteration bound on the steepest-descent circuit augmentation algorithm, by extending the analysis of the minimum mean-cycle cancelling algorithm of Goldberg and Tarjan (Theorem~\ref{thm:steepest-main}).

Section~\ref{sec:graver} gives an outlook to integer programming, showing the relationship between the max-circuit imbalance and Graver bases. Finally, Section~\ref{sec:conjecture} formulates a conjecture on circuit decompositions with bounded fractionality.
