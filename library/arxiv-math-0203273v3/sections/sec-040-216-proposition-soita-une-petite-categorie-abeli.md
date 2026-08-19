---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-040-216-proposition-soita-une-petite-categorie-abeli
section_title: "Proposition. SoitA une petite cat´egorie ab´elienne semi-simple, o`uK est un"
section_number: 2.1.6
pages: 16-17
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
corps commutatif. NotonsS(A) (resp I(A),C(A)) l’ensemble des classes d’isomor-
phismes d’objets simples deA (resp. l’ensemble des id´eaux deA, l’ensemble des
sous-cat´egories strictement ´epaisses deA, c’est-`a-dire strictement pleines et stables
par somme directe et facteur direct). Consid´erons les applications suivantes :
7Selon la terminologie de Bourbaki [5] ; selon la terminologi e anglo-saxonne, on dirait plutˆ ot
“semisimple artinian”, cf. [51].
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 17
– SC :C(A)→S(A) :B↦→S(B).
– CS :S(A)→C(A) :X↦→{⨁ Si|Si∈X}.
– IC :C(A)→ I(A) :B↦→IB (cf. exemple 1.3.1).
– SI : I(A)→S(A) :I↦→{S∈S(A)| 1S∈I} .
AlorsSC,CS,IC etSI sont bijectives, SC etCS sont inverses l’une de l’autre,
SI◦IC =SC etCS◦SI =IC−1.
D´emonstration. Le fait que SC◦ CS = Id est ´ evident. SiB ∈C(A), on a
CS◦SC (B)⊂B parce queB estK-lin´ eaire, avec ´ egalit´ e parce queB est pseudo-
ab´ elienne. De plus,SI◦IC (B) = {S | 1S se factorise ` a travers un objet deB}
contient clairement S(B). R´ eciproquement, pour unS ∈ SI◦IC (B), il existe
a : S→ X etb : X→ S tels que ba = 1 S. Soit S′ = a(S) : restreignantb ` aS′,
on se ram` ene au cas o` uX est simple. Ceci montre que S∈ S(B) puisqueB est
strictement pleine.
Il reste ` a montrer queIC◦CS◦SI = Id. PourI ∈I, IC◦CS◦SI (I)
est l’id´ eal des morphismes qui se factorisent ` a travers unobjet de la forme ⨁ Si,
o` u lesSi sont simples et tels que 1Si ∈I pour tout i. Cet id´ eal est ´ evidemment
contenu dansI. R´ eciproquement, soitf ∈I : ´ ecrivonsf comme somme directe
d’un morphisme nul et d’un isomorphismeu (lemme A.2.13). Alorsu∈I . SiS est
un facteur simple de la source deu, 1S se factorise ` a traversu, donc 1S∈I . □
