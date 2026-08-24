---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-001-energy-bound
section_title: "Energy bound."
section_number: null
pages: 21-25
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us to a"
---
In this section we indicate how the quantity H123(B; T ) invariant under frozen-in-ﬁeld de-
formations provides a lower bound for the L2-energy E2(B) of a volume preserving ﬁeld B
on M = S3. We restrict our considerations to the case of an invariant unlinked handlebody
T , deﬁned in Section 4. For the notation used in this section see Appen dix C.
Recall the deﬁnition
E2(B) =
∫
M
|B|2 = ‖B‖2
L2(M ) . (7.1)
The ordinary helicity H12(B) provides a well known lower bound (see [3, p. 123]):
1
λ1
|H12(B)| ≤ E2(B),
where λ1 is the ﬁrst eigenvalue of the elliptic self adjoint operator ∗ d : Ω 1(M) ↦→Ω 1(M)
(known as the curl operator), ∗ denotes the Hodge star. Importance of such lower energy
bounds, stems from an area of interest in the ideal magnetohydro dynamics, [32], as this
constrains the phenomenon of “magnetic relaxation”, [14]. A need f or higher helicities can
be justiﬁed by the fact that one may easily produce examples of vec tor ﬁelds B for which
H12(B) vanishes, but the energy of the ﬁeld B still cannot be relaxed. For example, consider
a classical case of Borromean ﬂux tubes T Borr with B smooth and vanishing outside the
tubes. Furthermore, assume that orbits of B are just “parallel circles” inside each tube. By
taking B = B1 + B2 + B3, bilinearity of H12( · , · ) on SVect( S3) and disjoint supports of Bi
yield
H12(B) = H12(B, B) =
3∑
i=1
H12(Bi) +
∑
i⁄=j
H12(Bi, Bj) = 0 ,
where “cross-helicities” H12(Bi, Bj), i ⁄= j vanish by Formula (6.1), and self helicities H12(Bi)
vanish because the average linking number of orbits is zero (orbits a re just parallel circles).
21
Nevertheless, Formula (6.2) tells us
H123(B; T Borr) ⁄= 0,
as a result we may regard H123(B; T ) as a possible “higher obstruction” to the energy relax-
ation or the third order cross-helicity of B on T .
To obtain a lower bound for E2(B) in such situations we notice that H123(B; T ) is the
L2-inner product of the 6-forms: ∗(ω ∧ αω) and ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3. Indeed, from (4.4) we
have
H123(B; T ) =
(
∗(αω ∧ ω), ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3
)
L2Ω 6((S3)3) .
Let CT = ‖αω ∧ ω‖L2, for a ﬁxed Riemannian product metric on ( S3)3 this constant depends
on the domain T in ( S3)3. We estimate using the Cauchy-Schwarz inequality
|H123(B; T )| ≤ ‖ αω ∧ ω‖L2‖ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3‖L2
= CT
(∫
T
(ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3) ∧ ∗(ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3)
) 1
2
(1)
= CT
(∫
T
|B1|2|B2|2|B3|2 µ
) 1
2
(2)
= CT
(∫
T1
|B1|2
) 1
2
(∫
T2
|B2|2
) 1
2
(∫
T3
|B3|2
) 1
2
≤ CT E2(B)
3
2 ,
(7.2)
where E2(B) =
∫
S3 |B|2. To observe (1) ﬁrst note that for any pair of forms: α ∈ Ω k(M),
and β ∈ Ω j(N), on Riemannian manifolds M and N, on the product M × N we have
∗M ×N (π∗
M (α) ∧ π∗
N (β)) = ( ∗M π∗
M α) ∧ (∗N π∗
N β), (7.3)
where πM : M × N − →M and πN : M × N − →N are the natural projections, (the proof is
a simple calculation in an orthogonal frame of the product and is left t o the reader). Now,
step (1) in (7.2) follows by applying (7.3) to the integrand, and obser ving in the coframe
{ηi
k}:
ιBiµi ∧ ∗ιBiµi = ( a1ηi
2 ∧ ηi
3 − a2ηi
1 ∧ ηi
3 + a3ηi
1 ∧ ηi
2) ∧ (a1ηi
1 − a2ηi
2 + a3ηi
3)
= ( a2
1 + a2
2 + a2
3) ηi
1 ∧ ηi
2 ∧ ηi
3 = |Bi|2ηi
1 ∧ ηi
2 ∧ ηi
3 = |Bi|2µi,
where Bi = (a1, a2, a3). Step (2) in (7.2) follows from Fubini Theorem.
Next, we aim to provide an estimate for CT . For this purpose we review some basic
L2-theory of the operator d−1 (i.e. inverse of the exterior derivative d). The main goal is
to estimate an L2-norm of the potential αω of ω in (4.2). Following the standard elliptic
theory of diﬀerential forms, [34], the potential αω in (4.2) can be obtained via a solution to
the Neumann problem for 2-forms on ~T (see Appendix C)
{
∆ φN = ω, in ~T
n φN = n dφN = 0, on ∂~T , (7.4)
22
where n stands for the normal component of a diﬀerential form, and ∆ = dδ + δd, δ = ± ∗d∗,
(c.f. [34]). As T is a domain with corners we replace it by a slightly larger domain ~T in (S3)3
with the same topology (i.e. T is a deformation retract of ~T ) but with smooth boundary ∂~T .
(One may argue that it is not really necessary, since T is Lipschitz and elliptic problems,
such as (7.4) are well posed on Lipschitz domains, [31]). Because of ( i) in Theorem 4.3, we
may use the restriction of
αω = δφN , (7.5)
to T (see Appendix C for justiﬁcation of (7.5)). Associated to (7.4) is th e Neumann Laplacian
∆ N : H 2Ω 2
N (~T ) − →L2Ω 2(~T ),
which has a discrete positive spectrum {λi,N } and eigenvalues satisfy the variational principle
called Rayleigh-Ritz quotient, [11]. The ﬁrst (principal) eigenvalue λ1,N may be expressed as
λ1,N = inf
(‖dϕ‖2
L2 + ‖δϕ‖2
L2
‖ϕ‖2
L2
⏐
⏐
⏐ ϕ ∈ H 1Ω 2
N (M) ∩ H2
N (M)⊥
)
We denote the inverse of ∆ N by
GN : L2Ω 2(~T ) − →H 2Ω 2
N (~T ),
which restricts to a compact, self-adjoint operator on L2. As a result the spectrum of GN
is discrete and given as {1/λi,N }. Note that based on these considerations we may deﬁne
d−1 := δGN .
Theorem 7.1 (Energy bound) . For every volume preserving vector ﬁeld B which has an
invariant unlinked domain T , the L2-energy of B on S3 is bounded below by the third order
helicity H123(B; T ), as follows
|H123(B; T )| ≤ CT (E2(B))
3
2 . (7.6)
Also, we may estimate the constant CT :
CT ≤ 1√
λ1,N
‖ω‖2
L∞Ω 2( eT )(Vol(S3))3, (7.7)
where λ1,N is the ﬁrst eigenvalue of the Neumann Laplacian on Ω 2(~T ).
Proof. We estimate
‖αω‖2
L2 = ‖δφN ‖2
L2 ≤ ‖ dφN ‖2
L2 + ‖δφN ‖2
L2
= |(∆ φN , φN )| ≤ ‖ ω‖L2‖φN ‖L2,
23
where we used the Green’s formula [34, p. 60] and boundary condit ions of (7.4) in the second
identity. Now, because φN = GN ω, and it is a well known fact that ‖GN ‖L2 = 1
λ1,N
, ( GN is
compact self adjoint on L2) we obtain:
‖αω‖L2 ≤ 1√
λ1,N
‖ω‖L2 .
As a result we estimate CT :
CT = ‖αω ∧ ω‖L2 ≤ ‖ ω‖L∞‖αω‖L2
≤ 1√
λ1,N
‖ω‖L2‖ω‖L∞.
Notably, the best energy estimate so far has been obtained by Fre edman and He, [15],
for the L3/2-energy of B, in the case when B admits an invariant domain T modeled on
an n-component link L = {L1, . . . , Ln} in R3. Their estimate is based on the asymptotic
crossing number and reads
E3/2(B) ≥
(π
16
) 1/4
( n∑
k=1
ac(Lk, L)|Flux(Bk)|
)
· min
1≤k≤n
{|Flux(Bk)|}, (7.8)
where the asymptotic crossing numbers ac( Lk, L) for Borromean links can be estimated below
by a smallest genus among surfaces in R3 \ {L1 ∪ . . . ∪ ˆLk ∪ . . . ∪ Ln} with a single boundary
component Li. Since L3/2-energy of B bounds the L2-energy, inequality (7.8) leads to a
lower estimate purely in terms of ﬂuxes and topological data. It is no t clear to the author
if this approach can be extended to the case of invariant handlebod ies considered in Section
4. A diﬀerent, more optimal estimate, has been obtained by Lauren ce and Stredulinsky, via
the Massey product formula, in [26], but the proof is provided only in a special case of the
vector ﬁeld B.
Contrary to these lower bounds, which are given in terms of topolog ical data, the estimate
in (7.6) depends on the geometry of the domain T , and also ‖ω‖L∞. Unfortunately, ω blows
up on the diagonals ∆ ⊂ (S3)3, and as a result the estimate is meaningless when the
handlebodies Ti get close to each other during the evolution of the magnetic ﬁeld B. At
this point, we need an assumption for Ti to stay 1cm apart during the evolution. Another
drawback is that λ1,N is a geometric constant which is altered during the evolution as well.
If we consider the situation in which the boundaries of Ti are invariant during the evolution,
the estimate may be useful. Under such assumption, which occurs w henever the velocity
ﬁeld v of plasma in (1.1) is tangent to ∂Ti, the bound in (7.7) stays constant.
24
