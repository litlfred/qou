---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-004-14-the-1-loop-invariant-and-its-twisted-version
section_title: "The 1-loop invariant and its twisted version"
section_number: 1.4
pages: 7-8
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
has a conjectural description in terms of the 1-loop invariant of [DG13]. The latter depends
on the NZ matrices of an ideal triangulation, its shapes, their ﬂattenings and a peripheral
curveγ. With the notation of Section 1.3 the 1-loop invariant is deﬁned by
τ CS
γ (T ) :=
det
(
ˆA diag(ζ) +ˆB diag(ζ′′)
)
2∏N
j=1ζ
fj
j ζ
′f′
j
j ζ
′′f′′
j
j
=
det
(
ˆG diag(ζ) +ˆG′ diag(ζ′) +ˆG′′ diag(ζ′′)
)
2∏N
j=1ζ
fj
j ζ
′f′
j
j ζ
′′f′′
j
j
∈F/(±1)
(20)
where the last equality follows from Equation (8). In [DG13] it is conjectured that the 1-loop
invariantτ CS
γ (T ) is equal to the adjoint torsion τγ(M) with respect to γ
τ CS
γ (T )
?
=τγ(M)∈F×/(±1). (21)
Given the above conjecture and the discussion of Section 1.2, it is natural to predict the
existence of a twisted version of the 1-loop invariant, deﬁned in terms of the twisted NZ
matrices. With the notation of Section 1.3, we deﬁne the twisted 1-loop invariant by
τ CS(T,t ) := det (A(t) diag(ζ) + B(t) diag(ζ′′))
∏N
j=1ζ
fj
j ζ
′f′
j
j ζ
′′f′′
j
j
:= det (G(t) diag(ζ) + G′(t) diag(ζ′) + G′′(t) diag(ζ′′))
∏N
j=1ζ
fj
j ζ
′f′
j
j ζ
′′f′′
j
j
∈F [t±1]/(±tZ )
(22)
where the second equality follows from the fact (analogous to Equation (8))
G(t) diag(ζ) + G′(t) diag(ζ′) + G′′(t) diag(ζ′′) = A(t) diag(ζ) + B(t) diag(ζ′′). (23)
An elementary observation is that τ CS(T,t ) is well-deﬁned up to multiplication by an
element in ±tZ . Indeed, the computation in [DG13, Sec.3.5] shows that up to sign, the
twisted 1-loop invariant is independent of the choice of a combinatorial ﬂattening. It also
manifestly independent of the choice of a quad type of ∆j, as the deﬁnition (22) is symmetric
with respect toζ,ζ′, andζ′′. Finally, a diﬀerent choice of lifts of the edges ofT results to left
multiplication of all of the matrices G□(t) by the same diagonal matrix diag(tc1,tc2,...,t cN )
for integers c1,c 2,...,c N, hence the observation follows.
By its very deﬁnition of τ CS(T,t ), it leads to a twisted version of Conjecture (21), namely
τ CS(T,t )
?
=τ(M,t )∈F [t±1]/(±tZ ). (24)
8 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
We now list some properties of the twisted 1-loop invariant. The ﬁrst concerns the topo-
logical invariance.
Theorem 1.5. τ CS(T,t ) is invariant under Pachner 2–3 moves between ideal triangulations
that support the geometric representation.
Combining the above theorem with Proposition 1.7 of [DG13], we conclude that the twisted
1-loop invariant deﬁnes a topological invariant of one-cusped hyperbolic 3-manifolds.
The next two theorems concern the properties (3) and (4) of the adjoint twisted Alexander
polynomial.
Theorem 1.6. For all n≥ 1 we have
τ CS(T (n),tn) =
∏
ωn=1
τ CS(T,ωt ). (25)
Theorem 1.7. We have τ CS(T, 1) = 0 and d
dt
⏐⏐
t=1τ CS(T,t ) =τ CS
λ (T ) whereλ is the periph-
eral curve satisfying α(λ) = 0.
A corollary of the above theorems is a relation between the twisted 1-loop invariant and
the 1-loop invariant of [DG13] for cyclic covers, namely
τ CS
µ (T (n))
τ CS
µ (T ) =
∏
ωn=1
ω⁄=1
τ CS(T,w ). (26)
The next result concerns the symmetries of the twisted 1-loop invariant. Conjecture 1.3
implies a symmetry of the twisted 1-loop invariant which is known to hold for the adjoint
twisted Alexander polynomial [Kit96, KL99], namely τ(M,t ) =τ(M, 1/t).
Corollary 1.8. (assuming Conjecture 1.3) We have
τ CS(T,t ) =τ CS(T, 1/t)∈F [t±1]/(±tZ ). (27)
We end our discussion on the twisted 1-loop invariant with a remark which suggests that
the t-deformation variable is independent from the variable m which is an eigenvalue of the
meridian of an SL 2(C )-representation of π1(M).
Remark 1.9. By varying the representation, the adjoint Reidemeister torsion can be ex-
tended to a rational function on the geometric component XM of the SL 2(C )-character
variety of a knot complement M [DG16], and consequently to a rational function of the
geometric component of the A-polynomial curve. The same holds for the 1-loop invariant;
see [DG13, Sec.4]. Likewise, we can extend the twisted 1-loop invariant to a twisted ra-
tional function on the geometric component of the character variety, i.e., to an element of
the ring C(XM)[t±1]/(±tZ ), where C(XM) is the ﬁeld of rational functions on XM. Then,
m∈C(XM) is a variable independent of t.
