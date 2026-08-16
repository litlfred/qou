---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-033-101-nonabelianization
section_title: "Nonabelianization"
section_number: 10.1
pages: 61-65
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
The space M(Σ,GL (1); m) is a torsor for ( C×)2g¯Σ, where ¯Σ is the closure of Σ, so
another way to read Ψ W is as a local coordinate system onMF (C,GL (K); m). These
coordinate systems are closely related to the “cluster coordinates” introduced by Fock and
– 59 –
Goncharov [13]. In the case K = 2, it is straightforward to see that our coordinates in
fact coincide with the cluster coordinates. In the case K >2 a fully explicit description of
the most general cluster coordinate system is not available in the literature; we conjecture
that the ΨW actually give the most general cluster coordinates, thus ﬁlling this gap.
One point in favor of this conjecture is that when W is of a special form, Ψ W yields
a coordinate system which was explicitly described by Fock and Goncharov; this will be
described in [32].
Although we are emphasizing its mathematical content in this section, this construc-
tion also has a natural physical meaning, which appears most clearly when the theory is
compactiﬁed from four to three dimensions on S1. Indeed, the expansion (10.6) of the
parallel transport of∇ as a linear combination of parallel transports Xa(∇ab) is precisely
the “Darboux expansion” of the vacuum expectation value of the supersymmetric interface
associated with ˜℘. This point of view was described at length in [5].
10.1 Nonabelianization
We now explain how, given a nondegenerate spectral networkW subordinate to a covering
Σ→C, and given also a twisted ﬂat rank 1 connection over Σ, we construct a corresponding
twisted ﬂat rank K connection over C.
By a twisted ﬂat rank K connection over a real surface S we mean a pair of a complex
rank K vector bundle on ˜S and a ﬂat connection therein, such that the holonomy around
each ﬁber of ˜S is−1. This is a very small modiﬁcation of the usual notion of a rank
K connection over S. In particular, given a spin structure on S, there is a canonical
isomorphism between the moduli space of twisted ﬂat connections and that of ordinary
connections.29 Nevertheless, this slight twisting is important in the construction we are
about to describe.
Now suppose given a rank 1 twisted ﬂat connection ( L,∇ab) over Σ. Recall that C′
denotes C minus the branch points of the covering Σ → C. Let π : ˜Σ → ˜C′ be the
projection. Then deﬁne the complex rank K vector bundle
E =π∗(L). (10.2)
The ﬁber of E at any ˜z∈ ˜C′ is simply
E˜z =
⨁
i
L˜z(i). (10.3)
Given the ﬂat rank 1 connection ∇ab onL, there is a canonical “pushforward” ﬂat
connectionπ∗(∇ab) onE. But the reader should beware that π∗(∇ab) is not the connection
we are trying to construct. Indeed, while π∗(∇ab) is ﬂat on ˜C′, it has nontrivial holonomy
around any small loop 𝓁b in ˜C′ linking the ﬁber over a branch point b; this monodromy
is induced by the permutation of sheets attached to b. It follows that π∗(∇ab) cannot be
29To obtain this isomorphism we use the fact that a spin structure is the same thing as a ﬁberwise
double covering of ˜S; then given a twisted ﬂat connection, pulling back to this double cover gives a new
ﬂat connection with holonomy +1 around the ﬁbers, which then descends to a ﬂat connection over S.
– 60 –
extended to a ﬂat connection over ˜C, since on ˜C the loop 𝓁b would be contractible. Our
construction will modify (E,π∗(∇ab)) in a way which eliminates this holonomy.
The key is the path-lifting rule F deﬁned in§9.4. Let C′
W :=C′\W . Given any path
˜℘ from ˜z1∈ ˜C′
W to ˜z2∈ ˜C′
W we have built a formal sum of paths on ˜Σ, given by (9.4):
F( ˜℘,W) =
∑
a
Ω
′
( ˜℘,W, a)Xa. (10.4)
Each a in the sum (10.4) is a homotopy class of paths on ˜Σ from ˜z(i)
1 to ˜z(j)
2 for some i, j.
Let
Xa(∇ab)∈ Hom(L˜z(i)
1
,L˜z(j)
2
) (10.5)
denote the parallel transport of ∇ab along any path in the class a. The fact that ∇ab is a
ﬂat connection implies that Xa(∇ab) depends only on the class a and not on the particular
path, and the fact that∇ab has holonomy−1 around the ﬁbers of ˜Σ implies that Xa(∇ab)
obeys the relation (9.3). Hence the map Xa→ Xa(∇ab) is well deﬁned.
We now deﬁne a new operatorF( ˜℘,W,∇ab) just by replacingXa→ Xa(∇ab) in (10.4):
F( ˜℘,W,∇ab) :=
∑
a
Ω
′
( ˜℘,W, a)Xa(∇ab)∈ Hom(E˜z1,E ˜z2). (10.6)
F( ˜℘,W,∇ab) has precisely the formal properties one would expect if it were the parallel
transport operator in some ﬂat vector bundle: it is homotopy invariant and behaves prop-
erly under composition. The key to our construction is that indeed F( ˜℘,W,∇ab) is the
parallel transport operator from ˜z1 to ˜z2 for a twisted rank K ﬂat connection ( ˆE,∇) over
C. ( ˆE,∇) will be constructed in an essentially tautological way to make this sentence true.
The most direct way of building ( ˆE,∇) is to construct its sheaf F of ﬂat sections, as
follows. For any open set U⊂ ˜C, F(U) consists of all sections ψ of E overU∩ ˜C′
W such
that for any path ˜℘⊂U with endpoints ˜z1, ˜z2∈ ˜C′
W, we have
ψ(˜z1)F( ˜℘,W,∇ab) =ψ(˜z2). (10.7)
(Note that the parallel transport acts from the right, in accordance with Appendix C.)
Any ψ∈ F(U) is obviously determined by its value at a single ˜z0∈U∩ ˜C′
W. Conversely,
ifU is contractible, then any chosen ψ(˜z0)∈ E˜z0 can be extended to ψ∈ F(U) (to prove
this one uses the invariance of F( ˜℘,W,∇ab) under homotopies of ˜℘ and the composition
law (9.5).) So F is a locally constant sheaf of K-dimensional vector spaces. Giving such
a sheaf is equivalent to giving a rank K vector bundle with connection; this is our desired
( ˆE,∇).
It will be useful in what follows to have a more concrete description of (ˆE,∇). The stalk
of F at any ˜z∈ ˜C′
W is justE˜z, so on ˜C′
W we have a canonical isomorphism ˆE≃E. Moreover,
for paths ˜℘⊂ ˜C′
W we have F( ˜℘,W) = D( ˜℘), from which it follows that F( ˜℘,W,∇ab) is
just the parallel transport of π∗(∇ab). So on ˜C′
W we have simply ( ˆE,∇)≃ (E,π∗∇ab).
Now, ˜C′
W is divided into various connected componentsUα, separated from one another by
the lifts of walls of W, which are topologically cylinders in ˜C. We want to know how to
– 61 –
patch together the bundle ˆE across these cylinders. Given a wall pc whose lift ˜pc separates
componentsUα andUβ, we deﬁne a section of End(E)|˜pc by
T α,β
c (˜z) = 1 +
∑
ν∈Sc(z)
Xa(ν, ˜℘)(∇ab) (10.8)
where ˜℘ denotes a short path which crosses from ˜z1∈U α to ˜z2∈U β, and we take the limit
as ˜z1 and ˜z2 approach the common point ˜z of ˜pc. Recall here that Sc(z) is the soliton set
ofW at z (W is nondegenerate, so only one of the soliton sets is nonempty.) The bundle
ˆE can be realized by extending E to the closure of each component and then gluing along
the boundary cylinders:
ˆE =
(⨆
α
E| ¯Uα
)
/∼ (10.9)
where the equivalence relation∼ identiﬁes (ψ, ˜z)∈E| ¯Uα with (T α,β
c ψ, ˜z)∈E| ¯Uβ whenever
˜z lies on the cylinder ˜pc.
10.2 Singularities and ﬂags
The twisted ﬂat connection ( ˆE,∇) produced by our nonabelianization construction carries
a bit of extra structure which will be important in what follows. In this section we brieﬂy
describe it.
Let us consider ( ˆE,∇) in a neighborhoodU⊂ ˜C of one of the singular points sn. OnU
we can trivialize the covering ˜Σ→ ˜C and hence there is a decomposition into line bundles
(cf. (10.3)),
E =
⨁
i
L(i), (10.10)
preserved by the connection π∗∇ab. We do not generally have such a decomposition for ˆE,
because the gluing transformations T α,β
c mix the diﬀerentL(i). Still, the T α,β
c do preserve
some structure, as follows. Recall that the walls pc ofW which end at sn carry labels ij
which obey a constraint: both i andj must belong too(sn) and we must havei<j . Using
(10.8) it then follows that all the T α,β
c are “upper triangular”: for i /∈o(sn) they preserve
L(i), and for i∈o(sn) they preserve the subspace
F (i) =
⨁
j≥i
L(j). (10.11)
So we ﬁnd that ˆE decomposes overU as
ˆE =

 ⨁
i/∈o(sn)
L(i)

⊕ ˆEsn (10.12)
where each L(i) is∇-invariant, and ˆEsn has rank |o(sn)| and carries various ∇-invariant
subbundles F (i). The ranks of these subbundles and of their intersections are determined
by the structure of the partial ordering in o(sn).
– 62 –
In the simplest case o(sn) is a totally ordered set containing all K sheets. In that
case we may as well identify the labels with integers 1 ≤i≤K, and write the ordering as
1< 2<··· <K . Then the extra structure just discussed is simply a ∇-invariant ﬁltration
of ˆE,
0 =F (K)⊂F (K−1)⊂F (K−2)⊂···⊂ F (0) = ˆE, (10.13)
where F (i) has dimension K−i. If the monodromy of ∇ around sn is diagonalizable with
all eigenvalues distinct, then there exist K! such invariant ﬁltrations, and our construction
picks one out of those K!.
What we have found is that our construction naturally produces not just ( ˆE,∇), but a
bit of extra structure around eachsn, namely the decomposition (10.12) and the subbundles
F (i). We refer to this extra structure as ﬂag data.
