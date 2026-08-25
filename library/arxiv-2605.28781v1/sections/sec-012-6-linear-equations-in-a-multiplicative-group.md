---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-012-6-linear-equations-in-a-multiplicative-group
section_title: "Linear equations in a multiplicative group"
section_number: 6
pages: 12-14
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
Let Γ≤C × be a multiplicative group. A natural question is how many solutions
the equation
(6.1)x 1 +···+x k = 1
can have withx i∈Γ. We are concerned only with non-degenerate solutions, which
are those such that P
i∈Ixi ̸= 0 for every non-emptyI⊆{1,...,k}. Building
on a sequence of earlier results, Evertse, Schlickewei, and Schmidt [16] proved the
following.
Theorem 6.1(Evertse-Schlickewei-Schmidt).IfΓ≤C × is a multiplicative group
of rankdthen, for anyk≥2, the number of non-degenerate solutions to(6.1)is
at most
exp(Ckd)
for some constantC k >0depending only onk.
THE SUM-PRODUCT CONJECTURE IS F ALSE FOR REAL NUMBERS 13
They gaveC k as an explicit function ofk, which has been improved (most
recently by Amoroso and Viada [3], and is now polynomial ink), but here we are
most concerned with the dependence on the rankd.
Erd˝ os, Stewart, and Tijdeman [12] constructed,2 for anyk≥2 and large enough
d, multiplicative groups Γ≤Q × of rankdin which the number of non-degenerate
solutions to (6.1) is at least
exp
 
ck
 d
logd
1− 1
k
!
for somec k >0. This has been improved in some regimes by Konyagin and
Soundararajan [24] (again for Γ≤Q ×).
It has been conjectured (see, for example, [16]) that the dependence ondin
Theorem 6.1 can be improved, perhaps to exp(C kd1−ck) for somec k >0. Our
construction is also able to disprove this, and shows that the linear dependence on
din the exponent is the best possible. Again, we stress that our construction makes
heavy use of algebraic number fields of large degree, and so it remains possible that
the dependence ondin the upper bound can be improved if Γ≤Q ×, for example.
Theorem 6.2.There is an absolute constantC >0such that the following holds.
Letk≥Cbe any integer. There exist infinitely manyd≥2and multiplicative
groupsΓ≤R × of rank≤dsuch that there are at least
exp((C−1klogk)d)
many non-degenerate solutions to(6.1).
Proof.LetKbe a totally real number field of degreedwith ∆ K≤C d for some
constantC >0, as provided by Theorem 3.2. LetAbe constructed as in Lemma 4.2
(so it is a ball of lattice points in the multiplicative unit lattice ofK), viewed as a
subset ofR. Note that the unit group has rankd−1. Losing only a factor of 2 in
|A|we can assume thata >0 for alla∈A. We therefore obtain, for anyY≥2,
infinitely manydwith accompanyingA(contained in a multiplicative group of rank
d−1) such that|A|≥(cY) d−1 and
|kA|≤(Cke Y )d
for some constantsc,C >0. By the pigeonhole principle there exists somex∈kA
such that
a1 +···+a k =x
has at least
|A|k
|kA|≥ (cY)k(d−1)
(CkeY )d ≥Y −k
(cY)k
CkeY
d
many solutions. Lettingz i =a i/x, and expanding the group of units with the
generatorx, we achieve at least this many solutions to (6.1) in a multiplicative
group of rank at mostd. Furthermore, sincez i >0, all of these solutions are
automatically non-degenerate.
The conclusion then follows from takingY=k.□
2In [12] they just address the casek= 2, but this is straightforward to generalise to arbitrary
k≥2 as indicated in [16].
14 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
A related question is to bound the number of solutions to (6.1) in the group of
unitsO ×
K. Evertse [14] proved that the number of solutions tox 1 +x 2 = 1 with
x1,x 2∈O ×
K is at most 3·7 3d, wheredis the degree ofK. (Suchx i are often
called ‘exceptional units’.) Niklasch [34] considered this question further and in
particular, generalising a conjecture of Stewart (see [15, p.120]), conjectured [34,
Conjecture 4.2] the sub-exponential upper bound of
exp(d2/3+o(1)).
We are able to prove that if we consider the analogous question with 2 variables
replaced by a sufficiently large (but still a constant) number of variables, the anal-
ogous conjecture is false, and in fact there are exponentially indmany solutions.
Theorem 6.3.There exists an integerk≥2and an absolute constantC >1such
that, for infinitely manyd, there exists a number fieldKof degreedsuch that there
are at leastC d non-degenerate solutions to(6.1)withx i∈O×
K.
This is, in hindsight, a simple consequence of the fact that units of bounded
height still have small height afterO(1) many sums, and so the size of theirk-fold
sumset is small. To highlight the simplicity of the example we will present the
construction from first principles, at the cost of some slight repetition of earlier
arguments.
Proof.LetC >0 be the constant provided by Theorem 3.2, and letKbe a number
field of degreedand discriminant ∆ K≤C d. LetY≥1 be some constant to be
chosen later, and letA=B ×(Y)⊂O ×
K, so that by Lemma 3.1 and Lemma 3.5
|A|≥Y d−1d−1/2C−d.
SinceB×(Y)⊆B +(eY ),kA⊆B +(keY ), and hence by Lemma 3.3
|kA|≤(2ke Y + 1)d≤(3ke Y )d,
say. By the Cauchy-Schwarz inequality it follows that
#{x1 +···+x k =y 1 +···+y k :x i,yi∈A}≥ |A|2k
|kA| ≥|A| 3k/2,
say, provided we first chooseYto be some large constant depending onC, and then
ksome larger constant depending onY. By H¨ older’s inequality (see, for example,
the proof of [1, Lemma 5]) the left-hand side is at most
Ck2
|A|k +X
for some constantC >1, whereXcounts the number of solutions tox 1+···−y k = 0
in which no subsum on the left-hand side vanishes. HenceX≥|A| k/4, say, provided
dis sufficiently large, which concludes the proof (using that−1∈O ×
K and dilating
by some fixedy k∈A).□
7.V ariants
