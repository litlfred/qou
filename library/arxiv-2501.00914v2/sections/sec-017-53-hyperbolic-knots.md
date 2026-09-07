---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-017-53-hyperbolic-knots
section_title: "Hyperbolic knots"
section_number: 5.3
pages: 27-28
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
some surgery in common with a torus knot.
Proposition 5.6.IfS 3
0(K)∼=S3
0(Tp,q)butKis not isotopic toT p,q, thenKis a fibered hyperbolic
knot, and its monodromy is not veering. In particular, neitherKnor its mirror is an L-space knot.
Proof.Since 0-surgery detects whether a knot is fibered [Gab87], andT p,q is fibered, we know that
Kmust be fibered as well. Now ifKis not hyperbolic then it is either a torus knot or a satellite
knot [Thu82, Corollary 2.5].
IfKis a torus knot other thanT p,q, then Lemma 2.11 says thatS 3
0(K)̸∼=S3
0(Tp,q). Similarly, if
Kis a satellite knot, then we cannot haveS 3
0(K)∼=S3
0(Tp,q). Assuming otherwise, Lemma 5.3 says
that the companion torus ofK=P(C) is incompressible inS 3
0(K), so thenS 3
0(Tp,q) must also be
toroidal, whenceS 3
0(K)∼=S3
0(T±2,3) by Lemma 5.4. But thenKmust be a genus-1 fibered knot,
since it has the same 0-surgery as another genus-1 fibered knot [Gab87], and we have a contradiction
because the only genus-1 fibered knots are not satellites.
The only remaining possibility ifK̸=T p,q is that it must be a fibered hyperbolic knot. In this
case, sinceS 3
0(K)∼=S3
0(Tp,q) is small Seifert fibered, Corollary 2.5 tells us that the monodromyh
ofKcannot be veering, as claimed. Moreover, ifKwere an L-space knot thenhwould have to be
veering by Lemma 2.7, soKcannot be an L-space knot. Similarly, if the mirror Kwere an L-space
knot then its monodromyh −1 would be veering, and thenhwould be veering, so Kcannot be an
L-space knot either. □
Proposition 5.6 has the following consequence, for which we recall that L-space knots have right-
veering monodromy.
Proposition 5.7.LetT p,q be a torus knot, and suppose there is some rationalr∈Qand some
fibered hyperbolic knotK⊂S 3 with right-veering monodromy such thatS 3
r (K)∼= S3
r (Tp,q). Then
0<r≤4g(K), and ifKis additionally an L-space knot thenr̸= 4g(K).
Proof.Writeg=g(K) for convenience. We know thatS 3
r (Tp,q) is always either reducible, a lens
space, or small Seifert fibered [Mos71], soS 3
r (K) is not hyperbolic. SinceKis fibered and hyperbolic
with right-veering monodromy, Ni [Ni20, Theorem 1.1] proved that 0≤r≤4g, and thatS 3
4g(K)
is not a small Seifert fibered L-space. Now Proposition 5.6 says thatKcannot have right-veering
monodromy ifS 3
0(K)∼=S3
0(Tp,q), so we must haver̸= 0 as well.
In the caser= 4g, we observe thatS 3
4g(K) is neither reducible nor a lens space. Indeed, if
we assume otherwise then its universal cover is not contractible, so it does not admit an essential
lamination [GO89, Theorem 6.1]. On the other hand, the monodromy ofKis pseudo-Anosov,
and the suspension of its stable lamination has some degeneracy sloped, which satisfies either
|d|≤4g−2 ord= n
0 for some integern≥1 [Gab97, Theorem 8.8]. Now by [GO89, Theorem 5.3]
this suspension gives rise to an essential lamination onS 3
4g(K) as long as ∆(d,4g)≥2, so we must
have ∆(d,4g)≤1, henced= 1
0. On the other hand, sinceKhas right-veering monodromyh, we
know that the fractional Dehn twist coefficientc(h) = 1
d is strictly positive [HKM07, Proposition 3.1]
and this is a contradiction.
ThusS 3
4g(K)∼= S3
4g(Tp,q) implies thatS 3
4g(K) can only be small Seifert fibered. IfKwere an
L-space knot, then all surgeries onKof slope at least 2g−1 would be L-spaces; but thenS 3
4g(K)
would be a small Seifert fibered L-space, contradicting [Ni20] as mentioned above, soKcannot be
an L-space knot after all.□
28 JOHN A. BALDWIN AND STEVEN SIVEK
Proposition 5.7 was the last remaining step in the proof of Theorem 5.1, so the latter proof is
now complete. □
6.Positive traces andT 2,2g+1 torus knots
As a special case of Theorem 1.2, we know that all torus knots are characterized by their 0-
traces, but the proof makes essential use of the fact thatS 3
0(Tp,q) is a fibered 3-manifold. Similarly,
Theorem 1.5 tells us that positive torus knots are characterized by any of their negative traces, but
reveals very little about their positive traces. However, in some cases we can say a bit more about
these positive traces. In this section we will prove Theorem 1.6, which we restate here:
Theorem 6.1.Suppose for some knotKand positive integersnandgthatX n(K)∼=Xn(T2,2g+1).
Then eitherK=T 2,2g+1,or1≤n≤4g−1andKis a hyperbolic knot such that
[HFK(K)∼= [HFK(T 2,2g+1)
as bigraded vector spaces.
