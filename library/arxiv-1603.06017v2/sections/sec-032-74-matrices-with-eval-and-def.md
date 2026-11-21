---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-032-74-matrices-with-eval-and-def
section_title: "Matrices with eval and def"
section_number: 7.4
pages: 29-29
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
We postponed discussing the exact syntax of the eval and def commands until this section. These two commands can take an optional argument:
\begin{itemize}
	\item eval <name> <space separated list of free variables>? <predicate> 
	\item def <name> <space separated list of free variables>? <predicate>
\end{itemize}

The question marks are representing the fact that the corresponding arguments are optional. When a list of free variables is preset, in addition to the ordinary computation, Walnut will calculate the \emph{incidence matrices} of the underlying graph of the computed automaton, corresponding to the transitions labeled by the listed free variables. It stores the matrices in the Maple syntax in a .mpl file in ``/Walnut/Result/'' directory.

Suppose $M\big(Q,q_0,F,\delta,\mathbf{S_1},\ldots,\mathbf{S_m}\big)$ is the automaton calculated for the predicate $(x_1,\ldots,x_n):P'$. For a free variable $x_i$ and a value $v \in \Sigma_{\mathbf{S_i}}$, we let $M\_x_i\_v$ denote the $|Q|\times |Q|$ matrix where the entry $M\_x_i\_v[p][q]$\footnote{$M\_x_i\_v[p][q]$ denotes the entry at $p$th row and $q$th column.}, for every pair of states $p$ and $q$,  is the number of tuples transitioning from $p$ to $q$ with $v$ in the $i$'th coordinate, or more formally
$$M\_x_i\_v[p][q] = \left|\left\{\left(\alpha_1,\ldots,\alpha_i,\ldots,\alpha_m\right): \delta\left((\alpha_1,\ldots,\alpha_i,\ldots,\alpha_m),p\right)=q \text{ such that } \alpha_i=v \text{ and } \alpha_j\in  \Sigma_{\mathbf{S_j}} \text{ for } j\neq i \right\}\right|.$$

We already saw in Figure \ref{fig:two inputs} an automaton accepting $b=a+1$. Now writing
\begin{lstlisting}[style=cmd]
eval example a "b=a+1";
\end{lstlisting}
causes Walnut to calculate the matrices $M\_a\_0$ and $M\_a\_1$:

\[
M\_a\_0 = 
\begin{bmatrix}
1 & 1 \\
0 & 0
\end{bmatrix}
\]
\[
M\_a\_1 =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\]

In the same command, we could ask Walnut to calculate the incidence matrices for $b$ as well as $a$ by writing:
\begin{lstlisting}[style=cmd]
eval example a "b=a+1";
\end{lstlisting}
\[
M\_b\_0 = 
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\]
\[
M\_b\_1 =
\begin{bmatrix}
1 & 1 \\
0 & 0
\end{bmatrix}.
\]

There are a lot of interesting things one can do using incidence matrices.
For example for Fibonacci word, and Sturmian words in general, the number of distinct subwords of length $n$, i.e., subword complexity, is $n+1$. Now can one verify this using Walnut? The answer is yes. Please refer to \cite{fib3} for this and a lot of other interesting applications.
