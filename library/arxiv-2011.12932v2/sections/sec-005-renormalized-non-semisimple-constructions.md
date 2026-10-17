---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-005-renormalized-non-semisimple-constructions
section_title: "Renormalized non-semisimple constructions"
section_number: null
pages: 4-7
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.97
---
\label{SS:renormalized_non-semisimple}

A key ingredient that was missing from these early attempts at non-semisimple constructions was the theory of \textit{modified traces} developed by Geer and Patureau together with many collaborators, among which Turaev \cite{GPT07}, Kujawa \cite{GKP10}, and Virelizier \cite{GPV11}. Indeed, one way to explain the problems we face when trying to generalize Turaev's TQFT construction is that the categorical trace operation, which associates scalars to endomorphisms in a ribbon category $\calC$, becomes highly degenerate as soon as $\calC$ is non-semisimple. For instance, in this case the categorical trace of every endomorphism of any projective object is zero. Since this operation is pervasive in all quantum topological constructions, invariants of closed oriented 3-manifolds are bound to vanish a lot in non-semisimple settings. The idea behind \textit{renormalization} consists in replacing this highly degenerate operation with a non-degenerate analogue, called modified trace, which in general is only defined on proper tensor ideals of $\calC$. This approach was pioneered by Costantino, Geer, and Patureau \cite{CGP12} in a different non-semisimple setting with respect to Lyubashenko's. Indeed, an alternative (and also potentially non-semisimple) generalization of Turaev's notion of modular category, called \textit{relative modular category}, exists. Relative modular categories are so different from Lyubashenko's modular categories that the two notions intersect exclusively along Turaev's modular categories. In other words, if a category $\calC$ is both modular in the sense of Lyubashenko and relative modular, then it is modular in the sense of Turaev. The main examples of relative modular categories are associated with a different family of quantum groups, called \textit{unrolled quantum groups}. Starting from a relative modular category, one can define a topological invariant of closed oriented 3-manifolds decorated with so-called \textit{admissible cohomology classes} which is called the \textit{CGP invariant}. Focusing on the unrolled quantum group $U^H_q \fsl_2$, this construction was extended for the first time to non-semisimple graded TQFTs in \cite{BCGP14}. The adaptation of this result to arbitrary relative modular categories, as well as a complete extension to graded ETQFTs in general, is presented in \cite{D17}.

Following the success of these constructions, renormalization was soon applied to the theory of Hennings and Lyubashenko. This was done at first without any mention to modified traces, and thus independently of the work of Geer and Patureau, by Murakami \cite{M13}. The resulting invariants of so-called \textit{admissible knots} in 3-manifolds were extended to invariants of \textit{admissible links} in 3-manifolds, and reformulated in terms of modified traces, by Beliakova, Blanchet, and Geer \cite{BBG17}. Both of these works deal exclusively with the case of the restricted quantum group $\bar{U}_q \fsl_2$. A generalization of these constructions to arbitrary finite-dimensional factorizable ribbon Hopf algebras, as well as corresponding TQFT extensions, was first obtained in \cite{DGP17}. The adaptation of this theory to the general framework of Lyubashenko was later achieved in \cite{DGGPR19}, where TQFTs are constructed starting from arbitrary, potentially non-semisimple modular categories. This result recovers both Turaev's TQFTs, in the semisimple case, and Lyubashenko's mapping class group representations, in general. It should be remarked, however, that the renormalization process changes the underlying 3-manifold invariants drastically. In particular, a complete answer to question $(i)$ is that Lyubashenko's invariants cannot be extended to TQFTs, but that his mapping class group representations can.

The invariants and representations arising from the CGP and the renormalized Lyubashenko constructions are related to each other, see \cite{DGP18} for a discussion of the quantum group case. Both theories exhibit behaviors which mark a sharp contrast with respect to the semisimple case. First of all, the CGP invariant associated with $U^H_q \fsl_2$ for $q=i$ recovers the abelian Reidemeister torsion, which completely classifies lens spaces \cite{BCGP14}. This could not be achieved by any Witten--Reshetikhin--Turaev invariant. Furthermore, the action of Dehn twists along simple closed curves on states spaces associated with both $U^H_q \fsl_2$ and $\bar{U}_q \fsl_2$ have infinite order \cite{BCGP14,DGGPR20}. This is also something that never happens in the semisimple case, and which provides a positive answer to question $(ii)$. We point out that, to the best of our knowledge, these remarkable properties of Lyubashenko's mapping class group representations had never been noticed before the completion of the TQFT program.

We finish this section by stressing an important feature of non-semisimple constructions. The admissiblity conditions we mentioned in several places have to do with the fact that modified traces are generally defined only on proper tensor ideals. This means that, if we want to add them to our toolbox, we need decorations of 3-manifolds to meet certain requirements. Typically, decorations carry labels given by objects of a category $\calC$, and we need at least one of these labels to belong to the tensor ideal supporting the modified trace. It should be noted that these constraints also affect cobordism categories. Indeed, certain decorated cobordisms have to be removed from sets of morphisms, and this operation usually breaks the rigidity of a few objects. In other words, certain decorated surfaces are not dualizable in these so-called \textit{admissible decorated cobordism categories}. However, the symmetric monoidal structure induced by disjoint union remains intact, and so the resulting TQFTs are indeed symmetric monoidal in the sense of Atiyah.


\section{Turaev's notion of modular category}\label{S:T-mod_cat}

Using the language of \cite{EGNO15}, a \textit{T-modular category} (T for Turaev) is a ribbon fusion category whose S-matrix is invertible. The definition originally appeared in \cite[Sec.~II.1.2]{T94} in a slightly more general form, but the version reported here has since become rather standard (compare with \cite{BK01,TV17}). In order to better grasp this notion, let us proceed to unpack the terminology. 

First of all, a \textit{ribbon} category $\calC$ is a braided rigid monoidal category with a twist. This means a ribbon category comes equipped with:
\begin{enumerate}
 \item a tensor product $\otimes : \calC \times \calC \to \calC$ and a tensor unit $\one \in \calC$;
 \item duality morphisms $\lev_X : X^* \otimes X \to \one$, $\lcoev_X : \one \to X \otimes X^*$, and $\rev_X : X \otimes X^* \to \one$, $\rcoev_X : \one \to X^* \otimes X$ for every $X \in \calC$;
 \item braiding morphisms $c_{X,Y} : X \otimes Y \to Y \otimes X$ for all $X,Y \in \calC$;
 \item twist morphisms $\theta_X : X \to X$ for every $X \in \calC$.
\end{enumerate}
All these structure data are subject to several axioms, which can be found explicilty in \cite[Sec.~2.1, 2.10, 8.1, 8.10]{EGNO15}, but which can also be understood efficiently using a more visual approach. Indeed, morphisms of a ribbon category can be represented using an extension of \textit{Penrose graphical notation} and \textit{string diagrams}. Structure morphisms listed above are represented by elementary diagrams
\begin{align*}
 \id_X &= \pic{graphical_rep_id} &
 \id_{X^*} &= \pic{graphical_rep_id_dual} \\[2pt]
 \lev_X &= \pic{graphical_rep_lev} &
 \lcoev_X &= \pic{graphical_rep_lcoev} \\[2pt]
 \rev_X &= \pic{graphical_rep_rev} &
 \rcoev_X &= \pic{graphical_rep_rcoev} \\[2pt]
 c_{X,Y} &= \pic{graphical_rep_braiding} &
 \theta_X &= \pic{graphical_rep_twist}
\end{align*}
In general, a morphism $f : X_1 \otimes \ldots \otimes X_m \to Y_1 \otimes \ldots \otimes Y_n$ which is not expressed as a combination of structure morphisms is simply placed inside a box 
\begin{equation}\label{E:coupon}
 f = \pic{graphical_rep_coupon}
\end{equation}
These diagrams are read from bottom to top.\footnote{Remark that the convention used here for orientations is opposite to the one used by Turaev, but also widely used.} Composition is given by vertical stacking, while tensor product corresponds to horizontal juxtaposition. Then, the axioms of a ribbon category translate precisely to the invariance of this diagrammatic calculus under isotopy and framed Reidemeister moves.

Next, let us fix an algebraically closed\footnote{This condition is not necessary, but convenient.} field $\Bbbk$. Throughout this paper, we will use the term ``linear'' as a shorthand for ``$\Bbbk$-linear''. Then, let us consider a linear category $\calC$, which is a category whose sets of morphisms carry vector space structures making compositions into bilinear maps. We say that $\calC$ is \textit{finite} if it is equivalent to the category of finite-dimensional representations of a finite-dimensional algebra. This definition is rather implicit, as no algebra is attached to $\calC$, but it can be reformulated in more explicit terms. In fact, as explained in \cite[Def.~1.8.6]{EGNO15}, $\calC$ is finite if and only if it is abelian and:
\begin{enumerate}
 \item it has a finite number of isomorphism classes of simple objects;
 \item it has enough projectives;
 \item its objects have finite lenght; 
 \item its morphism spaces have finite dimension.
\end{enumerate}
A \textit{fusion category} is a finite semisimple monoidal linear category. Therefore, it is this assumption that encodes the semisimplicity of T-modular categories. 

Finally, for every ribbon fusion category we can define an \textit{S-matrix} given by 
\[
 S(\calC) := \left( \pic{S-matrix} \right)_{i,j \in I}
\]
where $\Gamma(\calC) = \left\{ V_i \mid i \in I \right\}$ is a set of representatives of isomorphism classes of simple objects of $\calC$. We say a ribbon fusion category $\calC$ is T-modular if $S(\calC)$ is invertible. This requirement can be understood as a non-degeneracy condition for the braiding of a ribbon fusion category.

We finish this section with an additional definition. The \textit{Müger center} $M(\calC)$ of a ribbon category $\calC$ is the full subcategory of so-called \textit{transparent} objects of $\calC$, that is, $X \in M(\calC)$ if $c_{Y,X} \circ c_{X,Y} = \id_{X \otimes Y}$ for every $Y \in \calC$. The Müger center of a ribbon category $\calC$ is said to be trivial if every transparent object of $\calC$ is isomorphic to a direct sum of copies of the tensor unit $\one$. Then, a ribbon fusion category $\calC$ has trivial Müger center if and only if $S(\calC)$ is invertible \cite[Prop.~1.1]{B00}. This equivalent non-degeneracy condition for the braiding of $\calC$ will be useful later on.
