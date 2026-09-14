---
doc_id: arxiv-2311.05446v3
doc_title: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY"
section_id: sec-008-4-dimensional-convexity-properties-of-the-gaussi
section_title: "Dimensional convexity properties of the Gaussian relative entropy"
section_number: 4
pages: 18-25
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
doc_brief: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY — We study the connection between the concavity properties of a measureνand the convexity properties of the associated"
---
entropy
In this section, we will differentiate the relative entropyD(·∥ν), where
dν=e −V dx, directly along displacement interpolations without decom-
posing it into two parts as in the previous section. While we focus on the
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 19
Gaussian measure,ν=γ, we will introduce the relevant setup for a general
ν.
In this direction, the presentation is cleaner and more insightful if we
use the language of the Bakry– ´Emery Γ-calculus. Measures dν=e −V dx,
for smooth enoughV, naturally occur as the equilibrium measure for the
semigroup of operatorsP t =e tL, with generatorLf= ∆f−⟨∇V,∇f⟩. In-
troduction of the bilinear form Γ (called the carr´ e du champ) on functions,
and its iteration Γ 2, reduces the study of many properties regarding con-
vergence to equilibrium to the study of the relationships amongL, Γ, and
Γ2.
In the case of dν=e −V dxunder discussion, when the generatorLis as
described earlier, the carr´ e du champ and its iteration are given by,
Γ(f,g) =⟨∇f,∇g⟩,
Γ2(f,g) =⟨∇ 2f,∇ 2g⟩+⟨∇ 2V·∇f,∇g⟩, (46)
where the first inner-product in the expression for Γ2 is the Hilbert–Schmidt
inner product. It is customary to write Γ(f) for Γ(f,f), and Γ 2(f) for
Γ2(f,f). We refer the reader to the text [6] for a comprehensive treatment
of this subject. However, what we will use in calculating the derivatives of
D(µt∥ν) is a simple integration-by-parts formula that the reader may verify
directly, Z
Γ(f,g) dν=−
Z
fLgdν.(47)
Example 4.1.WhenV= 0, one obtains theheat semigroupwhich has
the Lebesgue measure as its equilibrium measure. In this case,Lf= ∆f,
Γ(f) =|∇f| 2, and Γ2(f) =∥∇ 2f∥ 2. Here∥·∥denotes the Hilbert–Schmidt
norm.
Example 4.2.WhenVcorresponds to the Gaussian measure onR n,ν=γ,
the semigroup obtained is the well-knownOrnstein–Uhlenbeck semigroup.
ThenLf= ∆f−⟨x,∇f⟩, Γ(f) =|∇f| 2, and Γ 2(f) =∥∇ 2f∥ 2 +|∇f| 2.
Let us differentiateD(·∥ν) two times, as needed. The underlying heuristic,
namely thatP tfdνis the gradient flow ofD(·∥ν) (starting atfdν) under
a natural Riemannian-like structure onW 2(Rn) introduced by Otto ([39]), is
a powerful tool in the field. However, we will be content with the following
simple calculation and refer the reader to [47, Chapter 8] or [48, Chapter
15] for more details.
Lemma 4.3.Letdν=e −V dx, for smoothV. Consider a displacement
interpolation{µ t}t∈[0,1] inW 2(Rn), with the optimal velocity field∇θ t. Sup-
poseθ t is sufficiently smooth, then
d
dtD(µt∥ν) =−
Z
Lθt dµt,
d2
dt2D(µt∥ν) =
Z
Γ2(θt) dµt.,
(48)
20 GAUTAM AISHWARYA AND LIRAN ROTEM
whereL,Γ 2 are as described earlier.
Proof.Letρ t denote the density ofµ t with respect toν. Then,
d
dtD(µt∥ν) = d
dt
Z
ρt logρt dν= d
dt
Z
logρt dµt
=
Z
∂t logρt dµt +
Z
⟨∇logρ t,∇θt⟩dµ t
= d
dt
Z
ρt dν+
Z
⟨∇logρ t,∇θt⟩ρt dν
= 0 +
Z
⟨∇ρt,∇θt⟩dν=−
Z
ρtLθt dν=−
Z
Lθt dµt.
(49)
In the above computation, the third equality uses the chain rule and the
continuity equation (27), and the sixth equality is an application of formula
(47) for the semigroup under consideration.
Furthermore, we can differentiate again to compute the second derivative,
d2
dt2D(µt∥ν) =− d
dt
Z
Lθt dµt =−
Z
L∂tθt dµt−
Z
⟨∇Lθt,∇θt⟩dµ t
=
Z
L
|∇θt|2
2

dµt−
Z
⟨∇Lθt,∇θt⟩dµ t
=
Z 
L
|∇θt|2
2

−⟨∇Lθt,∇θt⟩

dµt =
Z
Γ2(θt) dµt,
(50)
where in the second equality we use the change rule and the continuity
equation (27), the third equality uses the Hamilton–Jacobi equation (28),
while the last equality uses the formula
Γ2(f) =L
|∇f| 2
2

−⟨∇Lf,∇f⟩(51)
for smoothf. This is a well-known weighted version of Bochner’s formula,
which can be easily obtained from its unweighted counterpart (see, for ex-
ample, [48, Chapter 14]).□
Therefore, ifS⊆W 2(Rn) is a displacement convex set, and we would like
to prove thate −aD(·∥ν) is concave onS, we must prove that
Z
Γ2(θt) dµt≥a
Z
Lθt dµt
2
,(52)
for all displacement interpolations{µ t}t∈[0,1] inS. Actually, in this section,
we would like to go a little bit further than the above inequality to also utilize
the “curvature” associated with the semigroup. To this end, we introduce
the notion of (κ,1/a)-convexity of a function defined on a uniquely geodesic
space.
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 21
Definition 4.4.[21, Equation 1.2 rephrased] Let (X,d) be a uniquely ge-
odesic metric space. A functionS:X →[0,∞] is called (κ,1/a)-convexif
for every constant speed geodesicc: [0,1]→X, we have
d2
dt2S(ct)≥κd(c 0,c 1)2 +a
 d
dtS(ct)
2
,(53)
in the distributional sense.
Remark 4.5.A global formulation of the above condition can be found
in [21, Definition 2.7]. We discuss the particular case of (2,n)-convexity in
Lemma 5.3.
Thus, Theorem 3.10 from previous section establishes (0, p
p−1n)-convexity
of the relative entropyD(·∥ν) on the geodesic subspaceS={µ:
R
Vdµ≤
n
p} ⊆W2(Rn) when dν=e −V dx, whereVis ap-homogeneous convex
function onR n. In this case, it is possible to trade some of the dependence
onnfor a dependence on the lower bounds on∇ 2V, but we choose not to
pursue this direction in the current paper.
We will now specialize to the Gaussian case. Note that this corresponds
to the semigroup in Example 4.2. Here we aim to obtain a (κ,n)-convexity
ofD(·∥γ) on a suitable class of measures. Thus, we want to obtain an
inequality that reads,
Z
Γ2(θt) dµt≥κW 2
2 (µ0,µ 1) + 1
n
Z
Lθt dµt
2
,(54)
that is,
Z
∥∇2θt∥2 +|∇θt|2 dµt≥κW 2
2 (µ0,µ 1) + 1
n
Z
Lθt dµt
2
.(55)
This is remarkably similar to the sufficiency condition in [29] obtained from
the Kolesnikov–Milman approach ([30]) with the exception of the first term
on the right. This comparison goes beyond similarity, to the level of the proof
itself, since it is the same as in [22] albeit presented in a slightly different
form. While we claim no originality here, for the sake of completeness we
repeat the argument from [22] adapted to obtain the statement we want.
Theorem 4.6.Denote byS n the collection of all even measuresµinP 2,ac(Rn)
which satisfy the inequality
R
f 2 dµ≤
R
|∇f| 2 dµfor all odd test functions
f. Then,
Z
Γ2(u) dµ≥2
Z
Γ(u) dµ+ 1
n
Z
Ludµ
2
,(56)
for all even functionsu. HereL,Γ 2 are the generator and the iterated carr´ e
du champ, respectively, for the Ornstein–Uhlenbeck semigroup.
22 GAUTAM AISHWARYA AND LIRAN ROTEM
Consequently, if{µ t}t∈[0,1] is a displacement interpolation that lies en-
tirely inS n and is driven by a smooth velocity field, thenD(µ t∥γ)is(2,n)-
convex. In particular,
e−D(µt∥γ)
n ≥(1−t)e −D(µ0∥γ)
n +te−D(µ1∥γ)
n .(57)
Remark 4.7.If the measureµsatisfies the inequality Var µ(f)≤C
R
|∇f| 2 dµ,
we say thatµsatisfies aPoincar´ e inequalitywith constantC. The best pos-
sibleCis called thePoincar´ e constantofµ. If we assume that the function
fis odd and the measureµis even, then Var µ(f) =
R
f 2 dµ. Thus,S n
is the collection of even measures, absolutely continuous with respect to
the Lebesgue measure and having finite second moment, which satisfy a
Poincar´ e inequality for odd functions with constant 1.
Proof.Letube an even function. Considerv=u−r, wherer(x) =R
Ludµ
2n |x|2. We will writel=
R
Ludµfor notational convenience. Note
that∇r(x) = l
nx,∇ 2r(x) = l
nI, whereIdenotes the identity matrix, and
∆r=l. Therefore,
∥∇2u∥2 =∥∇ 2v+∇ 2r∥2 =∥∇ 2v∥2 + 2l
n ∆v+ l2
n =∥∇ 2v∥2 + 2l
n ∆u− l2
n
=∥∇ 2v∥2 + 2l
n (Lu+⟨x,∇u⟩)− l2
n
=∥∇ 2v∥2 + 2l
n⟨x,∇u⟩+
2l
nLu− l2
n

.
(58)
Now, sincevis even,∂ ivis an odd function, for eachi. Therefore, ifµ∈
Sn then we can apply the Poincar´ e inequality assumption to∂ ivin the
calculation below.
Z
∥∇2v∥2 dµ=
X
i
Z X
j
(∂j∂iv)2 dµ=
X
i
Z
|∇∂iv|2 dµ≥
X
i
Z
(∂iv)2 dµ
=
X
i
Z 
∂iui− l
nxi
2
dµ=
Z 
|∇u|2− 2l
n⟨x,∇u⟩+ l2
n2|x|2

dµ.
(59)
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 23
Putting this inequality into the expression for∥∇ 2u∥2 obtained earlier,Z
Γ2(u) dµ=
Z  
∥∇2u∥2 +|∇u| 2
dµ
=
Z 
∥∇2v∥2 + 2l
n⟨x,∇u⟩+
2l
nLu− l2
n

+|∇u| 2

dµ
≥
Z 
|∇u|2− 2l
n⟨x,∇u⟩+ l2
n2|x|2 + 2l
n⟨x,∇u⟩+
2l
nLu− l2
n

+|∇u| 2

dµ
=
Z 
2|∇u|2 + l2
n2|x|2 +
2l
nLu− l2
n

dµ
≥
Z 2l
nLu− l2
n

dµ+ 2
Z
|∇u|2 dµ= 1
nl2 + 2
Z
|∇u|2 dµ
= 1
n
Z
Ludµ
2
+ 2
Z
Γ(u) dµ.
(60)
For the second part, observe that a potentialθ t for the velocity field∇θ t
corresponding to optimal transport between any two measuresµ 0 andµ 1
inS n must be even, since the measures themselves are even. Further,R
Γ(θt) dµt =
R
|∇θt|2 dµt, but the latter quantity equalsW 2
2 (µ0,µ 1) by
[47, Remarks 5.40 (iii), Example 5.42]. Therefore, by the first part, if the
displacement interpolation betweenµ 0 andµ 1 is contained inS n then the
condition of inequality (54) is satisfied. This establishes the second part of
the theorem.□
Remark 4.8.As indicated in the Introduction, an affirmative answer to
Question 1.6 forµ 0 =γ K0,µ 1 =γ K1, for symmetric convex bodiesK 0 and
K1, would imply the result of Eskenazis–Moschidis ([22]).
Definition 4.9.A measureµ∈P(R n) is said to bestrongly log-concaveif
its density with respect to the Gaussian measureγonR n exists, and is a
log-concave function.
Example 4.10.LetKbe a convex body. Then,γ K is strongly log-concave
because dγK
dγ = 1
γ(K) 1K is a log-concave function.
Returning to our investigation of displacement convexity properties ofSn,
we note thatS n itself is displacement convex whenn= 1.
Theorem 4.11.The setS 1⊆W 2(R)is displacement convex. Therefore, in
particular,
e−D(µt∥γ)≥(1−t)e −D(µ0∥γ) +te−D(µ1∥γ),(61)
whenµ 0,µ 1 are even strongly log-concave probability measures.
Proof.Letµ 0,µ 1 ∈S 1. Denote byTthe optimal map pushing forward
µ0 toµ 1 guaranteed by Theorem 2.2. Thus, (T t)#µ0 =µ t,t∈[0,1], is
the displacement interpolation. Letfbe a continuously-differentiable odd
24 GAUTAM AISHWARYA AND LIRAN ROTEM
function supported within support(µ0). The main idea is to choose functions
ft such thatf ′
t =f′◦T−1
t . We let
ft(x) =
Z x
0
f′(T−1
t (y)) dy.(62)
Therefore,
Z
|ft|2 dµt =
Z
|ft(Tt(x))|2 dµ0(x) =
Z  Z Tt(x)
0
f′(T−1
t (y)) dy
!2
dµ0(x)
=
Z Z x
0
f′(z)T′
t(z) dz
2
dµ0(x) =
Z 
(1−t)
Z x
0
f′ +t
Z x
0
f′T′
2
dµ0,
(63)
which is clearly convex int. Thus,Z
|ft|2 dµt≤(1−t)
Z
|f0|2 dµ0 +t
Z
|f1|2 dµ1
≤(1−t)
Z
|f′
0|2 dµ0 +t
Z
|f′
1|2 dµ1 =
Z
|f′
t|2 dµt,
(64)
where we have used the fact that the integralZ
|f′
t|2 dµt =
Z
|f′◦T−1
t |2 dµt =
Z
|f′|2 dµ0 (65)
remains constant in timet. The one-to-one correspondence obtained by
the interpolation proceduref t among the test functions supported within
each support(µt) then concludes the proof of the first assertion. Given the
second assertion is about optimal transport between log-concave measures,
the regularity of the velocity required to draw the desired conclusion is
furnished by Caffarelli’s regularity theory ([16, 17]) and approximation.□
For higher dimensions, the fact that not all vector fields are conservative,
prevents us from finding the functionf t satisfying∇f t =∇f◦T −1
t . Yet, we
can derive some partial results.
Proposition 4.12.The following displacement convex subsets ofW 2(Rn)
lie completely inS n.
(1)The collection of all centered Gaussians whose covariance matrix is
dominated by the identity,{(Σ 1/2)#γ: 0<Σ≤I n×n}=:S n,G.
(2)Geodesic segments{µ t :t∈[0,1]}, when one endpoint is an even
strongly log-concave probability measure and the other isγitself.
Moreover, inequality(57)holds whenever both endpoints lie in any one of
these sets.
Proof.For the first set, use the following facts which are consequences of
the Brascamp–Lieb inequality and Theorem 2.2.
•Affine functions are the extremal functions in the Poincar´ e inequality
for Gaussian measures.
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 25
•The collection of the Gaussians considered in the proposition satisfy
the Poincar´ e inequality with constant 1.
•The collection of all centered Gaussian measures (that is, all linear
images of the standard Gaussianγ) is a displacement convex set.
We basically prove the convexity of the Poincar´ e constant in this case. Let
X0,X 1 be random vectors with distributions in the setS n,G. Then their
displacement interpolation is represented by a Gaussian random vectorXt =
(1−t)X 0 +tX 1, where (X 0,X 1) are optimally coupled. Supposef(x) =
⟨x,u⟩, for someu∈R n. Then,
Ef(Xt)2 =E⟨u,X t⟩2≤(1−t)E⟨u,X 0⟩2 +tE⟨u,X 1⟩2≤|u| 2 =E|∇f(X t)|2.
(66)
This completes the proof of the displacement convexity of the setS n,G. The
optimal transport map between Gaussian measures is linear ([28]), therefore
the velocity field has the regularity needed to deduce the inequality (57)
when both endpoints lie in this set.
For the second set, we will use Caffarelli’s contraction theorem ([18]),
which says that the optimal mapTfromµ 0 =γto a strongly log-concave
measureµ 1 is 1-Lipschitz. Therefore, theT t from Theorem 2.2 are also 1-
Lipschitz. A standard change of variables argument shows that the Poincar´ e
constant of a 1-Lipschitz image ofγcan be at most 1. This shows that all
theµ t in the second part of the proposition have Poincar´ e constants≤1.
We use (approximation and) Caffarelli’s regularity theory ([16, 17]) again to
obtain the required regularity of velocity fields to deduce inequality (57).
□
