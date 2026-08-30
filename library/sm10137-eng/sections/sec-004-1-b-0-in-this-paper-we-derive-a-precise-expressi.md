---
doc_id: sm10137-eng
doc_title: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel "
section_id: sec-004-1-b-0-in-this-paper-we-derive-a-precise-expressi
section_title: "(b) = 0. In this paper we derive a precise expression for QB"
section_number: 1
pages: 2-4
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
doc_brief: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel S. M. Gorbunov — We"
---
R(λb)
and estimate the rate of its convergence to 1.
This result has two special cases when ν = ±1/2.
In these cases the Bessel
operator (1.1) is known to be the sum of the Wiener–Hopf and Hankel operators:
Bf = Wf ± Hf
for ν = ∓1
2,
where Hf is the Hankel integral operator with kernel χ[0,∞)2(x, y) bf(x+y). In these
cases an expression for QB
R(b) was derived by Basor, Ehrhardt and Widom [5].
Rate of convergence in the central limit theorem
1609
It is notable that in these cases Bf has a discrete analogue, a sum of a Toeplitz
and a Hankel matrix. An analogue of Szeg˝o’s theorem for such matrices was proved
by Johansson [18]. Furthermore, there is a counterpart of the Borodin–Okounkov
formula for these matrices, a precise formula derived by Basor and Ehrhardt [4].
Another proof of this precise formula, which is similar to that of Borodin and
Okounkov for Toeplitz matrices, was given by Betea [8], who used symplectic
and orthogonal Schur measures.
Lastly, recall some results on the rate of convergence of additive functionals for
matrix ensembles. For example, classical compact groups were studied by Johans-
son [18]. In [19] authors considered the traces of random Haar-distributed matri-
ces multiplied by deterministic ones.
Lambert, Ledoux and Webb [20] studied
the rate of convergence of additive functionals in β-ensembles. Gaussian Laguerre
and Jacobi ensembles were considered by Bufetov and Berezin [7], who used the
Deift–Zhou asymptotic analysis of the Riemann–Hilbert problem [14]. The authors
of [1] studied convergence in Wigner ensembles. However, all ensembles mentioned
above are finite-dimensional. On the other hand, the Bessel kernel point process
is a measure on infinite configurations. Therefore, we pursue the operator-theoretic
approach used in [2] and [3].
§ 2. Statement of the result
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
1610
S. M. Gorbunov
Set
P± = F−1χR±F
and
H±
1 (R) = P±(H1(R)).
Then H1(R) = H+
