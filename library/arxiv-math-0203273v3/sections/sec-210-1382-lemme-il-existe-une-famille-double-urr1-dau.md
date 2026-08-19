---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-210-1382-lemme-il-existe-une-famille-double-urr1-dau
section_title: "Lemme. Il existe une famille double (u(r))r≥1 d’automorphismes deIdA,"
section_number: 13.8.2
pages: 77-78
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
avecu(r)
A ∈ 1 +R(A), ayant les propri´et´es suivantes :
(i) u(r+1)
A ≡u(r)
A (modR(A)r) pour toutA∈A et toutr≥ 1.
78 YVES ANDR ´E ET BRUNO KAHN
(ii) vA,B≡ (u(r)
A
−1
•u(r)
B
−1
)u(r)
A•B (modR(A•B)r) pour tous objetsA,B et
toutr≥ 1.
D´emonstration. R´ ecurrence surr, en partant de r = 1 avec u(1) = 1 . Sup-
posons r ≥ 1 et trouv´ ee un automorphisme u(r). Quitte ` a remplacer vA,B par
(u(r)
A •u(r)
B )u(r)
A•B
−1
vA,B, on peut supposer queu(r) = 1 et quev∈R r.
Pour tout motw en les objets deA, posons
C(w) ={x∈A (
•
w)|x centraliseA(w)}
C <r>(w) = C(w)∩R (
•
w)r (r≥ 0)
Γ [r](w) = C <r>(w)/C<r+1>(w)
Γ [r] =
∏
w
Γ [r](w).
L’alg` ebreK⟨Ob(A)⟩ op` ere ` a gauche et ` a droite surΓ [r] de la mani` ere habituelle.
Posons vA,B = 1 −νA,B : alors νA,B ∈ C <r>(AB) et on a la congruence
identique
νA•B,C +νA,B• 1C≡νA,B•C + 1A•νB,C (modR(A•B•C)r+1).
Soit u(r+1) un automorphisme de IdA solution de (i) et (ii). Posons u(r+1)
A =
1−µA : on a donc µA∈ C <r>(A). Soit ¯µA l’image deµA dans Γ [r](A). On a la
congruence identique
νA,B≡µA•B− 1A•µB−µA• 1B (modR(A•B)r+1).
R´ eciproquement, si(µA) est une famille d’´ el´ ements deC <r>(A) v´ eriﬁant ces
congruences, alors la famille (u(r+1)
A = 1 − µA) d´ eﬁnit un automorphisme de
IdA solution de (i) et (ii). Il reste ` a appliquer comme pr´ ec´ edemment la nullit´ e de
H 2(K⟨Ob(A)⟩, Γ <r>). □
