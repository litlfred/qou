---
doc_id: arxiv-math-0104249v1
doc_title: "Irrationality of values of the zeta-function"
section_id: sec-014-3-analitiqeskaꦪ-konstrukciꦪ-zafiksiruem-poloжite
section_title: "Analitiqeskaꦪ konstrukciꦪ. Zafiksiruem poloжitelьnye neqet-"
section_number: 3
pages: 10-12
source_pdf: 0104249v1.pdf
source_sha256: c2fcdefc73b8df24
doc_brief: "Irrationality of values of the zeta-function — 21 sections: W. ZUDILIN; Introduction. The irrationality of; Main results. In this note we gene"
---
nye parametry a,b,c , c /greaterorequalslant3 i a > b(c − 1), i dlꦪ kaжdogo celogo poloжi-
telьnogo nۈ
R(t) = Rn(t) :=
(
(t ± (n + 1)) · · ·(t ±cn)
) b
(
t(t ± 1) · · ·(t ±n)
) a · (2n)!a+b−bc
= (−1)n ·
( sinπt
π
) b
· Γ( ±t +cn + 1)bΓ(t −n)a+b
Γ(t +n + 1)a+b · (2n)!a+b−bc,
(3)
gde znak ‘ ±t mnoжiteli, otve-
wie kak znaku ‘ +’, tak i ‘ −’. Postavim v sootvetstvie funkcii (3)
summu
I =In :=
∞∑
t=n+1
1
(b − 1)!
db−1R(t)
dtb−1 ; (4)
rꦪd v pravo/ishort qasti(4)tno, poskolьku R(t) = O(t−2) pri
t → ∞ۈ3) v vide summy proste/ishortxih drobe/ishort i is-
qaem, qto
I =
∑
s neqetno
b<s<a+b
Asζ(s) −A0 (5)
IRRACIONALЬNOSTЬ ZNAQENI/Ishort DZETA-FUNKCII 11
(sm. (10) dalee), gde znamenateli racionalьnyh qisel As = As,n rastut ne
bystree qem зksponencialьno (sr. [R1, lemmy 1, 5 ]). Oboznaqim qerez Dn
naimenьxee obwee kratnoe qisel 1, 2,...,n ; iz asimptotiqeskogo zakona
raspredeleniꦪ prostyh qisel
lim
n→∞
logDn
n = 1.
Lemma 1. Dlꦪ kaжdogo neqetnogo c /greaterorequalslant3 suwestvuet posledovatelьnostь
celyh Π n = Π n,c /greaterorequalslant1, n = 1, 2,... , takaꦪ, qto qisla Π −b
n Da+b−1
2n As,ntsꦪ
celymi i spravedlivo predelьnoe sootnoxenie
̟c := lim
n→∞
log Π n,c
n = −
(c−1)/ 2∑
l=1
(
2ψ
( 2l
c − 1
)
+ 2ψ
( 2l
c
)
+ 2c − 1
l
)
+ 2(c − 1)(1 −γ),
(6)
gde γ ≈ 0.57712 – postoꦪnnaꦪ З/ishortlera, a ψ(x) – logarifmiqeskaꦪ proizvodnaꦪ
gamma-funkcii.
Dokazatelьstvo. Poloжim
Π n =
∏
√
(c+1)n<p⩽ 2n
pν p, gde νp = min
k=0, ±1,..., ±n
{
ordp
(cn +k)! (cn −k)!
(n +k)!c(n −k)!c
}
. (7)
Togda dlꦪ racionalьnyh funkci/ishort
G(t) = Gn(t) := (t ± (n + 1)) · · ·(t ±cn)
(
t(t ± 1) · · ·(t ±n)
) c−1 , H (t) = Hn(t) := (2n)!
t(t ± 1) · · ·(t ±n)
qeniꦪ
Π −1
n · Dj
2n
j!
dj
dtj
(
G(t)(t +k)c−1) ⏐
⏐
⏐
⏐
t=−k
∈ Z, Dj
2n
j!
dj
dtj
(
H(t)(t +k)
) ⏐
⏐
⏐
⏐
t=−k
∈ Z,
k = 0, ±1,..., ±n, j = 0, 1, 2,...
(8)
qeni/ishort(8) dlꦪ funkcii G(t) ispolьzuet obobwenie ari-
ۈ3)
v vide R(t) = G(t)bH(t)a+b−bc i primenꦪꦪ pravilo Le/ishortbnica dlꦪ differen-
qeniꦪm (8) poluqaem
Π −b
n Dj
2nBk,j ∈ Z, gde Bk,j = 1
j!
dj
dtj
(
R(t)(t +k)a) ⏐
⏐
⏐
⏐
t=−k
,
k = 0, ±1,..., ±n, j = 0, 1,...,a − 1.
(9)
qeniꦪ Π −b
n Da+b−1
2n As ∈ Z, tak kak
As = (−1)b−1
( s − 1
b − 1
) n∑
k=−n
Bk,a +b−s−1, s neqetno, b<s<a +b,
A0 = (−1)b−1
n∑
k=−n
k+n∑
l=1
(( a +b − 2
b − 1
) Bk, 0
la+b−1 + · · · +
( b
b − 1
) Bk,a −2
lb+1 + Bk,a −1
lb
)
.
(10)
