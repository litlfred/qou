---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-205-1363-lemme-il-existe-une-famille-double-ur
section_title: "Lemme. Il existe une famille double (u(r)"
section_number: 13.6.3
pages: 74-76
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
A )A∈A,r≥1, avecu(r)
A ∈ 1 +R(A),
ayant les propri´et´es suivantes :
(i) u(r+1)
A ≡u(r)
A (modR(A)r) pour toutA∈A et toutr≥ 1.
(ii) s′(f ) = u(r)
A s(f )(u(r)
A )−1 pour toutA∈A , toutf∈ ¯A(A) et toutr≥ 1.
(iii) u(r)
A•B≡u(r)
A •u(r)
B (modR(A•B)r) pour tous objetsA,B et toutr≥ 1.
Le lemme 13.6.3 implique b) de la mˆ eme mani` ere que les lemmes 13.6.1 et 13.6.2
impliquaient c) et a). On proc` ede toujours par r´ ecurrencesurr. Nous aurons besoin
des nouvelles notations suivantes, pour un mot w en les objets de A (voir aussi
§13.6.7) :
Cs(w) ={x∈A (
•
w)|xs(f ) = s(f )x pour toutf∈ ¯A(w)}
C r
s (w) =R(
•
w)r∩Cs(w)
C [r](w) = C r
s (w) +R(
•
w)r+1
R(
•
w)r+1
≃C r
s (w)/Cr+1
s (w).
Le groupe C [r](w) ne d´ epend pas du choix de s, puisque deux sections sont
conjugu´ ees par des ´ el´ ements de1 +R (th´ eor` eme 12.1.1 b)) et que1 +R op` ere
trivalement surR[n] par conjugaison. On prendra garde de ne pas le confondre avec
le groupeC(w)[r] du§13.6.7 : l’inclusion
C [r](w)⊂C(w)[r]
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 75
est en g´ en´ eral stricte.
En utilisant le th´ eor` eme 12.1.1 b), choisissons une famille (u(1)
A )A∈A, avecu(1)
A ∈
1A +R(A), v´ eriﬁent la propri´ et´ e (ii) du lemme 13.6.3. La condition (iii) est automa-
tique ; le lemme est donc vrai pourr = 1.
Supposons maintenantr≥ 1 et le lemme connu pourr. Posons
nA,B := 1A•B− (u(r)
A •u(r)
B )−1u(r)
A•B∈R (A•B)r.
Commes ets′ sont mono¨ ıdales strictes, on a l’identit´ e
(u(r)
A •u(r)
B )−1u(r)
A•B(s(f )•s(g))(u(r)
A•B)−1u(r)
A •u(r)
B =s(f )•s(g)
pour (f,g )∈ ¯A(A)× ¯A(B), ce qui ´ equivaut ` a
nA,B∈C r(AB).
Par ailleurs, la d´ eﬁnition denA,B donne imm´ ediatement la relation
1A• ¯nB,C− ¯nA•B,C + ¯nA,B•C− ¯nA,B• 1C = 0
o` u¯nA,B d´ esigne l’image denA,B dansC [r](AB).
Soit maintenant (u(r+1)
A ) une famille v´ eriﬁant les conclusions du lemme 13.6.3.
Posons
u(r+1)
A =u(r)
A (1 +mA).
On a doncmA∈R (A)r. La condition (ii) du lemme se traduit en
(1 +mA)s(f )(1 +mA)−1 =s(f )
pour toutf∈ ¯A(A), c’est-` a-dire
mA∈C r(A).
La condition (iii), d’autre part, se traduit en
¯nA,B = ¯mA•B− 1A• ¯mB− ¯mA• 1B
o` u¯mA est la projection de mA dans C [r](A) (calcul imm´ ediat). Inversement, la
donn´ ee demA∈R (A)r v´ eriﬁant ces deux conditions fournit une famille(u(r+1)
A )
v´ eriﬁant les conclusions du lemme 13.6.3.
On termine comme pr´ ec´ edemment, en utilisant leK⟨Ob(A)⟩-bimodule
C [r] =
∏
w
C [r](w),
et en posant
¯nw0,w1(w) =
{
¯n •
w0,
•
w1
siw0w1 =w,
0 sinon.
Ceci conclut la preuve de b), donc celle de la proposition 13.4.2, et ﬁnalement celle
du th´ eor` eme 13.2.1. □
13.6.4. Remarques.
76 YVES ANDR ´E ET BRUNO KAHN
a) SupposonsA ab´ elienne et engendr´ ee par un nombre ﬁni d’objetsAi, au sens
o` u tout objet est sous-quotient d’une somme ﬁnie de copies de•-monˆ omes
en ces objets. On prendra garde que ¯A n’est pas n´ ecessairement engendr´ ee
par lesπ(Ai) = Ai. Le point est que l’image dans ¯A d’un monomorphisme
deA n’est pas n´ ecessairement un monomorphisme. En fait, on verra plus
loin des exemples o` u¯A n’est engendr´ ee par aucun ensemble ﬁni d’objets.
b) Dans [1], nous appliquons le th´ eor` eme de scindage mono¨ ıdal ci-dessus pour
construire, inconditionnellement, des r´ ealisations de motifs num´ eriques, et
les groupes de Galois motiviques associ´ es.
c) Dans la quatri` eme partie de ce travail, nous appliquons le mˆ eme th´ eor` eme
pour d´ eﬁnir des “enveloppes” pro-semi-simples ou pro-r´ eductives.
13.7. Variantes. V oici un avatar mono¨ ıdal de la proposition 12.2.1.
