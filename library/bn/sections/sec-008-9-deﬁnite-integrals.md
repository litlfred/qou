---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-008-9-deﬁnite-integrals
section_title: "Deﬁnite integrals"
section_number: 9
pages: 40-45
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
toc_source: inferred
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cover- ings of P1, highlighting their"
---
Deﬁnite integrals
In this section we present another consequence of ﬁniteness of the represen-
tation of the braid group.
Theorem 9.1 Suppose n ≥3 and 0 < µ < 1. Then
I(b1, b2, . . . , bn) =
Z b2
b1
dx
((x −b1)(x −b2) · · · (x −bn))µ
is an algebraic function of (b1, . . . , bn) iﬀρq(Bn) is ﬁnite for q = exp(−2πiµ),
and µ̸ = 1/n.
Here the integral is initially deﬁned for distinct points bi ∈R, and then
extended to C by analytic continuation. Using Theorem 8.1 to check the
ﬁniteness of ρq(Bn), we obtain:
Corollary 9.2 The deﬁnite integral I(b1, . . . , bn) is algebraic exactly for the
17 values of (n, µ) given in Table 11.
39
n
3
µ
2/3
1/4
3/4
1/6
5/6
1/10
3/10
7/10
9/10
n
4
5
6
µ
3/4
1/6
5/6
1/4
3/4
1/6
5/6
5/6
Table 11. Algebraic deﬁnite integrals.
p
Cp
D
φ(D)
p
Figure 12. The cycle D is modiﬁed by a loop around p′.
The integral for the case (n, µ) = (4, 3/4) will be evaluated explicitly at
the end of this section.
Meromorphic diﬀerentials.
To set the stage for the proof, let ω be a
meromorphic 1-form on a compact Riemann surface X with a ﬁnite set of
poles P ⊂X. Then ω determines a cohomology class [ω] ∈H1(X −P). If
Res(ω, p) = 0 for every p ∈P, then ω is traditionally called a diﬀerential of
the second kind; it gives a well-deﬁned cohomology class
[ω] ∈H1(X) ⊂H1(X −P).
Now let φ ∈Mod(X, P) be a mapping-class stabilizing P, and assume
φ is isotopic to the identity on X (it is in the kernel of the natural map
Mod(X, P) →Mod(X)). Then in the course of the isotopy, each p ∈P
traces out a relative cycle Cp ∈H1(X, P) joining p to p′ = φ(p). It is then
easy to compute the action of φ on H1(X −P): it satisﬁes (with suitable
orientations)
[φ(D)] = [D] +
X
p∈P
(Cp · D)[Up′],
where Up′ is a small loop around p′ (see Figure 12).
40
This computation facilitates the study of periods of general meromorphic
1-forms (which may have residues); in particular, it shows that
Z
D
φ∗(ω) =
Z
D
ω +
X
P
(Cp · D) Res(ω, p′).
(9.1)
Proof of Theorem 9.1. The singularities of I(b) = I(b1, . . . , bn) along the
loci bi = bj in Cn are algebraic iﬀµ is rational, so we may restrict attention
to this case.
Consider a generic conﬁguration of distinct points B = {b1, . . . , bn}.
Let µ = k/d in lowest terms, let q = ζ−k
d , let X be the curve deﬁned by
yd = (x −b1) · · · (x −bn) as usual, and let ω = dx/yk. Then T ∗(ω) = qω.
The form ω potentially has poles on the set P = f
∞.
Let L ⊂X −P denote a lift of the segment [b1, b2] to an arc connecting
the corresponding points of eB, chosen so that ω|L agrees with the chosen
branch of the integrand I(b). Observe that D = L −T(L) is a cycle on
X −P, and that
I(b)
=
Z
L
ω = (1 −q)−1
Z
L
ω −T ∗(ω) = (1 −q)−1
Z
D
ω
=
(1 −q)−1⟨D, ω⟩.
Thus I(b) simply measures one of the periods of ω.
Now suppose b is allowed to vary, keeping its coordinates distinct. Then
I(b) can be analytically continued, along many diﬀerent paths, from b to
any point in Sn · b (where the coordinates of b are permuted). The set of
possible values for I(σ ·b) so obtained are given, up to a factor of (1−q), by
J(b) = {⟨eφ(D), ω⟩: φ ∈Mod(C, B) ∼= Bn}.
(9.2)
Since I(b) has algebraic singularities, it is a (multivalued) algebraic function
of b iﬀJ(b) is ﬁnite.
To evaluate |J(b)|, ﬁrst assume k/d̸ = 1/n. Then ω is a diﬀerential of
the second kind. To see this, let e = gcd(n, d). Then T e ﬁxes every p ∈P,
and satisﬁes
Res(ω, p) = Res((T e)∗ω, p) = qe Res(ω, p);
so the residues of ω vanish if e < d. On the other hand, if e = d then
k/d ≥2/n, which implies ω is actually a holomorphic 1-form on the whole
of X.
41
Since ω is of the second kind, it deﬁnes a cohomology class in H1(X).
Thus the pairing in (9.2) depends only on the class of eφ(D) ∈H1(X), and
therefore
J(b) = ⟨D, ρq(Bn) · ω⟩.
Clearly J(b) is ﬁnite if ρq(Bn) is ﬁnite. We also note that
0̸ = [D] ∈H1(X)∗
q,
(9.3)
because there exist conﬁgurations b such that I(b)̸ = 0 (e.g. when all bi ∈
R). So conversely, if J(b) is ﬁnite, then one of the ‘matrix entries’ of ρq :
Bn →U(H1(X)q) assumes only ﬁnitely many values; but ρq is irreducible
(Corollary 5.3), so this implies ρq(Bn) is ﬁnite as well.
It remains to show that J(b) is inﬁnite when k/d = 1/n. In this case
ω has simple poles along P and |P| = d. Write P = {p0, . . . , pd−1} with
pi = T(p0). Since ω is an eigenform, it satisﬁes
Res(ω, pi) = qi Res(ω, p0)̸ = 0.
The idea is to show that I(b) can be made to take on inﬁnitely many diﬀerent
values by pushing the path of integration repeatedly through inﬁnity, so it
picks up a residue of ω. Note that (9.3) continues to hold, e.g. by considering
one of the Galois conjugates of q.
Choose a cycle C ∈H1(X, Z) such that
0̸ = E =
d
X
i=1
qiT i(C) ∈H1(X)q ∼= H1(X)∗
q.
(9.4)
(Most cycles have this property). Represent C by a closed loop on X that
begins and ends at p0, and otherwise avoids P ∪eB. Then the projection of
C to bC gives a loop γ ∈π1(bC −B, ∞).
Let φ ∈Modc(C, B) be a mapping class that pushes ∞once around γ,
and maps to the identity in Mod(bC, B). Then its canonical lift eφ ∈Mod(X−
P) pushes pi once around the cycle Ci, where C0 = C and Ci = T i(C0); and
eφ maps to the identity in Mod(X). In particular, by (9.1) we have
⟨eφ(D), ω⟩
=
⟨D, ω⟩+
d
X
1
(Ci · D) Res(ω, pi)
=
⟨D, ω⟩+ Res(ω, p0)(E · D).
Similarly, we have
⟨eφk(D), ω⟩= ⟨D, ω⟩+ k Res(ω, p0)(E · D).
42
Thus J(b) is inﬁnite provided E · D̸ = 0, or more generally if E · eψ(D)̸ = 0
for some ψ ∈Modc(C, B). But if these intersection numbers are all zero,
then E = 0 or D = 0, since Bn acts irreducibly on H1(X)q. This contradicts
equations (9.3) and (9.4).
Genus 3 revisited.
Here is an explicit formula for one of the alge-
braic integrals provided by Theorem 9.1.
We have normalized so that
(b1, b2, b3, b4) = (0, 1, a, b).
Theorem 9.3 For 1 < a < b < ∞, the deﬁnite integral
I(a, b) =
Z 1
0
dx
(x(x −1)(x −a)(x −b))3/4
satisﬁes
I(a, b)4
=
16π2Γ(1/4)4
Γ(3/4)4
·
c(1 + c −2ac)4
a2(a −1)2(a −b)3(c2 −1)4 ,
where c > 1 is the largest root of the quadratic equation
(a −b)c2 + (4ab −2a −2b)c + (a −b) = 0.
Eliminating c, we obtain the expression:
I(a, b)4 = π2Γ(1/4)4
Γ(3/4)4 ·
((2a −1)
p
b(b −1) + (2b −1)
p
a(a −1))4
a2b2(a −1)2(b −1)2(a + b −2ab −2
p
ab(a −1)(b −1))3 ,
which exhibits the solution’s symmetry in a and b.
Proof of Theorem 9.3. As in §8, we use the fact that the conﬁguration
B = {0, 1, a, b} ⊂bC has an order-two M¨obius symmetry g(x) satisfying
g(0) = 1 and g(a) = b. (The point c has a natural meaning: it is the unique
ﬁxed point of g between a and b.) Thus by changing coordinates so the
ﬁxed points of g become x = 0 and x = ∞, we can transform I(a, b) into an
integral of the form:
Z 1
−1
(Ax + C) dx
((x2 −1)(x2 −d2))3/4 ·
The integrand is now a sum of elliptic diﬀerentials for the square torus, as
discussed in §8. The term Ax can be ignored because it is odd; evaluating
the remaining integral in terms of Γ-functions, we obtain the formula given
in Theorem 9.3.
43
Remark. If we change the exponent µ = 3/4 to 1/2, we essentially obtain
the complete elliptic integral of the ﬁrst kind,
K(k) =
Z 1
0
dx
√
1 −x2√
1 −k2x2 .
This is a transcendental function of k, deﬁned classically by the relation
sn(K, k) = 1 [WW, §22.3].
Notes and references. The values (α, β, γ) such that
I(b) =
Z 1
0
xα(x −1)β(x −b)γ dx
is an algebraic function of b were determined by Schwarz in 1873 [Sch, §VI];
see [CW2] for a generalization to multivariable hypergeometric integrals,
which includes Theorem 9.1 as a special case. The failure of algebraicity
when ω has nonzero residues (e.g. when µ = 1/n in Theorem 9.1) is discussed
by Klein in [Kl, §49], which corrects a statement of Riemann.
