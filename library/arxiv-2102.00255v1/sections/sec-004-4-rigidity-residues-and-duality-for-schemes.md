---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-004-4-rigidity-residues-and-duality-for-schemes
section_title: "Rigidity, Residues and Duality for Schemes"
section_number: 4
pages: 11-14
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.975
doc_brief: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS — In this article we explain the theory of rigid residue complexes in commutative algebra and algebraic geometry, summarizing the"
---
Recall that $\K$ is a regular finite dimensional noetherian base ring.
We use the notation $\cat{Sch} \ftover \K$ for the category of finite type (FT) 
$\K$-schemes. 

Consider a FT $\K$-scheme $X$. If $U \sub X$ is an affine open set, then 
$A := \Gamma(U, \mcal{O}_X)$ is a FT $\K$-ring.
Given a quasi-coherent $\mcal{O}_X$-module, for every affine open set $U$
we get an $A$-module $M := \Gamma(U, \mcal{M})$.
The resulting functor
$\Gamma(U, -) : \cat{QCoh}(X) \to \cat{Mod}(A)$
is exact. 

\begin{rem} \label{rem:261}
The theory discussed in this section extends easily to {\em essentially finite 
type $\K$-schemes}. But the geometry of EFT $\K$-schemes is a bit messy 
(or perhaps the foundations have not been studied well enough yet), and 
therefore we will not talk about them here. The paper \cite{Ye9} does deal 
with EFT $\K$-schemes, by making special adjustments to overcome a few 
annoying technicalities. 
\end{rem}

If $V \sub U$ is an inclusion of affine open sets in $X$, then geometric 
restriction
$\opn{rest}_{V / U} : \Gamma(U, \mcal{O}_X) \to \Gamma(V, \mcal{O}_X)$
is an {\em \'etale ring homomorphism}. For 
$\MM \in \cat{QCoh}(X)$ we get a nondegenerate forward homomorphism 
$\opn{rest}_{V / U} : \Gamma(U, \mcal{M}) \to \Gamma(V, \mcal{M})$
of $\Gamma(U, \mcal{O}_X)$-modules.

According to the Grothendieck-Matlis classification of injective 
$\OO_X$-modules from \cite[Section II.7]{RD}, every quasi-coherent 
$\OO_X$-module $\MM$ admits a monomorphism $\MM \inj \II$, where $\II$ is an 
$\OO_X$-module that is both quasi-coherent and injective in the category \lb
$\cat{Mod}(X)$ of all $\OO_X$-modules. In particular, the object $\II$ is 
injective in the full subcategory $\cat{QCoh}(X)$ of $\cat{Mod}(X)$. We call 
such an object $\II$ a {\em quasi-coherent injective $\OO_X$-module}. Every 
quasi-coherent injective $\OO_X$-module $\II$ is a direct sum (often infinite) 
of indecomposable quasi-coherent injective $\OO_X$-modules. These 
indecomposable quasi-coherent injective $\OO_X$-modules are classified by 
points $x \in X$. For every point $x$ the corresponding indecomposable 
injective $\JJ(x)$ is a skyscraper quasi-coherent $\OO_X$-module with support 
the closed set $\ol{\{ x \}}$, 
and whose stalk at $x$ is the injective hull of 
the residue field $\kk(x)$ over the local ring $\OO_{X, x}$. To match this with 
the ring theoretic Matlis classification from Section 3, when 
$X = \opn{Spec}(A)$ is affine, and $x = \p$, then $\JJ(x) \cong J(\p)$
as modules over $\OO_{X, x} \cong A_{\p}$.  

\begin{dfn}[\cite{Ye9}] \label{dfn:255}
Let $X$ be a FT $\K$-scheme. A {\em rigid residue complex on $X$} (relative to 
$\K$) is a pair $(\mcal{K}_X, \bsym{\rho}_X)$ consisting of these data:
\begin{itemize}
\rmitem{a} A bounded complex $\mcal{K}_X$ of quasi-coherent injective  
$\mcal{O}_X$-modules,

\rmitem{b} A collection $\bsym{\rho}_X := \{ \rho_U \}$ 
indexed by the affine open sets $U \sub X$, where each 
$\rho_U$ is a rigidifying isomorphism for the complex of  
$\Gamma(U, \mcal{O}_X)$-modules $\Gamma(U, \mcal{K}_X)$, 
in the sense of Definition \ref{dfn:230}.
\end{itemize}
There are two conditions:
\begin{enumerate}
\rmitem{i} For every $U$, the pair 
$\bigl( \Gamma(U, \mcal{K}_X), \rho_U \bigr)$
is a rigid residue complex over the 
ring  $\Gamma(U, \mcal{O}_X)$, in the sense of Definition \ref{dfn:250}.

\rmitem{ii} For every inclusion $V \sub U$ of affine open sets, the 
nondegenerate forward homomorphism 
$\opn{rest}_{V / U} : \Gamma(U, \mcal{K}_X) \to \Gamma(V, \mcal{K}_X)$
is the unique rigid \'etale-localization homomorphism between these rigid 
residue complexes (see Theorem$^{(*)}$ \ref{thm:126}). 
\end{enumerate}
The collection $\bsym{\rho}_X$ is called a {\em rigid structure} on the complex 
$\KK_X$. 
\end{dfn}

\begin{dfn}[\cite{Ye9}] \label{dfn:256}
Suppose $(\mcal{K}_X, \bsym{\rho}_X)$ and $(\mcal{K}'_X, \bsym{\rho}'_X)$
are two rigid residue complexes on the FT $\K$-scheme $X$. 
A {\em morphism of rigid residue complexes}
$\phi : (\mcal{K}_X, \bsym{\rho}_X) \to (\mcal{K}'_X, \bsym{\rho}'_X)$
is a homomorphism $\phi : \KK_X \to \KK'_X$ of complexes of
$\mcal{O}_X$-modules, such that for every
affine open set $U$, with $A := \Gamma(U, \mcal{O}_X)$, the 
homomorphism $\Gamma(U, \phi)$ is a morphism in 
$\cat{C}(A)_{\mrm{res} / \K}$.
\end{dfn}

The next four theorems are easy consequences of the corresponding theorems for 
rings in Section \ref{sec:rrr-rings}, combined with descent for QC sheaves on 
schemes. 
 
\begin{thmstar}[\cite{Ye9}] \label{thm:135}
Every FT $\K$-scheme $X$ has a rigid residue complex 
$(\mcal{K}_X, \bsym{\rho}_X)$, and it is unique up to a unique isomorphism of 
rigid residue complexes. 
\end{thmstar}

\begin{thmstar}[\cite{Ye9}] \label{thm:136}
For every map $f : Y \to X$ between FT $\K$-schemes there is a unique 
homomorphism of {\em graded quasi-coherent $\mcal{O}_X$-modules}
$\opn{tr}^{\mrm{ires}}_f : f_*(\mcal{K}_Y) \to \mcal{K}_X$,
called the {\em ind-rigid trace homomorphism}, 
which extends the ind-rigid trace homomorphism $\opn{tr}^{\mrm{ires}}_{(-)}$
on $\K$-rings from Theorem \tup{\ref{thm:132}}. The homomorphism 
$\opn{tr}^{\mrm{ires}}_f$ is functorial in $f$.   
\end{thmstar}
 
If $f$ is a {\em finite} map of schemes, then $\opn{tr}^{\mrm{ires}}_f$ 
is a homomorphism of complexes -- this is immediate from the result for rings. 
The case of a {\em proper map} will be mentioned soon. 

\begin{thmstar}[\cite{Ye9}] \label{thm:137}
For every \'etale map $g : X' \to X$ between FT $\K$-schemes
there is a unique homomorphism of complexes of quasi-coherent 
$\mcal{O}_X$-modules
$\opn{q}^{\mrm{res}}_g : \mcal{K}_X \to g_*(\mcal{K}_{X'})$,
called the {\em rigid \'etale-localization homomorphism}, 
which extends the rigid \'etale-localiza\-tions homomorphism 
$\opn{q}^{\mrm{res}}_{(-)}$ on $\K$-rings from Theorem \tup{\ref{thm:126}}. 
The homomorphism $\opn{q}^{\mrm{res}}_g$ is functorial in such maps $g$.  
\end{thmstar}
 
\begin{thmstar}[\cite{Ye9}] \label{thm:138}
The ind-rigid trace homomorphism $\opn{tr}^{\mrm{ires}}_{(-)}$ and the 
rigid \'etale-locali\-zation homomorphism $\opn{q}^{\mrm{res}}_{(-)}$ 
commute with each other, as in Theorem$^{(*)}$ \tup{\ref{thm:131}} but 
geometrized.
\end{thmstar}

The next result is really just a geometric version of Theorem \ref{thm:121}, 
without any significant difficulties. For a scheme $X$ with rigid residue 
complex $(\KK_A, \rho_A)$, we define
\begin{equation} \label{eqn:295}
\opn{D}_{X}^{\mrm{rig}} := \Hom_{X}(-, \KK_X) : \cat{D}(X) \to \cat{D}(X)  .
\end{equation}
Here $\cat{D}(X)$ is the derived category of $\OO_X$-modules.
As in the affine case, there are equivalences 
$\opn{D}_{X}^{\mrm{rig}} : \cat{D}^{\star}_{\mrm{c}}(X) \to 
\cat{D}^{-\star}_{\mrm{c}}(X)$
for reversed boundedness conditions $\star$ and $-\star$. 

\begin{thm}[{\cite{YZ2}, \cite{Ye9}}] \label{thm:290} 
There is a unique pseudofunctor 
\[ \opn{TwInvIm} : (\cat{Sch} \ftover \K)^{\mrm{op}} \to \cat{TrCat} \over \K \]
called {\em twisted inverse image}, with these properties\hsp{0.1}\tup{:}
\begin{enumerate} 
\item To an object $X \in \cat{Sch} \ftover \K$ it assigns the triangulated 
category $\cat{D}^{+}_{\mrm{c}}(X)$.
 
\item To a morphism $f : Y \to X$ in $\cat{Sch} \ftover \K$ it assigns the 
triangulated functor 
\[ \opn{TwInvIm}_{f} = f^! \ := \ 
\opn{D}_{Y}^{\mrm{rig}} \circ \, \mrm{L} f^* \circ \opn{D}_{X}^{\mrm{rig}}
\ :  \ \cat{D}^{+}_{\mrm{c}}(X) \to \cat{D}^{+}_{\mrm{c}}(Y) . \]
 
\item The composition isomorphisms of \, $\opn{TwInvIm}$ come from the 
evaluation isomorphisms of the rigid auto-duality functors 
\tup{(\ref{eqn:295})}, combined 
with the composition isomorphisms of the pseudofunctor $f \mapsto \mrm{L} f^*$.
\end{enumerate}
\end{thm}

The functorial properties of the rigid residue complexes (stated in the 
theorems above and below) provide the twisted inverse image pseudofunctor with 
more structure. 

Here is the rigid version of \cite[Theorem VII.2.1]{RD}.

\begin{thmstar}\tup{(Rigid Residue Theorem, \cite{Ye9})} \label{thm:1}
Let $f : Y \to X$ be a proper map between FT $\K$-schemes. Then the ind-rigid 
trace
$\opn{tr}^{\mrm{ires}}_f  : f_*(\mcal{K}_Y) \to \mcal{K}_X$
is a homomorphism of complexes. 
\end{thmstar}

The idea of the proof (imitating \cite{RD}) is to reduce to the case when 
$X = \opn{Spec}(A)$ for a local artinian ring 
$A \in \cat{Rng} \eftover \K$, and $Y = \mbf{P}^1_A$, the projective line.
We do it using Theorems \ref{thm:136}, \ref{thm:137} and \ref{thm:138}.
Then we do a calculation of residues, which similar to the one in the proof of 
the  classical Residue Theorem for $\mbf{P}^1(\mbb{C})_{\mrm{an}}$. The only 
minor complication is that a rational differential form on $Y$ relative to $A$, 
i.e.\ a form $\om \in \Om^1_{A(t) / A}$, where $A(t)$ is the total ring of 
fractions of $Y$, might have poles at closed points of $Y$ that do not belong 
to $Y(A)$. But the poles of $\om$ always belong to $Y(A')$ for a suitable 
finite faithfully flat $A$-ring $A'$, and by performing the base change 
$A \to A'$ the calculation can proceed. 

The next theorem is the rigid version of \cite[Theorem VII.3.3]{RD}.

\begin{thmstar}\tup{(Rigid Duality Theorem, \cite{Ye9})} \label{thm:2}
Let $f : Y \to X$ be a proper map between FT $\K$-schemes. 
For every $\mcal{N} \in \cat{D}^{}_{\mrm{qc}}(Y)$ the morphism  
\[ \DR f_* \bigl( \DR \Hom_{Y}(\mcal{N}, \mcal{K}_Y) \bigr) \to
\DR \Hom_{X} \bigl( \DR f_* (\mcal{N}), \mcal{K}_X \bigr) \]
in $\cat{D}(X)$, which is induced by the ind-rigid trace
$\opn{tr}^{\mrm{ires}}_f : f_*(\mcal{K}_Y) \to \mcal{K}_X$,
is an isomorphism. 
\end{thmstar}

The proof of  imitates the proof of the corresponding
theorem in \cite{RD}, once we have the Theorem$^{(*)}$ \ref{thm:1} at hand.

Theorem$^{(*)}$ \ref{thm:1} implies that for every complex 
$\MM \in \cat{D}^{+}_{\mrm{c}}(X)$ there is an ind-rigid trace morphism 
\begin{equation} \label{eqn:285}
\opn{tr}^{\mrm{irig}}_{f, \MM} : 
\mrm{R} f_*(f^!(\MM)) \to \MM  
\end{equation}
in $\cat{D}(X)$, which is functorial in $\MM$. 
Here is our version of \cite[Corollary 3.4]{RD}. 

\begin{corstar}\tup{(\cite{Ye9})} \label{cor:285}
Let $f : Y \to X$ be a proper map between FT $\K$-schemes. 
For every $\mcal{M} \in \cat{D}^{+}_{\mrm{c}}(X)$ and 
$\mcal{N} \in \cat{D}^{-}_{\mrm{qc}}(Y)$ the morphism  
\[ \DR f_* \bigl( \DR \Hom_{Y} \bigl( \mcal{N}, f^!(\MM) \bigr) \bigr) \to
\DR \Hom_{X} \bigl( \DR f_* (\mcal{N}), \mcal{M} \bigr) \]
in $\cat{D}(X)$, which is induced by the ind-rigid trace
$\opn{tr}^{\mrm{irig}}_{f, \MM}$, is an isomorphism. 
\end{corstar}

\begin{rem}
At this stage we have recovered almost all the results of the original book 
\cite{RD}. One advantage of our rigidity approach is that it is much cleaner
and shorter than the original approach in \cite{RD}. We can also treat EFT maps 
of schemes. Another advantage of the rigidity approach, as we shall see next, 
is that  it gives rise to a useful duality theory for DM stacks. 
On the down side, we must work with a fixed regular base ring $\K$. 

For complements to the book \cite{RD}, and for alternative approaches, due to 
J. Lipman, B. Conrad, A. Neeman, the author of this article, and others, please 
consult \cite{Co}, \cite{LH}, \cite{Ne1}, \cite{Ne2}, \cite{Ye7} and 
their references. 
\end{rem}
