---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-001-2-statement-of-the-result
section_title: "§2 Statement of the result"
section_number: null
pages: 3-5
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
For a function f ∈L1(R) ∩L∞(R) we define its Fourier transform by
bf(λ) = 1
2π
Z
R
e−iλxf(x) dx.
Here and below, if f is defined on R+, then we extend it to an even function.
In this case the Fourier transform coincides with the cosine transform. Recall that
the Sobolev p-seminorm of a function f on R+ is
∥f∥2
˙Hp =
Z
R+
| bf(λ)|2|λ|2p dλ.
For an integer p we have ∥f∥˙Hp = (2π)−1/2∥f (p)∥L2(R+) by Parseval’s theorem. We
set ∥f∥Hp = ∥f∥L2(R+)+∥f∥˙Hp and define the Sobolev space Hp(R+)={f ∈L2(R+):
∥f∥Hp <+∞} to be a Banach space with the norm ∥· ∥Hp. The Sobolev space Hp(R)
on the real line is defined similarly, and we keep the same notation for the norm.
We define the following seminorm of a function f on R+:
∥f∥˙B = ∥f∥˙H1 + ∥f∥˙H3 + ∥xf(x)∥˙H2 + ∥x2f(x)∥˙H3.
Again, set ∥f∥B = ∥f∥L1(R+) + ∥f∥L2(R+) + ∥xf ′(x)∥L∞(R+) + ∥f∥˙B and consider
the space
B = {f ∈L2(R+): ∥f∥B < +∞}
to be a Banach space with the norm ∥· ∥B.
For a function f ∈L∞(R) the Wiener–Hopf operator on L2(R+) is defined by
Wf = χR+F−1fFχR+,
where F is the unitary Fourier transform on L2(R): Fh =
√
2π bh, h ∈L2(R).
Again, if f is defined on R+, then we extend it to an even function.
Set
P± = F−1χR±F
and
H±
1 (R) = P±(H1(R)).
Then H1(R) = H+
1 (R) ⊕H−
1 (R).
For any function b ∈H1(R) let b± = P±b;
b = b+ + b−. The above space B is clearly a subspace of H1(R) with embedding
given by even continuation, so the decomposition is well defined on B, although the
components can fail to remain in B. We refer to this decomposition as Wiener–Hopf
factorization.
Our main result is then stated as follows.
Theorem 1. Let b ∈B. Then for any R > 0
det(χ[0,R]Bebχ[0,R]) = exp(RcB
1 (b) + cB
2 (b) + cB
3 (b))QB
R(b),
(2.1)
where
cB
1 (b) = bb(0),
cB
2 (b) = −ν
2 b(0),
cB
3 (b) = 1
2
Z
R+
x(bb(x))2 dx
and
QB
R(b) = det(χ[R,∞)Web−Be−bWeb+χ[R,∞)).
There exists a positive constant C such that for any R ⩾1 and b ∈B the following
estimate holds
|QB
R(b) −1| ⩽Ce4∥b+∥L∞
√
R
L(b) exp
Ce4∥b+∥L∞
√
R
L(b)

,
(2.2)
where
L(b) = (1 + ∥xb′(x)∥2
L∞+ ∥b∥2
˙B)∥b∥˙B.
Remark 1. Again, we mention the cases ν = ±1/2. Substituting Bb = Wb ∓Hb
into the formula for QB
R(b) we obtain
QB
R(b) = det(I ∓χ[R,∞)Heb−−b+χ[R,∞)).
(2.3)
We have used the following facts:
We−b = We−b−We−b+,
Web± = eWb±
and
Web−He−b+Web+ = Heb−−b+.
(For the first two identities, see § 6. For the last one, see [5], § II.) Indeed, the expres-
sion (2.3) for the remainder coincides with the one obtained by Basor, Ehrhardt
and Widom in [5], formula (3).
We now proceed to a corollary for the determinantal point process with Bessel
kernel PJν (see § 5).
Let SR
f
= SR
f −EJνSR
f .
We denote by FR,f and FN the
cumulative distribution functions of SR
f and the standard Gaussian, respectively.
Theorem 2. Let b ∈B be a real-valued function, satisfying cB
3 (b) = 1/2. Then
there exists a constant C = C(L(b), ∥b+∥L∞) providing the following estimate for
the Kolmogorov–Smirnov distance for any R ⩾1
sup
x |FR,b(x) −FN (x)| ⩽
C
log R.
(2.4)
