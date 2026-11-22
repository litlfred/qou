---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-001-1-dg-modules-and-their-resolutions
section_title: "DG Modules and their Resolutions"
section_number: 1
pages: 7-11
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.963
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:resol}
 
A {\em DG ring} (usually called an associative unital DG algebra over $\Z$) is 
a graded ring $A = \bigoplus_{i \in \Z} A^i$, with differential $\d$ of degree 
$1$, satisfying the graded Leibniz rule 
\[ \d(a \cd b) = \d(a) \cd b + (-1)^i \cd a \cd \d(b) \]
for $a \in A^i$ and $b \in A^j$. 
A homomorphism of DG rings is a degree $0$ ring homomorphism 
that commutes with the differentials. 
In this way we get a category, denoted by $\cat{DGR}$. 
Rings are viewed as DG rings concentrated in degree $0$. 
For a DG ring $A$, the cohomology 
$\opn{H}(A) = \bigoplus_{i \in \Z} \opn{H}^i(A)$ is a graded ring. 

The {\em opposite} of the DG ring $A$ is the DG ring $A^{\mrm{op}}$,
which is the same graded abelian group as $A$, with the same differential, but 
the multiplication $\cd^{\mrm{op}}$ is reversed in the graded sense. Namely, 
for 
elements $a \in A^i$ and $b \in A^j$, their product in $A^{\mrm{op}}$ is 
\[ a \, \cd^{\mrm{op}} \, b := (-1)^{i j} \cd b \cd a . \]

A left DG $A$-module is a graded left $A$-module $M = \bigoplus_{i \in \Z} 
M^i$, with differential $\d$ satisfying the graded Leibniz rule. 
If $M$ is a left DG $A$-module then 
$\opn{H}(M) = \bigoplus_{i \in \Z} \opn{H}^i(M)$
is a graded left $\opn{H}(A)$-module.
Note that a right DG $A$-module is the same as a left DG $A^{\mrm{op}}$-module.

\begin{conv} \label{conv:585}
By default, in this paper all DG modules are left DG modules.
\end{conv} 

From Section \ref{sec:localiz} onwards our DG rings will be commutative, 
and for them the distinction between left and right DG modules becomes 
negligible. 

\begin{dfn} \label{dfn:365}
Let $A$ be a DG ring. 
The category of (left) DG $A$-modules, with $A$-linear homomorphisms of degree 
$0$ that commute with differentials, is denoted by $\cat{DGMod} A$,
or by its abbreviation $\cat{C}(A)$. 
The derived category, gotten from $\cat{DGMod} A$ by inverting 
quasi-isomorphisms, is denoted by 
$\cat{D}(\cat{DGMod} A)$, or by the abbreviation $\cat{D}(A)$.
\end{dfn}

For information on $\cat{D}(A)$ see \cite[Section 10]{BL}, 
\cite[Section 2]{Ke1} or 
\cite[\href{http://stacks.math.columbia.edu/tag/09KV}{Section 09KV}]{SP}.
If $A$ is a ring, then 
$\cat{C}(A) = \cat{C}(\cat{Mod} A)$,
the category of complexes of $A$-modules; and 
$\cat{D}(A) = \cat{D}(\cat{Mod} A)$,
the usual derived category of the abelian category $\cat{Mod} A$. 


\begin{dfn} \label{dfn:105}
Let $A = \bigoplus_{i \in \Z} A^i$ be a DG ring.

\begin{enumerate}
\item We say that $A$ is  {\em a nonpositive DG ring} if 
$A^i = 0$ for all $i > 0$.

\item If $A$ is nonpositive DG ring, then we write 
$\bar{A} := \opn{H}^0(A)$, which is a ring. There is a canonical DG ring 
homomorphism $A \to \bar{A}$.
\end{enumerate}
\end{dfn}

The full subcategory of $\cat{DGR}$ on the nonpositive DG rings is 
denoted by $\cat{DGR}^{\leq 0}$.

\begin{conv} \label{conv:305}
By default, in this paper all DG rings are nonpositive; i.e.\ we work 
inside $\cat{DGR}^{\leq 0}$. 
\end{conv}

One of the important advantages of nonpositive DG rings
is that the differential $\d$ of any DG $A$-module $M$ is $A^0$-linear. This 
implies that the two smart truncations
\begin{equation} \label{eqn:425}
\opn{smt}^{\geq i}(M) := \bigl( \cdots \to 0 \to \opn{Coker}(\d|_{M^{i - 1}})
\to M^{i + 1} \to M^{i + 2} \to  \cdots \bigr)
\end{equation}
and
\begin{equation} \label{eqn:426}
\opn{smt}^{\leq i}(M) := \bigl( \cdots \to  M^{i - 2} \to  M^{i - 1} \to
\opn{Ker}(\d|_{M^{i}}) \to 0 \to  \cdots \bigr)
\end{equation}
remain within $\cat{C}(A)$; and there are functorial homomorphisms 
$M \to \opn{smt}^{\geq i}(M)$ and 
$\opn{smt}^{\leq i}(M) \to M$ in $\cat{C}(A)$, inducing isomorphisms in 
$\opn{H}^{\geq i}$ and $\opn{H}^{\leq i}$ respectively.
Note that these are the truncations $\tau_{\leq n}$ and $\tau_{\geq n}$ from 
\cite[\href{http://stacks.math.columbia.edu/tag/0118}{Section 0118}]{SP},
that are variants of the truncations $\si_{> n}$ and $\si_{\leq n}$ from 
\cite[Section I.7, page 69]{RD}.
Warning: the two stupid truncations might fail to work in this context -- these 
truncated complexes of abelian groups might not be DG $A$-modules. 
 
Recall that for a subset $S \subseteq \Z$, its infimum is
$\opn{inf}(S) \in \Z \cup \{ \pm \infty \}$,
where $\opn{inf}(S) = + \infty$ iff $S = \varnothing$. 
Likewise the supremum is $\opn{sup}(S) \in \Z \cup \{ \pm \infty \}$,
where $\opn{sup}(S) = - \infty$ iff $S = \varnothing$.
For $i, j \in \Z \cup \{ \infty \}$, the expressions 
$i + j$ and $-i - j$ have obvious values in 
$\Z \cup \{ \pm \infty \}$. And for 
$i, j \in \Z \cup \{ \pm \infty \}$, 
the expression $i \leq j$ has an obvious meaning.

Let $M = \bigoplus_{i \in \Z} M^i$ be a graded abelian group. We write  
\begin{equation} \label{eqn:371}
\inf (M) := \opn{inf}\, \{ i \mid M^i \neq 0 \} \quad \tup{and} \quad 
\sup (M) := \opn{sup}\, \{ i \mid  M^i \neq 0 \} .
\end{equation}
The amplitude of $M$ is 
\begin{equation} \label{eqn:372}
\opn{amp} (M) := \sup (M) - \inf (M) \in \N \cup \{ \pm \infty\} .
\end{equation}
(For $M = 0$ this reads $\inf (M) = \infty$, $\sup (M) = -\infty$ 
and $\opn{amp} (M) = -\infty$.)
Thus $M$ is bounded (resp.\ bounded above, resp.\ bounded below) iff 
$\opn{amp} (M) < \infty$ (resp.\ $\opn{sup} (M) < \infty$, resp.\
$\opn{inf} (M) > -\infty$).

Given $i_0 \leq i_1$ in $\Z \cup \{ \pm \infty \}$,
the {\em integer interval} with these endpoints is the set of integers
\begin{equation} \label{eqn:580}
[i_0, i_1] := \{ i \in \Z  \mid i_0 \leq i \leq i_1 \}  .
\end{equation}
The integer interval $[i_0, i_1]$ is said to be bounded (resp.\ bounded above, 
resp.\ \lb bounded below) if $i_0, i_1 \in \Z$ (resp.\  $i_1 \in \Z$, resp.\ 
$i_0 \in \Z$). 
The {\em length} of this interval is $i_1 - i_0 \in \N \cup \{ \infty \}$. 
Of course the interval has finite length iff it is bounded. 
We write $-[i_0, i_1] := [-i_1, -i_0]$.
Given a second integer interval $[j_0, j_1]$, we let 
\[ [i_0, i_1] + [j_0, j_1] := [i_0 + j_0, i_1 + j_1] . \]
For the empty interval $\varnothing$, the sum is 
$[i_0, i_1] + \varnothing := \varnothing$.

\begin{dfn}  \label{dfn:550}
Let $M = \bigoplus_{i \in \Z} M^i$ be a graded abelian group.
\begin{enumerate}
\item We say that $M$ is concentrated in an integer interval $[i_0, i_1]$
if 
\[  \{ i \in \Z \mid M^i \neq 0 \} \subseteq [i_0, i_1] . \]

\item The {\em concentration} of $M$ is the smallest integer interval 
$\opn{con}(M)$ in which $M$ is concentrated.
\end{enumerate}
\end{dfn}

In other words, if 
$i_0 = \opn{inf} (M) \leq i_1 = \opn{sup} (M)$, 
then the concentration of $M$ is the interval
$\opn{con}(M) = [i_0, i_1]$,
and the amplitude $\opn{amp}(M)$ is the length of $\opn{con}(M)$.
Furthermore, $\opn{con}(M) = \varnothing$ iff $M = 0$. 

Given an integer interval $[i_0, i_1]$, we 
denote by $\cat{D}^{[i_0, i_1]}(A)$ the full subcategory of $\cat{D}(A)$ 
consisting of the DG modules $M$ whose cohomologies $\opn{H}(M)$ are 
concentrated in this interval; namely 
$\opn{con}(\opn{H}(M)) \subseteq [i_0, i_1]$.
For $i \in \Z$ we write 
$\cat{D}^{i}(A) := \cat{D}^{[i, i]}(A)$.
The subcategory $\cat{D}^{[i_0, i_1]}(A)$ is additive, but not triangulated. 
Similarly we have the subcategory 
$\cat{C}^{[i_0, i_1]}(A) \subseteq \cat{C}(A)$,
consisting of the DG modules $M$ that are concentrated in the integer interval
$[i_0, i_1]$; namely $\opn{con}(M) \subseteq [i_0, i_1]$.

\begin{dfn} \label{dfn:370}
Let $A$ be a DG ring. 
\begin{enumerate}
\item A DG $A$-module $M$ is said to be {\em cohomologically bounded} 
(resp.\  {\em cohomologically bounded above}, 
resp.\  {\em cohomologically bounded below})
if the  graded module $\opn{H}(M)$ is bounded (resp.\  bounded above, 
resp.\ bounded below).
We denote by $\cat{D}^{\mrm{b}}(A)$, $\cat{D}^{-}(A)$ and $\cat{D}^{+}(A)$
the corresponding full subcategories of $\cat{D}(A)$.

\item The full subcategory of $\cat{D}(A)$ consisting of the DG modules $M$,
whose cohomology modules $\opn{H}^i(M)$ are finite over $\bar{A}$,  is denoted 
by $\cat{D}_{\mrm{f}}(A)$.

\item  For any boundedness condition $\star$ we write 
$\cat{D}^{\star}_{\mrm{f}}(A) := \cat{D}_{\mrm{f}}(A) \cap \cat{D}^{\star}(A)$.
\end{enumerate}
\end{dfn}

Thus we have 
\[ \cat{D}^{\mrm{b}}(A) = \bigcup_{-\infty < i_0 \leq i_1 < \infty }
\cat{D}^{[i_0, i_1]}(A) \ , \]
etc. The categories $\cat{D}^{\mrm{b}}(A)$, $\cat{D}^{-}(A)$ and 
$\cat{D}^{+}(A)$ are triangulated. If $\bar{A}$ is left 
noetherian, then the categories 
$\cat{D}^{\mrm{b}}_{\mrm{f}}(A)$, $\cat{D}^{-}_{\mrm{f}}(A)$ and 
$\cat{D}^{+}_{\mrm{f}}(A)$ are also triangulated.

Given a DG $A$-module $M$, its shift by an integer $i$ is the DG module 
$M[i]$, whose \lb $j$-th graded component is $M[i]^j := M^{i+j}$.
Elements of $M[i]^j$ are denoted by $m[i]$, with $m \in M^{i+j}$.
The differential of $M[i]$ is 
$\d_{M[i]}(m[i]) := (-1)^i \cd \d_M(m)[i]$.
The left action of $A$ on $M[i]$ is also twisted by $\pm 1$, as follows:
$a \cd m[i] := (-1)^{k i} \cd (a \cd m)[i]$ 
for $a \in A^k$. The right action remains untwisted:
$m[i] \cd a := (m \cd a)[i]$.
See \cite[Section 1]{Ye5} for a detailed study of the shift operation, 
including an explanation of the sign that appears in the left action. 

We now recall some resolutions of DG $A$-modules. 
A DG module $N$ is called acyclic if $\opn{H}(N) = 0$. 
A DG $A$-module $M$ is called {\em K-projective} (resp.\ {\em 
K-injective}), if for any acyclic DG $A$-module $N$, the DG 
$\Z$-module $\opn{Hom}_A(M, N)$ (resp.\ $\opn{Hom}_A(N, M)$) is also 
acyclic. The DG $A$-module $M$ is called {\em K-flat} if for any acyclic DG 
$A^{\mrm{op}}$-module $N$, the DG $\Z$-module $N \ot_A M$ is acyclic. 
It is easy to see that K-projective implies K-flat. 
More information about the operations 
$\opn{Hom}_A(-, -)$ and $- \ot_A -$, 
and the various resolutions, see \cite[Section 1]{Ye5}.

For a cardinal number $r$ (possibly infinite) we denote by $M^{\oplus r}$ the 
direct sum of $r$ copies of $M$.
Recall that a DG $A$-module $P$ is a {\em free DG module} if 
$P \cong \bigoplus_{i \in \Z} A[-i]^{\oplus r_i}$, where 
$r_i$ are cardinal numbers.
We say that $P$ is a {\em finite free DG module} if $\sum_i r_i < \infty$
(for some such isomorphism).  
 
\begin{dfn} \label{dfn:310}
Let $P$ be a DG $A$-module. 
A {\em semi-free filtration} of $P$ is an ascending filtration 
$\{ \nu_j(P) \}_{j \in \Z}$ by DG $A$-submodules
$\nu_j(P) \subseteq P$, such that 
$\nu_{-1}(P) = 0$, $P = \bigcup_j \nu_j(P)$, and each 
$\opn{gr}^\nu_j(P) :=  \nu_j(P) / \nu_{j-1}(P)$ is a free DG $A$-module.
\end{dfn}

\begin{dfn} \label{dfn:100}
Let $P$ be a DG $A$-module, with semi-free filtration 
$\{ \nu_j(P) \}_{j \in \Z}$.
\begin{enumerate}
\item The filtration $\{ \nu_j(P) \}_{j \in \Z}$ is said to have length $l$
if 
\[ l = \opn{inf}\, \{ j \in \N \mid  \nu_{j}(P) = P  \}
\in \N \cup \{ \infty \}  . \]

\item The filtration $\{ \nu_j(P) \}_{j \in \Z}$ is called {\em pseudo-finite} 
if each free DG $A$-module $\opn{gr}^\nu_j(P)$ is finite, and 
$\lim_{j \to  \infty} \sup (\opn{gr}^\nu_j(P)) = -\infty$.

\item The filtration $\{ \nu_j(P) \}_{j \in \Z}$ on $P$ is called 
{\em finite} if it is pseudo-finite and has finite length. 
\end{enumerate}
\end{dfn}

\begin{dfn} \label{dfn:311}
A DG $A$-module $P$ is called a {\em semi-free} (resp.\ {\em pseudo-finite 
semi-free}, resp.\ {\em finite semi-free}) {\em DG module} if it admits a 
semi-free (resp.\ pseudo-finite semi-free, resp.\  finite semi-free)  
filtration. The {\em semi-free length} of $P$ is defined to be the minimum of 
the lengths of its semi-free filtrations.  
\end{dfn}

Note that a semi-free DG module need not be bounded above.
If $P$ is a semi-free DG module then it is K-projective; see
\cite[Section 3.1]{Ke1}.

Recall that our DG rings are always nonpositive. 
The next proposition gives another characterization of pseudo-finite semi-free
DG modules. The graded ring gotten from $A$ by forgetting the differential is 
denoted by $A^{\natural}$. Likewise for DG modules. 


\begin{prop} \label{prop:100}
Let $P$ be a DG $A$-module. 
\begin{enumerate}
\item $P$ is pseudo-finite semi-free iff there are $i_1 \in \Z$
and $r_i \in \N$, such that 
$P^{\natural} \cong \lb \bigoplus_{i \leq i_1} A^{\natural}[-i]^{\oplus r_i}$
as graded $A^{\natural}$-modules. 

\item $P$ is finite semi-free iff there is an isomorphism of 
graded $A^{\natural}$-modules as in item \tup{(1)} above, and $i_0 \in \Z$,
such that $r_i = 0$ for all $i < i_0$.
\end{enumerate}
\end{prop} 

\begin{proof}
Given an isomorphism 
$P^{\natural} \cong \bigoplus_{i \leq i_1} A^{\natural}[-i]^{\oplus r_i}$,
define  
\[ \nu_j(P) := \bigoplus_{i_1 - j \leq i \leq i_1} A[-i]^{\oplus r_i} 
\subseteq P . \]
This is a pseudo-finite semi-free filtration, of length $\leq i_1 - i_0$
in the finite case. The converse is clear, and so is item (2). 
\end{proof}

\begin{dfn} \label{dfn:390} 
Let $[i_0, i_1]$ be an integer interval (possibly unbounded). 
\begin{enumerate}
\item Let $P$ be a free graded $A^{\natural}$-module. We say that $P$ has a
{\em basis concentrated in $[i_0, i_1]$}  
if there is an isomorphism of graded 
$A^{\natural}$-modules
\[ P \cong \bigoplus_{i \in [i_0, i_1]} A^{\natural}[-i]^{\oplus r_i} \]
for some cardinal numbers $r_i$.

\item A DG $A$-module $M$ is said to be {\em generated} in the integer interval
$[i_0, i_1]$ if there is a surjection of graded $A^{\natural}$-modules
$P \to M^{\natural}$, where $P$ is a free graded $A^{\natural}$-module
with a basis concentrated in $[i_0, i_1]$.
\end{enumerate}
\end{dfn}

\begin{prop} \label{prop:390} 
Let $M$ be a DG $A$-module generated in the integer interval $[i_0, i_1]$.
\begin{enumerate}
\item If $N \in \cat{C}^{[j_0, j_1]}(A^{\mrm{op}})$,
then 
\[ N \ot_A M \in \cat{C}^{[j_0, j_1] + [i_0, i_1]}(\Z)
= \cat{C}^{[j_0 + i_0, j_1 + i_1]}(\Z). \]

\item If $N \in \cat{C}^{[j_0, j_1]}(A)$,
then 
\[ \opn{Hom}_A(M, N) \in \cat{C}^{[j_0, j_1] - [i_0, i_1]}(\Z)
= \cat{C}^{[j_0 - i_1, j_1 - i_0]}(\Z). \]
\end{enumerate}
\end{prop}

The easy proof is left to the reader. 

\begin{dfn} \label{dfn:391}
Let $A$ be a DG ring.
\begin{enumerate}
\item $A$ is called {\em cohomologically left noetherian} if the graded ring 
$\opn{H}(A)$ is left noetherian.

\item $A$ is called {\em cohomologically left pseudo-noetherian} if it 
satisfies these two conditions:
\begin{enumerate}
\rmitem{i} The ring  $\bar{A} = \opn{H}^0(A)$ is left noetherian.

\rmitem{ii} For every $i$ the left $\bar{A}$-module $\opn{H}^i(A)$ is finite 
(i.e.\ finitely generated). 
\end{enumerate}
\end{enumerate} 
\end{dfn}

We shall be mostly interested in  cohomologically left pseudo-noetherian DG 
rings. Of course if $A$ is cohomologically left noetherian, then it is 
cohomologically left pseudo-noetherian. These conditions are equivalent when 
$A$ is cohomologically bounded.

As usual, by a semi-free resolution of a DG module $M$ we mean a 
quasi-iso\-mor\-phism $P \to M$ in $\cat{C}(A)$, where $P$ is semi-free. 
Likewise we talk about K-injective resolutions $M \to I$.

\begin{prop} \label{prop:101}
Let $M$ be a DG $A$-module. 
\begin{enumerate}
\item There is a semi-free resolution $P \to M$ such that 
$\opn{sup}(P) = \opn{sup}(\opn{H}(M))$.

\item If the DG ring $A$ is cohomologically left pseudo-noetherian, and if
$M \in \cat{D}^{-}_{\mrm{f}}(A)$, then there is a pseudo-finite semi-free 
resolution $P \to M$ such that $\opn{sup}(P) = \opn{sup}(\opn{H}(M))$.

\item There is a K-injective resolution $M \to I$ such that 
$\opn{inf}(I) = \opn{inf}(\opn{H}(M))$.
\end{enumerate}
\end{prop}

\begin{proof}
(1) See \cite[Theorem 3.1]{Ke1}, \cite{AFH}, or 
\cite[\href{http://stacks.math.columbia.edu/tag/09KK}{Section 09KK}]{SP},
noting that \lb $\opn{sup}(A) = 0$ (if $A$ is nonzero). 

\medskip \noindent
(2) In this case the construction in item (1) can be made 
with finitely many basis elements in each degree. 
See \cite[Theorem 3.1]{Ke1} or \cite{AFH}.

\medskip \noindent
(3) See \cite[Theorem 3.2]{Ke1}, \cite{AFH}, or 
\cite[\href{http://stacks.math.columbia.edu/tag/09KQ}{Section 09KQ}]{SP}.
The point is that any DG $A$-module can be embedded in a product of shifts of 
the DG $A$-module \lb $\opn{Hom}_{\Z}(A, \Q / \Z)$. 
\end{proof}

\begin{rem} \label{rem:90}
Suppose $A$ is a ring. A DG $A$-module $P$ is pseudo-finite semi-free iff it is 
a bounded above complex of finite free $A$-modules. Now according to 
\cite{SGA-6} or 
\cite[\href{http://stacks.math.columbia.edu/tag/064Q}{Definition 064Q}]{SP},
a DG $A$-module $M$ is called pseudo-coherent if it is quasi-isomorphic to
some pseudo-finite semi-free DG module $P$. This explains the choice of the 
name ``pseudo-finite semi-free DG module''.

The name ``pseudo-noetherian DG ring'' was chosen due to the close 
relation to pseudo-finite semi-free resolutions; see Proposition 
\ref{prop:101}(2).
\end{rem}
