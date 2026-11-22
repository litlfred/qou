---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-024-52-positive-links
section_title: "Positive links"
section_number: 5.2
pages: 35-38
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Positive links
35
The only common extension of the two MWF = 3 extensions is
[122331221123321], which has MWF = 4.
So it remains to verify that (the closures of) [22∗3∗122∗11∗23211∗]and [22∗3122∗11∗23∗211∗] have braid index
4.
For this we use the two-cabled MWF inequality. Let for a braid β ∈Bn, the “two-cabled” braid (β)2 ∈B2n be obtained
from β by replacing in (9) each σi by σ2iσ2i−1σ2i+1σ2i. Then (β)2 is a braid representation of the (blackboard framed)
two-cable link L2 of the closure L = ˆβ of β. We consider now for β the above braid β0.
We know, from the computations described in [MS, FW], that MWF((139465)2) = 7. This is in fact true also for
the connected cable (the one with braid representation (β0)2 · σ1). Now we claim that reducing or resolving a clasp
(changing a σ2
i into a σi or deleting it) does not reduce the two-cabled MWF bound. The 2-cable of a clasp can
be resolved by resolving 4 clasps. The 2-cable of a crossing in a 2-cabled clasp can be resolved by resolving one
clasp and changing twice σ2
i →σi. Finally, the 2-cable of an isolated σi can be reduced into two internal twists of
the doubled original strand. Such twists can be collected for every doubled component, resolved for each doubled
component to one, and joined if doubled components are joined by reducing a doubled crossing in a doubled clasp.
So the two-cabled MWF reduces to the one of the connected cable of 139465 and we are done.
The proof of theorem 5.1 is now completed.
5.2.
Positive links
In this section, we will reﬁne the arguments proving theorem 1.1 to restrict the possible 3-braid representations of pos-
itive links. Our positivity considerations will make use of the criterion of Yokota [Yo], and the Kauffman polynomial
F. We recall the properties (6) – (8) that determine F and its writhe-unnormalized version Λ.
Note that for P one can similarly deﬁne a regular isotopy invariant
˜P(D)(a,z) = (ia)−w(D)P(D)(ia,iz),
(37)
with i = √−1. Then ˜P satisﬁes similar relations to (6) – (8). The difference to Λ is that ˜P is deﬁned on oriented link
diagrams, and that the term making orientation incompatible on the right of (6) is missing.
Theorem 5.4 (Yokota [Yo]) If L is a positive link, then
mindega F(L) = mindegv P(L) = 1 −χ(L),
and
[F(L)]a1−χ(L) = [P(L)(ia,iz)]a1−χ(L) .
We also require an extension of braids to the context of F. This was described in [BW] and [Mr], but we use only
the generators of the algebra deﬁned there. Strings will be assumed numbered from left to right and words will be
composed from bottom to top. We write σi for a braid generator, where strand i from the lower left corner, passing
over strand i+1, goes to the upper right corner.
We add elements δi of the following form:
i i+1
.
By hat we denote the usual closure operation.
A word in the described generators gives rise to an unoriented tangle diagram that turns into an unoriented link diagram
under closure. If the word has no δi then this diagram can be oriented to give a(n oriented) closed braid diagram. We
will assume this orientation is chosen. Otherwise, a coherent orientation is not generally possible. In particular, the
sign of exponents of σi in this context may not coincide with the sign of the corresponding crossings after some (or
even any) orientation choice of the diagram. For kinks (the diagram fragments occurring in (7) on the left hand-sides),
however, a sign is deﬁnable since any possible component orientation chosen gives rise to the same (skein) sign. So
we will be able (and we will need) to distinguish between positive (in the left equation of (7)) and negative kinks (in
the right one).
36
5
Positivity of 3-braid links
Lemma 5.6 Let
D = b

σ
k1,1
1
σ
k1,2
2
...σ
k1,n1
1
σ−1
2
σ
k2,1
1
...σ
k2,n2
1
σ−1
2
...
σ
kl,1
l
...σ
kl,nl
1
δ2

(38)
where ni ≥1 odd and ki,j ≥2 when 1 < j < ni and ki,j ≥1 when j = 1 or ni. Then mindega Λ(D) = −l.
Proof. For l = 1 see lemma 5.9 below. Then use induction on l. Change a crossing of a σ−1
2
in D = D−. Then:
D+ can be reduced by the same argument as in the proof of lemma 5.2 of [St4] until we have a form (38) with smaller
l, and a non-zero number of negative kinks added. Then since negative kinks shift the a-degree of Λ up, we have
mindega Λ(D+) > −l.
D0 has mindega Λ(D0) = 1 −l > −l by induction.
D∞= Dl1#Dl2 with l1 +l2 = l, so mindega Λ(D∞) = −l1 −l2 = −l, and mindega Λ(D) is inherited from Λ(D∞).
✷
Lemma 5.7 Let
D = b

σ
k1,1
1
σ
k1,2
2
...σ
k1,n1
1
σ−1
2
σ
k2,1
1
...σ
k2,n2
1
σ−1
2
...
σ
kl,1
l
...σ
kl,nl
1
σ−1
2

(39)
where ni ≥1 odd and ki,j ≥2 when 1 < j < ni and ki,j ≥1 when j = 1 or ni. Then mindega Λ(D) ≥−2 when l ≤2
and mindega Λ(D) = −l when l ≥3.
Proof. Assume ﬁrst we proved the result for l ≤2, and that l > 2. We argue by induction on l.
Apply the Λ-relation at a σ−1
2
crossing in D = D−. Then D0 has mindega Λ = 1 −l by induction. D+ simpliﬁes
as in the proof of lemma 5.2 of [St4]. This simpliﬁcation only removes negative letters. It can be iterated until
one of two situations occurs. It can (a) happen that all negative letters disappear. Then we have a positive braid
and mindega Λ = −2 > −l by Yokota’s result. Or it can (b) occur that no σ1σ2σ1 or σ2σ1σ2 occur as subwords.
Then ki,j ≥2 for 1 < j < ni, and the number l of negative crossings has decreased strictly. So we have by induction
mindega Λ(D+) > −l. Finally we must deal with the D∞term. This follows from lemma 5.6.
It remains to justify the claim mindega Λ(D) ≥−2 when l ≤2. This is done exactly with the same argument, only
that now we observe that all of Λ(D0,+,∞) have a-degree ≥−2.
✷
Lemma 5.8 The closed braids in (39) are not positive for l ≥2.
Proof. The representation (39) clearly gives rise to a positive band representation by replacing σ2σ
ki,ni
1
σ−1
2
by σ
ki,ni
3
.
So [β] = 3 −χ(ˆβ). If l > 2, then we have
mindega F(D) = w(D) + mindega Λ(D) = 3 −χ(ˆβ)+mindega Λ(D) < 1 −χ(ˆβ)
but mindegv P(D) = 1 −χ(ˆβ) as before, so mindega F̸ = mindegv P and we are done by theorem 5.4.
If l = 1, then if n1 = 1, we have a (2,k1,1)-torus link, and for n1 = 3 we have the (1,k1,1,k1,2,k1,3)-pretzel link.
Otherwise we apply the relations for ˜P and Λ at the negative crossing. Then mindega Λ(D+,0) = mindega ˜P(D+,0) =
−2, and [Λ(D+,0)]a−2 = [ ˜P(D+,0)]a−2 by theorem 5.4 since D+,0 are positive braids. That the extra term Λ(D∞) has
no contribution to a−2 follows from lemma 5.9 below. So D satisﬁes Yokota’s conditions in theorem 5.4. (We do not
always know if D depicts a positive link; see remark 5.2.)
If l = 2 then resolve a negative crossing in D = D−via the relation ˜P−= z ˜P0 −˜P+ and via the Λ-relation Λ−=
zΛ0 +zΛ∞−Λ+. Now [ ˜P+,0]a−2 = [Λ+,0]a−2. This follows from the above argument for l = 1. The additional term Λ∞
has a-degree −2 by lemma 5.6, so [Λ−]a−2̸ = [ ˜P−]a−2. Again by theorem 5.4, D = D−can therefore not belong to a
positive link.
✷
Remark 5.1 Ishikawa asks in [I] whether strongly quasi-positive knots satisfy the equality TB = 2gs −1, where TB
is the maximal Thurston-Bennequin invariant. The proof of the lemma shows that there are inﬁnitely many strongly
quasi-positive 3-braid knots with TB < 2gs −1: take any of the knots with l > 2. (There are also many other such
knots, like the counterexamples to Morton’s conjecture in [St3].)
5.2
Positive links
37
Lemma 5.9 If
D = D[n] = b(σk1
1 σk2
2 ...σkn
1 δ2)
with n ≥1 odd, k1,kn ≥1 and ki ≥2 when i = 2,...,n −1, then mindega Λ(D) = −1. Writing k = (k1,...,kn) and
˜w(k) = (k1 −1)+
n
∑
l=2
(kl −2),
we have maxdegz[Λ(D)]a−1 = ˜w(k).
Proof. If n = 1 we check directly (we have a reduced diagram of the (2,k1)-torus link), so let n ≥3.
Consider ﬁrst three special forms of k.
If k = (12∗1) (with 2∗being a sequence of ‘2’), then D is regularly isotopic to a trivial 2-component link diagram. If
k = (12∗) or (2∗1), then D is regularly isotopic to an unknot diagram with one positive kink. In both situations the
claims follow directly.
Now let k = (2∗). We orient D so as to become negative. Then D depicts the (2,−n−1)-torus link. We can evaluate Λ
on L from F(L) by normalization. For its mirror image !L, we can use theorem 5.4 to conclude that mindega F(!L) = n.
Now it is also known that spana F(!L) = c(!L), and c(!L) = n +1, so
maxdega F(!L) = mindega F(!L)+spana F(!L) = n +(n +1) = 2n +1.
Thus mindega F(L) = −1 −2n, and since w(D) = −2n, we have
mindega Λ(D) = −w(D)+mindega F(D) = −(−2n)−1 −2n = −1.
That maxdegz[Λ(D)]a−1 = 1 can also be obtained by direct calculation.
If k is not of these special types, then kl ≥3 for some 1 ≤l ≤n. We resolve a positive crossing in σkl
j . We have (with
D = D+)
Λ(D+) = zΛ(D0) +zΛ(D∞)−Λ(D−).
(40)
Here D0 has ˜w by one less and comes with a z-factor, so it is enough to show that Λ(D−) and Λ(D∞) do not contribute.
If kl > 3, then D−is of the required form and has ˜w by two less, so by induction Λ(D−) has too small z-degree in
[Λ]a−1.
Now consider kl = 3. As in the proof of lemma 5.2 of [St4] we can move by braid relations (regular isotopy) a σ1 in
σ1σ2σ1 until we get a σiσ−1
i
(and then cancel). Here we replaced σ−1
i
by δi, so that such σi right before a δi becomes
a kink, which is negative. By repeating this transformation, we obtain a form that has no σiσi±1σi (i.e. ki > 1 for
1 < i < n) and a certain non-zero number of negative kinks collected at both ends. The negative kinks shift the degree
in a of Λ up, so by induction D−has no contribution to [Λ]a−1.
It remains to deal with the term of D∞in (40). It is the connected sum D[n1]#D[n2] with n1 + n2 = n −1, and with
kl −1 > 1 negative kinks. So by induction mindega Λ(D∞) = kl −1 + (−1) + (−1) > −1, and Λ(D∞) gives no
contribution to [Λ(D+)]a−1.
Theorem 5.5 If a 3-braid link is positive, then it is the closure of a positive or almost positive 3-braid. Along these
links the non-ﬁbered ones are exactly the (1, p,q,r)-pretzel links.
Proof. Consider the ﬁrst claim. Since L is positive, it is strongly quasi-positive, and so has a positive 3-braid band
representation β by theorem 1.1. So β is of Xu’s form R or (21)kR (with k > 0) up to extensions. If β contains σ1σ2σ1
or σ2σ1σ2 we can reduce it as before, until (a) it becomes positive, or (b) it still has a positive band representation, but
it does not contain σ1σ2σ1 or σ2σ1σ2. In case (a) we are done. In case (b) we observe that β is of the form (39), apply
lemma 5.8, and conclude that l ≤1.
It remains to argue which links are not ﬁbered. Positive braids are always ﬁbered, and by direct observation for an
almost positive braid we have Xu’s form R or (21)kR depending on whether in (39) (with l = 1) we have n1 = 3 or
n1 > 3. We proved in theorem 3.2 that the forms (21)kR (for k > 0) give ﬁbered closure links. For n1 = 3 we have as
before the (1, p,q,r)-pretzel links.
✷
38
