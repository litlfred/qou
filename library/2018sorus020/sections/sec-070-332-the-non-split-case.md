---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-070-332-the-non-split-case
section_title: "The non-split case"
section_number: 3.3.2
pages: 96-100
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
In this section we prove the following theorem :
95
Theorem (Theorem 3.0.2, the non-split case). Let x∈ ˆX be an ideal point in the
smooth projective model of a componentX of the character variety, that produces
an incompressible surfaceS in M which is a union of parallel copiesS1∪...∪Sn of
a Seifert surface. Then the torsion functiontor(M,ρ ) has a pole atx, in particular
it is non-constant.
In this section we assume that the incompressible surface associated tox is a union
of parallel Seifert surfaces. Recall from Section 1.3.7 that we ﬁx a base-pointp∈
S1, and that we identifyπ1(S) with π1(S1). We have the following splittingM =
H∪S1∪SnV (S), whereV (S) is a neighborhood ofS homeomorphic toS1×[0, 1] with
∂V (S) = S1∪Sn. We identify as wellπ1(V (S)) with π1(S). Givenα : π1(S1)→
π1(Sn), one can write the fundamental group ofM as an HNN extensionπ1(M) =
⟨π1(H),v | vγv−1 =α(γ),∀γ∈π1(S)⟩.
We denote byρ1 : π1(S)→ SL2(Ov) the restriction of ρ to π1(S), and by ρn :
π1(Sn)→ SL2(k(X)) its restriction toπ1(Sn) =vπ1(S)v−1, hence we deﬁneρn(γ) =
Vnρ1(γ)V−1
n forγ∈π1(S). The splitting above induces the following exact sequence
of twisted complexes :
0→C∗(M,ρ )→C∗(H,ρH)⊕C∗(S,ρ 1)→C∗(S,ρ 1)⊕C∗(S,ρn)→ 0
The following proposition recaps the series of lemmas in Section 3.3.1, we refer to
the corresponding lemmas for proofs, that translate in exactly the same way here.
We use the isomorphismH1(S,ρn)→H1(S,ρ 1), Z↦→Un ( 0 1
−1 0 )Z.
Proposition 3.3.9. The vanishing order of the torsion at the ideal pointx∈ ¯X is
given by computing−v(detθ), where the isomorphismθ is given by
θ :H1(H,ρH)⊕H1(S,ρ 1)→H1(S,ρ 1)⊕H1(S,ρ 1)
(Z1,Z 2)↦→ ((Z1−Z2)|S,Un ( 0 1
−1 0 ) (Z1−Z2)|S)
Since we want to show thatv(detθ)> 0, we focus on the residual map; it is of the
form
¯θ :H1(H, ¯ρH)⊕H1(S, ¯ρS)→H1(S, ¯ρS)⊕H1(S, ¯ρS)
(z1,z 2)↦→ (z1|S−z2|S,−
(
0
x1|S−x2|S
)
)
96
where zi =
(
xi
yi
)
. We show that it has a non trivial kernel.
Lemma 3.3.10.The kernel of the map
ψ :H1(H, ¯ρH)→H1(S, ¯ρS)
z1↦→
(
0
−x1|S
)
has dimensiond> −χ(S).
Proof. The relationρn = Vnρ1V−1
n implies that the residual representation¯ρ1 has
the form, forγ∈π1(S), ¯ρ1(γ) =
(
λ(γ) 0
∗ λ−1(γ)
)
. Hence we have the exact sequence
0→H1(S,λ−1)→H1(S, ¯ρ1)→H1(S,λ )→ 0
We denote byρ′
1 :π1(S)→ SL2(Ov) the representationρ′
1(γ) = ( 0 1
−1 0 )ρ1(γ) ( 0−1
1 0 ),
and the mapψ is the composition
H1(H, ¯ρH)→H1(S, ¯ρ′
1)→H1(S,λ )≃H1(S,λ−1)→H1(S, ¯ρ1)
(
x
y
)
→
(
x|S
y|S
)
→x|S→
(
0
x|S
)
We show that the compositionH1(H, ¯ρH)→H1(S,λ−1) is not surjective, and it is
enough to prove the lemma by a count of dimensions.
To see that it is not surjective, notice that it factors through the composition
H1(H, ¯ρH)→ H1(∂H, ¯ρ∂H)→ H1(S, ¯ρ′
1). Now we have the exact sequence of the
pair (∂H,S ) :
0→C∗(∂H,S ;ρ∂H)→C∗(H,ρ∂H)→C∗(S,ρ′
1)→ 0
hence the long exact sequence in cohomology provides
H1(∂H, ¯ρ∂H)→H1(S, ¯ρ′
1)→H2(∂H,S, ¯ρ∂H)→ 0
but by excision,H2(∂H,S, ¯ρ∂H)≃ H2(∂S× [0, 1],∂S, ¯ρ∂S), the latter isH0(∂S×
[0, 1], ¯ρ∂S) by Poincaré-Lefschetz duality, which isH1(∂S, ¯ρ∂S).
We deduce the diagram :
97
H1(H, ¯ρH)
H1(∂H, ¯ρ∂H)
H1(S, ¯ρ1)H1(S,λ ) H1(S,λ−1)
H1(∂S, ¯ρ∂S) H1(∂S,k )
0
0
0
F
We conclude because the commutativity of the diagram and the exactness of the
vertical arrows imply that the mapF cannot surjective.
Proof of Theorem 3.0.2.We prove that the map residual map¯θ is not an isomor-
phism, hence its determinant vanishes and it proves the theorem. To see that we
show that it is not surjective, in particular the map
H1(H, ¯ρH)⊕H1(S, ¯ρS)→H1(S, ¯ρS)
(z1,z 2)↦→−
(
0
x1|S−x2|S
)
is not surjective : the ﬁrst part of the map has rank strictly less than−χ(S) by
Lemma 3.3.10, and the second part has rank−χ(S). It proves the theorem.
98
Annexe A
Proof of Saito’s theorem
Let us recall the statement of the theorem. The proof we present here is adapted
from an unpublished version of [Sai94].
Theorem A.0.1.LetR be ak-algebra, andχ :B[Γ]→R an R-character. Assume
thatχ is irreducible, that isχ(∆α,β)∈R× for someα,β ∈ Γ, and letA,B∈ SL2(R)
such that TrA =χ(Yα), TrB =χ(Yβ), TrAB =χ(Yαβ). Then there exists a unique
representation ρ : Γ → SL2(R) whose character is χ and such that ρ(α) = A,
ρ(β) =B.
In the sequel we will denote byφ : Γ→R the mapφ(γ) =χ(Yγ).We ﬁrst introduce
the following deﬁnition :
Deﬁnition A.0.2.An R-valued form is a map h : Γ → R such that∀γ,δ ∈
Γ,h (γδ) +h(γδ−1) =φ(γ)h(δ). A form will be calledhomogeneous if h(e) = 0.
Remark A.0.3.By the trace formula, the mapφ is a (non-homogeneous) form. If
h is a homogeneous form, then clearlyh(γ) +h(γ−1) = 0, hence
h(γδ) +h(δγ) =φ(γ)h(δ) +φ(δ)h(γ) (A.1)
Lemma A.0.4.Leth be a homogeneous form, denote byVh ={γ∈ Γ :h(γ) = 0}.
Then the following holds :
1.∀γ∈Vh,∀n∈ Z,γn∈Vh.
2.∀δ∈Vh,∀γ∈ Γ,h (γδ) =h(δ−1γ).
