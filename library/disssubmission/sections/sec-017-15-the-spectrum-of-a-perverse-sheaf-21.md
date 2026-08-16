---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-017-15-the-spectrum-of-a-perverse-sheaf-21
section_title: "The spectrum of a perverse sheaf 21"
section_number: 1.5
pages: 29-31
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
Now forP of geometric origin the perverse sheavesNν∈ E(X) in (b)
and hence also all their simple constituentsN are of geometric origin. Each
such constituent has the formN∼= Lϕ⊗q∗(Q)[dim(A)] for suitableϕ and
some abelian subvarietyA⊆ X as in proposition 1.6(a). In this situation
the pullbacki∗(N) to A is an isotypic multiple ofi∗(Lϕ) and of geometric
origin. HenceΠ(i)(ϕ) is a torsion character. WritingS (N) = χ·K(A) we
can take forχ−1 any torsion character inΠ(i)−1(Π(i)(ϕ)). □
The above arguments can also be generalized to the relative setting of
theorem 1.3. For a homomorphismf : X→ B of abelian varieties, deﬁne
the relative spectrumSf (P) of a perverse sheafP∈ Perv(X,C) to be the
set of allχ∈ Π(X) such thatR f∗(Pχ) is not perverse. By abuse of notation,
for χ∈ Π(X) and ψ∈ Π(B) we writeχψ = χ· (Π(f )(ψ))∈ Π(X). Then
the projection formula shows
R f∗(Pχψ) = ( R f∗(Pχ))ψ,
hence Sf (P) is invariant underΠ(B). In particular, if B = X/A for an
abelian subvarietyA⊆ X, then Sf (P) is determined by its imageS f (P)
in Π(A) = Π(X)/Π(B). Furthermore, in the situation of theorem 1.3 the
assertionfor most characterscan be read inΠ(A), i.e. in the stronger sense
that S f (P) is contained in a ﬁnite union of translates of proper algebraic
subtori ofΠ(A). Indeed we have
LEMMA 1.12. Sf (P)⊆ S (P)· Π(B).
Proof. If a characterχ is not in S (P)· Π(B), then for anyψ∈ Π(B)
we haveχψ /∈ S (P) and henceHn(X,Pχψ) = Hn(B,(R f∗(Pχ))ψ)⁄= 0 for
somen⁄= 0. By theorem 1.1 thenR f∗(Pχ) is not perverse. □
CHAPTER 2
Proof of the vanishing theorem(s)
In this chapter we give an abstract Tannakian proof of theorem 1.1 based
on joint work with R. Weissauer [68]. As a geometric input we only require
the classiﬁcation of perverse sheaves with Euler characteristic zero from
section 1.4. For this classiﬁcation we have used the theory ofD-modules,
and at present we do not know whether it also holds over a ground ﬁeld
of positive characteristic. However, since this is the only reason why for
the time being the proof only applies to complex abelian varietes, in what
follows we formulate our arguments in a uniform way including also the
case ofl-adic perverse sheaves in positive characteristic.
