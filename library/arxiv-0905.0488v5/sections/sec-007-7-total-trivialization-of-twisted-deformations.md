---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-007-7-total-trivialization-of-twisted-deformations
section_title: "Total Trivialization of Twisted Deformations"
section_number: 7
pages: 33-36
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.974
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:tttf}

In this section we assume Setup \ref{setup:200}. 
Acyclic open sets were introduced in Definition \ref{dfn:23}.

Let $\mcal{A}$ be an $R$-deformation of $\mcal{O}_U$
(associative of Poisson) , for some open set 
$U \subset X$. By \cite[Corollary 3.8]{Ye9}, for every $p \geq 1$ 
the sheaf of $R$-modules $\m^p \mcal{A}$ is $\m$-adically complete.
As explained in Section \ref{sec:defs-alg-vars}, there is a sheaf of
pronilpotent groups $\opn{Exp}(\m^p \mcal{A})$ on $U$, with an isomorphism of
sheaves of sets 
$\exp : \m^p \mcal{A} \iso \opn{Exp}(\m^p \mcal{A})$.
If $V \subset U$ is an $\mcal{O}_X$-acyclic open set, then by 
\cite[Proposition 4.5]{Ye9} the algebra 
$A := \Gamma(V, \mcal{A})$ is an $R$-deformation of 
$C := \Gamma(V, \mcal{O}_X)$.

\begin{lem} \label{lem:mdd.101}
Let $U \subset X$ be an open set, and let
$\mcal{A}$ be an  $R$-deformation of $\mcal{O}_U$. Write
$\mcal{G} := \opn{IG}(\mcal{A}) = \opn{Exp} (\m \mcal{A})$,
and $\mcal{N}_p := \opn{Exp} (\m^{p} \mcal{A})$ for $p \geq 1$.
\begin{enumerate}
\item $\mcal{N}_p$ is a sheaf of normal subgroups of $\mcal{G}$, and
$\mcal{N}_p / \mcal{N}_{p+1}$ is central in $\mcal{G} / \mcal{N}_{p+1}$.
The canonical homomorphism 
$\mcal{G} \to \lim_{\leftarrow p}\, \mcal{G} / \mcal{N}_p$
is an isomorphism.

\item Suppose $V \subset U$ is an $\mcal{O}_X$-acyclic open set. 
Let $A := \Gamma(V, \mcal{A})$, and let
$N_p := \opn{Exp}(\m^{p} A)$. Then the cohomology groups 
$\mrm{H}^i(V, \mcal{N}_p / \mcal{N}_{p+1})$ are
trivial for all $p, i \geq 1$, and the canonical group homomorphisms 
$N_p \to \Gamma(V, \mcal{N}_p)$
and
$N_p / N_{q} \to \Gamma(V, \mcal{N}_p / \mcal{N}_{q})$
are bijective for all $q \geq p \geq 1$.
\end{enumerate}
\end{lem}

\begin{proof}
(1) We know that the Lie bracket satisfies 
$[\m \mcal{A}, \m^{p} \mcal{A}] \subset \m^{p+1} \mcal{A}$.
Hence $[ \mcal{G} , \mcal{N}_{p} ] \subset \mcal{N}_{p+1}$, 
so $\mcal{N}_{p}$ is normal in $\mcal{G}$ and 
$\mcal{N}_p / \mcal{N}_{p+1}$ is central in $\mcal{G} / \mcal{N}_{p+1}$.
Now $\mcal{G} / \mcal{N}_{p} \cong \opn{Exp}(R_{p-1} \ot_R \m \mcal{A})$,
and by definition 
$\opn{Exp} (\m \mcal{A}) = \lim_{\leftarrow p}\,
\opn{Exp}(R_{p} \ot_R \m \mcal{A})$.

\medskip \noindent
(2) Since $\opn{exp} : \m^{p} \mcal{A} \to \mcal{N}_p$
and
$\opn{exp} : \m^{p} \mcal{A} / \m^{q} \mcal{A} \to 
\mcal{N}_p / \mcal{N}_q$
are isomorphisms of sheaves of sets, and  
$\opn{exp} : \m^{p}  \mcal{A} / \m^{p+1} \mcal{A} \to 
\mcal{N}_p / \mcal{N}_{p+1}$
is an isomorphism of sheaves of abelian groups, we are allowed to switch 
from groups to Lie algebras. Namely, it suffices to prove the assertions 
for $\mcal{N}_p := \m^{p} \mcal{A}$ and $N_p := \m^{p} A$.

For the vanishing of cohomology we use the isomorphism
of sheaves of abelian groups
$\mcal{N}_p / \mcal{N}_{p+1} \cong 
(\m^{p} / \m^{p+1}) \ot \mcal{O}_U$
induced by the augmentation $\AA \to \OO_U$ 
(cf.\ \cite[Proposition 5.3]{Ye5}) to deduce
\[ \mrm{H}^i(V, \mcal{N}_p / \mcal{N}_{p+1}) \cong
(\m^{p} / \m^{p+1}) \ot \mrm{H}^i(V, \mcal{O}_U) = 0 \]
for $i \geq 1$.
The claim that the functions
$N_p \to \Gamma(V, \mcal{N}_p)$
and
$N_p / N_{q} \to \Gamma(V, \mcal{N}_p / \mcal{N}_{q})$
are bijective is  \cite[Corollary 3.6]{Ye9}, for $R$ and
$R_{q-1}$ respectively. 
\end{proof}

\begin{thm}[Total Trivialization] \label{thm:6}
Assume Setup \tup{\ref{setup:200}}. We consider the two cases\tup{:}
\begin{enumerate}
\item[$\vartriangleright$] The associative case, in which 
$\twocat{P}(R, X)$ is the stack  of crossed groupoids 
$\twocat{AssDef}(R, \mcal{O}_X)$ on $X$.

\item[$\vartriangleright$] The Poisson case, in which 
$\twocat{P}(R, X)$ is the stack  of crossed groupoids \lb
$\twocat{PoisDef}(R, \mcal{O}_X)$ on $X$. 
\end{enumerate}
Let 
$(\gerbe{G}, \gerbe{A}, \opn{cp})$ be a twisted object in 
$\twocat{P}(R, X)$, and let $U$ be an open set of $X$.
\begin{enumerate}
\item If $\mrm{H}^2(U, \mcal{O}_X) = 0$ then the groupoid
$\gerbe{G}(U)$ is nonempty.
\item If $\mrm{H}^1(U, \mcal{O}_X) = 0$ then the groupoid
$\gerbe{G}(U)$ is connected.
\end{enumerate}
\end{thm}

\begin{proof}
Let $i$ be a local object of the gauge gerbe $\gerbe{G}$, defined on
some open set $U \subset X$.
We write $\mcal{A}_i := \gerbe{A}(i) \in \twocat{P}(R, X)(U)$, which is
an $R$-deformation of $\mcal{O}_{U}$.
There is an isomorphism of sheaves of groups 
$\opn{cp}: \gerbe{G}(i) \iso \mrm{IG}(\mcal{A}_i)$ on $U$.
By definition 
$\mrm{IG}(\mcal{A}_i) = \opn{Exp}(\m \mcal{A}_i)$, and 
hence for any $p \geq 1$ we get a sheaf of normal subgroups
\[ \gerbe{N}_p(i) := \opn{cp}^{-1}
\bigl( \opn{Exp}(\m^{p} \mcal{A}_i) \bigr) \subset \gerbe{G}(i) . \]
By Lemma \ref{lem:mdd.101}(1) the sequence $\{ \gerbe{N}_p(i) \}_{p \geq 1}$
is a central filtration of the sheaf of groups $\gerbe{G}(i)$, in the sense
of \cite[Definition 6.1]{Ye4}
(except that here the filtration starts at $p = 1$,
whereas in \cite{Ye4} it starts at $p = 0$). Also  
$\gerbe{G}(i) \cong 
\lim_{\leftarrow p}\, \gerbe{G}(i) / \gerbe{N}_p(i)$.

Next suppose $j$ is another object of $\gerbe{G}(U)$, and
$g \in \gerbe{G}(U)(i, j)$. Since 
$\gerbe{A}(g) : \mcal{A}_i \to \mcal{A}_j$ 
is an $R$-linear sheaf isomorphism, and since 
$\opn{cp} : \opn{Aut}_{\gerbe{G}} \twoiso \opn{IG} \circ \, \gerbe{A}$
is a natural isomorphism of functors, it follows that 
$\opn{Ad}(g) \bigl( \gerbe{N}_p(i) \bigr) = 
\gerbe{N}_p(j)$. 
This says that for fixed $p$, the collection 
$\{ \gerbe{N}_p(i) \}$
is a normal subprestack of groupoids of the gerbe $\gerbe{G}$, in the
sense of \cite[Definition 3.6]{Ye4}.
Moreover, there is a central extension of gerbes
\begin{equation} \label{eqn:19}
1 \to \gerbe{N}_p / \gerbe{N}_{p+1} \to 
\gerbe{G} / \gerbe{N}_{p+1} \xar{F}
\gerbe{G} / \gerbe{N}_{p} \to 1 , 
\end{equation}
and an isomorphism
\[ \gerbe{N}_p / \gerbe{N}_{p+1} \cong 
(\m^{p} / \m^{p+1}) \ot \mcal{O}_X  \]
 of sheaves of abelian groups on $X$.
See \cite[Definition 3.10]{Ye4}.
As we let $p$ vary, we have a central filtration
$\{ \gerbe{N}_p \}_{p \geq 1}$ of the gerbe $\gerbe{G}$, and $\gerbe{G}$ is
complete with respect to this filtration, as in 
\cite[Definition 6.5]{Ye4}.

Let $U$ and $\mcal{A}_i$ be as above, and let $V \subset U$ be an
$\mcal{O}_X$-acyclic open set. 
According to Lemma \ref{lem:mdd.101}(2), the open set $V$ is acyclic with
respect to the central filtration 
$\{ \gerbe{N}_p(i) \}_{p \geq 1}$
of the sheaf of groups $\gerbe{G}(i)$, in the sense of
\cite[Definition 6.2]{Ye4}.

Now take an open covering
$\bsym{U} = \{ U_k \}_{k \in K}$ of $X$ such that 
$\opn{Ob} (\gerbe{G}(U_k)) \neq \emptyset$
for every $k \in K$. This is possible because $\gerbe{G}$ is locally nonempty.
Since $X$ has enough $\mcal{O}_X$-acyclic open sets, we can find an open
covering $\bsym{U}' = \{ U'_k \}_{k \in K'}$ which refines $\bsym{U}$, and such
that each finite intersection
$U'_{k_0, \ldots, k_m}$ is $\mcal{O}_X$-acyclic. Note that
$\opn{Ob} (\gerbe{G}(U'_{k_0, \ldots, k_m})) \neq \emptyset$.
The discussion in the previous paragraph (for 
$V := U'_{k_0, \ldots, k_m}$) tells us that the covering $\bsym{U}'$ is
acyclic with respect to the central filtration 
$\{ \gerbe{N}_p \}_{p \geq 1}$ of the gerbe $\gerbe{G}$.
We conclude that there are enough acyclic coverings with respect to 
$\{ \gerbe{N}_p \}_{p \geq 1}$, in the sense of \cite[Definition 6.9]{Ye4}.

Finally let $U$ be an open set of $X$. Then
\[ \mrm{H}^q(U, \gerbe{N}_p / \gerbe{N}_{p+1}) \cong
(\m^{p} / \m^{p+1}) \ot \mrm{H}^q(U, \mcal{O}_X) . \]
According to \cite[Theorem 6.10]{Ye4}, if 
$\mrm{H}^2(U, \gerbe{N}_p / \gerbe{N}_{p+1})$
is trivial for all $p \geq 1$, then then the groupoid
$\gerbe{G}(U)$ is nonempty; and if 
$\mrm{H}^1(U, \gerbe{N}_p / \gerbe{N}_{p+1})$
is trivial for all $p \geq 1$, then then the groupoid
$\gerbe{G}(U)$ is connected.
\end{proof}

Here is an immediate consequence of Theorem \tup{\ref{thm:6}}:

\begin{cor} \label{cor:4}
In the situation of Setup \tup{\ref{setup:200}}, and with 
$\twocat{P}(R, X)$ as in Theorem \tup{\ref{thm:6}}, suppose that
$\bsym{U}$ is an $\mcal{O}_X$-acyclic open covering of $X$. Then
$\bsym{U}$ totally trivializes the stack of crossed groupoids 
$\twocat{P}(R, X)$.
\end{cor}

For a crossed groupoid $\cat{G}$ we denote by 
$\ol{\opn{Ob}}(\cat{G})$ the set of $1$-isomorphism classes of objects.

\begin{cor} \label{cor:7}
In the situation of Theorem \tup{\ref{thm:6}}, suppose that
$\mrm{H}^2(X, \mcal{O}_X) = \lb \mrm{H}^1(X, \mcal{O}_X) = 0$.
Then the function
\begin{equation} \label{eqn:40}
\ol{\opn{Ob}} \bigl( \twocat{P}(R, X)(X) \bigr) \to
\ol{\opn{TwOb}} \bigl( \twocat{P}(R, X) \bigr)
\end{equation}
constructed in Example \tup{\ref{exa:19}} is a bijection.
\end{cor}

\begin{proof}
Let $(\gerbe{G}, \gerbe{A}, \opn{cp})$ be a twisted object of 
$\twocat{P}(R, X)$. By Theorem \ref{thm:6}(1) there exists an object
$i \in \opn{Ob} \bigl( \gerbe{G}(X) \bigr)$.
Let 
$\mcal{A}_i := \gerbe{A}(i) \in \opn{Ob} \bigl( \twocat{P}(R, X)(X) \bigr).$
Then $\gerbe{A}$ is twisted gauge
equivalent to the twisted object generated by $\mcal{A}_i$.
We see that the function (\ref{eqn:40}) is surjective. 

Now suppose that 
$\mcal{A}, \mcal{A}' \in \opn{Ob} ( \twocat{P}(R, X)(X) )$
are such that the corresponding twisted objects
$\gerbe{A}, \gerbe{A}' \in \opn{TwOb}(\twocat{P}(R, X))$
are twisted equivalent. Let 
\[ (\Phi_{\mrm{gau}}, \Phi_{\mrm{rep}}) :
(\gerbe{G}, \gerbe{A}, \opn{cp}) \to 
(\gerbe{G}', \gerbe{A}', \opn{cp}') \]
be a twisted gauge equivalence. 
There is an object
$i \in \opn{Ob} ( \gerbe{G}(X) )$
such that $\mcal{A} = \gerbe{A}(i)$, and there is an object
$i' \in \opn{Ob} ( \gerbe{G}'(X) )$
such that $\mcal{A}' = \gerbe{A}'(i')$.
Let 
$j' := \Phi_{\mrm{gau}}(i) \in \opn{Ob} ( \gerbe{G}'(X) )$; 
so there is an isomorphism 
$\Phi_{\mrm{rep}} : \mcal{A} = \gerbe{A}(i) \iso \gerbe{A}'(j')$
in $\twocat{P}(R, X)$. 

On the other hand, since the groupoid
$\gerbe{G}'(X)$ is connected, there is some isomorphism 
$g' : j' \iso i'$ in it. Therefore we get an isomorphism
$\gerbe{A}'(g') : \gerbe{A}'(j') \iso \gerbe{A}'(i') = \mcal{A}'$
in $\twocat{P}(R, X)(X)$. We see that 
$\mcal{A} \cong \mcal{A}'$ in $\twocat{P}(R, X)(X)$. This proves that 
function (\ref{eqn:40}) is injective. 
\end{proof}

We end this section with an example.

\begin{exa} \label{exa:18}
It is easy to construct an example of a commutative twisted associative (or
Poisson) $\K[[\hbar]]$-deformation of $\mcal{O}_X$ that is really
twisted (Definition \ref{dfn:25}). Take an algebraic variety $X$ with nonzero
cohomology class $c \in \mrm{H}^2(X, \mcal{O}_X)$. 
Let $\bsym{U}$ be an affine open covering of $X$, and let
$\{ c_{k_0, k_1, k_2} \}$ be a normalized \v{C}ech $2$-cocycle representing $c$
on this covering. Now consider the geometric descent datum
$\bsym{d} = \bigl( \{ \mcal{A}_{k_0} \}, \{ g_{k_0, k_1} \}, 
\{ a_{k_0, k_1, k_2} \} \bigr)$
with $\mcal{A}_{k_0} := \mcal{O}_{U_{k_0}}[[\hbar]]$, 
$g_{k_0, k_1} := \bsym{1}$ and
$a_{k_0, k_1, k_2} := \opn{exp}(\hbar c_{k_0, k_1, k_2})$.
The corresponding twisted deformation $\gerbe{A}$ that we get by Theorem
\ref{thm:glu.1} (namely $\gerbe{A} := \opn{glu}(\bsym{d})$ in Lemma
\ref{lem:bitorsors.9}) will have obstruction
class $c$ in the first order central extension.
More precisely, in the central extension of gerbes (\ref{eqn:19}),
with $p = 1$, the obstruction class for the unique (up to isomorphism)
object $j$ of $(\gerbe{G} / \gerbe{N}_1)(X)$ is
\[ \opn{cl}^2_{F}(j) = c \hbar 
\in \mrm{H}^2 \bigl( X, 
(\m / \m^{2}) \ot \mcal{O}_X \bigr) , \]
which is nonzero. According to \cite[Theorem 4.17]{Ye4} we have
$\opn{Ob} \bigl( (\gerbe{G} / \gerbe{N}_2)(X) \bigr) = \emptyset$, 
implying that 
$\opn{Ob} \bigl( \gerbe{G}(X) \bigr) = \emptyset$. 
\end{exa}
