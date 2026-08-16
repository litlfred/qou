---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-176-112-complexe-de-hochschild-mitchell-soita-une-pe
section_title: "Complexe de Hochschild-Mitchell. SoitA une petiteK-cat´ egorie, telle que"
section_number: 11.2
pages: 59-60
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
pour tout (A,B )∈A×A ,A(A,B ) soit unK-module projectif.
NotonsC∗(A) le complexe de Hochschild deA [38,§17] : c’est un complexe de
Ae-modules tel que
Cm(A)(A,B)=
⨁
A0,...,Am
A(A,A0)⊗KA(A0,A1)⊗K···⊗KA(Am−1,Am)⊗KA(Am,B), m ≥0
o` u(A0,...,A m) d´ ecrit lesn-uplets d’objets deA. La diff´ erentielle est
dm(f0⊗f1⊗···⊗ fm+1) =
m∑
i=0
(−1)if0⊗f1⊗···⊗ fifi+1⊗···⊗ fm+1.
Il est connu queC∗(A) est une r´ esolution projective duAe-moduleA.
Pour tout Ae-module M, on note C∗(A,M ) le complexe de K-modules
HomAe(C∗(A),M ). Plus concr` etement, pour m > 0, un ´ el´ ement de
C m(A,M )(A,B ) ´equivaut ` a la donn´ ee d’un ´ el´ ement deM (A,B ) pour chaque
m-uplet de ﬂ` eches composables(f1,...,f m),f1 ´ etant de sourceA etfm de butB,
cette donn´ ee ´ etantK-multilin´ eaire en(f1,...,f m) ; pour m = 0 , c’est la donn´ ee
d’un ´ el´ ement deM (A,A ) pour toutA.
V oici comment : on obtient une telle donn´ ee en consid´ erant , dans
HomAe(C∗(A),M )(A0,A m) le facteur correspondant ` aA = A0,f 0 = 1 A0,B =
Am,f m = 1 Am. R´ eciproquement, une telle donn´ ee fournit une cochaˆ ıne de
Hochschild grˆ ace ` a la commutativit´ e du carr´ e (bivariance en (A,B )) :
HomAe(C∗(A),M )(A,B ) −−−−→M (A,B )
(f0,fm+1)


↓ (f0,fm+1)


↓
HomAe(C∗(A),M )(A0,A m) −−−−→M (A0,A m).
60 YVES ANDR ´E ET BRUNO KAHN
Avec cette interpr´ etation, la diff´ erentielle de Hochschild prend la forme habituelle
(dmϕ)(f1,...,f m+1) = f1ϕ(f2,...,f m+1)
+
m∑
1
(−1)iϕ(f1,...,f ifi+1,...,f m+1)
+ (−1)m+1ϕ(f1,...,f m)fm+1.
PuisqueC∗(A) est une r´ esolution projective duAe-moduleA, on a
H i(A,M ) := H i(C∗(A,M )) = Ext i
Ae(A,M ).
SiA est s´ eparable,Ae est semi-simple, donc ces groupes de cohomologie sont
donc
nuls pour toutM et touti> 0 (cf. lemme 11.1.2 et proposition 2.1.2).
La formation de C∗(A) est naturelle en A. Plus pr´ ecis´ ement, toutK-foncteur
F : A → B donne lieu ` a des applications K-lin´ eairesCn(A)(A,B ) →
Cn(B)(FA,FB ), et, pour toutBe-moduleN, ` a un homomorphisme de complexes
deK-modules dans l’autre sens
C∗(B,N )→C∗(A,F∗N ).
