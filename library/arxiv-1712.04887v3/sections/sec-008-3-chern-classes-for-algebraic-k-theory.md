---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K-THEORY"
section_id: sec-008-3-chern-classes-for-algebraic-k-theory
section_title: "Chern Classes for algebraic K-theory"
section_number: 3
pages: 17-20
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "BLOCH GROUPS, ALGEBRAICK-THEORY — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F (e2πi/n), well-deﬁned up to n-th"
---
In this section, we will deﬁne the Chern class map (11).
3.1. Deﬁnitions. In the following discussion, certain isomorphisms will depend on a choice
of some primitive nth root of unity ζ. In order to make this clear, we shall write (in this
section only) either =ζ or = to denote isomorphisms which respectively do or do not depend
on such a choice. Let F be a number ﬁeld, and let O :=OF denote the ring of integers of
F . The Tate twist Zp(1) is deﬁned to be the projective limit proj limµpn of thepnth roots of
unity over all n, and Zp(m) := Zp(1)⊗m. The Galois group GF acts on Zp(m) via the mth
powerχm of the cyclotomic character. For all m≥ 1, there exists a Chern class map:
c :K2m−1(F )→H1(F, Zp(m)).
These Chern class maps arise as the boundary map of a spectral sequence, speciﬁcally,
the Atiyah–Hirzebruch spectral sequence for ´ etale K-theory. These maps were originally
constructed by Soul´ e [26, Section II]. We may compose this map with reduction mod pi to
obtain a map:
c :K2m−1(F )→H1(F, Z/piZ(m)).
By the Chinese remainder theorem, we may also piece these maps together to obtain a map:
c :K2m−1(F )→H1(F, Z/nZ(m))
for any integer n. Let ζ be a primitive nth root of unity, Fn = F (ζ) and write G for the
(possibly trivial) Galois group Gal( Fn/F ). Let µ denote the module of n roots of unity.
There is a canonical injection
χ :G→ Aut(µ) = (Z/nZ)×.
By inﬂation–restriction, there is a canonical map:
H1(F, Z/nZ(m))→H1(Fn, Z/nZ(m))G (27)
Form≥ 1, there is an invariant wm(F )∈ N that we will need. It is deﬁned in terms of
Galois cohomology by
wm(F ) =
∏
p
⏐⏐H0(F, Qp/Zp(m))
⏐⏐,
18 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
Note that w1(F ) is equal to wF , the number of roots of unity in F , and w2(F ) agrees
with (10) because the action of GF on Z/nZ(2)⊂ Qp/Zp(2) for any n precisely factors
through Gal(F (ζ +ζ−1)/F ) for a primitive nth root of unity ζ. We also deﬁne
~wF =
∏
p
⏐⏐H0(~F (ζp +ζ−1
p ), Qp/Zp(1))
⏐⏐. (28)
where ~F is the Galois closure of F over Q. Thus ~wF is divisible only by the ﬁnitely many
primesp suchζp belongs to ~F (ζp +ζ−1
p ). If p|~wF andp> 2, then p necessarily ramiﬁes in F .
Note that ~wF is always divisible by wF .
Lemma 3.1. The map (27) is injective for integers n prime to wm(F ).
Proof. The kernel of this map is H1(Fn/F, Z/nZ(m)). Assume that this is non-zero. By
Sah’s lemma, this group is annihilated by χm(g)− 1 for any g∈G. Equivalently, the kernel
has order divisible byp|n if and only if the elementsam−1 are divisible byp for all (a,p ) = 1.
Yet this is equivalent to saying that H0(F, Z/pZ(m))⊂ H0(F, Qp/Zp(m)) is non-zero, and
hence p|wm(F ). □
There is an isomorphism Z/nZ(1) = µ. A choice of primitive nth root of unity ζ gives a
trivialization tζ : Z/nZ(1) =ζ Z/nZ(m) deﬁned by sending ζ to ζ⊗n. This isomorphism is
not, in general, G-equivariant, but rather satisﬁes
tζ(σx) =χ1−m(σ)σtζ(x) (29)
The dependence of tζ on ζ is given by tζk = km−1tζ. By Hilbert 90, for a number ﬁeld L,
there is a canonical isomorphism H1(L,µ ) =L×/L×n, and hence (given ζ) an isomorphism
H1(Fn, Z/nZ(m))G =ζ H1(Fn, Z/nZ(1))χ1−m
=
(
F×
n/F×n
n
)χ1−m
,
where the ﬁrst isomorphism is induced by tζ. Thus c and ζ give rise to a map:
cζ :K2m−1(F )→
(
F×
n/F×n
n
)χ1−m
. (30)
3.2. The relation between ´ etale cohomology and Galois cohomology. There are
isomorphisms that can be found in Sections 5.2 and 5.4 of [35]
K2m−1(F )⊗ Zp≃K2m−1(OF [1/p])≃K2m−1(OF )⊗ Zp (31)
form> 1. These isomorphisms are also reﬂected in the following isomorphism between ´ etale
cohomology groups and Galois cohomology groups:
H1
´ et(OF [1/p], Zp(m))≃H1(F, Zp(m))
for m≥ 2. In particular, we may also view the Chern class maps considered above as
morphisms
c :K2m−1(F )⊗ Zp≃K2m−1(OF )⊗ Zp→H1
´ et(OF [1/p], Zp(m)).
Theorem 3.2. Forp> 2, there is an isomorphism
c :K3(F )⊗ Zp≃K3(OF )⊗ Zp→H1
´ et(OF [1/p], Zp(2)).
The rank of K3(F ) is r2.
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 19
Sketch. This follows from the Quillen–Lichtenbaum conjecture, as proven by Voevodsky and
Rost (see [35], [34]). In this case, it can also be deduced from the description of torsion
in K3(F ) by Merkurjev and Suslin [21] (described in terms of w2(F ) above) combined with
Borel’s theorem for the rank (see also Theorem 6.5 of [31]), and the result of Soul´ e that the
Chern class map is surjective. □
Lemma 3.3. Suppose that p ∤w2(F ) for every prime p with p2|n. Then the map
cζ :K3(F )→K3(F )/nK3(F )→
(
F×
n/F×n
n
)χ−1
(32)
is injective on K3(F )/nK3(F ).
Proof. By the Chinese Remainder Theorem, it suﬃces to consider the case n =pm. In light
of Theorem 3.2, it suﬃces to show that the map
H1(F, Zp(2))/n→H1(F, Z/nZ(2))→F×
n/F×n
n
is injective. The kernel of the ﬁrst map is H0(F, Zp(2))/n = 0. The kernel of the sec-
ond map is, via inﬂation–restriction, the group H1(Gal(Fn/F ),H 0(F, Z/nZ(2))). If n = p,
then Gal(Fn/F ) has order prime top and the cohomology group vanishes. If p2|n, this group
is certainly zero unless
H0(F, Z/nZ(2))⊂H0(F, Qp/Zp(2))
is non-zero, or in other words, unless p divides w2(F ). □
3.3. Upgrading from F×
n toOFn[1/S]×. The following is a consequence of the ﬁnite gen-
eration of K3(F ):
Lemma 3.4. For any ﬁeld F , there exists a ﬁnite set S of primes which avoids any given
ﬁnite set of primes not dividing n such that the image of cζ on K3(F )/nK3(F ) may be
realized by an element ofO×
F (ζ)[1/S].
Proof. Note that without the requirement that S avoids any given ﬁnite set of primes not
dividingn, the result is a trivial consequence of the fact thatK3(F ) is ﬁnitely generated. The
construction of c as a map to units in F×
n proceeded via Hilbert 90. In light of Theorem 3.2
above, it suﬃces to do the same with H1(Fn,µ ) replaced by H1
´ et(OFn[1/S],µ ) for some set S
containingp|n. However, in this case, the class group intervenes, as there is an exact sequence
([22], p.125):
OFn[1/S]×/OFn[1/S]×n→H1
´ et(OFn[1/S],µ )→ Pic(OFn[1/S])[n]
whereM[n] denotes then-torsion ofM and Pic is the Picard group, which may be identiﬁed
with the class group ofOFn[1/S]. On the other hand, it is well known that one can represent
generators in the class group by a set of primes avoiding any given ﬁnite set of primes,
and hence for a set S including primes for each generator of the class group, the last term
vanishes. □
20 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
