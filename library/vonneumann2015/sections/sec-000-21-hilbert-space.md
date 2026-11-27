---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-000-21-hilbert-space
section_title: "Hilbert Space"
section_number: 2.1
pages: 5-8
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Hilbert Space
A Hilbert Space is a complex vector space H with inner product ⟨, ⟩: HxH →
C which is linear in the ﬁrst variable, satisﬁes ⟨ξ, η⟩= ⟨η, ξ⟩, is positive
deﬁnite, i.e. ⟨ξ, ξ⟩> 0 for ξ̸ = 0, and is complete for the norm deﬁned by
test
||ξ|| =
p
⟨ξ, ξ⟩.
Exercise 2.1.1. Prove the parallelogram identity :
||ξ −η||2 + ||ξ + η||2 = 2(||ξ||2 + ||η||2)
and the Cauchy-Schwartz inequality:
|⟨ξ, η⟩| ≤||ξ|| ||η||.
Theorem 2.1.2. If C is a closed convex subset of H and ξ is any vector in
H, there is a unique η ∈C which minimizes the distance from ξ to C, i.e.
||ξ −η′|| ≤||ξ −η||
∀η′ ∈C.
Proof. This is basically a result in plane geometry.
Uniqueness is clear—if two vectors η and η′ in C minimized the distance
to ξ, then ξ, η and η′ lie in a (real) plane so any vector on the line segment
between η and η′ would be strictly closer to ξ.
To prove existence, let d be the distance from C to ξ and choose a sequence
ηn ∈C with ||ηn −ξ|| < d + 1/2n. For each n, the vectors ξ, ηn and ηn+1
deﬁne a plane. Geometrically it is clear that, if ηn and ηn+1 were not close,
some point on the line segment between them would be closer than d to ξ.
Formally, use the parallelogram identity:
||ξ −ηn + ηn+1
2
||2 = ||ξ −ηn
2
+ ξ −ηn+1
2
||2
5
= 2(||ξ −ηn
2
||2 + ||ξ −ηn+1
2
||2 −1/8||ηn −ηn+1||2)
≤(d + 1/2n)2 −1/4||ηn −ηn+1||2
Thus there is a constant K such that ||ηn −ηn+1||2 < K/2n or ||ξ −ηn+ηn+1
2
||2
would be less than d2.
Thus (ηn) is Cauchy, its limit is in C and has distance d from ξ.
Exercise 2.1.3. If φ ∈H∗(the Banach-space dual of H consisting of all
continuous linear functionals from H to C), kerφ is a closed convex subset
of H. Show how to choose a vector ξφ orthogonal to ker φ with φ(η) = ⟨ξφ, η⟩
and so that φ 7→ξφ is a conjugate-linear isomorphism from H∗onto H.
We will be especially concerned with separable Hilbert Spaces where there
is an orthonormal basis, i.e. a sequence {ξ1, ξ2, ξ3, ...} of unit vectors with
⟨ξi, ξj⟩= 0 for i̸ = j and such that 0 is the only element of H orthogonal to
all the ξi.
We will use the abbreviation ONB for orthonormal basis.
Exercise 2.1.4. Show that an ONB always exists (e.g. Gram-Schmidt) and
that if {ξi} is an ONB for H then the linear span of the {ξi} is dense in H.
A trivial but useful observation.
If H and K are Hilbert spaces with
vectors ξi ∈H and ψk ∈K respectively then if
⟨ξi, ξj⟩= ⟨ψi, ψj⟩
∀i, j
then the map ξi 7→ψi extends to a linear ⟨, ⟩-preserving bijection from the
closure of the subspace spanned by the ξi to the closure of the subspace
spanned by the ψi.
A linear map (operator) a : H →K is said to be bounded if there is a
number K with ||aξ|| ≤K||ξ||
∀ξ ∈H. The inﬁmum of all such K is called
the norm of a, written ||a||. The set of all bounded operators from H to K
is written B(H, K) and if H = K we use B(H). Boundedness of an operator
is equivalent to continuity.
To every bounded operator a between Hilbert spaces H and K, by exercise
2.1.3 there is another, a∗, between K and H, called the adjoint of a which is
deﬁned by the formula ⟨aξ, η⟩= ⟨ξ, a∗η⟩.
Exercise 2.1.5. Prove that
||a|| =
sup
||ξ|| ≤1, ||η|| ≤1|⟨aξ, η⟩|
= ||a∗|| = ||a∗a||1/2.
6
Some deﬁnitions:
The identity map on H is a bounded operator denoted 1.
An operator a ∈B(H) is called self-adjoint if a = a∗.
An operator p ∈B(H) is called a projection if p = p2 = p∗.
An operator a ∈B(H) is called positive if ⟨aξ, ξ⟩≥0
∀ξ ∈B(H). We say
a ≥b if a −b is positive.
An operator u ∈B(H) is called an isometry if u∗u = 1.
An operator v ∈B(H) is called a unitary if uu∗= u∗u = 1.
An operator u ∈B(H) is called a partial isometry if u∗u is a projection.
The last three deﬁnitions extend to bounded linear operators between dif-
ferent Hilbert spaces.
If S ⊆B(H) then the commutant S′ of S is {x ∈B(H)|xa = ax
∀a ∈S}.
Also S′′ = (S′)′.
Exercise 2.1.6. A word on matrices.
If ei is an ONB of H then ei 7→ξi
(the characteristic function of {i}) deﬁnes a unitary from H to ℓ2(N). So for
any ξ ∈H,
ξ =
∞
X
i=1
⟨ξ, ei⟩ei
the sum being convergent in the norm of H.
If a ∈B(H) we deﬁne the matrix of a wrt the ONB to be ai,j = ⟨aei, ej⟩.
For ﬁxed i, j 7→ai,j is in ℓ2 and for ﬁxed j, i 7→ai,j is in ℓ2. And a(ei) =
P
j ai,jej. Thus the matrix of a determines a and if b ∈B(H) has matrix bi,j
then
abi,j =
X
k
ai,kbk,j
the sum being absolutely convergent.
Exercise 2.1.7. Show that every a ∈B(H) is a linear combination of two
self-adjoint operators.
Exercise 2.1.8. A positive operator is self-adjoint.
Exercise 2.1.9. Find an isometry from one Hilbert space to itself that is
not unitary. (The unilateral shift on H = ℓ2(N) is a ﬁne example. There is
an obvious orthonormal basis of H indexed by the natural numbers and the
shift just sends the nth. basis element to the (n + 1)th.)
Exercise 2.1.10. If K is a closed subspace of H show that the map PK :
H →K which assigns to any point in H the nearest point in K is linear and
a projection.
7
Exercise 2.1.11. Show that the correspondence K →PK of the previous
exercise is a bijection between closed subspaces of H and projections in B(H).
If S is a subset of H, S⊥is by deﬁnition {ξ ∈H : ⟨ξ, η⟩= 0
∀η ∈S}.
Note that S⊥is always a closed subspace.
Exercise 2.1.12. If K is a closed subspace then K⊥⊥= K and PK⊥= 1−PK.
Exercise 2.1.13. If u is a partial isometry then so is u∗. The subspace u∗H
is then closed and called the initial domain of u, the subspace uH is also
closed and called the ﬁnal domain of u. Show that a partial isometry is the
composition of the projection onto its initial domain and a unitary between
the initial and ﬁnal domains.
The commutator [a, b] of two elements of B(H) is the operator ab −ba.
Exercise 2.1.14. If K is a closed subspace and a = a∗then
aK ⊆K
iff
[a, PK] = 0.
In general (aK ⊆K
and
a∗K ⊆K) ⇐⇒[a, PK] = 0.
