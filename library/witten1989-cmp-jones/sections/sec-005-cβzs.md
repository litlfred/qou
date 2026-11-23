---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-005-cβzs
section_title: "; C)+βZ(S"
section_number: null
pages: 29-35
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
3;
(4.12)
Together with (4.7),
10 this implies that the expectation value of an unknotted
Wilson line in the N dimensional representation of SU(N) is
(4.13)
Presently we will make this formula completely explicit by computing α, /?, and γ in
terms of the fundamental quantum field theory parameters N and k.
The induction sketched above expresses any knot expectation value as a
rational function of α, β and γ (a ratio of polynomials), after finitely many steps. It
is in this sense that the Jones knot invariants and their generalizations are
"polynomials". While it is, as we have seen, comparatively elementary to prove
that (4.11) uniquely determines the knot invariants, the converse is far less
obvious. Equations (4.11) can be used in many different ways to obtain the
expectation value of a given link, and one must show that one does not run into
10 This is the only point at which (4.7) has to be used. The induction sketched in the previous
paragraph reduces all computations for knots in S
3 to this special case without using (4.7)
380 
E. Witten
any inconsistency. While this has been proved in a variety of ways, the proofs have
not been intrinsically three dimensional -- (4.11) has not previously been derived
from a manifestly invariant three dimensional framework. This is the novelty of
the present discussion.
Change of Framing. We want to compute α, /?, and y, but as a prelude we must
discuss a certain technical point. At the end of Sect. 2, we learned that choosing a
circle C and a representation R is not enough to give a well defined quantum
holonomy operator WR(C) = Trκ Pexp J Adx. It is also necessary to pick a
c
"framing" of the circle C, which enters when one has to calculate the self-linking
number of C and its non-abelian and quantum generalizations. At the end of
Sect. 2, we promised to derive a formula (2.33) showing how any partition
function with an insertion of WR (C) transforms under a change of framing. Now
it is time to deliver on this promise.
As in Fig. 7b, let us cut the three manifold M on a Riemann surface Σ that
intersects C in a point P (and perhaps in some other points that will not be
material). In our previous argument, we used the fact that associated with the
boundaries ML or MR are Hubert spaces JήfL and ,^fR. Moreover, tfR (for
example) is "a flat bundle on moduli space" so the mapping class group of the
boundary Σ acts naturally on 3?R. We wish to act on the boundary of MR with a
very particular diffeomorphism before gluing the pieces of Fig. 7b back together
again. The diffeomorphism that we want to pick is a f-fold "Dehn twist" about the
point P on Σ. Making this diffeomorphism and then gluing the pieces of Fig. 7b
back together again, one gets an identical looking picture, but the framing of the
circle C has been shifted by ΐ units. On the other hand, one knows in conformal
field theory how the Dehn twist acts on .tf?R. Associated with the representation R
is a number HR, the "conformal weight of the primary field in the R represent-
ation". The /-fold Dehn twist acts on jήfR as multiplication by c
2πιΐhR. So we have
obtained (2.33) with h = hR.
Explicit Evaluation. We will now determine the parameters α, β, and 7 that appear
in the crucial equation (4.10). We need to determine the explicit relation among the
three vectors ψ, ψ1 and ψ2 that appear in Fig. 7c. This requires a further study of
the two dimensional Hubert space which arises as the space of conformal blocks
for the R, R, R, R four point function on S
2 [R being in this case the defining N
dimensional representation of SU(N) and R its dual]. The three configurations in
Fig. 7c can be regarded as differing from each other by a certain diffeomorphism
of S
2; the diffeomorphism in question is the "half-monodromy" under which the
two copies of R change places by taking a half-step around one another, as
indicated in Fig. 11. Moore and Seiberg call this operation B and study it
extensively. The states ψl and ψ2 are none other than
ψi = Bψ, 
ψ2 = B
2ψ. 
(4.14)
The matrix B, since it acts in a two dimensional space, obeys a characteristic
equation
= 0, 
(4.15)
Quantum Field Theory and the Jones Polynomial 
381
Fig. 11 a and b. The half-monodromy operation exchanging two equivalent points on S
2 is
sketched in a; the arrows are meant to suggest a process in which the first two points change places
by executing a half-twist about one another. The idea in b is that if the two points on the left in the
first picture undergo a half-twist about one another, the first picture becomes the second, and if
this is done again, the second picture becomes the third. In this way the three pictures on the right
of Fig. 7c differ by a succession of half-monodromies
where 
j'' = TrJ?, 
z = det5. 
(4.16)
In view of (4.14), the linear relation among ψ, ψi, and ψ2 is (up to an irrelevant
common factor) just 
Λ 
,Λ*n\
z - ψ-y - ψ1 + ψ2 = Q, 
(4.17)
and according to (4.16), to make this explicit we need only to know the eigenvalues
(and thus the determinant and trace) of B.
These can be obtained from [13], but before describing the formulas, I would
like to point out an important subtlety. As we have discussed in the last subsection,
all concrete results such as the values of α, /?, and γ depend on the framing of knots.
The convention that is most natural in working on an arbitrary three manifold is
not the convention usually used in discussing knots on S
3.
In studying Fig. 7c, to describe the relative framings, the task is to specify the
relative framing of the three pictures on the right, since the picture on the left is
being held fixed. If one just looks at these three pictures and ignores the fact that
the lines cannot pass through each other, there is an obvious sense in which one
would like to pick "the same" framing for each picture; for instance, a unit vector
coming out of the page defines a normal vector field on each link in the picture.
This is equivalent to the convention of Moore and Seiberg in defining the
eigenvalues of B, so we can now quote their results. Let hR be the conformal weight
of a primary conformal field transforming as R, let Eί be the irreducible
representations of SU (N) appearing in the decomposition o f R (x) R, and let hEι be
the weights of the corresponding primary fields. Then the eigenvalues of B are
λt= ±exp(zπ(2A Λ-A £ ι)) 5 
(4.18)
where the + or — sign corresponds to whether El appears symmetrically or
antisymmetrically in R (x) R. If R is the N dimensional representation of SU(N),
then one finds
 11 that the eigenvalues of B are
Λ 
I t / υ \ 
. I T 
I 
J. I 
\ 
r. 
I 
l ί < * \ J . 1 
LI 
V 
, . 
Λ Γl\
^=exp( J,>; 
, ,/), 
A^-expf^φ-^j. 
(4.19)
11 For this representation, hR = (N
2 — 1)/(2N(N + k)}. In the decomposition of R(χ)R, the
symmetric piece is an irreducible representation with HEl =(N
2 -f N— 2)/N(N + k), and the
antisymmetric piece is an irreducible representation with hE2 = (N
2 — N — 2)/N(N + k)
382 
E. Wilten
It is straightforward to put these formulas in (4.16), (4.17) and thus make our
previous results completely explicit.
Before comparing to the knot theory literature, it is necessary to make a
correction in these results. For a link in S
3, there is always a standard framing in
which the self-intersection number of each component of the link is zero. Values of
the knot polynomials for knots in S
3 are usually quoted without specifying a
framing; these are the values for the link with standard framing. However, if on the
right of Fig.Tc we use the "same" framing for each picture, then when the right of
Fig.7c is glued to the left, one does not have the canonical framing for each link. If
the first knot is framed in the standard fashion, then the second is in error by one
unit and the third by two units. So after using (4.19) to compute α, /?, y, we must, if
we wish to agree with the knot theory literature, multiply β by exp ( — 2πihR) and γ
by exp( — 4π/Λ R). After these corrections, one gets
/ 
2πι 
\
-- 
- 
(A
= ~
exp — 
+ exp -
- '
 
(4
If 
one 
multiplies 
α, 
β, 
γ 
by 
an 
irrelevant 
common 
factor
exp (in (N
2 — 2)/N(N+k)) and introduces the variable
(4.21)
then the skein relation can be written more elegantly as
-q
Nf2 L+ + fo
1/
2 - q-W) LO + q-W L_ = 0 . 
(4.22)
Here L+ , L0, and L_ [equivalent to L, Ll , and L2 in (4.11)] are standard notation
for overcrossing, zero crossing, and undercrossing; and for / = + , 0, — , we now
write simply Lz, instead of Z(Lf). Equation (4.22) is correctly normalized to give
the right answers for knots on S
3 with their standard framing, and if one is only
interested in knots on S
3 one can use it without ever thinking about the framings.
Finally, comparing (4.13) and (4.22), we see that the expectation value of an
unknotted Wilson line on S
3, with its standard framing, is
N/2_ 
-N/2
(4.23)
This formula can be subjected to several interesting checks. First of all, the right-
hand side of (4.23) is positive for all values of the positive integers TV" and k. This is
required by reflection positivity of the Chern-Simons gauge theory in three
dimensions. Second, in the weak coupling limit of k -> oo, we have <C> -> N. This
is easily interpreted; in the weak coupling limit, the fluctuations in the connection
A{ on S
3 are irrelevant, and the expectation value of the Wilson line approaches its
value for A{ = 0, which is the dimension of the representation, or in this case N.
Quantum Field Theory and the Jones Polynomial 
383
4.2. Surgery on Links
We have seen that it is possible to effectively calculate the expectation value of an
arbitrary link in S
3. We would now like to generalize this to computations on an
arbitrary three manifold. The basic idea is that by the operation of "surgery on
links" any three manifold can be reduced to S
3, so it is enough to understand how
the invariants that we are studying transform under surgery. The operation of
surgery can be described as follows. One begins with a three manifold M and an
arbitrarily selected embedded circle C. Note that there is, to begin with, no Wilson
line associated with C; C is simply a mathematical line on which we are going to
carry out "surgery". To do so we first thicken C to a "tubular neighborhood", a
solid torus centered on C. Removing this solid torus, Mis split into two pieces; the
solid torus is called MR in Fig. 12b, and the remainder is called ML. One then
makes a diffeomorphism on the boundary of MR and glues ML and MR back
together to get a new three manifold M.
It is a not too deep result that every three manifold can be obtained from or
reduced to S
3 (or any other desired three manifold) by repeated surgeries on
knots. However, such a description is far from unique and it is often difficult to use
a description of a three manifold in terms of surgery to compute the invariants of
interest. We will now see that the invariants studied in this paper can be effectively
computed from a surgery presentation.
M
Fig, 12a-c. Surgery on a circle C in a three manifold M is carried out by removing a tubular
neighborhood of C, depicted in a. At this point M has been separated into two pieces, ML and MR,
with a torus Σ for their boundaries, as sketched in b. MR is simply a solid torus. Surgery is
completed by gluing the two pieces back together after making a diffeomorphism of the boundary
of MR. At the end of this process, M has been replaced by a new three manifold M. As we will
eventually see, computations on M are equivalent to computations on M with a physical Wilson
line where the surgery was made, as in c. The difference between a and c is that in a the circle C is
just a locale for surgery, but in c it is a Wilson line
384 
E.Witten
We study Fig. 12b by the standard arguments. Hubert spaces JfL and J^,
canonically dual to one another, are associated with the boundaries of ML and
MR. The path integrals on ML and MR give vectors ψ and χ in jfL and JfR, and the
partition function on Mis just the natural pairing (ψ,χ). If we act on the boundary
of MR with a diffeomorphism Kbefore gluing ML and MR back together, then/ is
replaced by Kχ so (ψ,χ) is replaced by (ψ,Kχ).
This potentially gives a way to determine how the partition function of the
quantum field theory transforms under surgery. Upon gaining a suitable
understanding of Kχ, we will be able to reduce calculations on M to calculations
on M.
4.3. The Physical Hubert Space in Genus One
At this point we need a description of the physical Hubert space in genus one. A
beautiful description, perfectly adapted for our needs, appears in the work of
Verlinde [12].
First of all, the loop group LG has at level k finitely many integrable highest
weight representations. Let t be the number of these. For each such highest weight
representation of the loop group, the highest weight space is an irreducible
representation of the finite dimensional group G. In this way there appear /
distinguished representations of G; we label these as R0, R1 ... /?,_!, with R0
denoting the trivial representation (which is always one of those on this list).
Verlinde showed that ΊfΣ is a Riemann surface of genus one, then the dimension of
the physical Hubert space J^Σ is t. Moreover, though there is no canonical basis for
J^Σ, Verlinde showed that every choice of a homology basis for H
l (Σ, Z),
consisting of two cycles a and b, gives a canonical choice of basis in 3PΣ. For our
purposes, this can be described as follows. Topologically, there are many
inequivalent ways to identify a torus Σ as the boundary of a solid torus U. The
choice of U can be fixed by requiring that the cycle a is contractible in U. This is
indicated in Fig. 13 a. Next, for every i = 0 ... t — 1, one defines a state vt in J^Σ as
follows. One places a Wilson line in the Rl representation in the interior of U,
Fig. 13a and b. A Riemann surface Σ of genus one is shown in a as the boundary of a solid torus
C7; the indicated «-cycle is contractible in U. In b, a basis of the physical Hubert space is indicated
consisting of states obtained by placing a Wilson line, in the Rt representation, in the interior of U,
parallel to the cycle b, and performing the path integral to get a vector ι?f in j^Σ
Quantum Field Theory and the Jones Polynomial 
385
running in the b direction,
12 and one performs the Feynman path integral in Uΐo
define a vector vt in jjfΣ. The vt make up the Verlinde basis in 3ΊfΣ. It must be
understood that a Wilson line in the trivial representation is equal to 1, so the
vector v0 obtained by this definition is the same as the vector χ which in the last
subsection was obtained by a path integral on U with no Wilson lines:
X = »o 
(4-24)
A diffeomorphism K of Σ is represented in the Verlinde basis by an explicit
matrix K^ defined by the formula
