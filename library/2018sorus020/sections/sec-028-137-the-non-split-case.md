---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-028-137-the-non-split-case
section_title: "The non-split case"
section_number: 1.3.7
pages: 37-39
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
Let S be an incompressible surface associated to an ideal pointv∈ ˆX which is,
again, union ofn parallel copiesS =S1∪... ∪Sn, and we assume now thatM\Si
is connected. Hence[Si] = 0∈ H2(M;∂M ), and in particular∂Si is a homological
longitude. We say thatSi is aSeifert surfaceinM. LetV (Si) be a neighborhood of
36
Si in M, andE(Si) = M\V (Si). It is a classical fact (see [Oza01, Proposition 2])
that E(Si) is a handlebody if and only ifπ1(E(Si)) is free. In this case we say that
the surfaceSi is free. It is the case, for instance, as soon asM is small (does not
contain any closed incompressible surfaces), and a necessary and suﬃcient condition
for a knot to contain non-free Seifert surfaces is given in [Oza00].
In the sequel we assume that the Seifert surfaceSi is free, say of genusg, and we
denote byH =E(Si) the genus 2g handlebody complement ofSi. We assume that
∂V (S) = S1∪Sn. We haveM = V (S)∪S1∪Sn H, hence the HNN decomposition
π1(M) = π1(H)∗α, where we ﬁx the basepointp∈ S1, and α : π1(S1)→ π1(Sn)
an isomorphism between those subgroups ofπ1(M). This means that we have the
presentationπ1(M) =⟨π1(H),v | vγv−1 =α(γ),∀γ∈π1(S1)⟩.
Lemma 1.3.16. One can chose a conjugate of the tautological representationρ :
π1(M)→ SL2(k(X)) such that the restrictionsρH : π1(H)→ SL2(k(X)) and ρ1 :
π1(S1)→ SL2(k(X)) are convergent. Moreover,ρ(v) = Vn with Vn =
(
0 tn/2
−t−n/2 0
)
,
in particularn is an even integer, and the restrictionρn : π1(Sn)→ SL2(k(X)) is
equal toVnρ1V−1
n . Finally, the residual restricted representation¯ρ1 is reducible, with
Tr(¯ρ1(∂Si)) = 2.
Proof. We ﬁx a vertexs in the Bass-Serre treeT, that corresponds to the latticeO2
v
and is ﬁxed byπ1(H), henceρH is convergent. We denote bye1 the edge in the tree
T incident tos that is ﬁxed byπ1(S1), and the parallel copies ofS1 stabilize a series
of edgesei that form a segment inT, which hasUn·s1 as an end point, as depicted
below.
s1 ... Un·s1
e1 e2 en
In particular, the representation¯ρ1 is reducible by the same argument that in the
proof of Lemma 1.3.15. Now the elementv ∈ π1(M) acts on the tree T in the
following way : it sends the vertexs1 to Un·s1, but it sends the incident edgee1 to
en. Since it acts by isometries, the only possibility is to act as a central rotation with
center the mid-point of the segment[s1Un·s1]. But the fundamental groupπ1(M)
acts without inversion, hencen is even, andρ(v) is of the formUn
2
RπU−1
n
2
= Vn,
where Rπ = ( 0 1
−1 0 ).
The last statement follows from [CCG+94], where it is proven that the eigenvalues of
the matrix ¯ρ1(∂Σ1) are roots of unity, of order that divides the number of boundary
37
components of any surfaceΣi, hence those eigenvalues are equal to 1, and it achieves
the proof.
