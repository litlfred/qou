---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗"
section_id: sec-001-2-basic-notations
section_title: "Basic notations"
section_number: 2
pages: 5-8
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗ — We show an asymptotic formula of the divergent bilateral bas ic hypergeometric series 1ψ 0(a; −;q, ·)"
---
In this section, we ﬁx our notations. We assume that 0 < |q|< 1 andσq is the
q-diﬀerence operator such that σqf (x) = f (qx). The basic hypergeometric
series is
rϕ s(a1,...,a r;b1,...,b r;q,x )
:=
∑
n≥ 0
(a1,...,a r;q)n
(b1,...,b s;q)n(q;q)n
{
(−1)nq
n(n− 1)
2
} 1+s− r
xn. (6)
The radius of convergence ρ of the basic hypergeometric series is given by [7]
ρ =



∞, if r <s + 1,
1, if r =s + 1,
0, if r >s + 1.
The bilateral basic hypergeometric series is
rψ s(a1,...,a r;b1,...,b s;q,x )
:=
∑
n∈ Z
(a1,...,a r;q)n
(b1,...,b s;q)n
{
(−1)nq
n(n− 1)
2
} s− r
xn. (7)
Ifs<r , the series (7) diverges for x ⁄= 0 and if r =s, the series (7) converges
|b1...b s/a 1...a r| < |x| < 1 (see [3] for more detail). The series (6) is a q-
analogue of the generalized hypergeometric function
rFs(α 1,...,α r;β1,...,β s;x) :=
∑
n≥ 0
(α 1,...,α r)n
(β1,...,β s)nn!xn
and the series (7) is a q-analogue of the bilateral hypergeometric function
rHs(α 1,...,α r;β1,...,β s;x) :=
∑
n∈ Z
(α 1,...,α r)n
(β1;...,β s)n
xn.
5
By D’Alembert’s ratio test, it can be checked that rHr converges only for
|x| = 1 [12], provided that ℜ(β1 + · · · +βr −α 1 − · · · −α r)> 1.
The q-exponential function eq(x) is
eq(x) := 1ϕ 0(0; −;q,x ) =
∑
n≥ 0
xn
(q;q)n
The function eq(x) has the inﬁnite product representation as follows;
eq(x) = 1
(x;q)∞
, |x|< 1.
The limit q → 1 − 0 of eq(x) is the exponential function [3];
lim
q→ 1− 0
eq(x(1 −q)) = ex. (8)
The q-gamma function Γ q(x) is
Γ q(x) := (q;q)∞
(qx;q)∞
(1 −q)1− x, 0<q < 1.
The limit q → 1 − 0 of Γ q(x) gives the gamma gunction [3];
lim
q→ 1− 0
Γ q(x) = Γ(x). (9)
The theta function of Jacobi is given by
θ(x) :=
∑
n∈ Z
q
n(n− 1)
2 xn, ∀x ∈ C∗.
Jacobi’s triple product identity is
θ(x) = (q, −x, −q/x ;q)∞
and the theta function satisﬁes the following q-diﬀerence equation
θ(qkx) = x− kq− k(k− 1)
2 θ(x), ∀k ∈ Z.
The inversion formula is
θ(x) = xθ(1/x ). (10)
We remark that θ(λq k/x ) = 0 if and only if x ∈ [−λ;q]. In our study, the
following proposition [15] is useful to consider the limit q → 1 − 0 of our
formula.
6
Proposition 1. For any x ∈ C∗(−π <argx<π ), we have
lim
q→ 1− 0
θ(qαx)
θ(qβx) =xβ − α (11)
and
lim
q→ 1− 0
θ
( qαx
(1 −q)
)
θ
( qβx
(1 −q)
) (1 −q)β − α =
( 1
x
) α − β
. (12)
We also use the limit [3] as follows;
lim
q→ 1− 0
(xqα ;q)∞
(x;q)∞
= (1 −x)− α, |x|< 1. (13)
3 An asymptotic formula of the divergent se-
ries 1ψ 0(a; −;q,x )
In this section, we show an asymptotic formula of the divergent ser ies 1ψ 0(a; −;q,x ).
At ﬁrst, we review Ramanujan’s sum for 1ψ 1(a;b;q,z ) and its property. Ra-
manujan gives the following sum [4]
1ψ 1(a;b;q,z ) = (q,b/a,az,q/az ;q)∞
(b,q/a,z,b/az ;q)∞
, |b/a |< |z|< 1. (14)
We can regard this sum as a q-analogue of the bilateral binomial theorem [6]
as follows;
Theorem. (Horn [6]) If z is a complex number such that |z| = 1, we have
1H1(α ;β ;z) = Γ(β )Γ(1 −α )
Γ(β −α )
(1 −z)β − α − 1
(−z)β − 1 , (15)
provided that ℜ(β −α )> 1.
Let z is a complex number such that −π < argz < π. The summation
(14) is rewritten by
(q,b/a,az,q/az ;q)∞
(b,q/a,z,b/az ;q)∞
= (q,b/a ;q)∞
(b,q/a ;q)∞
θ(−az)
θ(−aqz/b )
(aqz/b ;q)∞
(z;q)∞
. (16)
7
In (16), we put a =qα and b =qβ (with ℜ(β −α )> 1), we obtain
1ψ 1(qα ;qβ ;q,z ) = Γ q(β )Γ q(1 −α )
Γ q(β −α )
θ(qα (−z))
θ(qα +1− β (−z))
(qα +1− βz;q)∞
(z;q)∞
, (17)
where |qβ − α | < |z| < 1. Combining (9), (11) and (13), we can check out
that the limit q → 1 − 0 of (17) gives the bilateral binomial theorem (15),
provided that −π <argz <π.
The bilateral basic hypergeometric series 1ψ 1(a;b;q,z ) satisﬁes the q-
diﬀerence equation
( b
q −az
)
u(qz) + (z − 1)u(z) = 0. (18)
We consider the degeneration of the equation (18) in the next sect ion.
