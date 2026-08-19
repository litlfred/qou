---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K-THEORY"
section_id: sec-014-51-proof-of-theorem-16
section_title: "Proof of Theorem 1.6"
section_number: 5.1
pages: 25-31
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "BLOCH GROUPS, ALGEBRAICK-THEORY — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F (e2πi/n), well-deﬁned up to n-th"
---
primitiventh root of unity. For a prime q≡− 1 mod n that splits completely in F , and for
a corresponding prime q aboveq, let Rζ,q denote the map B(OF/q) =B(Fq)→ F×
q2/F×n
q2 .
We have two maps we wish to compare. One of them is
cζ : B(F )/nB(F ) →
(
F×
n/F×n
n
)χ−1
.
Because B(F ) is a ﬁnitely generated abelian group, we may represent the generators of the
image by S-units for some ﬁxed S (at this point possibly depending on n) and consider the
map
cζ : B(F )/nB(F )→ (OF (ζ)[1/S]×/OF (ζ)[1/S]×n)χ−1
↪→
⨁
F×
q2/F×n
q2 ≃
⨁
B(Fq),
26 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
where the ﬁnal sum is over all but ﬁnitely may primes q of norm q≡− 1 modn which split
completely in F . We have the diagram
B(F )/nB(F ) Rζ- (OF (ζ)[1/S]×/OF (ζ)[1/S]×n)χ−1
⨁
B(Fq)⊗ Z/nZ
? Rζ,q -
⨁
F×
q2/F×n
q2 .
?
We have already shown, by Chebotarev (Proposition 4.2(b)), that cζ(ξ) for ξ∈ K3(F ) is
determined up to scalar by the set of primes for whichcζ,q(ξ) = 0. Hence the result is a formal
consequence of knowing that the mapsRζ,q are isomorphisms for all q of normq≡− 1 modn.
This is exactly Theorem 5.2 below. □
By (9), the p-torsion subgroup of K3(Q(ζ +ζ−1)) is isomorphic to Z/nZ. On the other
hand, since Q(ζ +ζ−1) is totally real, we have an isomorphism:
K3(Q(ζ +ζ−1))⊗ Zp≃ Z/nZ.
Lemma 5.1. Let p >2 and n = pm. Suppose that q≡− 1 mod n and q⁄≡− 1 mod pn.
The prime q splits completely in Q(ζ +ζ−1). Let Fq denote the residue ﬁeld at one of the
primes above q. Then the map
K3(Q(ζ +ζ−1))⊗ Zp→B(Fq)⊗ Zp
is an isomorphism.
Proof. Ifn is odd, a generator of B(Q(ζ +ζ−1))[n]≃K3(Q(ζ +ζ−1))⊗Zp is given explicitly
by the element
ηζ :=
∑
k modn
[
1−
( ζ−ζ−1
ζk−ζ−k
)2]
=
∑
k modn
(
[0] +
[(ζk−ζ−k
ζ−ζ−1
)2])
(34)
(The equivalence of these expressions follows from the identites [0] + [1 /X] = [0]− [X] =
[1−X].) This can also be proved by combining the calculation given on p. 40 of [37] with
the ones given at the end of Section 4.2, or following an argument similar to the proof of [39,
Theorem 1.4]. (See also [8, Proposition 5.4].) On the other hand, the reduction modulo any
prime above q generates the latter group, as follows from the discussion in Section 4.2 (see
in particular equation (33).) □
We now prove Theorem 5.2 as mentioned above:
Theorem 5.2. Letn be an odd prime power and q≡− 1 modn. Then the map
Rζ,q :B(Fq)⊗ Z/nZ→ F×
q2⊗ Z/nZ
is an isomorphism, where ζ is an nth root of unity.
Proof. Note thatB(Fq) is cyclic of orderq+1 up to 2-torsion, and F×
q2 is cyclic of orderq2−1.
In particular, for odd primes p withq≡− 1 modp, the groups B(Fq)⊗ Zp and F×
q2⊗ Zp are
isomorphic to each other and to Zp/(q + 1)Zp. We begin with the following:
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 27
Lemma 5.3. Forn an odd prime power,Rζ(ηζ) =ζγ∈ (Q(ζ)×/Q(ζ)×n)χ−1
for someγ∈ Zp.
Proof. Write ζn = ζ and let ζ′ be an n2th root of unity. Consider the image of Rζ′(ηζ′).
Becauseηζ is divisible by n inB(Q(ζ′)+), the image is a nth power. Hence, by the compat-
ibility of the maps R for varyingn (Lemma 2.7 (2)), it follows that Rζ(ηζ) lies in the kernel
of the map (
Q(ζ)×/Q(ζ)×n)χ−1
→
(
Q(ζ′)×/Q(ζ′)×n)χ−1
.
But this kernel consists precisely of nth roots of unity. □
Let ηζ,q ∈ B(Fq) denote the reduction of ηζ in B(Fq). By Lemma 5.1, the image also
generates B(Fq)⊗ Z/nZ. Since all primes q≡− 1 mod n split completely in Q(ζ)+, if
γ⁄≡ 0 mod p, the result above follows by specialization. We proceed by contradiction and
assume that γ≡ 0 mod p, which means that the image of the map Pζ,q is divisible by p for
all q of norm q satisfyingq≡− 1 modn. In particular, to prove the result, it suﬃces to ﬁnd
a single such q for which Rζ,q is an isomorphism.
Choose a completely split prime r in Q(ζ). Assume that
ζ≡a−1 mod r, ζ ⁄≡a−1 mod r2
for some integer a ⁄= 1. The splitting assumption means that an a satisfying the ﬁrst
condition exists. Replacing a−1 by (a +N(r))−1 if necessary implies the second, because
1
a− 1
a +N(r) = N(r)
a(a +N(r)) ⁄≡ 1 mod r2.
Let
τ =
n−1∏
k=0
(1−ζka)k ∈ Q(ζ)×.
Lemma 5.4. τ·ζi is not a perfect pth power for any i.
Proof. The assumption on r implies that all thepth roots of unity are distinct modulo r, and
hence the only factor of τ divisible by r is (1−aζ), which has valuation one. □
The element τ gives rise, via Kummer theory, to a Z/nZ-extension F/Q(ζ)+. By the
Lemma above, it is non-trivial. Let q≡− 1 mod n be prime. Then, for a prime q above q,
the element Frob q∈ Gal(F/Q(ζ)+) fails to generate Z/nZ if and only if τ is a perfect pth
power modulo q. This is equivalent to saying that Frobq generates Gal(F/Q(ζ)+) if and only
if
Rζ,q([an]) =Pζ,q([an]) =
n−1∏
k=0
(1−aζk)k∈ F×
q2⊗ Z/nZ
is a generator. Hence it suﬃces to ﬁnd a single q≡− 1 mod n and q⁄≡− 1 mod np with
the desired Frobenius. Such a q exists by Chebotarev density unless ⟨τ⟩ =⟨ζ⟩ mod Q(ζ)×p.
However, this cannot happen by Lemma 5.4. □
Proof of Theorem 1.2. Assume that n is prime to w2(F ). It follows that the Chern class
map gives an injection
K3(F )/nK3(F )→O Fn[1/S]×/OFn[1/S]×n
28 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
for some ﬁnite set of primes S. If, in addition, we assume that p does not divide ~wF , then
we deduce from Proposition 4.2 that this map can be extended to an injection into the
group⨁
qB(Fq)/nB(Fq). By Theorem 1.5, this agrees with the map Rζ deﬁned on B(F ),
which is thus injective. If one additionally assumes that n is prime to |∆F||K2(OF )|, then
by Lemma 3.4 one may additionally assume that the image is precisely the χ−1-invariants
ofO×
Fn/O×n
Fn . □
5.2. Digression: the mod-p-q dilogarithm. Letq be prime, and q + 1≡ 0 modn withn
a power of p as before. For convenience of exposition, assume that p > 3 so that Dζ(1)
is a perfect nth power. Fix an nth root of unity ζ in Fq2. Then there is a trivialization
logζ : F×
q2⊗ Z/nZ ≃ Z/nZ sending ζ to 1. The isomorphism B(Fq)⊗ Zp ≃ Z/nZ of
Theorem 5.2 now gives a curious function, the p-q dilogarithm, which is a function
L : Fq → F×
q2⊗ Z/nZ
logζ
→ Z/nZ
satisfying the 5-term relation. What is perhaps surprising is that the quantum logarithm
suﬃces to give an explicit formula, as follows.
Proposition 5.5. The function L is given by the formula
L(a) =
∑
bn=a
logζ(b) logζ(1−b) ( a∈ F×
q ),
where the sum is over the nth roots b of a in F×
q2.
Proof. Since F×
q has order prime to n, the element a has a unique nth power c ∈ F×
q .
Then (22) can be rewritten as L(a) = ∑
k modnk logζ(1−ζkc). (Note that Rζ = Pζ for
ﬁnite ﬁelds, and the assumption that p> 3 means that we can ignore theDζ(1) factor.) The
elements b = ζkc are the nth roots of a in F×
q2, and logζ(b) = k because c has order prime
to n and thus logζ(c) = 0. □
5.3. The Chern class map on n-torsion in Q (ζ)+. The following section contains a
speculative digression and is not used elsewhere in the paper. We have proved that the
mapscζ andRζ agree up to an invertible element of Z×
p . To determine the value of this ratio,
we need to compute the images of speciﬁc elements of the Bloch group. More speciﬁcally,
as explained in the introduction, we need the two statements (12) and (13). The ﬁrst of
these will be proved below (Theorem 7.4). Here we want to show that the second is not pure
fancy. We shall give a heuristic justiﬁcation of why the image of the Chern class map on ηζ
should be ζ — at least up to a sign and a small power of 2 in the exponent. We hope that
the arguments of this section could, with care, be made into a precise argument. However,
since the main conjecture of this section is somewhat orthogonal to the main purpose of this
paper, and correctly proving everything would (at the very least) involve establishing that
several diagrams relating the cohomology of SL 2 and PSL2 and GL2 and PGL2 commute up
to precise signs and factors of 2, we content ourselves with a sketch, and enter the happy
land where all diagrams commute.
The ﬁrst subtle point is that the relation between K3(F ) and B(F ) as established by
Suslin is not an isomorphism. There is always an issue with 2-torsion coming from the image
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 29
of Milnor K3. However, even for primes p away from 2, there is an exact sequence of Suslin
([30], Theorem 5.2; here F is a number ﬁeld so certainly inﬁnite):
0→ Tor1(µF,µF )⊗ Z[1/2]→K3(F )⊗ Z[1/2]→B(F )⊗ Z[1/2]→ 0,
and hence when p|wF =|µF|, the comparison map is not an isomorphism. (This is one
of the headaches which required us to assume that ζ /∈ F when computing the Chern
class map on B(F ).) This issue arises in the following way. Over the ﬁeld Q(ζ), the
Bott element provides a direct relationship between K1(F, Z/nZ) and K3(Z, Z/nZ). This
suggests we should push forward ηζ to Q(ζ) and compute the Chern class there. However,
since in B(Q(ζ)), the class ηζ may (and indeed does) become trivial, we instead consider ηζ
as an element of K3(Q(ζ)), and then compute the Chern class map directly in K-theory.
By Theorem 4.10 of Dupont–Sah [7], the diagonal map
x→
(
x 0
0 x−1
)
induces an injection
µC≃H3(µC, Z)→H3(SL2(C), Z)
whose image is precisely the torsion subgroup. (We shall be more precise about this ﬁrst
isomorphism below.) Let n be odd, and let ζ be a primitive nth root of unity, let E = Q(ζ),
and let E+ = Q(ζ)+. If µE is the group of nth roots of unity, the map µE→ SL2(E) is
conjugate to a map
µE→ SL2(E+)
as follows; send ζ to
t =A
(
ζ−1 0
0 ζ
)
A−1, where A =
(
ζ ζ−1
1 1
)
.
The cohomology of µE with coeﬃcients in Z/nZ is (non-canonically) isomorphic to Z/nZ in
all degrees. More precisely, there is a canonical isomorphism
H1(µE, Z) =H1(µE, Z/nZ) =µE,
we haveH2(µE, Z) = 0, and thus via the Bockstein mapH2(µE, Z/nZ) =H1(µE, Z)[n] =µE.
A choice of ζ leads to a choice of element β ∈ H2(µE, Z/nZ) = µE, and hence to an
isomorphism
µE =H1(µE, Z/nZ)
∗β
−→H3(µE, Z/nZ) =H3(µE, Z)
where the isomorphism is given by the Pontryagin product of µE with β∈ H2(µE, Z/nZ).
These choices induce a map
µE→H3(µE, Z)→H3(SL2(E+), Z)→K3(E+)→B(E+)
which sendsζ toηζ. That the image of ζ isηζ follows (for example) by §8.1 of [39]). Implicit
in this statement also is that the Pontryagin product of 1 ∈ Z/nZ = H1(Z/nZ, Z/nZ)
with 1 ∈ H2(Z/nZ, Z/nZ) is exactly the class constructed in Proposition 3.25 of Parry
and Sah [25]. (The maps above are only properly deﬁned modulo 2-torsion, since µ has odd
order this issue can safely be ignored). Denote by ηE+ the corresponding element inK3(E+).
The Chern class maps are compatible with base change, so to compute c(ηE+) it suﬃces to
compute c(ηE) where ηE∈ K3(E) is the image of ηE+ under the map K3(E+)→ K3(E).
30 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
The Chern class map on K1(E) = E× canonically sends ζ ∈ E× to ζ; we would like to
directly connect the Chern class map onK1 with the one onK3 using the Bott element. The
Bott element β∈K2(E; Z/nZ) is deﬁned as follows. There is an isomorphism:
µE = ker
(
E× n
−→E×
)
=π2(E×; Z/nZ).
The element β is deﬁned as the image of ζ under the composition
π2(BGL1(E); Z/nZ)→π2(BGL(E); Z/nZ)→π2(BGL(E)+; Z/nZ) =K2(E; Z/pZ).
The Bott element induces an isomorphism:
β :K1(E; Z/nZ)→K3(E; Z/nZ).
Hence there is, given our choice of ζ∈E, a canonically deﬁned map:
K3(E) E×/E×n
K3(E; Z/nZ)
?
cζ
-
K1(E, Z/nZ)
β−1
wwwwwwwww
c- E×/E×n
wwwwwwwwwwwwwwwwwwwwwww
Herecζ is the composition of the Chern class map toH1(E, Z/nZ(2)) which can be identiﬁed
with E×/E×n after a choice of ζ∈ E. Note that the deﬁnition of β also requires a similar
choice. Thus it makes sense to make the following:
Assumption 5.6. The diagram above commutes.
Using Assumption 5.6, we would like to show thatcζ(ηE) =ζ, and hence that cζ(ηE+) and
thuscζ(ηζ) are also both equal to ζ. This will follow if, under the Bott element, the class ηE
corresponds to ζ∈K1(E; Z/nZ). To prove this, one roughly has to show that the following
square commutes:
µE =H1(µE, Z/nZ) ∗β- H3(µE, Z/nZ)
E×/E×n =K1(E, Z/nZ)
? β- K3(E; Z/nZ).
?
The top line comes from the Pontryagin product structure of H1(µE, Z/nZ) =µE with
H2(µE, Z/nZ) = ker(µE
[n]
−→µE),
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 31
and the bottom line comes from Pontryagin product with the Bott elementβ coming via the
Bockstein map from
ker(E× [n]
−→E×).
We conveniently denote both maps by essentially the same letter in order to be more sugges-
tive. One caveat is that the maps from E×→ GL2(E) and µE→ SL2(E) considered above
diﬀer slightly in that x is sent to
(
x 0
0 1
)
and
(
x 0
0 x−1
)
respectively; since n is odd such
maps can be compared by comparing the cohomologies of GL, PGL, SL, and PSL respec-
tively; it is quite possible that such comparisons might require that the maps above include
a factor of 2 or −1 at some point.
The above discussion above makes the conjectured Equation (13) plausible.
