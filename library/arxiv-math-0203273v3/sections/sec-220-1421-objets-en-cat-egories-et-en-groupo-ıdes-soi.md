---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-220-1421-objets-en-cat-egories-et-en-groupo-ıdes-soi
section_title: "Objets en cat ´egories et en groupo ¨ıdes. SoitX une cat´ egorie avec limites"
section_number: 14.2.1
pages: 81-82
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
projectives ﬁnies. Rappelons qu’un objet en cat ´egories dansX est la donn´ eeΓ de
deux objetsE,S ∈X , d’un morphisme
(β,σ ) : E→S×S
“but” et “source” et d’un morphisme “loi de composition”
◦ :E×βSσ E→E
telles que, pour tout objet X∈X , le couple (X (X,E ),X (X,S )) et les morphis-
mes correspondants d´ eﬁnissent une petite cat´ egorieΓ(X) (objets :S(X) ; morphis-
mes :E(X)). Par le lemme de Yoneda, cela revient ` a exiger queβ,σ,◦ v´ eriﬁent les
identit´ es habituelles. Un objet en cat´ egoriesΓ est un objet en groupo¨ıdes si, pour
toutX∈X , Γ(X) est un groupo¨ ıde (mˆ eme remarque).
Si Γ = ( E,S,β,σ, ◦) et Γ′ = (E′,S′,β′,σ′,◦′) sont deux objets en cat´ egories
deX , un morphisme de Γ vers Γ′ est un couple T = (f,g ), avec f ∈X (E,E′),
82 YVES ANDR ´E ET BRUNO KAHN
g∈X (S,S′), tels que les diagrammes
E
(β,σ)
−−−−→S×S
f


↓ g×g


↓
E′ (β′,σ′)
−−−−→S×S
E×βSσ E ◦−−−−→E
f×f


↓ f


↓
E′×β′ S′σ′ E′ ◦′
−−−−→E′
soient commutatifs (ou, de mani` ere ´ equivalente, queT (X) : Γ( X)→ Γ′(X) soit
un foncteur pour toutX∈X ).
SiT = (f,g ) etT′ = (f′,g′) sont deux tels morphismes, une homotopie deT
versT′ est un morphismeu∈X (S,E′) tel que les diagrammes
S u−−−−→E′
(g′,g)ց (β′,σ′)


↓
S′×S′
E
(f,uβ )
−−−−→E′×β′ S′σ′ E′
(uσ,f ′)


↓ ◦′


↓
E′×β′ S′σ′ E′ ◦′
−−−−→ E′
soient commutatifs (ou, ce qui revient au mˆ eme, queu(X) soit une transformation
naturelle quel que soitX∈X ).
Les objets en cat´ egories, morphismes et homotopies d´ eﬁnissent une 2-cat´ egorie
Cat(X ). Sa sous-cat´ egorie1-pleine et 2-pleine form´ ee desobjets en groupo¨ ıdes est
not´ eeGr(X ).
