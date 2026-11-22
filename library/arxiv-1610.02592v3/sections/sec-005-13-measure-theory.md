---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-005-13-measure-theory
section_title: "Measure theory"
section_number: 1.3
pages: 31-34
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.735
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{measure:theory:section}
We will use some basic measure theory only in Chapter \ref{automorfismi:chapter}.


\subsection{Borel measure}
A \emph{Borel set} in a topological space $X$ is any subset obtained from open sets through the operations of countable union, countable intersection, and relative complement. Let $\calF$ denote the set of all Borel sets.
A \emph{Borel measure} on $X$ is a function $\mu\colon \calF \to [0,+\infty]$ which is additive on any countable collection of disjoint sets. 
\index{Borel set}
\index{Borel measure}

The measure is \emph{locally finite} if every point has a neighbourhood of finite measure and is \emph{trivial} if $\mu(S)=0$ for all $S\in\calF$. 

\begin{ex} If $\mu$ is a locally finite Borel measure then $\mu(X)<+\infty$ for any compact Borel set $K\subset X$.
\end{ex}

\begin{example}
Let $D\subset X$ be a discrete set. The \emph{Dirac measure} $\delta_D$ concentrated in $D$ is the measure
$$\delta_D(S) = \#(S\cap D).$$
Since $D$ is discrete, the measure $\delta_D$ is locally finite.
\end{example}

The \emph{support} of a measure is the set of all points $x\in X$ such that $\mu(U)>0$ for any open set $U$ containing $x$. The support is a closed subset of $X$. The measure is \emph{fully supported} if its support is $X$. The support of $\delta_D$ is of course $D$. A point $x\in X$ is an \emph{atom} for $\mu$ if $\mu(\{x\})>0$.


\subsection{Construction by local data}
A measure can be defined using local data in the following way.

\begin{prop} \label{ricoprimento:prop}
Let $\{U_i\}_{i\in I}$ be a countable, locally finite open covering of $X$ and for any $i\in I$ let $\mu_i$ be a locally finite Borel measure on $U_i$. If $\mu_i|_{U_i\cap U_j} = \mu_j|_{U_i\cap U_j}$ for all $i,j\in I$ there is a unique locally finite Borel measure  $\mu$ on $X$ whose restriction to $U_i$ is $\mu_i$ for all $i$.
\end{prop}
\begin{proof}
For every finite subset $J\subset I$ we define 
$$X_J = \big(\cap_{j\in J} U_j\big) \setminus \big(\cup_{i\in I\setminus J} U_i\big).$$ 
The sets $X_J$ form a countable partition of $X$ into Borel sets and every $X_J$ is equipped with a measure $\mu_J = \mu_j|_{X_j}$ for any $j\in J$. Define $\mu$ by setting
$$\mu(S)= \sum_{j\in J} \mu(S\cap X_j)$$
on any Borel $S\subset X$. 
\end{proof}

When $X$ is a reasonable space some hypothesis may be dropped.

\begin{prop} \label{ricoprimento2:prop}
If $X$ is paracompact and separable, Proposition \ref{ricoprimento:prop} holds for any open covering $\{U_i\}_{i\in I}$.
\end{prop}
\begin{proof}
By paracompactness and separability the open covering $\{U_i\}$ has a refinement that is locally finite and countable: apply Proposition \ref{ricoprimento:prop} to the refinement to get a measure $\mu$. To prove that indeed $\mu|_{U_i} = \mu_i$ apply Proposition \ref{ricoprimento:prop} again to the covering of $U_i$ given by the refinement.
\end{proof}


\subsection{Topology on the measures space} \label{topology:measure:subsection}
In what follows we suppose for simplicity that $X$ is a finite-dimensional topological manifold, although everything is valid in a much wider generality. We indicate by $\calM(X)$ the space of all locally finite Borel measures on $X$ and by $C_c(X)$ the space of all continuous functions $X\to \matR$ with compact support: the space $C_c(X)$ is not a Banach space, but it is a topological vector space.

Recall that the \emph{topological dual} of a topological vector space $V$ is the vector space $V^*$ formed by all continuous linear functionals $V\to \matR$.
A measure $\mu\in\calM(X)$ acts like a continuous functional on $C_c(X)$ as follows
$$\mu\colon f \longmapsto \int_\mu f$$
and hence defines an element of $C_c^*(X)$. A functional in $C_c^*(X)$ is \emph{positive} if it assumes non-negative values on non-negative functions. 

\begin{teo}[Riesz representation] The space $\calM(X)$ may be identified in this way to the subset in $C_c(X)^*$ of all positive functionals. 
\end{teo}

The space $\calM(X)$ in $C_c(X)^*$ is closed with respect to sum and product with a positive scalar.
We now use the embedding of $\calM(X)$ into $C_c(X)^*$ to define a natural topology on $\calM(X)$.

\begin{defn}
Let $V$ be a real topological vector space. Every vector $v\in V$ defines a functional in $V^*$ as $f\mapsto f(v)$. The \emph{weak-* topology} on $V^*$ is the weakest topology among those where these functionals are continuous.
\end{defn}

We give $C_c(X)^*$, and hence $\calM(X)$, the weak-* topology. 


\subsection{Sequences of measures} \label{mu:sequence:subsection}
By definition, a sequence of measures  $\mu_i$ converges to $\mu$ if and only if $\int_{\mu_i} f \to \int_\mu f$ for any $f\in C_c(X)$. This type of weak convergence is usually denoted with the symbol
$\mu_i \rightharpoonup \mu$.
 
\begin{ex} 
Let $x_i$ be a sequence of points in $X$ that tend to $x\in X$: we get $\delta_{x_i} \rightharpoonup \delta_x$. 
\end{ex}

It is important to note that $\mu_i \rightharpoonup \mu$ does \emph{not} imply $\mu_i(U) \to \mu(U)$ for any open (or closed) set $U$: consider for instance a sequence $\mu_i = \delta_{x_i}$ with $x_i$ exiting from (or entering into) the set $U$. We can get this convergence on compact sets if we can control their topological boundary.

\begin{prop} \label{delta:zero:prop}
Let $K\subset X$ be a Borel compact subset. If $\mu_i \rightharpoonup \mu$ and $\mu(\partial K)=0$ then $\mu_i(K) \to \mu(K)$.
\end{prop}

On Banach spaces, the unitary ball is compact in the weak-* topology. Here $\calM(X)$ is not a Banach space, but we have an analogous compactness theorem.

\begin{teo} \label{compact:measure:teo}
A sequence of measures $\mu_i$ such that $\mu_i(K)$ is bounded on every Borel compact set $K\subset X$ converges on a subsequence.
\end{teo}
