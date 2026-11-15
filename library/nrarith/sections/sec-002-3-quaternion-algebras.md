---
doc_id: nrarith
doc_title: "Arithmetic of Hyperbolic Manifolds"
section_id: sec-002-3-quaternion-algebras
section_title: "Quaternion algebras"
section_number: 3
pages: 7-9
source_pdf: nrarith.pdf
source_sha256: 085ec9541ddc6cd4
toc_source: inferred
doc_brief: "Arithmetic of hyperbolic manifolds (Neumann–Reid) — survey of arithmetic Kleinian groups: an arithmetic M = H³/Γ is determined up to commensurability by its invariant trace field and quaternion…"
---
3.1.
In this section we associate to a Kleinian group Γ a quaternion algebra over the
trace ﬁeld Q(tr Γ). Namely, let Γ be the inverse image of Γ ⊂PSL2C in SL2C and
denote by QΓ the algebra of all Q-linear combinations of elements of Γ. It follows
from the characteristic equation
A2 −(tr A)A + I = 0
that QΓ contains τI for any τ in the trace ﬁeld Q(tr Γ). Hence QΓ is an algebra over
Q(tr Γ) (and equals kΓ for any subﬁeld k of Q(tr Γ)). It is in fact a quaternion algebra
over this ﬁeld (cf. [Ba1, Prop. 2.2] or [Ba2]).
Note that the result of Macbeath quoted in the proof of Lemma 2.6 follows from
the observation that a quaternion algebra is generated over its base ﬁeld by any two
non-commuting elements. For the same reason, although QΓ is not a commensurability
invariant, QΓ(2) is. Together with the trace ﬁeld Q(tr Γ), this commensurability invariant
determines QΓ by the equation
QΓ = QΓ(2) ⊗k(Γ) Q(tr Γ).
Notation. We shall denote QΓ(2) by A(Γ) and call it the invariant quaternion algebra
of Γ.
Lemma 2.6 tells us that the invariant quaternion algebra A(Γ) gives no more infor-
mation than the invariant trace ﬁeld k(Γ) when Γ has cusps—A(Γ) then equals the
matrix algebra M2(k(Γ)). However, in general A(Γ) is more interesting, for instance
A(Γ) is a complete commensurability invariant for arithmetic Γ and equals M2(k(Γ))
in this case if and only if Γ has cusps, as we discuss in the next section.
Recall ([Vig]) that a quaternion algebra A over a number ﬁeld k is determined up to
isomorphism by the set S(A) of primes of k (ﬁnite or inﬁnite) at which A is ramiﬁed;
S(A) has a ﬁnite even number of elements and any ﬁnite even set of primes of k is the
ramiﬁcation set of some quaternion algebra over k.
Little seems to be known about what the invariant A(Γ) of Γ says about the geometry
of H3/Γ. If Γ is arithmetic then Clozel [Cl] has shown
Theorem 3.1. If Γ is arithmetic and S(A(Γ)) contains no ﬁnite primes of k = k(Γ) (or,
more generally, if for each ﬁnite ν ∈S(A(Γ)), the local ﬁeld kν contains no quadratic
extension of Qp, where p is the rational prime that ν divides), then Γ has a subgroup
of ﬁnite index with inﬁnite abelianization—in particular, H3/Γ is almost sufﬁciently
large.
On the other hand, using an observation of [KLS], the existence of ﬁnite ramiﬁcation
for A(Γ) also implies strong results about abelian quotients of ﬁnite index subgroups of
Γ, as we now describe. We formulate the result in terms of QΓ, so let Γ be a Kleinian
group and denote Q(tr Γ) = k and QΓ = A.
Theorem 3.2. Suppose A is ramiﬁed at the ﬁnite prime ν and let p be the rational
prime that ν divides. Then Γ has a normal subgroup ∆with ﬁnite cyclic quotient (of
order dividing pt −1 for some t ≤2[k:Q]) which is residually ﬁnite p, that is, the
intersection of all normal subgroups of ∆of p-power index is trivial.
Before we prove this theorem, we point out that being residually ﬁnite p is a strong
property. Since ﬁnite p-groups are nilpotent, it implies that the lower central p-series of
∆intersects in the trivial group (this is the series of subgroups
∆= ∆0(p) ⊃∆1(p) ⊃∆2(p) ⊃. . . ,
where ∆i(p)/∆i+1(p) is deﬁned inductively to be the largest exponent p quotient of
∆i(p)/[∆, ∆i(p)]). Moreover
Proposition 3.3. Every non-abelian subgroup of a residually ﬁnite p group has a
Z/p × Z/p quotient.
Proof. The subgroup is residually ﬁnite p, so it has a non-abelian p-group quotient.
But any non-abelian p-group G has a Z/p × Z/p quotient—if G/[G, G] were cyclic,
then G/[G, [G, G]] would be a central extension of a cyclic group, hence abelian, so
[G, G] = [G, [G, G]], which contradicts the fact that a ﬁnite p-group is nilpotent.
Proof of Theorem 3.2. (Following [KLS], see also [Vig].) Γ is represented into A1,
the group of elements of A of reduced norm 1, and hence into A1
ν. The discrete valuation
on the local ﬁeld kν extends to one on Aν. Let Oν be the valuation ring (elements of
non-negative valuation in Aν ) and Pν its maximal ideal. Then A1
ν is contained in the
multiplicative group O×
ν of Oν and this multiplicative group has a Hausdorff ﬁltration
O×
ν ⊃(1 + Pν) ⊃(1 + P2
ν) ⊃. . .
whose quotients after the ﬁrst are Z/p-vector spaces and whose ﬁrst quotient is the
multiplicative group of the residue class ﬁeld lν of a certain quadratic extension lν of
kν (the unique unramiﬁed extension of kν ). lν is an extension of degree t ≤2[k:Q] of
the ﬁeld of p elements, so its multiplicative group is cyclic of order pt −1.
A result of G. Mess [Me] is interesting in reference to Theorem 3.2 and Proposi-
tion 3.3—he shows that a 3-manifold group with a Z/p × Z/p quotient must either have
a ﬁnite index subgroup with inﬁnite abelianization or the sizes of the successive quotients
of the derived series must grow rapidly.
3.2.
The trace ﬁeld, invariant trace ﬁeld, and invariant quaternion algebra are quite
strong invariants. The following proposition is trivial (and also applies to the cusp ﬁeld).
Proposition 3.4. Let M = H3/Γ be a hyperbolic orbifold. If M is amphicheiral (has an
orientation reversing symmetry) then Q(tr Γ) = Q(tr Γ), and if M is commensurably
amphicheiral (has an orientation reversing commensurability) then k(Γ) = k(Γ) and
A(Γ) = A(Γ), where the bar is complex conjugation.
For arithmetic Γ, commensurable amphicheirality is equivalent to conjugation sym-
metry of the invariant quaternion algebra (and is also equivalent to the existence of
Fuchsian subgroups—see [R1]), but this is probably false in general. Nevertheless, in
practice the proposition gives an effective test for amphicheirality and commensurable
amphicheirality.
