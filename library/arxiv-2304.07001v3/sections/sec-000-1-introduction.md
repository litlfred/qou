---
doc_id: arxiv-2304.07001v3
doc_title: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 2304.07001v3.pdf
source_sha256: b6c0d7f50b6407f1
doc_brief: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES — We prove resurgence properties for the Borel transform of a f ormal power series associated to elements in the Habiro ring that come from radi al"
---
The modern theory of resurgence began with the voluminous wo rks of ´Ecalle in 1981 [ 16, 17]
and 1985 [ 18]. This theory now plays a vital rˆ ole in a remarkable number o f diverse areas, to
name just a few examples: nonlinear systems of ODEs and diﬀere nce equations [ 11,42], algebraic
combinatorics [9,10], enumerative combinatorics and quantum ﬁeld theory [ 8,46], period integrals
and string theory scattering amplitudes [ 15], wall-crossing phenomena [ 43] and matrix models
[48]. In this paper, we are interested in a conjecture due to Cost in and Garoufalidis [ 13] which
connects resurgence and quantum topology. For other such in teractions, see [ 3, 19, 24–26] and
the references therein.
Let us recall the general setup from [ 13]. For further details, see [ 12, 14, 47, 49] or [ 52, Section
2] for an excellent concise review of the basic notions of res urgence and alien calculus. A formal
power series
F(x) =
∞∑
n=0
anx−n∈ C[[1/x]] (1.1)
is called Gevrey-1 if there exists positive real numbers A, B such that
|an|≤ ABnn!
for all n≥ 0. Consider a Gevrey-1 formal power series given by ( 1.1) and its Borel transform
B : C[[1/x]]−→ C[[p]] deﬁned by
B
( ∞∑
n=0
anx−n
)
= a0δ +
∞∑
n=1
an
pn−1
(n− 1)! =: a0δ + G(p) (1.2)
where δ is a formal symbol that has Laplace transform given by the con stant function 1. For
simplicity, we writeB[F](p) for the transform ( 1.2). Here, G(p) has a positive radius of conver-
gence as it arose from a Gevrey-1 power series. In a standard a buse of notation, G(p) denotes the
formal power series in ( 1.2) (and is also commonly referred to in the literature as the Bo rel trans-
form of F(x)) and the analytic continuation of the associated germ at th e origin. In addition,
Date: April 14, 2025.
2020 Mathematics Subject Classiﬁcation. 57K16, 11F37, 30B40, 40A05.
Key words and phrases. Resurgence, Habiro ring, quantum topology, strange identi ties.
1
2 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
G(p) is called a resurgent function if it is endlessly analytically continuable [
49]. This property
means G(p) extends to a (possibly multi-valued) holomorphic functio n along unbounded paths
that need only circumvent a discrete set of singularities. I n the present work, we consider the
case where G(p) deﬁnes a multi-valued function on C\N , withN a discrete set of singularities
lying on the ray R>0, e.g.,N =
{
n2π2
6 : n∈ Z>0
}
.
Assuming G(p) satisﬁes suitable growth conditions, the left and right Bo rel resummations of
F(x) are deﬁned as
S+[F](x) =
∫
γl
e−pxB[F](p) dp
and
S−[F](x) =
∫
γr
e−pxB[F](p) dp
where x∈ C and γl and γr are contours in C\N from 0 to ∞ that turn left (respectively, right)
at each singularity in N (see Figure 1). In addition, the left and right Borel resummations give
analytic functions on a sector of opening angle π in the complex x-plane.
γl
γr
N
Figure 1. A singularity set N⊂ C and the contours γl and γr.
Following [13, Sections 4.2–4.3], the median resummation of F is given by
Smed(x) = Smed[F](x) := 1
2
(
S+[F](x) + S−[F](x)
)
. (1.3)
In general, care is required when deﬁning median summations , see [ 32, Section 2]. Under fa-
vorable circumstances, for example when G(p) is the Borel transform of a formal (Gevrey-1)
solution in powers of 1 /x to a linear diﬀerential equation, each of S ±[F](x) (and thus, of course,
Smed(x)) is a well-deﬁned homomorphic solution. This is one incarn ation of the terminology
“resummation”.
In this paper, we will study the median resummation of the Bor el transform for certain formal
power series associated to knots.
Let K be a knot and JN (K; q) be the usual colored Jones polynomial, normalized to be 1
for the unknot. If N = 2, then we recover the Jones polynomial [ 39]. As a knot invariant, the
colored Jones polynomial is of fundamental importance in se veral open problems in quantum
topology (see, e.g., [ 20, 22, 40, 51, 55]). We now recall the Habiro ring [ 31]
H := lim←−n
Z[q]/⟨(q)n⟩
where
(a)n = (a; q)n :=
n∏
k=1
(1− aqk−1)
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 3
is the standard q-Pochhammer symbol. Every element of H may be written as
∞∑
n=0
bn(q)(q)n
where bn(q)∈ Z[q]. Given K, there exists an element Φ K(q)∈H called the Kashaev invari-
ant [ 41] which matches JN (K; q) (up to a prefactor) when q = ζN := e
2πi
N [38, Theorem 2]. To
illustrate, for the trefoil knot K = 31, we have [ 30, 44]
JN (31; q) = q1−N
∞∑
n=0
q−nN (q1−N )n. (1.4)
In this case, the Kontsevich-Zagier series [ 55]
Φ 31(q) :=
∞∑
n=0
(q)n∈H (1.5)
gives the Kashaev invariant for the trefoil [ 41] and so from ( 1.4) and ( 1.5), we observe
Φ 31(ζN )ζN = JN (31; ζN ).
Now, a crucial aspect of the computations in [ 13] is the “strange identity”
Φ 31(q)“ = ”− 1
2
∞∑
n=1
n
(12
n
)
q
n2−1
24 (1.6)
where “ = ” means that both sides agree to inﬁnite order at any r oot of unity and
(12
∗
)
is the
quadratic character of conductor 12. More precisely, repla cing q by the product of a root of
unity and e−x, then letting x→ 0+, the right-hand side has an asymptotic expansion as a power
series in x and this power series is given by the left-hand side at q. For further details, see [ 2,54].
If q = e2πix, x∈ H, then ( 1.6) implies for 0 ⁄= α∈ Q
e
πiα
12 Φ 31(e2πiα) =− 1
2
∞∑
n=1
n
(12
n
)
e
n2πiα
12 (1.7)
where the right-hand side of ( 1.7) is interpreted as the radial limit x→ α. The signiﬁcance of
“identities” akin to ( 1.6) is evident in various applications, e.g., asymptotics and congruences
for Fishburn and generalized Fishburn numbers modulo prime powers [1,2,4,6,27,28,53,54], the
quantum modularity of Φ 31(q) [ 29, 55] and expressing WRT invariants of Brieskorn homology
spheres in terms of limiting values of Eichler integrals [ 33–35]. For a recent advance using the
“Bailey machinery” which not only recovers ( 1.6), but produces a wealth of new examples,
see [ 45].
Elements ofH can also be formally expanded around any root of unity. There fore, we let
FK(x) := Φ K(e− 1
x )∈ C[ [1/x] ]. (1.8)
To emphasize the dependence on K, we denote the Borel transform of FK (x) by GK (p) and its
conjecturally well-deﬁned median resummation by Smed
K (x). Finally, we use the notation .= to
denote equality up to a prefactor which depends on K. We can now state the main conjecture
from [13] (slightly edited for clarity) which is part of a larger prog ram to understand the analytic
continuation of invariants of “knotted objects” arising in Chern-Simons theory [ 21, 23].
4 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
Conjecture 1.1. For every knot K,
(1) FK (x) has a resurgent Borel transform GK (p).
(2) Smed
K (x) is an analytic function deﬁned on ℜ(x) > 0 with radial limits at the points 1
2πi Q
of its natural boundary.
(3) If (2) is true, then consider the radial limit
Smed
K
(
− 1
2πiα
)
:= lim
x→− 1
2πiα
Smed
K (x)
whereℜ(x) > 0. For 0⁄= α∈ Q, we have Smed
K
(
− 1
2πiα
) .= Φ K (e2πiα).
In [ 13, Theorem 2.5, Theorem 3.1], Conjecture 1.1 (1) and (2) were proven for K = 3 1. Here,
F31 (x) = e− 1
24x
∞∑
n=0
(e− 1
x )n
where an adjustment of ( 1.8) has been made. The Borel transform G31 (p) of F31(x) is explicitly
given by [ 13, Theorem 3.1]
G31(p) = 3π
2
√
2
∞∑
n=1
n
(12
n
)
(
−p + n2π2
6
) 5/2 . (1.9)
Moreover, a close inspection of the proofs of Theorems 2.5 an d 3.1 in [ 13] reveals that it is
actually ( 1.6) and the periodic function
(12
∗
)
which determine the analytic nature of G31(p) and
Smed
31 (x). Our main goal in this paper is to prove resurgence properti es for formal power series
associated to elements in H that satisfy a general type of strange identity motivated by (1.6).
Here, we emphasize the importance of periodic functions. Be fore stating our main result, we
introduce some notation.
Let M≥ 2 be an integer and k1, k2∈ Z with 0 < k 1 < k 2 < M
2 . Let 0 ⁄= c∈ R and f be the
function
f (n) :=





c if n≡ k1, M− k1 (mod M ),
−c if n≡ k2, M− k2 (mod M ),
0 otherwise.
(1.10)
Note that under the conditions on k1 and k2, f is a well-deﬁned even function of period M with
mean value zero. For integers a≥ 0 and b > 0, consider the partial theta series
θ(ν)
a,b,f (q) :=
∞∑
n=0
nνf (n)q
n2−a
b (1.11)
where q = e2πix, x∈ H, and ν∈{ 0, 1}. For ℓ∈ Z, set
˜f (ℓ) := (−1)ℓ sin
((k2− k1)ℓπ
M
)
sin
((M− k1− k2)ℓπ
M
)
. (1.12)
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 5
Suppose there exists
Φ f (q) :=
∞∑
n=0
An,f (q)(q)n∈H
where An,f (q)∈ Z[q] such that
Φ f (q)“ = ” θ(1)
a,b,f (q). (1.13)
Finally, deﬁne
Ff (x) := e− a
bx Φ f (e− 1
x ) =
∞∑
n=0
Cn,f
n!
( 1
bx
) n
. (1.14)
The asymptotics of the partial theta series θ(1)
a,b,f (q) around q = 1, which by the strange identity
in ( 1.13) gives the expansion of Φ f (q), can be computed by L-values. By standard calculations
using the Mellin transform (see, e.g., [ 2, 28, 55]), we ﬁnd that
Cn,f = (−1)nL(−2n− 1, f)
where
L(s, f) :=
∞∑
n=1
f (n)
ns
is the L-series associated to f . In particular, using [ 2, Lemma 3.2], we obtain that
Cn,f = (−1)n+1 M 2n+1
2n + 2
M∑
m=1
f (m)B2n+2
(m
M
)
(1.15)
where for k≥ 0, Bk(x) denotes the kth Bernoulli polynomial. By ( 1.14) and ( 1.15), we have
Ff
(1
x
)
=
∞∑
n=0
(−1)n+1M 2n+1
(2n + 2)n!
M∑
m=1
f (m)B2n+2
(m
M
)( x
b
) n
. (1.16)
We will denote the Borel transform of Ff (x) by Gf (p). Here, we write Smed
f (x) for Smed(x),
Smed
f
(
− 1
2πiα
)
:= lim
x→− 1
2πiα
Smed
f (x),
θ(ν)
a,b,f (x) for θ(ν)
a,b,f (q) = θ(ν)
a,b,f (e2πix) and θ(ν)
a,b,f (α) := lim
x→α
θ(ν)
a,b,f (x) where 0 ⁄= α∈ Q. Our main
result is now the following.
Theorem 1.2. For f given by (
1.10) andFf (x) as in (1.16), we have the following:
(1)Ff (x) has a resurgent Borel transform Gf (p).
(2) Smed
f (x) is an analytic function deﬁned on ℜ(x) > 0 with radial limits at the points 1
2πi Q
of its natural boundary.
(3) For 0⁄= α∈ Q, we have
Smed
f
(
− 1
2πiα
)
= cbeπi/4
M π(iα)3/2
∫ +i∞
0
θ(0)
0,4M 2, ˜f (bp)
(1
α + p
) 3/2 dp +
( b
iα
) 3/2√
2c
M 2 θ(1)
0,4M 2, ˜f
(
− b
α
)
. (1.17)
6 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
Remark 1.3. The proof of Theorem
1.2 demonstrates resurgence properties for the normal-
ized partial theta series e− a
bx θ(1)
a,b,f (e− 1
x ) without assuming ( 1.13). Our results and those in the
announcement [ 32] appear to be related; however, we give a proof that can be use d to prove
Conjecture 1.1 for our cases of interest (see Corollary 1.5).
We give two applications of Theorem 1.2. The ﬁrst result explicitly computes ( 1.17) in the
following situation. For coprime positive integers s and t, 1 ≤ m≤ t− 1 and 1 ≤ n≤ s− 1,
let χ(n,m)
s,t (k) be the periodic function obtained by choosing c = 1, M = 2st, k1 =|nt− ms| and
k2 = nt + ms in ( 1.10), i.e.,
χ(n,m)
s,t (k) =





1 if k≡± (nt− ms) (mod 2 st),
−1 if k≡± (nt + ms) (mod 2 st),
0 otherwise .
(1.18)
For coprime odd integers s, t, deﬁne the sets
D1(s, t) :=
{
(n, m) : 1≤ n≤ s− 1
2 , 1≤ m≤ t− 1
}
(1.19)
and
D2(s, t) :=
{
(n, m) : 1≤ n≤ s− 1, 1≤ m≤ t− 1
2
}
. (1.20)
There is a bijection between D1(s, t) and D2(s, t) (see Lemma 3.1 and (3.2)). For s and t coprime
and of opposite parities, we consider
D3(s, t) :=
{{
(n, m) : 1≤ n≤ s−1
2 , 1≤ m≤ t− 1
}
if s≡ 1 (mod 2) ,{
(n, m) : 1≤ n≤ s− 1, 1≤ m≤ t−1
2
}
if s≡ 0 (mod 2) .
Finally, deﬁne the set D(s, t) of pairs which yield distinct characters in ( 1.18) as follows:
D(s, t) :=
{
D1(s, t) or D2(s, t) if s≡ t≡ 1 (mod 2) ,
D3(s, t) if s⁄≡t (mod 2) . (1.21)
One sees that D(s, t) :=|D(s, t)| = (s−1)(t−1)
2 .
Theorem 1.4. Let s and t be coprime positive integers and (n, m)∈ D(s, t). For 0⁄= α∈ Q,
we have
Smed
χ(n,m)
s,t
(
− 1
2πiα
)
= θ(1)
0,4st,χ(n,m)
s,t
(α). (1.22)
The second result veriﬁes Conjecture 1.1 for two families of torus knots.
Corollary 1.5. Let u, k∈ Z≥1. Conjecture 1.1 is true for the families of torus knots T (2, 2u+1)
and T (3, 2k).
Corollary 1.5 generalizes Theorems 2.5 and 3.1 in [ 13] and upon taking either u = 1 or k = 1
conﬁrms Conjecture 1.1 for the trefoil knot 3 1 = T (2, 3) = T (3, 2).
The paper is organized as follows. In Section 2, we prove Theorem 1.2 by ﬁrst providing
an explicit evaluation of Gf (p) in ( 2.9), which generalizes ( 1.9), and then computing Smed
f (x)
directly via a careful contour deformation argument. In Sec tion 3, we prove Theorem 1.4 and
Corollary 1.5. In Section 4, we make some concluding remarks.
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 7
