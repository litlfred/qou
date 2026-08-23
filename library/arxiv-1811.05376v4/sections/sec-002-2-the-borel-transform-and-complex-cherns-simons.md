---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-002-2-the-borel-transform-and-complex-cherns-simons
section_title: "The Borel transform and Complex Cherns-Simons"
section_number: 2
pages: 15-17
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
We now provide the proof of Theorem 2. The reader not familiar with the Borel transformB and
its relation to the Laplace transform is encouraged to read Section A, before reading the proof of
Theorem 2. For a measurable functiong : R+→ C of suﬃcient decay, we use the notationLR+(g)
for the Laplace transform – see Equation (88).
Proof of Theorem 2.We start by giving a characterization of which of the phases in (16) give a
non-zero contribution. Introduce forµ∈ Q/Z the set
T (µ) ={m = 1,..., 2P− 1 :−m2/4P =µ mod Z}
={m = 1,..., 2P− 1 :g(2πim) = 2πiµ mod 2πiZ}
The set of phases2πiR∗(X) in (17) consists of the valuesg(2πim) = −m22πi
4P for which
∑
x∈T (−m2/4P)
Res
(F (y)ekg(y)
1−e−ky ,y = 2πix
)
⁄= 0, (34)
for m = 1,..., 2P− 1. Thus, by Corollary 8, we must prove that if (34) holds, then there exists
˜m∈T (−m2/4P ) such that at mostn− 3 of thepj’s which divide˜m.
We start by noting that the set of poles ofF is given by
PF ={2πim|m∈ Z and m is divisible by at mostn− 3 of thepj’s}. (35)
It follows that if ˜m is divisible by at leastn− 2 of the pj, then F (y) does not have a pole at
y = 2πi ˜m and we get for integralk
Res
(F (y)ekg(y)
1−e−ky ,y = 2πi ˜m
)
=F (2πi ˜m)ekg(2πi ˜m)Res
( 1
1−e−ky,y = 2πi ˜m
)
=F (2πi ˜m)ekg(2πi ˜m) 1
k.
As we already noted above, Lawrence and Rozansky checked that all thek−1 terms cancels, so it
follows that
∑
˜m∈T (−m2/4P),
and ˜m is divisible by at least n− 2 of the pj
Res
(F (y)ekg(y)
1−e−ky ,y = 2πi ˜m
)
= 0.
Resurgence Analysis of Quantum Invariants 16
Therefore we see that if (34) holds, then there is some˜m∈T (−m2/4P ) which is divisible by at
most n− 3 of thepj. This establishesR∗(X)⊂ CS∗
C and we get (3). Observe that as a corollary
we obatin for eachθ∈ CS∗
C the formula
e2πikθ Zθ(k) =−
∑
˜m∈T (θ)
Res
(F (y)ekg(y)
1−e−ky ,y = 2πi ˜m
)
. (36)
We now turn toB(Z0). The formal series Z0 is the the asymptotic expansion of the Laplace
integral
ZI(k) = 1
2πi
∫
γ
F (y)ekg(y) dy.
Let G be the rational function introduced in (2) and introduce the multivalued functionB0(ζ)
given by
B0(ζ) = κ
πi√ζG
(
exp
(κ√ζ
P
))
= κi
4π
∏n
j=1 sinh
(
κ√ζ
pj
)
√ζ
(
sinh
(
κ√ζ
))n−2.
With this notation, the equation for the Borel transform (4) which we want to prove, reads as
follows
B(Z0) =B0.
The functionB0 is related toF as follows
B0(ζ) =
√
2P√πiζF
(√
8πiPζ
)
. (37)
Now as,F (−y) =F (y) we have a convergent power series expansion valid fory close to 0
F (y) =
∞∑
m=1
F (2m)(0)
(2m)! y2m.
Therefore Equation (37) implies that if we set
Bm = 1
2πi
√
8πiPF (2m)(0)
(2m)! (8πiP )m
then we have a convergent expansion valid forζ close to 0 of the form
B0(ζ) =
∞∑
m=1
Bmζm−1/2. (38)
Introduce the variablet deﬁned by
−t =g(y) = iy2
8πP.
Thus
dy = 1
2
√
8πiP
t dt.
We now rewriteZI(k) as the Laplace transform ofB0
ZI(k) = 1
2πi
∫
γ
F (y)ekg(y) dy = 1
2πi
∫ ∞
0
e−kt
∫
g=t
F
dg dt
= 1
2πi
∫ ∞
0
e−kt
√
8πiP
t F
(√
8πiPt
)
dt
=
∫ ∞
0
e−ktB0(t) dt =LR+(B0)(k).
(39)
The existence of the asymptotic expansion (17)
Resurgence Analysis of Quantum Invariants 17
ZI(k) =LR+(B0)(k)∼k→∞ Z0(k)
can now be obtained by appealing to the ﬁrst part of Lemma 2 where we setB =B0. Here we use
the existence of the expansion (38). Therefore the desired identity (4)B(Z0) =B0 follows from
the second part of Lemma 2 and the convergence of the expansion (38).
As F (−y) =F (y) we note that the factor
ζ↦→F
(√
8πiPζ
)
gives a well-deﬁned meromorphic function. ThusB(Z0)(ζ) is a multivalued meromorphic function
with a square root singularity at0 and with singularities for√8πiPζ ∈P F wherePF is the set of
poles ofF (y). This set was computed above (see equation (35)) and we conclude that the poles of
B(Z0)(ζ) occur at
ζm =−πm2
2iP =−m2
4P
2π
i
with m∈ Z being divisible by less than or equal ton− 3 of thepj’s. This concludes the proof of
(5).
It is of course expected that only a Chern-Simons invariantθ of a ﬂatSU(2) connection have
a non-vanishing polynomialZθ⁄= 0, i.e.
R∗(X) = SCS(M∗ (X, SU(2))).
