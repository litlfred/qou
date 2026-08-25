---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-282-1947-proposition-a-pour-toutg-algebrique-on-a-un
section_title: "Proposition. a) Pour toutG alg´ebrique, on a une suite exacte"
section_number: 19.4.7
pages: 109-110
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
1→ pRed(G0)⊳→ pRed(G)→G/G0→ 1
o`uG0 est la composante neutre deG.
b) SiG est connexe, soitP unK-sous-groupe parabolique deG. Alors pRed(P )→
pRed(G) est ´epi.
c) SiG→H est ´epi, pRed(G)→ pRed(H) est ´epi.
D´emonstration. a) ´EcrivonsG = lim←−Gi, o` u lesGi = G/Ni sont de dimension
ﬁnie : alors, pour tout i,G0
i est l’image deG0 dansGi. Comme le syst` eme desG0
i
est de Mittag-Lefﬂer, on a un diagramme commutatif de suites exactes courtes :
1 −−−−→G0 −−−−→G −−−−→G/G0 −−−−→1
A


↓


↓ B


↓
1 −−−−→lim
←−G0
i −−−−→lim
←−Gi −−−−→lim
←−Gi/G0
i −−−−→1.
Comme KerB est proﬁni et que CokerA est connexe, ce diagramme montre que
A etB sont des isomorphismes. En particulier, on a G0 = lim←−G0/(G0∩Ni), et
N 0
i :=G0∩Ni est de codimension ﬁnie dansG0 et distingu´ e dansG.
Soit maintenant ρ : G0 → GL(V ) une repr´ esentation deG0 (de dimension
ﬁnie) : nous allons montrer qu’elle est isomorphe ` a un facteur direct d’une repr´ e-
sentationW provenant de G. Ceci impliquera que pRed(G0)→ pRed(G) est un
monomorphisme, d’o` u l’´ enonc´ e en appliquant la proposition 19.4.4 et le lemme
19.4.6.
110 YVES ANDR ´E ET BRUNO KAHN
Notons U = Ker ρ : alors U est de codimension ﬁnie dans G0, et d’apr` es ce
qui pr´ ec` ede il existeV ⊂ G0, de codimension ﬁnie et distingu´ e dans G. Notons
Γ 0 =G0/V , de sorte qu’on a une suite exacte
1→ Γ 0→G/V→G/G0→ 1.
Il existe un quotient ﬁni ∆ deG/G0 tel queG/V soit l’image r´ eciproque d’une
extension Γ de ∆ par Γ 0. Ainsi, on s’est ramen´ e au cas o` uG est alg´ ebrique. Dans
ce cas, il sufﬁt de prendre pourW la restriction ` aG0 deInd G
G0V .
b) Grˆ ace au lemme 19.4.6 (i), il sufﬁt de prouver que le foncteur RepK(G)→
RepK(P ) est pleinement ﬁd` ele. SoientV,W deux repr´ esentations deG. Le groupe
G op` ere sur l’espace afﬁneHom(V,W ) via un de ses quotients alg´ ebriquesΓ . Soit
¯P l’image deP dans Γ : c’est un sous-groupe parabolique de Γ . Comme Γ/ ¯P est
propre et connexe, il en r´ esulte queHom G(V,W )→Hom P (V,W ) est surjectif.24
c) Cela r´ esulte encore du lemme 19.4.6 (i). □
19.4.8. Corollaire. Pour toutK-groupe afﬁneG, on a pRed(G0) = ( pRed(G)0)⊳.
D´emonstration. En effet, d’apr` es le lemme 19.4.1,pRed(G0) est connexe, donc
aussi (pRed(G)0)⊳. □
Enﬁn, on a le r´ esultat suivant.
