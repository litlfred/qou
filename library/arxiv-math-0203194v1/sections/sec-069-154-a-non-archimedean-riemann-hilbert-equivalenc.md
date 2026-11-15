---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-069-154-a-non-archimedean-riemann-hilbert-equivalenc
section_title: "A non-archimedean Riemann-Hilbert equivalence."
section_number: 15.4
pages: 152-156
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.98
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::3.4} 

\begin{para}\label{para::3.4.1} Let us return to a general ordinary linear
 differential equation with polynomial or analytic coefficients 

 \begin{equation}
  \alpha_\mu(z) \partial^\mu y + \cdots + \alpha_0 (z) y = 0
  \;\text{ on $S\subset \A^1$, with $\partial=z\frac{d}{dz}$}.\tag{$\ast$}
 \end{equation}

 In the $p$-adic case, contrary to the complex situation, there
 does {\it not} exist, in general, any \'etale covering $S'\to S$ such
 that $(\ast)$ has a full set of solutions in $\mathcal{O}_{S'}$.
 
 \medskip\noindent {\it Example}: $\partial^2 y =0, \;S \supset
 \mathcal{C}(]1-\epsilon, 1[)$; there is no ``$p$-adic Riemann surface 
 of the logarithm'' on $S$.
 
 \medskip However, there are interesting global situations where this
 does happen. 

 \medskip\noindent {\it Example}: $\partial y - zy =0 $ on $S=\A^1$ :
 $S'=\matheur{D}(1,1^-)\xrightarrow{\log} S$, the infinite
 Galois \'etale covering with group $\mu_{p^\infty}\cong \Q_p/\Z_p$,
 trivializes the equation. 
 
 \medskip\noindent The object of this subsection is to investigate this
 phenomenon in full generality.
\end{para}

\begin{para}\label{para::3.4.2} Let $K$ be a complete non-archimedean
 field. We note that by definition, $K$-manifolds are `good' in the
 sense of \cite[1.2.6]{ecfnas}, \ie any point has an affinoid
 neighborhood. This property simplifies the theory of coherent sheaves
 (in the dictionary between rigid-analytic spaces and Berkovich analytic
 spaces, the theories of coherent sheaves and vector bundles correspond,
 \cf \cite[1.3.4, 1.6]{ecfnas})\footnote{Actually there are a number of
 technicalities involved in the analytic \'etale topology. First of all,
 since we restrict our attention to strictly analytic spaces in order to
 have the dictionary with rigid analytic varieties at disposal,
 Berkovich's definition of the \'etale site has to be slightly modified:
 this point is discussed in detail in R. Huber's book
 \cite[8.3]{ecoravaas}. Translated into rigid geometry, one gets the
 `partially proper \'etale' site of {\it loc.~cit.}. The associated
 sheaves correspond to the `overconvergent/conservative/constructible
 \'etale sheaves' of Van 
 der Put, Schneider, and De Jong \cite{jong96:_etale}, \cf
 \cite[8.2.12]{ecoravaas}. 
 We don't insist further on these subtleties.}.

 On the other hand, each coherent sheaf $M$ on $S$ gives rise to an
 \'etale sheaf $ M_{\mathrm{et}} $ on $S$ \cite[4.1.2]{ecfnas}.
 Moreover, one has \'etale descent for coherent sheaves: descent data are
 effective (\cf proof of \cite[4.1.10]{ecfnas}, and also
 \cite[3.2.3]{jong96:_etale} in the rigid setting). We shall use this only for
 locally free coherent sheaves (vector bundles) of rank $n$. These are
 in bijection with $\mathrm{H}^1_{\mathrm{et}}(S, GL_n)$.
  
\medskip In the sequel, $S$ will be a connected $K$-manifold, and $\ovl{s}$ a
geometric point of $S$. We assume that the point $s$ is $K$-rational,
 \ie is a classical point with residue field $K$.
\end{para}

\begin{para}\label{para::3.4.3} A continuous $K$-linear representation $\rho$
 of a topological group $\Gamma$ will be called {\it discrete} if its
 coimage $\Gamma/\ker \rho$ is discrete, or equivalently, if $\rho$
 factors through a discrete group.

 An {\it \'etale local system} on $S$ is a locally constant \'etale sheaf
 of $K$-vector spaces on $S$.
\end{para}

\begin{pro}\label{pro::3.4.4} There is a natural equivalence of categories   
\begin{equation*}
\{\text{discrete }\pi_1^{\mathrm{et}}(S,\ovl{s})\text{-representations }\}
 \xrightarrow{\sim}
 \{\text{\'etale local systems on $S$}\}.
\end{equation*}
\end{pro}

\begin{proof}
 Let $\rho $ be a discrete representation in a $K$-vector space
 $V$. This amounts to a continuous homomorphism $\pi_1^{\mathrm{et}}(S,
 \ovl{s}) \to \Aut_K V$, where $\Aut_K V$ denotes the discrete group of
 $K$-linear automorphisms of $V$.  On the other hand, any \'etale local
 system $\mathcal{V}$ on $S$ gives rise in the usual way to an \'etale 
 \v{C}ech cocycle with values in $\Aut_K V$, with $V=\mathcal{V}_s$, and
 its isomorphism class gives a well-defined element of 
 $\mathrm{H}^1_{\mathrm{et}}(S, \Aut_K V)$. Such a cohomology class may also be
 interpreted as usual as an $\Aut_K V$-principal homogeneous space
 $\mathcal{F}$ (as an \'etale sheaf) over $S$ up to isomorphism. What has
 to be shown is that such a principal homogeneous space is representable
 by an \'etale covering space. By lemma \ref{lem::1.2.6}. (ii), this is a local
 question on $S$. We thus may assume that $S$ is affinoid, and that for
 some finite \'etale covering $S'\to S$, $\mathcal{F}_{S'}$ is
 representable by an \'etale covering of $S'$. In that case, the
 representability of $\mathcal{F}$ follows from the descent theory of
 schemes.

 Starting from a representation $V$ of $\pi_1^{\mathrm{et}}(S,\ovl{s})$, we 
 have thus attached the $\Aut_K V$-principal homogeneous space and 
 etale sheaf $\FF$; the looked for \'etale local system is the 
 associated etale sheaf $\VV$ of $K$-vector spaces, with respect to 
 the canonical representation $V$ of $\Aut_K V$ (the pull-back of this 
 etale local system on $\FF$ is the constant sheaf with value $V$).
 
 Conversely, from an etale local system $\VV$, one attaches the $\Aut_K 
 V$-principal homogeneous space $\FF$ viewed as an \'etale covering 
 space (with $V=\VV_{\bar s}$); the structure of
 $\pi_1^{\mathrm{et}}(S,\ovl{s})$-set on its fiber at $\ovl{s}$ comes from
 a continuous homomorphism 
 $\pi_1^{\mathrm{et}}(S,\ovl{s})\to \Aut_K V$ (the cohomology class of
 $\FF$ in $\mathrm{H}^1(\pi_1^{\mathrm{et}}(S,\ovl{s}), \Aut_K V)$ is
 nothing but the latter homomorphism up to conjugation).
\end{proof}

In the sequel of this section, we assume that $K$ is of {\it
characteristic zero}.

\begin{para}\label{para::3.4.5} Let $M$ be a vector bundle (= locally free
 $\mathcal{O}_S$-module of finite rank) with a connection: $\nabla:
 M\to \Omega^1_S \otimes M$ (\ie a $K$-linear map satisfying Leibniz
 rule). This can also be interpreted $\mathcal{O}_S$-linearly, in terms
 of first-order jets, as a section $M\to \mathcal{P}^1(M)$ of the natural
 projection $\mathcal{P}^1(M)\to M$.

 \noindent The vector bundles with connection (\resp with integrable
 connection) form a tannakian category over $K$. The unit for $\otimes$
 is the trivial connection  $d: \mathcal{O}_S\to  \Omega^1_S $.

\medskip Because $s$ is a classical point with residue field $K$ (of
 characteristic zero), the stalk at $s$ of the sheaf $M^\nabla=\ker
 \nabla$ of germs of horizontal sections is a $K$-vector space of rank
 the rank of $M$, which can be identified with the fiber $M_{(s)}$ (note
 that since $S$ has a $K$-rational point, 
 $(\mathcal{O}_{S_{\mathrm{et}}})^{d_{S_{\mathrm{et}}}}=K$).

 \medskip To $M$ (\resp $\mathcal{P}^1(M)$), one attaches an \'etale sheaf
 $M_{\mathrm{et}}$ (\resp $\mathcal{P}^1(M)_{\mathrm{et}}$) --- locally free
 $\mathcal{O}_{S_{\mathrm{et}}}$-modules. Thus $\nabla$ also correspond
 to a section of the natural projection $\mathcal{P}^1(M)_{\mathrm{et}}\to 
 M_{\mathrm{et}}$, or equivalently, to a $K$-linear map
 $\nabla_{\mathrm{et}}: \;M_{\mathrm{et}}\to  \Omega^1_{S_{\mathrm{et}}}
 \otimes M_{\mathrm{et}}$. The kernel of the latter map is an \'etale
 sheaf of $K$-vector spaces denoted by $M_{\mathrm{et}}^\nabla$ (the
 \'etale sheaf of germs of horizontal sections). Let $t$ be point of
 $S$. The fiber of $M_{\mathrm{et}}^\nabla$ at $t$ (\cf
 \cite[4.2]{ecfnas} is a $\ovl{K}$-vector space endowed with a discrete
 $\Gal(\ovl{\mathscr{H}(t)}/{\mathscr{H}(t)})$-action. If
 $M_{\mathrm{et}}^\nabla$ is locally constant, the dimension of this
 vector space is independent of $t$; taking $t=s$, we find that it is
 the rank of $M$.  
\end{para}

 \medskip\noindent{\it Remark.} Any classical point admits a neighborhood
 over which $M^\nabla$ is constant of rank equal 
 to the rank of $M$ (by the non-archimedean analogue of Cauchy's theorem
 on solutions of analytic differential equations). 
 The constancy of $M_{\mathrm{et}}^\nabla$ imposes a constraint only at
 non-classical points of the Berkovich space $S$.  

\begin{thm}\label{thm::3.4.6} There is a natural equivalence of tannakian
 categories (the {\rm non-archimedean \'etale Riemann-Hilbert functor}):
 \begin{equation*}
  \left\{
   \begin{matrix}
    \text{discrete finite dimensional}\\
    \pi_1^{\mathrm{et}}(S, \ovl{s})\text{-representations}
   \end{matrix}
   \right\}
   \xrightarrow{RH^{\mathrm{et}}}
   \left\{
    \begin{matrix}
     \text{vector bundles with integrable}\\
     \text{connection $(M,\nabla)$ on $S$ such that}\\
     \text{$M_{\mathrm{et}}^\nabla$ is an \'etale local system}
    \end{matrix}
   \right\}.
 \end{equation*}
 In this correspondence, the subspace of 
 $\pi_1^{\mathrm{et}}(S, \ovl{s})$-invariants corresponds to the
 space of global sections of $M^\nabla$.
\end{thm}

\begin{proof}
 Using the previous proposition and \'etale descent of coherent
 modules, it suffices to show that the natural maps 
 \begin{equation*}
  \mathcal{V}\mapsto (\mathcal{V}\otimes_K \mathcal{O}_{S_{\mathrm{et}}},
   \id\otimes d_{S_{\mathrm{et}}}),\;\;\;(M,\nabla)\mapsto
   M_{\mathrm{et}}^\nabla,
 \end{equation*}
 induce quasi-inverse functors
 \begin{equation*}
  \left\{
   \begin{matrix}
    \text{locally constant \'etale sheaves}\\
    \text{of fin. dim. $K$-vector spaces}
   \end{matrix}
  \right\}
   \rightleftharpoons
   \left\{
    \begin{matrix}
     \text{vector bundles with integrable}\\
     \text{ connection $(M,\nabla)$ such that}\\
     \text{$M_{\mathrm{et}}^\nabla$ is an \'etale local system}
    \end{matrix}
   \right\}
 \end{equation*}
 It is clear that these maps are functorial (and the first one is clearly
 compatible with the tensor 
 structures). The point is to show that they are quasi-inverse. 
 
 On the one hand, it is clear that $\id\otimes d_{S_{\mathrm{et}}}$ is an
 integrable connection, and that $(\mathcal{V}\otimes_K
 \mathcal{O}_{S_{\mathrm{et}}} )^{\id\otimes
 d_{S_{\mathrm{et}}}}=\mathcal{V}$ (taking into account that
 $(\mathcal{O}_{S_{\mathrm{et}}} )^{d_{S_{\mathrm{et}}}}=K$).
 We have to show that if $(M,\nabla)  $ is a vector bundle with integrable
 connection such that $M_{\mathrm{et}}^\nabla$ is locally constant, then
 the natural horizontal map

 \begin{equation*}
 \phi: M_{\mathrm{et}}^{\nabla}\otimes_K \mathcal{O}_{S_{\mathrm{et}}}\to
 M_{\mathrm{et}}.
 \end{equation*}
 is an isomorphism. By the remark preceding the
 theorem, the stalks of $M_{\mathrm{et}}^\nabla$ are $\ovl{K}$-vector
 spaces of constant dimension, which is the rank of $M$. It follows that 
 $M_{\mathrm{et}}^\nabla\otimes_K \mathcal{O}_{S_{\mathrm{et}}}$ is the
 \'etale sheaf attached to a vector bundle of the same 
 rank as $M$. It is a general well-known fact about integrable
 connections\footnote{proven by passing to the completion around
 classical points.} that $\phi$ is a monomorphism of vector bundles, and
 that $\Im\phi$ is locally a direct summand of
 $M_{\mathrm{et}}$ (because the cokernel inherits an integrable
 connection, hence is locally free). To show that this it is an 
 epimorphism, it thus suffices to check that
 $M_{\mathrm{et}}^\nabla\otimes_K \mathcal{O}_{S_{\mathrm{et}}}$ and
 $M_{\mathrm{et}}$ have the same rank, which is the case by assumption.
\end{proof}

\begin{para}\label{para::3.4.7} The $ \pi_1^{\mathrm{et}}(S, \ovl{s})
 $-representation attached to $(M,\nabla)$ is called the {\it
mono\-dromy representation}. Note that the underlying vector space is
canonically identified with the fiber $M_s$. The image of the monodromy
representation is called the {\it monodromy group}. It may be
non-discrete (while the coimage is discrete by assumption); this
phenomenon is not specific to the non-archimedean situation, and is
indeed familiar in the complex case.
\end{para}

\begin{para}\label{para::3.4.8} The \'etale Riemann-Hilbert functor unifies
 several earlier constructions. Indeed, if the monodromy representation
 factors through $\pi_1^{\mathrm{top}}(S,s)$, we recover the
 `topological Riemann-Hilbert functor' considered in
 I.\ref{sub-connection}, whose image consists of connections with
 locally constant sheaves of solutions.

\noindent It also includes some cases of overconvergent unit-root
isocrystals with finite monodromy already considered in
I.\ref{sub-chiaroscuro} (in that case, the monodromy factors through a
discrete, hence finite, 
representation of $\pi_1^{\mathrm{alg}}(S, \ovl{s})$).

 Of course, connections in the image of the \'etale Riemann-Hilbert
 functor are still rather special\footnote{for instance, it does not
 account for the differential equation of the logarithm, as we 
 have said in \ref{para::3.4.1}; to see this, one can notice that otherwise the
 monodromy group would be contained in the additive 
 group of $K$, hence torsion-free, but this implies that the \'etale
 covering which trivializes the connection is a 
 topological covering (\ref{thm::2.1.8}), hence is trivial.}, but it
 seems difficult to extend its scope without invoking ``relative
 Fontaine rings''.
\end{para}

\begin{rems}
  (i) Whether $M_{\mathrm{et}}^\nabla$ is an
	\'etale local system or not can be checked locally on $S$. In 
	particular, the property for a connection to be in the essential image
	of $RH^{\mathrm{et}}$ is local. 

  (ii) The \'etale fundamental group $\pi_1^{\mathrm{et}}(\P^1_{\C_p},
	\ovl{s})$, although highly non-trivial, does not have any non-trivial
	discrete finite-dimensional representation. Indeed, 
	the corresponding connection on
	$\P^1_{\C_p}$ would be algebrizable, and necessarily trivial.
\end{rems}
