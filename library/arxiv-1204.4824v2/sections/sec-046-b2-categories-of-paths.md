---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-046-b2-categories-of-paths
section_title: "B.2 Categories of paths"
section_number: null
pages: 79-79
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
LetX be any topological space. By a path inX we mean a continuous map℘ : [T1,T 2]→X
for some interval [T1,T 2]⊂ R. We deﬁne the path groupoidP(X) as follows: the objects of
P(X) are points of X, and the morphism space P(X)(x1,x 2) is the set of all paths from
x1 to x2, with the obvious composition.
By taking a quotient on the morphism spaces inP(X) we can reduce to thefundamental
groupoidπ≤1(X). This is the groupoid whose objects are points of X and morphism spaces
π≤1(X)(x1,x 2) are homotopy classes of paths from x1 to x2.
In§B.4 and §B.5 we will also make use of a further “quotient” of the fundamental
groupoid, which we call the ﬁrst homology groupoid and denote H≤1(X). It is a groupoid
whose objects are again points of X. The morphism space between two points x1,x 2 inX,
denotedH≤1(x1,x 2), is deﬁned as follows. First let C1(x1,x 2) be the set of all 1-chains c in
X with∂c =x2−x1. Note that if x1 =x2 these are simply 1-cycles. In general C1(x1,x 2)
is a torsor for the group of 1-cycles. We identify
H≤1(x1,x 2) :=C1(x1,x 2)/∼ (B.4)
where c1 ∼ c2 if c1− c2 is a 1-boundary. The morphism space H≤1(X)(x1,x 2) is an
aﬃne subspace of the relative homology H1(X,{x1,x 2}; Z), and is a torsor for H1(X; Z).
Composition of morphisms is induced by addition of chains. The automorphism group
of any object is canonically H1(X; Z). Note that there are natural functors P(X) →
π≤1(X)→H≤1(X).
