---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-004-5-a-link-between-the-bessel-operator-and-the-det
section_title: "§5 A link between the Bessel operator and the determinantal point process with Bessel kernel"
section_number: null
pages: 7-10
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
and the determinantal point process with Bessel kernel
Let E be R or R+ = [0, ∞). Recall that a configuration on E is a discrete subset
of E. We denote the set of configurations by Conf(E). It can be endowed with
a σ-algebra of measurable subsets X (for instance, see [25]). A point process P is
defined to be a probability measure on (Conf(E), X).
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
In both cases conjugation by the unitary operator URf(x) = R−1/2f(x/R) com-
pletes the proof.
The proposition is proved.
