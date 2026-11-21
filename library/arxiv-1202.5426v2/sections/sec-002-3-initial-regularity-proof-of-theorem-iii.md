---
doc_id: arxiv-1202.5426v2
doc_title: "Hard analysis meets critical knots"
section_id: sec-002-3-initial-regularity-proof-of-theorem-iii
section_title: "Initial regularity: Proof of Theorem III"
section_number: 3
pages: 16-32
source_pdf: 1202.5426v2.pdf
source_sha256: 6c7668ad72e33b4b
toc_source: outline
doc_brief: "Hard analysis meets critical knots — 5 sections: Front matter; Introduction; Euler-Lagrange equation: Proof of"
---
Note that if we consider the constant factors to be irrelevant with respect to the mathematical
argument, for the sake of simplicity we will omit them in the calculations, writing ≲, ≳, ≈
instead of ≤, ≥and =.
Most techniques for dealing with critical partial diﬀerential equations of fractional order have
been developed for equations on the whole Euclidean space. For that reason, we prefer work-
ing on the real line over working on the circle.
16
We will show that for every u ∈R/Z we have
|D|
1
2 g′ ∈Lp((u −1/20, u + 1/20))
for a p > 2. Due to the invariance of the problem under shifting the parametrization, it is
enough to show this for u = 1/2, i.e.
|D|
1
2 g′ ∈Lp((9/20, 11/20)).
(3.1)
Let |D|s ≡(−∂2
x)s/2 ≡(−∆)
s
2 be the fractional Laplacian on R. The inverse, Is ≡(−∆)−s
2 ,
s ∈(0, 1), is the Riesz potential by
Is f(x) = cs
Z
R
f(y)
|x −y|1−s dy.
(3.2)
In case of positive powers s of the Laplacian |D|s, s ∈(0, 1), we use the corresponding formula
|D|s f(x) = ˜cs
Z
R
f(y) −f(x)
|x −y|1+s
dy.
(3.3)
For a detailed introduction to the fractional Laplacian we refer to, e.g., [DNPV11], [Sch10,
Section 2.5].
To switch from the circle to the real line, we interpret functions on R/Z as functions on R
which are periodic with period 1. We then choose a cutoﬀfunction η ∈C∞
0 (R), η ≡1 on
[−3, 4] and consider
g = η · γ
(3.4)
instead of γ. We will show that |D|
1
2 g′ ∈Lp((17/40, 23/40), Rn), for some p > 2 to conclude
the proof.
Before we begin to outline the structure of the proof, let us shortly recapitulate the notion of
Lorentz spaces and the main properties we are going to use in this article. For a measurable
function f : Ω→R and Ω⊂R one considers the decreasing rearrangement
f ∗(t) := inf
n
s > 0 : L1({|f| > s}) ≤t
o
where L1 denotes the Lebesgue measure. We deﬁne
|f|(p,q),Ω:=

R ∞
0 (t1/p f ∗(t))q dt
t
1/q
if p, q ∈[1, ∞),
supt>0 t1/p f ∗(t)
if q = ∞.
To prevent technical problems, unless p ∈(1, ∞) we will only take the spaces L1,1 = L1 and
L∞,∞= L∞into consideration.
17
Furthermore, |f|(p,p) ≈∥f∥Lp for all p ∈[1, ∞]. If Ω= R we will omit Ωin the notation.
Though | · |(p,q),Ωis not a norm, as it does not obey the triangle inequality, there is a norm
∥· ∥(p,q),Ωon the Lorentz spaces which is equivalent to | · |(p,q),Ω. These norms satisfy a H¨older
inequality, i.e., for p1, p2, p ∈[1, ∞) and q1, q2, q ∈[1, ∞] with 1/p1 + 1/p2 = 1/p and
1/q1 + 1/q2 = 1/q we have
∥fg∥(p,q),Ω≲∥f∥(p1,q1),Ω∥g∥(p2,q2),Ω.
(3.5)
For p1, p2, p ∈(1, ∞) and q1, q2 ∈[1, ∞] with 1/p1 + 1/p2 = 1/p + 1 and 1/q1 + 1/q2 = 1/q
we have the Young-O’Neil inequality [Hun66]
∥f ∗g∥(p,q),Ω≲∥f∥(p1,q1),Ω∥g∥(p2,q2),Ω.
(3.6)
Furthermore, we have the Sobolev inequality
∥Is f∥(p∗,q) ≲∥f∥(p,q)
for all s ≥0, p ∈[1, ∞), q ∈[1, ∞] and p∗:=
p
1−sp ∈[1, ∞). Further information and proofs
can be found in [Hun66, Gra08, Tar07].
The main reason for using Lorentz spaces in the context of critical equations, i.e. equations to
which standard Gagliardo-Nirenberg-Sobolev embeddings cannot be applied to gain regular-
ity, is the following fact. Although for functions f the L2-norm of |D|
1
2 f does not control the
L∞-norm of f, the L2,1 norm does, i.e. we have the estimate
∥f∥∞≲∥|D|
1
2 f∥(2,1).
We will also need this in the more general form
∥f∥∞≲∥|D|s f∥( 1
s ,1)
for all s ∈(0, 1).
In order to prove our regularity result, we will prove a Dirichlet growth theorem for the weak
H1/2-energy of γ′ on balls in a manner comparable to [DLR11a, Sch12] – which are as well
in the setting of sphere-valued mappings. In contrast to these papers, the techniques from
[DLR11b, DL11, Sch11] deal with a more general setting, but have to work (as we will here)
with estimates of the L2,∞-norm instead of the L2-norm. Note nevertheless that our right-hand
side is very diﬀerent from their’s. In order to obtain the estimates of the norms ∥|D|
1
2 g′∥(2,∞)
on small balls, we will have to use new arguments.
To prove the regularity theorem, we begin with an approach appearing in [DLR11a, Sch12]
and divide |D|
1
2 g′ into the part parallel to g′ (and thus normal to the sphere Sn−1) and the term
perpendicular to g′ (tangential to the sphere). More precisely, we use that for p ∈[1, ∞),
q ∈[1, ∞]
∥|D|
1
2 g′∥(p,q),Br ≲∥⟨g′, |D|
1
2 g′⟩∥(p,q),Br + sup
ωi j
∥g′
jωi j|D|
1
2 g′
i∥(p,q),Br,
(3.7)
where the supremum is over ωi j = −ωji ∈{−1, 0, 1}. For a detailed version of this linear
algebraic fact, the interested reader is referred to the appendix of [DLS12].
18
3.1. Estimate of the normal part
We have
⟨g′, |D|
1
2 g′⟩= −1
2H 1
2 (g′, g′) + 1
2|D|
1
2 

g′

2,
(3.8)
where
Hs(a, b) := |D|s(ab) −a |D|sb −b |D|sa.
(3.9)
Note that for any s ∈(0, 1), we have
|D|s|g′|2 (3.4)
= |D|sη2 + 2|D|s(η′γ′g) + |D|s(|η′|2|γ|2) ∈L∞((0, 1)).
(3.10)
In fact, |D|sη2 ∈L∞by interpolation inequalities. For the remaining terms we use the quasi-
locality, Lemma A.1, and the support of η and η′.
As in [Sch11] we will use pointwise estimates for Hs and some quantitative version of the
quasi-locality to estimate the normal part of |D|
1
2 g′:
Lemma 3.1 (Normal part). For any s ∈[0, 1
2) there exists θ > 0 such that for any Br ⊂[0, 1],
Λ > 4
∥|D|s⟨g′, |D|
1
2 g′⟩∥(
2
1+2s ,∞),Br ≲∥|D|
1
2 g′∥
2
(2,∞),BΛr+ Λ−θ ∥|D|
1
2 g′∥(2,∞),R
∞
X
k=1
2−θk ∥|D|
1
2 g′∥(2,∞),B2kΛr+r
1
2 +s.
(3.11)
For the readers’ convenience, a proof will be given in the appendix.
3.2. Estimate of the tangential part
It then remains to estimate the part normal to g′ (tangential to the sphere), i.e. for ωi j =
−ωji ∈{−1, 0, 1}, 1 ≤i, j ≤n we need to estimate suitable norms on small balls of the term
g′
jωi j|D|
1
2 g′
i.
We have
Z
R
g′
jωi j|D|
1
2 g′
i |D|
1
2 ϕ =
Z
R
|D|
1
2 g′
i |D|
1
2 
ωi jg′
jϕ

−
Z
R
|D|
1
2 g′
i ωi j|D|
1
2 g′
j ϕ −
Z
R
|D|
1
2 g′
i ωi jH1/2(g′
j, ϕ)
=
Z
R
|D|
1
2 g′
i |D|
1
2 
ωi jg′
jϕ

−
Z
R
|D|
1
2 g′
i ωi jH1/2(g′
j, ϕ)
(3.12)
where we have used that due to ωi j = −ωji the second term on the right-hand side of the ﬁrst
line vanishes.
The second term can be estimated analogously to similar terms in [DLR11b, DL11, Sch11]
using again quasi-locality together with Sobolev embeddings.
19
Lemma 3.2 (Tangential part). There is θ > 0, s0 ∈(0, 1
2) such that for all φ ∈C∞
0 (Br),
Λ > 16, s ∈[0, s0) we have
Z
|D|
1
2 g′
iωi jH1/2(g′
j, φ)dx
≲∥|D|−s+1/2φ∥(
2
1−2s ,1)
∥|D|
1
2 g′∥2
(2,∞),BΛr + Λ−θ∥|D|
1
2 g′∥(2,∞),R
∞
X
k=1
2−θ(k−1)∥|D|
1
2 g′∥(2,∞),B2kΛr
.
A proof is provided in the appendix.
It remains to estimate the ﬁrst term on the right-hand side of Equation (3.12) for which we
will use the Euler-Langrange equation (1.6).
Combining this equation with the formula
Z
R
|D|
1
2 f ′
1 |D|
1
2 f ′
2
= c lim
εց0
Z
R
Z
R\(−ε,ε)
 
 f ′
1(u), f ′
2(u)
 −⟨f1(u + w) −f1(u), f2(u + w) −f2(u)⟩
w2
! dw
w2 du
(3.13)
due to He [He99, Proposition 2] we get the following estimate which contains all the informa-
tion of the Euler-Langrange equation we need to proceed in the proof:
Lemma 3.3 (Essential estimate of the Euler-Lagrange equation). There is a constant C <
∞such that
Z
R
D
|D|
1
2 g′, |D|
1
2 φ
E
≤C
Z
R
|φ(u)|Γ(u)du + C∥φ∥L2
(3.14)
for any φ ∈C∞
0 ((4/10, 6/10), Rn) with ⟨φ, γ′⟩≡0 where
Γ(u) :=
Z
(−1,1)3
1/4
Z
−1/4
|g′(u) −g′(u + s2w)| |g′(u + s3w) −g′(u + s4w)|2
|w|2
dw ds.
The heart of the proof of Theorem III is the following pointwise estimate of the most prob-
lematic term Γ(u), which permits to localize it and which afterwards will be transformed into
a bound of its L1-norm.
Lemma 3.4 (Estimate of the critical term). We have
Γ(u) ≲

|D|−1
12 ||D|
1
2 g′|(u)

2
|D|−1
3 ||D|
1
2 g′|(u) + |D|−1
12 ||D|
1
2 g′|(u) |D|−1
4

|D|−1
12 ||D|
1
2 g′|(u)

2
(3.15)
almost everywhere.
20
In fact, Lemmata 3.3 and 3.4 provide the essential new estimates in this article on which
our entire reasoning relies crucially. Using these and the above-mentioned improved Sobolev
embeddings for Lorentz spaces, we are ready to show the following estimate. This will allow
us to prove a Dirichlet growth of the L2,∞-norm of |D|
1
2 g′.
Lemma 3.5. There exist R > 0, s0 ∈(0, 1
2), and σ > 0 such that for any Λ > 2, s ∈[0, s0),
BΛr ⊂( 5
10, 6
10), r ∈(0, Λ−1R) and ϕ ∈C∞
0 (Br) we have
Z
g′
iωi j|D|
1
2 g′
j |D|
1
2 ϕ
≲∥Is|D|
1
2 ϕ∥(
2
1−2s ,1)
rσ + ∥|D|
1
2 g′∥
2
(2,∞),BΛr + Λ−θ∥|D|
1
2 g′∥(2,∞),R
∞
X
k=1
2−θk ∥|D|
1
2 g′∥(2,∞),B2kΛr
.
3.3. Conclusion of the proof of Theorem III
Combining Lemma 3.5 with Proposition A.3, we get
∥|D|s
g′
iωi j|D|
1
2 g′
j

∥(
2
2s+1 ,∞),Br
≲


Λ2r
σ + ∥|D|
1
2 g′∥
2
(2,∞),BΛ3r + ∥|D|
1
2 g′∥(2,∞),RΛ−θ
∞
X
k=1
2−θk ∥|D|
1
2 g′∥(2,∞),BΛ32kr

+ Λ−θr−s
∞
X
k=1
2−θk ∥|D|
1
2 g′∥(
2
1+2s ,∞),BΛ2kr
≲
· · ·
+ Λs−θ
∞
X
k=1
2(s−θ)k ∥|D|
1
2 g′∥(2,∞),BΛ2kr
(3.16)
for some θ > 0 uniformly in Λ.
Let us ﬁrst use this for s = 0, to get in view of (3.7) and Lemma 3.1 that for all ε > 0 we have
for suﬃciently small r > 0, Br ⊂
 4
10, 6
10

and big enough Λ
∥|D|
1
2 g′∥(2,∞),Br ≤C


Λ2r
σ + ε ∥|D|
1
2 g′∥(2,∞),BΛ3r + (1 + ∥|D|
1
2 g′∥(2,∞),R)Λ−θ
∞
X
k=2
2−θk ∥|D|
1
2 g′∥(2,∞),B2kΛ3r

uniformly in Λ and ε.
Let us ﬁx such an r0, and consider the above equation for Λ = 2m/3, r = 2−m−kr0 (w.l.o.g.
r0 = 1). Setting b0 := ∥|D|
1
2 g′∥(2,∞) and bk := ∥|D|
1
2 g′∥(2,∞),B2−k the above estimate gives
bk+m ≤C2−σ(k+m/3) + εbk + C2−θm/3

k
X
l=1
2−θlbk−l + C2−θk

21
for every k ∈N0 where C < ∞does not depend on k.
Using the iteration argument, Lemma A.8, leads to
∥|D|
1
2 g′∥(2,∞),Br ≤Cγ r ˜σ
(3.17)
for all Br ⊂
 9
20, 11
20

and r small enough.
This immediately implies H¨older regularity of the solution g′. Instead, let us iterate the above
argument to get |D|
1
2 g′ ∈Lp
loc((9/20, 11/20)), for some p > 2.
Let us assume without loss of generality that ˜σ < θ
2. Then, plugging (3.17) into (3.16) one
obtains
∥|D|s
g′
iωi j|D|
1
2 g′
j

∥(
2
2s+1 ,∞),Br ≲CΛ,γ,s,R rmin{σ, ˜σ, ˜σ−s,θ/2}
for small enough 0 < s < (0, ˜σ), r > 0, and Br ⊂[9/20, 11/20]. Here we have used that
2kΛ3r ≥R0 for some R0 > 0 leads to 2−θk ≤2−θk/2  Λ3
R0
θ/2 rθ/2. So the series in (3.16)
converge and are bounded by some small positive power of r.
On the other hand, (3.17) and (3.11) together imply for any small enough r > 0, Λ := r−1
2 , and
Br ⊂
 9
20, 11
20

∥|D|
1
4 ⟨g′, |D|
1
2 g′⟩∥( 4
3 ,∞),Br
(3.11)
≲
∥|D|
1
2 g′∥
2
(2,∞),B
r
1
2 + r
θ
2 ∥|D|
1
2 g′∥
2
(2,∞),R + r
3
4
(3.17)
≤
Cγ

r ˜σ + r
θ
2 + r
3
4 
.
That is, |D|s
g′
iωi j|D|
1
2 g′
j

, and |D|
1
4 ⟨g′, |D|
1
2 g′⟩both belong locally to a Morrey space L(p,q),λ
loc
on
 9
20, 11
20

. More precisely, for some λ ∈(0, 1) we have
|D|s
g′
iωi j|D|
1
2 g′
j

∈
L
(
2
2s+1 ,∞),λ
loc
 9
20, 11
20
!
,
|D|
1
4 ⟨g′, |D|
1
2 g′⟩
∈
L
( 4
3 ,∞),λ
loc
 9
20, 11
20
!
.
The boundedness of Riesz potentials on Morrey spaces, as shown in [Ada75], implies that for
some p > 2
g′
iωi j|D|
1
2 g′
j, ⟨g′, |D|
1
2 g′⟩∈Lp
loc
 9
20, 11
20
!
.
Together, using (3.7), we have shown
|D|
1
2 g′
j ∈Lp
loc
 9
20, 11
20
!
,
which ﬁnishes the proof of Theorem III.
□
22
3.4. Proof of Lemma 3.3
The main idea is to use φ as the derivative of a test function for the Euler-Lagrange equation.
Of course this is not possible generally, but with some precaution we can actually do it up to
a benign error term: For φ ∈C∞
0 ((4/10, 6/10)) we set
h(u) :=
u
Z
0
φ(v)dv −au
where a =
R 1
0 φ(v)dv is chosen such that h(0) = h(1). Hence, if we set
hπ(k + t) := h(t),
∀t ∈[0, 1), k ∈Z,
φπ(k + t) := φ(t),
∀t ∈[0, 1), k ∈Z,
hπ is a smooth one periodic function satisfying
h′
π(u) = φπ −a.
and, as we assume in Lemma 3.3 that ⟨φ, γ′⟩≡0, also

φπ, γ′
 ≡0.
Since γ is a stationary point of the M¨obius energy, testing the equation (1.6) with hπ, (recall
(1.4), (1.5),(1.3))
Q(γ, hπ) := lim
ε→0 Qε(γ, hπ) = T1(γ, hπ) + T2(γ, hπ).
(3.18)
As φπ is perpendicular to γ′ we can estimate the term T1(γ, hπ) by
T1(γ, hπ) =
1
Z
−1
1/2
Z
−1/2

γ′(u), φπ(u) −a
 
1
|γ(u + w) −γ(u)|2 −1
w2
!
≤|a| E(2)(γ) ≤C∥φ∥L1 ≤C∥φ∥L2.
(3.19)
As for the remaining terms Q(γ, hπ) and T2(γ, hπ), we will identify them essentially with
the left-hand side of (3.14) and the Γ-term on the right-hand side of (3.14), respectively. A
technical detail one has to take into account here, is that the domain of (3.18) is the torus R/Z,
whereas the respective domain in (3.14) is the real line R. To estimate the other terms, let us
introduce for f1, f2 ∈H3/2
loc (R, Rn) the operators
˜Qε(f1, f2) :=
1
Z
0
Z
˜Iε
 
f ′
1(u), f ′
2(u)
 −⟨f1(u + w) −f(u), f2(u + w) −f2(u)⟩
w2
! dw
w2 du
23
=
1
Z
0
Z
˜Iε
1
Z
0
1
Z
0
D
f ′
1(u), f ′
2(u)
E
−
D
f ′
1(u + s1w), f ′
2(u + s2w)
E
w2
ds1ds2dw du,
where ˜Iε := [−1/4, 1/4] \ [−ε, ε],
˜Q := lim
εց0
˜Qε,
and
˜T2(f1, f2)
:=
1
Z
0
1/4
Z
−1/4
⟨f1(u + w) −f1(u), f2(u + w) −f2(u)⟩
 
1
|γ(u + w) −γ(u)|4 −
1
|w|4
!
dw du
=
1
Z
0
1/4
Z
−1/4
1
Z
0
1
Z
0

 f ′
1(u + s1w), f ′
2(u + s2w)
 w2
 
1
|γ(u + w) −γ(u)|4 −
1
|w|4
!
ds1 ds2 dw du.
(3.20)
Recall that [−1
2, 1
2]\(−ε, ε) is used for the deﬁnition of Q and ˜Iε := [−1/4, 1/4] \ [−ε, ε] is
used for ˜Q, so the diﬀerence only contains the set where |w| > 1
4, thus |w|−2 is not singular.
Quantitatively, this reads as
| ˜Q(γ, h) −Q(γ, h)| + | ˜T2(γ, h) −T2(γ, h)| ≤C∥γ′∥L2∥h′∥L2 ≤C∥γ′∥L2∥φ∥L2,
(3.21)
where we have used that γ is bi-Lipschitz in order to deal with T2.
We now compute
˜Qε(γ, hπ) =
1
Z
0
Z
˜Iε
1
Z
0
1
Z
0
 
γ′(u), h′
π(u)
 −
γ′(u + s1w), h′
π(u + s2w)
 ds1 ds2
dw
w2 du
=
1
Z
0
Z
˜Iε
1
Z
0
1
Z
0
 
γ′(u), φπ

 −
γ′(u + s1w), φπ(u + s2w)
 ds1 ds2
dw
w2 du
−
1
Z
0
Z
˜Iε
1
Z
0
1
Z
0
 
γ′(u), a
 −
γ′(u + s1w), a
 ds1 ds2
dw
w2 du
(3.22)
=
1
Z
0
Z
˜Iε
1
Z
0
1
Z
0
 
g′(u), φ(u)
 −
g′(u + s1w), φ(u + s2w)
 ds1 ds2
dw
w2 du.
(3.23)
24
Here we have used that
R 1
0 γ′(u + ˜w)du = 0 for all ˜w, i.e., the term (3.22) is constantly zero for
any w. The term (3.23) essentially is the L2-pairing of |D|
1
2 g′ and |D|
1
2 φ: More precisely we
will show
| ˜Q(γ, hπ) −
Z
R
|D|
1
2 g′|D|
1
2 φ| ≤Cγ∥φ∥L2.
(3.24)
Proof of (3.24). Using (3.13), we have for any f1, f2 ∈C∞
0 (R) as ε →0
Z
R
|D|
1
2 f ′
1|D|
1
2 f ′
2du + o(1)
= c
Z
R
Z
R\[−ε,ε]
1
Z
0
1
Z
0
 
f ′
1(u), f ′
2(u)
 −
 f ′
1(u + s1w), f ′
2(u + s2w)
 ds1 ds2
dw
|w|2 du.
(3.25)
We now connect and (3.25) and (3.23). The technical problem is, that the integral of φ is not
a feasible test-function for (3.25). Let therefore for η[−10,10] ∈C∞
0 ((−11, 11)) and η[−10,10] ≡1
in [−10, 10],
ψ :=
u 7→η[−10,10]
u
Z
0
φ
∈C∞
0 (R).
Thus, ψ is a feasible test-function for (3.25), which φ is not. Moreover,
ψ′ = η[−10,10]φ + η′
[−10,10]
u
Z
0
φ
supp φ
≡
φ + η′
[−10,10]
u
Z
0
φ.
(3.26)
We thus arrive at
˜Qε(γ, h)
(3.23)
=
1
Z
0
Z
˜Iε
1
Z
0
1
Z
0
 
g′(u), φ(u)
 −
g′(u + s1w), φ(u + s2w)
 ds1 ds2
dw
w2 du
supp φ, |w|,(3.26)
=
Z
R
Z
˜Iε
1
Z
0
1
Z
0
 
g′(u), ψ′(u)
 −
g′(u + s1w), ψ′(u + s2w)
 ds1 ds2
dw
w2 du
=
Z
R
Z
R\[−ε,ε]
1
Z
0
1
Z
0
 
g′(u), ψ′(u)
 −
g′(u + s1w), ψ′(u + s2w)
 ds1 ds2
dw
w2 du
−
Z
R
Z
|w|> 1
4
1
Z
0
1
Z
0
 
g′(u), ψ′(u)
 −
g′(u + s1w), ψ′(u + s2w)
 ds1 ds2
dw
w2 du
25
(3.25)
=
Z
⟨|D|
1
2 g′, |D|
1
2 ψ′⟩
−
Z
R
Z
|w|> 1
4
1
Z
0
1
Z
0
 
g′(u), ψ′(u)
 −
g′(u + s1w), ψ′(u + s2w)
 ds1 ds2
dw
w2 du
+ o(1)
(3.26)
=
Z
⟨|D|
1
2 g′, |D|
1
2 φ⟩+
Z
⟨|D|
1
2 g′, |D|
1
2 (η′
[−10,10]
·
Z
0
φ)⟩
−
Z
R
Z
|w|> 1
4
1
Z
0
1
Z
0
 
g′(u), ψ′(u)
 −
g′(u + s1w), ψ′(u + s2w)
 ds1 ds2
dw
w2 du
+ o(1).
Now, by usual interpolation and/or imbedding of Sobolev spaces, see, e.g. [Tar07, Sch10],
∥|D|
1
2 f∥2,R ≲∥f∥2,R + ∥f ′∥2,R,
we have
∥|D|
1
2 (η′
[−10,10]
·
Z
0
φ)∥2,R ≲∥φ∥1 + ∥φ∥2
supp φ
≲
∥φ∥2.
Moreover,
Z
R
Z
|w|> 1
4
1
Z
0
1
Z
0
 
g′(u), ψ′(u)
 −
g′(u + s1w), ψ′(u + s2w)
 ds1 ds2
dw
w2 du
≲
Z
|w|> 1
4
|w|−2 ∥g′∥2∥ψ′∥2
(3.26)
≲
∥g′∥2,R

∥φ∥1,R + ∥φ∥2,R
 supp g
≲
Cγ ∥φ∥2,R.
Thus, we have shown that (3.24) holds.
□
To estimate ˜T2(γ, h) we calculate
˜T2(γ, h) =
1
Z
0
1/4
Z
−1/4
1
Z
0
1
Z
0

γ′(u + s1w), φπ(u + s2w) + a
 w2·
26
·
 
1
|γ(u + w) −γ(u)|4 −
1
|w|4
!
ds1 ds2 dw du
=
1
Z
0
1/4
Z
−1/4
1
Z
0
1
Z
0

γ′(u + s1w), φ(u + s2w) −φ(u + s1w) + a
 w2·
 
1
|γ(u + w) −γ(u)|4 −
1
|w|4
!
ds1 ds2 dw du
and using
w2
 
1
|γ(u + w) −γ(u)|4 −1
|w|4
!
=
w4
|γ(u + w) −γ(u)|4

1 −|γ(u+w)−γ(u)|4
w4
w2

≤C
1 −|γ(u+w)−γ(u)|2
w2
w2
= C
2
1
Z
0
1
Z
0
|γ′(u + s3w) −γ′(u + s4w)|2
w2
ds3 ds4
we get
| ˜T2(γ, h)| ≤|a|E(2)(γ)
+
1
Z
0
1/4
Z
−1/4
Z
(0,1)4
|γ′(u + s1w) −γ′(u + s2w)| |γ′(u + s3w) −γ′(u + s4w)|2 |φ(u + s2w)|
w2
dsdw du
≤C∥φ∥L2 +
1
Z
0
1/4
Z
−1/4
Z
(−1,1)3
|γ′(u + s1w) −γ′(u)| |γ′(u + s3w) −γ′(u + s4w)|2 |φ(u)|
w2
dsdw du.
(3.27)
From (3.21),(3.19),(3.24), and (3.27) one gets the claim, since γ′ = g′ on [−1/4, 5/4].
3.5. Proof of Lemma 3.4
Let
F(u) := ||D|
1
2 g′(u)|.
Since g′, |D|
1
2 g′ ∈L2, we obtain
g′(x) −g′(y) = I 1
2 (|D|
1
2 g′)(x) −I 1
2 (|D|
1
2 g′(y))
27
= c 1
2
 Z
|x −ξ|−1+ 1
2 |D|
1
2 g′(ξ) dξ −
Z
|y −ξ|−1+ 1
2 |D|
1
2 g′(ξ) dξ
!
,
then
|g′(x) −g′(y)| ≲
Z
R
||ξ −x|−1+ 1
2 −|ξ −y|−1+ 1
2 | F(ξ) dξ,
and hence
Γ(u) ≲
Z
(−1,1)3
Z
R3
1/4
Z
−1/4
F(ξ1) F(ξ2) F(ξ3) k(ξ, u, s, w) dw dξ ds,
where for almost every s = (s1, s2, s3) ∈(−1, 1)3, ξ = (ξ1, ξ2, ξ3) ∈R3, w ∈R, u ∈R,
k(ξ, u, s, w) = m(ξ1 −u, 0, s1, w) m(ξ2 −u, s2, s3, w) m(ξ3 −u, s2, s3, w)
|w|2
(3.28)
and
m(a, s, t, w) := ||a + sw|−1
2 −|a + tw|−1
2 |.
The characteristic behavior of k is as follows: The factors m(·, ·, ·, w) will behave like |w|δ in a
neighborhood of w = 0 such that they somewhat absorb the singular behaviour of |w|−2, that is,
k becomes integrable around w = 0. This is an eﬀect very similar to the behaviour of Hs(·, ·),
see Lemma A.5, as developed in [Sch11].
More precisely, we will derive the estimate
Z
[−1,1]3
k(ξ, u, s, w) ds
≲|w|3δ−2|ξ1 −u|−1/2−δ
X
(σ(2),s(3))∈{(2,3),(3,2)}
|ξσ(2) −u|−1/2−δ
1
Z
−1
|ξσ(3) −u + tw|−1/2−δ dt
(3.29a)
+ |w|3δ−2|ξ1 −u|−1/2−δ
1
Z
−1
|ξ2 −u + tw|−1/2−δ|ξ3 −u + tw|−1/2−δ dt.
(3.29b)
We start with some abstract treatment of m.
In case 1,
max (|a + sw|, |a + tw|) ≥2|s −t||w|,
(3.30)
we obtain
|a + sw| ≈|a + tw|.
(3.31)
Applying the mean value theorem, for any δ ∈(0, 1) we arrive at
m(a, s, t, w) ≲max

|a + sw|−3/2, |a + tw|−3/2
|s −t||w|
28
≲max

|a + sw|−1/2−δ, |a + tw|−1/2−δ
max

|a + sw|−1+δ, |a + tw|−1+δ
|s −t||w|
(3.30)
≲max

|a + sw|−1/2−δ, |a + tw|−1/2−δ
|s −t|δ
| {z }
≤2δ
|w|δ
(3.31)
≲min

|a + sw|−1/2−δ, |a + tw|−1/2−δ
|w|δ.
(3.32)
In case 2,
max (|a + sw|, |a + tw|) ≤2|s −t||w|,
(3.33)
we immediately obtain
m(a, s, t, w) ≲max

|a + sw|−1/2, |a + tw|−1/2
≲max

|a + sw|−1/2−δ, |a + tw|−1/2−δ
|s −t|δ
| {z }
≤2δ
|w|δ.
(3.34)
We begin with the ﬁrst factor in (3.28). In case 1 we always have
m(ξ1 −u, 0, s1, w) ≲|ξ1 −u|−1/2−δ|w|δ.
(3.35)
In case 2 we have either |ξ1 −u + s1w| ≥1
2|ξ1 −u| which immediately results in (3.35) or the
opposite
|ξ1 −u + s1w| ≤1
2|ξ1 −u|
(3.36)
which leads to
1
Z
−1
χ|ξ1−u+s1w|≤|ξ1−u|m(ξ1 −u, 0, s1, w) ds1 ≲|w|δ
Z
|ξ1−u+s1w|≤|ξ1−u|
|ξ1 −u + s1w|−1/2−δ ds1
≲|w|δ−1
Z
|σ|≤|ξ1−u|
|σ|−1/2−δ dσ ≲|w|δ−1|ξ1 −u|1/2−δ
(3.38)
≲|ξ1 −u|−1/2−δ|w|δ,
for δ ∈(0, 1
2).
(3.37)
Here we made use of the fact that, given case 2 for a := ξ1 −u and (3.36),
|a| ≤min (|a + sw| + |s||w|, |a + tw| + |t||w|) ≤min (|a + sw|, |a + tw|) + |w|
(3.36)
≤
1
2|a| + |w|,
implies
|a| ≤2|w|.
(3.38)
29
Applying (3.32) and (3.34), we arrive at
Z
[−1,1]3
k(ξ, u, s, w) ds
≲|w|δ−2|ξ1 −u|−1/2−δ
"
[−1,1]2 m(ξ2 −u, s2, s3, w)m(ξ3 −u, s2, s3, w) ds2 ds3
≲|w|3δ−2|ξ1 −u|−1/2−δ
"
[−1,1]2 µ2

|ξ2 −u + s2w|−1/2−δ, |ξ2 −u + s3w|−1/2−δ
·
· µ3

|ξ3 −u + s2w|−1/2−δ, |ξ3 −u + s3w|−1/2−δ
ds2 ds3
(3.39)
where
µi = µi (ξi −u, s2, s3, w) ∈{min, max} ,
i = 2, 3,
depending on the respective case. If case 1 holds for at least one of the two factors in the
integrand, say the ﬁrst one, we may choose the argument of
µ2

|ξ2 −u + s2w|−1/2−δ, |ξ2 −u + s3w|−1/2−δ
which contains the same integration variable as the second one. This results in terms of
type (3.29b). If, however, case 2 applies to both factors, the integral in (3.39) is bounded
by
"
[−1,1]2

|ξ2 −u + s2w|−1/2−δ + |ξ2 −u + s3w|−1/2−δ
·
·

|ξ3 −u + s2w|−1/2−δ + |ξ3 −u + s3w|−1/2−δ
ds2 ds3.
Expanding the integrand, the terms |ξ2 −u + siw|−1/2−δ|ξ3 −u + siw|−1/2−δ, i = 2, 3, lead us
to (3.29b). For the two remaining terms we may separate the integrals which gives
X
(σ(2),s(3))∈{(2,3),(3,2)}
1
Z
−1
|ξσ(2) −u + s2w|−1/2−δ ds2
1
Z
−1
|ξσ(3) −u + s3w|−1/2−δ ds3.
One integral is kept in order to arrive at (3.29a), the other one is treated analogously to (3.36)
and (3.37). In order to estimate Γ(u), we obtain thus for δ1, δ2 ∈(0, 1
2)
Z
R3
Z
(−1,1)3
F(ξ1) F(ξ2) F(ξ3) k(ξ, u, s, w)ds dξ
≈
1
Z
−1
|w|−1+(3δ−1)|I 1−2δ
2 F(u)|2 I 1−2δ
2 F(u −tw) dt
+
1
Z
−1
|w|−1+(3δ−1)I 1−2δ
2 F(u) |I 1−2δ
2 F(u −tw)|2 dt,
30
which implies
Γ(u)
≲
1
Z
−1
Z
˜w
t2−3δ | ˜w|−1+(3δ−1)|I 1−2δ
2 F(u)|2 I 1−2δ
2 F(u −˜w) t−1 d ˜w dt
+
1
Z
−1
Z
˜w
t2−3δ | ˜w|−1+(3δ−1)I 1−2δ
2 F(u) |I 1−2δ
2 F(u −˜w)|2 t−1 d ˜w dt
δ∈( 1
3 , 1
2 )
≈
Z
w
|w|−1+(3δ−1)|I 1−2δ
2 F(u)|2 I 1−2δ
2 F(u −w) dw
+
Z
w
|w|−1+(3δ−1)I 1−2δ
2 F(u) |I 1−2δ
2 F(u −w)|2 dw
≈
|I 1−2δ
2 F(u)|2 I 4δ−1
2 F(u) + I 1−2δ
2 F(u) I3δ−1|I 1−2δ
2 F(u)|2.
Setting δ :=
5
12, this is (3.15).
3.6. Proof of Lemma 3.5
Plugging together (3.12), Lemma 3.2, and Lemma 3.3 we get for small s and some θ > 0 that
Z
g′
iωi j |D|
1
2 g′
j |D|
1
2 ϕ
≲∥ϕ∥∞∥Γ∥1,Br + ∥Is|D|
1
2 ϕ∥(
2
1−2s ,1)·
·
r
1
2 + ∥|D|
1
2 g′∥2
(2,∞),BΛr +

|D|
1
2 g′

(2,∞),R
∞
X
k=2
Λ−θ(k−1)∥|D|
1
2 g′∥(2,∞),BΛkr
.
By the estimate of Γ from Lemma 3.4, for F := ||D|
1
2 g′|,
∥Γ∥1,Br
≲

|I 1
12 |F||2 I 1
3 |F| + I 1
12 |F| I 1
4

|I 1
12 |F||2

1,Br
≲
Θ
 

I 1
3 |F|

(6,∞),Br +

I 1
12 |F|

( 12
5 ,∞),Br
!
,
where
Θ :=

I 1
12 |F|

2
( 12
5 ,2),Br +

I 1
4

|I 1
12 |F||2

( 12
7 ,1),Br.
Observe,
∥I 1
3 F∥(6,∞)
≲
∥F∥(2,∞)
∥I 1
12 F∥( 12
5 ,2)
≲
∥F∥2,
31
and because 5
12 + 5
12 + 1
6 = 1,
∥I 1
12 F∥( 12
5 ,q)
≲
∥F∥(2,q),
∥I 1
4 |I 1
12 F|2∥( 12
7 ,1)
≲
∥|I 1
12 F|2∥( 6
5 ,1) = ∥|I 1
12 F|∥2
( 12
5 ,2) ≲∥F∥2.
Consequently, Θ is uniformly small, if r is small enough. In order to conclude, it only remains
to apply Lemma A.2 to f := |F|.
□
