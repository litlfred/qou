---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-080-3c-constructions-des-nouvelles-réalisations
section_title: "3C. Constructions des nouvelles réalisations"
section_number: null
pages: 115-117
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
en combinant les constructions de la sous-section 2E avec la (−1)-connexité des complexes AK , AK, B et
AK,𝓁 . On rappelle que K est de caractéristique nulle et qu’on ne fait pas d’hypothèses sur la caractéristique
de k. On ﬁxe une Q-algèbre3.
Déﬁnition 3.14. Fixons un morphisme d’anneaux3→ K . La nouvelle réalisation de type de Rham sur
RigDA´et(ˆK;3) est le foncteur
Rnew: RigDA´et(ˆK;3)→ D(AK) (3-17)
déﬁni comme étant la composition de
RigDA´et(ˆK;3)
RK
(2-49)
// Ho(Mod(AK))
AK⊗AK−
(3-8)
// D(AK) (3-18)
où RK est le foncteur de l’exemple 2.36 ; voir la remarque 3.11. La nouvelle réalisation de type de Rham
sur DA´et(k;3) est le foncteur
Rnew◦ rel: DA´et(k;3)→ D(AK). (3-19)
Les deux foncteurs (3 -17) et (3-19) sont monoïdaux. Lorsque cela n’entraîne pas confusion, on écrit
« Rnew » au lieu de « R new◦ rel ».
Remarque 3.15. Les réalisations nouvelles de type de Rham permettent de retrouver la réalisation de
de Rham surconvergente sur RigDA´et(ˆK;3) ainsi que la réalisation rigide à la Berthelot sur DA´et(k;3).
Plus précisément, on a des triangles commutatifs
RigDA´et(ˆK;3)
Rnew //
RdR **
D(AK)
ˆK⊗AK−

D(ˆK)
et DA´et(k;3)
Rnew //
RBert ))
D(AK)
ˆK⊗AK−

D(ˆK)
(3-20)
à isomorphismes naturels près. Ceci découle aussitôt des triangles (2 -51) et (2 -60). Les réalisations
nouvelles de type de Rham permettent aussi de retrouver les réalisations 𝓁-adiques, pour𝓁 différent de la
caractéristique de k. Plus précisément, en ﬁxant certaines données comme dans la remarque 2.39, on a
1782 Joseph Ayoub
également des triangles commutatifs
RigDA´et(ˆK;3)
Rnew //
Q𝓁⊗Q𝓁 R𝓁 **
D(AK)
Q𝓁⊗AK−

D(Q𝓁)
et DA´et(k;3)
Rnew //
Q𝓁⊗Q𝓁 R𝓁 ))
D(AK)
Q𝓁⊗AK−

D(Q𝓁)
(3-21)
à isomorphismes naturels près.
Déﬁnition 3.16. (1) On ﬁxe un plongement complexeσ: K↪→ C. On déﬁnit les nouvelles réalisations
de type Betti
Rnew, B: RigDA´et(ˆK;3)→ D(AK, B) et R new, B◦ rel: DA´et(k;3)→ D(AK, B) (3-22)
en remplaçant « RK », « AK » et « AK » par « RK, B », « AK, B » et « AK, B » dans la déﬁnition 3.14.
(2) On ﬁxe une clôture algébrique K/K , un nombre premier𝓁 et un morphisme d’anneaux3→ Q𝓁.
On déﬁnit les nouvelles réalisations de type𝓁-adique
Rnew,𝓁: RigDA´et(ˆK;3)→ D(AK,𝓁) et R new,𝓁◦ rel: DA´et(k;3)→ D(AK,𝓁) (3-23)
en remplaçant « RK », « AK » et « AK » par « RK,𝓁 », « AK,𝓁 » et « AK,𝓁 » dans la déﬁnition 3.14.
Lorsque cela n’entraîne pas confusion, on écrit « Rnew, B/𝓁 » au lieu de « R new, B/𝓁◦ rel ».
Remarque 3.17. Soit𝓁 un nombre premier différent de la caractéristique de k et ﬁxons une clôture
algébrique de ˆK (ce qui détermine une clôture algébrique de K ). Fixons aussi un morphisme d’anneaux
3→ Q𝓁. Alors les nouvelles réalisations de type 𝓁-adique permettent de retrouver les réalisations
𝓁-adiques sur RigDA´et(ˆK;3) et DA´et(k;3). Plus précisément, on a des triangles commutatifs
RigDA´et(ˆK;3)
Rnew,𝓁 //
R𝓁 **
D(AK,𝓁)
Q𝓁⊗AK,𝓁−

D(Q𝓁)
et DA´et(k;3)
Rnew,𝓁 //
R𝓁 **
D(AK,𝓁)
Q𝓁⊗AK,𝓁−

D(Q𝓁)
(3-24)
à isomorphismes naturels près. Ceci découle aussitôt des triangles (2-57) et (2-61).
Remarque 3.18. Les nouvelles réalisations introduites dans les déﬁnitions 3.14 et 3.16 se comparent
entre elles. En effet, sous les hypothèses de la remarque 2.39, on a une chaîne de quasi-isomorphismes
C⊗K AK≃ C⊗3 AK, B≃ Q𝓁⊗3 AK, B≃ Q𝓁⊗Q𝓁 AK,𝓁 (3-25)
ainsi qu’une chaîne d’isomorphismes naturels
C⊗K Rnew(−)≃ C⊗3 Rnew, B(−)≃ Q𝓁⊗3 Rnew, B(−)≃ Q𝓁⊗Q𝓁 Rnew,𝓁(−) (3-26)
entre foncteurs déﬁnis sur RigDA´et(ˆK;3). Ceci découle aussitôt de (2-58) et (2-59).
Nouvelles cohomologies de Weil en caractéristique positive 1783
