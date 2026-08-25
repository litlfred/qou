---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-116-721-proposition-on-a
section_title: "Proposition. On a"
section_number: 7.2.1
pages: 38-39
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
tr(F ) =
p∏
k=1
tk.
D´emonstration. Soitβ∈ Sn. D’apr` es (7.5) et (7.2), on a
tr(βσ−1β−1◦ (fβ(1)•···• fβ(n)))
=tr(β◦σ−1◦ (f1•···• fn)◦β−1)
=tr(σ−1◦ (f1•···• fn)).
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 39
Cette formule permet de se ramener au cas o` u lesIk forment une partition crois-
sante de{1,...,n } :
Ik ={ℓ1 +··· +ℓk−1 + 1,...,ℓ 1 +··· +ℓk}
et o` u, de plus, pour toutk,σk est le cycle “croissant”
σk = (ℓ1 +··· +ℓk−1 + 1,··· ,ℓ 1 +··· +ℓk).
Posant alors
Fk =σ−1
k ◦ (fℓ1+···+ℓk−1+1•ots•fℓ1+···+ℓk )
une it´ eration de la formule (7.4) donne
tr(F ) =
p∏
k=1
tr(Fk).
Ceci ram` ene la d´ emonstration de la proposition 7.2.1 au cas o` uσ est la permu-
tation cyclique de{1,...,n }. Par it´ eration de la formule (6.4), et compte tenu de
(6.1) et (6.13), on trouve
(7.8) ι−1
A1A1(fn◦···◦ f1)
= (1A∨
1
•εA2···• εAn• 1A1)◦ (ι−1
A1A2f1•···• ι−1
AnA1fn)
= (1A∨
1
•εA∨
n•···•A∨
2
• 1A1)◦ (ι−1
A2•···•An•A1,A2•···•An•A1F ).
En appliquantεA∨ “aux deux facteurs extrˆ emesA∨ etA” (ce qui fait sens grˆ ace
au tressage), on obtient
(7.9) tr(fn◦···◦ f1) = εA∨
1•A∨
n•···•A∨
2
(ι−1
A2•···•An•A1,A2•···•An•A1F )
=εA∨
1•A∨
n•···•A∨
2
(ι−1
A2•···•An•A1,A2•···•An•A1F )
=εA∨
n•···•A∨
1
(ι−1
A1•···•An,A1•···•An(σ◦ (f1•···• fn))) = tr(σ◦ (f1•···• fn))
(cf. aussi [14, 7.2]). □
