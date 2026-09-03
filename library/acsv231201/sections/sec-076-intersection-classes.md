---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-076-intersection-classes
section_title: "Intersection classes"
section_number: null
pages: 498-503
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
illustrate how to convert the Cauchy integral into an integral lying “on” the
singular setV⊂ Cd of F. After introducing these concepts, we discuss how
to use Morse theory to manipulate integrals over chains in V into representa-
tions that will ultimately allow us to use saddle point approximations. Morse
theory is a large subject, and our treatment is restricted to the core topics we
need: height functions, attachments, homology groups, and homotopy type. In
this appendix we focus on the case where V∗ :=V∩ Cd
∗ is a complex mani-
fold. Appendix D, our ﬁnal appendix, describes extensions of this material to
general algebraic sets (and their complements) using stratiﬁed Morse theory.
480
C.1 Intersection classes 481
C.1 Intersection classes
Before describing how to generalize residues from the classical univariate set-
ting to several variables, we ﬁrst need to describe the domains of integration
over which we can take multidimensional residues of di ﬀerential forms with
singularities onV. These domains of integration will be intersection classes.
The intuition behind intersection classes is captured in Figure C.1. A torusT
on one side ofV expands to a torus T′ on the other side ofV. Mathematically,
this expansion could be obtained by expanding each coordinate at a constant
rate, or by a more complicated deformation, or perhaps not by a deformation
at all but through a cobordism, meaning some ( d + 1)-chain whose boundary
is T′− T. In getting from T to T′ this expansion crossesV; if the crossing is
transverse, as it will be generically, it sweeps out a ( d− 1)-chainγ⊆V . For
the intersection class to be well deﬁned for our purposes, the homology class
ofγ in Hd−1(V∗) should depend only on the homology classes of T and T′ in
M.
Figure C.1 The intersection class of a cobordism from α toβ.
The concepts involved in deﬁning an intersection class are analytic in nature,
so we work with analytic functions instead of restricting ourselves to polyno-
mials. LetV =VQ be the complex manifold in Cd deﬁned by the vanishing
of an analytic function Q(z) onCd whose gradient does not vanish onV. Our
ﬁrst step in constructing the intersection class is to derive a diﬀeomorphism be-
tween a neighborhood ofV inCd and a product A× B, where A is a connected
482 Residue forms and classical Morse theory
open set inV and B is a neighborhood of the origin inC. This is accomplished
by considering the embedded complex manifold V in its ambient space Cd.
The tangent bundle of V may be identiﬁed with a sub-bundle of the tangent
space toCd by sendingv to e∗(v), where e :V→ Cd is the embedding ofV
intoCd.
Recall from Appendix A that for anyw∈Cd there is a natural identiﬁcation
φ of the tangent space TwCd withCd using the standard basis∂/∂z1,...,∂/∂ zd
for the holomorphic tangent space. Intuitively, we decompose Cd nearw by
taking the tangent plane toV atw and its orthogonal complement. Formally,
the embedded tangent spaceand the embedded normal spaceofV atw are the
subsets Sw :={w+φ(e∗(X)) : X∈ TwV} and S′
w :={w+v :v∈ NwV} ofCd,
respectively, where NwV⊆ Cd is the orthogonal complement toφ(e∗(TwV)).
Under our assumptions, NwV is the one-dimensional complex vector space
(or two-dimensional real vector space) described in local coordinates as the
span of the vector (∇ Q)(w). The total space of the normal bundle toV is the
set{(w,v)∈V× Cd :v∈ NwV} pairing elements ofV and normal vectors.
Lemma C.1 (Collar Lemma). Under our running assumption that the gra-
dient of Q is nonvanishing on V, there is an open neighborhood of V inCd
that is di ﬀeomorphic to the total space of the normal bundle to V under a
diﬀeomorphism that mapsw∈V to the vector (w, 0).
Proof Because∇ Q is nonvanishing onV, the gradient ∇ Q is non-zero in
a neighborhood ofV and thus deﬁnes a complex line bundle whose integral
surfaces have real dimension two. If U is any suﬃciently small neighborhood
ofV, we let a : U→V be the map sendingz∈ U to the unique point ofV
on whose integral curve it lies; see Figure C.2. The map ψ sendingz∈ U to
ψ(z) = (a(z),ρ (z)) is the desired diﬀeomorphism, whereρ(z) is the projection
ofz−a(z) onto the aﬃne set S′
a(z), becauseρ(z)∈ Na(z)V by construction and
the kernels of da and dρ are transverse onV (they are orthogonal subspaces),
hence also transverse in a suﬃciently small neighborhood ofV. □
Lemma C.1 implies that for anyk-chainγ inV we can deﬁne a (k+1)-chain
oγ, which we call a tube aroundγ, by taking the union of small circles in the
ﬁbers of the normal bundle with centers in γ. The radii of these disks should
be positive and small enough to ﬁt into the domain of the collar map, but can
(continuously) vary with the point on the base. Diﬀerent choices of the radii of
these circles lead to homologous tubes. Similarly, we let•γ denote the union of
solid disks in the ﬁbers of the normal bundle with centers inγ. The elementary
rules for boundaries of products imply
∂(oγ) = o(∂γ) and ∂(•γ) = oγ∪• (∂γ).
C.1 Intersection classes 483
Figure C.2 Integral curves (dotted) making up the normal bundle, and a decom-
position ofz into (a(z),ρ (z)).
Because o commutes with∂, cycles map to cycles, boundaries map to bound-
aries, and the map o on the singular chain complex ofV induces a map from
Hk−1(V∗) to Hk(M), whereM =Cd
∗\V . To simplify notation, we also denote
this map on homology by o.
We are now ready to deﬁne intersection classes after recalling a few con-
structions from diﬀerential geometry. Two submanifolds A, B⊂Cd are said to
intersect transversely if for all w∈ A∩ B the tangent spaces of A and B at
w jointly span Cd. Two classic results of di ﬀerential geometry state that if A
and B intersect transversely then A∩ B is a manifold, and that if B is ﬁxed and
A is any manifold then A can be slightly perturbed into a manifold A′ that in-
tersects B transversely (i.e., transversality is a generic property) – see [Hir76,
Chapter 3], for instance.
Theorem C.2 (intersection classes). Deﬁne o : Hd−1(V)→ Hd(M) as above.
Under our running assumption thatV is a manifold,
(i) ◦ is injective and its image is the kernel of the map ι∗ induced by the
inclusionM
ι
−→Cd
∗.
(ii) Given α∈ ker(ι∗) one may compute the inverseI(α) = o−1(α) by inter-
sectingV∗ with any (d + 1)-chain inCd+1
∗ whose boundary is α and for
which the intersection withV∗ is transverse.
Whenα =C−C ′ in Theorem C.2, whereC andC′ are two d-cycles inM
homologous in Cd
∗, we call INT[C,C′;V] =I(C−C ′) the intersection class
ofC andC′. We usually use the intersection class whenC = T andC′ = T′ are
484 Residue forms and classical Morse theory
tori and T′ can be deformed to points where the Cauchy integral representing
a multivariate sequence is asymptotically negligible.
Proof of Theorem C.2 The Thom–Gysin long exact sequence implies exact-
ness of a sequence
0→ Hd−1(V∗)
o
→ Hd(M)→ Hd(Cd
∗). (C.1.1)
This may be found in [Gor75, page 127] (where, in the notation of that source,
W =Cd
∗) though in the particular situation at hand it goes back to Leray [Ler59].
Injectivity of o follows from exactness at Hd−1(V∗) while the rest of part ( i)
follows from exactness at Hd(M).
For part (ii), we begin by showing that the map I which takes a subset S of
Cd
∗ transverse toV∗ and returns I(S ) = S∩V∗ induces a well-deﬁned map from
ker(ι∗) to Hd−1(V∗). Because transversality is generic, given any α∈ ker(ι∗)
there exist (d + 1)-chains intersectingV∗ transversely whose boundary isα. If
D is such a chain andC = I(D) thenC is a cycle, since
∂C =∂(D∩V ∗) = (∂D)∩V∗ =α∩V∗ =∅.
LetD1 andD2 be two such chains, and deﬁne C j =D j∩V∗. Observe that
D1−D 2 is null homologous because there is no (d + 1)-homology inCd
∗. Thus,
D1−D 2 =∂ H for some (d + 1)-chain H inCd
∗. Choosing H transverse toV∗,
C1−C 2 = I(D1−D 2) =∂(H∩V∗)
is a boundary inV∗. Thus, the class [I(D)] in Hd−1(V∗) is the same for anyD
with∂D = α. Ifα = o(γ) then takingD =•(γ) gives I(D) = γ, showing that
I does in fact invert o and thus computesI. □
Remark C.3. BecauseC∗ is topologically a circle, the homology groupHd(Cd
∗)
is cyclic and generated by a product of small circles about the coordinate axes,
and Hk(Cd
∗) vanishes for k > d. The kernel of ι∗ consists of the classes that
don’t link the origin in Cd
∗, i.e., the classes σ for which the integer invariant
𝓁(σ) = (2πi)−d ∫
σ dz1/z1∧···∧ dzd/zd vanishes. This holds, for example, if
σ = T− T′, where T and T′ are standard oriented tori around the origin, since
𝓁(T) =𝓁(T′) = 1.
There is a version of the intersection class in relative homology as well.
This will be useful to us when we integrate over a diﬀerence of tori, one being
the starting domain of integration in the Cauchy integral and the other being
a “large” torus, because it helps us ignore whether we have chosen a large
enough torus to avoidV∗ at points that are asymptotically negligible. We omit
the proof of this construction, which is similar to the proof of Theorem C.2.
