---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-006-6-pronilpotent-gerbes
section_title: "Pronilpotent Gerbes"
section_number: 6
pages: 29-33
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.98
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
\label{sec:pronilp}

Let $X$ be a topological space. Recall that given an inverse system 
$\{ \mcal{G}_p \}_{p \in \N}$ of sheaves of groups on $X$, its inverse limit is
the sheaf of groups 
$\opn{lim}_{\leftarrow p} \, \mcal{G}_p$
whose group of sections on an open set $U$ is
\[ \Gamma(U, \opn{lim}_{\leftarrow p} \, \mcal{G}_p) = 
\opn{lim}_{\leftarrow p} \, \Gamma(U, \mcal{G}_p) . \]

\begin{dfn} \label{dfn.10}
Let $\mcal{G}$ be a sheaf of groups on $X$. 
\begin{enumerate}
\item A {\em normal filtration} of $\mcal{G}$ is a descending sequence 
$\{ \mcal{N}_p \}_{p \in \N}$ of sheaves of normal subgroups of $\mcal{G}$.

\item A {\em central filtration} of $\mcal{G}$ is a normal filtration
$\{ \mcal{N}_p \}_{p \in \N}$, such that 
$\mcal{N}_0 = \mcal{G}$, $\bigcap_p \mcal{N}_p = 1$, and for every $p$ the
extension of sheaves of groups 
\[ 1 \to \mcal{N}_p / \mcal{N}_{p+1} \to \mcal{G} / \mcal{N}_{p+1} 
\to \mcal{G} / \mcal{N}_p \to 1 \]
is central.

\item Let $\{ \mcal{N}_p \}_{p \in \N}$ be a normal filtration of $\mcal{G}$.
We say that $\mcal{G}$ is {\em complete} with respect to this filtration if
the canonical homomorphism of sheaves of groups
\[ \mcal{G} \to \opn{lim}_{\leftarrow p} \, 
\mcal{G} / \mcal{N}_{p} \] 
is an isomorphism.

\item If $\mcal{G}$ is complete with respect to some central filtration,
then we call it a {\em pronilpotent sheaf of groups}.
\end{enumerate}
\end{dfn}

Note that when $\{ \mcal{N}_p \}_{p \in \N}$ is a central filtration, then
each $\mcal{N}_p / \mcal{N}_{p+1}$ is a sheaf of abelian groups.

\begin{dfn} \label{dfn:11}
Let $\mcal{G}$ be a sheaf of groups on $X$, with central filtration
$\{ \mcal{N}_p \}_{p \in \N}$. An open set $U \subset X$ is called 
{\em acyclic} with respect to  $\{ \mcal{N}_p \}_{p \in \N}$ if
the following two conditions hold.
\begin{enumerate}
\rmitem{i} For every $p \geq 0$ and $i > 0$ the sheaf cohomology group 
$\mrm{H}^i(U, \mcal{N}_p / \mcal{N}_{p+1})$ is trivial.

\rmitem{ii} For every $q \geq p \geq 0$ the canonical group homomorphism
\[ \Gamma(U, \mcal{N}_p) \to \Gamma(U, \mcal{N}_p / \mcal{N}_{q}) \] 
is surjective. 
\end{enumerate}
\end{dfn}

\begin{lem} \label{lem.1}
Let $\{ \mcal{N}_p \}_{p \in \N}$ be a central filtration of the sheaf of
groups $\mcal{G}$. Suppose that $\mcal{G}$ is complete with respect to the
filtration $\{ \mcal{N}_p \}_{p \in \N}$, and the open set $U \subset X$ is 
acyclic with respect to $\{ \mcal{N}_p \}_{p \in \N}$. 
Let $G := \Gamma(U, \mcal{G})$ and
$N_p := \Gamma(U, \mcal{N}_p)$.
Then $G$ is complete with respect to the filtration $\{ N_p \}_{p \in \N}$.
\end{lem}

\begin{proof}
Condition (ii) of Definition \ref{dfn:11}, combined with Proposition
\ref{prop:9}(1), say that for every $p$ there is an exact sequence of groups
\[ 1 \to N_p \to G \to \Gamma(U, \mcal{G} / \mcal{N}_{p}) \to 1 . \]
Now use Definition \ref{dfn.10}(3).
\end{proof}

In the situation above the filtration $\{ N_p \}_{p \in \N}$ of $G$ is
separated. Therefore it defines a metric topology on
$G$, say by letting $N_p \cdot g = g \cdot N_p$ be the ball of radius $2^{-p}$
around the point $g \in G$ (cf.\ \cite[Section III.5]{CA}).
The condition that $G \cong \opn{lim}_{\leftarrow p} \, G / N_p$
translates to $G$ being a complete metric space.

\begin{dfn}
Let $\mcal{G}$ be a sheaf of groups on $X$, with central filtration
$\{ \mcal{N}_p \}_{p \in \N}$.
\begin{enumerate}
\item A collection $\bsym{U} = \{ U_k \}_{k \in K}$ of open sets of $X$ is
called {\em  acyclic} with respect to  $\{ \mcal{N}_p \}_{p \in \N}$
if every finite intersection $U_{k_0, \ldots, k_m}$ is acyclic with respect to 
$\{ \mcal{N}_p \}_{p \in \N}$, in the sense of Definition \ref{dfn:11}.

\item We say that there are {\em enough acyclic coverings} with respect to 
$\{ \mcal{N}_p \}_{p \in \N}$ if every open covering $\bsym{U}$ of an open set
$U \subset X$ admits a refinement $\bsym{U}'$ which is acyclic  with
respect to $\{ \mcal{N}_p \}_{p \in \N}$.
\end{enumerate}
\end{dfn}

Now we move to gerbes. Let $\gerbe{G}$ be a gerbe on $X$.
The notion of normal subgroupoid $\gerbe{N} \subset \gerbe{G}$ was introduced
in Definition \ref{dfn.9}.

\begin{dfn} \label{dfn.12}
Let $\gerbe{G}$ be a gerbe on $X$. 
\begin{enumerate}
\item A {\em normal filtration} of $\gerbe{G}$ is a descending sequence 
$\{ \gerbe{N}_p \}_{p \in \N}$ 
of normal subgroupoids of $\gerbe{G}$.

\item A {\em central filtration} of $\gerbe{G}$
is a normal filtration $\{ \gerbe{N}_p \}_{p \in \N}$, such that for every
local object $i$ of $\gerbe{G}$, the filtration 
$\{ \gerbe{N}_p(i, i) \}_{p \in \N}$ of the sheaf of groups 
$\gerbe{G}(i, i)$ is central.

\item Let $\{ \gerbe{N}_p \}_{p \in \N}$ be a normal filtration of $\gerbe{G}$.
We say that $\gerbe{G}$ is {\em complete} with respect to this filtration if
for every local object $i$ of $\gerbe{G}$, the sheaf $\gerbe{G}(i, i)$
is complete with respect to the filtration 
 $\{ \gerbe{N}_p(i, i) \}_{p \in \N}$.

\item If $\gerbe{G}$ is complete with respect to some central filtration,
then we call it a {\em pronilpotent gerbe}.
\end{enumerate}
\end{dfn}

\begin{prop}
Suppose $\{ \gerbe{N}_p \}_{p \in \N}$ is a central filtration of the gerbe
$\gerbe{G}$. Then for every $p$ there is a central extension of gerbes
\begin{equation} \label{eqn:16}
1 \to \gerbe{N}_p / \gerbe{N}_{p+1} \to 
\gerbe{G} / \gerbe{N}_{p+1} \xar{F} \gerbe{G} / \gerbe{N}_{p} \to 1 .
\end{equation}
\end{prop}

\begin{proof}
Use Theorem \ref{thm:1}.
\end{proof}

Observe that $\gerbe{N}_p / \gerbe{N}_{p+1}$ is a central subgroupoid of the
gerbe $\gerbe{G} / \gerbe{N}_{p+1}$; so 
$\gerbe{N}_p / \gerbe{N}_{p+1}$ can be
regarded as a sheaf of abelian groups on $X$. See Proposition \ref{prop:12}.

\begin{dfn}
Let $\gerbe{G}$ be a gerbe on $X$, with central filtration
$\{ \gerbe{N}_p \}_{p \in \N}$.
An open set $U \subset X$ is called {\em acyclic} with respect to
$\{ \gerbe{N}_p \}_{p \in \N}$ if the following two condition hold:
\begin{enumerate}
\rmitem{i} The groupoid $\gerbe{G}(U)$ is nonempty.
\rmitem{ii} For every $i \in \opn{Ob} \gerbe{G}(U)$, the set $U$ is 
acyclic with respect to the central filtration
$\{ \gerbe{N}_p(i, i) \}_{p \in \N}$
of the sheaf of groups $\gerbe{G}(i, i)$. 
\end{enumerate}
\end{dfn}

\begin{dfn}
Let $\gerbe{G}$ be a gerbe on $X$, with central filtration
$\{ \gerbe{N}_p \}_{p \in \N}$.
\begin{enumerate}
\item A collection $\bsym{U} = \{ U_k \}_{k \in K}$ of open sets of $X$ is
called {\em acyclic} with respect to  $\{ \gerbe{N}_p \}_{p \in \N}$
if every finite intersection $U_{k_0, \ldots, k_m}$ is acyclic with respect to 
$\{ \gerbe{N}_p \}_{p \in \N}$.

\item We say that there are {\em enough  acyclic  coverings} with respect to 
$\{ \gerbe{N}_p \}_{p \in \N}$ if every open covering $\bsym{U}$ of an open set
$U$ admits a refinement $\bsym{U}'$ which is acyclic  with
respect to $\{ \gerbe{N}_p \}_{p \in \N}$.
\end{enumerate}
\end{dfn}

Suppose $\gerbe{G}$ is a gerbe, complete with respect to a  central
filtration $\{ \gerbe{N}_p \}_{p \in \N}$. Let $U$ be an open set of $X$ which
is acyclic with respect to $\{ \gerbe{N}_p \}_{p \in \N}$, and
let $i$ be an object of the groupoid $\gerbe{G}(U)$. 
By Lemma \ref{lem.1} the group $\gerbe{G}(U)(i, i)$ is complete with respect to
the filtration $\{ \gerbe{N}_p(U)(i, i) \}_{p \in \N}$; so 
$\gerbe{G}(U)(i, i)$ is a complete metric space.
Now let $j$ be another object of $\gerbe{G}(U)$, and suppose 
$\gerbe{G}(U)(i, j) \neq \emptyset$. Then the set
$\gerbe{G}(U)(i, j)$ is a $\gerbe{G}(U)(j, j)$-$\gerbe{G}(U)(i, i)$-bitorsor.
One can introduce a metric topology on this set, by letting 
\[ g \circ \gerbe{N}_p(U)(i, i) = \gerbe{N}_p(U)(j, j) \circ g \]
be the ball of radius
$2^{-p}$ around $g \in \gerbe{G}(U)(i, j)$. 
For any such $g$ the function 
$h \mapsto g \cdot h$ is an isomorphism of metric spaces
$\gerbe{G}(U)(i, i) \iso \gerbe{G}(U)(i, j)$; and hence 
$\gerbe{G}(U)(i, j)$ is complete.


\begin{thm} \label{thm.4}
Let $\gerbe{G}$ be a gerbe on the topological space $X$, and let 
$\{ \gerbe{N}_p \}_{p \in \N}$ be a central filtration on it.
Assume that $\gerbe{G}$ is complete with respect to 
$\{ \gerbe{N}_p \}_{p \in \N}$, and that there are enough
acyclic coverings with respect to 
$\{ \gerbe{N}_p \}_{p \in \N}$.
Let $U$ be some open set of $X$.
\begin{enumerate}
\item If $\mrm{H}^1(U, \gerbe{N}_p / \gerbe{N}_{p+1}) = 1$
for every $p \geq 0$, then the groupoid $\gerbe{G}(U)$ is connected.

\item If $\mrm{H}^2(U, \gerbe{N}_p / \gerbe{N}_{p+1}) = 1$
for every $p \geq 0$, then the groupoid $\gerbe{G}(U)$ is nonempty.
\end{enumerate}
\end{thm}

\begin{proof}
(1) This is very similar to Theorem \ref{thm.3}. Given 
$i, j \in \opn{Ob} \gerbe{G}(U)$, we must show that 
$\gerbe{G}(U)(i, j) \neq \emptyset$.

Since $\gerbe{G}$ is locally connected, we can find an open covering 
$\bsym{U} = \{ U_k \}_{k \in K}$ of $U$ such that
$\gerbe{G}(U_k)(i, j) \neq \emptyset$ for any $k \in K$.
By refining $\bsym{U}$, we can assume that it is  acyclic with
respect to $\{ \gerbe{N}_p \}_{p \in \N}$.
For each $k \in K$ let us choose an element
$g_{k; 0} \in \gerbe{G}(U_k)(i, j)$.
We are going to construct new elements
$g_{k; p} \in \gerbe{G}(U_k)(i, j)$, for all $k \in K$ and $p \in \N$, 
satisfying these conditions:
\begin{enumerate}
\rmitem{a} $g_{k; p+1} \in g_{k; p} \circ \gerbe{N}_p(U_k)(i, i)$.
\rmitem{b} $g_{k_1; p}^{-1} \circ g_{k_0; p} \in 
\gerbe{N}_p(U_{k_0, k_1})(i, i)$
for any $k_0, k_1 \in K$.
\end{enumerate}
The construction is by recursion on $p$.

For $p = 0$ the elements $g_{k; 0}$ are already given. So let $p \geq 0$,
and assume that we have elements $g_{k; p'}$ for $p' \leq p$, satisfying
conditions (a)-(b). 
Let us denote by 
$\bar{g}_{k; p} \in (\gerbe{G} / \gerbe{N}_{p+1})(U_k)(i, j)$
the image of $g_{k; p}$, and define
\[ \bar{g}_{k_0, k_1; p} := \bar{g}_{k_1; p}^{-1} \circ
\bar{g}_{k_0; p} \in (\gerbe{G} / \gerbe{N}_{p+1})(U_{k_0, k_1})(i, i)  \]
for $k_0, k_1 \in K$.
Consider the central extension of gerbes (\ref{eqn:16}).
By condition (b) we have 
$F(\bar{g}_{k_0, k_1; p}) = 1$; 
so
\[ \bar{g}_{k_0, k_1; p} \in 
(\gerbe{N}_p / \gerbe{N}_{p+1})(U_{k_0, k_1})(i, i) . \]
We get a \v{C}ech $1$-cocycle 
$c := \{ \bar{g}_{k_0, k_1; p} \}_{k_0, k_1 \in K}$ with values in the sheaf
$\gerbe{N}_p / \gerbe{N}_{p+1}$.

According to the assumptions and Proposition \ref{prop:11}(1), we have
\[ \check{\mrm{H}}^1(\bsym{U}, \gerbe{N}_p / \gerbe{N}_{p+1}) \cong 
\mrm{H}^1(U, \gerbe{N}_p / \gerbe{N}_{p+1}) = 1 . \]
Hence there is a $0$-cochain 
$b = \{ \bar{f}_k \}_{k \in K}$ 
such that $c = \d(b)$, where $\d$ is the \v{C}ech coboundary.
By condition (ii) of Definition \ref{dfn:11} the homomorphism
\[ \gerbe{N}_p(U_k)(i, i) \to (\gerbe{N}_p / \gerbe{N}_{p+1})(U_k)(i, i) \]
is surjective, so we can lift $\bar{f}_k$ to an element
$f_k \in \gerbe{N}_p(U_k)(i)$.
Let us define
\[ g_{k; p+1} := g_{k; p} \cdot f_k^{-1} . \]
Then conditions (a)-(b) are satisfied. 

We know that the set $\gerbe{G}(U_k)(i, j)$ is a complete metric space. 
Condition (a) says that $\{ g_{k; p} \}_{p \in \N}$ is a Cauchy sequence. 
Let 
\[ g_k := \lim_{p \to \infty} \, g_{k; p} \in \gerbe{G}(U_k)(i, j) . \]
Condition (b) now says that $\{ g_k \}_{k \in K}$ is a $1$-cocycle. 
By descent for morphisms there is an element
$g \in \gerbe{G}(U)(i, j)$ such that $g|_{U_k} = g_k$.

\medskip \noindent
(2) This is like Theorem \ref{thm.2}. Since $\gerbe{G}$ is locally nonempty,
there is an open covering $\bsym{U} = \{ U_k \}_{k \in K}$ of $U$ such that 
all the groupoids $\gerbe{G}(U_k)$ are nonempty. By refining $\bsym{U}$ we may
assume it is acyclic with respect to $\{ \gerbe{N}_p \}_{p \in \N}$.
Let's choose some $i_k \in \opn{Ob} \gerbe{G}(U_k)$.
For any $k_0, k_1 \in K$, and any $p \in \N$, we have
$\mrm{H}^1(U_{k_0, k_1}, \gerbe{N}_p / \gerbe{N}_{p+1}) = 1$. According to part
(1) of the theorem, applied to the open set $U_{k_0, k_1}$, the groupoid 
$\gerbe{G}(U_{k_0, k_1})$ is connected. 
Let us choose some element
$g_{k_0, k_1; 0} \in \gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1})$.

Using recursion on $p$ we shall construct elements
$g_{k_0, k_1; p} \in \gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1})$
satisfying these conditions:
\begin{enumerate}
\rmitem{a} $g_{k_0, k_1; p+1} \in g_{k_0, k_1; p} 
\circ \gerbe{N}_p(U_{k_0, k_1})(i_{k_0}, i_{k_0})$.
\rmitem{b} $g_{k_0, k_2; p}^{-1} \circ g_{k_1, k_2; p} \circ
g_{k_0, k_1; p} \in \gerbe{N}_p(U_{k_0, k_1, k_2})(i_{k_0}, i_{k_0})$
for any $k_0, k_1, k_2 \in K$.
\end{enumerate}

For $p = 0$ the elements $g_{k_0, k_1; 0}$ are already given. So let
$p \geq 0$,
and assume that we have elements $g_{k_0, k_1; p'}$ for $p' \leq p$, satisfying
conditions (a)-(b). 
Let us denote by 
\[ \bar{g}_{k_0, k_1; p} \in (\gerbe{G} / \gerbe{N}_{p+1})(U_{k_0, k_1})
(i_{k_0}, i_{k_1}) \]
the image of $g_{k_0, k_1; p}$, and define 
\[ \bar{g}_{k_0, k_1, k_2; p} := 
\bar{g}_{k_0, k_2; p}^{-1} \circ \bar{g}_{k_1, k_2; p} \circ
\bar{g}_{k_0, k_1; p} \in 
(\gerbe{G} / \gerbe{N}_{p+1})(U_{k_0, k_1, k_2})(i_{k_0}, i_{k_0}) . \]
Consider the central extension of gerbes (\ref{eqn:16}).
By condition (b) we have \linebreak
$F(\bar{g}_{k_0, k_1, k_2; p}) = 1$; 
so
\[ \bar{g}_{k_0, k_1, k_2; p} \in 
(\gerbe{N}_p / \gerbe{N}_{p+1})(U_{k_0, k_1, k_2})(i_{k_0}, i_{k_0}) . \]
Lemma \ref{lem:10} says that 
$c := \{ \bar{g}_{k_0, k_1, k_2; p} \}$
is a \v{C}ech $2$-cocycle.

According to the assumptions and Proposition \ref{prop:11}(1), we have
\[ \check{\mrm{H}}^2(\bsym{U}, \gerbe{N}_p / \gerbe{N}_{p+1}) \cong 
\mrm{H}^2(U, \gerbe{N}_p / \gerbe{N}_{p+1}) = 1 . \]
Hence there is a $1$-cochain 
$b = \{ \bar{f}_{k_0, k_1} \}$ 
such that $c = \d(b)$. As before, we can lift $\bar{f}_{k_0, k_1}$ to an element
$f_{k_0, k_1} \in \gerbe{N}_p(U_{k_0, k_1})(i_{k_0}, i_{k_0})$.
Let us define
\[ g_{k_0, k_1; p+1} := g_{k_0, k_1; p} \circ f_{k_0, k_1}^{-1} . \]
Then conditions (a)-(b) are satisfied. 

As in the proof of part (1), let
\[ g_{k_0, k_1} := \lim_{p \to \infty} \, g_{k_0, k_1; p} \in 
\gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1}) . \]
Condition (b) says that $\{ g_{k_0. k_1} \}_{k_0, k_1 \in K}$ is a $2$-cocycle. 
By descent for objects there is an object
$i \in \opn{Ob} \gerbe{G}(U)$.
\end{proof}
