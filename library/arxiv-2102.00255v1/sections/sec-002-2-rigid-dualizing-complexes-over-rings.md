---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-002-2-rigid-dualizing-complexes-over-rings
section_title: "Rigid Dualizing Complexes over Rings"
section_number: 2
pages: 6-9
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.977
doc_brief: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS — In this article we explain the theory of rigid residue complexes in commutative algebra and algebraic geometry, summarizing the"
---
\label{sec:RRD-rings}
 
Again $\K$ is a regular base ring, and $A$ is an EFT $\K$-ring. 
The next definition is taken from \cite{RD}, except that the derived Morita 
property (Definition \ref{dfn:232}) had not yet been introduced when 
\cite{RD} was written. 

\begin{dfn} \label{dfn:240}
A complex $R \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$
is called {\em dualizing} if it has finite injective dimension and 
the derived Morita property.
\end{dfn}

\begin{dfn}[\cite{VdB}, \cite{YZ2}, \cite{Ye7}, \cite{OSY}] \label{dfn:241}
A {\em rigid dualizing complex} over $A$ relative to $\K$ is a rigid 
complex $(R, \rho)$, as in Definition \ref{dfn:230}, such that $R$ is a 
dualizing complex. 
\end{dfn}

\begin{thm}[{\cite{VdB}, \cite{YZ2}, \cite{OSY}}] \label{thm:120}
Let $A$ be an EFT $\K$-ring. The ring $A$ has a rigid dualizing complex 
$(R_A, \rho_A)$, and it is unique, up to a unique isomorphism in 
$\cat{D}(A)_{\mrm{rig} / \K}$. 
\end{thm}

The uniqueness part of this theorem is a combination of a result of 
Grothendieck (see \cite[Theorem V.3.1]{RD} or \cite[Theorem 13.1.35]{Ye7}), 
with a variation of Theorem \ref{thm:233} (see \cite[Theorem 13.5.4]{Ye7}).
Existence is much harder. The strategy of proof in \cite{OSY} is this: we
factor the structure homomorphism $u : \K \to A$ into 
$u = u_{\mrm{loc}} \circ u_{\mrm{fin}} \circ u_{\mrm{pl}}$,
where $u_{\mrm{pl}} : \K \to A_{\mrm{pl}}$ is a homomorphism to a polynomial 
ring over $\K$; 
$u_{\mrm{fin}} : A_{\mrm{pl}} \to A_{\mrm{ft}}$ is a surjection;
and $u_{\mrm{loc}} : A_{\mrm{ft}} \to A$ is a localization homomorphism. 
Then we show that the dualizing complexes $R_{\mrm{pl}}$,  $R_{\mrm{ft}}$ and 
$R$, over the rings $A_{\mrm{pl}}$,  $A_{\mrm{ft}}$ and $A$ respectively, that 
are constructed in the course of the proof of \cite[Theorem 13.1.34]{Ye7}, are 
all rigid. This is achieved using {\em induced rigidity} for essentially smooth 
ring homomorphisms, and {\em coinduced rigidity} for finite ring homomorphisms. 

\begin{thm}[\cite{YZ2}, \cite{OSY}] \label{thm:241} 
Let $u : A \to B$ be a finite ring homomorphism.
There exists a unique nondegenerate rigid backward morphism
\[ \opn{tr}^{\mrm{rig}}_u : (R_B, \rho_B) \to (R_A, \rho_A) \]
in $\cat{D}(A)$ over $u$, called the {\em rigid trace morphism}.
\end{thm}

\begin{cor}[\cite{YZ2}, \cite{OSY}] \label{cor:241}
Let $A \xar{u} B \xar{v} C$ be finite ring homomorphisms. Then 
$\opn{tr}^{\mrm{rig}}_u \circ \opn{tr}^{\mrm{rig}}_v = 
\opn{tr}^{\mrm{rig}}_{v \circ u}$, as backward morphisms 
$R_C \to R_A$ in $\cat{D}(A)$ over $v \circ u$.
\end{cor}

\begin{thm}[\cite{YZ2}, \cite{OSY}] \label{thm:242} 
Let $v : A \to A'$ be an essentially \'etale ring homomorphism.
There exists a unique nondegenerate rigid forward morphism
\[ \opn{q}^{\mrm{rig}}_v : (R_A, \rho_A) \to (R_{A'}, \rho_{A'}) \]
in $\cat{D}(A)$ over $v$, called the {\em rigid \'etale-localization morphism}.
\end{thm}

\begin{cor}[\cite{YZ2}, \cite{OSY}] \label{cor:242}
Let $A \xar{v} A' \xar{v'} A''$ be essentially \'etale ring homomorphisms.
Then $\opn{q}^{\mrm{rig}}_{v'} \circ \opn{q}^{\mrm{rig}}_v = 
\opn{q}^{\mrm{rig}}_{v' \circ v}$, as forward morphisms 
$R_A \to R_{A''}$ in $\cat{D}(A)$ over $v' \circ v$.
\end{cor}

\begin{thm}[\cite{YZ2}, \cite{OSY}] \label{thm:240} 
Suppose $u : A \to  B$ and $v : A \to  A'$ are ring homomorphisms, with $u$
finite and $v$ essentially \'etale. Define the ring $B' := A' \ot_A B$.
We get the following commutative diagram
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
} \]
in $\cat{Rng} \eftover \K$, in which $u'$ is finite and $w$ is essentially 
\'etale. Then the diagram  
\[ \UseTips \xymatrix @C=10ex @R=6ex {
R_A
\ar[d]_{\opn{q}^{\mrm{rig}}_{v}}
&
R_B
\ar[l]_{\opn{tr}^{\mrm{rig}}_u}
\ar[d]^{\opn{q}^{\mrm{rig}}_{w}}
\\
R_{A'}
&
R_{B'}
\ar[l]_{\opn{tr}^{\mrm{rig}}_{u'}}
} \]
in $\cat{D}(A)$ is commutative. 
\end{thm}

For a ring $A$ with rigid dualizing complex $(R_A, \rho_A)$, let us define the 
{\em rigid auto-duality functor}
\begin{equation} \label{eqn:130}
\opn{D}^{\mrm{rig}}_A := \opn{RHom}_{A}(-, R_A) : \cat{D}(A) \to \cat{D}(A) . 
\end{equation}
According to \cite{RD}, or \cite[Chapter 13]{Ye7}, the functor 
$\opn{D}^{\mrm{rig}}_A$ induces an equivalence
$\opn{D}^{\mrm{rig}}_A : \cat{D}^{\star}_{\mrm{f}}(A)^{\mrm{op}} \to 
\cat{D}^{-\star}_{\mrm{f}}(A)$,
where $\star$ and $-\star$ are reverse boundedness conditions. 
In particular there is the {\em evaluation isomorphism} 
\begin{equation} \label{eqn:245}
\opn{ev} : \opn{Id} \iso \opn{D}^{\mrm{rig}}_A \circ \opn{D}^{\mrm{rig}}_A 
\end{equation}
of triangulated functors from $\cat{D}^{+}_{\mrm{f}}(A)$ to itself.

The next discussion involves {\em $2$-categories} and {\em pseudofunctors}.
The only textbook reference for $2$-categories seems to be in 
\cite[Chapter XII]{Mc}. There is a brief discussion of $2$-categories and 
pseudofunctors in 
\cite[Section \href{https://stacks.math.columbia.edu/tag/003G}
{\tt tag=003G}]{SP}, 
and a summary of $2$-categorical notation in Section 8.1 of 
our book \cite{Ye7}. A detailed exposition of $2$-categories and pseudofunctors
can be found in Sections 1-2 of our paper \cite{Ye4}. We should stress that our 
$2$-categories are strict, and our pseudofunctors are normalized. 
 
Recall that to a ring homomorphism $u : A \to B$ we can associate the {\em 
derived induction functor}
\begin{equation} \label{eqn:220}
\mrm{LInd}_u  := B \ot^{\mrm{L}}_{A} (-) : \cat{D}^{-}_{\mrm{f}}(A) \to
\cat{D}^{-}_{\mrm{f}}(B)  . 
\end{equation}
It is the left derived functor of the {\em induction functor} 
$\mrm{Ind}_u  := B \ot_{A} (-) : \cat{M}(A) \to \cat{M}(B)$.

Consider the $2$-category of $\K$-linear triangulated categories, which we 
denote by \lb $\cat{TrCat} \over \K$.
Derived induction is actually a pseudofunctor
\begin{equation} \label{eqn:221}
\mrm{LInd} :  \cat{Rng} \eftover \K \to \cat{TrCat} \over \K ,
\end{equation}
sending a ring $A$ to the category $\cat{D}^{-}_{\mrm{f}}(A)$, and 
a ring homomorphism $u : A \to B$ to the functor 
$\mrm{LInd}_u$. The composition isomorphisms of $\mrm{LInd}$ arise from those 
of the plain induction pseudofunctor $\opn{Ind}$; and 
these are just the associativity isomorphisms for tensor products. 

The next result is our ring-theoretic version of the geometric {\em 
twisted inverse pseudofunctor} $f \mapsto f^!$ from \cite{RD}. 
See Theorem \ref{thm:290}  for our geometric result. 

\begin{thm}[{\cite{YZ2}, \cite{OSY}}] \label{thm:121}
There is a unique pseudofunctor 
\[ \opn{TwInd} : \cat{Rng} \eftover \K \to \cat{TrCat} \over \K \]
called {\em twisted induction}, with these properties\hsp{0.1}\tup{:}
\begin{enumerate} 
\item To an object $A \in \cat{Rng} \eftover \K$ it assigns the triangulated 
category $\cat{D}^{+}_{\mrm{f}}(A)$.
 
\item To a morphism $u : A \to B$ in $\cat{Rng} \eftover \K$ it assigns the 
triangulated functor 
\[ \opn{TwInd}_{u} \ := \ 
\opn{D}_{B}^{\mrm{rig}} \circ \opn{LInd}_u \circ \opn{D}_{A}^{\mrm{rig}}
\ :  \ \cat{D}^{+}_{\mrm{f}}(A) \to \cat{D}^{+}_{\mrm{f}}(B) . \]
 
\item The composition isomorphisms of \hsp{0.1} $\opn{TwInd}$ come from the 
evaluation isomorphisms of the rigid auto-duality functors 
\tup{(\ref{eqn:245})}, combined with the composition isomorphisms of the 
pseudofunctor $\opn{LInd}$.
\end{enumerate}
\end{thm}

In the next section we shall see how $\opn{TwInd}$ interacts with rigid traces 
and rigid \'etale-localizations.

\begin{rem} \label{rem:279}
Observe that the pseudofunctor $\opn{TwInd}$ is constructed {\em purely by 
algebraic methods}, namely without geometry, and especially without {\em 
global duality}, which is a key ingredient in all earlier approaches to GD. 
The only other such purely algebraic construction we are aware of is the very 
recent one by P. Scholze and D. Clausen \cite{Sc}. They use {\em condensed 
mathematics}, and so far it works only for FT $\Z$-rings. 
\end{rem}

\begin{rem} \label{rem:278}
Here are a few historical details on the squaring operation and 
rigid dualizing complexes. 

{\em Noncommutative dualizing complexes} were introduced in our 1992 paper
\cite{Ye3}. These are complexes of bimodules over a NC ring $A$, central over 
a base field $\K$, satisfying conditions similar to those of commutative 
dualizing complexes. 
 
{\em Noncommutative rigid dualizing complexes} were invented by M. Van 
den Bergh in 1997, in his seminal paper \cite{VdB}. Observe the similarity 
between the squaring operation (Theorem \ref{thm:230}) and {\em Hochschild 
cohomology}. This is not a coincidence. An idea similar to that of a NC rigid 
dualizing complex was independently discovered by M. Kontsevich in the late 
1990's, and it is one of the cornerstones of the theory of {\em Calabi-Yau 
categories} that emerged from the work of Kontsevich and others. These NC 
theories are explained in \cite[Chapter 18]{Ye7}.
 
J.J. Zhang and the author imported the concept of rigid dualizing complexes 
back to commutative algebra and algebraic geometry. We added two features 
to the original concept of NC rigidity of Van den Bergh: the {\em functoriality 
of rigid complexes}, and the {\em passage from base field to base ring}, which 
is sometimes referred to as the {\em arithmetic setting}. This 
was done in our papers \cite{YZ1} and \cite{YZ2} from around 2008. 
As already mentioned in Section 1, the generalization from base field to base 
ring required the use of {\em DG ring resolutions}. 

Unfortunately there were several serious errors regarding the manipulation of 
DG rings in the paper \cite{YZ1}, and these errors affected some constructions 
and proofs in \cite{YZ1} and \cite{YZ2}. Interestingly, our main results in 
these two paper were correct, as we now know. 

The errors in \cite{YZ1} and \cite{YZ2} were discovered by the authors of 
\cite{AILN} in 2010, and they also fixed one of these errors. 
(However, contrary to the norms of ethical scientific conduct, the authors of 
\cite{AILN} failed to inform us of the errors in our work before publishing 
their own paper.) 
 
This accident --  the errors regarding DG rings -- took a lot of time and 
effort to correct. Some of the errors were fixed in our paper \cite{Ye6} from  
2016 , and the rest are corrected in the upcoming paper \cite{OSY}, which is 
joint work with M. Ornaghi and S. Singh.  
This is one of the main reasons the project discussed in this article was 
delayed for so many years.
\end{rem}
