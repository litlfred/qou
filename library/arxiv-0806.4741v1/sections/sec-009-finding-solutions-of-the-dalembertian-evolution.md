---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-009-finding-solutions-of-the-dalembertian-evolution
section_title: "Finding solutions of the Dalembertian evolution by variable separation"
section_number: null
pages: 15-17
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
For convenience, we ﬁx a particular choice of closed star product ⋆ on M associated as above with the
function
P(ζ) = P
closed
(ζ) :=
√
cosh(ℏζ). (80)
We denote the corresponding intertwiner by T closed. We then note that, from the above discussion, the
analogue of equation (68) for the direct operator U in this case can be rewritten under the following form:
− 2|¯zW (x, ¯z) =F⋆
(x)W (x, ¯z) , (81)
with
W (x, ¯z) =
(
(φ∗
ℏ)−1◦F◦ T
closed)
|zu(z−1x) , (82)
and where the operator 2 is given by (61). Observe that from (82) the function W (x, ¯z) =W (a,n,b,r ) takes
the form
W (a,n,b,r ) = (1 + ℏ2r2)1/4qe−irnqF (q,r ) , (83)
with q =e2(a−b) and
F (q,r ) =
∫
eiqry u(1
2 lnq,y )dy , (84)
and where ( a,n ) are the coordinates of x, (b,𝓁 ) those of z, and, ( b,r ) those of ¯z, r being the variable
conjugated to 𝓁 through the Fourier transformationF which only aﬀect the second z-coordinate.
The right-hand side of eq. (81) is simpler :
F⋆
xW (x, ¯z) =e2aq
(
2qn∂ q− (k′ +n2)∂n
)
W (q,n,r ) (85)
15
k′ being for the operator F⋆
x the corresponding of k for the operator F in ρ1
ℏ(F )|z (see eqs (48)), so ﬁnally
eq. (81) simpliﬁes to the following equation for F (q,r ) :
(
−r ℏ2q2 (1 + ℏ2r2)∂2
q−r (1 + ℏ2r2)2∂2
r + 2q (1 + ℏ2r2)2∂r∂q− 2 ℏ2r2 (1 + ℏ2r2)∂r +V
)
F (q,r ) = 0, (86)
with
V = V (q,r ) := r (− ℏ2
4 (2 + ℏ2r2) + (1 +ℏ2r2)(k−k′q2)). (87)
The problem amounts thus to solve the corresponding equation for Fℏ(q,r ), from which we could ﬁnd uℏ by
inverting (84). We set
G(q,r ) =q1/2(1 +r2ℏ2)1/4F (q,r ), (88)
and use the variables:
U =q
1
2 sinh( ℏ
2ζ) , V =q
1
2 cosh( ℏ
2ζ) , (89)
with
r =: 1
ℏ sinh(ℏζ). (90)
The equation then becomes [
∂U∂V + ˜Q(U,V )
]
G(U,V ) = 0 , (91)
with
˜Q(U,V ) =− 4
ℏ2
UV
(U2−V 2)2 ( ℏ2
4 −k +k′(U2−V 2)2) . (92)
Note that here :U2−V 2 =−q, henceU2−V 2 < 0. Setting U2 = 1
2(t−x),V 2 = 1
2(t+x) andG(q,r ) =H(t,x ),
one then gets {
x2(∂2
t−∂2
x)− 1
ℏ2 [ ℏ2
4 −k +k′x2]
}
H(t,x ) = 0. (93)
Applying a method of separation of variables to the latter yields solutions as superpositions of the following
modes:
Fℏ,s(q,r ) =hs(q)(1 + ℏ2r2)−1/4eisq
√
1+ℏ2r2
, (94)
with
hs(x) =AJ√
k
ℏ
[
√
s2 +k′/ℏ2 x] +BY√
k
ℏ
[
√
s2 +k′/ℏ2 x] , (95)
where Jµ and Yµ denote Bessel functions of the ﬁrst and second kinds (see ref. [41]). From (84)
u(a,l ) = e2a
2π
∫
e−irle 2a
F (e2a,r )dr , (96)
thus (up to constant factors)
uℏ,s(a,l ) =e2ahs(e2a)
∫
Hs(a,b )eible2a
db , (97)
with
Hs(a,b ) = (1 + ℏ2r2)−1/4eis
√
1+ℏ2r2e2a
. (98)
We may use a similar technique to determine the kernel of the inverse operator U−1. By writing
[U−1f](x) =
∫
v(z−1x)f(z)dz , (99)
one ﬁnds:
2¯xM(¯x,z ) =−F⋆
zM(¯x,z ) (100)
with
M(¯x,z ) =
(
(φ∗
ℏ)−1◦F◦ TP)
|xvP(z−1x) . (101)
Solutions to (100) can be deduced by using a slight generalization of what we have done here above. We
ﬁnally get,
vℏ,s(a,l ) =e−2ahs(e−2a)
∫
(1 + ℏ2r2)−1/4eis
√
1+ℏ2r2e−2a
e−ibldb . (102)
16
