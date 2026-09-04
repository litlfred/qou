---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-011-43-convergence-to-the-polarization
section_title: "Convergence to the polarization."
section_number: 4.3
pages: 13-14
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
stable polynomial of degree at most m: say f(x) = c(x−ξ1)··· (x−ξn) in which
c⁄= 0,n≤m, and ξi⁄∈ H for all i∈ [n]. Then the polynomial F0∈ C[x] deﬁned by
F0(x1,...,x m) =c(x1−ξ1)··· (xn−ξn)
is multiaﬃne and stable, and F0(x,...,x ) = f(x). Let Σ = ( {ik,jk} : k ∈ N)
be a sequence of two-element subsets of [ m], and for each k∈ N let Tk = T (1/2)
ikjk
and deﬁne Fk+1 = Tk(Fk). By induction using Lemma 4.3, each Fk∈ S[x]MA is
multiaﬃne and stable, andFk(x,...,x ) =f(x) for allk∈ N. We will construct such
a sequence Σ for which (Fk : k∈ N) converges to Polmf.
Let P∈ C[x]MA be multiaﬃne, say P (x) =∑
S⊆[m]c(S)xS. For{i,j}⊆ [m] let
ωij(P ) =
∑
S⊆[m]
|c(S)−c(τij(S))|
be theij-th imbalance ofP , and let||P|| =∑
{i,j}⊆[m]ωij(P ) be the total imbalance
of P .
Exercise 4.5. (a) Let (Pk : k∈ N) be polynomials in C[x]MA for which there is a
p∈ C[x] such that Pk(x,...,x ) = p(x) for all k∈ N. If ||Pk||→ 0 as k→ 0, then
(Pk : k∈ N) converges to a limit P∈ C[x]MA, and||P|| = 0.
(b) For P∈ C[x]MA,||P|| = 0 if and only if P is invariant under all permutations
of [m]. Thus, in part (a) the limit is P = Polmp.
14 DAVID G. WAGNER
Exercise 4.6. Let P∈ C[x]MA, let{i,j}⊆ [m], and let Q =T (1/2)
ij P .
(a) Then ωij(Q) = 0.
(b) Ifh∈ [m] r{i,j} thenωhi(Q)≤ (ωhi(P )+ωhj(P ))/2, and similarly forωhj(Q).
(c) If{h,k}⊆ [m] r{i,j} then ωhk(Q) =ωhk(P ).
(d) Consequently,||Q||≤|| P||− ωij(P ).
Now we choose the sequence Σ = ({ik,jk} : k∈ N) as follows: for each k∈ N,
{ik,jk}⊆ [m] is any pair of indices {i,j} for which ωij(Fk) attains its maximum
value. Then ωikjk(Fk)≥
(m
2
)−1
||Fk||, so that by Exercise 4.6(d) and induction on
k∈ N,
||Fk+1||≤
(
1−
(m
2
)−1)
||Fk||≤
(
1−
(m
2
)−1)k+1
||F0||.
Thus, by Exercise 4.5, Fk converges to Polmf, the m-th polarization of f. Finally,
since each Fk is stable (and the limit is a polynomial), Hurwitz’s Theorem implies
that Polmf is stable. This completes the proof of Lemma 4.2, and hence of Theorem
4.1.
