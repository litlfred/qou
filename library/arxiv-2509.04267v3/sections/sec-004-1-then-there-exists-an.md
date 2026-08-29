---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-004-1-then-there-exists-an
section_title: "Then there exists an"
section_number: 1
pages: 8-10
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
infinitesimal deformation ˜R=ϕ 0 +ℏϕ 1 =R+ℏϕand˜µ=µ+ℏµ 1 on ˜V=k[[ℏ]]/(ℏ 2)⊗Vsuch
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 9
that ˜S= ( ˜R,α,β,˜µ)is an EYBO on ˜Vif and only if the following equations hold:
X
(i,j,k)∈Γ
(µi⊗µj)ϕk =
X
(i,j,k)∈Γ
ϕi(µj⊗µk),(5)
X
(i,j,k)∈Γ
Tr2(ϕi(µj⊗µk)) =αβµ 1,(6)
X
(i,j,k)∈Γ
Tr2(ˆϕi(µj⊗µk)) =α −1βµ1,(7)
where ˆϕ0 =ϕ−1
0 , and ˆϕ1 =−ϕ−1
0 ϕ1ϕ−1
0 .
Moreover, if ˜Sis an EYBO andb m is anm-braid representing a knotK, the quantity
Ψ1
˜S(bm) =
X
(i,j1,...,jm)∈Γm+1
α−w(bm)β−n Tr(Ψi
ϕ(bm)(µj1⊗···⊗µ jm))(8)
does not depend on the choice ofb m used, and it is invariant under Markov moves. It is therefore
a knot invariant.
Proof.We prove the first statement. Observe that given ˜R=ϕ 0 +ℏϕ 1, its inverse is given by
˜R−1 = ˆϕ0 +ℏ ˆϕ1, up to quadratic terms inℏ, as one might verify directly. The characterization of
the conditions on ˜Sbeing an EYBO module up to degree 2 gives, quotienting out higher degrees
inℏ, Equation (1) and Equation (2).
For the second statement, since ˜Sis an EYBO on ˜V=k[[ℏ]]/(ℏ 2)⊗V, using classical results
of Turaev in [20], it follows that the trace ofα −w(D)β−nΨϕ(bm) is a knot invariant. Since the
summationP
(i,j1,...,jm)∈Γm+1 collects degree 1 terms with respect toℏ, one sees that it gives precisely
the term in (8). □
Definition 4.4.From the second statement of this theorem, we denote the Expression (8) by
Φ1
˜S(K), or Φ 1
ϕ(K) when other data for ˜Sare understood, without an explicit reference to the braid
bm used to obtain the operator Ψ 1
˜S(bm), as the trace is independent of this choice. We also denote
the Turaev’s invariant for the undeformedS= (R,α,β,µ) by Φ 0
ϕ(K), and combine both by the
expression Φϕ(K) = Φ0
ϕ(K) +ℏΦ 1
ϕ(K).
We now consider the effect of deforming an EYBO by a YB coboundary.
Lemma 4.5.Let(R,α,β,µ)denote an EYBO, and letϕ=δ 1
YB(f)be a cobounded YB2-cocycle.
Then,( ˜R,α,β,˜µ)is an EYBO, where ˜R=R+ℏϕ, and˜µ=µ+ℏµ 1, withµ 1 =µf−fµ.
Proof.We first show (5), i.e. ˜R(˜µ⊗˜µ) = (˜µ⊗˜µ)˜R. We need to show that the following equation
holds
ϕ(µ⊗µ) +R(µ 1⊗µ) +R(µ⊗µ 1) = (µ⊗µ)ϕ+ (µ 1⊗µ)R+ (µ⊗µ 1)R.
For the left-hand side, using the defining formula ofϕ=δ 1
YB(f) and the fact thatRand (µ⊗µ)
commute by assumption, we compute
ϕ(µ⊗µ) +R(µ 1⊗µ) +R(µ⊗µ 1) =R(fµ⊗µ) +R(µ⊗fµ)−(fµ⊗µ)R−(µ⊗fµ)R
+R(µf⊗µ)−R(fµ⊗µ) +R(µ⊗µf)−R(µ⊗fµ).
Similarly, for the right-hand side we obtain
(µ⊗µ)ϕ+ (µ 1⊗µ)R+ (µ⊗µ 1)R=R(µf⊗µ) +R(µ⊗µf)−(µf⊗µ)R−(µ⊗µf)R
+(µf⊗µ)R−(fµ⊗µ)R+ (µ⊗µf)R−(µ⊗fµ)R.
