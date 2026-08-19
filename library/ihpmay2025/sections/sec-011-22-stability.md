---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY"
section_id: sec-011-22-stability
section_title: "Stability"
section_number: 2.2
pages: 17-19
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
It is a crucial property of convex cocompact representations, known as stability, thatgCC (M)
is open in Hom(Γ , PSL(2, C)). This was first established by Marden [50]. Informally, if you
wiggle a convex cocompact representation a little bit it remains convex cocompact.
One can easily see how this phenomena works for Schottky groups. If Γ = ⟨γ1,...,γ n⟩
is the Schottky group constructed in Section 1, we may view it as the image of a convex
cocompact representation of Fn = ⟨a1,...,a n⟩, ρ : Fn → PSL(2,C ) where ρ(ai) = γi. If
σ∈ Hom(Fn,PSL (2,C ) is close enough to ρ, then
{C1,...,C n,ρ (a1)(C1),...,ρ (an)(Cn)}
is a collection of disjoint circle. So, the image of σ is a Schottky group and σ is convex
cocompact. It follows that ρ lies in the interior of CC (Hn).
Theorem 2.2. If ρ :π1(M)→ PSL(2, C) is convex cocompact, then there exists a neighborhood
U of ρ in Hom(π1(M), PSL(2, C)) such that if σ∈U, then σ is convex cocompact.
Theorem 2.2 was first establshed by Marden [50, Theorem 10.1]. Thurston [75, Proposition
8.3.3] observed that it followed from argument of the form due to Weyl, see also Canary-Epstein-
Green [23, Section I.2.5].
Proof. The proof relies on the following local-to-global principle. We will sketch a proof in our
setting in the next subsection.
Theorem 2.3. (Local to Global Principle) GivenK≥ 1,C≥ 0, there exists ˆK, ˆC andA so that
ifJ is an interval in R andh :J→ H3 is a (K,C )-quasi-isometric embedding restricted to every
connected subsegment of J with length≤A, then h is a ( ˆK, ˆC)-quasi-isometric embedding.
LetKM denote the Cayley graph ofπ1(M) with respect to some generating set S and choose
x0∈ H3. There exists ( K,C ) so that the orbit map τρ : KM → H3 (with basepoint x0) is
a (K,C )-quasi-isometric embedding. The local-to-global principle, see Theorem 2.5, implies
that there exists A≥ 1, ˆK, and ˆC so that if f : J → H3 (where J is an interval in R) is
a (K +C + 1, 2K + 3C + 5)-quasi-isometry on all segments of length at most A, then f is a
( ˆK, ˆC)-quasi-isometry.
Let U be an open neighborhood of ρ in Hom(π1(M), PSL(2, )) so that if σ∈U, γ∈π1(M)
and dS(1,γ )≤A, then d(ρ(γ(x0)),σ (γ)(x0))< 1. (We may do so since there are only finitely
many elements of γ within A of id.)
18 RICHARD D. CANARY
If σ∈U, let τσ be the orbit map of σ with basepoint x0. We see that if dS(1,γ )≤A, then
1
KdS(id,γ )−C− 1≤d(τσ(id),τσ(γ))≤KdS(id,γ ) +C + 1.
Since τσ is σ-equivariant, we see that if α,β ∈ Γ and dS(α,β )≤A, then
1
KdS(α,β )−C− 1≤d(τσ(α),τσ(β))≤KdS(α,β ) +C + 1.
We now check that τσ is a quasi-isometric embedding on all geodesic segments in KM of
length at most A. Since τσ is (K +C + 1)-bilipschitz on each edge with a vertex at the origin
and it is σ-equivariant, we conclude that τσ is (K +C + 1)-bilipschitz on each edge of KM and
hence globally bilipschitz.
Let ab be a segment in KM of length at most A joining a to b. Since τσ is (K +C + 1)-
bilipschitz,
d(τσ(a),τσ(b))≤ (K +C + 1)dKM (a,b ).
We must work a little harder to get the lower bound. Let α be the vertex on [a,b ] closest to
a and let β be the vertex on [a,b ] closest to b. Then d(a,α )< 1, d(b,β )< 1 and d(α,β )≤A.
So
d(τx(a),τx(b)) ≥ d(τσ(α),τσ(β))− 2(K +C + 1)
≥ 1
KdS(α,β )−C− 1− 2(K +C + 1)
≥ 1
K (dKM (a,b )− 2)− 2K− 3C− 3
≥ 1
KdKM (a,b )− 2K− 3C− 5
Therefore, the extended orbit map ˆτσ is a (K +C + 1, 2K + 3C + 5)-quasi-isometry on all
geodesic segments in KM of length at most A. Since ˆτσ isσ-equivariant, ˆτσ is a (K + 2,C + 2)-
quasi-isometric embedding on all geodesic segments in CM of length at most A. Therefore, ˆτσ
is a ( ˆK, ˆC)-quasi-isometric embedding on all geodesic segments in KM, which implies that ˆτσ
is a ( ˆK, ˆC)-quasi-isometric embedding. Therefore, σ is convex cocompact. □
Since the set CC (M) is invariant under conjugation, we immediately see that both gCC (M)
and its quotient CC (M) are open.
Corollary 2.4. IfM is a compact, irreducible 3-manifold with non-empty boundary, thenCC (M)
is open in X(M).
Remark: If M is a closed hyperbolic 3-manifold which admits a hyperbolic structure, then
Mostow’s Rigidity Theorem [62] implies that CC (M) consists of two points (one for each ori-
entation on M),
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS 19
