---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-004-14-interrelations
section_title: "Interrelations"
section_number: 1.4
pages: 4-6
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
Interrelations
The best known relation of C with the Hecke algebra Hn is the closure map
Rn
n →C, induced by taking a tangle T to its closure ˆT in the annulus, deﬁned
4
by
ˆT =
T
.
This is a linear map, whose image we call Cn.
Elements of the skein C can be used to decorate closed curves in a framed
diagram in any F to produce new skein elements of S(F). We shall restrict
the decorations in our work to elements drawn from Cn for some n, and write
C+ = ∪n≥0Cn.
A simple skein theory construction determines a natural linear map ϕ :
C →C, induced by taking a diagram X in the annulus and linking it once
with a simple loop to get
ϕ(X) =
X
.
This construction can be interpreted as an example of the decoration
technique above, applied to one loop of the diagram
.
We can extend this by decorating the other loop with any Y ∈C to give a
linear map ϕ(Y ) : C →C. Then
ϕ(Y )(X) =
X
Y
∈C.
The map ϕ is then ϕ(c1) where c1 ∈C is represented by a single closed curve
following the oriented core of the annulus.
Evaluation of ϕ(Y )(X) gives a scalar which we denote by ⟨X, Y ⟩, and
which forms the main focus of this paper.
The map ψn : C →Hn induced by decorating the closed curve in the dia-
gram below by an element X ∈C is readily seen to be a ring homomorphism,
5
whose image
ψn(X) =
X
∈Hn
lies in the centre of Hn.
There is a set of quasi-idempotent elements, eλ ∈Hn, one for each parti-
tion λ of n, known as the Gyoja-Aiston idempotents. They were originally
described algebraically by Gyoja [2], while skein pictures of these based on the
Young diagram for λ can be found in [1] or [10]. The skein theory version dis-
plays a nice ‘internal stability’ under multiplication which shows readily that
Zeλ is a scalar multiple of eλ for any central element Z ∈Hn. We can then
deﬁne a ring homomorphism tλ : C →Λ by the formula ψn(Y )eλ = tλ(Y )eλ,
using the homomorphism ψn from C to the centre of Hn.
Deﬁne Qλ ∈C to be the closure of the genuine idempotent
1
αλeλ, where
e2
λ = αλeλ, as in [10] or [6]. Then clearly Qλ is an eigenvector of ϕ(Y ) with
eigenvalue tλ(Y ) for every Y ∈C. We make extensive use of these elements
of C, especially where λ is a single column or row. We write ci for Qλ where
λ is the column with i cells, and dj where λ is the row with j cells, and take
c0 = d0 = 1 ∈C represented by the empty diagram.
