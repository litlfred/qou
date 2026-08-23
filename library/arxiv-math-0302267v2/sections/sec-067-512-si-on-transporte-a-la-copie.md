---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-067-512-si-on-transporte-a-la-copie
section_title: "Si on transporte ` a la copie ∏"
section_number: 5.12
pages: 59-60
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
1,0 de ∏ la loi de groupe de Vω, on obtient une nouvelle
loi de groupe ◦ sur le sch´ ema∏ . Elle est donn´ ee par
(5.12.1) a ◦ b = a · ⟨a⟩0 (b).
En eﬀet, ⟨b⟩1,0 envoie 1 1,0 ∈ ∏
1,0 sur b et ⟨a⟩1,0 envoie b = 1 1,0 · b ∈ ∏
1,0 sur a · ⟨a⟩0 (b).
Prenant l’espace tangent ` a l’origine, on d´ eduit de 5.11 unisomorphisme de pro-espaces
vectoriels de Lie Vω avec L
∧
. Transportons ` a L
∧
l’action de Lie Vω d´ eduite de l’action de
Vω sur la structure 5.9. D´ erivant (5.11.4), on trouve que a ∈ L
∧
agit sur L
∧
= Lie
( ∏
0,0
)
par
(5.12.2) ∂a: e0 ↦− →0, e ζ ↦− →[−[ζ](a), eζ] .
L’action sur ∏
00 s’en d´ eduit. Il est clair sur (5.12.2) que∂e1 = 0. Puisque le centralisateur
de e1 dans L
∧
est r´ eduit aux multiples de e1 (4.7), le noyau de a ↦→∂a est r´ eduit ` aQe1.
Pour ´ ecrire l’action de LieVω = L
∧
tant sur ∏
00 que sur le ∏
00-torseur ∏
1,0, il est
commode de plonger ces sch´ emas aﬃnes dans le dual de leur alg ` ebre aﬃne, un sch´ ema
provectoriel dont ils sont le sous-sch´ ema des ´ el´ ements groupaux. A la structure de groupe
de ∏
0,0 correspond une structure d’alg` ebre sur ce dual, ` a celle de ∏
0,0-torseur de ∏
0,1
une structure de module ` a droite sous cette alg` ebre:
∏
0,1 : torseur sous ∏
0,0 , ´ el´ ements groupaux de
∩ ∩
Q ≪ e0, (eζ) ≫ : module ` a droite sur Q ≪ e0, (eζ) ≫ .
Si Q[ε] est l’alg` ebre des nombres duaux ( ε2 = 0), l’action de a ∈ L
∧
= Lie( Vω)
est le coeﬃcient de ε dans l’action du Q[ε]-point 1 + aε de Vω. L’action sur l’alg` ebre
Q ≪ e0, (eζ) ≫, duale de O(∏
0,0), est e0 ↦→e0, eζ ↦→(1 + [ ζ]aε)−1eζ(1 + [ ζ]aε), et
correspond ` a l’action de a par la d´ erivation ∂a: e0 → 0, eζ ↦→ −[[ζ]a, eζ]. L’action sur le
module ` a droite Q ≪ e0, (eζ) ≫, dual de O(∏
0,1), est par x ↦→(1 + aε)(x + ∂ax · ε) et
correspond ` a l’action de a par
(5.12.3) x ↦− →ax + ∂ax.
Au crochet de Lie de Lie Vω correspond un nouveau crochet de Lie { , } sur L
∧
.
57
Proposition 5.13. On a
(5.13.1) {a, b} = [a, b] + ∂a(b) − ∂b(a).
Preuve. V´ eriﬁons d’abord que
(5.13.2) [ ∂a, ∂b] = ∂[a,b]+∂a(b)−∂b(a).
Puisque, comme ∂a et ∂b, la d´ erivation [∂a, ∂b] de L
∧
ﬁxe e0 et est µN -´ equivariante, il suﬃt
de tester son action sur e1. On a
∂a∂b: e1 ↦− → −[b, e1] ↦− → −[∂a(b), e1] + [b, [a, e1]]
∂b∂a: e1 ↦− → −[a, e1] ↦− → −[∂b(a), e1] + [a, [b, e1]]
[∂a, ∂b]: e1 ↦− → −[∂a(b) − ∂b(a) + [a, b], e1].
Deux m´ ethodes pour d´ eduire (5.13.1) de (5.13.2):
a. Le crochet { , } est compatible aux graduations, toutes les constructions f aites ´ etant
compatibles ` a l’action de Gm. Le noyau de l’action de L
∧
= Lie( Vω) sur L
∧
´ etant r´ eduit
aux multiples de e1, si a et b sont homog` enes (de degr´ e≥ 1), il r´ esulte de (5.13.2) que les
deux membres de (5.13.1) co ¨ ıncident ` a un multiple de e1 pr` es. Etant homog` ene de degr´ e
≥ 2, ils co ¨ ıncident.
b. Testons sur (5.12.3). Si µa est la multiplication ` a gauche par a, on a
[µa + ∂a,µb + ∂b] = µ[a,b]+∂ab−∂ba + [∂a, ∂b]
= µ[a,b]+∂ab−∂ba + ∂[a,b]+∂ab−∂ba.
