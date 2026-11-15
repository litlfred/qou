---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-008-3-decomposition-of-the-first-variation-of-mathca
section_title: "Decomposition of the first variation of mathcalE"
section_number: 3
pages: 7-8
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
In 1994, Freedman, He and Wang stated the Gâteaux differentiability of the Möbius energy
E and additionally a formula of the ﬁrst variation of E [10, Lemma 6.1, Lemma 6.4.]. Reiter
could prove that E is Fréchet differentiable and he computed its ﬁrst variation at an injective
regular curve η ∈H2 in direction h ∈H2 [38, Chapter 2]. In order to work with the Möbius
energy in a sophisticated way, He and Reiter used a kind of linearization of the ﬁrst variation
of E in [17,38]. Using these ideas and results, we want to determine a suitable decomposition
of the ﬁrst variation of the Möbius energy E at γ which helps us proving the main result
Theorem 1.2.
Assume n ∈N and let γ ∈C∞(R/Z, Rn) be a simple, closed, and by arc-length
parametrized curve. Recall that the orthogonal projection of Rn onto the normal vector
plane to γ at γ (x) P⊥
˙γ (x) : Rn →Rn for every g ∈Rn is given by
(P⊥
˙γ g)(x) := P⊥
˙γ (x)(g) := g −⟨g, ˙γ (x)⟩Rn ˙γ (x).
Then we get by [10, Lemma 6.4.] and [38, Theorem 2.24] the following
Theorem 3.1 The ﬁrst variation of E at γ ∈H2(R/Z, Rn) in direction h ∈H2(R/Z, Rn)
may be written as
δE(γ, h) =
 1
0
⟨(Hγ )(x), h(x)⟩Rndx
(3.1)
where
(Hγ )(x) := 2 lim
ε↓0

|w|∈

ε, 1
2


2
P⊥
˙γ (x)(γ (x + w) −γ (x))
|γ (x + w) −γ (x)|2
−¨γ (x)

dw
|γ (x + w) −γ (x)|2 .
Since P⊥
˙γ (x)( ˙γ (x)) = 0, ⟨˙γ (x), ¨γ (x)⟩Rn = 0 and by the linearity of P⊥
˙γ (x) for all x ∈R/Z,
one sees that
(Hγ )(x) = (P⊥
˙γ 
Hγ )(x) = P⊥
˙γ (x)(( 
Hγ )(x))
(3.2)
where
( 
Hγ )(x) := 2 lim
ε↓0

|w|∈

ε, 1
2


2γ (x + w) −γ (x) −w ˙γ (x)
|γ (x + w) −γ (x)|2
−¨γ (x)

dw
|γ (x + w) −γ (x)|2 .
16
Page 8 of 28
S. Blatt, N. Vorderobermeier
Now, motivated by [17,38] as explained above, simply by adding and subtracting the terms
4(γ (x+w)−γ (x)−w ˙γ (x))
w4
and 2 ¨γ (x)
w2 , we may decompose 
H into three functionals Q, R1, R2
given point-wise for all x ∈[0, 1] by
Qγ (x) = lim
ε↓0 Qεγ (x), R1γ (x) = lim
ε↓0 Rε
1γ (x), R2γ (x) = lim
ε↓0 Rε
2γ (x),
where for any 0 < ε ≤1
2
(Qεγ )(x) := 2

|w|∈

ε, 1
2


2γ (x + w) −γ (x) −w ˙γ (x)
w2
−¨γ (x)
 dw
w2 ,
(Rε
1γ )(x) := 4

|w|∈

ε, 1
2


1
|γ (x + w) −γ (x)|4 −1
w4

(γ (x + w) −γ (x) −w ˙γ (x))dw,
(Rε
2γ )(x) := −2

|w|∈

ε, 1
2


1
|γ (x + w) −γ (x)|2 −1
w2

¨γ (x)dw,
such that
( 
Hγ )(x) = (Qγ )(x) + (R1γ )(x) + (R2γ )(x)
(3.3)
for all x ∈R/Z.
In the upcoming section we will see that Q contains the highest order part of the ﬁrst
variation of E. We will see that the tangential part of Q is the most difﬁcult part to get under
control, whereas R1 and R2 are of lower order and can be estimated more elementary.
