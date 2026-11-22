---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-6
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.983
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
The present work forms an initial step in a formalism for topological quantum field theory using stratified spaces. This larger program proposes to understand locality in topological quantum field theory by a fusion of the algebra of factorization homology and the geometry of stratifications. Before delineating this step and, briefly, this future program, we first review the subject of factorization homology.

\medskip

Factorization homology is, heuristically, a procedure which takes an $n$-manifold $M$ and an algebraic input $A$, such as an $\cE_n$-algebra, and produces an object $\int_MA$. The manifold provides the gluing data, the algebra provides the gluing rules, and one can think of integrating the multiplication of the algebra over the gluing data of the manifold. Viewing this object as an invariant of the manifold, the procedure generalizes usual homology theories; viewing the object as an invariant of the algebra, it generalizes Hochschild homology when the manifold is the circle and offers a natural repository for traces or index-type invariants.

\medskip

Such a procedure was introduced for algebraic varieties by Beilinson \& Drinfeld in their work on an algebro-geometric formalism for conformal field theory; see \cite{bd} and \cite{fg}. In \S5.5 of~\cite{HA}, Lurie defined a topological analogue of their construction -- known as factorization homology or topological chiral homology -- and this topological construction likewise generalizes the labeled configuration spaces of Salvatore \cite{salvatore} and Segal \cite{segallocal}. The main theorem of this area, non-abelian Poincar\'e duality, naturally generalizes the James construction and configuration space models of mapping spaces dating to the 1970s in work of McDuff \cite{mcduff} and others -- see \cite{Fact} for a more detailed history.

\medskip

Another recent catalyst for study in this area has been the approach of Costello \& Gwilliam to perturbative quantum field theory in \cite{kevinowen}. In mathematical approaches to topological field theory at least since Atiyah in \cite{atiyah}, it is common to organize the formalism around the functoriality of the state spaces in the theory. This choice leads to cobordisms and, proceeding deeper, higher categories of cobordisms after Baez \& Dolan in \cite{baezdolan}. In contrast, Costello \& Gwilliam, following the factorization algebra structures of \cite{bd}, codify their theory around the structure of observables, or operators, rather than state spaces. In their work, the earlier renormalization machinery of \cite{kevin} is married with the factorization point of view; the intuitive factorization homology procedure becomes a way of constructing a candidate object $\int_MA$ of global observables on a space-time $M$ from the algebra of observables $A$ on Euclidean space. This candidate object $\int_MA$ is intended to accurately capture the global observables on $M$ if the quantum field theory is perturbative. They prove a quantization theorem, designed as a mathematical formulation of physicists methods of perturbative renormalization, using the Batalin--Vilkovisky formalism applied to derived symplectic geometry. From this quantization theorem they construct a number of interesting examples of such perturbative field theories.

\medskip

The structural favoring of observables over state spaces has geometric consequences, namely a favoring of open embeddings over cobordisms. Dual to restricting fields, observables can extend by zero. This is unlike state spaces, where there is no procedure for extension by zero, no naturality with respect to open embeddings, and no values for non-compact manifolds. The cobordism hypothesis with singularities, after Baez--Dolan \cite{baezdolan} and Lurie \cite{cobordism}, gives a proposed classification for certain topological field theories in terms of their state spaces. With this in mind, one can ask if there is a similar classification which applies to this class of topological field theories constructed in \cite{kevinowen} in terms of the Batalin--Vilkovisky formalism, in terms of their observables. Our first main result, Theorem \ref{hmlgy=FH}, can be viewed as just such a classification.

\medskip

In the present work, we lay the foundations for a general theory of factorization homology, following the outline of \cite{Fact} and after the originating work of Lurie in \cite{HA}. We do this for stratified spaces and, more generally, $\cB$-manifolds, where $\cB$ is a collection of basic singularity types endowed with a tangential structure, applying the theory of stratified spaces and tangential structures developed in \cite{aft1}. This extra level of generality is carried out for two reasons. First, the theory without stratifications is related to observables on space-time in perturbative field theory; adding nontrivial stratifications allows one to incorporate boundary conditions and defects in this theory, such as Wilson line operators in Chern--Simons. The second reason concerns the extension of our theory outside of the perturbative range in quantum field theories; our larger program in progress (see \cite{striation} and the papers that follow) uses stratifications to effect this greater generality.

\medskip

We now turn to a linear overview of contents of the current work, which has three parts.

\medskip

In the first part, we cover the definition (Definition \ref{def:fact-hmlgy}) of factorization homology as a Kan extension from $\disk(\cB)$-algebras to $\cB$-manifolds, and we prove its existence. The first main result is that the symmetric monoidal and underlying left Kan extensions are equivalent, and that there is therefore a comprehensible formula (Theorem \ref{fact-explicit}) which computes factorization homology; this generalizes a formula for usual homology. To establish this existence result and this explicit formula we prove a general result giving conditions for existence and agreement of symmetric monoidal and underlying left Kan extensions in Lemma \ref{shape-existence}. To verify the conditions of this lemma requires proving that the $\oo$-category $\disk(\cB)_{/X}$ of basic singularity types embedded in a manifold is sifted, Corollary \ref{quittersifted}; our proof makes use of a localization result relating discrete and topological categories of embedded disks and of Dugger--Isaksen's work in \cite{Dugger--Isaksen}.

\medskip

Together with this explicit existence, we prove in Theorem \ref{:(} the existence of push-forwards for factorization homology along constructible bundles of stratified spaces. An immediate consequence is a Fubini theorem for factorization homology, Corollary \ref{fubini}. Along with an analysis of factorization homology in the case of a closed interval, which we identify as a relative tensor product in Proposition \ref{tensor-prod}, these results culminate in a main structural theorem. To state it, we require some terminology: let $\cB$ be an $\oo$-category of basic singularity types and $\mfld(\cB)$ the collection of stratified spaces locally modeled on $\cB$; let $\cV$ be a symmetric monoidal $\oo$-category which is $\ot$-sifted cocomplete (see Definition \ref{def-siftedcocplt}). Below, we next define the collection of $\cV$-valued homology theories $\bcH(\mfld(\cB), \cV)$ as a full $\infty$-subcategory of symmetric monoidal functors $\Fun^{\ot}(\mfld(\cB),\cV)$ satisfying the following symmetric monoidal generalization of the Eilenberg--Steenrod axioms.


\begin{definition}\label{homology}[Definition \ref{homology}]
The $\infty$-category of \emph{homology theories (over $X$)} is the full $\infty$-subcategory
\[
\bcH\bigl(\mfld(\cB)_{/X},\cV\bigr)~\subset~\Fun^\ot\bigl(\mfld(\cB)_{/X},\cV\bigr)
\]
consisting of those $H$ that satisfy the following two properties:
\begin{itemize}
\item {\bf $\ot$-Excision:} 
Let $W \cong W_- \underset{\RR\times W_0} \bigcup W_+$ denote a collar-gluing among $\cB$-manifolds over $X$.
Then the canonical morphism~(\ref{exc-compare})
\begin{equation}\label{ot-excision}
H(W_-)\underset{H(W_0)}\bigotimes H(W_+)\xra{~\simeq~} H(W)
\end{equation}
is an equivalence in $\cV$.
\item {\bf Continuous:}
Let $W_0\subset W_1\subset \dots \subset X$ be a sequence of open sub-stratified spaces of $X$ with union denoted as $\underset{i\geq 0} \bigcup W_i = : W$.
Then then the canonical morphism
\begin{equation}\label{continuous}
\colim\Bigl(H(W_0) \to H(W_1)\to \dots \Bigr)\xra{~\simeq~} H(W)
\end{equation}
is an equivalence in $\cV$.

\end{itemize}
Absolutely, the $\infty$-category of \emph{homology theories (for $\cB$-manifolds}) is the full $\infty$-subcategory
\[
\bcH\bigl(\mfld(\cB),\cV\bigr)~\subset~\Fun^\ot\bigl(\mfld(\cB),\cV\bigr)
\]
consisting of those $H$ for which, for each $\cB$-manifold $X$, the restriction $H_{|\mfld(\cB)_{/X}}$ is a homology theory for $X$.  

\end{definition}

The preceding definition generalizes to stratified spaces a notion introduced in \cite{Fact}; see also the introduction of that work for a discussion of the present concepts, such as $\ot$-excision. We can now state our main result, which generalizes the main result of {\it loco citato} from manifolds to stratified spaces.

\begin{theorem}[Theorem \ref{hmlgy=FH}]
There is an equivalence between $\disk(\cB)$-algebras in $\cV$ and $\cV$-valued homology theories for $\cB$-manifolds
\[\Alg_{\disk(\cB)}(\cV) \simeq \bcH(\mfld(\cB),\cV)\] defined by sending a $\disk(\cB)$-algebra $A$ to the factorization homology $\int A$.
\end{theorem}

Here the $\ot$-excision property of the homology theory becomes a formulation of the locality of the field theory. The theorem includes a relative version, for a fixed $\cB$-manifold $X$, which in this interpretation is a fixed space-time. Thus, our result both generalizes the Eilenberg--Steenrod axioms and attempts to axiomatize the structure of the observables in a perturbative topological quantum field theory. This latter topic also lies in the domain of the cobordism hypothesis, or the cobordism hypothesis with singularities of \cite{cobordism}. A direct comparison between these approaches is possible, subject to suitable construction of the functor $Z$, below, proposed in the cobordism hypothesis. Namely, there should be a commutative diagram below (subject to a suitable construction of the dashed functors, which we do not provide in the present work):
\[\xymatrix{
\Alg_{\disk_n}(\cV)^{\sim}\ar[d]_{\int}\ar[r]&\bigl(\Alg_{n}(\cV)^{\sim}\bigr)^{\sO(n)}\ar@{-->}[d]^Z\\
\bcH(\mfld(\cB), \cV)^{\sim} \ar@{-->}[r]& \Fun^\ot({\sf Bord}_n, \Alg_{n}(\cV))\\
}\]
\noindent

We briefly explain the terms in this picture: $\disk_n$ and $\mfld$ are the $\oo$-categories of $n$-disks and $n$-manifolds and embeddings; ${\sf Bord}_n$ is the $(\oo,n)$-category of bordisms of manifolds from \cite{cobordism}; and $\Alg_{n}(\cV)$ is the higher Morita category, where $k$-morphisms are framed $(n-k)$-disk algebras in bimodules; the superscript $\sim$ denotes that we have taken the underlying $\oo$-groupoids, restricting to invertible morphisms. The bottom dashed arrow from homology theories valued in $\cV$ to topological quantum field theories valued in $\Alg_{n}(\cV)$, assigns to a homology theory $\cF$ the functor on the bordism category sending a $k$-manifold $M$ to $\cF({M}^\circ\times\RR^{n-k})$, the value of $\cF$ on a thickening of the interior of $M$. There is a similar diagram replacing $n$ with a general  collection of basic singularity types $\cB$, where on the right we substitute bordism categories with singularities.

\medskip

We assert that this diagram commutes, but this assertion relies on the existence of the higher bordism $(\oo,n)$-category ${\sf Bord}_n$ and on the verification of the cobordism hypothesis, i.e., the existence of the dotted arrow $Z$. A proof by Lurie has been outlined in \cite{cobordism}, building on earlier work with Hopkins. We defer the commutativity of this diagram to a future work, after the full completion of the right hand side.

\medskip

We turn to a description now of the the second part of this work. There, we apply our main result, Theorem \ref{hmlgy=FH}, to give a proof of non-abelian Poincar\'e duality, after \cite{salvatore}, \cite{segallocal}, and Section~5.5.6 of~\cite{HA}. Further, our Theorem \ref{non-abel} is a stratified generalization, that there is a homotopy equivalence
\[\int_X A_E \simeq \Gammac(X,E)\]
between a factorization homology theory and a space of sections of a stratified bundle $E$ over a $\cB$-manifold $X$, subject to stratum by stratum connectivity conditions on $E$. The left hand side can be thought of either as a labeled configuration space or a form of nonabelian homology with coefficients in a higher loop space. 

\medskip

In the last section of this paper, we detail the structure involved in particular choices of $\cB$-structures. We observe that the intersection homology theories of Goresky \& MacPherson fit our axiomatics. As such, our stratified theories generalize intersection homology in the way that the unstratified factorization homology of \cite{HA} and \cite{Fact} generalize ordinary homology. We then study two examples: manifolds with boundary and $n$-manifolds with a submanifold of fixed dimension $d$. Both of these have descriptions as special cases of our main theorem, and each of these descriptions mix with the form of the higher Deligne conjecture proved by Lurie \cite{HA}, which asserts that the higher Hochschild cohomology $\hh^\ast_{\sD^{\fr}_d}(B)$ of a framed $d$-disk algebra $B$ carries a framed $(d+1)$-disk algebra structure which is characterized by a universal property. In particular, we prove the following by combining our main theorem and this form of Deligne's conjecture:

\begin{cor} There is an equivalence 
\[
\int\colon \Alg_{\disk_{d\subset n}^{\fr}}(\cV)\leftrightarrows\bcH(\mfld^{\fr}_{d\subset n}, \cV)\colon \rho
\] 
between $\disk_{d\subset n}^{\fr}$-algebras in $\cV$ and $\cV$-valued homology theories for framed $n$-manifolds with a framed $d$-dimensional submanifold with trivialized normal bundle. The datum of a $\disk_{d\subset n}^{\fr}$-algebra is equivalent to the data of a triple $(A,B,\alpha)$, where $A$ is a $\disk_n^{\fr}$-algebra, $B$ is a $\disk_d^{\fr}$-algebra, and $\alpha:\int_{S^{n-d-1}}A\ra \hh^\ast_{\sD^{\fr}_d}(B)$ is a map of $\disk^{\fr}_{d+1}$-algebras.
\end{cor}

Specializing to the case of 3-manifolds with a 1-dimensional submanifold, i.e., to links, the preceding provides an algebraic structure that gives rise to a link homology theory. To a triple $(A, B, \alpha)$, where $A$ is a $\disk_3^{\fr}$-algebra, $B$ is an associative algebra, and $\alpha: \hh_\ast (A) \ra \hh^\ast (B)$ is a $\disk_2^{\fr}$-algebra map, one can then construct a link homology theory, via factorization homology with coefficients in this triple. This promises to provide a new source of such knot homology theories, similar to Khovanov homology. Khovanov homology itself does not fit into this structure, for a very simple reason: an open embedding of a noncompact knot $(U, K) \subset (U', K')$ does not define a map on Khovanov homologies, from ${\sf Kh}(U,K)$ to ${\sf Kh}(U',K')$. (In addition, Khovanov homology still has not been constructed for general manifolds $K$, other than $S^3$ or $\RR^3$.) factorization homology theories can be constructed, however, using the same input as Chern--Simons theory, and these appear to be closely related to Khovanov homology -- these theories will be the subject of another work, one which requires a more involved use of stratifications to capture nonperturbative phenomena.

\begin{remark}
In this work, we use Joyal's {\it quasi-category} model  of $\oo$-category theory \cite{joyal}. 
Boardman \& Vogt first introduced these simplicial sets in \cite{bv}, as weak Kan complexes, and their and Joyal's theory has been developed in great depth by Lurie in \cite{HTT} and \cite{HA}, our primary references; see the first chapter of \cite{HTT} for an introduction. We use this model, rather than model categories or simplicial categories, because of the great technical advantages for constructions involving categories of functors, which are ubiquitous in this work. 
More specifically, we work inside of the quasi-category associated to this model category of Joyal's.  In particular, each map between quasi-categories is understood to be an iso- and inner-fibration; and (co)limits among quasi-categories are equivalent to homotopy (co)limits with respect to Joyal's model structure.

We will also make use of $\Kan$-enriched categories, such as $\snglr$ of stratified spaces and conically smooth embeddings among them. 
By a functor $\cS \ra \cC$ to an $\infty$-category from a $\Kan$-enriched category we will always mean a functor $\sN\cS \ra \cC$ from the simplicial nerve of $\cS$.  

The reader uncomfortable with the language of $\infty$-categories can substitute the words ``topological category" for ``$\oo$-category" wherever they occur in this paper to obtain the correct sense of the results, but they should then bear in mind the proviso that technical difficulties may then abound in making the statements literally true. The reader only concerned with algebra in chain complexes, rather than spectra, can likewise substitute ``pre-triangulated differential graded category" for ``stable $\oo$-category" wherever those words appear, with the same proviso.
\end{remark}

 \medskip

{\bf Acknowledgements.} We are indebted to Kevin Costello for many conversations and his many insights which have motivated and informed the greater part of this work. We also thank Jacob Lurie for illuminating discussions, his inspirational account of topological field theories, and his substantial contribution to the theory of $\infty$-categories. JF thanks Alexei Oblomkov for helpful conversations on knot homology.
