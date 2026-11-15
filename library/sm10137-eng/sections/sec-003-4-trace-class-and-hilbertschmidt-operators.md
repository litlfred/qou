---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-003-4-trace-class-and-hilbertschmidt-operators
section_title: "§4 Trace class and Hilbert–Schmidt operators"
section_number: null
pages: 6-7
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
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
