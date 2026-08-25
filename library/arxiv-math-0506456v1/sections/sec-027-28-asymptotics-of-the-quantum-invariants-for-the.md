---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-027-28-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 28
pages: 27-28
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
diﬃcult since higher order terms in the Taylor expansion of Ψ( x0 +αs,y 0 +βt) need
to be involved, and it is likely that the analysis can not be carried throu gh in this
case.) For that reason we make the following deﬁnition.
Deﬁnition 1. A critical point ( x,y ) of the phase function Ψ is called positive
deﬁnite if ( x,y ) is non-degenerate and there exists ( α,β ) ∈ S1 × S1 such that
Im(A) is positive deﬁnite, where
A = diag(α,β )Hdiag(α,β ),
where H is the Hessian of Ψ in ( x,y ).
Assume that (x0,y 0) is positive deﬁnite and let ( α,β ) ∈S1 ×S1 such that Im(A)
is positive deﬁnite. Then the main contribution to the integral K(x0,y 0) in the limit
of large r is given by
Kmain(x0,y 0) = αβ sin
(π
q (x0 − 2nd)
)
e2πirΨ( x0,y0)
∫
R2
e
πir⟨A

 s
t

,

 s
t

 ⟩
dsdt,
and this integral can be evaluated using the results of [12, Sec. 3.4]. In fact,
∫
R2
e
πir⟨A

 s
t

,

 s
t

 ⟩
dsdt = 1
r (det(−iA))−1/2,
whereA is independent of r. Note here that the set S of complex symmetric 2 × 2–
matricesB with Re(B) positive deﬁnite is an open convex set in the 3–dimensional
complex vector space of symmetric 2 × 2–matrices. It follows that their is a unique
analytic branch of B ↦→(det(B))1/2 onS such that (det(B))1/2> 0 for B real. We
have used that branch in the above result. We note that det( −iA) = −(αβ)2 det(H).
In conclusion we can state the following result.
Theorem 4. Let Sµ,ν,n
k,l,a,b be the set of critical points of Φ a,b
n in Σ µ,ν,n
k,l,a,b. IF Conjec-
ture 3 is true and if all the critical points of Φ a,b
n in Σ µ,ν,n
k,l,a,b are positive deﬁnite,
k,l = 0, 1, (a,b ) ∈ Fk,l, µ,ν ∈ {± 1}, n ∈ Z/|q|Z, then the leading order large r
asymptotics of the quantum invariant is given by
¯τr(Mp/q) ∼ isign(q)
4
√
|q|
e
3πi
4 sign(pq) ∑
n∈Z/|q|Z
∑
(k,l)∈{0,1}2
∑
(a,b)∈Fk,l
∑
(µ,ν)∈{±1}2
µν
×
∑
(x,y)∈S µ,ν,n
k,l,a,b
(
− det(H(x,y)Φa,b
n )
) −1/2
× sin
(π
q (x − 2nd)
)
e2πirΦ a,b
n (x,y),
where H(x,y)Φa,b
n is the Hessian of Φ a,b
n in (x,y ).
28 Asymptotics of the quantum invariants for the ﬁgure 8 knot
According to the above theorem the growth rate of the quantum in variants of
Mp/q is r0 if we can prove that the values of the phase functions Φ a,b
n in the points
Sµ,ν,n
k,l,a,b are real. This we do in Sec. 5.3, see Corollary 5. This is in agreement with
our computer studies of the quantum invariants of Mp/q. To obtain Theorem 3
from Theorem 4, hence a leading asymptotics as predicted by the AE C, we have to
prove i) that the union of the sets of critical points Sµ,ν,n
k,l,a,b corresponds to the ﬂat
(irreducible) SU(2)–connections onMp/q and ii) that the values of the relevant phase
functions Φ a,b
n in these critical points are equal to the Chern–Simons invariants of
these ﬂat connections. This we also do in Sec. 5.3. Note that we have used the
expression (4.52) for the determinant of the Hessian H(x,y)Φa,b
n in Theorem 3.
Remark 4. The manifolds Mp/q, |p/q| ∈ { 1, 2, 3}, are Seifert manifolds and by [10]
(1.11) holds for these manifolds if we put m ¯ρ = 4 for all ¯ρ ∈ M ′
p/q. Moreover, the
results in Appendix C show that the part of the leading order large r asymptotics
of τr(M0) associated to the irreducible SU(2)–connections on M0 is equal to the
right-hand side of (1.11) if we put m ¯ρ = 4 for both points ¯ ρ in M′
