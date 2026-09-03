---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-008-16-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 16
pages: 16-18
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
This computation is similar to the one for quandle 2-cocycles, and it is seen thatϕsatisfies the YB
2-cocycle condition, from the quandle 2-cocycle condition ofψ.□
Lemmas 3.1 and 5.4 imply the following.
Lemma 5.5.Setk=Z[A], whereAis a coefficient abelian group of a quandle 2-cocycleψof a
quandleQ, andVbe a freek-module on whichRis defined. Define the operator
˜R(x⊗y) =R(x⊗y) +ℏϕ(x⊗y) on ˜V=k[[ℏ]/(ℏ 2)⊗V.
Then ˜Ris a YBO on ˜V.
Lemma 5.6.LetQbe a quandle, and forx,y∈Q, letz∈Qbe a unique element such that
z∗x=y. Set ˆϕ(x⊗y) :=−ψ(z⊗x)R −1(x⊗y). ThenR −1 +ℏ ˆϕis the inverse of ˜R.
Proof.We note thatR(z⊗x) = (x⊗y) andR −1(x⊗y) = (z⊗x). Then one computes
(R+ℏϕ)(R −1 +ℏ ˆϕ)(x⊗y) = (R+ℏϕ)[(z⊗x) +ℏ(−ψ(z⊗x)(z⊗x)] =x⊗y.
The other case is similar.□
Lemma 5.7.Let ˜R=R+ℏϕas in Lemma 3.1. Define ˜S= ( ˜R,1,1,˜µ), where˜µ=µ 0 +ℏµ 1 with
µ0 =1andµ 1 = 0. Then ˜Sis an EYBO.
Proof.This follows fromψ(x⊗x) = 0. Since Lemma 5.5 shows that ˜Ris a YBO, we need only to
show that the condition on partial traces (2) is satisfied. For notational clarity, denote bye x the
elements ofVcorresponding toQ, instead of using the letterxdirectly. We denote bye ∗
x the dual
element, defined by⟨e x|e∗
y⟩:=e ∗
y(ex) =δ xy. Then, for each basis vectore x, to compute the partial
trace Tr2( ˜R◦˜µ⊗˜µ) we have
ex 7→
X
y∈Q
ex⊗ey⊗e∗
y
7→
X
y∈Q
[ey⊗ex∗y⊗e∗
y +ℏϕ(ex⊗ey)⊗e ∗
y]
=
X
y∈Q
[ey⊗ex∗y⊗e∗
y +ℏψ(x,y)·e y⊗ex∗y⊗e∗
y]
7→
X
y∈Q
[⟨ex∗y|e∗
y⟩ey +ℏψ(x,y)⟨e x∗y|e∗
y⟩ey]
=e x +ψ(x,x)·e x
=e x,
where we have used the fact thatx∗y=yin a quandle impliesx=y. A similar computation
holds for Tr2( ˜R−1◦˜µ⊗˜µ).□
Lemma 5.7 and Theorem 4.3 imply the following.
Proposition 5.8.The EYBO ˜Sdefined from ˜R=R+ℏϕin Lemma 5.7 defines via trace a YB
2-cocycle invariantΦ ϕ(K) = Φ0
ϕ(K) +ℏΦ 1
ϕ(K)for knotsK.
We now show a relation between quandle 2-cocycle invariants and the YB 2-cocycle invariants
of knots. Then we have the following result.
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 17
Proposition 5.9.We haveΦ 1
ϕ(K) = P
C∈ColQ(D)
P
uϵ(u)ψ(xu,yu), where both summations are
taken ink=Z[A]. Thus we have
Φϕ(K) = Φ0
ϕ(K) +ℏΦ 1
ϕ(K) =|Col Q(D)|+ℏ
X
C∈ColQ(D)
X
u
ϵ(u)ψ(xu,yu),
where|Col Q(D)|denotes the number of coloring ofDbyQ.
Proof.LetCbe a coloring of a diagramDof a knotKby a quandleQ. LetDbe a diagram in
a closed braid form of ann-braidb m ofK. As in the proof of Lemma 5.7, we use a basis ofV
denoted bye x, wherex∈Q, dual basis vectorse ∗
x and the pairing
⟨ex1⊗···⊗e xk|e∗
yk⊗···⊗e ∗
y1⟩=
Y
i
δxiyi.
At a crossing with a coloring pair (x,y) as in Figure 8, the map
˜R(x⊗y) =R(x⊗y) +ℏψ(x⊗y)R(x⊗y)
is assigned, and the composition is taken over all crossings, as in Definition 4.1. For the inverse,
˜R−1(x⊗y) =R −1(x⊗y)−ℏψ(y∗x,y)R −1(x⊗y)
is assigned by Lemma 5.6. More specifically, suppose thatKhas a braid presentation as the closure
ofb m =σ ϵ(i1)
i1 ···σ ϵ(ik)
ik . Recall that we make the assignmentsσ ±
i 7→1⊗(i−1)⊗ ˜R±⊗1⊗(m−i−1). We
consider the terms ofℏ-degree at most one, so that we take the terms where at most one of
the braid generators receive the assignmentσ ±
i 7→1 ⊗(i−1)⊗ ˜R±⊗1⊗(m−i−1) and othersσ ±
i 7→
1⊗(i−1)⊗R±⊗1⊗(m−i−1). Then, Φ 1
ϕ(K) is written as
Φ1
ϕ(K) = Tr(Ψ 1
ϕ(bm))
=
X
x1,...,xm∈Q
⟨Ψ1
ϕ(bm)(ex1⊗···⊗e xm)|e∗
xm⊗···⊗e ∗
x1⟩
=
X
x1,...,xm∈Q
kX
r=1
ϵ(ir)⟨σϵ(ik)
ik ···(1 ⊗(ir−1)⊗ϕ⊗1 ⊗(m−ir−1))···σ ϵ(i1)
i1 (ex1⊗···⊗e xm)
|e∗
xm⊗···⊗e ∗
x1⟩
=
X
x1,...,xm∈Q
kX
r=1
ϵ(ir)ψ(y(r)
ir ,y (r)
ir+1)⟨ey(k)
1
⊗···⊗e y(k)
m
|e∗
xm⊗···⊗e ∗
x1⟩
=
X
C∈ColQ(D)
kX
r=1
ϵ(ir)ψ(y(r)
ir ,y (r)
ir+1),
where we have indicated byy (r)
h the coloring of theh th string after applying the firstroperators
in the braid presentation ofb m, so thaty (k)
ir is the the color of the output of Ψ ϕ(bm). The last
expression represents P
C∈ColQ(D)
P
x∈Cvx(modℏ 2). Since Φ 0
ϕ(K) =|Col Q(D)|without cocycle
contributions in the above computations, we obtain the formula in the statement.□
Remark 5.10.Recall that the quandle cocycle invariant is defined by
ΦQ
ψ (D) =
X
C∈ColQ(D)
Y
u
ψ(xu,yu)ϵ(u).
