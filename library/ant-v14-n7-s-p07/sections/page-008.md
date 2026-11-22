---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
1902
Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
We begin by computing the main term:
Tr(Frobq | H2n
c,ét((Xa
n)Fq; Qλ) = qn.
This follows immediately from the fact that (Xa
n)Fq ∼= (Xn)Fq is irreducible. When n is odd, this is shown
in the proof of [Ellenberg et al. 2016, Theorem 8.8] as a consequence of a big monodromy theorem
of J.K. Yu. (This is actually the only place where we need n to be large, and indeed n = 3 would be
enough.) When n is even, we argue as follows. The map from Xn to the conﬁguration space Confn A1
sending a G-cover to its branch locus is a ﬁnite cover [loc. cit., Section 2.2], and irreducibility of Xn is
equivalent to the monodromy group of this cover acting transitively on the ﬁber. It sufﬁces to check that
this holds on a closed subvariety of the base. So write Z for the subvariety of Confn A1 consisting of
those conﬁgurations containing some speciﬁed point p0 ∈P1(Fq), and let Y be the preimage of Z in Xn.
An automorphism of P1 taking p0 to ∞now identiﬁes Y with Hnc
G,n−1, which we know to be irreducible
since n −1 is odd. This implies that Xn is irreducible.
We now turn to the error term. The moduli space Xn is a closed and open subscheme of Hnc
G,n, so its
Betti numbers are bounded by those of Hnc
G,n; by [loc. cit., (7.8.1)] we have
dim H2n−i
c,ét ((Xa
n)Fq; Qλ) ≤Kℓ(Bℓ)i
where Kℓ, Bℓare constants depending only on ℓ.
Using the Deligne bound [1980], the eigenvalue of Frobenius on Hi
c,ét((Xa
n)Fq; Qλ) is bounded in
absolute value by qi/2; so the absolute value of the contribution of all i < 2n to (2.5) is bounded above by
the sum of a geometric series which converges for all q > B2
ℓ. In particular, as in [Ellenberg et al. 2016,
Section 1.8], this contribution is at most
KℓBℓq−1/2(1 −Bℓq−1/2)−1qn.
So if we take Qℓ= 4B2
ℓand q > Qℓ, we may take Cℓ= 2KℓBℓand conclude
|Xa
n(Fq) −qn| =

2n−1
X
i=0
(−1)i Tr(Frobq | Hi
c,ét((Xa
n)Fq; Qλ)
 < Cℓqn−1/2
which proves (2.4) and thus the desired result.
□
Proposition 2.1 allows us to bound the proportion of hyperelliptic curves whose étale cohomology has
a Frobenius eigenvalue congruent to a mod ℓ. Recall from Section 2A that Qa,ℓ
n,q is the set of squarefree
polynomials over Fq of degree n such that ma( f ) is greater than 0.
Corollary 2.6. There are constants C′
ℓ, Qℓ, Nℓsuch that for any a ∈(Z/ℓZ)× we have
|Qa,ℓ
n,q|
|Qn,q| ≤
1
ℓ−1 + C′
ℓq−1/2
for all n ≥Nℓ, q ≥Qℓ.
