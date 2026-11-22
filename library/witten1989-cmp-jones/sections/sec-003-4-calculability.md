---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-003-4-calculability
section_title: "Calculability"
section_number: 4
pages: 24-29
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
Our considerations so far may have seemed somewhat abstract, and we would
now like to show that in fact these considerations can actually be used to calculate
things. As an introduction to the requisite ideas, we will first deduce a certain
theoretical principle that is of great importance in its own right.
Consider, as in Fig. 5 a, a three manifold M which is the connected sum of two
three manifolds Mγ and M2, joined along a two sphere S
2. There may be knots in
M1 or M2, but if so they do not pass through the joining two sphere. If for every
three manifold X we denote the partition function or Feynman path integral (1 .6)
as Z(JΓ), then we wish to deduce the formula
Z(M) - Z(S
3) - Z(MJ - Z(M2) 
(4.1)
[it being understood that Z(S
3) denotes the partition function of a three sphere
that contains no knots]. This can be rewritten
Z(M2)
( 
}
Z(S
3) 
Z(S
3) 
Z(S
3)
In some special cases, (4.2) is equivalent or closely related to known formulas. If
Mi and M2 are copies of S
3 with knots in them, then the ratios appearing in (4.2)
turn out to be the knot invariants that appear in the Jones theory, and (4.2)
expresses the fact that these invariants are multiplicative when one takes the
disjoint sum of knots. If Ml and M2 are arbitrary three manifolds without knots,
then (in view of our discussion in Sect. 2) (4.2) is closesly related to the
multiplicativity of Reidemeister and Ray-Singer torsion under connected sums.
So let us study Fig. 5 a using the general ideas of quantum field theory. On the
left of this figure, we see a three manifold M1 with boundary S
2. According to the
general ideas of quantum field theory, one associates a "physical Hubert space"
2tf with this S
2; as we have seen in the last section, it is one dimensional. The
Feynman path integral on Mi determines a vector/ in J^. Likewise, on the right of
Quantum Field Theory and the Jones Polynomial
375
a 
M
Fig. 5a-c. In a is sketched a three manifold M which is the connected sum of two pieces Λ/Ί and
M2, joined along a sphere S
2. Similarly, a three sphere S
3 can be cut along its equator, as in b.
Cutting both M and S
3 as indicated in a and b, the pieces can be rearranged into the disconnected
sum of M1 and M2, as in c
Fig. 5a we see a three manifold M2 whose boundary is the same S
2 with opposite
orientation; its Hubert space 2tf" is canonically the dual of Jtif. The path integral
on M2 determines a vector ψ in ffl', and according to the general ideas of quantum
field theory, the partition function of the connected sum M is
Z(M) = (/,(//). 
(4.3)
The symbol (/, ψ} denotes the natural pairing of vectors/ 6 ffl, ψ e ffi'. We cannot
evaluate (4.3), since we do not know χ or ψ. Instead, let us consider some
variations on this theme. The two sphere S
2 that separates the two parts of Fig. 5 a
could be embedded in S
3 in such a way as to separate S
3 into two three balls BL
and BR. The path integrals on BL and BR would give vectors υ and v' in ffl and Jf ',
and the same reasoning as led to (4.3) gives
Z(S*) = ( v , v
f ) . 
(4.4)
Again, we do not know v or v' and cannot evaluate (4.4). But we can say the
following. As 3C is one dimensional, v is a multiple of/; likewise, since ffl' is one
dimensional, v' is a multiple of ψ. It is then a fact of one dimensional linear algebra
that
The two terms on the right-hand side of (4.5) are respectively Z (M±) and Z(M2),
as we see in Fig. 5c. So (4.5) is equivalent to the desired result (4.1).
One may wonder what is the mysterious object Z(S
3) that is so prominent in
(4.1). Can it be set to one? Actually, the axioms of quantum field theory are strong
enough so that the value of Z(£
3) is uniquely determined and cannot be
postulated arbitrarily; as we will see later it can be calculated from the theory of
affine Lie algebras. For G = SU(2) the formula has been given in (2.26).
As a special case of (4.1), pick ^irreducible representations of G, say Rl9... Rs,
and consider a link in S
3 that consists of s unlinked and unknotted circles Q, with
376 
E.Wilten
Fig. 6. A three sphere with 3 unlinked and unknotted circles Ch
associated with representations Rλ ...R^. The figure can be cut in
various ways to separate the circles
one of the Rt associated with each circle. This is indicated in Fig. 6. Denote the
partition function of S
3 with this collection of Wilson lines as Z(S
3; Cl , . . . Cs)
(the representations Rt being understood). Then by cutting the figure to separate
the circles, and repeatedly using (4.1), we learn that
Z(5
3;Q)
(4'6)
Z(S
3 
~
If we introduce the normalized expectation value of a link L, defined by
<L> - ZGS
3;L)/ZCS
3), then (4.6) becomes
<C 1...C β> = Π<Q> 
(4.7)
k
for an arbitrary collection of unlinked, unknotted Wilson lines on S
3,
In knot theory there is another notion of connected sum, the "connected sum
of links". The Jones invariants also have a simple multiplicative behavior under
this operation, as we will sketch briefly at the end of Sect. 4.5.
4.1. Knots in S
3
We will now describe the origin of the "skein relation" which can be taken as the
definition of the knot polynomials for knots on S
3. (A special case of the skein
relation was first used by Conway in connection with the Alexander polynomial.)
Consider a link L on a general three manifold M, as indicated in Fig. 7 a. The
components of the link are associated with certain representations of G, and we
wish to calculate the Feynman path integral (1.6), which we will denote as Z(L)
(with the representations understood). We will evaluate it by deducing an
algorithm for unknotting knots. If the lines in Fig. 7 could pass through each other
unimpeded, all knots could be unknotted. As it is, this is prevented by some
unfortuitous crossings, such as the one circled in the figure. Let us draw a small
sphere about this crossing, cut it out, and study it more closely. This cuts M into
two pieces, which after rearrangement are shown in Fig. 7b as a complicated piece
ML shown on the left of the figure and a simple piece MR shown on the right. MR
consists of a three ball with boundary S
2\ on this boundary there are four marked
points that are connected by two lines in the interior of the ball.
To make the discussion concrete, let us suppose that the gauge group is
G = SU(N) and that the Wilson lines are all in the defining N dimensional
representation of SU(N), which we will call R. Then, as we saw at the end of the
Quantum Field Theory and the Jones Polynomial
377
Fig. 7a-c. A link C on a general three manifold M is sketched in a. A small sphere S has been
drawn about an inconvenient crossing; it cuts M into a simple piece (the interior of S) and a
complicated piece. In b, the picture is rearranged to exhibit the cutting of M more explicitly; the
two pieces now appear on the left and right as ML (the complicated piece whose details are not
drawn) and MR (the interior of S). The key to the skein relation is to consider replacing MR with
some substitutes, as shown in c
last section, the physical Hubert spaces JfL and Jf# associated with the
boundaries of ML and MR are two dimensional.
The strategy is now the same as the strategy which led to the multiplicativity
relation (4.1). The Feynman path integral on ML determines a vector χ in 3?L. The
Feynman path integral on MR determines a vector ψ in 3?R. The vector spaces ^L
and Jfβ (which are associated with the same Riemann surface S
2 with opposite
orientation) are canonically dual, and the partition function or Feynman path
integral Z(L) is equal to the natural pairing
Z(L) = ( χ , ψ ) . 
(4.8)
We cannot evaluate (4.8), since we know neither χ nor ψ. The one thing that we do
know, at present, is that (for the groups and representations we are considering)
this pairing is occurring in a two dimensional vector space. A two dimensional
vector space has the marvelous property that any three vectors obey a relation of
378 
E. Witten
linear dependence. Thus, given any two other vectors ι//1 and ψ2 in 3fR, there
would be a linear relation
uψ + βψl + γψ2 = 0, 
(4.9)
where α, β, and y are complex numbers. Physically, there is a very natural way to
get additional vectors in J^R. If one replaces Mκ in Fig. 7b by any other three
manifold A'with the same boundary (and with suitable strings in X connecting the
marked points on the boundary of Mκ), then the Feynman path integral on X
gives rise to a new vector in J^R . Picking any two convenient three manifolds X1
and X2 for this computation gives vectors ψ1 and ψ2 that can be used in (4.9). We
will consider the case in which Xv and X2 are the same manifolds as MR but with
different "braids" connecting the points on the boundary; this is indicated in
Fig. 7c.
Once ψ1 and ψ2 are obtained in this way, (4.9) has the obvious consequence
that
o. 
(4.10)
The three terms in (4.10) have a "physical" interpretation, evident in Fig. 7c. By
gluing ML back together with MR or one of its substitutes Xl and X2 , one gets back
the original three manifold M, but with the original link L replaced by some new
links Lί and L2. Thus, (4.10) amounts to a relation among the link expectation
values of interest, namely
αZ(L) + βZ(LJ + γZ(L2) = 0 . 
(4.11)
This recursion relation is often drawn as in Fig. 8. The meaning of this figure is
as follows. If one considers three links whose plane projections are identical
outside a disc, and look inside this disc like the three drawings in the figure, then
the expectation values of those links, weighted with coefficients α, /?, and γ, add to
zero.
It is well known in knot theory that (4. 1 1) uniquely determines the expectation
values of all knots in S
3. For convenience we include a brief explanation of this.
One starts with a plane projection of a knot, indicated in Fig. 9. The number p of
crossings is finite. Inductively, suppose that all knot expectation values for knots
with at most p — \ crossings have already been computed. One wishes to study
knots with/) crossings. If one haάβ = 0 in (4.11), one could at each crossing pass
the two strands through each other with a factor of — y/α in replacing an over-
crossing by an under-crossing. If this were possible, the lines would be effectively
transparent, and one could untie all knots. As it is, β φ 0, but the term
proportional to β reduces the number of crossings, giving rise to a new link whose
expectation value is already known by the induction hypothesis.
This process reduces the discussion to the case p = Q where there are no
crossings, and therefore we are dealing only with a certain number of unlinked and
unknotted circles. For practice with (4.11), let us discuss this case explicitly. In
Fig. 10, we sketch a useful special case of Fig. 8. The first and third links in links in
Fig. 10 consist of a single unknotted circle, and the second consists of two
unlinked and unknotted circles. If we denote the partition function for s unlinked
Quantum Field Theory and the Jones Polynomial
379
Fig. 8. A recursion relation for links
Fig. 9. A plane projection of a knot, with four crossings
α
