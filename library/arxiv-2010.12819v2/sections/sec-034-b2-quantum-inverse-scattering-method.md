---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-034-b2-quantum-inverse-scattering-method
section_title: "B.2 Quantum Inverse Scattering Method"
section_number: null
pages: 39-40
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
In the framework of the quantum inverse scattering method, we express local operators O in terms of the
operators A,B,C,D . Let t(η
2 ) = A(η
2 ) +D(η
2 ) denote the transfer matrix, that is, the trace of T(u) in the
homogeneous case u = η/2 = iγ/2 (which will sometimes have to be taken as a limit, as we shall see below).
We recall that the XXZ Hamiltonian (19) is recovered from T−1(u)∂T
∂u
⏐⏐⏐
u=η/2
. Acting on a Bethe state, where
n is the number of roots characterizing the state, the transfer matrix has eigenvalues
t
(η
2
) n∏
k=1
B(λk)|0⟩ =
[
a
(η
2
) n∏
k=1
b−1
(
λk,η
2
)
+d
(η
2
) n∏
k=1
b−1
(η
2,λk
)] n∏
k=1
B(λk)|0⟩. (157)
With the conventions used in [58], a(λ) = 1, d(λ) =∏N
m=1b(λ,ξm), so that d(ξm) = 0 even before taking the
homogeneous limit. We denote by φm{λ} =∏N
k=1
(
b−1(
λk, η
2
))m
the factor produced by the action of tm(η
2
)
,
which appears in the computation of form factors. We can then express the matrix elements of j neighbouring
operators (acting on consecutive sites m,m + 1,...,m +j− 1) in the form
⟨{µ}|
j∏
i=1
(Oi)m+i−1|{λ}⟩ =φm−1({µ})φ−1
m+j−1({λ})FO1,...,Oj, (158)
where FO1,...,Oj depends on the combination of operators O whose matrix elements we wish to obtain, while
the pre-factors φm{λ} only depend on how many operators we consider and at which sites. The expression
for FO1,...,Oj is site-independent: all dependence on the site m is in the phase coming from the φ pre-factors in
(158). Below we use the shorthand notation z↔ σz,−↔ σ−, +↔ σ+ to denote the required operators O,
and we wish to compute expressions such as F−+.
Because of this site-independence, in numerical applications it is most eﬃcient to compute the relevant
FO1,...,Oj only once for each sizeN, and then add up any site-dependent phases (see section 4.3) in an independent
step when using the form factors. 17 Combined with the parity and conjugation relations mentioned earlier, this
signiﬁcantly reduces the computational load. Furthermore most scalar products Sn (see below) are used in
several form factors. This can be taken advantage of as well.
We wish to ﬁnd FO1,...,Oj for the combinations of Pauli matrices shown in and below (88)–(89). To this end,
we shall need to consider the following operators (given here with their shorthand abbreviation):
z : σz
m↔A(ξm)−D(ξm), or 2A(ξm)− 1, or 1− 2D(ξm), (159a)
+ : σ+
m↔C(ξm), (159b)
− : σ−
m↔B(ξm) (159c)
16Note that the Bethe roots come in conjugate pairs (or are real, or self-conjugate), so that in total we do indeed get the expression
for Bethe states as in eq (90).
17For the speciﬁc purpose of computing the Koo-Saleur generators, keeping track of phases actually turns out to be unnecessary,
because of the considerations about momentum conservation made in section 5.1.
39
in the homogeneous limit ξm → η/2. For instance, to get Fz we can compute FD =⟨C|D(ξm)|B⟩, where
⟨C| =⟨0|∏
jC(µj) and |B⟩ = ∏
kB(λk) are Bethe states. We shall always keep ⟨C| untouched (and thus
still on-shell), commuting the operators above past the string of B-operators, so that the result will become
expressed in terms of new, oﬀ-shell states | ˜B⟩. (See the commutation relations below, where some B(λk) are
swapped into B (ξm) with ξm = η
2 .) When computing the ﬁnal scalar products Sn =⟨C| ˜B⟩, we can then still
use relations that hold when one of the states is on-shell.
In order to commute all the operators past the B-operators we use the following commutation relations,
where ϕ(λ) = sinh(λ):
A(ξm)
n∏
k=1
B(λk)|0⟩ =
n∏
k=1
ϕ(λk−ξm +η)
ϕ(λk−ξm)
n∏
k=1
B(λk)|0⟩
−
n∑
a=1
ϕ(η)
ϕ(λa−ξm)
n∏
k=1,k⁄=a
ϕ(λk−λa +η)
ϕ(λk−λa) B(ξm)
n∏
k=1,k⁄=a
B(λk)|0⟩, (160a)
C(ξm)
n∏
k=1
B(λk)|0⟩ =
n∑
a=1
Ma(ξm)
n∏
k=1,k⁄=a
B(λk)|0⟩ +
∑
a⁄=b
Mab(ξm)B(ξm)
n∏
k=1,k⁄=a,b
B(λk)|0⟩, (160b)
D(ξm)
n∏
k=1
B(λk)|0⟩ = −
n∑
a=1
ϕ(η)
ϕ(ξm−λa)
n∏
k=1,k⁄=a
ϕ(λa−λk +η)
ϕ(λa−λk) d(λa)B(ξm)
n∏
k=1,k⁄=a
B(λk)|0⟩, (160c)
with
Ma(ξm) = ϕ(η)
ϕ(λa−ξm)
∏
k⁄=a
ϕ(λk−ξm +η)
ϕ(λk−ξm)
ϕ(λk−λa +η)
ϕ(λk−λa) , (161a)
Mab(ξm) = ϕ(η)2
ϕ(λa−ξm)ϕ(λb−ξm)
∏
k⁄=a
ϕ(λk−λa +η)
ϕ(λk−λa)
ϕ(λk−λb +η)
ϕ(λk−λb) . (161b)
We have written out factors ofb−1(µ,λ ) explicitly to make it clearer later which terms will need to be combined
in the homogeneous limit. Note that the B-operators commute among themselves.
Finally we need to divide through with the norms of the Bethe states after obtaining the required form
factors, as the states we use are otherwise not normalized. For roots {λ} solving the Bethe equations, the
corresponding state has the norm squared (written using the conventions of [58])
Nn({λ}) =ϕn(η)
∏
α⁄=β
ϕ(λα−λβ +η)
ϕ(λα−λβ) det(G({λ}), (162)
with
Gab({λ}) =− ∂
∂λb
ln

r(λa)
n∏
k=1,k⁄=a
b(λa,λk)
b(λk,λa)

. (163)
Here r(λ) =a(λ)/d(λ).
