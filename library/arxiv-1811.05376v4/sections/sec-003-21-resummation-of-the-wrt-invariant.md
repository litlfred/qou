---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-003-21-resummation-of-the-wrt-invariant
section_title: "Resummation of the WRT invariant"
section_number: 2.1
pages: 17-18
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
We now turn to the resummation of the normalized WRT invariant˜Zk(X). Recall that forµ∈ Q/Z
we introduced the set
T (µ) ={m = 1,..., 2P− 1 :−m2/4P =µ mod Z}.
We also introdude the residue operatorIµ which for a meromorphic functionˆϕ is given by
Iµ( ˆϕ)(ξ) =−
∑
x∈T (µ)
Res


exp
(
ξ iy2
8πP
)
(1−e−ξy)
y
4P ˆϕ
( y2
i8πP
)
,y = 2πix


Observe that by deﬁnitionT (µ) is empty for all but ﬁnitely manyµ∈ Q/Z and thereforeIµ is 0
for all but these ﬁnitely manyµ.
Corollary 10. The polynomialsZθ and the quantum invariant~Zk(X) are determined byB(Z0) as
follows
Zθ(k) =e−2πikθIθ (B(Z0)) (k). (40)
~Zk(X) =LR+(B(Z0))(k) +
∑
θ∈ i
2π Ω mod Z
Iθ (B(Z0)) (k). (41)
The identity (41) of Corollary 10 is reminiscent of the typical resummation process from resur-
gence [6, 19]. The Ohtsuki-series is known to determine τk(X). The new insight provided by
resurgence is that it does so via resummation as stated in Corollary 10.
We now prove Corollary 10.
Proof. It easily follows from (4) that
F (ζ) =B(Z0)
( ζ2
i8Pπ
) ζ
4P. (42)
Resurgence Analysis of Quantum Invariants 18
Recall from (36) that
e2πikθ Zθ(k) =−
∑
˜m∈T (θ)
Res
(F (y)ekg(y)
1−e−ky ,y = 2πi ˜m
)
.
From this and Equation (42) one easily obtains (40).
In the proof of Theorem 2 we obtained the following exact formula
˜Zk(X) =LR+(B)(k) +
∑
θ∈CS∗
C(X)
e2πikθ Zθ(k). (43)
Thus we see that (41) follows from this formula and (40).
