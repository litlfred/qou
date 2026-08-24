---
doc_id: arxiv-1712.04887v3
doc_title: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture"
section_id: sec-012-41-local-chern-class-maps
section_title: "Local Chern class maps"
section_number: 4.1
pages: 21-23
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F"
---
work with these primes for several (related) reasons. The ﬁrst is that the groups K3(Fq) we
consider below have orderq2−1, and so to see interesting classes inK3(F )/nK3(F ) we require
thatq2−1 be divisible byn, and this necessitates choosingq≡± 1 modn. On the other hand,
ifq≡ 1 modn, then Fq contains the nth roots of unity, which we generally need to avoid in
our construction. The reason to avoid nth roots of unity manifests itself quite concretely in
this setting: the Bloch group B(Fq) itself turns out to have order (more or less) q + 1 rather
thanq2−1, so it won’t see any interestingn-torsion classes unlessq≡− 1 modn. The residue
ﬁeld ofOF at q is Fq, and the residue ﬁeld of OF (ζ) at a prime Q above q is Fq2 = Fq(ζ).
Following Lemma 3.4, suppose that S does not contain any primes dividing q.
Lemma 4.1. There exists a commutative diagram of Chern class maps as follows:
K3(F )/nK3(F ) cζ- (O[1/S]×
F (ζ)/O[1/S]×n
F (ζ))χ−1
K3(Fq)/nK3(Fq)
?
= = = = = = = = = = =
cζ,q
F×
q2/F×n
q2 .
?
Proof. By the Chinese Reminder Theorem, we may reduce to the case when n =pm. There
is an isomorphismK3(F )⊗Zp≃K3(OF )⊗Zp (see Theorem 3.2). LetOF,q be the completion
ofOF at q. We have a more general diagram as follows:
K3(OF )/nK3(OF ) cζ- H1
´ et(OF [1/p], Z/nZ(2)) - (O[1/S]×
F (ζ)/O[1/S]×n
F (ζ))χ−1
K3(OF,q; Zp)/nK3(OF,q; Zp)
?
= = = =
cζ,q
H1
ur(OF,q, Z/nZ(2))
?
= = = = = = = = = = = =F×
q2/F×n
q2
?
K3(Fq)/nK3(Fq)
wwwwwwwww
= = = = = = = = = =
cζ,q
H1(Fq, Z/nZ(2))
wwwwwwwww
= = = = = = = = = = = = =F×
q2/F×n
q2 .
wwwwwwwww
22 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
The image of H1
´ et(OF [1/p]) in the cohomology of OF,q for q prime to p lands in the sub-
group H1
ur of unramiﬁed classes. This subgroup is precisely the image of H1(O/q, Z/nZ(2))
under inﬂation. The ﬁrst horizontal map on the right hand side was constructed previ-
ously, and the other two horizontal maps on the right hand side are constructed in the same
way. The reason that the χ−1-invariants do not appear on the factors F×
q2/F×n
q2 is that the
Galois group already acts by χ−1. More precisely, on the one hand, Gal( Fq2/Fq) is gener-
ated by Frobenius which acts as multiplication by q≡− 1 mod n, and on the other hand,
Gal(Fq2/Fq) = Gal(Fq(ζp)/Fq), and the character χ−1 is precisely the non-trivial character
of this group. The identiﬁcation of the two lower horizontal lines is a reﬂection of Gabber
rigidity, which implies that K3(OF,q; Zp)≃K3(Fq)⊗ Zp. □
Proposition 4.2. Let ~F denote the Galois closure of F , and suppose that ζ /∈ ~F (ζ +ζ−1).
(Equivalently, suppose thatn is prime to ~wF of Equation 28.)
(a) There is a map:
K3(F )/nK3(F )
⨁cζ,q-
⨁
F×
q2/F×n
q2
where the sum ranges over all primes q of prime norm q≡− 1 mod n which split
completely inF , or alternatively runs over all but ﬁnitely many primesq≡− 1 modn
which split completely in F .
(b) The image of this map is isomorphic to the image of the global map cζ, which is
injective if (n,w 2(F )) = 1.
(c) For ξ∈K3(F ), the set
{q⊂O F [1/S]| cζ,q(ξ) = 0}
(for any ﬁnite S) determines the image of ξ up to a scalar.
Proof. It suﬃces to consider the case when n = pm. Let ξ ∈ K3(F ), and let the class
of cζ(ξ) be represented by an S-unit ϵ. Because of the Galois action, this gives rise via
Kummer theory to a Z/nZ-extensionH ofF (ζ +ζ−1), and such that the reduction mod q ofϵ
determines the element Frobq∈ Gal(H/F (ζ +ζ−1)). (Explicitly, we haveH(ζ) =F (ζ,ϵ 1/n).)
Hence our assumptions imply that any prime q which splits completely inF (ζ +ζ−1) (which
forces q≡± 1 mod n) and is additionally congruent to −1 mod p must split in H. Let ~H
denote the Galois closure of H over Q, and ~F the Galois closure of F over Q. Note that the
Galois closure of F (ζ +ζ−1) is ~F (ζ +ζ−1). A prime q splits completely in H if and only if it
splits completely in ~H, and splits completely in F (ζ +ζ−1) if and only if it splits completely
in ~F (ζ +ζ−1). We have a diagram of ﬁelds as follows:
~H ~H(ζ)
~F (ζ +ζ−1) ~F (ζ)
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 23
By assumption, we have ζ /∈ ~F (ζ +ζ−1). Since H/F (ζ +ζ−1) is cyclic of degree n, it follows
that Gal(~H/~F (ζ +ζ−1)) is an abelian p-group. On the other hand, Gal( ~F (ζ)/~F (ζ +ζ−1)) =
Z/2Z. so Gal( ~H(ζ)/~F (ζ + ζ−1)) is the direct sum of Z/2Z with a p-group, Let σ ∈
Gal(~H(ζ)/~F (ζ +ζ−1))⊂ Gal(~H/Q) denote an element of order 2p. By the Chebotarev den-
sity theorem, there exist inﬁnitely many primes q∈ Q with Frobenius element in Gal(~H/Q)
corresponding to σ. By construction, the prime q splits completely in ~F (ζ +ζ−1) because
the corresponding Frobenius element is trivial in Gal( ~F (ζ +ζ−1)/Q). On the other hand,
since σ has order divisible by 2 and by p, it is non-trivial in both Gal( ~F (ζ)/~F (ζ +ζ−1)) =
Gal(Q(ζ)/Q(ζ + ζ−1)) and Gal( ~H/~F (ζ + ζ−1)). The ﬁrst condition implies that q ≡
−1 mod n, and the second condition implies that q does not split completely in H, a
contradiction. The injectivity (under the stated hypothesis) follows from Lemma 3.1. □
Remark 4.3. The condition thatζ /∈ ~F (ζ+ζ−1) is automatic ifp is unramiﬁed inF , because
then the ramiﬁcation degree of Q(ζ) is p− 1 whereas the ramiﬁcation degree of ~F (ζ +ζ−1)
is (p− 1)/2 for p odd. If ζ∈ ~F (ζ +ζ−1), then there are no primes q which split completely
inF and have norm−1 modn. In particular, when ζ∈ ~F (ζ +ζ−1), we haveB(Fq)⊗Fp = 0
for every prime q which splits completely in F .
