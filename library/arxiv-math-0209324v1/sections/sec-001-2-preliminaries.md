---
doc_id: arxiv-math-0209324v1
doc_title: "arXiv:math/0209324v1 [math.AC] 24 Sep 2002"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 5-6
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.972
doc_brief: "arXiv:math/0209324v1 [math.AC] 24 Sep 2002 — The main object of study in this paper is the completion Z[q]N = lim ←−n Z[q]/((1−q)(1−q2) · · · (1−qn)) of the polynomial ring Z[q], which arises from"
---
\label{sec:preliminaries}

Throughout the paper, rings are unital and commutative, and
homomorphisms of rings are unital.  By ``homomorphism'' we will
usually mean a ring homomorphism.  Two rings that are considered to be
canonically isomorphic to each other will often be identified.  Also,
if a ring $R$ embeds into another ring $R'$ in a natural way, we will
often regard $R$ as a subring of $R'$.

If $R$ is a ring and $I\subset R$ is an ideal, then the $I$-adic completion
of $R$ will be denoted by
\[
R^I = \varprojlim_j R/I^j,
\]
and if $J\subset I$ is another ideal, then let
\[
\rho ^R_{J,I}\zzzcolon R^J\rightarrow R^I
\]
denote the homomorphism induced by $\id_R$.  These notation should not
cause confusions with $R[q]^S$ and $\rho ^R_{S,S'}$ defined in the
introduction.  We will further generalize these notations in the later
sections.  The ring $R$ is said to be {\em $I$-adically separated\/}
(resp. {\em $I$-adically complete\/}) if the natural homomorphism
$R\rightarrow R^I$ is injective (resp. an isomorphism).  Recall that $R$ is
$I$-adically separated if and only if $\bigcap_{j\ge 0}I^j=(0)$.

Let $\modN =\{1,2,\ldots\}$ denote the set of positive integers.  We
regard $\modN $ as a directed set with respect to the divisibility
relation $|$.  We will not use the letter $\modN $ for the same set
$\{1,2,\ldots\}$ when it is considered as an ordered set with the
usual order $\le $.

The letter $q$ will always denote an indeterminate.
