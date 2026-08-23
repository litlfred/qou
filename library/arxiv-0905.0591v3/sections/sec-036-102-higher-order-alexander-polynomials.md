---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-036-102-higher-order-alexander-polynomials
section_title: "Higher order Alexander polynomials"
section_number: 10.2
pages: 32-34
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
are arguably the most interesting examples of φ–compatible homomorphisms from π1(N ) to
a non–commutative Laurent polynomial ring. The ideas of thi s section are due to Cochran
and Harvey.
Theorem 10.2. Let γ be a torsion–free solvable group and let F be a commutative ﬁeld.
Then the following hold.
(1) F[Γ] is an Ore domain, in particular it embeds in its classical rig ht ring of quotients
K(Γ) .
(2) K(Γ) is ﬂat over F[Γ] .
Indeed, it follows from [KLM88] that F[Γ] has no zero divisors. The ﬁrst part now
follows from [DLMSY03, Corollary 6.3]. The second part is a w ell–known property of Ore
localizations. We call K(Γ) the Ore localization of F[Γ]. In [COT03] the notion of a poly–
torsion–free–abelian (PTF A) group is introduced, it is wel l–known that these groups are
torsion–free and solvable.
Remark. (1) It follows from Higman’s theorem [Hi40] that the above th eorem also holds
for groups which are locally indicable and amenable. We will not make use of this,
but note that throughout this section ‘torsion–free solvab le’ could be replaced by
‘locally indicable and amenable’.
(2) Note that the poly–torsion–free–abelian (PTF A) groups introduced in [COT03] are
solvable and torsion–free.
We need the following deﬁnition.
Deﬁnition. Letπ be a group, φ :π → Z an epimorphism and ϕ :π →γ an epimorphism to
a torsion–free solvable group γ such that there exists a map φΓ : Γ → Z (which is necessarily
unique) such that
π
φ /d31/d31/d63/d63/d63/d63/d63/d63/d63/d63
ϕ /d47/d47
Γ
φΓ
/d15/d15
Z
commutes. Following [Ha06, Deﬁnition 1.4] we call ( ϕ,φ ) an admissible pair.
Now let (ϕ :π1(N ) → Γ,φ ) be an admissible pair for π1(N ). In the following we denote
Ker{φ : Γ → Z} by Γ ′(φ). When the homomorphism φ is understood we will write Γ ′
for Γ ′(φ). Clearly Γ ′ is still solvable and torsion–free. Let F be any commutative ﬁeld
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 33
and K(Γ ′) the Ore localization of F[Γ ′]. Pick an element µ ∈ γ such that φ(µ ) = 1. Let
γ : K(Γ ′) → K(Γ ′) be the homomorphism given by γ(a) = µaµ −1. Then we get a ring
homomorphism
Z[Γ] → K(Γ ′)γ[t±1]
g ↦→ (gµ −φ(g)tφ(g)), for g ∈γ.
We denote this ring homomorphism again by ϕ. It is clear that ϕ isφ–compatible. Note that
the ring K(Γ ′)[t±1] and hence the above representation depends on the choice of µ . We will
nonetheless suppress µ in the notation since diﬀerent choices of splittings give iso morphic
rings. We will refer to a non–commutative Alexander polynom ial corresponding to such a
group homomorphism as a higher order Alexander polynomial .
An important example of admissible pairs is provided by Harv ey’s rational derived series
of a group γ (cf. [Ha05, Section 3]). Let γ(0)
r =γ and deﬁne inductively
γ(n)
r =
{
g ∈γ(n−1)
r |gk ∈
[
γ(n−1)
r ,γ (n−1)
r
]
for some k ∈ Z \ {0}
}
.
Note that γ(n−1)
r /γ(n)
r ∼
=
(
γ(n−1)
r /
[
γ(n−1)
r ,γ (n−1)
r
])
/Z–torsion. By [Ha05, Corollary 3.6] the
quotients Γ /γ(n)
r are solvable and torsion–free for any γ and any n. If φ : Γ → Z is an
epimorphism, then (Γ → Γ/γ(n)
r ,φ ) is an admissible pair for (Γ ,φ ) for any n> 0.
For example if K is a knot, γ =π1(S3 \νK ), then it follows from [St74] that Γ (n)
r = Γ (n),
i.e. the rational derived series equals the ordinary derive d series (cf. also [Co04] and [Ha05]).
Remark. The Achilles heel of the higher order Alexander polynomials is that they are
unfortunately diﬃcult to compute in practice. We refer to [S a07] for some ideas on how to
compute higher order Alexander polynomials in some cases.
10.3. Comparing diﬀerent φ–compatible maps. We now recall a deﬁnition from [Ha06].
Deﬁnition. LetN be a 3–manifold with empty or toroidal boundary. We write π =π1(N ).
Let φ : π → Z an epimorphism. Furthermore let ϕ1 : π → γ1 and ϕ2 : π → γ2 be
epimorphisms to torsion–free solvable groups γ1 and γ2. We call ( ϕ1,ϕ 2,φ ) an admissible
triple forπ if there exist epimorphisms ϕ1
2 :γ1 →γ2 andφ2 :γ2 → Z such that ϕ2 =ϕ1
2 ◦ϕ1,
and φ =φ2 ◦ϕ2.
The situation can be summarized in the following diagram
γ1
ϕ1
2
/d15/d15
π
φ /d32/d32/d64/d64/d64/d64/d64/d64/d64/d64
ϕ1
/d62/d62/d126/d126/d126/d126/d126/d126/d126/d126ϕ2 /d47/d47γ2
φ2
/d15/d15
Z.
Note that in particular ( ϕi,φ ),i = 1, 2 are admissible pairs for π. The following theorem
is perhaps the most striking feature of higher order Alexand er polynomials. In light of
Theorem 10.1 the statement can be summarized as saying that h igher order Alexander
polynomials corresponding to larger groups give better bou nds on the Thurston norm.
34 STEF AN FRIEDL AND STEF ANO VIDUSSI
Theorem 10.3. Let N be a 3–manifold whose boundary is a (possibly empty) collect ion
of tori. Let (ϕ1,ϕ 2,φ ) be an admissible triple for π1(N ). Suppose that ∆ ϕ2
N,φ ⁄= 0 , then it
follows that ∆ ϕ1
N,φ ⁄= 0. We write
di := deg(∆ ϕi
N,φ) − deg(∆ ϕi
N,φ,0) − deg(∆ ϕi
N,φ,2),i = 1, 2
Then the following holds:
d1 ≥d2.
Furthermore, if the ordinary Alexander polynomial ∆ φ
N ∈ Z[t±1] is non–trivial, then d1 −d2
is an even integer.
Proof. The fact that ∆ ϕ2
N,φ ⁄= 0 implies that ∆ ϕ1
N,φ ⁄= 0 and the inequality d2 ≥d1 were ﬁrst
proved for knots by Cochran [Co04]. Cochran’s result were th en extended to the case of
3–manifolds by Harvey [Ha06] (cf. also [Fr07]). Finally the fact that d2 −d1 is an even
integer when ∆ φ
N ⁄= 0 is proved in [FK08a]. □
The strong relationship between the Thurston norm and highe r order Alexander polyno-
mials is also conﬁrmed by the following result (cf. [FH07]).
Theorem 10.4. LetN be a 3–manifold with empty or toroidal boundary, let ϕ :π1(N ) →γ
be an epimorphism to a torsion–free solvable group such that the abelianization π1(N ) →
F :=H1(N ; Z)/torsion factors through ϕ. Then the map
H 1(N ; Z) = Hom(F, Z) → Z≥0
φ ↦→ max{0, deg(∆ ϕ
N,φ) − deg(∆ ϕ
N,φ,0) − deg(∆ ϕ
N,φ,2)}
deﬁnes a seminorm on H 1(N ; Z) which gives a lower bound on the Thurston norm.
