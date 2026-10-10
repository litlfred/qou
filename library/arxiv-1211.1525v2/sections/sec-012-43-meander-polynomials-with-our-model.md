---
doc_id: arxiv-1211.1525v2
doc_title: "PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES: EXACT FORMULAS AND MEANDERS"
section_id: sec-012-43-meander-polynomials-with-our-model
section_title: "Meander polynomials with our model"
section_number: 4.3
pages: 19-21
source_pdf: 1211.1525v2.pdf
source_sha256: 51ff1c8f90c025a4
toc_source: outline
---
where c = 1, where our model gives the meander polynomials.
Theorem 4.2. If m
n →c = 1 and q ∈N then the 2q-th moment of µlmρΓ
converges as n →∞to the meander polynomial Mq(l).
20
MOTOHISA FUKUDA AND PIOTR ´SNIADY
(A)
(B)
FIGURE 4. (a) graphical representation of a noncrossing
partition

{1, 3, 4}{2}
	
∈NC(4), (b) the corresponding
noncrossing pair-partition from NC2(8).
FIGURE 5. Graphical representation of noncrossing parti-
tions τ1 = (1, 3, 5)(7) and τ2 = (2, 8)(4, 6)
Proof. First, since c = 1
(4.5)
(4.2) =
X
τ1,τ2
l#[π−1(τ1⊕τ2)].
Here, τ1 ∈NC({1, 3, . . . , p −1}) and τ2 ∈NC({2, 4, . . . , p}).
Next, we recall the well-known bijection between NC(q) and NC2(2q).
We represent a noncrossing partition as in Figure 4a. We add two points i−
and i+ for both sides of each i ∈[q], left and right respectively. Then we
connect i+ and j−if α(i) = j. The example is drawn in Figure 4b, where
we also use arrows to show the action of the permutation α. This procedure
is commonly known as fattening.
PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES
21
Finally, we will calculate #[π−1(τ1 ⊕τ2)].
To understand the loop-
structure of π−1(τ1 ⊕τ2) we note that τ1 and τ2 act in turn; τ1 acts on odd
numbers and τ2 even numbers, but π−1 switches parities. For this reason,
we suggest the following graphical representation, see Figure 5.
(1) We draw two parallel horizontal straight lines with odd-numbered
points on the upper line and even-numbered points on the lower line.
(2) Draw the graphical representation for τ1 above the upper line and
the graphical representation for τ2 below the lower line.
(3) Identify respectively (2i + 1)−and (2i)+, and then (2i)−and (2i −
1)+.
Here, note that the last step corresponds to the action of π−1. An example
with is drawn in Figure 5. Since we can think of τ1 and τ2 as elements of
NC2(2q), identifying 1−1 and 2q+ reduces (4.5) into the meander polyno-
mials Mq(l).
□
To compare our result with an existing matrix model for the meander
polynomial, we quote a result of Di Francesco [DF01, Eqs. (6)–(9)]:
Mq(l) = lim
N→∞
1
N 2
l
X
a1,a2,...,a2q=1
E
h

Tr

Ba1Ba2 · · · Ba2q


2i
.
Here, {B1, . . . , Bl} are i.i.d. random N × N Hermitian matrices such that
E [(B)xy(B)zw] = 1
N δxwδyz.
On the other hand, our model of partial transposed random quantum states
can be modiﬁed for the meander polynomial in the following way:
Corollary 4.3. Take random complex Gaussian matrices G of n2 ×l, where
Gxy = axy+bxyi and axy, bxy are i.i.d. real Gaussian distribution with mean
0 and variance
1
2n. Then,
Mq(l) = lim
n→∞
1
n2 Tr E

(GG∗)Γ2q
.
