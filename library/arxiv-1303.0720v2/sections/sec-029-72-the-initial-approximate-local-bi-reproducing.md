---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-029-72-the-initial-approximate-local-bi-reproducing
section_title: "The initial approximate local bi-reproducing kernel. We now turn our attention to the"
section_number: 7.2
pages: 20-23
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
space PA2
q,m with q = 2 (the bianalytic case). The ﬁrst step is to ﬁnd the analogue in this setting
of the kernel Mm given by (6.3.1), and then to obtain an approximate reproducing identity
similar to (6.3.3).
We keep the assumptions on the potential Q and the disk D(z0, r) from Subsection 6.1, and
the smooth cut-oﬀfunction χ0 will be as in Subsection 6.3. We will need to add the requirement
that r∥¯∂2χ0∥L2(Ω) is uniformly bounded by an absolute constant, which is possible to achieve.
Suppose u is biholomorphic (or bianalytic) in D(z0, r), which means that ¯∂2u = 0 there. It
is well-known that the fundamental solution to ¯∂2
z is ¯z/(πz). By integration by parts applied
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
21
twice, we have that
(7.2.1)
Z
Ω
u(w)χ0(w) ¯∂2
w
 ¯w −¯z
w −ze2m(z−w)θ

dA(w) =
Z
Ω
¯w −¯z
w −ze2m(z−w)θ ¯∂2
w{u(w)χ0(w)}dA(w)
=
Z
Ω
¯w −¯z
w −ze2m(z−w)θn
2 ¯∂wu(w) ¯∂wχ0(w) + u(w) ¯∂2
wχ0(w)
o
dA(w)
=
Z
Ω
e2m(z−w)θu(w)

2
¯∂wχ0(w)
z −w
−¯w −¯z
w −z
¯∂2
wχ0(w) −4m(¯z −¯w) ¯∂wχ0(w) ¯∂wθ

dA(w).
Here, the integral on the left-hand side needs to be understood in the sense of distribution
theory. If we combine (7.2.1) with (6.2.1), it follows that we obtain the estimate

Z
Ω
u(w)χ0(w) ¯∂2
w
 ¯w −¯z
w −ze2m(z−w)θ

dA(w)

≤emQ(z)−1
18 mr2∆Q(z)
Z
Ω
|u(w)|

2

¯∂wχ0(w)
z −w

 + | ¯∂2
wχ0(w)| + 4m

(¯z −¯w) ¯∂wχ0(w) ¯∂wθ


e−mQ(w)dA(w),
for z ∈D(z0, 1
3r). Next, if we assume that u ∈PA2
q,m, with q = 2, so that – in particular – u
extends biholomorphically to Ω, then
(7.2.2)

Z
Ω
u(w)χ0(w) ¯∂2
w
 ¯w −¯z
w −ze2m(z−w)θ

dA(w)

≤r−1emQ(z)−1
18 mr2ǫ0∥u∥m

6∥¯∂χ0∥L2(Ω) + r∥¯∂2χ0∥L2(Ω) + 5mr2∥¯∂χ0∥L2(Ω)∥¯∂wθ∥L∞(D(z0, 3
4 r)2)

,
= O

r−1emQ(z)−δ0m∥u∥m
n
1 + mr2∥¯∂wθ∥L∞(D(z0, 3
4 r)2)
o
,
for z ∈D(z0, 1
3r), where we write as before δ0 =
1
18r2ǫ0, and the implied constant is absolute. We
interpret (7.2.2) as saying that the left-hand side decays exponentially small compared with
the typical size emQ(z). Let δ0 denote the distribution which corresponds to a unit point mass at
0 in the complex plane C. By a direct calculation, we ﬁnd that
(7.2.3)
1
π
¯∂2
w
 ¯w −¯z
w −ze2m(z−w)θ

= δ0(z −w) −M2,m(z, w)e−2mQ(w),
where M2,m is the kernel
(7.2.4)
M2,m(z, w) :=
4m
π
¯∂wθ −2m
π (¯z −¯w) ¯∂2
wθ −4m2
π |z −w|2( ¯∂wθ)2

e2mQ(z,w).
The kernel M2,m is the bianalytic analogue of the kernel Mm which was our staring point in
Subsection 6.3. It is also automatically bianalytic in z, but not necessarily in ¯w.
Proposition 7.1. We have that for all u ∈PA2
2,m,
u(z) =
Z
Ω
u(w)χ0(w)M2,m(z, w) e−2mQ(w)dA(w) + O

r−1emQ(z)−δ0m∥u∥m
n
1 + mr2∥¯∂wθ∥L∞(D(z0, 3
4 r)2)
o
,
for z ∈D(z0, 1
3r), where δ0 =
1
18r2ǫ0 > 0. The implied constant is absolute.
Proof. This is an immediate consequence of the relation (7.2.3) and of the estimate (7.2.2).
□
22
ANTTI HAIMI AND HAAKAN HEDENMALM
7.3. Approximate local kernels. We will interpret Proposition 7.1 as saying that the function
M2,m(z, w) is a local bi-reproducing kernel mod(me−δm), with δ = δ0 > 0. Generally, we say that
a function Lm(z, w) deﬁned on D(z0, r) and biholomorphic in z is a a local bi-reproducing kernel
mod(e−δm) if
u(z) =
Z
Ω
u(w)χ0(w)Lm(z, w) e−2mQ(w)dA(w) + O(∥u∥memQ(z)−mδ),
z ∈D(z0, 1
3r),
holds for large m and all u ∈PA2
2,m. Here and in the sequel, it is implicit that δ should be
positive. Analogously, a function Lm(z, w) deﬁned on D(z0, r) and biholomorphic in z is a a local
bi-reproducing kernel mod(m−k) if
u(z) =
Z
Ω
u(w)χ0(w)Lm(z, w) e−2mQ(w)dA(w) + O(∥u∥mm−kemQ(z)),
z ∈D(z0, 1
3r),
holds for large m and all u ∈PA2
m. We speak of approximate local bi-reproducing kernels when
it is implicit which of the above senses applies. The bianalytic Bergman kernel K2,m(z, w) is of
course an approximate local bi-reproducing kernel in the above sense (no error term!), and it
has the additional property of being biholomorphic in ¯w. This suggests the term approximate
local bianalytic Bergman kernel for an approximate local bi-reproducing kernel, which is biholo-
morphic in ¯w. It remains to describe the corrective algorithm which turns the approximate
local bi-reproducing kernel into an approximate local bianalytic Bergman kernel.
7.4. Bi-negligible amplitudes. We recall the deﬁnition of the diﬀerential operator ∇in (6.4.1).
By squaring the operator identity (6.4.3), we arrive at
n
M ¯∂wθ∇M ¯∂wθ∇A(z, w)
o
e2m(z−w)θ = ¯∂2
w
n
A(z, w)e2m(z−w)θo
,
provided that A(z, w) depends C∞-smoothly on the pair (z, w). As a consequence, we have by
integration by parts (applied twice) that
(7.4.1)
Z
Ω
u(w)χ0(w)
n
M ¯∂wθ∇M ¯∂wθ∇A(z, w)
o
e2m(z−w)θdA(w)
=
Z
Ω
u(w)χ0(w) ¯∂2
w
n
A(z, w)e2m(z−w)θo
dA(w) =
Z
Ω
A(z, w)e2m(z−w)θ ¯∂2
w{u(w)χ0(w)}dA(w)
=
Z
Ω
A(z, w)e2m(z−w)θn
2 ¯∂wu(w) ¯∂wχ0(w) + u(w) ¯∂2
wχ0(w)
o
dA(w)
= −
Z
Ω
u(w)e2m(z−w)θn
2 ¯∂wA(z, w) ¯∂wχ0(w) + A(z, w)[4m(z −w) ¯∂wχ0(w) ¯∂wθ + ¯∂2
wχ0(w)]
o
dA(w),
provided u is biholomorphic on D(z0, r). If u ∈PA2
2,m, we can now obtain the estimate (use
(6.2.1))
(7.4.2)

Z
Ω
u(w)χ0(w)
n
M ¯∂wθ∇M ¯∂wθ∇A(z, w)
o
e2m(z−w)θdA(w)

 ≤emQ(z)−δ0m
×
Z
Ω
|u(w)| e−mQ(w)n
2| ¯∂wA(z, w) ¯∂wχ0(w)| + |A(z, w)|[5mr|¯∂wχ0(w) ¯∂wθ| + | ¯∂2
wχ0(w)|]
o
dA(w)
≤r−1emQ(z)−δ0m∥u∥m
n
2r∥¯∂wA∥L∞(D(z0, 3
4 r)2)∥¯∂χ0∥L2(Ω) + ∥A∥L∞(D(z0, 3
4 r)2)[r∥¯∂2χ0∥L2(Ω)
+ 5mr2∥¯∂wθ∥L∞(D(z0, 3
4 r)2)∥¯∂χ0∥L2(Ω)]
o
= O

r−1emQ(z)−δ0m∥u∥m
n
r∥¯∂wA∥L∞(D(z0, 3
4 r)2) + ∥A∥L∞(D(z0, 3
4 r)2)[1 + mr2∥¯∂wθ∥L∞(D(z0, 3
4 r)2)]
o
,
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
23
for z ∈D(0, 1
3r), where δ0 =
1
18r2ǫ0 > 0, as before. We note that the implied constant in (7.4.2)
is absolute. If we allow the implied constant in “O” to depend on the triple (A, z0, r), then the
right-hand side of (7.4.2) may be condensed to O(memQ(z)−δ0m∥u∥m), for m ≥1.
Compared with the typical size emQ(z), (7.4.2) says that the estimated quantity decays ex-
ponentially in m. For this reason, we call expressions of the form M ¯∂wθ∇M ¯∂wθ∇A bi-negligible
amplitudes.
