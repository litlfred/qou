---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-6
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 0.945
---
This article is about the {\em rigid approach to Grothendieck Duality} (GD).
We survey the main features of this approach, discussing both results that were 
already obtained, and future expected results. 
 
Throughout this article we work over a fixed base ring $\K$, which is a finite 
dimensional regular noetherian commutative ring (e.g.\ a field or the ring of 
integers $\Z$). All rings are commutative $\K$-rings, and by default they are 
essentially finite type (EFT) over $\K$.

In Section 1 we review the {\em squaring operation}. Given a ring $A$, the 
squaring operation is a functor $\opn{Sq}_{A / \K}$ from the derived category 
$\cat{D}(A)$ to itself. This is a quadratic functor, and -- unless $A$ is flat 
over $\K$ -- its construction requires the use of {\em commutative and 
noncommutative DG rings}; see \cite{Ye6}. The squaring operation has 
{\em backward functoriality} over any ring homomorphism $u : A \to B$, and 
{\em forward functoriality} when $u$ is {\em essentially \'etale}.

A {\em rigid complex} over $A$ (relative to $\K$) is a pair $(M, \rho)$, where 
$M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$, and 
$\rho : M \iso \opn{Sq}_{A / \K}(M)$ is an isomorphism in $\cat{D}(A)$. 
There is a pretty obvious notion of {\em rigid morphism} between rigid 
complexes (see Definition \ref{dfn:235} ). This notion extends to {\em rigid 
backward morphisms} over any ring homomorphism $u : A \to B$, and to {\em rigid 
forward morphisms} when $u$ is essentially \'etale.

A {\em rigid dualizing complex} over $A$ is a rigid complex 
$(R_A, \rho_A)$ as above, such that $R_A$ is a dualizing complex over $A$ in 
the sense of \cite{RD}. This concept is discussed in Section 2. 
The ring $A$ has a rigid dualizing complex
$(R_A, \rho_A)$, and it is unique up to a unique rigid isomorphism. 
If $u : A \to B$ is a finite ring homomorphism, then there is a unique 
nondegenerate rigid backward morphism 
$\opn{tr}^{\mrm{rig}}_u : (R_B, \rho_B) \to (R_A, \rho_A)$
called the {\em rigid trace morphism}. 
If $v : A \to A'$ is an essentially \'etale ring homomorphism, then 
there is a unique nondegenerate rigid forward morphism 
$\opn{q}^{\mrm{rig}}_v : (R_A, \rho_A) \to (R_{A'}, \rho_{A'})$
called the {\em rigid \'etale-localization morphism}. The morphisms 
$\opn{tr}^{\mrm{rig}}_u$ and $\opn{q}^{\mrm{rig}}_v$
commute with each other in the appropriate sense. 

Having the rigid dualizing complex $(R_A, \rho_A)$ on every EFT $\K$-ring $A$
allows to construct the {\em twisted induction pseudofunctor}, in a
totally algebraic way (rings only, no geometry), equipped with forward and 
backward functorialities. All the material up to this point (the content of 
Sections 1-2) is in the papers \cite{Ye6} and \cite{OSY}, the latter joint 
with M. Ornaghi and S. Singh. 

Looking to the future, we plan to study a more refined object than the rigid 
dualizing complex: it is the {\em rigid residue complex} 
$(\KK_A, \rho_A)$ of a ring $A$. Given an essentially \'etale ring homomorphism 
$v : A \to A'$, there is the {\em nondegenerate rigid \'etale-localization 
homomorphism} $\opn{q}^{\mrm{res}}_{v} : \KK_{A} \to \KK_{A'}$. 
For a finite ring homomorphism $u : A \to B$ there is the {\em nondegenerate 
rigid trace homomorphism} 
$\opn{tr}^{\mrm{res}}_{u} : \KK_{B} \to \KK_{A}$. 
The latter extends to a functorial backward homomorphism 
$\opn{tr}^{\mrm{ires}}_{u} : \KK_B \to \KK_A$ 
for an arbitrary ring homomorphism $u$, called the {\em ind-rigid trace}, but 
$\opn{tr}^{\mrm{ires}}_{u}$ is only a homomorphism of graded $A$-modules.
We should stress that $\opn{q}^{\mrm{res}}_{v}$ and 
$\opn{tr}^{\mrm{res}}_{v}$ are actual homomorphisms of complexes (see Remark 
\ref{rem:295} regarding notation). 
This topic, summarized in Section 3, is planned for the paper \cite{Ye8}. 

Rigid residue complexes can be easily glued on finite type (FT) $\K$-schemes, 
and they still have the ind-rigid trace 
$\opn{tr}^{\mrm{ires}}_f : f_{*}(\KK_Y) \to \KK_X$
for an arbitrary scheme map $f : Y \to X$. The twisted induction pseudofunctor 
from Section 2 now becomes the geometric {\em  twisted inverse image 
pseudofunctor} $f \mapsto f^!$. We expect to prove the Rigid Residue Theorem
\ref{thm:1} and the Rigid Duality Theorem \ref{thm:2} for proper maps of EFT 
$\K$-schemes, thus recovering almost all the results from the original book 
“Residues and Duality” \cite{RD}, yet in a very explicit way.
This topic is covered in Section 4, and planned for the paper \cite{Ye9}. 

For every scheme $X$ the assignment $X' \mapsto \KK_{X'}$ 
is a quasi-coherent sheaf on the small \'etale site $X_{\rm{et}}$.
This implies that every finite type Deligne-Mumford (DM) $\K$-stack $\XX$ 
admits a rigid residue complex $\KK_{\XX}$. Here too we have the 
twisted inverse image pseudofunctor $f \mapsto f^!$ . For a map 
$f : \YY \to \XX$ of FT DM $\K$-stacks there is the ind-rigid trace
$\opn{tr}^{\mrm{ires}}_f : f_{*}(\KK_Y) \to \KK_X$. Under a mild 
technical condition, we expect to prove the Rigid Residue Theorem \ref{thm:10}
for proper maps of DM stacks, and the Rigid Duality Theorem \ref{thm:11} for 
such maps that are also tame. This is the content of Section 5 of the article, 
and will be written in the paper \cite{Ye10}. 

To finish the Introduction, a few words on the history of the rigid approach to 
GD. Rigid dualizing complexes were invented by M. Van den Bergh in the 1990's, 
in the noncommutative setting. This concept was imported to commutative 
algebra by J.J. Zhang and the author around 2005, where it was made functorial, 
and it was also expanded to the arithmetic setting (namely allowing a base 
ring $\K$ that is not a field). More details on the history of the topic, with 
references, can be found  in Remark \ref{rem:279}. 
Many of the ideas in this article were already mentioned in our lectures from 
2013, see \cite{Ye5}.


\medskip \noindent 
{\em Acknowledgments.}
Because this is a project spanning almost 15 years (and counting), it is 
impossible to thank all the people who had contributed to it. Therefore I shall 
only mention my collaborator James J. Zhang with whom the project began; my 
current collaborators Mattia Ornaghi and Saurabh Singh;   
Martin Olsson and Dan Edidin who assisted me in my attempts to understand 
DM stacks; and Jack Hall and Amnon Neeman who explained some of their work to 
me.  The project is currently supported by the Israel Science Foundation 
grant no.\ 824/18. 





\section{The Squaring Operation and Rigid Complexes over Rings}
 
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
