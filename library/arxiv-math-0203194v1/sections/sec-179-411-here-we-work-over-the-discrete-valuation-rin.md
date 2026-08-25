---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-179-411-here-we-work-over-the-discrete-valuation-rin
section_title: "Here, we work over the discrete valuation ring v = W = ˆ"
section_number: 4.1.1
pages: 87-89
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
Zur
p (the
completion of the maximal unramiﬁed extension of Zp), with uniformizing
parameter̟ =p. Recall that Nil v denote the category of locally noetherian
v-schemesS on which p is locally nilpotent.
Let
Λ be a ﬁxed p-divisible group over k = Fp. The following theorem
is due to M. Rapoport and T. Zink [ RZ96, 2.16, 2.32].
Theorem 4.1.2. The functor
Nilv→ Sets
S↦→
{
(Λ ,ρ )
⏐
⏐
⏐ Λ : p-divisible group on S,
ρ∈ qisog(Λ ×SSred,
Λ ×FpSred)
}/
∼
=
is representable by a formal scheme M over v; Mred is locally of ﬁnite type
over
Fp and its irreducible components are projective Fp-varieties.
Of course, the rigidity of p-divisible groups up to isogeny (2.2.3) is crucial
here. The main diﬃculty in proving 4.1.2 is to control the pow ers of p which
are needed in the process of lifting isogenies.
The separated formal scheme M is not formally smooth in general, but
has been conjectured to be ﬂat over v. The group J of self-quasi-isogenies of
Λ acts (on the right) on M by (Λ ,ρ ).j = (Λ ,ρ◦j). This group J is actually
the group of Qp-points of an algebraic group over Qp.
We denote byM the Berkovich analytic space over Cp attached to M :
M = Man ˆ⊗K Cp (cf. 3.5). This is a paracompact (strictly) analytic space.
We shall see later that it is smooth, and a p-adic manifold in the sense of
I.1.3.7.
4.2. Examples.
We take
Λ = A[p∞], the p-primary torsion of an elliptic curve A over
Fp (h = 2).
4.2.1. The ordinary case , i.e. A[p](Fp)⁄= 0.
Then Λ ∼
= ˆGm⊕ Qp/Zp, and J = (GmQp)2. For any (Λ ,ρ ) in M(S), the
separable rank of Ker[ p] is constant (due to the quasi-isogeny ρ). Therefore
Λ is an extension
ˆΛ → Λ → Λ et.
The quasi-isogeny ρ respects this extension, hence splits into two parts
(ˆρ,ρ et). We have ˆΛ ∼
= ˆGm, Λ et ∼
= Qp/Zp. Up to isomorphism, the pair
84 II. INTRODUCTION TO THE THEORY OF p-ADIC PERIOD MAPPINGS.
(ˆρ,ρ et) thus amounts to an element of ( Q×
p/Z×
p )2∼
= Z2. Therefore
M =
∐
Z2
M0
is a disjoint sum of copies of a formal (group) scheme M0 which parametrizes
extensions of Qp/Zp by ˆGm. It is known that
M0 = ˆGm
This identiﬁcation is given by the following recipe. Recall that if S =
Spec(R), R local artinian with residue ﬁeld
Fp and radical m (mn+1 = 0),
then ˆGm(S) = 1 + m; in particular ˆGm(S) is killed by [ pn]. Let us choose
any lift qn of 1/pn∈ Qp/Zp in Λ. Then [ pn]qn is a well-deﬁned element q in
ˆΛ( S)∼
= 1 + m, which is unchanged if n is replaced by a bigger integer (but
another choice of the isomorphism ˆΛ ∼
= ˆGm would changeq intoqa, a∈ Z×
p ).
As a formalW -scheme, M0 = Spf( v[[q−1]]), with the (p,q−1)-adic topology.
The associated analytic space M0 over Cp is the open unit disc |q− 1|< 1.
The parameterq is thus the local modulus for deformations of
A[p∞]. On
the other hand, if p⁄= 2, we have an algebraic local modulus for deformations
of A (say, with level two structure): the Legendre parameter z =λ around
the Legendre parameter ζcan of the canonical lifting Acan of A (cf. I.3.4.2).
The p-divisible group Acan[p∞] splits: its parameter is q = 1. Therefore,
in this special case, the Serre-Tate theorem 2.2.4 asserts t hat q∈ 1 + (z−
ζcan)ˆZur[[z−ζcan]]. It has been proved by W. Messing and N. Katz that q is
the Dwork-Serre-Tate parameter discussed in I.3.4, ([ Mes76], [ Ka81]) —
which explains the terminology.
4.2.2. The supersingular case , i.e. A[p](Fp) = 0.
In this case Λ = ˆΛ is a so-called Lubin-Tate formal group, End Λ = Bp,
“the” maximal order in the (non-split) quaternion algebra Bp over Qp, and
J =B×
p .
Here again, there is a discrete invariant: the “height” of th e quasi-isogeny
ρ, which amounts to the p-adic valuation of the norm of its image in J =B×
p .
Therefore
M =
∐
Z
M0
is a disjoint sum of copies of a formal scheme M0 which parametrizes de-
formations of the Lubin-Tate group ˆΛ. According to Lubin-Tate, M0 ∼
=
Spf(v[[t]]), with the ( p,t )-adic topology. The associated analytic space M0
over Cp is the open unit disc |t|< 1.
Assume for simplicity that
A is deﬁned over Fp. Then one can describe
the universal formal deformation Λ over Spf Zp[[t]] through its logarithm
