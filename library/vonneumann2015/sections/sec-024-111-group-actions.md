---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-024-111-group-actions
section_title: "Group actions."
section_number: 11.1
pages: 69-71
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Group actions.
Let M be a von Neumann algebra and G a group. An action of G on M
is a homomorphism g 7→αg from G to the automorphism group AutM of
M (where automorphisms may be assumed ultraweakly continuous if neces-
sary). The algebra of ﬁxed points for the action is denoted M G and is a von
69
Neumann algebra. A special case of some importance is when the action is a
unitary group representation g 7→ug with ugMu∗
g = M ∀g ∈G. In that case
setting αg(x) = ugxu∗
g deﬁnes an action of G on M (and M ′). We say that
the action α is implemented by the unitary representation ug. If the ug are
actually in M, we say that the action is inner as an inner automorphism of
M is by deﬁnition one of the form Ad u(x) = uxu∗for u a unitary in M. An
automorphism is called outer if it is not inner.
Actions are not always implementable though the notion depends on the
Hilbert space on which M acts.
Exercise 11.1.1. If (X, µ) is a measure space and T is a bijection of X
which preserves the measure class of µ (i.e. µ(A) = 0 ⇔µ(T −1(A)) = 0.)
show how T deﬁnes an automorphism αT of L∞(X, µ). Show further that
this automorphism is implemented by a unitary u on L2(X, µ).
A bijection T as above is called ergodic if T(A) = A for a measurable
subset A ⊆X implies either µ(A) = 0 or µ(X \ A) = 0.
Proposition 11.1.2. With notation as above T is ergodic iﬀthe only ﬁxed
points for αT are constant functions.
Proof. (⇒) Let f ∈L∞and αT(f) = f. After throwing away a null set we
may assume that f(x) = f(T(x)) for all x ∈X. Then for every ϵ > 0, by
the deﬁnition of the essential supremum, µ({x : ||f|| −|f(x)| < ϵ}̸ = 0. But
this set is invariant under T so it is equal to X up to a set of measure 0.
Letting ϵ tend to 0 we see that µ({x : |f(x)|̸ = ||f||}) = 0. So we may assume
f(x) = eig(x) for some measurable g taking values in [0, 2π). Repeating the
argument for g gives f constant almost everywhere.
(⇐) If A is a measurable invariant set then its characteristic function is
ﬁxed by α in L∞iﬀA is invariant.
Exercise 11.1.3. Let σx = ( 0 1
1 0 ), σy = ( 0 −i
i
0 ) and σz = ( 1
0
0 −1 ) be the Pauli
spin matrices.
Show that Ad ux, Ad uy and Ad uz deﬁne an action of the
group Z/2Z ⊕Z/2Z on the two by two matrices which is not implementable
for M2(C) on C2.
Exercise 11.1.4. Show that any group action is implementable for a type
II1 factor in standard form and more generally any automorphism group pre-
serving a faithful normal state is implementable in the GNS representation.
Exercise 11.1.5. Show that every automorphism of B(H) is inner.
Exercise 11.1.6. Show that the automorphism of vN(F2) coming from the
group automorphism which exchanges the 2 generators is outer.
70
If G is a topological group there are many possible notions of continuity.
The most useful is that of pointwise *-strong convergence, i.e. we assume that
the map g 7→α(g)(x) is *-strong continuous for any x ∈M. Typically many
other notions of continuity will be equivalent to that and even a measurability
assumption can be enough to ensure this continuity.
We will always assume pointwise *-strong continuity when referring to an
action of a topological group.
Exercise 11.1.7. Is the action by translation of R on L∞(R) pointwise norm
continuous? pointwise strongly continuous? pointwise *-strong continuous?
Actions of a given group on von Neumann algebras are easy to construct
but actions of a group on a given von Neumann algebra may be hard to come
by.
Deﬁnition 11.1.8. An action of G on M is said to be ergodic if M G = Cid.
Exercise 11.1.9. Show that if G acts preserving µ on (X, µ) then the re-
sulting action of G on L∞(X, µ) is ergodic iﬀthe only measurable subsets
A ⊆X which satisfy µ(g(A)∆A) = 0 ∀g ∈G satisfy either µ(A) = 0 or
µ(X \ A) = 0.
(Here A∆B means A \ B ∪B \ A.)
The following question is an intriguing open problem:
Does SU(3) have any ergodic action on a type II1 factor?
It is shown in [] that SU(2) has no such action and it is shown in [] that
if a compact group acts ergodically on a von Neumann algebra then that von
Neumann algebra has a faithful normal trace.
