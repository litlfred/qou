---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.996
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
In this paper we fix our ground field to be $\mathbb{C}$. A fusion category is a rigid semisimple linear monoidal category with finitely many isomorphism classes of simple objects and whose unit object is simple. A basic example of a fusion category is the category of representations of a finite group; in this way the study of fusion categories can be regarded as a common generalization of group theory and representation theory. For an overview on fusion categories, see \cite{muger2008tensor, calaque2004lectures}.

Many of the basic results on fusion categories were obtained by Etingof, Nikshych and Ostrik in \cite{eno02-ofc}. These results include the fact that the quadruple dual functor is canonically isomorphic to the the identity functor, positivity of the paired dimensions, and Ocneanu rigidity.

These results were proved in \cite{eno02-ofc} using the theory of weak Hopf algebras. The idea is that since every fusion category can be expressed as the category of finite-dimensional representations of some semisimple weak Hopf algebra \cite{eno02-ofc}, one may prove results about fusion categories by translating them into the language of weak Hopf algebras. One motivation for this paper, building on \cite{hh09-snbfcor3, k05-aes, muger2003-subfactors, bv13-ocfc}, was to give a unified account of how these results can be proved directly in the fusion category itself, using the graphical calculus of string diagrams \cite{js91-gtc, js-gtcii, s11-sgc}. 

Another motivation has been the string-net description for the vector spaces in the Turaev-Viro model of 3-dimensional topological quantum field theory \cite{kirillov2011-string-net}, where the graphical calculus plays a prominent role. 

However, the main motivation has been to investigate the conjecture of Etingof, Nikshych and Ostrik, that every fusion category admits a pivotal structure \cite{eno02-ofc}, as we now explain.

\subsection*{The pairing convention}
In the string diagram calculus, the objects $V$ of the fusion category $\cat{C}$ are used as labels for strands in the plane. The main feature is rigidity --- the notion that the strands are oriented, and that there are left and right dual structure maps, drawn as
\[
 \left( \ig{d58.pdf}\, , \, \ig{d59.pdf} \right) \quad \text{and} \quad \left( \ig{d56.pdf} \, , \, \ig{d57.pdf} \right)
\]
respectively, satisfying `snake equations' such as
\[
\ba \ig{straight} \ea = \ba \ig{curvy} \ea.
\]
One can also form closed loops, which involves pairing left and right dual structure maps together:
\begin{equation} \label{loop_a}
\ba \ig{i3.pdf} \ea \in \Hom(1,1) \,.
\end{equation}
In order to make this well-defined, it is usually imagined that one needs a {\em pivotal structure} on the fusion category, that is, a monoidal natural isomorphism $\gamma : \id \Rightarrow **$ from the identity functor on the fusion category to the double dual functor (see Section \ref{Explicit_equations}). Etingof, Nikshych and Ostrik have conjectured that such a structure always exists:

\begin{conjecture}[\cite{eno02-ofc}] Every fusion category admits a pivotal structure.
\end{conjecture}

The main idea we use in this article is that, in fact, there is a well-defined way to make sense of diagrams which employ both left and right dual structure maps together, such as \eqref{loop_a}, {\em even without} a pivotal structure. The rule (at least for simple objects $V$) is that if left and right dual structure maps appear in a diagram, then they cannot be chosen independently but must be correlated in the following way: when paired together, they must give the {\em fusion dimension} of $V$. The fusion dimension of $V$ is a certain positive number canonically associated to $V$ in a fusion category which we define in Section \ref{fusion_frobenius}; it does not make use of a pivotal structure. We call this the pairing convention, and it allows us to unambiguously evaluate diagrams such as
\[
\ig{d55.pdf}
\]
in a `bare' fusion category, which would otherwise not be well-defined. 

\subsection*{Pivotal operators}

Using the pairing convention, we can give a simple diagrammatic definition of the {\em pivotal operators} of a fusion category, which are certain canonically defined linear maps
\[
 T^A_{BC} : \Hom(A, B \otimes C) \rightarrow \Hom(A, B \otimes C)
\]
associated to every triple of objects $A$,$B$ and $C$ in a fusion category. One advantage of our framework is that these maps are canonical, not depending on any choices of duals for their definition. The pivotal operators play the role of the double dual functor, and the string diagram calculus then gives a simple proof that $T^A_{BC}$ squares to the identity, see Theorem \ref{piv_involution_thm}. The idea of this graphical proof is originally due to Hagge and Hong \cite{hh09-snbfcor3}.

\subsection*{Main results}
Our main results are as follows. Firstly, we show that every fusion category $\cat{C}$ over $\mathbb{C}$ comes equipped with a canonical monoidal endofunctor $\mathcal{T}$, whose underlying functor is the identity, whose action on the hom-sets $\Hom(X_i, X_j \otimes X_k)$ between tensor products of simple objects is given graphically by the pivotal operators, and which squares to the identity (Theorem \ref{piv_operator_C}). 

Secondly, we use this viewpoint to give graphical proofs of the following results from \cite{eno02-ofc}: 
\begin{itemize}
\item the quadruple dual is monoidally naturally isomorphic to the identity (Corollary \eqref{explicit_eno_cor})
\item positivity of the paired dimensions (Theorem \ref{realpositive}), 
\item a pseudo-unitary fusion category is spherical (Corollary \ref{pseudo_cor})
\item the sphericalization of a fusion category is spherical (Corollary \ref{spher_cor})
\item Ocneanu rigidity, i.e. the vanishing of the Davydov-Yetter cohomology (Theorem \ref{ocneanu})
\end{itemize}
Thirdly, in Theorem \ref{formula_piv} we explicitly compute the pivotal operators in terms of the associators of the fusion category as a product of the {\em pivotal indicators}, which we introduce in Section \ref{piv_ind_sec}, with the {\em apex associator monodromy}, which we introduce in Section \ref{Form_piv_op}. 

Finally, we characterize pivotal structures as solutions of an explicit set of equations over the complex numbers (Theorem \ref{piv_structure_thm}), refining a formula of Wang \cite[Prop 4.17]{wang2010-topological}.


\subsection*{Outline of paper}

In Section \ref{string_sec} we give our conventions on string diagrams. In Section \ref{stss} we define the pairing convention and the pivotal operators, show that the paired dimensions are positive, and show how to interpret the pivotal operators as a monoidal functor. In Section \ref{explicit_sec} we compute the pivotal operators explicitly in terms of the associators. In Section \ref{piv_struc_sec} we express pivotal structures as solutions of certain explicit algebraic equations, and formulate the sphericalization of a fusion category from our approach. Finally in Section \ref{ocneanu_sec} we give a graphical proof of Ocneanu rigidity.
