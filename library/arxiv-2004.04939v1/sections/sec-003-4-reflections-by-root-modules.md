---
doc_id: arxiv-2004.04939v1
doc_title: "BRAID GROUP ACTION ON THE MODULE CATEGORY OF"
section_id: sec-003-4-reflections-by-root-modules
section_title: "Reflections by root modules"
section_number: 4
pages: 8-8
source_pdf: 2004.04939v1.pdf
source_sha256: 59a06f9f7d97cad2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.981
doc_brief: "BRAID GROUP ACTION ON THE MODULE CATEGORY OF — Let g0 be a simple Lie algebra of type ADE and let U ′ q(g) be the corre- sponding untwisted quantum aﬃne algebra."
---
Recall that for each pair of non-zero modules $(X,Y)$ of $\catA$, there exists a distinguished nonzero morphism $\rmat{X,Y}\col t^{\Lambda(X,Y)}X \conv Y \to Y \conv X$ called the \emph{r-matrix} (\cite{KKK18A}). 
Here, $t$ is the grading shift functor.
We have 
${\Omega_N(\rmat{X,Y}}) \col t^{\Lambda_N(X,Y)}X \star Y \to Y \star X$ in $\T_N$,
where  $\Lambda_N(X,Y) = \Lambda(X,Y)-B(\wt(X),\wt(Y)) + B(\wt(Y),\wt(X))$.

For a pair $(X,Y)$ of objects in $\T_N$, set $$\de(X,Y)\seteq\dfrac{1}{2}(\Lambda_N(X,Y) + \Lambda_N(Y,X)).$$
Note that $\de(X,Y)= \dfrac{1}{2}(\Lambda(X,Y) + \Lambda(Y,X))$ if $\Omega(\rmat{X,Y}) \neq 0$.

A simple object $X$ in an abelian monoidal category is called \emph{real} if $X\tens X$ is  simple.
A real simple object $L$ in $\T_N$ is called a \emph{root module} if 
\eqn 
\de(L, \D^k(L)) =\delta(k =\pm1).
\eneqn
For example, the objects $L(a,b)$ with $b-a+1 < N$ are  root modules. 
If $L$ is a root module, then $\D(L)$, $\D^{-1}(L)$ and $\Refl_i(L)$ for $i\in \Z$ are  root modules.









The following is the main theorem of this section.
\begin{theorem} \label{thm:S_i(X)}
Let $X$ be a simple object in $\T_N$.
For $i\in \Z$, if 
\eqn \de(\D^k(L(i)), X) =n \delta(k=a)\eneqn
for some $n\ge 0$ and $a \in \Z$, then
$$\Refl_i (X) \simeq (\D^a L(i))^{\circ n} \hconv X$$
up to a multiple of a power of $t$.
\end{theorem}

The following is 
one of  the applications of Theorem \ref{thm:S_i(X)}.
\begin{theorem} \label{thm: reflection by root modules}
Let $[L]$ belongs to the orbit of $L(i)$ for some $1\le i\le N-1$
under the braid group $B(A_{N-1})$ action in Theorem~\ref{thm: braid group action}. 
Then there is an automorphism $s_L$ on $K(\T_N)$ such that
\bnum
\item $s_{L(i)} = s_i$ for $1\le i\le N-1$.
\item $s_{(s_{L}(L'))} =s_L \circ s_{L'} \circ s_{L}^{-1}$ if $L'$ also satisfies the condition in the theorem.
\item $s_{\D^a L} =s_{L}$ for all $a \in \Z$
\item $s_{L}([X]) = [(\D^{a} L )^{\circ n} \hconv X]$ up to a power of $t$, 
if $\de(\D^k L, X) = n\delta(k=a)$ for some $n\ge 0$ and $a \in \Z$.
\end{enumerate}
\end{theorem}
