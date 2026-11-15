---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic fields"
section_id: sec-009-b-gauge-invariance-of-the-third-order-invariant
section_title: "Gauge invariance of the third-order invariant $H^{(3)}$"
section_number: B
pages: 12-13
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magnetic ﬁelds is presented."
---
We now prove that the integral invariant (19) is unchanged under all gauge
transformations Ai →Ai′ = Ai + ∇φi for i = 1, 2, 3, which obey the following
two conditions: First we require
∇· Gi = ∇· Gi′ = 0,
(B.1)
where as before we deﬁne Gi = Aj × Ak and Gi′ = Aj′ × Ak′ for cyclic indices i, j, k.
Second, the gauge transformations must respect the boundary condition
Ai × n|∂V = Ai′ × n|∂V = 0,
(B.2)
where n is a normal vector to the boundary ∂V of the integration volume V .
It is easily checked that a general gauge transformation that leaves the condition
∇· Gi = 0 unchanged for i = 1, 2, 3 has to be a simultaneous gauge transformation of
all three ﬁelds. Substituting Ai + ∇φi for Ai our invariant of equation (19) changes
according to
H(3) →H(3)′ =
Z
V
(A1 + ∇φ1) · [(A2 + ∇φ2) × (A3 + ∇φ3)] d3x
(B.3)
=
Z
V
A1· (A2 × A3) d3x
+
Z
V

∇φ1· (A2 × A3) + ∇φ2· (A3 × A1) + ∇φ3· (A1 × A2)

d3x
+
Z
V

A1· (∇φ2 × ∇φ3) + A2· (∇φ3 × ∇φ1) + A3· (∇φ1 × ∇φ2)

d3x
+
Z
V
∇φ1· (∇φ2 × ∇φ3) d3x.
We have to show that for gauge transformations respecting equations (B.1) and (B.2),
H(3)′ = H(3), i.e. the sum of the last three integrals in equation (B.4) has to vanish.
We can rewrite the ﬁrst integral as
Z
V
∇φi · Gi d3x =
Z
∂V
φiGi · n d2x −
Z
V
φi(∇· Gi) d3x = 0,
which vanishes since Ai × n|∂V = 0 implies Gi · n|∂V = 0. To show that the second
integral vanishes we use the identities
∇φ2 × ∇φ3 = ∇× (φ2∇φ3) = −∇× (φ3∇φ2)
(B.4)
= 1
2∇× (φ2∇φ3 −φ3∇φ2)
(B.5)
and
∇· G1′ −∇· G1 = ∇φ3 · B2 −∇φ2 · B3,
Third-order topological invariant
13
as well as expressions obtained by cyclic permutations of the indices (1, 2, 3).
Substituting the ﬁrst identity into the second integral we obtain
Z
V
h
A1 · (1
2∇× (φ2∇φ3 −φ3∇φ2)) + (1, 2, 3) cyclic
i
d3x
= −1
2
Z
∂V
h
(A1 × (φ2∇φ3 −φ3∇φ2)) · n + (1, 2, 3) cyclic
i
d2x
+ 1
2
Z
V
h
(∇× A1) · (φ2∇φ3 −φ3∇φ2) + (1, 2, 3) cyclic
i
d3x
= + 1
2
Z
V
h
φ1(B3∇φ2 −B2∇φ3) + (1, 2, 3) cyclic
i
d3x
= −1
2
Z
V
h
φ1(∇· G1′ −∇· G1) + (1, 2, 3) cyclic
i
d3x
=
0.
The surface integral vanishes due to condition (B.2) and the last volume integral due
to condition (B.1). Finally we can see that the third integral vanishes by substituting
equation (B.5) for the term ∇φ2 × ∇φ3
Z
V
∇φ1 · (∇φ2 × ∇φ3) d3x = 1
2
Z
V
(∇φ1 · ∇× (φ2∇φ3 −φ3∇φ2)) d3x
= 1
2
Z
∂V
(φ2∇φ3 −φ3∇φ2) × ∇φ1 · n d2x
= 0.
In the last step we used that due to condition (B.2) the gradients ∇φ1, ∇φ2 and ∇φ3
have to be parallel to n. This completes the proof.
