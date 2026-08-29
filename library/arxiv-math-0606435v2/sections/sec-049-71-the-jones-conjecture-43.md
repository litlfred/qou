---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-049-71-the-jones-conjecture-43
section_title: "The Jones conjecture 43"
section_number: 7.1
pages: 43-45
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
in contradiction to (45).
The effort focusses on the other braids β = µ∗ for µ = σ6a−1
1 σ2. In this case we consider ! K, whose Xu form has
only negative bands. The inequalities (13) show that we must rule out a braid representation β′′ ∈ Bn′ of !K with
[β′′] = wmin(!K) +2 + (n′ − 3), where (we set in the samea posteriori to be justiﬁed manner) wmin(!K) = −2g(K) − 2.
We prohibit β′′ by evaluating the 2-cable skein polynomial P(ˆγa) of !K for
γa = [ 4354] · [2132]6a−1(∆2
6)−2a ∈ B6,(46)
with a > 1 and ∆2
6 = [12345]6 generating the center of B6, and showing that the polynomial has non-zero terms in
v-degree [γa] − 5 or [γa] − 3. This may appear a banality, but in fact requires a substantial use of Jones’ work in [J].
Consider the more general 6-braids
βk,l := [ 4354] · [2132]k ∆2l
6 .
(We are of course only interested in the special case k = 6a − 1, l = −2a and a > 1, but it is useful to treat the
2-parameter family ﬁrst.)
The skein polynomial of ˆβk,l can be evaluated using the representation theory in [J]. We a dopt the convention that
all references to lemmas, page and paragraph numbers, equations of the form (x.y), etc. for the rest of this proof are
understood to be to Jones’s paper, unless noted otherwise.
Jones’s version of the skein polynomial,
X(q,λ) = P(v,z) with v =
√
λq and z = √q − 1/ √q ,
can be evaluated on a closed n-braid β by a weighted sum, with weights WY in λ and q, of traces (in q) of irreducible
representations (irreps) πY of Bn, indexed by Young diagrams (or tableaux1) Y, or equivalently by partitions of n. (A
partition of n is a tuple (n1, . . . ,nk) with nk > 0, ni ≥ ni+1 and ∑ ni = n.) We may identify the Young diagram with
its partition, counting partitions in horizontal rows. For example the partition (4) = means one row (trivial
representation), while (1111) = means one column (parity representation); thus π3,1 = π . Since the calculation
of WY was given in [J], we will not repeat it in detail. We will also deal (mostly) with Y where the calculation of πY is
explained in [J].
Using Deﬁnition 6.1 (of [J]), (5.5) and the formula for WY (q,λ) from p. 347 top, one has for a 6-braid β of exponent
sum e = [β],
Xˆβ(q,λ) = −
√
λ
e−5
∑
Y ⊢6
~WY (q,λ)tr πY (β) .(47)
Here ~WY denote the slightly rescaled weights
~WY (q,λ) = RY (q,λ)
QY (q) · 1 − q
1 − λq ,
with RY being speciﬁed on p. 347 after Figure 5.6, and QY (q) being the hook length product term from p. 346 middle.
The symbol ‘⊢’ is taken from partition theorists and is used to mean here th at Y is a Young tableau of 6 boxes (or
equivalently a partition of 6). In order to avoid denominators it is useful to multiply (47) by (1 − q2) · . . .· (1 − q6), so
−(1 − q2) · . . .· (1 − q6)Xˆβ =
√
λ
e−5
∑
Y ⊢6
ˆWY (q,λ)tr πY (β) ,(48)
with
ˆWY (q,λ) = RY (q,λ)
1 − λq · (1 − q)(1 − q2) · . . .· (1 − q6)
QY (q)
becoming a Laurent polynomial in λ and q .
1Here consistently ‘tableau’ is used as a synonym for (Young)diagram, i.e. with no additional information attached to it.
44 7 Applications of the representation theory
Note that πY are representations that involve only the variable q, not λ. The obvious question is how to evaluate their
traces.
Consider ﬁrst
βk = βk,0 = [ 4354] [2312]k .
There are 11 Young diagrams Y of 6 boxes. Now βk ∈ B4 ⊂ B6, and according to p. 340 top, the restriction of πY to
B4 splits into a direct sum of representations πY ′ indexed by 4-box Young diagramsY ′, which we name for shorthand
A = B = C = D = E = .(49)
The representations πY ′ are clariﬁed completely in §8 (see also §7.2 in this paper below). Denote by ψ n−1 the (reduced)
(n − 1)-dimensional representation of Bn; see §2. Let us also write −1 for the parity representation (−1)[ .], and
−ρ = −1 ⊗ ρ for the direct (tensor, or Kronecker) product of a represent ation ρ with the parity. Then πA = −1,
πE is given by q[ .], πB = −ψ 3 (Note 5.7; the sign disappears here, though, because for us a lways e = [β] is even),
πD = − V2 ψ 3 and πE = π ◦ , with being the homomorphism B4 → B3 given by σ1,2,3 = σ1,2,1 (p. 355). Also
π = −ψ 2.
Let us write below Y for the transposed (or dual) Young diagram to Y , given by exchanging rows and columns. For
example, for Y = , we have Y = . The relation between πY and πY is given in Note 4.6.
Now ψ 3(α) and ψ 2( ¯α) for
α = [2132]
are easy to calculate (see §2). We ﬁnd former’s eigenvalues to be ±t and −t2, and latter’st and t3. In particular, both
matrices are diagonalizable (because the eigenvalues are d istinct for generic t). Setting t = q as in Note 5.7, then we
have the following table of eigenvalues of the πY ′(α)
A B C D E
1 −q q3 −q3 q4
q q q3
−q2 −q2
i 1 2 3 4 5 6 7
δi 1 q4 q −q −q2 q3 −q3
Let us number the 7 possible eigenvalues of π′
Y (α) by δi as shown on the right.
Thus πY (α) are all diagonalizable, with eigenvalues δi. The multiplicities of πY ′ in πY are also easy to calculate. They
are the number of descending paths from Y ′ to Y in the Figure 3.3 (continued one more row to the bottom). Tabl e 1
shows the multiplicities of πY ′ (in the shorthand of (49)) in πY and the resulting ones, which we write M(i,Y ), of the
eigenvalues δi in πY (α).
Since with πY ′(α) also all πY (α) are diagonalizable, we have
tr πY (βk) = tr πY (αk · [4354]) =
7
∑
i=1
c(i,Y ) δk
i ,(50)
with c(i,Y ) given as follows. Consider πY ([4354]) in the basis of πY that diagonalizes πY (α). Then to obtain c(i,Y ),
sum the ( j, j)-entries of the matrix of πY ([4354]) over rows/columns j, for which the ( j, j)-entry of πY (α) is δi.
So the problem to evaluate trπY (βk) transforms into the one to determine c(i,Y ). There are a priori 77 of those, given
by combining 7 eigenvalues δi with 11 Young diagrams Y. However, one immediately notes that clearly c(i,Y ) = 0
when M(i,Y ) = 0. This leaves 45 of the 77 values.
If we can calculate tr πY for general 6-braids, then we can use (50) as a linear equatio n for c(i,Y ). If πY (α) has lY
different eigenvalues, we can determine c(i,Y ) for that Y by calculating the l.h.s. of (50) for lY different values of k
and solving for c(i,Y ). (Always lY ≤ 6, as evident from table 1.)
