---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-003-12-the-local-model
section_title: "The local model"
section_number: 1.2
pages: 10-17
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
Consider T = T ∗Sn with its standard forms ωT ∈ Ω 2(T ), θT ∈ Ω 1(T ). For
concrete computations we use the coordinates T ={(u,v )∈ Rn+1× Rn+1 :
⟨u,v⟩= 0,||v|| = 1}. For each λ >0, the subspace T (λ) of cotangent vectors
of length≤λ is an exact symplectic manifold. We write similarly T (0)⊂T for
the zero-section. The length function µ : T → R, µ(u,v ) = ||u||, generates a
Hamiltonian circle action σ on T\T (0) which, after identifying T ∼= TSn via
the standard metric, can be described as the normalized geod esic ﬂow on Sn.
In coordinates
σt(u,v ) = (cos(t)u− sin(t)||u||v, cos(t)v + sin(t) u
||u|| ).
σπ is the antipodal involution A(u,v ) = (−u,−v), hence extends continuously
over T (0) (unlike any σt, 0 < t < π). This can be used to deﬁne certain
symplectic automorphisms of T . The construction is by now well-known, but
we repeat it here since precise control over the parameters w ill be important
later on.
Lemma 1.8. Let R∈ C∞(R, R) be a function which vanishes for t≫ 0 and
which satisﬁes R(−t) = R(t)−kt for small |t|, with some k∈ Z. Let (φH
t )
be the Hamiltonian ﬂow of H = R(µ), deﬁned on T\T (0). Then φH
2π extends
smoothly over T (0) to a compactly supported symplectic automorphism φ of T .
The function K = 2π (R′(µ)µ−R(µ)) also extends smoothly over T (0), and
φ∗θT−θT =dK. (1.6)
Proof. Two Hamiltonians H1,H 2 which are both functions of µ always Poisson-
commute, so that φH1
t φH2
t =φH1+H2
t . Decomposing H intoH1 =R(µ)− (k/2)µ
and H2 = (k/2)µ, one gets
φH
2π =φH1
2π◦σkπ.
We may assume that R(−t) = R(t)−kt holds everywhere, since that can be
achieved by modifying R for negative values only, which does not aﬀect φ. Then
R(t)− (k/2)t is an even function, so it can be written as a smooth function o f
t2. This proves that H1 and its ﬂow extend smoothly over T (0). We know that
σkπ = Ak extends smoothly, so the same holds for φH
2π. Since H(y) vanishes
for points with µ(y)≫ 0, φ is compactly supported (one can show that the
compactly supported symplectic automorphisms which are ob tained in this way
are precisely those which are equivariant for the obvious O(n + 1)-action). The
10
function R′(t)t−R(t) is even, so K extends smoothly over T (0) for the same
reason as before. A computation shows that the Hamiltonian v ector ﬁeld X of
H satisﬁes L2πXθT =dK. Since H andK are both functions of µ,φH
t preserves
K, which implies (1.6).
Clearly, ifsupp(R)⊂ (−∞;λ) then φ restricts to a symplectic automorphism
ofT (λ) which is the identity near the boundary. (1.6) shows that th is is an exact
symplectic automorphism. In the case k = 1 we call these automorphisms model
Dehn twists , and generally denote them by τ ; any two of them are isotopic in
Sympe(T (λ)). An explicit formula is
τ (y) =
{
σ2πR′(µ(y))(y) y∈T (λ)\T (0),
A(y) y∈T (0), (1.7)
where the angle of rotation goes from 2 πR′(0) = π to 2πR′(λ) = 0. Note that
τ maps T (0) to itself, and is the antipodal map on it. If one considers T (0) as
an exact Lagrangian submanifold, with a function KT (0) =const. associated to
it, then by (1.1) and (1.6)
Kτ (T (0)) = (KT (0) +KτL|T (0))◦τ −1
L =KT (0)− 2πR(0). (1.8)
On occasion, it is useful to demand that the angle R′(t) does not oscillate too
much. We say that τ isδ-wobbly for some 0 <δ < 1/2 if R′(t)≥ 0 for all t≥ 0,
and R′′(t)< 0 for all t≥ 0 such that R′(t)≥δ.
Lemma 1.9. Suppose that τ is δ-wobbly. Let F0 =T (λ)y0, F1 =T (λ)y1 be the
ﬁbres of T (λ)→ Sn at points y0,y 1, whose distance in the standard metric is
dist(y0,y 1)≥ 2πδ. Then τ (F0) intersectsF1 transversally and at a single point
y, which satisﬁes
2πR′(||y||) = dist(y0,y 1).
In the special case where y1 = A(y0) one has y = y1; and then the tangent
space of T (λ) at y can be identiﬁed symplectically with Cn in such a way that
the subspaces tangent to τ (F0), T (0),F1 become respectively, Rn,e2πi/3Rn, and
eπi/3Rn.
Proof. Consider ﬁrst the case when y1⁄=A(y0). Suppose that y∈F1 is a point
with τ −1(y)∈ F0. By identifying T ∼= TSn and using the interpretation of
σ as normalized geodesic ﬂow, one sees that y must be a positive multiple of
c′(1), where c : [0; 1]→Sn is the minimal geodesic from c(0) = y0 to c(1) = y1.
Moreover, the angle of rotation must be 2 πR′(||y||) = ||c′(1)|| = dist(y0,y 1).
These two conditions are also suﬃcient. δ-wobblyness implies that 2 πR′(t) =
dist(y0,y 1) has exactly one solution t > 0, which proves that there is exactly
one y. Combine the two conditions above into one, c′(1) = 2πR′(||y||)(y/||y||).
Taking the derivative, one sees that a vector Y ∈ T (F1)y∼= T (Sn)y1 satisﬁes
(Tτ )−1(Y )∈T (F0) iﬀ
R′′(||y||)⟨y
||y||,Y⟩y
||y|| +R′(||y||)
(
Y−⟨y
||y||,Y⟩y
||y||
)
= 0.
11
We know that R′(||y||)≥ δ; by δ-wobblyness this implies R′′(||y||) < 0, which
shows that Y = 0. Therefore y∈τ (F0)∩F1 is a transverse intersection point.
Now consider the case wheny1 =A(y0). Then y =y1 clearly lies inτ (F0)∩F1,
and because R′(t) < 1/2 for all t >0, there is no other intersection point. In
the notation from the proof of Lemma 1.8, τ (F0) = φH1
2π (A(F0)) = φH1
2π (F1),
and y is a stationary point of ( φH1
t ). It follows that T (τ (F0))y is the image of
T (F1)y under the time 2 π map of the linear Hamiltonian ﬂow generated by the
quadratic form 1
2Hess(H1)y. If one identiﬁes the tangent space to T at y with
T (Sn)y⊕T (Sn)y in such a way that the ﬁrst summand is T (F1)y, then
Hess(H1)y =
(
R′′(0)·I 0
0 0
)
.
Taking some isomorphism T (Sn)y ∼= Rn and its complexiﬁcation T (Sn)y⊕
T (Sn)y∼= Cn, one ﬁnds that the tangent spaces of τ (F0), T (0), and F1 at y
correspond respectively to
(1 + 2πiR′′(0))Rn, iRn, Rn⊂ Cn. (1.9)
In particular, since R′′(0) < 0 by δ-wobblyness, the intersection τ (F0)∩F1 is
transverse. At this point we need to recall a fact from symple ctic linear alge-
bra, see e.g. [13, p. 40]: the classiﬁcation of triples of mut ually transverse linear
Lagrangian subspaces, up to the action of Sp(2n), is equivalent to the classiﬁ-
cation of nondegenerate quadratic forms on Rn, up to GL(n, R). In particular
there is a ﬁnite number of equivalence classes, and deformin g a triple continu-
ously while keeping transversality will not change its equi valence class. One can
clearly deform the three subspaces (1.9) in this way to Rn, e2πi/3Rn, eπi/3Rn,
which proves the last part of the statement.
The next result links model Dehn twists to exact Lefschetz ﬁb rations. The
connection has been known to algebraic geometers for a very l ong time, as
attested by the terminology “Picard-Lefschetz transforma tions” used for model
Dehn twists. But while the traditional approach ignores sym plectic forms, they
are of course crucial for our purpose.
Lemma 1.10. Fix λ > 0 and r > 0, and let ¯D(r)⊂ C be the closed disc of
radius r around the origin. There is an exact Lefschetz ﬁbration (E,π ) over
¯D(r), together with a diﬀeomorphism φ : Er→ T (λ) which respects both the
symplectic forms and the exact one-forms, such that the foll owing holds. Denote
by ρ∈ Sympe(Er) the symplectic monodromy around ∂ ¯D(r), in positive sense.
Then τ =φ◦ρ◦φ−1∈ Sympe(T (λ)) is a model Dehn twist.
Proof. Take Cn+1 with its standard forms ωCn+1, θCn+1 and the function q :
Cn+1→ C, q(x) = x2
1 +··· +x2
n+1. Even though ( Cn+1,q ) is clearly not an
exact Lefschetz ﬁbration (its ﬁbres are not even compact), m uch of what was
said in the previous section carries over to it. The horizont al subspaces
T (Cn+1)h
x ={X∈ Cn+1 : ωCn+1(X, kerDqx) = 0} = C¯x (1.10)
12
deﬁne a symplectic connection away from the critical point x = 0, so that one
has parallel transport maps q−1(c(a))→ q−1(c(b)) along paths c : [a;b]→ C∗.
Consider the family of Lagrangian spheres
Σ z =√zSn ={(√zy1,..., √zyn+1) : y∈Sn⊂ Rn+1}⊂ q−1(z), (1.11)
z⁄= 0, which for z→ 0 degenerate to Σ 0 ={0}⊂ q−1(0). Write Σ ∗ for the
union of all Σ z, z⁄= 0, and Σ = Σ ∗∪ Σ 0. One computes that
θCn+1| Σ ∗ =q∗dc(− 1
4|z|). (1.12)
Actually, the precise formula does not matter much for the mo ment. All we
need is that ωCn+1| Σ ∗ is the pullback by q of some two-form on C∗, since that
implies that parallel transport in any direction in C∗ takes the Σ z into each
other; compare Lemma 1.3. The next observation is that if one removes Σ then
parallel transport can be extended even to the singular ﬁbre , so that for any
pathc in C one has a canonical symplectic isomorphism
q−1(c(a))\ Σ c(a)→q−1(c(b))\ Σ c(b).
Since taking out Σ 0 removes the critical point, the only possible problem is
that a point in Cn+1\ Σ might move in horizontal direction and converge to
some point of Σ, which means that the ﬂow of some horizontal ve ctor ﬁeld
would not be deﬁned for all time. However, that cannot happen since there is a
function, h(x) =||x||4−|q(x)|2, which satisﬁes dhx(C¯x) = 0, hence is constant
horizontally, and with h−1(0) = Σ. Therefore one can use parallel transport in
radial direction to trivialize q : Cn+1\ Σ −→ C symplectically. In particular, if
˜ρs :q−1(s)→q−1(s) is the monodromy along the circle of radius s> 0 around
the origin, ˜ρs| (q−1(s)\ Σ s) will be isotopic to the identity in the group of all
symplectic automorphisms of q−1(s)\ Σ s. We have mentioned all this mainly
to motivate the subsequent proof, which is more computation al.
Consider the map
Φ : Cn+1\ Σ −→ C× (T\T (0)),
Φ( x) = (q(x),σα/2(−im(ˆx)||re(ˆx)||, re(ˆx)||re(ˆx)||−1)),
(1.13)
whereseiα =q(x) are polar coordinates on the base, and ˆx =e−iα/2x. We claim
that this is a diﬀeomorphism ﬁbered over C. First of all, because of the use of
polar coordinates, it is not obvious that Φ is well-deﬁned an d smooth at q−1(0)\
Σ 0. To dispel any doubts about that one writes, after some manip ulations,
Φ( x) =
(
q(x),− 1
2 im(x)β(x)− 1
2 im(q(x)x)β(x)−1,
h(x)−1/2re(x)β(x)−h(x)−1/2re(q(x)x)β(x)−1)
,
where β(x) = ( ||x||2 +h(x)1/2)1/2. The fact that Φ is a diﬀeomorphism on
each ﬁbre is easy to see, either directly or by using the sympl ectic forms and
13
(1.14) below. Moreover, if one restricts Φ to a ﬁbre over s > 0, it extends to
a diﬀeomorphism φs :q−1(s)→ T . Such an extension does not exist for other
ﬁbres, due to the non-continuity of σ at T (0). A computation yields
(Φ −1)∗θCn+1 =θT− ˜Rs(µ)dα, ˜Rs(t) = 1
2t− 1
2
(
t2 +s2/4
) 1/2
. (1.14)
This implies that the restriction of Φ to any ﬁbre is symplect ic, and actually
maps the respective one-forms into each other. Of course, th e same will then
be true for the continuous extensions φs, s > 0. In fact (1.14) shows even
more: if one restricts to any ray α = const. in the basis then Φ ∗ωT = ωCn+1,
which means that Φ trivializes the symplectic parallel tran sport on ( Cn+1\ Σ ,q )
in radial directions, in accordance with the strategy which we set out before.
Consider ˜τs =φs◦ ˜ρs◦φ−1
s :T→T , where ˜ρs is the monodromy map introduced
above. From (1.14) it follows that ˜ τs restricted to T\T (0) is the time 2 π map
of the Hamiltonian ˜Hs = ˜Rs(µ). Since ˜Rs(−t) = ˜Rs(t)−t, this is quite close to
the case k = 1 of Lemma 1.8. The diﬀerence is that ˜Rs(t) does not vanish for
t≫ 0. Instead, it decays as follows:
0> ˜Rs(t)≥− 1
16s2t−1, 0< d
dt
˜Rs(t)≤ 1
16s2t−2. (1.15)
This is good enough to imply that ˜ τs is asymptotic to the identity at inﬁnity,
for each s > 0. It remains to tweak the given data slightly, so as to produc e
a honest exact Lefschetz ﬁbration, whose monodromy is an act ual model Dehn
twist.
Fixλ> 0,r> 0. Choose a cutoﬀ function g∈C∞(R+, R) such thatg′(t)≥ 0
everywhere, g(t) = 0 for small t, and g(t) = 1 if t is close to λ. We claim that
there is a unique γ∈ Ω 1(Cn+1) with, again in polar coordinates on the base,
(Φ −1)∗γ =g(µ) ˜Rs(µ)dα. (1.16)
Since ˜R0(t) = 0, the function ˜Rs(t)/s extends smoothly to s = 0, t ⁄= 0.
Therefore the right hand side of (1.16) can be written as g(µ)( ˜Rs(µ)/s)sdα,
which means thatγ is smooth at least on Cn+1\Σ. Now µ(Φ( x)) = (1/2)h(x)1/2;
since Σ = h−1(0) and g(t) = 0 for small t, one sees that Φ ∗(g(µ) ˜Rs(µ)dα)
vanishes near Σ, so that γ extends by zero over Σ. Set



E = Φ −1( ¯D(r)× (T (λ)\T (0)))∪ (Σ ∩q−1( ¯D(r))),
π =q|E :E−→ ¯D(r),
Θ = ( θCn+1 +γ)|E, Ω = dΘ ,
φ =φr|Er :Er−→T (λ).
(1.17)
E⊂ Cn+1 is cut out by the inequalities h(x)≤ 4λ2,|q(x)|≤ r. This makes
it easy to show that it is a compact manifold with corners, who se boundary
faces are ∂vE = π−1(∂ ¯D(r)) and ∂hE ={h(x) = 4 λ2} ={µ(Φ( x)) = λ} =
Φ −1( ¯D(r)×∂T (λ)). Because γ vanishes when restricted to any ﬁbre, Ω |TEv
x =
ωCn+1|kerDqx is nondegenerate for all x. In
Θ | (E\ Σ) = Φ ∗(θT + (g(µ)− 1) ˜Rs(µ)dα) (1.18)
14
the second term on the right hand side vanishes close to ¯D(s)×∂T (λ), so that
Φ provides a trivialization near ∂hE in the sense introduced in the previous
section. Moreover, since γ vanishes near the critical point x = 0, equipping
E with the standard complex structure J0 near that point, and ¯D(r) with the
standard complex structure j0, turns ( E,π ) into an exact Lefschetz ﬁbration.
As for the statement about the monodromy ρ, one can repeat the argument
above, using (1.18) instead of (1.14). This shows that τ = φ◦ρ◦φ−1, when
restricted to T (λ)\T (0), is the time 2 π map of Rr(µ), where
Rr(t) = (1−g(t)) ˜Rr(t); (1.19)
by deﬁnition, this is a model Dehn twist.
Let (M,ω,θ ) be an exact symplectic manifold. A framed3 exact Lagrangian
sphere is an exact Lagrangian submanifold L⊂M together with an equivalence
class [f ] of diﬀeomorphisms f :Sn→L. Here f1,f 2 are equivalent iﬀ f −1
2 f1 can
be deformed inside Diﬀ( Sn) to an element of O(n + 1). To any such (L, [f ]) one
associates a Dehn twist τ(L,[f ])∈ Sympe(M ) as follows. Choose a representative
f and extend it to a symplectic embedding ι :T (λ)→M for some λ> 0. Take
a model Dehn twist τ which is supported in the interior of T (λ), and deﬁne
τ(L,[f ]) =
{
ι◦τ◦ι−1 on im(ι),
id elsewhere.
The exactness of τ(L,[f ]) follows from that of L; moreover, the analogue of (1.8)
holds. It is not diﬃcult to show that the isotopy class [ τ(L,[f ])]∈π0(Sympe(M ))
is independent of the choices made in the deﬁnition. In contr ast, it is unknown
whether a change of the framing [ f ] can aﬀect [ τ(L,[f ])]; if the answer is negative
the notion of framing could be dropped altogether, but while the question is
open one cannot do without it. Still, for the sake of brevity w e will often omit
framings from the notation and write τL instead of τ(L,[f ]). We will say that τL
is δ-wobbly if the local model it is constructed out of has this pr operty.
Proposition 1.11. Let (L, [f ]) be a framed exact Lagrangian sphere in M . Fix
some r >0. There is an exact Lefschetz ﬁbration (EL,πL) over ¯D(r) together
with an isomorphism φL :EL
r →M of exact symplectic manifolds, such that if
ρL is the symplectic monodromy around ∂ ¯D(r), then τL =φL◦ρL◦ (φL)−1 is a
Dehn twist along (L, [f ]).
We will prove this under the assumption that there is an embed ding ι :
T (λ)→M as before, with ι∗θ =θT . This is not really a restriction, since one
can always satisfy it by adding the derivative of a function t oθ, which does not
change M up to exact symplectic isomorphism. On the other hand, it all ows
us to make the statement slightly sharper: φL will map the one-forms on EL
r
and M into each other, and the Dehn twist obtained from the monodro my of
(EL,πL) will be one constructed using the given embedding ι.
3This has little or nothing to do with the usual topological no tion of framed manifold.
15
Proof. Take (E,π ) and φ from Lemma 1.10, with the given r and λ. We will
construct (EL,πL) by attaching a trivial piece to ( E,π ). By construction, there
is a neighbourhood N⊂E of ∂hE, a neighbourhood V of ∂T (λ) in T (λ), and
a diﬀeomorphism Φ : N→ ¯D(r)×V ﬁbered over ¯D(r), such that Θ |N = Φ ∗θT .
Moreover, Φ agrees with φ on N∩Er. Set
EL =E∪∼ ¯D(r)× (M\ι(T (λ)\V )),
where∼ identiﬁes N with ¯D(r)×ι(V ) through (id×ι)◦ Φ. One similarly deﬁnes
πL fromπ and the projection ¯D(r)×M→ ¯D(r). The forms Ω L, Θ L onEL come
from the corresponding ones on E and the pullbacks of ω,θ on the trivial part.
φL is constructed from ι◦φ and the identity map. The complex structure near
the critical point and critical value are inherited from E. All properties stated
above are obvious from the construction and the deﬁnition of Dehn twists.
We call the ( EL,πL) standard ﬁbrations . For future reference, we will now
state certain properties which these ﬁbrations inherit fro m the local model
(E,π ), and which depend on the details of its construction.
Lemma 1.12. Any standard ﬁbration (EL,πL) has the following properties.
(i) There is a closed subset Σ L⊂EL such that
Σ L
z = Σ L∩EL
z =
{
is an embedded n-sphere if z⁄= 0,
is the unique critical point x0∈EL
0 if z = 0.
In fact (Σ L)∗ = Σ L\ Σ L
0 is a smooth n-sphere bundle over ¯D(r)\{ 0}, and
satisﬁes
Θ L| (Σ L)∗ = (πL)∗dc(− 1
4|z|). (1.20)
As in the discussion following (1.12), this implies that each Σ L
z ⊂ EL
z ,
z⁄= 0 , is an exact Lagrangian submanifold, and that symplectic pa rallel
transport within ¯D(r)\{0} carries these spheres into each other. Moreover,
φL(Σ L
r ) = L.
(ii) There are holomorphic Morse charts (ξ, Ξ) around the unique critical point
x0∈ EL
0 , such that ξ is the inclusion֒→¯D(r) of some neighbourhood
U⊂ C of the origin; Ξ ∗Θ L =θCn+1 and Ξ ∗Ω L =ωCn+1; and Ξ −1(Σ L
z ) =
Σ z for all suﬃciently small z∈ C.
(iii) (EL,πL) has nonnegative curvature.
(iv) τL =φL◦ρL◦ (φL)−1 is the Dehn twist deﬁned using ι and the function
Rr from (1.19); in particular Rr(0) =−r/4. By making r smaller while
keeping all other choices in the construction ﬁxed, one can a chieve that τL
is δ-wobbly for an arbitrary δ.
16
Proof. (i) From (1.17) one sees that Σ ∩q−1( ¯D(r))⊂E, and that Θ = θCn+1 in
a neighbourhood of that subset. Σ L is deﬁned to be the image of this in EL, so
that (1.20) is a consequence of (1.12). (ii) The deﬁnition of ξ, Ξ is obvious, and
the claim about Ξ ∗Θ L follows from the fact that in (1.17) Θ = θCn+1 near the
critical point. (iii) One can compute the curvature of ( E,π ) from (1.14) and
(1.16); it turns out to be
Φ ∗(
(g(µ)− 1) ∂
∂s
˜Rs(µ)
)
ds∧dα,
which is≥ 0 everywhere. This implies the same property for ( EL,πL). (iv) The
nontrivial statement is δ-wobblyness, which requires that we take another look
at the function Rr. There is a t0 > 0 such that g(t) = 0 for t∈ [0;t0], and in
that interval Rr(t) = ˜Rr(t), so that ( ∂/∂t )Rr(t) > 0, (∂2/∂t2)Rr(t) < 0. For
t∈ [t0;λ] one estimates using (1.15) that
0≤ ∂
∂tRr(t) =−g′(t) ˜Rr(t) + (1−g(t))∂
∂t
˜Rr(t)≤ r2
