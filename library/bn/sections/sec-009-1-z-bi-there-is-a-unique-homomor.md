---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-009-1-z-bi-there-is-a-unique-homomor
section_title: "(z −bi). There is a unique homomor-"
section_number: 1
pages: 11-14
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove r- ings of P1, highlighting their"
---
phism w : π1(C −B) → Z/d sending a loop to the sum of its winding
numbers around the points of B; concretely, it is given by
w(α) = 1
2πi
∫
α
p′(z)dz
p(z) modd.
Let π :X → ˆC denote the corresponding covering of C −B, completed
to a branched covering of ˆC. Let T :X →X be the generator of the deck
group corresponding to 1 ∈ Z/d, and let ~∞ and ~B denote the preimages of
∞ and B under π. It is easy to see that |~B| = |B| and
e = |~∞| = gcd(d,n );
in particular, X is unramiﬁed over inﬁnity iﬀ d dividesn. By the Riemann-
Hurwitz formula, the genus g of X is given by
g = (n − 1)(d − 1) + 1 −e
2 ·
Eigenspaces. Recall that H 1(X, C) = H 1(X) carries a natural intersec-
tion form of signature ( g,g ), deﬁned by ( √−1/2)
∫
α ∧β. Any orientation-
preserving diﬀeomorphism of X preserves this form, so the map
f ↦→(f −1)∗|H 1(X) (2.3)
gives a natural unitary representation of the mapping-clas s group
Mod(X) → U(H 1(X)) ∼
= U(g,g ).
Since [T ] ∈ Mod(X) has order d, we also have an eigenspace decomposi-
tion
H 1(X) =
⨁
qd=1
H 1(X)q
where H 1(X)q = Ker(T ∗ −qI ). Let ( r,s ) denote the signature of the inter-
section form on H 1(X)q. The mapping-classes Mod( X)T commuting with
T also preserve these eigenspaces, so we have a natural repres entation
Mod(X)T → U(H 1(X)q) ∼
= U(r,s )
for each q.
10
Clearly the invariant cohomology satisﬁes H 1(X)1 ∼
= H 1(ˆC) ∼
= 0. For
the sequel, we assume qd = 1 but q ⁄= 1.
Lifting braids. To bring the braid group into the picture, observe that
any compactly supported diﬀeomorphism φ : (C,B ) → (C,B ) has a unique
lift ~φ : X → X which is the identity on a neighborhood of ~∞. This lifting
gives a natural map
Bn ∼
= Modc(C,B ) → Mod(X)T. (2.4)
Passing to cohomology, we obtain a natural representation
ρq :Bn → U(H 1(X)q) ∼
= U(r,s ).
Our goal is to understand this representation.
Lifting mapping classes. Note that any ψ ∈ Mod(C,B ) has a lift ~ψ toX
which is well-deﬁned up to a power of T ; we pass to the braid group only to
make the lift unique. Since T |H 1(X)q =qI , the representation ρq descends
to a map Mod( C,B ) → PU(r,s ). On the other hand, if X is unramiﬁed
over inﬁnity (i.e. if d|n), then ~ψ is uniquely determined by the condition
that it ﬁxes ~∞ pointwise, so ρq factors through Mod( C,B ). Similarly, if
X is unramiﬁed over ∞ then any ψ ∈ Mod(ˆC,B ) has a lift to X which is
well-deﬁned up to the action of T . Thus we have a commutative diagram:
Bn
/d15/d15
ρq /d47/d47U(r,s )
/d15/d15
Mod∗
0,n
/d15/d15
/d57/d57
/d47/d47PU(r,s )
Mod0,n
/d57/d57 (2.5)
whose diagonal arrows exist when d|n.
Invariant subsurfaces. To describeρq, we ﬁrst choose standard generators
τ1,...,τ n for Bn ∼
= Modc(C,B ). Each τi is a half Dehn twist supported in
an open disk Di ⊂ C withDi ∩B = {bi,b i+1} (or {bn,b 1} when i =n). Let
Xi =π−1(Di) ⊂X.
This is an open, connected, incompressible subsurface of X of genus
⌊(d − 1)/2⌋, with one or two boundary components (depending on the parit y
of d; see Figure 5).
11
i i+1b
8 b
Figure 5. The surface Xi is built from the Z/d-covering space of a pair of
pants in ˆC shown above, by capping oﬀ the inner and outer circles at the le ft
with disks.
LetYi be the closed subsurface X −Xi. Since τi is supported on Di and
~τi ﬁxes ~∞ ⊂ Yi, the lift ~τi is supported on Xi. In particular, both Xi and
Yi are invariant under T and~τi.
Action on cohomology . For n ≥ 3, Yi is connected. In this case, by
Mayer-Vietoris, we have an equivariant exact sequence
0 →H 1
c (Xi) →H 1(X) →H 1(Yi) → 0,
where H 1
c (Xi) denotes cohomology with compact supports. We denote the
corresponding exact sequence of eigenspaces of T by
0 →H 1
c (Xi)q →H 1(X)q →H 1(Yi)q → 0. (2.6)
The same sequences are exact for n = 2, except when d is even. If d
is even then Yi is disconnected (it is a pair of disjoint disks), and we have
instead the exact sequence
H 1(∂Xi) →H 1
c (Xi) →H 1(X) →H 1(Yi) = 0. (2.7)
In any case, since ~τi is supported in Xi, we have
~τ ∗
i |H 1(Yi) = I. (2.8)
In the next section we will show that ~τ ∗
i |H 1
c (Xi) = −qI .
Remark: stabilization. Note that if d divides d′, then the correspond-
ing branched covering X ′ factors through X, and we obtain an equivariant
isomorphism
ι :H 1(X)q ∼
=H 1(X ′)q.
12
Thus the representation ρq of Bn depends only on q, not on d. The isomor-
phismι is not, however, unitary; it multiplies the intersection fo rm by d′/d.
To obtain a unitary isomorphism, one must rescale ι by
√
d/d′.
