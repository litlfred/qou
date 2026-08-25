---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-033-26-perverse-multiplier-37
section_title: "Perverse multiplier 37"
section_number: 2.6
pages: 45-46
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
By assumptionP is an N-multiplier, hencePm∈ N for all m⁄= 0. Via the
twisting axiom (N2) it follows that for most charactersχ and alln∈ Z,
Hn(X,P∗(g+1)
χ ) = Hn(X,(P0)χ).
The right hand side vanishes for|n| > g sincerat(P0)χ is perverse. But for
the left hand side we have
H•(X,P∗(g+1)
χ ) = ( H•(X,Pχ))⊗(g+1)
by proposition 2.1 and sinceH•(X,−) is a tensor functor by the K¨unneth
theorem. So the above vanishing statement for|n| >g implies thatH•(X,Pχ)
is concentrated in degree zero.
(b) Put Q = (P⊕P∨)∗r for any r∈ N. Since hypercohomology is a
tensor functor by the K¨unneth theorem, withH•(X,Pχ) also H•(X,Q) is
concentrated in degree zero. Using the hard Lefschetz axiom (D5), one
then deduces that for alln⁄= 0 one hasH•(X, pHn(Q)) =0 so that by (N3)
the subcategoryN containspHn(Q). Since this holds for arbitraryr∈ N, it
follows thatP is anN-multiplier. □
In view of part(a) of the lemma, to prove theorem 1.1 we want to show
that for a suitable subcategoryN every object ofP is an N-multiplier. For
this we will argue by contradiction, using the following
LEMMA 2.12. Suppose thatN satisﬁes the stability axiom (N1) and the
Euler axiom (N4), thatD satisﬁes all axioms (D1) – (D5) and that P∈ P is
not anN-multiplier. Then for some r∈ N the convolution power
(P∗P∨)∗r = (P∗P∨)∗···∗ (P∗P∨)
admits a direct summand of the form1[2i](i) with an integer i⁄= 0.
Proof. If P is not an N-multiplier, we can ﬁnd integersa,b∈ N such
that P∗a∗ (P∨)∗b admits a direct summandQ[i] for somei⁄= 0 and some
simple objectQ∈ P which is not inN. By the hard Lefschetz axiom (D5)
thenQ[−i](−i) is a direct summand ofP∗a∗(P∨)∗b as well. It then follows
that also the dualQ∨[i](i) is a direct summand ofP∗b∗(P∨)∗a. Altogether
then the convolution productQ[i]∗Q∨[i](i) = Q∗Q∨[2i](i) will be a direct
summand of(P∗P∨)∗r for the exponentr = a+b.
It remains to show that1 is a direct summand ofQ∗Q∨. For this note
that the trace maptr(Q) : 1−→Q∗Q∨∼= Q∨∗Q−→1 is non-zero since
we haveχ(Q)⁄= 0 by axiom (N4). Nowtr(Q) factors overpH0(Q∗Q∨),
indeedHomD(P, pτ>0P) = HomD(pτ<0P,P) = 0. So tr(Q) exhibits1 as a
retract ofpH0(Q∗Q∨) in the abelian categoryP, and we are done. □
38 Chapter 2 – Proof of the vanishing theorem(s)
