---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-004-4-localization-of-commutative-dg-rings
section_title: "Localization of Commutative DG Rings"
section_number: 4
pages: 19-24
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.96
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:localiz}

In this section we specialize to DG rings satisfying a commutativity 
condition. Such a DG ring $A$ can be localized on $\opn{Spec} \bar{A}$. 

\begin{dfn} \label{dfn:305}
Let $A = \bigoplus_{i \in \Z} A^i$ be a DG ring. 
\begin{enumerate}
\item $A$ is called {\em weakly commutative} if 
$b \cd a =  (-1)^{i j} \cd a \cd b$ 
for all $a \in A^{i}$ and $b \in A^{j}$.

\item $A$ is called {\em strongly commutative} if it is weakly commutative, and 
if $a \cd a = 0$ for all $a \in A^{i}$ with $i$ odd.

\item $A$ is called a {\em commutative DG ring} if it is  strongly commutative 
and nonpositive. 
\end{enumerate}
\end{dfn}

If $A$ is weakly commutative, then any left DG 
$A$-module $M$ can be viewed as a
right DG $A$-module. The formula for the right action is this: 
$m \cd a := (-1)^{i j} \cd a \cd m$ 
for $a \in A^i$ and $m \in M^j$.

The full subcategory of $\cat{DGR}$ on the commutative DG rings 
is denoted by $\cat{DGR}^{\leq 0}_{\mrm{sc}}$.

\begin{conv} \label{conv:100}
By default, all DG rings from here on in the paper are 
commutative (Definition \ref{dfn:305}(3)), unless explicitly stated otherwise; 
i.e.\ we work inside $\cat{DGR}^{\leq 0}_{\mrm{sc}}$.
In particular all rings are commutative by default. 
\end{conv}

Since our DG rings are now commutative, we can talk about cohomologically 
pseudo-noetherian DG rings, instead of cohomologically left pseudo-noetherian 
ones (Definition \ref{dfn:391}).

\begin{rem} \label{rem:580}
In \cite{YZ1}, and in earlier versions of this paper, we used the name 
``super-commutative'' for what we now call ``strongly commutative''. The book 
\cite{ML} uses the term ``strictly commutative''. 

Of course when $2$ is invertible in the ring $A^0$ (e.g.\ in characteristic 
$0$), there is no difference between weakly commutative and strongly 
commutative DG rings.

The reader may wonder why we chose to work in the category 
$\cat{DGR}^{\leq 0}_{\mrm{sc}}$ of strongly commutative nonpositive DG rings, 
and not in the category $\cat{DGR}^{\leq 0}_{\mrm{wc}}$ of
weakly commutative ones. Here is the reason. 

Consider any nontrivial commutative 
base ring $\K$ (e.g.\ $\K = \Z$), and the corresponding slice category 
$\cat{DGR}^{\leq 0}_{\mrm{sc}} / \K$.
Let $X$ be a set of nonpositive graded variables. 
The strongly commutative polynomial ring 
in $X$ (see \cite[Definition 3.10]{Ye5}) is denoted by $\K_{\mrm{sc}}[X]$. 
It is easy to see that $\K_{\mrm{sc}}[X]$ is a flat $\K$-module. 
A DG ring $A \in \cat{DGR}^{\leq 0}_{\mrm{sc}} / \K$
is called semi-free if $A^{\natural} \cong \K_{\mrm{sc}}[X]$ for some $X$.
Such a semi-free DG ring $A$ is a bounded above complex of flat $\K$-modules, 
and thus it is a K-flat DG $\K$-module. We had shown in \cite{YZ1} that there 
are enough semi-free resolutions in $\cat{DGR}^{\leq 0}_{\mrm{sc}} / \K$.
Therefore there are enough K-flat resolutions in 
$\cat{DGR}^{\leq 0}_{\mrm{sc}} / \K$.

On the other hand, let us examine the category 
$\cat{DGR}^{\leq 0}_{\mrm{wc}} / \Z$.
The weakly commutative polynomial ring $\Z_{\mrm{wc}}[x]$ over $\Z$, 
in a single variable $x$ of degree $-1$, has this structure as a graded 
$\Z$-module:
\[ \Z_{\mrm{wc}}[x] = \Z \oplus (\Z \cd x) \oplus 
\bigl( \smfrac{\Z}{(2)} \cd x^2 \bigr) \oplus 
\bigl( \smfrac{\Z}{(2)} \cd x^3 \bigr)  \oplus \cdots . \] 
We see that it is not flat over $\Z$. Moreover, it is not hard to see that if
$A$ is any object in $\cat{DGR}^{\leq 0}_{\mrm{wc}} / \Z$
such that $A^{\natural} \cong \Z_{\mrm{wc}}[x]$,
then $A$ is not a K-flat DG $\Z$-module. 
Similarly, it seems that any semi-free object 
$A \in \cat{DGR}^{\leq 0}_{\mrm{wc}}$ that has a nontrivial degree $-1$ 
component, also fails to be a K-flat DG 
$\Z$-module. The upshot is that, most likely, {\em there are not enough 
K-flat resolutions in $\cat{DGR}^{\leq 0}_{\mrm{wc}} / \Z$}.
\end{rem}

\begin{prop} \label{prop:311}
Let $A$ be a DG ring. The action of $A^0$ on $\cat{C}(A)$ 
makes $\cat{D}(A)$ into an $\bar{A}$-linear category.
\end{prop}

\begin{proof}
Let $\phi : M \to N$ be a morphism in  $\cat{C}(A)$; namely 
$\phi$ is a degree $0$ cocycle in the DG abelian group 
$\opn{Hom}_A(M, N)$. For any $a \in A^{-1}$, 
the homomorphism $\d(a) \cd \phi = \d(a \cd \phi)$ 
is a degree $0$ coboundary in $\opn{Hom}_A(M, N)$, and so it
vanishes in the homotopy category $\cat{K}(A)$. Therefore $\cat{K}(A)$ is 
an $\bar{A}$-linear category, and hence so is its localization 
$\cat{D}(A)$.
\end{proof}

\begin{dfn} \label{dfn:40}
Let $A$ be a DG ring, with canonical homomorphism
$\pi : A \to \bar{A} = \opn{H}^0(A)$. Given a multiplicatively closed 
subset $S$ of $\bar{A}$, the set
$\til{S} := \pi^{-1}(S) \cap A^0$ is a 
multiplicatively closed subset of $A^0$. Define the ring 
$A^0_S :=  \til{S}^{-1} \cd A^0$ 
(this is the usual localization), and the DG ring 
$A_S := A^0_S \ot_{A^0} A$.
There is a canonical DG ring homomorphism 
$\la_S : A \to A_S$.

If $S = \{ s^i \}_{i \in \N}$ for some element $s \in \bar{A}$, 
then we also use the notation $A_s := A_S$.
\end{dfn}

There is the usual localization $\bar{A}_S = S^{-1} \cd \bar{A}$ of the 
ring $\bar{A}$ w.r.t.\ $S$. We get a graded ring 
$\opn{H}(A)_S := \bar{A}_S \ot_{\bar{A}} \opn{H}(A)$. 
There are graded ring homomorphisms 
$\opn{H}(A) \to \opn{H}(A)_S$ and 
$\opn{H}(\la_S) :\opn{H}(A) \to \opn{H}(A_S)$.

\begin{prop} \label{prop:300}
Let $A$ be a DG ring and $S \subseteq \bar{A}$ a multiplicatively closed 
subset. 
\begin{enumerate}
\item There is a unique isomorphism of graded $\opn{H}(A)$-rings 
$\opn{H}(A_S) \cong \opn{H}(A)_S$.

\item For any DG $A$-module $M$ there is a unique isomorphism of graded 
$\opn{H}(A_S)$-modules 
\[ \opn{H}(A_S \ot_A M) \cong \opn{H}(A)_S \ot_{\opn{H}(A)} \opn{H}(M)  \]
that is compatible with the homomorphisms from $\opn{H}(M)$.

\item If $A$ is cohomologically pseudo-noetherian, then so is $A_S$.
\end{enumerate}
\end{prop}

\begin{proof}
Items (1-2) are true because the ring homomorphism $\la_S : A^0 \to A^0_S$ is 
flat. Item (3) is an immediate consequence of (1-2). 
\end{proof}

\begin{dfn}  \label{dfn:70}
Let $A$ be a ring, and let $\bsym{a} = (a_1, \ldots, a_n)$ be a 
sequence of elements of $A$. 
We call $\bsym{a}$ a {\em covering sequence} of $A$ if
$\sum_{i = 1}^n A \cd a_i = A$. 
\end{dfn}
 
Consider the spectrum $\opn{Spec} A$ of the ring $A$. For an element $a \in A$ 
we identify the principal open set \
$\{ \p \in \opn{Spec} A \mid a \notin \p \}$
with the scheme $\opn{Spec} A_a$, where $A_a$ is the localization of $A$ 
w.r.t.\ $a$. Clearly a sequence 
$\bsym{a} = (a_1, \ldots, a_n)$ in $A$ is a covering sequence iff
$\opn{Spec} A = \bigcup_{i = 1}^n \, \opn{Spec} A_{a_i}$.

Let $A$ be a DG ring, and let $\bsym{a} = (a_1, \ldots, a_n)$ be a 
covering sequence of $\bar{A}$.
For any  strictly increasing sequence
$\bsym{i} = (i_0, \ldots, i_p)$ of length $p$ in the integer interval $[0, n]$, 
i.e.\  $1 \leq i_0 < \cdots < i_p \leq n$, we define the ring 
\begin{equation} \label{eqn:341}
\opn{C}(A^0; \bsym{a})(\bsym{i}) := 
A^0_{a_{i_0}} \ot_{A^0} \cdots \ot_{A^0} A^0_{a_{i_p}} , 
\end{equation}
where $A^0_{a_{0}}, \ldots, A^0_{a_{p}}$ are the localizations from Definition 
\ref{dfn:40}. Next, for any $p \in [0, n - 1]$ we let 
\begin{equation} \label{eqn:342}
\opn{C}^p(A^0; \bsym{a}) := \bigoplus_{\bsym{i}} \, 
\opn{C}(A^0; \bsym{a})(\bsym{i}) \ , 
\end{equation}
where the sum is on all strictly increasing sequences $\bsym{i}$ of length $p$.
Finally we define the DG $A^0$-module 
\begin{equation} \label{eqn:340}
\opn{C}(A^0; \bsym{a}) := 
\bigoplus_{p = 0}^{n - 1} \, \opn{C}^p(A^0; \bsym{a}) .
\end{equation}
The differential 
$\opn{C}^p(A^0; \bsym{a}) \to \opn{C}^{p+1}(A^0; \bsym{a})$
is $\sum_{\bsym{i}, k} (-1)^k \cd \la_{\bsym{i}, k}$,
where $\bsym{i}$ runs over the strictly increasing sequences of length $p + 1$,
$k \in [0, p + 1]$, 
$\pa_k(\bsym{i})$ is the sequence obtained from $\bsym{i}$ by omitting 
$i_k$, and 
$\la_{\bsym{i}, k} : \opn{C}(A^0; \bsym{a})(\pa_k(\bsym{i})) \to 
\opn{C}(A^0; \bsym{a})(\bsym{i})$
is the canonical ring homomorphism.

\begin{dfn}  \label{dfn:72}
Let $A$ be a DG ring, and let  $\bsym{a} = (a_1, \ldots, a_n)$ be a 
covering sequence of $\bar{A}$.
For a DG $A$-module $M$, the {\em \v{C}ech DG module} of $M$ is the DG 
$A$-module
\[ \opn{C}(M; \bsym{a}) := 
\opn{C}(A^0; \bsym{a}) \ot_{A^0} M . \]
\end{dfn}

There is a canonical DG module homomorphism 
$\opn{c}_M : M \to \opn{C}(M; \bsym{a})$, 
sending $m \in M$ to $\sum_i 1_i \ot m \in \opn{C}(M; \bsym{a})$,
where $1_i$ is the element 
$1 \in A^0_{a_{i}} \subseteq \opn{C}^0(A^0; \bsym{a})$.

\begin{prop} \label{prop:70}
Let $\bsym{a} = (a_1, \ldots, a_n)$ be a covering sequence of $\bar{A}$, and 
let $M$ be a DG $A$-module. Then the homomorphism 
$\opn{c}_M : M \to \opn{C}(M; \bsym{a})$ is a quasi-isomorphism. 
\end{prop}

\begin{proof}
Since $\opn{C}(A; \bsym{a})$ is a K-flat DG $A$-module, and 
$\opn{C}(M; \bsym{a}) \cong \opn{C}(A; \bsym{a}) \ot_A M$, we see that 
$\opn{C}(-; \bsym{a})$ is a triangulated functor from $\cat{D}(A)$ to 
itself. 
The homomorphism $\opn{c}_M$ is a quasi-isomorphism iff it is an isomorphism 
in $\cat{D}(A)$.

The cohomological dimension of the functor $\opn{C}(-; \bsym{a})$ is finite: 
it is at most $n-1$. 
According to Theorem \ref{thm:70}(3) it suffices to check that $\opn{c}_M$
is a quasi-isomorphism for 
$M \in \cat{Mod} \bar{A}$. But in this case 
$\opn{C}(M; \bsym{a}) \cong \opn{C}(\bar{A}; \bsym{a}) \ot_{\bar{A}} M$,
so $\opn{C}(M; \bsym{a})$ is the usual \v{C}ech complex for the covering of
$\opn{Spec} \bar{A}$ determined by the sequence $\bsym{a}$. 
In geometric language (cf.\ \cite[Section III.4]{Ha}), writing 
$X := \opn{Spec} \bar{A}$ and $U_i := \opn{Spec} \bar{A}_{a_i}$,
and letting $\mcal{M}$ denote the quasi-coherent $\OO_X$-module corresponding 
to $M$, we have $M \cong \Ga(X, \MM)$ and
$\opn{C}(M; \bsym{a}) \cong \opn{C}(\{ U_i \}, \MM)$. 
By 
\cite[\href{http://stacks.math.columbia.edu/tag/01X9}{Lemma 01X9}]{SP},
the homomorphism 
$\opn{c}_M : M \to \opn{C}(M; \bsym{a})$ 
is a quasi-isomorphism. 
\end{proof}

\begin{rem}
Actually the DG $A$-module $\opn{C}(A; \bsym{a})$
has more structure. There is a cosimplicial commutative ring 
$\opn{C}_{\mrm{cos}}(A^0; \bsym{a})$, 
whose degree $p$ piece is 
\[ \opn{C}_{\mrm{cos}}^p(A^0; \bsym{a}) := 
\prod_{\bsym{i}} \ \opn{C}(A^0; \bsym{a})(\bsym{i}) , \]
where $\bsym{i} = (i_0, \ldots, i_p)$ are weakly increasing
sequences in $[1, n]$. 
The \v{C}ech DG module $\opn{C}(A^0; \bsym{a})$ is the standard 
normalization 
of $\opn{C}_{\mrm{cos}}(A^0; \bsym{s})$, and as such it has a structure 
of noncommutative central DG $A^0$-ring (which is concentrated in non-negative 
degrees). Hence $\opn{C}(A; \bsym{a})$ is a noncommutative DG ring,
and $\opn{c}_A : A \to \opn{C}(A; \bsym{a})$ 
is a DG ring quasi-isomorphism. 
See \cite[Section 8]{PSY}.
\end{rem}

\begin{dfn}  \label{dfn:90}
Let $A$ be a ring, and let $\bsym{e} = (e_1, \ldots, e_n)$ be a 
sequence of elements of $A$. We call $\bsym{e}$ an {\em idempotent covering 
sequence} if each $e_i$ is an idempotent element of $A$, $e_i \cd e_j = 0$ 
for $i \neq j$, and $1 = \sum_{i = 1}^n e_i$. 
\end{dfn}

Suppose $\bsym{e} = (e_1, \ldots, e_n)$ is an idempotent covering sequence of 
the ring $A$. Of course $\bsym{e}$ is a covering sequence in the sense of 
Definition \ref{dfn:70}. 
For any $i$ there is a unique $A$-ring isomorphism
$A_{e_i} \cong A / (1 - e_i) \cd A$; 
namely the localization of $A$ with respect to the element $e_i$ is also 
the quotient ring modulo the ideal generated by the complementary idempotent 
$1 - e_i$. There is a ring isomorphism 
\begin{equation} \label{eqn:585}
A \iso \prod_{i = 1}^n \ A_{e_i} \,  .
\end{equation}
The scheme $\opn{Spec} A_{e_i}$ is an open-closed subscheme of $\opn{Spec} A$, 
and 
\begin{equation} \label{eqn:551}
\opn{Spec} A = \coprod_{i = 1}^n \ \opn{Spec} A_{e_i} \, . 
\end{equation}

\begin{dfn} \label{dfn:585}
Let $\bsym{e} = (e_1, \ldots, e_n)$ be an idempotent covering sequence of 
the ring $A$. The {\em $\bsym{e}$-induced decomposition} of $A$ is 
the ring isomorphism (\ref{eqn:585}). 
\end{dfn}

\begin{dfn} \label{dfn:560}
Let $A$ be a ring. The set of locally constant functions 
$f : \opn{Spec} A \to \Z$ (for the Zariski topology on $\opn{Spec} A$) shall be 
denoted by $\opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$. 
It is an abelian group by pointwise addition.  
\end{dfn}

\begin{prop} \label{prop:550}
Let $A$ be a ring. There is a bijection between the set 
$\opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$,
and the set of pairs $(\bsym{e}, \bsym{k})$, consisting of 
an idempotent covering sequence $\bsym{e} = (e_1, \ldots, e_n)$
of $A$, and a nondecreasing sequence of integers 
$\bsym{k} = (k_1, \ldots, k_n)$. 
This bijection sends a function $f \in \opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$
to the pair $(\bsym{e}, \bsym{k})$ that satisfies
$f^{-1}(k_i)  = \opn{Spec} A_{e_i}$.
\end{prop}

\begin{proof}
Consider a locally constant function $f : \opn{Spec} A \to \Z$.
Then $f$ is continuous for the discrete topology on $\Z$. 
Since the topological space $\opn{Spec} A$ is quasi-compact, the image of $f$ 
must be finite. This gives rise to a finite decomposition of 
$\opn{Spec} A$ into open-closed subsets, which must be of the form 
(\ref{eqn:551}) for some idempotent covering sequence $\bsym{e}$. 
After suitable renumbering we get the pair  $(\bsym{e}, \bsym{k})$.

The converse is clear. 
\end{proof}

\begin{exa} \label{exa:550}
Often $\opn{Spec} A$ of the ring $A$ has finitely many connected 
components; say $n$ of them. Prototypes are: 
\begin{enumerate}
\item $A$ is a noetherian ring.
\item $A$ is a semilocal ring. 
\item $A$ is the ring of continuous (resp.\ differentiable) 
functions $X \to \R$, where $X$ is a connected topological space (resp.\ a 
connected differentiable manifold). Here $n = 1$. 
\end{enumerate}

An ordering of the connected components of $\opn{Spec} A$
gives rise to an idempotent covering sequence $\bsym{e} = (e_1, \ldots, e_n)$.
The sequence of delta functions $(\de_1, \ldots, \de_n)$
is a basis of the group $\opn{F}_{\mrm{lc}}(\opn{Spec} A, \Z)$, 
which is thus isomorphic to $\Z^n$.
\end{exa}

\begin{dfn}  \label{dfn:551}
Let $A$ be a ring, and assume that $\opn{Spec} A$ has finitely many 
connected components. A {\em connected component idempotent covering sequence}
of $A$ is an idempotent covering sequence
$\bsym{e} = (e_1, \ldots, e_n)$, such that each $\opn{Spec} A_{e_i}$
is nonempty and connected. 
\end{dfn}

Clearly a connected component idempotent covering sequence of $A$ is unique up 
to permutation. 

\begin{prop} \label{prop:20}
Let $A$ be a DG ring, and let 
$\bsym{e} = (e_1, \ldots, e_n)$ be an idempotent covering sequence of 
$\bar{A} = \opn{H}^0(A)$. For any $i$ we have the localized DG ring 
$A_i := A_{e_i}$ from Definition \tup{\ref{dfn:40}}, and the DG ring 
homomorphism $\la_i : A \to A_i$. Then the DG ring homomorphism
\[ (\la_1,  \ldots , \la_n) : A \to A_1 \times \cdots \times A_n \]
is a quasi-isomorphism. 
\end{prop}

\begin{proof}
Let's write $\bar{A}_i := \bar{A}_{e_i} = \opn{H}^0(A)_{e_i}$, so 
$\bar{A} = \prod_{i = 1}^n \, \bar{A}_i$. 
Using Proposition \ref{prop:300}(1) we obtain canonical graded ring isomorphisms
\[ \opn{H}(A) \cong 
\prod\nolimits_{i = 1}^n \, \bigl( \bar{A}_i \ot_{\bar{A}} \opn{H}(A) \bigr) 
\cong \prod\nolimits_{i = 1}^n \, \opn{H}(A_i) \cong 
\opn{H}\bigl( \prod\nolimits_{i = 1}^n \, A_i \bigr) . \] 
The composition of these isomorphisms is exactly 
$\opn{H}(\la_1,  \ldots , \la_n)$. 
\end{proof}

\begin{cor} \label{cor:22}
With $A_1, \ldots, A_n$ as in Proposition \tup{\ref{prop:20}}, the 
restriction functors 
$\opn{rest}_{\la_i} : \cat{D}(A_{i}) \to \cat{D}(A)$
induce an equivalence of triangulated categories
$\bigoplus_{i = 1}^n \,  \cat{D}(A_{i}) \to \cat{D}(A)$.
\end{cor}

\begin{proof}
This is standard. Cf.\ \cite[Proposition 1.4]{YZ1}. 
\end{proof}

\begin{dfn} \label{dfn:102}
Let $A$ be a DG ring, and let $e \in \bar{A} = \opn{H}^0(A)$
be an idempotent element. Consider the localized DG ring 
$A_{e}$ corresponding to $e$, as in Definition \ref{dfn:40}. 
The triangulated functor
\[ E : \cat{D}(A) \to \cat{D}(A) \ , \  
E(M) := A_{e} \ot_A M, \]
is called the {\em idempotent functor} corresponding to $e$.
\end{dfn}

\begin{dfn}  \label{dfn:343}
Let $A$ be a DG ring, and let 
$\bsym{e} = (e_1, \ldots, e_n)$
be an idempotent covering sequence of $\opn{Spec} \bar{A}$. 
\begin{enumerate}
\item The corresponding DG ring quasi-isomorphism 
\[ (\la_1,  \ldots , \la_n) : A \to A_1 \times \cdots \times A_n \, , \]
from Proposition \ref{prop:20} 
is called the {\em $\bsym{e}$-induced decomposition} of $A$. 

\item The corresponding functors  $E_1, \ldots, E_n$ from Definition 
\ref{dfn:102} are called the 
{\em $\bsym{e}$-induced idempotent functors} of $A$. 

\item In case $\opn{Spec} \bar{A}$ has finitely many connected components, and 
$\bsym{e}$ is one of its connected component idempotent covering sequence, then 
 the expression ``$\bsym{e}$-induced'' above is sometimes replaced by 
``connected component''. 
\end{enumerate}
\end{dfn}

\begin{prop} \label{prop:90}
Suppose $\bsym{e} = (e_1, \ldots, e_n)$ is an idempotent covering sequence of 
$\bar{A}$. Let \lb $E_1, \ldots, E_n$ be the $\bsym{e}$-induced
idempotent functors. 
\begin{enumerate}
\item We have $E_i \circ E_i \cong E_i$, $E_i \circ E_j = 0$ for $i \neq j$, 
and $\sum_{i = 1}^n E_i \cong \opn{id}_{\cat{D}(A)}$.

\item Under the equivalence of categories in Corollary \tup{\ref{cor:22}},
$\cat{D}(A_{i})$ is  the essential image of $E_i$.
\end{enumerate}
\end{prop}

\begin{proof}
This is similar to the proof of Proposition \ref{prop:20}, and is left to the 
reader.
\end{proof}

\begin{prop} \label{prop:21}
Let $f : A \to B$ be a DG ring homomorphism, and let 
$M, N \in \cat{D}(B)$.
We write $\bar{f} := \opn{H}^0(f)$ and 
$F := \opn{rest}_f : \cat{D}(B) \to \cat{D}(A)$. 
Assume that the ring homomorphism 
$\bar{f} : \bar{A} \to \bar{B}$ is surjective.
Let $\bsym{e} = (e_1, \ldots, e_n)$ be an idempotent covering sequence of 
$\bar{B}$,  let $E_1, \ldots, E_n$ be the $\bsym{e}$-induced idempotent
functors of $B$, and write $M_i := E_i(M)$ and $N_i := E_i(N)$. 
Then for any  $i \neq j$ we have
\[ \opn{Hom}_{\cat{D}(A)} \bigl( F(M_i), F(N_j) \bigl) = 0 . \]
Therefore we get a canonical isomorphism of $\bar{A}$-modules 
\[ \opn{Hom}_{\cat{D}(A)} \bigl( F(M), F(N) \bigl) \cong 
\bigoplus_{i = 1}^n \,
\opn{Hom}_{\cat{D}(A)} \bigl( F(M_i), F(N_i) \bigl) . \]
\end{prop}

\begin{proof}
For any $i$ choose some element $a_i \in \bar{A}$ such that 
$\bar{f}(a_i) = e_i$.
Consider the noncommutative rings $\opn{End}_{\cat{D}(B)}(M_i)$ and 
$\opn{End}_{\cat{D}(A)}(F(M_i))$. 
There is a commutative diagram (of noncommutative rings) 
\[  \UseTips \xymatrix @C=5ex @R=5ex {
\bar{A}
\ar[r]
\ar[d]_{ \bar{f} }
&
\opn{End}_{\cat{D}(A)}  ( F(M_i) )
\\
\bar{B}
\ar[r]
&
\opn{End}_{\cat{D}(B)} ( M_i )
\ar[u]_{F} \ . 
} \]
Cf.\ Proposition \ref{prop:311}.

Take two distinct indices $i, j$.
We know that $e_i \cd \opn{id}_{M_i} = \opn{id}_{M_i}$
in $\opn{End}_{\cat{D}(B)}(M_i)$,
and $e_i \cd \opn{id}_{M_j} = 0$ in $\opn{End}_{\cat{D}(B)}(M_j)$.
Therefore
$a_i \cd \opn{id}_{F(M_i)} = \opn{id}_{F(M_i)}$
in $\opn{End}_{\cat{D}(A)}(F(M_i))$,
and $a_i \cd \opn{id}_{F(M_j)} = 0$ in $\opn{End}_{\cat{D}(A)}(F(M_j))$.

Consider any morphism $\phi : F(M_i) \to F(N_j)$ in $\cat{D}(A)$.
Then 
\[ \begin{aligned}
& \phi =  \opn{id}_{F(M_j)} \circ \, \phi \circ \opn{id}_{F(M_i)}  = 
\opn{id}_{F(M_j)} \circ \, \phi \circ (a_i \cd \opn{id}_{F(M_i)}) \\
& \qquad = (a_i \cd \opn{id}_{F(M_j)}) \circ \phi \circ \opn{id}_{F(M_i)}  = 0 .
\end{aligned} \]
\end{proof}
