---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-088-intersection-classes
section_title: "Intersection classes"
section_number: null
pages: 499-503
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
481
C.1 Intersection classes
Before describing how to generalize residues from the classical univariate set-
ting to several variables, we ﬁrst need to describe the domains of integration
over which we can take multidimensional residues of diﬀerential forms with
singularities on V. These domains of integration will be intersection classes.
The intuition behind intersection classes is captured in Figure C.1. A torus T
on one side of V expands to a torus T ′ on the other side of V. Mathematically,
this expansion could be obtained by expanding each coordinate at a constant
rate, or by a more complicated deformation, or perhaps not by a deformation
at all but through a cobordism, meaning some (d + 1)-chain whose boundary
is T ′ −T. In getting from T to T ′ this expansion crosses V; if the crossing is
transverse, as it will be generically, it sweeps out a (d −1)-chain γ ⊆V. For
the intersection class to be well deﬁned for our purposes, the homology class
of γ in Hd−1(V∗) should depend only on the homology classes of T and T ′ in
M.
Figure C.1 The intersection class of a cobordism from α to β.
The concepts involved in deﬁning an intersection class are analytic in nature,
so we work with analytic functions instead of restricting ourselves to polyno-
mials. Let V = VQ be the complex manifold in Cd deﬁned by the vanishing
of an analytic function Q(z) on Cd whose gradient does not vanish on V. Our
ﬁrst step in constructing the intersection class is to derive a diﬀeomorphism be-
tween a neighborhood of V in Cd and a product A × B, where A is a connected
482
Residue forms and classical Morse theory
open set in V and B is a neighborhood of the origin in C. This is accomplished
by considering the embedded complex manifold V in its ambient space Cd.
The tangent bundle of V may be identiﬁed with a sub-bundle of the tangent
space to Cd by sending v to e∗(v), where e : V →Cd is the embedding of V
into Cd.
Recall from Appendix A that for any w ∈Cd there is a natural identiﬁcation
φ of the tangent space TwCd with Cd using the standard basis ∂/∂z1, . . . , ∂/∂zd
for the holomorphic tangent space. Intuitively, we decompose Cd near w by
taking the tangent plane to V at w and its orthogonal complement. Formally,
the embedded tangent space and the embedded normal space of V at w are the
subsets S w := {w+φ(e∗(X)) : X ∈TwV} and S ′
w := {w+v : v ∈NwV} of Cd,
respectively, where NwV ⊆Cd is the orthogonal complement to φ(e∗(TwV)).
Under our assumptions, NwV is the one-dimensional complex vector space
(or two-dimensional real vector space) described in local coordinates as the
span of the vector (∇Q)(w). The total space of the normal bundle to V is the
set {(w, v) ∈V × Cd : v ∈NwV} pairing elements of V and normal vectors.
Lemma C.1 (Collar Lemma). Under our running assumption that the gra-
dient of Q is nonvanishing on V, there is an open neighborhood of V in Cd
that is diﬀeomorphic to the total space of the normal bundle to V under a
diﬀeomorphism that maps w ∈V to the vector (w, 0).
Proof
Because ∇Q is nonvanishing on V, the gradient ∇Q is non-zero in
a neighborhood of V and thus deﬁnes a complex line bundle whose integral
surfaces have real dimension two. If U is any suﬃciently small neighborhood
of V, we let a : U →V be the map sending z ∈U to the unique point of V
on whose integral curve it lies; see Figure C.2. The map ψ sending z ∈U to
ψ(z) = (a(z), ρ(z)) is the desired diﬀeomorphism, where ρ(z) is the projection
of z−a(z) onto the aﬃne set S ′
a(z), because ρ(z) ∈Na(z)V by construction and
the kernels of da and dρ are transverse on V (they are orthogonal subspaces),
hence also transverse in a suﬃciently small neighborhood of V.
□
Lemma C.1 implies that for any k-chain γ in V we can deﬁne a (k+1)-chain
oγ, which we call a tube around γ, by taking the union of small circles in the
ﬁbers of the normal bundle with centers in γ. The radii of these disks should
be positive and small enough to ﬁt into the domain of the collar map, but can
(continuously) vary with the point on the base. Diﬀerent choices of the radii of
these circles lead to homologous tubes. Similarly, we let •γ denote the union of
solid disks in the ﬁbers of the normal bundle with centers in γ. The elementary
rules for boundaries of products imply
∂(oγ) = o(∂γ)
and
∂(•γ) = oγ ∪•(∂γ) .
C.1 Intersection classes
483
Figure C.2 Integral curves (dotted) making up the normal bundle, and a decom-
position of z into (a(z), ρ(z)).
Because o commutes with ∂, cycles map to cycles, boundaries map to bound-
aries, and the map o on the singular chain complex of V induces a map from
Hk−1(V∗) to Hk(M), where M = Cd
∗\ V. To simplify notation, we also denote
this map on homology by o.
We are now ready to deﬁne intersection classes after recalling a few con-
structions from diﬀerential geometry. Two submanifolds A, B ⊂Cd are said to
intersect transversely if for all w ∈A ∩B the tangent spaces of A and B at
w jointly span Cd. Two classic results of diﬀerential geometry state that if A
and B intersect transversely then A ∩B is a manifold, and that if B is ﬁxed and
A is any manifold then A can be slightly perturbed into a manifold A′ that in-
tersects B transversely (i.e., transversality is a generic property) – see [Hir76,
Chapter 3], for instance.
Theorem C.2 (intersection classes). Deﬁne o : Hd−1(V) →Hd(M) as above.
Under our running assumption that V is a manifold,
(i) ◦is injective and its image is the kernel of the map ι∗induced by the
inclusion M
ι
−→Cd
∗.
(ii) Given α ∈ker(ι∗) one may compute the inverse I(α) = o−1(α) by inter-
secting V∗with any (d + 1)-chain in Cd+1
∗
whose boundary is α and for
which the intersection with V∗is transverse.
When α = C −C′ in Theorem C.2, where C and C′ are two d-cycles in M
homologous in Cd
∗, we call INT[C, C′; V] = I(C −C′) the intersection class
of C and C′. We usually use the intersection class when C = T and C′ = T ′ are
484
Residue forms and classical Morse theory
tori and T ′ can be deformed to points where the Cauchy integral representing
a multivariate sequence is asymptotically negligible.
Proof of Theorem C.2
The Thom–Gysin long exact sequence implies exact-
ness of a sequence
0 →Hd−1(V∗)
o→Hd(M) →Hd(Cd
∗).
(C.1.1)
This may be found in [Gor75, page 127] (where, in the notation of that source,
W = Cd
∗) though in the particular situation at hand it goes back to Leray [Ler59].
Injectivity of o follows from exactness at Hd−1(V∗) while the rest of part (i)
follows from exactness at Hd(M).
For part (ii), we begin by showing that the map I which takes a subset S of
Cd
∗transverse to V∗and returns I(S ) = S ∩V∗induces a well-deﬁned map from
ker(ι∗) to Hd−1(V∗). Because transversality is generic, given any α ∈ker(ι∗)
there exist (d + 1)-chains intersecting V∗transversely whose boundary is α. If
D is such a chain and C = I(D) then C is a cycle, since
∂C = ∂(D ∩V∗) = (∂D) ∩V∗= α ∩V∗= ∅.
Let D1 and D2 be two such chains, and deﬁne Cj = D j ∩V∗. Observe that
D1 −D2 is null homologous because there is no (d +1)-homology in Cd
∗. Thus,
D1 −D2 = ∂H for some (d + 1)-chain H in Cd
∗. Choosing H transverse to V∗,
C1 −C2 = I(D1 −D2) = ∂(H ∩V∗)
is a boundary in V∗. Thus, the class [I(D)] in Hd−1(V∗) is the same for any D
with ∂D = α. If α = o(γ) then taking D = •(γ) gives I(D) = γ, showing that
I does in fact invert o and thus computes I.
□
Remark C.3. Because C∗is topologically a circle, the homology group Hd(Cd
∗)
is cyclic and generated by a product of small circles about the coordinate axes,
and Hk(Cd
∗) vanishes for k > d. The kernel of ι∗consists of the classes that
don’t link the origin in Cd
∗, i.e., the classes σ for which the integer invariant
ℓ(σ) = (2πi)−d R
σ dz1/z1 ∧· · · ∧dzd/zd vanishes. This holds, for example, if
σ = T −T ′, where T and T ′ are standard oriented tori around the origin, since
ℓ(T) = ℓ(T ′) = 1.
There is a version of the intersection class in relative homology as well.
This will be useful to us when we integrate over a diﬀerence of tori, one being
the starting domain of integration in the Cauchy integral and the other being
a “large” torus, because it helps us ignore whether we have chosen a large
enough torus to avoid V∗at points that are asymptotically negligible. We omit
the proof of this construction, which is similar to the proof of Theorem C.2.
