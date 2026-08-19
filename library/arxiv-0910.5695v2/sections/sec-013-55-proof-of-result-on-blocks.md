---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-013-55-proof-of-result-on-blocks
section_title: "Proof of result on blocks"
section_number: 5.5
pages: 34-37
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
To start, given a Young diagramλ we will describe how Liftt(L(λ)) decomposes as a
sum of indecomposable objects in Re p(ST ;K) (see Lemma 5.20). This description,
along with Lemma 5.4 will be used to prove Theorem 5.3. We begin with the
following proposition.
Proposition 5.19. Supposeλ,λ (1),...,λ (m) are Young diagrams with the property
that Liftt(L(λ)) = L(λ(1))⊕···⊕ L(λ(m)) in Rep(ST ;K). Then λ(i) t
∼ λ for all
i = 1,...,m .
Proof. Fix a positive integer k such that λ(i)
k = λk = 0 for all i = 1,...,m . By
Lemma 5.4(2), it suﬃces to show ξλ(i)(t)
r,k = ξλ(t)
r,k for all r > 0 and i = 1,...,m .
Fix a positive integer r, set n = |λ|, e = eλ and let ε ∈ KPn(T ) be a lift of
e. Let A(x)∈ K[x] be the minimal monic polynomial with A(ωr
n(T ))ε = 0. If
ε =ε1 +··· +εm′ is an orthogonal decomposition of ε into primitive idempotents,
then m′ = m and (after reordering) L(λ(i)) = ([n],εi) for all i = 1,...,m . Hence
A(x) is the product of linear terms of the formx−ξλ(i)(T )
r,k (see Proposition 4.9). Let
B(x),C (x)∈K[x] be the unique monic polynomials with A =BC such that B(x)
(resp. C(x)) is the product of linear terms of the formx−ξλ(i)(T )
r,k withξλ(i)(t)
r,k equal
to (resp. not equal to) ξλ(t)
r,k . Suppose for a contradiction that C(x)⁄= 1. Since B(x)
and C(x) are relatively prime polynomials of positive degree, there exist nonzero
polynomials G(x),H (x)∈ K[x] with deg G(x) < degC(x), deg H(x) < degB(x)
and
(5.11) G(x)B(x) +H(x)C(x) = 1.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 35
LetN be the minimal integer so that all coeﬃcients of both G′(x) := (T−t)NG(x)
and H′(x) := (T−t)NH(x) lie in F [[T−t]]. Then from equation (5.11) we have
(5.12) G′(x)B(x) +H′(x)C(x) = (T−t)N.
Let b(x),c (x),g (x),h (x)∈ F [x] be the polynomials obtained by evaluating T = t
in the polynomials B(x),C (x),G′(x),H′(x) respectively. If N >0, then equation
(5.12) implies b(x) (resp. c(x)) divides h(x) (resp. g(x)). On the other hand,
degb(x) = deg B(x) > degH(x)≥ degh(x). Similarly deg c(x) > degg(x). Thus
h(x) = g(x) = 0 which contradicts the minimality of N. Hence N = 0 which
implies the coeﬃcients of H(x) =H′(x) and G(x) =G′(x) are in F [[T−t]]. Thus
evaluatingT =t, x =ωr
n(t) in equation (5.11) and multiplying by e gives
(5.13) g(ωr
n(t))b(ωr
n(t))e +h(ωr
n(t))c(ωr
n(t))e =e.
Sinceωr
n(t) is in the center of FPn(t) (Proposition 4.6(2)) and b(ωr
n(t))c(ωr
n(t))e =
0, the two summands on the left side of equation (5.13) are idempotents. As e is
assumed to be primitive, either g(ωr
n(t))b(ωr
n(t))e = 0 or h(ωr
n(t))c(ωr
n(t))e = 0.
Since G(ωr
n(T ))B(ωr
n(T ))ε and H(ωr
n(T ))C(ωr
n(T ))ε are lifts of g(ωr
n(t))b(ωr
n(t))e
and h(ωr
n(t))c(ωr
n(t))e respectively, it follows that either G(ωr
n(T ))B(ωr
n(T ))ε = 0
or H(ωr
n(T ))C(ωr
n(T ))ε = 0 (see Theorem A.2) which contradicts the minimality
of A(x). This completes the proof. □
Among other things, Proposition 5.19 implies that Lift t(L(λ)) =L(λ) whenever
λ is in a trivial
t
∼-equivalence class. The following lemma describes Lift t(L(λ)) for
arbitrary λ.
Lemma 5.20. (1) Suppose t∈ F and λ is a Young diagram which is either in
a trivial
t
∼-equivalence class or the minimal element of a nontrivial
t
∼-equivalence
class. Then Liftt(L(λ)) =L(λ).
(2) Suppose d is a nonnegative integer and B ={λ(0)⊂ λ(1)⊂···} is a non-
trivial
d
∼-equivalence class. Then Liftd(L(λ(i))) =L(λ(i))⊕L(λ(i−1)) for all i> 0.
Proof. Part (1) follows from Propositions 3.12(3) and 5.19. To prove part (2),
assume Liftd(L(λ(i))) is indecomposable. Then it follows from Proposition 3.12(3)
that Liftd(L(λ(i))) =L(λ(i)). Hence, by Proposition 3.12(2) and Proposition 3.28,
dimRep(Sd;F )L(λ(i)) = Pλ(i)(d), which is nonzero by Proposition 5.11. Therefore
F(L(λ(i))) is nonzero in Rep(Sd;F ), which is only possible ifi = 0 (see Propositions
3.25 and 5.9). Hence Lift d(L(λ(i))) is decomposable whenever i > 0. We now
proceed by induction on ≺.
For our base case, assume that B is the minimal
d
∼-equivalence class. Fix i> 0
and let ρ be as in as in Lemma 5.18(1). Since ρ is in a trivial
d
∼-equivalence class
Liftd(L(ρ)) =L(ρ) (by part (1)). Hence, by Example 3.11(1), Proposition 3.12(1),
and Lemma 5.18(1),
Liftd(L(ρ)⊗ ([1], id1)) =L(ρ)⊗ (L(2)⊕L(∅)) =L(λ(i))⊕L(λ(i−1))⊕A
in Re p(ST ;K) where A is an object with no indecomposable summands of the
form L(λ(j)). By Propositions 3.12(3) and 5.19, L(ρ)⊗ ([1], id1) must have L(λ(i))
as an indecomposable summand in Re p(Sd;F ). Moreover, since Lift d(L(λ(i))) is
decomposable, it must be the case that Lift d(L(λ(i))) =L(λ(i))⊕L(λ(i−1)).
36 JONATHAN COMES AND VICTOR OSTRIK
Now assume B is not minimal and let B′ ={ρ(0)⊂ρ(1)⊂···} be as in Lemma
5.18(2). Since B′ ⪵ B, by induction we have Lift d(L(ρ(i))) = L(ρ(i))⊕L(ρ(i−1))
whenever i > 0. Hence, by Example 3.11(1), Proposition 3.12(1) and Lemma
5.18(2),
Liftd(L(ρ(i))⊗ ([1], id1)) = ( L(ρ(i))⊕L(ρ(i−1)))⊗ (L(2)⊕L(∅))
= L(λ(i))⊕L(λ(i−1))⊕A
in Rep(ST ;K) whereA is an object with no indecomposable summands of the form
L(λ(i)). As in the base case, this implies the desired result. □
Remark 5.21. Lemma 5.20(2) implies thatPλ(i)(d) =−Pλ(i−1)(d) fori> 0 whence
Pλ(i)(d) = (−1)iPλ(0)(d). This identity was observed by Deligne, see [Del07, §7.5].
We are ready to prove the main result section 5, which we restate now.
Theorem 5.3. L(λ) and L(λ′) are in the same block of Rep(St;F ) if and only if
λ
t
∼λ′.
Proof. If L(λ) and L(λ′) are in the same block of Re p(St;F ), then Lemma 5.4
implies λ
t
∼ λ′. To prove the converse, by Corollary 5.6(1) we may assume t = d
is a nonnegative integer. Suppose {λ(0)⊂λ(1)⊂···} is a nontrivial
d
∼-equivalence
class and ﬁx i >0. By Proposition 3.12(5) dim F HomRep(Sd;F )(L(λ(i−1)),L (λ(i)))
is equal to dim K HomRep(ST ;K)(Liftd(L(λ(i−1))), Liftd(L(λ(i)))), which is nonzero
by Lemma 5.20. The result follows. □
We close this section by examining the dimensions of the Hom spaces between
indecomposable objects in Re p(St;F ).
Proposition 5.22. (1) dimF EndRep(St;F )(L(λ)) = 1 whenever λ is in a trivial
t
∼-
equivalence class. In particular, the block corresponding to a trivial
t
∼-equivalence
class is trivial.
(2) Given a nontrivial block {λ(0)⊂λ(1)⊂···} in Rep(St;F ),
dimF HomRep(St;F )(L(λ(i)),L (λ(j))) =



2 if i =j >0,
0 if|i−j|> 2,
1 otherwise.
Proof. By Lemma 5.20 and Proposition 3.12(5), it suﬃces to prove
dimK HomRep(ST ;K)(L(λ),L (λ′)) =
{ 1 if λ =λ′,
0 if λ⁄=λ′.
By Proposition 3.8 it suﬃces to consider the case whenK is algebraically closed. As
Rep(ST ;K) is semisimple (Corollary 3.17), the result follows from Schur’s lemma.
□
Corollary 5.23. Rep(St;F ) is semisimple if and only if t is not a nonnegative
integer.
Proof. This follows from Proposition 5.22(1) along with corollaries 5.6(1) and 5.9.
□
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 37
