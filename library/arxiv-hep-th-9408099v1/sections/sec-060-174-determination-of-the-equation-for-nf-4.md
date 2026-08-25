---
doc_id: arxiv-hep-th-9408099v1
doc_title: "Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD"
section_id: sec-060-174-determination-of-the-equation-for-nf-4
section_title: "Determination Of The Equation For Nf = 4"
section_number: 17.4
pages: 81-84
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
We have ﬁnally assembled the tools to determine the precise f unction F in our equa-
tions y2 = F (x,u ). First we do this for the theory with Nf = 4. We will determine
the expansion of ω in terms of the C(i)a for some given i; we may as well pick i = 1.
(The expansions in terms of the C(j)a for j ⁄= 1 are then determined by the above triality
formulas.) By requiring that ω = − 1√
2
∑
ama[C(1)a], F will be determined.
In coordinates with v = 1, the cubic part of F is (x −e1u)(x −e2u)(x −e3u). Since e1
is in any case singled out by the decision to expand in the C(1)a, it is convenient to make
the change of variables x −e1u →x. The lines x =e1u +θ are now described simply by
x =θ. (17.38)
Also, if we set
α =e2 −e1, β =e3 −e1, (17.39)
the cubic part of F isx(x −αu)(x −βu). The quadratic part of F is a linear combination
ofx2,xu , and u2. We can eliminate any two of the three by shifting x andu by constants.
We choose to set the coeﬃcients of xu and u2 to zero. The general structure is then
F =x(x −αu)(x −βu) +ax2 +bx +cu +d. (17.40)
80
Restricted to the line (17.38), one has
F =θαβu 2 + (c −θ2(α +β))u +θ3 +aθ2 +bθ +d. (17.41)
If we write the right hand side as Au2 +Bu +C, then the discriminant ∆ = B2 − 4AC is
∆ = θ4(α −β)2 − 4aαβθ 3 + (−2c(α +β) − 4bαβ)θ2 − 4αβdθ +c2. (17.42)
∆ has four roots θa, a = 1... 4. For θ =θa, the equation y2 =F takes the form
y2 =θaαβ(u −u0)2 (17.43)
for some u0. Restoring the v dependence, in homogenous coordinates, the equations for
the divisors D(1)±,a take the form
x =θv
y = ±(θaαβ)1/2v(u −u0v).
(17.44)
Computation Of Periods
Now we want to expand [ ω] in terms of these divisors. The main point is to study
the behavior of ω near ∞ (that is, v = 0), where we can set u = 1. The equation
y2 =vF (x,u,v ) becomes in this coordinate system
y2 =vx(x −α)(x −β) +av2x2 +bv3x +cv3 +dv4. (17.45)
So near the singularity at x =v = 0, we get
2y ·dy =vαβdx +... (17.46)
where the ... are terms proportional to dv (which will drop out when we compute ω) or
v2,vx (which are negligible near v =x = 0). Inserting (17.46) in ω = (
√
2/8π)dvdx/vy ,
we get
ω ∼
√
2
4π
dvdy
v2αβ. (17.47)
81
This means that near v = 0 we can write ω =dλ with
λ = −
√
2
4π
y dv
v2αβ. (17.48)
Let Xǫ be the region with |v| < ǫ. We want to modify ω inside Xǫ to eliminate the
pole at v = 0, while preserving the fact that ω is closed. The ω so modiﬁed extends over
a neighborhood of the singularity at x =v = 0 in the compactiﬁcation of X. (ω could be
extended over all of X, but that will not be necessary.)
To make the modiﬁcation, let λ′ =f (v)λ, withf a smooth function such that f (v) = 1
for |v|> ǫand f ∼ |v|2 for v → 0. Now, leave ω unchanged outside of Xǫ, but inside Xǫ
take
ω =dλ′. (17.49)
We now have all the information required to compute the desir ed residues, which,
according to (17.10) and (17.12), are equivalent to the inte grals ofω overC(1)a =D(1)+,a −
D(1)−,a. The integral over C(1)a is twice the integral overD =D(1)+,a, using the symmetry
under y ↔ −y:
ca =
∫
C(1)a
ω = 2
∫
D
ω. (17.50)
Let Dǫ be the part of D with |v|<ǫ . Then
∫
D
ω =
∫
Dǫ
ω, (17.51)
as outside Dǫ, ω is of type (2 , 0). Inside Dǫ, ω =dλ′, so
∫
Dǫ
ω =
∫
Dǫ
dλ′ =
∮
|v|=ǫ
λ′ =
∮
|v|=ǫ
λ = −
√
2
4π
∮
|v|=ǫ
ydv
v2αβ
= −
√
2
4π
∮
|v|=ǫ
√θaαβ dv
vαβ = − i√
2
√
θa
αβ.
(17.52)
The next to last step uses the fact that near v = 0 on D,
y ∼ (θaαβ)1/2v (17.53)
according to (17.44). So
ca = −
√
2i
√
θa
αβ. (17.54)
82
Now we can determine the desired residues from (17.12) – usin g the fact that the
matrix M is M = −4 according to (17.29). We get
ResC(1)aλ = − 1
4π
√
2
√
θa
αβ. (17.55)
Here of course θa is any of the roots of the discriminant (17.42).
Final Steps
On the other hand, we want the residues to be ma/2πi
√
2, with ma the masses. So
the four zeroes θa of the discriminant should be θa = −4αβma2. For the discriminant to
have these roots means that (17.42) can be rewritten as follo ws:
