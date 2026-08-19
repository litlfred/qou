---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-006-21-polynomial-functions-on-the-set-of-young-diag
section_title: "Polynomial functions on the set of Young diagrams"
section_number: 2.1
pages: 12-14
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
⋆ of poly-
nomial functions on the set of Young diagrams (brieﬂy: the ring of polynomial
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 13
i1
i2
i3
o1
o2 Oλ = {−1, 2}
Iλ = {−3, 0, 4}
FIGURE 2. A Young diagram with its inner and outer corners
(marked respectively with i and o).
functions) has been introduced by Kerov and Olshanski in order to studyirreducible
character values of the symmetric groups [KO94].
The ﬁrst characterization of Λ (1)
⋆ , that we shall use as deﬁnition, is the following.
Deﬁnition 2.1. A function F on the set of all Young diagrams belongs to Λ (1)
⋆ if
there exists a collection of polynomials (Fh ∈ Q[λ1, . . . , λh])h>0 such that
• for a diagramλ = (λ1, . . . , λh) of length h, one hasF (λ) = Fh(λ1, . . . , λh);
• each Fh is symmetric in variables λ1 − 1, λ2 − 2, . . . , λh − h;
• the compatibility relation
Fh+1(λ1, . . . , λh, 0) = Fh(λ1, . . . , λh)
holds true for all values of h.
The ring Λ (1)
⋆ , as deﬁned above, is sometimes called the ring of shifted symmet-
ric functions in λ1, λ2, . . .. It was ﬁrst considered by Knop and Sahi [KS96] in a
more general context. While this is not obvious, one can prove that Ch(1)
µ belongs
to Λ (1)
⋆ . In fact, one has more [KO94, Section 3].
Proposition 2.2. When µ runs over all partitions, the family (Ch(1)
µ )µ forms a
linear basis of Λ (1)
⋆ .
An equivalent description of Λ (1)
⋆ can be given using Kerov’s interlacing coor-
dinates of a Young diagram. Recall that the content of a box of a Young diagram
is j − i, where j is its column index and i its row index and, more generally, the
content of a point of the plane is the difference between its x-coordinate and its
y-coordinate. We denote by Iλ the set of contents of the inner corners of λ, that
is corners, at which a box could be added to λ to obtain a new diagram of size
|λ| + 1. Similarly, the set Oλ is deﬁned as the contents of the outer corners, that
is corners at which a box can be removed from λ to obtain a new diagram of size
|λ| − 1. An example is given in Figure 2 (we use the French convention to draw
Young diagrams).
If k is a positive integer, one can consider the power-sum symmet ric function
pk, evaluated on the difference of alphabets Iλ − Oλ. By deﬁnition, it is a function
14 M. DOŁ ˛ EGA AND V . FÉRAY
on Young diagrams given by:
λ ↦→pk(Iλ − Oλ) :=
∑
i∈Iλ
ik −
∑
o∈Oλ
ok.
It can easily be seen that, for any Young diagram, p1(Iλ − Oλ) = 0 . As any
symmetric function can be written (uniquely) in terms of pk, we can deﬁne f (Iλ −
Oλ) for any symmetric function f as follows: if aρ (ρ partition) are the coefﬁcients
of the p-expansion of f, that is f =∑
ρ aρpρ1 · · ·pρℓ, then by deﬁnition,
f (Iλ − Oλ) =
∑
ρ
aρpρ1(Iλ − Oλ) · · ·pρℓ(Iλ − Oλ).
With this notion of symmetric functions evaluated on differ ence of alphabets, the
ring Λ (1)
⋆ admits the following equivalent description [IO02, Corollary 2.8].
Proposition 2.3. The functions (λ ↦→pk(Iλ − Oλ))k≥2 form an algebraic basis of
Λ (1)
⋆ .
In other terms, any function F in Λ (1)
⋆ is equal to λ ↦→f (Iλ − Oλ), for some
symmetric function f. This symmetric function f is unique up to addition of a
multiple of p1.
