---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-028-74-ray-and-interval-stability
section_title: "Ray and interval stability"
section_number: 7.4
pages: 30-34
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
We now apply the above results to projectively convex regions of the form H+ ∪J c, where
J ⊂R is some connected set. From this, we obtain a classiﬁcation of operators which both
preserve strong J-rootedness and weak real-rootedness (a polynomial p ∈V (n) is J-rooted
if all its roots lie in J). This of course does not completely solve the open problem of providing
a classiﬁcation of interval- and ray-stability preserving operators (see, e.g., [3]). However, it
does seem to be the natural corollary obtained by applying proof methods similar to that of
[1].
That said, we now proceed to prove the main result of this subsection, Theorem 7.8. We
ﬁrst start with a short-hand deﬁnition in order to simplify the proof.
Deﬁnition 7.5 Fix λ, α ∈Nm
0 and a linear operator T ∈Hom(V (λ), V (α)) such that T
restricts to a real linear operator and preserves weak real-stability. We say T is degenerate if
it satisﬁes condition (ii)(c) of Corollary 7.4.
We now prove two lemmas. The ﬁrst is straightforward, but rather interesting in its own
right.
Lemma 7.6 Fix a closed bounded interval J ⊂R and a subspace W ⊆VR(n) consisting of
weakly real-rooted polynomials. Let S ⊆W denote the subset of top-degree monic J-rooted
polynomials. There exist p, q ∈S such that p ≪q and S is the convex hull of p and q.
Proof Lemma 4.12 implies W is of dimension at most two, and so then Lemma 4.13 implies
the relation ≪is a total order on S. Applying the root ordering property of Lemma 4.13, the
closedness of S implies there are p, q ∈S such that p ≪q and p ≪r ≪q for all r ∈S.
Basic sign arguments and the fact that S is contained in the span of {p, q} then imply S is
the the convex hull of {p, q}.
⊓⊔
The second lemma is perhaps less straightforward in terms of proof, but follows from
the following intuitive idea: an open ball in some complex subspace of polynomials yields,
roughly speaking, an open ball of zeros.
Lemma 7.7 Fix n, m ∈N0 and a linear operator T ∈Hom(V (n), V (m)) which restricts
to a real linear operator and preserves weak real-rootedness. If there exist some H+-stable
p0 ∈V (n) and some (x0 : y0) ∈R such that T (p0)(x0, y0) = 0, then one of the following
holds:
A representation theoretic explanation...
1389
(a) T (p0) is real-rooted or identically zero.
(b) T (p)(x0, y0) = 0 for all p ∈V (n).
Proof Let q0,r0 ∈VR(m) be such that T (p0) = q0 + ir0. Also suppose that T (p0)̸ ≡0
and that (b) does not hold, and let p1 be such that T (p1)(x0, y0)̸ = 0. WLOG, we may also
assume p1 ∈VR(n) by considering its real or imaginary part. We will now prove that T (p0)
must be real-rooted.
First, suppose further that T (p0) has a multiple root at (x0, y0). For small ﬁxed ϵ, p0+ϵ p1
is H+-stable and so Lemma 4.10 implies T (p0 + ϵ p1) is either H+-stable or H−-stable.
Hermite-Biehler (Proposition 4.9) then implies q0 + ϵT (p1) and r0 have interlacing roots.
However,since T restrictstoareallinearoperator,itmustbethatq0 andr0 bothhaveamultiple
root at (x0, y0). The fact that q0 + ϵT (p1) has no root at (x0, y0) yields a contradiction, as
interlacing is then impossible.
Otherwise, T (p0) has a simple root at (x0, y0). Deﬁne R ∈Hom(V (n), V (1)) via
R := dn−1
φ
◦T , where φ ∈SL2(C) is such that (x0 : y0) is the pole of φ. We have that
R(p0)(x0, y0) = 0, but R(p0)̸ ≡0 since the root is simple. Further, R(p1)(x0, y0)̸ = 0, and
therefore R is a surjective continuous linear map. By the open mapping theorem, there exists
a one-real-dimensional curve 
 ⊂V (n) through p0, for which R(
) contains elements with
root in H+ on one side of p0 (call this side 
+) and elements with root in H−on the other
side (call it 
−). So by Laguerre’s theorem (Proposition 4.6), elements of T (
+) have some
roots in H+ and elements of T (
−) have some roots in H−. Since polynomials near p0 are
H+-stable, Lemma 4.10 implies elements of T (
 ∩Bϵ(p0)) are all H+-stable or H−-stable
for some small ball Bϵ(p0) about p0. So elements of T (
+ ∩Bϵ(p0)) are H−-stable and
elements of T (
−∩Bϵ(p0)) are H+-stable, and therefore T (p0) is real-rooted.
⊓⊔
We now prove our main result on ray- and interval-stability preserving operators. First we
state the theorem for closed bounded output intervals, as it clariﬁes the proof quite a bit. We
will then extend the result to other connected regions in R.
Theorem 7.8 Fix n, m ∈N0 and a linear operator T ∈Hom(V (n), V (m)) which restricts
to a real linear operator. Further, let I ⊆R be any interval, and let J ⊂R be any closed
bounded interval. The following are equivalent.
(i) T preserves weak real-rootedness and maps I-rooted polynomials to nonzero J-rooted
polynomials.
(ii) One of the following holds:
(a) Symb(T ) is (H−∪I) × (H+\J)-stable.
(b) Symb(T ) is (H−∪I) × (H−\J)-stable.
(c) T has image of dimension at most two, and is of the form
T : p →q · ψ1(p) + r · ψ2(p)
where q,r ∈VR(m) are top-degree monic and weakly J-rooted such that q ≪r,
and ψ1 and ψ2 are real linear functionals such that ψ1(p) · ψ2(p) ≥0 (not both
zero) holds for any I-rooted p.
Proof (i) ⇒(ii). Suppose T is nondegenerate. So, Symb(T ) is either (H−× H+)-stable or
(H−× H−)-stable by Corollary 7.4. By Lemma 7.3, either T maps H+-stable evaluation
symbols entirely to nonzero H+-stable polynomials or entirely to nonzero H−-stable poly-
nomials. If for some (z0 : w0) ∈H−we have that T [(w0x −z0y)n] has a root in R, then we
can apply the previous lemma. If condition (a) of the lemma holds, then T [(w0x −z0y)n]
1390
J. Leake
is real-rooted or identically zero. The proof of Lemma 7.3 then implies T is degenerate, a
contradiction. Otherwise condition (b) of the lemma holds, and therefore the real roots of
T [(w0x −z0y)n] must be in J. So in fact, T maps H+-stable evaluation symbols entirely
to nonzero (H+\J)-stable polynomials or entirely to nonzero (H−\J)-stable polynomials.
Finally, T maps I-rooted evaluation symbols to nonzero (H+\J)-stable and (H−\J)-stable
polynomials by assumption. The complex characterization (Theorem 6.2) then implies (a) or
(b).
Otherwise, T is degenerate and T [VR(n)] consists entirely of real-rooted polynomials.
Condition (c) follows from Lemma 7.6.
(ii) ⇒(i). By Corollary 7.4, T preserves weak real-rootedness. If (a) or (b) holds, then the
complex characterization (Theorem 6.2) and the fact that T restricts to a real operator imply
T maps I-rooted polynomials to nonzero J-rooted polynomials.
Otherwise (c) holds. For any real-rooted p, let λ(p) and μ(p) denote the largest and
smallest roots of p, respectively. Since q,r are top-degree monic, every convex combination
of q and r has all its roots in the interval [μ(q), λ(r)] ⊆J. Since ψ1 · ψ2 ≥0 (not both
zero) holds for I-rooted polynomials, we have that T maps I-rooted polynomials to nonzero
J-rooted polynomials.
⊓⊔
Notice that this result immediately holds for other closed, connected regions I, J ⊂R by
the action of some appropriate φ ∈SL2(R). In fact, one can directly apply the action of φ
to conditions (ii)(a) and (ii)(b), due to the fact that our deﬁnition of the “universal” symbol
works for any projectively convex regions. The only signiﬁcant change comes when applying
φ to condition (ii)(c). Further, the only issue with (ii)(c) as it is written now is the requirement
that p1 and p2 be top-degree monic polynomials. Having zeros at inﬁnity, for instance, means
that a polynomial cannot ever be top-degree monic (as the leading homogeneous coefﬁcient is
0). There are ways to rewrite (ii)(c) that avoids this problem, but it is probably more intuitive
to state the result as above and apply φ ∈SL2(R).
Additionally, the result holds for open and half-open bounded intervals J ⊂R, with a bit
of tweaking to condition (ii)(c). (Again, the universality of the symbol means that (ii)(a) and
(ii)(b) remain unchanged.) We state this in the following, where the action of φ ∈SL2(R)
can be used to obtain similar results regarding open and half-open connected regions in R.
Corollary 7.9 The previous theorem holds when J ⊂R is an open (or half-open) bounded
interval, given the following alterations to condition (ii)(c): if the image of T is of dimension
exactly two, then p1, p2 ∈VR(m) are top-degree monic J-rooted polynomials such that the
largest root of p1 and the smallest root of p2 are in J (for p1 ≪p2), and ψ1̸ = 0 (resp.
ψ2̸ = 0) whenever p2 (resp. p1) is not J-rooted.
Proof The condition that the largest root of p1 and the smallest root of p2 are in J (and the
fact that p1 ≪p2) implies that α p1 + β p2 is J-rooted for all α, β > 0. Applying Lemma
7.6 to J completes the proof.
⊓⊔
We now give a few examples. The ﬁrst demonstrates the necessity of the premise that T
preserves weak real-rootedness.
Example 7.10 Consider the operator Tn : V (n) →V (n) deﬁned via:
Tn : xk yn−k →Hmgn[x(x −1)(x −2) · · · (x −k + 1)]
By Proposition 7.31 in [7], Tn preserves positive-rootedness for all n. However, T2 does not
preserve real-rootedness, for example. In particular:
T2(x2 + 2xy + y2) = x(x −y) + 2xy + y2 = x2 + xy + y2
A representation theoretic explanation...
1391
We now compute the symbol of T2:
Symb(T2) = T2[(xw −zy)2] = x(x −y)w2 −2xzyw + z2y2 = Hmg(2,2)[(x −z)2 −x]
Notice that for x = −1, we have that (−1 −z)2 + 1 is not real rooted. Therefore, Symb(T2)
is neither (H−∪(0, ∞)) × (H+\(0, ∞))-stable nor (H−∪(0, ∞)) × (H−\(0, ∞))-stable
when the variables are ordered (z, w), (x, y). That is, the operator T2 does not contradict the
previous theorem.
In the second example, we demonstrate root preservation properties of f (∂x) for real-
rooted f . These are standard results of the classical theory: see, e.g., Corollary 5.4.1 in
[15].
Example 7.11 For any real-rooted f ∈C[x], consider the operator D f ∈Hom(V (n), V (n))
deﬁned via D f : g →f (y∂x)g (i.e., the homogenized version of f (∂x)). To determine
properties of this operator, we ﬁrst write:
f (y∂x) = c0
m

j=1
(y∂x −α j)
Here, the α j ∈R are the roots of f . Next, we compute the symbol of (y∂x −α j) ∈
Hom(V (n), V (n)) for j ∈[m]:
Symb(y∂x −α j) = (y∂x −α j)(zy −xw)n
= −(α j(zy −xw) + nwy)(zy −xw)n−1
= Hmg(n,n)

−(α j(z −x) + n)(z −x)n−1

We now have three cases, depending on the sign ofα j. If α j > 0, we have thatSymb(y∂x−α j)
is both (H−∪[a, ∞]) × (H+\[a, ∞])-stable and (H−∪[−∞, a]) × (H+\[−∞, a + n
α j ])-
stable for any a ∈R. (As usual, we order the variables (z, w), (x, y).) Using Theorem 7.8
and the discussion following the proof, this implies (y∂x −α j) preserves [a, ∞]-rootedness
and maps [−∞, a]-rooted polynomials to [−∞, a +
n
α j ]-rooted polynomials. So, if the
(non-inﬁnite) roots of g are contained in the interval [b, c], then the (non-inﬁnite) roots of
(y∂x −α j)g are contained in the interval [b, c + n
α j ].
If α j < 0, we have that Symb(y∂x −α j) is both (H−∪[a, ∞])×(H+\[a+ n
α j , ∞])-stable
and (H−∪[−∞, a])×(H+\[−∞, a])-stable for any a ∈R. As above, this implies (y∂x −α j)
preserves [−∞, a]-rootedness and maps [a, ∞]-rooted polynomials to [a + n
α j , ∞]-rooted
polynomials. So, if the (non-inﬁnite) roots of g are contained in the interval [b, c], then the
(non-inﬁnite) roots of (y∂x −α j)g are contained in the interval [b + n
α j , c].
Finally for α j = 0, the operator (y∂x −α j) = y∂x weakly preserves any interval in
which the (non-inﬁnite) roots reside. The main difference for this case is that y∂x only
preserves weak real-rootedness. Combining these three cases, we are lead to the following
root preservation property of f (∂x) : Cn[x] →Cn[x]. Let α+
j and α−
j be the positive and
negative roots of f , respectively. We then have the following, which refers to non-inﬁnite
roots:
f (∂x) : [b, c]-rooted →
⎡
⎣b +

j
n
α−
j
, c +

j
n
α+
j
⎤
⎦-rooted
1392
J. Leake
If f has zeros at 0, then f (∂x) may map some nonzero [b, c]-rooted polynomials to 0.
Otherwise, f (∂x) is invertible on Cn[x].
