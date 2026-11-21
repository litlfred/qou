---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-017-31-realizations-of-coxeter-systems
section_title: "Realizations of Coxeter systems"
section_number: 3.1
pages: 18-22
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.98
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-realization}


For both Soergel's construction of Soergel bimodules, and for our construction of a diagrammatic category by generators and relations, the starting point will be the data of a realization
of a Coxeter system.

\begin{defn} \label{defn:realization} Let $\Bbbk$ be a commutative ring. A \emph{realization} of $(W,S)$ over $\Bbbk$ is a free, finite rank $\Bbbk$-module $\hg$, together with subsets $\{ \a_s^\vee \; | \; s \in S\} \subset \hg$ and $\{ \a_s \; | \; s \in S\} \subset \hg^* = \Hom_{\Bbbk}(\hg,\Bbbk)$, satisfying:
\begin{enumerate}
\item $\langle \alpha_s^\vee, \alpha_s \rangle = 2$ for all $s \in S$;
\item the assignment $s(v) \define v - \langle v, \alpha_s\rangle \alpha_s^{\vee}$ for all $v \in \hg$ yields a representation of $W$;
\item the technical condition in \eqref{eq:technical-condition} is satisfied. (Its description requires some background.)
\end{enumerate}
We will often refer to $\hg$ as a realization, however the choice of $\{ \alpha_s^\vee \}$ and $\{\alpha_s \}$ is always implicit. \end{defn}


Given a realization over $\Bbbk$ and a homomorphism $\Bbbk \to \Bbbk'$ we obtain a realization $\Bbbk' \otimes_{\Bbbk} \hg$ over $\Bbbk'$ by base change. We call a realization
\emph{faithful} if the action of $W$ on $\hg$ (and hence the contragredient action on $\hg^*$) is faithful. Base change does not preserve faithfulness in general. For us, the ability to
perform base change is the more important property, so we must allow realizations which are not faithful. For instance, any realization of the dihedral group with $m_{st}=m<\infty$ is also
a realization of the dihedral group with $m_{st}=2m, 3m, \ldots$, and is also a realization of the infinite dihedral group.

We call a realization \emph{symmetric} if $\langle \alpha_s^\vee, \alpha_t \rangle = \langle \alpha_t^\vee, \alpha_s \rangle$ for all $s, t \in S$.

\begin{ex} \label{ex:realizations} Some examples of realizations that we have in mind are the following:
  \begin{enumerate}
  \item Let $(W,S)$ be any Coxeter system of finite rank. Let $\Bbbk = \RM$ and $\hg = \bigoplus_{s \in S} \RM \alpha_s^{\vee}$. Define elements $\{ \alpha_s \} \subset \hg^*$ by
\begin{equation} \label{eq:justcos}
\langle \alpha_t^\vee, \alpha_s \rangle = -2\cos(\pi/m_{st})
\end{equation}
(by convention $m_{ss} =1$ and $\pi/\infty = 0$). Then $\hg$ is a symmetric realization of $(W,S)$, called the \emph{geometric representation} (see \cite[\S 5.3]{Humphreys}). Note that the subset $\{ \alpha_s \} \subset  \hg^*$ is linearly independent if and only if $W$ is finite.

\item
More generally, given a real vector space $\hg$ with subsets $\{ \alpha_s^{\vee} \} \subset \hg$ and $\{ \alpha_s \} \subset \hg^*$ satisfying \eqref{eq:justcos} then $\hg$ is a realization of $(W,S)$. In  \cite[\S 2]{Soe3} Soergel builds his theory of Soergel bimodules for arbitrary Coxeter systems on a realization for which both $\{ \alpha_s^{\vee} \} \subset \hg$ and $\{ \alpha_s \} \subset \hg^*$ are linearly independent, and such that $\hg$ has minimal dimension with this property. To construct such a representation, Soergel mimics the construction of the action of an affine Weyl group on the Cartan subalgebra of an affine Kac-Moody group.

\item Let $(X, R, X^\vee, R^\vee)$ be a (reduced) root datum (see \cite[\S 7.4]{SprLAG} for notation) and let $\Delta \subset R$ be a set of simple roots. Let $(W,S)$ be the corresponding Weyl group and simple reflections. Then the triple $\hg = X$, $\{\alpha \; | \; \alpha \in \Delta \} \subset \hg$ and $\{\alpha^\vee \; | \; \alpha \in \Delta \} \subset \hg^* = X^\vee$ gives a faithful realization of $(W,S)$ over $\ZM$. We obtain a (potentially non-faithful) realization of $(W,S)$ over any $\Bbbk$ by extension of scalars.

\item
More generally, if $A$ is a generalized Cartan matrix and $\tg$ denotes the Cartan subalgebra of the corresponding Kac-Moody Lie algebra $\gg(A)$ (see \cite[Chapters 1 and 3]{KacBook}) then any choice of $\ZM$-lattices $\hg \subset \tg$ such that $\hg$ contains the root lattice and its dual lattice $\hg^* \subset \tg^*$ contains the coroot lattice yields a realization of the Weyl group $(W,S)$ of $\gg(A)$. In this way one obtains realizations over $\ZM$ (and hence over any $\Bbbk$) of any Coxeter system for which $m_{st} \in \{ 2,3,4,6, \infty\}$ for all $s \ne t \in S$. (Such Coxeter systems are called \emph{crystallographic}.)

\item Let $(W,S)$ be a Coxeter system for  which $m_{st} \in \{ 2,3,5,\infty\}$ and let $\Bbbk = \ZM[\phi]$ where $\phi = (1 + \sqrt{5})/2$ denotes the golden ratio. Let $\hg = \bigoplus_{s \in S} \Bbbk \alpha_s^{\vee}$ and define $\alpha_s \in \hg^*$ via
\[
\langle \alpha_s^\vee, \alpha_t \rangle = \begin{cases} 2 & \text{if $s = t$,} \\ 0 & \text{if $m_{st} =2 ,$} \\ -1 & \text{if $m_{st} =3 ,$} \\ -\phi & \text{if $m_{st} =5,$} \\ -2 & \text{if $m_{st} =\infty.$} \end{cases}
\]
Using that $-2\cos(\pi/5) = -\phi$ it follows from the example of the geometric realization that $(\hg, \{ \alpha_s^{\vee} \}, \{ \alpha_s \})$ is a (symmetric) realization of $(W,S)$ over $\Bbbk$. In particular, the finite reflection groups of types $H_3$ and $H_4$ have symmetric realizations over (any extension of) $\Bbbk$.

\item Let $(W,S)$ be the affine Weyl group of type $\widetilde{A_n}$ for $n \ge 2$. Let $\Bbbk = \ZM[q,q^{-1}]$ and $\hg = \bigoplus_{s \in S} \ZM[q,q^{-1}] \alpha_s^{\vee}$, and let the values of
$\langle \alpha_s^\vee, \alpha_t \rangle$ be encoded (as will be described soon) in the following matrix: \[A = \left( \begin{array}{ccccc} 2 & -1 & 0 & 0 & -q^{-1} \\ -1 & 2 & -1 & 0 & 0
\\ 0 & -1 & 2 & -1 & 0 \\ 0 & 0 & -1 & 2 & -q \\ -q & 0 & 0 & -q^{-1} & 2 \end{array} \right).\] 
(More precisely, this is the example when $n = 4$.)
This gives a realization of $W$. Specializing $q$ to an element of $\CM \setminus \RM$, one
obtains a realization of $W$ over $\CM$ which can not be obtained by extension of scalars from a realization defined over $\RM$.
\end{enumerate}
\end{ex}

Given a realization $(\hg, \{\alpha_s^{\vee} \}, \{\alpha_s\})$ of $(W,S)$ over $\Bbbk$ we can consider its \emph{Cartan matrix} $(\langle \alpha_s^\vee, \alpha_t \rangle ) _{s,t \in S}$.
Clearly a realization is symmetric if and only if its Cartan matrix is. Conversely, given a matrix $(a_{st})_{s,t \in S}$ such that $a_{ss}=2$, one can construct the free $\Bbbk$-module
$\hg = \bigoplus_{s \in S} \Bbbk \alpha_s^{\vee}$, and define $\alpha_s \in \hg^*$ by $\langle \alpha_s^\vee, \alpha_t \rangle = a_{st}$. When this yields a realization of $(W,S)$ we call
the matrix $(a_{st})$ a \emph{Cartan matrix} for $(W,S)$ over $\Bbbk$. Any realization for which $\{\a_s^\vee\}$ is a basis for $\hg$ can be reconstructed from its Cartan matrix; we call
such realizations \emph{minimal}.

\begin{ex} In Example \ref{ex:realizations} the realizations discussed in (1), (5) and (6) are minimal. The example in (3) is minimal if and only if the root system is simply connected and
of adjoint type (so that root lattice coincides with $\hg$). Examples (2) and (4) are not minimal in general. \end{ex}

\begin{remark} We expect that there is a rich Koszul duality theory for categories obtained from Soergel bimodules for arbitrary Coxeter systems (generalizing Soergel's description
\cite{Soe1} of the algebra of category $\OC$ in the case of Weyl groups). Here one expects Koszul duality to exchange $\hg$ and $\hg^*$, roots and coroots. In this setting it seems natural
to require both $\{ \alpha_s^{\vee} \} \subset \hg$ and $\{ \alpha_s \} \subset \hg^*$ to be linearly independent. This explains in part why we do not assume that our realizations are
minimal. \end{remark}

It is natural to ask under which conditions a matrix $(a_{st})_{s,t \in S}$ with $a_{ss} = 2$ is a Cartan matrix of $(W,S)$. A thorough discussion of this can be found in the appendix to
\cite{EDihedral}. We provide a short discussion here.

\begin{defn} \label{def:2qnum} Define the \emph{2-colored quantum numbers} $[k]_x$ and $[k]_y$ inside the ring $\ZM[x,y]$ inductively. One has $[0]_x = [0]_y = 0$, $[1]_x = [1]_y = 1$, and $[2]_x = x$, $[2]_y=y$. The other 2-colored quantum numbers are defined by the rules

\begin{subequations}
\begin{equation} [2]_x [k]_y = [k+1]_x + [k-1]_x, \end{equation}
\begin{equation} [2]_y [k]_x = [k+1]_y + [k-1]_y. \end{equation}
\end{subequations}

When $k$ is odd, $[k]_x = [k]_y$ and we shorten the notation to $[k]$. \end{defn}

Fix a pair $s,t \in S$ and let $x=a_{st}$ and $y=a_{ts}$. The condition that $(st)$ has order exactly $k$ is an algebraic condition on $x$ and $y$. For instance, when $\a_s$ and $\a_t$ are
linearly independent, the action of $(st)$ on their span has order $k$ when $[2k+1]=1$ and $[2k]_x = [2k]_y = 0$. In fact, this implies further that $2[k]_x = 2[k]_y = [2]_x [k]_y = [2]_y
[k]_x = 0$. This suggests that one should set \begin{equation} \label{eq:technical-condition} [m_{st}]_x = [m_{st}]_y = 0. \end{equation} This is the technical condition mentioned in
Definition \ref{defn:realization}. While \eqref{eq:technical-condition} is sufficient to imply that $(st)$ has order dividing $k$ on the span of the roots, it is independent of the
condition that $W$ acts on $\hg$. The reason that \eqref{eq:technical-condition} is required is to ensure that 2-colored Jones-Wenzl projectors are rotation-invariant, as discussed in
section \ref{subsec-JW}.

If either $x$ or $y$ is a non-zero-divisor, then \eqref{eq:technical-condition} is equivalent to the statement that $xy$ satisfies the minimal polynomial of the algebraic integer $4
\cos^2(\frac{\pi}{m})$. If this algebraic integer does not exist in $\Bbbk$ then $(W,S)$ does not admit a realization over $\Bbbk$. Any Coxeter system (of finite rank) admits a realization
over some ring of integers. Finally, we introduce one other technical condition.

\begin{defn} We call a realization \emph{balanced} if for every $s,t \in S$ one has $[m_{st}-1]_x = [m_{st}-1]_y = 1$. We refine this notion by calling the realization \emph{even-balanced}
(resp. \emph{odd-balanced}) if this property holds when $m_{st}$ is even (resp. odd). The opposite of even-balanced is \emph{even-unbalanced}. \end{defn}

The familiar Cartan matrices of Weyl groups are balanced. However, the Cartan matrix of type $A_2$ is not balanced when viewed as a realization of $G_2$. The exotic Cartan matrices for
type $\tilde{A}_n$, $n \ge 3$ given in Example (6) above are not balanced, except when $q=1$. Being balanced is equivalent to the existence of an unambiguous notion of positive roots in
$\hg^*$; when the realization is symmetric, being balanced is similar to the condition that simple roots form an obtuse angle. Faithful realizations are almost always even-balanced; any
minimal even-unbalanced realization over a domain is not faithful. Once again, a thorough discussion of these technicalities can be found in \cite{EDihedral}.

Fix a realization $(\hg, \{ \alpha_s^\vee \}, \{ \alpha_s \})$ of $(W,S)$ and let \[ R = \bigoplus_{m \ge 0} S^m(\hg^*) \] denote the symmetric algebra on $\hg^*$, which we view as a
graded $\Bbbk$-algebra with $\deg \hg^* = 2$. Then $W$ acts on $\hg^*$ via the contragredient representation ($s(\gamma) = \gamma - \langle \alpha_s^\vee, \gamma \rangle \alpha$ for all
$\g \in \hg^*$) and this extends to an action of $W$ on the algebra $R$ by graded automorphisms. We think of $R$ as the polynomial functions on $\hg$.

We let $R-\Mod$ and $R-\Bim$ denote the category of graded $R$-modules and bimodules respectively. We view $R-\Mod$ and $R-\Bim$ as graded categories; that is, as categories enriched in
graded $\Bbbk$-modules. We denote the grading shift by $(1)$: if $M = \bigoplus M^i$ is a graded (bi)module then $M(1)^i = M^{i+1}$. Degree $0$ maps of (graded) $R$-(bi)modules will be
denoted by $\Hom_0(M,N)$.
