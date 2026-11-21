---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-006-21-a-simple-invariant
section_title: "A simple invariant"
section_number: 2.1
pages: 22-29
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
A simple invariant
Let (E2n+2, π) be an exact Lefschetz ﬁbration over S. A Lagrangian boundary
condition is an (n+1)-dimensional submanifold Q ⊂E|∂S which is disjoint from
∂hE and such that π|Q : Q →∂S is a submersion, together with κQ ∈Ω1(∂S)
and KQ ∈C∞(Q, R), satisfying Θ|Q = π∗κQ + dKQ. This implies that each
Qz = Q ∩Ez, z ∈∂S, is an exact Lagrangian submanifold of Ez, with function
KQ|Qz (one could consider a more general situation in which the condition on
π|Q is dropped, so that the Qz could have singularities; but we will not do that).
From Lemma 1.3 one sees that parallel transport along ∂S carries the Qz into
each other, in the ordinary sense of the word; this holds in the “exact” sense,
that is to say as exact Lagrangian submanifolds, iﬀκQ = 0. Note also that if
one equips E with a symplectic form Ω+π∗β as in Lemma 1.5, Q itself becomes
a Lagrangian submanifold. The aim of this section is to introduce, in the case
where S is compact with ∂S̸ = ∅, a Gromov-type invariant
Φ1(E, π, Q) ∈H∗(Qζ; Z/2),
where ζ is some point of ∂S. In a nutshell, this is the cycle represented by the
values at ζ of pseudo-holomorphic sections of E with boundary in Q.
To begin, we remind the reader of a class of almost complex structures suit-
able for exact symplectic manifolds. The Liouville vector ﬁeld N on such a
manifold, iNω = θ, deﬁnes a collar R−× ∂M֒ →M. Let σ be the function on
a neighbourhood of ∂M whose composition with R−× ∂M֒ →M is projection
to the R−factor. An ω-compatible almost complex J is called convex near the
boundary if θ ◦J = d(eσ) near ∂M. This implies d(d(eσ) ◦J) = −ω, which
serves to control the behaviour of J-holomorphic curves. It is well-known that
the space of these J is contractible (in particular, nonempty).
22
Given an exact Lefschetz ﬁbration (E, π), one can consider the Liouville
vector ﬁeld on each ﬁbre, and this gives rise to a function σ on a neighbourhood
of ∂hE in E. Choose a complex structure j on the base S (whenever we do
that, now or later, j is assumed to be positively oriented and equal to j0 in
some neighbourhood of Scrit). An almost complex structure J on E is called
compatible relative to j if
(i) J = J0 in a neighbourhood of Ecrit;
(ii) Dπ ◦J = j ◦Dπ;
(iii) Ω(·, J·)|T Ev
x is symmetric and positive deﬁnite for any x ∈E;
(iv) in a neighbourhood of ∂hE, J(T Eh) = T Eh and Θ ◦J = d(eσ).
To see more concretely the meaning of these conditions, take x /∈Ecrit and split
T Ex = T Eh
x ⊕T Ev
x ∼= T Sz ⊕T Ev
x, z = π(x). One can then write
Jx =
 jz
0
Jvh
x
Jvv
x

(2.1)
where Jvv
x
∈End(T Ev
x) is a complex structure compatible with Ω|T Ev
x, and
Jvh
x
∈Hom(T Sz, T Ev
x) is C-antilinear with respect to j and Jvv.
This is a
reformulation of (ii), (iii). An immediate consequence is the following result,
which sharpens Lemma 1.5:
Lemma 2.1. Let J be compatible relative to j. Then for any suﬃciently posi-
tive β ∈Ω2(S), Ω+ π∗β tames J.
Because of the lack of antisymmetry in (2.1), J will not be compatible with
Ω+ π∗β in the ordinary sense of the word, unless Jvh = 0; we will return
to this more restricted class of almost complex structures in the next section.
Continuing with the analysis of the conditions above, suppose now that x ∈E
is suﬃciently close to ∂hE. More precisely, we require that σ(x) is deﬁned and
that (iv) applies. There is then a further splitting
T Ev
x ∼= RN ⊕RR ⊕(ker Θ ∩ker dσ ∩T Ev
x),
(2.2)
where N is the Liouville vector ﬁeld and R is the Hamiltonian vector ﬁeld of
eσ|Ez. The two parts of (iv) say that Jvh
x
= 0 and that with respect to (2.2),
Jvv
x
=


0
−1
0
1
0
0
0
0
∗

.
(2.3)
The pointwise analysis which we have just carried out can be recast in terms of
sections of ﬁbre bundles, and one sees then that the space J(E, π, j) of almost
complex structures which are compatible relative to j is contractible.
Suppose now that we have a Lagrangian boundary condition Q. The theory of
pseudo-holomorphic sections with boundary in Q ﬁts into a familiar framework
23
of inﬁnite-dimensional manifolds and maps. We will now review this, on a formal
level, that is to say using C∞spaces and without assuming that S is compact.
In that sense, J(E, π, j) is an inﬁnite-dimensional manifold; its tangent space at
J consists of sections Y ∈C∞(End(T E)) which are zero near Ecrit and can be
written, in parallel with (2.1), as
Yx =
 0
0
Y vh
x
Y vv
x

(2.4)
with Y vv
x
an inﬁnitesimal deformation of the compatible complex structure Jvv
x ,
and Y vv
x Jvh
x
+ Jvv
x Y vh
x
= −Y vh
x jz.
There is a further requirement about Y
near ∂hE, the linearization of (iv), which we leave to the reader to write
down.
The space B of sections u : S →E satisfying u(∂S) ⊂Q is also
an inﬁnite-dimensional manifold, with T Bu = {X ∈C∞(u∗T Ev)
:
Xz ∈
T (Qz) for all z ∈∂S}; note that u∗T Ev →S is really a vector bundle, since u
as a smooth section of π avoids Ecrit. Consider the inﬁnite-dimensional vector
bundle E →B × J(E, π, j) whose ﬁbre at (u, J) is Ω0,1(u∗T Ev), the space of
(0, 1)-forms on (S, j) with values in u∗(T Ev, J|T Ev). It has a canonical sec-
tion ¯∂univ(u, J) = 1
2(Du + J ◦Du ◦j), and the zero set Muniv = (¯∂univ)−1(0)
consists of pairs (u, J) such that u is (j, J)-holomorphic. We denote by ¯∂J,
MJ the restrictions of ¯∂univ, Muniv to a ﬁxed J ∈J(E, π, j).
The deriva-
tive of ¯∂J at u ∈MJ is a map Du,J : T Bu →Eu,J. An explicit formula is
Du,J(X) = 1
2(L ˜
XJ)◦Du ◦j where ˜X is any section of T Ev, deﬁned on a neigh-
bourhood of im(u) in E, such that u∗˜X = X. After choosing a torsion-free
connection ∇on T E (away from Ecrit) which preserves the integrable subbun-
dle T Ev, one transforms this into the more familiar expression
Du,J(X) = ¯∂J,u∗∇X + 1
2(∇XJ) ◦Du ◦j,
(2.5)
in which ¯∂J,u∗∇= (u∗∇)0,1 is the ¯∂-operator associated to the pullback con-
nection u∗∇on u∗(T Ev, J|T Ev).
The derivative of ¯∂univ, Duniv
u,J
: T Bu ×
T J(E, π, j)J −→Eu,J, is obviously
Duniv
u,J (X, Y ) = Du,J(X) + 1
2Y ◦Du ◦j.
(2.6)
From this point onwards, we pass to a more realistic situation, and assume
that S is compact with ∂S̸ = ∅.
Our ﬁrst observation is a consequence of
(iv). Informally speaking, it says that for the purposes of pseudo-holomorphic
sections, the boundary ∂hE of the ﬁbres can be ignored.
Lemma 2.2. For every J ∈J(E, π, j) there is a compact subset K ⊂E \ ∂hE
such that all u ∈MJ satisfy u(S) ⊂K.
Proof. Let W ⊂E be a closed neighbourhood of ∂hE which, under the collar
embedding provided by the Liouville vector ﬁelds on the ﬁbres, corresponds to
[−ǫ; 0] × ∂hE for some ǫ > 0. By deﬁnition σ(W) = [−ǫ; 0]. After possibly
making W and ǫ smaller, we may assume that W ∩Q = ∅, that Ω|T Eh vanishes
24
on W, and that (iv) holds there. From Ω|T Eh
x = 0 and J(T Eh
x) = T Eh
x it
follows that Ω(X, JX) ≥0 for all X ∈T Ex, x ∈W. Take u ∈MJ and consider
the function h = eσ ◦u on U = u−1(W). This satisﬁes h|∂U ≡e−ǫ and is
subharmonic, because d(dh ◦j) = d(Θ ◦J ◦Du ◦j) = −u∗Ω≤0. It follows
that h ≤e−ǫ everywhere, which shows that K = E \ int(W) has the required
property.
The action of u ∈B is deﬁned to be A(u) =
R
S u∗Ω. This is actually the
same for all u, since
Z
S
u∗Ω=
Z
∂S
u∗Θ =
Z
∂S
κQ.
(2.7)
Therefore, if one equips E with a symplectic form Ω+ π∗β taming J, all the
u ∈MJ become pseudo-holomorphic curves with the same energy 1
2
R
S ||Du||2 =
A(u) +
R
S β.
Lemma 2.3. MJ is compact in any Cr-topology.
Proof. We apply the Gromov compactness theorem for (j, J)-holomorphic maps
S →E with boundary in Q. The bubble components in the Gromov limit appear
through a reparametrization which “magniﬁes” successively smaller parts of the
domain. Since in our case all maps are sections, the bubbles are either noncon-
stant J-holomorphic spheres in some ﬁbre Ez, or nonconstant J-holomorphic
discs in Ez, z ∈∂S, with boundary on Qz. But both are excluded by our as-
sumptions, since Ωis exact and Qz ⊂Ez an exact Lagrangian submanifold.
A less formal version of the inﬁnite-dimensional framework introduced above
involves spaces of W 1,p-sections, p > 2. We omit the construction itself, and
only mention its main consequence. For (u, J) ∈Muniv, the diﬀerential operator
Du,J extends to a Fredholm operator W1
u →W0
u,J from the W 1,p-completion
W1
u of T Bu to the Lp-completion W0
u,J of Eu,J. We denote this extension equally
by Du,J. If it is onto (in which case one says that u is regular), MJ is a smooth
ﬁnite-dimensional manifold near u. If that holds for all u ∈MJ, J itself is called
regular, and the space of such J is denoted by Jreg(E, π, Q, j) ⊂J(E, π, j).
Lemma 2.4. Jreg(E, π, Q, j) is C∞-dense in J(E, π, j). In fact the following
stronger statement holds: take some nonempty open subset U ⊂S and a J ∈
J(E, π, j). Then there are J′ ∈Jreg(E, π, Q, j) arbitrarily close to J, such that
J = J′ outside π−1(U).
Proof. Even though this is a well-known argument, we recall part of it as a
preparation for subsequent more reﬁned versions. Fix U and J. By Lemmas 2.2
and 2.3 there is an open subset V ⊂E with V ∩(∂hE ∪Ecrit) = ∅, such that
im(u) ⊂V for each u ∈MJ. A modiﬁed version of the compactness argument
shows that this property, with the same V , remains true for all almost complex
structures in J(E, π, j) which are suﬃciently close to J. We want to make J
25
regular by perturbing it on V ∩π−1(U). Take T ⊂T J(E, π, j)J to be the subset
of those Y which vanish outside V ∩π−1(U), and consider the operator
Duniv
u,J
: W1
u × T −→W0
u,J
(2.8)
given by the same formula as in (2.6). By a standard arguments surjectivity
of this operator implies the desired result (strictly speaking, what comes up in
this argument is a dense subspace of those Y which have “ﬁnite C∞
ǫ -norm”, but
since the ﬁrst component Du,J is Fredholm, this makes no diﬀerence as far as
surjectivity is concerned). Let F →S be the bundle dual to Λ0,1(u∗T Ev), so
that (W0
u,J)∗∼= Lq(F), p−1 + q−1 = 1. Suppose that η ∈Lq(F) is orthogonal
to the image of (2.8). It then satisﬁes
D∗
u,Jη = 0 on S \ ∂S,
and
Z
S
⟨η, Y ◦Du ◦j⟩= 0 for Y ∈T.
(2.9)
The ﬁrst equation implies that η is smooth away from the boundary. Suppose
that z ∈U \ ∂S is a point where ηz̸ = 0, and set x = u(z) ∈V ∩π−1(U). Take
a (j, J)-antilinear map Z : T Sz →T Ev
x such that ⟨ηz, Z ◦j⟩̸ = 0. One can see
from (2.4) that there is a Y ∈T J(E, π, j)J with Y vh
x
= Z, Y vv
x
= 0, and this
will satisfy ⟨ηz, (Y ◦Du ◦j)z⟩̸ = 0. By multiplying Y with a bump function
supported near x, one can achieve that it lies in T and that
R
S⟨η, Y ◦Du◦j⟩̸ = 0,
a contradiction. This means that η | (U \ ∂S) = 0. By unique continuation
η | (S \ ∂S) = 0, which proves that η = 0.
Take some ζ ∈∂S and consider the map evζ : B →Qζ, evζ(u) = u(ζ). The
next result belongs to a type called “transversality of evaluation”.
Lemma 2.5. Let g be a smooth map from some arbitrary manifold G to Qζ.
Then, for any J and U as in the previous lemma, there are J′ ∈Jreg(E, π, Q, j)
arbitrarily close to J, with J′ = J outside π−1(U), such that evζ|MJ′ is trans-
verse to g.
Proof. In the same setup as before, one now has to prove that for u ∈MJ and
x = u(ζ) ∈Qζ, the operator
W1
u × T −→W0
u,J × T (Qζ)x,
(X, Y ) 7−→(Duniv
u,J (X, Y ), Xζ)
is onto. Take (η, ξ) orthogonal to the image, with ξ ∈T (Qζ)∨
x. One still has
(2.9) and as before it follows that η = 0. Then ⟨ξ, Xζ⟩= 0 for all X ∈W1
u, so
that ξ = 0 as well.
For a given (E, π, Q) and ζ, one now proceeds as follows. After choosing
some j and a J ∈Jreg(E, π, Q, j), one obtains a smooth compact moduli space
MJ; and then one sets
Φ1(E, π, Q) = (evζ)∗[MJ] ∈H∗(Qζ; Z/2).
This is independent of the choice of j, J by a standard argument using parame-
trized moduli spaces. The same reasoning shows that it remains invariant under
26
any “smooth deformation” of the geometric objects involved, that is to say of
Q, Ω, Θ or of the ﬁbration π : E →S itself, as long as one remains within
the class of exact Lefschetz ﬁbrations with Lagrangian boundary conditions. It
seems pointless to formalize this notion of deformation, because the necessary
conditions will be quite obviously satisﬁed in all our applications.
Remark 2.6. Since the regular spaces MJ are actual manifolds, one can re-
ﬁne Φ1(E, π, Q) by regarding it as an element of the unoriented bordism group
MO∗(Qζ). But even with this reﬁnement, it is far from capturing all the infor-
mation contained in MJ. To get more sophisticated invariants one can use eval-
uation at several points, allowing those to move; we will now explain the simplest
version of this. Given ζ ∈∂S, choose a positively oriented path c : [0; 1] →∂S,
c(0) = c(1) = ζ, parametrizing the boundary component on which ζ lies. Let
φt : Qc(t) →Qζ be the diﬀeomorphisms obtained from symplectic parallel trans-
port along c|[t; 1].
Denote by ∆, Γ ⊂Q2
ζ the diagonal and the graph of φ0,
respectively. For regular J, the parametrized evaluation map
eevζ : [0; 1] × MJ →[0; 1] × Q2
ζ,
eevζ(t, u) = (t, u(ζ), φt(u(c(t))))
represents a class ˜Φ2(E, π, Q) ∈H∗([0; 1] × Q2
ζ, {0} × Γ ∪{1} × ∆; Z/2), and
this (as well as its cobordism version) is an invariant of (E, π, Q). An example
of this invariant will be computed in Remark 2.17(iii).
Let S1, S2 be two compact surfaces with marked points ζk ∈∂Sk, and denote
by S = S1#ζ1∼ζ2S2 their boundary connected sum (Figure 2). To be precise,
one should choose oriented embeddings ψk : ¯D+(1) →Sk of the closed half-
disc ¯D+(1) = {z ∈C
:
|z| ≤1, im z ≥0} into Sk, such that ψk(0) =
ζk and (ψk)−1(∂Sk) = [−1; 1].
Then, writing D+(ρ) for the open half-disc
of some radius 0 < ρ < 1, one forms S by taking the two Sk \ ψk(D+(ρ))
and identifying ψ1(z) with ψ2(−ρ−1z). Suppose that we have exact Lefschetz
ﬁbrations (Ek, πk) over Sk, such that their symplectic connections are trivial on
im(ψk); together with Lagrangian boundary conditions Qk ⊂Ek, such that the
one-forms κQk vanish on ψk([−1; 1]); and ﬁnally, an exact syplectic manifold M
with an exact Lagrangian submanifold L, and isomorphisms φk : M →(Ek)ζk
satisfying φk(L) = (Qk)ζk.
One can then glue the (Ek, πk) and Qk to an
exact Lefschetz ﬁbration over S. To do that, one ﬁrst uses symplectic parallel
transport to construct embeddings
¯D+(1) × M
Ψk /

Ek
πk

¯D+(1)
ψk
/ Sk
such that Ψk|{0} × M = φk. These will satisfy
(Ψk)∗Ωk = ω,
(Ψk)∗Θk = θ + dRk,
(Ψk)−1(Qk) = [−1; 1] × L
27
for some functions Rk.
As in the pasting construction described in Section
1.1, one needs to introduce modiﬁed forms ˜Θk such that (Ψk)∗˜Θk = θ near
{0} × M.
The functions KQk need to be modiﬁed accordingly, but that is
rather straightforward, so we will not write it down explicitly. Now take the Ek\
Ψk(D+(ρ)×M) and identify Ψ1(z, x) with Ψ2(−ρz−1, x). This yields a manifold
E with a map π : E →S, and the remaining data matches up, producing the
structure of an exact Lefschetz ﬁbration together with a Lagrangian boundary
condition Q.
1
ζ
S
S
S
2
1
ζ2
Figure 2:
Assume that one has chosen complex structures jk on Sk such that the ψk
are holomorphic; these determine a complex structure j on S.
Take Jk ∈
J(Ek, πk, jk) such that (Ψk)∗(Jk) is the product of the standard complex struc-
ture on ¯D+(1) and of some ﬁxed ω-compatible almost complex structure on M
(the same for both k). Then there is a canonical induced J ∈J(E, π, j). Note
that even though we have restricted the behaviour of Jk over im(Ψk), it is still
possible to choose them regular, by using the more precise statement in Lemma
2.4. Moreover, Lemma 2.5 says that for suitably chosen Jk, the evaluation maps
evζk|MJk : MJk →Qk
ζk ∼= L will be transverse to each other.
Proposition 2.7. Assume that Jk ∈Jreg(Ek, πk, Qk, jk) for k = 1, 2, and that
the evζk|MJk are mutually transverse. Choose a suﬃciently small parameter ρ
for the gluing. Then J ∈Jreg(E, π, Q, j), and there is a diﬀeomorphism
MJ ∼= MJ1 ×L MJ2,
where the right hand side is the ﬁbre product of (evζ1, evζ2).
This is an average specimen of the “gluing theorem” type. The closest re-
lated argument in the literature would seem to be the gluing theory for pseudo-
holomorphic discs from [8, Section 18], which is far more sophisticated than
28
what we need here; as an alternative, one can probably adapt the proof of the
more familiar gluing theorem for closed pseudo-holomorphic curves [21, Section
6], [15, Appendix A], [14]. The obvious next step would be to write down the
outcome as a “gluing formula”. However, while gluing will be important later,
the situation then will be slightly diﬀerent from that covered by Proposition
2.7. For this reason, further discussion is postponed to Section 2.4.
