---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-034-61-diagrammatics-for-light-leaves
section_title: "Diagrammatics for light leaves"
section_number: 6.1
pages: 57-60
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.972
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-LibedDiag}


Fix a rex ${\un{w}}$. We want to find a basis of diagrams for the space of morphisms $B_{\un{x}} \to B_{\un{w}}$ modulo ``lower terms." Here, lower terms are morphisms which induce the
zero map to the unique standard summand $Q_w \sumset B_{\un{w}}$ after localization. This basis will be parametrized by subsequences $\eb$ of $\un{x}$ which express $w$. Libedinsky
associates a morphism $\LL_{{\un{w}},\eb}$ to $\eb$, although this choice is not canonical. In fact, there are many valid choices for what each $\LL_{{\un{w}},\eb}$ can be, and selecting
one morphism for each $\eb$ will give a basis modulo lower terms. Thus we will give a general rubric for selecting $\LL_{{\un{w}},\eb}$, which does not specify a single map but a set of
maps, any of which will suffice. See Remark \ref{LLprecision} below on how to be more specific.

Recall that a rex move is a morphism constructed from $2m$-valent vertices which corresponds to a path in the reduced expression graph of some element $w \in W$. Rex moves have degree $0$.
When the realization is unbalanced, there is an ambiguity when defining the rex move associated to a path, which amounts to an invertible scalar. This scalar will be irrelevant for our
discussion below: a rescaled basis is a basis still. However, we use the convention that rex moves always preserve the 1-tensor.

\begin{constr} For every $({\un{x}},\eb)$ expressing $w$ and every $k \le \ell({\un{x}})$, we let $({\un{x}}_{\le k},\eb_{\le k})$ be the first $k$ terms, expressing an element $w_k$, and let ${\un{x}}_{> k}$
denote the remaining terms. When ${\un{x}}$ is the empty set and $\eb$ its unique subsequence, the map $\LL_{{\un{w}},\eb}$ is the empty diagram. Suppose that, by induction, we have already chosen  a map $\LL_{k-1} \define \LL_{{\un{x}}_{\le k-1},\eb_{\le k-1}} \co B_{{\un{x}}_{\le k-1}} \to B_{{\un{w}}_{k-1}}$ for some rex ${\un{w}}_{k-1}$ of $w_{k-1}$. Suppose that the next index ${\un{x}}_k$ is $s$. By
placing a vertical line $\1_{s}$ next to $\LL_{{\un{x}}_{\le k-1},\eb_{\le k-1}}$ we get a map from $B_{{\un{x}}_{\le k}} \to B_{{\un{w}}_{k-1}} \ot B_s$. We will now choose a map $\phi_k \co
B_{{\un{w}}_{k-1}} \ot B_s \to B_{{\un{w}}_k}$ for some rex ${\un{w}}_k$ of $w_k$. The composition will be $\LL_k \define \LL_{{\un{x}}_{\le k},\eb_{\le k}}$.

It follows that $\LL_{{\un{w}},\eb}$ is a composition $\phi_{\ell({\un{w}})} \circ \phi_{\ell({\un{w}})-1} \ot \1 \circ \cdots \circ \phi_1 \ot \1$, where at the $k$-th step $\1$ denotes the
identity map of $B_{{\un{w}}_{> k}}$. The composition of the first $k$ terms is $\LL_k \ot \1_{B_{{\un{w}}_{>k}}}$.

\begin{equation} \label{LLinduction} \ig{1}{LLinduction} \end{equation}

There are four possibilities for the map $\phi_k$, depending on $\eb_k$. To obtain $\phi_k$ follow these three steps (see also figure \ref{fourmaps}):

\begin{itemize} \item If $\eb_k$ is either U1 or U0, do nothing. If $\eb_k$ is either D0 or D1, then $s$ is in the right descent set of $w_{k-1}$. Apply $\b \ot \1_{B_s}$, where $\b$ is
some rex move from ${\un{w}}_{k-1}$ to a rex with $s$ on the right. Now the top has $B_s \ot B_s$ on the far right.

\item If $\eb_k$ is U1 do nothing. If $\eb_k$ is U0, apply a dot to the rightmost $B_s$. If $\eb_k$ is D1, apply a cap to the final $B_s \ot B_s$. If $\eb_k$ is D0, apply a merging
trivalent vertex to the final $B_s \ot B_s$.

\item We have now reached some reduced expression for $w_k$. Now apply some rex move $\a$ to get to the desired rex ${\un{w}}_k$. \end{itemize} \end{constr}

\begin{figure}  \caption{The Four Maps} $\ig{1}{wisemap1} \ig{1}{wickedmap1} \ig{1}{simplemap1} \ig{1}{noaskmap1}$ \label{fourmaps} \end{figure}

As expected, the degree of the morphism $\LL_{{\un{w}},\eb}$ is $+1$ for each U0 and $-1$ for each D0 and hence agrees with defect of $\eb$.
Note also that the width (i.e. number of strands) always weakly decreases from bottom to top in an $\LL$ map.

\begin{ex} Here is a possible map $\LL_{\un{w},\eb}$ for $\un{w}=rbrgbrr$ with $m_{br}=3$ and $m_{bg}=m_{gr}=2$, and for $\eb = 1111010$. \igc{1}{LLexample} \end{ex}

\begin{remark} \label{LLprecision} Clearly there are many choices in this construction. The first important choice is which rex ${\un{w}}$ is the final target. If one is to compare
$\LL_{{\un{x}},\eb}$ with $\LL_{{\un{x}},\fb}$ for two subsequences $\eb,\fb$ both expressing $w$, then they should have the same target ${\un{w}}$, and this is generally assumed. However, at each step
in the inductive construction one needs to choose a rex ${\un{w}}_k$, and there is no particular need to be consistent with this choice. For instance, the intermediate map $LL_k$ in the
construction of $\LL_{{\un{x}},\eb}$ need not equal the map we constructed for $\LL_{{\un{x}}_{\le k},\eb_{\le k}}$. There is even no need for the intermediate rex ${\un{w}}_k$ to agree with the final
target for the chosen map $\LL_{{\un{x}}_{\le k},\eb_{\le k}}$. When $\eb_k$ is D0 or D1, one has a free hand to choose which rex with $s$ on the right will be factored through, and which rex
move $\b$ will take us there. The rex move $\a$ is also freely chosen, and by no means does it have to be the shortest or easiest way to traverse the reduced expression graph $\G_w$.

To be absolutely precise, i.e. to make the above construction into an algorithm, one should fix once and for all the following data: \begin{enumerate} \item For each $w \in W$, a rex
${\un{w}}$. \item For each $w \in W$ and each index $s \in \SC$ in the \emph{right descent set} of $w$, a rex ${\un{w}}_s$ which ends in $s$. \item For any two rexes ${\un{w}}_1$ and ${\un{w}}_2$ in for $w$, a rex move from ${\un{w}}_1$ to ${\un{w}}_2$. \end{enumerate} This is not the only way to make the algorithm precise.

The more precise one is, the more annoying certain statements get. Flexibility will be more useful. However, at some point (in the final chapter) we will have to show how one set of
choices ``spans" all the other possible choices. \end{remark}

\begin{remark} \label{LLof111} When $\eb=(1,1,\ldots,1)$, it is a sequence of all U1 precisely when ${\un{w}}$ is a reduced expression. If so, the set of possible $\LL_{{\un{w}},\eb}$ is precisely
the set of rex moves. The most convenient choice is for $\LL_{{\un{w}},\eb}$ to be the identity map.

Now suppose that $({\un{w}},\eb)$ has length $k$, and the first $k-1$ terms are all U1, a rex for $w_{k-1}$. In the construction of $\LL_{{\un{w}},\eb}$ we may choose $\LL_{k-1}$ to be the identity
map, meaning that $\LL_{{\un{w}},\eb} = \phi_k$. Thus for any sequence $({\un{w}},\eb)$ the map $\phi_k$ is a valid choice for $\LL_{{\un{w}}',\eb'}$, where ${\un{w}}' = {\un{w}}_{k-1} s$ and $\eb' =
(1,1,1,\ldots,1,\eb_k)$. This observation gives us a different inductive way to look at light leaves: \igc{1}{LLinductionAlt} One should think of the top of an $\LL$ map as being a rex
labelled with all U1's, for the purpose of further $\LL$ maps. \end{remark}

We will write $\LL_{{\un{x}},w}$ to indicate a set consisting of one fixed choice of $\LL_{{\un{x}},\eb}$ for each subexpression $\eb$ of $\un{x}$ expressing $w$. When we speak of the ``span" of  $\LL_{{\un{x}},w}$, we mean all morphisms obtained as linear combinations of $\LL$ maps, with polynomials appearing in the left-most region. Note that $\LL$ maps themselves never have polynomials in any region.

\begin{remark} Not every diagram is in the light leaves basis. Here is a diagram which is not in the light leaves basis, and a description of it as an $R$-linear combination of $\LL$ maps.
\igc{1}{notLLexample1}

Here is a diagram which is not in the span of $\LL$ maps at all, because it factors through ``lower terms."
\igc{1}{notLLexample2}
However, when viewed under adjunction as a map to $\emptyset$, it is an $\LL$ map.
\igc{1}{notLLexample3}
Note that $\emptyset$ has no lower terms, so that $\LL_{{\un{x}},e}$ should genuinely form a basis for
$\Hom_{\DC}(B_{\un{x}},\1)$.
\end{remark}
