---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-246-122-a-geometric-point-s-of-s-is-a-point-with-val
section_title: "A geometric point s of S is a point with value in some complete"
section_number: 1.2.2
pages: 118-121
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
algebraically closed extension (Ω ,|| ) of (K,|| ), i.e. a morphism s : M(Ω) →
S in the category of analytic spaces over K [Ber90, p.48]. For any ﬁnite
´ etale covering there are exactly n liftings s′ : M(Ω) → S′ of s, i.e. n
geometric points of S′ above S. We usually denote by s the point of S
which is the image of s.
Deﬁnition 1.2.3 (Berkovich, De Jong) . A morphism f : S′→ S is a cov-
ering (resp. ´ etale covering, resp. topological covering) ifS is covered by open
subsets U such that ∐ Vj =f−1U→U and the restriction of f to every Vj
is ﬁnite ( resp. ´ etale ﬁnite, resp. an isomorphism).
1. ´ETALE COVERINGS AND FUNDAMENTAL GROUPS. 115
There is an obvious notion of morphism between coverings of S. The cate-
gory of ´ etale coverings, resp. ﬁnite ´ etale coverings, resp. topological cover-
ings, will be denoted by Cov et
S , resp. Covalg
S , resp. Covtop
S .
There are inclusions (fully faithful embeddings)
Covalg
S֒→Covet
S, Covtop
S֒→Covet
S .
Remarks 1.2.4. (i) If S′→S is an ´ etale covering, thenS′ is a K-manifold.
(ii) It is worth noticing that the notions of ´ etale and of top ological cov-
erings are local on the base S, but not the notion of algebraic coverings
(except if S is compact).
(iii) Even if S is covered by ﬁnitely many U ’s as in the deﬁnition, it
does not follow that S′ is a disjoint union of ﬁnite algebraic coverings of S.
For instance, a Tate elliptic curve (with universal coverin g ˜S∼
= Gm) has
a covering by two open subsets U1,U 2 such that ˜S|Ui is a disjoint union of
copies of S.
(iv) It is an immediate but important fact that these categor ies are
stable under taking ﬁber product (over S). It is also stable under taking
ﬁnite disjoint unions.
(v) One should pay attention to the fact that unlike Cov top
S , Covet
S is not
stable under arbitrary disjoint unions, nor under composit ion (in the sense
that the composition of an ´ etale covering S′/S and an ´ etale coveringS′′/S′
may not be an ´ etale covering S′′/S). However, we have:
Lemma 1.2.5. Any morphism which is the composition of a covering (resp.
´ etale covering) followed or preceded by a ﬁnite (resp. ﬁnit e ´ etale) morphism
is a covering (resp. ´ etale covering).
Proof. Let us consider the case of a covering g : S′′ → S′ followed by
a ﬁnite covering f : S′→ S (the reverse situation is immediate from the
deﬁnition). Let s be a point of S. Then for any s′ in the ﬁnite set f−1(s),
there exists an open neighborhood Us′ ⊂ S′ of s′ such that g−1(Us′) is a
disjoint union of spaces Us′,i, each being ﬁnite over Us′ via g. We may
assume that the Us′ are pairwise disjoint. Since f is ﬁnite, it is in particular
a closed continuous map, hence S′ admits a basis of open neighborhoods of
f−1(¯s) of the form f−1(V ). In particular, there is an open neighborhood Vs
of s such that
∐
s′∈f −1(s)
Us′ contains f−1(Vs). We may replace each Us′ by
its intersection with f−1(Vs) (which is a union of connected components of
f−1(Vs)). It is then clear that g◦f induces a ﬁnite morphism from Us′,i to
Vs. Hence g◦f is a covering. The ´ etale variant is similar.
Examples 1.2.6. (i) The prototype of an ´ etale covering is given by the log-
arithm map
log : DCp(1, 1−)−→ (A1
Cp)an.
116 III. p-ADIC ORBIFOLDS AND MONODROMY.
For any m∈ N, the inverse image of the open disk
Dm = D
(
0,
(
|p|−m+ 1
p−1
)−)
⊂ (A1
Cp)an
is a disjoint union
∐
ζ∈µp∞
{
q∈ D(1, 1−)
⏐
⏐
⏐ζq pm
∈ D
(
1,
(
|p|
1
p−1
)−)}
and each of these components is isomorphic to Dm ifm = 0, and ﬁnite ´ etale
onto Dm in general (we are using here the factorization q↦→ζq pm
= t↦→
logt↦→p−m logt = logq of the logarithm).
(ii) This example may be interpreted as a Dwork period mappin g (II.6.3.1).
In fact, all examples of period mappings considered in II.6. 3 are ´ etale cov-
erings of the period domain D. For instance, the Gross-Hopkins period
mapping (II.6.3.2) is an ´ etale covering of ( P1
Cp)an, cf. [dJ95b, 7.2].
Any period mapping is ´ etale, but it may happen in some cases t hat it is
surjective without being an ´ etale covering, cf. [RZ96, 5.41] (this some-
what mysterious phenomenon is due to the existence of biject ive non-quasi-
compact ´ etale morphisms).
(iii) Any (possibly inﬁnite) topological covering of a ﬁnit e ´ etale covering
is an ´ etale covering after 1.2.5.
The following two lemmas are due to V. Berkovich and J. De Jong (and
not stated in the most general form).
Lemma 1.2.7. (i) An ´ etale presheafF on S which is representable by
an ´ etale coveringS′ is a sheaf. For any subdomain U ⊂ S,F|U is
representable by S′×SU .
(ii) LetF be an ´ etale sheaf. LetUi an open covering of S. If for every i,
F|Ui is representable by an ´ etale covering, so is F.
For (i), cf. [Ber93, 4.1.3, 4.1.4, 4.1.5]. Here we take advantage of
working with strict analytic spaces. Gluing — using [ Ber93, 1.3.3] — gives
(ii) ( cf. also [ dJ95b, 2.3]).
Lemma 1.2.8. LetS′→S be an ´ etale covering, and let R⊂S′×SS′ be a
union of connected components which is an equivalence relat ion on S′ over
S. Then S′/R (viewed as an ´ etale sheaf on S) is representable by an ´ etale
coveringS′′→S.
cf. [dJ95b, 2.4]: by the previous lemma, the question is local on S; the
proof is by reduction to the case of a ﬁnite ´ etale covering of aﬃnoid spaces.
In the situation of 1.2.8, we say that the S′′ → S is a quotient ´ etale
covering of S′→S.
1. ´ETALE COVERINGS AND FUNDAMENTAL GROUPS. 117
1.3. Existence of ´ etale paths.
