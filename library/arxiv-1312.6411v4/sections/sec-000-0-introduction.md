---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 2-7
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.986
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS — We consider commutative DG rings (better known as nonpositive strongly commutative associative unital DG algebras)."
---
In this paper we are interested in {\em commutative DG rings}. 
This is an abbreviation for strongly commutative nonpositive associative 
unital differential graded algebras over $\Z$. Thus a commutative DG ring is a 
graded ring $A = \bigoplus_{i \leq 0} A^i$, together with a 
differential $\d$ of degree $1$, that satisfies the graded Leibniz rule. 
The multiplication satisfies 
$b \cd a = (-1)^{i j} \cd a \cd b$
for all $a \in A^i$ and $b \in A^j$, and $a \cd a = 0$ if $i$ is odd.
By default, the DG rings in the Introduction are commutative. 
Rings are viewed as DG rings concentrated in degree $0$ (so they are 
commutative by default throughout the Introduction). 

Commutative DG rings come up in the foundations of {\em derived algebraic 
geometry}, as developed by To\"en-Vezzosi \cite{TV}.
Indeed, a {\em derived stack} is a stack of groupoids
on the site of commutative DG rings (with its \'etale topology). 
Some precursors of this point of view are the papers \cite{Hi2}, 
\cite{Ke2}, \cite{KoSo} and \cite{Be}. 
Another role of commutative DG rings is as {\em resolutions of commutative 
rings}. We shall say more on this role below, since it was the immediate 
motivation for writing the present paper. 

In our paper we study {\em perfect, tilting, dualizing, 
Cohen-Macaulay and rigid DG modules} over commutative DG 
rings. We give definitions that generalize the familiar definitions for rings. 
Many of the results that hold for rings, continue to hold in the much more 
complicated DG setting. Later in the Introduction we discuss the main 
definitions and results of the paper, and a couple of conjectures.  
  
But first let us explain the problem that motivated our work on commutative DG 
rings. {\em Rigid dualizing complexes} over noetherian
commutative rings are the foundation of a new approach to 
Grothendieck Duality on schemes and Deligne-Mumford stacks. 
See the papers \cite{YZ1}, \cite{YZ2}, \cite{Ye3}, \cite{Ye6}, \cite{Ye8} and 
\cite{Ye9}. Rigid dualizing complexes were introduced by Van den Bergh in the 
context of noncommutative rings over a base field $\K$; see \cite{VdB}.
But for the new approach to Grothendieck Duality in algebraic geometry, 
that should apply also to the arithmetic setup, we are interested in 
commutative rings over a base commutative ring $\K$ that is {\em not a field}. 

In this context, the definition of a rigid complex relies on the more primitive 
notion of the {\em square of a complex}. Given a commutative $\K$-ring $A$, 
we choose a  {\em K-flat commutative DG ring resolution} $\til{A} \to A$ 
relative $\K$. Such resolutions exist, because we work with strongly 
commutative DG rings (see Remark \ref{rem:580} for a discussion of this issue). 
For any complex of $A$-modules $M$, its square is the complex of $A$-modules
\begin{equation} \label{eqn:100}
\opn{Sq}_{A / \K}(M) := \opn{RHom}_{\til{A} \ot_{\K} \til{A}}
(A, M \ot_{\K}^{\mrm{L}} M) . 
\end{equation}
The question of independence of $\opn{Sq}_{A / \K}(M)$ of the 
choice of resolution $\til{A}$ is very subtle; and in fact there was a mistake 
in the original proof in \cite{YZ1} 
(which has since been corrected; see \cite{Ye5}). 
A rigid dualizing complex over $A$ relative to $\K$ is a pair 
$(R, \rho)$, consisting of a dualizing complex $R$, and an isomorphism 
$\rho : R \iso \opn{Sq}_{A / \K}(R)$ in the derived category $\cat{D}(A)$. 

In the course of writing the new paper \cite{Ye7} -- which corrects further 
mistakes in the earlier paper \cite{YZ1}, and extends it  -- we realized 
that we need Theorem \ref{thm:61}, that deals with Cohen-Macaulay DG modules.
This is explained in Remark \ref{rem:120}.
The parts of the present paper leading to Section \ref{sec:cm} set the stage 
for the definition of Cohen-Macaulay DG modules and the proof of Theorem 
\ref{thm:61}. 

From a wider perspective, we expect that the results in this paper shall find 
further applications in algebra and geometry. One such possible application 
would be the development of 
a theory of {\em rigid dualizing complexes in derived algebraic 
geometry} (of either flavor: Lurie's or To\"en's). Indeed, a commutative DG 
ring is an affine derived scheme; so what is needed is a way to sheafify our 
constructions. That should be facilitated by  the {\em \'etale descent} and 
{\em \'etale codescent} properties of {\em rigid residue complexes} (see 
\cite{Ye6}). 

Our work in the present paper should be easily accessible to anyone with a 
working knowledge of the derived category of modules over a ring (e.g.\ from 
the 
book \cite{We}). This is because the methods we use are basically the same; 
there are only slight modifications. The necessary tools to upgrade from 
rings to DG rings (such as K-injective resolutions in place of injective 
resolutions) are recalled in Section \ref{sec:resol} of our paper. We do not 
resort at all to the daunting technicalities of $\mrm{E}_{\infty}$ rings. 
Likewise, we do not touch simplicial methods or Quillen model structures. 

Let us now describe the work in this paper. 
Consider a commutative DG ring $A = \bigoplus_{i \leq 0} A^i$. Its cohomology 
$\opn{H}(A) = \bigoplus_{i \leq 0} \opn{H}^i(A)$ is a commutative 
graded ring. We use the notation $\bar{A} := \opn{H}^0(A)$. There is a 
canonical homomorphism of DG rings $A \to \bar{A}$. 
We say that $A$ is {\em cohomologically pseudo-noetherian} if $\bar{A}$ is a 
noetherian ring, and $\opn{H}^i(A)$ is a finite (i.e.\ finitely generated) 
$\bar{A}$-module for every $i$. (Note that this is weaker than the condition 
that the ring $\opn{H}(A)$ is noetherian.)

The category of DG $A$-modules is denoted by $\cat{C}(A)$. It is a DG 
category, and its derived category, gotten by inverting the 
quasi-isomorphisms, is denoted by $\cat{D}(A)$. There are full triangulated 
subcategories $\cat{D}^{+}(A)$, $\cat{D}^{-}(A)$ and $\cat{D}^{\mrm{b}}(A)$
of $\cat{D}(A)$, made up of the DG modules $M$ with bounded below, 
bounded above and bounded cohomologies, respectively. 
The full subcategory of $\cat{D}(A)$ on the DG modules $M$, whose cohomology 
modules $\opn{H}^i(M)$ are finite over $\bar{A}$, is denoted by
$\cat{D}_{\mrm{f}}(A)$. As usual, for any boundedness condition $\star$ we let 
$\cat{D}^{\star}_{\mrm{f}}(A) := \cat{D}_{\mrm{f}}(A) 
\cap \cat{D}^{\star}(A)$. If $A$ is cohomologically
pseudo-noetherian, then the categories $\cat{D}^{\star}_{\mrm{f}}(A)$ are 
triangulated, and $A \in \cat{D}^{-}_{\mrm{f}}(A)$.
In case $A$ is a ring, then 
$\cat{D}(A) = \cat{D}(\cat{Mod} A)$, the derived category of $A$-modules. 

In Section \ref{sec:resol} we recall some facts on DG modules. We mention 
several kinds of resolutions of DG modules, and special attention is paid to 
semi-free resolutions. 
Section \ref{sec:coh-dim} is about various notions of 
cohomological dimension for DG modules and derived functors.
For instance, in Definition \ref{dfn:11} we introduce the projective and  
injective dimensions of a DG $A$-module $M$ {\em relative to a subcategory}
$\cat{E} \subseteq \cat{D}(A)$. 
In Section \ref{sec:lifting} we study the reduction functor 
$\cat{D}(A) \to \cat{D}(\bar{A})$, 
$M \mapsto \bar{A} \ot^{\mrm{L}}_{A} M$. 
We show that projective $\bar{A}$-modules can be lifted to DG $A$-modules. 

In Section \ref{sec:localiz} we discuss localization of
a commutative DG ring $A$ on $\opn{Spec} \bar{A}$. We introduce the {\em 
\v{C}ech resolution} $\opn{C}(M; \bsym{a})$ of a DG $A$-module $M$,
associated to a {\em covering sequence} 
$\bsym{a} = (a_1, \ldots, a_n)$ of $\bar{A}$. 
In case there is a decomposition 
$\opn{Spec} \bar{A} = \coprod_{i = 1}^n \opn{Spec} \bar{A}_i$
into open-closed subsets, we show that there are canonically defined DG rings 
$A_1, \ldots, A_n$, and a DG ring 
quasi-iso\-morph\-ism $A \to \prod_{i = 1}^n A_i$, that in $\opn{H}^0$ recovers 
the decomposition
$\bar{A} \cong \prod_{i = 1}^n \bar{A}_i$.

The topic of Section \ref{sec:perfect} is {\em perfect} DG modules. 
A DG $A$-module $P$ is called {\em geometrically perfect} if locally on 
$\opn{Spec} \bar{A}$ it is isomorphic, in the derived category, to a finite 
semi-free DG module. See Definition \ref{lem:34} for the precise formulation. 
This definition appears to be completely new for DG rings.
When $A$ is a ring (so that $A = A^0 = \bar{A})$, this definition coincides 
with the one in \cite[Expos\'e I]{SGA-6}, since a finite semi-free DG module 
over a ring is just a bounded complex of finite free modules. 

A DG $A$-module $P$ is called  {\em algebraically perfect} if it can be 
finitely built from $A$ by shifts, direct summands and cones. In other words, 
if $P$ belongs to the epaisse subcategory of $\cat{D}(A)$ classically generated 
by $A$, in the sense of \cite{BV}. This definition (without the qualification 
``algebraically'') was already used in \cite{ABIM}. 

When $A$ is a ring, it is known that geometrically perfect complexes are the 
same as algebraically perfect complexes; see \cite[Expos\'e I]{SGA-6}. 
Therefore they are just called ``perfect complexes''.  
 
Here is the main result Section \ref{sec:perfect}. It is a combination of 
Theorem \ref{thm:50}, Theorem \ref{thm:74} and Corollary \ref{cor:550}.

\begin{thm} \label{thm:63}
Let $A$ be a commutative DG ring, and let $P$ be a DG $A$-module. 
The following four conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i} The DG $A$-module $P$ is geometrically perfect. 

\rmitem{ii} The DG $A$-module $P$ is in $\cat{D}^{-}(A)$, and the DG 
$\bar{A}$-module $\bar{A} \ot^{\mrm{L}}_A P$ is geometrically perfect.

\rmitem{iii} For any $M, N \in \cat{D}(A)$, the canonical morphism 
\[ \opn{RHom}_A(P, M) \ot^{\mrm{L}}_A N \to 
\opn{RHom}_A(P, M \ot^{\mrm{L}}_A N) \]
in $\cat{D}(A)$ is an isomorphism.

\rmitem{iv} The DG $A$-module $P$ is algebraically perfect. 
\end{enumerate}
If $A$ is cohomologically pseudo-noetherian, then the four conditions above are 
equivalent to\tup{:}
\begin{enumerate}
\rmitem{v} The DG $A$-module $P$ is in $\cat{D}^{-}_{\mrm{f}}(A)$,
and it has finite projective dimension relative to $\cat{D}(A)$.
\end{enumerate}
\end{thm}

When $A$ is a commutative ring, conditions (i) and (ii) are essentially the 
same; and (as already mentioned above) the equivalence of conditions 
(i) and (iv) was proved in \cite{SGA-6}. 
But for DG rings this is a new result. In light of Theorem \ref{thm:63} we can 
unambiguously talk about ``perfect DG modules''.  

Section \ref{sec:tilting} is about {\em tilting} DG modules. 
A DG $A$-module $P$ is said to be tilting if there is some DG module
$Q$ such that $P \ot^{\mrm{L}}_A Q \cong A$ in $\cat{D}(A)$. The DG module
$Q$ is called a quasi-inverse of $P$. 
The next theorem is repeated as Theorem \ref{thm:76}.

\begin{thm} \label{thm:420}
Let $A$ be a commutative DG ring, and let $P$ be a DG $A$-module. The following 
four conditions are equivalent\tup{:}
\begin{enumerate}
\rmitem{i}  The DG $A$-module $P$ is tilting .

\rmitem{ii} The functor $P \ot^{\mrm{L}}_A -$ is an equivalence of 
$\cat{D}(A)$.

\rmitem{ii} The functor $\opn{RHom}_A(P, -)$ is an equivalence 
of $\cat{D}(A)$.

\rmitem{iv}  The DG $A$-module $P$ is perfect, and the adjunction 
morphism $A \to \opn{RHom}_A(P, P)$ in $\cat{D}(A)$ is an isomorphism.
\end{enumerate} 
\end{thm}

A combination of Theorems \ref{thm:420} and \ref{thm:63} implies that the 
DG $A$-module $Q := \lb \opn{RHom}_A(P, A)$
is a quasi-inverse of the tilting DG module $P$.

As in \cite{Ye2}, we define the {\em commutative derived Picard group} 
$\opn{DPic}(A)$ to be the group whose elements are the 
isomorphism classes of tilting DG $A$-modules, and the multiplication is 
induced by $- \ot^{\mrm{L}}_A -$.  

If $A \to B$ is a homomorphism of DG rings,  
then the operation $P \mapsto B \ot^{\mrm{L}}_A P$ induces a group homomorphism 
$\opn{DPic}(A) \to \opn{DPic}(B)$.
The next result is Theorem \ref{thm:40} in the body of the paper. 

\begin{thm} \label{thm:60}
Let $A$ be a commutative DG ring. The canonical group homomorphism 
\[ \opn{DPic}(A) \to \opn{DPic}(\bar{A}) \]
is bijective.
\end{thm}

In an earlier version of the paper we had a finiteness condition: we required 
$\opn{Spec} \bar{A}$ to have finitely many connected components. 
But, as noticed by Negron \cite{Ng}, this condition is superfluous.

It is known that the commutative derived Picard group of the ring $\bar{A}$ has 
this structure: 
\[ \opn{DPic}(\bar{A}) \cong 
\opn{Pic}(\bar{A}) \times \opn{F}_{\mrm{lc}}(\opn{Spec} \bar{A}, \Z)  \ . \]
Here $\opn{F}_{\mrm{lc}}(\opn{Spec} \bar{A}, \Z)$
is the group of locally constant functions $\opn{Spec} \bar{A} \to \Z$, and 
$ \opn{Pic}(\bar{A})$ is the usual (commutative) Picard group. See
Theorem \ref{thm:315}, due to Negron, that refines earlier results in 
\cite{Ye2}, \cite{RZ} and \cite {Ye4}.

In Section \ref{sec:dualizing} we talk about {\em dualizing} DG modules. 
Here $A$ is a cohomologically pseudo-noetherian commutative DG ring.
A DG $A$-module $R \in \cat{D}^{+}_{\mrm{f}}(A)$ 
is called dualizing if it has finite injective dimension relative to 
$\cat{D}(A)$, and the adjunction morphism 
$A \to \opn{RHom}_A(R, R)$ is an isomorphism. 
Note that when $A$ is a ring, this is precisely the original definition found 
in \cite{RD}; but for a DG ring there are several possible notions of 
injective dimension, and the correct one has to be used. See  
Definition \ref{dfn:11}(2) and Remark \ref{rem:50}.
Note also that $R$ need not have bounded cohomology -- see 
Corollary \ref{cor:380}  and Example \ref{exa:400}.
For comparisons to dualizing DG modules, as defined previously in \cite{Hi1}, 
\cite{FIJ} and \cite{Lu2}, see Example \ref{exa:113}, Proposition \ref{prop:80}
and Remark \ref{rem:316} respectively.

A DG ring $A$ is called  {\em tractable} if it is cohomologically 
pseudo-noetherian, and there is a homomorphism $\K \to A$ from a finite 
dimensional regular noetherian commutative ring $\K$, such that the induced 
homomorphism $\K \to \bar{A}$ is essentially finite type. Such a homomorphism
$\K \to A$ is called a {\em traction} for $A$. 

The next result is a combination of Theorem \ref{thm:51} and Corollary 
\ref{cor:50}. When $A$ is a ring, this was proved by Grothendieck 
\cite[Sections V.3 and V.10]{RD}.

\begin{thm} \label{thm:90}
Let $A$ be a tractable  commutative DG ring. Then\tup{:}
\begin{enumerate}
\item $A$ has a dualizing DG module. 

\item The operation $(P, R) \mapsto P \ot^{\mrm{L}}_A R$,
for a tilting DG module $P$ and a dualizing DG module $R$, induces a simply 
transitive action of the group $\opn{DPic}(A)$ on the set of isomorphism 
classes of dualizing DG $A$-modules. 
\end{enumerate}
\end{thm}

In particular, if $\bar{A}$ is a local ring, then by Theorems \ref{thm:60} 
and \ref{thm:315} we have \lb $\opn{DPic}(A) \cong \Z$. Thus any two dualizing 
DG $A$-modules $R, R'$ satisfy $R' \cong R[m]$ for an integer $m$. 

A combination of Theorems \ref{thm:60} and \ref{thm:90} yields (see Corollary 
\ref{cor:80}):

\begin{cor}
If $A$ is a tractable commutative DG ring, then the operation 
$R \mapsto \lb \opn{RHom}_A(\bar{A}, R)$ induces a bijection 
\[ \frac{ \{  \tup{dualizing DG} \, A \tup{-modules} \} }
{ \tup{isomorphism} } \iso 
\frac{ \{ \tup{dualizing DG} \, \bar{A} \tup{-modules} \}  }
{ \tup{isomorphism} } . \]
\end{cor}

Here is a result that is quite surprising. It relies 
on a theorem of J{\o}rgensen \cite{Jo}, who proved it in the local case (i.e.\ 
when $\bar{A}$ is a local ring). 

\begin{thm} 
Let $A$ be a cohomologically bounded tractable commutative DG ring. 
If $\bar{A}$ is a perfect DG $A$-module, then the canonical homomorphism 
$A \to \bar{A}$ is a quasi-isomorphism. 
\end{thm}

This is repeated (in slightly stronger form) as Theorem \ref{thm:73} in the 
body of the paper. See Remark \ref{rem:70} for an interpretation of this 
theorem.

Section \ref{sec:cm} of the paper is about {\em Cohen-Macaulay} DG modules.
The definition does not involve regular sequences of course; nor does it 
involve 
vanishing of local cohomologies as in \cite{RD} (even though it could probably 
be stated in this language). Instead we use a fact discovered in \cite{YZ3}: 
for 
a noetherian scheme $X$ with dualizing complex $\RR$, a complex 
$\MM \in \cat{D}^{\mrm{b}}_{\mrm{c}}(\cat{Mod} \OO_X)$ 
is CM (in the sense of \cite{RD}, for the dimension function determined by 
$\RR$) iff $\mrm{R} \Hom_{\OO_X}(\MM, \RR)$ 
is (isomorphic to) a coherent sheaf. 
In \cite{YZ3} the CM complexes inside 
$\cat{D}^{\mrm{b}}_{\mrm{c}}(\cat{Mod} \OO_X)$ 
were also called {\em perverse coherent sheaves}. 

With the explanation above, the next definition makes sense. Let $R$ be a 
dualizing DG $A$-module. A DG module $M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$
is called {\em CM with respect to $R$} if 
$\opn{RHom}_A(M, R) \in \cat{D}^{0}_{\mrm{f}}(A)$.
Here $\cat{D}^{0}_{\mrm{f}}(A)$ is the full subcategory of 
$\cat{D}(A)$ consisting of DG modules with finite cohomology concentrated in 
degree $0$; and we know that it is equivalent to the category 
$\cat{Mod}_{\mrm{f}} \bar{A}$ of finite $\bar{A}$-modules. 

The next theorem is repeated, in slightly greater generality, 
as Theorem \ref{thm:251}.

\begin{thm} \label{thm:61}
Let $f : A \to B$ be a homomorphism between tractable commutative DG rings,
such that $\opn{H}^0(f) : \bar{A} \to \bar{B}$
is surjective. Let $R_B$ be a dualizing DG $B$-module, and let  
$M, N \in \cat{D}^{\mrm{b}}_{\mrm{f}}(B)$. 
\begin{enumerate}
\item If $M$ is CM w.r.t.\ $R_B$, and there is an isomorphism
$\opn{rest}_f(M) \cong \opn{rest}_f(N)$ in $\cat{D}(A)$, then 
$N$ is also CM w.r.t.\ $R_B$. 

\item If $M$ and $N$ are both CM w.r.t.\ $R_B$, then the homomorphism 
\[ \opn{rest}_f : \opn{Hom}_{\cat{D}(B)}(M, N) \to 
\opn{Hom}_{\cat{D}(A)} \bigl( \opn{rest}_f(M), \opn{rest}_f(N) \bigr) \]
is bijective. 
\end{enumerate}
\end{thm}

In the theorem, $\opn{rest}_f : \cat{D}(B) \to \cat{D}(A)$ is the restriction 
functor. As already mentioned, Theorem \ref{thm:61} is needed in \cite{Ye7}.

In our paper \cite{Ye5} we introduce the {\em squaring operation} for 
commutative DG rings. The construction goes like this. The input is a 
homomorphism $A \to B$ of commutative DG rings. To this datum we associate a 
functor $\opn{Sq}_{B / A}$ from $\cat{D}(B)$ to itself. The formula is a bit 
more general than (\ref{eqn:100}): we choose any K-flat DG ring resolution 
$\til{A} \to \til{B}$ of $A \to B$ (see Section \ref{sec:rigid}), and we define 
\begin{equation} \label{eqn:505}
\opn{Sq}_{B / A}(M) 
:= \opn{RHom}_{\til{B} \ot_{\til{A}} \til{B}}(B, M \ot_{\til{A}}^{\mrm{L}} M)
\in \cat{D}(B) . 
\end{equation}
The proof that this definition does not depend on the resolution 
$\til{A} \to \til{B}$ is quite difficult. 

A {\em rigid DG module} over $B$ relative to $A$ is a pair $(M, \rho)$, 
consisting of a DG $B$-module $M$, and a {\em rigidifying isomorphism}
$\rho : M \iso \opn{Sq}_{B / A}(M)$
in $\cat{D}(B)$. There is a notion of rigid morphism between rigid DG modules
(Definition \ref{dfn:501}).  
Here are our results on rigid DG modules. The first is a DG version of
\cite[Theorem 0.2]{YZ1}, and it is repeated as Theorem \ref{thm:501}.

\begin{thm} \label{thm:505}
Let $A \to B$ be a homomorphism of commutative DG rings, and let 
$(M, \rho)$ be a rigid DG module over $B$ relative to $A$. Assume that the 
adjunction morphism $B \to \opn{RHom}_{B}(M, M)$ in $\cat{D}(B)$
is an isomorphism. Then the only rigid automorphism of $(M, \rho)$ is the 
identity. 
\end{thm}

Next is a DG version of the uniqueness in
\cite[Theorem 1.1]{YZ2}(1). It is repeated as Theorem \ref{thm:502}.

\begin{thm} \label{thm:506}
Let $A$ be a tractable  commutative DG ring, with traction $\K \to A$.  
Suppose  $(R, \rho)$ and $(R', \rho')$ are rigid dualizing DG modules over $A$ 
relative to $\K$. Then there is a unique rigid isomorphism 
$(R, \rho) \cong (R', \rho')$.
\end{thm}

Thus we can call $(R, \rho)$ {\em the} rigid dualizing DG module of $A$ 
relative to $\K$. 

\begin{conj} \label{conj:505}
In the situation of Theorem \tup{\ref{thm:506}}, the rigid dualizing 
DG module over $A$ relative to $\K$ exists.
\end{conj}

Indeed, we give more detailed conjectures in Section \ref{sec:rigid}, that 
would imply Conjecture \ref{conj:505}. When $A$ is a ring, these assertions 
were already proved in \cite{YZ1} (with some corrections in \cite{Ye7}).
In case $A$ has bounded cohomology, Conjecture \ref{conj:505} was very recently 
proved by Shaul \cite{Sh2}. 

We end the Introduction with another conjecture on rigid DG modules. 

\begin{conj} \label{conj:506}
In the situation of Theorem \tup{\ref{thm:506}}, let $(M, \rho)$
be a rigid DG module over $A$ relative to $\K$. Assume that 
$M \in \cat{D}^+_{\mrm{f}}(A)$, and that $M$ is nonzero on each connected 
component of $\opn{Spec} \bar{A}$. Then $M$ is a dualizing DG $A$-module. 
\end{conj}

When $A$ is a ring and 
$M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$, this was proved in \cite{YZ2} 
and \cite{AIL}. More on this conjecture in Remark \ref{rem:520}. 


\medskip \noindent
{\bf Acknowledgments}. 
I wish to thank Peter J{\o}rgensen, Bernhard Keller, Vladimir Hinich,
Liran Shaul, James Zhang, Amnon Neeman, Dennis Gaitsgory, 
Rishi Vyas, Matan Prasma, Jacob Lurie, Benjamin Antieau, John Palmieri, 
Pieter Belmans, \lb Michel Vaqui\'e, Joseph Lipman, Srikanth Iyengar and Cris 
Negron for helpful discussions.
