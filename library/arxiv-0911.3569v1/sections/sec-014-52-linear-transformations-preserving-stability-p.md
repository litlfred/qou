---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-014-52-linear-transformations-preserving-stability-p
section_title: "Linear transformations preserving stability – polynomial case."
section_number: 5.2
pages: 15-19
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
Theorem 5.2 (Theorem 1.1 of [5]) . Let κ∈ Nm, and let T : C[x]≤κ→ C[x] be a
linear transformation. Then T maps S[x]≤κ into S[x] if and only if either
(a) T (f) =η(f)·p for some linear functional η : C[x]≤κ→ C and p∈ S[x], or
(b) the polynomial T ((x + y)κ) is stable in S[x, y].
Proof. Let u = {uij : ( i,j ) ∈ I(κ)}, and deﬁne a linear transformation ~T :
C[u]MA → C[x] as follows. For every A ⊆ I(κ), deﬁne α(A) : [ m] → N by
putting α(A,i ) = |{j ∈ [κ(i)] : ( i,j ) ∈ A}| for each i ∈ [m]. Then for each
A⊆I(κ) deﬁne ~T (uA) = T (xα(A)), and extend this linearly to all of C[u]MA. Let
∆ : C[u]MA→ C[x] be the diagonalization operator deﬁned by ∆( uij) = xi for all
(i,j )∈I(κ), extended algebraically.
Notice that T = ~T◦ Polκ, and that ~T =T◦ ∆. By Proposition 5.1 (and Lemma
2.4), it follows that T preserves stability if and only if ~T preserves stability. This
is equivalent to one of two cases in Theorem 3.4.
In case (a), if ~T =p·~η for some p∈ S[x] and linear functional ~η : C[y]MA→ C
then T = p· (η◦ Polκ) is also in case (a). Conversely, if T is in case (a) then the
same is true of ~T , by construction.
In case (b), let Pol (y)
κ : C[y]≤κ→ C[v]MA denote the κ-th polarization of the y
variables. The symbols of T and ~T are related by
~T ((u + v)I(κ)) = (T◦ ∆)((u + v)I(κ)) = Pol(y)
κ T ((x + y)κ),
and Proposition 5.1 shows that T is in case (b) if and only if ~T is in case (b). □
5.3. Linear transformations preserving stability – transcendental case.
Exercise 5.3. Let T : C[x]→ C[x] be a linear transformation.
(a) Then T : S[x]→ S[x] if and only if T : S[x]≤κ→ S[x] for all κ∈ Nm.
(b) Deﬁne S : C[x, y]→ C[x, y] by S(xαyβ) = T (xα)yβ and linear extension. If
T ((x + u)κ) is stable for all κ∈ Nm then S((x + u)κ(y + v)β) is stable for all
κ,β∈ Nm.
Let S[x] denote the set of all power series in C[[x]] that are obtained as the limit
of a sequence of stable polynomials in S[x] which converges uniformly on compact
sets. Theorem 5.4 is an astounding generalization of the P´ olya-Schur Theorem. For
α∈ Nm, let α! =∏m
i=1α(i)!.
Theorem 5.4 (Theorem 1.3 of [5]). LetT : C[x]→ C[x] be a linear transformation.
Then T maps S[x] into S[x] if and only if either
(a) T (f) =η(f)·p for some linear functional η : C[x]→ C and p∈ S[x], or
(b) the power series
T (e−xy) =
∑
α:[m]→N
(−1)αT (xα)yα
α!
is in S[x, y]
(Theorem 3.5 has a similar extension – see Theorems 1.2 and 1.4 of [5].)
Forα≤β in Nm, let (β)α =β!/(β−α)!, and for α⁄≤β let (β)α = 0.
16 DAVID G. WAGNER
Theorem 5.5 (Theorem 5.1 of [5]) . Let F (x, y) = ∑
α∈NmPα(x)yα be a power
series in C[x][[y]] (so that each Pα∈ C[x]). Then F (x, y) is in S[x, y] if and only
if for all β∈ Nm,
∑
α≤β
(β)αPα(x)yα
is stable in S[x, y].
(This implies the analogous result for real stability, since SR[x] = S[x]∩ R[x].)
Exercise 5.6. Derive Theorem 5.4 from Theorems 5.2 and 5.5. (Hint: T ((x +y)κ)
is stable if and only if T ((1− xy)κ) is stable.)
One direction of Theorem 5.5 is relatively straightforward.
Lemma 5.7 (Lemma 5.2 of [5]). Fixβ∈ Nm. The linear transformation T : yα↦→
(β)αyα on C[y] preserves stability.
Proof. By Theorem 5.2 and Exercise 5.3(a), it suﬃces to show that for all κ∈ Nm,
the polynomial T ((y + u)κ) is stable. Now
T ((y + u)κ) =
m∏
i=1


κ(i)∑
j=0
j!
(κ(i)
j
)(β(i)
j
)
yj
iuκ(i)−j
i

,
so it suﬃces to show that for all k,b∈ N, the polynomial f(t) =∑k
j=0j!
(k
j
)(b
j
)
tj is
real stable. Let g(t) = (1 +d/dt)ktb. One can check that f(t) = tbg(1/t). It thus
suﬃces to show that 1+d/dt preserves stability. For anya∈ N, (1+d/dt)(t+u)a =
(t +u +a)(t +u)a−1 is stable, and so Theorem 5.2 implies the result. □
Now, letF =F (x, y) be as in the statement of Theorem 5.5, and let (Fn : n∈ N)
be a sequence of stable polynomials Fn(x, y) =∑
α∈NmPn,α(x)yα in S[x, y] con-
verging to F uniformly on compact sets. Fix β∈ N and deﬁne a linear transfor-
mation T : C[x, y]→ C[x, y] by T (xγyα) = (β)αxγyα and linear extension. By
Lemma 5.7 and Exercise 5.3,T preserves stability inS[x, y]. Thus, (T (Fn) : n∈ N)
is a sequence of stable polynomials converging toT (F ). Since T (F ) is a polynomial
the convergence is uniform on compact sets, and so Hurwitz’s Theorem implies that
T (F ) is stable.
The converse direction of Theorem 5.5 is considerably more technical, although
the idea is simple. With F as in the theorem, for each n≥ 1 let
Fn(x, y) =
∑
α≤n1
(n1)αPα(x)yα
nα.
The sequence (Fn : n≥ 1) converges to F , since for each α∈ Nm, n−α(n1)α→ 1
as n→ ∞. Each Fn is stable, by hypothesis (and scaling). The hard work is
involved with showing that the convergence is uniform on compact sets. To do this,
Borcea and Br¨ and´ en develop a very ﬂexible multivariate generalization of the Szasz
Principle [5, Theorem 5.6] – in itself an impressive accomplishment. Unfortunately,
we have no space here to develop this result – see Section 5.2 of [5].
MULTIVARIATE STABLE POLYNOMIALS 17
6. Johnson’s Conjectures.
Let A = (A1,...,A k) be a k-tuple of n-by-n matrices. Deﬁne the mixed deter-
minant of A to be
Det(A) = Det(A1,...,A k) =
∑
(S1,...,Sk)
k∏
i=1
detAi[Si],
in which the sum is over all ordered sequences of k pairwise disjoint subsets of [n]
such that [n] =S1∪···∪ Sk, and Ai[Si] is the principal submatrix of Ai supported
on rows and columns in Si. Let Ai(Si) be the complementary principal submatrix
supported on rows and columns not in Si, and for j∈ [n] let Ai(j) =Ai({j}).
For example, when k = 2 and A1 = xI and A2 = −B, this specializes to
Det(xI,−B) = det(xI−B), the characteristic polynomial of B. In the late 1980s,
Johnson made three conjectures about the k = 2 case more generally.
Johnson’s Conjectures. LetA and B ben-by-n matrices, with A positive deﬁ-
nite and B Hermitian.
(a) Then Det(xA,−B) has only real roots.
(b) Forj∈ [n], the roots of Det(xA(j),−B(j)) interlace those of Det(xA,−B).
(c) The inertia of Det(xA,−B) is the same as that of det(xI−B).
In part (c), the inertia of a univariate real stable polynomial p is the triple
ι(p) = (ι−(p),ι 0(p),ι +(p)) with entries the number of negative, zero, or positive
roots of p, respectively.
In 2008, Borcea and Br¨ and´ en [1] proved all three of these statements in much
greater generality.
Theorem 6.1 (Theorem 2.6 of [1]) . Fix integers 𝓁,m,n ≥ 1. For h∈ [𝓁] and
i∈ [m] let Bh and Ahi ben-by-n matrices, and let
Lh =
m∑
i=1
xiAhi +Bh.
(a) If all the Ahi are positive semideﬁnite and all the Bh are Hermitian, then
Det(L) = Det(L1,...,L 𝓁)∈ SR[x] is real stable.
(b) For eachj∈ [n], let L(j) = (L1(j),...,L 𝓁(j)). With the hypotheses of part (a),
the polynomial Det(L) +yDet(L(j))∈ SR[x,y ] is real stable.
Proof. Let Y = diag(y1,...,y n) be a diagonal matrix of indeterminates. By Propo-
sition 2.1, for each h∈ [𝓁] the polynomial
det(Y +Lh) =
∑
S⊆[n]
yS detLh(S)
is real stable in SR[x, y]. By inversion of all the y indeterminates, each
det(I−YLh) =
∑
S⊆[n]
(−1)|S|yS detLh[S]
18 DAVID G. WAGNER
is real stable. Since∏𝓁
h=1 det(I−YLh) is real stable, contraction and specialization
imply that
Det(L) = (−1)n ∂n
∂y1··· ∂yn
𝓁∏
h=1
det(I−YLh)
⏐⏐⏐⏐⏐
y=0
is real stable, proving part (a).
For part (b), letV be the n-by-n matrix with all entries zero except for Vjj =y.
By part (a),
Det(V,L 1,...,L h) = Det(L) +yDet(L(j))
is real stable. □
Theorem 6.1 (with Corollary 2.10) clearly settles Conjectures (a) and (b).
Proof of Conjecture (c). Let A and B be n-by-n matrices with A positive deﬁnite
and B Hermitian. Let ( ι−,ι 0,ι +) be the inertia of det( xI− B). Let f(x) =
Det(xA,−B), and let (ν−,ν 0,ν +) be the inertia of f.
We begin by showing thatν0 =ι0. Since ι0 = min{|S| : S⊆ [n] and det(B(S))⁄=
0}, it follows that ν0≥ ι0. The constant term of f(x) is (−1)n det(B), so that if
ι0 = 0 then ν0 = 0. If ι0 = k > 0 then let S ={s1,...,s k}⊆ [n] be such that
det(B(S))⁄= 0. For 0 ≤ i≤ k let fi(x) = Det(A({s1,..,s i}),−B({s1,..,s i})), so
that f0(x) = f(x). By Theorem 6.1, the roots of fi−1 and of fi are interlaced, for
eachi∈ [k]. Thus,
ν0 =ι0(f0)≤ι0(f1) + 1≤ι0(f2) + 2≤···≤ ι0(fk) +k =k =ι0,
since ι0(fk) = 0 because det(B(S))⁄= 0. Therefore ν0 =ι0.
For any positive deﬁnite matrix A, Det(xA,−B) is a polynomial of degree n.
Suppose that A is such a matrix for which ν+⁄= ι+. Consider the matrices Aλ =
(1−λ)I +λA for λ∈ [0, 1]. Each of these matrices is positive deﬁnite. From the
paragraph above, each of the polynomials gλ(x) = Det(xAλ,−B) has ι0(gλ) = ι0.
Since ι+(g0) = ι+⁄= ν+ = ι+(g1) and the roots of gλ vary continuously with λ,
there is some value µ∈ (0, 1) for which ι0(gµ)>ι 0. This contradiction shows that
ν+ =ι+, and hence ν− =ι− as well. □
Borcea and Br¨ and´ en [1] proceed to derive many inequalities for the principal
minors of positive semideﬁnite matrices, and some for merely Hermitian matrices.
These are applications of inequalities valid more generally for real stable polynomi-
als. The simplest of these inequalities are as follows.
For ann-by-n matrix A, the j-th symmetrized Fisher product is
σj(A) =
∑
S⊆[n]:|S|=j
det(A[S]) det(A(S)).
and the j-th averaged Fisher product isˆσj(A) =
(n
j
)−1
σj(A). Notice that σj(A) =
σn−j(A) for all 0≤j≤n.
Corollary 6.2. LetA be an n-by-n positive semideﬁnite matrix.
(a) Thenˆσj(A)2≥ˆσj−1(A)ˆσj+1(A) for all 1≤j≤n− 1.
(b) Also,ˆσ0(A)≤ˆσ1(A)≤···≤ ˆσ⌊n/2⌋.
(c) If A is positive deﬁnite and det(A) =d then
ˆσ1(A)
d ≥
(ˆσ2(A)
d
)1/2
≥
(ˆσ3(A)
d
)1/3
≥···≥
(ˆσn(A)
d
)1/n
= 1.
MULTIVARIATE STABLE POLYNOMIALS 19
Proof. It suﬃces to consider positive deﬁnite A. By Theorem 6.1, the polynomial
Det(xA,−A) = ∑n
j=0(−1)jσj(A)xj has only real roots, and these roots are all
positive. Part (a) follows from Newton’s Inequalities [12, Theorem 51]. Part (a)
and the symmetry σj(A) = σn−j(A) for all 0 ≤ j≤ n imply part (b). Part (c)
follows from Maclaurin’s Inequalities [12, Theorem 52]. □
