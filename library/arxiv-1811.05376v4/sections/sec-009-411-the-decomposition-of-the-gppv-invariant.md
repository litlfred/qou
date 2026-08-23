---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-009-411-the-decomposition-of-the-gppv-invariant
section_title: "The decomposition of the GPPV invariant"
section_number: 4.1.1
pages: 27-31
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
Recall that q = exp(2πiτ ) with τ ∈ h where h denotes the upper half plane, and recall the
deﬁnitions ofF∈M (C) and g∈ C[x] given in (15). Let˜Γ+ =e
πi
4 .
Lemma 1. Introduce the holomorphic functionsL,R∈O (h) given by
L(τ) = 2λ√τ
∫
Γ+
e−x/τB(Z0)(x) dx,
R(τ) =− 2λ√τ
∞∑
m=0
Res
(
exp
(g(ξ)
τ
)
F (ξ),ξ = 2πim
)
.
Resurgence Analysis of Quantum Invariants 28
Then we have that
q∆ˆZ0(q) =L(τ) +R(τ). (61)
Forτ in the ﬁrst quadranth+ ={z∈ h|ℜ (z)> 0} we have that
L(τ) = 2λ√τ
∫ ∞
0
e−x/τB(Z0)(x) dx. (62)
Proof of Lemma 1.Recall the contour formula from Theorem 3
q∆ˆZ0(q) = I(τ) = λ√τ
∫
Γ
exp(−x/τ)B(Z0)(x) dx.
Under the coordinate change
x =y2
the contourΓ corresponds to the contour
Ψ =eiπ 3
8 R+ +eiπ 1
8 R+
Therefore we have that
q∆ˆZ0(q) = λ√τ
∫
Ψ
exp(−y2/τ)B(Z0)(y2)2y dy.
Introduce the meromorphic functionB∈M (C) given for ally∈ C by
B(y) = 2yB(Z0)(y2). (63)
By Theorem 2 we have that
B(y) = 2κ
πiG
(
exp
(κy
P
))
= 2κ
πiF
(κy
2
)
. (64)
From (64) we see thatB is periodic with periodκ, i.e. for allm∈ Z we have that
B(y +κm) =B(y). (65)
LetP be the set of poles ofB. It follows from Theorem 2 thatP is a subset of the axiseπi/4R
and that
{−ω2|ω∈P} = 2πi CSC(X) + 2πiZ.
Write
Ψ± =eiπ( 1
4∓ 1
8 )R+.
We will now apply Cauchy’s residue theorem to moveΨ− across eiπ/4R+ to Ψ+ in order to obtain
the formula (61). Deform Ψ± on the complement of a neighbourhood around the origin to two
curvesL±, which are parallel toeiπ/4R+ outside this neighbourhood of the origin, as indicated in
Figure 7. Set
L =L+∪L−.
We ﬁrst show that ∫
Ψ
exp(−y2/τ)B(y) dy =
∫
L
exp(−y2/τ)B(y) dy, (66)
and then we show that the right hand side of (66) can be rewritten as a sum of residues. LetR> 0
be a positive constant, and letR± be the arc segment of the circle of radiusR, which connectsΨ±
and L±. Because L± is parallel toκR+ outside a neighbourhood of the origin, there exists a real
positive constantb0 > 0 such that everyy∈R± is of the form
y =κa±b, (a,b )∈ R+× [b0, +∞)
and therefore exists a positive real constantA> 0 independent ofR, which gives an upper bound
⏐⏐⏐⏐
1
1−e−κy
⏐⏐⏐⏐< 1
1− exp (−ℜ(κ)b0) :=A> 0
Resurgence Analysis of Quantum Invariants 29
for ally∈R+. It follows that we obtain a uniform estimate
B(y) = 2n−2 2κ
πi
∏n
j=1 sinh( κy
2pj
)
(
eκy/2(1−e−yκ)
)n−2
=O

e−yκ/2
n∏
j=1
sinh
(κy
2pj
)
 =O(eA1R).
(67)
for ally∈ R+ for a real constantA1. For ﬁxedτ, there exists a positive real constantA2 > 0
giving a uniform bound onR+
e−y2/τ =O(e−A2R2
). (68)
By combining the estimates (67) and (68), and using that the arc length ofR± is proportional to
R, we obtain the estimate
∫
R+
exp(−y2/τ)B(y) dy =O(Re−A2R2+A1R).
By similar reasoning, there exists constantsB2 > 0,B 1∈ R giving the estimate
∫
R−
exp(−y2/τ)B(y) dy =O(Re−B2R2+B1R).
Thus we obtain that
lim
R→∞
∑
ϵ∈{±1}
∫
Rϵ
exp(−y2/τ)B(y) dy = 0, (69)
which gives the desired identity (66) .
We now turn to the computation of
∫
L exp(−y2/τ)B(y) dy. For eachm∈ N, letLm be a small
line segment with
Lm∩eiπ/4R+ ={mκ},
and which meetseiπ/4R+ in a right angle. We can arrange thatLm is of ﬁxed lenght and thatLm
meet L± in a point. Thus we have
Lm =L0 +mκ
Let Lm
± be the bounded component ofL±\Lm, and letPm⊂P be the set of poles ofB that lie
within the bounded component of the complement of the contour
Ψm =Lm
+∪Lm∪Lm
−.
See Figure 7. EquipΨm with the counter clockwise orientation. An application of Cauchy’s residue
theorem now gives
2πi
∑
ω∈Pm
Res(e−y2/τB(y),y =ω) =
∫
Ψm
exp(−y2/τ)B(y) dy
=
∫
Lm
exp(−y2/τ)B(y) dy +
∑
ϵ∈{±1}
ϵ
∫
Lmϵ
exp(−y2/τ)B(y) dy.
(70)
Because B is κ periodic as stated in (65) andLm =L0 +mκ, we see that that there existsC >0
giving a uniform bound
C >sup{|B(y)| |y∈∪ m∈NLm}.
Because of this universal bound, it is easy too see that
lim
m→∞
∫
Lm
exp(−y2/τ)B(y) dy = 0.
Resurgence Analysis of Quantum Invariants 30
κ R +
κm
·L m
.
.
.
P m
·
κ
Ψ −
L m
−
L −
Ψ +
L m
+
L +
Figure 7: The contoursL±,Lm
± andΨ± and the subset of polesPm drawn rotated, such thatκR+
points straight up.
It follows that the right hand side of (70) converges to
∑
ϵ∈{±1}
∫
Lϵ
exp(−y2/τ)B(y) dy =
∑
ϵ∈{±1}
ϵ
∫
Ψϵ
exp(−y2/τ)B(y) dy.
This also implies that the sum of residues is convergent.
Let us now recall a simple transformation law for residues. Letz0∈ C and letf∈M z0(C)
be the germ of a meromorphic function with a pole atz0. Assume w0∈ C and thatz∈O w0(C)
satisﬁesz(w0) = z0, ˙z(w0)⁄= 0. If eitherz0 is a simple pole, orz(w) is linear inw, then we have
that
Res(f(z(w)),w =w0) = Res(f(z),z =z(w0))
˙z(w0) . (71)
Introduce the variable
ξ = κy
2 .
By using the relation (64) betweenB and F, the relation (63) betweenB andB(Z0) and the
tranformation law (71) we obtain
q∆ˆZ0(q) = λ
τ
∫
Ψ
exp
(
−y2
τ
)
B(y) dy
= 2λ
τ
(∫
Ψ+
exp
(
−y2
τ
)
B(y) dy− 2πi
∑
ω∈P
Res(e−y2/τB(y),y =ω)
)
= 2λ
τ
(∫
Γ+
exp
(
−x
τ
)
B(Z0)(x) dx−
∞∑
m=1
Res(e−g(ξ)/τF (ξ),ξ = 2πim)
)
=L(τ) +R(τ).
Finally, we prove (62) forτ∈ h+. First observe that forx and τ in the upper right half plane we
have
ℜ(x/τ)> 0. (72)
Resurgence Analysis of Quantum Invariants 31
Push the contour ˜Γ+ to R+. If the integral is invariant under this deformation of the contour,
we obtain the desired identity. To see that the integral is invariant under this deformation of the
contour, we apply a limiting argument, together with Cauchy’s residue formula. To that end, let
R > 0 be a positive parameter, and letCR be the arc segment of the circle of radiusR, which
connects R to Reiπ 3
4 and stays in the upper half plane. As we are not moving the contour across
any singularities ofB(Z0), the only diﬃculty is to show that
lim
R→+∞
∫
CR
e−x/τB(Z0)(x) dx = 0. (73)
As CR remain at least a ﬁxed distance away from the axis of poles ofB(Z0)(x), the limit (73)
follows by (72) together with arguments similar to the arguments giving the limit (69) above.
