---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu"
section_id: sec-008-31-the-schreier-normal-form-for-3-braids-and-vol
section_title: "The Schreier normal form for 3-braids and volume"
section_number: 3.1
pages: 12-13
source_pdf: 1406.7337v4 (1).pdf
source_sha256: 5bae8237742733b9
doc_brief: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and"
---
A useful development in the history of 3-braids was the solution to the Conjugacy Problem ([15]). During
this time, an algorithm was developed that produces from an arbitrary 3-braid word β a conjugate 3-braid
wordβ′, called the Schreier normal form , which is the unique representative of the conjugacy class of β. A
version of this algorithm is presented below.
Schreier Normal Form Algorithm:
(1) Let β∈B3 =⟨σ1,σ 2| σ1σ2σ1 =σ2σ1σ2⟩ be cyclically reduced into syllables. Introduce new variables
x = (σ1σ2σ1)−1 and y = σ1σ2. Thus we have that σ1 = y2x, σ2 = xy2, σ−1
1 = xy, and σ−1
2 = yx.
Possibly using cyclic permutation, rewrite β as a cyclically reduced word (that is positive) in x andy.
(2) Introduce C =x−2 =y3∈Z(B3), where Z(B3) denotes the center of the 3-braid group B3. By using
these relations and the commutativity ofC as much as possible, group all powers ofC at the beginning
of the braid word and reduce the exponents of x and y as much as possible. Rewrite β as β = C jη,
where j∈ Z and where
η =



(xy)p1
(
xy2)q1
··· (xy)ps
(
xy2)qs
for some s,p i,q i≥ 1
(xy)p for some p≥ 1(
xy2)q
for some q≥ 1
y
y2
x
1
(3) Possibly using cyclic permutation and the commutativity of C, rewrite β back in terms of σ1 and σ2
as β′ =C kη′, where k∈ Z and where
η′ =



σ−p1
1 σq1
2 ··· σ−ps
1 σqs
2 for some s,p i,q i≥ 1
σp
1 for some p∈ Z
σ1σ2
σ1σ2σ1
σ1σ2σ1σ2
Deﬁnition 3.1. We call β′ = C kη′∈ B3 the Schreier normal form of β∈ B3. The braid word β′ is the
unique representative of the conjugacy class of β. Following [11], we will call a braid β generic if it has
Schreier normal form
β′ =C kσ−p1
1 σq1
2 ··· σ−ps
1 σqs
2 .
Using the Schreier normal form of a 3-braid, Futer, Kalfagianni, and Purcell ([11]) classiﬁed the hyperbolic
3-braid closures. Furthermore, given such a hyperbolic closed 3-braid, they gave two-sided bounds on the
volume of the link complement, expressing the volume in terms of the parameter s from the Schreier normal
form of the 3-braid. By using the more recent machinery built by the same authors in [8], we aim to obtain
a sharper lower bound on volume. To begin our study, we ﬁrst recall two propositions from [11].
Proposition 3.1 ([11], Theorem 5.5) . Let D(K) = ˆβ denote the closure of a 3-braid β∈ B3. Then K is
hyperbolic if and only if
(1) β is generic, and
12
(2) β is not conjugate to σp
1σq
2 for any integers p and q.
Proposition 3.2 ([11], Theorem 5.6) . Let D(K) = ˆβ denote the closure of a 3-braid β ∈ B3. Then,
assuming that K is hyperbolic, we have that
4v3·s− 276.6< vol(S3\K)< 4v8·s.
