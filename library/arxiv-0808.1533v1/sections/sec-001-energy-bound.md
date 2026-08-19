---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S3 R. Komendarczyk ∗"
section_id: sec-001-energy-bound
section_title: "Energy bound."
section_number: null
pages: 23-27
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
doc_brief: "The third order helicity of magnetic fields via link maps. R. Komendarczyk ∗† — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us"
duplicate_of: "arxiv-0808.1533v3"
---
In this section we indicate how the quantity H123(X; T ) invariant under frozen-in-ﬁeld defor-
mations provides a lower bound for the L2-energy E2(X) of a volume preserving ﬁeld X on
M = S3. For simplicity we restrict our considerations to the case of an invar iant unlinked
handlebody T , as in Section 4. For the notation used in this section see Appendix C.
Recall the deﬁnition
E2(X) =
∫
M
|X|2 = ‖X‖2
L2(M ) . (35)
The ordinary helicity H12(X) provides the well known lower bound (see [3, p. 123]):
1
λ1
|H12(X)| ≤ E2(X),
23
where λ1 is the ﬁrst eigenvalue of the elliptic self adjoint operator ∗ d : Ω 1(M) ↦→Ω 1(M) (i.e.
the curl operator). Importance of such lower energy bounds, s tems from an area of interest
in the ideal magneto-hydrodynamics, [26], as this constrains the ph enomenon of “magnetic
relaxation”. A need for higher helicities can be justiﬁed by the fact t hat one may easily
produce examples of vector ﬁelds X for which H12(X) vanishes, but the energy of the ﬁeld X
still cannot be relaxed. For example consider a classical case of bor romean ﬂux tubes T Borr
with X smooth and vanishing outside the tubes. Moreover assume that or bits of X are just
“parallel circles” inside each tube. By taking X = X1 + X2 + X3, bilinearity of H12( · , · ) on
Vectvol(S3) and disjoint supports of Xi yield
H12(X) = H12(X, X) =
3∑
i=1
H12(Xi, Xi) +
∑
i⁄=j
H12(Xi, Xj) = 0 ,
because “cross-helicities” H12(Xi, Xj), i ⁄= j vanish by Formula (30), and self-helicities
H12(Xi, Xi) vanish as well because the average linking number of orbits is zero ( orbits are
just parallel circles). Nevertheless, Formula (31) tells us
H123(X; T Borr) ⁄= 0,
thus we may regard H123(X; T ) as a possible “higher obstruction” to the energy relaxation
or the third order cross-helicity of X on T .
To obtain a lower bound for E2(X) in such situations we notice that H123(X; T ) is the
L2-inner product of the 6-forms: ∗(ω ∧ αω) and ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3. Indeed from (19) we
have
H123(X; T ) =
(
∗(αω ∧ ω), ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3
)
L2Ω 6((S3)3) .
Let CT = ‖αω ∧ ω‖L2, for a ﬁxed Riemannian product metric on ( S3)3 this constant depends
on the domain T in ( S3)3. We estimate using the Cauchy-Schwartz inequality
|H123(X; T )| ≤ ‖ αω ∧ ω‖L2‖ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3‖L2
= CT
(∫
T
(ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3) ∧ ∗(ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3)
) 1
2
(36)
(1)
= CT
(∫
T
|X1|2|X2|2|X3|2 µ
) 1
2
(2)
= CT
(∫
T1
|X1|2
) 1
2
(∫
T2
|X2|2
) 1
2
(∫
T3
|X3|2
) 1
2
≤ CT E2(X)
3
2 , (37)
where E2(X) =
∫
S3 |X|2. To observe (1) ﬁrst note that for any pair of forms: α ∈ Ω k(M),
and β ∈ Ω j(N), on Riemannian manifolds M and N, on the product M × N we have
∗M ×N (π∗
M (α) ∧ π∗
N (β)) = ( ∗M π∗
M α) ∧ (∗N π∗
N β), (38)
24
where πM : M × N − →M and πN : M × N − →N are the natural projections, (the proof is
a simple calculation in an orthogonal frame of the product and is left t o the reader). Now,
identity (1) follows by applying (38) to the integrand in (36), and obs erving in the coframe
{ηi
k} on the i-th factor of ( S3)3 (Xi = (a1, a2, a3)):
ιXiµi ∧ ∗ιXiµi = ( a1ηi
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
3 = |Xi|2ηi
1 ∧ ηi
2 ∧ ηi
3 = |Xi|2µi .
The next identity (2) follows from the Fubini’s Theorem.
Our next goal is to provide an estimate for CT . For this purpose we review some basic
L2-theory of the operator d−1 (i.e. inverse of the exterior derivative d). The main goal is to
estimate an L2-norm of the potential αω of ω in (17).
Following the standard elliptic theory of diﬀerential forms, [27], the p otential αω in (17)
can be obtained via a solution to the Neumann problem for 2-forms on ~T (see Appendix C)
{
∆ φN = ω, in ~T
n φN = n dφN = 0, on ∂~T , (39)
where n stands for the normal component of a diﬀerential form, and ∆ = dδ + δd. Because
T is a domain with corners we replace it by a slightly larger domain ~T in ( S3)3 with the
same topology (i.e. T is a deformation retract of ~T ) but with smooth boundary ∂~T . Notice
that because of the “gauge invariance” ( i) of Theorem 4.3, in the deﬁnition of H123(X; T )
we my use the restriction of
αω = δφN , (40)
to T (see Appendix C for justiﬁcation of (40)). Associated to (39) is th e Neumann Laplacian
∆ N : H 2Ω 2
N (~T ) − →L2Ω 2(~T ),
which has a discrete positive spectrum {λi,N } and eigenvalues satisfy the variational principle
called Rayleigh-Ritz quotient, [10]. The ﬁrst (principal) eigenvalue λ1,N may be expressed as
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
which restricts to a compact, self-adjoint operator on L2. As a result spectrum of GN is
discrete and given as {1/λi,N }. Note that based on these considerations we may deﬁne
d−1 := δGN .
25
Theorem 6.1 (Energy bound) . For every volume preserving vector ﬁeld X which has an
invariant unlinked domain T , the L2-energy of X on S3 is bounded below by the third order
helicity H123(X; T ), as follows
|H123(X; T )| ≤ CT (E2(X))
3
2 . (41)
Moreover, we may estimate the constant CT :
CT ≤ 1√
λ1,N
‖ω‖2
L∞Ω 2( eT )(Vol(S3))3, (42)
where λ1,N is the ﬁrst eigenvalue of the Neumann Laplacian on Ω 2(~T ).
Proof. We estimate
‖αω‖2
L2 = ‖δφN ‖2
L2 ≤ ‖ dφN ‖2
L2 + ‖δφN ‖2
L2
= |(∆ φN , φN )| ≤ ‖ ω‖L2‖φN ‖L2,
where we used the Green’s formula [27, p. 60] and boundary conditio ns of (39) in the second
identity. Now, because φN = GN ω, and it is a well known fact that ‖GN ‖L2 = 1
λ1,N
, ( GN is
compact self-adjoint on L2) we obtain:
‖αω‖L2 ≤ 1√
λ1,N
‖ω‖L2 .
As a result we estimate CT :
CT = ‖αω ∧ ω‖L2 ≤ ‖ ω‖L∞‖αω‖L2
≤ 1√
λ1,N
‖ω‖L2‖ω‖L∞.
Notably the best energy estimate has been obtained by Freedman a nd He, [15], for the
L3/2-energy of X, in the case when X admits an invariant domain T modeled on an n-
component link L = {L1, . . . , Ln} in R3. Their estimate is based on the asymptotic crossing
number and reads
E3/2(X) ≥
(π
16
) 1/4
( n∑
k=1
ac(Lk, L)|Flux(Xk)|
)
· min
1≤k≤n
{|Flux(Xk)|}, (43)
where the asymptotic crossing numbers ac( Lk, L) for borromean links can be estimated below
by a smallest genus among surfaces in R3 \ {L1 ∪ . . . ∪ ˆLk ∪ . . . ∪ Ln} with a single boundary
component Li. Since L3/2-energy of X bounds the L2-energy, via the H¨ older Inequality,
thus (43) leads to a lower estimate purely in terms of ﬂuxes and topo logical data. It is not
26
clear to the author if this approach can be extended to the case of invariant handlebodies
considered in Section 4. A diﬀerent, more optimal estimate, has bee n obtained by Laurence
and Stredulinsky, via the Massey product formula, in [21], but the pr oof is provided only in
a special case of the vector ﬁeld X.
Contrary to these lower bounds which are given in terms of topologic al data the estimate
in (42) depends on the geometry of the domain T , and also ‖ω‖L∞. Unfortunately, ω blows
up on the diagonals ∆ ⊂ (S3)3, and as a result the estimate is meaningless when the
handlebodies Ti get close to each other during the evolution of the magnetic ﬁeld X. At
this point, we need an assumption for Ti to stay 1cm apart during the evolution. Another
drawback is that λ1,N is a geometric constant which is altered during the evolution as well.
