---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-005-5-rigidity-residues-and-duality-for-dm-stacks
section_title: "Rigidity, Residues and Duality for DM Stacks"
section_number: 5
pages: 14-19
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.987
doc_brief: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS — In this article we explain the theory of rigid residue complexes in commutative algebra and algebraic geometry, summarizing the"
---
Here is a brief recollection of facts about Deligne-Mumford (DM) stacks and 
quasi-coherent sheaves on them, extracted from \cite{SP} and \cite{Ol}, with 
some additional  elaboration. This will help us state our results. 

As a first approximation, it useful to think of a DM stack $\XX$ as a 
scheme equipped with an extra structure: the points of $\XX$ are bunched 
together as objects of a groupoid, in an intricate geometric way. 
(This can be understood, for instance, as the way $\XX$ sits above its coarse 
moduli space $X$; we will return to this idea later.)

To give a more precise description of DM stacks,
we need to place ourselves in the realm of sheaves and stacks 
on $(\cat{Sch} \ftover \K)_{\mrm{et}}$, the big \'etale site of FT $\K$-schemes.

For us a {\em prestack of groupoids} on $\cat{Sch} \ftover \K$ is 
a pseudofunctor 
$\XX : (\cat{Sch} \ftover \K)^{\mrm{op}} \to \cat{Grpd}$,
where $\cat{Grpd}$ is the $2$-category of groupoids.
The prestack $\XX$ is a {\em stack} if it satisfies descent for morphisms and 
descent for objects with respect to coverings in 
$(\cat{Sch} \ftover \K)_{\mrm{et}}$. 
See \cite[Section 2]{Ye4} for details on stacks, as viewed from the 
pseudofunctor approach. 

Most algebraic geometry texts (including \cite{Ol} and \cite{SP}) prefer 
viewing a prestack of groupoids on $\cat{Sch} \ftover \K$ as a {\em category 
fibered in groupoids}. The passage from this approach to ours is this: 
a prestack of groupoids $\XX$ in our sense is the same as a category 
fibered in groupoids equipped with a cleavage. See \cite[Remark 2.5]{Ye4}.

A benefit of our approach to stacks of groupoids is that it lets us 
refer to a sheaf of sets as a very trivial kind of stack. Indeed, a sheaf of 
sets $X$ on $(\cat{Sch} \ftover \K)_{\mrm{et}}$ can be seen as a stack of 
groupoids, in which the only local isomorphisms between local objects are the 
identity automorphisms. 

We know how a scheme $X$ becomes a sheaf of sets on 
$(\cat{Sch} \ftover \K)_{\mrm{et}}$ -- it is the Yoneda incarnation of $X$ 
as the sheaf $\Hom(-, X)$. An {\em algebraic space} $X$ is a more 
complicated sheaf of sets on $(\cat{Sch} \ftover \K)_{\mrm{et}}$; 
it is not representable, but only "locally representable". One way to express 
this condition is that the sheaf $X$ is 
isomorphic to the quotient sheaf $U_0 / U_1$ of an {\em \'etale equivalence 
relation in schemes} $(U_1 \rightrightarrows U_0)$. Let's refer to the 
isomorphism of sheaves $p : U_0 / U_1 \iso X$ as a {\em presentation} of 
$X$. See \cite[Proposition 5.2.5]{Ol}.

There is an analogous way to say when an abstract stack $\XX$
on $(\cat{Sch} \ftover \K)_{\mrm{et}}$ is a DM stack. 
The condition is that $\XX$ is equivalent, in the $2$-category of stacks of 
groupoids on $(\cat{Sch} \ftover \K)_{\mrm{et}}$,
to the quotient stack $[X_0 / X_1]$ of an {\em \'etale groupoid in algebraic 
spaces} \lb $(X_1 \rightrightarrows X_0)$. Note that the groupoid 
$(X_1 \rightrightarrows X_0)$ involves a third algebraic space $X_2$, with a map
$X_2 \to X_1 \times_{X_0} X_1$ that encodes composition of morphisms. 
Again we call the equivalence
$p : [X_0 / X_1] \equiv \XX$ a presentation of $\XX$. See 
\cite[Theorem \href{https://stacks.math.columbia.edu/tag/04TK}{\tt tag=04TK}
and Lemma \href{https://stacks.math.columbia.edu/tag/04T5}{\tt tag=04T5}]{SP}.
We shall use the term {\em map of stacks} for a $1$-morphism
$f : \YY \to  \XX$ between stacks of groupoids on 
$(\cat{Sch} \ftover \K)_{\mrm{et}}$. 

Thus there are four stages, or levels of complexity, in the geometry of 
FT DM $\K$-stacks: 
\begin{equation} \label{280}
\cat{AfSch} \ftover \K 
\sub \cat{Sch} \ftover \K 
\sub \cat{AlgSp} \ftover \K 
\sub \cat{DMStk} \ftover \K  .
\end{equation}
These are the affine schemes, schemes, algebraic spaces and DM stacks, all of 
FT over $\K$. If we ignore the fact that $\cat{DMStk} \ftover \K$ is 
a $2$-category (i.e.\ if we 
forget the $2$-morphisms between $1$-morphisms of DM stacks), formula 
(\ref{280}) describes full embeddings of categories. 
Morphisms in these categories will be called {\em maps}. 
In what follows all our stacks (and algebraic spaces and schemes) 
are FT over the base ring $\K$; and the rings are EFT over $\K$. 

A map $f : \YY \to \XX$ of DM stacks is {\em surjective} if it is locally 
essentially surjective on objects. (This is a property of a map between 
abstract stacks of groupoids, not just of algebraic stacks.) 

A map $f : \YY \to \XX$ between DM stacks is called {\em \'etale} if there exist
presentations 
$p : [X_0 / X_1] \equiv \XX$ and $q : [Y_0 / Y_1] \equiv \YY$,
and an \'etale map of algebraic spaces
$g : Y_0 \to X_0$, such that the diagram 
\begin{equation} \label{eqn:270}
\UseTips \xymatrix @C=7ex @R=5ex {
Y_0
\ar[r]^{q}
\ar[d]_{g}
&
\YY
\ar[d]^{f}
\\
X_0
\ar[r]^{p}
&
\XX }
\end{equation}
of stacks is commutative up to isomorphism.
For this condition we need to know what is an \'etale map 
$g : Y_0 \to X_0$ between algebraic spaces, and this is done by going down the 
staircase of embeddings (\ref{280}).
(This same yoga is how other local properties of a map of DM 
stacks $f : \YY \to \XX$, such as being smooth or flat, are defined -- they 
are reflected by the corresponding properties of $g : Y_0 \to X_0$.)
The more conventional criterion for $f : \YY \to \XX$ to be 
\'etale is in \cite[Definition 8.2.6]{Ol}.

Presentations of algebraic spaces and DM stacks allow us to describe 
{\em quasi-coherent sheaves} on these geometric objects. Thus, a presentation 
$p : U_0 / U_1 \iso X$ of an algebraic space $X$ induces an equivalence of 
abelian categories 
\begin{equation} \label{eqn:211}
p^* : \cat{QCoh}(X) \to \cat{QCoh} (U_1 \rightrightarrows U_0) , 
\end{equation}
where the latter refers to the category of equivariant quasi-coherent 
sheaves on the equivalence relation $(U_1 \rightrightarrows U_0)$. 
Analogously, a presentation $p : [X_0 / X_1] \equiv \XX$ of a DM stack 
$\XX$ induces an equivalence of abelian categories 
\begin{equation} \label{eqn:212}
p^* : \cat{QCoh}(\XX) \to \cat{QCoh} (X_1 \rightrightarrows X_0) , 
\end{equation}
where now $(X_1 \rightrightarrows X_0)$ is an \'etale groupoid in algebraic 
spaces. See \cite[Sections 7.1 and 9.2]{Ol} and 
\cite[Proposition \href{https://stacks.math.columbia.edu/tag/03M3}{\tt 
tag=03M3} and Lemma 
\href{https://stacks.math.columbia.edu/tag/06WV}{\tt tag=06WV}]{SP}.

The discussion above suggests a mechanism for producing a quasi-coherent 
sheaf $\MM_{\XX}$ on a FT DM $\K$-stack $\XX$. Consider a presentation 
$[X_0 / X_1] \equiv \XX$, the finitely many schemes $U$ involved in presenting 
the algebraic spaces $X_i$, the finitely many affine schemes $\opn{Spec}(A)$
involved in suitable hypercoverings of these schemes, and the finitely many 
\'etale maps between these geometric objects,  going down the staircase in 
the hierarchy (\ref{280}). 
The first step in this mechanism is to provide an $A$-module $M_A$ 
for every affine scheme $\opn{Spec}(A)$ involved, and a consistent collection
of nondegenerate forward homomorphisms $M_A \to M_{A'}$ for all the \'etale ring
homomorphisms $A \to A'$ involved. The second step is to glue these modules
into QC sheaves $\MM_U$ on all the schemes $U$ involved. There will be 
an induced consistent collection of isomorphisms $g^*(\MM_U) \iso \MM_{U'}$ for 
the \'etale maps $g : U' \to  U$ involved. The third step is to use 
the equivalences (\ref{eqn:211}) associated to presentations to obtain 
QC sheaves $\MM_{X_i}$ on the algebraic spaces $X_i$, with consistent pullback 
isomorphisms. Finally, formula (\ref{eqn:212}) will give us the 
desired quasi-coherent sheaf $\MM_{\XX}$. 

Suppose we have a map $f : \YY \to \XX$ of DM stacks, and QC sheaves
$\MM \in  \cat{QCoh}(\XX)$ and $\NN \in  \cat{QCoh}(\YY)$. 
To specify a homomorphism 
$\phi : f_{*}(\NN) \to \MM$ in $\cat{QCoh}(\XX)$
we can use presentations. After having arranged for 
presentations $p : [X_0 / X_1] \equiv \XX$ and $q : [Y_0 / Y_1] \equiv \YY$,
and a map of algebraic spaces $\til{f}_0 : Y_0 \to X_0$, such that the diagram 
(\ref{eqn:270}), with $\til{f}_0$ instead of $g$,  is commutative (up to 
isomorphism), the map $\til{f}_0$ can be extended to a map 
\begin{equation} \label{eqn:284}
\til{f} = (\til{f}_0, \til{f}_1, \til{f}_2) : 
(Y_1 \rightrightarrows Y_0) \to (X_1 \rightrightarrows X_0)
\end{equation}
of groupoids in algebraic spaces (see
\cite[
Definition \href{https://stacks.math.columbia.edu/tag/043W}{\tt tag=043W}
and 
Section  \href{https://stacks.math.columbia.edu/tag/04TJ}{\tt tag=04TJ}]{SP}).
By pullback along $p$ and $q$ we get quasi-coherent sheaves $\MM_i \in 
\cat{QCoh}(X_i)$ and $\NN_i \in \cat{QCoh}(Y_i)$ satisfying the appropriate 
relations. Then we need to arrange for homomorphisms 
$\til{\phi}_i : \til{f}_{i \, *}(\NN_i) \to \MM_i$
that respect the relations; and these will determine $\phi$ by the equivalence 
(\ref{eqn:212}). As before, this construction requires going 
down the staircase of the hierarchy (\ref{280}). 

After recalling and elucidating the mechanism of gluing quasi-coherent sheaves 
on DM stacks, we can finally talk about rigid residue complexes. As we shall 
see, the definition of a rigid residue complex on a DM stack $\XX$ is
very similar to the definition for a scheme, with only a minor adjustment. (We 
will skip the algebraic space case, since it is identical to the DM 
stack case.)

\begin{dfn}[\cite{Ye10}] \label{dfn:270}
Let $\XX$ be a FT DM $\K$-stack. A {\em rigid residue complex on $\XX$} 
(relative to $\K$) is a pair $(\mcal{K}_{\XX}, \bsym{\rho}_{\XX})$ consisting 
of these data:
\begin{itemize}
\rmitem{a} A bounded complex $\mcal{K}_X$ of quasi-coherent injective  
$\mcal{O}_{\XX}$-modules.

\rmitem{b} A collection 
$\bsym{\rho}_{\XX} := \{ \rho_{(U, g)} \}$ 
indexed by \'etale maps $g : U \to \XX$ from affine $\K$-schemes $U$,
where each $\rho_{(U, g)}$ is a rigidifying isomorphism for the complex of  
$\Gamma(U, \mcal{O}_U)$-modules $\Gamma(U, g^*(\mcal{K}_{\XX}))$, 
in the sense of Definition \ref{dfn:230}.
\end{itemize}
There are two conditions:
\begin{enumerate}
\rmitem{i} For every \'etale map $g : U \to  \XX$ from an affine scheme 
$U = \opn{Spec}(A)$, letting
$\KK_A := \Gamma(U, g^*(\mcal{K}_{\XX}))$, 
the pair $(\KK_A, \rho_{(U, g)})$ 
is a rigid residue complex over the ring $A$, in the sense of Definition 
\ref{dfn:250}.

\rmitem{ii} For every commutative diagram 
\[ \UseTips \xymatrix @C=7ex @R=4ex {
U_2
\ar[r]^{h}
\ar[dr]_{g_2}
&
U_1
\ar[d]^{g_1}
\\
&
\XX
} \]
of \'etale maps, where  $U_1$ and $U_2$ are affine schemes, 
the homomorphism $h^*$ arising from the equality $g_2 = g_1 \circ h$
is the unique nondegenerate rigid \'etale-localization homomorphism
\[ h^* : \bigl( \Gamma(U_1, g_1^*(\mcal{K}_{\XX})), \rho_{(U_1, g_1)} \bigr) \to
\bigl( \Gamma(U_2, g_2^*(\mcal{K}_{\XX})), \rho_{(U_2, g_2)} \bigr) , \]
in the sense of Theorem$^{(*)}$ \ref{thm:126}.
\end{enumerate}
The collection $\bsym{\rho}_{\XX}$ is called a {\em rigid structure} on the 
complex $\KK_{\XX}$. 
\end{dfn}
 
\begin{thmstar} \tup{ (\cite{Ye10})} \label{thm:3}
Let $\XX$ be a FT DM $\K$-stack. There exists a rigid residue complex 
$(\KK_{\XX}, \bsym{\rho}_{\XX})$, and it is unique up to a unique rigid 
isomorphism.
\end{thmstar}

The proof is by applying the mechanism of gluing quasi-coherent sheaves that 
was explained above, where in the first 
step of affine schemes we use Corollary$^{(*)}$ \ref{cor:125}. 
 
\begin{thmstar}\tup{ (\cite{Ye10})} \label{thm:4}
Let $f : \YY \to \XX$ be a map between FT DM $\K$-stacks. 
There is a homomorphism of {\em graded quasi-coherent 
$\OO_{\XX}$-modules} 
$\opn{tr}^{\mrm{ires}}_f : f_*(\mcal{K}_{\YY}) \to \mcal{K}_{\XX}$
called the {\em ind-rigid trace}, extending the ind-rigid trace on FT 
$\K$-rings. 
\end{thmstar}
 
To prove this theorem we apply the construction explained above for 
homomorphisms between quasi-coherent sheaves, starting with 
Theorem$^{(*)}$ \ref{thm:133} for affine schemes. 

\begin{thmstar}[{\cite{Ye10}}] \label{thm:287} 
There is a pseudofunctor 
\[ \opn{TwInvIm} : (\cat{DMStk} \ftover \K)^{\mrm{op}} \to \cat{TrCat} \over \K
, \quad \XX \mapsto \cat{D}^{+}_{\mrm{c}}(\XX) 
, \quad f \mapsto f^!  \]
called the {\em twisted inverse image}, with properties like in Theorem 
\tup{\ref{thm:290}}.
\end{thmstar}

In this theorem we consider $\cat{DMStk} \ftover \K$ as a $1$-category, 
ignoring the $2$-isomorphisms between $1$-morphisms, as we had done in the 
hierarchy (\ref{280}). 
However, the $2$-category structure of $\cat{DMStk} \ftover \K$ is reflected in 
this property: if $f_0, f_1 : \YY \to \XX$ are maps in 
$\cat{DMStk} \ftover \K$
for which a $2$-isomorphism $\ga : f_0 \twoiso f_1$ exists, then the 
triangulated functors 
$f_0^!, f_1^! : \cat{D}^{+}_{\mrm{c}}(\XX) \to \cat{D}^{+}_{\mrm{c}}(\YY)$
are isomorphic. This implies that when $f : \YY \to \XX$ is an 
equivalence of stacks, the functor $f^!$ will also be an equivalence. 

The obvious question now is this: {\em Do the Rigid Residue Theorem and the 
Rigid Duality Theorem hold for a proper map $f : \YY \to \XX$ 
between DM stacks}~{\hspace{-0.2ex}}?
We only know a partial answer. 

By the Keel-Mori Theorem \cite[Theorem 11.1.2]{Ol}, a separated FT $\K$-stack 
$\YY$ has a {\em coarse moduli space} $\pi : \YY \to Y$. The map $\pi$ is 
proper and quasi-finite, and $Y$ is, in general, an {\em algebraic 
space}. 

\begin{dfn} \label{dfn:271}
\begin{enumerate}
\item Let $\YY$ be a separated FT DM $\K$-stack, with coarse moduli space
$\pi : \YY \to Y$. We call $\YY$ a {\em coarsely schematic stack} if its coarse 
moduli space $Y$ is a scheme. 

\item Let $f : \YY \to \XX$ be a separated map between FT DM $\K$-stacks. 
We say that $f$ is a {\em coarsely schematic map} if for some surjective 
\'etale 
map $U \to \XX$ from an affine scheme $U$, the stack 
$\YY' := \YY \times_{\XX} U$ is  coarsely schematic.
\end{enumerate} 
\end{dfn}

This appears to be a rather mild restriction: most DM stacks that come up in
examples are of this kind. See Remark \ref{rem:275} about the necessity of this 
condition.

\begin{thmstar}[Rigid Residue Theorem, \cite{Ye10}] \label{thm:10}
Suppose $f : \YY \to \XX$ is a proper coarsely schematic map of FT DM 
$\K$-stacks. Then the ind-rigid trace
$\opn{tr}^{\mrm{ires}}_f : f_*(\mcal{K}_{\YY}) \to \mcal{K}_{\XX}$
is a homomorphism of complexes of $\OO_{\XX}$-modules. 
\end{thmstar}

It is not expected that duality will hold in this generality. In fact, there
are easy counter examples. The problem is not geometric, but rather a basic 
difficulty with {\em representations of finite groups in positive 
characteristics}.
  
Following \cite{AOV} (see also \cite[Definition 11.3.2]{Ol}), a separated FT DM 
stack $\YY$ is called {\em tame} if for every field 
$L \in \cat{Rng} \eftover \K$, the automorphism groups in the groupoid 
$\YY(L)$, which are always finite, have orders prime to the characteristic of 
$L$. 

\begin{dfn} \label{dfn:275}
A separated map of FT DM $\K$-stacks $f : \YY \to \XX$ is called a {\em tame 
map} if for some surjective \'etale map $U \to \XX$ from an affine scheme $U$, 
the stack $\YY' := \YY \times_{\XX} U$ is tame.
\end{dfn}

\begin{thmstar}[Rigid Duality Theorem, \cite{Ye10}] \label{thm:11}
Suppose $f : \YY \to \XX$ is a proper tame coarsely schematic map between FT
DM $\K$-stacks. 
For every $\mcal{N} \in \cat{D}^{-}_{\mrm{qc}}(\YY)$ the morphism  
\[ \DR f_* \bigl( \DR \Hom_{\YY}(\mcal{N}, \mcal{K}_{\YY}) \bigr) \to
\DR \Hom_{\XX} \bigl( \DR f_* (\mcal{N}), \mcal{K}_{\XX} \bigr) \]
in $\cat{D}(\XX)$, which is induced by the ind-rigid trace
$\opn{tr}^{\mrm{ires}}_f : f_*(\mcal{K}_{\YY}) \to \mcal{K}_{\XX}$,
is an isomorphism. 
\end{thmstar}

Theorem$^{(*)}$ \ref{thm:10} implies that for every complex 
$\MM \in \cat{D}^{+}_{\mrm{c}}(\XX)$ there is an ind-rigid trace morphism 
$\opn{tr}^{\mrm{irig}}_{f, \MM} : 
\mrm{R} f_*(f^!(\MM)) \to \MM$  
in $\cat{D}(\XX)$, which is functorial in $\MM$. 

\begin{corstar}\tup{(\cite{Ye10})} \label{cor:286}
Suppose $f : \YY \to \XX$ is a proper tame coarsely schematic map between FT
DM $\K$-stacks. For every $\mcal{M} \in \cat{D}^{+}_{\mrm{c}}(\XX)$ and 
$\mcal{N} \in \cat{D}^{-}_{\mrm{qc}}(\YY)$ the morphism  
\[ \DR f_* \bigl( \DR \Hom_{\YY}(\mcal{N}, f^!(\MM)) \bigr) \to
\DR \Hom_{\XX} \bigl( \DR f_* (\mcal{N}), \mcal{M} \bigr) \]
in $\cat{D}(\XX)$, which is induced by the ind-rigid trace
$\opn{tr}^{\mrm{irig}}_{f, \MM}$, is an isomorphism. 
\end{corstar}

Here is a sketch of the proofs of Theorems$^{(*)}$ \ref{thm:10} and 
\ref{thm:11}, which we are going to refer to as "Residue" and "Duality", 
respectively. 
Take a surjective \'etale map $U \to \XX$ from an affine scheme 
$U$ such that the stack $\YY' := \YY \times_{\XX} U$ is coarsely schematic.
Consider the commutative up to isomorphisms diagram of maps of stacks
\begin{equation*}
\UseTips \xymatrix @C=5ex @R=3ex {
&
\YY'
\ar[dl]_{\pi'}
\ar[dd]^{f'}
\ar[r]
&
\YY
\ar[dd]^{f}
\\
Y'
\ar[dr]_{g'}
\\
&
U
\ar[r]{}
&
\XX
}
\end{equation*}
where $f'$ is gotten from $f$ by base change, and 
$Y'$ is the coarse moduli space of $\YY'$.
The maps $\pi'$ and $g'$ are both proper.  

Because the functor 
$\cat{QCoh}(\XX) \to \cat{QCoh}(U)$ is faithful, it suffices to prove 
``Residue'' and ``Duality'' for the map $f'$.  
Now $Y'$ is a scheme, so the proper map $g' : Y' \to U$ satisfies both
``Residue'' and ``Duality'', by Theorems$^{(*)}$ \ref{thm:1} and 
\ref{thm:2}.

It remains to verify ``Residue'' and ``Duality'' for the proper map 
$\pi' : \YY' \to Y'$. These properties are \'etale local on $Y'$.
Namely let $V'_1, \ldots, V'_n$ be affine schemes, and let
\begin{equation}  \label{eqn:11}
\coprod\nolimits_{i} V'_i \ \to \ Y'
\end{equation}
be a surjective \'etale map. For any $i$ let 
$\YY'_i := \YY' \times_{Y'} V'_i$.
We get this commutative (up to isomorphism) diagram of maps of stacks
\begin{equation*}
\UseTips \xymatrix @C=6ex @R=5ex {
\coprod_{i} \YY'_i 
\ar[r]
\ar[d]_{\coprod_{i}  \pi'_i}
&
\YY'
\ar[d]^{\pi'}
\\
\coprod_{i} V'_i
\ar[r]
&
Y'
} 
\end{equation*}
It is enough to check ``Residue'' and ``Duality'' for the maps
$\pi'_i : \YY'_i \to V'_i$.
Note that the affine scheme $V'_i$ is the coarse moduli space of the stack 
$\YY'_i$. 

According to \cite[Theorem 11.3.1]{Ol} it is possible to choose a covering 
(\ref{eqn:11}) such that 
\begin{equation}
\YY'_i \approx [W_i / G_i] \quad \tup{and} \quad
V'_i \cong W_i / G_i . 
\end{equation}
Here  $W_i$ is an affine scheme, $G_i$ is a finite group acting on $W_i$,  
$[W_i / G_i]$ is the quotient stack, and $W_i / G_i$ is the quotient scheme. 
Moreover, in the tame case we can assume that 
the order of the group $G_i$
is invertible in the ring $\Ga(W_i, \OO_{W_i})$.

We have now reduced the problem to proving ``Residue'' and ``Duality'' for a
map of stacks 
\[ \pi \, : \, \YY = [W / G] \, \to \, V = W / G \, , \]
where $W = \opn{Spec}(A)$ for some ring $A$, $G$ is a finite group acting on
$A$, and in the tame case the order of $G$ is invertible in $A$. 

Let $A^{G}$ be the ring of $G$-invariants inside $A$.
So $A^{G}$ is a FT $\K$-ring, and the quotient 
scheme is $W / G = \opn{Spec}(A^{G})$. 
Consider the {\em skew group ring} $G \ltimes A$; this is the noncommutative 
(NC) ring appearing in \cite[Exercise 9.E]{Ol}. The NC ring $G \ltimes A$ is 
finite over its center $A^{G}$. It is known that 
$\cat{QCoh}(\YY) \approx \cat{Mod}(G \ltimes A)$
as abelian categories, and the functor $\pi_*$ on the geometric side 
goes to the $G$-invariants functor $(-)^G$ on the NC algebraic side. 
 
We finish the proof by using GD for NC rings, see \cite[Chapters 14-18]{Ye7}. 
 
\begin{rem} \label{rem:275}
It is very likely that the ``coarsely schematic'' condition can be removed 
from Theorems$^{(*)}$ \ref{thm:10} and \ref{thm:11}.
This will probably require a better understanding of the geometry of 
algebraic spaces. 
\end{rem}

\begin{rem} \label{rem:276}
We do not know how to handle {\em Artin stacks}. This is because we do 
not understand the {\em smooth functoriality of the squaring operation}. 
\end{rem}

\begin{rem}
Let us end the article with a brief discussion of related work. 
\begin{enumerate}
\item There is a preprint \cite{Ni} by F. Nironi from 2008 on GD for DM stacks.
It has neither been updated nor published. 
The details in that paper are not clear to us.

\item J. Hall and D. Rydh wrote several papers dealing with derived categories 
on stacks. In their paper \cite{HR} from 2017 they prove a version of GD for a 
finite faithfully flat representable map $f : \YY \to \XX$ of Artin stacks. 

\item A. Neeman wrote the paper \cite{Ne2}, last updated in 2017.
It deals with GD in great generality, and also in a very abstract manner. 
The geometric objects considered in it range from schemes to Artin stacks; and 
the maps between them are required to be concentrated and compactifiable.  
For any such map $f : \YY \to \XX$ the functor $\mrm{R} f_*$ is shown to 
have a right adjoint $f^{\times}$; and under certain further conditions one has 
$f^{\times} \cong f^!$. According to Neeman (in a private communication), his 
work implies that our Corollary \ref{cor:286} holds, when $f : \YY \to \XX$ is 
a concentrated proper map between DM stacks. 
\end{enumerate}

There might be other work on global GD, perhaps also from the direction of 
derived algebraic geometry, but we are not aware of any at present. 
\end{rem}
