---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-008-32-linear-transformations-preserving-stability-m
section_title: "Linear transformations preserving stability – multiaffine case."
section_number: 3.2
pages: 10-11
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
Lemma 3.2 (Lieb-Sokal Lemma, Lemma 2.1 of [5]). Letg(x) +yf (x)∈ S[x,y ] be
stable and such that degi(f)≤ 1. Then g−∂if∈ S[x] is stable.
Proof. Since g is stable (by specialization to y = 0), there is nothing to prove if
∂if≡ 0 identically, so assume otherwise (and hence that f⁄≡ 0). By permutation
we can assume that i = 1. Since f is stable and z1,z∈ H imply thatz1−z−1∈ H,
it follows that
yf (x1−y−1,x 2,...,x m) =−∂1f(x) +yf (x)
is stable. Proposition 2.7(b) implies that for all z∈ Hm,
Im
(g(z)−∂1f(z)
f(z)
)
= Im
(g(z)
f(z)
)
+ Im
(−∂1f(z)
f(z)
)
≥ 0.
Thus, by Proposition 2.7(b) again, g−∂1f +yf is stable. Specializing to y = 0
shows that g−∂1f is stable. □
Exercise 3.3 (Lemma 3.1 of [5]). Letf∈ C[x]MA and w∈ Hm. Then for all ϵ> 0
suﬃciently small, (x + w)[m] +ϵf(x) is stable. (Here ( x + w)[m] =∏m
i=1(xi +wi).)
For a linear transformationT : C[x]MA→ C[x] of multiaﬃne polynomials, deﬁne
the algebraic symbol of T to be the polynomial
T ((x + y)[m]) =T
( m∏
i=1
(xi +yi)
)
=
∑
S⊆[m]
T (xS)y[m]rS
in C[x1,...,x m,y 1,...,y m] = C[x, y].
Theorem 3.4 (Theorem 1.1 of [5]) . Let T : C[x]MA→ C[x] be a linear transfor-
mation. Then T maps S[x]MA into S[x] if and only if either
(a) T (f) =η(f)·p for some linear functional η : C[x]MA→ C and p∈ S[x], or
(b) the polynomial T ((x + y)[m]) is stable in S[x, y].
Proof. First, assume (b) that T ((x + y)[m])∈ S[x, y] is stable. By inversion, it
follows that y[m]T ((x− y−1)[m]) is also stable. Thus, if f∈ S[w1,...,w m] is stable
then
y[m]T ((x− y−1)[m])f(w) =
∑
S⊆[m]
T (xS)(−y)Sf(w)
is stable. If f is also multiaﬃne then repeated application of the Lieb-Sokal Lemma
3.2 (replacing yi by−∂/∂wi for i∈ [m]) shows that
∑
S⊆[m]
T (xS) ∂S
∂wSf(w)
is stable. Finally, specializing to w = 0 shows that T (f(x)) is stable. Thus, the
linear transformation T maps S[x]MA into S[x]. This is clearly also the case if (a)
holds.
Conversely, assume that T maps S[x]MA into S[x]. Then for any w∈ Hm,
(x + w)[m]∈ S[x]MA, so that T ((x + w)[m])∈ S[x].
First, assume that there is a w∈ Hm for which T ((x + w)[m])≡ 0 identically.
For anyf∈ C[x]MA letϵ> 0 be as in Exercise 3.3. ThenϵT (f) =T ((x+w)[m]+ϵf)
is stable, so thatT (f) is stable. Thus, the image of C[x]MA underT is a C-subspace
of S[x]. By Proposition 2.12(b), T has the form of case (a).
MULTIVARIATE STABLE POLYNOMIALS 11
Secondly, ifT ((x + w)[m])⁄≡ 0 for all w∈ Hm then, since each of these polyno-
mials is in S[x], we haveT ((x + w)[m])|x=z⁄= 0 for all z∈ Hm and w∈ Hm. This
shows that T ((x + y)[m])) is stable in S[x, y], which is the form of case (b). □
Theorem 3.4 has a corresponding real form – the proof is completely analogous.
Theorem 3.5 (Theorem 1.2 of [5]) . Let T : R[x]MA→ R[x] be a linear transfor-
mation. Then T maps SR[x]MA into SR[x] if and only if either
(a) T (f) = η(f)·p +ξ(f)·q for some linear functionals η,ξ : R[x]MA→ R and
p,q∈ SR[x] such that p≪q, or
(b) the polynomial T ((x + y)[m]) is real stable in SR[x, y], or
(c) the polynomial T ((x− y)[m]) is real stable in SR[x, y].
Proof. Exercise 3.6. □
4. The Grace-W alsh-Szeg˝o Coincidence Theorem.
Let f ∈ C[x] be a univariate polynomial of degree at most m, and let x =
(x1,...,x m) as usual. For 0 ≤j≤m, the j-th elementary symmetric function of x
is
ej(x) =
∑
1≤i1<···<ij≤m
xi1··· xij =
∑
S⊆[m]:|S|=j
xS.
Them-th polarization off is the polynomial obtained as the image of f under the
linear transformation Polm deﬁned byxj↦→
(m
j
)−1
ej(x) for all 0≤j≤m, and lin-
ear extension. In other words, Polmf is the unique multiaﬃne polynomial in C[x]MA
that is invariant under all permutations of [m] and such that Polmf(x,...,x ) =f(x).
A circular region is a nonempty subset A of C that is either open or closed, and
which is bounded by either a circle or a straight line.
Theorem 4.1 (Grace-Walsh-Szeg˝ o, Theorem 3.4.1b of [14]). Let f ∈ C[x] have
degree at most m and let A be a circular region. If either deg(f) = m or A is
convex, then for every z∈ Am there exists z∈ A such that Polmf(z) =f(z).
Figure 1 illustrates the Grace-Walsh-Szeg˝ o (GWS) Theorem for the polynomial
f(x) = x5 + 10x2 + 1. The black dots mark the solutions to f(x) = 0. Any
permutation of the red (grey) dots is a solution to Pol 5f(x1,...,x 5) = 0. By GWS,
any circular region containing all the red dots must contain at least one of the black
dots. The ﬁgure indicates the boundaries of several circular regions for which this
condition is met.
The proof of GWS in this section is adapted from Borcea and Br¨ and´ en [6].
