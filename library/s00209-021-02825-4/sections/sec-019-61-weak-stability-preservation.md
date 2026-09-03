---
doc_id: s00209-021-02825-4
doc_title: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021"
section_id: sec-019-61-weak-stability-preservation
section_title: "Weak stability preservation"
section_number: 6.1
pages: 21-25
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
doc_brief: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021 — In 2009, Borcea and Brändén"
---
Borcea and Brändén deﬁne the following symbol:
SymbBB (T) := T[(x + z)λ]=
∑
μ≤λ
( λ
μ
)
zλ−μT(xμ)
They then obtain the following characterization of stability-preserving linear operators.
Theorem 1.1 (Borcea–Brändén) Fixλ ∈ Nm
0 and any linear operator T: Cλ[x1,..., xm]→
C[x1,..., xm]. The following are equivalent.
(i) T maps Hm
+-stable polynomials to weakly Hm
+-stable polynomials.
(ii) One of the following holds:
(a) Symb BB (T) is H2m
+ -stable.
(b) T has image of dimension at most one, and is of the form
T : p ↦→ q · ψ( p)
where q ∈ C[x1,..., xm] is Hm
+-stable, and ψ is some linear functional.
Using our terminology, this is a characterization of weak stability-preserving linear oper-
ators. This fantastic result perhaps has but one unfortunate piece: the degeneracy condition
(ii)(b). Its necessity is demonstrated in the following.
Example 6.1 Deﬁne T : Cn[x]→ C[x] via:
T :
n∑
k=0
( n
k
)
ak xk ↦→ (an + an−2)xn
This operator obviously preserves weak H+-stability. We then have that Symb BB (T) =
(z2 + 1)xn , which is not H2
+-stable.
As we will see below, this condition can be removed once we only consider strong stability-
preserving operators. So then, maybe strong stability is the more natural notion? However
“natural” it is, unfortunately it leaves out operators one might wish to consider. The most
fundamental of such operators is the derivative operator ∂x . While ∂x preserves strong H+-
stability, it only preserves weak H+-stability. Speciﬁcally, 1 ∈ Cn[x] is H+-stable (all its
roots are at ∞), but ∂x 1 ≡ 0. With this, one obviously wants to be able to include weak
stability preserving operators in any characterization of H+-stability preserving operators.
We discuss how to use our strong stability preservation characterization to deal with operators
like ∂x in Example 6.8.
123
1380 J. Leake
6.2 Strong stability preservation
We now state one of our main characterization results, the strong stability preservation char-
acterization. We then derive the Borcea–Brändén characterization as a corollary.
Theorem 6.2 Fix λ ∈ Nm
0 , α ∈ Nl
0, a linear operator T ∈ Hom(V(λ), V(α)), any disjoint
Grace pair (C1 ×···× Cm, B1 ×···× Bm), and any sets S1,..., Sl ⊆ CP1. The following
are equivalent.
(i) T maps (C1×···× Cm)-stable polynomials to nonzero(S1×···× Sl)-stable polynomials.
(ii) T maps (C1 ×···× Cm)-stable evaluation symbols to nonzero (S1 ×···× Sl)-stable
polynomials.
(iii) Symb (T) is (B1 ×···× Bm) × (S1 ×···× Sl)-stable.
One should notice the generality of this result in terms of stability regions. First note that
any disjoint Grace pair can be considered, without altering the symbol in any way (e.g., via
conjugation by Möbius transformations). And further, the output sets that can be considered
have no restrictions whatsoever. The power of these extra features can be seen in the following
examples, which demonstrate classical results regarding polynomial convolutions in a very
symbol-oriented way.
Example 6.3 Fix p, q ∈ V(n),s ot h a t(z j : 1) are the roots in CP1 of q for j ∈[ n].S o , q
has no roots at ∞. The additive (Walsh) convolution of p and q is deﬁned via:
p ∗n
+ q := 1
n!
n∑
k=0
∂k
x p · (∂n−k
x q)(0, 1)
With this, Tq(p) := p ∗n
+ q is a linear operator in Hom (V(n), V(n)), and we have:
Symb(Tq) =
n∏
j=1
(xw − (z + z j w)y) = Hmg(n,n)
⎡
⎣
n∏
j=1
(x − (z + z j ))
⎤
⎦
Let C ⊂ CP1 be any projectively convex region, and deﬁneS := ⋃
j (C +z j).I fw eo r d e rt h e
input variables of Symb(Tq) as (z,w, x, y), it is then straightforward to show that Symb(Tq)
is C × (CP1\S)-stable. (First deal with possible (x : y) = (1 : 0) or (z : w) = (1 : 0)
cases, and then assume y = w = 1 to simplify the remaining cases.) Applying the previous
theorem, this implies Tq maps polynomials with roots in C to polynomials with roots in
S. (This is Theorem 5.3.1 in [ 15].) Picking C = H− and real-rooted q implies Tq maps
H+-stable polynomials to H+-stable polynomials. Restricting to p ∈ VR(n) then shows that
Tq preserves real-rootedness.
Example 6.4 Fix p, q ∈ V(n),s ot h a t(z j : 1) ⁄= 0 are the roots of q for j ∈[ n].S o ,q has no
roots at 0 or ∞. The multiplicative (Grace–Szeg˝o) convolution of p and q (with coefﬁcients
pk and qk , respectively) is deﬁned via:
p ∗n
× q :=
n∑
k=0
( n
k
) −1
(−1)k pkqk xk yn−k
With this, Tq(p) := p ∗n
× q is a linear operator in Hom (V(n), V(n)), and we have:
Symb(Tq) =
n∏
j=1
(xw − z j zy) = Hmg(n,n)
⎡
⎣
n∏
j=1
(x − z j z)
⎤
⎦
123
A representation theoretic explanation... 1381
Let C ⊂ CP1 be any projectively convex region, and deﬁne S := ⋃
j(z j · C).I fw eo r d e rt h e
input variables of Symb(Tq) as(z,w, x, y), it is then straightforward to show that Symb(Tq) is
C ×(CP1\S)-stable. (As above, ﬁrst deal with possible (x : y) = (1 : 0) or (z : w) = (1 : 0)
cases, and then assume y = w = 1 to simplify the remaining cases.) Applying the previous
theorem, this implies Tq maps polynomials with roots in C to polynomials with roots in S.
(This is Theorem 3.4.1d in [15].) PickingC = H−∪R+ and q with only positive roots implies
Tq maps (H+ ∪ R−)-stable polynomials to (H+ ∪ R−)-stable polynomials. Restricting to
p ∈ VR(n) then shows that Tq preserves positive-rootedness.
In order to prove the above theorem, we need an operator-theoretic corollary to Grace’s
theorem. The following result is the main motivation for the symbol lemma (Lemma3.7), and
demonstrates just how closely Grace’s theorem relates to stability properties of linear opera-
tors. Further, it gives a slightly stronger result in one direction of the above characterization,
as Grace pair disjointness is not a required premise.
Proposition 6.5 Fix λ ∈ Nm
0 , α ∈ Nl
0, a linear operator T ∈ Hom(V(λ), V(α)), any Grace
pair (C1 ×···× Cm, B1 ×···× Bm), and any sets S 1,..., Sl ⊆ CP1.I f Symb(T) is
(B1 ×···× Bm) × (S1 ×···× Sl)-stable, then T maps (C1 ×···× Cm)-stable polynomials
to nonzero (S1 ×···× Sl)-stable polynomials.
Proof Fix any (C1 ×···× Cm)-stable q ∈ V(λ) and any (c, d) = (c1, d1,..., cl, dl) ∈ C2l
such that (cj : dj ) ∈ Sj for all j ∈[ l].L e t kλ,α := (−1)α(λ!)2(α!)2. The evaluation
symbol lemma (Lemma 5.10) and the symbol lemma (Lemma 3.7) then give us the following
expression of T(q) evaluated at (c, d) = (c1, d1,..., cl, dl):
kλ,α T(q)(c, d) = kλ,0 Dα(
T(q) ⊗ (dx − cy)α)
= Dλ⊔α(
Symb(T) ⊗ q · (dx − cy)α)
= k0,α Dλ(
Symb(T)(z,w, c, d) ⊗ q(z,w)
)
In the last expression above, Dλ acts on the variables (z,w) = (z1,w 1,..., zm,w m).S i n c e
r(z,w) := Symb(T)(z,w, c, d) is (B1 ×···× Bm)-stable and q(z,w) is (C1 ×···× Cm)-
stable, we have that the last expression above is nonzero by deﬁnition of Grace pair (Deﬁnition
5.2). This implies T(q) is (S1 ×···× Sl)-stable. ⊓⊔
With this, we now give the proof of Theorem 6.2.
Proof of Theorem 6.2 The statement of this result, as well as its proof, is quite similar to that
of the evaluation symbol version of Grace’s theorem given in Corollary 5.11. We explicitly
give the proof anyway, as it is rather short and straightforward.
(i) ⇒ (ii). Immediate.
(ii) ⇒ (iii). Fix (a, b) = (a1, b1,..., am, bm) ∈ C2m such that (a j : bj ) ∈ Bj for all
j ∈[ m],a n dﬁ x (c, d) = (c1, d1,..., cl, dl) ∈ C2l such that (cj : dj ) ∈ Sj for all j ∈[ l].
Let kλ,α := (−1)α(λ!)2(α!)2.S i n c eBj and C j are disjoint, we have that (a j : bj)/∈ C j for
all j, and therefore Symb (ev(a,b)) = (bx − ay)λ ∈ V(λ) is an evaluation symbol which is
(C1 ×···× Cm)-stable. Using the evaluation symbol lemma (Lemma 5.10) and the symbol
lemma (Lemma 3.7), we compute:
(−1)λkλ,α Symb(T)(a, b, c, d) = Dλ⊔α(Symb(T)
⊗(bx − ay)λ(dx − cy)α) = kλ,α T[(bx − ay)λ](c, d)
By (ii) the last expression is nonzero, and thus Symb (T)(a, b, c, d) ⁄= 0. This implies
Symb(T) is (B1 ×···× Bm) × (S1 ×···× Sl)-stable.
123
1382 J. Leake
(iii) ⇒ (i). Proposition 6.5 above. ⊓⊔
As mentioned above, the previous proposition gives a slightly stronger result in the (symbol
stability ⇒ operator stability) direction. Using it, we revisit the additive and multiplicative
convolutions with a more algebraic/symbolic mentality.
Example 6.6 By Deﬁnition 3.6, the Symb map gives a bijection between certain spaces of
linear operators and polynomials. So, we can uniquely deﬁne a linear operator by giving
its symbol. Using this idea, we specify T ∈ Hom(V(n, n), V(n)) by deﬁning its symbol in
V(n, n, n) with variables (z,w) ,(t, s), (x, y) as follows:
Symb(T) := Hmg(n,n,n)
[
(x − (z + t))n]
= (xws − (zs + tw)y)n
Now, let us consider the additive convolution∗n
+ as an element of Hom(V(n, n), V(n)) in the
following way. SinceV(n, n) ∼= V(n)⊠ V(n),w ed e ﬁ n e∗n
+ on elements p⊠ q ∈ V(n)⊠ V(n)
via ∗n
+(p ⊠ q) := p ∗n
+ q and extend linearly. We then compute Symb(∗n
+) as follows:
Symb(∗n
+) =∗ n
+
[
(zy − xw)n ⊠ (ty − xs)n]
= (xws − (zs + tw)y)n
That is, ∗n
+ is the operator that has our desired symbol. Fixing any a, b, c, d ∈ R such that
a < b and c < d,w ed e ﬁ n et h es e t sC1 := H+\(a, b), C2 := H+\(c, d), B1 := H− ∪[a, b],
B2 := H− ∪[ c, d]),a n d S := H+\[a + c, b + d]. Proposition 6.5 then implies p ∗n
+ q has
all its roots in [a + c, b + d] whenever p, q ∈ VR(n) have all their roots in (a, b) and (c, d),
respectively. For real-rooted p, q of degree n, this implies:
minroot(p) + minroot(q) ≤ minroot(p ∗n
+ q) ≤ maxroot(p ∗n
+ q) ≤ maxroot(p) + maxroot(q)
Notice that we actually get a bit more. For(C1×C2)-stabler := ∑
j pj ⊠q j ∈ V(n)⊠ V(n) ∼=
V(n, n),w eh a v et h a t∗n
+[r] is S-stable. That is, ∗n
+ has stability properties as an operator in
Hom(V(n, n), V(n)), not just as a convolution between two polynomials in V(n).
Example 6.7 As in the previous example, we can consider the multiplicative convolution
∗n
× as an element of Hom (V(n, n), V(n)) by deﬁning ∗n
×(p ⊠ q) := p ∗n
× q on elements
p ⊠ q ∈ V(n) ⊠ V(n) ∼= V(n, n) and extending linearly. We then compute its symbol in
V(n, n, n) with variables (z,w) ,(t, s), (x, y) as follows:
Symb(∗n
×) =∗ n
×
[
(zy − xw)n ⊠ (ty − xs)n]
= (xws − zty )n = Hmg(n,n,n)
[
(x − zt)n]
Fixing any a, b, c, d ∈ R+ such that 0 < a < b and 0 < c < d,w ed e ﬁ n et h es e t sC1, C2,
B1,a n dB2 as in the previous example. We then deﬁne S := R\[ac, bd]. Proposition 6.5 then
implies p ∗n
× q has all its real roots in [ac, bd] whenever p, q ∈ VR(n) have all their roots
in (a, b) and (c, d), respectively. (Notice that we could not apply the proposition if H+ ⊂ S
or H− ⊂ S.) Since Example 6.4 implies p ∗n
× q is positive-rooted (and hence, real-rooted)
whenever p and q are, this implies:
minroot(p) · minroot(q) ≤ minroot(p ∗n
× q) ≤ maxroot(p ∗n
× q) ≤ maxroot(p) · maxroot(q)
As in the previous example, we also obtain stability properties for ∗n
× as an operator in
Hom(V(n, n), V(n)), and not just as a polynomial convolution.
Using similar techniques, we can also circumvent the issue that arises from the fact that
∂x only preserves weak stability.
123
A representation theoretic explanation... 1383
Example 6.8 For ﬁxed n ≥ 1, consider the operator∂x ∈ Hom(V(n), V(n−1)). We compute:
Symb(∂x) = ∂x[(zy − xw)n]=− nw(zy − xw)n−1 = Hmg(n,n−1)
[
−n(z − x)n−1]
For any a, b ∈ R such that a < b, it is straightforward to see that Symb(∂x) is (C × B)-stable
for C := H− ∪ (a, b) and B := H+\(a, b), where the variables are ordered (z,w) ,(x, y).
(Notice that this does not hold when∞∈ C, due to the w factor in the symbol.) Since(C, B)
is a disjoint Grace pair, the Theorem 6.2 implies ∂x preserves strong B-stability.
With this, let f ∈ Cn[x] be a H+-stable polynomial of degree 1 ≤ m ≤ n,a n dl e t
p ∈ V(m) be its degree- m homogenization. Then p has no roots at inﬁnity, and therefore
there exists a < b such that p is
(
H+\(a, b)
)
-stable. The previous discussion implies ∂x p
is
(
H+\(a, b)
)
-stable, and in particular ∂x p is H+-stable. Since ∂x commutes with homog-
enization, this also implies ∂x f is H+-stable.
Other issues related to weak stability preservation can be dealt with in a similar way, by
considering stability regions with small intervals in R about ∞ attached. More generally
though, the Borcea–Brändén characterization ends up being a corollary of Theorem 6.2,
which we discuss and demonstrate now.
