---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-190-1341-la-construction-de-mac-lane36-xi-3-a-toute
section_title: "La construction de Mac Lane[36, XI 3]. `A toute petite cat´ egorie mono¨ ıdale"
section_number: 13.4.1
pages: 67-67
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
(A,•), on associe une petite cat´ egorie mono¨ ıdale stricte(Astr,⊤), et deux foncteurs
mono¨ ıdauxB
u→
←v
A, avecu strict, tels que le compos´ euv soit le foncteur mono¨ ıdal
identique deA (les foncteurs sous-jacents ` au etv sont donc quasi-inverses).
Rappelons cette construction : on prend pour objets deAstr les mots (ﬁnis) dont
les lettres sont les objets de A. Les morphismes entre mots sont les morphismes
entre les objets de A correspondants obtenus par parenth´ esage canonique (toutes
les parenth` eses commencent au d´ ebut du mot). Le produit⊤, souvent omis de la
notation, est donn´ e au niveau des objets par la concat´ enation des mots ;v est donn´ e
par la “formation de mots d’une lettre”, tandis queu est donn´ e par le “parenth´ esage
canonique” (e.g.u(ABC ) = (A•B)•C)). L’unit´ e est le mot vide :u(∅) = 1.
C’est uneK-cat´ egorie siA l’´ etait, etu,v sont alors desK-foncteurs.
Noter que lorsque A estK-lin´ eaire, la constructionA⊕ est un cas particulier de
cette construction, en prenant• =⊕.
Si s :B → Aest un foncteur, on lui associe canoniquement comme suit un
foncteur mono¨ ıdal strictsstr :Bstr→A str : on associe au mot w =B1...B n de
Bstr le motsstr(w) = s(B1)...s (Bn) deAstr (sstr(∅) =∅).
On associe ` af∈B str(w,w′) =B(u(w),u (w′)) le morphismesstr(f ) = s(f )∈
A(u(sstr(w)),u (sstr(w′))) =Astr(sstr(w),s str(w′)).
Si s est sous-jacent ` a un foncteur mono¨ ıdal strict, on ausstr = su (donc s =
uA◦sstr◦vB).
Vu la construction de Mac Lane et le sorite 13.3.3, pour d´ emontrer le th´ eor` eme
13.2.1, on peut supposerA stricte. Le th´ eor` eme 13.2.1 r´ esulte alors de la proposition
plus pr´ ecise suivante :
