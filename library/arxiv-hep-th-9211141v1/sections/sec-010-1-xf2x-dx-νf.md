---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-010-1-xf2x-dx-νf
section_title: "(x)f2(x) dx = −νf ′"
section_number: 1
pages: 27-30
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
2(0) + νf ′
1(0) + ν
Z ∞
0
f2(y)f ′′
1 (y) dy .
Thus, since ν̸ = 0 (this follows easily from the fact that the Fourier transform of A(x) is
nonzero), we have f ′
1(0) = f ′
2(0). But it is clear from (4.7) that for any eigenfunction f we
have f ′(0) = t2 −µ. Thus f1 and f2 correspond to the same eigenvalue of L and so are equal.
The case when (4.20) holds is even easier. Diﬀerentiating both sides of the ﬁrst relation
once and integrating by parts gives
νf ′
1(x) = −A(x −2t) −
Z ∞
0
A(x + y −2t)f ′
1(y) dy .
Multiplying both sides of this by f2(x) and integrating, using the second relation of (4.20),
we obtain
ν
Z ∞
0
f ′
1(x)f2(x) dx = −ν + ν
Z ∞
0
f2(y)f ′
1(y) dy ,
contradicting ν̸ = 0.
Since, as we now know, the eigenvalues of K are simple, there is a permutation σ of
N = {0, 1, 2, · · ·} such that fi is the eigenfunction of K corresponding to its σ(i)th largest
eigenvalue λσ(i); this permutation is independent of t or else, by the continuity of the eigen-
values in t, there would be a multiple eigenvalue for some t.
Up to now our kernel K corresponded to an arbitrary factor λ. Of course formula (1.21)
refers to the case λ = 1.
Lemma 2 For each i we have λi →1 as s →−∞.
Proof. In this case λ = 1 formula (4.6) reads
K(x, y) =
Z ∞
0
Ai(x + z)Ai(z + y) dz .
(4.21)
For the purposes of this proof we denote by A (resp. K) the operator on (−∞, ∞) with
kernel Ai(x + y) (resp. K(x, y)) and by Ps the projection from L2(−∞, ∞) to L2(s, ∞). So
the λi are the eigenvalues of PsKPs. Now it is known [13] that A2 = I, and (4.21) says
that K = AP0A. Thus K2 = AP0A2P0A = AP0A = K. In other words, K is a projection
27
operator. (This is not surprising since its kernel is a scaling limit of the kernels KN(x, y) of
projection operators.) Clearly it has inﬁnite-dimensional range. It now follows easily from
the minimax characterization of the eigenvalues that, for each i, the ith largest eigenvalue of
PsKPs tends to 1 as s →−∞.
We now state a lemma which is the basis of a trick used by Fuchs [11] in his derivation
of the asymptotics of the eigenvalues of the sine kernel.
Lemma 3 Let J(x, y) be a symmetric kernel, on a ﬁxed interval, depending smoothly on a
parameter t. Let g be an eigenfunction normalized so that
R g(x)2 dx = 1 and let λ be the
corresponding eigenvalue. Then, with the subscript t denoting ∂/∂t, we have
λt =
Z Z
Jt(x, y)g(y)g(x) dydx .
Proof. From
Z
J(x, y)g(y) dy = λg(x)
(4.22)
we get
Z
Jt(x, y)g(y) dy +
Z
J(x, y)gt(y) dy = λtg(x) + λgt(x) .
Multiplying both sides by g(x) and integrating over x, we obtain (using the normalization
of g and (4.22))
Z Z
Jt(x, y)g(y)g(x) dydx +
Z Z
J(x, y)gt(y)g(x) dxdy = λt + λ
Z
gt(x)g(x) dx
= λt +
Z Z
J(x, y)g(y)gt(x) dydx .
By symmetry of J the two double integrals involving it cancel, and we obtain the statement
of the lemma.
We apply the lemma to the opertor with kernel A(x + y −2t) on (0, ∞) whose square
is our Airy operator (translated to act on (0, ∞)). Thus we may write its eigenvalues as
q
λσ(i), where the square roots might have either sign. The lemma gives
28
∂
∂t
q
λσ(i) = −2
Z ∞
0
Z ∞
0
A′(x + y −2t)gi(y)gi(x) dydx
(4.23)
where
gi(x) = fi(x)

Z ∞
0
fi(y)2 dy
1/2
.
But from
Z ∞
0
A(x + y −2t)gi(y) dy =
q
λσ(i)gi(x)
we obtain upon diﬀerentiation that
Z ∞
0
A′(x + y −2t)gi(y) dy =
q
λσ(i)g′
i(x)
so (4.23) may be rewritten
∂
∂t
q
λσ(i) = −2
q
λσ(i)
Z ∞
0
g′
i(x)gi(x) dx .
The integral is of course −1
2gi(0)2. Recalling that fi(0) = 1 we see that we have established
the relation
∂
∂t
q
λσ(i) =
q
λσ(i)

Z ∞
0
fi(x)2 dx

,
or
∂
∂t log λσ(i) = 2

Z ∞
0
fi(x)2 dx

We now use (4.18) and integrate the resulting relation with respect to t from t to ∞.
Recalling Lemma 2, we deduce
−log λσ(i) ∼
√π
i! 25i+3t
3
2i+ 3
4 exp

−8
3t3/2

,
precisely the right side of (1.21).
All that remains now is to show that σ(i) = i for all i. But it is clear from this asymptotic
relation that i < j implies λσ(i) > λσ(j) for large t (and so for all t), so that σ(i) < σ(j).
Thus σ is order preserving, and since σ : N →N is onto we must have σ(i) = i for all i.
This concludes the derivation of (1.21). The deduction of (1.22) from (1.21) is completely
analogous to the corresponding deduction for the sine kernel in ref. [28], Sec. VIIB.
29
