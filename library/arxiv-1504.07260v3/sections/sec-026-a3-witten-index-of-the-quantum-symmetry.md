---
doc_id: arxiv-1504.07260v3
doc_title: "Prepared for submission to JHEP Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3 1Fundamental Physics, Chalmers University of Technology, 412 96, Gothenburg, Swe"
section_id: sec-026-a3-witten-index-of-the-quantum-symmetry
section_title: "A.3 Witten index of the quantum symmetry"
section_number: null
pages: 41-44
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
doc_brief: "Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3 1Fundamental Physics, Chalmers University of Technology, 412 96, Gothenburg, Sweden 2Theory Group, SLAC National Accelerator Laborat"
---
LetC be a non-linear sigma model on K3,g be a symmetry preserving theN = (4, 4)
superconformal algebra and let us assume that the orbifold theoryC′ =C/⟨g⟩ is consistent,
i.e. the twisted sectors satisfy the level-matching condition (λ = 1). In this section, we
compute the twined Witten index of the quantum symmetryQ. By deﬁnition ofQ, this is
given by
IC′
Qk =
N∑
t=1
e
2πikt
N sdim(H⟨g⟩
gt ) , (A.17)
whereHgt denotes the space ofgt-twisted Ramond-Ramond ground states (i.e. with con-
formal weights( 1
4, 1
4)),H⟨g⟩
gt is itsg-invariant subspace andsdimH⟨g⟩
gt is the superdimension
(Z2-graded by(−1)F + ˜F) ofH⟨g⟩
gt . By the standard orbifold construction,sdimH⟨g⟩
gt is given
by
sdimH⟨g⟩
gt = 1
N
N∑
v=1
IC
gt,gv , (A.18)
where
IC
gt,gv := TrRR,Hgt(gv(−1)F + ˜FqL0− c
24 ¯q
¯L0− c
24 ) , (A.19)
is thegt-twisted gv-twined Witten index. The indexIC
gt,gv is a specialization toz = 0 of
the twisted twining elliptic genusφgt,gv(τ,z ). In turn, the twisted-twining elliptic genus
φgt,gv(τ,z ) can be obtained from the untwisted oneφ1,g(t,v,N)(τ,z ) by a modular transfor-
mation. By specializing to z = 0, the dependence on τ drops and we have simply the
identity
IC
gt,gv =IC
g(v,t,N) . (A.20)
– 40 –
Using (3.19), we can now prove (3.20):
IC′
Qk =
N∑
t=1
e
2πikt
N
1
N
N∑
v=1
IC
gt,gv =
N∑
t=1
e
2πikt
N
1
N
N∑
v=1
IC
g(v,t,N)
=
N∑
t=1
e
2πikt
N
1
N
N∑
v=1
∑
u|(t,v,N)
m(u)u
=
N∑
t=1
e
2πikt
N
∑
u|(t,N)
m(u)u
N
N∑
v=1
δ(v modu)
=
N∑
t=1
e
2πikt
N
∑
u|(t,N)
m(u) =
∑
u|N
m(u)
N∑
t=1
e
2πikt
N δ(t modu)
=
∑
u|N
m(u)
N/u∑
l=1
e
2πikl
N/u =
∑
u|N
m(u)N
uδ(k modN/u)
=
∑
n|(k,N)
m(N/n)n .
(A.21)
Finally, let us consider the analysis of the Witten index for case whereλ >1. In this
case, the orbifold ofC by g is not consistent andλ is the smallest power such thatgλ
gives rise to a consistent orbifold. Failure of the level matching condition implies that the
twining genusφg(τ,z ) is modular up to a phase. This implies that the twining Witten index
IC
g =φ(τ, 0) must vanish. The same argument applies togk, for anyk with (λ,k )⁄=λ
IC
gk = 0 if (λ,k )⁄=λ . (A.22)
As a consequence, a cycle of lengtha in the cycle shape ofg can have non-zero multiplicity
m(a)⁄= 0 only ifa is a multiple ofλ. To show this, consider by absurd that there is some
cycle of lengthb such thatm(b)⁄= 0 and (b,λ ) < λ. Without loss of generality, we can
assume thatb is the smallest such cycle. Then, we have the contradiction
0 =IC
gb =
∑
u|(b,N)
um(u) =bm(b) , (A.23)
where the last equality follows because allu < bwith m(u)⁄= 0 are multiple ofλ and
therefore cannot divideb.
Let∏
a|N
λ
a ˜m(a) be the cycle shape ofgλ. Since all cycle lengths in the cycle shape of
g are multiple ofλ, we have the relation
˜m(a) =λm(λa) , (A.24)
which allows us to reconstruct the cycle shape ofg when the cycle shape ofgλ is known.
Since the orbifold bygλ is consistent, then (3.15) holds and
IC′
:=
∑
a|N
λ
N
λa ˜m(a)∈{ 0, 24} (A.25)
– 41 –
whereIC′
is the Witten index of the orbifoldC′ =C/⟨gλ⟩. Using (A.24) we have
∑
a|N
λ
N
λa ˜m(a) =
∑
a|N
λ
N
λaλm(λa) =λ
∑
b|N
N
b m(b). (A.26)
so that ∑
b|N
N
b m(b) =IC′
λ . (A.27)
By assumption, (3.15) is not satisﬁed byg, so thatIC′
⁄= 0,C′ is a K3 model and
∑
b|N
N
b m(b) = 24
λ . (A.28)
As explained in appendix A.2, we are interested in a symmetryg′ in the orbifold theoryC′
that acts by
e
2πia
N gE−1
g , (A.29)
on thegλ-invariantgλa-twisted sectorH⟨gλ⟩
gaλ . Here,E−1
g ∈ Z/λZ is determined byE−1
g Eg≡ 1
mod λ. Such an element always exist because(Eg,λ ) = 1. Furthermore,g has orderλ on
H⟨gλ⟩
gaλ , so thatgE−1
g is well-deﬁned. The standard orbifold formula gives
IC′
g′k =
N/λ∑
a=1
e
2πiak
N
λ
N
N/λ∑
v=1
IC
gλa,gλv+E−1g k . (A.30)
By (A.22),IC′
g′k vanishes unlessk is a multiple ofλ, i.e.
IC′
g′k = 0 if (λ,k )⁄=λ . (A.31)
By the same reasoning as forg, we obtain that the cycle shape∏
a|Nam′(a) of g′ contains
only cycles with length multiple ofλ and that the cycle shape∏
a|Na ˜m′(a) of g′λ is given
by the analogue of (A.24)
˜m′(a) =λm′(λa) . (A.32)
The twining indicesIC′
g′jλ, j = 1,...,N/λ are given by
IC′
g′jλ =
N/λ∑
a=1
e
2πiajλ
N
λ
N
N/λ∑
v=1
IC
gλ(a,v+E−1g j,N/λ) =
N/λ∑
a=1
e
2πiajλ
N
λ
N
N/λ∑
v=1
IC
gλ(a,v,N/λ) . (A.33)
By the same computation as in theλ = 1 case, we obtain
IC′
g′jλ =
∑
n|(j,N/λ)
˜m(N
λn)n . (A.34)
This implies that
˜m′(n) = ˜m(N
λn) , (A.35)
– 42 –
that is
m′(λn) =m(N/n) , (A.36)
or, equivalently,
m′(a) =m(Nλ
a ) . (A.37)
