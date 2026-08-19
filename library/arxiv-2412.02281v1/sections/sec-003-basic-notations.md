---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-003-basic-notations
section_title: "Basic Notations"
section_number: null
pages: 3-5
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
the q-Borel resummation. Section 2.4 then gives the explicit con nection formula of the equation (5) via the
conﬂuence method.
2.1 Basic Notations
We recall some basic notations of q-calculus with 0 <q< 1 (referring to [8] for more details):
• The q-Pochhammer symbol is
(a;q)n :=
ß 1, if n = 0,∏ n−1
l=0 (1 −aql), if n ≥ 1.
Moreover, (a;q)∞ := ∏ ∞
l=0
(
1 −aql)
and
(a1,a 2,...,a m;q)∞ := (a1;q)∞ (a2;q)∞ · · · (am;q)∞.
3
• The q-theta function is
θq(z) :=
∑
n∈Z
q
n(n−1)
2 zn, z ∈ C∗.
It satisﬁes
θq(qnz) = z−nq− n(n−1)
2 θq(z) = θq
Å 1
qn−1z
ã
, n ∈ Z, (6)
and the Jacobi’s triple product identity
θq(z) = (q, −z, −q/z ;q)∞. (7)
• The q-exponential function is
eq(z) := 1
((1 −q)z;q)∞
,
with the Taylor expansion
eq(z) =
∞∑
k=0
(1 −q)k
(q;q)k
zk, 0 ≤ |z|< 1. (8)
• The q-Gamma function Γ q(z) is
Γq(z) := (q;q)∞
(qz;q)∞
(1 −q)1−z, z ∈ C\{0, −1, −2,... },
where qz and (1 −q)1−z take the principal values.
2.2 Basic Hypergeometric Series
Deﬁnition 2.1. A basic hypergeometric series associated to a = (a1,a 2,...,a n) and b = (b1,b 2,...,b m) is
nϕm
Å a1,a 2,...,a n
b1,...,b m
;q,z
ã
:=
∞∑
k=0
∏ n
l=1 (al;q)k
(q;q)k
∏ m
l=1 (bl;q)k
[
(−1)kq
k(k−1)
2
] 1+m−n
zk,
for b1,...,b m /∈q−N. We also denote it by nϕm(a1,a 2,...,a n;b1,...,b m;q,z ), or simply nϕm(a; b;q,z ).
The basic hypergeometric series is a q-analog of the generalized hypergeometric series deﬁned as follows.
Deﬁnition 2.2. A generalized hypergeometric series for α = (α 1,...,α n) and β = (β 1,...,β m) is deﬁned as
nFm
Å α 1,α 2,...,α n
β 1,...,β m
;z
ã
:=
∞∑
k=0
∏ n
l=1 (αl)k
∏ m
l=1 (βl)k
zk
k!,
where (α )0 = 1 and (α )k =α (α + 1) · · · (α +k − 1), for k ≥ 1 and βl /∈ Z≤0, for 1 ≤l ≤m. We also denote
it by nFm(α 1,α 2,...,α n;β 1,...,β m;z), or simply nFm(α ; β ;z).
Proposition 2.3 (see e.g., [28, Chapter 16, Chapter 17]) . The radius of convergence of nϕm (a; b;q,z ) and
nFm (α ; β ;z) is 0, 1 and ∞, for n ≥m + 2, n =m + 1 and n ≤m respectively.
The equation (5) is a special case of the hypergeometric q-diﬀerence equation:
z
n∏
l=1
(1 −alσq)y(z) = (1 −σq)
n−1∏
l=1
Å
1 − bl
qσq
ã
y(z), (9)
and we have
Proposition 2.4 ([5]). If the following condition holds for a1,...,a n,b 1,...,b n−1:
ai ⁄= 0, ai/a j /∈qZ\{0}, for 1 ≤i,j ≤n, and bl ⁄= 0, for 1 ≤l ≤n − 1,
then the equation (9) has a fundamental system of meromorphic solutions around in ﬁnity:
nϕn−1
Ç
ai,a iq/b 1,...,a iq/b n−1
aiq/a 1,..., ÷aiq/a i,...,a iq/a n
;q, q ∏ n−1
l=1 bl
z ∏ n
l=1al
å
z− logqai, for i = 1,...,n. (10)
Here ÷aiq/a i means the i-th item aiq/a i is skipped.
4
When an = 0, nϕn−1
Å a1,a 2,...,a n−1, 0
b1,...,b n−1
;q,z
ã
is known as a conﬂuent type basic hypergeometric series,
and satisﬁes the conﬂuent hypergeometric q-diﬀerence equation (5). The equation (5) also has a solutio n of
the form
Ä
1 +c1z−1 +c2z−2 +...
äz
∑ n−1
l=1 logq (al/b l)
(z;q)∞
,
where ck can be uniquely determined recursively and 1 + ∑ ∞
k=1ckz−k is convergent on some neighbourhood
of inﬁnity (see e.g., [2]). Then we get
Proposition 2.5. Suppose the following condition holds for a1,...,a n−1,b 1,...,b n−1:
ai ⁄= 0, ai/a j /∈qZ\{0}, for 1 ≤i,j ≤n − 1, and bl ⁄= 0, for 1 ≤l ≤n − 1,
then the equation (5) has a fundamental system of formal solutions around inﬁnity :
ˆfq(z) =
Ä ˆfq(z)1,..., ˆfq(z)n−1,f q(z)n
ä
:=
(
ˆhq(z)1 ·z− logqa1,..., ˆhq(z)n−1 ·z− logqan−1,h q(z)n · z
∑ n−1
l=1 logq (al/b l)
(z;q)∞
)
, (11)
with
ˆhq(z)i = nϕn−2
Ç
ai,a iq/b 1,...,a iq/b n−1
aiq/a 1,..., ÷aiq/a i,...,a iq/a n−1
;q,
∏ n−1
l=1 bl
aiz ∏ n−1
l=1 al
å
, for i = 1,...,n − 1,
hq(z)n = 1 + c1z−1 +c2z−2 +..., (12)
with ck uniquely determined in a recursive way. The equation (5) also has a fundamental system of meromor-
phic solutions around the origin:
f (0)
q (z) =
Ä
f (0)
q (z)1,...,f (0)
q (z)n−1,f (0)
q (z)n
ä
,
with
f (0)
q (z)i := nϕn−1
Ç qa1/b i,...,qa n−1/b i, 0
q2/b i,qb 1/b i,..., ÷qbi/b i,...,qb n−1/b i
;q,z
å
z1−logqbi, for i = 1,...,n − 1,
f (0)
q (z)n := nϕn−1
Å a1,a 2,...,a n−1, 0
b1,...,b n−1
;q,z
ã
.
