---
doc_id: nrarith
doc_title: "Arithmetic of Hyperbolic Manifolds"
section_id: sec-007-8-commensurators-of-chain-links-proofs
section_title: "Commensurators of chain links: proofs"
section_number: 8
pages: 30-34
source_pdf: nrarith.pdf
source_sha256: 085ec9541ddc6cd4
toc_source: inferred
doc_brief: "Arithmetic of hyperbolic manifolds (Neumann–Reid) — survey of arithmetic Kleinian groups: an arithmetic M = H³/Γ is determined up to commensurability by its invariant trace field and quaternion…"
---
In this section we prove parts (iv) and (v) of Theorem 5.1.
Lemma 8.1. Let (p, s) be such that C(p, s) is non-arithmetic. The cusp parameter τ is
not in Q(√−1) or Q(√−3), unless (|p + s|, |s|) = (6, 6).
Proof. Since τ +2 = −4/z we must just show that z is not in Q(√−1) or Q√−3). If
p = 0 then equations (6.4) and (6.5) give x = exp((s+2)πi/2s), and since z = x−x −1,
it is easy to see that z is in Q(√−1) or Q(√−3) if and only if |s| = 3, 4, or 6. The
Table 3. [k(W ′(p, s)):Q]
|s|
0
1
2
3
4
5
6
7
8
9
10
11
12
13
|p + s|
0
2
2
4
2
6
4
6
4
10
4
12
1
2
3
4
5
6
7
8
9
10
11
12
2
2
2
4
3
6
4
8
5
10
6
12
3
2
2
2
2
3
4
4
6
7
6
9
10
8
12
4
2
3
2
3
2
4
3
6
4
8
5
10
6
12
5
4
4
4
4
4
4
5
6
7
8
8
10
11
12
6
2
5
3
4
3
5
2
6
4
6
5
10
4
12
7
6
6
6
6
6
6
6
6
7
8
9
10
11
12
8
4
7
4
7
4
7
4
7
4
8
5
10
6
12
9
6
8
8
6
8
8
6
8
8
6
9
10
8
12
10
4
9
5
9
5
8
5
9
5
9
4
10
6
12
11
10
10
10
10
10
10
10
10
10
10
10
10
11
12
12
4
11
6
8
6
11
4
11
6
8
6
11
4
12
13
12
12
12
12
12
12
12
12
12
12
12
12
12
12
cases |s| = 3 or 4 are arithmetic, so the only case is |s| = 6. If p + 2s = 0 then
C(p, s) is commensurable with C(0, s) by part (i) of Theorem 5.1, so again, the only
non-arithmetic case with z in Q(√−1) or Q(√−3) is |s| = 6.
Finally, if p̸ = 0
and p + 2s̸ = 0 then the proof of Theorem 6.3 shows that z is an algebraic integer
divisor of 4. The only algebraic integer divisors of 4 with positive imaginary part in
Q(√−1) or Q(√−3) are z = i, 2i, 4i, 1 + i, −1 + i, 2 + 2i, −2 + 2i, ω, 2ω,
4ω, −ω, −2ω, and −4ω, where ω = exp(2πi/3). One computes directly that these
correspond to (p + s, s) = (3, 3), (∞, ∞), (3, −3), (1, 3), (3, 1), (1, −3), (3, −1),
(2, 3), (0, 4), (2, −3), (3, 2), (4, 0), (3, −2), respectively, which are arithmetic cases,
and thus excluded in the lemma.
Proof of Theorem 5.1 (iv). An orbifold cusp is called rigid if its fundamental group is
the non-abelian split extension of Z/n by (Z⊕Z) with n = 3, 4, or 6. In this case the
parameter τ of a ﬂat torus covering a horosphere section of the cusp must be in Q(√−1)
or Q(√−3).
Suppose C(p, s) is nonarithmetic and (|p+s|, |s|)̸ = (6, 6). By Lemma 8.1, C(p, s)
cannot cover an orbifold with a rigid cusp. On the other hand, by the Thurston/Jørgenson
theory (cf., [T, Chapter 5]) the quotient W ′′(p, s) of C(p, s) has volume less than
vol(W ′′) ≈0.918.
If W ′′(p, s) non-trivially covered the orientable commensurator
quotient of C(p, s), then this commensurator quotient would have volume at most half
this value, namely <≈0.459. But this volume bound puts the commensurator quotient
on Adams’ list of smallest orientable orbifolds with non-rigid cusps ([A1]), and these
orbifolds are all arithmetic. Thus W ′′(p, s) is the orientable commensurator quotient.
Finally, suppose |(p + s|, |s|) = (6, 6). By Table 2, the cusp parameter of W ′′(p, s)
lies in Q(√−3).
Now, W ′′(p, s) cannot cover an orbifold with a non-rigid cusp by
(0,3)
(0,4)
(1,−4)
(1,−3)
(1,3)
(1,4)
(2,−4)
(2,−3)
(2,3)
(2,4)
(3,−4)
(3,−3)
(3,−2)
(3,−1)
(3,0)
(3,1)
(3,2)
(3,3)
(3,4)
(4,−4)
(4,−3)(4,−2)
(4,−1)
(4,0)
(4,1)
(4,2)
(4,3)
(4,4)
0
−1
−2
2i
Figure 18
the argument of the previous paragraph, so if it non-trivially covers some orbifold, that
orbifold must have a (2, 3, 6) or (3, 3, 3) cusp. But W ′′(p, s) has volume 5v0/6, where
v0 is the volume of the regular ideal tetrahedron, and Adams, in these Proceedings ([A2]),
shows that the four orbifolds with rigid cusps of type (2, 3, 6) or (3, 3, 3) and with volume
less than v0/4 have volumes v0/12, v0/6, v0/6, or 5v0/24. W ′′(p, s) cannot cover
any of these because they are arithmetic (cf. [NR2]). Thus the orientable commensurator
quotient of W ′′(p, s) has volume at least v0/4, so π1W ′′(p, s) has index 1, 2, or 3 in
its orientation preserving commensurator. The cusp of W ′′(p, s) cannot 2-fold cover a
(2, 3, 6) or (3, 3, 3) cusp, because of the 3-torsion. If the commensurator had index 3
then either W ′′(p, s) or some 2-fold cover of W ′′(p, s) would have a 3-fold symmetry.
By considering the set of 3-orbifold points, it is not hard to eliminate the existence of
such a symmetry.
Proof of Theorem 5.1 (v). Recall that we have already shown that the C(p, s) of part
(v) of Theorem 5.1 have orientation reversing commensurabilities, so we must just show
that the others do not. If C(p, s) has an orientation reversing commensurability, then its
orientable commensurator quotient W ′′(p, s) admits an orientation reversing symmetry,
so the cusp of W ′′(p, s) also does. The result thus follows from the following lemma.
0
−1
−2
2i
i
−1+i
−2+i
Figure 19
Lemma 8.2. The cusp of W ′′(p, s) has an orientation reversing symmetry if and only if
p + s = 0, s = 0, p + s = ±s, or W ′′(p, s) is arithmetic.
Proof. The complex parameter of the cusp of W ′′(p, s) is τ(p, q)/2 with q = s/2
(by the parameter for a ﬂat (2, 2, 2, 2)-orbifold we mean the parameter of its unique
2-fold torus covering space). In Fig. 18 we show the image in (τ/2)-space of the integer
lattice in (p + s, s)-space (excluding the non-hyperbolic region N ). The moduli space
of ﬂat (2, 2, 2, 2)-orbifolds is the moduli space of ﬂat tori, namely U/PSL2Z, where U
is complex upper half-space. Orientation reversal induces an involution on U/PSL2Z
(induced by τ 7→−τ ) whose ﬁxed point set gives the set of moduli of orbifolds which
admit an orientation reversing isometry. The lift of this set to U is shown in Fig. 19.
Fig. 20 superimposes the previous two ﬁgures—it is clear that the only (p + s, s) lattice
points for which the cusp of W ′′(p, s) admits an orientation reversing isometry are those
with p + s = 0, s = 0, or p + s = ±s, or {|p + s|, |s|} ∈{{3, 1}, {3, 2}, {4, 2}}. By
Theorem 5.1 part (iii), this proves the lemma.
0
−1
−2
2i
(0,3)
(0,4)
(1,−3)
(1,3)
(2,−4)
(2,−3)
(2,3)
(2,4)
(3,−3)
(3,−2)
(3,−1)
(3,0)
(3,1)
(3,2)
(3,3)
(4,−4)
(4,−2)
(4,0)
(4,2)
(4,4)
Figure 20
