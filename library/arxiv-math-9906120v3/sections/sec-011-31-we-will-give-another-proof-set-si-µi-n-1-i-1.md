---
doc_id: arxiv-math-9906120v3
doc_title: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson"
section_id: sec-011-31-we-will-give-another-proof-set-si-µi-n-1-i-1
section_title: "We will give another proof. Set si = µi + N + 1 −i, 1 ≤i ≤N and"
section_number: 3.1
pages: 31-37
source_pdf: 9906120v3.pdf
source_sha256: 436982ef45e940bd
doc_brief: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson — We consider discrete orthogonal polynomial ensembles which are discrete analogues of the orthogonal polynomial"
---
rj = N + j −µ′
j, 1 ≤j ≤M. Then,
(5.9)
{s1, . . . , sN} ∪{r1, . . . , rM} = {1, . . . , N + M}.
To see this, notice that since 1 ≤si, rj ≤N + M it suﬃces to show that
si̸ = rj for all i, j. Looking at the µ-diagram one sees that µi + µ′
j ≤i + j −2
or µi + µ′
j ≥i + j, which implies si̸ = rj.
Let nk = 1 if k ∈{s1, . . . , sN} and nk = 0 if k ∈{r1, . . . , rM}, k =
1, . . . , N + M. Then, by (5.9),
(5.10)
VM(µ′) =
Y
1≤k<l≤N+M
(l −k)(1−nk)(1−nl).
290
KURT JOHANSSON
Now,
Y
1≤k<l≤N+M
(l −k)nknl = VN(µ),
Y
1≤k<l≤N+M
(l −k)nk =
N
Y
j=1
N+M
Y
l=sj+1
(l −sj) =
N
Y
j=1
(N + M −sj)!
and
Y
1≤k<l≤N+M
(l −k)nl =
N
Y
j=1
sj−1
Y
k=1
(sj −k) =
N
Y
j=1
(sj −1)!.
Inserting this into (5.10) gives the formula (5.8). The lemma is proved.
We can now ﬁnish the proof of the proposition. If we write µ = λ′, we see
from (5.8) that (5.7) can be written as
P[L(W) ≤n] = (1 + ρ)−MN
N−1
Y
j=0
(j + M)!
j!
(5.11)
×
X
µ∈ΩN(M)
µ1≤n
VN(µ)2WN(µ)
N
Y
j=1
ρµj
(M + j −1 −µj)!.
As usual we introduce the new coordinates hj = µj + N −j. Then, using
ρ = 1/q −1, we obtain
P[L(W) ≤n] = 1
N!
N−1
Y
j=0
(j + M)!
j!
(pq)N(N−1)/2
((N + M −1)!)N
×
X
h∈NN
max(hj)≤n+N−1
∆N(h)2
N
Y
j=1
N + M −1
hj

phjqN+M−1−hj,
which completes the proof.
Using Proposition 5.1 we can prove a limit theorem for the ﬁrst passage
time T(k, l). The result should be compared with Remark 1.8 and Conjecture
1.9 in [Jo3].
Theorem 5.3. If µ(x, y) is given by (5.2),
σ(x, y) = (pq)1/6
(xy)1/6 (√px + √qy)2/3(√qx −√py)2/3
ENSEMBLES AND THE PLANCHEREL MEASURE
291
and py < qx, then
lim
n→∞P
T([nx], [ny]) −nµ(x, y)
σ(x, y)n1/3
≤ξ

= 1 −F(−ξ),
where F(t) is the Tracy-Widom distribution (1.5).
Proof. The proof uses (5.4) and Proposition 5.1 and is analogous to the
proof of Theorem 1.7, the diﬀerence being that we now need the analogue
of Lemma 4.1 for the Krawtchouk polynomials. This can be obtained from
a steepest descent analysis of the integral formula for these polynomials in
much the same way as in the analysis of the Meixner polynomials in Section
5 of [Jo3]; see [Jo4] for some more details. The time constant is related to
the right endpoint of the support of the equilibrium measure associated with
the Krawtchouk ensemble, and the constant σ(x, y) comes out of the steepest
descent argument. We can also get large deviation results by using the general
results of Section 4 in [Jo3].
5.2.
The Aztec diamond. We turn now to the relation between the
Krawtchouk ensemble and domino tilings of the Aztec diamond introduced
by Elkies, Kuperberg, Larsen and Propp in [EKLP]. The deﬁnitions are taken
from that paper and the papers [JPS] and [CEP] where more details and pic-
tures can be found. A domino is a closed 1 × 2 or 2 × 1 rectangle in R2 with
corners in Z2, and a tiling of a region R ⊆R2 by dominoes is a set of dominoes
whose interiors are disjoint and whose union is R. The Aztec diamond, An, of
order n is the union of all lattice squares [m, m + 1] × [l, l + 1], m, l ∈Z, that
lie inside the region {(x, y) ; |x| + |y| ≤n + 1}. It is proved in [EKLP] that the
number of possible domino tilings of An equals 2n(n+1)/2. Color the Aztec dia-
mond in a checkerboard fashion so that the leftmost square in each row in the
top half is white. A horizontal domino is north-going if its leftmost square is
white, otherwise it is south-going. Similarly, a vertical domino is west-going if
its upper square is white, otherwise it is east-going. Two dominoes are adjacent
if they share an edge, and a domino is adjacent to the boundary if it shares an
edge with the boundary of the Aztec diamond. The north polar region is de-
ﬁned to be the union of those north-going dominoes that are connected to the
boundary by a sequence of adjacent north-going dominoes. The south, west
and east polar regions are deﬁned analogously. In this way a domino tiling
partitions the Aztec diamond into four polar regions, where we have a regular
brick wall pattern, and a ﬁfth central region, the temperate zone, where the
tiling pattern is irregular.
Consider the diagonal of white squares with opposite corners Qr
k, k =
0, . . . , n + 1, where Qr
k = (−r + k, n + 1 −k −r), r = 1, . . . , n. A zig-zag path
Zr in An from Qk
0 to Qr
n+1 is a path of edges going around these white squares.
292
KURT JOHANSSON
When going from Qr
k to Qr
k+1 we can go either ﬁrst one step east and then one
step south, or ﬁrst one step south and then one step east. A domino tiling on
An deﬁnes a unique zig-zag path Zr from Qr
0 to Qr
n+1 if we require that the
zig-zag path does not intersect the dominoes. Similarly, we can deﬁne zig-zag
paths from P r
0 = (−r, n −r) to P r
n = (n −r, −r) going around black squares.
We consider random tilings of the Aztec diamond, where each of the
2n(n+1)/2 possible tilings have the same probability.
This induces a proba-
bility measure on the zig-zag paths. Consider a zig-zag path in An from Qk
0
to Qr
n+1 around white squares. Let hr < · · · < h1 be those k for which we go
ﬁrst east and then south when we go from Qr
k to Qr
k+1, k = 0, . . . , n; there are
exactly r such k if the zig-zag path comes from a domino tiling, [EKLP]. Call
this zig-zag path Zr(h).
Proposition 5.4. Let {h1, . . . , hr} ⊆{0, . . . , n} be the positions of
the east/south turns in a zig-zag path Zr(h) in the Aztec diamond An from
(−r, n + 1 −r) to (n + 1 −r, −r) around white squares. Then, the probability
for this particular zig-zag path is
(5.12)
P[Zr(h)] = PKr,r,n,1/2[h].
If {h1, . . . , hr} ⊆{0, . . . , n −1} are the positions of the south/east turns in a
zig-zag path Z′
r(h) in An from (−r, n −r) to (n −r, −r) around black squares,
then
(5.13)
P[Z′
r(h)] = PKr,r,n−1,1/2[h].
Proof. Let Ur(h) be the number of possible domino tilings above Zr(h) in
the Aztec diamond. From the arguments in [EKLP], see also [PS], it follows
that
(5.14)
Ur(h) = 2r(r−1)/2
Y
1≤i<j≤r
hi −hj
j −i .
Let k1 < · · · < kn+1−r be deﬁned by
{k1, . . . , kn+1−r} = {0, . . . , n} \ {h1, . . . , hr}.
If Lr(h) is the number of domino tilings of the region below Zr(h) in An, then,
using the symmetry of the Aztec diamond, we see that
(5.15)
Lr(h) = 2(n+1−r)(n−r)/2
Y
1≤i<j≤n+1−r
kj −ki
j −i .
Thus, the probability for a certain zig-zag path Zr = Zr(h), speciﬁed by h, is
(5.16)
P[Zr(h)] = 2(n+1−r)(n−r)/2+r(r−1)/2
2n(n+1)/2
Y
1≤i<j≤r
hi −hj
j −i
Y
1≤i<j≤n+1−r
kj −ki
j −i .
ENSEMBLES AND THE PLANCHEREL MEASURE
293
If we let hi = µi + r −i, 1 ≤i ≤r and kj = r + j −1 −µ′
j, 1 ≤j ≤n + 1 −r,
then µ and µ′ are conjugate partitions; compare with the proof of Lemma 5.1
(N = r, M = n + 1 −r, si = hi + 1, rj = kj + 1). We see from (5.16) that
P[Zr(h)] = 2−(n+1−r)r


r−1
Y
j=1
1
j!




n−r
Y
j=1
1
j!

Vr(µ)Vn+1−r(µ′),
where µ ∈Ωr(n + 1 −r). We can now apply Lemma 5.1, which gives
P[Zr(h)] = 2r(r−1)
(n!)r
r−1
Y
j=1
(n −j)!
j!
Vr(µ)2
r
Y
j=1

n
µj + r −j
 1
2n .
Now, hi = µi + r −i, so we obtain
(5.17)
P[Zr(h)] = 2r(r−1)
(n!)r
r−1
Y
j=1
(n −j)!
j!
∆r(h)2
r
Y
j=1
 n
hj
 1
2n ,
which is the Krawtchouk ensemble. Note that in (5.17) the order of the hi’s
is unimportant, so we can let {h1, . . . , hr} ⊆{0, . . . , n} be the (unordered)
positions of the east/south turns. A completely analogous argument applies to
the zig-zag paths in An from P r
0 to P r
n around black squares. This completes
the proof.
It is proved in [JPS] that, with probability tending to 1 as n →∞, the
asymptotic shape of the temperate zone is a circle centered at the origin and
tangent to the boundary of the Aztec diamond (the arctic circle theorem).
This can be deduced from Proposition 5.4 and the general results in Section 4
of [Jo3]. The arctic circle is determined by the endpoints of the support of the
equilibrium measure (or the points where it saturates). Also, from Theorem
5.3, we see that the ﬂuctuations of the temperate zone around the arctic circle
is described by the Tracy-Widom distribution. This can also be deduced from
the fact, derived in [JPS], that the shape of a polar region is related to the
shape of a randomly growing Young diagram. The growth model obtained is
exactly the discrete time growth model studied in [Jo3], and we can apply the
results of that paper. See [Jo4] for more details.
Finally, we will shortly discuss another random tiling problem related to
plane partitions using the combinatorial analysis by Cohn, Larsen and Propp
in [CLP]. For more details and pictures see the paper [CLP]. Plane partitions
in an a×b×c box can be seen to be in one-to-one correspondence with tilings of
an a, b, c-hexagon with unit rhombi with angles π/3 and 2π/3, called lozenges.
An a, b, c-hexagon has sides of length a, b, c, a, b, c (in clockwise order), equal
angles and the length of the horizontal sides is b. If the major diagonal of
the lozenge is vertical we talk about a vertical lozenge. Consider the uniform
294
KURT JOHANSSON
distribution on the set of all possible tilings of the a, b, c-hexagon with lozenges,
which corresponds to the uniform distribution on all plane partitions in the
a×b×c box. For simplicity we will now restrict ourselves to the case a = b = c.
A horizontal line k steps from the top, k = 0, . . . , a will intersect the vertical
lozenges at positions h1 + 1, . . . , hk + 1, 0 ≤h1 < · · · < hk ≤a + k −1,
otherwise it passes through sides of the lozenges.
A random tiling induces
a probability measure on the sequences h = (h1, . . . , hk).
Interpreting the
formulas in Theorem 2.2 in [CLP] we see that the probability for h is
(5.18)
P[h] =
1
Zk,a
∆k(h)2
k
Y
j=1
hj + a −k
hj
 2a −1 −hj
a + k −1 −hj

,
where Zk,a is a constant that can be computed explicitly.
Note that the
measure is symmetric in the hi’s so we can regard (5.18) as a measure on
{0, . . . , a + k −1}k. Thus, again we get a discrete orthogonal polynomial en-
semble, this time with the weight
(5.19)
w(x) =
x + α
x
N + β −x
N −x

on {0, . . . , N}, with α = β = a −k and N = a + k −1.
The orthogonal
polynomials for this weight are the Hahn polynomials, [NSU], so (5.18) should
be called the Hahn ensemble. If we do not have a = b = c we will again get a
weight function of the form (5.19) but with diﬀerent values of α, β and N and
with a diﬀerent number of particles. This model is further discussed in [Jo4],
but to obtain the Tracy-Widom distribution in this model is more complicated
due to the fact that it is less straightforward to compute the asymptotics of
the Hahn polynomials.
Acknowledgement. I thank Eric Rains, Craig Tracy and Harold Widom for
helpful conversations and correspondence. I also thank Alexei Borodin, Andrei
Okounkov and Grigori Olshanski for keeping me informed about their work,
and Timo Sepp¨al¨ainen for drawing my attention to the papers [JPS] and [CEP].
Part of this work was done while visiting MSRI and I would like to express my
gratitude to its director David Eisenbud for inviting me and to Pavel Bleher
and Alexander Its for organizing the program on Random Matrix Models and
their Applications. This work was supported by the Swedish Natural Science
Research Council (NFR).
Royal Institute of Technology, Stockholm, Sweden
E-mail address: kurtj@math.kth.se
ENSEMBLES AND THE PLANCHEREL MEASURE
295
