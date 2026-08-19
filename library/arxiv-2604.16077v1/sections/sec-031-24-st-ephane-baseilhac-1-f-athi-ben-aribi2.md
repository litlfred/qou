---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-031-24-st-ephane-baseilhac-1-f-athi-ben-aribi2
section_title: "ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2"
section_number: 24
pages: 24-26
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
(iv) We can give explicit numerical values for the constants B′,B ′′ > 0 in Lemma 3.3, fol-
lowing the computations in [11, Lemma 7.13] (see the formula of Bδ on page 367 of that
paper).
Proof. It follows from Lemmas 7.13 and 7.14 in [11] by a change of vari able and a very small
adaptation. Let us give a few details. First we consider the i nequalities, since for them the
adaptation is simpler to describe.
Lemmas 7.13 and 7.14 in [11] deal with Φ b( y
2πb ), with the assumptions I(y) ∈ [δ,π −δ]
and I(y) ∈ [−π +δ, −δ] respectively. From the proof of these lemmas, it is easy to s ee
that these assumptions, keeping the same conclusions, can b e extended to I(y) ∈ [0,π −δ]
and I(y) ∈ [−π +δ, 0] respectively. By setting b := 1/
√
N and y = z −iπ +iπ/N, these
conclusions imply immediately that, given δ >0,N , and z ∈ R +i[δ − π
N, 2π − π
N −δ], there
exists a constant Bδ > 0 as in the statement such that⏐
⏐
⏐
⏐R
(
Log( ˆSN (z)) − N
2iπ Li2(ez+ iπ
N )
) ⏐
⏐
⏐
⏐ ≤ Bδ
N .
More precisely, denoting
ǫ(z) := 1
z2
( z
sinh(z) − 1
)
(the Taylor remainder at 0 of order 2 of the function z ↦→z/ sinh(z)), and Ω ⊂ C a contour
equal to R except near 0 where it avoids 0 upwards while staying in a disk D(0,R ) with
center 0 and radius R ∈]0,π [, we have
(58) Log( ˆSN (z)) − N
2iπ Li2(ez+ iπ
N ) = 1
N ΞN (z)
for z ∈ R +i[δ − π
N, 2π − π
N −δ], where
(59) Ξ N (z) :=
∫
v∈Ω
ǫ
(v
N
) exp(−izv
π −v + v
N )
4 sinh(v) dv
is holomorphic in the open strip R +i] − π
N, 2π − π
N [ and satisﬁes |ΞN (z)| ≤ Bδ on the closed
substrip R +i[δ − π
N, 2π −δ − π
N ]. (We stress that in Lemma 7.13 of [11] the stated upper
bound is |R(ΞN (z))| ≤ Bδ, where the constant Bδ := B′/δ +B′′ is described explicitly on
page 367, but the conclusion is deduced from the inequality |R(ΞN (z))| ≤ | ΞN (z)| and an
upper bound for |ΞN (z)|).
We want to replace the term N
2iπ Li2(ez+ iπ
N ) with N
2iπ Li2(ez). For this, we will use a Taylor
expansion.
Recall that we take z ∈]−∞,M ]+i[δ − π
N, 2π −δ − π
N ], with N large enough so that δ − π
N > 0.
In particular, the arguments of the logarithms and dilogari thms in the following formulas will
avoid the cuts of these functions. Since
(60) Li 2(ez+ iπ
N ) − Li2(ez) = −iπ
N
∫ 1
0
Log(1 −ez+ iπ
Nt)dt,
we have
R
(N
2iπ Li2(ez+ iπ
N ) − N
2iπ Li2(ez)
)
= − 1
2
∫ 1
0
Log
⏐
⏐
⏐1 −ez+ iπ
Nt
⏐
⏐
⏐dt = −
∫ 1
0
Log
⏐
⏐
⏐1 −ez+ iπ
Nt
⏐
⏐
⏐
1
2
dt.
Now |1 −ez|
1
2 ≤
√
1 + |ez| ≤
√
1 +eM for all z ∈] − ∞,M ] + i[δ − π
N, 2π −δ]. Deﬁne
cM :=
√
1 +eM . We get, for every z ∈] − ∞,M ] +i[δ − π
N, 2π −δ − π
N ]:
⏐
⏐
⏐
⏐R
(
Log( ˆSN (z)) − N
2iπ Li2(ez)
) ⏐
⏐
⏐
⏐ ≤ Log(cM ) + Bδ
N .
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 25
The pair of inequalities in the statement immediately follo ws.
Let us now prove the equality (56) and the upper bound (57). Fr om (58) and (60), we obtain
Log( ˆSN (z)) = N
2iπ Li2(ez+ iπ
N ) + 1
N ΞN (z)
= N
2iπ Li2(ez) − 1
2
∫ 1
0
Log(1 −ez+ iπ
Nt)dt + 1
N ΞN (z).
Another Taylor expansion gives us
(61) Log(1 −ez+ iπ
Nt) = Log(1 −ez) − 1
N EN (z,t ),
where EN (z,t ) := (iπt)
∫ 1
0
ez+ iπ
Nts
1 −ez+ iπ
Ntsds. Hence we obtain
Log( ˆSN (z)) = N
2iπ Li2(ez) − 1
2 Log(1 −ez) + 1
2N
∫ 1
0
EN (z,t )dt + 1
N ΞN (z).
This gives (56), by setting
(62) Ψ N (z) := ΞN (z) + 1
2
∫ 1
0
EN (z,t )dt = ΞN (z) + iπ
2
∫ 1
t=0
t
∫ 1
s=0
ez+ iπ
Nts
1 −ez+ iπ
Ntsdsdt.
Consider the strip ] − ∞,M ] +i[δ − π
N, 2π −δ − π
N ]. We know that |ΞN (z)| ≤ Bδ, and from
Lemma 3.2 the second term gives:⏐
⏐
⏐
⏐
⏐
iπ
2
∫ 1
t=0
t
∫ 1
s=0
ez+ iπ
Nts
1 −ez+ iπ
Ntsdsdt
⏐
⏐
⏐
⏐
⏐ ≤ π
2
∫ 1
s=0
⏐
⏐
⏐
⏐
⏐
ez+ iπ
Nts
1 −ez+ iπ
Nts
⏐
⏐
⏐
⏐
⏐ds ≤ πeM/2
2δ
√
1 − π2
24
.
By the triangle inequality, (57) follows at once. ✷
Let us draw the following important though easy consequence of Lemma 3.3 and the functional
equation (51). It will be used in Lemma 5.5.
By the domains where Log( ˆSN (z)) (deduced after (51)) and Li 2(ez) and Log(1 −ez) are holo-
morphic functions (here, C \ (∪k∈Z (2iπk + [0, +∞[))), the identity (56) immediately shows
that ΨN has a holomorphic extension on the domain
(63) C \

⋃
p∈N
(
[0, +∞[+i
(
2π + 2πp
N
)) ⋃ (⋃
l∈N
(
[0, +∞[−i(l + 1) 2π
N
) ) ⋃
[0, +∞[

.
In particular Ψ N is holomorphic on the domain (see Figure 2)
U := {z ∈ C | R(z)< 0}
⋃
{z ∈ C | 0< I(z)< 2π}.
In the following lemma, for every M ∈ R, α ∈]0, 1[, k ∈ Z≤0, K >2π, and c> 0 we consider
the sets UM,α,k,K,c ⊂ C formed by the points z such that (see Figure 2):
• R(z) ≤M and (α − 1)π
N < I(z)< 2π − (α + 1)π
N , or
• R(z)< 0 and 2πk + (α − 1)π
N ≤ I(z) ≤ (α − 1)π
N , or
• R(z)< −c and 2π − (α + 1)π
N ≤ I(z) ≤K.
Lemma 3.5. (i) The sequence of functions ΨN converges simply to a holomorphic function
on the strip 0< I(z)< 2π.
(ii) The function | exp( 1
N ΨN )| is bounded from above by a constant independent of N on each
set UM,α,k,K,c .
