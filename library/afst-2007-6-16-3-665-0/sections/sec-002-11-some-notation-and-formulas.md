---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-002-11-some-notation-and-formulas
section_title: "Some notation and formulas"
section_number: 1.1
pages: 4-5
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
A diﬀerence ring is a commutative R with a given automorphism φ.
The skew ring of diﬀerence operators R[Φ, Φ−1], consists of the ﬁnite for-
mal sums 
n∈Z anΦn with all an ∈R. The multiplication is deﬁned by
Φr = φ(r)Φ. A diﬀerence module M is a left R[Φ, Φ−1]-module which is
free and ﬁnitely generated as R-module. The action ΦM of Φ on M is an
additive bijection satisfying ΦM(rm) = φ(r)ΦM(m). Thus we may describe
a diﬀerence module as a pair (M, F), with F an additive bijective map and
such that F(fm) = φ(m)F(m) holds.
As before we choose q ∈C with 0 < |q| < 1. Further we ﬁx τ in
the complex upper half plane with e2πiτ = q. The ﬁelds K = C({z}) and
K = C((z)) are made into diﬀerence ﬁelds by the automorphisms φ given
by φ(z) = qz. These automorphisms are extended to the ﬁnite extensions
Kn and Kn of degrees n and to the algebraic closures K∞and K∞of K
and K, by φ(zλ) = qλzλ where qλ := e2πiτλ for all λ ∈Q.
The formula φ(zλ) = qλzλ makes C[z, z−1] into a diﬀerence ring. A
diﬀerence module over this ring will be called a global diﬀerence module. As
we will prove later on, any diﬀerence module M over K is obtained from
a unique global module Mglobal as a tensor product, i.e., M ∼= K ⊗C[z,z−1]
Mglobal.
Other diﬀerence rings that we will use are C[z1/n, z−1/n] and O = O(C∗),
the ring of the holomorphic functions on C∗.
Closely related to q-diﬀerence equations is the complex Tate curve Eq :=
C∗/qZ. We write pr : C∗→Eq for the natural map. Theta functions are re-
lated to both Eq and q-diﬀerence equations. Put Θ := 
n∈Z qn(n−1)/2(−z)n.
Then
Θ = d

n>0
(1 −qnz−1) ·

n⩾0
(1 −qnz) for some constant d̸ = 0.
The divisor of Θ on C∗is 
n∈Z[qn]. Further −zΘ(qz) = Θ(z) or −zφ(Θ) =
Θ. The latter implies dz
z + φ( dΘ
Θ ) = dΘ
Θ . Moreover, the poles of dΘ
Θ form the
set qZ. Each pole is simple and has residue 1.
For c ∈C∗one deﬁnes θc :=
Θ(cz)
Θ(z) . This function has the property:
c · θc(qz) = θc(z). Moreover, the diﬀerential form ωc := dθc
θc is φ-invariant
– 667 –
Marius van der Put, Marc Reversat
and deﬁnes a diﬀerential form on Eq. If c̸ ∈qZ, then ωc has simple poles in
pr(c−1) and 1 = pr(1) with residues 1 and −1. Further ωqc = ωc −dz
z .
