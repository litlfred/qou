---
doc_id: arxiv-math-0409565v2
doc_title: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings"
section_id: sec-000-introduction
section_title: "Introduction."
section_number: null
pages: 1-10
source_pdf: 0409565v2.pdf
source_sha256: 236704063f12c05e
doc_brief: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings — Let R be a commutative ring with unity and a let A be a not necessarily commutative R-algebra which is free as an R-module."
---
There have been several generalizations of Gr¨ obner basis theor y, coming in one
of two ﬂavors: noncommutative theory and theories for working o ver special
ground rings, e.g. Euclidean domains, PID’s or UFD’s. For an overview of the
theory of such rings see [1]. Over a ﬁeld, one of the main uses of a Gr¨ obner
basis is to ﬁnd a basis for the quotient of an algebra A by a (left or two-sided)
ideal I. Let us consider two examples for k a (commutative) ﬁeld (with unity)
whose quotient algebras can be readily described through the know n Gr¨ obner
basis theory.
Example 1.
1.1. Let A be the polynomial algebra k[x1, · · · , xn] and consider the ideal
m = ( x1, · · · , xn). Taking a graded lexicographic ordering on A with
xi < x j if i < j , m2 has a Gr¨ obner basis given by {xixj }. Thus the
quotient A/m2 is an n + 1-dimensional k-vector space with a basis given
by:
A/m2 = k{1, x1, · · · , xn}
∗ Both authors were supported under a NSF VIGRE grant.
1
1.2. If g is a lie algebra with lie bracket [ , ]g over k then one forms the
universal enveloping algebra Ug as the quotient of the tensor or free algebra
T g on g by the two sided ideal J:
J = (xy − yx − [x, y]g |x, y ∈ g֒→T g)
If one chooses a total ordering < on the index set I for a k-basis g = k <
xi|i ∈ I > then a Gr¨ obner basis argument yields the Poincare-Birkhoﬀ-
Witt(PBW) theorem which says that Ug has a basis of non-decreasing
words ([5] [2]).
A consideration of the ﬁrst example shows the fact that k was a ﬁeld was not
important – one would have a similar statement with the integers Z, though not
through Gr¨ obner basis techniques. The same holds for the secon d example if
we replace k by an arbitrary (commutative) ring. However, in this more general
setting, one cannot make use of Gr¨ obner basis techniques – one m ust prove this
by “ad-hoc” methods as in [6]. However, these arguments bear a clo se relation
to those used in the Gr¨ obner basis theory. We view the inability of Gr ¨ obner
basis techniques to apply to these mild generalizations as an unsatisf actory state
of aﬀairs.
If one regards the above two examples closely, one sees that the g round ﬁeld
k never enters into the picture. Speciﬁcally, one does not need to inv ert any
constants, and this leads to the notion of a unital Gr¨ obner basis. We will prove
the following:
Theorem 2. Let R be a commutative algebra with unity. Let A be an R-
algebra which is free as an R-module and without quasi-zeros. Let (B, <) be an
admissible system on A and let I be a two-sided ideal of A with a unital Gr¨ obner
basis G. Deﬁne ˜O(G) to be the free R-module spanned by the monomials which
do not occur as leading monomials of members of G. Then:
1. There is a k-module isomorphism A/I ≃ ˜O(G) of free R-modules.
2. A = I ⊕ ˜O(G)
For the case of a left ideal I, or for the case where A has quasi-zeros, one only
need to combine the techniques in [3] with ours. As a corollary we obt ain the
PBW theorem over an arbitrary commutative ring with unity. In part icular, if R
is a Q-algebra we have a Gr¨ obner basis proof of the equivalence of the category of
(ﬁnite dimensional) lie algebras over R and (ﬁnite dimensional) smooth formal
groups over R.
2 Unital Gr¨ obner Bases.
Throughout this section R is a commutative ring with unity and A an R-algebra
with no quasi-zeros, i.e. elements a ∈ A such that for all b, c ∈ A not both 1
one has bac = 0. For brevity, we only state and prove the results in the case of
a two-sided ideal. We take time to ﬁx notation, following closely that of ([3]),
2
Deﬁnition 3.
Let A be an R-algebra with multiplication · (and without quasi-zeros).
Choose a set of (algebra) generators A = R⟨xi|i ∈ Λ ⟩ for some index set
Λ.
3.1. Let α be a ﬁnite length word in Λ, i.e. an ordered expression:
α = α1α2 · · · αn αi ∈ Λ
Then a monomial in A is the ordered product:
xα := xα 1 · xα 2 · · · xα n
3.2. Suppose that A is a free R-module. We say that A has a monomial
basis B sub-ordinate to Λ if B is a subset of all words of ﬁnite length in Λ
such that A has an R-basis:
A = R{xβ | β ∈ B}
We identify β with xβ to simplify notation.
3.3. Assume that B is well ordered by <. Let f ∈ A, then we may write f
uniquely as the ﬁnite sum:
f = c1b1 + c2b2 · · · + cnbn for ci ∈ R∗ := R \ {0} and bi ∈ B .
such that b1 > b 2 > · · · > b n. Then the leading (or head) monomial of f
with respect to B and < is deﬁned as:
LM (f ) := LM< (f ) := b1
i.e. the largest basis element appearing. The leading (or head) coeﬃcient
of f with respect to B and < is deﬁned as:
LC (f ) := LC< (f ) := c1
while the leading (or head) term of f with respect to B and < is deﬁned
as:
L T(f ) := L T< (f ) := LC (f ) LM (f )
3.4. A monomial ordering for a basis B of an algebra B is a well ordering
< on B such that for b, b′, r, s ∈ B we have:
(a) if b < b ′ then r · b · s < r · b′ · s whenever:
r · b · s and LM (r · b′ · s) ⁄= 0
(b) if b′ = LM (r · b · s) ⁄= 0 with r or s ⁄= 1 then b < LM (b′)
3
3.5. If B admits a monomial ordering <, then the pair ( B, <) is an admis-
sible system .
3.6. If ( B, <) is an admissible system, and 0 ⁄= f ∈ A, then we say that
β ∈ B divides f ( and write β|f ) if there are u, v ∈ B and λ ∈ R∗ such
that:
λL T(u · β · v) = L T(f )
We now describe for a subset I ⊆ A, I not necessarily an ideal, a “division
algorithm.” We have put quotations to emphasize that this algorithm d oes not
in general have a meaning. In fact, one may view the statement of ( Theorem 2)
as ascribing a meaning to this algorithm when we make the assumption o f the
existence of a unital Gr¨ obner basis for I. A second reason for putting this in
quotations is that we give no prescription for choosing the elements of I with
which to divide. However, this need not be a hindrance and is in fact a b eneﬁt
in view of (Lemma 6). We need one more set of deﬁnitions at this point:
Deﬁnition 4. Let R be a commutative ring with unity, A an R-algebra which
is free as an R-module and without quasi-zeros, ( B, <) an admissible system
on A, and a subset I ⊆ A. Then deﬁne a R-submodule O(I) of A to be the
R-submodule spanned by the set:
o(I) := {λβ | λ ∈ R∗, β ∈ B , ∀h ∈ I we have L T(h) ⁄= λβ}
We also deﬁne the R-module ˜O(I) as the R-submodule spanned by the set:
˜o(I) := B \ {LM (h) | h ∈ I}
Clearly ˜O(I) is a free R-module.
Input: R a commutative ring with unity, A an R-algebra which is free as an
R-module and without quasi-zeros, ( B, <) an admissible system on A, a
subset I ⊆ A, and f ∈ A.
Output: ˜f ∈ I and r ∈ O(I) the remainder of f on division by I so that
f = r + ˜f
1: i := 0
2: f0 := f .
3: while fi ⁄= 0 do
4: i := i + 1
5: if ⁄ ∃h ∈ I such that L T(h) |f then
6: ri := L T(f )
7: fi := fi−1 − ri
8: else
9: Choose some hi ∈ I such that 0 ⁄= L T(hi) |fi−1
10: Choose some λi ∈ R∗ ui, vi ∈ B so that:
11: λiL T(ui · hi · vi) = L T(fi−1)
12: fi := fi−1 − λiui · hi · vi
4
13: ri := 0
14: end if
15: end while
16: r :=∑
i ri
17: ˜f :=∑
i λiui · hi · vi = f − r
We note that, because we do not specify how to choose the hi (nor the ui and
vi) we do not in general have a unique output.
Deﬁnition 5.
Let R be a commutative ring with unity, A an R-algebra which is free
as a R-module and without quasi-zeros, and let ( B, <) be an admissible
system on A.
5.1. Let I be a (two-sided) ideal in I. Let I have a set of generators:
G = {gγ | γ ∈ Γ } for some index set Γ
Then we say that G is a Gr¨ obner basis with respect to (B, <) if for every
h ∈ I we have a representation:
h =
∑
k∈K
λkuk · gγ k · vk
for K an index set, γk ∈ Γ, λk ∈ R∗ and uk, vk ∈ B such that
LM (uk · gγ k · vk) ≤ LM (f ) whenever uk · gγ k · vk ⁄= 0
5.2. We call a subset G ⊆ A unital if:
(a) For all γ ∈ Γ we have:
LC (gγ ) ∈ R× := units of R
(b) For all γ ∈ Γ and for all α, β ∈ B we have
LC (α · gγ · β) ∈ R× whenever α · gγ · β ⁄= 0
5.3. For f, f ′ ∈ A we say that an S-polynomial is constructible about f and
g if there is some u, u′, v′, v′ ∈ B , λ, λ′ ∈ R∗ such that:
λL T(u · L T(f ) · v) = λ′L T(u′ · L T(f ′) · v′)
In which case we write:
S := S(f, f ′) := λu · f · v − λ′u′ · f ′ · v′
We say that S is an S-polynomial about f and f ′. The choices of u, u′, v, v′
are not in general unique.
5
The extra conditions of a Gr¨ obner basis being unital are not that s trong: If the
ground ring is a ﬁeld, then a Gr¨ obner basis is automatically a unital Gr ¨ obner
basis. If B is closed under multiplication, then the third condition follows if the
second condition holds. We also note that the construction of a S-polynomial
ensures that:
LM (S) < LM (u · LM (f ) · v) = LM (u′ · LM (f ′) · v′)
Lemma 6 ([4]). Let R be a commutative ring with unity, A an R-algebra which
is free as an R-module, (B, <) an admissible system on A, and let I be a two
sided ideal of A which is generated by a unital Gr¨ obner basis:
G = {gγ | γ ∈ Γ }.
Then in the division algorithm, we may choose hi ∈ I so that hi = gγ i for some
γi ∈ Γ .
Proof. Let us set h := hi, f := fi to stop the proliferation of subscripts. Then
since G = {gγ | γ ∈ G} is a Gr¨ obner basis, we may write:
h =
∑
k∈K
λkuk · gγ k · vk (1)
with λk ∈ R∗, uk, vk ∈ B and γk ∈ Γ. Denote:
α := LM (h)
As we are free to choose our representation (Equation 1) of h as we wish, we
may choose one so that α is minimal with respect to the ordering <. Denote:
T := {k ∈ K | LM (uk · gγ k · vk) = α}
We can further choose a representation of h so that |T | is minimal. If |T | = 1 we
are done. Otherwise, let k1 ⁄= k2 ∈ T , and denote cki := LC
(
uki · gγ ki
· vki
)
.
By the assumption that G was a unital Gr¨ obner basis, we have that cki ∈ R×
so that we may form the S-polynomial:
S := λk2
ck2
ck1
uk1 · gγ k1 · vk1 − λk2 uk2 · gγ k2 · vk2
Then we have:
h = λk1 uk1 · gγ k1 · uk1 + λk2 uk2 · gγ k2 · uk2 +
∑
k⁄=k1,k 2
λkuk · gγ k · uk
= λk1 uk1 · gγ k1 · uk1 +
(
λk2
ck2
ck1
uk1 · gγ k1 · vk1
−λk2
ck2
ck1
uk1 · gγ k1 · vk1
)
+ λk2 uk2 · gγ k2 · uk2
+
∑
k⁄=k1,k 2
λkuk · gγ k · uk
=
(
λk1 − λk2
ck2
ck1
)
uk1 · gγ k1 · vk1 − S +
∑
k⁄=k1,k 2
λkuk · gγ k · uk
6
We have two possibilities. The ﬁrst is that we may have succeeded in ca n-
celing all terms with leading monomial α, which contradicts the minimality of
α. Otherwise, as LM (S) < α , we have written h with no more than |T | − 1
terms containing α, contradicting the minimality of T . Thus we conclude that
for such a minimal representation we must have |T | = 1 as desired. ■
Now we may proceed with the proof of our theorem.
Proof. (Theorem 2) Let f be an element of A. Then the division algorithm
allows us to write:
f = r + ˜f
with r ∈ O(I) and ˜(f ) ∈ I. By (Lemma 6) we see that we can take r ∈ ˜O(G).
As f is arbitrary in A, we then have
A = I + ˜O(G)
The theorem will follow if we can show that this sum is direct, which in tur n will
follow from showing that r is unique. So suppose that the division algorithm
produces two representations for f :
f = ˜f + r = ˜f ′ + r′
Then we have ˜f − ˜f ′ ∈ I so that r − r′ ∈ I. Now assume that r − r′ ⁄= 0, then
(Lemma 6) shows that if there is some h ∈ I such that L T(h) |r − r′ then there
is some gγ ∈ G such that L T(gγ ) |r − r′. But then, by construction of r and
r′, we know that there is no such gγ and we will have a contradiction by taking
h = r − r′. ■
Proposition 7. Let R be a commutative ring with unity, A an R-algebra which
is free as an R-module, (B, <) an admissible system on A. Let α ∈ B and
suppose that f1, · · · , fn ∈ A satisfy LM (fi) = α and LC (fi) ∈ R×. Then if:
f :=
∑
i
cifi ci ∈ R∗
satisﬁes LM (f ) < α then we may write:
f =
∑
i⁄=j
di,j Si,j
where the Si,j are the S-polynomials about fi and fj given by:
Si,j := 1
ai
fi − 1
aj
fj ai := LC (fi) , aj := LC (fj) ∈ R×
7
Proof. Because we have a cancellation of the terms of fi involving α we have
that∑
i ci = 0. Then:
f = c1f1 + · · · + cnfn
= c1a1
( 1
a1
f1
)
+ · · · + cnan
( 1
an
fn
)
= c1a1
( 1
a1
f1 − 1
a2
f2
)
+ (c1a1 + c2a2)
( 1
a2
f2 − 1
a3
f3
)
+ · · ·
+(c1a1 + · · · cn−1an−1)
( 1
an−1
fn−1 − 1
an
fn
)
+ (c1a1 + · · · cnan) 1
an
fn
= c1a1S1, 2 + (c1a1 + c2a2)S2, 3 + · · ·
+(c1a1 + · · · + cn−1an−1)Sn−1,n + 0 1
an
fn
which gives the desired result. ■
Theorem 8 (Buchberger). Let R be a commutative ring with unity, A an
R-algebra which is free as an R-module, (B, <) an admissible system on A. Let
I ≤ A be an ideal generated by a unital set:
G := {gγ | γ ∈ Γ }
for some index set Γ . Then G is a Gr¨ obner basis for I if and only if all S-
polynomials for G have zero remainder under the division algorithm.
Proof. We show that if all S-polynomials reduce to zero and f ∈ I then f has
a Gr¨ obner basis representation – i.e a representation satisfying ( Deﬁnition 5.1).
As G generates I we may choose a representation of f as:
f =
∑
i
hi · gγ i · h′
i hi, h ′
i ∈ A γ i ∈ Γ (2)
As A has an R-basis given by B then we may write hi = ∑
k∈K ckβk, hi =∑
k′∈K ′ c′
k′ β′
k′ with ck, c′
k′ ∈ R∗ and βk, β′
k′ ∈ B , so that we have:
f =
∑
i,k,k ′
ckc′
k′ βk · gi · β′
k′
If for some representation of f as in (Equation 2) we have for all βk · gi · β′
k′ ⁄= 0
that LM (βk · gi · β′
k′ ) ≤ LM (f ) then we are done. Otherwise, let us sup-
pose that for all such representations of f we have the maximal term appear-
ing α := max {LM (hi · gi · h′
i)} is such that α > LM (f ). Over all such
representations we may choose one so that α is minimal. We will now pro-
duce a new representation for f whose corresponding maximal term is strictly
less than α, thereby obtaining a contradiction. To this end, let us deﬁne
8
T := {i|LM (hi · gi · h′
i) = α} and:
g :=
∑
i∈T
L T(hi) · gi · L T(h′
i)
=
∑
i∈T
LC (hi) LC (h′
i) LM (hi) · gi · LM (h′
i)
so that each term of f − g has leading monomial less than α. As G is assumed
to be unital, we have that ai := LC (LM (hi) · gi · LM (h′
i)) ∈ R× so that we
may apply to (Proposition 7) to g and write:
g =
∑
i⁄=j∈T
di,j Si,j (3)
where the Si,j are the the S-polynomials about LM (hi) · gi · LM (h′
i) and
LM (hj) · gj · LM
(
h′
j
)
given by:
Si,j := 1
ai
LM (hi) · gi · LM (h′
i) − 1
aj
LM (hi) · gj · LM
(
h′
j
)
But then, the Si,j ’s are also S-polynomials about gi and gj, so that we have, by
assumption, that they reduce to zero on the division algorithm, i.e. t hat:
Si,j =
∑
l
λli,j uli,j · gli,j · vli,j uli,j , vli,j ∈ B , λ li,j ∈ R∗ gli,j ∈ G (4)
As LM (Si,j ) < α we see that by substituting (Equation 4) into (Equation 3) we
are able to write g, and thus f , in the form of (Equation 2) such that the leading
monomial of each term is strictly less than α, our desired contradiction. ■
Corollary 9 (PBW). Let g be a lie algebra over R, a commutative ring with
unity, with lie bracket [ , ]g. Then:
Ug = T g/J where J = (xy − yx − [x, y]g |x, y ∈ g֒→T g)
is isomorphic as an R-module to Sg, the symmetric algebra on g.
Proof. Choosing a well ordered basis {xi | i ∈ I} for g then T g has a multi-
plicative monomial basis consisting of the words of ﬁnite length in the xi’s with
the graded lexicographic ordering. Also Sg has a basis of words of ﬁnite length
written in non-decreasing order. The ideal J is generated by:
G := {gi,j := xixj − xj xi − [xi, xj]g | xi > xj }
The argument that G is a Gr¨ obner basis is exactly as in [5] or [2] which makes
use of (Theorem 8). As the leading terms L T(gi,j ) = xixj are monic and the
basis is multiplicative we have that G is a unital Gr¨ obner basis. The corollary
follows. ■
9
References
[1] Adams, W; Loustaunau, P; “An Introduction to Grobner Bases ”. AMS,
Providence, 1994.
[2] de Graaf, W; “Lie Algebras: Theory and Algorithms”. North-Holland
Mathematical Library, 56 . North-Holland Publishing Co., Amsterdam,
2000.
[3] Li, H; “Noncommutative Gr¨ obner Bases and Filtered-Graded Tr ansfer.”
Lecture Notes in Mathematics, 1795 Springer-Verlag, Berlin, 2002.
[4] Madlener, K; Reinert, B; “On Gr¨ obner Bases in Monoid and Group s
Rings”. Report SR-93-08, SEKI Univeristy of Kaiserslautern, 199 3.
[5] Mora, T; “An Introduction to Commutative and Noncommutative
Gr¨ obner Bases”.Theoretical Computer Science 134 (1994) 131–173.
[6] Serre, J-P; “Lie Algebras and Lie Groups. 1964 Lectures Given a t Harvard
University”. W. A. Benjamin, Inc., New York-Amsterdam 1965.
10
