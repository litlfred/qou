---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-012-6-linear-equations-in-a-multiplicative-group
section_title: "Linear equations in a multiplicative group"
section_number: 6
pages: 12-14
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
Let Γ ≤C× be a multiplicative group. A natural question is how many solutions
the equation
(6.1)
x1 + · · · + xk = 1
can have with xi ∈Γ. We are concerned only with non-degenerate solutions, which
are those such that P
i∈I xi̸ = 0 for every non-empty I ⊆{1, . . . , k}. Building
on a sequence of earlier results, Evertse, Schlickewei, and Schmidt [16] proved the
following.
Theorem 6.1 (Evertse-Schlickewei-Schmidt). If Γ ≤C× is a multiplicative group
of rank d then, for any k ≥2, the number of non-degenerate solutions to (6.1) is
at most
exp(Ckd)
for some constant Ck > 0 depending only on k.
THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS
13
They gave Ck as an explicit function of k, which has been improved (most
recently by Amoroso and Viada [3], and is now polynomial in k), but here we are
most concerned with the dependence on the rank d.
Erd˝os, Stewart, and Tijdeman [12] constructed,2 for any k ≥2 and large enough
d, multiplicative groups Γ ≤Q× of rank d in which the number of non-degenerate
solutions to (6.1) is at least
exp
 
ck

d
log d
1−1
k !
for some ck > 0.
This has been improved in some regimes by Konyagin and
Soundararajan [24] (again for Γ ≤Q×).
It has been conjectured (see, for example, [16]) that the dependence on d in
Theorem 6.1 can be improved, perhaps to exp(Ckd1−ck) for some ck > 0. Our
construction is also able to disprove this, and shows that the linear dependence on
d in the exponent is the best possible. Again, we stress that our construction makes
heavy use of algebraic number fields of large degree, and so it remains possible that
the dependence on d in the upper bound can be improved if Γ ≤Q×, for example.
Theorem 6.2. There is an absolute constant C > 0 such that the following holds.
Let k ≥C be any integer. There exist infinitely many d ≥2 and multiplicative
groups Γ ≤R× of rank ≤d such that there are at least
exp((C−1k log k)d)
many non-degenerate solutions to (6.1).
Proof. Let K be a totally real number field of degree d with ∆K ≤Cd for some
constant C > 0, as provided by Theorem 3.2. Let A be constructed as in Lemma 4.2
(so it is a ball of lattice points in the multiplicative unit lattice of K), viewed as a
subset of R. Note that the unit group has rank d −1. Losing only a factor of 2 in
|A| we can assume that a > 0 for all a ∈A. We therefore obtain, for any Y ≥2,
infinitely many d with accompanying A (contained in a multiplicative group of rank
d −1) such that |A| ≥(cY )d−1 and
|kA| ≤(CkeY )d
for some constants c, C > 0. By the pigeonhole principle there exists some x ∈kA
such that
a1 + · · · + ak = x
has at least
|A|k
|kA| ≥(cY )k(d−1)
(CkeY )d
≥Y −k
(cY )k
CkeY
d
many solutions. Letting zi = ai/x, and expanding the group of units with the
generator x, we achieve at least this many solutions to (6.1) in a multiplicative
group of rank at most d.
Furthermore, since zi > 0, all of these solutions are
automatically non-degenerate.
The conclusion then follows from taking Y = k.
□
2In [12] they just address the case k = 2, but this is straightforward to generalise to arbitrary
k ≥2 as indicated in [16].
14
THOMAS F. BLOOM, WILL SAWIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
Since B×(Y ) ⊆B+(eY ), kA ⊆B+(keY ), and hence by Lemma 3.3
say. By the Cauchy-Schwarz inequality it follows that
#{x1 + · · · + xk = y1 + · · · + yk : xi, yi ∈A} ≥|A|2k
Ck2|A|k + X
