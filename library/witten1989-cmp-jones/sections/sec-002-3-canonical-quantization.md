---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-002-3-canonical-quantization
section_title: "Canonical Quantization"
section_number: 3
pages: 16-24
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
The basic strategy for solving the Yang-Mills theory with Chern-Simons action on
an arbitrary three manifold Mis to develop a machinery for chopping Min pieces,
solving the problem on the pieces, and gluing things back together. So to begin
with we consider a three manifold M, perhaps with Wilson lines, as in Fig. 4a. We
"cut" M along a Riemann surface Σ. Near the cut, M looks like Σ x R*, and our
first step in learning to understand the theory on an arbitrary three manifold is to
solve it on Σ x R
1.
The special case of a three manifold of the form Σ x R
1 is tractable by means of
canonical quantization. Canonical quantization on Σ x R
1 will produce a Hubert
space ^Σ, "the physical Hubert space of the Chern-Simons theory quantized on
Σ".
Ί These will turn out to be finite dimensional spaces, and moreover spaces that
have already played a noted role in conformal field theory. In rational conformal
field theories, one encounters the "conformal blocks" of Belavin, Polyakov, and
Zamolodchikov. Segal has described these in terms of "modular functors" that
canonically associate a Hubert space to a Riemann surface, and has described in
algebra-geometric terms a particular class of modular functors, which arise in
current algebra of a compact group G at level k [16]. The key observation in the
present work was really the observation that precisely those functors can be
obtained by quantization of a three dimensional quantum field theory, and that
this three dimensional aspect of conformal field theory gives the key to
understanding the Jones polynomial.
7 It is conventional in physics to call vector spaces obtained in this fashion 'Ήilbert spaces", and
we will follow this terminology. In fact, the claim that comes most naturally from path integrals
and that we will actually use is only that /fΣ is a vector space canonically associated with Σ, and
exchanged with its dual when the orientation of Σ is reversed. However, a Hubert space structure
is natural in the Hamiltonian viewpoint, and in the particular problem we are considering here, an
inner product on j4fΣ is important in more delicate aspects of conformal field theory; such an inner
product gives a "metric on the flat vector bundle" in the language of Friedan and Shenker [31].
According to Segal [16], Jfj in fact has a canonical projective Hubert space structure
Quantum Field Theory and the Jones Polynomial 
367
Actually, the general situation that must be studied is that in which possible
Wilson lines on M are "cut" by Σ, as in the figure. In this case Σ is presented with
finitely many marked points P^...Pk, with a G representation Rt assigned to each
Pi (since each Wilson line has an associated representation). To this data - an
oriented topological surface with marked points, and for each marked point a
representation of G - we wish to associate a vector space. This is also the general
situation that arises in conformal field theory - the marked points are points at
which operators with non-vacuum quantum numbers have been inserted. If one
reverses the orientation of Σ (and replaces the representations Rt associated with
the marked points with their complex conjugates) the vector space 3^Σ must be
replaced with its dual.
The Canonical Formalism. At first sight, (1.3) might look like a typically
intractable nonlinear quantum field theory, but this is far from being so. Working
on Σx R
l, it is very natural to choose the gauge AQ = 0 (with A0 being the
component of the connection in the R
l direction). In this gauge we immediately
see that the Lagrangian becomes quadratic. It reduces to
X-^dt^TrA^A,. 
(3.1)
For the time being we will ignore extra complications due to Wilson lines that may
be present on Σ x R
l. From (3.1) we may deduce the Poisson brackets,
8
4-π
{A«(x\ A](y)}=^ - £ijo
abS
2(x-y}. 
(3.2)
Before rushing ahead to quantize these commutation relations, we should
remember that the system is subject to a "Gauss law" constraint, which is
Ό = 0, or (ignoring the Wilson lines)
(3.3)
This constraint equation is nonlinear (since F contains a quadratic term), and - as
(3.1) is certainly a free theory - this nonlinearity is what remains of the underlying
nonlinearity of (1.3).
In quantum field theory, one very often quantizes first and then imposes the
constraints. The situation that we are considering here is a situation in which it is
far more illuminating to first impose the constraints and then quantize. For the
phase space Jί0 of connections Af(x) 
without the constraints is an infinite
dimensional phase space; imposing the constraints will reduce us to a rather subtle
but eminently finite dimensional phase space J/ί. The problem that faces us here,
of reducing from M§ to Jί by imposing the constraints (3.2), has been studied
before - and has proved to have extremely rich properties - in the work of Atiyah
and Bott on equivariant Morse theory, two dimensional Yang-Mills theory, and
8 This is a typical problem in which it is not appropriate to "introduce canonical momenta". The
purpose of introducing such variables is to reexpress a given Lagrangian in a form which is first
order in time derivatives, but (3.1) is already first order in time derivatives. The variables in (3.1)
are already canonic-ally conjugate, as indicated in the following equation
368 
E.Wilten
the moduli space of holomorphic vector bundles [33]. In our present investigation,
this familiar problem appears from a novel three dimensional vantage point.
It is necessary to recall the nature of constraint equations in classical physics.
The constraints (3.2) are functions that should vanish, but they also generate
gauge transformations via Poisson brackets. Imposing the constraints means two
things classically: First, we restrict ourselves to values of the canonical variables
for which the constraint functions vanish; and second, we identify two solutions of
the constraint equations if they differ by a gauge transformation. In the case at
hand, the first step means that we should consider only "flat connections", that is,
connections for which Ffj = 0. The second step means that we identify two flat
connections if they differ by a gauge transformation. Taking the two steps
together, we see that the physical phase space, obtained by imposing the
constraints (3.2), is none other than the moduli space of flat connections on Σ,
modulo gauge transformations. Such flat connections are completely character-
ized by the "Wilson lines", that is, the holonomies around non-contractible loops
on Σ. A simple count of parameters shows that on a Riemann surface of genus
g > 1, the moduli space Ji of flat connections modulo gauge transformations has
dimension (2g — 2) d, where d is the dimension of the group G.
The topology of Jt is rather intricate (and this was in fact the main subject of
interest in [33]). On general grounds J/l inherits a symplectic structure (that is, a
structure of Poisson brackets) from the symplectic structure present on J/l'0 before
imposing the constraints. Ji is a compact space (with some singularities), and in
particular its volume with the natural symplectic volume element is finite. Since in
quantum mechanics there is one quantum state per unit volume in classical phase
space, the finiteness of the volume of M means that the quantum Hubert spaces
will be finite dimensional. We would like to determine them.
3.1. The Holomorphic 
Viewpoint
Quantization of classical mechanics is usually carried out by separating the
canonical variables into "coordinates", q\ which are a maximal set of real
commuting variables, and "momenta", ;;
;, which are conjugate to the q
l. The
quantum Hubert space is then the space ffl of square integrable functions of the q
l.
Such a scheme definitely requires a noncompact phase space of infinite
volume, since - though the q
l may take values in a compact space - the p
j are
definitely unbounded. Accordingly, the space ffl is infinite dimensional.
Quantizing a compact, finite volume phase space, such as the moduli space .Jί
of flat connections modulo gauge transformations, is quite a different kind of
problem. It has no known general solution, but there is one important class of
cases in which there is a natural notion of quantization. This arises in the case in
which M is a Kahler manifold, and the symplectic structure on Jt is the curvature
form that represents the first Chern class of a holomorphic line bundle L endowed
with some metric. In this case, one carries out quantization not by separating the
variables in phase space into "coordinates" and "momenta", #'s and^'s, but by
separating them into holomorphic and anti-holomorphic degrees of freedom,
essentially z ~ q -f- ip and z ^ q — ίp. The quantum Hubert space 2tf is then a
suitable space of holomorphic "functions". More exactly, J^
7 is the space of
Quantum Field Theory and the Jones Polynomial 
369
holomorphic sections of the line bundle L. If ,M is compact, this latter space will be
finite dimensional. In our problem, with J/l being the moduli space of flat
connections modulo gauge transformations on an oriented smooth surface Σ, is
there a natural Kahler structure on JίΊ The answer is crucial for all that follows.
There is not quite a natural Kahler structure on Jt, but there is a natural way to
obtain such structures. Once one picks a complex structure J on Σ, the moduli
space J/l of flat connections can be given a new interpretation - it is the moduli
space of stable holomorphic Gc bundles on Σ which are topologically trivial (Gc is
the complexification of the gauge group G). Let us refer to the latter space as Jίj.
M j is naturally a complex Kahler (and in fact projective algebraic) variety. Upon
picking a linear representation of G (for our purposes it is convenient to pick a
representation with the smallest value of the quadratic Casimir operator, e.g. the
TV dimensional representation of SU(N) or the adjoint representation of E8), and
passing from a principal Gc bundle to the associated vector bundle, we can think
of Jίj as the moduli space of a certain family of holomorphic vector bundles. For
G = SU(N), Jίj is simply the moduli space of all stable rank TV holomorphic
vector bundles of vanishing first Chern class.
The symplectic form on Ji that appears in (3.1) or (3.2) without picking a
complex structure on Σ has a very special interpretation in holomorphic terms
once we do pick such a complex structure. Let us recall the notion [34] of the
determinant line bundle of the c operator. The d operator on Σ can be "twisted"
by any holomorphic vector bundle. Jίj parametrizes a family of holomorphic
vector bundles on Σ, and thus it can be regarded as parametrizing a family of d
operators. Taking the determinant line gives a line bundle L over the base space
J/j of this family. Furthermore [34], the Dirac determinant gives a natural metric
on L, and the first Chern class of L, computed with this metric, is precisely the
symplectic form that appears in (3.1) or (3.2), provided k — \. For general k, the
symplectic form that appears in (3.1) or (3.2) represents the first Chern class of the
/c
th power of the determinant line bundle.
 9
Thus, all of the conditions are met for a straightforward quantization of (3.1),
taking into account the constraints (3.3). The constraints mean that the classical
space to be quantized is the moduli space Jf of flat connections. Picking an
arbitrary complex structure J on Σ, J/l becomes a complex manifold, and the
symplectic form of interest represents the first Chern class of L
Θ/C, the k
ih tensor
power of the determinant line bundle. The quantum Hubert space J^Σ is thus the
space of global holomorphic sections of L®
k.
3.2. A Flat Vector Bundle on Moduli Space
This gives an answer to the problem of canonically quantizing the Chern-Simons
theory on Σ x 7?
1, but a crucial point now requires discussion.
9 This description is valid for the gauge group G = SU(N). but in general the following
modification is needed. For groups other than SU(N) the determinant line bundle L is not the
fundamental line bundle on =.// but a tensor power thereof. For instance, for G — E8, there is a line
bundle L' with (A')® 10 ~ L. It is then L' whose first Chern class corresponds to (3.1) or (3.2) with
370 
E. Witten
Quantizing (3.1), with the constraints (3.3), is a problem that can be naturally
asked whenever one is given an oriented smooth surface Σ. Beginning with a
generally covariant Lagrangian in three dimensions, we were led to this problem in
a context in which it was not natural to assume any metric or complex structure on
Σ. However, to solve the problem and construct fflΣ, it was very natural to pick a
complex structure /on Σ. Thus, our description of fflΣ depends on the choice of/,
and what we have called #?Σ might perhaps be better called ^
 (
Σ
J}, As / varies, the
2fΣ
J) vary holomorphically with /, and thus we could interpret this object as a
holomorphic vector bundle on the moduli space of complex Riemann surfaces.
But since Jfj
j) is the answer to a question that depends on Σ and not on /, we
would like to believe that likewise the JfΣ
(J) canonically depend only on Σ and not
on /. The assertion that the JfI
(J) are canonically independent of /, and depend
only on Σ, is the assertion that the vector bundle on moduli space given by the
J^Σ
J) has a canonical flat connection that permits one to identify the fibers. Such
"flat vector bundles on moduli space" first entered in conformal field theory
somewhat implicitly in the differential equations of Belavin, Polyakov, and
Zamolodchikov [32]. They were discussed much more explicitly by Friedan and
Shenker [31], who proposed that they would play a pivotal role in conformal field
theory, and they have been prominent in subsequent work such as [12,13]. At least
in one important class of examples, we have just met a natural origin of "flat
vector bundles on moduli space". The problem "quantize the Chern-Simons
action" can be posed without picking a complex structure, so the answer is
naturally independent of complex structure and thus gives a "flat bundle on
moduli space". The particular flat bundles on moduli space that we get this way
are those that Segal has described [16] in connection with conformal field theory;
Segal also rigorously proved the flatness, which is explained somewhat heuristi-
cally by the physical argument sketched above. (Because of the conformal
anomaly, this bundle has only a projectively flat connection, with the projective
factor being canonically odd under reversal of orientation.)
The role of these flat bundles in conformal field theory is as follows. If one
considers current algebra on a Riemann surface, with a symmetry group G, at
"level" k, then one finds that in genus zero the Ward identities uniquely determine
the correlation functions for descendants of the identity operator, but this is not so
in genus ^ 1. On a complex Riemann surface Σ of genus ^ 1, the space of solutions
of the Ward identities for descendants of the identity is a vector space $Σ, which
might be called the "space of conformal blocks". Segal calls the association
Σ -> $Σ a "modular functor", and has given an algebra-geometric description of
the modular functors that arise in current algebra. In quantizing the Chern-
Simons theory we have exactly reproduced this description! This is then the secret
of the relation between current algebra in 1 + 1 dimensions and Yang-Mills theory
in 2 -f 1 dimensions: the space of conformal blocks in 1 + 1 dimensions are the
quantum Hubert spaces obtained by quantizing a 2 -f 1 dimensional theory. It
would take us to far afield to explain here the algebra-geometric description of the
space of conformal blocks. Suffice it to say that when one tries to use the Ward
identities of current algebra to uniquely determine the correlation functions of
descendants of the identity on a curve Σ of genus ^ 1, one meets an obstruction
which involves the existence of non-trivial holomorphic vector bundles on Σ\ the
Quantum Field Theory and the Jones Polynomial 
371
Ward identities reduce the determination of the correlation functions to the choice
of a holomorphic section of L®
k over the moduli space of bundles.
It seems appropriate to conclude this discussion with some remarks on the
formal properties of the association Σ -» jjfΣ. It is good to first think of the functor
Σ-+H
l(Σ,R) which to a Riemann surface Σ associates its first de Rham
cohomology group. This functor is defined for every smooth surface Σ,
independent of complex structure. A diffeomorphism of Σ induces a linear
transformation on H
l(Σ,R), 
so H
l(Σ,R) 
furnishes in a natural way a
representation of the mapping class group. The formal properties of the functors
Σ -» #Cτ that come by quantizing the Chern-Simons theory are quite analogous.
Though a complex structure /on Σ is introduced to construct fflΣ, the existence of
a natural projectively flat connection on the moduli space of complex structures
permits one locally to (projectively) identify the various 2?^ and forget about the
complex structure. One might think that the global monodromies of the flat
connection on moduli space would mean that globally one could not forget the
complex structure, but this is not so; these monodromies just correspond to an
action of the purely topological mapping class group, so that the formal properties
of ^ are just like those of H
l (Σ, K).
3.3. Inclusion of Wilson Lines
So far, we have discussed the quantization of the Chern-Simons theory on a
Riemann surface Σ without Wilson lines. Now we wish to include the Wilson lines,
which, as in Fig. 4b? pierce Σ in some points Pf; associated with each such point is a
representation R . Quantizing the Chern-Simons theory in the presence of the
Wilson lines should give a Hubert space J^Σ.PijRι that is canonically associated
with the oriented surface Σ together with the choice of Pi and R{.
It is pretty clear what problem in conformal field theory this should
correspond to. Instead of simply considering correlation functions of the
descendants of the identity, we should consider in the conformal field theory
primary fields transforming in the Rt representations of G. With these fields (or
their descendants) inserted at points Pt on Σ, one gets in conformal field theory a
more elaborate space ^
?Σ ,PI,RI of conformal blocks. Again, there is an algebra-
geometric description of this space [16], and this is what we should expect to
recover by quantizing the Chern-Simons theory in the presence of the Wilson lines.
I will now briefly sketch how this works out, deferring a fuller treatment for
another occasion. First of all, the Wilson lines correspond to static non-abelian
charges which show up as extra terms in the constraint equations. So (3.3) is
replaced by
^-^F?j(X)=^δ
2(x-P,)^, 
(3.4)
0 π 
& = i
where Ps, 5=1 ...r are the points at which static external charges have been
placed, and 7^, 0=1 ...dimG are the group generators associated with the
external charges. Now, a naive attempt to quantize (3.1) with the generalized
constraints (3.4) would run into extremely unpleasant difficulties. One could try to
quantize first and then impose the constraints, but this is difficult to see through
372 
E. Witten
even in the absence of the external charges. Alternatively, one can try to impose
the constraints at the classical level and then quantize, as we did above. But it is
hard to make sense of (3.4) as constraints in the classical theory; the solution A? of
(3.4) cannot be an ordinary r-number connection, since 
non-commuting
operators appear on the right-hand side. It is clear that to solve (3.4), Af would
have to be some sort of "^-number connection", whose holonomy would
presumably be an element of a "quantum group", not an ordinary classical group.
Indeed, it seems likely that the theory of quantum groups [35] can be considered to
arise in this way.
However, there is a much better way to quantize the Chern-Simons theory with
static charges. We certainly wish to impose (3.4) at the classical level. This cannot
be done directly, since on the right-hand side there appear quantum operators. A
useful point of view is the following. A representation Rt of a group G should be
seen as a quantum object. This representation should be obtained by quantizing a
classical theory. The Borel-Weil-Bott theorem gives a canonical way to exhibit for
every irreducible representation R of a compact group G a problem in classical
physics, with G symmetry, such that the quantization of this classical problem
gives back R as the quantum Hubert space. One introduces the "flag manifold"
G/7
1, with T being a maximal torus in G, and for each representation R one
introduces a symplectic structure ωR on G/Γ, such that the quantization of the
classical phase space G/Γ, with the symplectic structure ω#, gives back the
representation R. Many aspects of representation theory find natural explan-
ations by thus regarding representations of groups as quantum objects that are
obtained by quantization of classical phase spaces.
In the problem at hand, this point of view can be used to good effect. We
extend the phase space J/ί§ of G connections on Σ by including at each marked
point P{ a copy of G/Γ, with the symplectic structure appropriate to the R{
representation. The quantum operators T(
c
 } that appear on the right of (3.4) can
then be replaced by the classical functions on G/Γ whose quantization would give
back the Tfa. The constraints (3.4) then make sense as classical equations, and the
analysis can be carried out just as we did without marked points, though the
details are a bit longer. Suffice it to say that after imposing the classical
constraints, one gets a finite dimensional phase space JfPιtRι that incorporates the
static charges; a point on this space is a flat G connection on Σ with a reduction of
structure group to Γ at the points Pt. Upon picking an arbitrary conformal
structure on Σ, this phase space can be quantized. In this way one gets exactly
Segal's description of the space of conformal blocks in current algebra in a general
situation with primary fields in the Rt representation inserted at the points Pt. (In
current algebra at level /c, one only permits certain representations, the "integrable
ones". If one formally tries to include other representations, the Ward identities
show that they decouple [36]. According to Segal, the analogous statement in
algebraic geometry is that the appropriate line bundle over ^Pι> Rι has no non-zero
holomorphic sections unless the Rt all correspond to integrable representations.
For the Chern-Simons theory, this means that unless the representations Rt are all
integrable, the zero vector is the only vector in the physical Hubert space.)
Finally, let us note that the Borel-Weil-Bott theorem should not be used simply
as a tool in quantization. It should be built into the three dimensional description.
Quantum Field Theory and the Jones Polynomial 
373
One should use the theorem to replace the Wilson lines (1.5) that appear in (1.6)
with a functional integral over maps of the circle 5 into G/T(or actually an integral
over sections of a G/T bundle, twisted by the restriction to S of the G-bundle E).
This gives a much more unified formalism.
3.4. The Rίemann Sphere with Marked Points
The above description may seem a little bit dense, and we will supplement it by
giving a simple intuitive description of the physical Hubert space ^Σ ,RI,PI ^
n the
important case of genus zero. Let Σ be an oriented surface of genus zero, with
static charges in the Rt representation at points Pt. Let us consider the case of very
large k. Now, the gauge coupling in (1.3) is of order l//c, so for large k we are
dealing with very weak coupling. Rather naively, one might believe that for
extremely weak coupling the physical Hubert space is the same as it would be if the
charges were not coupled to gauge fields, ΐf so, the physical Hubert space would be
simply the tensor product Jf0 = (x) t Rt of the Hubert spaces Rt of the individual
charges. However, there is a key error here. No matter how weak the gauge
coupling may be, we must remember that in a closed universe the total charge must
be zero (since the electric flux has nowhere to go). The total charge being zero
means in a nonabelian theory that all of the charges together must be coupled to
the trivial representation of G. So the physical Hubert space, for large k, is
precisely the (/-invariant subspace of ^0, or
Jf = Inv(®^.). 
(3.5)
This is a familiar answer in conformal field theory for the space of conformal
blocks obtained, in the large k limit, in coupling representations Rt. Consider-
ations of conformal field theory also show that for finite k the correct answer is
always a subspace of (3.5). The most important modification of (3.5) that arises
for finite k (and is explained algebra-geometrically in [16]) is that Jtf is zero unless
the Rt correspond to integrable representations of the loop group; in what follows
a restriction to such representations is always understood.
Now we consider some important special cases.
(i) For the Riemann sphere with no marked points, the Hubert space is one
dimensional. This is well known in conformal field theory - for descendants of the
identity on the Riemann sphere, there is only one conformal block.
(ii) For the Riemann sphere with one marked point in a representation Rt, the
Hubert space is one dimensional if RI is trivial, and zero dimensional otherwise.
(iii) For the Riemann sphere with two marked points with representations Rt
and Rj, the Hubert space is one dimensional if Rj is the dual of Rt (so that there is
an invariant in Rt ® Rj) and zero dimensional otherwise. Again, this is well known
in conformal field theory.
(iv) For the Riemann sphere with three marked points in representations Rt,
Rj, and Rk, the dimension of Jjf is the number Nijk for which Verlinde has
proposed [12] and Moore and Seiberg have proved [13] rather striking properties.
Here, Niίk may in general be less than its large k limit which is the dimension of
(3.5).
374 
E. Witten
(v) From the results of Verlinde, the dimensions of the physical Hubert spaces
for an arbitrary collection of marked points on S
2 can be determined from a
knowledge of the Nijk. But let us consider a particularly important special case.
Suppose that there are four external charges, and that the representations are
R, R, R, and R. If the decomposition of R® R is
s
i= 1
with the EI being distinct irreducible representations of G, then the physical
Hubert space Jjf at large k will be s dimensional, since the possible invariants in
R ® R ® R ® R are uniquely fixed by giving the representation to which R (x) R is
coupled. (For small k the dimension of ffl might be less than s.) In understanding
the knot polynomials, an important special case is that in which G is SU(N) and R
is the defining TV dimensional representation. In that case, s = 2 and the physical
Hubert space is two dimensional (except for k = 1 where it is one dimensional).
