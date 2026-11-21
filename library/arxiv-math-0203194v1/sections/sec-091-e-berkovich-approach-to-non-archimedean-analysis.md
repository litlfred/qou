---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-091-e-berkovich-approach-to-non-archimedean-analysis
section_title: "Berkovich' approach to non-archimedean analysis"
section_number: E
pages: 222-225
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
Berkovich’ viewpoint provides an innovative approach to topological
problems of p-adic geometry and analysis, which is much closer to the famil-
iar intuition derived from the complex context [Ber90](5). His analysis, in
fact, generalizes, or properly speaking, “completes” the rigid analysis. This
situation is, according to what he says in the introduction of his book, some-
how analogous to that of R completing Q. The standard archimedean metric
space Q is totally disconnected. The rigid analytic viewpoint corresponds,
to some extent, to regarding every rational interval {r ∈Q | a ≤r ≤b} as
(4)We refer [BGR84, 9.3.1] for the deﬁnition of open subanalytic spaces.
(5)Already in [vdP82] the esquisse of Berkovich’ idea can be seen.
5. BERKOVICH’ APPROACH TO NON-ARCHIMEDEAN ANALYSIS
219
“connected”, and considering only those functions which come from analytic
functions on the corresponding real interval. Berkovich’ non-archimedean
analysis can be compared, in this context, to analysis on R itself. Namely,
his presentation of analytic spaces complements those of rigid analysis by
putting some “generic points”, and consequently, simpliﬁes their topology.
Let us be a little more precise about his theory. Let A be a Banach ring,
i.e., a ring together with a norm ∥· ∥with respect to which A is complete.
Deﬁnition 5.1. (1) A semi-norm | · | on A is said to be bounded if there
exists C > 0 such that |f| ≤C∥f∥for any f ∈A.
(2) A semi-norm | · | on A is said to be multiplicative if |fg| = |f||g| for
all f, g ∈A.
Replacing the maximal spectra Spm(A) of rigid geometry, we have:
Deﬁnition 5.2. The Berkovich’ spectrum M(A) for a Banach ring A is the
set of all bounded multiplicative semi-norms on A, endowed with the weakest
topology so that the real valued functions of form | · | 7→|f| for f ∈A are
continuous.
In case A is an aﬃnoid algebra (a strict aﬃnoid algebra, in Berkovich’
term) over K, the aﬃnoid space Spm(A) is naturally viewed as a subspace,
with the relative topology, of the Berkovich’ spectrum M(A). This is done
by identifying an element m in Spm(A) with the unique semi-norm | · | on
A such that m = Ker | · |. The space Spm(A) is identiﬁed, in terms of this
correspondence, with the subspace of M(A) consisting of semi-norms | · |
such that dimK A/ Ker | · | is ﬁnite (the “classical points”).
Example 5.3. Let us consider the usual absolute-value norm | · |∞on Z.
The spectrum M(Z) consists of the following points:
(i) | · |∞,ǫ: = | · |ǫ
∞(0 < ǫ ≤1).
(ii) The p-adic norm | · |p,ǫ: with |p|p,ǫ = ǫ (0 < ǫ ≤1).
(iii) The semi-norm | · |p induced from the trivial norm on Z/pZ.
(iv) The trivial norm | · |0.
As a topological space, M(Z) is a tree with end points | · |p and | · |∞. Each
of these points is connected by a single edge with | · |0.
On the Berkovich’ spectrum, the aﬃnoid subdomains (incl. rational sub-
domains) are deﬁned in the similar way to rigid analysis.
Thus one can
deﬁne the structure sheaves on spectra, which one calls aﬃnoid spaces. The
local data consisting of Berkovich’ aﬃnoids and the structure sheaves can
glue to locally ringed spaces; thus we obtain analytic spaces in Berkovich’
sense.
Example 5.4. (Cf. [Ber90, 1.5].) Let K be a non archimedean complete
ﬁeld. An aﬃne space over K is deﬁned by
An
K = {multiplicative seminorm | · | on K[t1, . . . , tn] | | · ||K is bounded}
220
A. RAPID COURSE IN p-ADIC ANALYSIS.
together with the weakest topology so that | · | 7→|f| (f ∈K[t1, . . . , tn])
is continuous. This has a structure of analytic space so that the analytic
functions over it is characterized by limits of rational functions. When K =
C the space An
K is nothing but the usual aﬃne space in the complex analytic
sense. If K is a non-archimedean ﬁeld, then An
K is a union of balls; i.e., the
spectrum of Tate algebra.
Here are some general properties of Berkovich’ analytic spaces:
(i) Every connected K-analytic space is arcwise connected.
(ii) If X = M(A) with A an aﬃnoid algebra over K, then Krull-dimA =
dim|X|, where |X| is the underlying topological space of X.
(iii) If a K-analytic space X is smooth, then it is locally contractible.
Relation between Berkovich’ analytic spaces and rigid analytic spaces is
as follows. If a Berkovich’ K-analytic space X is formed only by spectra
of (strict) aﬃnoid algebras, we say X is strict. There exists a functor from
the category of separated strict K-analytic spaces to that of separated rigid
analytic spaces over K by
X 7→X0 = {x ∈X | [K(x): K] < ∞},
where K(x) is the residue ﬁeld at x.
Theorem 5.5. This functor is fully-faithful, and preserves ﬁber products.
APPENDIX B
Overview of theory of p-adic uniformization.
By F. Kato
In this appendix we always denote by K, R, and π a complete discrete
valuation ﬁeld, its valuation ring, and a prime element of R, respectively.
We assume that the residue ﬁeld k = R/πR is ﬁnite and consists of q ele-
ments. The Mumford-Kurihara-Mustaﬁn uniformization is a procedure to
construct nice analytic (and in many cases algebraic) varieties by taking
discrete Schottky-type quotients of a certain p-adic analogue of symmetric
space, so-called Drinfeld symmetric space Ω, or its variants.
