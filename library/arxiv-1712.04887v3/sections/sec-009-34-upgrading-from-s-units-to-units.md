---
doc_id: arxiv-1712.04887v3
doc_title: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture"
section_id: sec-009-34-upgrading-from-s-units-to-units
section_title: "Upgrading from S-units to units"
section_number: 3.4
pages: 20-20
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F"
---
Lemma 3.4.
Lemma 3.5. Suppose that any prime divisor p ofn is odd and divides neither the discrimi-
nant ofF nor the order ofK2(OF ). Then the image of cζ onK3(F )/nK3(F ) may be realized
by an element ofO×
n .
Proof. By Lemma 2.8, it suﬃces to consider the case when n is a power of p. Let ζ = ζn.
The fact that p is prime to the discriminant of F implies that F (ζ)/F is totally ramiﬁed
at p. The image of cζ factors through H1
´ et(O[1/p], Z/nZ(2)), and, via inﬂation–restriction,
throughH1
´ et(OF (ζ)[1/p], Z/nZ(1)). The Kummer sequence for ´ etale cohomology gives a short
exact sequence:
OF (ζ)[1/p]×/OF (ζ)[1/p]×n→H1
´ et(OF (ζ)[1/p], Z/n(1))→ Pic(OF (ζ)[1/p])[n].
The image of cζ lands in the χ−1-invariant part of the second group. The χ−1-invariant
partMχ−1
of aG-moduleM is non-zero if and only if the largestχ−1-invariant quotientMχ−1
is non-zero. However, by results of Keune [18], there is an injection
(Pic(OF (ζ)[1/p])/pm)χ−1→K2(OF )/pm.
In particular, the pushforward of the image of cζ to the Picard group is trivial when-
everK2(OF )⊗Zp is trivial. Since we are assuming thatp does not divide the order ofK2(OF ),
we deduce that the image of cζ is realized by p-units. We now upgrade this to actual units.
There is an exact sequence:
(OF (ζ))×/(OF (ζ))×n→ (OF (ζ)[1/p])×/(OF (ζ)[1/p])×n→
⨁
v|p
Z/nZ,
where the last map is the valuation map. Since p is totally ramiﬁed in F (ζ)/F , the action
of G on the ﬁnal term is trivial. By assumption, the quotient Gal( F (ζp)/F ) is non-trivial,
and hence the χ−1-invariants of the ﬁnal term are zero. Hence, after taking χ−1-invariants,
we see that the image of cζ comes from a unit. □
