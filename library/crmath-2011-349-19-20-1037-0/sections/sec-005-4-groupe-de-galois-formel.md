---
doc_id: crmath-2011-349-19-20-1037-0
doc_title: "Classification analytique et théorie de Galois locales des modules aux q-différences à pentes non entières"
section_id: sec-005-4-groupe-de-galois-formel
section_title: "Groupe de Galois formel"
section_number: 4
pages: 3-3
source_pdf: CRMATH_2011__349_19-20_1037_0.pdf
source_sha256: fd5bd0558dfe892f
toc_source: outline
doc_brief: "Classification analytique et théorie de Galois locales des modules aux q-différences à pentes non entières — Van der Put and Reversat described the form of a pure q-difference module with non"
---
Van der Put et Reversat ont décrit dans [2] le groupe de Galois formel des équations aux q-différences sur ˆK du point de
vue algébrique, en tant qu’extension de Picard–Vessiot. Nous donnons ici, une description matricielle explicite de ce groupe
dans le but d’avoir une description explicite de son effet sur les Stokes (sur lesquels il opère par conjugaison).
Le groupe de Galois des équations aux q-différences G(0) est déﬁni dans [7], et plus généralement dans [3], par voie
tannakienne (cf. [1]), comme l’ensemble des automorphismes tenseur-compatibles d’un foncteur ﬁbre ωz0, z0 ∈C∗. Dans [3],
le groupe de Galois pur (ou formel) G(0)
p,1 des équations aux q-différences à pentes entières est décrit explicitement : G(0)
p,1 =
C∗× Homgr(Eq,C∗) × C.
Ici, on ﬁxe r ∈N∗le dénominateur des pentes des modules aux q-différences sur ˆK et on note G(0)
p,r le groupe de Galois
associé. Un objet de cette catégorie est somme directe de modules du type E(s,t,b) ⊗Um de pente k
r = s
t (pgcd(t, s) = 1).
Le théorème suivant décrit l’action de G(0)
p,r sur les modules irréductibles E(r,d,br) de matrice B associée (déﬁnie dans 1).
On ﬁxe donc r ∈N∗, également z0 ∈C∗, une racine re de z0 notée z1/r
0
, ξr = e2iπ/r racine primitive re de l’unité et qr une
racine re de q. Pour tout groupe abélien E, on note E∨le groupe proalgébrique Hom(E,C∗). On note également diag pour
matrice diagonale.
Théorème 4.1. Soit ϕ ∈G(0)
p,r. Alors ϕ = (t,γ ,λ) où t ∈C∗, γ ∈E∨
q et λ ∈C et on a
ϕ(B) = G−1
b,d

z1/r
0

tdγ (b)γ (Tr) diag

1,γ (qr),...,γ (qr)r−1dGb,d

z1/r
0

,
où
Gb,d

z1/r
0

= diag(1,α0,α0α1,...,α0 ···αr−2),
α j = b−1q−jd
r
z−d/r
0
et
Tr =
⎛
⎝
0
1
0
...
1
1
0...
0
⎞
⎠∈GLr(C).
La loi de groupe est alors : (t,γ ,λ)(t′,γ ′,λ′) = (tt′ε(γ ,γ ′),γ γ ′,λ + λ′) où ε(γ ,γ ′) =
1
γ ′(γ (qr)) = ξ−lk′
r
si γ (qr) = ξl
r et
γ ′(ξr) = ξk′
r .
Le groupe de Galois G(0)
p,r est alors égal à Hr × C où 1 →C∗→Hr →E∨
q →1 est une extension centrale. On retrouve
de manière explicite le résultat de van der Put et Reversat qui aﬃrme que le groupe de Galois formel des équations aux
q-différences G(0)
p
est égal à H × C où 1 →Q∨→H →E∨
q →1 est une extension centrale.
