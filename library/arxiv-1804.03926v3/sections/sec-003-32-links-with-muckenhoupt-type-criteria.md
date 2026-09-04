---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-003-32-links-with-muckenhoupt-type-criteria
section_title: "Links with Muckenhoupt-type criteria"
section_number: 3.2
pages: 14-18
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
doc_brief: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one — We investigate links between the so-called Stein’s density approach indimension"
---
It is well-known that the Muckenhoupt criterion [Muc72], wh ich provides a necessary and suﬃcient
condition for a (weighted) Hardy inequalty to hold on the rea l line, can be used to sharply estimate
the best constant in Poincar´ e inequalities (see for instan ce [ABC +00] and [Mic08] and references
therein). The following theorem, providing sharp estimate s, is given in [Mic08].
Theorem 9 ([Mic08]) Letη be a probability measure on R with median m and let χ be a measure
on R with Radon-Nikodym derivative with respect to the Lebesgue measure denoted by n. The best
constantCP such that, for every locally Lipschitz f : R → R it holds
Varη (f) ≤CP
∫ (
f ′) 2dχ ,
veriﬁes max {B+,B −} ≤ CP ≤ 4 max{B+,B −} where
B+ = sup
x>m
η ([x, +∞))
∫ x
m
dt
n (t) and B− = sup
x<m
η ((−∞,x ])
∫ m
x
dt
n (t) .
Considering Theorem 6, a natural question is: can we recover (up to a constant) Inequality (22)
from Theorem 9 above? The answer is positive. Indeed, we want to show that max {B+,B −} is
ﬁnite. We will only discuss computations for B+ since B− can be treated symmetrically. With the
notations of Theorems 6 and 9, we take η =ν and n (t) =τν (t)p (t). This gives
B+ = sup
x>m
ν ([x, +∞))
∫ x
m
dt
τv (t)p (t) = sup
x>m
ν ([x, +∞))
∫ x
m
dt∫ ∞
t (y −µ)p (y)dy .
Furthermore, there exists δ >0 such that v ([x0, +∞))> 0 for x0 = max {m,µ } +δ. Hence, for any
x ≥x0,
ν ([x, +∞))
∫ x
m
dt∫ ∞
t (y −µ)p (y)dy ≤ ν ([x, +∞))∫ ∞
x (y −µ)p (y)dy ≤ 1
δ .
14
As
sup
x∈(m,x 0)
ν ([x, +∞))
∫ x
m
dt∫ ∞
t (y −µ)p (y)dy ≤ x0 −m∫ ∞
m (y −µ)p (y)dy ∧
∫ ∞
x0
(y −µ)p (y)dy < +∞ ,
we get B+ < +∞. Consequently, we quickly recover under the assumptions of Theorem 6 the fact
that the measure ν satisﬁes a weighted Poincar´ e inequality of the form of (22) , although with a
multiplicative constant at the right-hand side that a prior i depends on the measure ν. Using (22)
together with Theorem 9, we have in fact max {B+,B −} ≤ 1, but we couldn’t achieve this bound -
even up to a numerical constant - by direct computations. It i s maybe worth mentioning that the
proof of Theorem 9 in [Mic08] is technically involved and tha t the bound max {B+,B −} ≤ 1 in our
case might be rather diﬃcult to establish by direct computat ions.
Let us turn now to the important, natural question of the exis tence of weighted log-Sobolev
inequalities under the existence of a Stein kernel. The proo f of the following theorem is based on a
Muckenhoupt-type criterion due to [BG99] (see also [BR03] f or a reﬁnement) giving a necessary and
suﬃcient condition for existence of (weighted) log-Sobole v inequalities on R, together with the use
of the formulas given in Propostion 5 above.
Theorem 10 Take a real random variable X of distribution ν with density p with respect to the
Lebesgue measure on R. Assume that E [|X|]< +∞,p has a connected support [a,b ] ⊂ ¯R and denote
τν the Stein kernel of ν. Take g absolutely continuous. Then the following inequality holds
Entν
(
g2)
≤Cν
∫
τ2
ν
(
g′) 2dν , (29)
for some constant Cν > 0 if one of the following aymptotic condition holds at the supr emum of its
support, together with one of the symmetric conditions - tha t we don ’t write explicitely since they are
obviously deduced - at the inﬁnimum of its support:
• b< +∞ and τ−1
ν is integrable at b− with respect to the Lebesgue measure.
• b = + ∞ and 0 < c− ≤ τν (x) ≤ c+x2/ logx for some constants c−and c+ and for x large
enough.
• b = +∞ and 0<c −x ≤τν (x) for a constant c−and for x large enough.
Reciprocally, if b = + ∞ and τν →x→±∞ 0 then inequality (29) can not be satisﬁed for every
smooth function g.
Theorem 10 gives a suﬃcient condition for the weighted log-Sobolev inequality (29) to hold when
the support is a bounded interval: it suﬃces that the inverse of the Stein kernel is integrable at the
edges of the support. Furthermore, when an edge is inﬁnite, i f the weighted log-Sobolev inequality
(29) is valid, then the Stein kernel does not tend to zero arou nd this edge.
Consider the Subbotin densities, deﬁned by pα (x) = Z −1
α exp (− |x|α /α ) for α > 0 and x ∈ R.
There Stein kernels τα satisfy τα (x) ∼x→+∞x2−α (see the discussion in Section 3.1 above), so they
achieve a weighted log-Sobolev inequality (29) if and only ifα ∈ (0, 2]. In the case where α ∈ [2, +∞),
they actually achieve a (unweighted) log-Sobolev inequali ty ([LaO00]).
It is reasonable to think that inequality (29) should be true under suitable conditions in higher
dimension, with the right-hand side replaced by
∫
|τν ∇f |2dν up to a constant, where τν is the Stein
kernel constructed by Fathi in [Fat18] using moment maps. Ho wever, some technical details remain
to be solved at this point of our investigations.
15
Furthermore, notice that Theorem 10 allows to recover in dim ension one and with a worst con-
stant, a result due to [BL09a] in dimension d ≥ 1, stating that generalized Cauchy distributions (see
Section 3.1 above for a deﬁnition) verify the following weig hted log-Sobolev inequality,
Entν β
(
g2)
≤ 1
β − 1
∫ (
1 +x2) 2(
g′ (x)
) 2dνβ (x) , β >1 . (30)
Using the Muckenhoupt-type criterion due to [BG99], we can a ctually sharpen and extend the pre-
vious inequality in the following way. There exists a consta ntCβ such that, for any smooth function
g,
Entν β
(
g2)
≤Cβ
∫ (
1 +x2)
log
(
1 +x2)(
g′ (x)
) 2dνβ (x) , β >1/ 2 . (31)
Indeed, using the quantities deﬁned in (32) below, with dη =dνβ =Z −1
β
(
1 +x2) −βdx and n (t) =
Z −1
β
(
1 +x2) −β +1 log
(
1 +x2)
, we note that m = 0, L+ =L− and by simple computations, we have
for β >1/ 2,
∫ x
m
dt
n (t) =Ox→+∞
(x2β −1
logx
)
, Λ ( νβ ([x, +∞))) =Ox→+∞
(
x−2β +1 logx
)
.
This means that L+ is ﬁnite and so, Inequality (31) is valid, which constitutes an improvement upon
inequality (30). A natural question that remains open, is we ther the weighted log-Sobolev inequality
obtained for generalized Cauchy measures in [BL09a] can be a lso improved in dimension d ≥ 2?
Proof. Let us denote Λ ( x) = −x logx for x ≥ 0 - setting by continuity Λ(0) = 0. By the
Muckenhoupt-type criterion derived in [BG99] (see also The orem 1 in [BR03]), we know that if
L+ = sup
x>m
Λ (η ([x, +∞)))
∫ x
m
dt
n (t) and L− = sup
x<m
Λ (η ((−∞,x ]))
∫ m
x
dt
n (t) (32)
are ﬁnite, then it holds for any smooth function g,
Entη
(
g2)
≤CLS
∫ (
g′) 2dχ ,
wherem is a median ofη,n is the absolutely continuous component ofχ and 1/ 150 ≤CLS/ max {L−,L +} ≤
468. So by taking η =ν andn =τ2
νp, we only have to check thatL+ andL− are ﬁnite. We will only
detail computations related to L+ since L− can be handled with symmetric arguments.
Without loss of generality, we may assume thatν is centered,
∫
xdν (x) = 0. Let us denoteR (x) =
Λ (ν ([x, +∞)))
∫ x
m
(
τ2
ν (t)p (t)
) −1dt. First remark that since τν (t)p (t) =
∫ ∞
t (y −µ)p (y)dy, we
have for any x ∈ (a,b )
⋂
(m, +∞),
∫ x
m
dt
n (t) =
∫ x
m
p (t)dt
(τν (t)p (t))2 ≤ 1(∫ ∞
m (y −µ)p (y)dy
) 2 ∨ 1(∫ ∞
x (y −µ)p (y)dy
) 2 < +∞ .
This yieds that for any segment [c,d ] ⊂ [m,b ), we have supx∈[c,d ]R (x)< +∞. We will thus focus on
the behavior of the function R around the supremum b of the support. Recall Formula (19),
p (x)τν (x) = E
[
(X)+
]
exp
(
−
∫ x
0
y
τν (y)dy
)
. (33)
16
Moreover, Identity (20) applied to h =Id and x0 = 0, gives for any x ∈I (ν), x> max {m, 0},
ν ([x, +∞)) ≤ E
[
(X)+
] 1
x exp
(
−
∫ x
0
y
τν (y)dy
)
.
Let δ >max {m, 0} be such that δ ∈I (ν) - note that δ exists since ν is centered. By using formula
(33) and an integration by parts, it holds, for any x ∈I (ν) ∩ [δ, +∞),
E
[
(X)+
] ∫ x
m
dt
τ2ν (t)p (t) = E
[
(X)+
] ∫ δ
m
dt
τ2ν (t)p (t) +
∫ x
δ
1
t
t
τν (t) exp
(∫ t
0
y
τν (y)dy
)
dt
≤ E
[
(X)+
] ∫ δ
m
dt
τ2ν (t)p (t) + 1
x exp
(∫ x
0
y
τν (y)dy
)
+
∫ x
δ
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt (34)
Furthermore, notice that the function Λ is increasing - and i n particular bounded - at the neighbor-
hood of 0 (more precisely on [0 , 1/e ]). Hence, if b< +∞ andτ−1
ν is integrable at b− then it is easily
seen from the previous computations that sup x>m
∫ x
m
(
τ2
ν (t)p (t)
) −1dt< +∞ and so, L+ is ﬁnite.
From now on, assume that b = + ∞. Hence, inequality (34) is valid with δ = 1. If x is large
enough, it holds
Λ (ν ([x, +∞))) ≤ Λ

E
[
(X)+
] exp
(
−
∫ x
0
y
τ ν (y)dy
)
x


and by using (34) we get that there exists a constant r> 0 such that, for x large enough,
R (x) ≤ r + 1
x2
(
log
(
x
E
[
(X)+
]
)
+
∫ x
0
y
τν (y)dy
)
/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
(I)
(35)
+
(
log
(
x
E
[
(X)+
]
)
+
∫ x
0
y
τν (y)dy
)
1
x exp
(
−
∫ x
0
y
τν (y)dy
) ∫ x
1
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
(II )
.
If τν (x) ≥ c− > 0 for x large enough, then quantity ( I) remains bounded around + ∞. As for
quantity (II ), notice that, for any a> 1,
∫ x
x/a
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt ≤ a − 1
x exp
(∫ x
0
y
τν (y)dy
)
and so, for x large enough,
∫ x
1
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt ≤ a − 1
x exp
(∫ x
0
y
τν (y)dy
)
+
∫ x/a
1
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt .
If in addition, τν (x) ≤c+x2/ logx for x large enough, then
∫ x
x/a
y
τν (y)dy ≥c−1
+
∫ x
x/a
logy
y dy =c−1
+ loga logx −c−1
+ (loga)2 .
Takea = exp (c+), then there exists a constant Cc+ > 0 depending on c+ such that, for x large
enough,
∫ x/a
1
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt ≤ exp
(∫ x/a
0
y
τν (y)dy
)
≤ Cc+
x exp
(∫ x
0
y
τν (y)dy
)
.
17
This gives that, up to a constant, quantity ( II ) is bounded from above by quantity ( I) and the
conclusion follows if c− ≤τν (x) ≤c+x2/ logx for x large enough.
We discuss now the case where c−x ≤τν (x) for a constant c−> 0 and for x large enough. As in
particularτν ≥c−> 0 for x large enough, then quantity (I) remains bounded around + ∞. We also
have, for x large enough, ∫ x
0
y
τν (y)dy ≤ 2
c−
x
and ∫ x
1
1
t2 exp
(∫ t
0
y
τν (y)dy
)
dt ≤ exp
(∫ x
0
y
τν (y)dy
)
,
which is suﬃcient to ensure that (II ) =Ox→+∞ (1) and L+< +∞.
To conclude the proof, it remains to consider the situation whereb = +∞ and for anyc> 0 there
exists x0 such that for any x ≥x0, τν (x) ≤c. In this case, we have to show that L+ = +∞. Since
there exists x1 such that τν (x) ≤ 1 for x1 ≤x, then for x1 ≤x ≤y,
exp
(
−
∫ y
x
t
τν (t)dy
)
≤ exp
(
−y2 −x2
2
)
Notice also that, for any x ≥ 2, we have by integration by parts,
∫ +∞
x
1
y2 exp
(
−y2 −x2
2
)
dy ≤ 1
x3 ≤ 1
4x .
Hence, by formula (20) applied to h =Id and x0 = 0, we have for x ≥ max {x1, 2},
ν ([x, +∞)) = E
[
(X)+
]
exp
(
−
∫ x
0
y
τν (y)dy
)( 1
x −
∫ +∞
x
1
y2 exp
(
−
∫ y
x
t
τν (t)dt
)
dy
)
≥ E
[
(X)+
]
exp
(
−
∫ x
0
y
τν (y)dy
)( 1
x −
∫ +∞
x
1
y2 exp
(
−y2 −x2
2
)
dy
)
≥ 3E
[
(X)+
]
4x exp
(
−
∫ x
0
y
τν (y)dy
)
.
It is then easily seen that Inequality (35) can be reversed, u p to a positive multiplicative constant
at the right-hand side (together with changing the value of r that can be negative). Also, if for any
c> 0 there exists x0 such that for any x ≥x0, τν (x) ≤c, then the term x−2∫ x
0 τ−1
ν (y)ydy goes to
+∞ when x tends to + ∞. This gives L+ = +∞ and concludes the proof.
