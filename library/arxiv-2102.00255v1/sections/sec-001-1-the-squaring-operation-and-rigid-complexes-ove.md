---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-001-1-the-squaring-operation-and-rigid-complexes-ove
section_title: "The Squaring Operation and Rigid Complexes over Rings"
section_number: 1
pages: 3-6
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.969
doc_brief: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS — In this article we explain the theory of rigid residue complexes in commutative algebra and algebraic geometry, summarizing the"
---
We fix a base ring $\K$, which is regular noetherian of finite Krull 
dimension (e.g.\ a field or $\Z$).
Recall that a commutative $\K$-ring $A$ is called {\em essentially finite type} 
(EFT) if it is a localization of a finite type $\K$-ring. 
Note that such a ring $A$ is noetherian and of finite Krull dimension.
The category of EFT commutative $\K$-rings is denoted by 
$\cat{Rng} \eftover \K$.
All rings in this paper belong to $\cat{Rng} \eftover \K$.

For a ring $A$ we denote by $\cat{M}(A)$ the abelian category of 
$A$-modules, and by $\cat{C}(A)$ the DG category of complexes of 
$A$-modules. The strict subcategory 
$\cat{C}_{\mrm{str}}(A) \sub \cat{C}(A)$
has the same objects, but its morphisms are the degree $0$ cocycles (i.e.\ 
the degree $0$ homomorphisms $\phi : M \to  N$ that commute with the 
differentials). The derived category is $\cat{D}(A)$.
The categorical localization functor 
$\opn{Q} : \cat{C}_{\mrm{str}}(A) \to \cat{D}(A)$
is the identity on objects, and it is universal for inverting 
quasi-isomorphisms in $\cat{C}_{\mrm{str}}(A)$. 
Note that $\cat{C}_{\mrm{str}}(A)$ is an abelian category, $\cat{D}(A)$ is a 
triangulated category, and the functor $\opn{Q}$ is $A$-linear. 
Inside $\cat{D}(A)$ there is the full triangulated subcategory
$\cat{D}^{\mrm{b}}_{\mrm{f}}(A)$
of complexes with bounded finitely generated cohomology. 
All the necessary facts about derived categories can be found in our book 
\cite{Ye7}. Furthermore, the contents of Sections 1-3 are treated in detail in 
this book, under the assumption that the rings in question are flat over $\K$. 

Following \cite{Ye6} and \cite[Chapter 3]{Ye7}, by {\em commutative DG 
$\K$-ring} we mean a nonpositive strongly commutative DG ring 
$\til{A} = \bigoplus_{i \leq 0} \til{A}^i$,
equipped with a ring homomorphism $\K \to \til{A}^0$.
Strong commutativity means that $b \cd a = (-1)^{i \cd j} \cd a \cd b$ for 
all $a \in \til{A}^i$ and $b \in \til{A}^j$, and that $a \cd a = 0$ when $i$ is 
odd. The DG ring $\til{A}$ is said to be K-flat if it is K-flat as a DG 
$\K$-module. 

Let $A$ be a ring. A {\em K-flat commutative DG ring resolution} of $A$ is  
a quasi-isomorphism $\til{A} \to A$ from a K-flat commutative DG $\K$-ring 
$\til{A}$. Such resolutions always exist. 

Here is the main theorem of \cite{Ye6}:

\begin{thm}[\cite{YZ1}, \cite{Ye6}] \label{thm:230}
There is a functor
\[ \opn{Sq}_{A / \K} : \cat{D}(A) \to \cat{D}(A) \]
called the {\em squaring operation}, equipped with a canonical isomorphism 
\[ \opn{Sq}_{A / \K}(M) \cong  
\opn{RHom}_{\til{A} \ot_{\K} \til{A}}(A, M \otimes^{\mrm{L}}_{\K} M) \]
for every K-flat  commutative DG ring resolution $\til{A} \to A$. 
\end{thm}

See \cite[Theorem 0.3.4]{Ye6} for the precise statement. It is interesting to 
mention that the proof requires the use of {\em noncommutative DG rings}. 

\begin{thm}[\cite{YZ1}, \cite{Ye6}] \label{thm:231}
The functor $\opn{Sq}_{A / \K}$ is a {\em quadratic functor}, namely for a 
morphism $\phi : M \to N$ in $\cat{D}(A)$ and an element $a \in A$, there is 
equality 
\[ \opn{Sq}_{A / \K} (a \cd \phi) = a^2 \cd \opn{Sq}_{A / \K} (\phi) . \]
\end{thm}

\begin{dfn}[\cite{YZ1}, \cite{Ye6}] \label{dfn:230}
A {\em rigid complex} over $A$ relative to $\K$ is a pair 
$(M, \rho)$, consisting of a complex 
$M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$, and an isomorphism
$\rho : M \iso \opn{Sq}_{A / \K}(M)$ in $\cat{D}(A)$,
called a {\em rigidifying isomorphism} for $M$. 
\end{dfn}

\begin{dfn}[\cite{YZ1}, \cite{Ye6}] \label{dfn:231}
Suppose $(M, \rho)$ and $(N, \sigma)$ are rigid complexes. A {\em 
rigid morphism} $\phi : (N, \sigma) \to (M, \rho)$
is a morphism $\phi : N \to M$ in $\cat{D}(A)$, such that the diagram
\[ \UseTips \xymatrix @C=7ex @R=4ex {
N
\ar[r]^(0.34){\sigma}
\ar[d]_{\phi}
&
\opn{Sq}_{A / \K}(N)
\ar[d]^{\opn{Sq}_{A / \K}(\phi)}
\\
M
\ar[r]^(0.34){\rho}
&
\opn{Sq}_{A / \K}(M)
} \]
in $\cat{D}(A)$ is commutative.

We denote by $\cat{D}(A)_{\mrm{rig} / \K}$
the category of rigid complexes and rigid morphisms between them.
\end{dfn}

\begin{dfn}[\cite{Ye7}] \label{dfn:232}
A complex $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$
is said to have the {\em derived Morita property} if the derived homothety 
morphism $A \to \opn{RHom}_{A}(M, M)$ in $\cat{D}(A)$ is an isomorphism.
\end{dfn}

Dualizing complexes (to be recalled later) and tilting complexes (see 
\cite[Chapter 14]{Ye7}) have the derived Morita property. 

\begin{thm}[\cite{YZ1}, \cite{Ye6}] \label{thm:233}
If $(M, \rho)$ is a rigid complex, such that $M$ has the derived Morita 
property, then the only  automorphism of $(M, \rho)$ in
$\cat{D}(A)_{\mrm{rig} / \K}$ is the identity. 
\end{thm}

The key to the proof of this theorem is the quadratic property of the functor 
$\opn{Sq}_{A / \K}$, see Theorem \ref{thm:231}.

The squaring operation $\opn{Sq}_{A / \K}$  has two kinds of functorialities, 
which we describe next.  First there is {\em backward functoriality}. 
Given a ring homomorphism $u : A \to B$, and
complexes $M \in \cat{D}(A)$ and $N \in \cat{D}(B)$, a morphism 
$\th : N \to  M$ in $\cat{D}(A)$ is called a {\em backward morphism} over $u$. 
The backward morphism $\th$ is called {\em nondegenerate} if the morphism
$N \to \opn{RHom}_A(B, M)$ in $\cat{D}(B)$,
which corresponds to $\th$ by adjunction, is an isomorphism.
 
The next theorem extends Theorem \ref{thm:230}. 

\begin{thm}[\cite{YZ1}, \cite{Ye6}] \label{thm:234}
Let $u : A \to B$ be a ring homomorphism, and let 
$\th : N \to  M$ be a backward morphism in $\cat{D}(A)$ over $u$. Then 
there is a  backward morphism
\[ \opn{Sq}_{u / \K}(\th) :\opn{Sq}_{B / \K}(N) \to \opn{Sq}_{A / \K}(M) \]
in $\cat{D}(A)$ over $u$, with an explicit formula given suitable DG ring 
resolutions $\til{A} \to A$ and $\til{B} \to B$. 
The operation $\opn{Sq}_{u / \K}(\th)$ is functorial in $u$ and $\th$. 
\end{thm}

For a precise statement see \cite[Theorem 0.3.5]{Ye6}.

\begin{dfn}[\cite{YZ1}, \cite{OSY}] \label{dfn:233}
Let $u : A \to B$ be a ring homomorphism, let 
$(M, \rho) \in \cat{D}(A)_{\mrm{rig} / \K}$, and let 
$(N, \si) \in \cat{D}(B)_{\mrm{rig} / \K}$. 
A {\em rigid backward morphism} 
$\th :  (N ,\si) \to (M ,\rho)$
over $u$ is a backward morphism $\th : N \to M$ in $\cat{D}(A)$ over $u$,  
such that the diagram 
\[ \UseTips \xymatrix @C=7ex @R=4ex {
N
\ar[d]_{\th}
\ar[r]^(0.34){\si}
&
\opn{Sq}_{B / \K}(N)
\ar[d]^{\opn{Sq}_{u / \K}(\th)}
\\
M
\ar[r]^(0.34){\rho}
&
\opn{Sq}_{A / \K}(M)
} \]
in $\cat{D}(A)$ is commutative.
\end{dfn}

Next is a generalization of Theorem \ref{thm:233}.

\begin{thm}[\cite{YZ1}, \cite{OSY}] \label{thm:235}
In the situation of Definition \ref{dfn:233}, if $N \in \cat{D}(B)$ has the 
derived Morita property, then there is at most 
one nondegenerate rigid backward morphism 
$\th :  (N ,\si) \to (M ,\rho)$ over $u$. 
\end{thm}

The second functoriality of the squaring operation is {\em forward 
functoriality}. A homomorphism $v : A \to A'$ is called 
{\em essentially \'etale} if it is EFT and formally \'etale. 
We know that an essentially \'etale  homomorphism is flat. 
Given an essentially \'etale  homomorphism $v : A \to A'$, and complexes 
$M \in \cat{D}(A)$ and $M' \in \cat{D}(A')$, a morphism 
$\la : M \to  M'$ in $\cat{D}(A)$ is called a {\em forward morphism} over $v$. 
The forward morphism $\la$ is called {\em nondegenerate} if the morphism
$A' \ot_A M \to M'$ in $\cat{D}(A')$, which corresponds to $\la$ by 
adjunction, is an isomorphism.

\begin{thm}[\cite{YZ1}, \cite{OSY}] \label{thm:236}
Let $v : A \to A'$ be an essentially \'etale ring homomorphism, and let 
$\la : M \to  M'$ be a forward morphism in $\cat{D}(A)$ over $v$. Then 
there is a forward morphism 
\[ \opn{Sq}_{u / \K}(\la) :\opn{Sq}_{A / \K}(M) \to \opn{Sq}_{A' / \K}(M') \]
in $\cat{D}(A)$ over $v$, with an explicit formula given suitable DG ring 
resolutions $\til{A} \to A$ and $\til{B} \to B$. 
The operation $\opn{Sq}_{u / \K}(\la)$ is functorial in $v$ and $\la$. 
\end{thm}

In \cite{YZ1} we only considered the case of a {\em localization} homomorphism 
$v : A \to A'$. The essentially \'etale case, proved in \cite{OSY}, is much 
more difficult, and it relies on a detailed study of the diagonal embedding of 
$\opn{Spec}(A')$ in $\opn{Spec}(A' \ot_A A')$. 

\begin{dfn}[\cite{YZ1}, \cite{OSY}] \label{dfn:235} 
Let $v : A \to A'$ be an essentially \'etale ring homomorphism, let 
$(M, \rho) \in \cat{D}(A)_{\mrm{rig} / \K}$, and let 
$(M', \rho') \in \cat{D}(A')_{\mrm{rig} / \K}$. 
A {\em rigid forward morphism} 
$\la :  (M ,\rho) \to (M' ,\rho')$
over $v$ is a forward morphism $\la : M \to M'$ in $\cat{D}(A)$ over $v$,  
such that the diagram 
\[ \UseTips \xymatrix @C=7ex @R=4ex {
M
\ar[d]_{\la}
\ar[r]^(0.34){\rho}
&
\opn{Sq}_{B / \K}(M)
\ar[d]^{\opn{Sq}_{v / \K}(\la)}
\\
M'
\ar[r]^(0.34){\rho'}
&
\opn{Sq}_{A / \K}(M')
} \]
in $\cat{D}(A)$ is commutative.
\end{dfn}

Here is a second generalization of Theorem \ref{thm:233}.

\begin{thm}[\cite{OSY}] \label{thm:237}
In the situation of Definition \tup{\ref{dfn:235}}, if $M' \in \cat{D}(A')$ has 
the derived Morita property, then there is at most 
one nondegenerate rigid forward morphism 
$\la :  (M ,\rho) \to (M' ,\rho')$ over $v$. 
\end{thm}
 
The backward and forward squaring operations commute with each other. This is 
the content of the next theorem. 

\begin{thm}[\cite{OSY}] \label{thm:238}
Suppose we are given ring homomorphisms $u : A \to  B$ and $v : A \to  A'$, 
such 
that $v$ is essentially \'etale, and a backward morphism $\th : N \to M$ in 
$\cat{D}(A)$ over $u$. Define the ring $B' := A' \ot_A B$, and the complexes 
$M' := A' \ot_A M \in \cat{D}(A')$ and
$N' := B' \ot_B N \in \cat{D}(B')$. Let 
$\th' : N' \to M'$ be the induced backward morphism in $\cat{D}(A')$,
and let $\opn{q}_{M} : M \to M'$ and $\opn{q}_{N} : N \to N'$ be the canonical 
nondegenerate forward morphisms. We get the following commutative diagrams
\[ \UseTips \xymatrix @C=6ex @R=5ex {
A
\ar[r]^{u}
\ar[d]_{v}
&
B
\ar[d]^{w}
\\
A'
\ar[r]^{u'}
&
B'
}
\qquad \qquad 
\UseTips \xymatrix @C=6ex @R=5ex {
M
\ar[d]_{\opn{q}_{M}}
&
N
\ar[l]_{\th}
\ar[d]^{\opn{q}_{N}}
\\
M'
&
N'
\ar[l]_{\th'}
} \]
in $\cat{Rng} \eftover \K$ and in $\cat{D}(A)$. Then the diagram  
\begin{equation} \label{eqn:219}
\UseTips \xymatrix @C=10ex @R=6ex {
\opn{Sq}_{A / \K}(M)
\ar[d]_{\opn{Sq}_{v / \K}(\opn{q}_{M})}
&
\opn{Sq}_{B / \K}(N)
\ar[l]_{\opn{Sq}_{u / \K}(\th)}
\ar[d]^{\opn{Sq}_{w / \K}(\opn{q}_{N})}
\\
\opn{Sq}_{A / \K}(M')
&
\opn{Sq}_{B / \K}(N')
\ar[l]_{\opn{Sq}_{u' / \K}(\th')}
}
\end{equation}
in $\cat{D}(A)$ is commutative. 
\end{thm}

This theorem implies that there is no conflict between Definitions  
\ref{dfn:233} and \ref{dfn:235} when $A = B = A'$ and $u = v = \opn{id}_A$, in 
which case the morphisms $\th$ and $\la$ in these definitions are 
both forward and backward morphisms.
