---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-020-36-haar-integrals
section_title: "Haar integrals"
section_number: 3.6
pages: 29-31
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Since ﬁnite dimensional weak Hopf algebras do not go beyond t he ”compact” and ”discrete”
case, the following very conservative deﬁnition of Haar mea sure will suﬃce.
Deﬁnition 3.24 An element h of a WHA A is called a Haar integral in A or Haar measure
on ˆA if h is a normalized 2-sided integral, i.e. h ∈ I (A) and ⊓L(h) = ⊓R(h) = 1 .
Obviously, if Haar integral exists then it is a unique S-invariant idempotent. As a matter of
fact let h and h′ be Haar integrals. Then h′ = ⊓L(h)h′ = hh′ = h ⊓R (h′) = h. In particular
h2 =h. S-invariance follows from uniqueness since S(h) is a always a Haar integral if h is.
In ﬁnding criteria for the existence of Haar measure in A an important role will be played
by a special element χ ∈ ˆA the deﬁnition of which was inspired by similar computations in
Hopf algebra theory [21]:
χ :=
∑
i
βi↼S −2(bi) ≡ ˆL′(ˆ1), (3.63)
where {bi} and {βi} are dual bases of A and ˆA, respectively, and ˆL′: ˆA → ˆA is given by
ˆL′(ψ) := ∑
iβiψ ↼S−2(bi) . Note that ˆL′ is the ”cop” version of the dual analogue ˆL of
the projection (3.23) onto the space of left integrals. Henc e χ is a left integral in ( ˆA)cop and
therefore in ˆA.
As we will see below if χ is non-degenerate and a q-trace then its dual left integral w ill
automatically be the Haar measure. In order to see that it is a q-trace let Tr A be the standard
trace on End KA and introduce the notation Q−(x)y :=yx. Then for x ∈A we have
χ(x) =
∑
i
⟨βi,S −2(bi)x⟩= TrA Q−(x) ◦S−2
χ(xy) = Tr A Q−(y) ◦Q−(x) ◦S−2 = TrA Q−(y) ◦S−2 ◦Q−(S2(x)) =
= χ(yS 2(x)).
The next Lemma will be crucial in deciding whether χ is non-degenerate.
Lemma 3.25 Let l be a left integral in a WHA A and let χ ∈ ˆA be the q-trace left integral
deﬁned in Eq(3.63). Then
l⇀χ = ˆS2(ˆ1↼l ) . (3.64)
Proof: Using the q-trace property of χ and then (2.19a)
l⇀χ =
∑
i
βi↼S −2(bil) = ( ˆ1↼ 1(1))↼S −2(1(2)l) =
= ⟨ˆ1(1),S −1(1(2))1(1)⟩ˆ1(2)↼S −2(l) = ˆ1↼S −2(l) = ˆS2(ˆ1↼l )
Q.e.d.
Proposition 3.26 LetA be a weak Hopf algebra over a ﬁeld K and let χ be given by (3.63).
29
i) The Haar integral h ∈A exists if and only if χ is non-degenerate, in which case (h,χ ) is a
dual pair of left integrals. In particular Haar integrals ar e non-degenerate.
ii) A left integral l ∈ IL(A) is a Haar integral if and only if ⊓R(l) = 1 .
The characterization of Haar measures under (ii) is so simpl e that it could be well used as a
deﬁnition of Haar measure. Notice that in that case the forma l diﬀerence between the notions
of normalized left integral and Haar measure were so tiny (ch ange ⊓L for ⊓R) that it would
smear out the big conceptual diﬀerence: The existence of nor malized left integrals is equivalent
to semisimplicity while the existence of Haar measures is mu ch stronger.
Proof: ii) Assumel ∈ IL(A) satisﬁes ⊓R(l) = 1. Then by Lemma 3.25 l⇀χ = ˆ1. Therefore
the duality Theorem (Thm 3.18) implies that (l,χ ) is a dual pair of non-degenerate left integrals.
Since χ is a q-trace, Lemma 3.20 shows that l is an S invariant non-degenerate left integral.
Furthermore ⊓L(l) = ⊓L(S(l)) = S ◦ ⊓R(l) = 1. Thus l is a Haar integral. Now assume h is a
Haar integral. Then obviously h is a left integral satisfying ⊓R(h) = 1.
i) The ”only if” part follows from the proof of (ii). Assume χ is non-degenerate and let h
be its dual left integral. Then by Lemma 3.20 h is 2-sided and by Lemma 3.25 it is normalized.
Q.e.d.
However simple, the criteria of the above Proposition are ve ry diﬃcult to verify in concrete
situations. So it is worth looking for other criteria even if they are not applicable in full
generality.
Theorem 3.27 Let A be a WHA over an algebraically closed ﬁeld K. Then a necessary and
suﬃcient condition for the existence of Haar measure h ∈A is that A is semisimple and there
exists a g ∈ A× such that gxg−1 = S2(x) for x ∈ A and tr Dr(g−1) ⁄= 0 for all irreducible
representationDr of A .
The assumption on K is used only to ensure that A is split semisimple, A = ⊕rMnr (K), once
knowing that it is semisimple. In particular there will be a K-basis {eαβ
r } forA obeying matrix
unit relations.
Proof: Suﬃciency : Let τ :A →K be the trace with trace vector τr = trDr(g−1). Then τ
is non-degenerate and has as quasibasis the element
∑
i
xi ⊗yi :=
∑
r
1
τr
nr∑
α,β=1
eαβ
r ⊗eβα
r .
Notice that ∑
ixig−1yi = 1. Now we deﬁne χ′ :=g⇀τ and claim that χ′ coincides with the χ
of Eq(3.63). As a matter of fact
χ′(x) = τ (gx) =
∑
i
τ (xig−1yigx) =
∑
τ (xiS−2(yi)x) =
=
∑
i
⟨βi,S −2(bi)x⟩=χ(x)
where we used the fact that the dual of the basis bi = yi is βi = τ ↼xi. Since χ′ was non-
degenerate by construction, we conclude that theχ of Eq(3.63) is non-degenerate and therefore
its dual left integral l has ⊓R(l) = 1 by Eq(3.64). Therefore l is a Haar measure.
Necessity: If h ∈ A is a Haar measure then A is semisimple by Theorem 3.13. Therefore
A is a symmetric algebra and θA = id . This means that θψ is inner for all non-degenerate
30
functional ψ. In particular θχ = S2 is inner where χ is the dual left integral of h. Choose a
g ∈A× implementingS2 and construct the non-degenerate trace τ :=g−1⇀χ .
τ (x) = χ(xg−1) = TrA Q−(xg−1) ◦S−2 = TrA Q+(g−1) ◦Q−(x)
where Q+(x)y :=xy is left multiplication on A. Choosing a matrix unit basis to evaluate the
trace we obtain
τ (x) =
∑
r
trDr(g−1) trDr(x)
and by non-degeneracy of τ all components tr Dr(g−1) of the trace vector are non-vanishing.
Q.e.d.
