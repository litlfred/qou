---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-019-74-ray-and-interval-stability
section_title: "Ray and Interval Stability"
section_number: 7.4
pages: 26-31
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
We now apply the above results to projectively convex regions of th e form H+ ∪J c, where J ⊂ R is some
connected set. From this, we obtain a classiﬁcation of operators w hich both preserve strong J-rootedness
and weak real-rootedness (a polynomial p ∈ V (n) is J-rooted if all its roots lie in J). This of course does
not completely solve the open problem of providing a classiﬁcation of in terval- and ray-stability preserving
operators (see, e.g., [ BB09c]). However, it does seem to be the natural corollary obtained by ap plying proof
methods similar to that of [ BB09a].
That said, we now proceed to prove the main result of this subsectio n, Theorem 7.8. We ﬁrst start with
a short-hand deﬁnition in order to simplify the proof.
Deﬁnition 7.5. Fix λ,α ∈ Nm
0 and a linear operator T ∈ Hom(V (λ),V (α)) such that T restricts to a real
linear operator and preserves weak real-stability. We say T is degenerate if it satisﬁes condition ( ii)(c) of
Corollary 7.4.
We now prove two lemmas. The ﬁrst is straightforward, but rather interesting in its own right.
Lemma 7.6. Fix a closed bounded interval J ⊂ R and a subspace W ⊆VR(n) consisting of weakly real-rooted
polynomials. Let S ⊆ W denote the subset of top-degree monic J-rooted polynomials. There exist p,q ∈ S
such that p ≪q and S is the convex hull of p and q.
Proof. Lemma 4.12 implies W is of dimension at most two, and so then Lemma 4.13 implies the relation ≪
is a total order on S. Applying the root ordering property of Lemma 4.13, the closedness of S implies there
are p,q ∈ S such that p ≪ q and p ≪ r ≪ q for all r ∈ S. Basic sign arguments and the fact that S is
contained in the span of {p,q } then imply S is the the convex hull of {p,q }.
The second lemma is perhaps less straightforward in terms of proof , but follows from the following
intuitive idea: an open ball in some complex subspace of polynomials yield s, roughly speaking, an open ball
of zeros.
26
Lemma 7.7. Fix n,m ∈ N0 and a linear operator T ∈ Hom(V (n),V (m)) which restricts to a real linear
operator and preserves weak real-rootedness. If there exis t some H+-stablep0 ∈V (n) and some (x0 :y0) ∈ R
such that T (p0)(x0,y 0) = 0 , then one of the following holds:
(a) T (p0) is real-rooted or identically zero.
(b) T (p)(x0,y 0) = 0 for all p ∈V (n).
Proof. Letq0,r 0 ∈VR(m) be such that T (p0) = q0 +ir0. Also suppose that T (p0) ⁄≡0 and that ( b) does not
hold, and let p1 be such that T (p1)(x0,y 0) ⁄= 0. WLOG, we may also assume p1 ∈VR(n) by considering its
real or imaginary part. We will now prove that T (p0) must be real-rooted.
First, suppose further that T (p0) has a multiple root at ( x0,y 0). For small ﬁxed ǫ,p0 +ǫp1 is H+-stable
and so Lemma 4.10 impliesT (p0 +ǫp1) is either H+-stable or H−-stable. Hermite-Biehler (Proposition 4.9)
then implies q0 +ǫT (p1) and r0 have interlacing roots. However, since T restricts to a real linear operator,
it must be that q0 and r0 both have a multiple root at ( x0,y 0). The fact that q0 +ǫT (p1) has no root at
(x0,y 0) yields a contradiction, as interlacing is then impossible.
Otherwise, T (p0) has a simple root at ( x0,y 0). Deﬁne R ∈ Hom(V (n),V (1)) via R := dn−1
φ ◦T , where
φ ∈ SL2(C) is such that ( x0 : y0) is the pole of φ. We have that R(p0)(x0,y 0) = 0, but R(p0) ⁄≡0 since
the root is simple. Further, R(p1)(x0,y 0) ⁄= 0, and therefore R is a surjective continuous linear map. By
the open mapping theorem, there exists a one-real-dimensional cu rve Γ ⊂V (n) through p0, for which R(Γ)
contains elements with root in H+ on one side of p0 (call this side Γ +) and elements with root in H− on
the other side (call it Γ −). So by Laguerre’s theorem (Proposition 4.6), elements of T (Γ +) have some roots
in H+ and elements of T (Γ −) have some roots in H−. Since polynomials near p0 are H+-stable, Lemma
4.10 implies elements of T (Γ ∩Bǫ(p0)) are all H+-stable or H−-stable for some small ball Bǫ(p0) about p0.
So elements of T (Γ + ∩Bǫ(p0)) are H−-stable and elements of T (Γ − ∩Bǫ(p0)) are H+-stable, and therefore
T (p0) is real-rooted.
We now prove our main result on ray- and interval-stability preservin g operators. First we state the
theorem for closed bounded output intervals, as it clariﬁes the pro of quite a bit. We will then extend the
result to other connected regions in R.
Theorem 7.8. Fix n,m ∈ N0 and a linear operator T ∈ Hom(V (n),V (m)) which restricts to a real linear
operator. Further, let I ⊆ R be any interval, and let J ⊂ R be any closed bounded interval. The following
are equivalent.
(i) T preserves weak real-rootedness and maps I-rooted polynomials to nonzero J-rooted polynomials.
(ii) One of the following holds:
(a) Symb(T ) is (H− ∪I) × (H+ \J)-stable.
(b) Symb(T ) is (H− ∪I) × (H− \J)-stable.
(c) T has image of dimension at most two, and is of the form
T :p ↦→q ·ψ1(p) +r ·ψ2(p)
whereq,r ∈VR(m) are top-degree monic and weakly J-rooted such that q ≪r, and ψ1 and ψ2 are
real linear functionals such that ψ1(p) ·ψ2(p) ≥ 0 (not both zero) holds for any I-rootedp.
Proof. (i) ⇒ (ii). Suppose T is nondegenerate. So, Symb( T ) is either ( H− × H+)-stable or ( H− × H −)-
stable by Corollary 7.4. By Lemma 7.3, either T maps H+-stable evaluation symbols entirely to nonzero
H+-stable polynomials or entirely to nonzero H−-stable polynomials. If for some ( z0 : w0) ∈ H − we have
thatT [(w0x −z0y)n] has a root in R, then we can apply the previous lemma. If condition ( a) of the lemma
holds, then T [(w0x −z0y)n] is real-rooted or identically zero. The proof of Lemma 7.3 then implies T
is degenerate, a contradiction. Otherwise condition ( b) of the lemma holds, and therefore the real roots
of T [(w0x −z0y)n] must be in J. So in fact, T maps H+-stable evaluation symbols entirely to nonzero
27
(H+ \J)-stable polynomials or entirely to nonzero ( H− \J)-stable polynomials. Finally, T maps I-rooted
evaluation symbols to nonzero ( H+ \J)-stable and ( H− \J)-stable polynomials by assumption. The complex
characterization (Theorem 6.2) then implies ( a) or (b).
Otherwise, T is degenerate and T [VR(n)] consists entirely of real-rooted polynomials. Condition ( c)
follows from Lemma 7.6.
(ii) ⇒ (i). By Corollary 7.4, T preserves weak real-rootedness. If ( a) or ( b) holds, then the complex
characterization (Theorem 6.2) and the fact that T restricts to a real operator imply T maps I-rooted
polynomials to nonzero J-rooted polynomials.
Otherwise (c) holds. For any real-rooted p, let λ(p) and µ(p) denote the largest and smallest roots of p,
respectively. Since q,r are top-degree monic, every convex combination of q and r has all its roots in the
interval [µ(q),λ (r)] ⊆J. Since ψ1 ·ψ2 ≥ 0 (not both zero) holds for I-rooted polynomials, we have that T
maps I-rooted polynomials to nonzero J-rooted polynomials.
Notice that this result immediately holds for other closed, connecte d regions I,J ⊂ R by the action of
some appropriate φ ∈ SL2(R). In fact, one can directly apply the action of φ to conditions (ii)(a) and (ii)(b),
due to the fact that our deﬁnition of the “universal” symbol works for any projectively convex regions. The
only signiﬁcant change comes when applying φ to condition (ii)(c). Further, the only issue with ( ii)(c) as it is
written now is the requirement that p1 andp2 be top-degree monic polynomials. Having zeros at inﬁnity, for
instance, means that a polynomial cannot ever be top-degree mon ic (as the leading homogeneous coeﬃcient
is 0). There are ways to rewrite ( ii)(c) that avoids this problem, but it is probably more intuitive to state
the result as above and apply φ ∈ SL2(R).
Additionally, the result holds for open and half-open bounded interv alsJ ⊂ R, with a bit of tweaking to
condition (ii)(c). (Again, the universality of the symbol means that ( ii)(a) and (ii)(b) remain unchanged.)
We state this in the following, where the action of φ ∈ SL2(R) can be used to obtain similar results regarding
open and half-open connected regions in R.
Corollary 7.9. The previous theorem holds when J ⊂ R is an open (or half-open) bounded interval, given the
following alterations to condition (ii)(c): if the image of T is of dimension exactly two, then p1,p 2 ∈VR(m)
are top-degree monic J-rooted polynomials such that the largest root of p1 and the smallest root of p2 are in
J (for p1 ≪p2), and ψ1 ⁄= 0 (resp. ψ2 ⁄= 0) whenever p2 (resp. p1) is not J-rooted.
Proof. The condition that the largest root of p1 and the smallest root of p2 are in J (and the fact that
p1 ≪ p2) implies that αp1 +βp2 is J-rooted for all α,β > 0. Applying Lemma 7.6 to J completes the
proof.
We now give a few examples. The ﬁrst demonstrates the necessity o f the premise that T preserves weak
real-rootedness.
Example 7.10. Consider the operator Tn :V (n) →V (n) deﬁned via:
Tn :xkyn−k ↦→Hmgn[x(x − 1)(x − 2) · · ·(x −k + 1)]
By Proposition 7.31 in [ Fis06], Tn preserves positive-rootedness for all n. However, T2 does not preserve
real-rootedness, for example. In particular:
T2(x2 + 2xy +y2) = x(x −y) + 2xy +y2 =x2 +xy +y2
We now compute the symbol of T2:
Symb(T2) = T2[(xw −zy)2] = x(x −y)w2 − 2xzyw +z2y2 = Hmg (2,2)[(x −z)2 −x]
Notice that for x = −1, we have that ( −1 −z)2 + 1 is not real rooted. Therefore, Symb( T2) is neither
(H− ∪ (0, ∞)) × (H+ \ (0, ∞))-stable nor ( H− ∪ (0, ∞)) × (H− \ (0, ∞))-stable when the variables are ordered
(z,w ), (x,y ). That is, the operator T2 does not contradict the previous theorem.
28
In the second example, we demonstrate root preservation prope rties of f (∂x) for real-rooted f . These
are standard results of the classical theory: see, e.g., Corollary 5 .4.1 in [ RS02].
Example 7.11. For any real-rooted f ∈ C[x], consider the operator Df ∈ Hom(V (n),V (n)) deﬁned via
Df :g ↦→f (y∂x)g (i.e., the homogenized version of f (∂x)). To determine properties of this operator, we ﬁrst
write:
f (y∂x) = c0
m∏
j=1
(y∂x −αj)
Here, the αj ∈ R are the roots of f . Next, we compute the symbol of ( y∂x −αj) ∈ Hom(V (n),V (n)) for
j ∈ [m]:
Symb(y∂x −αj) = (y∂x −αj)(zy −xw)n
= −(αj(zy −xw) +nwy)(zy −xw)n−1
= Hmg (n,n)
[
−(αj(z −x) +n)(z −x)n−1]
We now have three cases, depending on the sign of αj. If αj > 0, we have that Symb( y∂x −αj) is both
(H− ∪ [a, ∞]) × (H+ \ [a, ∞])-stable and ( H− ∪ [−∞,a ]) × (H+ \ [−∞,a + n
αj
])-stable for any a ∈ R. (As
usual, we order the variables ( z,w ), (x,y ).) Using Theorem 7.8 and the discussion following the proof, this
implies (y∂x −αj) preserves [a, ∞]-rootedness and maps [ −∞,a ]-rooted polynomials to [ −∞,a + n
αj
]-rooted
polynomials. So, if the (non-inﬁnite) roots of g are contained in the interval [ b,c ], then the (non-inﬁnite)
roots of (y∂x −αj )g are contained in the interval [ b,c + n
αj
].
If αj < 0, we have that Symb( y∂x −αj) is both ( H− ∪ [a, ∞]) × (H+ \ [a + n
αj
, ∞])-stable and ( H− ∪
[−∞,a ])×(H+\[−∞,a ])-stable for anya ∈ R. As above, this implies ( y∂x −αj) preserves [−∞,a ]-rootedness
and maps [ a, ∞]-rooted polynomials to [ a + n
αj
, ∞]-rooted polynomials. So, if the (non-inﬁnite) roots of g
are contained in the interval [ b,c ], then the (non-inﬁnite) roots of ( y∂x −αj)g are contained in the interval
[b + n
αj
,c ].
Finally forαj = 0, the operator (y∂x −αj) = y∂x weakly preserves any interval in which the (non-inﬁnite)
roots reside. The main diﬀerence for this case is that y∂x only preserves weak real-rootedness. Combining
these three cases, we are lead to the following root preservation p roperty of f (∂x) : Cn[x] → Cn[x]. Let α+
j
and α−
j be the positive and negative roots of f , respectively. We then have the following, which refers to
non-inﬁnite roots:
f (∂x) : [b,c ]-rooted →

b +
∑
j
n
α−
j
,c +
∑
j
n
α+
j

 -rooted
If f has zeros at 0, then f (∂x) may map some nonzero [ b,c ]-rooted polynomials to 0. Otherwise, f (∂x) is
invertible on Cn[x].
Acknowledgements
We would like to thank Nick Ryder for many graduate school convers ations on stable polynomials and linear
stability preservers. We would also like to thank an anonymous refer ee for a thorough reading of this paper
and many helpful comments.
References
[BB09a] Julius Borcea and Petter Br¨ and´ en, The Lee-Yang and P´ olya-Schur programs. I. Linear operator s
preserving stability , Inventiones Mathematicae 177 (2009), no. 3, 541–569.
29
[BB09b] , The Lee-Yang and P´ olya-Schur programs. II. Theory of stable polynomials and applications,
Communications on Pure and Applied Mathematics 62 (2009), no. 12, 1595–1631.
[BB09c] , P´ olya-Schur master theorems for circular domains and thei r boundaries, Annals of Math-
ematics (2009), 465–492.
[BCF07] Joseph P Brennan, Jaydeep V Chipalkatti, and Robert M Fos sum, Apolarity and covariant forms ,
Illinois Journal of Mathematics 51 (2007), no. 1, 21–27.
[ER93] Richard Ehrenborg and Gian-Carlo Rota, Apolarity and canonical forms for homogeneous polyno-
mials, European Journal of Combinatorics 14 (1993), no. 3, 157–181.
[FH13] William Fulton and Joe Harris, Representation theory: A ﬁrst course , vol. 129, Springer Science &
Business Media, 2013.
[Fis06] Steve Fisk, Polynomials, roots, and interlacing , arXiv preprint math/0612833 (2006).
[Gra02] John H Grace, The zeros of a polynomial , Proc. Cambridge Philos. Soc, vol. 11, 1902, pp. 352–357.
[GY03] John Hilton Grace and Alfred Young, The algebra of invariants , Chelsea Pub. Co., 1903.
[Hum12] James Humphreys, Introduction to Lie algebras and representation theory , vol. 9, Springer Science
& Business Media, 2012.
[Kow14] Emmanuel Kowalski, An introduction to the representation theory of groups , vol. 155, American
Mathematical Society, 2014.
[Mel15] Eugeny Melamud, Linear operators on polynomials preserving roots in open ci rcular domains ,
Proceedings of the American Mathematical Society 143 (2015), no. 12, 5213–5218.
[Olv99] Peter J Olver, Classical invariant theory , vol. 44, Cambridge University Press, 1999.
[PS14] G P´ olya and J Schur, ¨Uber zwei arten von faktorenfolgen in der theorie der algebr aischen gleichun-
gen., Journal f¨ ur die Reine und Angewandte Mathematik 144 (1914), 89–113.
[RS02] Qazi Ibadur Rahman and Gerhard Schmeisser, Analytic theory of polynomials , no. 26, Oxford
University Press, 2002.
[Wag11] David Wagner, Multivariate stable polynomials: Theory and applications , Bulletin of the American
Mathematical Society 48 (2011), no. 1, 53–84.
[Zah76] Neyamat Zaheer, On polar relations of abstract homogeneous polynomials , Transactions of the
American Mathematical Society 218 (1976), 115–131.
[Zer60] Spiros P Zervos, Aspects modernes de la localisation des z´ eros des polynˆ omes d’une variable, Annales
scientiﬁques de l’ ´Ecole Normale Sup´ erieure, vol. 77, Elsevier, 1960, pp. 303–410.
30
