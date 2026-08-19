---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-009-43-the-haar-functional
section_title: "The Haar functional"
section_number: 4.3
pages: 27-28
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Recall from Deﬁnition 2.8 that a linear functional on A is called a left invariant
Haar functional if it satisﬁes
(1⊗h)(∆ x) = h(x)· 1M(A), (4.23)
and a right invariant Haar functional if it satisﬁes
(h⊗ 1)(∆ x) = h(x)· 1M(A), (4.24)
where 1 M(A) is the unital element in the multiplier algebra M (A).
Theorem 4.7. There exists a left invariant Haar functional on A, given by
h
( ∫
R+i0
∫
R
f (s,t )Aib−1sBib−1tdsdt
)
=f (0,iQ ). (4.25)
Proof. From Proposition 4.4, the coproduct is given by
∆
( ∫
R+i0
∫
R
f (s,t )Aib−1sBib−1tdsdt
)
=
∫
R+i0
∫
R
∫
C
f (s,t )Gb(−iτ )Gb(iτ−it)
Gb(−it) Aib−1sBib−1(t−τ )⊗Aib−1(s+t−τ )Bib−1τdτdsdt
=
∫
R
∫
R−i0
∫
C
f (s,t +τ−s)Gb(−iτ )Gb(is−it)
Gb(is−it−iτ ) Aib−1sBib−1(t−s)⊗Aib−1tBib−1τdτdsdt.
In the last step, we push the contour of t back to the real line, and the contour of
τ to be the real line that goes above the pole at τ = 0 only. This will force the
contour of s to move below the pole at s =t.
27
Now as a function of τ the integrand is well-deﬁned for 0 <Im (τ )<Q . There-
fore to apply the Haar functional, we take the analytic continuation to τ = iQ
by
τ = lim
ǫ− →0
iQ−iǫ.
Using Corollary 3.11, we have
= lim
ǫ− →0
∫
R−i0
f (s,iQ−s−iǫ)Gb(Q−ǫ)Gb(is)
Gb(Q +is−ǫ) Aib−1sBib−1(−s)ds
= f (0,iQ )
as desired.
Using exactly the same technique, we can derive the counit for A:
Corollary 4.8. The counit is given by
ǫ(f ) = lim
t− →0
Gb(Q +it)
∫
R
f (s,t )ds (4.26)
and satisﬁes
(1⊗ǫ)∆ = Id A = (ǫ⊗ 1)∆ . (4.27)
