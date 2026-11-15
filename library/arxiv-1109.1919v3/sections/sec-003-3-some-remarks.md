---
doc_id: arxiv-1109.1919v3
doc_title: "COMBINATORIAL DESCENT DATA FOR GERBES"
section_id: sec-003-3-some-remarks
section_title: "Some Remarks"
section_number: 3
pages: 10-12
source_pdf: 1109.1919v3.pdf
source_sha256: 2b634edddf232047
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.988
doc_brief: "COMBINATORIAL DESCENT DATA FOR GERBES — We consider descent data in cosimplicial crossed groupoids. This is a combinatorial abstraction of the descent data for gerbes in algebraic geom- etry."
---
\label{sec:remarks}

To finish the note, here are a few remarks and clarifications, to help place
our work in context. 

\begin{rem} \label{rem:10}
Cosimplicial crossed groupoids arise naturally in the geometry of gerbes. 
This is well-known -- see \cite{Gi, Br1, Br2, BGNT1}. 
Let us quickly indicate how this occurs. Let $\mcal{G}$ be a sheaf of groups on
a topological space $X$, and let $\mcal{A}ut(\mcal{G})$ be its sheaf of
automorphism groups. There is an obvious sheaf of crossed
groups (i.e.\ crossed modules)
\[ \gerbe{G} = \big( \opn{D} : \mcal{G} \to \mcal{A}ut(\mcal{G}) \big)  \] 
on $X$. Consider an open covering $\bsym{U} = \{ U_k \}$ of $X$. 
The \v{C}ech construction gives rise to a cosimplicial crossed group
$G := \mrm{C}(\bsym{U} , \gerbe{G})$.
The set $\ol{\opn{Desc}}(G)$ is an approximation of {\em the set of
equivalence classes of $\mcal{G}$-gerbes} on $X$ (the discrepancy is because we
may have to use refinements and hypercoverings). 

If  every $\mcal{G}$-gerbe totally trivializes on the covering $\bsym{U}$ (see
\cite[Definition 9.16]{Ye1}),
then $\ol{\opn{Desc}}(G)$ actually classifies $\mcal{G}$-gerbes.
If $\bsym{V}$ is another such covering, and 
$\bsym{V} \to \bsym{U}$ is a refinement, then there is an induced 
weak equivalence of cosimplicial crossed groups
$\mrm{C}(\bsym{U} , \gerbe{G}) \to \mrm{C}(\bsym{V} , \gerbe{G})$.

More general gerbes (not $\mcal{G}$-gerbes as above) 
can sometimes be classified by a {\em sheaf of crossed groupoids} 
$\gerbe{G}$ -- see next remark.
For the full generality is it necessary to invoke more complicated
combinatorics -- see Remark \ref{rem:15}.
\end{rem}

\begin{rem} \label{rem:12}
Theorem \ref{thm:1} is used to prove {\em twisted deformation quantization} in
our paper \cite{Ye1} (see also the survey article \cite{Ye3}). We look at a
smooth algebraic variety $X$ over a field $\K$ of characteristic $0$.
By parameter $\K$-algebra we mean a complete noetherian local commutative 
$\K$-algebra $R$, with maximal ideal $\m$ and residue field 
$R / \m = \K$. The main example is $R = \K[[\hbar]]$, the algebra of
power series in a variable $\hbar$. 

On the variety $X$ there are two important sheaves of DG Lie algebras: the
algebra $\mcal{T}_{\mrm{poly}, X}$ of poly derivations, and the algebra 
$\mcal{D}_{\mrm{poly}, X}$ of poly differential operators. 
Consider the sheaves of pronilpotent DG Lie algebras
$\m \hot \mcal{T}_{\mrm{poly}, X}$ and 
$\m \hot \mcal{D}_{\mrm{poly}, X}$. The {\em Deligne crossed groupoid}
construction (see \cite{Ge} or \cite{Ye2}) gives rise to 
sheaves of crossed groupoids 
$\gerbe{G} := \opn{Del} \bigl( \m \hot \mcal{T}_{\mrm{poly}, X} \bigr)$
and
$\gerbe{H}:= \opn{Del} \bigl( \m \hot \mcal{D}_{\mrm{poly}, X} \bigr)$.

Now let $\bsym{U}$ be a finite affine open covering of $X$. 
Consider the cosimplicial crossed groupoids 
$G := \mrm{C}(\bsym{U} , \gerbe{G})$
and 
$H := \mrm{C}(\bsym{U} , \gerbe{H})$.
The sets $\ol{\opn{Desc}}(G)$ and $\ol{\opn{Desc}}(H)$
classify {\em twisted Poisson $R$-deformations} and {\em
twisted associative $R$-deformations} of $\mcal{O}_X$, respectively.
These twisted deformations are stacky versions of usual deformations 
(similar to the stacks of algebroids in \cite{Ko, KS}). The fact that twisted
$R$-deformations of $\mcal{O}_X$ totally trivialize on any affine open covering 
relies on our paper \cite{Ye4}.

There is a diagram of weak equivalences of cosimplicial crossed groupoids
\[ \UseTips \xymatrix @C=8ex @R=6ex {
G
\ar[d]_{\Phi_{\til{G}}}
&
H
\ar[d]^{\Phi_{\til{H}}}
\\
\til{G}
\ar[r]^{\til{\Psi}}
&
\til{H}
} \]
The weak equivalences $\Phi_{\til{G}} : G \to \til{G}$ and
$\Phi_{\til{H}} : H \to \til{H}$ come from suitable 
resolutions of the sheaves of DG Lie algebras 
$\mcal{T}_{\mrm{poly}, X}$ and $\mcal{D}_{\mrm{poly}, X}$ respectively. The 
weak equivalence $\til{\Psi} : \til{G} \to \til{H}$ comes from the Kontsevich 
Formality Theorem and its adaptation to the algebro-geometric setting; see 
\cite[Theorems 10.3 and 10.6]{Ye1}. Due to Theorem \ref{thm:1} we obtain a 
bijection  
\[ \opn{tw{.}quant} : \ol{\opn{Desc}}(G) \to \ol{\opn{Desc}}(H) , \]
\[ \opn{tw{.}quant} := \ol{\opn{Desc}}(\Phi_{\til{H}})^{-1} \circ 
\ol{\opn{Desc}}(\til{\Psi}) \circ \ol{\opn{Desc}}(\Phi_{\til{G}}) . \]
A refinement argument shows that $\opn{tw{.}quant}$ is independent of the 
resolutions. We call it the {\em twisted quantization map}. 
 
The twisted quantization map $\opn{tw{.}quant}$ does not arise from a
refinement or any similar geometric operation. Indeed, it is conjectured that in
some cases (e.g.\ when $X$ is a Calabi-Yau surface) the twisted quantization 
would send a sheaf to a stack, thus destroying the geometry. 

An earlier approach to twisted deformation quantization (in previous versions
of \cite{Ye1}) relied on {\em nonabelian multiplicative integration on
surfaces} \cite{Ye6}. The new approach uses Theorem \ref{thm:1}, and is
much shorter. Let us mention however that the ideas of \cite{Ye6} were recently
picked up by \cite{BGNT2}, for comparing various nerves of a $2$-groupoid. 
\end{rem}

\begin{rem} \label{rem:11}
A crossed groupoid (i.e.\ crossed module over a groupoid) is the same as a {\em
strict $2$-groupoid}; see \cite[Proposition 5.5]{Ye2}. The homotopy set
$\bsym{\pi}_0(G)$ and 
groups $\bsym{\pi}_i(G, x)$ are the same in both incarnations.
A crossed groupoid  is also the same as a 
category with inner gauge groups $(\cat{P}, \opn{IG}, \opn{ig})$ where
$\cat{P}$ is a groupoid -- see \cite[Section 5 and Proposition 10.4]{Ye1}. 

Traditionally papers used the $2$-groupoid language to discuss descent for
gerbes (cf.\ \cite{BGNT1}). In \cite{Ye1} we realized that the crossed groupoid
language is more effective: geometric descent data comes naturally in terms of a
cosimplicial crossed groupoid (see \cite[Section 10]{Ye1}), and also the Deligne
construction (see \cite[Section 6]{Ye2}) appears as a crossed groupoid, so it is
more natural to talk about the Deligne crossed groupoid. 

Another reason for preferring the crossed groupoid language is that defining
combinatorial descent data, and proving Theorem \ref{thm:100}, is easier this
way.
\end{rem}

\begin{rem}
To the best of our knowledge there is no prior proof of Theorem \ref{thm:1},
and moreover such a general result was not even conjectured before.

Results of similar flavor do appear in the work of Breen \cite{Br1, Br2} on 
classification of gerbes. Indeed Breen shows that the morphism of crossed
groups arising from a refinement (cf.\ Remark \ref{rem:10}) 
induces a bijection on $\ol{\opn{Desc}}(-)$. 
It is possible that Theorem \ref{thm:1} can be given a shorter proof using
Breen's diagram calculus. 

Another earlier result, a special case of our Theorem \ref{thm:1}, is
\cite[Proposition 3.3.1]{BGNT1}. However it is too restricted for the purposes
of \cite{Ye1}. 

Assertions in \cite{CH} that are similar to Theorem
\ref{thm:1} are, to the best of our understanding, not actually proved there. 

The paper \cite{Pr} by Prezma, which is a follow-up to our own present note, 
extends Theorem \ref{thm:1} significantly (see next remark). The proof given
in \cite{Pr} uses methods from homotopy
theory, and is much more sophisticated than our direct calculations. 
Nonetheless our proof is somewhat shorter, and is completely self-contained. 
\end{rem}

\begin{rem} \label{rem:cosim.1}
Let $G \in \bsym{\Delta} (\cat{CrGrpd})$.
The set $\opn{Desc}(G)$ has a crossed groupoid structure, in
which the gauge transformations are the $1$-morphisms; so 
$\bsym{\pi}_0(  \opn{Desc}(G) ) = \ol{\opn{Desc}}(G)$.
See \cite{Pr}, and also \cite[Section 5]{Br2}, \cite{Hi} and \cite{BGNT1} for
special cases. A morphism $\Phi : G \to H$ in 
$\bsym{\Delta} (\cat{CrGrpd})$ induces a morphism 
\[ \opn{Desc}(\Phi) : \opn{Desc}(G) \to 
\opn{Desc}(H) \]
in $\cat{CrGrpd}$. 

Prezma \cite{Pr} proves that if $\Phi$ is a cosimplicial weak equivalence,  then 
the morphism of crossed groupoids $\opn{Desc}(\Phi)$ is a {\em weak
equivalence}. This of course implies Theorem \ref{thm:1}.
The result of Prezma extends Jardine's
corresponding result for (ordinary) groupoids \cite{Ja}.
Moreover Prezma shows how to extend his equivalence theorem to higher 
($n > 2$) groupoids.
\end{rem}

\begin{rem} \label{rem:15}
We should emphasize that Theorem \ref{thm:1} holds in much greater
generality than stated. First observe that we made no use of the full
cosimplicial structure of the cosimplicial crossed groupoids $G$ and 
$H$ -- all we needed is that these are {\em $3$-truncated
semi-cosimplicial crossed groupoids}. Namely that $G$ and 
$H$ are functors 
$\bsym{\Delta}^{\leq 3}_{\mrm{inj}} \to \cat{CrGrpd}$, where
$\bsym{\Delta}^{\leq 3}_{\mrm{inj}}$ is the subcategory of 
$\bsym{\Delta}$ on the object set $\{ 0, 1, 2, 3 \}$, and with only injective 
functions $\al : p \to q$. Likewise for the weak equivalence 
$\Phi : G \to H$.

The reason  we chose to use the cosimplicial language is convenience. It
also fits nicely with the conventions of \cite{Ye1}. 

Other papers dealing with descent for gerbes and stacks (cf.\ \cite{Br1, Br2,
DP}) indicate that Theorem \ref{thm:1} might be extended further. It is almost
clear to us that the theorem holds for {\em $4$-truncated
pseudo-semi-cosimplicial crossed groupoids}, namely for pseudo-functors
$G, H : \bsym{\Delta}^{\leq 4}_{\mrm{inj}} \to \cat{CrGrpd}$.
This would correspond to a \v{C}ech construction performed on a {\em stack
of crossed groupoids} on a space $X$. 

A more complicated extension would be to replace the $2$-category 
$\cat{CrGrpd}$ of crossed groupoids with the $2$-category
$\cat{w2Grpd}$  of {\em weak $2$-groupoids}, i.e.\ to work with pseudo-functors
$\bsym{\Delta}^{\leq 4}_{\mrm{inj}} \to \cat{w2Grpd}$.

It is reasonable to assume that proving such extended results would require
either a bare-hands approach like ours, or else a very sophisticated
homotopical machinery.
\end{rem}
