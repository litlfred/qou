---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-017-4-2-knots-and-morse-theory
section_title: "Knots And Morse Theory"
section_number: "4.2"
pages: 71-85
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
4.2 Knots And Morse Theory
Beginning in section 2.5.3, we described the analytic continuation of Chern-Simons knot
invariants in a rather informal way. To make this more precise, we need to incorporate in
the language of oscillatory integrals the holonomy functions that are included in the path
integral to define knot invariants. How to do this has been briefly explained in [51], section
3.3, and in [54], pp. 1218-9, and in much more detail in [34]. We consider first the case of a
compact gauge group H with connection A.
For a knot K labeled by a representation R, the basic factor is
TrR P exp −
I
K
A

. (4.15)
According to the Borel-Weil-Bott theorem, letting T denote a maximal torus in H, the representation R can be constructed as the space of holomorphic sections of a certain holomorphic
line bundle LR over the flag manifold H/T. This means that there is a quantum mechanical
problem with H symmetry for which the space of physical states is the representation R.
Writing a path integral representation of this system and coupling it to the gauge field A
will give the representation that we need of the holonomy function.
The line bundle LR → H/T admits an essentially unique H-invariant connection that
we will call aR. We can describe as follows a classical problem with R symmetry whose
quantization leads, in view of the Borel-Weil-Bott theorem, to the representation R. Let S
be a one-manifold and let ρ : S → H/T be a map. On the space of such maps, we define an
action IR(ρ) = R
S
ρ
∗
(aR). For S a circle, this is defined mod 2π, so that exp(iIR(ρ)) is welldefined. (If instead S has boundaries, exp(iIR(ρ)) is not a complex number but a transition
amplitude between quantum wavefunctions; we will not need the details here.) Since IR(ρ)
is invariant under reparametrizations of S, this system is a topological field theory in the
one-dimensional sense; the Hamiltonian vanishes.
71

The basic path integral for this system is the integral over maps ρ : S → H/T:
Z
Dρ exp(iIR(ρ)). (4.16)
For S a circle, the value of the path integral can be determined by observing that the path
integral determines a trace in the physical Hilbert space. The physical Hilbert space is simply
the representation R, and as the Hamiltonian vanishes, the trace is simply the trace of the
identity operator. So the value of the path integral is dR, the dimension of the representation
R.
We want to generalize this to couple to a gauge field A and to compute the trace not of
the identity operator but of the holonomy operator TrRP exp −
H
S A

. To do this, we simply
couple the gauge field A to the ρ field in a gauge-invariant fashion. Quantum mechanically,
we would couple A to the matrices that generate the action of H in the representation R.
The classical limit of these matrices is the moment function µR associated to the action of
H on H/T. µR is a map from H/T to the dual of the Lie algebra h. So for h ∈ h, we have a
real valued function µR(h) on H/T. It obeys dµR(h) = ιhdaR (where ιh is contraction with
the vector field on H/T that corresponds to h). As A is h-valued, there is a natural pairing
(A, µR). The gauge-invariant extension of the action IR(ρ) is IR(ρ, A) = IR(ρ) −
R
S
(A, µR).
(A more intrinsic description of the geometry involved in defining this action can be found
in [54]; for more detail see also [34].) Thus we arrive at a path integral representation of the
holonomy:
TrRP exp −
I
S
A

=
Z
Dρ exp (iIR(ρ, A)). (4.17)
Now we can rewrite the basic formula (2.19) for the Chern-Simons invariant of a knot in
a convenient form:
ZH(K; k) = Z
U
DA Z
Dρ exp(ikW(A) + iIR(ρ, A)). (4.18)
What we have gained is that now, although we are integrating over a larger number of
variables, the integrand is simpler: it is just the exponential of a local functional of the
fields. In other words, we have reduced the problem to an oscillatory integral (with more
variables), and we can apply the Morse theory machinery rather as if no knot were present.
As usual, the main step in analytic continuation is to extend the action to a holomorphic
function of complex variables. We analytically continue the connection A to a complexvalued connection A and we replace the flag manifold H/T with HC/TC, where TC is a
complex maximal torus in HC. The analytically continued integral thus takes the form
ZH(K; k) = Z
C
DA
Z
Dρ exp(ikW(A) + iIR(ρ, A)), (4.19)
72

where C is an integration cycle in the space of fields A, ρ.
Any integration cycle C, including the original real integration cycle of Chern-Simons
theory in the presence of a knot, can be expressed in terms of Lefschetz thimbles in the usual
way. Such cycles are convenient for several reasons. One reason, discussed in section 3.1.3, is
that it is straightforward to determine the asymptotic value of the integral over such a cycle,
in the semiclassical region in which the action is large. What is this region? In the absence
of a knot, the action is proportional to k, so the semiclassical region is the region of large k.
In the presence of a knot labeled by a representation R with highest weight λR, the action
IR(ρ, A) is proportional to λR, since it is linear in aR and µR which are both proportional to
λR. So in the presence of a knot, the natural semiclassical limit is obtained by taking k and
λR to infinity with a fixed ratio. The Morse theory machinery will enable us to understand
the asymptotic behavior of the analytically continued Chern-Simons path integral in this
limit.
4.2.1 Classical Equations In The Presence Of A Knot
In the presence of a knot K, the classical equation for A receives an extra contribution and
no longer asserts simply that F is flat. Rather, the equation receives an extra contribution
that is supported on K:
kF
2π
= δKµR. (4.20)
(Here δK is a delta function that is Poincar´e dual to K, and we use the linear form Tr to
identify the Lie algebra h with its dual; this is also done in eqn. (4.22) below.) The fact that
the curvature is a delta function supported on K means that the connection is flat away from
K and has a monodromy around K. Exponentiating the delta function in the curvature,
this monodromy is
U = exp(2πµR/k). (4.21)
To understand this result, recall that H/T is a homogeneous space, and that the conjugacy
class of µR (as an element of h
∗
) is constant and depends only on R. So eqn. (4.21) really
defines a conjugacy class in H; the monodromy around the knot must lie in this conjugacy
class. We note that the conjugacy class in question depends only on the ratio µR/k.
Let us make this more explicit for H = SU(2). Take R to be the n-dimensional irreducible
representation of SU(2). Its highest weight is
n − 1
2

i 0
0 −i

. (4.22)
(To keep the structure constants real, we represent a real Lie algebra such as su(2) by antihermitian matrices.) Up to conjugacy, this is µR for the representation R. So the monodromy
73

around a knot labeled by this representation is
exp 
iπ(n − 1)
k

1 0
0 −1
 . (4.23)
We will now make a remark on quantum corrections to this classical formula. In physics
in general, quantum corrections cannot be entirely understood by shifting the values of
classical parameters, but many quantum results in Chern-Simons theory can be understood
more readily from a semiclassical point of view if one shifts n−1 to n and k to k+2 in (4.23).
(The shift in k was discussed in section 2.7.1, and the shift in n has a similar interpretation.
For the analogous shifts for noncompact Lie groups, see [48].) For our purposes, it is not
necessary to take these shifts into account explicitly. Our goal is to determine the correct
integration cycle for the path integral in the limit of large k and n with fixed ratio n/k. The
answer to this question is not affected by shifts n → n + 1 or k → k + 2. Those shifts enter
when, after having found the right integration cycle for the path integral, one carries out the
integral including one-loop effects. This will generate the shifts in n and k in the usual way.
4.2.2 More On The Classical Equations
There are some important subtleties concerning the gauge fields obeying (4.20), especially
after we analytically continue to a complex gauge field A. In that case, the equation becomes
kF
2π
= δKµR, (4.24)
where F = dA+A∧A. We want to supplement this equation with a condition for vanishing
of the moment map,
dA ⋆M φ = 0, (4.25)
where A = A + iφ. To describe what sort of gauge fields obey this equation, it suffices to
work in a two-plane normal to K. We take polar coordinates r, θ on this two-plane, with K
understood to lie at r = 0. To obey (4.24) and (4.25), we can take
A = α dθ + . . .
φ = − γ dθ + . . . , (4.26)
where α and γ are commuting elements of the real Lie algebra h with α − iγ = µR/2k, and
the ellipses refer to terms less singular than 1/r. (The angular form dθ has a 1/r singularity
at r = 0.) This type of singularity in gauge theory was studied in detail19 in [55], starting
19In that context, there was another term in φ of the form β dr/r; β can be removed by a gauge transformation (which is singular at r = 0), and tentatively it seems that in the present problem we can just as well
take β = 0.
74

in section 2.1. The most natural way to proceed is to fix a gauge in which µR lies in the
Lie algebra of a specified complex maximal torus TC. This can always be done globally
along K. Then we require A to have a singularity of the sort described in (4.26), and we
only allow gauge transformations that preserve the gauge condition – in other words, gauge
transformations that are TC-valued when restricted to K.
One important point, discussed in [55], is that by a gauge transformation that is singular
at r = 0, one can shift α by a coroot of H. This means that the formalism is invariant under
shifting µR by k times a coroot. For H = SU(2), this corresponds to the symmetry
n → n + 2k, (4.27)
which actually undergoes a quantum correction to n → n + 2(k + 2).
There is an important subtlety, which we will describe first for H = SU(2). Suppose
that we vary µR and k so that µR/k goes to zero, or more generally so that it approaches a
cocharacter (which we then remove by a singular gauge transformation, as mentioned in the
last paragraph). This means that α and γ go to zero, and a naive look at (4.26) might make
one believe that in the limit, A and φ become nonsingular. The correct conclusion, however,
because of the ellipses in (4.26), which represent terms less singular than 1/r, is only that
in such a case, A and φ are less singular than 1/r. The equations F = dAφ = 0 have a
solution with a singularity at r = 0 that is (slightly) milder than 1/r, and this less singular
solution may be the result if one varies a family of solutions with the 1/r singularity (4.26)
so that the coefficient of 1/r approaches zero. The singular solution in question, which was
essentially first studied by Nahm [56], takes the form
A =
t1 dθ
ln r
φ =
t2 dr
r ln r
−
t3 dθ
ln r
, (4.28)
where [t1, t2] = t3, and cyclic permutations thereof. This condition means that the ti define
a homomorphism from su(2) to h. For H = SU(2), there is up to conjugation only one nontrivial homomorphism and we pick this one. (For other groups, all possible homomorphisms
can arise, in general.) For this solution, the monodromy of A around the singularity at r = 0
is not trivial but is in the conjugacy class that contains the non-diagonalizable, unipotent
element
V =

1 1
0 1
. (4.29)
This is demonstrated by directly showing that, with A, φ given in (4.28), the holonomy of
A = A + iφ along any path that loops around r = 0 is in the stated conjugacy class. For
example, if the path is the circle r = r0 for some r0, the monodromy is exp(2π(t1−it3)/ ln r0),
which is in the stated conjugacy class. (For more detail, see section 3.8 of [55].)
75

What is happening here is that in the complex Lie group G = HC, as µR/k → 0, the
conjugacy class that contains the element U = exp(2πµR/k) does not approach the conjugacy
class of the identity; rather it approaches the conjugacy class of the element V . This may
become clear if one considers the family of SL(2, C) elements

λ 1
0 λ
−1

, (4.30)
which are conjugate to the diagonal matrix diag(λ, λ−1) for generic λ, but to V if λ = 1.
So if we consider a family of connections A representing Chern-Simons critical points,
parametrized by µR/k, with monodromy U = exp(2πµR/k), then as µR/k → 0, the monodromy of A around the knot might approach 1, but it also might approach a unipotent
element conjugate to V . The latter behavior is generic, since the conjugacy class of V has
dimension two, while that of the identity consists of a single point.
Modulo a singular gauge transformation that shifts α to zero,20 the behavior is exactly
the same if µR/k approaches a value for which U → −1. Given a family of flat connections
A of monodromy U, consider a limit in which U → −1. The monodromy of A may approach
−1, but instead it may approach
−V = −

1 1
0 1
. (4.31)
We will encounter both cases in section 5.
We have described this exceptional behavior for SL(2, C), but it has a close analog for
any complex Lie group G. As long as U = exp(2πµR/k) is regular (that is, at long as
the subgroup of G that it commutes with is a copy of TC), Chern-Simons critical points in
the presence of a knot correspond to flat connections whose monodromy around the knot
is conjugate to U. But in general, the monodromy may be in any conjugacy class whose
closure contains U. For more on this, see section 3.8 of [55].
The Flow Equations In The Presence Of A Knot
Now let us briefly describe the flow equations in the presence of a knot. As usual, to
formulate the flow equations, we introduce an extra “time” coordinate. So to study ChernSimons theory on a three-manifold M in the presence of a knot K, we consider flow equations
on the four-manifold X = R × M, with the knot now filling out the two-manifold R × K.
The flow equations are the same as before, but now we must consider solutions with a
20Such a gauge transformation is single-valued in SO(3), but not in SU(2). It is not quite a symmetry
of SU(2) Chern-Simons theory, but it is useful for analyzing the classical equations and describing critical
points. For more on this, see section 4.2.7.
76

singularity along R × K. The singularity is given by (4.28) modulo terms less singular than
1/r. In particular, for special values of µR/k, we must allow a singularity that (perhaps
after a singular gauge transformation to set α to zero) takes the form (4.28). This seemingly
exceptional case is important in applications, because the flat SL(2, C) connection associated
to a hyperbolic metric on the knot complement has this sort of monodromy.
In effect, the flow equations have a codimension two singularity in four dimensions that
can be modeled by the same surface operators studied in [55].
4.2.3 Analog For Noncompact Lie Groups
For the case of a compact Lie group H, we have described how to incorporate a knot labeled
by a representation R in the framework of oscillatory integrals and Morse theory.
What happens if the gauge group is not compact, for example if it is G = HC? If the
representation R is unitary and arises by quantization of a coadjoint orbit O of G, then there
is a close analog of (4.17), with H/T replaced by O. The resulting knot invariants, however,
have not been seriously studied.
Let us consider instead the case that R is a finite-dimensional holomorphic representation
of G, obtained by analytic continuation of an irreducible representation of H, as described
in section 2.6.1. It is straightforward to bring such a representation into the Morse theory
framework. We represent the holonomy around the knot in such a representation by the
same factor as in (4.19), namely RDρ exp(iIR(ρ, A)). So the path integral definition (2.29)
of knot invariants associated to such a representation can be rewritten
ZG(K;t, et) = Z
C
DA DAeDρ exp itW(A)/2 + iet W(Ae)/2

exp(iIR(ρ, A)). (4.32)
Morse theory can now be used in the usual way to describe possible integration cycles for
this integral. After analytic continuation, A and Ae are independent. Since IR(ρ, A) is
independent of Ae, the presence of the knot does not affect the Euler-Lagrange equation
for Ae. The equation for a critical point thus tells us simply that Ae is flat, while A is a
flat connection on the complement of K whose monodromy around K is in the conjugacy
class of the element U = exp(2πµR/k) described in eqn. (4.21). (When U is not regular,
this statement must be refined in a way described in section 4.2.2.) Of course, now we are
supposed to take the conjugacy class of U in G rather than in H.
One point deserves note. As IR(ρ, A) is not real, the exponential exp(iIR(ρ, A)) grows
exponentially in some regions. As a result, even if t and et are complex conjugates, the path
integral (4.32) does not converge if evaluated on the usual real cycle Ae = A. Perhaps it
77

is possible to slightly displace the real cycle to make the integral converge, or perhaps the
integral can only be defined using Lefschetz thimbles. As explained in section 2.6.1, in the
case of knots in S
3
, a suitable integration cycle can essentially be borrowed from the case of
a compact gauge group.
A similar analysis applies if the gauge group is a noncompact real form H′ of G = HC. If
R is a unitary representation, one can imitate (4.17) using the appropriate coadjoint orbit.
If R is a finite-dimensional representation of H′(obtained by analytic continuation from H
to G = HC and then restriction to H′), one can represent the knot by the now familiar factor
R
Dρ exp(iIR(ρ, A′)), where now A′is h
′
-valued. Prior to analytic continuation, ρ is a map
to H/T, which admits an action of G and hence of H′. After analytic continuation, the fields
and the integrand of the path integral are the same as they are in the H-valued theory, but
the integration cycle is different. This last statement holds exactly as it does in the absence
of the knot.
4.2.4 Classification Of Critical Points
To study the Chern-Simons path integral via the Morse theory machinery, a first step is to
classify the critical points and evaluate the classical action at a critical point. As long as one
considers only physical values of the coupling parameters, critical points correspond to flat
connections modulo gauge transformation (perhaps with monodromy around a knot), and
the Chern-Simons invariant W(A) of such a flat connection is understood as an element of
R/2πZ (or C/2πZ in the case of a complex Lie group).
Upon analytic continuation away from physical values of the coupling, one must be
more careful. Let us consider first the case that the gauge group is a compact Lie group
H and one wishes to continue away from integer values of k. In this case, the integrand
exp(ikW(A)) is invariant only under the subgroup of gauge transformations that leave W(A)
fixed, rather than shifting it by a multiple of 2π. If H is connected and simply-connected,
this subgroup is the connected component of the group of gauge transformations. At any
rate, exp(ikW(A)) should be understood as a function not on the space U of gauge fields
modulo gauge transformations, but on a cover Ub on which the Chern-Simons invariant is
well-defined. For connected and simply-connected H, Ub is the universal cover of U.
So we need to consider critical points of the Chern-Simons function on Ub. Such a critical
point is simply a flat connection together with a lift of its Chern-Simons invariant to R (or
C, if we consider complex critical points).
As an example, let us consider Chern-Simons theory on S
3
in the presence of a knot K.
Typically there are only finitely many critical orbits in the usual sense. In other words, up
78

to gauge transformation, there are typically only finitely many flat connections on the knot
complement S
3\K with prescribed monodromy about K. However, when we analytically
continue away from integer values of k, we need a real-valued Chern-Simons function, meaning that a critical point must be understood as a pair consisting of a flat connection and a
lift of its Chern-Simons function to R. This combined data determines a critical point of
the function W(A) on Ub. There always are infinitely many of these critical points, as the
Chern-Simons invariant of any given flat connection can be lifted to R in infinitely many
ways. In section 5, we will study in detail the analytic continuation of the Chern-Simons
path integral for some specific knots (the trefoil and the figure-eight knot) and we will see
the important role played by distinct critical points that differ only in the value of their
Chern-Simons invariant. This should come as no surprise, since in eqn. (3.73) we have
already seen similar behavior in the analytic continuation of the Bessel function away from
integer values of κ.
The same ideas hold if the gauge group is a non-compact real form H′ of G = HC.
However, the case that the gauge group is the complex Lie group G involves a new wrinkle.
The Chern-Simons theory depends naturally on an integer-valued parameter ℓ and a real
parameter s, as shown in eqn. (2.2). As explained in section 2, to analytically continue to
complex s, we view Ae, which begins life as the complex conjugate of the gauge field A, as
an independent g-valued connection in its own right. The action is a linear combination of
the two Chern-Simons actions W(A) and W(Ae),
I =
t W(A)
2
+
et W(Ae)
2
, t = ℓ + is, et = ℓ − is. (4.33)
If we impose invariance under all gauge transformations, a critical point is a pair of flat
connections A, Ae, up to gauge equivalence. In that case, W(A) and W(Ae) are each naturally
defined as elements of C/2πZ. But then (for complex s) the indeterminacy of I is not just
an integer multiple of 2π and the integrand exp(iI) of the path integral is not defined.
One might think that to make sense of the path integral, we would have to lift both W(A)
and W(Ae) from C/2πZ to C. We indeed have to do this if the aim is to analytically continue
to generic values of both ℓ and s. However, there is a fairly natural problem, described in
section 2, in which ℓ remains an integer and only s is continued to complex values. In this
case, (t+et)/2 remains an integer, so adding 2π to both W(A) and W(Ae) causes no change in
exp(iI). The most natural way to proceed is to regard exp(iI) as a function on the smallest
cover of UC×UC where it can be defined. In practice, this means that a critical point is a pair
of flat connections A, Ae together with a lift of the pair W(A), W(Ae) to (C×C)/2πZ, where
Z is diagonally embedded. In other words, we can shift both Chern-Simons invariants by a
common multiple of 2π, but we cannot shift them independently. We can use this freedom
to arbitrarily specify how we want to lift the Chern-Simons invariant of either A or Ae, but
then we must consider all lifts of the other.
79

It is instructive to consider the usual example of a knot K in S
3
. In this case, as explained
in section 4.2.3, a critical point in the usual sense corresponds to an ordinary flat connection
Ae on S
3 plus a flat connection A on S3\K whose monodromy around K is in a prescribed
conjugacy class. As S
3
is simply connected, Ae is gauge-equivalent to a trivial flat connection,
and W(Ae) vanishes modulo 2π. It is natural to fix the complex lift of W(Ae) to be zero.
Once we do this, we have exhausted our freedom to shift the Chern-Simons invariants, and
we must consider all possible complex lifts of W(A).
The possible critical points, then, are classified by a flat connection A on S
3\K with
appropriate monodromy and with all possible choices for its Chern-Simons invariant. But
this is the same set of critical points that we encounter in analytically continuing the theory
on S
3 with compact gauge group H in the presence of the same knot K labeled by the same
representation R. What we have just described is a nonperturbative aspect of the relation
between theories with gauge groups H or G = HC for the special case of knots in S
3
. This
relation was already discussed in section 2.6.
4.2.5 Variation Of The Action
To use the Morse theory formalism, we need some information about the value of the ChernSimons function W(A) for a classical solution. We take the gauge group to be a complex
Lie group G = HC.
The following ideas prove to be useful. First of all, as sketched in fig. 10, the boundary
of a small neighborhood of a knot K is a two-torus Y . On Y , we draw two circles – the
meridian mb, which goes the short way around Y and has linking number 1 with K, and the
longitude bl, which goes the long way around Y and which we choose to have linking number
0 with K.
Since the fundamental group of Y is abelian, if A is a flat connection, its monodromies
around mb and bl (which we will denote by the same symbols) are commuting elements of
G. Generically, we can conjugate them to a common maximal torus TC ⊂ G. According to
(4.21), for a knot labeled by a representation R, mb is conjugate to U = exp(2πµR/k). (More
exactly, as explained in section 4.2.2, this is so if U is regular. In general, U is contained in
the closure of the conjugacy class that contains mb.)
Let us consider in detail the case G = SL(2, C). The maximal torus of G is a copy of
C
∗
, consisting of diagonal matrices

λ 0
0 λ
−1

. (4.34)
An important fact is that in a classical solution of Chern-Simons theory in the presence of a
80

K
mb
bl
Figure 10: A knot K (dotted line) surrounded by a two-torus Y . On Y are drawn the meridian
mb, a circle whose linking number with K is 1, and the longitude bl, whose linking number with K
vanishes.
knot K, we have a little more structure than just a flat connection on the knot complement.
In putting knots in the Morse theory framework, we introduced an H/T or G/TC-valued
field ρ along K. In a classical solution, ρ is invariant under mb and bl, and once mb and bl are
given, the choice of ρ amounts to a choice of one of the two eigenvalues of mb and bl, say
the first eigenvalue (corresponding to λ as opposed to λ
−1
in (4.34)). We write m and l for
the eigenvalues of the loops mb and bl that correspond to ρ. According to (4.23), if R is the
n-dimensional representation of SU(2), then
m = exp(iπ(n − 1)/k). (4.35)
In section 5, we will use this formula in the semiclassical limit of large n, k with fixed ratio
n/k. (In this limit, the difference between n and n − 1 is irrelevant.)
Once K is embedded in a three-manifold – which we will take to be simply a threesphere – l and m are no longer independent. They are constrained by a requirement that an
SL(2, C) flat connection on T with monodromies bl and mb should actually extend over the
knot complement S
3\K.
One simple class of SL(2, C) flat connections are the abelian ones. These are the flat
connections whose structure group reduces to C
∗
, the group of diagonal matrices (4.34).
They are classified very simply. Although the fundamental group of S
3\K can be very
complicated, its first homology group is simply isomorphic to Z, generated by m. This
means that there is up to gauge transformation one flat C
∗
-valued connection on S
3\K for
every choice of m. Such a flat connection always has l = 1.
What about flat connections whose structure group does not reduce to C
∗
? Flat connec81

tions with triangular structure group

α β
0 γ

(4.36)
are unstable and need not be considered as critical points. What this really means is that
to any strictly triangular flat connection there is a corresponding abelian one obtained by
deleting the off-diagonal part of A, and this should be considered instead. An important
point which follows directly from the definition of the Chern-Simons function W(A) is that
this function is invariant under this operation:

α β
0 γ

→

α 0
0 γ

. (4.37)
There remain the irreducible SL(2, C) flat connections. (A flat connection is called
irreducible if the only elements of SL(2, C) that commute with all monodromies are the
central elements ±1.) An irreducible flat connection does not exist for all values of l, m.
Rather, for each knot K, there is a Laurent polynomial A(l, m) (a polynomial in l, l
−1
,
m, m−1) such that the moduli space of irreducible SL(2, C) flat connections on S
3\K is
described by an equation
A(l, m) = 0 (4.38)
which parametrizes values of l and m for which there exists such a connection. A(l, m), which
is often called the A polynomial, is effectively computable for any given knot. We will make
use of some examples in section 5. The A polynomial is invariant under the exchange
l → l
−1
, m → m
−1
, (4.39)
which comes from a Weyl transformation exchanging the two eigenvalues in (4.34). Such a
Weyl transformation does not leave invariant the field ρ that is defined along the knot, but
the definition of the A polynomial does not “know” about ρ. Another symmetry of the A
polynomial is
l → l, m → −m. (4.40)
This symmetry reflects the fact that on S
3\K, there exists a flat complex line bundle L
with monodromies m = −1, l = 1. If E → S
3\K denotes a flat complex vector bundle of
rank 2 and determinant 1, corresponding to a flat SL(2, C) connection, then the operation
E → E ⊗ L reverses the sign of m without changing l. It is not immediately apparent
whether this operation leaves fixed the Chern-Simons function W(A) and therefore whether
it is a symmetry of Chern-Simons theory. We return to this issue in section 4.2.7.
To describe the function W(A) once the A polynomial is known (see [57] for a mathematical treatment), we simply use the variational principle for W(A), which follows directly
from its definition:
δW(A) = 1
2π
Z
S3
Tr δA ∧ F. (4.41)
82

On the other hand, for a flat connection on the knot complement, we have F = (2πµR/k)δK =
(ln mb)δK. In the last step, we used the fact that mb = exp(2πµR/k). So the right hand side
of (4.41) reduces to Tr H
K
δA ln mb. Here, once we diagonalize m, A and δA are also diagonal
along K, and H
K
δA = δ lnbl. So the formula becomes δW = Tr (δ lnbl) ln mb/2π. In expressing
this result in terms of the eigenvalues l and m of the Lie algebra elements bl and mb, we get a
factor of 2 from the trace:
δW(A) = 1
π
δ ln l · ln m. (4.42)
In practice, once the relation between l and m is known, the important results about
W(A) can usually be obtained by integrating this formula. Some slightly subtle examples
will be considered in section 5. Here we will practice with some easy cases.
For an abelian flat connection, l is always 1, so 0 = δ ln l = δW(A). So W(A) is constant
as a function on the moduli space of abelian flat connections on S
3\K. It vanishes for a
trivial flat connection (l = m = 1) so it vanishes for any abelian flat connection. For another
example, consider a unitary flat SL(2, C) connection – in other words, one whose holonomy
lies in SU(2). In this case, l and m are both of absolute value 1, so ln m and ln l are both
imaginary. Hence, δW is real on this locus, consistent with the fact that W is real for an
SU(2) flat connection.
Apart from the factor exp(ikW(A)), the integrand of the path integral in the presence of
a knot also contains an additional factor exp(iIR(ρ, A)), so we need to know how to evaluate
this factor for a classical solution. In the usual gauge in which ρ is constant along K, this
factor reduces to exp(−i
R
K
(µR, A)). This depends only on l and can be understood as a
character of the maximal torus in which l takes values. Schematically we might write it as
l
µR . For the n-dimensional representation of SU(2), this factor is l(n−1)
. Equivalently,
IR(ρ, A) = −i(n − 1) ln l. (4.43)
4.2.6 Branches Of The Logarithm
An obvious point about this last formula is that ln l has many branches. This reflects the
fact that the underlying action IR(ρ, A) is similarly defined only modulo 2π. There are two
possible ways to proceed. If we wish to analytically continue to non-integral values of n,
we should consider a critical point to be a pair consisting of a flat connection of suitable
monodromy and a lift of ln l to C (plus a similar lift of W(A) if we are analytically continuing
in k). This amounts to replacing the loop space of H/T or G/TC with its universal cover.
If we leave n as an integer and analytically continue only with respect to k, we need not
consider the choice of a lift of ln l to be part of the definition of a critical point. Instead,
83

the multivaluedness of the logarithm enters in the following way. Consider the quantity
Im(ikW(A) + iIR(ρ, A)) which one may expect to be conserved by the flow equations. The
multivaluedness of the logarithm means that this quantity is actually only conserved modulo
2π(n − 1)Z. It is conserved in any flow provided we make suitable choices for the branches
of ln l, but there may be no way to choose branches of ln l that depend only on the choice
of a critical point (and not on the choice of a flow line) such that Im(ikW(A) + iIR(ρ, A))
is conserved in every flow.
If instead we analytically continue with respect to n, we must consider the choice of branch
of ln l as part of the definition of a critical point and then the quantity Im(ikW(A)+iIR(ρ, A))
really is conserved by all flows.
See the end of section 5.2.4 for an example in which this issue becomes relevant.
4.2.7 Tensoring With A Flat Line Bundle
As a further application of eqn. (4.42), we will return to the question of whether, for
H = SU(2), the operation E → E × L, where L is a flat line bundle of order 2, is a
symmetry of Chern-Simons theory.
Let ∆W(A) denote the change in W(A) under this operation. We can differentiate
∆W(A) with respect to A by making use of (4.42). The operation E → E ⊗ L leaves
l unchanged and (as it changes the sign of m) shifts ln m to ln m − iπ. So δ∆W(A) =
(δ ln l/π)(−iπ) = −iδ ln l. Integrating, we have ∆W(A) = −i ln l up to an additive constant.
In Chern-Simons theory on a general three-manifold (such as RP3) the constant may be
nonzero.21 But it vanishes for the special case of a knot K ⊂ S
3
. This can be proved by
considering the special case that A is a flat abelian connection (embedded in SL(2, C)) with
appropriate monodromy around K. Tensoring with L gives another flat abelian connection
A′. The monodromies of A and A′ around the longitude and the meridian are related by
m′ = −m, l
′ = l = 1, and moreover W(A) = W(A′
) = 0. So for a knot in S
3
, we have simply
∆W(A) = −i ln l, and, making use of (4.43), we get a symmetry of kW(A) + IR(ρ, A) if we
combine E → E ⊗ L with n → n + k. Allowing for a one-loop quantum shift described in
section 2.7.1, the symmetry is actually
E → E ⊗ L, n → n + k + 2. (4.44)
This is actually the one place in the present paper that it is important to distinguish
a knot (an embedded circle in S
3
) from a link (a disjoint union of embedded circles). The
21It is always an integer multiple of π, though not necessarily of 2π. This can be proved by considering
the Chern-Simons invariant for SO(3, C) = SL(2, C)/Z2.
84

Figure 11: Two linked circles in S
3
.
operation E → E ⊗L, where L has monodromy around a knot, does not affect the longitude
for that knot. But in the case of two or more disjoint embedded circles with nonzero linking
(fig. 11), if L has monodromy around one circle, then tensoring with L may reverse the sign
of the longitude for a second circle. So (4.44) is a symmetry of Chern-Simons theory for a
knot, but not necessarily for a link.
The square of the operation (4.44)
n → n + 2(k + 2) (4.45)
is a universal symmetry of Chern-Simons theory (already mentioned in eqn. (4.27)). Indeed,
L
2
is completely trivial, and tensoring with L
2
leaves m fixed.
