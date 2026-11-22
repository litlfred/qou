---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-7
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.591
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS — Let A →B be a homomorphism of commutative rings."
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
