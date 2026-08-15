---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-018-312-the-t-qβ-reduction-from-bps-spectral-sequenc
section_title: "The t =qβ reduction from BPS spectral sequence"
section_number: 3.1.2
pages: 30-32
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
One interesting property of the invariants ( 3.1) and ( 3.12) is their behavior under the spe-
cialization t =qβ with β∈ Z. First, they all become polynomial after taking this limit. For
example,
Ir,f=1(q,t )
t=qβ
−→
∞∏
j=0
1−q1−r/2−β+j
1−qr/2+β+j = (q1−r/2−β;q)r+2β−1, (3.16)
is simply a polynomial (as opposed to a power series). Second, they exhibit “positivity” in
the sense that if one adds a minus sign setting t =−qβ, one ﬁnds a polynomial with only
positive coeﬃcients:
Ir,f=1(q,t =−qβ) =
r+2β−2∏
j=0
(
1 +q1−r/2−β+j
)
. (3.17)
Here, these phenomena originate from the fact that, upon setting t =qβ, there is a lot of can-
cellation between contributions from bosonic and fermionic generators, with onlyψ+,∂ψ+,. . . ,
∂2β
+ ψ+ remaining. However, as we will see in later part of this paper, these phenomena are
actually very universal and also appear in a wide variety of 3d N = 2 theories T [M3] with
the symmetry U(1)β. Therefore, it is interesting to understand the t = qβ reduction at the
categoriﬁed level.
The natural uplift of the reduction of superconformal indices
IT [M3](q,t ) ↝ I(β)
T [M3](q) =I(q,qβ) (3.18)
is a BPS spectral sequence [44]:
HBPS
Q ↝ HBPS
Q+Q′, (3.19)
– 29 –
which starts with the space of BPS states of T [M3] on S2 and converges to the space of
Q +Q′-cohomology with a deformed supercharge. For concreteness, we will focus on the
example of a single chiral Φ = ( φ,ψ ) with R-charge r = 2, which can be understood as the
theory T [S3,U (1)]. The ﬁrst step is to explicitly identify the space of BPS states HS2 found
in the previous section as the Q-cohomology for a supercharge in the following way.
All four supercharges of a 3d N = 2 theory can be preserved on S2× R. We pick a
supercharge Q =Q− parametrized by a Killing spinor ζ+ with
j3(ζ+) = 1
2, R (ζ+) =−1. (3.20)
The supergravity background is given by
Vµ =A(R)
µ =−iδµ3, (3.21)
with the other components of the background multiplet set to zero. 29 Then, the on-shell
SUSY variation given by Q− is
δφ = 0
δψ = 0
δφ =
√
2ζ+ψ−,
δψ =−
√
2iγµζ+Dµφ +
√
2iσφζ+,
(3.23)
where we have included a background U(1)β vector multiplet (Aµ,λ, λ,σ,D ), and Dµ is a
covariant derivative that involves the Levi-Civita connection, Aµ and A(R)
µ . Then the Q-
closed states are φ, ψ± and their derivatives. Among them ψ−, D3φ and ∂−φ are Q-exact,
while D3ψ+ and∂−ψ+ are eliminated by the equation of motion. So we have found that the
space of BPS states is exactly the cohomology of Q =Q−.
One might expect a spectral sequence to arise when Q is deformed into Q +Q′, whose
second page is given by
E•,•
2 =H•(H•
Q,Q′). (3.24)
The simplest scenario is to have only non-trivial diﬀerentials on the second page, enabling us
to read oﬀH•
Q+Q′ from the third page, like most examples studied in [44].
When we take t =qβ, we are eﬀectively shifting the U(1)R charge by 2β multiple of the
U(1)β charge. As a result, the operators φ and ∂2β+1
+ ψ+ have the same R/2 +j3 quantum
number and their contribution to the index cancels. Then, naively, we expect to have the
following action of Q′ on φ:
[Q′,φ ]∼∂2β+1
+ ψ+. (3.25)
29We have chosen the round metric and the veilbein
e1 =dθ, e 2 = sinθdϕ, e 3 =dx3. (3.22)
– 30 –
However, no supercharges can achieve this, even if we turn on more general supergravity
backgrounds, as φ and ψ live in diﬀerent representations of the supersymmetry algebra and
don’t mix.
Another possibility is to have φ and ∂2β+1
+ ψ+ to be eliminated separately. This can be
achieved by turning on −2β + 1 units of U(1)β ﬂux along S2 = CP1.30 Now φ and ψ+ are
holomorphic sections of
φ∈H0(CP1,O (−2β + 1)), ψ+∈H0(CP1,O (2β)). (3.26)
The former has no sections, while the latter has 2β+1 sections given byψ+,∂+ψ+,...,∂ 2β
+ ψ+.
At the level of SUSY transformations, we now have a term in δψ of the following form
(δψ)−∼γ−ζ+D−φ, (3.27)
making all modes of φ exact under Q +Q′. On the other hand, the equation of motion for
ψ+ will impose
D−ψ+ = 0, (3.28)
but there are solutions to this equation, because ψ have negative charge under U(1)β. It
would be interesting to pursue this analysis further in non-trivial examples and also make
contact with [64] and [65], where similar phenomena were studied in theories with larger
supersymmetry.
