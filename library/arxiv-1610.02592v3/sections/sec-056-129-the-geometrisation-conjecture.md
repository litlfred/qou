---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-056-129-the-geometrisation-conjecture
section_title: "The geometrisation conjecture"
section_number: 12.9
pages: 409-413
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
(by Propositions 1.4.3 and 1.4.10) the groupπ1(S) would also be, and hence
it would contain a normal cyclic subgroup, contradicting Corollary 5.1.10.
If X =~SL2 thenπ1(S) =π1(M)/K and no ﬁnite-index subgroup ofπ1(S)
can lift toπ1(M) by Proposition 12.6.4.
Finally, if X = H3 then π1(M) contains no normal cyclic groupK by
Corollary 5.1.10 again. □
The boundary case is slightly diﬀerent. Of the eight geometries, only three
produce non-compact ﬁnite-volume complete orientable manifolds:
H3, H2× R, ~SL2.
These non-compact ﬁnite-volume manifolds are diﬀeomorphic to the interior
of a compact manifoldM with boundary consisting of tori.
Theorem12.8.4. LetM beacompactorientable3-manifoldwithboundary
consisting of tori. The following are equivalent:
• M has a ﬁnite-volume completeH2× R structure,
• M has a ﬁnite-volume complete~SL2 structure,
• M is Seifert withχ< 0.
In contrast with the closed case, a non-closedM may admit two diﬀerent
geometric structures of Seifert type. On the other hand, a manifoldM cannot
admit both a hyperbolic and a Seifert structure.
12.9. The geometrisation conjecture
We can ﬁnally state the famous Geometrisation Conjecture, proposed by
Thurston in 1982 and proved twenty years later by Perelman in 2002.
12.9.1. Statement and main consequences.We say that a compact 3-
manifold with (possibly empty) boundary consisting of tori isgeometric if its
interior has a ﬁnite-volume complete geometric structure modelled on one of
the eight geometries:
S3, R3, H3, S2× R, H2× R, Nil, Sol, ~SL2.
The following conjecture was formulated by Thurston in 1982:
Conjecture 12.9.1 (Geometrisation Conjecture).Let M be an irreducible
orientable compact 3-manifold with (possibly empty) boundary consisting of
tori. Every block of the geometric decomposition ofM is geometric.
The conjecture has been proved by Perelman in 2002 and its proof goes
very very far from the scope of this book. It is however quite easy to deduce
important consequences from it.
Conjecture 12.9.2 (Poincaré conjecture).Every simply connected closed
3-manifoldM is diﬀeomorphic toS3.
402 12. THE EIGHT GEOMETRIES
Proof using geometrisation. Via the prime decomposition we may restrict
to the caseM is prime, hence irreducible. The groupπ1(M) is trivial and
hence does not containZ× Z: every torus inM is thus compressible and the
geometric decomposition is trivial. By geometrisationM is itself geometric.
The only geometry with ﬁnite fundamental groups isS3, and henceM =S3/Γ
is elliptic. SinceM is simply connected, the groupΓ = π1(M) is trivial and
henceM =S3. □
Conjecture 12.9.3 (Elliptisation). Every closed 3-manifoldM with ﬁnite
π1(M) is elliptic.
Proof using geometrisation. Same proof as above. Note that this isnot a
consequence of Poincaré conjecture in general, for a manifold covered bySn
needs not to be elliptic a priori. □
Conjecture 12.9.4 (Hyperbolisation). Every closed irreducible 3-manifold
M with inﬁniteπ1(M) not containing Z× Z is hyperbolic.
Proof using geometrisation. Sinceπ1(M) does not contain Z× Z every
torus is compressible and the geometric decomposition ofM is trivial. By
geometrisationM is geometric. Its geometry is notS3 sinceπ1(M) is inﬁnite,
and is notS2× R sinceM is irreducible. In the other Seifert geometries and
in Sol the fundamental groupπ1(M) always contain aZ× Z (there is always
a ﬁnite covering containing an incompressible torus). □
Corollary 12.9.5.Let ˜M→M be a ﬁnite covering. If˜M is geometric, then
M also is (with the same geometry).
Proof using geometrisation. Note that this is stronger than Conjecture
12.9.3. Since ˜M is geometric, it is irreducible and hence alsoM is. Proposi-
tion 11.5.7 implies that the geometric decomposition ofM is trivial, and by
geometrisationM is geometric. □
Concerning bounded manifolds, we get the following simple statement.
Corollary 12.9.6. Every simple compact manifoldM bounded by a non-
empty collection of tori is hyperbolic.
Proof using geometrisation. Being simple, it is geometric. Seifert mani-
folds with boundary are never simple. □
That statement is not true for closed manifolds, because many Seifert
manifolds ﬁbering overS2 with at most 3 singular ﬁbres are simple.
12.9.2. Surface bundles. There is a nice way to formulate geometrisa-
tion for surface bundles. We start with the much simpler torus case.
Proposition 12.9.7. Let MA be a torus bundle with monodromyA⁄=±I.
The following holds:
12.9. THE GEOMETRISATION CONJECTURE 403
• if|trA|< 2, i.e.A has ﬁnite order, thenMA is ﬂat;
• if|trA| = 2, i.e.A is reducible, thenMA is Nil;
• if|trA|> 2, i.e.A is Anosov, thenMA is Sol.
Proof. Use Proposition 11.4.14. □
We now turn to the generic case. LetΣ be a closed orientable surface
withχ(Σ)< 0.
Theorem 12.9.8.LetMψ be a surface bundle with ﬁbreΣ and monodromy
ψ∈ MCG(Σ). The following holds:
• ifψ has ﬁnite order, thenMψ has a H2× R geometry,
• ifψ is reducible, thenMψ contains an essential torus,
• ifψ is pseudo-Anosov, thenMψ is hyperbolic.
Proof using geometrisation. Use Proposition 11.4.15. □
Theorem 12.9.8 was initially proved by Thurston in the 1980s. In the
same years Thurston also proved the geometrisation conjecture for all Haken
3-manifolds. Before Perelman’s proof the conjecture was open “only” in the
non-Haken case, and it naturally split in three parts: the Conjectures 12.9.2,
12.9.3, and 12.9.4. Perelman’s proof certiﬁes geometrisation in all cases with
a uniﬁed technique.
12.9.3. References. This chapter contains many technical proofs. Most
of them were taken from Scott [52], that is the standard reference on the
geometrisation of Seifert manifolds, and Thurson’s book [57]. We have also
consulted a nice survey of Bonahon [8], that contains in particular the sugges-
tion of calculating the Ricci tensors in the non-product geometries. Thurson’s
geometrisation conjecture appears in [58] in 1982, while Perelman’s proof con-
sists of three papers that he sent to the arXiv in 2003 [45, 46, 47].
CHAPTER 13
Mostow rigidity theorem
We have deﬁned in Chapter 7 the Teichmüller spaceTeich(Sg) of a genus-
g closed orientable surfaceSg as the space of all the hyperbolic metrics onSg,
considered up to isometries isotopic to the identity; we have then proved that
Teich(Sg) is homeomorphic toR6g−6 using the Fenchel–Nielsen coordinates.
This deﬁnition ofTeich(M) actually applies to any closed hyperbolic man-
ifold M, and we show here a striking diﬀerence between the dimensions two
and three: ifdimM = 3 then Teich(M) is a single point. This strong result is
known as theMostow rigidity Theorem.
TheimpactofMostow’srigidityonourunderstandingofthree-dimensional
topology cannot be overestimated. Thanks to this theorem every geometric
information on a given closed hyperbolic three-manifoldM like its volume,
geodesic spectrum, etc. is promoted to atopological invariant ofM, that is
it depends on the diﬀerentiable structure ofM only. In its strongest version,
Mostow’s rigidity says that the hyperbolic metric ofM is fully determined by
the groupπ1(M) alone.
We expose here Gromov’s proof of Mostow’s rigidity, which uses hyper-
bolic tetrahedra and introduces a nice invariant on closed manifolds of any
dimension, called thesimplicial volume.
