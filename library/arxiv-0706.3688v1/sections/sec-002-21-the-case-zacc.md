---
doc_id: arxiv-0706.3688v1
doc_title: "WHY THE STANDARD MODEL"
section_id: sec-002-21-the-case-zacc
section_title: "The case Z(AC)=C"
section_number: 2.1
pages: 4-6
source_pdf: 0706.3688.pdf
source_sha256: f2a18b0defebff66
toc_source: outline
doc_brief: "WHY THE STANDARD MODEL — The Standard Model is based on the gauge invariance principle with gauge group U(1) × SU(2) × SU(3) and suitable representations for fermions and bosons, which are begging"
---
We assume Z(AC) = C. Then (cf. [14]) there exists k ∈N such that AC = Mk(C) as
an involutive algebra over C. Moreover the algebra homomorphism
(2.6)
AC ⊗A0
C →L(H) , β(x ⊗y) = xy0 ,
∀x, y ∈AC ,
is injective since AC ⊗A0
C ∼Mk2(C) is a simple algebra.
Lemma 2.4. The representation β of AC ⊗A0
C in H of (2.6) is irreducible.
Proof. Since AC ⊗A0
C ∼Mk2(C), the representation β is a multiple of the unique
representation given by the left and right action of AC = Mk(C) on itself. We need
to show that the multiplicity m is equal to 1. We let e be a minimal projection of
AC = Mk(C), and let E = eJeJ−1. By construction E is a minimal projection of B =
AC ⊗A0
C ∼Mk2(C) and thus its range has dimension m. Moreover, by construction, E
commutes with J so that J restricts to an antilinear isometric involution of square 1 on
EH. Thus EH is the complexiﬁcation of a real Hilbert space and J the corresponding
complex conjugation. Hence the algebra of endomorphisms of EH which commute
with J is Mm(R) and3, if dim EH > 1, it contains a non-trivial idempotent F. For any
ξ ∈FH, η ∈(E −F)H and b ∈B one has
(2.7)
⟨b ξ, η⟩= 0
since, as E is a minimal projection of B one has EbE = λE for some λ ∈C, and
⟨b ξ, η⟩= ⟨EbE ξ, η⟩= 0. Thus BFH is a non-trivial subspace which is invariant under
B and J since JBJ−1 = B and J commutes with F. This contradicts the irreducibility
condition (2).
□
Proposition 2.5. Let H be a Hilbert space of dimension n. Then an irreducible solu-
tion with Z(AC) = C exists iﬀn = k2 is a square. It is given by AC = Mk(C) acting
by left multiplication on itself and antilinear involution
(2.8)
J(x) = x∗,
∀x ∈Mk(C) .
3This is the only place where we use the hypothesis J2 = 1.
WHY THE STANDARD MODEL
5
Proof. We have AC ⊗A0
C ∼Mk2(C) and by Lemma 2.4 the representation β in H is
irreducible. This shows that n = k2 is a square. The action of AC ⊗A0
C by left and
right multiplication on AC = Mk(C) (endowed with the Hilbert-Schmidt norm) is a
realization of the unique irreducible representation of AC ⊗A0
C ∼Mk2(C). In that
realization the canonical antiautomorphism
(2.9)
σ(a ⊗b0) = b ⊗a0
is implemented by the involution J0, J0(x) = x∗of (2.8) i.e. one has
σ(x) = J0 x∗J−1
0
,
∀x ∈AC ⊗A0
C .
Since the same property holds for the involution J of the given pair (A, J) once trans-
ported using the unitary equivalence of the representations, it follows that the ratio
J−1
0 J commutes with B and hence is a scalar λ ∈C of modulus one by irreducibility
of β. Adjusting the unitary equivalence by a square root µ of λ (using µJµ−1 = µ2J)
one can assume that J = J0 which gives the desired uniqueness.
□
This determines AC and its representation in (H, J) and it remains to list the various
possibilities for A. Now A is an involutive subalgebra of Mk(C) such that A + iA =
Mk(C). The center Z(A) is contained in Z(Mk(C)) = C. If Z(A) = C then i ∈A
and A = Mk(C). Otherwise one has Z(A) = R, A is a central simple algebra over R
(the simplicity follows from that of A + iA = Mk(C)) and A ∩iA = {0} (since this
is an ideal in A). Thus A is the ﬁxed point algebra of the antilinear automorphism α
of Mk(C) commuting with the ∗-operation, given by α(a + ib) = a −ib for a, b ∈A.
There exists (comparing α with complex conjugation) an antilinear isometry I of Ck
such that α(x) = IxI−1 for all x ∈Mk(C). One has α2 = 1 and thus I2 ∈{±1} (it is
a scalar λ ∈C of modulus one and commutes with I). Thus A is the commutant of I
and the only two cases are I2 = 1 which gives matrices Mk(R) over R and I2 = −1. In
the latter case the action of I turns Ck into a right vector space over the quaternions
H and k = 2a, A = Ma(H) is the algebra of endomorphisms of this vector space over
H. We can thus summarize the three possibilities
• A = Mk(C) (unitary case)
• A = Mk(R) (orthogonal case)
• A = Ma(H), for even k = 2a, (symplectic case)
while the representation is by left multiplication on Mk(C) and the antilinear involution
J is given by (2.8).
Remark 2.6. Note that in the case J2 = −1 the possibility of multiplicity m = 2 arises
and the dimension of H is 2k2 in that case.
We shall prove below in Lemma 3.1 that the above case Z(AC) = C is incompatible with
the commutation relation Jγ = −γJ for the grading and hence with the K-theoretic
dimension 6. Thus we now concentrate on the second possibility: Z(AC) = C ⊕C.
6
CHAMSEDDINE AND CONNES
