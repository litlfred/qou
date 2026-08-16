---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-046-35-nearby-cycles-57
section_title: "Nearby cycles 57"
section_number: 3.5
pages: 65-66
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
cycles functorΨ then sends the Serre subcategoryS(Xη)⊂ P(Xη) into the
Serre subcategoryS(Xs)⊂ P(Xs) and hence induces a functor
Ψ : P(Xη)−→P(Xs)
between the quotient categories. The property(i) of Ψ is inherited from the
corresponding estimate forΨ shown above.
Secondly we takef = m to be the group law, withY = X×k X, Z = X
andL = P⊠Q. In D(Xs) we can identifyΨZ(R f∗(L)) withΨ(P∗Q). Since
by [60, th. 4.7] the exterior tensor product⊠ commutes with nearby cycles,
we can also identifyR f∗(ΨY(L)) withΨ(P)∗Ψ(Q). Then the factorization
of β from above shows that the nearby cyclesΨ(P∗Q) admitΨ(P)∗Ψ(Q)
as a direct summand inP(Xs). Hence(ii) follows. □
In general we cannot expectΨ to be a tensor functor since it does not
preserve the Euler characteristic (see example 3.12). In what follows we
will call a perverse sheafP on Xη admissible if
χ(Ψ(P)) = χ(P).
Note that for an abelian schemeX→ S every perverse sheaf is admissible
since the nearby cycles are compatible with proper morphisms.
LEMMA 3.14. The admissible objects form a rigid symmetric monoidal
full abelian subcategory
P(Xη)ad⊂ P(Xη)
which is stable under the formation of extensions and subquotients.
Proof. Any short exact sequence 0→ P1→ P2→ P3→ 0 in P(Xη) is
mapped under the nearby cycles functor to a short exact sequence in the
categoryP(Xs). Then in particular
χ(P2) = χ(P1) +χ(P3) and χ(Ψ(P2)) = χ(Ψ(P1)) +χ(Ψ(P3))
because the Euler characteristic is additive in short exact sequences. But on
the other handχ(Pi)≥ χ(Ψ(Pi)) for i = 1,2,3 by lemma 3.13(i). Hence it
follows that
χ(Pi) = χ(Ψ(Pi)) holds fori = 2 iff it holds fori = 1 andi = 3.
In other words, the perverse sheafP2 is admissible if and only if bothP1
andP3 are admissible. So the category of admissible objects is stable under
the formation of extensions and subquotients.
58 Chapter 3 – Perverse sheaves on semiabelian varieties
It remains to show that for admissibleP1,P2∈ P(Xη) also P1∗ P2 is
admissible. This follows from
χ(P1∗P2) = χ(P1)· χ(P2) (part(d) of lemma 3)
= χ(Ψ(P1))· χ(Ψ(P2)) (admissibility ofP1, P2)
= χ(Ψ(P1)∗Ψ(P2)) (part(d) of lemma 3)
≤ χ(Ψ(P1∗P2)) (part(ii) of lemma 12)
≤ χ(P1∗P2) (part(i) of lemma 12)
which implies that the last two estimates must in fact be equalities.□
Concerning the failure of tensor functoriality it now follows that the
situation is as good as one could possibly hope for.
THEOREM 3.15. On the rigid symmetric monoidal abelian subcategory
of admissible objects, the nearby cycles deﬁne a tensor functor ACU
Ψ : P(Xη)ad−→P(Xs)
so that for P∈ Pad
η we obtain a closed immersion G(Ψ(P)) ↪→G(P).
Proof.LetP1,P2∈ P(Xη)ad. The last statement in lemma 3.13(ii)gives
a split monomorphism
Ψ(P1)∗Ψ(P2) ↪→ Ψ(P1∗P2)
in the abelian categoryP(Xs). But χ(Ψ(P1)∗Ψ(P2)) =χ(Ψ(P1∗P2)) as we
have seen in the proof of lemma 3.14. So the above monomorphism is an
isomorphism inP(Xs), and henceΨ is a tensor functor onP(Xη)ad. For the
statement about the Tannaka groups, recall that by deﬁnition every object
of⟨Ψ(P)⟩ is a subquotient of the image underΨ of some object in⟨P⟩. So
our claim follows from the Tannakian formalism [33, prop. 2.21b)]. □
