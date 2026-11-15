---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-009-9-rigid-dg-modules
section_title: "Rigid DG Modules"
section_number: 9
pages: 47-51
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.966
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
\label{sec:rigid}

Recall that all our DG rings are commutative (Convention \ref{conv:100}); 
namely we work inside the category $\cat{DGR}^{\leq 0}_{\mrm{sc}}$.
At the beginning of this section we do not make any finiteness assumptions on 
DG rings. 

In our new paper \cite{Ye5} we introduced the {\em squaring operation} for
commutative DG rings. It is summarized in Theorem \ref{thm:500}  below,
which is a combination of \cite[Theorems 0.3.4, 0.3.5 and 7.16]{Ye5}.

Given a homomorphism $u : A \to B$ of DG rings, a {\em K-flat resolution} of 
$u$ is a commutative diagram 
\[ \UseTips \xymatrix @C=8ex @R=6ex {
\til{A}
\ar[r]^{\til{u}} ="tilu"
\ar[d]_{v} ="v"
{} \save 
[]+<-12ex,-1ex> *+[F-:<3pt>]{\scriptstyle \text{qu-isom}} 
\ar@(r,l)@{..} "v" 
\restore
&
\til{B}
\ar[d]^{w} ="w"
{} \save 
[]+<10ex,4ex> *+[F-:<3pt>]{\scriptstyle \text{K-flat}} 
\ar@(l,ur)@{..} "tilu" 
\restore
&
{} \save 
[]+<4ex,-1ex> *+[F-:<3pt>]{\scriptstyle \text{surj qu-isom}} 
\ar@(l,r)@{..} "w" 
\restore
\\
A
\ar[r]_{u} ="u"
&
B
} \]
in $\cat{DGR}^{\leq 0}_{\mrm{sc}}$, where $v$ is a quasi-isomorphism, $w$ is a 
surjective quasi-isomorphism, and $\til{B}$ is K-flat as a DG $\til{A}$-module. 
Such resolutions always exist. 

A K-flat resolution $\til{A} \to \til{B}$ of $A \to B$ gives rise to a functor 
$\opn{Sq}_{B / A}^{\til{B} / \til{A}} : \cat{D}(B) \to \cat{D}(B)$,
\[ \opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) := 
\opn{RHom}_{\til{B} \ot_{\til{A}} \til{B}}(B, M \ot^{\mrm{L}}_{\til{A}} M) . \]

\begin{thm}[\cite{Ye5}] \label{thm:500}
Let $A \to B$ be a homomorphism of DG rings. 
\begin{enumerate}
\item There is a functor 
\[ \opn{Sq}_{B / A} : \cat{D}(B) \to \cat{D}(B) \ , \]
called the squaring operation, together with a compatible system of 
isomorphisms of functors
$\opn{Sq}_{B / A} \cong \opn{Sq}_{B / A}^{\til{B} / \til{A}}$,
where $\til{A} \to \til{B}$ runs over all K-flat resolutions  of $A \to B$
in $\cat{DGR}^{\leq 0}_{\mrm{sc}}$.

\item The functor $\opn{Sq}_{B / A}$ is quadratic, in the following 
sense\tup{:} for any morphism $\phi : M \to N$ in $\cat{D}(B)$, and any element
$b \in \bar{B}$, there is equality 
\[ \opn{Sq}_{B / A}(b \cd \phi) = b^2 \cd \phi \ . \]
\end{enumerate}
\end{thm}

The compatible system of isomorphisms of functors in item (1) of the theorem is 
stated in detail in \cite[Theorem 0.3.4]{Ye5}. These isomorphisms make the 
functor $\opn{Sq}_{B / A}$ unique up to a unique isomorphism. 
In part (2) we use the fact that $\cat{D}(B)$ is a 
$\bar{B}$-linear category (see Proposition \ref{prop:311}). 
 
\begin{dfn} \label{dfn:500}
Let $A \to B$ be a homomorphism of DG rings.
\begin{enumerate}
\item Let $M$ be a DG $B$-module. A {\em rigidifying isomorphism} for $M$ 
relative to $A$ is an isomorphism 
\[ \rho : M \iso \opn{Sq}_{B / A}(M) \]
in $\cat{D}(B)$.

\item A {\em rigid DG module over $B$ relative to $A$} is a pair 
$(M, \rho)$, consisting of a DG $B$-module $M$, and a rigidifying isomorphism
$\rho : M \iso \opn{Sq}_{B / A}(M)$ in $\cat{D}(B)$.
\end{enumerate}
\end{dfn}

Unlike in \cite{YZ1}, here we do not impose any finiteness conditions on $M$ 
as part of the definition of rigidity. 

\begin{dfn} \label{dfn:501}
Let $A \to B$ be a homomorphism of DG rings.
\begin{enumerate}
\item Let $(M, \rho)$ and $(M', \rho')$ be rigid DG modules over $B$ relative 
to $A$. A {\em rigid morphism} 
\[ \phi : (M, \rho) \to (M', \rho') \]
is a morphism $\phi : M \to M'$ in $\cat{D}(B)$, such that the diagram 
\[ \UseTips \xymatrix @C=5ex @R=5ex {
M 
\ar[r]^(0.35){\rho}
\ar[d]_{\phi}
&
\opn{Sq}_{B / A}(M)
\ar[d]^{\opn{Sq}_{B / A}(\phi)}
\\
M' 
\ar[r]^(0.35){\rho'}
&
\opn{Sq}_{B / A}(M')
} \]
in $\cat{D}(B)$ is commutative. 

\item The category of rigid DG modules over $B$ relative to $A$ is denoted by 
\lb $\cat{D}(B)_{\mrm{rig} / A}$.
\end{enumerate}
\end{dfn}

\begin{thm}[Uniqueness of Rigid Automorphisms] \label{thm:501}
Let $A \to B$ be a homomorphism of DG rings, and let 
$(M, \rho)$ be a rigid DG module over $B$ relative to $A$. Assume that the 
adjunction morphism 
$B \to \opn{RHom}_{B}(M, M)$ is an isomorphism. Then the only automorphism of 
$(M, \rho)$ in $\cat{D}(B)_{\mrm{rig} / A}$ is the identity. 
\end{thm}

\begin{proof}
The idea of the proof is already in \cite[Theorem 5.2]{Ye2}.
The adjunction condition implies that the ring homomorphism 
$\bar{B} \to \opn{End}_{\cat{D}(B)}(M)$
is bijective. Take any automorphism $\phi$ of $(M, \rho)$ in 
$\cat{D}(B)_{\mrm{rig} / A}$. Then $\phi = b \cd \opn{id}_M$, for a unique 
invertible element $b \in \bar{B}$. By item (2) of Theorem \ref{thm:500}
we know that 
$\opn{Sq}_{B / A}(\phi) = b^2 \cd \opn{Sq}_{B / A}(\opn{id}_M)$. 
On the other hand, because $\phi$ and $\opn{id}_M$ are both rigid, we get 
\[ \begin{aligned}
& \opn{Sq}_{B / A}(\phi) = \rho \circ \phi \circ \rho^{-1} = 
\rho \circ (b \cd \opn{id}_M) \circ \rho^{-1} 
\\
& \qquad = b \cd (\rho \circ \opn{id}_M \circ \rho^{-1}) = 
b \cd \opn{Sq}_{B / A}(\opn{id}_M) .
\end{aligned} \]
This shows that
$b^2 \cd \opn{id}_M = b \cd \opn{id}_M$, so $b^2 = b$, and hence $b = 1$. 
\end{proof}

\begin{dfn} \label{dfn:503}
Let $A$ be a tractable cohomologically pseudo-noetherian DG ring, with traction 
$\K \to A$ (see Definition \ref{dfn:46}). 
A {\em rigid dualizing DG module over $A$ relative to $\K$} is a 
rigid DG module $(R, \rho)$ over $A$ relative to $\K$ (Definition 
\ref{dfn:500}), such that $R$ is a dualizing DG module over $A$
 (Definition \ref{dfn:253}).
\end{dfn}

\begin{lem} \label{lem:526}
Suppose $\K$ is a noetherian ring, $A$ is a cohomologically pseudo-noetherian 
DG ring, and $\K \to A$ is a cohomologically essentially finite type 
homomorphism. Let $\K \to \til{A}$ be a K-flat resolution of $\K \to A$, and 
define 
$\til{A}^{\mrm{en}} := \til{A} \ot_{\K} \til{A}$. 
\begin{enumerate}
\item The DG ring $\til{A}^{\mrm{en}}$ is cohomologically pseudo-noetherian,
and the homomorphism $\K \to \til{A}^{\mrm{en}}$ is a cohomologically 
essentially finite type. 

\item Let $P \in \cat{D}(A)$ be a tilting DG $A$-module. Then 
$P \ot^{\mrm{L}}_{\K} P \in \cat{D}(\til{A}^{\mrm{en}})$
is a tilting DG $\til{A}^{\mrm{en}}$-module.
\end{enumerate}
\end{lem}

The derived tensor product $P \ot^{\mrm{L}}_{\K} P$ in item (2) is calculated 
as follows: we take any K-flat resolution $\til{P} \to P$ in 
$\cat{C}(\til{A})$, and define 
$P \ot^{\mrm{L}}_{\K} P := \til{P} \ot_{\K} \til{P}$.
Because $\til{P}$ is K-flat over $\K$, this is independent of the resolution, 
up to a canonical isomorphism in $\cat{D}(\til{A}^{\mrm{en}})$. 

\begin{proof}
(1) As in the proof of Lemma \ref{lem:380}, we can find a commutative diagram 
in $\cat{DGR}^{\leq 0}_{\mrm{sc}}$
\[  \UseTips \xymatrix @C=5ex @R=5ex {
\K
\ar[r]
\ar[d]
&
\til{A}
\ar[r]
\ar[d]^{\til{f}}
&
A 
\ar[r]
\ar[d]
& 
\bar{A}
\\
\til{A}_{\mrm{eft}}
\ar[r]^{\til{g}}
&
\til{A}_{\mrm{loc}}
\ar[r]
&
A_{\mrm{loc}}
\ar[ur]
} \]
such that $\til{f}$ is a K-flat quasi-isomorphism, $\til{g}$ is a 
quasi-isomorphism, the DG ring $\til{A}_{\mrm{eft}}$ is K-flat over $\K$, 
the ring $\til{A}^0_{\mrm{eft}}$ is essentially finite type over $\K$, and each 
module $\til{A}^i_{\mrm{eft}}$ is finite over $\til{A}^0_{\mrm{eft}}$.
Now $\til{A}$, $\til{A}_{\mrm{eft}}$ and $\til{A}_{\mrm{loc}}$
are all K-flat over $\K$. Hence, letting 
$\til{A}_{\mrm{loc}}^{\mrm{en}} := \til{A}_{\mrm{loc}} \ot_{\K} 
\til{A}_{\mrm{loc}}$
and
$\til{A}_{\mrm{eft}}^{\mrm{en}} := \til{A}_{\mrm{eft}} \ot_{\K} 
\til{A}_{\mrm{left}}$,
we get DG ring quasi-isomorphisms 
$\til{A}_{\mrm{eft}}^{\mrm{en}} \to \til{A}_{\mrm{loc}}^{\mrm{en}}$
and 
$\til{A}_{}^{\mrm{en}} \to \til{A}_{\mrm{loc}}^{\mrm{en}}$.
Therefore it suffices to prove the required assertions for 
$\til{A}_{\mrm{eft}}^{\mrm{en}}$. 

Consider the ring 
$(\til{A}_{\mrm{eft}}^{\mrm{en}})^0 = \til{A}^0_{\mrm{eft}} \ot_{\K} 
\til{A}^0_{\mrm{eft}}$. 
It is essentially finite type over $\K$, and thus it is also noetherian. 
For any $i \leq 0$ we have 
\[ (\til{A}_{\mrm{eft}}^{\mrm{en}})^i = 
\bigoplus_{i \leq p \leq 0} \til{A}^p_{\mrm{eft}} \ot_{\K} 
\til{A}^{i - p}_{\mrm{eft}} , \]
and this is a finite module over  
$(\til{A}_{\mrm{eft}}^{\mrm{en}})^0$. 
Therefore the ring $\opn{H}^0(\til{A}_{\mrm{eft}}^{\mrm{en}})$,
being a quotient of $(\til{A}_{\mrm{eft}}^{\mrm{en}})^0$, is 
essentially finite type over $\K$. Each 
$\opn{H}^i(\til{A}_{\mrm{eft}}^{\mrm{en}})$,
being a subquotient of $(\til{A}_{\mrm{eft}}^{\mrm{en}})^i$, 
is a finite module over $\opn{H}^0(\til{A}_{\mrm{eft}}^{\mrm{en}})$. 

\medskip \noindent
(2) Let $Q \in \cat{D}(A)$ be a quasi-inverse of $P$. Then 
\[ (Q \ot^{\mrm{L}}_{\K} Q) \ot^{\mrm{L}}_{A} (P \ot^{\mrm{L}}_{\K} P) \cong
(Q \ot^{\mrm{L}}_{A} P)  \ot^{\mrm{L}}_{\K} (Q \ot^{\mrm{L}}_{A} P)
\cong A  \ot^{\mrm{L}}_{\K} A \cong \til{A}^{\mrm{en}} \]
in $\cat{D}(\til{A}^{\mrm{en}})$. 
\end{proof}

\begin{thm}[Uniqueness of Rigid Dualizing DG Modules] \label{thm:502}
In the situation of Definition \tup{\ref{dfn:503}}, suppose that
$(R, \rho)$ and $(R', \rho')$ are rigid dualizing DG modules over $A$ relative 
to $\K$. Then there is a unique isomorphism 
$(R, \rho) \cong (R', \rho')$ in $\cat{D}(A)_{\mrm{rig} / \K}$.
\end{thm}

\begin{proof}
The idea of first half of the proof goes back to the original work of Van den 
Bergh \cite{VdB}. According to Theorem \ref{thm:43}(2), there is a tilting DG 
module $P$ such that $R' \cong P \ot^{\mrm{L}}_{A} R$
in $\cat{D}(A)$. 
Choose a K-flat DG ring resolution $\K \to \til{A}$ of $\K \to A$,
and let $\til{A}^{\mrm{en}} := \til{A} \ot_{\K} \til{A}$. 
Then we have isomorphisms 
\[ \begin{aligned}
& P \ot^{\mrm{L}}_{A} R \cong^1 R' \cong^{2}
\opn{RHom}_{\til{A}^{\mrm{en}}}(A, R' \ot^{\mrm{L}}_{\K} R')
\\ & \quad 
\cong^1 \opn{RHom}_{\til{A}^{\mrm{en}}} \bigl( A, (P \ot^{\mrm{L}}_{A} R) 
\ot^{\mrm{L}}_{\K} (P \ot^{\mrm{L}}_{A} R) \bigr)
\\ & \quad 
\cong^3 \opn{RHom}_{\til{A}^{\mrm{en}}} \bigl( A, (R \ot^{\mrm{L}}_{\K} R) 
\ot^{\mrm{L}}_{\til{A}^{\mrm{en}}} (P \ot^{\mrm{L}}_{\K} P) \bigr)
\\ & \quad 
\cong^4 \opn{RHom}_{\til{A}^{\mrm{en}}} ( A, R \ot^{\mrm{L}}_{\K} R) 
\ot^{\mrm{L}}_{\til{A}^{\mrm{en}}} (P \ot^{\mrm{L}}_{\K} P) 
\\ & \quad 
\cong^2 R \ot^{\mrm{L}}_{\til{A}^{\mrm{en}}} (P \ot^{\mrm{L}}_{\K} P) 
\cong^3 R \ot^{\mrm{L}}_{A} P \ot^{\mrm{L}}_{A} P 
\end{aligned} \]
in $\cat{D}(A)$. The isomorphisms $\cong^1$ come from the given isomorphism 
$R' \cong P \ot^{\mrm{L}}_{A} R$
in $\cat{D}(A)$; the isomorphisms $\cong^2$ come from the rigidifying 
isomorphisms $\rho'$ and $\rho$, together with the isomorphisms from 
Theorem \ref{thm:500}(1); the isomorphism $\cong^3$
is by a standard tensor product identity (that is valid also in this derived 
setting, because $\til{A}$ is K-flat over $\K$); and the 
the isomorphism $\cong^4$ is by Lemma \ref{lem:45}, that 
applies because $\til{A}^{\mrm{en}}$ is cohomologically pseudo-noetherian,
$R \ot^{\mrm{L}}_{\K} R$ is in $\cat{D}^+(\til{A}^{\mrm{en}})$, and 
$P \ot^{\mrm{L}}_{\K} P$ is perfect over $\til{A}^{\mrm{en}}$ -- thanks to 
Lemma \ref{lem:526}. 
Now Theorem \ref{thm:43}(3) tells us that 
$P \ot^{\mrm{L}}_{A} P \cong P$ in $\cat{D}(A)$. This implies that $P \cong A$.
We conclude that $R' \cong R$ in $\cat{D}(A)$. 

The remainder of the proof is the same as in the proof of 
\cite[Theorem 5.2]{Ye2}.
Let $\phi : R \iso R'$ be any isomorphism in $\cat{D}(A)$. The calculation in 
the proof of Theorem \ref{thm:501} shows that 
$\opn{Sq}_{A / \K}(\phi) = 
a \cd (\rho' \circ \phi \circ \rho^{-1})$
for a unique invertible element $a \in \bar{A}$. Then 
$a^{-1} \cd \phi : R \to R$ is a rigid isomorphism; and it is unique by 
Theorem \ref{thm:501}.
\end{proof}

Existence of rigid dualizing DG modules in this generality is not known, but we 
believe it it true -- this is Conjecture \ref{conj:505} in the Introduction. 
Conjecture \ref{conj:501} below implies Conjecture \ref{conj:505}.

Suppose $u : A \to B$ is a homomorphism between cohomologically 
pseudo-noetherian DG rings. We say that $u$ is {\em 
cohomologically essentially smooth of relative dimension $n$} if 
$\bar{u} : \bar{A} \to \bar{B}$ is essentially smooth of relative dimension 
$n$, 
and the induced homomorphism 
$\opn{H}(A) \ot_{\bar{A}} \bar{B} \to \opn{H}(B)$
is bijective. In this case, the module of differentials 
$\Omega^1_{\bar{B} / \bar{A}}$ is projective of rank $n$, and hence 
$\Omega^n_{\bar{B} / \bar{A}}$ is projective of rank $1$. 
We define 
$\Omega^n_{B / A}[n] \in \cat{D}(B)$ to be the lift of 
$\Omega^n_{\bar{B} / \bar{A}}[n] \in \cat{D}(\bar{B})$,
under the group isomorphism 
$\opn{DPic}(B) \cong \opn{DPic}(\bar{B})$
of Theorem \ref{thm:40}. There is an alternative description of 
$\Omega^n_{B / A}[n]$ in terms of the {\em cotangent complex} of $B / A$. 
 
\begin{conj} \label{conj:501}
In the situation of Definition \tup{\ref{dfn:503}}, suppose 
$(R_A, \rho_A)$ is a rigid dualizing DG module over $A$ relative to $\K$.
Let $B$ be another DG ring, and let $A \to B$ be a cohomologically 
essentially finite type homomorphism. 
\begin{enumerate}
\item If $A \to B$ is cohomologically pseudo-finite, then the DG module 
\[ R_B := \opn{RHom}_{A}(B, R_A ) \in  \cat{D}(B) \]
has an induced rigidifying isomorphism $\rho_B$ relative to $\K$. 

\item If $A \to B$ is cohomologically essentially smooth of relative dimension 
$n$, then the DG module 
\[ R_B := \Omega^n_{B / A}[n] \ot^{\mrm{L}}_{A} R_A \in  \cat{D}(B) \]
has an induced rigidifying isomorphism $\rho_B$ relative to $\K$. 
\end{enumerate}
\end{conj}

In the case when  $A$ and $B$ are rings, Conjectures \ref{conj:505} and 
\ref{conj:501} were already proved in \cite{YZ1}.
The proofs will be repeated, with improvements, in \cite{Ye7}. 
In the case when the cohomology of $A$ is bounded, Conjectures \ref{conj:505} 
and \ref{conj:501} were very recently proved by Shaul \cite{Sh2}. 
What remains to prove is the case when $\opn{H}(A)$ is unbounded. 

\begin{rem} \label{rem:520}
Finally, a few words on Conjecture \ref{conj:506} from the Introduction. 
We can see three possible routes to try to prove it.
The first route is by generalizing the original proof of 
\cite[Theorem 1.2]{YZ2}, that talked about a regular tractable ring $A$, to the
DG ring case. The second route is by generalizing the proof 
of \cite[Theorem 4]{AIL}, which applied to any tractable ring $A$, to the DG 
ring case. 

There is also a more conceptual route. 
In \cite{Ye5} we introduced the {\em rectangle operation} 
\[ \opn{Rect}_{A / \K}(M, N) := 
\opn{RHom}_{\til{A} \ot_{\K} \til{A}}(A, M \ot^{\mrm{L}}_{\K} N) , \]
for $M, N \in \cat{D}(A)$. Here $\K \to \til{A}$ is a K-flat resolution of 
$\K \to A$, but the rectangle operation is independent of this resolution. 
Notice that the square is a special instance of the rectangle:
$\opn{Sq}_{A / \K}(M) =  \opn{Rect}_{A / \K}(M, M)$.

Recently Shaul \cite{Sh1} proved that when $A$ is a tractable ring, and under 
certain finiteness conditions on $M$ and $N$, there is a canonical isomorphism 
\[ \opn{Rect}_{A / \K}(M, N) \cong 
D \bigl( D(M) \ot^{\mrm{L}}_{A} D(N) \bigr) , \]
where $D := \opn{RHom}_{A}(-, R_A)$, and $R_A$ is the rigid dualizing complex 
of $A$ relative to $\K$. Thus, writing 
$M \ot_{A / \K}^! N := \opn{Rect}_{A / \K}(M, N)$,
this operation becomes a symmetric monoidal structure on (a suitable 
subcategory of) $\cat{D}^{+}_{\mrm{f}}(A)$.

Suppose now that $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$ is rigid relative to 
$\K$. Define 
$L := D(M) \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$. 
Then $L$ satisfies 
$L \ot^{\mrm{L}}_{A} L \cong L$. If $M$ is nonzero on each connected component 
of $\opn{Spec} \bar{A}$, then the same holds for $L$. 
It is not hard to show that in this case $L \cong A$ in $\cat{D}(A)$. Therefore
$M \cong R_A$, so it is a rigid dualizing complex. 

If this work of Shaul could be extended to cover tractable DG rings, we would 
have a proof of Conjecture \ref{conj:506}, at least when $A$ is cohomologically 
bounded. 
\end{rem}
