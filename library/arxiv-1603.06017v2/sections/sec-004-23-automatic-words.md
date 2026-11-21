---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-004-23-automatic-words
section_title: "Automatic Words"
section_number: 2.3
pages: 6-7
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.984
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:automatic words}
An automatic word $W=(a_i)_{i\geq 0}$ is a word in $\Sigma^\omega$ for
which there exists a number system $\mathbf{S}$ and an automaton with
output $M\big(Q,q_0,O,\delta,\Sigma,\mathbf{S}\big)$ for which reading
$x\in R_{\mathbf{S}}$ outputs $W[[x]_\mathbf{S}] = a_{[x]_\mathbf{S}
}$. In other words, for an automatic word, the symbol at position $i$
for all $i$ can be effectively computed by running an automaton with
output on any single representation of $i$ in a number system. As usual
we assume $\Sigma$ is a finite subset of $\mathbb{Z}$.

The word $T$ for which the symbol at position $i$, is the number of $1$s in any binary representation of $i$, modulo $2$, is called the Thue-Morse word. The Thue-Morse word is well-defined since all the infinitely many different binary representations of an integer have the same number of $1$'s. It is instantly clear that $T$ is an automatic word over $\MSD[2]$ if one notes the automaton with output in Figure \ref{fig:thue}.
\begin{figure}[h]
	\centering
	\includegraphics[scale=.6]{Thue}
	\caption{The Thue-Morse word}
	\label{fig:thue}
\end{figure}

In the introduction, we mentioned that Walnut decides some properties of automatic words. Recall from Section \ref{sec:words and automata} that squares are non-empty words of the form $xx$. It is easy to see that $T$ has square subwords. The following predicate captures this property:
$$\exists{i} \exists{n} \forall{j}, j<n \implies T[i+j]=T[i+n+j].$$

Walnut provides a decision procedure that takes predicates like this
and decides whether they are true or false. Walnut does so, by
constructing automata for every subpredicate in the predicate above;
see Section \ref{sec:automata accepting predicates} for more details.
It starts by constructing from the automaton in Figure \ref{fig:thue}
an automaton $M_1\big(Q,q_0,F,\delta,\MSD[2],\MSD[2],\MSD[2]\big)$ for
subpredicate $P_1\coloneqq T[i+j]=T[i+j+n]$. This means (see Section
\ref{sec:automata accepting predicates}) that $M_1$ is constructed so
that it accepts tuples $t=(w_1,w_2,w_3)$ if and only if
$|w_1|=|w_2|=|w_3|$ and substitutions $i=[w_1]_{\MSD[2]}$,
$j=[w_2]_{\MSD[2]}$, and $n=[w_3]_{\MSD[2]}$ are satisfying $P_1$.
Walnut then using $M_1$ constructs an automaton $M_2$ for
$P_2\coloneqq\forall{j}, j < n \implies T[i+j]=T[i+n+j]$. The automaton
$M_2$ takes two inputs representing the two free variables $i$ and $n$
in $P_2$. Walnut continues by constructing the automaton $M_3$ for
\linebreak$P_3\coloneqq\exists{n} \forall{j}, j < n \implies
T[i+j]=T[i+n+j]$. In the end, Walnut returns true if $M_3$ accepts
anything. The fact that $M_1$,$M_2$, and $M_3$ exist is explained in
Section \ref{sec:automata accepting predicates}. The details of how
Walnut constructs these automata are explained in Section
\ref{sec:decision procedure}. The details of what comprises a valid
predicate is explained in Section \ref{sec:syntax and semantic}. To see
more examples of the properties of the Thue-Morse word and their proofs
see Section \ref{sec:eval}.

We can extend the definition of automatic words to higher dimensions.
The ($n$-dimensional) automatic word
$$W=\big(a_{i_1,i_2,\ldots,i_n}\big)_{i_1\geq 0,i_2\geq 0,\ldots,
i_n\geq 0}$$ is an infinite word over $\Sigma$ for which there
exist number systems $\mathbf{S_j}$ and an automaton with output
$$M\big(Q,q_0,O,\delta,\Sigma,\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}\big)$$
for which reading $x$, such that $\pi_j(x) \in R_{\mathbf{S_j}}$ for
all $j$, outputs
$$W\big[[\pi_1[x]]_{\mathbf{S_1}}\big]\big[[\pi_2[x]]_{\mathbf{S_2}}\big]\cdots\big[[\pi_n[x]]_{\mathbf{S_n}}\big]
=
a_{[\pi_1[x]]_{\mathbf{S_1}},[\pi_2[x]]_{\mathbf{S_2}},\ldots,[\pi_n[x]]_{\mathbf{S_n}}}.$$
