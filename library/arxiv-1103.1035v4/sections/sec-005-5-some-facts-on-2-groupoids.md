---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-005-5-some-facts-on-2-groupoids
section_title: "Some Facts on 2-Groupoids"
section_number: 5
pages: 18-21
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.979
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:2-grpd}

Let us recall that a (strict) {\em $2$-groupoid} $\bsym{G}$ is a groupoid
enriched in the monoidal category of groupoids. Another way of saying this is
that a $2$-groupoid $\bsym{G}$ is a $2$-category in which all $1$-morphisms and
$2$-morphisms are invertible. A comprehensive review of $2$-categories and
related constructions is available in \cite[Section 1]{Ye3}. 
See also \cite{Ma, Bw, Ge}.

We wish to make things as explicit as possible, to make calculations
(both in Section \ref{sec:del-2-grpd} of this paper, and in the new
version of \cite{Ye4}) easier.
A (small strict) $2$-groupoid $\bsym{G}$ is made up of the following
ingredients: there
is a set $\opn{Ob}(\bsym{G})$, whose elements are the {\em objects}
of $\bsym{G}$. For any $x, y \in \opn{Ob}(\bsym{G})$ there is a set 
$\bsym{G}(x, y)$, whose elements are called the {\em $1$-morphisms} from $x$
to $y$. Given $f \in \bsym{G}(x, y)$, we write $f : x \to y$. 
For any $f, g \in \bsym{G}(x, y)$ there is a set 
$\bsym{G}(x, y)(f, g)$, whose elements are called the {\em $2$-morphisms} from
$f$ to $g$. For $a \in \bsym{G}(x, y)(f, g)$ we write 
$a : f \twoto g$. 

There are three types of composition operations in $\bsym{G}$. There is {\em
horizontal composition of $1$-morphisms}: given $f_1 : x_0 \to x_1$ and 
$f_2 : x_1 \to x_2$, their composition is
$f_2 \circ f_1 : x_0 \to x_2$. Suppose we are also given $1$-morphisms 
$g_i : x_{i-1} \to x_i$ and $2$-morphisms $a_i : f_i \twoto g_i$. Then there is
a $2$-morphism 
\[ a_2 \circ a_1 : f_2 \circ f_1 \twoto g_2 \circ g_1 . \]
This is {\em horizontal composition of $2$-morphisms}. 
If we are also given \lb $1$-morphisms 
$h_i : x_{i-1} \to x_i$ and $2$-morphisms $b_i : g_i \twoto h_i$,
then there is the {\em vertical composition} (of $2$-morphisms) 
$b_i \ast a_i : f_i \twoto h_i$. 
There are pretty diagrams to display all of this (see \cite[Section 1]{Ye3} or
many other references). 

For every $x \in \opn{Ob}(\bsym{G})$ there is the identity $1$-morphism 
$\bsym{1}_x : x \to x$, and for every 
$f \in \bsym{G}(x, y)$ there is the identity $2$-morphism 
$\bsym{1}_f : f \twoto f$. 

Here are the conditions required for the structure $\bsym{G}$ to be a 
$2$-groupoid: 
\begin{itemize}
\item The set $\opn{Ob}(\bsym{G})$, together with the $1$-morphisms
$f : x \to y$, horizontal composition $g \circ f$, and the identity morphisms 
$\bsym{1}_x$, is a groupoid. 
We refer to this groupoid as the $1$-truncation of $\bsym{G}$. 

\item For every $x, y \in \opn{Ob}(\bsym{G})$, the set 
$\bsym{G}(x,y)$, together with the $2$-morphisms 
$a : f \twoto g$, vertical composition
$b \ast a$, and the identity morphisms $\bsym{1}_f$, is a groupoid. We refer
to it as the vertical groupoid above $(x, y)$. 

\item Horizontal composition of $2$-morphisms is associative, 
$\bsym{1}_{g \circ f} = \bsym{1}_g \circ \bsym{1}_f$ whenever $g$ and $f$ are
composable, and the $2$-morphisms $\bsym{1}_{\bsym{1}_x}$ are identities for
horizontal composition.

\item The exchange condition: given $f_i, g_i, h_i : x_{i-1} \to x_i$,
$a_i : f_i \twoto g_i$ and $b_i : g_i \twoto h_i$, one has
\[ (b_2 \ast a_2) \circ (b_1 \ast a_1) = 
(b_2 \circ b_1) \ast (a_2 \circ a_1) , \]
as $2$-morphisms $f_2 \circ f_1 \twoto h_2 \circ h_1$.
\end{itemize}

A consequence of these four conditions is that $2$-morphisms are invertible for
horizontal composition. Indeed, given $a : f \twoto g$ in 
$\bsym{G}(x, y)$,  its horizontal inverse 
$a^{- \circ} : f^{-1} \twoto g^{-1}$ is given by the formula
$a^{- \circ} = \bsym{1}_{g^{-1}} \circ a^{- \ast} \circ \bsym{1}_{f^{-1}}$,
where 
$a^{- \ast} : g \twoto f$ is the vertical inverse of $a$. 

Suppose $\bsym{H}$ is another $2$-groupoid. A (strict) {\em $2$-functor} 
$F : \bsym{G} \to \bsym{H}$ is a collection of functions 

\[ \begin{aligned}
F & : \opn{Ob}(\bsym{G}) \to \opn{Ob}(\bsym{H})
\\
F & : \bsym{G}(x_0, x_1) \to \bsym{H} \bigl( F(x_0), F(x_1) \bigr)
\\
F & : \bsym{G}(x_0, x_1)(g_0, g_1) \to 
\bsym{H} \bigl( F(x_0), F(x_1) \bigr) \bigl( F(g_0), F(g_1) \bigr) 
\end{aligned} \]
that respect the various compositions and identity morphisms. We denote by
$\cat{2-Grpd}$ the category consisting of $2$-groupoids and $2$-functors between
them.  

Consider a $2$-groupoid $\bsym{G}$. There is an equivalence relation on the set 
$\opn{Ob}(\bsym{G})$, given by existence of $1$-morphisms, i.e.\ $x \sim y$ if 
$\bsym{G}(x, y) \neq \emptyset$. We let 
$\pi_0(\bsym{G}) := \opn{Ob}(\bsym{G}) / {\sim}$. 

For objects $x, y \in \opn{Ob}(\bsym{G})$ there is an equivalence relation on
the set $\bsym{G}(x, y)$, given by existence of $2$-morphisms:
$f \sim g$ if $\bsym{G}(x, y)(f, g) \neq \emptyset$. We let 
\[ \pi_1(\bsym{G}, x, y) := \bsym{G}(x, y) / {\sim} . \]
We define $\pi_1(\bsym{G})$ to be the  groupoid with object set
$\opn{Ob}(\bsym{G})$, \lb
morphism sets $\pi_1(\bsym{G}, x, y)$, and composition induced by horizontal
composition in $\bsym{G}$. Thus $\pi_1(\bsym{G})$ is a quotient groupoid of the
$1$-truncation of $\bsym{G}$, and \lb
$\pi_0(\pi_1(\bsym{G})) = \pi_0(\bsym{G})$.
We write $\pi_1(\bsym{G}, x) := \pi_1(\bsym{G}, x, x)$, which is a group.
We also define 
\[ \pi_2(\bsym{G}, x)  := \bsym{G}(x, x)(\bsym{1}_x, \bsym{1}_x) . \]
This is an abelian group. 

The homotopy set $\pi_0(\bsym{G})$ and groups $\pi_i(\bsym{G}, x)$ are
functorial in an obvious way. 
A morphism $F : \bsym{G} \to \bsym{H}$ in 
$\cat{2-Grpd}$ is called a {\em weak equivalence} if the functions 
\[ \begin{aligned}
\pi_0(F) & : \pi_0(\bsym{G}) \to \pi_0(\bsym{H})
\\
\pi_1(F, x) & : \pi_1(\bsym{G}, x) \to \pi_1(\bsym{H}, F(x))
\\
\pi_2(F, x) & : \pi_2(\bsym{G}, x) \to \pi_2(\bsym{H}, F(x))
\end{aligned} \]
are bijective for all $x \in \opn{Ob}(\bsym{G})$. 

It will be useful to relate the concept of $2$-groupoid to the less
familiar concept of {\em crossed module over a groupoid}, recalled below.

For a groupoid $\bsym{G}$ and an object $x \in \opn{Ob}(\bsym{G})$
we denote by $\bsym{G}(x) := \bsym{G}(x, x)$, the automorphism group of $x$. 
The composition in $\bsym{G}$ is $\circ = \circ_{\bsym{G}}$.

Let $\bsym{G}$ and $\bsym{N}$ be groupoids, such that 
$\opn{Ob}(\bsym{G}) = \opn{Ob}(\bsym{N})$. An {\em action} $\Psi$ of $\bsym{G}$
on 
$\bsym{N}$ is a collection of group isomorphisms 
\[ \Psi(g) : \bsym{N}(x) \iso \bsym{N}(y) \]
for all $x, y \in \opn{Ob}(\bsym{G})$ and $g \in \bsym{G}(x, y)$, 
such that 
\[ \Psi(h \circ g) = \Psi(h) \circ \Psi(g) \]
whenever $g$ and $h$ are composable, and 
$\Psi(\bsym{1}_x) = \bsym{1}_{\bsym{N}(x)}$.

\begin{exa}
Let $\bsym{G}$ be any groupoid. The adjoint action $\opn{Ad}_{\bsym{G}}$ of
$\bsym{G}$ on itself is defined by
\[ \opn{Ad}_{\bsym{G}}(g)(h) := g \circ h \circ g^{-1} \]
for $g \in \bsym{G}(x, y)$ and $h \in \bsym{G}(x)$.
\end{exa}

A {\em crossed module over a groupoid}, or a {\em crossed groupoid} 
for short, is data \lb
$(\bsym{G}, \bsym{N}, \Psi, \opn{D})$ consisting of:
\begin{itemize}
\item Groupoids $\bsym{G}$ and $\bsym{N}$, such that
$\bsym{N}$ is totally disconnected, and  
$\opn{Ob}(\bsym{N}) = \opn{Ob}(\bsym{G})$.

\item An action $\Psi$ of $\bsym{G}$ on $\bsym{N}$, called the {\em twisting}.

\item A morphism of groupoids (i.e.\ a functor)
$\opn{D} : \bsym{N} \to \bsym{G}$, called the {\em feedback}, which is the 
identity on objects.
\end{itemize}

These are the conditions:
\begin{enumerate}
\rmitem{i} The morphism $\opn{D}$ is $\bsym{G}$-equivariant with respect to
the actions $\Psi$ and $\opn{Ad}_{\bsym{G}}$. Namely 
\[ \opn{D}(\Psi(g)(a)) = \opn{Ad}_{\bsym{G}}(g)(\opn{D}(a)) \]
in the group $\bsym{G}(y)$, for any $x, y \in \opn{Ob}(\bsym{G})$, 
$g \in \bsym{G}(x, y)$ and $a \in \bsym{N}(x)$.

\rmitem{ii} For any $x \in \opn{Ob}(\bsym{G})$ and 
$a \in \bsym{N}(x)$ there is equality
\[ \Psi(\opn{D}(a)) = \opn{Ad}_{\bsym{N}(x)}(a) , \]
as automorphisms of the group $\bsym{N}(x)$.
\end{enumerate}

\begin{exa}
If $\bsym{G}$ and $\bsym{N}$ are groups, namely 
$\opn{Ob}(\bsym{G}) = \opn{Ob}(\bsym{N}) = \{ 0 \}$, then 
a crossed groupoid is just a crossed module.
\end{exa}

\begin{exa} \label{exa:100}
Let $G$ be a group acting on a set $X$. For $x \in X$ let $G(x)$ denote the
stabilizer of $x$. Let $\{ N_x \}_{x \in X}$ be a 
collection of groups. Assume that for every $g \in G$ and $x \in X$ there is
given a group isomorphism $\Psi(g) : N_x \iso N_{g(x)}$, and these satisfy the
functoriality conditions of an action. 
Also assume there are
group homomorphisms $\opn{D}_x : N_x \to G(x)$ such that 
\[ \opn{Ad}_{G}(g) \circ \opn{D}_x = \opn{D}_{g(x)} \circ \, \Psi(g) \]
for any $g \in G$ and $x \in X$. 

Define $\bsym{G}$ to be the transformation groupoid associated to the
action of $G$ on $X$. And define $\bsym{N}$ to be the totally
disconnected groupoid with $\opn{Ob}(\bsym{N}) := X$ and 
$\bsym{N}(x) := N_x$. Then 
$( \bsym{G}, \bsym{N}, \Psi, \opn{D})$ is a crossed
groupoid, which we call the {\em transformation crossed groupoid} associated to
the action of $G$ on $\{ N_x \}_{x \in X}$.
\end{exa}

\begin{exa}
Suppose $\bsym{G}$ is any groupoid, and $\bsym{N}$ is a {\em normal subgroupoid}
of $\bsym{G}$, in the sense of \cite{Bw, Ye4}. Let 
$\opn{D} : \bsym{N}\to \bsym{G}$ be the inclusion, and let 
$\Psi$ be the restriction of $\opn{Ad}_{G}$ to $\bsym{N}$. Then 
$(\bsym{G}, \bsym{N}, \Psi, \opn{D})$ is a crossed groupoid.
\end{exa}

It is known that crossed groupoids are the same as $2$-groupoids
(cf.\ \cite{Bw}). We will now give a precise statement of this fact. 

\begin{prop} \label{prop:102}
Let $(\bsym{H}, \bsym{N}, \Psi, \opn{D})$ 
be a crossed groupoid. Then there is a unique $2$-groupoid 
$\bsym{G}$ with these properties:
\begin{enumerate}
\rmitem{i} The $1$-truncation of $\bsym{G}$ is the same groupoid as
$\bsym{H}$. Namely $\opn{Ob}(\bsym{G}) = \opn{Ob}(\bsym{H})$,
$\bsym{G}(x, y) = \bsym{H}(x, y)$, the identity morphisms $\bsym{1}_x$ are the
same, and the horizontal composition is 
$g \circ_{\bsym{G}} f = g \circ_{\bsym{H}} f$
for $f : x \to y$ and $g : y \to z$.

\rmitem{ii} For any $f, g : x \to y$ in $\bsym{G}$ we have
\[ \bsym{G}(x, y)(f, g) = 
\{ a \in \bsym{N}(x) \mid g = f \circ_{\bsym{H}} \opn{D}(a) \} . \]
The identity morphism $\bsym{1}_f \in \bsym{G}(x, y)(f, f)$ is 
$\bsym{1}_x \in \bsym{N}(x)$.
Given $h : x \to y$, $a : f \twoto g$ and $b : g \twoto h$,
the vertical composition is 
$b \ast_{\bsym{G}} a = a \circ_{\bsym{N}} b$.

\rmitem{iii} For any $x_0, x_1, x_2 \in \opn{Ob}(\bsym{G})$, any
$f_i, g_i : x_{i-1} \to x_i$ and any
$a_i : f_i \twoto g_i$ in $\bsym{G}$, 
the horizontal composition $a_2 \circ_{\bsym{G}} a_1$ satisfies
\[ a_2 \circ_{\bsym{G}} a_1 =  
\Psi(f_1^{-1})(a_2) \circ_{\bsym{N}} a_1 . \]
\end{enumerate}

Moreover, any $2$-groupoid $\bsym{G}$ arises this way. 
\end{prop}

\begin{proof}
It is easy to verify that the conditions of a $2$-groupoid hold. 

Conversely, suppose $\bsym{G}$ is any $2$-groupoid. Define the groupoid
$\bsym{G}_1$ to be the $1$-truncation of $\bsym{G}$. 

For any $x \in \opn{Ob}(\bsym{G})$ consider the set of $2$-morphisms
\begin{equation} \label{eqn:105}
\bsym{G}_2(x) := \coprod_{g \in \bsym{G}(x, x)} 
\bsym{G}(x, x)(\bsym{1}_x, g) .
\end{equation}
This is a group under horizontal composition $\circ_{\bsym{G}}$
of $2$-morphisms, with identity element 
$\bsym{1}_{\bsym{1}_x}$. There is a group homomorphism 
$\opn{D} : \bsym{G}_2(x) \to \bsym{G}_1(x)$, defined by 
\begin{equation} \label{eqn:104}
\opn{D}(a : \bsym{1}_x \twoto g) := g  .
\end{equation}
Let $\bsym{G}_2$ be the totally disconnected groupoid with set of objects 
$\opn{Ob}(\bsym{G})$, and automorphism groups $\bsym{G}_2(x)$ as defined above.
Then $\opn{D} : \bsym{G}_2 \to \bsym{G}_1$
is a morphism of groupoids.

A $1$-morphism $f : x \to y$ in $\bsym{G}$ induces a group isomorphism 
\[ \opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}(f) : 
\bsym{G}_2(x) \to \bsym{G}_2(y) , \]
with formula
\begin{equation} \label{eqn:106}
\opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}(f)(a) := 
\bsym{1}_f \circ a \circ \bsym{1}_{f^{-1}} 
\end{equation}
for $a \in \bsym{G}_2(x)$.
It is a simple verification that
$(\bsym{G}_1, \bsym{G}_{2}, 
\opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}, \opn{D})$
is a crossed groupoid.
\end{proof}

\begin{rem}
An amusing consequence of the proof above is that the vertical
composition in a $2$-groupoid can be recovered from the horizontal
compositions.
\end{rem}

In view of Proposition \ref{prop:102}, in a $2$-groupoid $\bsym{G}$ 
we can talk about the group of $2$-morphisms 
$\bsym{G}_2(x)$ for any object $x$. There is a feedback homomorphism 
\[ \opn{D} :  \bsym{G}_2(x) \to \bsym{G}_1(x) , \]
and a twisting 
\[ \opn{Ad}(g) =  
\opn{Ad}_{\bsym{G}_1 \curvearrowright \bsym{G}_{2}}(g) :
\bsym{G}_2(x) \to \bsym{G}_2(y)  \]
for any $g : x \to y$.
These satisfy the conditions of a crossed groupoid.
