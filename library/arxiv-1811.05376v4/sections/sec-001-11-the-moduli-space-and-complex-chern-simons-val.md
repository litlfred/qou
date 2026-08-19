---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-001-11-the-moduli-space-and-complex-chern-simons-val
section_title: "The moduli space and complex Chern-Simons values"
section_number: 1.1
pages: 6-15
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
Wenowbeginourinvestigationof M(X, SL(2, C)),whichcloselyfollows[23]. Wehavethefollowing
presentation of the fundamental group ofX
π1(X)≃
⟨
h,x 1,...,x n|x1x2··· xn,xpj
j h−qj, [xj,h ],j = 1,...,n
⟩
.
LetusﬁrstrecallafewofFintushelandStern’sresultsconcerningthemodulispace M(X, SU(2))
establish in [23]. AsX is an integral homology sphere, the only reducible representation intoSU (2)
is the trivial one. For an irreducible representationρ :π1(X)→ SU(2) at mostn− 3 of theρ(xj)
are±I, and if exactlyn−m of theρ(xj) are equal to±I, then the component ofρ inM(X, SU(2))
is of dimension2(n−m)− 6.
Let L(p1,...,p n)⊂ Nn be the the set ofn-tuples l = (l1,...,l n) which satisﬁes the following
condition. We have0≤l1≤p1 and 0≤lj≤ pj−1
2 , for j = 2,...,n and there exists at least three
distinct j1 < j2 < j3 with ljt⁄= 0 for t = 1, 2, 3. The following proposition is an adaptation and
generalization of Lemma2 in [7] and Lemma2.1 and Lemma 2.2 in [23].
Proposition 5. Let l = (l1,l 2,...,l n)∈ L(p1,...,p n). Then there exists matricesQj ∈ SL(2, C)
and a representationρl :π1(X)→ SL(2, C) with
ρl(x1) =Q1
(
e
πil1
p1 0
0 e−πil1
p1
)
Q−1
1 , ρ l(xj) =Qj

e
2πilj
pj 0
0 e
−
2πilj
pj

Q−1
j
for j = 2,...n . In fact we can chooseQj =I for j⁄=j2,j 3.
Furthermore we can choose theQj’s such that
ρl :π1(X)→ SL(2, R)
Resurgence Analysis of Quantum Invariants 7
or
ρl :π1(X)→ SU(2)
depending on properties ofl. For any non-trivial representationρ :π1(X)→ SL(2, C) there exists
l′∈ Nn such thatpj divides l′
j for at mostn− 3 of the indicesj = 1, 2, 3,...,n and such thatρ is
of the form
ρ(x1) =S1

e
πil′
1
p1 0
0 e−
πil′
1
p1

S−1
1 , ρ (xj) =Sj

e
2πil′
j
pj 0
0 e
−
2πil′
j
pj

S−1
j (19)
for someS1,...,S n∈ SL(2, C).
Finally we have that the map which associatesl∈L(p1,...,p n) to a non-trivial representation
ρ :π1(X)→ SL(2, C) via (19) induces an isomorphism
π0(M∗(X, SL(2, C)))∼=L(p1,...,p n)
The family of Brieskorn integral homology spheres (n = 3) is very special due to the fact that
the moduli spaceM(Σ(p1,p 2,p 3), SL(2, C)) is ﬁnite with cardinality given by theSL(2, C) Casson
invariant introduced by Curtis [16, 17]
λSL(2,C)(Σ(p1,p 2,p 3)) = (p1− 1)(p2− 1)(p3− 1)/4.
This is shown by Boden and Curtis [7]. Prior to this and in relation to Floer homology, Fintuschel
and Stern [23] analyzed theSU(2) moduli spaceM(X, SU(2)) of the Seifert ﬁbered three mani-
fold X considered in this paper and their work shows that the components are even dimensional
manifolds with top dimension 2n− 6. This is in stark contrast to the ﬁniteness of the moduli
spaceM(Σ(p1,p 2,p 3), SL(2, C)). In the three ﬁbered case Kitano and Yamaguchi [38] has gives a
decomposition
M(Σ, SL(2, C)) =M(Σ, SL(2, R))
⋃
M(Σ,U(1))
M(Σ, SU(2)).
Where Σ = Σ( p1,p 2,p 3). Here we can observe the following generalization of this work as an
imidiate corollary of Proposition 5.
Theorem 6. The natural inclusion
M(X, SL(2, R))⊔M(X,U(1))M(X, SU(2))→M (X, SL(2, C))
induces an isomorphism on the level ofπ0
π0(M(X, SL(2, R))⊔M(X,U(1))M(X, SU(2)))∼=π0(M(X, SL(2, C))).
By this corollary we can in particular conclude that all Chern-Simons values are real and they
only depend onl∈L(p1,...,p n). In Proposition 7 below we actually provide an explicit formula.
Before commencing the proof let us introduce the following notation
exp(x) =
(
ex 0
0 e−x
)
,
which should not cause any ambiguities as long as the context shows that we are dealing with a
matrix.
Proof. We start with the construction ofρl. Introduce the matrices
X1 = exp(πil1/p1), X j = exp(2πilj/pj)
for j∈{ 2,....,n}\{ j2,j 3}. Rewrite the relation∏n
j=1xj = 1 as the equivalent relation
xj3+1··· xnx1··· xj1··· xj2··· xj3−1 =x−1
j3 .
Resurgence Analysis of Quantum Invariants 8
Assume we can chosenQj2,Qj3∈ SL(2, C) such that
Xj3+1··· XnX1··· Xj1··· Qj2Xj2Q−1
j2 ··· Xj3−1 =Q−1
j3 X−1
j3 Qj3. (20)
TakingQj =I for j /∈{j2,j 3}, we can deﬁneρ :π1(X)→ SL(2, C) by the assigment
ρ(xj) =QjXjQ−1
j , ρ(h) =Xp1
1 .
To see this, observe thatB := Xp1
1 = (−I)l1 is central and asq1 is odd whereasqj is even for
j≥ 2, we also haveXpj
j =Bqj,∀j. The last relation inπ1(X) is ensured by (20). Observe that it
will suﬃce to chooseQj2∈ SL(2, C) such that
tr
(
Xj3+1··· XnX1··· Xj1··· Qj2Xj2Q−1
j2 ··· Xj3−1
)
= 2 cos
(2πlj3
pj3
)
(21)
because this will ensure that there exists someQj3∈ SL(2, C) with the property that
Qj3Xj3+1··· XnX1··· Xj1··· Qj2Xj2Q−1
j2 ··· Xj3−1Q−1
j3 =Xj3,
since non-diagonalizable elements of SL(2, C) have trace±2, given that the unit determinant
condition implies that the unique eigenvalue with multiplicity two for such elements must be either
1 or−1 and we have that
2
⏐⏐⏐⏐cos
(2πlj3
pj3
)⏐⏐⏐⏐< 2.
For (21) we used our assumption onj3. Write
Xj3+1··· XnX1··· Xj1··· Xj2−1 = exp(ia),
Xj2 = exp(ib),
Xj2+1··· Xj3−1 = exp(ic),
Xj3 = exp(id).
We observe that by the conditions on(lj2,pj2) and (lj3,pj3) we have that
b,d /∈πZ.
Let Qj2 = ˜Q where
˜Q = ˜Q(u,v,w,z ) =
(u v
w z
)
for u,v,w,z to be chosen below. Assumeuz−vw = 1 so that ˜Q∈ SL(2, C). We compute
Xj3+1··· XnX1··· Xj1··· Xj2−1 ˜QXj2
˜Q−1Xj2+1··· Xj3−1
=
(zuei(a+b+c)−wvei(a−b+c) −uvei(a+b−c) +uvei(a−b−c)
zvei(b+c−a)−zwei(c−a−b) −vwe−i(a+b+c) +zuei(b−a−c)
)
.
Thus we have that
tr
(zuei(a+b+c)−wvei(a−b+c) −uvei(a+b−c) +uvei(a−b−c)
zwei(b+c−a)−zwei(c−a−b) −vwe−i(a+b+c) +zuei(b−a−c)
)
= 2zu cos(a +b +c)− 2wv cos(a +c−b).
It follows that we must solve
(cos(a +b +c) cos( a +c−b)
1 1
)( zu
−wv
)
=
(2 cos(d)
1
)
. (22)
Using the trigonometric identitycos(x +y)− cos(x−y) =−2 sin(x) sin(y) we get
det
(cos(a +b +c) cos( a +c−b)
1 1
)
= cos((a +c) +b)− cos((a +c)−b)
=−2 sin(a +c) sin(b).
Resurgence Analysis of Quantum Invariants 9
Thus it remains to arguea +c /∈πZ andb /∈πZ. Assume towards a contradiction thata +c =πm
for somem∈ Z. Hence we would haveP (a +c) =Pmπ for some integerm, which would imply
lj12ϵ ∏
t⁄=j1
pt = 0 mod pj1
for ϵ∈{ 0, 1}, with ϵ = 0 for j1 = 1 and ϵ = 0 otherwise. This is a contradiction, as2ϵ∏
t⁄=j1pt is
invertible in Z/pj1 Z and 1≤ lj1≤ (pj1− 1)/2ϵ. We see thatb /∈ πZ directly from the conditions
on lj2. Thus we can solve (22), and hence ﬁnd the neededu,v,w,z , which concludes the proof of
the ﬁrst part of the proposition.
Let us now prove that we can actually choose the Qj’s such that we obtain anSL(2, R)-
representation. We will denote this new choice of the Qj by QR
j. We set QR
j = Q for j ∈
{1,...j 2− 1,j 3 + 1,...,n }, where
Q =
√
2
2
( 1 −i
−i 1
)
.
which has the following property
Q exp(a)Q−1 =
(cos(a) − sin(a)
sin(a) cos( a)
)
.
Introduce the notation ˜Xj =QXjQ−1 and observe by the above computations that
tr( ˜Xj3+1··· ˜Xn ˜X1··· ˜Xj1··· ˜Xj2−1Q ˜QXj2(Q ˜Q)−1) =
tr(Xj3+1··· XnX1··· Xj1··· Xj2−1 ˜QXj2
˜Q−1) =
= 2zu cos(a +b)− 2wv cos(a−b).
To understand which values, sayt, this trace can take, we consider in analogy with (22) the
equation (cos(a +b) cos( a−b)
1 1
)( zu
−wv
)
=
(t
1
)
. (23)
The determinant isD =−2 sin(a) sin(b), which is non-vanishing sincea,b /∈ πZ. Then we have
that ( zu
−wv
)
= 1
D
( t− cos(a−b)
−t + cos(a +b)
)
.
Fort∈ R we observe thatzu∈ R and wv∈ R. Now we compute
Q ˜QXj2(Q ˜Q)−1 =((uz−wv) cos(b) + (uv +wz) sin(b) ( −(uz +wv)−i(uv−wz)) sin(b)
((uz +wv)−i(uv−wz)) sin(b) ( uz−wv) cos(b)− (uv +wz) sin(b)
)
.
From which we see that
Q ˜QXj2(Q ˜Q)−1∈SL(2, R)
if and only if
Im(uv +wz) = 0, Re(uv−wz) = 0
or equivalently
uv =wz
whenevert∈ R. But then this implies that
|u|2|v|2 = (t− cos(a +b))(t− cos(a−b))
D2 .
Which we can solve whent> cos(a±b) by letting
u =
√
t− cos(a +b)
D , v =
√
t− cos(a−b)
D
Resurgence Analysis of Quantum Invariants 10
and then
z =
√
t− cos(a +b), w =
√
t− cos(a−b)
and whent< cos(a±b) then we can take
u =
√
cos(a +b)−t
D , v =
√
cos(a−b)−t
D
and then
z =
√
cos(a +b)−t, w =
√
cos(a−b)−t.
This allows us to complete the construction as follows. First we assume thata,c /∈πZ. For
˜Qi = ˜Q(ui,vi,wi,zi)
for i = 1, 2 we consider the equation
[
˜Xj3+1··· ˜Xn ˜X1··· ˜Xj1··· Q ˜Q1Xj2(Q ˜Q1)−1
]
=
[(
˜Xj2+1... ˜Xj3−1Q ˜Q2Xj3(Q ˜Q2)−1
)−1]
which is equivalent to
tr
(
˜Xj3+1··· ˜Xn ˜X1··· ˜Xj1··· Q ˜Q1Xj2(Q ˜Q1)−1
)
= tr
(
˜Xj2+1... ˜Xj3−1Q ˜Q2Xj3(Q ˜Q2)−1
)
since these are certainly allSL(2, C) matrices. But now, using that we also have thatc,d /∈ πZ,
we can choset bigger than cos(a±b) and cos(c±d) and ﬁx˜Qi as above such that
tr
(
˜Xj3+1··· ˜Xn ˜X1··· ˜Xj1··· Q ˜Q1Xj2(Q ˜Q1)−1
)
=t (24)
and
tr
(
˜Xj2+1... ˜Xj3−1Q ˜Q2Xj3(Q ˜Q2)−1
)
=t (25)
Thus we can now conclude that there existQR∈ SL(2, R) such that
˜Xj3+1··· ˜Xn ˜X1··· ˜Xj1··· Q ˜Q1Xj2(Q ˜Q1)−1 =
QR
(
˜Xj2+1... ˜Xj3−1Q ˜Q2Xj3(Q ˜Q2)−1
)−1
(QR)−1 =
QRQ ˜Q2X−1
j3 (QRQ ˜Q2)−1QR ˜X−1
j3−1(QR)−1...Q R ˜X−1
j2+1(QR)−1.
Thus if we further set
QR
j2 =Q ˜Q1,Q R
j3 =QRQ ˜Q2
and
QR
j =QRQ
for j∈{ j2 + 1,...,j 3− 1}, then we have found the needed conjugation to obtain anSL(2, R)-
representation. Let us now consider the remanning cases. Suppose thata∈πZ butc /∈πZ. Then
the common tracet is by (24) forced to beeia cosb, so we can solve (25) if and only ifeia cosb is
not contained in the interval spanned by the two valuescos(c±d). If this is the case we proceed
with the argument as above. If on the other handeia cosb is contained in the interval spanned
by cos(c±d), then it is well known that we can chooseQj ∈ SU(2) so as to obtain anSU(2)-
representation. A similar argument of course works in the case wherec∈ πZ but a /∈ πZ. If we
havea,c∈πZ, thena +c∈πZ, but this we have already argued is impossible.
Now letρ :π1(X)→ SL(2, C) be an arbitrary non-trivial representation. As remarked before
any non-trivial representation is irreducible sinceX is an integral homology three sphere. Since
ρ(h) commutes with the image ofρ, we see thatρ(h) =±I. Hence the relationxpj
j =hqj implies
that ρ(xj)pj =±I, and forj = 2,...,n we must haveρ(xj)pj =I, since qj is even. Henceρ must
be of the form (19) for somel′∈ Nn. It only remains to argue that at mostn− 3 of theρ(xj) are
±I. If not, the relationx1x2··· xn = 1 implies that there isj1 <j 2 withρ(xj1)ρ(xj2) =±I. Aspj1
and pj2 are relatively coprime, this is only possible ifρ(xj1) =±I and ρ(xj2) =±I. This would
Resurgence Analysis of Quantum Invariants 11
imply thatρ(π1(X))⊂{± 1} = Z(SU(2)) which contradicts the fact thatρ is irreducible since it
was assumed non-trivial.
Wedescribetheconnectedcomponentsof M∗(X, SL(2, C)). Firstweassumethat l1∈{ 1,...p 1−
1} and l2 > 0 for an l∈ L(p1,...,p n). We will now prove that the subsetM∗
l (X, SL(2, C)) of
M∗(X, SL(2, C)) consisting of conjugacy classes of representationsρ for which
tr(ρ(x1)) = 2 cos(πl1/p1), tr(ρ(xj)) = 2 cos(2πlj/pj), j = 2,...n
is connected. Let
T =
n
×
j=3
[
exp
(2πilj
pj
)]
.
It is obvious thatT is connected. Let nowm : T→ SL(2, C) be the algebraic product map. Let
P⊂ SL(2, C) be the set of non-diagonalizable elements inSL(2, C) and observe thatP has complex
co-dimension one, thus so doesm−1(P )⊂ T, but then it follows thatT′ = T−m−1(P ) is also
connected. For any
(M3,...,M n)∈T′,
we observe that the set of(Q1,Q )∈ SL(2, C) which solves
exp(πl1/p1)Q1 exp(2πl2/p2)Q−1
1 =QM−1
n ...M −1
3 Q−1 (26)
is non empty and connected since it is acted transitively on by (C∗)2× C∗, where the ﬁrst
factor comes from the ambiguity from solving (23) and the second comes from the stabiliser of
M−1
n ...M −1
3 under conjugation. But then we see that an open dense subset ofM∗
l (X, SL(2, C))
is connected, thusM∗
l (X, SL(2, C)) it self must be connected. Ifl1∈{ 0,p 1} orl2 = 0, we proceed
as follows. Choosej1,j 2∈{ 1,...,n − 2} such that
a =πl1
p1
+ 2π
j1∑
j=2
lj
pj
, b = 2π
j2∑
j=j1+1
lj
pj
,
has the property thata,b /∈πZ. Now consider the equation
exp(a)Q1 exp(b)Q−1
1 =QM−1
n ...M −1
j2+1Q−1. (27)
The connectedness is now argued in exactly the same way, with (27) in place of (26).
For an SL(2, C)-connection a in the trivialSL(2, C)-bundle onX we recall the Chern-Simons
action is given by
SCS(a) = 1
8π2
∫
X
tr
(
a da + 2
3a3
)
mod Z.
We now compute the Chern-Simons values of the representations constructed above.
Proposition7. For any representationρ :π1(X)→SL(2, C), deﬁnel = (l1,...,l n)∈L(p1,...,p n),
so that
tr(ρ(x1)) = 2 cos(πl1/p1), tr(ρ(xj)) = 2 cos(2πlj/pj), j = 2,...n.
Then we have that
SCS (ρ) =−P
4

l1
p1
+
n∑
j=2
2lj
pj


2
mod Z. (28)
Formula (28) was proven forSU(2) connections by Kirk and Klassen and it is stated in Theorem
5.2in [37]. It is proven using the following general result. LetM be a closed oriented three manifold
containing a knotK. LetY be the complement of a tubular neighborhood ofK inM. With respect
to an identiﬁcationM\Y ≃ D2×S1, choose simple closed curvesµ,λ on ∂Y intersecting in a
single point such thatµ bounds a disc of the formD2×{ 1}. Let ρt : π1(Y )→ SU(2) be a path
of representations such thatρ0(µ) = ρ1(µ) = 1, and for which there exists continuous piecewise
diﬀerentiable functions
α,β :I→ R
Resurgence Analysis of Quantum Invariants 12
with
ρt(µ) =
(e2πiα(t) 0
0 e−2πiα(t)
)
, ρt(λ) =
(e2πiβ(t) 0
0 e−2πiβ(t)
)
.
Thinking ofρ1,ρ 0 as ﬂat connections onM we have
SCS(ρ0)− SCS(ρ1) =−2
∫ 1
0
β(t)α′(t) dt mod Z. (29)
Notice that formula (29) diﬀers from the corresponding formula in [37] by a sign. This discrepancy
was already discussed by Freed and Gompf in [24] and is due to a sign convention. See the footnote
on page98 in [24]. The formula (29) was also used in the work [3] by the ﬁrst author and Hansen.
Proof of Proposition 7.Let K⊂ X be the n’th exceptional ﬁber. LetY be the complement of
a tubular neighborhood ofK in X. Removing K has the eﬀect onπ1 of removing the relation
xpn
n =h−qn, i.e. we have a presentation
π1(Y )≃
⟨
h,x 1,...,x n|x1x2··· xn,xp1
1 h−q1,...,x pn−1
n−1h−qn−1,∀j[xj,h ]
⟩
. (30)
As the meridian and longitude of∂Y we can takeµ =xpn
n hqn and λ =x−p1···pn−1
n hc respectively,
where c = ∑n−1
j=1
p1···pn−1qj
pj
. These choices of meridian and longitude coincide with the choices
made in [23].
Let ρ : π1(X) → SL(2, C) be any irreducible representation with its corresponding l =
(l1,...,l n) ∈ L(p1,...,p n). Now ρ(h) = exp( πiv) for some integer v ∈ Z. Introduce the two
quantities
ξ =P

l1
p1
+
n∑
j=2
2lj
pj


and
η = ξ
P.
The proof of (28) presented here consists analogously with the proof of Theorem5.2 in [37] of
two parts. In the ﬁrst part, we ﬁnd a path ofSL(2, C) connections onX connectingρ to an abelian
representationρ0. In factρ0 will be anSU(2) connection onX. In the second part, we then ﬁnd a
path fromρ0 to the trivial representationρtriv and we then apply Kirk and Klassens formula (29).
The only diﬀerence from the proof in [37] is that we need to explicitly ensure that our paths stay
away from parabolic representations. The relevant paths are chosen such thatλ,µ are mapped to
the maximal C∗ torus of diagonal matrices.
After conjugating byS−1
n we haveρ(xn) = exp
(
2πiln
pn
)
. Consider the subset
S⊂ Hom (π1(Y ), SL(2, C))
of representations ˜ρ satisfying
˜ρ(h) =ρ(h), [˜ρ(x1)] =
[
exp
(πil1
p1
)]
and
[˜ρ(xj)] =
[
exp
(2πilj
pj
)]
, for 2≤j≤n− 1.
where [Q] denotes the SL(2, C) conjugacy class ofQ∈ SL(2, C). By considering the presentation
(30), we see thatS is naturally homeomorphic to the product of then− 1 conjugacy classes
S≃
[
exp
(πil1
p1
)]
×
n−1
×
j=2
[
exp
(2πilj
pj
)]
.
Resurgence Analysis of Quantum Invariants 13
Therefore the connectedness ofSL(2, C) implies thatS is connected. Following a similar argument
use in the proof of the previous proposition, we let
m :S→ SL(2, C)
be the algebraic product map. Let P ⊂ SL(2, C) be the set of non-diagonalizable elements in
SL(2, C) and observe thatP has complex co-dimension one, thus so doesm−1(P )⊂ S, but then
it follows thatS′ =S−m−1(P ) is also connected.
Writeρ =ρ1 and observe thatρ1∈S′. Choose a smooth pathρt inS′ connectingρ1 toρ0∈S′
given by
ρ0(x1) = exp
(
−πil1
p1
)
, ρ0(xj) = exp
(
−2πilj
pj
)
, j = 2,...,n − 1
and ρ0(xn) = exp
(
πil1
p1
+∑n−1
j=2
2πilj
pj
)
. By an over all conjugation we can choose the arcρt such
that ρt(xn) = exp(2 πif (t)) for a smooth function f(t). We have f(0) = l1
2p1
+∑n−1
j=2
lj
pj
and
f(1) = ln
pn
. Notice thatf(0) = η
2−f(1). As qn is even we have the following two equalities
ρt(µ) =ρt(xn)pnρt(h)qn = exp(2πipnf(t)),
ρt(λ) =ρt(xn)−p1···pn−1ρt(h)c = exp (−2πip1··· pn−1f(t) +vcπi).
Writey =vc∈ Z. Deﬁneα1(t) =pnf(t) and β1(t) =−P
pn
f(t) + y
2. We have that
−2
∫ 1
0
α′
1(t)β1(t) dt =−2
∫ 1
0
pnf′(t)
(
−P
pn
f(t) +y
2
)
dt
=−2
∫ f(1)
f(0
(
−Pu + pny
2
)
du
=−2
[
−Pu 2
2 + pnyu
2
]u=f(1)
u=f(0)
=Pf (1)2−ypnf(1)−Pf (0)2 +ypnf(0)
=Pf (1)2−Pf (0)2 +ypnf(0) mod Z.
(31)
For the last identity we used thatypnf(1) =yln∈ Z.
For the second part we use the fact thatH1(Y )≃ Z with generator µ to conclude that the
abelian SU(2) connectionρ0 can be connected to the trivial representationρtriv by a path ofSU(2)
representations σt with σt(µ) = exp(2πitα1(0)) and σt(λ) = exp(2πiβ1(0)). Let α0(t) = tα1(0)
and β0(t) =β1(0). As SCS(ρtriv) = 0, we can apply Kirk and Klassen’s formula (29) to obtain
− SCS(ρ) = SCS(ρtriv)− SCS(ρ) =−2
∫ 1
0
α′
0(t)β0(t) dt− 2
∫ 1
0
α′
1(t)β1(t) dt.
We have
−2
∫ 1
0
α′
0(t)β0(t) dt =−2f(0)(−Pf (0) +ypn
2 ) = 2Pf (0)2−ypnf(0).
Comparing this with (31) we get that
− SCS(ρ) =P (f(1)2 +f(0)2) mod Z
=P ((f(1) +f(0))2− 2f(0)f(1)) mod Z
= ξ2
4P mod Z.
For the last equality we used that2Pf (0)f(1)∈ Z and that
f(0) +f(1) = η
2 = ξ
2P.
This is what we wanted.
Resurgence Analysis of Quantum Invariants 14
Forx∈ Q let [x] =x mod Z. Introduce the set
W(p1,...,p n) =
{[−m2
4P
]
: m∈ Z is divisible by at mostn− 3 of thepj’s
}
.
Recall that the classical complex Chern-Simons valuesCS∗
C(X) is the range of the restriction of
SCS toM∗(X, SL(2, C)). Thus we can computeCS∗
C(X) as a corollary of Proposition 7.
Corollary 8. We have that
CS∗
C(X) =W(p1,...,p n).
Proof. It is clear that CS∗
C(X)⊂W (p1,...,p n). We must show that for anyy∈ Z which is not
divisible by more than three of thepj we can ﬁndl = (l1,...,l n)∈ L(p1,...,p n) which solves the
congruence equation
y2 =

P

l1
p1
+
n∑
j=2
2lj
pj




2
mod 4P Z (32)
Forx∈ Z and d∈ N let [x]d denote the congruence class ofx in the quotient ringZ/dZ. Since
pj is odd forj≥ 2, it follows that 4p1,p 2,...,p n are also pairwise co-prime. Hence the Chinese
remainder theorem applies and the natural ring homomorphismq : Z→ Z/4p1Z⊕n
j=2 Z/pjZ, given
byx↦→ ([x]4p1,..., [x]pn), descends to an isomorphism of rings
q : Z/4P Z
∼
→ Z/4p1Z ⊕
n⨁
j=2
Z/pjZ.
It follows that (32) is in fact equivalent to the followingn congruence equations
[y]2
4p1 =

l1
n∏
j=2
pj + 2


n∑
j=2
lj
∏
t⁄=j
pt




2
4p1
, (33)
[y]2
pj =

2lj
∏
t⁄=j
pt


2
pj
, ∀j≥ 2.
The coprimality conditions ensures that2∏
t⁄=jpt is an invertible element inZ/pjZ and therefore
solving the lastn− 1 of the equations in (33) can indeed be done with0≤ lj≤ (pj− 1)/2. It
remains only to consider the ﬁrst of the equations in (33). To this end we ﬁrst observe that

l1
n∏
j=2
pj + 2
n∑
j=2
lj
∏
t⁄=j
pj


2
=

l1
n∏
j=2
pj


2
mod 4p1
But then we can solve
y2 =l2
1
n∏
j=2
p2
j mod 4p1
for 0≤l1≤ 2p1. But we also have that
y2 = (−l1± 2p1)2
n∏
j=2
p2
j mod 4p1.
Thus it follows that we can in fact solve (33) withl1 ∈ {0,...,p 1}. Thus we have shown that
CS∗
C(X) =W(p1,...,p n).
Our analysis of the components of theSL(2, C) moduli space and the Chern-Simons values now
allow us to prove the following.
Resurgence Analysis of Quantum Invariants 15
Theorem 9. The Chern-Simons action
SCS :π0(M(X, SL(2, C)))→ R/Z
is injective and induces an isomorphism
π0(M(X, SL(2, C)))∼=W(p1,...,p n)⊔{ 0}.
Proof. We use the inverse of the isomorphism
q : Z/4P Z
∼
→ Z/4p1Z
n⨁
j=2
Z/pjZ
to conclude that for each Chern-Simons value inW(p1,...,p n), there is a uniquel∈L(p1,...,p n)
with the given Chern-Simons value, concluding the proof by the last statement of Proposition 5.
Thereom 1 is a summary of the main results obtained in this section.
Proof of Theorem 1.This follows from Theorem 6, Corollary 8 and Theorem 9.
