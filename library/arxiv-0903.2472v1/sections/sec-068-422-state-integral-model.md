---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-068-422-state-integral-model
section_title: "State integral model"
section_number: 4.2.2
pages: 55-57
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
4.2.2 State integral model
The state integral model (3.53) for the ﬁgure-eight knot com plement gives:
Z (α)(M ; ℏ,u ) = 1
√
2πℏ
∫
Cα
dp Φ ℏ(p +iπ + ℏ)
Φ ℏ (−p− 2u−iπ− ℏ)e− 2
ℏ u(u+p)−u. (4.45)
There are two tetrahedra (N = 2) in the standard triangulation of M , and so two quantum
dilogarithms in the integral. There is a single integration variablep, and we can identify
g1(p,u ) = p, g2(p,u ) =−p− 2u, and f (p, 2u, ℏ) =−4u(u +p).
-2 
-1 
0
1
2 -4 
-2 
0
2
4
-10 
0
10 
/X52/X65/X28/X78/X29 
/X49/X6D/X28/X78/X29 
/X4C/X6F/X67/X7C/X65 /X59 /X7C
-1 
-0.5 
0
0.5 
1 -4 
-2 
0
2
4
0
20 
40 
/X52/X65/X28/X78/X29 
/X49/X6D/X28/X78/X29 
/X7C/X65 /X59 /X7C
Figure 7: Plots of|eΥ( ℏ ,p,u )| and its logarithm at u = 0 and ℏ = i
3 .
It will be convenient here to actually change variables p↦→p−u−iπ− ℏ, removing the
(iπ + ℏ) terms in the quantum dilogarithms, and obtaining the somew hat more symmetric
expression
Z (α)(M ; ℏ,u ) = 1√
2πℏ
e
2πiu
ℏ +u
∫
Cα
dp Φ ℏ(p−u)
Φ ℏ(−p−u)e− 2pu
ℏ (4.46)
= 1√
2πℏ
e
2πiu
ℏ +u
∫
Cα
dpe Υ( ℏ,p,u). (4.47)
We deﬁneeΥ( ℏ,p,u) = Φ ℏ (p−u)
Φ ℏ (−p−u)e− 2pu
ℏ . Figures 7 and 8 show plots of |eΥ( ℏ,p,u)| and log|eΥ( ℏ,p,u)| =
Re Υ( ℏ,p,u ) at ℏ =i/3 and two values of u. The half-lines of poles and zeroes of the two
quantum dilogarithms combine into similar singularities f or Υ( ℏ,p,u ), as is depicted in
Figure 9; note the splitting of these poles and zeroes by an am ount 2u.
After our change of variables, the “potential” function V (p,u ) as in (3.43) is now seen
to be
V (p,u ) = 1
2
[
Li2(−ep−u)− Li2(−e−p−u)− 4pu + 4πiu
]
. (4.48)
– 54 –
-1 
-0.5 
0
0.5 
1 -4 
-2 
0
2
4
-5 
0
5
/X52/X65/X28/X78/X29 
/X49/X6D/X28/X78/X29 
/X4C/X6F/X67/X7C /X65 /X59 /X7C
-0.5 
0
0.5 
1 -4 
-2 
0
2
4
0
5
10 
15 
20 
/X52/X65/X28/X78/X29 
/X49/X6D/X28/X78/X29 
/X7C/X65 /X59 /X7C
Figure 8: Plots of|eΥ( ℏ ,p,u )| and its logarithm at u = 1
2i and ℏ = i
3 .
Instead of looking directly at ∂
∂pV = 0 to ﬁnd its critical points, we consider the simpler
equation
r(x,m ) = e2 ∂
∂p V = x
m2(m +x)(1 +mx) = 1, (4.49)
in terms of x =ep and m =eu. This clearly has two branches of solutions, which both lift
to true critical points of V , given by
p(geom,conj)(u) = log
[1−m2−m4∓m2∆( m)
2m3
]
, (4.50)
with ∆( m) deﬁned in (4.32). The lift is unique if (say) ℏ∈i R>0. We claim that these
correspond to the geometric and con-
X X X X X X X X X X X X
X X X X X X X X
X X X X X X X X X X X X
X X X X X X X X XX
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
/Minus15 /Minus10 /Minus5 5 10 15Re/LParen1p/RParen1
/Minus15
/Minus10
/Minus5
5
10
15
Im/LParen1p/RParen1
Figure 9: Poles, zeroes, and critical points of eΥ( ℏ ,p,u )
for u = 1
2i and ℏ = 3
4eiπ/ 6.
jugate branches of the A-polynomial,
which can be veriﬁed by calculating 25
s(x,m ) = exp
(∂
∂uV (p,u )
)
=
[m+x
x3+mx4
] 1/2,
and checking indeed thats(x(geom,conj)(m),m ) =
lgeom,conj(m).
The two critical points of Λ ℏ which
correspond to the critical points of V
(as ℏ→ 0) are indicated in Figures 7
and 8. As mentioned at the end of Sec-
tion 3.4, at any ﬁxed ℏ⁄= 0 there exist
many other critical points of Λ ℏ that
can be seen between consecutive pairs
of poles and zeroes in Figures 7 and
8; however, these other critical points
become trapped in half-line singulari-
ties as ℏ→ 0, and their saddle point
approximations are not well-deﬁned.
We now calculate the perturbative
invariantsS(geom)
n (u) and S(conj)
n (u) by doing a full saddle point approximation of the in-
tegral (4.46) on (dummy) contours passing through the two cr itical points. We begin by
25Here s(x, m ) is the square root of a rational function rather than a ratio nal function itself due to our
redeﬁned variables. Using (4.45) directly, we would have go tten a pure rational expression.
– 55 –
formally expanding Υ( ℏ,p,u ) = log Λ ℏ(p,u ) as a series in both ℏ and p around some ﬁxed
point p0:
Υ( ℏ,p 0 +p,u ) =
∞∑
j=0
∞∑
k=−1
Υ j,k(p0,u )pj ℏk. (4.51)
Our potential V (p,u ) is identiﬁed with Υ 0,−1(p,u ) + 2πiu, and critical points of V are
deﬁned by Υ 1,−1(p,u ) = ∂
∂pV (p,u ) = 0. Let us also deﬁne
b(p,u ) :=−2Υ 2,−1(p,u ) =− ∂2
∂p2V (p,u ). (4.52)
Then at a critical point p0 =p(α)(u), the integral (4.46) becomes 26
Z (α )(M ; ℏ,u ) = eu+ 1
ℏ V (α )(u)
√
2πℏ
∫
Cα
dpe − b(α ) (u)
2ℏ p2
exp

 1
ℏ
∞∑
j=3
Υ (α )
j, −1(u)pj +
∞∑
j=0
∞∑
k=1
Υ (α )
j,k (u)pjℏk

,
(4.53)
where V (α)(u) = V (p(α)(u),u ), b(α)(u) = b(p(α)(u),u ), and Υ (α)
j,k (u) = Υ j,k(p(α)(u),u ) are
implicitly functions of u alone.
We can expand the exponential in (4.53), integrate each term using
∫
dpe − b
2ℏ p2
pn =
{
(n− 1)!!
(ℏ
b
) n/2√
2πℏ
b n even
0 n odd
, (4.54)
and re-exponentiate the answer to get a ﬁnal result. The inte grals in (4.54) are accurate
up to corrections of order O(e−const/ℏ ), which depend on a speciﬁc choice of contour and
are ignored. Following this process, we obtain
Z (α)(M ; ℏ,u ) = 1√
2πℏ
√
2πℏ
b(α)eu+ 1
ℏ V (α )(u)eS(α )
2 ℏ+S(α )
3 ℏ2+... (4.55)
= exp
[1
ℏV (α)(u)− 1
2 logb(α) +u +S(α)
2 ℏ +S(α)
3 ℏ2 +...
]
, (4.56)
where the coeﬃcients Sn can be straightforwardly computed in terms of b and the Υ’s. For
example, S(α)
2 = 15
2(b(α ))3 Υ (α)
3,−1 + 3
(b(α ))2 Υ (α)
4,−1 + Υ (α)
0,1 and S(α)
3 = 3465
8(b(α ))6 (Υ (α)
3,−1)4+ (sixteen
other terms). In addition, we clearly have
S(α)
