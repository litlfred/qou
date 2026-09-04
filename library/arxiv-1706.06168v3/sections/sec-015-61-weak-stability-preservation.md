---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-015-61-weak-stability-preservation
section_title: "Weak Stability Preservation"
section_number: 6.1
pages: 18-23
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
Borcea and Br¨ and´ en deﬁne the following symbol:
SymbBB (T ) := T [(x +z)λ] =
∑
µ≤λ
( λ
µ
)
zλ−µT (xµ)
They then obtain the following characterization of stability-preser ving linear operators.
Theorem 1.1 (Borcea-Br¨ and´ en). Fix λ ∈ Nm
0 and any linear operator T : Cλ[x1,...,x m] → C[x1,...,x m].
The following are equivalent.
(i) T maps Hm
+ -stable polynomials to weakly Hm
+ -stable polynomials.
(ii) One of the following holds:
(a) SymbBB (T ) is H2m
+ -stable.
(b) T has image of dimension at most one, and is of the form
T :p ↦→q ·ψ(p)
whereq ∈ C[x1,...,x m] is Hm
+ -stable, and ψ is some linear functional.
Using our terminology, this is a characterization of weak stability-pr eserving linear operators. This
fantastic result perhaps has but one unfortunate piece: the deg eneracy condition ( ii)(b). Its necessity is
demonstrated in the following.
Example 6.1. Deﬁne T : Cn[x] → C[x] via:
T :
n∑
k=0
( n
k
)
akxk ↦→(an +an−2)xn
This operator obviously preserves weak H+-stability. We then have that Symb BB (T ) = (z2 + 1)xn, which is
not H2
+-stable.
As we will see below, this condition can be removed once we only conside r strong stability-preserving
operators. So then, maybe strong stability is the more natural no tion? However “natural” it is, unfortunately
it leaves out operators one might wish to consider. The most fundam ental of such operators is the derivative
operator ∂x. While ∂x preserves strong H+-stability, it only preserves weak H+-stability. Speciﬁcally,
1 ∈ Cn[x] is H+-stable (all its roots are at ∞), but ∂x1 ≡ 0. With this, one obviously wants to be able
to include weak stability preserving operators in any characterizat ion of H+-stability preserving operators.
We discuss how to use our strong stability preservation character ization to deal with operators like ∂x in
Example 6.8.
18
6.2 Strong Stability Preservation
We now state one of our main characterization results, the strong stability preservation characterization. We
then derive the Borcea-Br¨ and´ en characterization as a corollary.
Theorem 6.2. Fix λ ∈ Nm
0 , α ∈ Nl
0, a linear operator T ∈ Hom(V (λ),V (α)), any disjoint Grace pair
(C1 × · · · ×Cm,B 1 × · · · ×Bm), and any sets S1,...,S l ⊆ CP1. The following are equivalent.
(i) T maps (C1 × · · · ×Cm)-stable polynomials to nonzero (S1 × · · · ×Sl)-stable polynomials.
(ii) T maps (C1 × · · · ×Cm)-stable evaluation symbols to nonzero (S1 × · · · ×Sl)-stable polynomials.
(iii) Symb(T ) is (B1 × · · · ×Bm) × (S1 × · · · ×Sl)-stable.
One should notice the generality of this result in terms of stability reg ions. First note that any disjoint
Grace pair can be considered, without altering the symbol in any way (e.g., via conjugation by M¨ obius
transformations). And further, the output sets that can be co nsidered have no restrictions whatsoever. The
power of these extra features can be seen in the following examples , which demonstrate classical results
regarding polynomial convolutions in a very symbol-oriented way.
Example 6.3. Fix p,q ∈V (n), so that ( zj : 1) are the roots in CP1 of q for j ∈ [n]. So, q has no roots at
∞. The additive (Walsh) convolution of p and q is deﬁned via:
p ∗n
+q := 1
n!
n∑
k=0
∂k
xp · (∂n−k
x q)(0, 1)
With this, Tq(p) := p ∗n
+q is a linear operator in Hom( V (n),V (n)), and we have:
Symb(Tq) =
n∏
j=1
(xw − (z +zjw)y) = Hmg (n,n)


n∏
j=1
(x − (z +zj))


LetC ⊂ CP1 be any projectively convex region, and deﬁne S := ⋃
j(C +zj). If we order the input variables
of Symb(Tq) as (z,w,x,y ), it is then straightforward to show that Symb( Tq) is C × (CP1 \S)-stable. (First
deal with possible ( x : y) = (1 : 0) or ( z : w) = (1 : 0) cases, and then assume y = w = 1 to simplify
the remaining cases.) Applying the previous theorem, this implies Tq maps polynomials with roots in C to
polynomials with roots in S. (This is Theorem 5.3.1 in [ RS02].) Picking C = H− and real-rooted q implies
Tq maps H+-stable polynomials to H+-stable polynomials. Restricting to p ∈ VR(n) then shows that Tq
preserves real-rootedness.
Example 6.4. Fix p,q ∈ V (n), so that ( zj : 1) ⁄= 0 are the roots of q for j ∈ [n]. So, q has no roots at 0
or ∞. The multiplicative (Grace-Szeg˝ o) convolution of p and q (with coeﬃcients pk and qk, respectively) is
deﬁned via:
p ∗n
×q :=
n∑
k=0
( n
k
) −1
(−1)kpkqkxkyn−k
With this, Tq(p) := p ∗n
×q is a linear operator in Hom( V (n),V (n)), and we have:
Symb(Tq) =
n∏
j=1
(xw −zjzy) = Hmg (n,n)


n∏
j=1
(x −zjz)


Let C ⊂ CP1 be any projectively convex region, and deﬁne S := ⋃
j(zj ·C). If we order the input variables
of Symb(Tq) as ( z,w,x,y ), it is then straightforward to show that Symb( Tq) is C × (CP1 \S)-stable. (As
above, ﬁrst deal with possible ( x : y) = (1 : 0) or ( z : w) = (1 : 0) cases, and then assume y = w = 1 to
19
simplify the remaining cases.) Applying the previous theorem, this implie s Tq maps polynomials with roots
in C to polynomials with roots in S. (This is Theorem 3.4.1d in [ RS02].) Picking C = H− ∪ R+ and q
with only positive roots implies Tq maps ( H+ ∪ R−)-stable polynomials to ( H+ ∪ R−)-stable polynomials.
Restricting to p ∈VR(n) then shows that Tq preserves positive-rootedness.
In order to prove the above theorem, we need an operator-theo retic corollary to Grace’s theorem. The
following result is the main motivation for the symbol lemma (Lemma 3.7), and demonstrates just how
closely Grace’s theorem relates to stability properties of linear oper ators. Further, it gives a slightly stronger
result in one direction of the above characterization, as Grace pair disjointness is not a required premise.
Proposition 6.5. Fix λ ∈ Nm
0 ,α ∈ Nl
0, a linear operator T ∈ Hom(V (λ),V (α)), any Grace pair (C1 × · · · ×
Cm,B 1 × · · · ×Bm), and any sets S1,...,S l ⊆ CP1. If Symb(T ) is (B1 × · · · ×Bm) × (S1 × · · · ×Sl)-stable,
then T maps (C1 × · · · ×Cm)-stable polynomials to nonzero (S1 × · · · ×Sl)-stable polynomials.
Proof. Fix any (C1 × · · · ×Cm)-stableq ∈V (λ) and any (c,d ) = (c1,d 1,...,c l,d l) ∈ C2l such that (cj :dj) ∈
Sj for all j ∈ [l]. Let kλ,α := (−1)α(λ!)2(α!)2. The evaluation symbol lemma (Lemma 5.10) and the symbol
lemma (Lemma 3.7) then give us the following expression of T (q) evaluated at ( c,d ) = (c1,d 1,...,c l,d l):
kλ,αT (q)(c,d ) = kλ,0Dα(
T (q) ⊗ (dx −cy)α)
=Dλ⊔α(
Symb(T ) ⊗q · (dx −cy)α)
=k0,αDλ(
Symb(T )(z,w,c,d ) ⊗q(z,w )
)
In the last expression above, Dλ acts on the variables ( z,w ) = ( z1,w 1,...,z m,w m). Since r(z,w ) :=
Symb(T )(z,w,c,d ) is ( B1 × · · · × Bm)-stable and q(z,w ) is ( C1 × · · · × Cm)-stable, we have that the last
expression above is nonzero by deﬁnition of Grace pair (Deﬁnition 5.2). This implies T (q) is (S1 × · · · ×Sl)-
stable.
With this, we now give the proof of Theorem 6.2.
Proof of Theorem 6.2. The statement of this result, as well as its proof, is quite similar to th at of the
evaluation symbol version of Grace’s theorem given in Corollary 5.11. We explicitly give the proof anyway,
as it is rather short and straightforward.
(i) ⇒ (ii). Immediate.
(ii) ⇒ (iii). Fix ( a,b ) = ( a1,b 1,...,a m,b m) ∈ C2m such that ( aj : bj) ∈ Bj for all j ∈ [m], and ﬁx
(c,d ) = (c1,d 1,...,c l,d l) ∈ C2l such that (cj :dj ) ∈Sj for all j ∈ [l]. Let kλ,α := (−1)α(λ!)2(α!)2. Since Bj
and Cj are disjoint, we have that ( aj :bj) ⁄∈Cj for all j, and therefore Symb(ev (a,b)) = (bx −ay)λ ∈V (λ)
is an evaluation symbol which is ( C1 × · · · ×Cm)-stable. Using the evaluation symbol lemma (Lemma 5.10)
and the symbol lemma (Lemma 3.7), we compute:
(−1)λkλ,α Symb(T )(a,b,c,d ) = Dλ⊔α(Symb(T ) ⊗ (bx −ay)λ(dx −cy)α) = kλ,αT [(bx −ay)λ](c,d )
By (ii) the last expression is nonzero, and thus Symb( T )(a,b,c,d ) ⁄= 0. This implies Symb( T ) is (B1 × · · · ×
Bm) × (S1 × · · · ×Sl)-stable.
(iii) ⇒ (i). Proposition 6.5 above.
As mentioned above, the previous proposition gives a slightly strong er result in the (symbol stability ⇒
operator stability) direction. Using it, we revisit the additive and mult iplicative convolutions with a more
algebraic/symbolic mentality.
Example 6.6. By Deﬁnition 3.6, the Symb map gives a bijection between certain spaces of linear ope rators
and polynomials. So, we can uniquely deﬁne a linear operator by giving it s symbol. Using this idea, we
specify T ∈ Hom(V (n,n ),V (n)) by deﬁning its symbol in V (n,n,n ) with variables ( z,w ), (t,s ), (x,y ) as
follows:
Symb(T ) := Hmg (n,n,n) [(x − (z +t))n] = (xws − (zs +tw)y)n
20
Now, let us consider the additive convolution ∗n
+ as an element of Hom( V (n,n ),V (n)) in the following way.
Since V (n,n ) ∼= V (n) ⊠V (n), we deﬁne ∗n
+ on elements p ⊠q ∈ V (n) ⊠V (n) via ∗n
+(p ⊠q) := p ∗n
+q and
extend linearly. We then compute Symb( ∗n
+) as follows:
Symb(∗n
+) = ∗n
+ [(zy −xw)n ⊠ (ty −xs)n] = (xws − (zs +tw)y)n
That is, ∗n
+ is the operator that has our desired symbol. Fixing any a,b,c,d ∈ R such that a < band
c < d, we deﬁne the sets C1 := H+ \ (a,b ), C2 := H+ \ (c,d ), B1 := H− ∪ [a,b ], B2 := H− ∪ [c,d ]), and
S := H+ \ [a +c,b +d]. Proposition 6.5 then implies p ∗n
+ q has all its roots in [ a +c,b +d] whenever
p,q ∈VR(n) have all their roots in ( a,b ) and (c,d ), respectively. For real-rooted p,q of degree n, this implies:
minroot(p) + minroot(q) ≤ minroot(p ∗n
+q) ≤ maxroot(p ∗n
+q) ≤ maxroot(p) + maxroot(q)
Notice that we actually get a bit more. For ( C1 ×C2)-stable r := ∑
jpj ⊠qj ∈V (n) ⊠V (n) ∼=V (n,n ), we
have that ∗n
+[r] is S-stable. That is, ∗n
+ has stability properties as an operator in Hom( V (n,n ),V (n)), not
just as a convolution between two polynomials in V (n).
Example 6.7. As in the previous example, we can consider the multiplicative convolut ion ∗n
× as an element
of Hom(V (n,n ),V (n)) by deﬁning ∗n
×(p ⊠q) := p ∗n
×q on elements p ⊠q ∈ V (n) ⊠V (n) ∼= V (n,n ) and
extending linearly. We then compute its symbol in V (n,n,n ) with variables ( z,w ), (t,s ), (x,y ) as follows:
Symb(∗n
×) = ∗n
× [(zy −xw)n ⊠ (ty −xs)n] = (xws −zty)n = Hmg (n,n,n) [(x −zt)n]
Fixing any a,b,c,d ∈ R+ such that 0 <a<b and 0 <c<d , we deﬁne the sets C1,C2,B1, and B2 as in the
previous example. We then deﬁne S := R \ [ac,bd ]. Proposition 6.5 then implies p ∗n
×q has all its real roots
in [ac,bd ] whenever p,q ∈VR(n) have all their roots in ( a,b ) and (c,d ), respectively. (Notice that we could
not apply the proposition if H+ ⊂S or H− ⊂S.) Since Example 6.4 implies p ∗n
×q is positive-rooted (and
hence, real-rooted) whenever p and q are, this implies:
minroot(p) · minroot(q) ≤ minroot(p ∗n
×q) ≤ maxroot(p ∗n
×q) ≤ maxroot(p) · maxroot(q)
As in the previous example, we also obtain stability properties for ∗n
× as an operator in Hom( V (n,n ),V (n)),
and not just as a polynomial convolution.
Using similar techniques, we can also circumvent the issue that arises from the fact that ∂x only preserves
weak stability.
Example 6.8. For ﬁxed n ≥ 1, consider the operator ∂x ∈ Hom(V (n),V (n − 1)). We compute:
Symb(∂x) = ∂x[(zy −xw)n] = −nw(zy −xw)n−1 = Hmg (n,n−1)
[
−n(z −x)n−1]
For any a,b ∈ R such that a < b, it is straightforward to see that Symb( ∂x) is ( C ×B)-stable for C :=
H− ∪ (a,b ) and B := H+ \ (a,b ), where the variables are ordered ( z,w ), (x,y ). (Notice that this does not
hold when ∞ ∈ C, due to the w factor in the symbol.) Since ( C,B ) is a disjoint Grace pair, the Theorem
6.2 implies ∂x preserves strong B-stability.
With this, let f ∈ Cn[x] be a H+-stable polynomial of degree 1 ≤ m ≤ n, and let p ∈ V (m) be its
degree-m homogenization. Then p has no roots at inﬁnity, and therefore there exists a < bsuch that p is(
H+ \ (a,b )
)
-stable. The previous discussion implies ∂xp is
(
H+ \ (a,b )
)
-stable, and in particular ∂xp is
H+-stable. Since ∂x commutes with homogenization, this also implies ∂xf is H+-stable.
Other issues related to weak stability preservation can be dealt with in a similar way, by considering
stability regions with small intervals in R about ∞ attached. More generally though, the Borcea-Br¨ and´ en
characterization ends up being a corollary of Theorem 6.2, which we discuss and demonstrate now.
21
6.3 Deriving the Complex Borcea-Br¨ and´ en Characterizati on
As mentioned above, we hope to obtain the Borcea-Br¨ and´ en cha racterization from our strong stability
characterization given in Theorem 6.2. To this end, we state two corollaries to Theorem 6.2, which look
(naively) as close to the Borcea-Br¨ and´ en characterization as possible. Let Cc denote the complement of C
in CP1.
Corollary 6.9. Fix λ,α ∈ Nm
0 , a linear operator T ∈ Hom(V (λ),V (α)), and a Grace pair of the form
(C1 × · · · ×Cm,C c
1 × · · · ×Cc
m). The following are equivalent.
(i) T preserves strong (C1 × · · · ×Cm)-stability.
(ii) Symb(T ) is (Cc
1 × · · · ×Cc
m) × (C1 × · · · ×Cm)-stable.
Corollary 6.10. Fix λ,α ∈ Nm
0 and a linear operator T ∈ Hom(V (λ),V (α)). T preserves strong stability
iﬀ Symb(T ) is (H−
m
× Hm
+ )-stable.
In Theorem 1.1, the analogous “if” direction of the previous corollary is paraphras ed as follows: T
preserves weak stability if the Borcea-Br¨ and´ en symbol ofT is stable . To see how this statement relates, we
restate the deﬁnition of the Borcea-Br¨ and´ en symbol:
SymbBB (T ) := T
[
(z +x)λ]
=
∑
µ≤λ
( λ
µ
)
zλ−µT (xµ)
Notice that by applying z ↦→ −z and homogenizing, we obtain (up to scalar) the universal symbol Sy mb(T )
deﬁned in this paper. The crucial diﬀerence then is the fact that th e Borcea-Br¨ and´ en “if” direction deals only
with open upper half-planes, whereas the previous corollary requires closed half-plane stability of Symb( T )
in the ﬁrst m pairs of variables. That is, the required premises of the “if” directio n of the previous corollary
are strictly stronger than that of the Borcea-Br¨ and´ en result.
These two results can be reconciled, however, which we now demons trate. The following result provides
the main link to the Borcea-Br¨ and´ en characterization, and it can be intuitively described as follows: with
the exception of having a one-dimensional range, a linear operator which maps ( C1 × · · · × Cm)-stable
polynomials to weak ( B1 × · · · ×Bm)-stable polynomials can only have zeros on the boundary of the set of
(C1 × · · · ×Cm)-stable polynomials.
Lemma 6.11. Fix λ,α ∈ Nm
0 , a linear operator T ∈ Hom(V (λ),V (α)), and any open circular regions
C1,...,C m,B 1,...,B m ⊆ CP1. The following are equivalent.
(i) T maps (C1 × · · · ×Cm)-stable polynomials to weakly (B1 × · · · ×Bm)-stable polynomials.
(ii) One of the following holds:
(a) T maps (C1 × · · · ×Cm)-stable polynomials to nonzero (B1 × · · · ×Bm)-stable polynomials.
(b) T ≡p0 ·ψ for some weakly (B1 ×· · ·×Bm)-stable polynomial p0 ∈V (α) and some linear functional
ψ.
Proof. By appropriate SL 2(C) action, we can assume WLOG that Ck = Bk = D, the unit disc, for all
k ∈ [m].
(i) ⇒ (ii). We show that if ( a) is not the case, then ( b) must hold. It follows from ( i) that T maps
D
m
-stable polynomials to (possibly identically zero) Dm-stable polynomials. So, if ( a) is not the case, we
have that T (p) ≡ 0 for some D
m
-stable polynomial p ∈V (λ).
The rest of the argument is essentially the proof of necessity foun d in [ BB09a] for Theorem 1.1. Since
the set of nonzero D
m
-stable polynomials is open in V (λ), there is some ball B(p) ⊂V (λ) centered at p such
that B(p) contains only D
m
-stable polynomials. So, T [B(p)] is an open set in the image of T containing 0
and otherwise consisting of Dm-stable polynomials. Therefore, the image of T is a vector space consisting
22
of Dm-stable polynomials. Lemma 4.12 (and appropriate SL 2(C) action) then implies the image of T is of
dimension ≤ 1, and (b) follows.
(ii) ⇒ (i). If ( b) holds, then ( i) is immediate. Otherwise, ﬁx p ∈V (λ) such that p is Dm-stable. For all
n ∈ N, deﬁne:
pn :=p((1 −n−1)x1,y 1, (1 −n−1)x2,y 2,..., (1 −n−1)xm,y m)
So, pn is D
m
-stable for all n, and lim n→∞pn = p coeﬃcient-wise. By ( ii), T (pn) is Dm-stable for all n,
and by continuity, T (p) = lim n→∞T (pn). Hurwitz’s theorem then implies T (p) is either identically zero or
Dm-stable.
This lemma then yields the following corollaries to Theorem 6.2. Applying the necessary maps to convert
Symb to SymbBB as discussed above, these results give precisely the Borcea-Br¨ and´ en characterization proven
in Theorem 1.1 and more generally in Theorem 6.3 of [ BB09a]. In particular, Corollary 6.12 can be seen as
a uniﬁcation of the complex characterization results of [ BB09a].
Corollary 6.12. Fix λ,α ∈ Nm
0 , a linear operator T ∈ Hom(V (λ),V (α)), and any open circular regions
C1,...,C m. The following are equivalent.
(i) T preserves weak (C1 × · · · ×Cm)-stability.
(ii) One of the following holds:
(a) Symb(T ) is (C1
c
× · · · ×Cm
c
) × (C1 × · · · ×Cm)-stable.
(b) T ≡p0 ·ψ for some weakly (C1 ×· · ·×Cm)-stable polynomial p0 ∈V (α) and some linear functional
ψ.
Proof. The result follows from the Lemma 6.11 and Theorem 6.2 applied to an operator T which maps
(C1 × · · · ×Cm)-stable polynomials to nonzero ( C1 × · · · ×Cm)-stable polynomials.
Corollary 6.13. Fix λ,α ∈ Nm
0 and a linear operator T ∈ Hom(V (λ),V (α)). T preserves weak stability iﬀ
one of the following holds:
(a) Symb(T ) is (Hm
− × Hm
+ )-stable.
(b) T ≡p0 ·ψ for some weakly stable polynomial p0 ∈V (α) and some linear functional ψ.
Notice that our naive guess at strong stability results which emulate the Borcea-Br¨ and´ en characterization
(Corollaries 6.9 and 6.10) was incorrect. We actually needed to consider closed circular stability regions Ck,
so that their complements in CP1 would be open (i.e., to ensure Grace pair disjointness, which is require d
to apply Theorem 6.2). We see this play out in condition ( ii)(a) of Corollary 6.12.
