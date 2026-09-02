---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-008-rational-operations-on-generating-functions
section_title: "Rational operations on generating functions"
section_number: null
pages: 38-48
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
A combinatorial class (in d variables) is a setA together with a partition ofA
into ﬁnite sets{Ar :r∈Nd} encoded by the weight mapφ of the class, which
takesx∈A to the unique indexφ(x) =r∈Nd withx∈Ar. In one variable,
we have a disjoint union A =∪∞
n=0An and call the weight function φ(x) the
size of x∈A , so thatAn contains the number of elements inA of size n.
Exercise 2.3. Prove that the objects in any combinatorial class form a (possi-
bly ﬁnite) countable set.
The generating function of the combinatorial classA is the formal power
series
A(z) =
∑
x∈A
zφ(x) =
∑
r∈Nd
|Ar|zr∈C[[z]],
and we say that A enumeratesA under the weightingφ.
Arithmetic operations in the ring of formal power series were deﬁned so
as to correspond to existing operations on analytic power series. However, it
is instructive to interpret these operations combinatorially. We begin with a
list of set-theoretic interpretations for rational operations; the combinatorial
wealth of these interpretations helps explain why there are so many rational
generating functions in combinatorics.
Equality corresponds to bijection
Equality between two generating functions A and B corresponds to bijective
correspondence between the classes A andB that they enumerate, because
A(z) = B(z) as formal series if and only if|Ar| =|Br| for allr∈Nd.
Multiplying by z j corresponds to re-indexing
In the univariate case, the product zF(z) enumerates the right-shifted sequence
0, a0, a1, a2,... . More generally, the productz jF(z) enumerates the right-shifted
array{ar−δ j}, where ar−δ j is deﬁned to be zero if any coordinate of r−δ j
is negative. Conversely, the left-shifted sequence {ar+δ j} is enumerated by
(F(z)− F j(z))/z j, where F j(z) = [z0
j]F(z) is obtained from F by taking only
the terms that are free of z j.
Sum corresponds to disjoint union
If A(z) and B(z) enumerate classesA andB, respectively, then A(z) + B(z)
enumerates the disjoint union classC =A⊔B whereCr is the disjoint union
2.2 Rational operations on generating functions 21
ofAr andBr (so that objects from A are always considered distinct from
objects inB).
The combinatorial interpretations of equality, multiplication by variables
and disjoint union are fairly simple, but already yield interesting examples.
Example 2.1 (binary sequences with no repeated 1s) . LetAn be the set of
sequences of 0s and 1s of length n that do not begin with 1 and have no two
consecutive 1s. Each such sequence ends either in 0 or in 01, and the previous
terms can be any sequence in An−1 orAn−2, respectively. Thus, stripping oﬀ
the last one or two symbols yields a bijective correspondence betweenAn and
the disjoint unionAn−1⊔A n−2. At the generating function level, this would
translate to A(z) = zA(z) + z2A(z), except the correspondence fails for n = 0 (it
works for n = 1 if we takeAn to be empty for n< 0). If we considerA to have
a single object of size zero (the empty string) then correcting for this base case
gives the equation
A(z) = 1 + zA(z) + z2A(z).
Formal power series manipulations then allow us to rearrange and divide by
1− z− z2 to obtain the generating function
A(z) = 1
1− z− z2 = 1 + z + 2z2 + 3z3 + 5z4 +···
enumerating binary sequences with no repeated 1s. One may recognizeA(z) as
the (shifted) generating function for the Fibonacci numbers. ◁
Example 2.2 (binomial coeﬃcients). LetAr,s be the set of colorings of the
set [ r + s] = {1,..., r + s} for which r elements are red and s are green.
Decomposing according to the color of the last element, Ar+s is in bijective
correspondence with the disjoint union of Ar−1,s andAr,s−1. This is a com-
binatorial interpretation of the identity
(r + s
r
)
=
(r + s− 1
r
)
+
(r + s− 1
r− 1
)
and
holds as long as r + s> 0. It follows that F(x, y)− 1 = xF(x, y) + yF(x, y), and
solving for F gives the generating function
F(x, y) = 1
1− x− y =
∑
r,s≥0
(r + s
r
)
xrys
of the binomial coeﬃcients. ◁
Product corresponds to convolution
Let A(z) and B(z) enumerate classesA andB, respectively. The deﬁnition of
multiplication of power series shows that A(z)B(z) enumerates the product
22 Generating functions
classC = A×B deﬁned by letting Cr be the disjoint union of Cartesian
productsAs×Br−s over alls∈Nd that are coordinatewise less than or equal to
r. This is the canonical deﬁnition of product in any category of graded objects.
Students of probability theory will recognize the product class as a convolu-
tion. Suppose that F and G are any power series with nonnegative coeﬃcients
whose sets of coeﬃcients both sum to 1. Then F is the probability generating
function for a probability distribution on Nd that gives mass [ zr]F(z) to the
pointsr∈ Nd, and the analogous result holds for G. The series coe ﬃcients
in the product FG characterize the convolution of these distributions, which is
the distribution of the sum of independent picks from the two given distribu-
tions. Thus the study of sums of independent, identically distributed random
variables taking values inNd is subsumed by the study of powers of generating
functions. The laws of large numbers in probability theory may be derived via
generating function analyses, and the central limit theorem is usually proved
this way. In Chapter 12, versions of these laws are proved for coe ﬃcients of
generating functions beyond powers of probability generating functions.
Example 2.3 (enumerating partial sums) . Let A(z) enumerate a class A and
let B(z) = 1/(1−z) enumerate the classB with|Bn| = 1 for all n. Then A(z)B(z)
enumerates the classC whereCn is the disjoint union⊔n
j=0A j of objects inA
with size at most n, and the coeﬃcients of C(z) = A(z)/(1− z) form the partial
sum sequence cn = ∑n
j=0 a j. ◁
Quasi-inverse corresponds to ﬁnite tuples
LetB be a combinatorial class with B0 =∅. Then we can construct the se-
quence classA = SEQ(B) containing all ﬁnite tuples of elements ofB, where
Ar consists of all tuples ( x1,..., xk) ∈ Bk (of any length k) with φ(x1) +
··· + φ(xk) = r. For instance, in the univariate case An contains all ﬁnite
tuples of elements inB whose sizes sum to n. SinceA is the disjoint union of
the empty sequence, the class of singleton sequences, the class of sequences
of length 2, and so forth, we have the generating function equation A(z) =
1 + B(z) + B(z)2 +··· = 1/(1− B(z)), where convergence in the ring of formal
power series follows from the fact that B(0) =|B0| = 0.
Example 2.4 (binary strings by zeros and ones) . Consider the classA of bi-
nary strings in Example 2.1 enumerated by the number of zeros and the num-
ber of ones they contain, rather than by total length. Any such sequence can be
uniquely decomposed into a ﬁnite sequence of the blocks 0 and 01. IfB is the
combinatorial class containing these blocks, with weight functionφ(0) = (1, 0)
2.2 Rational operations on generating functions 23
andφ(01) = (1, 1) encoding the blocks by the number of zeros and ones they
contain, thenB has generating function x + xy. The generating function forA
is therefore A(x, y) = 1/(1− x− xy). Note that setting x = y = z recovers the
univariate generating function A(z, z) = 1/(1− z− z2) counting these strings by
total length. ◁
Example 2.5 (preﬁx codes). This example illustrates the use of preﬁx codes
to encode messages over an arbitrary alphabet using binary strings. Fix a ﬁnite
rooted planar binary tree T with at least two vertices such that every vertex has
exactly zero or exactly two children. We label each non-root vertexv of T with
the binary string obtained by taking the unique path from the root of T to v
and recording a 0 whenever we move to the left and a 1 whenever we move to
the right. Thus, the elements in T of distance d from the root are labeled with
binary strings of length d (we can consider the root itself to have the empty
string as its label).
Any binary string may be uniquely decomposed into blocks by repeatedly
stripping oﬀ the left-most substring that corresponds to a label of a leaf in T,
where the decomposition may end with a partial block corresponding to an
internal node of T. LetB be the class of binary sequences enumerated by their
length and the number of blocks they have under this decomposition. If L(x)
is the univariate generating function enumerating the number of leaves inT by
depth (i.e., distance to the root of T) then the subclass ofB containing strings
consisting of a single block under this decomposition has generating function
yL(x). If I(x) is the univariate generating function enumerating the internal
vertices in T by depth then 1 + y(I(x)− 1) enumerates the possible partial
blocks that a binary string can end with under our decomposition, including
having no partial block. As an arbitrary binary string can be uniquely split
into a sequence of blocks followed by a (possibly empty) partial block, the
generating function B(x, y) enumeratingB is
B(x, y) = 1 + y(I(x)− 1)
1− yL(x) .
To use a preﬁx code over the alphabet A one creates a binary tree T whose
leaves correspond to the symbols in A and parses a binary string into a word
over A using the block decomposition described above. The generating func-
tion B(x, y) encodes how many diﬀerent messages can be transmitted through
binary strings of a ﬁxed length (in applications one would like to pick the tree
T to maximize this quantity, perhaps under some constraints). ◁
The ﬁeld of lattice path enumeration also yields a large and well-studied
class of examples.
24 Generating functions
Example 2.6. Let S be a ﬁnite subset of Nd\{ 0}, let x0 = 0 and letA be
the class of ﬁnite tuples σ = (x0,x1,..., x𝓁) with elements in Nd such that
xk−xk−1 ∈ S for all 1 ≤ k ≤ 𝓁. The elements of A are the lattice paths
with steps in S (starting at the origin). The name lattice path comes from
concatenating the vectorsxk ofσ in the plane, giving a path of steps from the
origin to the endpointφ(σ) = ∑𝓁
k=0xk.
The polynomial S (z) = ∑
r∈Szr enumerates S by the endpoint of its steps,
so the generating function ofA with respect to the endpoint is A(z) = 1/(1−
S (z)). Many other combinatorial classes can be studied in the context of lattice
path enumeration, for instance the multinomial coe ﬃcient
( |r|
r1,...,rd
)
= (r1+···+rd)!
r1!···rd!
counts the number of paths ending at r with the step set S ={e1,..., ed} of
standard basis vectors, giving the generating function 1 /(1− ∑d
j=1 z j) for the
multinomial coeﬃcients. ◁
Example 2.7 (Delannoy numbers). IfA is the class of lattice paths inN2 using
the steps North (0, 1), East (1, 0), and Northeast (1, 1) enumerated by endpoint
then the counting sequencear =|Ar| deﬁnes the Delannoy numbers [Com74,
Exercise I.21]. The generating function x + y + xy for the set of steps leads to
the Delannoy generating function
F(x, y) = 1
1− x− y− xy.
◁
Example 2.8 (no gaps of size 2) . For any n ∈ N letBn be the collection
of all subsets of [ n] where no two consecutive members are absent. One can
enumerateBn by mapping bijectively to Example 2.1. In [CLP04] an estimate
was required on the number of such sets that were mapped into other sets of
the same form by a random permutation. That paper showed that in order to
compute the second moment of this random variable it su ﬃces to count the
pairs (S, T)∈ B2
n where the parameters n,|S|,|T|, and|S∩ T| are ﬁxed. To
that end, let F(x, y, z, w) be the 4-variable generating function for the class F
of all pairs ( S, T)∈B 2
n for any n∈ N, using the weight function φ(S, T) =
(n,|S|,|T|,|S∩ T|).
We may derive F by investigating what happens between consecutive ele-
ments of S∩ T. Identify (S, T)∈B 2
n with a sequence
α∈{ (0, 0), (0, 1), (1, 0), (1, 1)}n
2.2 Rational operations on generating functions 25
where
α j =

(1, 1) if j∈ S∩ T,
(1, 0) if j∈ S\ T,
(0, 1) if j∈ T\ S ,
(0, 0) if j< S∪ T.
If j and j + r are positions of consecutive occurrences of (1, 1) inα then the
possibilities for the stringα j+1··· α j+r are as follows.
(i) If α j+1 = (1, 1) then the only possibility is r = 1.
(ii) If α j+1 = (0, 0) then the only possibility is r = 2 and α j+1··· α j+r =
((0, 0), (1, 1)).
(iii) If α j+1 = (1, 0) then r≥ 2 may be arbitrary and α j+1··· α j+r alternates
between (1, 0) and (0, 1) until the ﬁnal (1, 1).
(iv) If α j+1 = (0, 1) then r≥ 2 may be arbitrary and α j+1··· α j+r alternates
between (0, 1) and (1, 0) until the ﬁnal (1, 1).
We will build an element ofF uniquely from blocks of one of these four types.
In the ﬁrst case, the generating function G1(x, y, z, w) for a single block is sim-
ply xyzw, while in the second case we obtain G2(x, y, z, w) = x2yzw. In the
third case, we can write the block as either ((1 , 0)) or ((1, 0), (0, 1)), followed
by zero or more alternations of length two; decomposing this way shows the
generating function to be G3(x, y, z, w) = xyzw xy+x2yz
1−x2yz . Similarly, in the fourth
case we obtain G4(x, y, z, w) = xyzw xz+x2yz
1−x2yz . Summing these four cases gives
the generating function
G(x, y, z, w) = xyzw(1 + x)(1− x2yz) + xy + xz + 2x2yz
1− x2yz
that enumerates all possible conﬁgurations of one block.
Stringing together blocks of the four types gives all elements ofF that end
in (1, 1), and this subclass thus has generating function 1/(1−G(x, y, z, w)). An
element (S, T)∈B 2
n of this subclass must have n∈ S∩ T, and by removing
n we obtain a bijection of such pairs to B2
n−1, except that when n = 0 it is not
possible to delete n. Applying this bijection reduces the weight of each pair in
F by (1, 1, 1, 1), ultimately giving
F(x, y, z, w) =
( 1
1− G(x, y, z, w)− 1
)
/ (xyzw)
= (1 + x)(1− x2yz) + xy + xz + 2x2yz
1− x2yz− xyzw[(1 + x)(1− x2yz) + xy + xz + 2x2yz].
26 Generating functions
◁
Exercise 2.4. Fix a natural number n.
(a) What is the generating polynomial for the number of strictly increasing
sequences of length k chosen from [n]?
(b) Let S be the set of sequences of symbols from{0}∪[n] starting with a 0 and
such that the subsequence between any two consecutive zeros is strictly
increasing. Find the bivariate generating function counting elements of S
by their length and number of zeros.
Transfer matrices and restricted transitions
Suppose we want to count words (ﬁnite sequences) on an alphabet V such
that consecutive pairs of letters must come from a ﬁxed set E. Allowed words
of length n are equivalent to paths of length n in the directed graph whose
vertices are identiﬁed by the elements of V and whose edges are identiﬁed
by the elements of E. To count such paths by number of steps, let M be the
adjacency matrix of (V, E): the square matrix indexed by V with Mvw = 1 if
(v, w)∈ E and Mvw = 0 otherwise. The number of allowed paths of length
n from v to w is (M n)vw. If we wish to enumerate paths by length we must
sum (zM)n over n, so the generating function counting ﬁnite paths from v to
w weighted by their length is
Fvw(z) =
∞∑
n=0
((zM)n)vw =
[
(I− zM)−1]
vw .
This approach, known as the transfer matrix method, is quite versatile. For
instance, to count all allowed paths by length we may sum in v and w, giving
the generating function F(z) = trace((I− zM)−1J) where J is the|V|×| V|
square matrix of 1s. More generally, we can enumerate by the number of each
type of transition: if E ={p1,..., pr} and ˜Mvw = zk ifpk = (v, w) and ˜Mvw = 0
if (v, w) < E then ˜Fvw(z) = [(I− ˜M)−1]vw enumerates paths from v to w by
the number of each transition, and ˜F(z) = trace((I− ˜M)−1J) enumerates all
paths by the number of each transition.
Example 2.9 (binary strings revisited) . The transfer matrix method may be
used to re-derive the generating function in Example 2.1. Let V ={0, 1} and
E ={(0, 0), (0, 1), (1, 0)} contain all directed edges except (1, 1). Then
M =
[ 1 1
1 0
]
2.2 Rational operations on generating functions 27
so the entries of
Q = (I− zM)−1 = 1
1− z− z2
[ 1 z
z 1− z
]
enumerate binary strings without consecutive ones, depending on their starting
and ending symbols. The paths from 0 to 0 havingn≥ 0 transitions are in one-
to-one correspondence, via stripping oﬀ the last 0, to the words in Example 2.1
of length n. Thus, the generating function for the class in Example 2.1 is the
(0, 0)-entry of Q, namely 1/(1− z− z2). ◁
Composition corresponds to block substitution
Let F(z) be a d-variate formal power series and G1,..., Gd be d formal power
series in any number of variables, all with vanishing constant terms. We deﬁne
the formal composition F(G1,..., Gd) as a limit in the formal power series
ring,
F(G1,..., Gd) := lim
n→∞
∑
|r|≤n
arG(z)r. (2.1)
The degree of the term G(z)r := G1(z)r1··· Gd(z)rd is at least|r| = ∑d
j=1 r j
by the assumption that G j(0) = 0 for all j, hence the coeﬃcients of degree at
mostδ in the sum in (2.1) do not change once n>δ , and the limit exists in the
formal power series ring.
Remark. Even if some G j has a non-zero constant term, it may still happen
that the sum converges in the ring of analytic functions, meaning that the in-
ﬁnitely many contributions to all coe ﬃcients are absolutely summable. The
composition exp(1− x) is not formally allowed inC[[x]] because, for instance,
the constant term cannot be computed in a ﬁnite number of operations, but
exp(1− x) = e∑∞
n=0
(−x)n
n! represents the composition as a convergent series for
all x∈C, meaning it belongs toC{x}.
A slightly unwieldy combinatorial interpretation of composition is given
in [GJ04, Section 2.2.20]. SupposeA = Φ(S) where Φ is a speciﬁcation built
from the combinatorial sum, product and sequence operations described above
andS = {s1,..., sd} is a class with d distinct elements such that φ(sk) is
the elementary basis vector ek. IfB1,..., Bd are combinatorial classes with no
objects of weight zero, then thecomposition classA◦(B1,..., Bd) enumerated
by A(B1,..., Bd) is the class obtained fromA by replacing each occurrence of
sk by an element ofBk in all possible ways.
Example 2.10 (queries). Queries from a database have integer computation
28 Generating functions
times associated with them. Suppose we have a database such that for each
k≥ 1 there are bk diﬀerent queries that take k time units, and the protocol in
use does not allow two large queries in a row, where a large query is one of
size greater than some ﬁxed number M. How many query sequences are there
of total time n?
The sequences of queries are bijectively equivalent to the compositionA◦
(B1,B2), whereA is the class from Example 2.9, counted by numbers of 0s
and 1s, andB1 andB2 are respectively the short queries and the long queries,
counted by computation time. Thus,
A(B1, B2) = 1
1− B1(z)− B1(z)B2(z)
enumerates query sequences in this model by length, where B1(z) = ∑M
k=1 bkzk
and B2(z) = ∑
k>M bkzk. ◁
Our next example may seem a natural candidate for the transfer matrix
method, but is simpler to analyze from the viewpoint of compositions.
Example 2.11 (Smirnov words). LetA be the class of Smirnov words on the
alphabet [d], which are words where no consecutive repetition of any symbol is
allowed. The deﬁnition immediately implies that there are d· (d− 1)n−1 words
of length n, and we now perform a more reﬁned enumeration tracking each
symbol.
Let A(z) enumerate Smirnov words and B(z) enumerate the class B of all
words on the alphabet [d], both weighted by the number of occurrences of each
symbol. Starting withx∈A and substituting an arbitrary nonempty string of
the symbol j for every occurrence of j inx produces each element of B in
a unique way. The generating function for a nonempty string of js is z j
1−z j
,
whence
B(z) = A
( z1
1− z1
,..., zd
1− zd
)
.
We can solve for A by setting y j = z j/(1− z j) in this equation, since inverting
the substitution gives z j = y j/(1 + y j) and thus
A(y) = B
( y1
1 + y1
,..., yd
1 + yd
)
.
Since B(z) = 1/(1− ∑d
j=1 z j) we ultimately obtain
A(z) = 1
1− ∑d
j=1
z j
1+z j
.
◁
2.2 Rational operations on generating functions 29
In probability theory, the study of branching processes is almost always dealt
with by means of analytic generating functions.
Example 2.12 (Galton–Watson process). Let f (z) be a probability generating
function supported on N, meaning that f (z) = ∑∞
n=0 pnzn with pn ≥ 0 and∑∞
n=0 pn = 1. A branching process with oﬀspring distribution f is a random
tree with one vertex in generation 0 where each individual in each generation
has a random number of children, and the numbers of children born to the
individuals in a generation are independent and equal to n with probability pn.
If Zn is the random variable tracking the number of individuals in generation
n then we can compute the probability generating function gn(z) = ∑
k≥0 pn,kzk
for Zn inductively, where pn,k is the probability that Zn = k.
Indeed, the probability generating function for Z1 is simply f (z). In a con-
ﬁguration with Zn = k, the next generation is composed of a sequence of k
families, each independently having size j with probability p j. The probabil-
ity generating function for such a sequence is f (z)k, whence gn+1 = gn◦ f .
Inductively then, gn = f◦···◦ f is the n-fold composition of f with itself.
Observe that, unless p0 = 0 (no extinction), this composition is not deﬁned in
the formal power series ring, but since all functions involved are convergent on
the unit disk, the compositions are well deﬁned analytically. ◁
Example 2.13 (branching random walk). Associate to each particle in a branch-
ing process a real number, which we interpret as the displacement in one di-
mension between its position and that of its parent. If these are independent of
each other and of the branching, and are identically distributed, then one has
the classical branching random walk. A question that has been asked several
times in the literature, for instance in [Kes78], is how to determine when there
exists a line of descent from a single particle at position 1 that remains to the
right of the origin for all time. Here we consider the simplest non-trivial case,
where the branching process is deterministic binary splitting ( p2 = 1) and the
displacement distribution is a random walk that moves one unit to the right
with probability p< 1/2 and one unit to the left with probability 1− p.
If we modify the process so that particles stop moving or reproducing when
they hit the origin, then p < 1/2 implies an inﬁnite line of descent to the
right of the origin is equivalent to inﬁnitely many particles reaching the origin.
To analyze the process we thus let X be the number of particles ever to hit
the origin, beginning with a single particle at 1, and let φ be the probability
generating function
φ(z) =
∞∑
n=0
anzn where an =P(X = n).
30 Generating functions
If the initial condition is changed to a single particle at position 2, then the
number of particles ever to reach the origin will have probability generating
functionφ◦φ. To see this, apply the analysis of Example 2.12, noting that the
number of particles ever to reach 1 before any ancestor has reached 1, together
with their collections of descendants who ever reach 0, form two generations
of a branching process with o ﬀspring distribution the same as X. If the ini-
tial condition is changed to a single particle at position 0 then the generating
function is z.
Each of the two children in the ﬁrst generation is located at 0 with probabil-
ity 1− p and at 2 with probability p, so the probability generating function for
the contribution to X of each child is (1− p)z+ pφ(φ(z)). The two contributions
are independent so their sum is a convolution, whose probability generating
function is therefore the square of this. Thus, we have the identity
φ(z) = [(1− p)z + pφ(φ(z))]2. (2.2)
While this does not produce an explicit formula for φ, it is possible from this
to derive asymptotics for φ(t) as t↑ 1, allowing us to use so-called Tauberian
theorems to recover asymptotic information about an. See Example 3.17 for
more information. ◁
Derivation corresponds to marking an atom
If A(z) = ∑
n≥0 anzn enumerates the class A then the deﬁnition of the for-
mal derivative implies that zA′(z) = ∑
n≥1 nanzn. Thus, zA′(z) can be viewed
combinatorially as the generating function of a new class obtained fromA by
taking each object and marking, in all possible ways, one of the atomic pieces
it is composed of. Similarly, if A(z) is a multivariate generating function then
(zk∂kA)(z) can be interpreted as the generating function of a combinatorial
class obtained by marking pieces deﬁning the parameter of A tracked by the
variable zk.
Exercise 2.5. Let f (z) = ∑∞
n=0 pnzn be the probability generating function
for the probability that a randomly chosen household in some town consists
of n people. Let g(z) = z f′(z)/ f′(1). Show that g is a probability generating
function and determine what sampling probability it represents.
