---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-007-22-horizontality
section_title: "Horizontality"
section_number: 2.2
pages: 29-32
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
Horizontality
Let (E, π) be an exact Lefschetz ﬁbration. Choose a complex structure j on its
base. J ∈J(E, π, j) is called horizontal if Jx(T Eh
x) = T Eh
x for all x /∈Ecrit, or
what is equivalent, if Ω(·, J·) is symmetric. In terms of (2.1) these are just the J
with Jvh = 0, which shows that they form a contractible subspace Jh(E, π, j) ⊂
J(E, π, j). The importance of horizontal almost complex structures is that they
are sensitive to the geometry of the symplectic connection; the following is a
particularly simple instance of this.
Lemma 2.8. Let (E, π) be an exact Lefschetz ﬁbration over a compact surface
S, ∂S̸ = ∅, with a Lagrangian boundary condition Q. Assume that (E, π) has
nonnegative curvature, and that the boundary condition satisﬁes
R
∂S κQ < 0.
Then Φ1(E, π, Q) = 0.
Proof. For J ∈Jh(E, π, j), take a symplectic form Ω+ π∗β as in Lemma 2.1.
Then J is compatible with it in the ordinary sense of the word; we denote the as-
sociated metric by ||·||. Write Ω|T Eh = f(π∗β|T Eh) with f ∈C∞(E\Ecrit, R).
For any map u from a compact Riemann surface, possibly with boundary, to E
there is the familiar equality 1
2
R
||Du||2 =
R
u∗(Ω+π∗β)+
R
||¯∂Ju||2. Specialize
to sections u and split Du = (Du)h + (Du)v into horizontal and vertical parts.
Since ||(Du)h||2 = 2(f(u) + 1)β, one obtains
1
2
Z
S
||(Du)v||2 +
Z
S
f(u)β =
Z
S
u∗Ω+
Z
S
||¯∂Ju||2.
(2.10)
This implies that MJ = ∅.
In fact, the curvature assumption is just that
f ≥0, while for u ∈MJ one would have R
S u∗Ω< 0 by (2.7) and the second
assumption.
A section u : S →E is called horizontal if Duz(T Sz) = (T Eh)u(z) for
all z ∈S. To see the geometric meaning of this, it is convenient to exclude
temporarily the presence of critical points, so that (E, π) is an exact symplectic
ﬁbration. If u is horizontal, parallel transport along any path c : [a; b] →S
carries u(c(a)) ∈Ec(a) to u(c(b)) ∈Ec(b). In other words, if M is some ﬁbre
of E and x ∈M the unique point through which u passes, the structure group
of the symplectic connection on E is reduced from Sympe(M) to the subgroup
Sympe(M, x) of maps preserving x. This entails a restriction on the curvature,
29
namely, writing Ω|T Eh = f(π∗β|T Eh) for some positive β ∈Ω2(S), one has
d(f|Ez)u(z) = 0
for all z ∈S.
(2.11)
If u is horizontal, the symplectic vector bundle u∗T Ev →S has a preferred con-
nection ∇u, obtained by linearizing parallel transport around u. Equivalently,
this is induced from the connection on E by the derivative map Sympe(M, x) →
Sp(T Mx). Explicitly ∇u
ZX = u∗([Zh, ˜X]), where ˜X is any section of T Ev with
u∗˜X = X. Using the canonical isomorphism sp(V ) ∼= sym2(V ∗) for any sym-
plectic vector space V , one can write the curvature of ∇u as a two-form on S
with values in quadratic forms on the ﬁbres of u∗T Ev. In those terms it is given
by F∇u = Hess(f|Ez)u(z)β, which is well-deﬁned by (2.11). We say that ∇u is
nonnegatively curved if all these Hessians are ≥0. The “inﬁnitesimal deforma-
tions” of a horizontal section u are the covariantly constant sections, ∇uX = 0.
If such a section exists, it further reduces the structure group of (E, π) to the
subgroup of maps in Sympe(M, x) which preserve a certain tangent vector at x.
The resulting curvature restriction is
Hess(f)u(z)(X(z), X(z)) = 0
for all z ∈S.
(2.12)
Finally, if one readmits critical points, all the formulae derived above remain
valid, with essentially the same proofs, except that when talking about the
symplectic connection on E it is necessary to restrict to a neighbourhood of a
ﬁxed horizontal section.
The connection between the two notions which we have introduced so far is
that a horizontal section is (j, J)-holomorphic for any horizontal J. This pro-
vides a useful class of pseudo-holomorphic sections with a geometric origin, but
it also raises a problem: if the space of horizontal sections has “too large dimen-
sion”, one cannot ﬁnd an almost complex structure which is both regular and
horizontal. The rest of this section discusses this issue in more detail. Assume
from now on that S is compact with ∂S̸ = ∅, and that we have a Lagrangian
boundary condition Q. Write Mh for the space of horizontal sections u which
lie in B, meaning that u(∂S) ⊂Q. Since a horizontal section is determined by
its value at any point, evaluation at ζ ∈∂S identiﬁes Mh with a subset of Qζ.
As observed above, Mh ⊂MJ for all J ∈Jh(E, π, j).
Lemma 2.9. Let U ⊂S be a nonempty open subset, such that any partial
section u : U →E|U which is horizontal and satisﬁes u(∂S ∩U) ⊂Q is the
restriction of some u′ ∈Mh.
Then, given some J ∈Jh(E, π, j), there are
J′ ∈Jh(E, π, j) arbitrarily close to it and which agree with it outside π−1(U),
with the property that any u ∈MJ′ \ Mh is regular.
Proof. Take V ⊂E as in the proof of Lemma 2.4. In parallel with the argument
there, we have to show that for any u ∈MJ \ Mh,
Duniv
u,J
: W1
u × Th −→W0
u,J
(2.13)
30
is onto. Here Th = T ∩T Jh(E, π, j)J is the space of inﬁnitesimal deformations
Y of J within the class of horizontal almost complex structures, that is to say
with Y vh = 0 in (2.4), and such that Y = 0 outside V ∩π−1(U). As before, an
η which is orthogonal to the image of (2.13) is smooth away from the boundary
and satisﬁes
Z
S
⟨η, Y ◦Du ◦j⟩= 0
for Y ∈Th.
(2.14)
Suppose that u|U is horizontal. By assumption one could then ﬁnd a u′ ∈Mh
with u′|U = u|U; unique continuation for pseudo-holomorphic curves would im-
ply that u′ = u, a contradiction. Hence there is a z ∈U such that Duz(T Sz)̸ =
(T Eh)u(z). This is an open condition, so we can assume that z ∈U \ ∂S. By
choosing Y suitably in Th, one can make (Y ◦Du ◦j)z equal to any arbitrary
(j, J)-antilinear homomorphism T Sz →(T Ev)u(z). In particular, if ηz̸ = 0 one
can achieve that ⟨ηz, (Y ◦Du ◦j)z⟩̸ = 0, which after multiplying with a cutoﬀ
function leads to a contradiction with (2.14). The same argument applies to
all points close to z, proving that η vanishes on a nonempty open subset, from
which it follows that η = 0.
In particular, taking U = S shows that if Mh = ∅then Jreg,h(E, π, Q, j) =
Jreg(E, π, Q, j) ∩Jh(E, π, j) ⊂Jh(E, π, j) is a dense subset. In the same way
one proves the following analogue of Lemma 2.5:
Lemma 2.10. Let g be a smooth map from an arbitrary manifold G to Qζ,
for some ζ ∈∂S.
Let U ⊂S be a nonempty open subset, such that there
are no horizontal partial sections u : U →E|U with u(∂S ∩U) ⊂Q. Given
J ∈Jh(E, π, j), there are J′ ∈Jreg,h(E, π, Q, j) arbitrarily close to it and which
agree with it outside π−1(U), such that evζ|MJ′ is transverse to g.
Let TZar(Mh)u be the Zariski tangent space of Mh at some section u. It
consists of those X ∈C∞(u∗T Ev) that satisfy ∇uX = 0 and lie in T Bu,
meaning that X|∂S ⊂u∗(T Q ∩T Ev).
The next result helps to determine
when u, considered as a pseudo-holomorphic section for some horizontal almost
complex structure, is regular.
Lemma 2.11. Take J ∈Jh(E, π, j) and u ∈Mh. Then TZar(Mh)u ⊂ker Du,J,
and if moreover ∇u is nonnegatively curved, the two spaces are equal.
Proof. We take the second derivative of (2.10) at u. This is well-deﬁned because
the action A is constant on B and the other terms vanish to ﬁrst order at u.
The outcome is that for X ∈T Bu,
Z
S
||∇uX||2 +
Z
S
Hess(f ◦u)(X, X) β = 2
Z
S
||Du,JX||2.
(2.15)
If ∇uX = 0 then Hess(f ◦u)(X, X) = 0 by (2.12), which implies that Du,JX =
0. If ∇u has nonnegative curvature, the converse also holds, since the second
term in (2.15) is ≥0.
31
Call Mh clean if it is a smooth manifold and its tangent space is everywhere
equal to TZarMh.
The next result can be considered as a limiting case of
Lemma 2.8 (and is again just a sample application, in itself without any great
importance, but hopefully instructive).
Lemma 2.12. Assume that (E, π) has nonnegative curvature, and that the La-
grangian boundary condition Q satisﬁes
R
∂S κQ = 0. In addition, assume that
Mh is clean and that its dimension agrees at every point with the index of Du,J.
Then Φ1(E, π, Q) = [evζ(Mh)].
Proof. Take J ∈Jh(E, π, j), and consider (2.10). Since f ≥0 and
R
S u∗Ω= 0,
it follows that MJ = Mh, and moreover that every u ∈Mh satisﬁes f(u) ≡0,
which in turn implies Hess(f|Ez)u(z) ≥0. Applying Lemma 2.11 shows that
dim ker Du,J = dim TZarMh = dim Mh = ind Du,J, from which one sees that
coker Du,J = 0; hence J is regular.
