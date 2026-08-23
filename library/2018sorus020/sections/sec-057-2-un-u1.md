---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-057-2-un-u1
section_title: "Un =U−1"
section_number: 2
pages: 75-76
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
n
d
dt(Unρ′
2U−1
n )(Unρ′
2
−1U−1
n )Un
= (d
dtρ′
2 +U−1
n
d
dtUnρ′
2 +ρ′
2
dU−1
n
dt Un)ρ′
2
−1
= (d
dtρ′
2)ρ′
2
−1 + 1
tn (ρ′
2Nρ′
2
−1−N)
where the matrixN is ( 1 0
0 0 ). Observe then that the last term on the right is the
boundary ofN0 =N− 1
2 Id, and the ﬁrst assertion follows. The second is clear.
For the third point, the naturality of the Mayer-Vietoris sequence and the exact
sequence of a pair provide the following diagram.
H1(Σ, Ad◦ρ) H2(M, Ad◦ρ)
H1(∂Σ, Ad◦ρ) H2(∂M, Ad◦ρ) H0(∂M, Ad◦ρ)∗
δ
∼
As the second vertical arrow is an isomorphism, it’s enough to compute the compo-
sition H1(Σ, Ad◦ρ)→ H1(∂Σ, Ad◦ρ)→ H2(∂M, Ad◦ρ)→ k(Y ), which is simply
λ↦→ Tr(λ([∂Σ])H).
74
Now each term of the sequence can be thought as anOv-module tensorized byk(Y ),
but the mapd2 does not restrict to a morphism ofOv-module. Hence in the sequel
we will consider the exact sequenceHt :
0→k(Y )
d1
− →H1(M1, Ad◦ρ1)⊕H1(M2, Ad◦ρ′
2)
tn.d2
− −− →H1(Σ, Ad◦ρΣ)
δ
− →k(Y )→ 0
where we just have multiplied d2 by tn. We will denote by D2 this new map,
which restricts to morphism ofOv-modulesH1(M1, Ad◦ρ1)v⊕H1(M2, Ad◦ρ′
2)v
D2
−→
H1(Σ, Ad◦ρΣ)v.
From now on we suppose that the choices of bases we madehΣ,h 1 and h2 gave
splittings H1(M1, Ad◦ρ1)⊕H1(M2, Ad◦ρ′
2) = ker d2⊕E1, and H1(Σ, Ad◦ρΣ) =
d2(E1)⊕E2. Let ∆2 be the restricted mapD2|E1
:E1→d2(E1).
Lemma 2.4.7.
tor(Ht) = 1
det ∆2
c, withc∈O∗
v
Proof. Considering the deﬁnition of the torsion of Section 1.5.3, the following equa-
lity holds :
tor(Ht) = det(d1 :k(Y )→d1(k(Y ))) det(δ :E2→k(Y ))
det ∆2
Then we conclude the proof noting that the numerator lies inO∗
v.
Hence we are now reduced to computev(det(∆2)).
To do this, the idea is the following : recall that the completion of the valuation ring
Ov is isomorphic tok[[t]], the ring of formal series. Consider a matrixA∈M n(Ov)
as a formal seriesA =∑tiAi, withAi∈M n(k), the problem is to compute the
valuation of its determinant. IfdetA0⁄= 0, then A is invertible, detA∈O ∗
v and
v(detA) = 0. If not, we havekn A0
−→kn which is not invertible and deﬁneH0(A0) =
kerA0, H1(A0) = cokerA0, henceH0(A0)≃H1(A0)⁄= 0. PickP,Q∈ GLn(k) such
thatPA 0Q =
( 0 0
