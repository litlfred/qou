---
doc_id: cspaper
doc_title: "Combinatorics of Triangulations and the Chern-Simons Invariant for Hyperbolic 3-Manifolds"
section_id: sec-001-2-consistency-and-cusp-conditions-and-the-condit
section_title: "Consistency and cusp conditions, and the conditions on c"
section_number: 2
pages: 4-8
source_pdf: cspaper.pdf
source_sha256: 1910c380cf79bf42
toc_source: inferred
doc_brief: "Combinatorics of Triangulations and the Chern-Simons Invariant for Hyperbolic 3-Manifolds — 7 sections: Front matter; Introduction; Consistency and cusp conditions, a"
---
An ideal hyperbolic structure on a tetrahedron ∆is speciﬁed by assigning a complex
number with positive imaginary part to each edge, these numbers being related as in
Fig. 1. The geometric meaning of these parameters is that the Euclidean triangle cut off
by a horosphere section at a vertex is similar to the Euclidean triangle pictured in Fig. 1
with vertices 0, 1, and z in the complex plane; the parameter z is only well-deﬁned
after choosing an edge of ∆, and parameters for different edges are related as illustrated.
Instead of these parameters z, 1/(1 −z), and (z −1)/z, it will be convenient to use
their natural logarithms
log(z),
−log(1 −z),
log(1 −z) −log(z) + πi
(unless otherwise stated, log is always the standard branch on C −(−∞, 0]). We call
these the log-parameters of the tetrahedron.
Given a tetrahedron ∆, we shall choose a labelling of its edges e1, e2, . . . , e6 as in
Fig. 2. Thus ej and ej+3 are opposite edges for j = 1, 2, 3.
Let M be a hyperbolic 3-manifold which is ideally triangulated as
M = ∆1 ∪. . . ∪∆n.
(2.1)
Choose a labelling ej, j = 1, . . . , 6, of the edges of each ∆ν as above. Let zν be the
parameter for ∆ν with respect to the edge e1 of ∆ν. We do not assume the hyperbolic
1– 1
z
1–z
1
1
1–z
z
1
1–
z
z
z
1
0
Figure 1
5e
2e
6e
3e
4e
1e
Figure 2
structure on M is complete, but we assume it results by deforming from a complete
structure on M with tetrahedral parameters z0
ν say.
Consistency conditions.
Each edge of each tetrahedron of the triangulation of M has
an associated log-parameter. The condition that the ideal tetrahedra ﬁt together around
an edge E of the triangulation is equivalent to the condition that the log-parameters sum
to 2πi around this edge. We call this the consistency condition at the edge E. It has
the form
n
X
ν=1
r′
ν(E) log(zν) + r′′
ν(E) log(1 −zν) = d(E)πi
(2.2)
for some integer d(E) and integers r′
ν(E) and r′′
ν(E), (ν = 1, . . . , n).
We can describe the integer d(E) as follows. Associate an integer ϵi(∆ν) to the i-th
edge of ∆ν as follows:
ϵ1(∆ν) = ϵ4(∆ν) = 0,
ϵ2(∆ν) = ϵ5(∆ν) = 0,
ϵ3(∆ν) = ϵ6(∆ν) = 1.
(2.3)
Associate a complex number ζj(∆ν) to the j-th edge of ∆ν by:
ζ1(∆ν) = ζ4(∆ν)
ζ2(∆ν) = ζ5(∆ν)
ζ3(∆ν) = ζ6(∆ν)
= log(zν),
= −log(1 −zν),
= −log(zν) + log(1 −zν).
(2.4)
The log-parameters of ∆ν are then
µj(∆ν) = ζj(∆ν) + ϵj(∆ν)πi,
j = 1, . . . , 6.
(2.5)
Equation (2.2) is the result of equating the sum of log-parameters around the edge E
with 2πi and moving the ϵj(∆ν)πi terms to the right of the equation. Thus
Lemma 2.1. d(E) = 2 −P
κ ϵjκ(∆νκ) where the sum is the sum of the ϵj(∆ν) around
the edge E.
Cusp conditions.
The torus T section of an end of M is triangulated by triangles cut
off the vertices of the ∆ν by horospheres. Each vertex of a triangle of this triangulation
determines some edge of a tetrahedron, and hence has an associated log-parameter, which
can be written µ = ζ + ϵπi as in equation (2.5).
C
6
5
4
3
2
1
µ
µ
µ
µ
µ
µ
µ(C) = −µ1 +µ2 −
µ3 −µ4 + µ5 −
µ6 + . . .
Figure 3
Let C be an essential simple closed curve in T which is in general position with
respect to the 1-skeleton of the triangulation of T and, moreover, “has no back-tracking,”
in the sense that it never departs a 2-simplex across the same edge by which it entered.
Then as C passes through a 2-simplex it determines a vertex of the 2-simplex, the vertex
between the entering and departing edges, and a sign + or −according as it goes past
this vertex counter-clockwise or clockwise. Let µ(C) = P ±µj be the sum over the
vertices that C passes of the corresponding log-parameter µj with sign ± as above
(Fig. 3). Clearly,
µ(C) =
n
X
ν=1
r′
ν(C) log(zν) + r′′
ν(C) log(1 −zν) −d(C)πi
(2.6)
for some integer d(C) and integers r′
ν(C) and r′′
ν(C), (ν = 1, . . . , n).
It is not hard to see (cf. Sect. 6 or [NZ]) that, given the consistency conditions, µ(C)
only depends on the homology class of C in T and µ gives a homomorphism from
H1(T) to C. In fact, µ(C) = 2 log λ(H(C)), where λ(H(C)) is an eigenvalue of the
holonomy H(C) of C.
The cusp condition corresponding to C is the condition that C have parabolic
holonomy, that is, µ(C) = 0, which by (2.6) can be written
n
X
ν=1
r′
ν(C) log(zν) + r′′
ν(C) log(1 −zν) = d(C)πi.
(2.7)
Just as for Lemma 2.1 one sees:
Lemma 2.2. d(C) = −P ±ϵj, where the ϵj are the ϵ’s (cf. equation (2.3)) at the
vertices that C passes, with signs ± given as above.
Consistency and cusp conditions.
For each edge E of our triangulation we have
the consistency condition (2.2). At each cusp of M choose two curves C as above
representing a basis of the ﬁrst homology of the cusp and consider the corresponding cusp
conditions (2.7). The complete hyperbolic structure on M —the one with tetrahedral
parameters z0
ν —is determined by all of these consistency and cusp conditions together.
This is a system of linear equations with integral coefﬁcients, which can be written
UZ0 = πid,
as described in the Introduction, with
Z0 =










log z0
1
...
log z0
n
log(1 −z0
1)
...
log(1 −z0
n)










.
Now suppose we are given a 2n-vector c = (c′
1, . . . , c′
n, c′′
1, . . . , c′′
n)t.
Assign
numbers ηi(∆ν) to the edges of ∆ν as follows:
η1(∆ν) = η4(∆ν) = c′
ν ,
η2(∆ν) = η5(∆ν) = −c′′
ν ,
η4(∆ν) = η6(∆ν) = −c′
ν + c′′
ν + 1.
(2.8)
Proposition 2.3. The equation Uc = d (equation (∗) of the Introduction) is equivalent
to the following conditions:
C1. the sum of the η ’s around any edge E of the triangulation is 2;
C2. for any path C as above in a torus section of an end of M, the signed sum of the
η ’s over the vertices adjacent to the path C is zero.
Proof. Replace log(z0
ν) by c′
ν and log(1 −z0
ν) by c′′
ν in the proofs of Lemmas 2.1 and
2.2.
The parity conditions.
We consider an integral vector c ∈Z2n. Thus, the ηj(∆ν)
deﬁned above are integers. Let C be any closed path in M which is in general position
with respect to the 2-skeleton of our triangulation. We also assume C “has no back-
tracking” in the sense that it never departs a 3-simplex across the same face by which it
entered. Then as C passes through a 3-simplex it determines an edge of the 3-simplex—
the edge common to the entering and departing faces—and hence an integer η as above.
We call the modulo-2 sum of these η ’s along C the parity of c along C .
The parity condition on c is the condition:
C3. The parity of c along C is even for all C as above.
The combinatorial part of Theorem 2 is re-formulated and made precise in part (i) of
the following theorem, which will be proved in Sect. 6.
Theorem 2.4.
(i)
There exists c ∈Z2n satisfying the above conditions C1, C2, and C3.
(ii) Any two elements c1 and c2 of Z2n satisfying conditions C1, C2, and C3, differ by
an integral linear combination of the vectors
J2nr(E) = (r′′
1(E), . . . , r′′
n(E), −r′
1(E), . . . , −r′
n(E))t ,
where the r(E) are the coefﬁcient vectors of the consistency conditions and
J2n =

0
In
−In
0

.
Remark. The parity condition C3 implies that C1 holds modulo 2. Given that C1 holds
modulo 2, the parity of c along C is easily seen to depend only on the homology class
of C and to give a homomorphism H1(M; Z/2) →Z/2. If C2 holds modulo 2, this
homomorphism vanishes on H1(E; Z/2), where E is the union of the ends of M. Thus,
one then need only check the parity condition on a set of representatives for generators of
H1(M; Z/2)/ Im H1(E; Z/2) = H1(M ∗; Z/2), where M ∗is the end compactiﬁcation
of M.
