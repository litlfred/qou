---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-25
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
---
Sbornik: Mathematics
215:12 1607–1632
Matematicheski˘ı Sbornik
215:12 30–55
DOI: https://doi.org/10.4213/sm10137e
Rate of convergence in the central limit theorem
for the determinantal point process with Bessel kernel
S. M. Gorbunov
Abstract. We consider a family of linear operators diagonalized by the
Hankel transform.
We express explicitly the Fredholm determinants of
these operators, as restricted to L2[0, R], so that the rate of their conver-
gence as R →∞can be found. We use the link between these determinants
and the distribution of additive functionals in a determinantal point process
with Bessel kernel and estimate the distance in the Kolmogorov–Smirnov
metric between the distribution of these functionals and the Gaussian dis-
tribution.
Bibliography: 27 titles.
Keywords: Bessel kernel, Wiener–Hopf operators, Fredholm determi-
nants, additive functionals.
§ 1. Introduction
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
1608
S. M. Gorbunov
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
Rate of convergence in the central limit theorem
1611
§ 3. Structure of the paper
First recall the result of Basor and Chen and the main steps of its proof.
Theorem 3. For f ∈H1(R) ∩L1(R) we have
det(χ[0,R]Wef χ[0,R]) = exp(RcS
1 (f) + cS
2 (f))QS
R(f),
where
cS
1 (f) = bf(0),
cS
2 (f) = 1
2
Z
R+
x bf(x) bf(−x) dx
and
QS
R(f) = det(χ[R,∞)Wef−We−f+We−f−Wef+χ[R,∞)).
Remark 2. We state Theorem 3 under assumptions different from [2] to outline
clearer the proof of Theorem 1.
The proof consists of three main steps.
Step 1. The properties of Wiener–Hopf factorization give the following identity:
det(χ[0,R]Wef χ[0,R]) = exp(RcS
1 (f)) det(χ[0,R]We−f+Wef We−f−χ[0,R]).
(3.1)
Step 2. It is shown below that the operator We−f+Wef We−f−−I is trace class.
We can apply the Jacobi–Dodgson identity det(PAP) = det(A) det(QA−1Q) for
orthogonal projections P and Q satisfying P + Q = I and a determinant-class
invertible operator A. Then we have
det(χ[0,R]We−f+Wef We−f−χ[0,R])
det(χ[R,∞)Wef−We−f+We−f−Wef+χ[R,∞)) = det(We−f+Wef We−f−),
(3.2)
where W −1
ef = We−f+We−f−, as follows from the properties of Wiener–Hopf factor-
ization.
Step 3. From the properties of the Fredholm determinant and Wiener–Hopf
factorization we obtain det(We−f+Wef We−f−) = det(Wef−Wef+We−f−We−f+).
Widom’s formula (see [27]) states that determinant on the right is well defined and
its value is
det(Wef−Wef+We−f−We−f+) = exp(cS
2 (f)).
(3.3)
This finishes the proof.
We now pass to the proof of Theorem 1.
Lemma 1. For b ∈H1(R+) ∩L1(R+) we have
det(χ[0,R]Bebχ[0,R]) = exp(RcB
1 (b)) det(χ[0,R]We−b+BebWe−b−χ[0,R]).
(3.4)
By contrast to the proof of Theorem 3, it is not known if We−b+BebWe−b−−I
is trace class, so the Jacobi–Dodgson identity cannot be applied directly. However,
one can observe that equality (3.2) means that the ratio of the determinants in
the left-hand side does not depend on R.
In our case we can use an analogue
of the Jacobi–Dodgson identity (Corollary 2) to show the independence of this
ratio of R.
1612
S. M. Gorbunov
Lemma 2. Let b ∈H1(R+) ∩L1(R+), and let χ[R,∞)(Be−b −We−b)χ[R,∞) be
a trace-class operator for each R > 0. Then there exists Z(b) such that for all
R > 0 we have
det(χ[0,R]We−b+BebWe−b−χ[0,R])
det(χ[R,∞)Web−Be−bWeb+χ[R,∞)) = Z(b).
(3.5)
Observe that the denominator in (3.5) equals QB
R(b). The central step in the
proof of Theorem 1 is as follows.
Lemma 3. For b ∈L1(R+)∩L∞(R+) such that ∥b∥˙B < ∞and z ∈C the operator
χ[R,∞)(Bb+z −Wb+z)χ[R,∞) is trace class for any R > 0. There exists a constant C
such that for any R ⩾1, z ∈C and b satisfying the conditions above we have
∥χ[R,∞)(Bb+z −Wb+z)χ[R,∞)∥J1 ⩽
C
√
R
∥b∥˙B.
(3.6)
The operator QB
R(b) is related to the operator in Lemma 3 by formula (8.5)
below. This allows us to obtain estimate (2.2). Further, the asymptotic for the
numerator in (3.5) follows from Lemma 1 and an asymptotic result of Basor and
Ehrhardt (see Theorem 6). This proves that Z(b) = exp(cB
2 (b) + cB
3 (b)).
The rest of the paper has the following structure. In § 4 we recall some facts and
notation for trace-class and Hilbert–Schmidt operators. Then in § 5 we explain the
relation between the Fredholm determinant in Theorem 1 and the determinantal
point process with Bessel kernel. In § 6 we establish some properties of Wiener–Hopf
factorization and deduce Lemma 1.
Section 7 presents the proof of Lemma 3.
We complete the proof of Theorems 1 and 2 in § 8.
§ 4. Trace class and Hilbert–Schmidt operators
Here and below we denote the ideals of trace-class and Hilbert–Schmidt operators
by J1 and J2, respectively. For more details of the theory, we refer the reader to [24]
and [22]. We let E denote R or R+ = [0, ∞).
Definition 1. The operator K on L2(E) is locally trace class if for each bounded
measurable subset B of E the operator χBKχB is trace class. Let J loc
1
(L2(E))
denote the space of locally trace-class operators.
Recall that for K ∈J1 the Fredholm determinant det(I + K) is well defined,
which is equal to a product, det(I + K) = Q
λ∈σ(K)(1 + λ), by Lidskii’s theorem.
It is continuous with respect to the trace norm. We also define the regularized
determinant by
det 2(I + K) = exp(−Tr(K)) det(I + K).
It is continuous with respect to the Hilbert–Schmidt norm, so it can extended by
continuity to all operators in J2.
The following theorem implies that for a function f ∈L1(R+) ∩L∞(R+) the
determinants det(I + χ[0,R]Bfχ[0,R]) and det(I + χ[0,R]Wfχ[0,R]) are well defined.
Rate of convergence in the central limit theorem
1613
Theorem 4 ([22], Theorem 3.11.9). Let K be a continuous kernel on [a, b]2 induc-
ing a positive self-adjoint operator K on L2[a, b]. Then the operator K is trace
class. In addition, for any trace-class K with continuous kernel we have
Tr(K) =
Z b
a
K(x, x) dx.
(4.1)
We refer to (4.1) as the calculation of the trace over the diagonal.
Recall that the kernel of an integral operator is defined almost everywhere
on [a, b]2.
Thus, for an operator satisfying the assumptions of Theorem 4, for-
mula (4.1) can fail to hold after we change the kernel on the diagonal, although the
induced operator remains the same. This explains the assumption of continuity.
Let us now extend the class of kernels for which we can calculate the trace over the
diagonal.
Let K be a self-adjoint trace-class operator. By the Hilbert–Schmidt theorem
we have a spectral decomposition, so that its kernel can be chosen in the form
K(x, y) =
X
i∈N
λiϕi(x)ϕ∗
i (y),
(4.2)
where {ϕi}i∈N forms an orthonormal basis. Now, by definition the trace is
Tr(K) =
Z b
a
X
i∈N
λiϕi(x)ϕ∗
i (x) dx,
which is equal to
Z b
a
K(x, x) dx if we choose K as in (4.2). Observe that this does
not require the kernel to be continuous, but this choice is better defined: we can
only change K on subsets of [a, b]2 having projections with zero measure. Choosing
similarly the kernel of an operator fK:
(fK)(x, y) =
X
i∈N
λi(f(x)ϕi(x))ϕ∗
i (y),
we see that then Tr(fK) =
Z b
a
f(x)K(x, x) dx in a similar way.
We use these
observations in § 5.
We will also use the following theorem.
Theorem 5 ([15], Theorem 2.2). For A, B ∈B(H) such that [A, B] ∈J1 we have
eAeBe−A−B −I ∈J1. For the Fredholm determinant we have
ln det(eAeBe−A−B) = 1
2 Tr([A, B]).
(4.3)
§ 5. A link between the Bessel operator
and the determinantal point process with Bessel kernel
Let E be R or R+ = [0, ∞). Recall that a configuration on E is a discrete subset
of E. We denote the set of configurations by Conf(E). It can be endowed with
a σ-algebra of measurable subsets X (for instance, see [25]). A point process P is
defined to be a probability measure on (Conf(E), X).
1614
S. M. Gorbunov
For a measurable function f : E →C we define two measurable functions on
configurations by the following formulae:
Sf(X) =
X
x∈X
f(x)
and
Ψ1+f(X) =
Y
x∈X
(1 + f(x));
they are called additive and multiplicative functionals, respectively.
Definition 2. A point process PK on Conf(E) is determinantal if there exists an
operator K ∈J loc
1
(L2(E)) satisfying the following condition: for any bounded
measurable function f with compact support B = supp f
EKΨ1+f = det(I + fKχB).
(5.1)
We consider the limit distribution of SR
f = Sf(x/R) as R →∞for the determinan-
tal point process with Bessel kernel PJν on R+ [26] induced by the operator Bχ[0,1].
Theorem 3 describes the limit under consideration for the sine process PS on R
induced by the operator F−1χ[−π,π]F on L2(R). To be precise, we formulate the
following statement.
Proposition 1. For f ∈L1(E) ∩L∞(E) we have
EJνΨR
1+f = det(I + χ[0,R]Bfχ[0,R])
(5.2)
and
ESΨR
1+f = det(I + χ[0,2πR]Wfχ[0,2πR]).
(5.3)
The Laplace transform of additive functionals is expressed in terms of multi-
plicative functionals by the formula
EeλSR
b = EΨR
eλb.
By Proposition 1 it is equal to the Fredholm determinant det(χ[0,R]Beλbχ[0,R])
for PJν and to det(χ[0,2πR]Weλbχ[0,2πR]) for the sine process.
To prove Proposition 1 we follow Bufetov (see [13], § 2.9). We extend the class of
functions for which (5.1) holds. Let K be a Hilbert–Schmidt self-adjoint operator
on L2(E).
We choose its kernel K to coincide with its spectral decomposition
(see § 4). We set
det(I + K) = exp
Z
E
K(x, x) dx

det 2(I + K)
(5.4)
if the integral of the diagonal exists. Observe, that this definition does not require
K to be trace class.
However, if it is trace class, then we obtain the ordinary
Fredholm determinant.
Let Π ∈J loc
1
(L2(E)) be an orthogonal projection. By the Macchi–Soshnikov
theorem (see [21] and [25]) Π defines a point process PΠ. We choose the kernel
Π(x, y) to coincide with the spectral decomposition of χBΠχB for every compact
subset B of E. Consider the measure dµΠ(x) = Π(x, x) dx on E.
Rate of convergence in the central limit theorem
1615
Proposition 2. If f ∈L1(E, dµΠ) ∩L∞(E, dµΠ), then Ψ1+f ∈L1(Conf(E), PΠ)
and
EΠΨ1+f = det(I + fΠ).
(5.5)
In other words, multiplicative functionals define a continuous mapping
Ψ1+(−) : L∞(E, dµΠ) ∩L1(E, dµΠ) →L1(Conf(E), PΠ).
Proof. The formula holds for f ∈L∞(E) with compact support The exponential
of the integral of the diagonal in (5.4) is continuous with respect to the norm
in L1(E, dµΠ).
The regularized determinant is continuous with respect to the
Hilbert–Schmidt norm, which is equal to
∥fΠ∥2
J2 =
Z
E
|f(x)Π(x, y)|2 dx dy =
Z
E
|f(x)|2Π(x, y)Π(y, x) dx dy
=
Z
E
|f(x)|2 dµΠ(x),
and therefore it is continuous with respect to the L2(E, dµΠ)-norm. Thus, multi-
plicative functionals define a continuous mapping of a dense subset of L1(E, dµΠ)∩
L∞(E, dµΠ) and therefore of the whole space. This extension coincides by con-
tinuity with the expectation of the multiplicative functionals by Beppo Levi’s
theorem, since one can approximate any multiplicative functional Ψ1+|f|, f ∈
L1(E, dµΠ)∩L∞(E, dµΠ) by the functionals Ψ1+|fn|, |fn| = χ[−n,n]|f|. Hence (5.5)
is an extension of (5.1) by continuity. The proposition is proved.
Proof of Proposition 1. The proof for the sine process case can be found in [13],
Lemma 3.3. We proceed differently by proving the equality between the extended
determinants of I +fF−1χ[−π,π]F and I +fBχ[0,1] and the Fredholm determinants
of I + χ[0,2π]Wfχ[0,2π] and I + χ[0,1]Bfχ[0,1], respectively. Note that by Theorem 4
we can take the kernel of Bχ[0,1] to be equal to (1.1), and the kernel of F−1χ[−π,π]F
to be sin(π(x −y))/(π(x −y)). It is straightforward to see in both cases that the
integrals over the diagonals of the kernels coincide.
Now we show that the regularized determinants coincide. This is a consequence of
unitary invariance. Recall that Bχ[0,1] is unitarily equivalent to χ[0,1] via the Hankel
transform Hν (see § 8 and formula (8.4)). Then we have the unitary equivalence
fHνχ[0,1]Hν ∼HνfHνχ[0,1],
where the last operator has the same regularized determinant as χ[0,1]Bfχ[0,1].
Notably, the operator obtained is trace class and its Fredholm determinant is well
defined.
We turn to the proof for the sine kernel.
We use the translation operator
Ttf(x) = f(x + t) to proceed as follows:
F∗χ[−π,π]Ff = FT−πχ[0,2π]TπF∗f = e−iπxFχ[0,2π]F∗feiπx ∼Fχ[0,2π]F∗f.
Now the Fourier transform gives the following unitary equivalence:
Fχ[0,2π]F∗f ∼χ[0,2π]F∗fF,
where the determinant of the obtained operator coincides, as above, with the one
for χ[0,2π]Wfχ[0,2π]. Again, χ[0,2π]Wfχ[0,2π] is trace class.
1616
S. M. Gorbunov
In both cases conjugation by the unitary operator URf(x) = R−1/2f(x/R) com-
pletes the proof.
The proposition is proved.
§ 6. Wiener–Hopf factorization on H1(R)
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
Rate of convergence in the central limit theorem
1617
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
that B(L2[R, ∞)) ≃J ∗
1 (L2[R, ∞)), where A ∈B(L2[R, ∞) acts on J ∗
1 (L2[R, ∞))
by the rule X 7→Tr(AX). For the norm of K, considering it as a functional on
B(L2[R, ∞)) and using the definition of a trace and the expression (7.2), we have
∥K∥J1 =
sup
B∈B(L2),∥B∥=1
|Tr(BK)|
=
sup
B∈B(L2),∥B∥=1

X
i∈N
Z ∞
0
a(t)⟨fi, Bht
1⟩L2⟨(ht
2)∗, fi⟩L2 dt

,
where {fi}i∈N is an arbitrary orthonormal basis in L2[R, ∞).
Next we use the
Cauchy–Bunyakovsky–Schwarz inequality to obtain
X
i∈N
|⟨fi, Bht
1⟩L2⟨(ht
2)∗, fi⟩L2|
⩽
X
i∈N
|⟨fi, Bht
1⟩L2|2
1/2X
i∈N
|⟨(ht
2)∗, fi⟩L2|2
1/2
⩽∥ht
1∥L2 ∥ht
2∥L2,
which finishes the proof.
Rate of convergence in the central limit theorem
1619
Proposition 5. Let the kernel K(x, y) of an integral operator K be absolutely con-
tinuous with respect to y on [a, b]. Assume that K = Kχ[a,b]. Consider the operator
∂yK with kernel ∂K(x, y)/∂y and assume that ∂yK ∈J2. Then
∥K∥J1 ⩽∥K∥+ (b −a)
√
2
∥∂yK∥J2.
(7.3)
Proof. Let Pf(x) = (1/(b −a))χ[a,b](x)⟨χ[a,b], f⟩L2 be a one-dimensional projector
onto χ[a,b], and let Q = χ[a,b] −P. We decompose the operator: K = KP + KQ.
The operator KP is also a one-dimensional projector with trace norm of at most
∥KP∥J1 ⩽∥K∥∥P∥J1 = ∥K∥.
Recall that the Volterra operator V on L2([a, b]) is defined by the formula
V f(x) =
Z x
a
f(t) dt.
It is a Hilbert–Schmidt operator with kernel V (x, y) =
χ[a,x](y), and its Hilbert–Schmidt norm is
∥V ∥2
J2 =
Z b
a
dx
Z x
a
dy = (b −a)2
2
.
Integrating KQ by parts we obtain
Z b
a
K(x, y)Qf(y) dy =
Z b
a
K(x, y) d(V Qf(y)) = K(x, y)V Qf(y)

b
a −∂yKV Qf,
where
V Qf(a) = 0
and
V Qf(b) = ⟨χ[a,b], Qf⟩L2 = 0
by the definition of V and Q.
The inequality ∥∂yKV Q∥J1 ⩽∥∂yK∥J2 ∥V ∥J2
finishes the proof.
Corollary 1. There exists a constant C such that for any kernel K of an integral
operator on L2(R+) with the estimates
|K(x, y)| ⩽
A
(x + y)2
and
|∂yK(x, y)| ⩽
A
(x + y)2 ,
x, y > 0,
for some constant A, for any R > 0 we have
∥χ[R,∞)Kχ[R,∞)∥J1 ⩽AC
 1
R +
1
√
R

.
(7.4)
Proof. By Proposition 5 we have
∥χ[R,∞)Kχ[R,∞)∥J1 ⩽
∞
X
l=0
∥χ[R,∞)Kχ[R+l,R+l+1]∥J1
⩽
∞
X
l=0
(∥χ[R,∞)Kχ[R+l,R+l+1]∥J2 + ∥χ[R,∞)∂yKχ[R+l,R+l+1]∥J2),
1620
S. M. Gorbunov
where for each term we have by assumption
∥χ[R,∞)Kχ[R+l,R+l+1])∥2
J2 + ∥χ[R,∞)∂yKχ[R+l,R+l+1])∥2
J2
⩽2A2
Z ∞
R
dx
Z R+l+1
R+l
dy
1
(x + y)4 = 3A2
4R + 2l + 1
(2R + l)2(2R + l + 1)2
⩽
6A2
(2R + l)2(2R + l + 1).
Therefore, the trace norm satisfies
∥χ[R,∞)Kχ[R,∞)∥J1 ⩽
√
3 A
R
+ 2
√
3 A
∞
X
l=1
1
(2R + l)3/2 .
Finally, we have
∞
X
l=1
1
(2R + l)3/2 ⩽
Z
R+
1
(2R + x)3/2 dx =
1
√
2R
,
which finishes the proof.
Recall several properties of Bessel functions. Set J(x) = √x Jν(x) and D(x) =
Jν(x) −
p
2/π cos(x −ϕν), where ϕν = π/4 + (π/2)ν.
We have the following
asymptotics for the Bessel function and its derivative as x approaches infinity:
D(x) = −
r
2
π sin(x −ϕν)ν2 −1/4
x
+ O(x−2)
(7.5)
and
D′(x) = Aν
cos(x −ϕν)
x
+ O(x−2),
(7.6)
where Aν is some constant. These imply uniform estimates on R+ for ν > −1 and
some constant Cν:
|D(x)| ⩽
Cν
√x(1 + √x)
(7.7)
and

D′(x) −Aν
cos(x −ϕν)
x

 ⩽
Cν
x3/2(1 + √x).
(7.8)
Recall the following improper integral.
Proposition 6 ([3], Lemma 2.6). We have
Z ∞
0

J(xt)J(yt) −2
π cos(xt −ϕν) cos(yt −ϕν)

dt = −sin(2ϕν)
π(x + y).
(7.9)
Lastly, we establish some properties of the function spaces we have introduced.
Rate of convergence in the central limit theorem
1621
Lemma 5. There exists a constant C such that for any a ∈L1(R+) ∩L∞(R+)
satisfying ∥a∥˙B < ∞we have
(1) ∥a′′∥L1 ⩽C(∥a∥˙H1 + ∥a∥˙H2 + ∥ta(t)∥˙H2);
(2) ∥ta′′′(t)∥L1 ⩽C(∥a∥˙H3 + ∥a∥˙H1 + ∥ta(t)∥˙H2 + ∥t2a(t)∥˙H3);
(3) limt→+∞a(t) = 0, limt→+∞a′(t) = 0 and limt→+∞ta′′(t) = 0;
(4) |a′(0)| ⩽∥a∥˙H1 + ∥a∥˙H2 .
In particular, the above estimates are bounded by C∥a∥˙B.
Proof. (1) Using the Cauchy–Bunyakovsky–Schwarz inequality, for the L1-norm
we write
∥a′′∥L1 =
Z 1
0
|a′′(t)| dt +
Z ∞
1
|a′′(t)| dt ⩽∥a∥˙H2 + ∥ta′′(t)∥L2.
Since ta′′(t) = (at)′′ −2a′, the second term is estimated by 2∥a∥˙H1 + ∥ta(t)∥˙H2.
(2) The proof is quite similar to the previous one.
(3) The statement on a follows from ba ∈L1(R) and the Riemann–Lebesgue
lemma.
Since a′ ∈H1(R+) we see that ba′ is absolutely integrable and the statement on a′
follows again from the Riemann–Lebesgue lemma.
By the first and second assertions (ta′′(t))′ = a′′(t) + ta′′′(t) is absolutely inte-
grable, so ta′′(t) tends to a finite limit as t approaches infinity. Since (ta(t))′′ and
a′(t) are square integrable, so is ta′′(t), which yields that the limit is zero.
(4) The expression of a′(0) in terms of the cosine transform yields
|b′(0)| ⩽1
π
Z ∞
0
λ|bb(λ)| dλ,
and by the Cauchy–Bunyakovsky–Schwarz inequality and Parseval’s theorem we
have
Z 1
0
λ|bb(λ)| dλ ⩽∥b∥˙H1
and
Z ∞
1
λ2
λ |bb(λ)| dλ ⩽∥b∥˙H2.
Lemma 5 is proved.
We devote the rest of this section to the proof of Lemma 3.
Proof of Lemma 3. Since B1 −W1 = 0, it is sufficient to prove the statement for
b ∈L1(R+) ∩L∞(R+) satisfying ∥b∥˙B < ∞.
Recall the formula for the kernel of the difference Rb(x, y) = Bb(x, y)−Wb(x, y):
Rb(x, y) =
Z ∞
0

J(xt)J(yt) −1
π cos((x −y)t)

b(t) dt.
Let us outline the plan of the proof. One can observe from the asymptotics (7.5)
and (7.6) that the above integral contains an asymptotically small function for
large x and y. Thus, we substitute J(x) = √x Jν(x) = D(x) +
p
2/π cos(x −ϕν)
into the expression for Rb(x, y).
This substitution and several integrations by
parts represent the kernel as a sum of other kernels, to which Corollary 1 and
Proposition 4 can be applied.
1622
S. M. Gorbunov
To be precise, we perform a sequence of decompositions of our kernel, for which
we use the following notation:
Rb(x, y) = R1(x, y) −R2(x, y),
(7.10)
R2(x, y) = S(x, y) + T(x, y) + T(y, x)
(7.11)
and
T(x, y) = T0(x, y) + T1(x, y) + Z(x, y).
(7.12)
Explicit formulae are presented below (see (7.13)–(7.15)). We prove an estimate for
the trace norm for each of the above kernels separately. In particular, the estimate
of the trace norm for χ[R,∞)R1χ[R,∞) follows from Corollary 1. Estimates for the
trace norms of the operators with the kernels
χ[R,∞)2(x, y)S(x, y),
χ[R,∞)2(x, y)T0(x, y),
χ[R,∞)2(x, y)T1(x, y),
χ[R,∞)2(x, y)(Z(x, y) + Z(y, x))
follow from Proposition 4.
The sequence of decompositions. 1. The decomposition (7.10). First we sub-
stitute the following formula into the kernel Rb(x, y):
1
π cos((x −y)t) = 2
π cos(xt −ϕν) cos(yt −ϕν) −1
π cos((x + y)t −2ϕν).
By part (3) of Lemma 5 the following integral can twice be integrated by parts and
thus expressed as follows:
1
π
Z ∞
0
cos((x + y)t −2ϕν)b(t) dt
= sin(2ϕν)b(0)
π(x + y)
−b′(0) cos(2ϕν)
π(x + y)2
−
1
π(x + y)2
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt.
Next we substitute the expression (7.9) for sin(2ϕν)/(π(x + y)) into the above
identity. These calculations prove the decomposition (7.10) for the following kernels
R1 and R2:
R1(x, y) =
1
π(x + y)2

cos(2ϕν)b′(0) +
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt

,
R2(x, y) =
Z ∞
0

J(xt)J(yt) −2
π cos(xt −ϕν) cos(yt −ϕν)

b0(t) dt,
(7.13)
where b0(x) = b(x) −b(0).
2. The decomposition (7.11). It can be verified directly that (7.11) holds if we
take S and T to be
S(x, y) =
Z ∞
0
D(xt)D(yt)b0(t) dt,
T(x, y) =
Z ∞
0
D(xt)
r
2
π cos(yt −ϕν)b0(t) dt.
(7.14)
Rate of convergence in the central limit theorem
1623
3. The decomposition (7.12). We integrate the expression for T(x, y) by parts:
Z ∞
0
D(xt)
r
2
π
1
y b0(t) d(sin(yt −ϕν)) = D(xt)
r
2
π
1
y b0(t) sin(yt −ϕν)

∞
0
−
Z ∞
0
D(xt)
r
2
π
1
y sin(yt −ϕν)b′(t) dt
−
Z ∞
0
xD′(xt)
r
2
π
1
y sin(yt −ϕν)b0(t) dt,
where the first term is zero by Lemma 5 and (7.7). Next we take the following
kernels for the decomposition (7.12):
T0(x, y) = −
Z ∞
0
D(xt)
r
2
π
1
y sin(yt −ϕν)b′(t) dt,
T1(x, y) = −
Z ∞
0
x

D′(xt) −Aν
cos(xt −ϕν)
xt
r
2
π
1
y sin(yt −ϕν)b0(t) dt,
Z(x, y) = −
Z ∞
0
xAν
cos(xt −ϕν)
xt
b0(t)
r
2
π
1
y sin(yt −ϕν) dt.
(7.15)
Trace norm estimates. Before diving into calculations we present several inequal-
ities we need.
Firstly, the Cauchy–Bunyakovsky–Schwarz inequality implies the following:
|b0(t)| =

Z t
0
b′(x) dx

 ⩽
√
t ∥b∥˙H1.
(7.16)
The same argument for the derivative gives
|b′(t)| ⩽
√
t (|b′(0)| + ∥b∥˙H2).
(7.17)
Further, using (7.17) we have
|b0(t)| =

Z t
0
b′(x) dx

 ⩽(|b′(0)| + ∥b∥˙H2)t3/2.
(7.18)
Lastly, observe the identity
d
dt
b0(t)
t

= 1
t2
Z t
0
b′(x) dx −b0(t) +
Z t
0
xb′′(x) dx

= 1
t2
Z t
0
xb′′(x) dx.
The Cauchy–Bunyakovsky–Schwarz inequality implies that

Z t
0
xb′′(x) du

 ⩽t3/2∥b∥˙H2.
Substituting this in yields

d
dt
b0(t)
t


 ⩽∥b∥˙H2
√
t .
(7.19)
1624
S. M. Gorbunov
1. An estimate for R1. We have
|R1(x, y)| ⩽
1
(x + y)2 (|b′(0)| + ∥b′′∥L1).
By Lemma 5 b′′ is absolutely integrable, so we have the following expression for
the derivative:
∂yR1(x, y) = −
2
π(x + y)3

cos(2ϕν)b′(0) +
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt

−
1
π(x + y)2
Z ∞
0
sin((x + y)t −2ϕν)tb′′(t) dt.
Next we integrate the second term by parts:
1
(x + y)
Z ∞
0
d(cos((x + y)t −2ϕν))tb′′(t) dt = cos((x + y)t −2ϕν)tb′′(t)

∞
0
−
1
(x + y)
Z ∞
0
cos((x + y)t −2ϕν)(tb′′′(t) + b′′(t)) dt,
where the limit at infinity is zero by Lemma 5.
These calculations imply the
following estimate for x, y ⩾1:
|∂yR1(x, y)| ⩽
2
(x + y)2 (|b′(0)| + ∥b′′∥L1 + ∥tb′′′(t)∥L1).
Finally, applying Corollary 1 and Lemma 5 we obtain the required estimate for
some constant C and R ⩾1:
∥χ[R,∞)R1χ[R,∞)∥J1 ⩽C∥b∥˙B
√
R
.
2. An estimate for S. Using (7.7) we obtain
Z ∞
R
|D(xt)|2 dx ⩽C2
ν
Z ∞
R
1
xt(1 +
√
xt)2 dx = 2C2
ν
t

ln

1 +
1
√
tR

−
1
1 +
√
tR

.
Set G(x) = ln(1 + 1/√x) −1/(1 + √x). Using Proposition 4 we have
∥χ[R,∞)Sχ[R,∞)∥J1 ⩽2C2
ν
Z ∞
0
|b0(t)|
t
G(tR) dt.
Next we substitute (7.16) in to obtain
∥χ[R,∞)Sχ[R,∞)∥J1 ⩽2C2
ν∥b∥˙H1
Z ∞
0
G(tR)
√
t
dt = 4C2
ν
√
R
∥b∥˙H1 ⩽4C2
ν
√
R
∥b∥˙B.
3. An estimate for T0. Again, Proposition 4 in combination with (7.7) gives
∥χ[R,∞)T0χ[R,∞)∥J1 ⩽Cν
√
R
Z ∞
0
|b′(t)|
√
t
p
G(tR) dt.
Rate of convergence in the central limit theorem
1625
For the integral over [0, 1] using inequality (7.17), for some constant C we can write
Z 1
0
|b′(t)|
√
t G1/2(tR) dt ⩽(|b′(0)| + ∥b∥˙H2)
Z 1
0
p
G(tR) dt ⩽C(|b′(0)| + ∥b∥˙H2).
And for the integral over [1, ∞) we use the Cauchy–Bunyakovsky–Schwarz inequa-
lity:
Z ∞
1
|b′(t)|
√
t
p
G(tR) dt ⩽∥b∥˙H1
sZ ∞
1
G(xR)
x
dx ⩽
√
2 ∥b∥˙H1.
These calculations yield the following estimate by Lemma 5:
∥χ[R,∞)T0χ[R,∞)∥J1 ⩽2CCν
√
R
(|b′(0)| + ∥b∥˙H1 + ∥b∥˙H2) ⩽4CCν
√
R
∥b∥˙B.
4. An estimate for T1. Using estimate (7.8) we obtain
Z ∞
R
x2

D′(xt) −Aν
cos(xt −ϕν)
xt
2
dx ⩽C2
ν
t3
Z ∞
R
1
x(1 +
√
xt)2 dx = 2C2
ν
t3 G(tR).
In combination with Proposition 4, this implies that
∥χ[R,∞)T1χ[R,∞)∥J1 ⩽
√
2Cν
√
R
Z ∞
0
|b0(t)|
t3/2
p
G(tR) dt.
For the integral over [0, 1] we use inequality (7.18) to obtain
Z 1
0
|b0(t)|
t3/2
p
G(tR) dt ⩽(|b′(0)| + ∥b∥˙H2)
Z 1
0
p
G(tR) dt ⩽C(|b′(0)| + ∥b∥˙H2)
for some constant C. For the integral over [1, ∞), using (7.16), for some constant eC
we have
Z ∞
1
|b0(t)|
t3/2
p
G(tR) dt ⩽∥b∥˙H1
Z ∞
1
p
G(tR)
t
dt ⩽eC∥b∥˙H1.
Therefore, we conclude that
∥χ[R,∞)T1χ[R,∞)∥J1 ⩽
√
2(C + eC)Cν
√
R
(∥b∥˙H1 + ∥b∥˙H2 + |b′(0)|)
⩽2
√
2(C + eC)Cν
√
R
∥b∥˙B.
5. An estimate for Z(x, y) + Z(y, x). We denote the operator induced by this
kernel by eZ. Integration of the kernel by parts yields
eZ(x, y) = Z(x, y) + Z(y, x) = Aν
r
2
π
Z ∞
0
b0(t)
xyt
d
dt(sin(xt −ϕν) sin(yt −ϕν)) dt
= −Aν
r
2
π
b′(0)
xy sin2(ϕν)
−Aν
r
2
π
1
xy
Z ∞
0
d
dt
b0(t)
t

sin(xt −ϕν) sin(yt −ϕν) dt.
1626
S. M. Gorbunov
The first term induces the one-dimensional projector h1(x)⟨h2(y), −⟩L2 with trace
norm bounded by ∥h1∥L2∥h2∥L2. By Lemma 5, for the trace norm of the corres-
ponding operator on L2[R, ∞) we have |Aνb′(0)|/R ⩽|Aν|∥b∥˙B/R.
We apply Proposition 4 to the second term. This results in the estimate
∥χ[R,∞) eZχ[R,∞)∥J1 ⩽|Aν|∥b∥˙B
R
+ |Aν|
R
Z ∞
0

d
dt
b0(t)
t


 dt.
The integral over [0, 1] is estimated as follows in view of (7.19):
Z 1
0

d
dt
b0(t)
t


 dt ⩽∥b∥˙H2.
The integral over [1, ∞) is estimated using (7.16) and the Cauchy–Bunyakovsky–
Schwarz inequality:
Z ∞
1

d
dt
b0(t)
t


 dt ⩽
Z ∞
1
|b′(t)|
t
+ ∥b∥˙H1
t3/2

dt ⩽3∥b∥˙H1.
Therefore, we conclude that
∥χ[R,∞) eZχ[R,∞)∥J1 ⩽5|Aν|∥b∥˙B
R
.
This finishes the proof of Lemma 3.
§ 8. Proof of Theorems 1 and 2
Recall the Jacobi–Dodgson identity.
Proposition 7 ([23], Proposition 6.2.9). Let A be an invertible operator on a sep-
arable Hilbert space H and A −I ∈J1(H). Let P be an orthogonal projection in H
and Q = I −P . Then
det(PAP) = det(A) det(QA−1Q).
(8.1)
We use the following variation of this identity.
Corollary 2. Let P1 and P2 be two commuting orthogonal projections in a sepa-
rable Hilbert space H. Let Qi = I −Pi, i = 1, 2. Then
det(P1AP1)
det(Q1A−1Q1) =
det(P2AP2)
det(Q2A−1Q2),
(8.2)
if A is invertible, A −I ∈J2(H) and all Fredholm determinants are well defined.
Remark 3. It is not required that A −I ∈J1(H) in this statement.
Proof of Corollary 2. Let A = I + K, where K ∈J2(H).
We choose a joint
orthogonal basis {ei}i∈N of eigenvectors of P1 and P2. Let Rn be the orthogonal
projection onto span({ei}i∈1,...,n). We regard RnH as a separable Hilbert space.
Since the Pi and Qi commute with Rn, they remain orthogonal projections in RnH.
Rate of convergence in the central limit theorem
1627
Since K is compact, RnKRn →K in the operator norm. This implies that for
all sufficiently large n the operator I + RnKRn is invertible on RnH. Applying
Proposition 7 we have
det(RnP1AP1Rn)
det(Q1(RnARn)−1Q1) =
det(RnP2AP2Rn)
det(Q2(RnARn)−1Q2) = det(RnARn).
(8.3)
It remains to show that (RnARn)−1 −RnA−1Rn
J1(H)
−−−−→0 as n →∞. For the
above difference we have
(Rn + RnKRn)−1 −Rn(I + K)−1Rn
= (RnKRn)2(Rn + RnKRn)−1 −RnK2(I + K)−1Rn,
where (Rn + RnKRn)−1 →(I + K)−1 and Rn →I strongly, and (RnKRn)2 →K
and RnK2 →K2 in the trace norm since K ∈J2(H). Therefore, we have
lim
n→∞det(Qi(RnARn)−1Qi) = lim
n→∞det(RnQiA−1QiRn) = det(QiA−1Qi).
Equality (8.2) follows by taking limits in (8.3) as n →∞.
The corollary is proved.
Let us extend the definition (1.1) to all functions in L∞(R+). Recall that the
Hankel transform Hν on L2(R+) is defined by
Hνf(λ) =
Z ∞
0
√
λx Jν(λx)f(x) dx.
Similarly to the Fourier transform, it is an isometry of L1(R+)∩L2(R+) and extends
to L2(R+) by continuity. Also recall that H∗
ν = H−1
ν
= Hν. Now for b ∈L∞(R+)
we define the Bessel operator by
Bb = HνbHν.
(8.4)
This coincides with the definition (1.1) for b ∈L1(R+)∩L∞(R+), but from (8.4) it is
clear that B: f →Bf, L∞(R+) →B(L2(R+)) is a Banach algebra homomorphism
and, in particular, B−1
eb = Be−b.
Next we want to show that for b ∈B the operator Bb −Wb is Hilbert–Schmidt.
By Lemma 3 we have χ[1,∞)(Bb −Wb)χ[1,∞) ∈J1 and χ[0,1](Bb −Wb)χ[0,1] ∈J1 by
Theorem 4. The following statement, completing the argument, can be verified
directly.
Lemma 6 (see [3], Lemmas 3.1 and 3.2). For b ∈H1(R+) ∩L1(R+) the operators
χ[0,1]Bb and χ[0,1]Wb are Hilbert–Schmidt.
Proof of Lemma 2. For arbitrary R1, R2 > 0 we set P1 = χ[0,R1], P2 = χ[0,R2]
and A = We−b+BebWe−b−. By the first statement of Proposition 3 and the defi-
nition (8.4)
A is invertible and its inverse is Web−Be−bWeb+. In the notation of
Corollary 2 we also have Q1 = χ[R1,∞) and Q2 = χ[R2,∞). Using the second and
third assertions of Proposition 3 we can write
QiA−1Qi = χ[Ri,∞) + χ[Ri,∞)Web−χ[Ri,∞)Re−bχ[Ri,∞)Web+χ[Ri,∞),
(8.5)
1628
S. M. Gorbunov
where Rb = Bb−Wb. Hence by the assumptions and since Re−b is Hilbert–Schmidt,
we can apply Corollary 2 to obtain
det(χ[0,R1]We−b+BebWe−b−χ[0,R1])
det(χ[R1,∞)Web−Be−bWeb+χ[R1,∞)) = det(χ[0,R2]We−b+BebWe−b−χ[0,R2])
det(χ[R2,∞)Web−Be−bWeb+χ[R2,∞)) = Z(b),
(8.6)
where all Fredholm determinants are well defined.
Lemma 2 is proved.
Recall an asymptotic result due to Basor and Ehrhardt.
Theorem 6 ([3], Theorem 1.1). Suppose the function b ∈L1(R+) ∩L∞(R+) sat-
isfies the following conditions:
• b is continuous and piecewise C2-smooth on [0, ∞);
• limt→∞b(t) = 0;
• (1 + t)−1/2b′(t) ∈L1(R+), b′′(t) ∈L1(R+).
Then the following asymptotic formula holds as R →∞:
det(χ[0,R]Bebχ[0,R]) = exp(RcB
1 (b) + cB
2 (b) + cB
3 (b))QB
R(b),
QB
R(b) →1,
(8.7)
where the cB
i (b) are as in Theorem 1.
By Lemma 5 the functions in B satisfy the assumptions of Theorem 5.
The following lemma shows that for each b ∈B the function e−b satisfies the
assumption of Lemma 3.
Lemma 7. Let b ∈B. Then eb −1 ∈L1 ∩L∞. There exists a constant C such
that for any b ∈B we have
∥eb∥˙B ⩽C exp(∥b∥L∞)(1 + ∥xb′(x)∥2
L∞+ ∥b∥2
˙B)∥b∥˙B.
Proof. The first assertion follows directly from L∞being a Banach algebra with
pointwise multiplication and the inequality
∥eb −1∥L1 ⩽∥b∥L1

eb −1
b

L∞
.
For an estimate of the ˙B-seminorm, we have by definition
∥eb∥˙H1 ⩽exp(∥b∥L∞)∥b∥˙H1.
The third derivative of eb is
(eb)′′′ = eb(b′′′ + (b′)3 + 3b′b′′).
Observe that
∥b′∥L∞⩽∥λbb(λ)∥L1 ⩽∥b∥˙H1 + ∥b∥˙H2.
This yields the estimate
∥eb∥˙H3 ⩽exp(∥b∥L∞)(∥b∥˙H3 + ∥b∥2
˙B∥b∥˙H1 + 3∥b∥˙B∥b∥˙H2).
Rate of convergence in the central limit theorem
1629
Next we write out the second derivative of xeb(x):
(xeb(x))′′ = eb(x)((xb(x))′′ + x(b′(x))2).
Therefore,
∥xeb(x)∥˙H2 ⩽exp(∥b∥L∞)(∥xb(x)∥˙H2 + ∥xb′(x)∥L∞∥b∥˙H1).
Finally, the third derivative of x2eb(x) is as follows:
(x2eb(x))′′′ = eb(x)(6x(b′(x))2 + 3x2b′(x)b′′(x) + (x2b(x))′′′ + x2(b′(x))3).
This implies that
∥x2eb(x)∥˙H3 ⩽exp(∥b∥L∞)(3∥xb′(x)∥L∞∥xb(x)∥˙H2
+ ∥x2b(x)∥˙H3 + ∥xb′(x)∥2
L∞∥b∥˙H1).
The lemma is proved.
Proof of Theorem 1. Recall the inequality
| det(I + K) −1| ⩽∥K∥J1 exp(∥K∥J1).
Also recall that for any trace-class operator A and bounded B we have ∥AB∥J1 ⩽
∥A∥J1∥B∥. By the definition of Wiener–Hopf operators ∥Wb∥= ∥b∥L∞. These facts
and Lemmas 3 and 7, in combination with the expression (8.5), prove estimate (2.2).
By the above argument the denominator in (3.5) approaches 1. From Lemma 1
and Theorem 6, for the numerator in (3.5) we have
det(χ[0,R]We−b+BebWe−b−χ[0,R]) →exp(cB
2 (b) + cB
3 (b)),
R →∞.
It is now clear that Z(b) = exp(cB
2 (b) + cB
3 (b)). This finishes the proof.
We now proceed to the proof of Theorem 2. First we establish an estimate for the
rate of convergence of EJνSR
f . The argument is based on the proof of Proposition 5.1
in [3].
Lemma 8. There exists a constant C such that for any b ∈B we have

EJνSR
f −

bb(0) −ν
2b(0)


 ⩽C∥b∥˙B
√
R
.
Proof. Recall the expression for the expectation of an additive functional:
EJνSR
f =
Z
R+
f
 x
R

Bχ[0,1](x, x) dx.
The Bessel kernel Bχ[0,1](x, y) is defined on the diagonal by
Bχ[0,1](x, x) = x
2 (J2
ν(x) −Jν+1(x)Jν−1(x)).
1630
S. M. Gorbunov
Its asymptotic as x →∞is
Bχ[0,1](x, x) = 1
π + sin(2(x −ϕν))
x
+ O(x−2).
Consider the function
F(ξ) = −
Z ∞
ξ
 t
2(J2
ν(t) −Jν+1(t)Jν−1(t)) −1
π

dt.
It is clear that F(ξ) = O(ξ−1) as ξ →∞. Therefore, we have |F(ξ)| ⩽C(1+ξ)−1 for
some constant C. Integrating by parts in the formula for the expectation we obtain
Z
R+
f
 x
R

Bχ[0,1](x, x) dx −1
π
Z
R+
f
 x
R

dx
= f
 x
R

F(x)

∞
0
−1
R
Z
R+
f ′
 x
R

F(x) dx,
(8.8)
where f(∞)F(∞) = 0 by Lemma 5.
For the value at zero, using the equality
Jν−1(t) + Jν+1(t) = (2ν/t)Jν(t) we write
F(0) =
Z ∞
0
 t
2(J2
ν(t) −Jν+1(t)Jν−1(t)) −1
π

dt
=
Z ∞
0
 t
2(J2
ν(t) + J2
ν+1(t)) −1
π

dt −ν
Z ∞
0
Jν+1(t)Jν(t) dt.
The second integral is equal to 1/2 (see [17], § 6.512(3)). The first term is asymp-
totically equal to
Z T
0
xJ2
ν(x) dx = T 2
2 (J2
ν(T) −Jν+1(T)Jν−1(T))
= T
π + sin(2(T −ϕν)) + o(1)
as T →∞.
Recall that ϕν+1 = ϕν + π/2. Therefore, the first term is zero. We conclude that
F(0)b(0) = (ν/2)b(0).
What is left to do is to estimate the second term in (8.8). Using F(ξ) ⩽C(1+ξ)−1
we can write

Z
R+
f ′(x)F(Rx) dx

 ⩽
Z
R+
C|b′(x)|
1 + Rx dx,
which is at most C∥b∥˙H1/
√
R. This completes the proof.
Proof of Theorem 2. Recall that we denote by FR,b and FN the cumulative distribu-
tion functions of SR
b and the standard Gaussian distribution N(0, 1), respectively.
Using Feller’s smoothing estimate (see [16], Ch. XVI, § 3), Theorem 1 and Propo-
sition 1, for any T > 0 we have
sup
x |FR,b(x) −FN (x)| ⩽
24
√
2π3 T
+ 1
π
Z T
−T
1
|k|

exp

ikRbb(0) −ik ν
2 b(0) −ikEJνSR
b

QB
R(kb) −1

 dk.
(8.9)
Rate of convergence in the central limit theorem
1631
By the second statement of Theorem 1 and Lemma 8 the integrand can be esti-
mated by the following expression for some C > 0 depending only on ∥b+∥L∞
and L(b):
C
√
R
(1 + |k|2)eC|k| exp
C|k|
√
R
(1 + |k|2)eC|k|

.
Observe that if |k| ⩽C1 ln R, where C1C < 1/2, then there exists a constant eC
such that for any R ⩾1 the above expression is at most
eC(1 + (ln R)2)
R1/2−CC1
.
Therefore, if we take T = C1 ln R, then the integral in (8.9) is at most
2 eCC1 ln R(1 + (ln R)2)
R1/2−CC1
,
and the statement of the theorem follows.
