---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-002-3-structure-of-the-paper
section_title: "§3 Structure of the paper"
section_number: null
pages: 5-6
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
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
