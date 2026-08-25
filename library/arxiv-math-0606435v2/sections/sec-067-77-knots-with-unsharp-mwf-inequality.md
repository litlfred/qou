---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-067-77-knots-with-unsharp-mwf-inequality
section_title: "Knots with unsharp MWF inequality"
section_number: 7.7
pages: 60-64
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
This brief part was motivated by the paper of Kawamuro [Kw], which I came across during the continuous work on my
paper. Kawamuro was interested in ﬁnding inﬁnitely many knots for which the MWF inequality is strict, in particular
such satisfying Jones’ conjecture in§7.1. The point to make is that we have at least two ways allowing us to obtain her,
and further such knots much more easily. (In particular it is not necessary to appeal to the heavy geometric machinery
of Neumann-Rudolph-Giroux.)
We already saw an inﬁnite family of examples with unsharp MWF (and satisfying Jones’ conjecture) in the proof of
theorem 7.1. This family is, of course, little insightful, s ince it is settled already by Birman-Menasco’s 3-braid work.
The 4-braid examples they proposed, but could not decide about, deserve more attention. As given in ﬁgure 4 of [Kw],
consider for (x,y,z,w) ∈ Z4 the 4-braids βx,y,z,w = [212213x2y − 12z3w], and let Kx,y,z,w = ˆβx,y,z,w. Birman-Menasco
observe that MW F(Kx,y,z,w) ≤ 3 (see lemma 2.9 in [Kw]), but suspect that many of theKx,y,z,w have braid index 4. One
can exhibit an inﬁnite family of Kx,y,z,w of b = 4, and thus recover theorem 2.8 of [Kw], like this.
Proposition 7.7 There is a natural number N and 6 tuples (α1, . . . ,α4) ∈ Z4 of different mod-2-reductions in (Z/ 2)4,
such that if Kγ := Kγ1,...,γ4 is a knot, then b(Kγ) = 4 whenever (αi) ≡ (γi) mod 2 and gcd
( γi − αi
2
)
≥ N.
Proof. Since (complex) roots of unity are dense on the complex unit c ircle, choose a root of unity t, for which the
3-braid test in corollary 7.3 applies for 9 42 or 949 (see example 7.1). Then, using the formula for ∆ in lemma 3.1 of
[SSW], we see that for each such t there is an n ∈ 2Z \ {0}, such that ∆ ˆβ(t) is preserved when β is replaced by σn
i β.
Moreover, it is easy to check that for all 6 of the 16 possible v ectors of parities of (x,y,z,w), for which Kx,y,z,w is a
knot, there is a representation of (at least one of) 942 or 949 of that parity combination. (The representations given after
deﬁnition 2.7 of [Kw] show 3 of the parity types.) Now, take su ch a representation βα1,...,α4 and vary the parameters
αi by multiples of n. Then, since we can choose (for proper t) n to be any sufﬁciently large even natural number, we
obtain in the claim. ✷
Of course, this elementary argument could be further concre tiﬁed and strengthened. Presumably, one can do much
better using J. Murakami’s test theorem 4.7 (since it is an eq uality). Note that our proof does not conﬁrm Jones’
conjecture on any Kx,y,z,w, so it may trigger the question: would it help to ﬁnd a counter example? This seems very
optimistic, though, as we will soon see from an alternative approach to Kawamuro’s theorem, using the work in§7.1.
First we can settle (also with regard to Jones’ conjecture) the concrete examples K−1,−2,m,2 for m ≥ 2 even, obtained
in her proof.
Proposition 7.8 We have b(K−1,−2,m,2) = 4 for m ⁄= −1,0.
Proof. We give just a brief explanation. We try to calculate the skei n polynomial of the 2-cable β[2]
−1,−2,m,2 of
β−1,−2,m,2, obtained by replacing σi by σ2iσ2i+1σ2i−1σ2i, and we may consider just the coefﬁcient of v4[β−1,−2,m,2]+7.
Again πY ([2312]) has at most 7 different eigenvalues δi, for all Y ⊢ 8 taken together. But now we have no full twist,
and so do not need to deal with the various Y (and their weights WY etc.) one by one. We can sum WY · c(i,Y ) over
Y ⊢ 8, and are left with 7 different q-rational expressions ci to determine. Again this can be done from 7 explicit
polynomials, which can be obtained using Morton’s program. (If we focus on one parity of m only, we can again
reduce the unknowns ci and test polynomials to 5, but need to calculate polynomials from slightly more complicated
braids.)
We calculated in fact 11 polynomials, for|m| ≤ 5, and used those 9 for |m| ≤ 4 in the determination of ci to have extra
safety. The resulting linear equation system for ci (with matrix {δm
i }) is now not a serious problem to MATHEMAT-
ICA, which gives the solution (for generic q) in just a few seconds. Clearing denominators, and looking already at the
extremal q-degrees, we see that for |m| ≥ 6 among the 7 terms ciδm
i the one for i = 2 has the lowest minimal or highest
maximal degree (as a unique term, except for m = 6, where we must use also that the leading coefﬁcient of c6δm
6 has
the same sign). With an explicit check for the other m, we conclude the claim. ✷
This method of proof has also the advantage of easily leading to a qualitative improvement of Kawamuro’s theorem,
which is closer to what one should expect.
61
Proposition 7.9 The tuples (x,y,z,w) for which Kx,y,z,w has braid index 4 (and satisﬁes Jones’ conjecture) are generic
in Z4, in the sense that
lim
n→∞
⏐⏐ { (x,y,z,w) ∈ Z4 : b(Kx,y,z,w) = 4 } ∩ [−n,n]4 ⏐⏐
⏐⏐ [−n,n]4 ⏐⏐ = 1 .(74)
Proof. Extending the argument for proposition 7.8, we see that
˜P(x,y,z,w) := [P(ˆβ[2]
x,y,z,w)]v4[βx,y,z,w]+7(√q − 1/ √q) · √q4[βx,y,z,w]+7 =
7
∑
ix,iy,iz,iw=1
cix,iy,iz,iw δx
ix δy
iyδz
iz δw
iw ,
where cix,iy,iz,iw are again some rational expressions in q. They are obviously not all zero, and the polynomials
˜P(x,y,z,w) have the following property: if one ﬁxes three of the paramet ers (say x,y,z), and ˜P(x,y,z,w) = 0 for 7
different values of the remaining parameter (herew), then it vanishes for all values of that parameter (at the given ﬁxed
3 others). It is then not hard to deduce (74) from this (see e.g. the proof of lemma 11.1 of [St8]). ✷
Acknowledgement. I would like to thank to M. Hirasawa, M. Ishiwata and K. Murasu gi for their contribution, and
S. Kamada, K. Kawamuro, T. Nakamura and D. Silver for some hel pful remarks. The calculations were performed
largely using the programs of [MS2] and [HT], and MATHEMATICA
TM
[Wo]. I also wish to thank to my JSPS host
Prof. T. Kohno at University of Tokyo for his support.
Appendix A. Postliminaries
A.1. Fibered Dean knots (Hirasawa-Murasugi)
Here we present some material due to Hirasawa and Murasugi, w ho studied ﬁbering of generalized Dean knots. An
overview is given in [HM]. As this is work in progress, a longer exposition may appear subsequently elsewhere.
Deﬁnition A.1 The Dean knot K(p,q|r,rs) is given by the closed p-braid
(σp−1σp−2 · · ·σ1)q(σ1σ2 · · ·σr−1)rs ,
with p > r > 1 and q,s non-zero integers such that (q,p) = 1.
Hirasawa and Murasugi proposed a conjecture on these knots and obtained so far the following partial results.
Conjecture A.1 (Hirasawa-Murasugi) A Dean’s knotK(p,q|r,rs) is a ﬁbred knot if and only if its Alexander polyno-
mial is monic, that is, maxcf ∆ = ±1.
Proposition A.1 (Hirasawa-Murasugi) This conjecture has been proven for the following cases.
(a) q = kp + 1, and r and s are arbitrary,
(b) q = kp − 1, and r and s are arbitrary,
(c) r = p − 1, and q and s are arbitrary.
The last case implies in particular that the conjecture is tr ue for p = 3. Below follows a part of the argument in this
case that settles lemma 3.1. (Other parts of their proof are v ery similar to some of our previous arguments. It seems,
for example, that Hirasawa and Murasugi were to some extent aware of Theorem 3.2.)
62 A Postliminaries
(a) ( b) ( c)
Figure 7
Proof of lemma 3.1. We consider the braids [(123)k − 2], with k > 0 ﬁxed. By isotopies and Hopf plumbings, we
modify our surface
[(123)k − 2] → [(1223)k − 2] = [12(2312)k−123 − 2] → [(2312)k−123 − 212] = [(2312)k−12312 − 1] = [(2312)k − 1].
Let F be the surface of the band representation β = [(2312)k − 1]. We will show that F is a ﬁber surface.
Consider the subsurface F0 of F that spans [2312] in the natural manner. We deform the k copies of F0 to the (isotopic
sub)surfaces F ′
0 by a series of diagrams, see ﬁgure 7. (Here strands are numbered from right to left and words composed
downward.)
In ﬁgure 7, for the move (a) → (b), we slide B and C, respectively, along D and A, then delete D (by deplumbing a
Hopf band), and then slide C back along A. For the move (b) → (c), we slide C along B, then slide B along C. The
k bands A can be subsequently removed by Murasugi desumming a (2,k)-torus link ﬁber surface. Thus the surface
F, spanned by ˆβ, turns after (de)summing Hopf bands into a surface F ′ consisting of k copies of F ′
0 and one negative
band N. See ﬁgure 8 (a).
(a) ( b)
Figure 8
Figure 9
A.2 A-decomposition (joint with Hirasawa-Ishiwata) 63
In ﬁgure 8, we perform the move (a) → (b), sliding B along N. The last surface F ′, in ﬁgure 8 (b), is Murasugi sum of
a ﬁbre surface spanning the (2,2,−2)-pretzel link and ˜F, where ˜F consists of k − 1 copies of F ′
0 and the band N. By
induction on k, we see that F ′ is a ﬁbre surface, and hence ˆβ is a ﬁbred link. ✷
A.2. A-decomposition (joint with Hirasawa-Ishiwata)
For the proof of theorem 1.2 we introduce the A-decomposition due to T. Kobayashi [Ko].
A sutured manifold in the sense of Gabai [Ga3] can be understood as a pair(L,H) consisting of a closed 3-dimensional
submanifold H of R3 with boundary S = ∂H a connected surface, and a set of oriented loops L ⊂ H. We require that
one can orient the connected components of S \ L so that the induced orientations on L coincide from both sides of L
(in particular a connected component ofS \ L never bounds to itself along a loop ofL), and are given by the orientation
of L.
Let F be a connected Seifert surface of a(n oriented) linkL = ∂F. We embed F as F × {0.5} into the bicolar H = F ×I
(with I = [0,1]). Then (L,H) becomes a sutured manifold. We call it canonical sutured manifold C(F) of F.
We describe some basic operations on sutured manifolds (L,H).
A decomposition disk D is a disk with P = ∂D ⊂ ∂H, properly embedded in the complement of H (i.e. D ∩ H = P).
We require that D is not parallel to S = ∂H, and satisﬁes P ∩ F ⁄= ∅ . We assume also that the intersection of P and F
is transversal, so that it is a collection of points.
Since L = ∂F is separating on S, the intersection D ∩ L = P ∩ F is an even number of points, and the orientation of L
at the intersection points is alternating (with respect to the orientation of the loop P). See ﬁgure 10 (a).
D
L
D
L
L
a − →
D
(a) (b)
Figure 10
Then L ∩ P separates P into a collection of intervals or arcs. Let a be such an arc. An A-operation on D along a is a
transformation of (L,H) into a sutured manifold (L′,H), where L′ is obtained by splicing L along a. See ﬁgure 10 (b).
A product decomposition along D is a similar operation, due to Gabai [Ga3], and can be described as an A-operation if
|L ∩ D| = 2 (in which case which of the two arcs is chosen is irrelevant), followed by a subsequent gluing of a D2 × I
into H along a neighborhood N(P) ≃ S1 × I of P on S.
Deﬁnition A.2 We deﬁne a sutured manifold (L,H) to be A-decomposable as follows:
1) Assume H is a standardly embedded handlebody (i.e. so that S3 \ H is also one). If L is a collection of trivial
loops on ∂H, and all loops bound disjoint disks in ∂H, then (L,H) is A-decomposable.
2) If (L′,H′) is obtained from (L,H) by a product decomposition (along some decomposition disk D), and (L′,H′)
is A-decomposable, then so is (L,H).
3) Let D be a decomposition disk of H with |L ∩ D| = 2n and choose among the 2 n arcs on P = ∂D a collection
of n cyclically consecutive arcs a1, . . . ,an. (Consecutive is to mean that, taken with their boundary in L ∩ P,
their union is a single interval in P, and not several such intervals.) Let (Li,H) be obtained from (L,H) by
A-decomposition on D along ai for i = 1, . . . ,n. Then if all (Li,H) are A-decomposable, so is (L,H).
