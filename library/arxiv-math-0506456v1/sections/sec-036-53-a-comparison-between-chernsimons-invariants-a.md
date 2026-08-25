---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-036-53-a-comparison-between-chernsimons-invariants-a
section_title: "A comparison between Chern–Simons invariants and critical values"
section_number: 5.3
pages: 39-43
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
of the phase functions Φa,b
n
The purpose of this section is to combine the Chern–Simons theory d escribed in the
previous two sections with the asymptotic analysis in Sec. 4.3. First w e will describe
a correspondence between the critical points of the phase funct ions Φ a,b
n in (4.36)
and the nonabelian SL(2 , C)–representations of π1(Mp/q). Thereafter we will show
that the set of Chern–Simons invariants of ﬂat irreducible SU(2)–c onnections on
Mp/q is a certain subset of the critical values of the functions Φ a,b
n . Like in Sec. 4.3
we will most of the time work with the shifted phase functions Ψ a,b
n in (4.39). We
refer to Remark 5 below for a comparison between the phase funct ions Φ a,b
n and
Ψ a,b
n . Recall the set ˜N given by (5.62).
Theorem 7. The map ( x,y ) ↦→ρ(eπix,e2πiy −1) gives a surjection ϕ from the set
of critical points ( x,y ) of the functions Ψ a,b
n , a,b,n ∈ Z, with x /∈ Z onto the set
of representations ρ(s,u) : π → SL(2, C), (s,u ) ∈ ˜N , which extend to SL(2 , C)–
representations of π1(Mp/q).
If (x,y ) is a critical point, let us say of Ψ a,b
n , then ( x + 2k,y +l) is a critical
point of Ψ a+l,b+2k
n+pk for any k,l ∈ Z, so ϕ−1(ϕ(x,y )) = { (x + 2k,y +l) |k,l ∈ Z } if
x /∈ Z.
Proof. The last statement follows immediately from (4.40), so let us concent rate on
the ﬁrst part. Let ψ : C2 → C be given by
ψ(z,w ) = (1 −zw)(w −z) −zw,
so ψ(v2,w ) = 0 if and only if ( v,w ) is a solution to (4.42). Then
ψ(z,u + 1) = −zφ(z,u )
for (z,u ) ∈ C∗ × C, where φ is the function (5.61). It follows that ( v,w ) is a solution
to (4.42) if and only if either ( v,w ) = (0, 0) or (v,w − 1) ∈ ˜N .
Next assume that ( v,u ) ∈ ˜N and put ( z,w ) = ( v2,u + 1). Since ψ(z,w ) = 0
and z ⁄= 0 we have that w ⁄= 0 and w −z ⁄= 0. Therefore 1 −zw =wz/(w −z) and
(v,w ) is a solution to (4.41) if and only if
v−p =
((w −z)2
wz
) q
=
(
wz −1 − 2 +zw −1) q
=
(
λ11(v,w − 1) − 1 −z2 +zw −1 +wz +z
) q
.
Butψ(z,w ) = 0 and w ⁄= 0 implies that −1 −z2 +zw −1 +wz +z = 0. Thus ( v,w )
is a solution to (4.41) if and only if ( s,u ) = (v,u ) is a solution to (5.64).
The above shows together with the discussion around (5.64) that t here is a one
to one correspondence between common nonzero solutions ( v,w ) to (4.41), (4.42)
with v2 ⁄= 1 and representations ρ(v,w−1) : π → SL(2, C), (v,w − 1) ∈ ˜N , which
extend to SL(2 , C)–representations of π1(Mp/q). By the remarks following (4.40)
this proves the theorem.
40 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Recall the set S in (1.5). Moreover, recall that if ( x,y ) is a critical point of Ψ a,b
n ,
a,b,n ∈ Z, with (x,y ) ∈ S then x /∈ Z is automatically satisﬁed. By Proposition 2
and the above theorem we therefore have
Corollary 3. The surjection ϕ in Theorem 7 restricts to a surjection from the
set of critical points ( x,y ) of Ψ a,b
n , a,b,n ∈ Z, with ( x,y ) ∈ S onto the set of
representations ρ(s,u) : π1(Mp/q) → SL(2, C), (s,u ) ∈ ˜N , which are equivalent to
SU(2)–representations of π1(Mp/q).
Theorem 8. Let (x,y ) ∈ C2 such that ρ(eπix,e2πiy −1) is equivalent to a nonabelian
SU(2)–representation ofπ1(Mp/q) and choose in accordance with Theorem 7 integers
a,b,n such that ( x,y ) is a critical point of Ψ a,b
n . If a′,b ′,n ′ is another such set of
integers, then b′ =b and a′ +n′/q =a +n/q. In fact we have
a + n
q = y + p
2qx + i
2π
(
Log
(
1 −e2πi(x+y)
)
− Log
(
1 −e2πi(x−y)
))
,
b = x + i
2π
(
Log
(
1 −e2πi(x+y)
)
+ Log
(
1 −e2πi(x−y)
))
.
Moreover, for any such set of integers a,b,n we have
CS(¯ρθ,ε) = Ψ a,b
n (x,y ) (mod Z),
where θ ∈ [−1/3, −1/6] ∪ [1/6, 1/3] and ε ∈ {±} with e2πiθ =eπix and 1 + uε(θ) =
e2πiy, and ¯ρθ,ε is a SU(2)–representation of π1(Mp/q) equivalent to ρ(eπix,e2πiy −1)
and given by Proposition 2.
Remark 5. i) In general we have Φ a,b
n = Ψ a+b,a−b
n , so there is a ono to one cor-
respondence between the phase functions Φ a,b
n and the phase functions Ψ a′,b′
n with
a′ +b′ even. If ( x,y ) is a critical point of Ψ a′,b′
n with a′ +b′ odd, then (x,y ) is also
a critical point of Ψ a′+1,b′
n−q by Theorem 8. In that way we see that any critical point
of one of the functions Ψ a′,b′
n is also a critical point of one of the functions Φ a,b
n .
ii) Assume that |p/q| >
√
20 and assume that ( xj,yj), j = 1, 2, are degenerate
critical points of phase functions Φ a,b
n belonging to S. Let vj = eπixj and wj =
e2πiyj . By Proposition 1 we have cos(2 πx1) = cos(2πx2) and wj =w−ε(xj ), where
ε = sign(p/q), so w1 = w2. Moreover, x1,x 2 ∈ [−2/3, −1/3] ∪ [1/3, 2/3] + 2 Z.
We are interested in comparing the equivalence classes of the repre sentationsρj =
ρ(vj,wj −1). For that purpose we can without loss of generality assume that x1,x 2 ∈
[1/3, 2/3]. Then x2 = x1 or x2 = 1 −x1. In the second case v2 = −v1. Note here
that −v1 = v−1
1 if and only if v1 ∈ {±i}. But in that case cos(2 πx1) = −1 and
by (4.53) we get that p/q ∈ {±2/
√
5} which is impossible. Thus ρ1 and ρ2 are not
equivalent. If p is odd we must have x2 =x1 since only one of the points ( v1,w 1),
(−v1,w 1) can be a solution to (4.41). If p is even both ( v1,w 1) and ( −v1,w 1) are
solutions to both of the equations (4.41) and (4.42). Thus Proposit ion 1 shows that
the set of degenerate critical points in S of the phase functions Φ a,b
n , a,b,n ∈ Z,
is either empty or corresponds under the surjection in Theorem 7 t o one point in
Mp/q in case p is odd and to two points in the moduli space in case p is even.
Asymptotics of the quantum invariants for the ﬁgure 8 knot 41
The phase functions Ψ 0,0
n , Ψ 1,−1
n , Ψ 1,1
n and Ψ 2,0
n are the ones entering Conjec-
ture 3. By Theorem 8 the parameter b is ﬁxed by a critical point of Ψ a,b
n , while
a and n can be varied as long as we keep ﬁxed a +n/q. Because of this (see also
Lemma 5 below) we only need to consider Ψ 0,0
n , Ψ 0,−1
n , and Ψ 0,1
n . By Theorem 8
(and also the proof of this theorem and Proposition 2) we get
Corollary 4. Let (x,y ) ∈ C2 such that ρ(eπix,e2πiy −1) is equivalent to a nonabelian
SU(2)–representation of π1(Mp/q). Let ( x′,y ′) ∈ C2 such that ( eπix′
,e 2πiy′
) =
(eπix,e 2πiy) and Re(x′) ∈] − 1, 1] and Re(y′) ∈] − 1/2, 1/2]. Moreover, let
n = q
(
y′ + p
2qx′ + i
2π
(
Log
(
1 −e2πi(x+y)
)
− Log
(
1 −e2πi(x−y)
)) )
,
b = x′ + i
2π
(
Log
(
1 −e2πi(x+y)
)
+ Log
(
1 −e2πi(x−y)
))
.
Then θ :=x′/2 ∈ [−1/3, −1/6] ∪ [1/6, 1/3] and
b =



−1, θ ∈ [−1/3, −1/4]
0, θ ∈] − 1/4, −1/6] ∪ [1/6, 1/4]
1, θ ∈]1/4, 1/3].
Moreover,n ∈ Z and (x′,y ′) is a critical point of Ψ 0,b
n and
CS(¯ρθ,ε) = Ψ 0,b
n (x′,y ′) (mod Z),
whereε ∈ {±} with 1+uε(θ) = e2πiy, and ¯ρθ,ε is a SU(2)–representation ofπ1(Mp/q)
equivalent to ρ(eπix,e2πiy −1) and given by Proposition 2.
We note that the ﬁrst part of Theorem 8 is an immediate consequenc e of (4.40).
To prove the second part we start by observing that if a,a ′,n,n ′,b are integers such
that a′ +n′/q = a +n/q then Ψ a,b
n (x,y ) − Ψ a′,b
n′ (x,y ) is an integer independent of
(x,y ) ∈ C2. The remaining part of the proof will consists of a series of lemmas. W e
start by
Lemma 5. Let a,b,n ∈ Z and assume that ( x,y ) is a critical point of Ψ a,b
n . Let
l,k ∈ Z and put a′ =a +l, b′ =b + 2k, and n′ =n +pk. Then ( x + 2k,y +l) is a
critical point of Ψ a′,b′
n′ and
Ψ a′,b′
n′ (x + 2k,y +l) − Ψ a,b
n (x,y ) ≡ 0 (mod Z).
Proof. That (x + 2k,y +l) is a critical point of Ψ a′,b′
n′ is an immediate consequence
of (4.40) and was already observed in Theorem 7. Put x′ =x + 2k and y′ =y +l.
Since e2πix′
=e2πix and e2πiy′
=e2πiy we get
Ψ a′,b′
n′ (x′,y ′) − Ψ a,b
n (x,y ) = a′x′ +b′y′ −x′y′ + n′
q x′ − p
4qx′2 − d
qn′2
−ax −by +xy − n
qx + p
4qx2 + d
qn2
= 2( a +l)k + 2n
q (1 −pd)k + p
q (1 −pd)k2.
42 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Here pd −cq = 1 for an integer c so
Ψ a′,b′
n′ (x′,y ′) − Ψ a,b
n (x,y ) = 2(a +l −nc)k −pck2.By Proposition 2 and the above lemma we are thus left with the following
to prove: Let θ ∈ [−1/3, −1/6] ∪ [1/6, 1/3] and assume that ¯ ρθ,ε extends to a
representation of π1(Mp/q) for ε ∈ {±} . Let b = b(θ) and n = n(θ) be the unique
integers such that (2θ,y ) is a stationary point of Ψ 0,b
n , where y = 1
2πi Log(1 +uε(θ))
(so Re(y) = 1
2 ) (see around (4.43) and (4.44)). Then
CS(¯ρθ,ρ) = Ψ 0,b
n (2θ,y ) (mod Z). (5.78)
In the course of the proof of this identity we will prove that
CS(¯ρθ,ε) = − 1
6 − p
qθ2 + m
q 2θ − d
qm2 − 2
∫ θ
1/6
βε(t)dt (mod Z), (5.79)
for θ ∈ [1/6, 1/3], where m = pθ +qβε(θ) ∈ Z by (5.74). Unfortunately the proof
of (5.78) is rather technical, but we have tried to emphasize the main ideas of the
proof here and defer many technicalities to the appendices C and D.
The Chern–Simons invariants of SU(2)–connections are real, so we begin by
investigating to what extent a general phase function Ψ a,b
n ,a,b,n ∈ Z, is real in its
critical points. Assume that ( x,y ) is such a critical point and write z =e2πix and
w =e2πiy as usual. From (4.40) we ﬁnd that
a − Re(y) = p
2q Re(x) − n
q − 1
2π Im
(
Log(1 −zw) − Log(1 −zw −1)
)
,
and
b − Re(x) = − 1
2π Im
(
Log(1 −zw) + Log(1 −zw −1)
)
.
Moreover, we have Im( x) = − 1
2π Log|z| and Im(y) = − 1
2π Log|w|. By (4.39) we
therefore get
Im
(
Ψ a,b
n (x,y )
)
= ( a − Re(y))Im(x) + (b − Re(x))Im(y) − p
2q Im(x)Re(x)
+n
q Im(x) + 1
4π2 Im
(
Li2(zw) − Li2(zw −1)
)
.
This together with the above expressions for a − Re(y) and b − Re(x) leads to the
formula
Im
(
Ψ a,b
n (x,y )
)
= 1
4π2
(
Im(Log(1 −zw) − Log(1 −zw −1))Log|z|
+Im(Log(1 −zw) + Log(1 −zw −1))Log|w|
+ Im
(
Li2(zw) − Li2(zw −1)
))
.
Asymptotics of the quantum invariants for the ﬁgure 8 knot 43
By introducing the Bloch–Wigner dilogarithm function
D(z) = Im (Li 2(z)) + Arg(1 −z)Log|z|
we obtain
Lemma 6. Let a,b,n ∈ Z and let (x,y ) be a critical point of Ψ a,b
n . Then
Im
(
Ψ a,b
n (x,y )
)
= 1
4π2
(
D
(
e2πi(x+y)
)
−D
(
e2πi(x−y)
))
.
We note that D is analytic on C \ {0, 1} and continuous on C. Moreover, D
satisﬁes the identities
D(z) +D(¯z) = 0, D (z) +D(1/z) = 0 (5.80)
for all z ∈ C \ {0}. From this we have
Corollary 5. Leta,b,n ∈ Z and let (x,y ) be a critical point of Ψ a,b
n withe2πix ∈S1
and e2πiy ∈ R. Then
Im
(
Ψ a,b
n (x,y )
)
= 0.
Remark 6. Let (v,w ) be a non-zero solution to (4.41) and (4.42). Then (¯ v, ¯w) is
also a solution to these two equations as already observed. Let z = v2 and write
(z,w ) = (e2πix,e 2πiy). Then (¯z, ¯w) = (e−2πi¯x,e −2πi ¯y). If ( x,y ) is a critical point of
Ψ a,b
n , then ( −¯x, −¯y) is a critical point of Ψ −a,−b
−n . By Lemma 6 and (5.80) we have
Im
(
Ψ a,b
n (x,y )
)
= −Im
(
Ψ −a,−b
−n (−¯x, −¯y)
)
.
Hence, if this value is diﬀerent from zero, then either exp(2 πirΨ −a,−b
−n (−¯x, −¯y))
or exp(2πirΨ a,b
n (x,y )) grows exponentially. We note that by Conjecture 3 and
Corollary 5 stationary points leading to such exponential growth do not contribute
to the large r asymptotics of ¯τr(Mp/q), see also Theorem 4.
We now embark upon proving (5.78). We start by reducing to the cas e θ ∈
[1/6, 1/3]. By Proposition 2 we know that the representations ¯ ρθ,ε and ¯ρ−θ,ε are
SU(2)–equivalent, so in particular they have the same Chern–Simon s invariant.
Lemma 7. Let the situation be as in (5.78). Then
