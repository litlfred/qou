---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-005-6-wienerhopf-factorization-on-h-1mathbbr
section_title: "§6 Wiener–Hopf factorization on $H_1(\mathbb{R})$"
section_number: null
pages: 10-12
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
Recall that the Wiener–Hopf operator as a map W: f 7→Wf, L∞(R) →
B(L2(R+)) is not a Banach algebra homomorphism. But it can be restricted to
some subalgebras on which it preserves multiplication.
Recall that H1(R) is a Banach algebra. The spaces
H±
1 (R) = {f ∈H1(R): supp bf ⊂R±}
are Banach subalgebras since supp( bf ∗bg) ⊂supp bf + supp bg. The operators P± =
F−1χR±F map H1(R) into itself and P±H1(R) = H±
1 (R). Then W, as restricted
to H±
1 (R), is a Banach algebra homomorphism. As before, we consider H1(R+) to
be embedded in H1(R) by an even continuation, which defines a decomposition for
functions on R+.
We also let
H±
1 (R) ⊕C = {f + c: f ∈H±
1 (R), c ∈C}
be the Banach algebras H±
1 (R) with adjoined unit. Then for b ∈H±
1 ⊕C and an
entire function Φ = P∞
i=0 Φizi the element
Φ(b) =
∞
X
i=0
Φibi ∈H±
1 (R) ⊕C
is well defined.
Recall that for functions in the spaces under consideration the Wiener–Hopf
operators have kernels.
Lemma 4 ([3], Proposition 5.2). Let a be a function on R such that ∥a∥H1/2 +
∥ba∥L1 < ∞. Then F−1aF is an integral operator on L2(R) with kernel k(x, y) =
ba(x −y).
Proposition 3. 1. The map W

H±
1 (R) : f 7→Wf defines Banach algebra homo-
morphisms H±
1 (R) ⊕C →B(L2(R+)).
2. For b± ∈H±
1 (R) ⊕C we have
χ[0,R]Wb+ = χ[0,R]Wb+χ[0,R],
Wb+χ[R,∞) = χ[R,∞)Wb+χ[R,∞),
Wb−χ[0,R] = χ[0,R]Wb−χ[0,R],
χ[R,∞)Wb−= χ[R,∞)Wb−χ[R,∞).
3. For b± ∈H±
1 (R) ⊕C we have Wb−Wb+ = Wb−b+ .
In particular, Web± = exp(Wb±) and Web = exp(Wb−) exp(Wb+).
Proof. It is sufficient to prove the statements for b± ∈H±
1 (R). We give proofs
for H+
1 (R); the case of H−
1 (R) is proved similarly.
1. By Lemma 4 Wiener–Hopf operators have kernels. Let a and b be functions
in H+
1 (R). Since bb±(x) = χR±(x)bb±(x), we have
Wab(x, y) = χR2
+(x, y)
Z
R
ba(x −y −t)χR+(t)bb(t)χR±(t) dt
= χR2
+(x, y)
Z
R
ba(x −t)χR+(t −y)bb(t −y) dt
= χR2
+(x, y)
Z
R
ba(x −t)χR+(t)bb(t −y) dt = (WaWb)(x, y),
where the identity χR+(y)χR+(t −y) = χR+(y)χR+(t −y)χR+(t) has been used.
2. Since χ[0,R](x)χR+(x −y) = χ[0,R](x)χR+(x −y)χ[0,R](y) for all (x, y) ∈R+,
for the kernel of (χ[0,R]Wb+)(x, y) we can write
(χ[0,R]Wb+)(x, y) = χ[0,R](x)bb+(x −y)χR+(y)
= χ[0,R]2(x, y)bb+(x −y) = (χ[0,R]Wb+χ[0,R])(x, y).
The proof for Wb+χ[R,+∞) follows from the equality
χ[R,∞)(y)χR+(x −y)χR+(x) = χ[R,∞)(y)χR+(x −y)χ[R,∞)(x).
3. This is similar to the first part and follows from the equality
Wb−b+(x, y) = χR2
+(x, y)
Z
R
bb−(x −y −t)bb+(t)χR+(t) dt
after the substitution χR+(y)χR+(t −y) = χR+(y)χR+(t −y)χR+(t).
The proposition is proved.
Proof of Lemma 1. The properties of Fredholm determinants and the first and
second parts of Proposition 3 yield the following expression:
det(χ[0,R]Bebχ[0,R]) = det(χ[0,R]Web+We−b+BebWe−b−Web−χ[0,R])
= det(χ[0,R]We−b+BebWe−b−χ[0,R]) det(exp(χ[0,R]Wb−χ[0,R])
× exp(χ[0,R]Wb+χ[0,R])).
It remains to prove that
det(exp(χ[0,R]Wb−χ[0,R]) exp(χ[0,R]Wb+χ[0,R])) = exp(Rbb(0)).
(6.1)
By Theorem 4 the operator χ[0,R]Wbχ[0,R] is trace class for b ∈L1(R+) ∩L∞(R+),
so the left-hand side of (6.1) is equal to
det(exp(χ[0,R]Wb−χ[0,R]) exp(χ[0,R]Wb+χ[0,R]) exp(−χ[0,R]Wbχ[0,R]))
× exp(Tr(χ[0,R]Wbχ[0,R])),
where Tr(χ[0,R]Wbχ[0,R]) = Rbb(0) is calculated over the diagonal. A direct calcu-
lation shows that the operator χ[0,R]Wfχ[0,R] is Hilbert–Schmidt for f ∈H1(R+).
Hence the commutator [χ[0,R]Wb−χ[0,R], χ[0,R]Wb+χ[0,R]] is trace class, and its trace
is zero. Theorem 5 gives
det(exp(χ[0,R]Wb−χ[0,R]) exp(χ[0,R]Wb+χ[0,R]) exp(−χ[0,R]Wbχ[0,R])) = 1.
This finishes the proof of (6.1). Lemma 1 is proved.
