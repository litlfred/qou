---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS"
section_id: sec-002-2-resolutions-of-dg-modules
section_title: "Resolutions of DG Modules"
section_number: 2
pages: 12-16
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.93
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS — Let A →B be a homomorphism of commutative rings."
---
\label{sec:resolutions-modules}

Let $A$ be a DG ring. 
We already mentioned that $\cat{M}(A) = \cat{DGMod} A$ is a DG category, 
equipped with a translation automorphism $\opn{T}$. The homotopy category of 
$\cat{DGMod} A$ is 
$\til{\cat{K}}(\cat{DGMod} A)$, where by definition 
\begin{equation} \label{eqn:1016}
\opn{Hom}_{\til{\cat{K}}(\cat{DGMod} A)}(M, N) := 
\mrm{H}^0 \bigl( \opn{Hom}_A(M, N) \bigr) .
\end{equation}
This is a triangulated category. 
The derived category $\til{\cat{D}}(\cat{DGMod} A)$ is  gotten
from $\til{\cat{K}}(\cat{DGMod} A)$ by inverting the 
quasi-isomorphisms. The localization functor (identity on objects) is
\begin{equation} \label{eqn:450}
\opn{Q} : \cat{DGMod} A \to \til{\cat{D}}(\cat{DGMod} A) . 
\end{equation}
If $A$ is a ring, i.e.\ $A = A^0$, with module category $\cat{Mod} A$, 
then $\cat{DGMod} A = \cat{C}(\cat{Mod} A)$,
$\til{\cat{K}}(\cat{DGMod} A) = \cat{K}(\cat{Mod} A)$
and $\til{\cat{D}}(\cat{DGMod} A) = \cat{D}(\cat{Mod} A)$.
Here are some references for the derived category of DG modules: 
\cite[Section 10]{BL}, 
\cite[Section 2]{Ke1}, and 
\cite[\href{http://stacks.math.columbia.edu/tag/09KV}{Section 09KV}]{SP}.
Another reference is our course 
notes \cite{Ye4}, but there (in Sections 4 and 9) the DG category 
$\cat{C}(\cat{M})$, associated to an abelian category $\cat{M}$, should be 
replaced by the DG category $\cat{DGMod} A$. 

\begin{dfn}   \label{dfn:875}   
We shall use the following abbreviations for the triangulated categories 
related 
to a DG ring $A$: 
$\cat{K}(A) := \til{\cat{K}}(\cat{DGMod} A)$ and 
$\cat{D}(A) := \til{\cat{D}}(\cat{DGMod} A)$. 
\end{dfn}

Let us recall a few facts about resolutions of DG $A$-modules. 
A DG module $N$ is called acyclic if $\opn{H}(N) = 0$. A DG $A$-module 
$P$ (resp.\ $I$) is called {\em K-projective} (resp.\ {\em K-injective})
if for any acyclic DG $A$-module $N$, the DG $\Z$-module 
$\opn{Hom}_{A}(P, N)$ (resp.\ $\opn{Hom}_{A}(N, I)$) is also acyclic. 
The DG module $P$ is called {\em K-flat} if for every acyclic 
DG $A^{\mrm{op}}$-module $N$, the $\Z$-module  $N \ot_A P$ is acyclic. 
As in the ``classical'' situation, K-projective implies K-flat. 
These definitions were introduced in \cite{Sp}. 
In \cite[Section 3]{Ke1} it is shown that ``K-projective'' is the same as 
``having property (P)'', and ``K-injective'' is the same as ``having property 
(I)''. Every $M \in \cat{M}(A)$ admits K-projective resolutions $P \to M$ and 
K-injective resolutions $M \to I$. 
See also \cite{BL}, \cite{BN}, \cite{AFH} and
\cite[\href{http://stacks.math.columbia.edu/tag/09JD}{Chapter 09JD}]{SP}.
(Semi-free DG modules will be discussed in Section \ref{sec:resolutions-rings}.)

Recall that a diagram  
\[ \UseTips \xymatrix @C=12ex @R=6ex {
M
\ar @/^1.5em/ [r]^{ \phi_0 }
\ar @/_1.5em/ [r]_{ \phi_1 }
&
N
} \]
in $\cat{M}(A)$ is called {\em commutative up to homotopy} if the homomorphisms 
$\phi_0$ and $\phi_1$ are homotopic. Or in other words, if the corresponding 
diagram in  $\cat{K}(A)$ is commutative. 

The next proposition is essentially a standard fact. We state it here because 
it will play a key role, especially in Section \ref{sec:pairs-DG-modules}.  

\begin{prop} \label{prop:460} 
Let $P, I \in \cat{M}(A)$. Assume either $P$ is K-projective or $I$ is 
K-injective. 
\begin{enumerate}
\item The additive homomorphism 
\[ \opn{Q} : \opn{Hom}_{\cat{M}(A)}(P, I) \to 
\opn{Hom}_{\cat{D}(A)}(P, I) \]
is surjective, and its kernel is the group 
$\opn{B}^0(\opn{Hom}_A(P, I))$ of null-homotopic homomorphisms.

\item Let $\psi : P \to I$ be a morphism in $\cat{D}(A)$. There exists a 
homomorphism $\phi : P \to I$ in $\cat{M}(A)$, unique up to homotopy, such that 
$\opn{Q}(\phi) = \psi$. 

\item Let $\phi_0, \phi_1 : P \to I$ be homomorphisms in $\cat{M}(A)$. The 
homomorphisms $\phi_0$ and $\phi_1$ are homotopic iff 
$\opn{Q}(\phi_0) = \opn{Q}(\phi_1)$ in $\cat{D}(A)$. 
\end{enumerate}
\end{prop}

In other words, item (2) says that given a morphism $\psi$ in $\cat{D}(A)$, 
as in the first diagram below, there exists a homomorphism $\phi$ in 
$\cat{M}(A)$ making that diagram commutative; and such $\phi$ is unique up to 
homotopy. Item (3) says that the second diagram below, in $\cat{M}(A)$, is 
commutative up to homotopy, iff the third diagram below, in $\cat{D}(A)$, is 
commutative. 
\[ \UseTips \xymatrix @C=12ex @R=6ex {
P
\ar @/^1.5em/ [r]^{ \psi }
\ar@{-->} @/_1.5em/ [r]_{ \opn{Q}(\phi) }
&
I
}
\qquad \qquad 
\UseTips \xymatrix @C=10ex @R=6ex {
P
\ar @/^1.5em/ [r]^{ \phi_0 }
\ar @/_1.5em/ [r]_{ \phi_1 }
&
I
}
\qquad 
\UseTips \xymatrix @C=10ex @R=6ex {
P
\ar @/^1.5em/ [r]^{ \opn{Q}(\phi_0) }
\ar @/_1.5em/ [r]_{ \opn{Q}(\phi_1) }
&
I
} \]

\begin{proof}
(1) According to \cite[Propositions 1.4 and 1.5]{Sp}, the additive homomorphism 
\[ \opn{Hom}_{\cat{K}(A)}(P, I) = \opn{H}^0(\opn{Hom}_A(P, I)) \to 
\opn{Hom}_{\cat{D}(A)}(P, I) \]
is bijective. Note that in \cite{Sp} $A$ is a ring; but the definitions and 
proofs pass without change to the case of a DG ring.

\medskip \noindent 
(2, 3) These are immediate from (1). 
\end{proof}

A DG ring homomorphism $u : A \to B$ induces the forgetful (or restriction of 
scalars) functor 
$\opn{For}_{u} : \cat{M}(B) \to \cat{M}(A)$, 
which is exact, and hence gives rise to a triangulated functor
$\opn{For}_{u} : \cat{D} (B) \to \cat{D} (A)$. 
We usually do not mention the functor $\opn{For}_{u}$ explicitly, unless it is 
important for the discussion at hand. 

If $u : A \to B$ is a quasi-isomorphism then 
$\opn{For}_{u} : \cat{D} (B) \to \cat{D} (A)$ is an equivalence, with 
quasi-inverse  $M \mapsto B \ot^{\mrm{L}}_A M$.
For any $M_0 \in \cat{D}(A^{\mrm{op}})$ and $M_1, M_2 \in \cat{D} (A)$
there are bi-functorial isomorphisms 
$M_0 \ot^{\mrm{L}}_A M_1 \cong M_0 \ot^{\mrm{L}}_B M_1$ and 
$\opn{RHom}_A(M_1, M_2) \cong \opn{RHom}_B(M_1, M_2)$
in $\cat{D}(\Z)$; cf.\ \cite[Proposition 1.4]{YZ2}.

Here is a result that will be used a lot in our paper. The restriction 
functors are suppressed in it. The easy proof is left to the reader. 

\begin{prop} \label{prop:461} 
Let $A_0 \xar{u_1} A_1 \xar{u_2} A_2$ and 
$B_0 \xar{v_1} B_1 \xar{v_2} B_2$ 
be homomorphisms in $\cat{DGR}$.
For $k = 0, 1, 2$ let $M_k \in \cat{M}(B_k \ot_{\Z} A_k)$ and
$N_k \in \cat{M}(B_k)$; and for $k = 1, 2$ let 
$\ze_k : M_{k - 1} \to M_k$ and $\th_k : N_k \to N_{k - 1}$ 
be homomorphisms in $\cat{M}(B_{k - 1} \ot_{\Z} A_{k - 1})$ and 
$\cat{M}(B_{k - 1})$ respectively.
\begin{enumerate}
\item The abelian group $\opn{Hom}_{B_0}(M_0, N_0)$ is a DG 
$A_0^{\mrm{op}}$-module,  with action 
\[ (\phi \cd a)(m) :=  \phi(a \cd m) \]
for $\phi \in \opn{Hom}_{B_0}(M_0, N_0)$, $a \in A_0$  
and $m \in M_0$.

\item The function 
\[ \opn{Hom}_{v_1}(\ze_1, \th_1) : \opn{Hom}_{B_1}(M_1, N_1) \to
\opn{Hom}_{B_0}(M_0, N_0) , \]
with formula 
\[ \opn{Hom}_{v_1}(\ze_1, \th_1)(\phi) := \th_1 \circ \phi \circ \ze_1 \]
for $\phi \in \opn{Hom}_{B_1}(M_1, N_1)$,
is a homomorphism in $\cat{M}(A_0^{\mrm{op}})$.

\item There is equality 
\[ \opn{Hom}_{v_1}(\ze_1, \th_1) \circ \opn{Hom}_{v_2}(\ze_2, \th_2) =
\opn{Hom}_{v_2 \circ v_1}(\ze_2 \circ \ze_1, \th_1 \circ \th_2) . \]

\item Say 
$\ze'_1 : M_{0} \to M_1$ and $\th'_1 : N_1 \to N_{0}$ are also homomorphisms in 
\lb $\cat{M}(B_0 \ot_{\Z} A_0)$ and $\cat{M}(B_{0})$ respectively, and there 
are homotopies 
$\ze_1 \twoto \ze'_1$ and $\th_1 \twoto \th'_1$ in
$\cat{M}(B_0 \ot_{\Z} A_0)$ and $\cat{M}(B_{0})$ respectively.
Then there is a homotopy 
\[ \opn{Hom}_{v_1}(\ze_1, \th_1) \twoto \opn{Hom}_{v_1}(\ze'_1, \th'_1) \]
in $\cat{M}(A_0^{\mrm{op}})$.
\end{enumerate}
\end{prop}

Item (2) of the proposition is illustrated here:

\[ \UseTips \xymatrix @C=10ex @R=6ex {
M_0
\ar[r]^{\ze_1}
\ar[d]_{\opn{Hom}_{v_1}(\ze_1, \th_1)(\phi)}
&
M_1
\ar[d]^{\phi}
\\
N_0
&
N_1
\ar[l]_{\th_1}
} \]

\begin{prop} \label{prop:462}
Let $v : A' \to A$ be a quasi-isomorphism between DG rings.
Let $Q, I \in \cat{M}(A)$, $P \in \cat{M}(A^{\mrm{op}})$, 
$Q', I' \in \cat{M}(A')$ and $P' \in \cat{M}(A'^{\, \mrm{op}})$.
Let $\phi : P' \to P$ be a quasi-isomorphism in  
$\cat{M}(A'^{\, \mrm{op}})$, and let 
$\psi : Q' \to Q$ and $\chi : I \to I'$ be quasi-isomorphisms in  $\cat{M}(A')$.
\begin{enumerate}
\item If \tup{((}$P$ is K-flat over $A^{\mrm{op}}$ or $Q$ is K-flat over 
$A$\tup{)} and
\tup{(}$P'$ is K-flat over $A'^{\mrm{\, op}}$ or $Q'$ is K-flat over 
$A'$\tup{))} then 
\[ \phi \ot_v \psi : P' \ot_{A'} Q' \to P \ot_A Q \] 
is a quasi-isomorphism.

\item If \tup{((}$Q$ is K-projective or $I$ is K-injective over $A$\tup{)} 
and
\tup{(}$Q'$ is K-projective or $I'$ is K-injective over $A'$\tup{))} then
\[ \opn{Hom}_v(\psi, \chi) : \opn{Hom}_A(Q, I) \to \opn{Hom}_{A'}(Q', I') \]
is a quasi-isomorphism.
\end{enumerate}
\end{prop}

\begin{proof}
This is implicit in the proof of \cite[Proposition 1.4]{YZ2}. Here is a 
detailed proof. 

\medskip \noindent 
(1) By the symmetry of the situation we can assume that either $P'$ and $P$ 
are K-flat (over the respective DG rings), or that $Q'$ and $P$ are
K-flat. We begin by reducing the second case to the first case. Choose a K-flat 
resolution $\mu : \til{P}' \to P'$. Then 
$\til{P}' \ot_{A'} Q' \to P' \ot_{A'} Q'$ is a quasi-isomorphism, and it 
suffices to prove that 
\[ (\phi \circ \mu) \ot_v \psi : \til{P}' \ot_{A'} Q' \to P \ot_A Q \]
is a quasi-isomorphism, which is the first case.

Now we assume that  $P'$ and $P$ are K-flat. Consider the homomorphism 
$\phi \cd \opn{id}_A : P' \ot_{A'} A \to P$, 
$(\phi \cd \opn{id}_A)(p' \ot a)  := \phi(p') \cd a$. 
We claim this is a quasi-isomorphism. To see why, let us look at the first 
commutative diagram below. The homomorphism $\opn{id}_{P'} \ot v$ is a 
quasi-isomorphism since $v$ is a quasi-isomorphism and $P'$ is K-flat; 
the homomorphism $\opn{id}_{P'} \cd \opn{id}_{A'}$ is an isomorphism; and 
$\phi$ is a quasi-isomorphism; therefore $\phi \cd \opn{id}_A$ 
is a quasi-isomorphism.
\[ \UseTips \xymatrix @C=10ex @R=6ex {
P' \ot_{A'} A' 
\ar[r]^(0.6){ \opn{id}_{P'} \cd \opn{id}_{A'} }
\ar[d]_{ \opn{id}_{P'} \ot v }
&
P'
\ar[d]^{\phi}
\\
P' \ot_{A'} A
\ar[r]^(0.6){\phi \cd \opn{id}_{A}  }
&
P 
} 
\qquad 
\UseTips \xymatrix @C=8ex @R=6ex {
P' \ot_{A'} Q'
\ar[r]^{ \phi \ot_v \psi }
\ar[d]_{ \opn{id}_{P'} \ot \psi }
&
P \ot_A Q 
\\
P' \ot_{A'} Q
\ar[r]^(0.45){ \lambda }
&
P' \ot_{A'} A \ot_A Q 
\ar[u]_{ (\phi \cd \opn{id}_{A}) \ot \opn{id}_{Q} }
} \]

Next look at the second commutative diagram above.
The homomorphism  $\lambda$, defined by
$\lambda(p' \ot q) := p' \ot 1 \ot q$, is an isomorphism.
The homomorphism $\opn{id}_{P'} \ot \psi$ is a quasi-isomorphism because 
$\psi$ is a  quasi-isomorphism and $P'$ is K-flat; 
and $(\phi \cd \opn{id}_{A}) \ot \opn{id}_{Q}$ is a quasi-isomorphism because 
$\phi \cd \opn{id}_{A}$ a quasi-isomorphism between K-flat DG 
$A^{\mrm{op}}$-modules. Therefore $\phi \ot_v \psi$ is a quasi-isomorphism.

\medskip \noindent 
(2) Choose K-projective resolutions 
$\al: \til{Q} \to Q$ and $\al' : \til{Q}' \to Q'$,
and K-injective resolutions 
$\be : I \to \til{I}$ and $\be' : I' \to \til{I}'$,
in $\cat{M}(A)$ and $\cat{M}(A')$ respectively. 
By Proposition \ref{prop:460}, we can lift $\psi$ and $\chi$ 
to quasi-isomorphisms $\til{\psi}$ and $\til{\chi}$, such that the diagrams 
\[ \UseTips \xymatrix @C=6ex @R=6ex {
\til{Q}'
\ar[d]_{\al'}
\ar[r]^{\til{\psi}}
&
\til{Q}
\ar[d]^{\al}
\\
Q'
\ar[r]^{\psi}
&
Q
} 
\qquad \qquad 
\UseTips \xymatrix @C=8ex @R=6ex {
\til{I}
\ar[r]^{\til{\chi}}
&
\til{I}'
\\
I
\ar[u]^{\be}
\ar[r]^{\chi}
&
I'
\ar[u]_{\be'}
} \]
in $\cat{M}(A')$ are commutative up to homotopy. We get a diagram 
\begin{equation} \label{eqn:970}
\UseTips \xymatrix @C=14ex @R=6ex {
\opn{Hom}_A(Q, I)
\ar[r]^{\opn{Hom}_v(\psi, \chi)}
\ar[d]_{ \opn{Hom}_{\mrm{id}}(\al, \be) }
&
\opn{Hom}_{A'}(Q', I')
\ar[d]^ {\opn{Hom}_{\mrm{id}}(\al', \be') }
\\
\opn{Hom}_A(\til{Q}, \til{I})
\ar[r]^{\opn{Hom}_v(\til{\psi}, \til{\chi})}
&
\opn{Hom}_{A'}(\til{Q}', \til{I}')
} 
\end{equation}
in $\cat{M}(\Z)$ that is commutative up to homotopy. 
Now let us examine the commutative diagram 
\[ \UseTips \xymatrix @C=14ex @R=8ex {
\opn{Hom}_A(Q, I)
\ar[r]^{ \opn{Hom}_{\mrm{id}}(\al, \mrm{id}_I) }
\ar[d]_{ \opn{Hom}_{\mrm{id}}(\mrm{id}_Q, \be) }
\ar[dr]^{ \ \opn{Hom}_{\mrm{id}}(\al, \be) }
&
\opn{Hom}_{A}(\til{Q}, I)
\ar[d]^{ \opn{Hom}_{\mrm{id}}(\mrm{id}_{\til{Q}}, \be) }
\\
\opn{Hom}_A(Q, \til{I})
\ar[r]^{ \opn{Hom}_{\mrm{id}}(\al, \mrm{id}_{\til{I}}) }
&
\opn{Hom}_A(\til{Q}, \til{I})
} 
\]
in $\cat{M}(\Z)$.
The homomorphisms 
$\opn{Hom}_{\mrm{id}}(\al, \mrm{id}_{\til{I}})$ 
and 
$\opn{Hom}_{\mrm{id}}(\mrm{id}_{\til{Q}}, \be)$
are both quasi-isomorphisms. At least one of the homomorphisms
$\opn{Hom}_{\mrm{id}}(\mrm{id}_Q, \be)$
and 
$\opn{Hom}_{\mrm{id}}(\al, \mrm{id}_I)$
is a quasi-isomorphism. It follows that the diagonal homomorphism 
$\opn{Hom}_{\mrm{id}}(\al, \be)$ is a quasi-isomorphism. 
A similar argument shows that 
$\opn{Hom}_{\mrm{id}}(\al', \be')$ is a quasi-isomorphism. Going back to 
diagram (\ref{eqn:970}), we see that it is enough to prove that 
$\opn{Hom}_v(\til{\psi}, \til{\chi})$
is a quasi-isomorphism.

Let 
$\la : \til{I} \to \opn{Hom}_{A'}(A, \til{I}')$
be the homomorphism 
$\la(i)(a) := \til{\chi}(a \cd i)$
in $\cat{M}(A)$.
It fits into a commutative diagram 
\[ \UseTips \xymatrix @C=6ex @R=6ex {
\til{I}
\ar[r]^(0.3){\la}
\ar[d]_{\til{\chi}}
& 
\opn{Hom}_{A'}(A, \til{I}')
\ar[d]^{ \opn{Hom}_{\mrm{id}}(v, \mrm{id}) }
\\
\til{I}'
& 
\opn{Hom}_{A'}(A', \til{I}')
\ar[l]_(0.7){ \opn{can} }
} 
\]
in $\cat{M}(A')$, where $\opn{can}$ is the canonical isomorphism. 
Because $\til{\chi}$ and $v$ are quasi-isomorphisms, and $\til{I}'$ is 
K-injective, we see that $\la$ is a quasi-isomorphism. 

Finally, consider the commutative diagram 
\[ \UseTips \xymatrix @C=8ex @R=6ex {
\opn{Hom}_A(\til{Q}, \til{I})
\ar[r]^{ \opn{Hom}_v(\til{\psi}, \til{\chi}) }
\ar[d]_{ \opn{Hom}_{\mrm{id}}(\mrm{id}, \la) }
&
\opn{Hom}_{A'}(\til{Q}', \til{I}')
\\
\opn{Hom}_A(\til{Q}, \opn{Hom}_{A'}(A, \til{I}'))
\ar[r]^(0.6){ \opn{adj} }
&
\opn{Hom}_{A'}(\til{Q}, \til{I}')
\ar[u]_{ \opn{Hom}_{\mrm{id}}(\til{\psi}, \mrm{id}) }
} 
\]
in $\cat{M}(\Z)$, where $\opn{adj}$ is the adjunction isomorphism. 
Since $\la$ and $\til{\psi}$ are quasi-isomorphisms, $\til{Q}$ is K-projective, 
and  $\til{I}'$ is K-injective, it follows that 
$\opn{Hom}_v(\til{\psi}, \til{\chi})$
is a quasi-isomorphism.
\end{proof}
