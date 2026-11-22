---
doc_id: arxiv-2002.04901v5
doc_title: "Weak Proregularity, Derived Completion, Adic Flatness, and Prisms"
section_id: sec-005-5-weak-proregularity-and-quotient-rings
section_title: "Weak Proregularity and Quotient Rings"
section_number: 5
pages: 15-18
source_pdf: 2002.04901v5.pdf
source_sha256: f1320c4b87229215
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.955
doc_brief: "Weak Proregularity, Derived Completion, Adic Flatness, and Prisms — We begin by recalling the role that weak proregularity of an ideal in a commu- tative ring has in derived completion and adic"
---
Again $A$ is some commutative ring. The purpose of this extremely technical 
section is to prove Theorem \ref{thm:105}. 

\begin{dfn} \label{dfn:106} 
An element $a \in A$ is called a {\em weakly proregular element} 
if the length one sequence $\aa := (a)$ is weakly proregular in $A$.
\end{dfn}

Given an element $a \in A$ and an $A$-module $M$, the {\em annihilator} of $a$ 
in $M$ is the submodule 
\[ \opn{Ann}_M(a) := \opn{Ker} \bigl( \opn{mult}_M(a) \bigr) = 
\{ m \in M \mid a \cd m = 0 \} \sub  M . \]
The element $a$ is called {\em $M$-regular} or a {\em non-zero-divisor on $M$}
if $\opn{Ann}_M(a) = 0$. This means that $\opn{mult}_M(a)$ is an 
injective endomorphism of $M$. When $M = A$ we just call $a$ a {\em regular 
element}. Of course 
\begin{equation} \label{eqn:102}
\opn{Ann}_M(a^i) \sub \opn{Ann}_M(a^j) \sub M
\end{equation}
if $i \leq j$. For such $i, j$ there is a homomorphism 
\begin{equation} \label{eqn:130} 
\opn{mult}_M(a^{j - i}) : \opn{Ann}_M(a^j) \to \opn{Ann}_M(a^i) . 
\end{equation}
Note that $a^0 = 1$, so that $\opn{Ann}_M(a^{0}) = 0$. The element $a$ is 
$M$-regular iff  $\opn{Ann}_M(a^{}) = 0$, iff 
$\opn{Ann}_M(a^{i}) = 0$ for all $i \in \N$.

As can be seen immediately from (\ref{eqn:101}), for every $i \in \N$
there is equality 
\begin{equation} \label{eqn:105}
\opn{Ann}_M(a^i) = \opn{H}^{-1} \bigl( \opn{K}(A; a^{i}) \ot_A M \bigr)
\end{equation}
of submodules of $M$, after we make the obvious identification 
$M \cong A \ot_A M$.

\begin{dfn} \label{dfn:100}
Let $a \in A$ and let $M$ be an $A$-module. We say that $M$ has {\em bounded 
$a$-torsion} if there is some $j_0 \in \N$ such that 
$\opn{Ann}_M(a^{j}) = \opn{Ann}_M(a^{j_0})$ for all $j \geq j_0$.

Let $\opn{tb}_{M}(a)$ be the smallest such number $j_0 \in \N$, if it exists; 
and otherwise let $\opn{tb}_{M}(a) := \infty$. The generalized number
$\opn{tb}_{M}(a) \in \N \cup \{ \infty \}$ is called the {\em torsion bound} of
$a$ on $M$. 

\end{dfn}

Thus $M$ has bounded $a$-torsion iff $\opn{tb}_{M}(a) < \infty$.
Also $a$ is an $M$-regular element iff $\opn{tb}_{M}(a) = 0$. 

The next proposition is well-known, yet we find 
it instructive to give a proof here, since the same ideas will be used in the 
subsequent lemmas.

\begin{prop} \label{prop:100}
Let $a \in A$. The following conditions are equivalent\tup{:}
\begin{itemize}
\rmitem{i} The element $a$ is WPR. 

\rmitem{ii} $A$ has bounded $a$-torsion. 
\end{itemize}
\end{prop}

\begin{proof} \mbox{}

\smallskip \noindent 
(ii) $\Rightarrow$ (i): Let $i_0 := \opn{tb}_{A}(a) \in \N$. 
We must prove that given $i$, there 
exists some $j \geq i$ such that the homomorphism 
\[ \opn{mult}(a^{j - i}) : \opn{Ann}_A(a^j) \to \opn{Ann}_A(a^i) \]
is the zero homomorphism. This just means that $a^{j - i}$ annihilates 
$\opn{Ann}_A(a^j)$; or in other words, taking the inclusion (\ref{eqn:102}) 
into account, that 
$\opn{Ann}_M(a^j) = \opn{Ann}_M(a^{j - i})$.  
By the choice of $i_0$, the number $j := i + i_0$ works. 

\medskip \noindent 
(i) $\Rightarrow$ (ii): By the WPR condition, with $i = 1$, there is some 
$j_0 \in \N$ such that the homomorphism 
\begin{equation} \label{eqn:106}
\opn{mult}(a^{j_0}) : \opn{Ann}_A(a^{j_0 + 1}) \to \opn{Ann}_A(a^1)
\end{equation}
is the zero homomorphism. We will prove that 
$\opn{tb}_{A}(a) \leq j_0$. This will be done as follows: by induction on 
$j \geq j_0$, we will prove that 
$\opn{Ann}_A(a^{j}) = \opn{Ann}_A(a^{j + 1})$. 

\medskip \noindent 
$\triangleright$ \, 
For $j = j_0$ this is simply the vanishing of the homomorphism (\ref{eqn:106}). 

\medskip \noindent 
$\triangleright$ \, Assume this is true for $j \geq j_0$. Consider an 
element $b \in \opn{Ann}_A(a^{j + 2})$. Then 
$a \cd b \in \opn{Ann}_A(a^{j + 1})$. By assumption 
$a \cd b \in \opn{Ann}_A(a^{j})$. Hence $b \in \opn{Ann}_A(a^{j + 1})$.
\end{proof}

\begin{lem} \label{lem:320} 
Let $b \in A$, and let 
\[ 0 \to M' \xar{\ep} M \xar{\pi} M'' \to 0 \]
be a short exact sequence in $\cat{M}(A)$. Then 
$\opn{tb}_{M}(b) \leq \opn{tb}_{M'}(b) + \opn{tb}_{M''}(b)$.
\end{lem}

\begin{proof}
Let's write $l' := \opn{tb}_{M'}(b)$ and $l'' := \opn{tb}_{M''}(b)$; and we may 
assume that $l', l'' < \infty$. 
Given some $j \geq l' + l''$ and some $m \in M$ s.t.\
$b^j \cd m = 0$, we must prove that 
$b^{l' + l''} \cd m = 0$. 

Since $b^j \cd m = 0$ in $M$, it follows that 
$b^j \cd \pi(m) = 0$ in $M''$. Now $j \geq l''$, so by the definition of 
$l'' = \opn{tb}_{M''}(b)$ we have $b^{l''} \cd \pi(m) = 0$ in $M''$.

Define $n := b^{l''} \cd m \in M$. Then $\pi(n) = 0$, i.e.\ 
$n \in \opn{Ker}(\pi)$. Let us identify $\opn{Ker}(\pi) \sub M$ with $M'$ by 
way of $\ep$. We know that $b^j \cd n = b^{j + l''} \cd m = 0$, and that $j 
\geq l'$; so by the definition of $l' = \opn{tb}_{M'}(b)$ it follows that 
$b^{l'} \cd n = 0$ in $M' \sub M$. 

Combining the calculations above we obtain 
$b^{l' + l''} \cd m = b^{l'} \cd n = 0$,
as required. 
\end{proof}


\begin{lem} \label{lem:105}
Let $a, b \in A$. For every $k \in \N$ let $A_k := A / (a^{k + 1})$.
Assume that $a$ is a regular element, and that $A_0$ has bounded $b$-torsion. 
Then $A_k$ has bounded $b$-torsion for every $k$. 
\end{lem}

\begin{proof}
The assumption is that $l := \opn{tb}_{A_0}(b) < \infty$. 
We shall prove that 
\begin{equation} \label{eqn:120}
\opn{tb}_{A_k}(b) \leq (k + 1) \cd l 
\end{equation}
for all $k \geq 0$.
 
Define the ideal $\a := (a) \sub A$.
For  $k \geq 1$ define the $A$-module
\[ N_k := \a^k / \a^{k + 1} \cong \opn{Ker}(A_k \xar{\pi_k} A_{k - 1}) , \]
where $\pi_k : A_k \xar{} A_{k - 1}$ is the $A$-ring homomorphism. 
And let $N_0 := A_0$. 
Since $a$ is a regular element of $A$, it follows that 
$\opn{mult}_A(a) : \a^k \to \a^{k + 1}$
is bijective for all $k \geq 0$; and hence it induces an 
$A$-module isomorphism $N_k \iso N_{k + 1}$. We see that  
$\opn{tb}_{N_k}(b) = l$ for all $k \geq 0 $. 

We shall now prove (\ref{eqn:120}), by induction on $k$.
For $k = 0$ there is nothing to prove.
Next, take any $k \geq 0$, and assume formula (\ref{eqn:120}) holds for $k$. 
Consider the short exact sequence of $A$-modules 
\begin{equation} \label{eqn:121}
0 \to N_{k + 1} \to  A_{k + 1} \xar{\pi_{k + 1}} A_k \to 0 . 
\end{equation}
According to Lemma \ref{lem:320}, applied to this short exact sequence, we 
obtain 
\[ \opn{tb}_{A_{k + 1}}(b) \leq 
\opn{tb}_{N_{k + 1}}(b) + \opn{tb}_{A_{k}}(b) \leq 
l + (k + 1) \cd l = (k + 2) \cd l . \]
This is the inequality (\ref{eqn:120}) for $k + 1$.
\end{proof}

\begin{thm} \label{thm:105}
Let $A$ be a commutative ring, and let $a, b \in A$. Assume that $a$ is 
a regular element of $A$, and the image $\bar{b}$ of $b$ in 
$\mbar{A} := A / (a)$ is a weakly proregular element. Then the length $2$ 
sequence $\aa := (a, b)$ in $A$ is weakly proregular.
\end{thm}

\begin{proof}
The Koszul complexes $\opn{K}(A; \aa^i)$ are concentrated in degrees 
$0, -1, -2$. We need to prove that for $q = -1, -2$ and for  
$i \geq 0$ there exists some $j \geq i$ for which the homomorphism 
\begin{equation} \label{eqn:133}
\opn{H}^q(\mu_{j, i}) : \opn{H}^q \bigl( \opn{K}(A; \aa^j) \bigr) \to
\opn{H}^q \bigl( \opn{K}(A; \aa^i) \bigr) 
\end{equation}
is zero. We will consider all these cases of $q$ and $i$ in three steps. 
We shall use the fact that 
\begin{equation} \label{eqn:134}
\opn{K}(A; \aa^i) = \opn{K}(A; a^i) \ot_A \opn{K}(A; b^i)
\end{equation}
as complexes.

\medskip \noindent 
Step 1. Here we deal with $i = 0$. 
Since $a^0 = b^0 = 1$, the complexes 
$\opn{K}(A; a^0)$ and $\opn{K}(A; b^0)$ are acyclic. 
From (\ref{eqn:134}) we conclude that the 
complex $\opn{K}(A; \aa^0)$ is acyclic. Hence the homomorphism 
(\ref{eqn:133}) is zero for all $q$ and all $j \geq 0$. 

\medskip \noindent 
Step 2. Here we deal with $q = -2$. Take any $i \geq 1$. 
The regularity of $a$ implies that 
$\opn{H}^{-1} \bigl( \opn{K}(A; a^i) \bigr) = 0$, 
so the augmentation homomorphism
\begin{equation} \label{eqn:123}
\opn{K}(A; a^i) \to \opn{H}^{0} \bigl( \opn{K}(A; a^i) \bigr)
= A / (a^i) = A_{i - 1} 
\end{equation}
is a quasi-isomorphism. From (\ref{eqn:134}), with the fact that 
$\opn{K}(A; b^i)$ is a K-flat complex, we see that the homomorphism of 
complexes 
\begin{equation} \label{eqn:240}
\opn{K}(A; \aa^i) \to A_{i - 1} \ot_A \opn{K}(A; b^i)
\end{equation}
induced by (\ref{eqn:123}) is a quasi-isomorphism. But 
\begin{equation} \label{eqn:241}
A_{i - 1} \ot_A \opn{K}(A; b^i) \cong \opn{K}(A_{i - 1}; b^i)
\end{equation}
canonically as complexes of $A$-modules.
The complex $\opn{K}(A_{i - 1}; b^i)$ is concentrated in degrees $-1, 0$. 
It follows that 
$\opn{H}^{-2} \bigl( \opn{K}(A; \aa^i) \bigr) = 0$,
and hence the homomorphism (\ref{eqn:133}) is zero for $q = -2$ and all 
$i \geq 1$. 

\medskip \noindent 
Step 3. Here we handle the case $q = -1$ and $i \geq 1$. For every 
$j \geq i \geq 1$ the ring homomorphism 
$\pi : A_{j - 1} \to A_{i - 1}$
induces a homomorphism of complexes 
\[  \opn{K}(\pi; b^j) : \opn{K}(A_{j - 1}; b^j) \to 
\opn{K}(A_{i - 1}; b^j) . \]
Taking the $q = -1$ cohomology in (\ref{eqn:240}) and (\ref{eqn:241}), we 
obtain a canonical isomorphism of $A$-modules 
\[ \opn{H}^{-1} \bigl( \opn{K}(A; \aa^j) \bigr) \cong 
\opn{H}^{-1} \bigl( \opn{K}(A_{j - 1}; b^j) \bigr) . \]
Likewise with $i$ instead of $j$. These, with the isomorphism 
(\ref{eqn:105}), make the diagram 
\begin{equation} \label{eqn:124}
\UseTips \xymatrix @C=6ex @R=6ex {
\opn{H}^{-1} \bigl( \opn{K}(A; \aa^j) \bigr)
\ar[d]_{ \opn{H}^{-1}(\mu_{j, i}) }
\ar[r]^(0.45){\simeq}
&
\opn{H}^{-1} \bigl( \opn{K}(A_{j - 1}; b^j) \bigr) 
\ar[d]_{ \opn{H}^{-1}(\mu_{j, i} \, \circ \, \opn{K}(\pi; b^j)) }
\ar[r]^(0.55){\simeq}
&
\opn{Ann}_{A_{j - 1}}(b^j)
\ar[d]_{ \opn{mult}(b^{j - i}) \, \circ \, \pi }
\\
\opn{H}^{-1} \bigl( \opn{K}(A; \aa^i) \bigr)
\ar[r]^(0.45){\simeq}
&
\opn{H}^{-1} \bigl( \opn{K}(A_{i - 1}; b^i) \bigr) 
\ar[r]^(0.55){\simeq}
&
\opn{Ann}_{A_{i - 1}}(b^i)
} 
\end{equation}
commutative. The rightmost column factors into this commutative diagram:
\begin{equation} \label{eqn:127}
\UseTips \xymatrix @C=6ex @R=6ex {
\opn{Ann}_{A_{j - 1}}(b^j)
\ar[r]^{ \pi }
\ar[dr]_{ \opn{mult}(b^{j - i}) \, \circ \, \pi \ }
&
\opn{Ann}_{A_{i - 1}}(b^j)
\ar[d]^{ \opn{mult}_{A_{i - 1}}(b^{j - i}) }
\\
&
\opn{Ann}_{A_{i - 1}}(b^i)
}
\end{equation}

Let's fix $i \geq 1$ now. By Lemma \ref{lem:105} the $b$-torsion on 
$A_{i - 1}$ is bounded, i.e.\ 
$\opn{tb}_{A_{i - 1}}(b) < \infty$. This implies that for every 
$j \geq i + \opn{tb}_{A_{i - 1}}(b)$
the vertical arrow in (\ref{eqn:127}) is zero. Going back to 
diagram (\ref{eqn:124}), we see that the leftmost vertical arrow in it is zero 
for every $j \geq i + \opn{tb}_{A_{i - 1}}(b)$.
The conclusion is that the homomorphism (\ref{eqn:133}) is zero 
for $q = -1$ and $j \gg i$.
\end{proof}

\begin{rem} \label{rem:320}
In an earlier version of this paper we asked the following three questions, 
which are variations of Theorem \ref{thm:105}.
Let $\a$ and $\b$ be finitely generated ideals in the ring $A$. Define the ring 
$\mbar{A} := A / \a$ and the ideal $\bar{\b} := \b \cd \mbar{A} \sub \mbar{A}$.
\begin{enumerate}
\item[(Q1)] Suppose $\a$ and $\b$ are WPR. Is the ideal $\a + \b \sub A$ WPR?

\item[(Q2)] Suppose $\a$ and $\b$ are WPR. Is the ideal 
$\bar{\b} \sub \mbar{A}$ WPR?

\item[(Q3)] (Disegni) Assume that $\a \sub A$ and $\bar{\b} \sub \mbar{A}$ are 
WPR ideals. Is the ideal $\a + \b \sub A$ WPR?
\end{enumerate}

Since then, L. Positselski (in a private communication) provided us with 
counterexamples to the first two questions, which we now reproduce. 
Consider a ring $C$, with an element $c \in C$ that is not weakly proregular 
(there are known examples of this in the literature). 
By Corollary \ref{cor:140}, the ideal 
$\c := (c) \sub C$ is not WPR. Let 
$A := C[t]$, the polynomial ring in the variable $t$, so that 
$A \cong C \ot_{\Z} D$, where $D := \Z[t]$. Define the element
$b := c + t \in A$, and the principal ideals $\a := (t)$ and $\b := (b)$ in 
$A$. The elements $t, b \in A$ are regular, and hence the ideals $\a, \b \sub A$ 
are WPR. 

The ring $\bar{A} = A / \a$ is isomorphic to $C$, and the ideal 
$\bar{\b} = \b \cd \bar{A} \sub \bar{A}$ is sent to the ideal 
$\c \sub C$ under this isomorphism. By assumption the ideal 
$\c \sub C$ is not WPR. This is a counterexample to (Q2). 

Next let's consider the ideal 
$\a + \b \sub A$. It is easy to see that the ideal $\a + \b$ is generated by 
the sequence $(t, c)$. We will prove that the sequence $(t, c)$ in $A$ is not 
WPR, implying that the ideal $\a + \b$ is not WPR, thus providing a 
counterexample to (Q1). 

For $k \geq 0$ define 
$A_k := A / \a^{k + 1} = A / (t ^{k + 1})$
and $D_k :=  D / (t ^{k + 1}) = \Z[t] / (t ^{k + 1})$. There is a canonical 
ring isomorphism 
$A_k \cong C \ot_{\Z} D_k$, and a canonical isomorphism of complexes
\begin{equation} \label{eqn:322}
\opn{K}(A; t^{k + 1}, c^{k + 1}) \cong 
\opn{K}(D; t^{k + 1}) \ot_{\Z} \opn{K}(C; c^{k + 1}) .
\end{equation}
The canonical homomorphism $\opn{K}(D; t^{k + 1}) \to D_k$ is a 
quasi-isomorphism. Due to the flatness of $D$ and $D_k$ over $\Z$ we get a 
canonical isomorphism of $C$-modules 
\begin{equation} \label{eqn:321}
\opn{H}^{-1} \bigl( \opn{K}(D; t^{k + 1}) \ot_{\Z} \opn{K}(C; c^{k + 1}) 
\bigr) \cong 
D_k \ot_{\Z} \opn{H}^{-1} \bigl( \opn{K}(C; c^{k + 1}) \bigr) .
\end{equation}
Because the homomorphisms $D_{k + 1} \to D_k$ are surjective, and the 
inverse system
\[ \bigl\{ \opn{H}^{-1} \bigl( \opn{K}(C; c^{k + 1}) \bigr) \bigr\}_{k \in \N} 
\]
is not pro-zero, it follows that the inverse system (\ref{eqn:321}) is not 
pro-zero. Combining this with the canonical isomorphisms (\ref{eqn:322}) we 
conclude that the sequence $(t, c)$ in $A$ is not WPR. 

As for (Q3): it is still open. 
\end{rem}
