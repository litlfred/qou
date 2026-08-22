---
doc_id: arxiv-1208.1663v2
doc_title: "The 3D index of an ideal triangulation and angle structures"
section_id: sec-014-52-an-independent-proof-of-convergence-for-stric
section_title: "An independent proof of convergence for strict index structures"
section_number: 5.2
pages: 16-21
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "The 3D index of an ideal triangulation and angle structures — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
implies that IM converges when M admits a strict index structure. In this section we give
an independent proof of this fact without using the restriction of the summand of the index
to a ray.
Proposition 5.4. If M supports a strict index structure, then IM(m,e )(q)∈ Z((q1/2)) is
convergent for all m,e∈ Zs.
The proof of proposition 5.4 requires some lemmas.
Lemma 5.5. Fix positive real numbersα,β > 0 withα+β <1/2 and letγ = min{α,β, 1/2−
α−β}. Then for all for all integers m,e we have:
δ(I∆(m,e )q−βm+αe)≥γ max{|m|,|e|,|m +e|}.
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 17
Proof. (of Lemma 5.5) Let L+(m,e ) = max{|m|,|e|,|m +e|}. L+(m,e ) is a piece-wise linear
function given by Figure 7.
Figure 7. A piece-wise linear function L+.
With the notation of Lemma 3.6, we need to show that
(5.3) δ(m,e )−βm +αe≥γL+(m,e ).
First, consider the three rays of δ(m,e ):
ray left hand side of (5.3) right hand side of (5.3)
m = 0,e≥ 0 αe γe
e = 0,m≤ 0 −βm −γm
m =−e≥ 0 m(1/2−α−β) γm
This proves inequality (5.3) in the three rays and shows that the choice of γ is optimal.
Now, in the interior of each of the 6 cones of linearity of L+, δ(m,e )−βm +αe is given
by a quadratic polynomial of m,e . The degree 2 (resp. 1) part of this polynomial is always
greater than or equal to 1/2L+(m,e ) (resp. (1/2−γ)L+(m,e )) by a case computation. For
example, in the cone m≥ 0,e ≤ 0,e +m≥ 0 with rays R+(1, 0) and R+(1,−1) we have
δ(m,e ) =m(m +e)/2 +m/2 and L+(m,e ) =m and
δ(m,e )−βm +αe = m(e +m)
2 + m
2 −βm +αe
≥ m
2 + m
2 −βm +αe
= (1 −β−α)m +α(m +e)
≥ (1−β−α)m≥ (1−β−α)L+(m,e )
The other cases are similar. □
The next lemma is well-known [30].
Lemma 5.6. Consider the convex polytope P in Rr deﬁned by
P ={x∈ Rr|vi·x≤ci i = 1,...s }
where vi∈ Rr and ci∈ R for i = 1,...,s . Then P is compact if and only if the linear
span of the set {vi|i = 1,...,s } is Rr and 0 is a R≥0-linear combination of elements of
{vi|i = 1,...,s }.
18 STA VROS GAROUF ALIDIS
Proof. (of Proposition 5.4) Let ai andbi fori = 1,...,s denote the columns of ( A|B). If M
admits a strict index structure then there exist αi,γi > 0 that satisfy ai +γi < 1 for all i
such that
s∑
i=1
αiai +γiβi =ν.
It follows that
IM(m,e )(q) =
∑
k∈Zr
s∏
i=1
I(mi−bi·k,ei +ai·k)(q)q
βi
2 bi·k+αi
2 ai·k.
Applying Lemma 5.5, it follows that for everyk∈ Zd, the degree of the summand is bounded
below by
s∑
i=1
(βimi−αiei) +γ′
s∑
i=1
(|− mi +bi·k| +|ei +ai·k|) .
Now, Lemma 5.6 and admissibility implies that for ﬁxed N0, there are ﬁnitely many k∈ Zd
such that the above degree is less than N0. Proposition 5.4 follows. □
6. Invariance of the 3D index under 2↔ 3 moves and 2↔ 0 moves
6.1. Invariance under the 3→ 2 move. Consider two ideal triangulationsT and ~T with
N and N + 1 tetrahedra, respectively, related by a 2− 3 move shown in Figure 8.
x1
x
￿
1
x
￿￿
1
x2
x
￿
2
x
￿￿
2
x1x
￿
1
x
￿￿
1
x2
x
￿
2
x
￿￿
2
w1
w
￿
1
w
￿￿
1
w1
w
￿
1
w
￿￿
1
w2
w
￿
2
w
￿￿
2
w2
w
￿
2
w
￿￿
2
w3
w
￿
3
w
￿￿
3
w3
w
￿
3
w
￿￿
3
Figure 8. A 2− 3 move.
The above ﬁgure matches the conventions of [7, Sec.3.6]. For a variable, matrix or vectorf
associated toT , we will denote by ~f the corresponding variable, matrix or vector associated
to ~T . Let us use variables ( Z,Z′,Z′′) and (~Z, ~Z′,~Z′′) to denote the angles of T and and ~T
respectively, where
(6.1) Z := (X1,X 2,Z 3,...,Z N), ˜Z := (W1,W 2,W 3,Z 3,...,Z N).
We ﬁx a quad type assigning these variables to T and ~T as in Figure 3. When calculating
the Neumann-Zagier matrices, we will assume that we keep the edge equation which comes
from the internal edge of the 2-3 bipyramid.
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 19
There are nine linear relations among the shapes of the tetrahedra involved in the move;
three come from adding dihedral angles on the equatorial edges of the bipyramid:
(6.2) W′
1 =X1 +X2, W ′
2 =X′
1 +X′′
2, W ′
3 =X′′
1 +X′
2,
and six from the longitudinal edges:
(6.3)
X1 =W2 +W′′
3 , X ′
1 =W3 +W′′
1 , X ′′
1 =W1 +W′′
2 ,
X2 =W′′
2 +W3, X ′
2 =W′′
1 +W2, X ′′
2 =W′′
3 +W1.
Moreover, due to the central edge of the bipyramid, there is an extra gluing constraint in~T :
(6.4) W′
1 +W′
2 +W′
3 = 2πi.
Let GA(T ) and A(T ) denote, respectively, the sets of generalized and strict angle structures
ofT .
Lemma 6.1. Consider the map:
(6.5) µ3→2 : GA(~T )→ GA(T ), µ 3→2(~Z, ~Z′,~Z′′) = (Z,Z′,Z′′)
deﬁned by Equations (6.3). It induces a map
µ3→2 : A(~T )→ A(T )
Proof. To check thatµ3→2 is well-deﬁned we need to show that Xi +X′
i +X′′
i = 1 is satisﬁed
for i = 1, 2, assuming that Equation (6.4) holds and Wi +W′
i +W′′
i = 1 for i = 1, 2, 3. This
is easy to check. If (~Z, ~Z′,~Z′′)∈ R3(N+1)
+ (where R+ is the set of positive real numbers), it is
manifest from the deﬁnition that (Z,Z′,Z′′)∈ R3N
+ . In other words, µ3→2 sends strict angle
structures on ~T to those onT . □
This proves the ﬁrst part of Proposition 2.13. To prove the remaining part, we study how
are the gluing equation matrices of T and ~T related. Let ( ¯A| ¯B| ¯C) denote the matrix of
exponents of the gluing equations of T . We will use column notation and write
¯A = (¯a1, ¯a2, ¯ai), ¯B = (¯b1, ¯b2, ¯bi), ¯C = (¯c1, ¯c2, ¯ci),
where ¯ai meaning (¯a3, ¯a4,..., ¯aN) and similarly for ¯bi and ¯ci. Eliminating the Z′ variables, we
obtain
A = ¯A− ¯B, B = ¯C− ¯B.
In other words,
(6.6) ( a1,a 2,ai) = (¯a1− ¯b1, ¯a2− ¯b2, ¯ai− ¯bi) ( b1,b 2,bi) = (¯c1− ¯b1, ¯c2− ¯b2, ¯ci− ¯bi).
To compute the corresponding matrices of ~T , use
2 = ¯a1X1 + ¯a2X2 + ¯aiZi + ¯b1X′
1 + ¯b2X′
2 + ¯biZ′
i + ¯c1X′′
1 + ¯c2X′′
2 + ¯ciZ′′
i
= ¯a1(W2 +W′′
3 ) + ¯a2(W′′
2 +W3) + ¯aiZi
+ ¯b1(W3 +W′′
1 ) + ¯b2(W′′
1 +W2) + ¯biZ′
i
+ ¯c1(W1 +W′′
2 ) + ¯c2(W′′
3 +W1) + ¯ciZ′′
i .
20 STA VROS GAROUF ALIDIS
Collecting the coeﬃcients of ˜Z, ˜Z′, ˜Z′′ it follows that the matrix of exponents of the gluing
equations of ~T is given by
~¯A =
(
0 0 0 0
¯c1 + ¯c2 ¯a1 + ¯b2 ¯a2 + ¯b1 ¯ai
)
, ~¯B =
(
1 1 1 0
0 0 0 ¯bi
)
,
~¯C =
(
0 0 0 0
¯b1 + ¯b2 ¯a2 + ¯c1 ¯a1 + ¯c2 ¯ci
)
.
Use a row operation via P =
(
1 0
¯b1 + ¯b2 I
)
it follows that
P~¯A =
(
0 0 0 0
¯c1 + ¯c2 ¯a1 + ¯b2 ¯a2 + ¯b1 ¯ai
)
, P ~¯B =
(
1 1 1 0
¯b1 + ¯b2 ¯b1 + ¯b2 ¯b1 + ¯b2 ¯bi
)
,
P~¯C =
(
0 0 0 0
¯b1 + ¯b2 ¯a2 + ¯c1 ¯a1 + ¯c2 ¯ci
)
.
Since ~A = ~¯A−~¯B and ~B = ~¯C−~¯B, the above combined with Equation (6.6) implies that
(6.7) P~A =
(
−1 −1 −1 0
b1 +b2 a1 a2 ai
)
, P ~B =
(
−1 −1 −1 0
0 a2 +b1 a1 +b2 bi
)
,
Since the 3D index is invariant under row operations (see Remark 2.8), Equation (6.7) and
the pentagon identity (3.5) concludes that I ~T =IT . □
6.2. Invariance under the 2→ 3 move. In this section we will deﬁne what is a special
angle structure onT , and show the partial invariance of the 3D index under a 2 → 3 move.
We will use the same notation as in Section 6.1. To deﬁne a map ( Z,Z′,Z′′)↦→ (~Z, ~Z′,~Z′′),
we need to solve for Wi,W′
i,W′′
i for i = 1, 2, 3 in terms of Xi,X′
i,X′′
i for i = 1, 2 using
Equations (6.2) and (6.3). The answer involves one free variable (say, W1) and it is given by
(W1,W 2,W 3) = (W1,W 1 +X1 +X2 +X′′
2− 1,W 1 +X1 +X2 +X′
1− 1)(6.8a)
(W′
1,W′
2,W′
3) = (X1 +X2,X′
1−X2−X′′
2 + 1,−X1−X′
1 +X′
2 + 1) (6.8b)
(W′′
1,W′′
2,W′′
3 ) = (−W1 + 1−X1−X2,−W1−X1−X′
1 + 1,−W1−X2−X′
2 + 1)(6.8c)
If (Z,Z′,Z′′) is a strict angle structure on T , then (~Z, ~Z′,~Z′′) is a strict angle structure if
and only if Equations (6.8) have a strictly positive solution. It is easy to see that this is
equivalent to the following condition
(6.9) X1 +X2 < 1, X ′′
1 +X′
2 < 1, X ′
1 +X′′
2 < 1.
These conditions are precisely equivalent to the W′
1,W′
2,W′
3 < 1, as follows by Equation
(6.2). I.e., a special strict angle structure is an angle structure such that all angles of the
bipyramid are less than 1.
Deﬁnition 6.2. We will say that (Z,Z′,Z′′) is a special strict angle structure onT if the
inequality (6.9) is satisﬁed.
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 21
Let Asp(T ) denote the set of special strict angle structures on T . Then, we have a map
(more precisely, a section of µ3→2)
µ2→3 : Asp(T )→A(~T ), µ 2→3(Z,Z′,Z′′) = (~Z, ~Z′,~Z′′).
The conclusion is that if T admits a special strict angle structure, then so does ~T . In that
case,IT andI ~T both exist. An application of the pentagon identity as in Section 6.1 implies
that IT =I ~T . □
