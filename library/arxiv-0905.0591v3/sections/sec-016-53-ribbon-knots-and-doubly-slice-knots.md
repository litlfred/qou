---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-016-53-ribbon-knots-and-doubly-slice-knots
section_title: "Ribbon knots and doubly slice knots"
section_number: 5.3
pages: 16-17
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
exists a slice disk D such that π1(NK ) →π1(D4 \νD) is surjective. Note that if a knot is
ribbon, then it is also homotopy ribbon. It is an open conject ure whether every knot that
is slice is also homotopy ribbon.
Let K ⊂S3 be a knot. Recall that there exists a non–singular hermitian pairing
λ :H1(NK ; Z[t±1]) ×H1(NK ; Z[t±1]) → Q(t)/Z[t±1]
which is referred to as the Blanchﬁeld pairing . We say that M ⊂ H1(NK ; Z[t±1]) is a
metabolizer for the Blanchﬁeld pairing if M =M ⊥, i.e. if M satisﬁes
M = {x ∈H1(NK; Z[t±1]) |λ(x,y ) = 0 ∈ Q(t)/Z[t±1] for all y ∈M }.
IfK is slice, then there exists a metabolizer for the Blanchﬁeld pairing. Also recall from the
previous section that for any k there exists a canonical isomorphism H1(NK ; Z[t±1])/(tk −
1) = H1(Lk; Z). If M is a metabolizer for the Blanchﬁeld pairing, then for any k we have
that M/(tk − 1) ⊂ H1(NK ; Z[t±1])/(tk − 1) = H1(Lk; Z) is a metabolizer for the linking
form λk. We refer to [Bl57], [Ke75], [Go78, Section 7], [Let00] and [ Fr04, Section 2.3] for
more information.
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 17
The proof of Theorem 5.2 can now be modiﬁed along well establi shed lines (cf. e.g. [Fr04,
Theorem 8.3]) to prove the following theorem:
Theorem 5.4. LetK ⊂S3 be a ribbon knot, then there exists a metabolizer M ⊂H1(NK; Z[t±1])
for the Blanchﬁeld pairing λ such that for any k and any non–trivial character χ :H1(Lk; Z) →
S1 of prime power vanishing on M/(tk − 1) we have
∆ α(k,χ)
NK
.=f (t)
f (t)
for some f (t) ∈Q(Z[ζq])[t±1] = Q(ζq)[t±1].
Using [Fr04, Proposition 4.6] one can show that if a knot K satisﬁes the ribbon obstruction
of Theorem 5.4, then it also satisﬁes the sliceness obstruct ion given by Theorem 5.3.
A knot K ⊂S3 is called doubly slice if there exists an unknotted locally ﬂat two–sphere
S ⊂ S4 such that S ∩S3 = K. Note that a doubly slice knot is in particular slice. The
ordinary Alexander polynomial does not contain enough info rmation to distinguish between
slice and doubly slice knots. On the other hand twisted Alexa nder polynomials can detect
the diﬀerence. The following theorem is well–known to the exp erts. It can be proved using
the above ideas of Kirk and Livingston combined with the resu lts of Gilmer and Livingston
[GL83] (cf. also [Fr04, Section 8.2]). Note that many of the i deas already go back to the
original paper by Sumners [Sum71].
Theorem 5.5. LetK be a doubly slice knot. Then for any prime power k there exist two
metabolizers M1 and M2 of λk with M1 ∩M2 = {0} such that for any odd prime power n
and any character χ : H1(Lk; Z) → Z/n → S1 which vanishes either on M1 or on M2 we
have
∆ α(k,χ)
NK
.=f (t)
f (t)
for some f (t) ∈Q(Z[ζn])[t±1].
It is also possible to state and prove an analogue of Theorem 5 .3 for doubly slice knots.
