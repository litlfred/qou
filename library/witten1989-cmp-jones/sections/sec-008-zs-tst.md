---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-008-zs-tst
section_title: "Z(S*) = (TST"
section_number: null
pages: 40-47
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
m)w 
(4.40)
This may readily be evaluated. In the Verlinde basis, Γis a diagonal matrix with
T 
ΌΪ = £
2πί(
Λ'-< /
24 ) . v.-y fa. is the conformal weight of the primary field in the
representation Rt and c is the central charge for current algebra with symmetry
group G at level k. Since hQ = 0, if we replace (4.38) by (4.40) the partition function
transforms as
Z-»Z exp (2πi(n-m) 
. 
(4.41)
Though we have obtained this formula in the example of a particular surgery
(giving S
3 from S
2 x S
1), the same ambiguity arises in any process of surgery.
Whenever one makes surgery on a circle C, in a three manifold M, with the surgery
being determined by an SL (2, Z) element u, one could instead consider surgery on
the same circle C, using the 5L(2, Z) element u - T
m. This would have the same
effect topologically, but our surgery law would give a partition function
containing an extra phase exp( — 2πim - c/24).
This phase ambiguity was already encountered, in the large k limit, in formula
(2.24). What is more, from the discussion in Sect. 2, we know what topological
structure on three manifolds must be considered in order to keep track of the
factors of exp(2τπ c /24). One must consider "framed" three manifolds. Two
surgeries that have the same effect on the topology of a three manifold may have
different effects on the framing. I will discuss elsewhere how to systematically keep
track of the factors of exp (2πi 
c/24) under surgery. In the simple applications in
this paper, this will not be necessary. All of our applications will involve
considering the standard surgery (by the modular transformation S) that was used
in the last subsection to obtain S
3 from S
2 x S
1.
Some Expectation Values. Now let us see if we can go farther and determine the
path integral Z (*S
3; JR; ) on S
3 with an unknotted Wilson line on S
3 in an arbitrary
Quantum Field Theory and the Jones Polynomial 
391
representation Rj.
16 To do this, we start on S
2 x S
1 with a Wilson line in the Rj
representation running parallel to the circle C on which we are doing surgery, as in
Fig. 15b. Carrying out the same surgery as before turns S
2 x S
1 into S
3, with a
Wilson line in the Rj representation on S
3. Application of (4.27) now gives
S
l;Ri,Rj). 
(4.42)
Using (4.35), we can evaluate this and determine the partition function for a
Wilson line in an arbitrary representation Rp it is
Z(S
3 
Rj) = ^S0
ίgίJ = SOJ. 
(4.43)
ί
Let us compare this to our previous evaluation (4.23) of the expectation value of
an unknotted Wilson line in S
3. We must recall that the symbol (C> in (4.23)
represented a ratio <C> - Z(S
3;R)/Z(S
3). 
Let us take G - 5C/(2), so that we
can use the explicit formulas (4.39), and take R to be the two dimensional
representation of SU(2), so that we can compare to (4.23). Using (4.38), (4.43),
and (4.39), we get
^L =
 sin(
2^/(^ +
 2)) 
(Λ AΛ}
' 
( 
J
It is easy to see that setting N = 2 in (4.23) gives the same formula. Let us take this
one step further and try to calculate by these methods the partition function
Z(5
3; RJ, Rk) for S
3 with two unknotted, unlinked Wilson lines in represen-
tations RJ and Rk. In Fig. 15c, we start on S
2 x S
1 with two Wilson lines, in
representations Rj and Rk, parallel to the circle C on which surgery is to be
performed. Carrying out the surgery, we get to S
3 with the desired unlinked,
unknotted circles. In this case, the surgery formula (4.27) tells us that
Z(S
3ι Rj, Rk) = ΣS
l
0Z(S
2xS
1; Ri9Rj, Rk) . 
(4.45)
i
The right-hand side can be evaluated with (4.36), while the left-hand side can be
reduced to (4.43) using (4.6). We get
(4.46)
Proof of Verlinde's Conjecture. The last equation is a special case of a celebrated
conjecture by Verlinde, which has been proved by Moore and Seiberg [1 3]. We can
use these methods to give a new proof of Verlinde's conjecture, in the case of
current algebra. We will have to use the generalized surgery relation (4.28). We
return to Fig. 15b but now instead of treating C as a purely imaginary contour on
which surgery is to be performed, we suppose that there is a Wilson line on C in the
R{ representation. In this case, the standard surgery on C will still turn S
2 x S
1 into
S
3, but now on S
3 we will have two Wilson lines, in the Rt and Rj representations.
Some mental gymnastics shows that they are linked, as in Fig. 17 a; schematically,
16 We give this Wilson line the framing described in the footnote after (4.34); after surgery this
turns into the standard framing on S
3
392
E. Witten
Fig. 17a-c. In a, we sketch linked but unknotted Wilson lines on S
3, in the R, and Rj
representations. In b, a Wilson line R{ is linked with two Wilson lines Rj and Rk on S
3. In c, we
sketch how two crucial amplitudes can be factored through the same one dimensional space
we refer to this linked pair of Wilson lines as L (Rt; Rj). The use of (4.28) therefore
determines the partition function of S
3 with a pair of linked Wilson lines:
k
In the second step, we have used the fact that the partition function of S
2 x S
1 with
static charges Rk and Rj is the metric that we have called gkj - one iΐRk is dual to Rj
and otherwise zero.
Now let us go back to Fig. 15c, and again on what was previously the purely
imaginary circle C we put a Wilson line in the Rt representation. The standard
surgery on this link will now produce a picture sketched in Fig. 17b, with a Wilson
line on S
3 in the Rt representation that links a pair of Wilson lines Rjy Rk that are
themselves unlinked and unknotted. We call this configuration L (Rt; Rj, Rk). The
evaluation of (4.28) now gives
m 
m
To obtain Verlinde's formula, it is now necessary to find an independent way to
evaluate the left-hand side.
Such a method is provided by the following generalization of the multiplica-
tivity formula (4.1). The key point in the derivation of (4.1) was that the physi-
cal Hubert space for S
2 with no charges was one dimensional. It is likewise true
that the physical Hubert space Jtif for S
2 with a pair of charges in the dual
Quantum Field Theory and the Jones Polynomial 
393
representations Rt and Rτis one dimensional. Using this and otherwise repeating
the derivation of (4.1) gives the following formula:
Z(S
3;L(RiιRj9Rk)) 
Z(S
3;Rt) = Z(S^;L(Ri; Rj) 
- Z(S
3;L(Ri'9Rk)). 
(4.49)
The idea in (4.49) is that, as in Fig. 17c, the evaluation of Z(S
3; L (Rt; RJ9 Rk)) can
be expressed as a pairing (ψ, χ) where ψ and χ are certain vectors in ^ and its dual.
Likewise the evaluation of Z(S
3; Rt) is a pairing (ι/, υ), where υ' and v are vectors
in ffl and its dual. Using the wonderful fact of one dimensional linear algebra
(ψ,χ) ' (v',v) = (ψ,v) 
- (v',χ), we arrive at (4.49). Since all factors in (4.49) are
known except the first, we arrive at the result
c, RJ9 Rk)) = S^S^/S^. 
(4.50)
Combining this with (4.48), we have
SijStJS^^ΣsrN^. 
(4.51)
m
This is equivalent to Verlinde's statement that "the matrix S diagonalizes the
fusion rules". In other words, in the basis υ{ indicated in Fig. 13, the structure
constants of the Verlinde algebra are by definition υiυj = ^Ni^vk, where
k
N^ = Σ Nijr g
rk. If we introduce a new basis wt = S0 t ί 
]Γ S™ vm , then the Verlinde
r
algebra reduces to wi w} = Stj Wj . To verify this, we compute
wtwJ = ΣSt
kSJ
lvkvl 
S0,iS0.j. 
(4.52)
k,l
Using vkvl = ΣNkΓ
vm
 and (4.51), this becomes
wiwj = Sj
lv™ SnSr SOJ. 
(4.53)
Using the unitarity of S, in the form Sj S{1 = δijy we see that
w; Wj = δijΣS™ vm - SOJ = δtj 
- Wj , 
(4.54)
m
showing that the Verlinde algebra has been diagonalized and that the wt are
idempotents.
Connected Sum of Links. At the beginning of Sect. 4, we have seen that the
quantum partition function has a multiplicative behavior under connected sum
of three manifolds. From (4.1), if M=Mi+M2, 
then Z(M) 
Z(5
3)
= Z(M1) Z(M2). In the special case that Ml and M2 are copies of S
3 with links
in them, the connected sum of M1 and M2 is a copy of S
3 containing the
disconnected sum of the two links.
In knot theory there is also an operation of taking the connected sum of two
links. This operation has appeared in the above discussion. The link that we have
called L(RiιRj, Rk) is the connected sum of the two links that we have called
L(Ri9Rj) and L (Ri9Rk). In fact, in Fig. 17c, L(R^ R J 9 Rk) is "cut" into two pieces,
which are respectively L(Rί,Rj) and L(Ri,Rk) with in each case a connected
segment removed. This is the defining configuration for the "connected sum of
links". Accordingly, the reasoning that led to (4.49) has the following more
394 
E.Witlen
general consequence. If Lv and L2 are two links, and Lv -f- L2 is their connected
sum, then
Z(5
3;L 1+L 2) Z(5
3;C) = Z(5
3;L!) Z(S
3;L2). 
(4.55)
Here it is understood that [as in (4.49)] representations have been assigned to the
connected components of Ll , L2, and Lv + L2 in a compatible fashion; C is an
unknot placed in whatever representation is carried by the strand "cut" in the
generalization of Fig. 17c. Equation (4.55) has a generalization in which L1 and
L2 are links in arbitrary three manifolds M1 and M2; then the connected sum of
links L! -f L2 is a link in the connected sum of manifolds M= Mv + M2, and
(4.55) is replaced by
L1) Z(M2;L2). 
(4.56)
4.6. TTze A>2<9/ Polynomials and the Braid Group
The results in the last subsection are nice enough so that one may wonder if the
partition function for an arbitrary link on S
3 can be evaluated in this way. This
can indeed be done, and in a way that is closely related to the original route by
which the Jones polynomial was discovered, though we cannot expect such explicit
formulas as in the simple cases treated above. An arbitrary link L on S
3, whose
partition function we will call Z (5°; L), can be arranged in the form of a braid, as
indicated in Fig. 18 a. One can imagine "lifting" this braid B out of S
3 and putting
it on S
2 x S
l. To get back to S
3 one would have to do surgery on a circle running
parallel to the braid, as suggested in Fig. 18b. The general surgery formula (4.27)
then tells us
Z(S
3;L) = ΣS 0^Z(5
2xS
1; RJ9 B), 
(4.57)
j
where Z(S
2 x S
1; RJ9 B} is the partition function on S
2 x S
1 in the presence of
both the braid B and a parallel Wilson line in the Rj representation. We want to
rewrite this in the spirit of (4.32). Suppose that the braid B contains n strands
making up a collection of representations < Λ). Then B can be regarded as defining
an element of the Artin braid group on n letters. The braid group is closely related
to the mapping class group for S
2 with marked points. The reason for that is that if
in Fig. 18b we "cut" S
2 x S
1, to get back to S
2 x /(this amounts to undoing what
was done in Fig. 14, then the braid can be unbraided. Thus, the complete
information about the braid is in the choice of a diffeomorphism of S
2
(constrained to preserve the marking of the points) by which the top and bottom of
Fig. 18c are to be identified. This, however, does not quite mean that the braid
group is the same as the mapping class group. In Fig. 18b, there are n + 1 strands,
one of which arose from the surgery and does not participate in the braid, while the
other n strands make up the braid. The braid group on n letters is the subgroup of
the mapping class group on n -f1 letters which fixes one of the (framed) strands.
There are a number of invariant traces on the braid group that can be naturally
defined with the data at our disposal. They are
(4.58)
Quantum Field Theory and the Jones Polynomial
395
S'xS
1
Fig. 18a-d. Any link on S
3 can be shaped into the form of a braid, as in a; putting the same braid
on S
2 x S
l, and doing surgery on the circle Cindicated with the dotted line in part b, one gets back
to the original link on S
3. If one "cuts" S
2 x S
1 to get to S
2 x L the braid can be "unbraided"; the
braid is recovered by prescribing a diffeomorphism of S
2, via which the top and bottom of part c
are to be identified. In d, we sketch the origin of the key property of the braid traces. In the
presence of an arbitrary Wilson line on the dotted contour (reflecting the results of surgery), two
braids B1 and B2 are joined end to end in S
2 x S
1. There is no way to tell which comes first, so the
partition function is invariant under exchange of Bl and B2
This has the key property of a trace,
(4.59)
since the two sides of (4.59) have the same path integral representation, in which
the two braids are glued end to end in S
2 x S
1, as in Fig, 18d. Not only does (4.58)
obey (4.59); it is actually equal to the trace of the operator B in a certain
representation of the braid group, namely the representation furnished by the
physical Hubert space 2tf for S
2 with the n + 1 charges, it being understood that
the braid group is acting on the first n charges, and the (n + l)
sί is fixed in the Rt
representation. That τ^B) is the trace of B in this Hubert space is a statement just
along the lines of (4.32).
So we can rewrite (4.57) in the form
Z(S
3; L) = ΣS0
jτj(B). 
(4.60)
j
This shows that the link invariants on S
3 may be written as linear combinations of
braid traces. This is very close to how the knot polynomials were originally
396 
E. Witten
discovered. It is clear from the work of Tsuchiya and Kanie [11] and Segal [16]
along with what has been said above that the braid traces that arise from the
Chern-Simons theory are precisely those that first appeared in the work of Jones.
5. Applications To Physics
Finally, I would like to comment on the likely implications of these results for
physics. We have been exploring a three dimensional viewpoint about conformal
field theory, at least for the important special case of current algebra on Riemann
surfaces. Many aspects of rational conformal field theory have emerged as natural
consequences of general covariance in three dimensions. It seems likely that the
marvelous hexagons and pentagons of [13], and the other consistency conditions
of rational conformal field theories, can be synthesized by saying that such
theories come from generally covariant theories in three dimensions. If so, general
covariance in three dimensions may well emerge as one of the main unifying
themes governing two dimensional conformal field theory. Such considerations
have motivated a study of 2 -f 1 dimensional gravity which will appear elsewhere
[38].
The basic connection that we have so far stated between general covariance in
2 -f-1 dimensions and conformally invariant theories in 1 -f 1 dimensions is that
the physical Hubert spaces obtained by quantization in 2 + 1 dimensions can be
interpreted as the spaces of conformal blocks in 1 + 1 dimensions. This connection
may seem rather abstract, and I will now make a few remarks aimed at making a
more concrete connection. Starting from three dimensions we were led to the
problem of quantizing the Lagrangian (3.1), which we repeat for convenience:
^=έf
ΛF
T r^J/^
 
(5Λ)
This is to be quantized with constraints ε
l}' F^ = 0, these constraints being the
generators of the infinitesimal gauge transformations
Ai-tAi-Dte. 
(5.2)
So far we have quantized (5.1) on Riemann surfaces without boundary, but now
let us relax this requirement. Quantization of (5.2) in this more general case
amounts to studying the three dimensional Chern-Simons theory on a three
manifold with boundary, namely Σ x R
1, where Σ is a Riemann surface with
boundary. For instance, let Σ be a disc D. To quantize (5.1) on the disc, we must
impose the constraints, which generate the gauge transformations (5.2). As D has
a boundary, we must choose boundary conditions on At and ε (for closed surfaces
this question did not arise). We will adopt free boundary conditions for Ah but
require ε = 0 on the boundary of S. (A rationale for this choice is that the Chern-
Simons action is not invariant under gauge transformations that do not vanish on
the boundary.) With this condition, ε generates in (5.2) the group Gt of gauge
transformations which are the identity on the boundary of the disc. An element of
this group is an arbitrary continuous map V\ D -> G whose restriction to 5 is the
Quantum Field Theory and the Jones Polynomial 
397
identity. Now we impose the constraints. The first step is to require that ε
lj Ffj — 0.
Since the disc is simply connected, this implies that Ai — —di U U~
l for some
map U: D -> G. U is uniquely defined up to
U -> U 
W, 
(5.3)
for a constant element WεG. Then we must identify two [7's that differ by an
element of the restricted gauge group Gl. This means that we must impose the
equivalence relation U~ VU for any V such that V=\ on the boundary S. The
equivalence relation means that only the restriction of U to S is relevant. This
restriction defines an element of the loop group LG, but because of the freedom
(5.3), we should actually regard U as an element of LG/G. Geometrically, we have
learned that the homogeneous space LG/G can be regarded as the symplectic
quotient of the space of G connections on the disc D, by the group G1 of symplectic
diffeomorphisms. Now we wish to quantize the theory, which means doing
quantum mechanics on LG/G, which inherits a natural symplectic structure from
(5.1). Clearly, the group LG of gauge transformations on the boundary of Σ acts
on LG/G, so the quantum Hubert space will be at least a projective representation
of the loop group. In fact, according to Segal [39], the quantization of LG/G, with
this symplectic structure, gives rise to the basic irreducible highest weight
representation of the loop group. This makes the connection between 2 + 1 dimen-
sions and 1 +1 dimensions far more direct, since the irreducible representations
of the loop group are a basic ingredient in the 1 + 1 dimensional theory. It is
obvious at this point that by considering more complicated Riemann surfaces with
various boundary components, we can generate the whole 1 + 1 dimensional
conformal field theory, essentially by studying the generally covariant 2+1
dimensional theory on various three manifolds with boundary.
Acknowledgements. This work originated with the realization that some results about conformal
field theory described by G. Segal could be given a three dimensional interpretation by
considering a gauge theory with Chern-Simons action. I am grateful to Segal for explaining his
results, and to M. Atiyah for interesting me in and educating me about the Jones polynomial.
V.F.R. Jones and L. Kauffman, and other participants at the IAMP Congress, raised many
relevant questions. Finally, ί must thank S. Deser and D.J. Gross for pointing out Polyakov's
paper, G. Moore and N. Seiberg for explanations of their work, and the organizers of the I AMP
Congress for their hospitality.
