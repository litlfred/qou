---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.985
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
In their seminal work, Chuang and Rouquier introduced $\fsl_2$ categorifications on abelian categories \cite{CR}.  Their definition mirrors the notion of an $\fsl_2$ representation on a vector space: weight spaces are replaced by weight categories, Chevalley generators acting on them are replaced by Chevalley functors, and Lie algebra relations are replaced by isomorphisms of functors.  But, crucially, these isomorphisms are part of the ``higher data'' of categorification.


The richness of this theory was immediately evident.  As a corollary of an $\fsl_2$ categorification on representations of symmetric groups in positive characteristic, Chuang and Rouquier proved Broue's abelian defect conjecture in that case.  The essential tool allowing them to do this is the Rickard complex, which is a categorical lifting of the reflection matrix in $\SL_2$, and provides a derived equivalence between opposite weight categories.

Subsequently, Rouquier and Khovanov-Lauda vastly generalised this theory to  quantum symmetrisable Kac-Moody algebras $U_q(\fg)$ \cite{Rou2KM,KLI,KLII}.  Let $\kk$ be any field.  A graded abelian $\kk$-linear category $\cC$ endowed with a categorical representation of $U_q(\fg)$ possesses a family of Rickard complexes $\Theta_i$, indexed by the simple roots of $\fg$, acting on the derived category $D^b(\cC)$.  

Henceforth let $\fg$ be a semisimple simply-laced Lie algebra of finite type with Dynkin diagram $I$, $W$  its Weyl group, and $B$ its Artin braid group. Let $\cC$ be a categorical representation of $U_q(\fg)$ as in the previous paragraph.  Cautis and Kamnitzer proved that Rickard complexes satisfy the braid relations, as conjectured by Rouquier \cite{CK3}.  This defines an action of $B$ on $D^b(\cC)$, and is our main object of study.    

Categorical braid group actions defined via Rickard complexes have many significant applications.  For example, in low dimensional topology, the type A link homology theories (in particular Khovanov homology) emerge as a byproduct of these types of categorical braid group actions \cite{CK, CKII, LQR}.  In mirror symmetry, the theory of spherical twists plays an important role, and these all arise from categorical $\fsl_2$ representations \cite{ST01}.  

To describe our first theorem, recall that minimal categorifications are certain distinguished categorifications of simple representations.  On these the Rickard complex $\Theta_i$  is t-exact up to shift \cite[Theorem 6.6]{CR}.  Notice that this is a result about $\fsl_2$ categorifications, and in fact, this is one of Chuang-Rouquier's key technical results which they use to prove the derived equivalence.  

We generalise this result to $U_q(\fg)$, where we show that the composition of Rickard complexes corresponding to a positive lift of the longest element $w_0 \in W$ is t-exact up to shift on any isotypic categorification.  More precisely:

\begin{namedtheorem}[A][Theorem \ref{thm:mincat} \& Corollary \ref{cor:mainthm}]\label{thm:A}
Let $\cC$ be a categorical representation of $U_q(\fg)$ categorifying an isotypic representation of type $\lambda$, where $\lambda$ is a dominant integral weight.  Let $\mu$ be any weight, and let $n$ be the height of $\mu-w_0(\lambda)$.  Then the derived equivalence
\begin{align*}
\Theta_{w_0}\bone_\mu[n]:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})
\end{align*}
is t-exact.  
\end{namedtheorem}

This theorem is the technical heart of the paper.
In order to prove it we introduce a new combinatorial notion of ``marked words'' (Section \ref{sec:commrels}).  This allows us to use relations between $\Theta_i$ and Chevalley functors established by Cautis and Kamnitzer to deduce  the commutation relations involving $\Theta_{w_0}$ (Proposition \ref{prop:mainrel}).  We then use these relations to prove the theorem by induction on $n$.     

Our second theorem describes $\Theta_{w_0}$ on an arbitrary categorical representation of $U_q(\fg)$, also generalising a result of Chuang-Rouquier in the case $\fg=\fsl_2$.  Indeed, their study of the Rickard complex on an $\fsl_2$ categorification led them to define the notion of a ``perverse equivalence'' \cite{CRperv}.  

Consider an equivalence of triangulated categories $\sF:\cT\to\cT'$ with t-structures \cite{BBD}.  Suppose further that $\cT$ (respectively $\cT'$) is filtered by thick triangulated subcategories 
\begin{align*}
0\subset \cT_0 \subset \cdots \subset \cT_r=\cT, \quad 0\subset \cT_0' \subset \cdots \subset \cT_r'=\cT',
\end{align*}
and $\sF$ is compatible with these filtrations (cf. Section \ref{sec:pervdef} for precise definitions).  Then, roughly speaking,  $\sF$ is a perverse equivalence if on each subquotient $\sF:\cT_i/\cT_{i-1} \to \cT_i'/\cT_{i-1}'$ is t-exact up to shift.  

Since their introduction, perverse equivalences have proven useful in various contexts (e.g. representations of finite groups \cite{Cra-Rou}, geometric representation theory and mirror symmetry \cite{Agan}, and algebraic combinatorics \cite{GJN}).  Our second theorem shows that perverse equivalences are ubiquitous in categorical representation theory:

\begin{namedtheorem}[B][Theorem \ref{thm:perveq}]\label{thm:B}
Let $\cC$ be a categorical representation of $U_q(\fg)$, and let $\mu$ be any weight.  The derived equivalence
$
\Theta_{w_0}\bone_\mu:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})
$
is a perverse equivalence with respect to a Jordan-H\"older or isotypic filtration of $\cC$.  
\end{namedtheorem}

Note that if $J\subseteq I$ is a subdiagram, and $w_0^J$ is corresponding longest element, then this theorem implies that $\Theta_{w_0^J}\bone_\mu$ is a perverse equivalence for any $J$.  We also remark that our argument go through  in the ungraded setting, where $\cC$ is a categorical representation of $\fg$.  

Let us explain the filtration arising in Theorem B more precisely.  We apply Rouquier's Jordan-H\"older theory for representations of $2$-Kac-Moody algebras to our setting \cite{Rou2KM}.  We thus obtain a filtration of $\cC$ by Serre subcategories, 
\begin{align*}
0\subset \cC_0 \subset \cdots \subset \cC_r=\cC,
\end{align*}
such that each factor $\cC_i$ is a subrepresentation, and each subquotient $\cC_i/\cC_{i-1}$ categorifies either a simple module (Theorem \ref{thm:JH}) or an isotypic component (Remark \ref{rem:isofilts}).  Then   $
\Theta_{w_0}\bone_\mu$ is a perverse equivalence with respect to the filtration whose $i$-th filtered component consists of complexes in $D^b(\cC_\mu)$ with cohomology supported in $\cC_i$.

We remark that in the case $\fg=\fsl_2$ this gives a more conceptual proof of a result of Chuang-Rouquier \cite[Proposition 8.4]{CRperv}.  If $\cC$ is the tensor product categorification of the $n$-fold tensor product of the standard representation of $\fsl_n$, we recover a theorem of the third author \cite{LosCacti}.  We explain this in Example \ref{ex:catO}, where we show how to interpret the filtration on the principal block of the BGG category $\cO$ using the Robinson-Schensted correspondence. 

In fact, the third author and Bezrukavnikov formulated a principle that suitable categorical braid group representations should have a ``crystal limit'' \cite[Section 9]{BLet}.  As an application of our results we can make this precise in the setting of categorical representations of $U_q(\fg)$.


Recall that to an integrable representation $V$ of $U_q(\fg)$, Kashiwara associated its crystal basis $\bB_V$ \cite{Kash90}, which is closely related to Lusztig's canonical basis \cite{GL92}.  If $V$ is categorified by $\cC$ then there is a natural identification $\bB_V=\Irr(\cC)$, the set of isomorphism classes of simple objects in $\cC$ up to shift (cf. Proposition \ref{prop:cryst})	.

One of the most important features of the theory is the existence of a tensor product, endowing the category of crystals with a monoidal structure. The commutator of crystals is controlled by a group called the cactus group, just as $B$ controls the commutator in the category of representations of $U_q(\fg)$ \cite{HK06}.  There is also an internal cactus group action, mirroring Lusztig's internal braid group action on $V$.  Indeed, there is a cactus group $C$ associated to $\fg$ (or rather to its Dynkin diagram $I$), which can be presented by generators $c_J$ indexed by connected subdiagrams $J \subseteq I$ (cf. Section \ref{sec:cactus}).  Then $C$ acts on $\bB_V$ via the so-called Sch\"utzenberger involutions (cf. Theorem \ref{thm:cactact}).  

So, starting with an integrable representation $V$ of the quantum group we obtain:
an action of $B$ on V,
a $\fg$-crystal $\bB_V$, and
an action of $C$ on $\bB_V$.
We schematically picture this situation as follows:
\[
\begin{tikzcd}
U_q(\fg) \curvearrowright V  \ar[rr]  \ar[d] &  & B \curvearrowright V  \arrow[d, dashed,"?"] \\
                        
\fg\text{-crystal } \bB_V \ar[rr]            &  & C       \curvearrowright    \bB_V        
\end{tikzcd}
\]
Naturally one asks: can we ``crystallise'' the braid group action on $V$ directly to obtain the cactus group action on $\bB_V$?  Our results allow us to answer this in the affirmative.    

The key point is that a perverse equivalence $\sF:\cT \to \cT'$ induces a bijection $\Irr(\cT^\heartsuit) \leftrightarrow \Irr((\cT')^\heartsuit)$, where $\cT^\heartsuit$ denotes the heart of the t-structure. In the setting of Theorem B, we obtain a bijection $\varphi_I:\Irr(\cC) \to \Irr(\cC)$.  In fact, if $J\subseteq I$ is a subdiagram and $\fg_J \subseteq \fg_I$ is the corresponding Lie subalgebra, we can regard $\cC$ as a categorical representation of $U_q(\fg_J)$ by restriction.  By Theorem B we also obtain a bijection $\varphi_J:\Irr(\cC) \to \Irr(\cC)$.

\begin{namedtheorem}[C][Theorem \ref{thm:cactus} \& Theorem \ref{thm:agree}]\label{thm:C}
Let $\cC$ be a categorical representation of $U_q(\fg)$, categorifying the integrable representation $V$.  The assignment $c_J \mapsto \varphi_J$ defines an action of $C$ on $\bB_V=\Irr(\cC)$, and this  agrees with the combinatorial action arising from Sch\"utzenberger involutions.  
\end{namedtheorem}

We thus obtain the sought-after crystalisation process for braid groups:
$$
B \curvearrowright V \quad\rightsquigarrow\quad B \curvearrowright D^b(\cC) \quad\rightsquigarrow\quad C \curvearrowright \Irr(\cC),
$$
which  associates a cactus group set $\Irr(\cC)$ to the braid group representation of $B$ on $V$.  The first appearance of such a crystalisation process is in the work of the third author, where a cactus group action on $W$ is constructed \cite{LosCacti}.  It's an interesting  question to crystallise the braid group action without appealing to categorical representation theory.

Finally we remark that perversity of Rickard complexes, and more specifically the t-exactness of $\Theta_{w_0}$ on isotypic categorifications as in Theorem A, is a fruitful vantage from which to view results in algebraic combinatorics.  

For example, we show in Section \ref{sec:typeA} how to use this to easily recover theorems of Berenstein-Zelevinsky \cite{BZ96}  and Stembridge \cite{Stem96}, namely that the action of $w_0\in S_n$ 
on the Kazhdan-Lusztig basis of a Specht module of $S_n$ is governed by the evacuation operator  on standard Young tableaux.  We note that this theorem was earlier proven by Mathas in slightly different form (without explicit reference to the evacuation operator, and credited to J.J. Graham) \cite[Theorem 3.1]{Mathas}, and a similar result was shown even earlier by Lusztig in 1990 \cite[Corollary 5.9]{LusCBII}.

As another example, we use our methods to also recover Rhoades' Theorem that the Coxeter element $(1,2,\hdots,n) \in S_n$ acts on the  Kazhdan-Lusztig basis of a Specht module associated to a rectangular partition by the promotion operator.  This point of view led us to generalise Rhoades' result to arbitrary partitions \cite{GY1}, and isolate the class of permutations (the separable permutations) for which such results can hold \cite{GY2}.
