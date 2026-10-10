---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-12
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.603
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
\numberwithin{equation}{subsection}

\subsection{Background: Rigid Dualizing Complexes}
The concept of {\em rigid dualizing complex} was introduced by M. Van den Bergh 
in his influential paper \cite{VdB} from 1997. This was done for a 
noncommutative ring $A$ 
over a base field $\K$. Let us recall the definition; but to simplify matters 
(and because here we are interested in the commutative situation), we 
shall state it for a commutative ring $A$.

So let $\K$ be a field and $A$ a commutative $\K$-ring. We denote by 
$\cat{D}(A)$ the derived category of $A$-modules. Given a complex 
$M \in \cat{D}(A)$, its {\em square} is the complex 
\begin{equation} \label{eqn:490}
\opn{Sq}_{A / \K}(M) := 
\opn{RHom}_{A \ot_{\K} A}(A, M \ot_{\K} M) \in \cat{D}(A) .
\end{equation}
The $A$-module structure on $\opn{Sq}_{A / \K}(M)$ comes from the first 
argument of $\opn{RHom}$. 
Note that if $M$ is a single module, then 
\[ \opn{H}^q \bigl( \opn{Sq}_{A / \K}(M) \bigr) = 
\opn{HH}^q(A, M \ot_{\K} M) , \]
the $q$-th Hochschild cohomology of the $A$-bimodule $M \ot_{\K} M$.

Now assume $A$ is finitely generated over $\K$ (and hence it is noetherian). A 
{\em rigid dualizing complex} over $A$ relative 
to $\K$ is a pair $(R, \rho)$, where $R \in \cat{D}(A)$ is a dualizing complex 
(in the sense of \cite{RD}), and 
\begin{equation} \label{eqn:499}
\rho : R \iso \opn{Sq}_{A / \K}(R) 
\end{equation}
is an isomorphism in $\cat{D}(A)$. 
Van den Bergh proved that a rigid dualizing complex $(R, \rho)$ exists, and 
it is unique up to isomorphism. Further work in this direction was done 
by J.J. Zhang and the author in a series of papers; see \cite{YZ1} and its 
references. (These papers dealt with the noncommutative 
situation, which is significantly more complicated.) 

In the current paper we are interested in {\em commutative rings}, but in a 
{\em relative situation}: instead of a base field $\K$, we have a homomorphism 
$A \to B$ of commutative rings, and we want to produce a useful theory of 
squaring and rigidity. 

If the homomorphism $A \to B$ is {\em flat}, then there is a pretty easy way to 
generalize (\ref{eqn:490}), as follows. Given a complex $M \in \cat{D}(B)$, we 
may define 
\begin{equation} \label{eqn:491}
\opn{Sq}_{B / A}(M) := 
\opn{RHom}_{B \ot_A B}(B, M \ot^{\mrm{L}}_A M) \in \cat{D}(B) . 
\end{equation}
However, when $A \to B$ is not flat, formula (\ref{eqn:491})  is 
meaningless, since  there is no way to interpret $M \ot^{\mrm{L}}_A M$ as an 
object of $\cat{D}(B \ot_A B)$~!

In our paper with Zhang \cite{YZ2}, we proposed to solve the flatness problem 
by replacing the ring $B$ with a {\em flat DG ring resolution} $\til{B} \to B$ 
over $A$. Further work on rigid dualizing complexes over commutative rings was 
done in the paper \cite{YZ3}, and more is outlined in the survey paper 
\cite{Ye1}. 

There is work in progress (\cite{Ye6} 
and \cite{Ye7}) about rigid dualizing on schemes and Deligne-Mumford stacks. 
Indeed, the rigid approach to Grothendieck duality allows, for the first time, 
to state and prove global duality for a proper map between DM stacks. 
The ideas are outlined in the lecture notes \cite{Ye3}. 

Unfortunately, there were {\em serious flaws in the proofs in \cite{YZ2}}, 
as explained in Subsection \ref{subsec:discussion} of the Introduction. 
The discovery of these flaws forced us to go back and repair the foundations. 
Thus, {\em in the present paper we provide a comprehensive and correct 
treatment of the squaring operation}, using the DG ring method. 
The companion paper \cite{Ye5} is destined to repair further problems in 
\cite{YZ2}, and to enhance the results of \cite{YZ3}. 

Once the repairs to the foundations are done, we intend to proceed with the 
geometric application of rigid dualizing complexes (namely the papers in 
progress \cite{Ye6} and \cite{Ye7}).



\subsection{DG Rings and their Resolutions} \label{subsec:DGR-res}
Let $A = \bigoplus_{i \in \Z} A^i$ be a DG ring, where as usual ``DG'' is short 
for ``differential graded''. (Most other texts would call $A$ a unital 
associative DG algebra over $\Z$; see Remark \ref{rem:1025} for a discussion 
of nomenclature.) We say that $A$ is {\em nonpositive} if  
$A^i = 0$ for $i > 0$. The DG ring $A$ is called {\em strongly commutative} if 
$a \cd b = (-1)^{i  j} \cd b \cd a$ for $a \in A^i$ and $b \in A^j$, and 
$a \cd a = 0$ if $i$ is odd. 
We call $A$ a {\em commutative DG ring} if it is both nonpositive and strongly 
commutative. This is the term appearing in the title of the paper. 

We denote by $\cat{DGR}_{\mrm{sc}}^{\leq 0}$ the category of commutative 
DG rings. Observe that the category of commutative rings is a full subcategory 
of $\cat{DGR}_{\mrm{sc}}^{\leq 0}$, since a ring 
can be seen as a DG ring concentrated in degree $0$. 
All DG rings appearing in the Introduction are commutative (with the 
exception of Subsections \ref{subsec:proofs} and \ref{subsec:discussion}). 
However, in the paper itself we must deal with noncommutative DG rings, as 
explained in Subsection  \ref{subsec:proofs}.

Even though our motivation is the squaring operation for commutative rings, 
we develop the squaring operation more generally for commutative DG rings, 
and this is the way we shall present the results in the Introduction. 
The reason is twofold: first, there is no added difficulty in working with 
commutative DG rings (as compared to commutative rings); and second, the 
presentation is cleaner when working totally in the commutative DG framework. 

Let $A \xar{u} B$ be a homomorphism of commutative DG rings, i.e.\ a morphism 
in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$. We refer to $A \xar{u} B$ as a {\em pair of 
commutative DG rings}, with notation $B / A$. These pairs form a category: 
given another pair 
$B' / A' = (A' \xar{u'} B')$, a morphism of pairs 
$w / v : B' / A' \to B / A$
is a commutative diagram 
\begin{equation} \label{eqn:985}
\UseTips \xymatrix @C=6ex @R=6ex {
A'
\ar[r]^{u'}
\ar[d]_{v}
&
B'
\ar[d]^{w}
\\
A
\ar[r]^{u}
&
B
} 
\end{equation}
in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$.
The resulting category is denoted by 
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$.

Consider a pair $B / A$ in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$.
A {\em K-flat resolution} of $B / A$ is a morphism 
$s / r : \til{B} / \til{A} \to B / A$
in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, such that $\til{B}$ is K-flat as a DG 
$\til{A}$-module, $r : \til{A} \to A$ is a quasi-isomorphism, and 
$s : \til{B} \to B$ is a surjective quasi-isomorphism.
(See Section \ref{sec:resolutions-modules} for a review of various kinds of DG 
module resolutions, including K-flat ones.) 

\begin{equation} \label{eqn:482}
\UseTips \xymatrix @C=8ex @R=6ex {
\til{A}
\ar[r]^{\til{u}} ="tilu"
\ar[d]_{r} ="v"
{} \save 
[]+<-12ex,-1ex> *+[F-:<3pt>]{\scriptstyle \text{qu-isom}} 
\ar@(r,l)@{..} "v" 
\restore
&
\til{B}
\ar[d]^{s} ="w"
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
}
\end{equation}

Let $w / v : B' / A' \to B / A$
be a morphism in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$. A K-flat resolution of 
$w / v$ is a commutative diagram
\begin{equation} \label{eqn:986}
\UseTips \xymatrix @C=8ex @R=6ex {
\til{B}' / \til{A}'
\ar[r]^{\til{w} / \til{v}}
\ar[d]_{s' / r'}
&
\til{B} / \til{A}
\ar[d]^{s / r}
\\
B' / A'
\ar[r]^{w / v}
&
B / A
}
\end{equation}
in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, where the vertical arrows $s / r$ and 
$s' / r'$ are K-flat resolutions.
We also say that $\til{w} / \til{v}$ is a morphism of resolutions above 
$w / v$. In case $B' / A' = B / A$, and  
$w / v$ is the identity automorphism of this pair, 
we say that $\til{w} / \til{v}$ is a morphism of resolutions of $B / A$. 
According to Proposition \ref{prop:1010}, 
K-flat resolutions of pairs, and of morphisms between pairs, exist. 

Let $A  \xar{u} B \xar{v} C$ be homomorphisms in 
$\cat{DGR}_{\mrm{sc}}^{\leq 0}$.
We refer to this data as a {\em triple of commutative DG rings}. 
A K-flat resolution of this triple is a commutative diagram 
\begin{equation} \label{eqn:966}
\UseTips \xymatrix @C=6ex @R=6ex {
\til{A}
\ar[r]^{\til{u}}
\ar[d]^{r}
&
\til{B}
\ar[d]^{s}
\ar[r]^{\til{v}}
&
\til{C}
\ar[d]^{t}
\\
A
\ar[r]^{u}
&
B
\ar[r]^{v}
&
C
} 
\end{equation}
in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$,
such that 
$\til{B} / \til{A}$ is a K-flat resolution of the pair $B / A$, and 
$\til{C} / \til{A}$ is a K-flat resolution of the pair $C / A$.
The first triple above can be viewed as a morphism of pairs 
$v / \mrm{id}_A : B / A \to C / A$; and 
$\til{v} / \mrm{id}_{\til{A}} : \til{B} / \til{A}  \to \til{C} / \til{A}$
can be viewed as a K-flat resolution of $v / \mrm{id}_A$. 
Such resolutions exist by Proposition \ref{prop:1011}.


\subsection{The Squaring Operation} \label{subsec:squaring}
Recall that our DG rings are all commutative. 
To a DG ring $A$ we associate the category of DG $A$-modules 
$\cat{M}(A)$, and its derived category $\cat{D}(A)$. There is an additive 
functor $\opn{Q} : \cat{M}(A) \to  \cat{D}(A)$, which is the identity on 
objects, and which sends quasi-isomorphisms to isomorphisms. 
In Sections \ref{sec:facts-DG-mods} and \ref{sec:resolutions-modules} we recall 
some facts about DG modules, their resolutions, and related derived functors.

Let $A \xar{u} B$ be a homomorphism of DG rings, namely an object $B / A$ of 
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$. 
Given a DG $B$-module $M$, and a K-flat resolution 
$\til{B} / \til{A}$ of $B / A$, 
we let 
\begin{equation} \label{eqn:815}
\opn{Sq}_{B / A}^{\til{B} / \til{A}} (M) := 
\opn{RHom}_{\til{B} \ot_{\til{A}} \til{B}}(B, M \ot_{\til{A}}^{\mrm{L}} M)
\in \cat{D}(B) . 
\end{equation}
In Proposition \ref{prop:915} and Definition \ref{dfn:950} we provide an 
explicit presentation of \lb 
$\opn{Sq}_{B / A}^{\til{B} / \til{A}} (M)$, 
in terms of {\em compound resolutions}. 
See Remark \ref{rem:965} regarding symmetric compound resolutions.  

Consider a morphism of pairs 
$w / v : B' / A' \to B / A$, a DG module $M \in \cat{D}(B)$, a DG module
$M' \in \cat{D}(B')$, and a morphism 
$\th : M \to M'$ in $\cat{D}(B')$.
Clarification: actually $\th$ is a morphism $\opn{For}_w(M) \to M'$, where 
$\opn{For}_w : \cat{D}(B) \to \cat{D}(B')$
is the forgetful functor (restriction of scalars) corresponding to the DG ring 
homomorphism $w : B' \to B$. However, most of the time 
we shall suppress these forgetful functors, for the sake of clarity. 

Given a K-flat resolution
$\til{w} / \til{v} : \til{B}' / \til{A}' \to \til{B} / \til{A}$
of $w / v$, there is a morphism
\begin{equation} \label{eqn:961}
\opn{Sq}_{w / v}^{\til{w} / \til{v}} (\th) : 
\opn{Sq}_{B / A}^{\til{B} / \til{A}} (M) \to
\opn{Sq}_{B' / A'}^{\til{B}' / \til{A}'} (M')
\end{equation}
in $\cat{D}(B')$. The morphism 
$\opn{Sq}_{w / v}^{\til{w} / \til{v}} (\th)$
is constructed using compound resolutions -- see Proposition \ref{prop:916} and 
Definition \ref{dfn:956}. 
This construction is functorial in all arguments. 
By this we mean that if
$w' / v' : B'' / A'' \to B' / A'$
is another morphism in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
with K-flat resolution 
$\til{w}' / \til{v}' : \til{B}'' / \til{A}'' \to \til{B}' / \til{A}'$, 
and if $\th' : M' \to M''$
is a morphism in $\cat{D}(B'')$, then 
\[ \opn{Sq}_{(w / v) \circ (w' / v')}^{(\til{w} / \til{v}) \circ 
(\til{w}' / \til{v}')} (\th' \circ \th) = 
\opn{Sq}_{w' / v'}^{\til{w}' / \til{v}'} (\th') \circ
\opn{Sq}_{w / v}^{\til{w} / \til{v}} (\th) , \]
as morphisms 
\[ \opn{Sq}_{B / A}^{\til{B} / \til{A}} (M) \to
\opn{Sq}_{B'' / A''}^{\til{B}'' / \til{A}''} (M'') \]
in $\cat{D}(B'')$. See Proposition \ref{prop:940}. 

Here is the key technical result of our paper. It is repeated as Theorem 
\ref{thm:950} in the body of the paper, and proved there. 
A brief discussion of the proof can be found in Subsection \ref{subsec:proofs} 
of the Introduction. 

\begin{thm}[Homotopy Invariance] \label{thm:960}
Let $w / v : B' / A' \to B / A$ be a morphism in  
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, let 
$M \in \cat{D}(B)$, let $M' \in \cat{D}(B')$, and let 
$\th : M \to M'$ be a morphism in $\cat{D}(B')$.
Suppose
$\til{B} / \til{A}$ and $\til{B}' / \til{A}'$
are K-flat resolutions of 
$B / A$ and $B' / A'$ respectively in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
and  
\[ \til{w}_0 / \til{v}_0,  \, \til{w}_1 / \til{v}_1 :
\til{B}' / \til{A}' \to \til{B} / \til{A} \]
are morphisms of resolutions above $w / v$. Then the morphisms 
\[ \opn{Sq}_{w / v}^{\til{w}_0 / \til{v}_0}(\th), \,
\opn{Sq}_{w / v}^{\til{w}_1 / \til{v}_1}(\th) :
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \to 
\opn{Sq}_{B' / A'}^{\til{B}' / \til{A}'}(M') \]
in $\cat{D}(B')$ are equal. 
\end{thm}

Here is the first main theorem of our paper. 

\begin{thm}[Existence of Squares] \label{thm:965}
Let $A \to B$ be a homomorphism of commutative DG rings,
and let $M$ be a DG $B$-module. There is a DG $B$-module 
$\opn{Sq}_{B / A}(M)$, 
unique up to a unique isomorphism in $\cat{D}(B)$, together with 
an isomorphism
\[ \opn{sq}^{\til{B} / \til{A}} : 
\opn{Sq}_{B / A}(M) \iso \opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \]
in $\cat{D}(B)$ for any K-flat resolution 
$\til{B} / \til{A}$ of $B / A$, 
satisfying the following condition. 
\begin{enumerate}
\item[($*$)] For any morphism 
$\til{w} / \til{v} : \til{B}' / \til{A}' \to \til{B} / \til{A}$
of resolutions of $B / A$, the diagram 
\[ \UseTips \xymatrix @C=18ex @R=8ex {
\opn{Sq}_{B / A}(M)
\ar[d]_{ \opn{sq}^{\til{B} / \til{A}} }
\ar[dr]^{ \opn{sq}^{\til{B}' / \til{A}'} }
\\
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M)
\ar[r]_{ \opn{Sq}_{\mrm{id} / \mrm{id}}^{\til{w} / \til{v}}(\mrm{id}_M) }
&
\opn{Sq}_{B / A}^{\til{B}' / \til{A}'}(M)
} \]
of isomorphisms in $\cat{D}(B)$ is commutative. 
\end{enumerate}
\end{thm}

The DG module $\opn{Sq}_{B / A}(M)$ is called the {\em square of $M$ over $B$ 
relative to $A$}. 

This theorem is repeated as Theorem \ref{thm:860} in the body of the paper. 
As we already mentioned, this assertion (for rings only, not DG rings) appeared 
as \cite[Theorem 2.2]{YZ2}; but the proof there had a large gap in it. 
For a discussion, and a comparison to \cite[Theorem 3.2]{AILN}, see
Subsection \ref{subsec:discussion} below. 


Here is the second main theorem of the paper. 

\begin{thm}[Trace Functoriality] \label{thm:966}
Let $A \to B \xar{v} C$ 
be homomorphisms of commutative DG rings, 
let $M \in \cat{D}(B)$, let $N \in \cat{D}(C)$, and let 
$\th : N \to M$ be a morphism in $\cat{D}(B)$.
There is a unique morphism 
\[ \opn{Sq}_{v / \mrm{id}_A}(\th) :
\opn{Sq}_{C / A}(N) \to \opn{Sq}_{B / A}(M) \]
in $\cat{D}(B)$, satisfying the condition\tup{:}
\begin{enumerate}
\item[($**$)] For any K-flat resolution
$\til{A} \to \til{B} \xar{\til{v}} \til{C}$
of the triple $A \to B \xar{v} C$, the diagram 
\[ \UseTips \xymatrix @C=14ex @R=8ex {
\opn{Sq}_{C / A}(N)
\ar[d]_{ \opn{sq}^{\til{C} / \til{A}} }
\ar[r]^(0.5){ \opn{Sq}_{v / \mrm{id}}(\th) }
&
\opn{Sq}_{B / A}(M) 
\ar[d]^{ \opn{sq}^{\til{B} / \til{A}} }
\\
\opn{Sq}_{C / A}^{\til{C} / \til{A}}(N)
\ar[r]^(0.5){ \opn{Sq}_{v / \mrm{id}}^{\til{v} / \mrm{id}}(\th) }
&
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) 
} \]
in $\cat{D}(B)$ is commutative. 
\end{enumerate}
\end{thm}

This theorem is repeated as Theorem \ref{thm:871}. The statement already 
appeared as \cite[Theorem 2.3]{YZ2} (for rings only, not DG rings). But the 
proof in loc.\ cit.\ was also incorrect. 

The known functoriality of the operation 
$\opn{Sq}_{B / A}^{\til{B} / \til{A}}$
(from Section \ref{sec:pairs-DG-modules}) now implies that the assignments 
$M \mapsto \opn{Sq}_{B / A}(M)$ and
$\th \mapsto \opn{Sq}_{\mrm{id}_B / \mrm{id}_A}(\th)$
are a functor 
\[ \opn{Sq}_{B / A} : \cat{D}(B) \to  \cat{D}(B) , \]
called the {\em squaring operation  over $B$ relative to $A$}. 

The functor $\opn{Sq}_{B / A}$ is not linear; in fact it is a 
{\em quadratic functor}, in the following sense. Given a morphism 
$\th : N \to M$ in $\cat{D}(B)$ and an element 
$b \in \opn{H}^0(B)$, we have 
\[ \opn{Sq}_{B / A}(b \cd \th) = b^2 \cd \opn{Sq}_{B / A}(\th) , \]
as morphisms 
$\opn{Sq}_{B / A}(N) \to \opn{Sq}_{B / A}(M)$ 
in $\cat{D}(B)$. See Theorem \ref{thm:1010} for a slightly more general 
statement. 




\subsection{On the Proofs} \label{subsec:proofs}
Theorems \ref{thm:965} and \ref{thm:966} are rather easy to prove, once we know 
Theorem \ref{thm:960} (and the existence of resolutions). 

However, the proof of Theorem \ref{thm:960} is quite long and difficult. 
As its name suggests, it involves a homotopy between the homomorphisms 
$\til{w}_0, \til{w}_1 : \til{B}' \to \til{B}$.
The only way we know to produce a homotopy 
$\til{w}_0 \twoto \til{w}_1$ is when the DG ring $\til{B}'$ is 
{\em noncommutative semi-free} over $\til{A}'$, and there is equality 
$\til{v}_0 = \til{v}_1$.  See Definition \ref{dfn:70} and 
Theorem \ref{thm:300}.

We are thus forced to deal with {\em noncommutative DG rings}. 
Instead of the pairs of commutative DG rings that were discussed above, 
the relevant noncommutative object is a {\em central pair of DG rings}, namely a 
central homomorphism $u : A \to B$ with commutative source $A$. See 
Definitions \ref{dfn:750} and \ref{dfn:910}. 

Let $B / A$ be a central pair of DG rings. A K-flat resolution of it is a 
central pair of DG rings $\til{B} / \til{A}$, such that $\til{B}$ is a K-flat 
DG $\til{A}$-module, together with a quasi-isomorphism 
$\til{B} / \til{A} \to B / A$
as in diagram (\ref{eqn:482}).
Now $B$ is a DG bimodule over 
$\til{B}$, namely it is a DG module over the {\em enveloping DG ring}
$\til{B} \ot_{\til{A}} \til{B}^{\mrm{op}}$. 
Because of this, we must replace the single DG module $M$ by a pair 
$(M^{\mrm{l}}, M^{\mrm{r}})$, consisting of a left DG $B$-module 
$M^{\mrm{l}}$ and a right DG $B$-module $M^{\mrm{r}}$.
In this situation, instead of a ``square'' we have a ``rectangle'':
\begin{equation} \label{eqn:965}
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})  := 
\opn{RHom}_{ \til{B} \ot_{\til{A}} \til{B}^{\mrm{op}} }
(B, M^{\mrm{l}} \ot^{\mrm{L}}_{\til{A}} M^{\mrm{r}}) . 
\end{equation}
This object lives in the derived category 
$\cat{D}(B^{\mrm{ce}})$, where $B^{\mrm{ce}}$ is the {\em center} of $B$ (in 
the graded sense, see Definition \ref{dfn:750}). 

In the noncommutative situation, the Homotopy Theorem (the noncommutative 
version of Theorem \ref{thm:960}) is Theorem \ref{thm:840}.
It is proved in two stages. First, an important special case 
($\til{B}' / \til{A}'$ is noncommutative semi-free and $\til{v}_0 = \til{v}_1$) 
is done in Lemma \ref{lem:827}. The proof of this 
lemma relies on Theorem \ref{thm:300}, and uses the cylinder DG ring. 
The general case is then reduced to that special case.
Theorem \ref{thm:985} (Existence of Rectangles) is the noncommutative version 
of Theorem \ref{thm:965}. 

The rectangle operation is interesting on its own, even when $B / A$ is a 
commutative pair of rings. This is due to its connection with the monoidal 
operation $\ot^!$. See Remark \ref{rem:720}. 


\subsection{Discussion of Related Papers} \label{subsec:discussion}
Early versions of Theorems \ref{thm:965} and \ref{thm:966} had already appeared 
in our paper \cite{YZ2} with Zhang, as Theorems 2.2 and 2.3 respectively. 
However, to our great embarrassment, the proofs of these results in \cite{YZ2} 
had severe gaps in them. The gaps are well-hidden in the text; but one clear 
error is this: the homomorphism 
$\sbmat{\phi_0 & 0 \\ 0 & \phi_1}$
in the middle of page 3225 (in the proof  of Theorem 2.2) does not make any 
sense (unless $\phi_0 = \phi_1$). In order to give a correct treatment, it is 
necessary to work with noncommutative semi-free DG ring resolutions, as 
explained in Subsection \ref{subsec:proofs} above. 

The mistake in the proof of \cite[Theorem 2.2]{YZ2} was discovered by Avramov, 
Iyengar, Lipman and Nayak \cite{AILN}. They also found a way to fix it, and 
their \cite[Theorem 3.2]{AILN} is a generalization of our 
\cite[Theorem 2.2]{YZ2}. Indeed, \cite[Theorem 3.2]{AILN} establishes the 
rectangle operation in the case when $A \to B$ is a central pair of rings. 
The proof of \cite[Theorem 3.2]{AILN} relies on the Quillen 
model structure on the category $\cat{DGR} \centover A$ of noncommutative DG 
rings, central over a commutative base ring $A$, following \cite{BP}. 
More on this aspect can be found in Remark \ref{rem:780}.
Note that our Theorem \ref{thm:840} (the noncommutative version of Theorem 
\ref{thm:965}) is stronger than \cite[Theorem 3.2]{AILN}, because we allow $A 
\to B$ be a central pair of nonpositive DG rings. 

Our goals are different from those of \cite{AILN}, and hence we adopt a 
different strategy. For us the relative situation of a homomorphism of 
commutative rings $A \to B$ is crucial, and we must consider triples of 
commutative rings $A \to B \to C$. For this reason we stick to commutative 
K-flat DG ring resolutions, relying on Theorem \ref{thm:960}. 
We do not know whether the methods of \cite{AILN}
can be adapted to yield the trace functoriality of the squaring operation 
(Theorem \ref{thm:966}). 
 

\medskip \noindent
{\em Acknowledgments}. 
I wish to thank James Zhang,  Bernhard Keller, Vladimir Hinich, 
Liran Shaul, Rishi Vyas, Asaf Yekutieli and Sharon Hollander for their help in 
writing this paper.
