---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-011-44-horizontal-sections-over-a-disk-with-one-crit
section_title: "Horizontal sections over a disk with one critical value"
section_number: 4.4
pages: 40-52
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
the counts of pseudo-holomorphic sections of the Lefschetz ﬁbr ations Ei →Di using
the theory of horizontal sections developed by Seidel in [39]. In pa rticular we will
apply results from section 2.5 of that paper, so we adopt its notatio n. This theory
involves analysis of the symplectic connection, whose horizontal su bspaces are the
symplectic orthogonal subspaces to the ﬁbers, and the symplect ic parallel transport
deﬁned by horizontal lifting of paths in the base of the ﬁbration.
In order for this technique to work, we need to set up carefully a mo del Lefschetz
ﬁbration over a base S, the disk with one end, in order to ensure that all the sections
we need to count are in fact horizontal. The key properties are:
• Transversality of the boundary conditions over the strip-like end. This means
that we cannot use a standard model Dehn twist ﬁbration, but nee d to intro-
duce a perturbation somewhere.
MIRROR OF THE PROJECTIVE PLANE 41
• Non-negative curvature. The curvature of the symplectic conne ction is a two-
form on the base with values in functions on the ﬁbers (the Lie algebr a of the
group of Hamiltonian diﬀeomorphisms), and we require that this two- form
evaluated on a positive basis of the tangent space to the base yields a non-
negative function on the ﬁber. The standard model Dehn twist ﬁbr ation has
non-negative curvature, but requiring the perturbation to have non-negative
curvature imposes a constraint.
• Vanishing action of horizontal sections. This imposes a further con straint on
the perturbation.
As we progress through the construction, the deﬁnitions of all of these terms will
be recalled.
The ﬁrst step is to construct a ﬁbration which is ﬂat away from the c ritical point,
following section 3.3 of [39]. Let S be the Riemann surface {Rez ≤ 0, | Imz| ≤
1} ∪ {|z| ≤ 1} (a negative half-strip which has been rounded oﬀ with a half-disk).
Let M denote the ﬁber, which is a cylinder with three bands attached. The van-
ishing cycle V is the equator of the cylinder. The circle running through the core
of one of these bands is L. Equip M with a symplectic form ω = dθ such that L is
exact. Over S− = (−∞, −1] × [−1, 1], we let π :E− →S− be a trivial ﬁbration and
equip E with 1-form Θ and 2-form Ω = dΘ which are pulled back from the ﬁber (to
get a symplectic form we add the pullback a positive 2-form ν ∈ Ω 2(S), but this does
not aﬀect the symplectic connection). Following the pasting proced ure described in
[39, §3.3] (though with the cut on the right rather than the left), we can complete
this ﬁbration π :E →S to one where the monodromy around the boundary is τV , a
standard model Dehn twist supported near the vanishing cycle. Th e result has non-
negative curvature, is actually trivial on the part of the ﬁber away from the support
of the Dehn twist, and is ﬂat over the part of the base away from th e critical value.
For this ﬁbration, there is a Lagrangian boundary condition which ov er the end
corresponds to the pair ( L,τ V (L)). Of course, these are not transverse since τV is
identity in the band. Hence we will perturb the symplectic form by a te rm which
depends on a Hamiltonian. We will introduce the perturbation in a neigh borhood of
the edge ( −∞, −1] × {1}. Let β be a cutoﬀ function which
• is supported in U = {s +it | −2 ≤s ≤ −1, 1 −ǫ ≤t ≤ 1},
• vanishes along the bottom, left and right sides of U, and
• has ∂β/∂t ≥ 0.
Figure 11 shows the base of the ﬁbration; the region where β has support is shaded.
Let H be a Hamiltonian function on the ﬁber M, and let XH be its vector ﬁeld
deﬁned by ω(·,X H) = dH. Then over S−, where our ﬁbration was originally trivial
with Ω = dΘ pulled back from the ﬁber, consider
(76) Θ ′ = Θ + Hβds
(77) Ω ′ =dΘ ′ = Ω + βdH ∧ds −H(∂β/∂t )ds ∧dt
This modiﬁes the symplectic connection as follows: Let Y ∈TE v denote the general
vertical vector. Then if Z ∈TS , and Z h is its horizontal lift
(78) 0 = Ω ′(Y,Z h) = Ω( Y,Z h) +βdH (Y )ds(Z)
42 JAMES PASCALEFF
Figure 11. The base of the ﬁbration with the region of perturbation shaded.
If we denote by Z again the horizontal lift with respect to the trivial connection,
we have Z h =Z −βds(Z)XH. Since β ≥ 0, this means that as we parallel transport
in the negative s-direction through the region U, we pick up a bit of the Hamiltonian
ﬂow of H, compared with the trivial connection. By adjusting the function β, we can
ensure that the parallel transport along the boundary in the posit ive sense picks up
φH, the time 1 ﬂow of H.
We must compute the curvature of this connection. This is the 2-fo rm on the base
with values in functions on the ﬁbers given by Ω ′(Z h
1,Z h
2 ). It will suﬃce to compute
for Z1 = ∂/∂s and Z2 = ∂/∂t, a positive basis. We have Z h
1 = ∂/∂s −βXH and
Z2 =∂/∂t.
Ω ′(Z h
1,Z h
2 ) =
Ω(Z h
1,Z h
2 ) +βdH (Z h
1 )ds(Z h
2 ) −βdH (Z h
2 )ds(Z h
1 ) −H(∂β/∂t )ds ∧dt(Z h
1,Z h
2 )
(79)
The ﬁrst term vanishes because Z h
2 is horizontal for the trivial connection, the sec-
ond term because ds(Z h
2 ) = 0, and the third because dH(Z h
2 ) = 0. This leaves
−H(∂β/∂t )ds ∧dt(Z h
1,Z h
2 ) = −H(∂β/∂t ). By our assumptions on β, this is non-
negative as long as H ≤ 0.
We equip the deformed ﬁbration with a Lagrangian boundary conditio n Q given
by parallel transport of L around the boundary. This picks up a Dehn twist and the
time 1 ﬂow of H, so over the end we have the pair ( L,φ H(τV (L))).
A horizontal section is a map u : S → E such that Du(TS ) = TE h. The impor-
tance of such sections is that, while they are determined by the sym plectic connection,
they are pseudo-holomorphic for any horizontal complex structure J, meaning an al-
most complex structure that preserves TE h and for which the projection E → S is
holomorphic.
The action A(u) of a section u is deﬁned to be
∫
Su∗Ω ′. The symplectic area of u
is then A(u) +
∫
Sν. The identity relating action to energy is ([39], eq. 2.31)
(80) 1
2
∫
S
||(Du)v||2 +
∫
S
f (u)ν =A(u) +
∫
S
|| ¯∂Ju||2
for any horizontal complex structure J. Here Du = (Du)h + (Du)v is the splitting
induced by the connection, and f is the function determined by the curvature as
f (π∗ν|TE h) = Ω ′|TE h. In our example f is supported near the critical point and in
suppβ, where f = −H(∂β/∂t ).
A direct consequence of (80) is the following:
MIRROR OF THE PROJECTIVE PLANE 43
Proposition 4.9. If the curvature of π : E → S is non-negative, and if u is a J-
holomorphic section with A(u) = 0 , then u is horizontal and the curvature function
f vanishes on the image of u.
With all this in mind, we choose our Hamiltonian H :M → R as follows:
• H ≤ 0 and H = 0 near ∂M . This ensures that the ﬁbration is still trivial
near the horizontal boundary and that the curvature is non-neg ative within
suppβ.
• H achieves its global maximum of 0 near ∂M and on the “cocore” of the band
in M. It achieves its minimum along the vanishing cycle, and has no other
critical points in the cylinder or lying on L (which intersects the vanishing
cycle and the cocore once). The ﬁrst condition implies that horizont al sections
passing through the cocore do not pick up any curvature, while the second is
there in order to ensure that ( L,φ H(τV (L))) is a transverse pair.
• The ﬂow φH has the property that L ∩φH (τV (L)) consists of one point x lying
on the cocore of the band. At this point, the tangent space to φH(τV (L)) is a
small clockwise rotation of the tangent space to L.
This implies that this intersection point has degree zero. To see this, recall
from Section 3.3.5 that the ﬁber has foliation by circles. We extend th is
foliation into the attached bands, foliating each band by intervals. T he Dehn
twist τV preserves this foliation, so it admits a grading in the sense of [41,
(12i)], namely an R-valued lift of the S1-valued function α(DτV (Λ))/α(Λ)
deﬁned on the Lagrangian Grassmannian bundle. We can choose the lift
to be zero in the bands, where τV is the identity. The Lagrangians L and
φH(τV (L)) do not rotate with this foliation, so they admit gradings. Thus,
if we equip L with some grading and φH(τV (L)) with the induced grading,
the R-valued grading functions for L andφH(τV (L)) diﬀer by a small amount.
Since tangent space to φH(τV (L)) is a small clockwise rotation of the tangent
space to L, the intersection point x has degree zero.
After this setup, we come to the problem of determining the set MJ (x) of J-
holomorphic sections u : S → E satisfying u(∂S ) ⊂ Q which are asymptotic to
x ∈L ∩φH(τV (L)) over the end.
Proposition 4.10. LetJ be a horizontal complex structure. Then MJ (x) consists of
precisely one section. It is horizontal, has A(u) = 0 , and is regular.
Proof. The ﬁrst step is to construct a horizontal section. Any horizonta l section, if it
exists, is determined by parallel transport of the point x ∈L ∩φH (τV (L)) throughout
E. Consider the section over S− given by u− : (s,t ) ↦→(s,t,x ). This is horizontal
outside supp β, since the ﬁbration is trivial over S− \ suppβ. In supp β, the fact
that x lies at a critical point of H means that ( TE h)(s,t,x) is the same as for the
trivial connection, so the section is horizontal there as well. Near t he singularity, the
ﬁbration is trivial in the band where x lies, so u− extends to a horizontal section
u :S →E.
For this section, we compute A(u) =
∫
Su∗Ω ′. Since u lies in the region where τV
is trivial,
∫
S\supp βu∗Ω ′ = 0. Since u passes through the point x where H(x) = 0, the
contribution
∫
supp βu∗Ω ′ =
∫
supp β −H(x)(∂β/∂t )ν vanishes.
44 JAMES PASCALEFF
Since A(u) = 0, any u′ ∈ MJ (X) must also have action 0. To see this, note
that Θ ′ is exact on each ﬁber of the boundary Lagrangian Q. This implies that
Θ ′|Q =π∗κQ +dKQ, where κQ is a one-form on ∂S , and KQ is a function on Q. Thus
(81) A(u) =
∫
S
u∗Ω ′ =
∫
∂S
u∗Θ ′ =
∫
∂S
κQ +
∫
∂S
dKQ
The ﬁrst term on the right-hand side does not depend on u, and the second term,
which is the net change in KQ along u(∂S ), depends on the asymptotic data for u,
which is the same for all u ∈ MJ (X).
Because the curvature of π : E → S is non-negative, proposition 4.9 implies that
u′ is horizontal. Since u′ and u are both asymptotic to x, they are equal. Hence
MJ (x) = {u}.
It remains to show that u is regular. The linearization of parallel transport along u
trivializes u∗(TE v) such that the boundary condition u∗(TQ ) is mapped to a family
of Lagrangian subspaces which, as we traverse ∂S in the positive sense, tilt clockwise
by a small amount. That ind Du,J = 0 follows from Proposition 11.13 of [41]. On the
other hand, Lemma 2.27 of [39] applies to the section u, implying ker Du,J = 0. We
could also appeal to Lemma 11.5 of [41] (with µ(ρ1) = 0 and |Σ −| = 1) to see that
kerDu,J = 0. Hence coker Du,J = 0 as well. □
4.5. Polygons with ﬁxed conformal structure. Recall from section 4.3 the trivial
ﬁbration π : ˆX 0 → T 0, with ﬁber M, where T 0 is a a disk with ( k + 3) boundary
punctures. We have ˆX 0 = M ×T 0 symplectically. We equip ˆX 0 with a product
almost complex structure J =JM ×j, where j is the complex structure on T 0.
Proposition 4.11. The (j,J )-holomorphic sections u : T 0 → ˆX 0 are in one-to-one
correspondence with (j,J M )-holomorphic maps uM :T 0 →M.
Proof. Givenu :T 0 → ˆX 0, write u = (uM,u T 0) with respect to the product splitting.
SinceJ is a product each component is pseudo-holomorphic in the appropria te sense.
But uT 0 is the identity map because u is a section. This correspondence is clearly
invertible. □
This reduces the problem of counting sections u : T 0 → ˆX 0 to the problem of
counting maps uM : T 0 → M. We emphasize that we are counting maps from a
Riemann surface with a ﬁxed conformal structure.
The maps uM : T 0 → M are holomorphic maps between Riemann surfaces, and
hence their classiﬁcation is mostly combinatorial. However, because we are in a
situation where the conformal structure on the domain is ﬁxed, we are not quite in
the situation described, for example, in [41, §13]. The holomorphic curves we are
looking for have non-convex corners and hence boundary branch points or “slits,”
and if the situation is complicated enough they may also have branch p oints in the
interior. However, the condition that the conformal structure o f the domain is ﬁxed
makes this an index zero problem, which is to say it prevents these slit s and branch
points from deforming continuously. The question is then, given a co mbinatorial type
of such a curve, what conformal structures (with multiplicity) can be realized by
holomorphic representatives?
The (k + 3) boundary components of T 0 are equipped with Lagrangian bound-
ary conditions ˆL(0)0, ˆL(n)0
0,..., ˆL(n)0
k, ˆL(n +m)0. Recall that over the ends where
MIRROR OF THE PROJECTIVE PLANE 45
disk bubbles are attached we have ˆL(n)0
i = τi( ˆL(n)0
i−1), where τi is the monodromy
around the i-critical point inside the i-th disk bubble. In section 4.4, we reﬁned the
construction and made a particular choice for this monodromy:
(82) τi =φH ◦τV
Since all of these symplectomorphisms are isotopic, we will denote th em all by τ for
most of this section.
In order to simplify notation, for the rest of this section 4.5 we will dr op the hats
and superscript zeros and denote by
(83) L(0),L (n),τL (n),τ 2L(n),...τ kL(n),L (n +m) ⊂M
the Lagrangians in the ﬁber M which give rise to the boundary conditions over the
(k + 3)-punctured diskT . Though the monodromies are all denoted by τ , we actually
choose the perturbations slightly diﬀerently so as to ensure that t his collection of
Lagrangians is in general position in M; this is necessary for the argument in Lemma
4.20.
Recall that q1 = qa,i and q2 = qb,j are the morphisms whose product we wish to
compute. We now regard qa,i ∈ L(0) ∩L(n) and qb,j ∈ τ kL(n) ∩L(n +m). Let
xi ∈τ i−1L(n) ∩τ iL(n) denote the unique intersection point.
Recall that the possible output points qa+b,h ∈ L(0) ∩L(n +m) are indexed by
h ∈ {0, 1,...,
⌊
(n+m)−|a+b|
2
⌋
}.
We can now state the main results of this section.
Proposition 4.12. If h is such that 0 ≤ h − (i +j) ≤ k, then there are
( k
h−(i+j)
)
homotopy classes of maps u :T →M satisfying the boundary conditions and asymp-
totic to qa,i,x 1,...,x k,q b,j,q a+b,h at the punctures. For h outside this range there are
no holomorphic maps satisfying these conditions.
Proposition 4.13. For each feasible homotopy class from Proposition 4.12, and for
each complex structure j on T , there is exactly one holomorphic representative u :
T →M.
The strategy of proof is ﬁrst to prove Proposition 4.12, which is don e in §4.5.1.
Then we show the existence of holomorphic representatives for so me conformal struc-
ture ( §4.5.2), and show that the number of representatives does not dep end on the
conformal structure. By degenerating the domain we are able to s how uniqueness
(§4.5.3).
4.5.1. Homotopy classes. The analysis of homotopy classes requires some explicit
combinatorics, which we shall now set up. Recall that M is a cylinder with three
bands attached, one for each of L(0),L (n),L (n +m). We will classify homotopy
classes of maps u :T → M by their boundary loop ∂u, which must be contractible,
traverse L(0),L (n),...,τ kL(n),L (n +m) in order, and hit the intersection points
qa,i,x 1,...,x k,q b,j,q a+b,h in order. That they arise as the boundary of a holomorphic
map controls their behavior within the bands.
Let us use L(n) to frame the cylinder, so that winding around the cylinder is
computed with respect to L(n). Let x ∈ M be a basepoint which is located in the
band near the intersection points xr. Let α ∈π1(M,x ) denote a loop that enters the
46 JAMES PASCALEFF
cylinder from the bottom, veers right, winds around once, and goe s back downward
to x. We also have a class β ∈π1(M) that is represented by the loop L(n), oriented
upward through the cylinder. Note that α and β generate a free group in π1(M).
Lemma 4.14. L(0) winds −(n − |a|)/2 times relative to L(n). τ rL(n) winds r times
relative to L(n). L(n +m) winds (m − |b|)/2 +k times relative to L(n).
Proof. We are using the symbols L(0),τ rL(n),L (n + m) to represent certain La-
grangians in a single ﬁber M, but we can compute the windings by comparing our
situation to certain ﬁbers of the original ﬁbration. In the original ﬁ bration,L(0) and
L(n) intersect in the ﬁber containing qa,i. Thus we have that L(0) winds −(n − |a|)/2
times relative to L(n). Now τ rL(n) winds r times relative to L(n) by construction.
Finally, in the original ﬁbration L(n +m) and L(n) intersect in the ﬁber containing
qb,j, and the relative winding in that ﬁber is ( m − |b|)/2. In the current context, this
becomes the winding of L(n +m) relative to τ kL(n). Thus the winding of L(n +m)
relative to L(n) in current context is ( m − |b|)/2 +k. □
The only unknown is how many times the boundary path traverses L(0), L(n),
τL (n), etc., as we traverse the boundary in the positive sense. The arg ument from
Proposition 4.7 shows that a holomorphic map cannot enter the band s corresponding
to L(0) and L(n +m). Hence the portion of our loop along L(0) and L(n +m) lies
within the cylinder, and therefore it is determined by the choices of qa,i,qb,j andqa+b,h.
As for the portion of the loop along τ rL(n), this can be represented by a sequence
of integers (δr)k
r=0, where δr represents the number of times we wind around τ rL(n).
With these conventions in place, we can compute the winding of a choic e of paths
satisfying the boundary and asymptotic conditions. We record the parts of the com-
putation:
• Passing from xk to qb,j by a short upward path on τ kL(n) contributes
(84)
(
1 − j
(m − |b|)/2
)
(k)
• The winding around the cylinder along L(n +m) as we pass from qb,j toqa+b,h
is
(85)
[ h
(n +m − |a +b|)/2 − j
(m − |b|)/2
]
(−1)((m − |b|)/2 +k)
• The winding around the cylinder along L(0) as we pass from qa+b,h to qa,i is
(86)
[ i
(n − |a|)/2 − h
(n +m − |a +b|)/2
]
(n − |a|)/2
• Passing from qa,i to x1 by a short downward path on L(n) contributes 0 to
the winding around the cylinder.
Adding up these contributions and using the fact that ( m−|b|)/2+(n−|a|)/2+k =
(n +m − |a +b|)/2, we get a total of i +j −h +k. Thus, if we go up on τ kL(n) and
down on L(n), we pick up the class αi+j−h+k ∈π1(M,x ) for the loop from xk to x1.
Thus, the class αi+j−h+k corresponds to the choice δr = 0 for 0 ≤ r ≤ k. The
homotopy class of any other path can be computed from this as follo ws:
• Taking another path on L(n) contributes a factor βδ0 on the right.
MIRROR OF THE PROJECTIVE PLANE 47
• Passing from xr to xr+1 along τ rL(n) contributes the word
(87) ( αrβ)δr
where δr ∈ Z, and this class is added on the right.
• Going down on τ kL(n) rather than up contributes the class ( αkβ)δk on the
left, which up to conjugation is the same as adding the class ( αkβ)δk on the
right.
Thus the class in question is
(88) αi+j−h+k
k∏
r=0
(αrβ)δr
The key condition is that this class is trivial in π1(M). This means in particular that
all of the β’s must cancel out. Because α and β generate a free group we have the
following:
Lemma 4.15. In the word (88), the β’s cancel out if and only if δr ∈ {−1, 0, 1} for
0 ≤ r ≤ k, the ﬁrst nonzero δ is 1, the last nonzero δ is −1, and the nonzero δ’s
alternate in sign.
Proof. The ﬁrst thing to see is that |δr| ≤ 1 for 1 ≤r ≤k. This is because ( αrβ)2 =
αrβα rβ contains an isolated β, while (αrβ)−2 contains an isolated β−1. Then we can
see that the nonzero δ’s must alternate sign, since having two consecutive δ’s equal
to 1 yields αr1βα r2β, which has an isolated beta, while having two consecutive δ’s
equal to −1 would yield an isolated β−1.
Since the nonzero δ’s in the range 1 ≤ r ≤ k alternate in sign, all the β’s coming
from the range 1 ≤r ≤k cancel, except for possibly the ﬁrst or the last. This implies
that |δ0| ≤ 1 as well, since the only thing that can cancel βδ0 is the ﬁrst non-identity
factor or the last non-identity factor.
Now the β from the ﬁrst non-identity factor can only cancel the β from the last
non-identity factor if all the α’s as well as β’s in between cancel. This means that
(89)
b∑
r=a
rδr = 0
for the appropriate range of r: a ≤ r ≤ b. Since the δ’s are in {−1, 0, 1} and they
alternate in sign, the only solution to this equation is when all δ = 0. In this case,
the ﬁrst and the last non-identity factors are in fact consecutive , the ﬁrst has δ = 1,
while the last has δ = −1. This shows that it is impossible to have β−1 from the ﬁrst
factor cancel a β from the last factor.
In general, we ﬁnd that each β is canceled by a β−1 from the next non-identity
factor, so that the nonzero δ’s alternate sign for 0 ≤ r ≤ k, the ﬁrst nonzero δ is 1,
and the last nonzero δ is −1. □
By passing to H1(M; Z), we obtain the relations
(90)
k∑
r=0
δr = 0
48 JAMES PASCALEFF
(91) i +j −h +k +
k∑
r=0
rδr = 0
Equation (90) is implied by Lemma 4.15, while (91) determines which h the homotopy
class contributes to.
The sequences (δr)k
r=0 which solve the constraints are in one-to-one correspondence
with sequences (sr)k−1
r=0 such thatsr ∈ {0, 1}. In one direction, we extend the sequence
bys−1 = 0 = sk, and set
(92) δr =sr −sr−1
In the other direction, given δr, we can solve for sr using this equation the initial
condition s−1 = 0. Since the signs of the nonzero δr alternate, and the ﬁrst nonzero
term is 1, we will have sr ∈ { 0, 1}, and since the ﬁnal nonzero term is −1, we will
havesk = 0, thus inverting the correspondence. This yields 2 k solutions.
Plugging this into the summation in (91), we have
(93)
k∑
r=0
rδr =
k∑
r=0
r(sr −sr−1) =
k−1∑
r=0
(−1)sr
because the summation telescopes. This is simply minus the number of 1’s in the
sequence sr. Thus we obtain
(94) h − (i +j) = k −
k−1∑
r=0
sr
The right hand side is always an integer between 0 and k, and it takes the value s for(k
s
)
choices of the sequence ( sr)k−1
r=0. Thus homotopy classes of maps exist for h such
that 0 ≤h − (i +j) ≤k, and there are
( k
h−(i+j)
)
such classes. This proves Proposition
4.12.
4.5.2. Existence of holomorphic representatives for some conform al structure. The
ﬁrst step in characterizing the holomorphic representatives of th ese homotopy classes
is to prove the existence of holomorphic sections for some conform al structure. This
is also essentially combinatorial.
We begin with some general concepts that will be useful in the proof .
Deﬁnition 5. Let γ :S1 → C be a piecewise smooth loop. A subloop γ′ of γ is the
restriction γ′ =γ|⋃
αIα to a collection of intervals ⋃
αIα. The indexing set inherits
a cyclic order from S1, and we require that for each α, γ(maxIα) = γ(minIα+1) is
a self-intersection of γ. Thus γ′ simply “skips” the portion of γ between maxIα and
minIα+1. A subloop is called simple if it is non-self-intersecting.
Note that a subloop is not the same as a loop formed by segments of γ joining
self-intersections. Such an object is only a subloop if the segments appear in a cyclic
order compatible with γ.
Deﬁnition 6. A piecewise smooth loop γ : S1 → C is said to have the (weak)
positive winding property (PWP) if the winding number of γ around any point in
C \ image(γ) is non-negative. The loop γ is said to have the strong positive winding
property (SPWP) if every subloop γ′ ⊂γ has the positive winding property.
MIRROR OF THE PROJECTIVE PLANE 49
Lemma 4.16. A loop γ :S1 → C has SPWP if and only if every simple subloop has
PWP.
Proof. The “only if” direction is contained in the deﬁnition. Suppose that eve ry
simple subloop of γ has PWP. If γ′ is a subloop that is not simple, then by splitting
γ′ at a self-intersection, we can write γ′ as the composition of two proper subloops.
Repeating this inductively, we can write γ′ as the composition of simple subloops.
By hypothesis, each of these subloops winds positively, and the wind ing of γ′ about
a point is the sum of the contributions from each of the simple subloop s. □
The next lemma shows that the strong positive winding property is st able under
branched covers. Suppose γ is a loop and y ∈ C \ image(γ) is a point where the
winding number of γ is m >1. Taking the m : 1 cover branched at y, we can lift γ
to a path ˜γ. The path ˜γ is a loop that covers γ.
Lemma 4.17. Supposeγ has SPWP. Then ˜γ has SPWP.
Proof. Suppose that ˜γ does not have SPWP. Then some subloop ˜ γ′ does not have
PWP. By Lemma 4.16, we may take ˜γ′ to be a simple subloop. Thus ˜γ′ winds around
some region once clockwise, and we have ˜ γ′ = ∂ ˜C, where ˜C is the chain consisting
of this region with coeﬃcient −1. Pushing ˜γ′ and ˜C forward under the branched
cover, we obtain a subloop γ′ ⊂γ, and chain C such that γ′ =∂C . Since ˜C is purely
negative, no cancellation can occur when we push forward, and C is purely negative
as well. Thus γ′ winds negatively about a point in the support of C, which contradicts
SPWP for γ. □
Lemma 4.18. Suppose γ : S1 → C is a piecewise smooth loop with SPWP. Then
there is a map u :D2 → C holomorphic on the interior of D2 such that ∂[u] = γ.
Proof. The idea of the proof is to iteratively take branched covers of the p lane and
liftγ so as to reduce the density of winding. So let y ∈ C \ image(γ) be a point where
the winding number is m >1. Taking the m : 1 branched cover at y, we obtain as
in Lemma 4.17 a lift ˜ γ that covers γ once and has SPWP. Repeating this process
and using Lemma 4.17 to guarantee that the lift always has SPWP, eve ntually we
obtain a simple piecewise smooth loop with positive winding. This loop bounds a
simply connected region in M, where M is the Riemann surface resulting from the
branched covering construction. By the Riemann mapping theorem , there is a map
from this region to the unit disk D2, biholomorphic on the interior and continuous
on the closure, that maps each boundary segment to an arc in ∂D 2 and each corner
to a point on ∂D 2. Let ˜u :D2 →M be the inverse of that map. Composing ˜ u with
the covering M → C yields the desired map u. □
Fix a choice of homotopy class φ of polygons u :T →M, which essentially means
ﬁxing a choice for the sequence ( δr)k
r=0. Passing to the universal cover ˜M of the ﬁber,
ﬁx a choice of lift ˜u :T → ˜M . Let y ∈ ˜M be any point. Because the boundary loop
∂[u] is contractible in M, it lifts to a closed loop ∂[˜u] in ˜M . In fact ∂[˜u] is contained
in a domain which is isomorphic to a domain in C, and with this identiﬁcation, we
have the following.
Lemma 4.19. The boundary loop ∂[˜u] has SPWP.
50 JAMES PASCALEFF
Proof. The key observation is that the slopes of the paths L(0),L (n),...,τ kL(n),L (n+
m) through the cylinder are positive and monotonically decreasing. If we frame the
cylinder using L(0), then
• L(0) has slope ∞
• L(n) has slope [( n − |a|)/2]−1
• τ rL(n) has slope [ r + (n − |a|)/2]−1
• L(n +m) has slope [( n +m − |a +b|)/2]−1.
Only at the intersection between L(n +m) and L(0) does the slope increase.
Hence as we traverse ∂[˜u], or any subloop thereof, the slope can only increase at
one point. This point is either where the subloop either uses or skips o verL(0).
Now we use some elementary plane geometry. Suppose that P is an oriented
polygonal path in the plane (possibly self-intersecting), all of whos e sides (Si)N
i=1 have
positive slope. Suppose that P winds negatively around some point y. We claim the
slope has to increase at no fewer than two vertices. We prove this b y induction on
the number of sides N.
Checking cases proves the claim when N = 3 and P is a triangle. See ﬁgure 12(a).
Suppose for induction that the claim is true for N <N0. Now we prove the claim
ifP is a simple N0-gon, so assume for a contradiction that P is a simple N0-gon that
winds negatively and has at most one vertex where the slope increas es. We assume
that N0 > 3, so there must be a side Si such that at both ends there is a decrease
in slope. We remove the side Si from the N0-gon P and extend the two incident
sides Si−1 and Si+1 in order to obtain an ( N0 − 1)-gon P ′. Since P has at most
one vertex where the slope increases, so does P ′: Since the slope decreased at both
Si−1Si and at SiSi+1, it will decrease at the new vertex Si−1Si+1. See Figure 12(b).
Since the original simple loop P winds negatively, the new loop P ′ must also wind
negatively around some point. This contradicts the induction hypot hesis. Now we
have established the claim for simple N0-gons.
Now supposeP is a self-intersecting N0-gon, that winds negatively around y. Using
Lemma 4.16, we can ﬁnd a simple subloop P ′ winding negatively around y. Since P ′
is a simple N-gon for some N ≤N0, it must have at least two vertices where the slope
increases. For each vertex v ofP ′ where the slope of P ′ increases, there is a vertex in
the original polygon P where the slope increases, either at v itself, or at some point
in the interval of P that was deleted at v. Thus, since P ′ has at least two vertices
where the slope increases, so does P .
□
Having chosen a lift ∂[˜u] of the boundary loop, deﬁne a 2-chain C on ˜M whose
multiplicity at y is the winding number of ∂[˜u] around y. This has ∂C =∂[˜u].
Lemma 4.20. There is a complex structure j on T and a holomorphic map ˜u :T →
˜M such that ˜u∗[T ] = C.
Proof. Lemma 4.19 allows us to apply Lemma 4.18, which yields map ˜ u : T → ˜M .
More precisely, the complex structure on T is the one obtained from uniformization
of the region bounded by the simple lift of γ =∂[u] at the end of the construction in
4.18, as a Riemann surface with boundary and punctures (at the no n-smooth points
of the loop). □
MIRROR OF THE PROJECTIVE PLANE 51
(a)
*
*
*
*
(b)
S₁
1
2 3 1
2
3
m₁ < m₂ < m₃
m₃ < m₁ < m₂
S₃
S₂
Figure 12. (a) Negatively winding triangles with positive slopes have
two slope increases ( m denotes slope). (b) Removing the side S2.
Pushing the map ˜u from Lemma 4.20 down to M, we obtain the existence of a
holomorphic representative in the homotopy classφ, for a particular complex structure
on the domain.
4.5.3. The moduli space of holomorphic representatives with varyi ng conformal struc-
ture. Let M(φ,j ) denote the moduli space of ( j,J M )-holomorphic maps u :T →M
in the homotopy class φ. Let M(φ) = ⋃
j M(φ,j ) denote the moduli space of such
maps with varying conformal structure on the domain. Let Rk+3 denote the moduli
space of conformal structures on the disk with ( k + 3) boundary punctures. There is
a natural map π : M(φ) → Rk+3 which forgets the map.
Lemma 4.21. For any u ∈ M(φ,j ), we have indDu,(j,JM ) = 0 and kerDu,(j,JM ) = 0.
Proof. Let the intersection points qa,i,x 1,...,x k,q b,j be regarded as positive punctures
and let qa+b,h be regarded as a negative puncture. Then by the conventions for
Maslov index, we have that all of these intersection points have inde x 0, for as we go
L(0) → L(n), L(n) → τL (n), . . . , τ kL(n) → L(n +m), and L(0) → L(n +m), the
Lagrangian tangent space tilts clockwise by a small amount. Then by Proposition
11.13 of [41] (with |Σ −| = 1 for the negative puncture), we have ind Du,(j,JM ) = 0.
Furthermore, the operator Du,(j,JM ) is a Cauchy–Riemann operator acting on the
line bundle u∗TM , so the results of Section (11d) of [41] apply. The hypotheses of
Lemma 11.5 are satisﬁed with µ(ρ1) = 0 and |Σ −| = 1, so ker Du,(j,JM ) = 0. □
Lemma 4.22. The map π : M(φ) → Rk+3 is a proper submersion of relative dimen-
sion zero (that is, a ﬁnite covering).
Proof. The index ind Du,(j,JM ) = 0 is the expected dimension of the space of curves
with ﬁxed conformal structure. When we allow the conformal stru cture to vary, this
52 JAMES PASCALEFF
adds k = dim Rk+3 dimensions, so M(φ) has expected dimension k. Lemma 4.21
implies cokerDu,(j,JM ) = 0, so M(φ) is a manifold of dimension k.
Ifu ∈ M(φ,j ) ⊂ M(φ) is a point where the map π : M(φ) → Rk+3 is not a submer-
sion, we must have ker Dπ ⁄= 0. On the other hand ker Dπ consists of inﬁnitesimal
deformations of the map which do not change the conformal struc ture on the domain,
and so is equal to ker Du,(j,JM ), which is zero by the previous lemma. Hence π is a
submersion.
The properness of π is an instance of Gromov–Floer compactness. The only thing
to check is whether, as we vary j ∈ Rk+3, any strips can break oﬀ. This is impossible
because our boundary conditions do not bound any bigons in M. □
Lemma 4.23. The map π : M(φ) → Rk+3 has degree one.
Proof. For this Lemma we will pass to the Gromov–Floer compactiﬁcation ¯π : ¯M(φ) →
¯Rk+3. Because no bigons can break oﬀ, this compactiﬁcation consists en tirely of sta-
ble disks, and ¯π is also a proper submersion. Hence to count the degree of π, it will
suﬃce to count the points in the ﬁber of ¯ π over a corner of ¯Rk+3, which is to say when
the domain is a maximally degenerate stable disk.
A maximally degenerate stable disk S = (G, (Sα)) consists of a trivalent graph
G = (V,E f in∪E∞) without cycles, with (k + 3) inﬁnite edges E∞, and a disk Sα with
three boundary punctures for each α ∈V . The boundary punctures of Sα are labeled
by elements ofEf in∪E∞. The elements of Ef in correspond to nodes of the stable disk,
while the elements of E∞ correspond to boundary punctures of the smooth domains
in Rk+3. The homotopy class φ determines the Lagrangian boundary conditions on
each component Sα, and the asymptotic values at the boundary punctures labeled by
E∞. The position of the nodes labeled by Ef in is not determined a priori .
Looking at the Lagrangians L(0), L(n), . . . , L(n +m) shows that any three of
them bound triangles, and that such triangles are determined by tw o of the corners.
Hence by tree-induction starting at the leaves of stable disk (thos e Sα for which two
punctures are labeled by E∞), the positions of all the nodes are determined by φ, or
we run into a contradiction because no triangles consistent with the labeling exist.
Furthermore, in each homotopy class of triangles consistent with t he labeling of
Sα, there is exactly one holomorphic representative.
Hence there is at most one stable map from the stable domain S = (G, (Sα)) to M
consistent with the homotopy class φ.
Thus we have shown that the degree of π : M(φ) → Rk+3 is either zero or one. On
the other hand, Lemma 4.20 shows that M(φ) is not empty, so the degree must be
one. □
Proposition 4.13 follows immediately from Lemmas 4.22 and 4.23.
