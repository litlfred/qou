---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-023-51-local-parameters-and-change-of-curve
section_title: "Local parameters and change of curve"
section_number: 5.1
pages: 39-41
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Consider h ⊂sln+1(C) the Cartan subalgebra of diagonal matrices, in particular
a diagonal matrix in PSL n+1(C) lies in exp h.
For a generic character χ ∈X0(M 3, PSLn+1(C)), one would like to consider
in a neighborhood U of χ:
logγ∶ U ⊂X0(M 3, PSLn+1(C)) → h
χρ ↦ log ρ(γ) (39)
but a priori this may not be well deﬁned. Notice that there are indet erminacies
due to the action of the Weyl group (permutation of elements in the diagonal)
and indeterminacies due to the complex logarithm. This motivates the following
deﬁnition.
Deﬁnition 5.10. A representation ρ ∈hom(π1M 3, PSLn+1(C)) is chamber reg-
ular is there exists a peripheral element γ ∈π1T 2 such that ρ(γ) has n + 1
diﬀerent eigenvalues.
In terms of Lie groups this is a regularity condition: ρ(π1T 2) is contained
in a Cartan subgroup and in the interior of the Weyl chamber of PSL n+1(C).
By [60], the symmetric functions on the eigenvalues of ρ(γ) deﬁne a local
biholomorphism in a neighborhood of ̺n, hence all eigenvalues of ρ(γ) are dif-
ferent in a Zariski open set. Thus:
Remark 5.11. The set of chamber regular characters is a non-empty Zariski
open subset of X0(M 3, PSL2(C)).
For a chamber regular character and a peripheral element γ ∈π1T 2, there
exist a neighborhood U ⊂X0(M 3, PSLn+1(C)) such that the logarithm log γ as
in (39) is deﬁned in U . Notice that the eigenvalues of the image of γ do not
need to be diﬀerent, provided that there is an element in the periphe ral group
with diﬀerent eigenvalues.
Next consider a nonzero element a ∈h. Using the Killing form, we deﬁne
a⋆ ∈h to be the pairing with a.
Lemma 5.12. Let ρ be a chamber regular representation, γ a peripheral curve
and a ∈h. Viewing H1(M 3; Adρ) as cotangent space:
a ∩ [γ] = d(a⋆ logγ). (40)
This must be compared with [82, Lemma 3.20]. Before proving this lemm a,
let us discuss its consequences.
39
Proposition 5.13. Let χρ ∈X0(M 3, PSLn+1(C)) be a chamber regular charac-
ter and γ a peripheral curve. Then TM,γ (χρ) ≠0 if and only if χρ is a scheme
reduced smooth point of X0(M 3, PSLn+1(C)) and logγ is a local parameter.
The proof follows easily from Lemma 5.12, and we just sketch it. Name ly,
the condition of being scheme reduced and smooth is equivalent to sa ying that
dim H 1(M 3; Adρ) = n. By the standard arguments of the long exact sequence
of the pair (M 3, T 2) this implies that dim H 0(T 2; Adρ) = n and that {a1 ∩
[T 2], . . . , an ∩ [T 2]} is a basis for H 2(M 3; Adρ). Then Lemma 5.12 yields that
{a1 ∩ [γ], . . . , an ∩ [γ]} is a basis for H 1(M 3; Adρ) iﬀ log γ is a local parameter.
For a chamber regular character, the condition of Proposition 5.13 is equiv-
alent to the notion of γ-regularity of [55, Deﬁnition 3.2].
Notice ﬁnally that for any non-trivial peripheral curve γ, for the lift of the
holonomy ̺, even if it is not chamber regular, TM,γ (χ̺n ) ≠0, by [55, Theo-
rem 3.4].
Proposition 5.14. Let γ1, γ2 be two peripheral elements. In a Zariski open
domain in X0(M 3, PSLn+1(C))
T(M,γ1)
T(M,γ2)
= ± J(logγ1 log−1
γ2 ).
Notice that the Jacobian J (logγ1 log−1
γ2 ) is well deﬁned generically on the
distinguished component X0(M 3, PSLn+1(C)), i.e. in a non-empty open Zariski
set, as log γ2 is a local parameter in an open set. In addition, this Jacobian
is independent of the parametrization of h, as any change of parametrization
cancels in the quotient. The proof of Proposition 5.14 is straightfor ward from
Lemma 5.12 and the formula of change of basis in homology (6).
Proposition 5.14 does not cover χ̺n , the character of Sym n of the holonomy
of the complete hyperbolic structure, as it is not chamber regular. However,
Corollary 5.7 and Proposition 4.21(d) yield:
T n+1
M,γ2(χ̺n ) = cs(γ2, γ1)n T n+1
M,γ1(χ̺n ),
where cs (γ2, γ1) denotes the cusp shape (Deﬁnition 3.19).
Proof of Lemma 5.12. Assume that ρ is a generic representation so that ρ(γ)
is diagonal with diﬀerent eigenvalues. Let h denote the Cartan algebra of di-
agonal matrices, and choose a non-zero element a ∈h. In particular a ∩ γ ∈
H1(M 3; Adρ). Consider the dual of a:
a⋆∶ h → C
h ↦ B(a, h)
where B denotes the Killing form. Consider also a ﬁrst order deformation ρt of
ρ, i.e.
ρt = (1 + t ˙ρ + O(t2))ρ (41)
where ˙ρ∶ π1M 3 → sln+1(C) is a group cocycle, that we project to H 1(M 3; Adρ).
Consider ﬁnally the Kronecker pairing
⟨⋅⟩∶ H k(M 3; Adρ) × Hk(M 3; Adρ) → C
40
deﬁned as follows. Let z ∈Ck(M 3; Adρ) be a cocycle, with z∶ Ck(/tild⟩comb.alt1M 3; Z) →
sln+1(C), and let h ⊗ m ∈Ck(M 3; Adρ), where h ∈sln+1(C) and m ∈Ck(/tild⟩comb.alt1M 3; Z).
At the (co-)chain level, the Kronecker pairing is
⟨z, h ⊗ m⟩ = B(h, z(m)) (42)
where B denotes again the Killing form. This induces a non-degenerate pair-
ing between homology and cohomology [82]. After all those preliminarie s, to
establish the lemma one must prove the following equality
⟨ ˙ρ, a ∩ [γ]⟩ = d
dt a⋆ log ρt(γ)/divid⟩s.alt3
t=0
. (43)
To prove (43), start with the group cohomology version of (42) in t he current
context (see [82]):
⟨ ˙ρ, a ∩ [γ]⟩ = B(a, ˙ρ(γ)). (44)
From (41) evaluated at γ and taking logarithms:
log ρt(γ) = log ρ(γ) + t ˙ρ(γ) + O(t2)) . (45)
Then (43) follows from a⋆ applied to (45), then diﬀerentiating and applying (44)
to the result.
Lemma 5.12 may be related to the results of Goldman [35].
Example 5.15 (Volumes on X(K, SU (2))). In [21, 22] Dubois makes a relevant
contribution of torsions as volume form on the variety of characte rs of a knot
in SU (2). Here the Cartan algebra has dimension one and the logarithm of a
matrix in SU (2) is an angle. Dubois volume form is, up to sign,
voltor = ± dϕγ
Tm,γ
where ϕγ denotes the angle of the representation of the peripheral curve γ.
Notice that by Proposition 5.14, this form is independent of the choic e of the
peripheral curve. In [21, 22], using Turaev’s reﬁnement of torsio n and a good
choice of ϕγ, Dubois avoids the sign indeterminacy. He also shows that it
equals to a volume form deﬁned from a Heegaard splitting, ` a la Johns on (Ex-
ample 2.25). This is related to the construction of an orientation on t he space
of representations of Heusener [40].
Proposition 5.14 suggests that a similar volume form can be construc ted for
representations in SU (n + 1), taking a convenient parametrization of the Cartan
algebra (i.e. inﬁnitesimal angles). It remains to know also whether th e variety
of characters of a knot in SU (n+1) is non-empty and n-dimensional. This holds
true for instance for two bridge knots. Another issue is to comput e explicitly
the variety of SU (n + 1) characters for a knot.
