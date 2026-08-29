---
doc_id: sm10137-eng
doc_title: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel "
section_id: sec-030-3-this-is-similar-to-the-first-part-and-follows
section_title: "This is similar to the first part and follows from the equality"
section_number: 3
pages: 11-12
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
doc_brief: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel S. M. Gorbunov — We"
---
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
1618
S. M. Gorbunov
§ 7. Proof of Lemma 3
In this section we establish Lemma 3. Our calculations follow Basor and Ehrhardt
(see [3], Lemmas 2.6–2.8). The section is structured as follows. In Propositions 4
and 5 and Corollary 1 we establish estimates for the trace norms of integral opera-
tors with kernels of certain form. Then we recall the necessary properties of Bessel
functions and their derivatives. We end the preparations to the proof by Lemma 5,
establishing some properties of the function spaces in question. The rest of the
section is devoted to the proof of Lemma 3 itself.
Proposition 4. Let K be an integral operator on L2[R, ∞) with kernel
K(x, y) =
Z
R+
a(t)h1(x, t)h2(y, t) dt,
where h1, h2 and a are some measurable functions. Then the estimate
∥K∥J1 ⩽
Z ∞
0
|a(t)|
Z ∞
R
|h1(x, t)|2 dx
1/2Z ∞
R
|h2(y, t)|2 dy
1/2
dt
(7.1)
holds, provided that the right-hand side is finite.
Proof. Let f, g ∈L2[R, ∞). Set ht
i(x) = hi(x, t), i = 1, 2. Then
⟨f, Kg⟩L2 =
Z ∞
R
Z ∞
R
Z ∞
0
a(t)h1(x, t)h2(y, t) dt

g(y) dyf ∗(x) dx
=
Z ∞
0
a(t)
Z ∞
R
h1(x, t)f ∗(x) dx
Z ∞
R
h2(y, t)g(y) dy

dt
=
Z ∞
0
a(t)⟨f, ht
1⟩L2⟨(ht
2)∗, g⟩L2 dt,
(7.2)
where Fubini’s theorem can be applied since the function under the integral is abso-
lutely integrable by the assumption that the right-hand side of (7.1) is finite. Recall
