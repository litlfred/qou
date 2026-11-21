---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-000-1-introduction
section_title: "§1 Introduction"
section_number: null
pages: 1-3
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
For f ∈L∞(R+) ∩L1(R+) consider the Bessel kernel
Bf(x, y) =
Z
R+
t√xyJν(xt)Jν(yt)f(t) dt,
(1.1)
where Jν is the Bessel function of order ν. Fix ν > −1. The kernel (1.1) induces
a bounded linear operator on L2(R+), which we will also denote by Bf. We let B1
be equal to the identity operator. We refer to Bf as the Bessel operator.
For any h ∈L∞(X) we also let h denote the operator of pointwise multiplication
by this function in L2(X). Let χA(x) be the characteristic function of the subset A.
In this work we consider the Fredholm determinant det(I + χ[0,R]Bfχ[0,R]) for
R > 0 and a sufficiently smooth function f. This determinant gives an exact expres-
sion for the Laplace transform of additive functionals in the determinantal point
process with Bessel kernel (see [26]). We describe the relation between the deter-
minantal point process and the operator in § 5. Briefly, the operator Bχ[0,1] induces
a probability measure PJν on countable subsets without accumulation points of R+.
These subsets, called configurations, are endowed with a certain σ-algebra (see [25]).
For any measurable function b on R+ an additive functional is defined as a measur-
able function on configurations by Sb(X) = P
x∈X b(x). The probability measure
This work was supported by Ministry of Science and Higher Education of the Russian Feder-
ation (grant no. 075-15-2024-529).
AMS 2020 Mathematics Subject Classification. Primary 47B35; Secondary 60G55.
c
○2024 Russian Academy of Sciences, Steklov Mathematical Institute of RAS
on configurations induces a random variable Sb. For b ∈L1(R+) ∩L∞(R+) the
Laplace transform of Sb is expressed by the formula
EJνeλSb = det(χ[0,1]Beλbχ[0,1]).
We consider the additive functionals SR
b = Sb(x/R). We have
det(χ[0,1]Beλb(x/R)χ[0,1]) = det(χ[0,R]Beλbχ[0,R]).
We conclude that the limit distribution of SR
b as R →∞can be derived in terms
of the asymptotic of the corresponding Fredholm determinant.
Recall an analogous problem for the sine process PS. Unlike the determinantal
point process with Bessel kernel, it is a measure on configurations on the real
line R. It is induced by the integral kernel KS(x, y) = (sin π(x −y))/(π(x −y)).
For b ∈L1(R) ∩L∞(R) the formula for the Laplace transform is in this case
ESeλSR
b = det(χ[0,2πR]Weλbχ[0,2πR]),
where Weλb is the Wiener–Hopf operator with symbol eλb, which we define in § 2.
For these determinants we recall two results. The first is the Kac–Akhiezer formula
(see [10], § 10.13), which states that under certain conditions on b we have
det(χ[0,2πR]Weλbχ[0,2πR]) = exp(λRcS
1 (b) + λ2cS
2 (b))QS
R(λb),
where QS
R(λb) →1 as R →∞; see Theorem 3 for the values of cS
1 (b) and cS
2 (b).
It follows that the distribution of additive functionals approaches here the Gaussian
distribution if cS
1 (b) = 0. The second result is a precise formula for the remain-
der term QS
R(λb); see Theorem 3 again. These results are continuous analogues
of the strong Szeg¨o limit theorem and the Borodin–Okounkov identity for Toeplitz
matrices (see [10], § 10.4, and [11], respectively). Borodin and Okounkov derived an
explicit expression for the determinants of Toeplitz matrices from Gessel’s theorem
and Schur measures. Several different proofs under less restrictive assertions were
given later [6], [9]. In a similar way a precise formula for the Wiener–Hopf operators
was obtained by Basor and Chen [2]. Under weaker assumptions about the symbol
this result was deduced by Bufetov [12] directly from the Borodin–Okounkov formula.
Having derived a formula for QS
R(λb), it is possible to estimate the rate of con-
vergence of additive functionals in the limit procedure under consideration. This
was done by Bufetov in [13], Lemma 3.10. Theorem 2 gives a similar estimate for
the Bessel kernel point process.
An analogue of the Kac–Akhiezer formula in case of the Bessel kernel was derived
by Basor and Ehrhardt [3]. We state it in Theorem 6. One consequence of Theo-
rem 6 is the rate at which the distribution of additive functionals approaches the
Gaussian one if cB
1 (b) = 0. In this paper we derive a precise expression for QB
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
