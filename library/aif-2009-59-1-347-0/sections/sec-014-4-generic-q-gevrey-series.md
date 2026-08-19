---
doc_id: aif-2009-59-1-347-0
doc_title: "L’INSTITUT FOURIER"
section_id: sec-014-4-generic-q-gevrey-series
section_title: "Generic q-Gevrey series"
section_number: 4
pages: 36-42
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "ANNALESDEL’INSTITUTFOURIER ANNALES L’INSTITUT FOURIER — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
We call generic q-Gevrey series a power series ˆf ∈ C[[x]] satisfying a
q-diﬀerence equation ∆ ˆf ∈ C{x} for some analytic q-diﬀerence operator ∆
of the form:
(4.1)
∆ := a0(x)(xσq)n +a1(x)(xσq)n−1 +... +an(x),
with aj ∈ C{x}, a0(0)an(0) ⁄= 0,
andσq(f (x)) = f (qx). This means that the associated Newton polygon has
only one ﬁnite slope equal to one ( cf. [13] and [ 20]).
An explicit calculation ( cf. also [ 6, Lemma 1.1.10]) shows that
Lemma 4.1. — Let dq = σq−1
x(q−1) and consider a q-diﬀerence operator
∆ ∈ C{x}[σq]. Then ∆ can be written as (4.1) if and only if it can be
rewritten in the following form:
(4.2)
∆ :=b0(x)(x2dq)n+b1(x)(x2dq)n−1+...+bn(x), b j ∈ C{x}, b0(0)bn(0) ⁄= 0.
Notice that the q-Euler series ˆE(x) considered in previous section is a
generic q-Gevrey series.
4.1. T wo formal q-Borel transforms
The classical Borel transform associates to each power series
∑
n/greaterorequalslant0
anxn+1
the more convergent (or less divergent ) power series ∑
n/greaterorequalslant0
an
n!ξn. For the
solutions of a q-diﬀerence equations, the Gevrey “scaling factor” (n!)s is
replaced by the q-Gevrey one: (qsn2/2) (cf. [4],[13],[20],[21]). Indeed, in the
literature there are (at least) two q-analogs of the factorial n!, namely [n]!
q
and qn(n−1)/2. The reason for this dichotomy is the identity
[n]!
q = (q;q)n
(1 −q)n = (p;p)n
(1 −p)nqn(n−1)/2 = [n]!
pqn(n−1)/2,
which implies that
(4.3) [n]!
q ∼ qn(n−1)/2
(1 −p)n , when n → +∞.
TOME 59 (2009), F ASCICULE 1
382 Lucia DI VIZIO & Changgui ZHANG
Let us consider the following two formal Borel transforms, associated to
those q-factorials:
Bq : xC [[x]] → C [[ξ]],
∑
n/greaterorequalslant0
anxn+1 ↦− →
∑
n/greaterorequalslant0
an
[n]!q
ξn
and
Bq : xC [[x]] → C [[ξ]],
∑
n/greaterorequalslant0
anxn+1 ↦− →
∑
n/greaterorequalslant0
an
qn(n−1)/2ξn.
Following J.P. Ramis [ 13] we set:
Definition 4.2. — An entire function φ is said to have q-exponential
growth of order 1 at ∞ if there exist two constants K >0 and µ> 0 such
that
|φ(x)|<K |x|µeq(|x|), |x| → ∞.
Remark that the function eq(|x|) can be replaced by eln2 |x|/(2 ln q).
Lemma 4.3 ([13, Prop. 2.1]) . — Let Eq be the set of all the entire
functions having a q-exponential growth of order 1 at ∞, and let C{x}
be the set of all power series having a positive convergence radius. Then
Eq = Bq(xC{x}) = Bq(xC{x}).
The following function space Hq has been introduced in [ 23] and [ 15]; see
also [ 20].
Definition 4.4. — For any λ ∈ C∗, let [λ;q] = λqZ.
(1) A germ of function φ analytic at 0 is said to belong to H[λ;q] if there
exist a domain Ω ⊂ C and a real number r> 0 such that:
• ∪m/greaterorequalslant0{x ∈ C : |x −λqm|<rq m} ⊂ Ω;
• φ can be continued to be an analytic function on Ω with a
q-exponential growth of order 1 at inﬁnity.
(2) A germ of function φ analytic at 0 is said to belong to Hq if there
exist a ﬁnite set Λ ⊂ C∗ such that φ ∈ H[λ;q] for any λ ∈ C∗ \ Λ.
Proposition 4.5. — Let ˆf ∈ xC[[x]], λ ∈ C∗ and let ψ = Bq ˆf , φ =
Bq ˆf . Then ψ ∈ H[λ;q] if and only if φ ∈ H[(1−p)λ;q].
Moreover, the map ∑
n/greaterorequalslant0anxn ↦→∑
n/greaterorequalslant0an[n]!
pxn induces an automor-
phism of the vector space Hq.
Proof. — Use the integral representation for the corresponding Hadamard
product. □
Definition 4.6. — Let λ ∈ C∗ and let ˆf ∈xC[[x]].
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 383
(1) We set C{x}[λ;q]
q = B−1
q H[λ/(1−p);q] = B−1
q H[λ;q]. We say that ˆf ∈
C{x}[λ;q]
q is q-Borel summable along [λ;q].
(2) Each element of D Sˆf := {[λ;q] : ˆf /∈ C{x}[λ;q]
q } will be called singu-
lar direction of ˆf .
(3) If D Sˆf is ﬁnite, ˆf is called q-Borel summable and we denote C{x}q
the set of q-Borel summable series.
Theorem 4.7 ([23, Thm. 1.2.1]) . — Every generic q-Gevrey series is
q-Borel summable.
4.2. Diﬀerent kinds of q-exponential summation
The classical Borel-Laplace exponential summation is based on the Eu-
ler’s integral representation of the Gamma function, namely
(4.4) n! =
∫ ∞
0
e−ttn+1dt
t .
In the deﬁnition of a q-summation procedure one must be guided by the
q-analogs of this last integral, question investigated since Jackson, Wigeret,
Watson, etc...
We recall the following q-analogs of the integral representation of the
Euler Gamma function.
Proposition 4.8. — Ford ∈ (−π,π ) and λ /∈ (−qZ) we have:
(4.5) [n]!
q = q − 1
lnq
∫ ∞eid
0
tn
eq(qt)dt = q − 1
lnq
∫ ∞eid
0
tnep(−qt)dt,
(4.6) [n]!
q =q
∫
λpZ
tn
eq(qt)dpt =q
∫
λpZ
tnep(−qt)dpt,
(4.7) qn(n−1)/2 = q
lnq
∫ ∞eid
0
tn
θp(qt)dt,
(4.8) qn(n−1)/2 = q
1 −p
∫
λpZ
tn
θp(qt)dpt.
Proof. — For the proof of the identities above cf. [1, pages 549-550]. More
precisely, letting c → n + 1, b → 1 and a → 0 (resp. letting c → n + 1,
b,a → 0) in
∫ ∞
0
xc−1 (−ax;p)∞(−pb/x;p)∞
(−x;p)∞(−p/x;p)∞
dx = (ab;p)∞(pc;p)∞(p1−c;p)∞π
(bpc;p)∞(ap−c;p)∞(p;p)∞ sin(πc),
TOME 59 (2009), F ASCICULE 1
384 Lucia DI VIZIO & Changgui ZHANG
one gets the formula
∫ ∞
0
xn
(−x;p)∞
dx = (lnq)(p;p)np−n(n+1)/2
(
resp.
∫ ∞
0
xn
(−x;p)∞(−p/x;p)∞
dx = (lnq) p−n(n+1)/2
)
,
which yields ( 4.5) (resp. ( 4.7)). Similarly, the formulae ( 4.6) and ( 4.8) can
be viewed as special cases of
∫ ∞
0
xc−1 (−ax;p)∞(−bp/x;p)∞
(−x;p)∞(−p/x;p)∞
dpx =
(1 −p)(p;p)∞(−pc;p)∞(−p1−c;p)∞(ab;p)∞
(−1;p)∞(−p;p)∞(ap−c;p)∞(bpc;p)∞
.
□
Remark 4.9. — In particular, ( 4.8) and ( 4.7) have been studied in [ 15]
and [ 23] as starting points for the corresponding summation procedures.
Other kinds of q-summation are considered in [ 20] and [ 12].
Let d ∈ [−π,π ). We will identify d to the half line [0, ∞eid) := R+eid.
Definition 4.10. — We set Hd
q = ∩λ∈(0,∞eid)H[λ;q].
Remark 4.11. — The functional space Hd
q is exactly the space Hd
q;1 in-
troduced in [ 20].
Let λ ∈ C∗ and d ∈ [−π,π ). According to Proposition 4.8, the following
four q-Laplace transforms are well deﬁned:
∀φ ∈ H[λ;q], L [λ]
q φ = q
1 −p
∫
λpZ
φ(ξ)
θp(q ξ
x )
dpξ;
∀φ ∈ H[λ/(1−p);q], L[λ]
q φ = q
1 −p
∫
λpZ
φ(ξ/(1 −p))
eq(q ξ
(1−p)x )
dpξ;
∀φ ∈ Hd
q, L d
qφ = q
lnq
∫ eid∞
0
φ(ξ)
θp(q ξ
x )
dξ, Ld
qφ = q − 1
lnq
∫ eid∞
0
φ(ξ)
eq(q ξ
x )
dξ.
Definition 4.12. — (1) If ˆf ∈ C{x}[λ;q]
q , we deﬁne its sums in the
direction [λ;q] as follows:
S [λ]
q ˆf = L[λ]
q (Bq ˆf ), S [λ]
q ˆf =L[λ]
q (Bq ˆf ).
(2) If ˆf ∈ C{x}d
q, deﬁne its sums in the direction d as follows:
S d
q ˆf = Ld
q(Bq ˆf ), S d
q ˆf =Ld
q(Bq ˆf ).
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 385
Remark 4.13. —
• The summation procedures ˆf →S[λ;q] ˆf and ˆf →Sd ˆf are introduced in
[23] and [ 21]: they have many good asymptotic properties.
• Suppose that ˆf isq-summable and that d is not a singular direction. Then
we have the following formal equality (meaning that we exchange carelessly
the inﬁnite sum and the integral):
(4.9) S d
q ˆf = 1
lnq
∫ qeid
eid
S [λ]
q ˆfdλ
λ
and
(4.10) Sd
q ˆf = 1
lnq
∫ qeid
eid
S[λ]
q ˆfdλ
λ .
To prove that this identity is not only formal, but analytic, one would like
to apply the dominated convergence theorem: unfortunately the dominated
convergence is a little bit delicate for a general ˆf , since we don’t really
control the spirals of poles of the discrete q-Borel sums. Anyway, we will
prove (4.9) and ( 4.10) for a generic q-Gevrey series ( cf. Theorem 4.14).
At this stage a natural question arises:
Do we have S[λ;q] ˆf = S [λ;q] ˆf and Sd ˆf = S d ˆf ?
The answer is clear, and trivially positive, if ˆf (x) is a germ of analytic
function at zero: in this case all the sums of ˆf (x) coincide with f .
The rest of the paper is devoted to the proof of the following theorem:
Theorem 4.14. — Let ˆf be a generic q-Gevrey series and let λ ∈ C∗,
d ∈ [−π,π ). Assume that λ /∈ D S( ˆf ) and (0,e id∞) ∩ D S( ˆf ) = ∅. Then
(1) S[λ]
q ˆf = S [λ]
q ˆf , on a convenient domain Ω.
(2) Sd
q ˆf = S d
q ˆf on a convenient sector containing the direction d.
Moreover we have:
S d
q ˆf = 1
lnq
∫ qeid
eid
S [λ]
q ˆfdλ
λ .
Remark 4.15. — Theorems 3.3 and 3.10 are a special case of Theo-
rem 4.14.
Before giving a proof of Theorem 4.14 in § 4.5, we make a digression
about two essential ingredients of the proof: ﬁrst we prove the theorem in
the special case of the Tschakaloﬀ series; then we introduce a functional
space that allows to read, in certain sense, any q-Gevrey series as a ﬁnite
linear combination of some modiﬁed Tschakaloﬀ series.
TOME 59 (2009), F ASCICULE 1
386 Lucia DI VIZIO & Changgui ZHANG
4.3. The T schakaloﬀ series
Let us consider another q-analogue of the Euler series:
Tq(x) =
∑
n/greaterorequalslant0
qn(n−1)/2xn+1,
called the Tschakaloﬀ series or the partial Theta function. It satisﬁes the
q-diﬀerence equation
xTq(qx) −qTq(x) = −qx,
that can also be rewritten in the form x2(q − 1)dqy + (x −q)y = −qx.
The Borel transforms of Tq are:
ψ(ξ) = Bq(Tq) =
∑
n/greaterorequalslant0
ξn
[n]!p
=ep(ξ) = ((1 −p)ξ;p)−1
and
φ(ξ) = Bq(Tq) = 1
1 −ξ.
Proposition 4.16. — Let us ﬁx λ /∈ [−1;q]. Then S [λ]
q Tq =S[λ]
q Tq.
Proof. — The deﬁnition of the Jackson integral ( cf. §A) and the Ja-
cobi triple product formula ( cf. (2.14)), plus the development of the q-
exponential eq(x) as an inﬁnite product ( cf. (2.15)), imply that:
L[λ]
q ψ = q
1 −p
∫
λpZ
ep(ξ)
eq
(
qξ
(1−p)x
)dpξ = q
1 −p
∫
λpZ
(
ξ, −qξ
x ;p
)−1
∞
dpξ
=λ(p;p)∞
∑
n∈Z
pn(−p1−nx/λ;p)∞
(pn+1λ;p)∞θp(pnλ/x).
Since θp(x) = pn(n−1)/2xnθp(pnx) for any n ∈ Z, we obtain:
S [λ]
q Tq = L[λ]
q ψ = λ(p;p)∞
θp(λ/x)
∑
n∈Z
(
−p1−n x
λ ;p
)
∞
(pn+1λ;p)∞
pn(n+1)/2
(λ
x
)n
.
On the other hand we have:
S[λ]
q Tq =L[λ]
q φ = q
1 −p
∫
pZλ
dpξ
(1 −ξ)θp(qξ/x)
=λ
∑
n∈Z
pn
(1 −pn+1λ)θp(pnλ/x)
= λ
θp(λ/x)
∑
n∈Z
pn(n+1)/2
1 −pn+1λ
(λ
x
)n
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 387
A straightforward calculation of the residues of (x,p )−1
∞ at x = p−k, for
k /greaterorequalslant0, gives the formula:
1
(x;p)∞
= 1
(p;p)∞
∑
k/greaterorequalslant0
ak
1 −xpk, with ak = 1
(p−k;p)k
= (−1)kpk(k+1)/2
(p;p)k
.
Therefore we obtain:
S [λ]
q Tq = λ
θ( λ
x )
∑
𝓁∈Z
p𝓁(𝓁+1)/2
1 −p𝓁λ
(λ
x
)𝓁
(a𝓁;p)∞ 0φ1(−;a𝓁;p,a 𝓁), a 𝓁 = −p1−𝓁x
λ.
The Ramanujan formula ( cf. [24, Thm. 4.4]):
(x;p)∞ 0φ1(−;x;p,x ) = 1, for any x /∈q−N,
implies that L[λ]
q ψ =L[λ]
q φ. □
