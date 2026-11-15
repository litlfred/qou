---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-005-new-multivariate-methods
section_title: "New multivariate methods"
section_number: null
pages: 27-30
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
9
and that sequences of generating functions obeying (1.4) satisfy a central limit
theorem and a local central limit theorem.
The GF-sequence method is limited to the single, though important, case
where the coeﬃcients ar are nonnegative and possess Gaussian (central limit)
behavior. The work of [BR83] has been greatly expanded upon, but always
in a similar framework. For example, it has been extended to matrix recur-
sions [BRW83] and, in [GR92; BR99], from algebraic to algebraico-logarithmic
singularities of the form F ∼(zd −g(x))q logα(1/(zd −g(x))). The diﬃcult step
under these hypotheses is deducing asymptotics from the quasi-power hypoth-
esis (1.4).
1.2 New multivariate methods
The research presented in this book grew out of several problems encoun-
tered by the ﬁrst author, concerning bivariate and trivariate arrays of probabil-
ities. One might have thought, based on the situation for univariate generating
functions, that there would be well-known, neatly packaged results yielding
asymptotic estimates for the probabilities in question. At that time, the most
recent and complete reference on asymptotic enumeration was a 1995 survey
of Odlyzko [Odl95]. As mentioned in the preface, only six of the over 100
pages of the survey are devoted to multivariate asymptotics, mainly to the GF-
sequence results of Bender et al., and its section on multivariate methods closes
with a call for further work in this area. Evidently, a general asymptotic method
was not known in the multivariate case, even for the simplest non-trivial class
of rational functions.
This stands in stark contrast to the univariate theory of rational functions,
which is trivial in combinatorial applications (see Chapter 3). The relative dif-
ﬁculty of the problem in higher dimensions is perhaps unexpected, but connec-
tions to other areas of mathematics such as Morse theory are quite intriguing.
These connections, as much as anything else, have caused us to pursue this
line of research long after the urgency of the original motivating problems had
faded.
Odlyzko [Odl95] describes why he believes multivariate coeﬃcient estima-
tion to be diﬃcult. First, generating function singularities are no longer iso-
lated, but generally form (d −1)-dimensional hypersurfaces, so even multivari-
ate rational functions have an inﬁnite set of singularities. Second, the multivari-
ate analogue of the one-dimensional residue theorem is the considerably more
diﬃcult theory of Leray residues [Ler59]. This theory is ﬂeshed out in the text
of Aizenberg and Yuzhakov [AY83], who also spend a few pages [AY83, Sec-
10
Introduction
tion 23] on generating functions and combinatorial sums. Further progress in
using multivariate residues to evaluate coeﬃcients of generating functions was
made by Bertozzi and McKenna [BM93], though at the time of Odlyzko’s sur-
vey none of the papers based on multivariate residues such as [Lic91; BM93]
had resulted in any kind of systematic application of these methods to enumer-
ation. It is interesting to note that several of these early works, such as [BM93;
KY96], are centered on queueing theory applications.
The focus of this book is a more recent vein of research, begun in [PW02],
continued in its infancy in [PW04; Lla03; Wil05; Lla06; RW08; RW11; PW08;
DeV10; PW10], and now comprising a stable and ever-growing component
of enumerative combinatorics. This research extends ideas that are present to
some degree in [Lic91; BM93; KY96], using complex methods that are gen-
uinely multivariate to evaluate coeﬃcients via the multivariate Cauchy formula
ar =
 1
2πi
!d Z
T
z−r−1F(z) dz ,
(1.5)
where T is a suitable product of circles in each variable. We hope that by
avoiding the symmetry-breaking decompositions of the GF-sequence method
we will obtain methods that are more universally applicable. In particular,
much of this past work can be viewed as instances of a more general result
estimating the Cauchy integral via topological reductions of the cycle T of
integration. These topological reductions, while not fully automatic, are algo-
rithmically decidable in many cases. The ultimate goal, now well on its way
to fruition [Mel21, Chapter 7], is to develop software to automate all of the
computation.
We can by no means say that the majority of multivariate generating func-
tions fall prey to these new techniques. Nevertheless, as illustrated in this
text and a steadily increasing number of papers, we can treat a large num-
ber of combinatorially interesting examples. The class of functions to which
the methods described in this book may be applied is larger than the class of
rational functions, but similar in spirit: the function must have singularities,
and the singularities dictating asymptotics must be poles. This translates to the
requirement that the function be meromorphic in a neighborhood of a certain
polydisk, which means that it has a representation, at least locally, as a quotient
of analytic functions.
Throughout this book, we reserve the symbols F, P, and Q for a meromor-
phic function F expressed as the quotient P/Q of analytic functions with a
1.2 New multivariate methods
11
convergent series expansion
F(z) = P(z)
Q(z) =
X
r
arzr .
Although this introduction has focused on power series expansions, we will
develop the theory for convergent Laurent expansions, allowing the index r to
range over Zd. The set V of singularities of F, which is crucial to the asymp-
totic analysis, is known as its singular variety. For instance, if P and Q are
coprime polynomials then the singular variety is the algebraic set V = {z ∈
Cd : Q(z) = 0}.
We now brieﬂy describe the ACSV approach to computing multivariate
asymptotics. A more detailed overview is provided in Chapter 7.
(i) Use the multidimensional Cauchy integral (1.5) to express ar as an inte-
gral over a d-dimensional torus (product of circles) T in Cd.
(ii) Observe that T may be replaced by any cycle homologous to [T] in
Hd(M), where M is the domain of analyticity of the integrand.
(iii) Deform the cycle T to lower the modulus of the integrand as much as
possible. Morse-theoretic arguments imply that local maxima are char-
acterized by the set critical(r) of critical points of V, which depend
only on the direction ˆr of r as r →∞and are saddle points for the
magnitude of the integrand.
(iv) Use algebraic methods to encode the elements of critical(r) by a ﬁnite
collection of equalities and inequalities (deﬁned by polynomials when F
is rational).
(v) Use topological methods to ﬁnd certain minimax cycles C(w) near each
critical point w, termed quasi-local cycles, such that the homology class
[T] can be represented by a sum P
w nwC(w) with each nw ∈Z.
(vi) Reﬁne the set of critical points to the set contrib(r) of contributing
points that maximize the modulus of the Cauchy integrand among the
critical points w with nw , 0. In the vast majority of cases for which we
have explicit asymptotic results, it is the case that nw ∈{0, ±1}.
(vii) Asymptotically approximate integrals over the C(w) as w ranges over
the set of contributing points, using a combination of residue and saddle
point techniques.
When successful, this approach leads to an asymptotic representation of the
coeﬃcients ar that is uniform as r varies on the interior of ﬁnitely many cones
that partition Rd. As ˆr varies over compact subsets in the interior of such cones,
12
Introduction
the elements of contrib(r) ⊆V vary smoothly with ˆr and there exist asymp-
totic series {Φw(r) : w ∈contrib(r)} whose terms can be computed explic-
itly such that
ar =
1
(2πi)d
Z
[T]
zr−1F(z) dz
=
X
w∈critical(r)
nw
(2πi)d
Z
C(w)
zr−1F(z) dz
(1.6)
=
X
w∈contrib(r)
nwΦw(r) .
The ﬁrst line in this chain of equalities reﬂects steps (i) and (ii) of our program
above, while the second is the result of steps (iii)–(v), and the ﬁnal line comes
from steps (vi) and (vii). The set critical(r) is algorithmically computable
in reasonable time, while determining membership in the subset contrib(r)
can be extremely challenging. The explicit formulae Φw(r) in the last line are
sometimes relatively easily to compute (see Chapter 9) and sometimes more
diﬃcult (see Chapter 10 and especially Chapter 11).
