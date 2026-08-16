---
doc_id: arxiv-1504.07260v3
doc_title: "Prepared for submission to JHEP Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3 1Fundamental Physics, Chalmers University of Technology, 412 96, Gothenburg, Swe"
section_id: sec-021-54-the-heterotic-helicity-supertrace
section_title: "The heterotic helicity supertrace"
section_number: 5.4
pages: 34-36
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
doc_brief: "Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3 1Fundamental Physics, Chalmers University of Technology, 412 96, Gothenburg, Sweden 2Theory Group, SLAC National Accelerator Laborat"
---
Let us now analyse the counting of BPS-states from the heterotic perspective. The gener-
ating function of helicity supertraces for heterotic strings onT 6 is [31]
Zhet(υ, ¯υ) = ϑ1(υ/2)4
η12¯η24
ξ(υ)¯ξ(¯υ)
τ2
ΘΓ6,22 , (5.30)
and the fourth helicity supertrace is5
B4 =
( 1
2πi
∂
∂υ + 1
2πi
∂
∂¯υ
)4
Zhet(υ, ¯υ)|υ=0 =
( 1
2πi
∂
∂υ
)4
Zhet(υ, ¯υ)|υ=0 = 3
2τ2
ΘΓ6,22
¯η24 .
(5.31)
5This corrects a typo in eq. (G.9) of [31] which lacks the factorΘΓ6,22.
– 33 –
Let us consider the case whereT 6 is the product of two orthogonal toriT 2×T 4, with
no Wilson lines alongT 2. The lattice of winding momenta decomposes accordingly as
Γ6,22∼= Γ2,2⊕ Γ4,20 . (5.32)
ACHLmodelisgivenbyaorbifoldbyasymmetry ˆg actingbya 1/ ˆN periodshift δ∈ Γ2,2⊗R
along one of the circles ofT 2 and by an automorphismg on the latticeΓ4,20. The generating
function is given by
Zhet
CHL[g](υ, ¯υ) = ϑ1(υ/2)4
η12
ξ(υ)¯ξ(¯υ)
τ2
1
ˆN
ˆN−1∑
r,s=0
ΘΓ2,2
[r
s
]Θ(r,s)
Γ4,20
¯ηgr,gs
, (5.33)
where
Θ(0,s)
Γ4,20 = Θ(Γ4,20)gs (5.34)
and when (r,s )≡ (lc,ld ), withc,d,l ∈ Z and c,d coprime, we have
Θ(lc,ld)
Γ4,20 (τ, ¯τ) = (cτ +d)−2(c¯τ +d)−10Θ(0,l)
Γ4,20
(aτ +b
cτ +d,a¯τ +b
c¯τ +d
)
, (5.35)
for some integersa,b such that
(a b
c d
)
∈ SL(2, Z). In the denominator of (5.33) we also
deﬁned the generalized eta product which in general takes form [53]:
ηg,h(τ) =q
1
Nλ
24∏
i=1
∞∏
n=0
(1−e
2πiti
M q
ri
N +n) , gh =hg , (5.36)
where M is the order ofh, and the integers0 < r1,...,r 24≤ N and 0 < t1,...,t 24≤ N
are such that{(e2πiri
N, e2πiti
M )} is the set of simultaneous eigenvalues ofg and h. Taking
derivatives ofZhet
CHL[g](υ, ¯υ) we obtain the fourth helicity supertrace
BCHL[g]
4,het = 3
2τ2
1
ˆN
ˆN−1∑
r,s=0
ΘΓ2,2
[r
s
]Θ(r,s)
Γ4,20
¯ηgr,gs
. (5.37)
IntegratingBCHL[g]
4,het against the fundamental domain ofSL(2, Z) should now yield the het-
erotic topological 1-loop amplitude [59]
˜F1 = 2
3
∫
F
BCHL[g]
4,het , (5.38)
which in particular depends on (Thet,U het) but is independent of Shet. Therefore, this
coupling is 1-loop exact on the heterotic side. If we expand this in the large-volume limit
ImThet→∞ and map to the type IIA picture via(Uhet↔ UIIA,T het↔ SIIA) we obtain
the one-loop IIA counterpart of ˜F1 supplemented with an inﬁnite series of exponentially
suppressed terms of orderO(e− ImSIIA) due to D-instantons. Finally, performing the mirror
map UIIA↔TIIA (see [59]) then reproduces precisely the couplingf CHL[ˆg]
R2 (TIIA) in (5.26).
Thus, the sequence of dualities just described ensures that the counting of 1/2 BPS-states
in CHL via the fourth helicity supertrace is indeed consistent with heterotic-type II duality
and Fricke S-duality.
– 34 –
