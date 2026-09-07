---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-057-2-there-is-a-functorial-morphism-ψ-πr-homgr
section_title: "There is a functorial morphism ψ : πR Homgr"
section_number: 2
pages: 32-32
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
˜A ( ˜M, ˜N ) → R HomA(π ˜M,π ˜N ).
Fixing ˜N these are way-out right contravariant functors of ˜M . By [RD] Proposition
I.7.1(iv) – reversed – it’s enough to check that ψ is an isomorphism when ˜M = ˜A,
and then it’s trivial.
Proof of Theorem 6.2. 1. By Proposition 4.8 and the graded version of Corollary
3.6 each cohomology module H q ˜R is k[t]-central (cf. Remark 6.6 below). Deﬁne
˜Rt := ˜At ⊗ ˜A ˜R ⊗ ˜A ˜At ∈ D(GrMod( ˜At)e).
We see that the homomorphisms ˜At ⊗ ˜A ˜R → ˜Rt and ˜R ⊗ ˜A ˜At → ˜Rt are quasi-
isomorphisms.
Because ˜A →A =π ˜A is ﬂat we also have
A ⊗ ˜A ˜R[−1] ∼= ˜R[−1] ⊗ ˜AA ∼=R ∈ D(Mod ˜Ae).
Considering only ˜A-modules we have R ∼=π ˜R[−1], so by Lemma 6.2, R has ﬁnite
injective dimension and ﬁnitely generated cohomologies over A. By symmetry this
is true also over A◦. Part 3 of the lemma implies that R Hom A(R,R ) ∼= π ˜A = A,
and likewise R HomA◦ (R,R ) = A. We conclude that R is dualizing.
Now let’s prove R is rigid. There is a functorial isomorphism π ˜M ∼= ( ˜Mt)0 for
˜M ∈ GrModk[t], and the algebra Ae is Z2-graded. Therefore we get
Ae ⊗ ˜Ae ( ˜R ⊗ ˜R) ∼= (A ⊗ ˜A ˜R) ⊗ ( ˜R ⊗ ˜AA) ∼= ( ˜Rt)0 ⊗ ( ˜Rt)0 ∼= ( ˜Rt ⊗ ˜Rt)(0,0).
The algebra ( ˜At)e is strongly Z-graded, and its degree 0 component is
( ˜At)e
0 ∼=Ae[s,s −1] ∼=k[s,s −1] ⊗Ae
where s :=t ⊗t−1. Applying ( ˜At)e ⊗ ˜Ae − to
˜R ∼= R Homgr
˜Ae ( ˜A, ˜R ⊗ ˜R)
we obtain
˜Rt ∼= R Homgr
( ˜At)e( ˜At, ˜Rt ⊗ ˜Rt)
and taking degree 0 components we get
R[1] ∼= R Homgr
( ˜At)e
0
(A, ( ˜Rt ⊗ ˜Rt)0)
∼= R Homk[s,s−1]⊗Ae(A,k [s,s −1] ⊗ (R[1] ⊗R[1])).
But
k ∼=
(
k[s,s −1]
s−1
− − →k[s,s −1]
)
∈ D(Modk[s,s −1]),
and A is a ﬁnitely presented Ae-module, so
R Homk[s,s−1]⊗Ae(k ⊗A,k [s,s −1] ⊗M ) ∼= R HomAe (A,M )[−1]
for any complex of Ae-modules M .
