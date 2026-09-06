---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-048-115-jsj-decomposition
section_title: "JSJ decomposition"
section_number: 11.5
pages: 372-377
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
In Chapter 9 we cut every closed three-manifold along spheres, and it is
now time to decompose it further along tori. This two-steps cutting operation
is called the JSJ decomposition of the manifold, after the names of Jaco,
Shalen, and Johansson who discovered it in the mid 1970s.
Thecoreofthisdecompositionistheexistenceofacanonicalsetofdisjoint
essential tori, unique up to isotopy.
11.5.1. Canonical torus decomposition. Let M be an orientable irre-
ducible and∂-irreducible compact 3-manifold with (possibly empty) boundary
consisting of tori. How can we deﬁne a canonical set of disjoint essential tori
in M? The answer is not obvious: for instance, ifM is a Seifert manifold, it
may contain many vertical incompressible tori and there is no canonical way
to choose among them.
We will soon see that the Seifert manifolds are in fact the only possible
source of ambiguity. Let
S =T1⊔···⊔ Tk
be a set of disjoint essential toriTi ⊂ int(M). We say that S is a torus
decomposition ofM if it decomposesM into blocks that are either:
• torus (semi-)bundles,
• Seifert manifolds, or
• simple manifolds.
A torus decomposition isminimal if no proper subset ofS is a torus de-
composition. We prove here the following.
Theorem 11.5.1 (JSJ decomposition).LetM be an orientable irreducible
and∂-irreducible compact 3-manifold with (possibly empty) boundary consist-
ing of tori. A minimal torus decomposition forM exists and is unique up to
isotopy.
Such a minimal decomposition is called thecanonical torus decomposition
or theJSJ decompositionof M. The canonical torus decomposition may be
empty: this holds precisely whenM is itself a torus (semi-)bundle, Seifert, or
simple.
11.5. JSJ DECOMPOSITION 365
Remark 11.5.2. Torus (semi-)bundles are closed: therefore ifM is not
itself a torus (semi-)bundle, the blocks of its canonical decomposition are
either Seifert or simple.
11.5.2. Existence and uniqueness. Let M be an orientable irreducible
and∂-irreducible compact 3-manifold with (possibly empty) boundary consist-
ing of tori. We now prove Theorem 11.5.1. Let us start by showing existence.
Proposition 11.5.3. The manifoldM has a torus decomposition.
Proof. LetT1,...,T k be a maximal set of disjoint non-parallel essential
tori inM, which exists by Corollary 9.4.8. We now prove thatS =T1⊔···⊔ Tk
is a torus decomposition.
Suppose it is not: one blockN of the decomposition is neither a (semi-
)bundle, nor Seifert, nor simple. The blockN is irreducible and∂-irreducible
sincethesepropertiesarepreservedaftercuttingalongincompressiblesurfaces.
Being not simple, it contains an essential annulusA or an essential torusT.
In the latter case we can addT to the familyT1,...,T k and get a con-
tradiction sinceS is maximal. In the former case Lemma 11.2.10 applies and
N is Seifert. □
Since M has a torus decomposition, it certainly has a minimal one. We
now prove that it is unique.
Proposition 11.5.4. The manifoldM has a unique minimal torus decom-
position up to isotopy.
Proof. Let S = T1⊔···⊔ Tk and S′ = T′
1⊔···⊔ T′
k′ be two minimal
torus decompositions forM. We minimise their transverse intersections, so
thatS∩S′ consists of essential circles cutting some tori into annuli.
Let T′
i be decomposed into some annuli. Each such annulus is essential
in M\S, hence it is contained in some non-simple block,i.e. a Seifert one.
It is contained there horizontally or vertically: in the former case, the block is(
D, (2, 1), (2, 1)
)
,S∗×∼ S1, orA×S1 withS∗ the Möbius strip. The ﬁrst two
blocks are diﬀeomorphic, and by swapping the ﬁbration the annulus becomes
vertical. The third blockT×I is excluded sinceS is minimal.
Now all annuli inT′
i are vertical. Two consequent vertical annuli are sepa-
rated by some torusTj; since the two annuli are ﬁbered, the ﬁbers of the two
Seifert blocks incident toTj are isotopic: hence the two blocks glue to a bigger
Seifert block andTj can be removed, a contradiction sinceS is minimal.
We have shown thatS∩S′ = ∅. IfTi is parallel toT′
j we superpose the
two tori, cutM alongTi =T′
j and proceed by induction. Now we suppose by
contradiction that there is no parallelism.
EveryT′
i is an essential vertical torus in a Seifert block ofM\S, and vice
versa. This easily implies that all the blocks inM\S, M\S′, and all their
intersections are Seifert! Pick one such intersection. It has a unique Seifert
366 11. CONSTRUCTIONS OF THREE-MANIFOLDS
ﬁbration, unless it isK×∼ I which may ﬁber in two ways. Since∂(K×∼ I) is
connected, one block isK×∼ I itself and we change the ﬁbration on this block
if necessary. Now all intersections and all blocks have unique ﬁbrations and
they all glue to a Seifert ﬁbration forM, a contradiction. □
The proof of Theorem 11.5.1 is complete.
Remark 11.5.5. The sphere decomposition of Theorem 9.2.29 and the
torus decomposition of Theorem 11.5.1 diﬀer in two aspects: (i) the set of
decomposing spheres isnot canonical up to isotopy, while the set of tori is;
(ii) on the other hand, after cutting along the spheres and capping oﬀ we get
a canonical set of prime manifolds, whereas if we cut along the tori we get
some canonical manifolds with toric boundaries, but there is no canonical way
to cap them oﬀ.
11.5.3. Geometric decomposition. The geometric decomposition is a
slight variation of the canonical torus decomposition that is more suited to
the geometrisation perspective that we will encounter in the next chapters.
It is constructed from the canonical torus decompositionS forM as follows.
Whenever a blockN of the torus decomposition is diﬀeomorphic toK×∼ I,
we substitute the torus∂N inS with the core Klein bottleK ofK×∼ I. This
substitution has the eﬀect of deletingN from the list of blocks of the decom-
position.
ThegeometricdecompositionconsistsofincompressibletoriandKleinbot-
tles. One reason for preferring the geometric decomposition to the canonical
torus one is that it contains no interval bundles and every Seifert block has a
unique ﬁbration up to isotopy (because we have eliminated theK×∼ I blocks).
In particular we get the following easy criterion, whose proof is straightforward.
Proposition 11.5.6. Let M be an orientable irreducible and∂-irreducible
compact 3-manifold with (possibly empty) boundary consisting of tori. A non-
empty torus decomposition ofM is the geometric one if and only if:
• every block is simple or Seifert withχ< 0,
• the ﬁbrations of two adjacent Seifert blocks do not match.
Another reason for preferring the geometric decomposition is that every
Seifert block can be geometrised with ﬁnite volume, whereasK×∼ I needs
inﬁnite volume (this will be shown in the next chapter).
Geometric decompositions also behave well under ﬁnite coverings. Let
˜M→M beaﬁnitecoveringbetweentwoorientableirreducibleand ∂-irreducible
compact 3-manifolds with (possibly empty) boundary consisting of tori.
Proposition 11.5.7.The geometric decomposition of˜M is the counterim-
age of that ofM.
Proof. The criterion of Proposition 11.5.6 lifts fromM to ˜M. □
11.5. JSJ DECOMPOSITION 367
11.5.4. Graph manifolds. Waldhausen introduced in the 1960s a simple
but non-trivial class of three-manifolds using only two blocks. HereD and P
are the disc and the pair-of-pants.
Deﬁnition 11.5.8. Agraph manifoldis any orientable three-manifold that
decomposes along disjoint tori into pieces diﬀeomorphic toD×S1 orP×S1.
One may describe any such manifold via a graph with vertices of valence
1 and 3 representing the blocks, and some appropriate2× 2-matrices labelling
the edges telling the way the two incident blocks are glued. As usual, diﬀerent
graphs may represent the same manifold.
Exercise 11.5.9. LetM be an orientable three-manifold. The following are
equivalent:
(1) M is a graph manifold,
(2) M = M1#... #Mh for some prime manifoldsMi whose geometric
decompositions consist of Seifert manifolds or torus (semi-)bundles.
Hint. Use Corollary 10.3.44 and Proposition 11.5.6. □
11.5.5. References. Most of the arguments contained in this chapter are
well-known to three-dimensional topologists and can be found in many books.
A standard introduction to knots and links is Rolfsen [50], and much more
on Dehn surgeries and their four-dimensional interpretations is contained in
Gompf – Stipsicz [23]. A proof of the JSJ decomposition can be found in
Hatcher [26], the original papers of Jaco – Shalen and Johannson are [31] and
[32]. Fomenko – Matveev [18] contains a chapter devoted to graph manifolds;
the original paper of Waldhausen is [60].
CHAPTER 12
The eight geometries
We have concluded the previous chapter by deﬁning ageometric decom-
position of three-manifolds along sphere and tori. The reason for using this
terminology is the famousgeometrisation conjecture, proposed by Thurston in
1982 and proved by Perelman in 2003, which states that each of the blocks of
the decomposition should begeometric, in the sense that it may be equipped
with a nice Riemannian metric.
There are eight nice Riemannian metrics available in dimension three.
Three of them are the constant curvature ones (hyperbolic, elliptic, and ﬂat),
while the other ﬁve are some kind of (sometimes twisted) products of low-
dimensional geometries. All these metrics arehomogeneous: distinct points
have isometric neighbourhoods.
The Seifert manifolds studied in the previous chapters occupy precisely six
of these eight geometries, and we analyse them in detail here.
