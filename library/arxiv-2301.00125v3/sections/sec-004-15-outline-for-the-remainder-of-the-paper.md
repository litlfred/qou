---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-004-15-outline-for-the-remainder-of-the-paper
section_title: "Outline for the remainder of the paper"
section_number: 1.5
pages: 4-8
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
The moments of the generalized Ulam problem appear to have been inv estigated primarily by Ross Pinsky.
We begin, in the next section, by stating Pinsky’s precise combinator ial formula for the second moment. Then
we calculate a generating function for the quantities that appear in Pinsky’s decomposition, with hopes of
4
returning later and extracting the precise asymptotics from the g enerating function. For us, the calculation
of the generating function was already diﬃcult.
In Section 2, we present Pinsky’s combinatorial second moment for mula, and we set-up the moment
generating function. In Section 3, we present the main tools for ca lculating the moment generating function.
These are Cauchy’s integral formula and the diagonal method, whic h allows one to specialize multivariate
generating functions by integrating over certain contours to res trict the terms in the double sum (or multiple
sums) occuring in the series. In Section 4 we give formulas for the ge nerating function, with several diﬀerent
equivalent formulas being presented. A number of technical lemmas and side-issues are presented in various
appendices.
2 Pinsky’s combinatorial second moment formula
In his paper [28], Pinsky calculated
E
[
Z 2
n,k
]
=
k∑
i=0
A(k−i,i )B(n, 2k−i), (17)
where for any N,j ∈{ 0, 1,... }, we have
B(N,j ) =
(N
j
)
· 1
j!, (18)
and
A(N,j ) =
∑
ℓ0,...,ℓj ∈{0,1,... }
ℓ0+···+ℓj =N
∑
m0,...,mj ∈{0,1,... }
m0+···+mj =N
j∏
r=0
((ℓr +mr
ℓr,m r
))2
. (19)
See Pinsky’s Proposition 2. We will not reproduce his proof, but we me ntion that his argument is elegant.
Let us deﬁne the new quantity
K(L,M,j ) =
∑
ℓ0,...,ℓj ∈{0,1,... }
ℓ0+···+ℓj =L
∑
m0,...,mj ∈{0,1,... }
m0+···+mj =M
j∏
r=0
((ℓr +mr
ℓr,m r
))2
. (20)
Then we have A(N,j ) = K(N,N,j ). Let us deﬁne the generating function
κ(w,x,y ) =
∞∑
j=0
∞∑
L=0
∞∑
M=0
wjxLyMK(L,M,j ), (21)
for x,y,w ∈ C. Then for w,x,y ∈ [0,∞), we have
κ(w,x,y ) =
∞∑
j=0
wj
( ∞∑
ℓ=0
∞∑
m=0
xℓym
((ℓ +m
ℓ,m
))2)j+1
, (22)
by the Tonelli theorem. (See for example, Section 2.5 of Folland [15].) So the left-hand-side diverges if
and only if the right-hand-side diverges. If neither diverges, the n umerical equality is valid. Also, if neither
diverges for a choice of x = x1, y = y1, w = w1 for x1,y 1,w 1 ∈ [0,∞), then for any complex numbers
x,y,w ∈ C such that|x|≤ x1,|y|≤ y1 and|z|≤ z1, the two sides of (22) are convergent and there is equality
of the two sides by Fubini’s theorem. Given |x|,|y|∈ [0, 1/4), let us deﬁne
κ (2)(x,y ) =
∞∑
ℓ=0
∞∑
m=0
xℓym
((ℓ +m
ℓ,m
))2
, (23)
so that, according to (22),
κ(w,x,y ) =
∞∑
j=0
wj
(
κ (2)(x,y )
)j+1
. (24)
5
z =reiθ
r> 0 and
−π <θ <π
√z =√re iθ/ 2 = exp((1/2) log(z))
Figure 1: Schematic for the standard square-root function on the open domain of C with branch cut along
the non-positive real axis: D1 = {reiθ : r > 0, −π < θ < π}. For z ∈ D1 we use the formula √z =
exp((1/2)
∫ 1
0 (z− 1)(1 +t(z− 1))− 1dt).
The reason we have denoted the function in (23) as κ (2), with the superscript index 2, is that it bears a
relation to a more famous generating function, which we call κ (1):
∀x,y∈ [0, 1/2) , we deﬁne κ (1)(x,y ) =
∞∑
ℓ,m=0
(ℓ +m
ℓ,m
)
xℓym, (25)
using the multinomial notation for the binomial coeﬃcient
(ℓ+m
ℓ,m
)
= (ℓ+m)!
ℓ! m! . We have
κ (1)(x,y ) =
∞∑
n=0
(x +y)n = 1
1− (x +y). (26)
The function that we have called κ (1) is among the ﬁrst examples in many textbooks on generating functio ns.
See, for example, Pemantle and Wilson’s Example 2.2.2 in [27].
The relation between κ (1) and κ (2) is as follows. Taking the product of κ (1)(x,y ) and κ (1)(u,v ) and then
multiplyingx byξ and u byξ−1, and multiplying y byζ and v byζ−1, we have
κ (1)(xξ,yζ )· κ (1)
(u
ξ , v
ζ
)
=
∞∑
ℓ,m,k,n=0
(ℓ +m
ℓ,m
)(k +n
k,n
)
xℓymukvnξℓ−kζm−n. (27)
Therefore, integrating over unit circles, and using the residue met hod:
κ (2)(xu,yv ) =
∮
C(0;1)
∮
C(0;1)
κ (1)(xξ,yζ )· κ (1)
(u
ξ , v
ζ
) dξ
2πiξ · dζ
2πiζ . (28)
Deﬁnition 2.1 LetC(z0;r) denote the circle in the complex plane {z : |z− z0| = r}, which may be
parametrized as z =z0 +reiθ for−π <θ≤π.
One can perform the integral to calculate the following.
Lemma 2.2 Given|x|,|y|∈ [0, 1/4), the series in (23) converges and
κ (2)(x,y ) =
(√
(1− (x +y))2− 4xy
)−1
. (29)
6
Remark 2.3 In our paper, we use the standard branch cut for the natural lo garithm along the non-positive
real axis. So the domain is D1 ={reiθ : r > 0, −π < θ < π} and for each z ∈ D1, the formula is
log(z) =
∫ 1
0 (z− 1)(1 + (z− 1)t)−1dt. Then, for each z∈D 1, we use √z = exp((1/2) log(z)). See Figure 1
for the schematic. In the decomposition of x =reiθ, we refer to the term eiθ as the “phase.” Some complex
analysis textbooks call this the argument as in Section 3.4 o f [1]. But we reserve the term “argument” for the
input of other functions. For example, given a term of the for m
√
f (x) we will refer to f (x) as the “argument
of the square-root function.”
The result of the calculation in the lemma is an instance related to the f act that the diagonal of a
rational bivariate generating function is an algebraic univariate gen erating function. (And it is generically
not rational.) This is proved in Section 2.4 of Pemantle and Wilson, credit ed to Furstenberg and to Hautus
and Klarner.
The residue method may be used to derive formulas such as this, whe n they are unknown. This is opposed
to proof methods for conjectural formulas, which are sometimes more automatic, such as induction. For this
example, we do the contour integral as an exercise in Appendix D. Bu t once the formula is “known,” whether
or not it is proved, there are often simpler combinatorial methods that prove the fo rmula. The methods are
often simpler because they bypass the need for contour integrals . Here we present such an alternative proof.
Proof of Lemma 2.2: Let the right-hand-side of equation (29) be denoted by g(2)(x,y ). Then we may
rewrite
g(2)(x,y ) = 1
1− (x +y)
(
1− 4xy
(1− (x +y))2
)−1/2
. (30)
Therefore, by Newton’s version of the binomial theorem, this gives
g(2)(x,y ) = 1
1− (x +y)
∞∑
n=0
(−1/2)n
n!
(−1)n4nxnyn
(1− (x +y))2n (31)
=
∞∑
n,k=0
(−1/2)n
n! · (−2n− 1)k
k! (−1)n+k4nxnyn(x +y)k, (32)
where the Pochhammer symbol, falling factorial, is
(z)n = z(z− 1)(z− 2)··· (z−n + 1) =
n−1∏
k=0
(z−k). (33)
Then, by the regular binomial formula, we have
g(2)(x,y ) =
∞∑
n,k=0
k∑
j=0
(−1/2)n
n! · (−2n− 1)k
k!
(k
j
)
(−1)n+k4nxn+jyn+k−j. (34)
Therefore, the lemma will be proved if we check that
∞∑
n=0
(−1/2)n
n! · (−2n− 1)k
k!
(k
j
)
(−1)n+k4n
⏐
⏐
⏐
⏐
⏐ j=ℓ−n
k−j=m−n
=
((ℓ +m
ℓ,m
))2
, (35)
for each ℓ,m ∈{ 0, 1,... }. But using well-known combinatorial formulas for the Pochhammer s ymbols of
−1/2 and of negative integers, which we review in Appendix E, this is equiva lent to checking the multinomial
identity:
∞∑
n=0
( ℓ +m
n,n,ℓ −n,m−n
)
=
((ℓ +m
ℓ,m
))2
. (36)
(We use the standard convention that if one of the indices in the sub script of a binomial or multinomial
coeﬃcient is outside the range of 0 to the superscript index, then t hat coeﬃcient equals 0 by deﬁnition.)
Equation (36) may be proved as follows. The key is to use distinguishable permutations .
Drawℓ +m black dots on the number line from 1 to ℓ +m. Above each dot place a circle with either the
top or bottom shaded in, such that if a is the subset of those r∈{ 1,...,ℓ +m} whose circle above it has
the top half shaded, then |a| = ℓ and|a∁| = m. Below each black dot, place a circle with either the left or
right shaded in, such that if B is the set of those r∈{ 1,...,ℓ +m} whose circle below it has the left half
7
shaded, then|B| =m and|B∁| =ℓ. We show a particular example of this mapping in the following displayed
equation:
(37)
Then, if we let n =|a∩B| we have|a∩B ∁| = ℓ−n and|a∁∩B| = m−n, as well. Therefore, |a∁∩B ∁| is
equal to ℓ +m−|a∩B|−| a∩B ∁|−| a∁∩B| , which is n. The number of ways of choosing one quadrant to
shade in – (top,left), (top,right), (bottom,left), (bottom,right) – with a prescribed number of each n, ℓ−n,
m−n, n is N (ℓ,m,n ) where
N (ℓ,m,n ) =
( ℓ +m
n,ℓ−n,m−n,n
)
. (38)
Summing over all choices of n gives all possibilities for choosing the two sets a andB. Since they are chosen
independently, that is equal to ~N (ℓ,m )~N (ℓ,m ) where ~N (ℓ,m ) is the number of ways of choosing a set of
cardinalityℓ as a subset of a larger set of cardinality ℓ +m, which is
~N (ℓ,m ) =
(ℓ +m
ℓ,m
)
. (39)
Since we have proved that ∑
nN (ℓ,m,n ) is equal to ~N (ℓ,m )~N (ℓ,m ), this proves equation (36). □
Remark 2.4 The picture as in (37) could have been made clearer if we had us ed multiple colors, as we did
in a ﬁrst draft of our preprint. But we wished to obtain anothe r picture which could be more easily printed in
black-and-white. The combinatorial object is the same as on e that was already in Pinsky’s paper in the ﬁrst
step of his proof of Lemma 2 [28].
Because of Lemma 2.2 and equation (22), we have
κ(w,x,y ) = κ (2)(x,y )
1−w· κ (2)(x,y ) = 1
(
(1− (x +y))2− 4xy
)1/2
−w
. (40)
Now deﬁne another generating function
α(w,z ) =
∞∑
j,N =0
wjzNA(N,j ) =
∞∑
j,N =0
wjzNB(N,N,j ), (41)
which is the generating function for the combinatorial numbers we w ant,A(N,j ) for N,j ∈{ 0, 1,... }.
