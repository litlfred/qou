---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-013-31-basic-notions
section_title: "Basic notions"
section_number: 3.1
pages: 25-28
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
we brieﬂy recall. Let Q = ( Q0, Q1, s, t) denote a quiver, that is, a pair of ﬁnite
sets Q0 and Q1, and a pair of maps s : Q1 → Q0 and t : Q1 → Q0, taking an arrow
to its source and target, respectively. Denote by CQ the free path category of Q
over C. Alternatively we may think of CQ as the free path algebra of Q, with a
distinguished family of mutually orthogonal idempotents ei in bijection with the
vertices Q0, summing to 1 CQ.
Let Sch C be the category of schemes over Spec( C). For S ∈ SchC we denote by
Vectf.d.
S the category of ﬁnite rank vector bundles over S. Let d ∈ NQ0 be a dimen-
sion vector. We denote by Md the groupoid valued functor on Sch C that assigns to
S ∈ SchC the groupoid obtained from forgetting the non-invertible morphism s in
the full subcategory of functors in Fun( CQ, Vectf.d.
S ) such that i ∈ Q0 is sent to a
vector bundle of dimension di. This prestack is an Artin stack, as it is represented
by the following global quotient stack. First deﬁne
(36) Xd :=
∏
a∈Q1
Hom(Cds(a) , Cdt(a) ).
This aﬃne space carries the change of basis action of
Gd :=
∏
i∈Q0
Aut(Cdi),
and there is an equivalence of stacks Md ∼
= Xd/Gd. We denote by M the union∐
d∈NQ0 Md, the stack of ﬁnite-dimensional representations of Q, which by the
equivalences just given is a countable disjoint union of ﬁnite type glob al quotient
Artin stacks.
In numerous instances we wish to take cohomology of sheaves rest ricted to a
substack of Md. To that end, we assume that for each d ∈ NQ0 we are given
reduced subschemes
(37) X S
d ⊂ Xd
which are preserved by the action of Gd, and such that the set S of CQ-representations
that are isomorphic to representations parametrised by points of X S =∐ X S
d are
the objects in a Serre subcategory of the category of ﬁnite-dime nsional CQ repre-
sentations. In other words, if
(38) 0 →ρ′ →ρ →ρ′′ → 0
is a short exact sequence of CQ-representations,ρ′ and ρ′′ are in S if and only if
ρ is in S. We set MS ⊂ M to be the reduced substack, the closed points of which
correspond to modules in S. Then MS
d = X S
d /Gd. We denote by
ωd : X S
d → Xd
ωd : MS
d → Md
the natural inclusions.
26 BEN DA VISON AND SVEN MEINHARDT
For the rest of the paper, Xd and X S
d will be as in (36) and (37) respectively.
Where we wish to be speciﬁc regarding the quiver with respect to whic h these
spaces are deﬁned, we will instead use the notation X(Q)d or X(Q)S
d.
For d′ + d′′ = d ∈ NQ0 let Md′,d′′ (S) be the groupoid of triples ( F ′, F, ι), where
F ′, F ∈ Fun(CQ, Vectf.d.
S ) and ι : F ′ → F is a natural transformation, such that
rank(F ′(i)) = d′
i, rank( F (i)) = di, and ι(i) is injective, with locally free cokernel,
for every i. Again, Md′,d′′ is a ﬁnite type Artin stack, which can be described
as follows. Let Xd′,d′′ ⊂ Xd be the subspace of representations such that the
ﬂag Cd′
i ⊂ Cdi is preserved for all i ∈ Q0, and let Gd′,d′′ ⊂ Gd be the subgroup
preserving these same ﬂags. Then
Md′,d′′ ∼
= Xd′,d′′ /Gd′,d′′ .
We likewise deﬁne MS
d′,d′′ ⊂ Md′,d′′ to be the reduced substack of the stack
parametrising triples as above, for which the d-dimensional CQ-representation Fx
corresponding to each of the closed points x are elements of S. For each such x
there is a short exact sequence
0 → F ′
x → Fx → F ′′
x → 0
and our condition is equivalent to asking that F ′
x and F ′′
x are in S, since S deﬁnes
a Serre property. So we have
MS
d′,d′′ ∼
= X S
d′,d′′ /Gd′,d′′
where
X S
d′,d′′ := Xd′,d′′ ∩ X S
d .
A tuple ζ = (ζi)i∈Q0 ∈ HQ0
+ := {r exp(+√
−1πφ ) ∈ C | r > 0, 0 <φ ≤ 1}Q0 ⊂
CQ0 provides a Bridgeland stability condition , as deﬁned in [6], with central charge
deﬁned on ﬁnite-dimensional CQ-modules
Z :ρ ↦→ζ · dim(ρ) =
∑
i∈Q0
ζi dim(ρi).
We deﬁne the slope of a nonzero representation ρ by setting
Ξζ (ρ) :=
{
−ℜe(Z(ρ))/ℑm(Z(ρ)) if ℑm(Z(ρ)) ⁄= 0
∞ if ℑm(Z(ρ)) = 0 .
Likewise we deﬁne Ξ ζ (d), for d ∈ NQ0 \ {0}, to be the slope of any representation
ρ of dimension d. A CQ-representation ρ is called ζ-semistable if for all proper
submodules ρ′ ⊂ ρ we have Ξ ζ (ρ′) ≤ Ξζ (ρ), and is ζ-stable if instead we have
Ξζ (ρ′) < Ξζ (ρ) for every proper submodule. To simplify notation in what follows,
we will assume that all representations satisfy Ξ ζ (ρ) < ∞ in this paper. In other
words, we choose our Bridgeland stability conditions to belong to
{r exp(+
√
−1πφ ) ∈ C | r > 0, 0 <φ < 1}Q0 ⊂ HQ0
+ .
We deﬁne two pairings on ZQ0 :
(d, e) :=
∑
i∈Q0
di ei −
∑
a∈Q1
ds(a) et(a)
and
⟨d, e⟩ := (d, e) − (e, d).
Note that ( d, d) = − dim Md.
As in the introduction, for every µ ∈ (−∞, ∞) we denote by Λζ
µ ⊂ NQ0 the
submonoid of dimension vectors d which are either zero, or have slope µ with
respect to the stability condition ζ.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 27
Deﬁnition 3.1. We say ζ is µ -generic if d, e ∈Λζ
µ implies ⟨d, e⟩ = 0 . We say ζ
is generic if it is µ -generic for all µ .
We say that ζ is a King stability condition if ℑm(ζi) = 1 and ℜe(ζi) ∈ Q for all
i ∈ Q0. Given a King stability condition ζ, we can ﬁx m ∈ N such that mℜe(ζi) ∈ Z
for every i. We linearize the Gd-action on Xd via the trivial line bundle on Xd and
the character
χ d : Gd → C∗(39)
(gi)i∈Q0 ↦→
∏
i∈Q0
det(gi)mℜe(ζ i ),
and deﬁne Xζ -ss
d to be the variety of semistable points with respect to this lin-
earization. By [27], using the constructions and deﬁnitions of [36], th e GIT quo-
tient Xζ -ss
d / /χ dGd provides a coarse moduli space of ζ-semistable representations of
dimension d, which we denote Mζ -ss
d . Similarly we deonote by Mζ -ss,S
d the scheme
Xζ -ss,S
d / /χ dGd, and we denote by
(40) ˜ ωζ
d : Mζ -ss,S
d → Mζ -ss
d
the natural inclusion.
Remark 3.2. Fix a dimension vector d ∈ NQ0 of slope µ , for a µ -generic stability
conditionζ. Then we can always ﬁnd a µ ′-generic King stability condition ζ′ such
that a d-dimensional CQ-module is ζ-stable if and only if it is ζ′-stable, by [12,
Lem.4.21], where µ ′ is the slope of d with respect to ζ′. By construction, a d-
dimensional CQ-module isζ′-semistable if and only if it is ζ-semistable. We deduce
that for every µ -generic Bridgeland stability condition ζ and every dimension vector
d of slope µ , there is a coarse moduli space Mζ -ss
d of d-dimensional ζ-semistable
CQ-modules.
Remark 3.3. Pick a rational slope µ ∈ (−∞, ∞). Then we can deﬁne a maximally
degenerate stability King condition, for which every CQ-module is automatically
semistable, by ﬁxing ζi = +√
−1−µ for all i ∈ Q0. In this case we have Λζ
µ = NQ0 ,
and M = Mζ -ss
µ . As a result, all the results in this paper in which we do not as sume
that we are working with a generic stability condition apply to the case in which
we do not impose any stability condition. In addition, those results in which we
do impose a genericity assumption on ζ apply to the case in which we impose no
stability condition and Q is symmetric, since in this case maximally degenerate
stability conditions are still generic in the sense of Deﬁni tion 3.1.
We write Md for the coarse moduli space, taken with respect to the above
degenerate stability condition. Then explicitly
Md = Spec
(
Γ(X(Q)d)Gd
)
and the closed points of Md are in bijection with isomorphism classes of d-dimensional
semisimple CQ-representations.
For a slope µ , we deﬁne
(41) Mζ -ss,S
µ =
∐
d∈Λ ζ
µ
Mζ -ss,S
d
and
(42) Mζ -ss,S
µ =
∐
d∈Λ ζ
µ
Mζ -ss,S
d .
28 BEN DA VISON AND SVEN MEINHARDT
We denote by
(43) pζ ,S
d : Mζ -ss,S
d → Mζ -ss,S
d
and
(44) pζ ,S
µ : Mζ -ss,S
µ → Mζ -ss,S
µ
the maps from the stacks to their respective coarse moduli space s, and by
(45) qζ ,S
d : Mζ -ss,S
d → M S
d
and
(46) qζ ,S
µ : Mζ -ss,S
µ → M S
µ
the maps to the subschemes of points in the union of the aﬃnizations Mµ corre-
sponding to representations in S. Deleting all superscripts S in the above deﬁnitions
we obtain morphisms pζ
d, qζ
d etc.
If d′, d′′ ∈Λζ
µ for some µ ∈ (−∞, ∞), we denote by Mζ -ss,S
d′,d′′ the stack of short
exact sequences as in (38) such that dim( ρ′) = d′, dim(ρ′′) = d′′ andρ ∈ S . There
is an isomorphism of stacks
Mζ -ss,S
d′,d′′ ∼
=
(
Xd′,d′′ ∩ Xζ -ss,S
d′ + d′′
)
/Gd′,d′′.
