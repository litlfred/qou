---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-019-432-higher-torsions-on-the-variety-of-characters
section_title: "Higher torsions on the variety of characters"
section_number: 4.3.2
pages: 30-32
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Again assume that M 3 is an oriented hyperbolic 3-manifold of ﬁnite volume
with a single cusp. We deﬁne the Reidemeister torsion on the distinguis hed
curve of characters X0(M 3).
Deﬁnition 4.14. For k1 or k2 odd, with k1 ≠k2, and for χρ ∈X0(M 3) − Ek1,k2,
where E k1,k2 is as in Deﬁnition 4.8, deﬁne
Tk1,k2
M (χρ) =
⎧
⎪
⎪
⎨
⎪
⎪
⎩
tor(M 3, ρk1,k2 ) if ρk1,k2 is acyclic;
0 otherwise.
For k1 and k2 even, with k1 ≠k2, γ a peripheral curve, and χρ ∈X0(M 3)−Fk1,k2
(where F k1,k2 is as in (30)), deﬁne
Tk1,k2
M,γ (χρ) =
⎧
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎩
tor(M 3, ρk1,k2 , {a ∩ γ, a ∩ [T 2]}) if ⟨a ∩ γ⟩ = H1(M 3; ρk1,k2 ),
⟨a ∩ [T 2]⟩ = H2(M 3; ρk1,k2 );
0 otherwise.
30
We also use the notation
Tk
M = Tk,0
M and Tk
M,γ = Tk,0
M,γ
for k odd or even respectively.
The proof of Proposition 3.16 with minor changes yields the following:
Proposition 4.15. For k1 ≠k2, Tk1,k2
M and Tk1,k2
M,γ are nonzero (real) analytic
functions on X0(M 3) − Ek1,k2 for k1 or k1 odd, or X0(M 3) − Fk1,k2 for k1 and
k2 even, holomorphic when k2 = 0 and antiholomorphic when k1 = 0.
When H 1(M 3; Z) ≅Z there is a well deﬁned Alexander polynomial ∆ (t),
and we can give conditions for the regularity of Tk
M and Tk,γ
M on the whole curve
X0(M 3).
Proposition 4.16. Assume that H 1(M 3; Z) ≅Z and that no root of ∆ (t) is a
root of unity. Then for k odd Ek,0 = ∅. Hence for k odd Tk
M is a holomorphic
function on X0(M 3).
Proof. The proof of Proposition 3.16 applies here with a minor modiﬁcation.
Notice that the condition on the homology implies that the trivial char acter
does not lie in X0(M 3). On the other hand, the reducible characters in X0(M 3)
are the characters of the composition of a surjection
π1M 3 → Z
with a representation that maps the generator of the cyclic group to
A = /par⟩nl⟩ft.alt4λ 0
0 λ−1/par⟩nright.alt4
with ∆ (λ2) = 0 [9, 18]. Since λ is not a root of unity and k is odd, Sym k(A) has
no eigenvalue equal to one, hence H 0(M 3; ρk) = 0 for every ρ with character in
X0(M 3).
Proposition 4.17. Assume that M 3 = S3 − K is a knot exterior in the sphere.
Assume also that no root of ∆ (t) is a root of unity and all roots have multiplicity
one. Then for k even, Tk
M,γ can be extended to the whole curve X0(M 3).
Proof. There are two issues to discus: the dimension of H 0(T 2; ρ) and the
vanishing or not of H 0(M 3; ρ). For the ﬁrst one, the assumption M 3 = S3 −
K implies that ρ is never trivial on the peripheral torus T 2. It my happen
that ρ(π1T 2) is non-trivial but Sym k(ρ(π1T 2)) has an invariant subspace of
dimension ≥2. However, this issue only occurs when ρ(π1T 2) is contained in a
1-parameter subgroup G of SL2(C) conjugate to the group of diagonal matrices.
Then Sym k(G) has only one invariant subspace, that varies analytically on ρ.
Thus the element a in the expression of the cup products can be chosen to
depend analytically on ρ.
Next discuss H 0(M 3; ρ). The argument in Proposition 4.16 fails in the case
k even because Sym k has always an invariant subspace, thus for those reducible
representations H 0(M 3; ρk) ≠0 and further discussion on reducible representa-
tions is required. Namely, at a reducible representation, for the co rresponding
abelian representation ρ as in the proof of Proposition 4.16, the hypothesis that
31
λ is not a root of unity implies that Sym k(A) has a single eigenvalue equal to
one, hence dim H 0(M 3; ρk) = 1. The results of [43, 41], and the hypothesis that
the root is simple, yield that there are, up to conjugation, two repr esentations
ρ′ and ρ′′ that are non abelian and have the same character as ρ. In partic-
ular H 0(M 3; (ρ′)k1,k2 ) ≅H 0(M 3; (ρ′′)k1,k2 ) = 0. Now, using the arguments of
Proposition 3.16, we may deﬁne the torsion in a Zariski dense subset of the
component of hom (π1M 3, SL2(C)) that corresponds to X0(M 3). It suﬃces to
consider an open neighborhood of ρ′ for the usual topology that projects to
a neighborhood of χρ [43, 41], which proves that the torsion on a punctured
neighborhood of χρ extends to χρ.
The assertion for the case k = 2 has been proved by Yamaguchi in [107]. More
precisely he computes the precise value of T2
M,γ at the reducible character.
Example 4.18. Some torsion functions are computed here for the ﬁgure eight
knot exterior. Let θ = θm denote the evaluation of a character of a meridian:
θm(χ) = χ(m) (i.e. the trace of a meridian). As mentioned in Example 3.18, in
[51] Kitano computes:
TM = T1
M = 2 − 2θ.
Further computations with the help of symbolic software yield:
T3
M = − /par⟩nl⟩ft.alt1θ2 − 2 θ − 2/par⟩nright.alt1
2
T5
M = 2 (θ − 1) /par⟩nl⟩ft.alt1θ8 + 2 θ7 − 13 θ6 − 20 θ5 + 49 θ4 + 48 θ3 − 33 θ2 − 18 θ − 18/par⟩nright.alt1
T7
M = − (θ − 1)2 /par⟩nl⟩ft.alt12 θ7 − 4 θ6 − 21 θ5 + 19 θ4 + 57 θ3 + 13 θ2 − 18 θ − 6/par⟩nright.alt1
2
T9
M = 2 (θ − 1) /par⟩nl⟩ft.alt1θ12 + 2 θ11 − 13 θ10 − 13 θ9 + 27 θ8 − θ7 + 95 θ6 + 90 θ5
−148 θ4 − 74 θ3 + 61 θ2 + 12 θ − 6/par⟩nright.alt1
2
.
Remark that these torsions are functions on the variable θ = θm, the trace of
the meridian. This is not always the case, for instance for T2
M,γ , computed in
[82] (and in Section 5) and described below. We also computed:
T2,1
M = 13 + 3 θ4 − 3
θ
3
− 14 θ2 − 3 θ
2
+ 13 θ + θ4θ + 4 θ2θ
3
+ 2 θ2θ
2
− 16 θ2θ − θ4θ
3
+ θ4θ
2
+ ηη /par⟩nl⟩ft.alt1θ2θ − θ2 − θ − 1/par⟩nright.alt1
where η is a variable that satisﬁes η2 = (θ2 − 1)(θ2 − 5). This variable can be
written in terms of the traces of other elements, see Equation (49 ).
In subsection 5.2 other torsions are computed. If m and l denote respectively
the meridian and the longitude, by (50), (51), (54):
T2
M,l = 5 − 2θ2, T2
M,m = 1
2 η, and T4
M,l = 8(2 − θ2).
