---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-009-41-interpolating-sums-of-r-cycles
section_title: "Interpolating sums of r-cycles"
section_number: 4.1
pages: 23-26
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
Rep0(St;F ) which “interpolate” the action of the sum of all r-cycles on represen-
tations of symmetric groups. To begin, let r andd be positive integers with r≤d.
Deﬁnition 4.1. Let Ωr,d∈FSd denote the sum of all r-cycles in Sd.
Since Ωr,d is in the center of FSd, the action of Ω r,d on V⊗n
d gives an element
of EndSd(V⊗n
d ) for each integer n≥ 0. This, along with Theorem 2.6, shows the
following deﬁnition is valid.
Deﬁnition 4.2. For nonnegative integers r,n, and d with r≤ d and 2n≤ d, let
Cr
n(d) denote the unique element of FPn(d) withf(Cr
n(d))∈ EndSd(V⊗n
d ) given by
the action of Ωr,d.
The ﬁrst goal of this section is to deﬁne elements of FPn(t) for arbitrary t∈F
which agree with the deﬁnition ofCr
n(t) whent is a suﬃciently large integer. We are
able to do this because, as we will show,Cr
n(d) depends polynomially ond. The fact
24 JONATHAN COMES AND VICTOR OSTRIK
that Cr
n(d) depends polynomially on d boils down to the following combinatorial
proposition.
Proposition 4.3. Suppose n is a nonnegative integer and π ∈ Pn,n. Fix the
following notation.
• Leta denote the number of parts of π.
• Let b denote the number of parts πk of π such that j,j′ ∈ πk for some
1≤j≤n.
• Let c denote the number of connected components in the trace diagram of
π (see section 2.3).
• Supposer and d are positive integers with d≥r, and i, i′∈ [n,d ] are such
that the (i, i′)-coloring of π is perfect. Let S(π,r,d ) denote the number of
r-cycles, σ∈Sd, such that σ(ij) =i′
j for all 1≤j≤n.
Fix a positive integer r.
(1) If S(π,r,d )⁄= 0 for some integer d≥r, then S(π,r,d′)⁄= 0 for all d′≥d.
(2) If S(π,r,d ) is nonzero, then
(4.5) S(π,r,d ) = (r−a +c− 1)!
(r−a +b)!
r+b−a∏
k=1
(d−r−b +k).‖
Proof. Part (1) is clear. To prove part (2), since S(π,r,d ) does not depend on the
choice of perfect coloring of π, we may assume {ij,i′
j| j = 1,...,n } ={1,...,a }.
Forx,y∈{ 1,...,a } writex→y ifx =ij andy =i′
j for some 1≤j≤n. Generate
the weakest equivalence relation on {1,...,a } such that x and y are equivalent
whenever x→ y. Notice that the equivalence classes correspond precisely to the
connected components in the trace diagram of π. Hence there are c equivalence
classes. Now assume S(π,r,d )⁄= 0. Then the following two implications must
hold: if x→ y and x→ y′ then y = y′; if x→ y and x′→ y then x = x′. In
particular, there are exactly b equivalence classes with only one element; hence the
c−b equivalence classes with more than one element must account fora−b elements
of{1,...,a }.
Now, anr-cycle inσ∈Sd can be thought of as a cyclic arrangement ofr distinct
elements of{1,...,d }. If σ(ij) =i′
j for all 1≤j≤n, then among the elements in
{1,...,a } the cyclic arrangement corresponding to σ contains precisely the a−b
elements in equivalence classes with more than one element. Moreover, if x→y for
distinctx,y∈{ 1,...,a }, then x andy must be adjacent in the cyclic arrangement
corresponding toσ. Hence σ is determined by a cyclic arrangement of the following
r−a+c items: c−b equivalence classes with more than one element;r−a+b elements
of{a + 1,...,d }. Finally, if such a σ exists, then any choice of r−a +b elements
of{a + 1,...,d } arranged cyclically with the equivalence classes containing more
than one element determines an r-cycle in Sd which maps ij↦→i′
j. Since there are
(r−a+c−1)! cyclic arrangements ofr−a+c items, and
( d−a
r−a+b
)
diﬀerent (r−a+b)-
element subsets of{a + 1,...,d }, it follows that S(π,r,d ) = (r−a +c− 1)!
( d−a
r−a+b
)
,
which is equivalent to the desired formula. □
‖If r = a−b then the empty product
r+b−a∏
k=1
(d−r−b +k) is equal to 1, and (4.5) gives
S(π,r,d ) = (c−b− 1)!. If r<a −b orr≤a−c thenS(π,r,d ) is zero for all d, so (4.5) does not
apply.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 25
Example 4.4. Let n = 15 and
Then a = 14, b = 3, and c = 7. For d≥ 14, let i, i′∈ [n,d ] be the functions which
give the perfect ( i, i′)-coloring of π below.
For an r-cycle σ∈ Sd to satisfy σ(ij) = i′
j for j = 1,...,n , σ must ﬁx the 3 = b
numbers 3, 9, 10, and map
(4.6) 1 → 5→ 13, 2→ 14, 4→ 11, 7→ 8→ 6→ 12.
Clearly, such an r-cycle exists if and only if r≥ 11 =a−b and d≥r + 3 =r +b.
In that case, the number of such r-cycles can be counted as follows. There are
(r− 8)! = (r−a +c− 1)! ways to arrange the 4 = c−b “chains” listed in (4.6)
along with the r− 11 = r−a +b other entries within the cycle. Moreover, there
are d− 14 = d−a choices for the remaining r− 11 = r−a +b entries within the
r-cycle after the “chains” in (4.6) have been taken into account. Hence the number
of desired r-cycles is given by (r− 8)!
(d−14
r−11
)
= (r−a +c− 1)!
( d−a
r−a+b
)
which agrees
with (4.5). 2
With Proposition 4.3 in mind, we are now ready for the following deﬁnition.
Deﬁnition 4.5. Fort∈ F and integers r >0, and n≥ 0, deﬁne ωr
n(t)∈ FPn(t)
as follows. Using the basis {xπ} for FPn(t) deﬁned in (2.1), set
ωr
n(t) =
∑
π∈Pn,n
qπ,r,txπ
where, using the notation set up in Proposition 4.3,
qπ,r,t =



0, if S(π,r,d ) = 0 for all integers d> 1,
(r−a+c−1)!
(r−a+b)!
r+b−a∏
k=1
(t−r−b +k), otherwise.
Although the deﬁnition of ωr
n(t) may seem a bit complicated, for the rest of this
paper we will only be concerned with the following (less complicated) properties of
ωr
n(t).
Proposition 4.6. (1) Fix integers r >0 and n≥ 0. Whenever d is a suﬃciently
large∗∗ integer, ωr
n(d) = Cr
n(d). In other words, when d is a suﬃciently large
integer, the map f(ωr
n(d)) :V⊗n
d →V⊗n
d is given by the action of Ωr,d∈Sd.
(2) Fix t ∈ F and an integer r > 0. The morphisms ωr
n(t) : [ n] → [n]
for each nonnegative integer n form an endomorphism of the identity functor on
Rep0(St;F ). In particular, ωr
n(t) is in the center of FPn(t) for every t∈ F and
integern≥ 0.
∗∗The statement is certainly true for d≥ 2n +r, although this bound is not sharp.
26 JONATHAN COMES AND VICTOR OSTRIK
Proof. For i, i′∈ [n,d ], let π(i, i′)∈ Pn,n denote the unique partition which has
a perfect ( i, i′)-coloring. Then the action of Ω r,d on V⊗n
d maps the basis vector
vi↦→ ∑
i
′
∈[n,d]S(π(i, i′),r,d )vi
′. On the other hand, (2.2) shows that f(ωr
n(t))
maps vi↦→∑
i
′
∈[n,d]qπ(i,i
′
),r,dvi
′. By Proposition 4.3, S(π(i, i′),r,d ) =qπ(i,i
′
),r,d
for suﬃciently large d. This proves part (1).
To prove part (2), choose µ ∈ Pn,m. For an integer d > r, we know that
f(µ) : V⊗n
d → V⊗m
d commutes with the action of Ω r,d∈ Sd. Hence, by part (1),
f(ωr
m(d)µ) = f(µωr
n(d)) when d is a suﬃciently large integer. Thus, by part (2)
of Theorem 2.6, ωr
m(d)µ = µωr
n(d) when d is a suﬃciently large integer. If we set
ωr
m(t)µ =:∑
π∈Pn,maπ(t)π and µωr
n(t) =:∑
π∈Pn,ma′
π(t)π for each t∈F , then we
have shown the polynomials aπ(t) and a′
π(t) are equal when t is a suﬃciently large
integer. Hence they are always equal. □
4.2. Frobenius’ formula. This section will be devoted to studying how ωr
n(t)
interacts with indecomposable objects in Re p(St;F ). We start with the following
proposition.
Proposition 4.7. Fixt∈F along with integersr> 0 andn≥ 0. If e is a primitive
idempotent in FPn(t), then there exist ξ∈ F and a positive integer m such that
(ωr
n(t)−ξ)me = 0.
Proof. Let ¯F denote the algebraic closure of F and write ω := ωr
n(t). Let a(x)
(resp. a′(x)) denote the monic polynomial of minimal degree in F [x] (resp. ¯F [x])
with a(ω)e (resp. a′(ω)e) equal to zero.†† First we will show that a(x) is a power
of an irreducible polynomial in F [x]. To do so, suppose b(x) and c(x) are rela-
tively prime monic polynomials in F [x] with a(x) = b(x)c(x). Then there exist
polynomials g(x),h (x)∈ F [x] with deg g(x) < degc(x), degh(x) < degb(x), and
g(x)b(x) +h(x)c(x) = 1. Hence g(ω)b(ω)e +h(ω)c(ω)e =e is a decomposition of e
into orthogonal idempotents (here we are using the fact that ω is in the center of
FPn(t), see Proposition 4.6(2)). Since e is primitive, this implies g(ω)b(ω)e = 0 or
h(ω)c(ω)e = 0. The minimality of a(x) implies that either g(x) = 0 or h(x) = 0,
which implies c(x) = 1 or b(x) = 1. Thus a(x) is a power of an irreducible poly-
nomial in F [x]. Since e is primitive in ¯FPn(t) (see Proposition 3.8), the same line
of reasoning shows a′(x) is a power of an irreducible polynomial in ¯F [x]. Hence
a′(x) = (x−ξ)m for some positive integer m and ξ∈ ¯F . Since a(x) is a power of
an irreducible polynomial in F [x] and (x−ξ)m divides a(x) in ¯F [x], we conclude
ξ∈F . □
Next, we use a classical result of Frobenius to produce a formula for the scalarξ in
