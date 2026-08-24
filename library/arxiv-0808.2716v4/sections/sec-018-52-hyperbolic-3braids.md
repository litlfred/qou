---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-018-52-hyperbolic-3braids
section_title: "Hyperbolic 3–braids"
section_number: 5.2
pages: 28-34
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
closure is a hyperbolic link can be easily identiﬁed from the ir Schreier normal form. Because
a closed braid presentation of a link K comes with a natural orientation, we need to consider
all possible orientations on components of K that are consistent with K being a 3–braid.
In the lemmas that lead up to Theorem 5.5, we rely on two classi cal invariants that are
insensitive to orientation changes on a component of K: the (absolute value of) the linking
number between components of K, and the determinant det( K). Recall that that det( K) is
the absolute value of the Alexander polynomial of K, evaluated at t = −1, or equivalently
the absolute value of the Jones polynomial of K, also evaluated at t = −1. It is well–known
that reversing the orientation on a component of K leaves the determinant unchanged: from
the point of view of the Jones polynomial, this follows becau se changing the orientation of
some component of K changes the Jones polynomial JK (t) by a power of t.
Lemma 5.3. LetK = ˆw be the closure of a generic 3–braid
w =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
where pi, qi are all positive. Suppose that K has two or three components and det(K) ≤ 4.
Then one of two possibilities holds:
(a) det(K) = 2 , and w =C ka, where k is even and a ∈
{
σ2
1σ−1
2 , σ1σ−2
2
}
, or
(b) det(K) = 4 , and w =C ka, where k is even and a ∈
{
σ2
1σ−2
2 , σ4
1σ−1
2 , σ1σ−4
2
}
.
Proof. The proof uses a result of Murasugi [45, Proposition 5.1]. Th ere, Murasugi shows
that a generic 3–braid must have strictly positive determin ant. (In his notation, the class of
generic 3–braids is denoted Ω 6.) The same proposition states that, if ˆ a denotes the closure
of a =σp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 , then
det(K) =
{
det(ˆa), if k is even,
det(ˆa) + 4, if k is odd.
Ifw is generic, then a is also generic, hence det(ˆa)> 0. Thus, if det( K) ≤ 4, we must have
k even and det(K) = det ˆa. Since ˆa is an alternating link, the minimum crossing number is
bounded above by the determinant (see, for example, Burde an d Zieschang [16]). Thus the
crossing number of ˆa is at most 4, and we may list the possibilities for a.
CUSP AREAS OF F AREY MANIFOLDS 29
Recall that the crossing number of an alternating link is rea lized by any alternating dia-
gram without nugatory crossings, and the only way an alterna ting 3–braid can have nugatory
crossings is if the braid word is σr
1σ−1
2 orσ1σ−r
2 . Thus alternating closed 3–braids with cross-
ing number at most 4 consist of words of the form σp
1 for appropriatep,σp
1σ−q
2 , for appropriate
p, q, and σ1σ−1
2 σ1σ−1
2 . All others will have higher crossing numbers.
Sinceσp
1 is not generic, we need not consider these. Since the closed b raid corresponding to
C kσ1σ−1
2 σ1σ−1
2 has just one component, and we are assuming K has at least two components,
we need not consider these words either. Finally, the braids σp
1σ−q
2 have the appropriate
number of crossings for ( p,q ) = (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (3, 1), and (4, 1). Of
these, (1, 1), (1, 3), and (3, 1) have only one link component. The remaining possibilitie s are
a ∈ {σ2
1σ−1
2 , σ1σ−2
2 , σ2
1σ−2
2 , σ4
1σ−1
2 , σ1σ−4
2 }.
If a =σ2
1σ−1
2 or a =σ1σ−2
2 , one easily computes that det( K) = det(ˆa) = 2, and conclusion
(a) holds. If a is one of σ2
1σ−2
2 , σ4
1σ−1
2 , or σ1σ−4
2 , then det(K) = det(ˆa) = 4, and conclusion
(b) holds. □
We can now restrict the 3–braids that correspond to Seifert ﬁ bered links.
Lemma 5.4. Let K = ˆw be the closure of a 3–braid w, and suppose that S3/integerdivideK is Seifert
ﬁbered. Then w is either non-generic, or else conjugate to σp
1σ±1
2 , σ±1
1 σq
2, or σ2
1σ−2
2 .
Proof. A theorem of Burde and Murasugi [15] states that if S3/integerdivideK is Seifert ﬁbered, then
K consists of ﬁnitely many ﬁbers in a (possibly singular) Seif ert ﬁbration of S3. In case
the Seifert ﬁbration of S3 is not singular, the ﬁbration extends to S3. The Seifert ﬁbrations
of S3 were classiﬁed by Seifert [53] (see also Orlik [48]). As a con sequence, K must be a
generalized torus link : a link that is embedded on an unknotted torus T (this is called an
(m,n ) torus link) plus possibly one or both cores of the solid tori in the complement of T .
The singular ﬁbration does not extend to S3: it is the product ﬁbration on a solid torus,
in which each ﬁber is a meridian of the complementary unknot. However, note that in this
case the result is again a generalized torus link, with the un knot making up the core of the
(m, 0) torus link. The question of which closed 3-braids represe nt generalized torus links has
been studied by Murasugi in [45].
In an ( m,n ) torus link, we may assume without loss of generality that m >0, and that
either n = 0 or |n| ≥ m. With this normalization, a theorem of Schubert [52] implie s that
the bridge number of the ( m,n ) torus link is m. Since the braid index is greater than or
equal to the bridge number, any choice of orientation on the c omponents of an ( m,n ) torus
link must yield a braid index of at least m. Thus, if we add c cores of solid tori and obtain
a 3–braid, 1 ≤m ≤ 3 −c. There are three cases, conditioned on the value of c.
Case 0: c = 0. Then K is an (m,n ) torus link, where 1 ≤m ≤ 3. Murasugi classiﬁes the
torus links that can be written as closed 3–braids in [45, Sec tion 12]. However, a careful
reading of his proofs indicates that he is assuming multiple components of torus links are
always oriented consistently. For our purposes, we will als o need to consider the torus links
in which the orientation of some component is reversed. In fa ct, the machinery developed
by Murasugi in this monograph is suﬃcient to handle all choic es of orientation. For ease of
reading, we will include the arguments for all the cases not i mmediately apparent from [45].
If m = 1, then K is the unknot, and Theorem 12.1 in Murasugi’s monograph show s
w ∼ σ±1
1 σ±1
2 . If m = 2, then K is a (2 ,n ) torus link. If the (one or two) components of
K are oriented consistently, then it is an elementary torus link in Murasugi’s terminology.
Then, Theorem 12.3 of his monograph implies w ∼σp
1σ±1
2 or w ∼σ±1
1 σq
2.
30 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Now, suppose that n = 2ℓ, and K is a (2, 2ℓ) torus link whose components have opposite
orientations. Then K is the oriented boundary of a Seifert surface that is an annul us.
Using this annulus, we calculate that the Alexander polynom ial of K is ∆ K(t) = ℓ(1 −t);
thus deg ∆ K(t) = 1. By Proposition 8.1 of [45], K can be the closure of a 3–braid only if
|ℓ| ≤ 1
2 deg ∆ K(t) + 2 = 5
2 . Since the determinant of the (2 , 2ℓ) torus link is |2ℓ|, and this
fact remains true under orientation reversal of components , det(K) = |2ℓ| ≤ 4. Thus, if w is
a generic 3–braid that represents K with this orientation, Lemma 5.3 applies.
If det(K) = 2, Lemma 5.3 says the generic braid w representingK must be conjugate to
C kσ2
1σ−1
2 or w ∼C kσ1σ−2
2 , where k is even. Without loss of generality, say w ∼C kσ2
1σ−1
2 .
Then the two components of ˆ w have linking number equal to |2k + 1|. But since K is
the (2, ±2) torus link, the linking number of the two components is 1. T hus k = 0, and
w ∼σ2
1σ−1
2 , as desired.
If det(K) = 4, Lemma 5.3 says the only generic braids representing K must be conjugate
to C kσ2
1σ−2
2 , C kσ4
1σ−1
2 , or C kσ1σ−4
2 . The closure of C kσ2
1σ−2
2 has three components, so we
don’t need to consider this case. If w ∼C kσ4
1σ−1
2 , then the two components of ˆw have linking
number |2 + 2k|, which is equal to 2 by hypothesis. Thus k is −2 or 0. But if k = −2, the
closure of C −2σ4
1σ−1
2 is a hyperbolic link, a contradiction. Thus k = 0, and w ∼σ4
1σ−1
2 , as
desired. The argument when w ∼C kσ1σ−4
2 is identical.
Finally, suppose that m = 3, and K is a (3,n ) torus link. Then K has either one or three
components. If K is a knot, Proposition 12.3 of [45] shows that K cannot be represented by
a generic 3–braid. In fact, Murasugi’s argument also works f or links, with all orientations,
but for completenss we include the argument here.
If K is a 3–component torus link (3 , 3ℓ), the linking number of any two components of
K has absolute value |ℓ|. Proposition 3.3 of [45] implies that det( K) is either 0 or 4. By
Lemma 5.3, any generic braid w ∼C ka representing K, must be conjugate to C kσ2
1σ−2
2 , as
all the other possibilities in the lemma have two components . Now, consider the pairwise
linking numbers between components in the closure of w ∼C kσ2
1σ−2
2 . These pairwise linking
numbers are equal in absolute value to |k|, |k + 1|, and |k − 1|. But all these numbers must
be equal to |ℓ|, a contradiction.
Case 1: c = 1. Then K =Lt ∪La, where Lt is a (m,n ) torus link with m = 1 or m = 2,
and La is the core of one of the two solid tori. If m = 1, then (depending on the choice of
solid torus) K is either a (2 , 2n) torus link and we reduce to case 0, or K is the Hopf link,
which is the (2, 2) torus link, and we again reduce to case 0. Thus we may suppos e that Lt is
a (2,n ) torus link. Then, as an unoriented link, K admits a diagram in one of two possible
forms, shown in Figure 10, depending on which solid torus La came from.
Subcase 1a: Suppose that the link K is depicted in the left panel of Figure 10. Then
we can characterize the linking number lk(Lt,L a) as follows. If n is odd and Lt is a knot,
then its linking number with La is ±2; if n is even and Lt has two components, then each
component of Lt has linking number ±1 with La. Note that the absolute value of the linking
number is insensitive to changes of orientation.
If all the strands in Figure 10 are oriented counterclockwis e, the link K in the left panel of
the ﬁgure can be represented by the braid word v =σn
1σ2σ2
1σ2. Of course, a priori there may
be other braid representatives, possibly corresponding to other choices of orientation on one
or more components of K. Nonetheless, knowing that K can be obtained as the closure ˆv of
the braid represented by v allows us to compute link invariants. Because the normal for m
of v is Cσ n−2
1 , Murasugi’s Proposition 3.6 gives that det( K) = 4. Suppose that, with some
CUSP AREAS OF F AREY MANIFOLDS 31
PSfrag replacements
nn
Figure 10. Case 1 of Lemma 5.4: two ways to add the core of a solid torus
to a (2,n ) torus link.
choice of orientation, K is represented by the generic braid w. Since det( K) = 4, Lemma
5.3 implies the normal form of w must be one of C kσ2
1σ−2
2 , C kσ4
1σ−1
2 , or C kσ1σ−4
2 .
If w ∼ C kσ2
1σ−2
2 , then K = ˆw is a 3–component link. The 2–component links contained
in K have pairwise linking numbers equal in absolute value to |k|, |k + 1|, and |k − 1|.
By hypothesis, two of these linking numbers must be equal to 1 . It follows that the only
possibility is k = 0, hence w ∼σ2
1σ−2
2 , as desired.
If w ∼C kσ4
1σ−1
2 , then K = ˆw =Lt ∪La is a 2–component link. In this case, we compute
that |lk(Lt,L a)| = |2 + 2k|, which is equal to 2 by hypothesis. Thus k is −2 or 0. But if
k = −2, the closure of C −2σ4
1σ−1
2 is a hyperbolic link, a contradiction. Thus k = 0, and
w ∼σ4
1σ−1
2 , as desired. The case when w ∼C kσ1σ−4
2 is identical.
Subcase 1b: Suppose that the unoriented link K is depicted in the right panel of Figure
10. It follows that lk(Lt,L a) = ±n, depending on choices of orientations of the components.
If all the strands of K are oriented counterclockwise, K can be represented by the braid
word v = (σ1σ2σ1)n. (Just as in Subcase 1a, there may be other braid representat ives, but
knowing one braid representative v allows us to compute invariants that are insensitive to
orientation.) Using the braid relation σ1σ2σ1 =σ2σ1σ2, we can rewrite v as
v =
{
C n/ 2, if n is even,
C (n−1)/ 2σ1σ2σ1, if n is odd.
If n is even, then ˆv is a torus link. Thus the unoriented link K is a torus link, and we
reduce to Case 0. If n is odd, then Murasugi’s Proposition 3.5 gives det( K) = 2. Thus, by
Lemma 5.3, any generic braid w that also represents K must have normal form C kσ2
1σ−1
2 or
C kσ1σ−2
2 .
If w ∼ C kσ2
1σ−1
2 , then K = ˆw = Lt ∪La is a 2–component link. We may immediately
compute that one component Lt is the (2, 2k − 1) torus knot, the other component La is the
unknot, and |lk(Lt,L a)| = |2k + 1|. Because by assumption, Lt is the (2,n ) torus link, this
implies |n| = |2k − 1|. Additionally, since by assumption lk(Lt,L a) = ±n, we may conclude
that |n| = |2k + 1|. This is possible only if k = 0. So w ∼σ2
1σ−1
2 , as desired. The case when
w ∼C kσ1σ−2
2 is identical.
32 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Case 2: c = 2. Then K = Lt ∪La ∪Lb, where Lt is an unknot on T , and La and Lb are
cores of the two solid tori. Since Lt is a (1,n ) curve on the torus T , one of the cores La or
Lb (say,Lb) can be isotoped to lie on T , disjointly from Lt. Thus, as an unoriented link,
Lt ∪Lb is a torus link on T , and this case reduces to Case 1. □
The next theorem characterizes the 3-braids whose closures represent hyperbolic links.
Theorem 5.5. Letw ∈B3 be a word in the braid group, and let K ⊂S3 be the link obtained
as the closure of w. Then S3/integerdivideK is hyperbolic if and only if w is generic and not conjugate
to σp
1σq
2 for arbitrary integers p,q .
Proof. First, we check the “only if” direction. If w is non-generic, then by Theorem 5.2,
Mw =S3/integerdivide(K ∪A) is a graph manifold with Gromov norm 0. Since the Gromov norm of a
manifold cannot increase under Dehn ﬁlling [56, Propositio n 6.5.2], S3/integerdivideK also has Gromov
norm 0, and is not hyperbolic. If w is generic and conjugate to σp
1σ±1
2 , then K is a (2 ,p )
torus link (similarly for σ±1
1 σq
2). Finally, if w is conjugate to σp
1σq
2, where |p|, |q| ≥ 2, then K
is the connected sum of (2 ,p ) and (2,q ) torus links, hence cannot be hyperbolic.
For the “if” direction, suppose that S3/integerdivideK is not hyperbolic. Then, by Thurston’s hy-
perbolization theorem [57], it is reducible, toroidal, or S eifert ﬁbered. If S3/integerdivideK is Seifert
ﬁbered, then Lemma 5.4 implies w is non-generic or conjugate to σp
1σq
2. Meanwhile, if S3/integerdivideK
is reducible, then K is a split link. By a theorem of Murasugi [45, Theorem 5.1], th is can
only happen if w ∼σp
1: hence, w is not generic.
Finally, suppose that S3/integerdivideK contains an essential torus T . If w is not generic, then we are
done. If w is generic, a theorem of Lozano and Przytycki [40, Corollary 3.3] says thatT always
has meridional compression disks, i.e. there is some disk D ⊂S3 such that D ∩T =∂D and
D ∩K is a point. 1 After meridionally compressing T , i.e. after replacing a neighborhood of
∂D on T with two parallel copies of the annulus D/integerdivideK, we obtain an essential, meridional
annulus that splits K into connected summands. But by a theorem of Morton [43], a br aid
w ∈B3 represents a composite link if and only if w ∼σp
1σq
2, where |p|, |q| ≥ 2. See Birman
and Menasco [12, Corollary 1] for another way to identify the toroidal 3–braids. □
5.3. V olume estimates. For suﬃciently long generic 3–braids, the methods of the pre vious
sections estimate hyperbolic volume.
Theorem 5.6. Let K = ˆw be the closure of a generic 3–braid w ∼ C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
wherepi, qi are all positive and w ≁σp
1σ−q
2 . Then K is hyperbolic, and
(6) 4 v3s − 276.6 < vol(S3/integerdivideK) < 4v8s.
Furthermore, the multiplicative constants in both the uppe r and lower bounds are sharp.
Proof. Let A be the braid axis of K. Then Mw = S3/integerdivide(K ∪A) is a 4–punctured sphere
bundle with monodromy
Ω = Lp1Rq1 · · ·LpsRqs.
Futer and Gu´ eritaud showed [31, Corollary B.2] that the length of Ω coarsely determines the
volume of M :
(7) 4 v3s ≤ vol(Mw) < 4v8s,
where both the upper and lower bounds are sharp. That is: ther e exist 4–punctured sphere
bundles that realize the lower bound, and other bundles that areε–close to the upper bound.
1Lozano and Przytycki’s result is stated for “hyperbolic” 3– braids. However, their deﬁnition of hyperbolic
is the same as our deﬁnition of generic.
CUSP AREAS OF F AREY MANIFOLDS 33
SinceS3/integerdivideK is obtained by Dehn ﬁlling on Mw, the same upper bound applies to the volume
ofS3/integerdivideK. Furthermore, by choosing an extremely long ﬁlling slope (w hich will happen when
|k| → ∞ ), one can arrange for vol( S3/integerdivideK) to be arbitrarily close to 4 v8s.
For the lower bound on volume, we rely on Theorem 4.7. That the orem states that the
meridian of A (which will be transverse to the ﬁbers) has length at least 8
√
3s/147. In
particular, when s ≥ 67, the meridian will be longer than 2 π. Thus we may apply Theorem
1.1 of [25], which estimates the change in volume under Dehn ﬁ lling along slopes longer than
2π. For all s ≥ 67, we obtain
vol(S3/integerdivideK) ≥
(
1 −
( 2π
8
√
3s/147
)2)3/ 2
vol(Mw), by [25, Thm 1.1] and Thm 4.7
≥
(
1 − 7203π2
16s2
)3/ 2
4v3s, by inequality (7)
Note that by calculus,
(
1 − 7203π2
16s2
)3/ 2
4v3s − 4v3s
has a minimum of −276.52 · · · for s ≥ 67. Thus vol(S3/integerdivideK)> 4v3s − 276.6.
On the other hand, if s ≤ 67, then 4v3s − 276.6< 0, hence the volume estimate is trivially
true. Thus the lower bound on volume holds for all hyperbolic 3–braids.
Finally, to show sharpness of the multiplicative constant i n the lower bound, consider
3–braids of the form w = (σ1σ−1
2 )s. In the proof of Theorem B.1 of [31], it was shown that
for the closures of these braids, vol( Mw) = 4 v3s. Since vol( S3/integerdivideK) < vol(Mw) = 4 v3s for
this sequence of knots, the multiplicative constant 4 v3 must be sharp. □
We close this section with an interesting side comment. Theo rem 5.6 compares in an
intriguing way to prior results that estimate the volume of a link complement in terms of
the twist number of a diagram. (See Section 1.2 and the introd uction of [27] for deﬁnitions
and background.) In the braid word w, each term σpi
1 or σ−qi
2 corresponds to a twist region
involving a pair of strands of K. Meanwhile, when k ⁄= 0, the term C k deﬁnes a single
generalized twist region , in which we perform k full twists on all three strands of the braid.
Altogether, the braid word w deﬁnes a diagram with either 2 s or 2s + 1 generalized twist
regions – including 2 s ordinary twist regions twisting on two strands of K. As a result,
Theorem 5.6 can be reformulated in the following way.
Corollary 5.7. LetK be a hyperbolic closed 3–braid, and let D(K) be the braid diagram cor-
responding to the Schreier normal form for K. If tgen(D) denotes the number of generalized
twist regions in the diagram D, then
2v3tgen(D) − 279 < vol(S3/integerdivideK) < 2v8tgen(D).
Proof. By Theorem 5.5,K must be represented by a generic word w =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 .
Substituting 2s ≤tgen(D) ≤ 2s + 1 into Theorem 5.6 gives the desired volume estimate. □
Remark. In [27, Corollary 3.2], we show that the twist number alone, a s opposed to the
generalized twist number, is not a good measure of the volume of 3–braids. Thus the single
generalized twist region from the term C k is important in the corollary above.
34 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
