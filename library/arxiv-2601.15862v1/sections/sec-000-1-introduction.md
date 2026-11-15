---
doc_id: arxiv-2601.15862v1
doc_title: "Synthetic Differential Jet Bundles are Reduced"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2601.15862v1.pdf
source_sha256: e37fa9b4515f58d1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.806
doc_brief: "Synthetic Differential Jet Bundles are Reduced — We have previously observed that the theory of solutions of par- tial differential equations, regarded as diffieties inside jet bundles, acquires a"
---
The tenet of \emph{synthetic differential geometry} (SDG, cf. \parencites{Kock1979}{lavendhomme1996}{Kock2010}) is that concepts and results in differential geometry often find a more natural and powerful formulation after faithfully embedding the category of smooth manifolds into a suitable \emph{topos} (cf. \parencites{MacLaneMoerdijk1992}{Borceux1994III}) where \emph{infinitesimal spaces} exist as actual objects. 

\smallskip 
Such a ``well-adapted'' SDG topos is the \emph{Cahiers topos} due to E. Dubuc (\cite{Dubuc1979}, cf. \cite[\S 2]{GS26-FieldsII}), which we may think of as the category of \emph{formal smooth sets} (recalled in \cref{FormalSmoothSets} --- here ``formal'' is common jargon for ``infinitesimally thickened'' or ``haloed''). This is a differential-geometric analog of working with \emph{formal schemes} in algebraic geometry.

\smallskip 
One striking example is from the geometry of partial differential equations. On top of describing classical solutions, SDG can treat formal (power series) solutions of partial differential equations as primary objects. Classically, these formal solutions appeared in the guise of \emph{diffieties} inside infinite jet bundles (a very fruitful perspective due to \cite{Vinogradov1981}, brief background is recalled in \cref{OnJetBundles}). Their appearance in SDG turns out to become largely structural (namely \emph{comonadic}) when viewed in the synthetic context of formal (infinitesimally thickened) smooth sets. This is the result of \cite{KS26}. However, a key technical step in this identification had remained unproven, recalled as \cref{i!PreservesInfiniteJetBundles} below:

\smallskip 
Namely, with \emph{infinite jet bundles} \cref{InfiniteJetBundleInBackground} being projective limits of finite-dimensional manifolds, there are \emph{a priori} two different ways of regarding them among formal smooth sets: Either by first taking the limit (in Fr{\'e}chet manifolds) and then passing to formal smooth sets, or the other way around! 
We prove here that that these two constructions are naturally isomorphic.

This has crucial implications for applications in variational calculus and in Lagrangian field theory, cf Cor. \ref{MapsOutOfJetBundleAreLocallyOfFiniteOrder} below.

\smallskip 
The result may be ``intuitively expected'' to be true, but proving it is not entirely trivial. Here we provide a detailed and largely constructive proof. Besides filling this particular gap in the previous literature, our proof may be interesting for the technique it uses, which seems to be new, and may be adapted to other situations, cf. \cref{OnTheNatureOfRInfinityInFormalSmoothSets} below.
