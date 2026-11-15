---
doc_id: arxiv-1606.01832v3
doc_title: "FLATNESS AND COMPLETION REVISITED"
section_id: sec-003-3-a-adic-flatness
section_title: "a-Adic Flatness"
section_number: 3
pages: 9-12
source_pdf: 1606.01832v3.pdf
source_sha256: da982c95b9674382
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.956
doc_brief: "FLATNESS AND COMPLETION REVISITED — We continue investigating the interaction between ﬂatness and a- adic completion for inﬁnitely generated A-modules."
---
\label{sec:adic-flatness} 

In this section we prove Theorem \ref{thm:168}, that 
characterizes adically flat modules.
As before, $A$ is a commutative ring and $\a$ is an ideal in it. 
We denote by $\cat{D}(A) = \cat{D}(\cat{Mod} A)$ the unbounded derived category 
of $A$. 

Let us first recall the notion of $\a$-torsion. An element $m$ in an $A$-module 
$M$ is called an {\em $\a$-torsion element} if $m$ is annihilated by some power 
of the ideal $\a$. The {\em $\a$-torsion submodule} $\Ga_{\a}(M)$ of $M$ is the 
submodule consisting of all $\a$-torsion elements. Thus 
\begin{equation} \label{eqn:210}
\Ga_{\a}(M) = \lim_{k \to} \, \opn{Hom}_A(A_k, M) \, ,
\end{equation}
where $A_k = A / \a^{k + 1}$ as before.
The module $M$ is called an {\em $\a$-torsion module} if $\Ga_{\a}(M) = M$.

It might be good to mention that if the ideal $\a$ is nilpotent, then all 
$A$-modules are both $\a$-torsion and $\a$-adically complete. Thus the 
discussion is only interesting when the ideal $\a$ is not nilpotent. 

\begin{dfn} \label{dfn:210}
Let $A$ be a commutative ring, let $\a$ be an ideal in $A$, and 
let $M$ be an $A$-module. We say that $M$ is {\em $\a$-adically flat} if 
$\opn{Tor}^{A}_i(N, M) = 0$
for every $\a$-torsion $A$-module $N$ and every $i > 0$. 
\end{dfn}

Here is a useful characterization of adic flatness. It holds in general -- no 
finiteness or completeness assumptions are needed on $A$, $\a$ or $M$. 

\begin{thm} \label{thm:168}
Let $A$ be a commutative ring, let $\a$ be an ideal in $A$, and 
let $M$ be an $A$-module. The following three conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} The $A$-module $M$ is $\a$-adically flat.

\rmitem{ii} For every $i > 0$ and $k \geq 0$ the module 
$\opn{Tor}^{A}_i(A_{k}, M)$ vanishes, and   
$A_{k} \ot_A M$ is a flat $A_k$-module.

\rmitem{iii} For every $i > 0$ the module 
$\opn{Tor}^{A}_i(A_{0}, M)$ vanishes, and   
$A_{0} \ot_A M$ is a flat $A_0$-module.
\end{enumerate}
\end{thm}

\begin{proof}
In terms of derived functors we have 
\[ \opn{Tor}^{A}_i(N, M) = \opn{H}^{-i}(N \ot_{A}^{\mrm{L}} M) \]
as $A$-modules.  Thus $M$ is $\a$-adically flat if and only if for every 
$\a$-torsion $A$-module $N$, and every $i > 0$, we have 
$\opn{H}^{-i}(N \ot_{A}^{\mrm{L}} M) = 0$.
This is equivalent to the condition that the canonical morphism 
\[ N \ot_A^{\mrm{L}} M \to N \ot_A M \]
in $\cat{D}(A)$ is an isomorphism.
Let us write $M_k := A_k \ot_A M$. 

\medskip \noindent 
(i) $\Rightarrow$ (ii): Since $A_k$ itself is an $\a$-torsion $A$-module, the 
modules $\opn{Tor}^{A}_i(A_{k}, M)$ vanish for $i > 0$. 
Thus there is an isomorphism 
$M_k \cong A_k \ot_A^{\mrm{L}} M$ in $\cat{D}(A_k)$.

It remains to prove that $M_k$ is flat over $A_k$. 
Take some $A_k$-module $N$. 
By the associativity of derived tensor products we have isomorphisms 
\[ N \ot_{A_k}^{\mrm{L}} M_k \cong 
N \ot_{A_k}^{\mrm{L}} A_k \ot_{A}^{\mrm{L}} M \cong
N \ot_{A}^{\mrm{L}} M  \]
in $\cat{D}(A_k)$. But $N$ is an $\a$-torsion module, so by our assumption we 
have \lb 
$\opn{H}^{-i}(N \ot_{A}^{\mrm{L}} M) = 0$ for all $i > 0$. 
Therefore 
$\opn{H}^{-i}(N \ot_{A_k}^{\mrm{L}} M_k) = 0$ for all $i > 0$. 


\medskip \noindent 
(ii) $\Rightarrow$ (i): Since for every $i$ the functor 
$\opn{Tor}^{A}_i(-, M)$
commutes with arbitrary direct limits, it suffices to check the vanishing of
$\opn{Tor}^{A}_i(N, M) = 0$
when $N$ is a finitely generated $\a$-torsion $A$-module. But then $N$ is an 
$A_k$-module for some $k$. By assumption $M_k$ is flat over $A_k$, and 
$A_k \ot_A^{\mrm{L}} M \cong M_k$ in $\cat{D}(A)$. 
Then there are isomorphisms 
\[ N \ot_{A}^{\mrm{L}} M \cong 
N \ot_{A_k}^{\mrm{L}} A_k \ot_{A}^{\mrm{L}} M \cong 
N \ot_{A_k}^{\mrm{L}} M_k \cong N \ot_{A_k} M_k  \]
in $\cat{D}(A)$. It follows that 
$\opn{H}^{-i}(N \ot_{A} M) = 0$ for all $i > 0$. 

\medskip \noindent 
(ii) $\Rightarrow$ (iii): This is trivial. 

\medskip \noindent 
(iii) $\Rightarrow$ (ii): We will use induction on $k$: 
assuming that (ii) holds for $k$, we will prove it for $k + 1$. 
For $k = 0$ this is given. 

Let $N$ be an $A_{k + 1}$-module. Define $N' := \a \cd N \subseteq N$ and
$N'' := N / N'$.  We get an exact sequence 
\[ 0 \to N' \to N \to N'' \to 0 \]
of $A_{k + 1}$-modules, that we view as a distinguished triangle
\begin{equation} \label{eqn:211}
N' \to N \to N'' \xar{\vartriangle} 
\end{equation}
in $\cat{D}(A_{})$. 
Now the modules $N'$ and $N''$ are annihilated by $\a^{k + 1}$, so they are in 
fact $A_k$-modules. By our assumption 
$A_k \ot_{A}^{\mrm{L}} M \cong M_k$ in $\cat{D}(A_{k})$, and $M_k$ is a flat 
$A_k$-module. So we have isomorphisms
\begin{equation} \label{eqn:220}
N' \ot_{A}^{\mrm{L}} M \cong 
N' \ot_{A_k}^{\mrm{L}} A_k \ot_{A}^{\mrm{L}} M \cong 
N' \ot_{A_k}^{\mrm{L}} M_k \cong N' \ot_{A_k} M_k 
\end{equation}
in $\cat{D}(A_{k})$. The same for $N''$. Thus, upon application of the 
functor 
$- \ot_{A}^{\mrm{L}} M$
to the distinguished triangle (\ref{eqn:211}), we obtain the 
distinguished triangle
\begin{equation} \label{eqn:212}
N' \ot_{A_k} M_k \to N \ot_{A}^{\mrm{L}} M 
\to N'' \ot_{A_k} M_k \xar{\vartriangle}  
\end{equation}
in $\cat{D}(A)$.
We conclude that 
$\opn{H}^{-i}(N \ot_{A}^{\mrm{L}} M) = 0$
for all $i > 0$. In particular, taking $N = A_{k + 1}$, this tells us that 
$\opn{H}^{-i}(A_{k + 1} \ot_{A}^{\mrm{L}} M) = 0$
for all $i > 0$, and that \lb 
$A_{k + 1} \ot_{A}^{\mrm{L}} M \cong M_{k + 1}$
in  $\cat{D}(A_{k + 1})$.

It remains to prove that $M_{k + 1}$ is flat over $A_{k + 1}$. Again we take an 
arbitrary \lb $A_{k + 1}$-module $N$, and examine the distinguished triangle 
(\ref{eqn:211}), but now it is in the category $\cat{D}(A_{k + 1})$. Using the 
isomorphisms from (\ref{eqn:220}) we obtain these isomorphisms
\[ N' \ot_{A_{k + 1}}^{\mrm{L}} M_{k + 1} \cong
N' \ot_{A_{k + 1}}^{\mrm{L}} A_{k + 1} \ot_{A_{}}^{\mrm{L}} M_{} \cong
N' \ot_{A_{}}^{\mrm{L}} M_{} \cong N' \ot_{A_k} M_k \]
in $\cat{D}(A_{k + 1})$. The same for $N''$.
Therefore, when we apply the functor 
$- \ot_{A_{k + 1}}^{\mrm{L}} M_{k + 1}$
to (\ref{eqn:211}), we obtain the distinguished triangle 
\[ N' \ot_{A_k} M_k \to N \ot_{A_{k + 1}}^{\mrm{L}} M_{k + 1}
\to N'' \ot_{A_k} M_k \xar{\vartriangle} \]
$\cat{D}(A_{k + 1})$.
We see that 
$\opn{H}^{-i}(N \ot_{A_{k + 1}}^{\mrm{L}} M_{k + 1}) = 0$
for all $i > 0$. 
\end{proof}

\begin{rem} \label{rem:310}
Theorem \ref{thm:168} is similar to \cite[Lemma 051C]{SP}. The latter says that
if \lb $\opn{Tor}^{A}_1(A_0, M) = 0$ and $M_0$ is flat over $A_0$, then 
$M_k$ is flat over $A_k$ for all $k$, and 
$\opn{Tor}^{A}_1(N, M) = 0$
for every $\a$-torsion $A$-module $N$.
It seems that this condition on $M$ is strictly weaker than being $\a$-adically 
flat; but we did not look for an example demonstrating this.
\end{rem}

\begin{prop} \label{prop:250}
Let $A$ be a commutative ring, let $\a$ be an ideal in $A$, and 
let $M$ be an $\a$-adically flat $A$-module. Then the canonical morphism 
$\mrm{L} \La_{\a}(M) \to \La_{\a}(M)$
in $\cat{D}(A)$ is an isomorphism. 
\end{prop}

\begin{proof}
Let
\begin{equation} \label{eqn:280}
\cdots P^{-1} \to P^0 \xar{\eta} M \to 0 
\end{equation}
be a flat resolution of the module $M$. We can view this as a quasi-isomorphism 
of complexes $\eta : P \to M$.
Then the completion 
$\La_{\a}(\eta) : \La_{\a}(P) \to \La_{\a}(M)$
represents the canonical morphism 
$\mrm{L} \La_{\a}(M) \to \La_{\a}(M)$. 
We are going to prove that $\La_{\a}(\eta)$ is a quasi-isomorphism. 

For every $k \in \N$, applying $A_k \ot_A -$ to (\ref{eqn:280}), there is a 
sequence 
\begin{equation} \label{eqn:251}
 \cdots A_k \ot_A P^{-1} \to A_k \ot_A P^0 \xar{\eta_k} A_k \ot_A M \to 0 .
\end{equation}
The complex 
$A_k \ot_A P$ represents $A_k \ot_{A}^{\mrm{L}} M$.
Because $M$ is $\a$-adically flat, we see that 
$\opn{H}^{-i}(A_k \ot_A P) = 0$ for all $i > 0$. Therefore the sequence 
(\ref{eqn:251}) is exact. The Mittag-Leffler argument (see 
\cite[Proposition 1.12.4]{KS}) says 
that the inverse limit of the sequences (\ref{eqn:251}) is also exact.
But then 
$\La_{\a}(\eta) : \La_{\a}(P) \to \La_{\a}(M)$
is a quasi-isomorphism. 
\end{proof}

\begin{rem} \label{rem:500}
Let $\a$ be a finitely generated ideal in a commutative ring $A$.
Our $\a$-adically flat modules are very close to the {\em flat contramodules} 
that were introduced in \cite{Po1}, \cite{PoRo}. 
According to Positselski, an $A$-module $M$ is called a contramodule if it 
is $\a$-adically cohomologically complete in the sense of \cite{PSY1}, namely if 
the canonical morphism $M \to \mrm{L} \La_{\a}(M)$ in $\cat{D}(A)$ is an 
isomorphism. A contramodule $M$ is called a flat contramodule if each 
$M_k := A_k \ot_A M$ 
is a flat $A_k$-module. Thus, by our Theorem \ref{thm:262}(1) and Proposition 
\ref{prop:250}, if $M$ is an $\a$-adically complete $A$-module and the ideal 
$\a$ is weakly proregular, then $M$ is an $\a$-adically flat module iff it is a 
flat contramodule.
We thank L. Positselski for mentioning this to us. 
\end{rem}

\begin{rem} \label{rem:501}
Let $\a$ be a finitely generated ideal in a commutative ring $A$.
Denote by $\cat{Mod}_{\a\tup{-tor}} A$ the subcategory of $\a$-torsion 
modules. Let $M$ be an $\a$-adically complete $A$-module.
It is easy to see that if $M$ is $\a$-adically flat, then $M$ is {\em flat 
relative to the subcategory $\cat{Mod}_{\a\tup{-tor}} A$}, i.e.\ the functor 
\begin{equation} \label{eqn:500}
M \ot_A - : \cat{Mod}_{\a\tup{-tor}} A \to 
\cat{Mod}_{\a\tup{-tor}} A 
\end{equation}
is exact. The converse is true if the ideal $\a$ is weakly proregular,
by Theorem \ref{thm:262}(1). But what if $\a$ is not weakly proregular? 

Surprisingly, the converse does not hold without weak proregularity. 
Here is the precise statement, communicated to us privately by Positselski (and 
can be proved using ideas in his paper \cite{Po2}). 
Let $P$ be the $\a$-adic completion of the free $A$-module of countable rank; 
so in the notation of Section \ref{sec:decay} we have 
$P = \opn{F}_{\mrm{dec}}(\N, \what{A})$.
Since $A_k \ot_A P$ is a free $A_k$-module (cf.\ Proposition \ref{prop:500}), it 
follows that the $A$-module $P$ 
is flat relative to the subcategory $\cat{Mod}_{\a\tup{-tor}} A$. 
However, Positselski claims that {\em if the $A$-module $P$ is $\a$-adically 
flat, then the ideal $\a$ is weakly proregular}. 
\end{rem}
