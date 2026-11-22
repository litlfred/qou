---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-017-41-cross-product
section_title: "Cross Product"
section_number: 4.1
pages: 12-14
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.84
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:cross product}
Let $M\big(Q,q_0,F,\delta,\mathbf{S_1},\ldots,\mathbf{S_m}\big)$ and
$M'\big(Q',q'_0,F',\delta',\mathbf{S'_1},\ldots,\mathbf{S'_n}\big)$ be
the automaton $(x_1,\ldots,x_m):P$ and $(x'_1,\ldots,x'_n):P'$
respectively. Let us assume that if $x_i=x'_j$ then
$\mathbf{S_i}=\mathbf{S'_j}$. Let $\{x''_1,\ldots,x''_p\}$ where $p\leq
m+n$ be the union of $\{x_1,\ldots,x_m\}$ and $\{x'_1,\ldots,x'_n\}$
and further assume that the $x''_i$ are appearing in lexicographic
order. Depending on whether $x''_k=x_i$ or $x''_k=x'_j$, let
$\mathbf{S''_k}$ denote $\mathbf{S_i}$ or $\mathbf{S'_j}$ respectively.
Then the cross product of $M$ and $M'$ denoted by $M\times M'$ is the
tuple $$\big(Q\times
Q',(q_0,q'_0),\delta'',\mathbf{S''_1},\ldots,\mathbf{S''_p}\big)$$
where the transition function is defined to be
$$\delta''\big((q,q'),(\gamma_1,\ldots,\gamma_p)\big)=\big(\delta(q,(\alpha_1,\ldots,\alpha_m)),\delta'(q',(\beta_1,\ldots,\beta_n))\big)$$
for $\gamma_k$ equals $\alpha_i$ or $\beta_j$ depending on whether
$x''_k=x_i$ or $x''_k=x'_j$ respectively. Note that $M\times M'$ is not
an automaton since a set of final states is not specified. For
$F''\subseteq Q\times Q'$, let $(M\times M')(F)$ denote the automaton
$\big(Q\times
Q',(q_0,q'_0),F'',\delta'',\mathbf{S''_1},\ldots,\mathbf{S''_p}\big)$.

\begin{THM}\label{thm:cross product}
For $F'' = \big\{(q,q'):q\in F \text{ and } q'\in F'\big\}$, the
automaton $(M\times M')(F'')$ accepts predicate $P\mathbin{\&}P'$.
Furthermore, minimizing $(M\times M')(F'')$, we obtain automaton
$(x''_1,\ldots,x''_p):P\mathbin{\&}P'$.
\end{THM}

\begin{proof}
Based on the definition for cross product, for $M\times M'$ to be
defined, the same variables in $P$ and $P'$ have to have the same
number systems assigned in $P$ and $P'$. But that is exactly the same
condition that needs to hold for number system annotations in
$P\mathbin{\&}P'$ to be consistent (in the sense defined in the last
bullet in Page \pageref{itm:number_system_declarations}).

Let $t=(w_1,\ldots,w_m)$ and $t'=(w'_1,\ldots,w'_n)$ such that $w_i \in
\Sigma_{\mathbf{S_i}}^*$ and $w'_j\in\Sigma_{\mathbf{S'_j}}^*$ where
$|w_i|$ and $|w'_j|$ are all equal and $w_i=w'_j$ whenever $x_i=x'_j$.
Let $t''=(w''_1,\ldots,w''_p)$ such that $w''_k=w_i$ or $w''_k=w'_j$
depending on whether $x''_k=x_i$ or $x''_k=x'_j$.

We have the following equivalent statements:
\begin{enumerate}
\item $(M\times M')(F'')$ accepts $t''$.
\item There is a path from $(q_0,q'_0)$ to $(q,q')\in F''$ in $M\times M'$ reading $t''$.
\item There is a path from $q_0$ to $q$ in $M$ reading $t$, and there is a path from $q'_0$ to $q'$ in $M'$ reading $t'$.
\item $M$ accepts $t$ and $M'$ accepts $t'$.
\item $P$ is satisfied by substituting $x_i=[w_i]_{\mathbf{S_i}}$ for all $i$, and $P'$ is satisfied by substituting $x'_j=[w'_j]_{\mathbf{S'_j}}$ for all $j$.
\item $P\mathbin{\&}P'$ is satisfied by substituting $x''_k=[w''_k]_{\mathbf{S''_k}}$.
\end{enumerate}
\end{proof}

Obviously both the construction of cross product and minimizing
automata can be carried out using algorithmic procedures. Therefore
Theorem \ref{thm:cross product} gives us a procedure for constructing
the automaton for conjunction.

With proper definitions for $F''$, we have similar theorems for
$P\otimes P'$ when $\otimes$ is any other binary logical operator.

Let us construct the automaton $(a,b):a=1\mathbin{\&}b=2$ from $(a):a=1$ in
Figure \ref{fig:one} and $(b):b=2$ in Figure \ref{fig:two}.

\begin{figure}[h]
\centering
\begin{minipage}[t]{.5\textwidth}
 	\centering
 	\includegraphics[scale=.5]{one}
 	\caption{Automaton $(a):a=1$}
 	\label{fig:one}
\end{minipage}
\begin{minipage}[t]{.5\textwidth}
 	\centering
 	\includegraphics[scale=.5]{two}
 	\caption{Automaton $(b):b=2$}
 	\label{fig:two}
\end{minipage}
\end{figure}
 Recall that transitions not depicted are transitions to a dead state. The
cross product operation is depicted below:
 \begin{figure}[H]
 	\centering
 	\includegraphics[scale=.5]{cross_product}
 	\caption{Cross product $(a):a=1\times(b):b=2$}
 	\label{fig:cross_product}
 \end{figure}
 
Making $(1,2)$ a final state, minimizing, and renaming the states, we get the automaton in Figure \ref{fig:minimized}.
 \begin{figure}[H]
 	\centering
 	\includegraphics[scale=.5]{minimized}
 	\caption{Automaton $(a,b):a=1\mathbin{\&}b=2$}
 	\label{fig:minimized}
 \end{figure}
