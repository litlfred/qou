---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-008-10-the-asymptotic-of-probability-measures-for-uq
section_title: "The asymptotic of probability measures for uq(sl2)"
section_number: 10
pages: 28-30
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
10.1. Corresponding Markov processes.
10.1.1. Probabilistic measures induced by Markov processes. Let X be a countable set. A
local Markov process on X is a collection of transition probabilities {Prob(x→ y)}x,y∈X, i.e.
0≤ Prob(x→y)≤ 1, such that
• for each x there are only finitely many y such that Prob(x→y)̸= 0,
• P
y
Prob(x→y) = 1, i.e. x with probability 1 will transition to some y.
Let{p(x)} be a probability measure on X, i.e. for each x∈X, 0≤p(x)≤ 1 and P
x
p(x) = 1.
We will say it is local, if p(x)̸= 0 only for finitely many x∈X.
One of the fundamental properties of Markov processes is that function
pN(x) = (ProbNp)(x) =
X
x1,x2,...,xN
p(x1)Prob(x1→x2)... Prob(xN→x)
is a probability measure on X for each N∈ Z>0, N≥ 2. For each such N it is local if p(x)
is local and the Markov process is local. In particular, if p(x) = δx,x0 by applying repeatedly
a local Markov process to such distribution we have a sequence of probability distributions on
X:
px0(x) =
X
x1,x2,...,xN−1
Prob(x0→x1)... Prob(xN−1→x)
It turned out that character and Plancherel measures introduced earlier are exactly of this
nature.
10.1.2. Character and Plancherel measures for Uq(sl2). Consider the Markov process on Z≥0
with transition probabilities determined by tensor product decomposition (4):
Prob(n→m) = chT (m)(x) dim Hom(T (n)⊗T (1),T (m))
chT (n)(x)chT (1)(x)
Here x = et > 0 which ensures positivity of transition probabilities. The Markov propertyP
m Prob(n→ m) = 1 is guaranteed by the decomposition rule of the tensor product. The
character measure on the set of tilting components of T (1)⊗N can be regarded as a probability
distribution on Z≥0 induced by this Markov process.
The probability p(l)
N (k;t) is the result of iteration of this random process starting from the
distribution supported at k = 0, i.e. from p(l)
0 (k;t) =δk,0:
p(l)
N (k;t) =
X
γ
Prob(0→ 1)Prob(1→k2)... Prob(kN−1→k)
TENSOR POWERS 29
Here the sum is taken over all lattice paths described in Section 6.1. A path γ starts at the
origin, follows the rules of elementary steps and ends at k after N + 1 steps (ki,ki+1).
Specializing the character measure to t = 0 we obtain the Markov process interpretation of
the Plancherel measure for Uq(sl2). The results on the asymptotic of probability measures for
Uq(sl2) can also be obtained by analyzing this Markov process. It will be done in a separate
publication.
10.1.3. Plancherel and quantum Plancherel measures for uq(sl2). The decomposition rules 5
define two natural Markov processes on {0, 1,..., 3l− 2}:
(17) Prob( n→m) = dm dim Hom(T (n)⊗T (1),T (m))
dnd1
.
Here T (n) are representations T (n) of uq(sl2) as described in Section 8.2. For Plancherel
and quantum Plancherel dn are dimensions dim T (n) and quantum dimensions dim qT (n) of
representationT (n) correspondingly, see Sections 8.2 and 8.3.
10.2. The asymptotic of Plancherel and quantum Plancherel measures on uq(sl2)-
modules. The asymptotic of these measures can be computed directly from the analysis of
multiplicities. But it is much easier to use Markov processes in this case.
10.2.1. Plancherel measure. For the small quantum group the Markov matrix (17) is a real
3l− 1× 3l− 1 matrix with non-negative matrix elements:
Prob(k→k + 1) =



k+2
2(k+1), if 0≤k≤l− 2
1, if k =l− 1, 2l− 1
0, if k = 3l− 2
1
2, if else
Prob(k→k− 1) =



k
2(k+1), if 0≤k≤l− 2
0, if k =l− 1, 2l− 1
1
2, if else
Prob(3l− 2→l− 1) = 1
2.
It is not difficult to check explicitly that its largest eigenvalue λmax = 1 and that it has
multiplicity 1. Thus the stationary distribution in this case is given by components of the
eigenvector corresponding to the largest eigenvalue of the Markov matrix. Straightforward
computation shows that it is given by
(p0,...,p 3l−2),
where
pj =



0, if k≤l− 2
2l−1−k
l2 , if l≤k≤ 2l− 2,
3l−1−k
l2 , if 2l≤k≤ 3l− 2,
1
2l, if k =l− 1 or k = 2l− 1.
30 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
It is normalized to the total probability condition
3l−2X
j=0
pj = 1.
10.2.2. Quantum Plancherel measure. The Markov matrix for the quantum Plancherel measure
is given by transition probabilities
Prob(k→k + 1) =
( qk+2−q−(k+2)
(qk+1−q−(k+1))(q+q−1), if 0≤k≤l− 3
0, if k =l− 2
Prob(k→k− 1) =
( qk−q−k
(qk+1−q−(k+1))(q+q−1), if 0≤k≤l− 3
1, if k =l− 2
It is al−1×l−1 matrix supported on irreducible representations because quantum dimensions
of other indecomposable summands in T (1)⊗N vanish. The largest eigenvalue λmax = 1 of this
matrix has multiplicity 1. It is not difficult to compute components of the corresponding
eigenvector (p0,...,p l−2):
pj =−(qj+1−q−(j+1))2
2l =
2sin2

π(j+1)
l

l .
It is normalized to the total probability condition
l−2X
j=0
pj = 1.
