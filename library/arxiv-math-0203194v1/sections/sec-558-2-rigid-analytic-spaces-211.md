---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-558-2-rigid-analytic-spaces-211
section_title: "RIGID ANALYTIC SPACES. 211"
section_number: 2
pages: 215-217
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
such that the following conditions are satisﬁed:
(1)∅∈ T; U,V ∈ T ⇒ U∩V ∈ T.
(2) U∈ T ⇒ {U}∈ Cov(U ).
(3){Ui}i∈I∈ Cov(U ), V⊆U, V∈ T ⇒ {Ui∩V}i∈I∈ Cov(V ).
(4){Ui}i∈I∈ Cov(U ), {Ui,j}j∈Ji∈ Cov(Ui) ⇒ {Ui,j}i∈I,j∈J∈ Cov(U ).
Elements in T are called admissible open sets , and elements in Cov(U )
are called admissible coverings of U .
Let X = Spm( A) be an aﬃnoid over K. We introduce a Grothendieck
topology to X by the following recipe:
• An admissible open set is a rational subdomain.
• For a rational subdomain, an admissible covering is a ﬁnite c overing
consisting of rational subdomains.
This is valid, due to Lemma 2.1.
We deﬁne the structure presheaf OX, with respect to the Grothendieck
topology, by assigning for each rational subdomain R the corresponding
aﬃnoid algebra AR. Due to the following weak form of Tate’s acyclicity
theorem, the presheaf OX is, in fact, a sheaf (a sheaf of local rings).
Theorem 2.4. Let U1,... ,U m be rational subdomains of X = Spm( A).
Set U =U1∪···∪ Um. Then the sequence
0−→O X (U )−→
m∏
i=1
OX (Ui)−→
m∏
i,j=1
OX (Ui∩Uj)
is exact, where the last arrow is the diﬀerence of the two poss ible restriction
morphisms.
For the proof, see, for example, [ BGR84, 8.2] or [ FvdP81, III.2.2].
Deﬁnition 2.5 (Rigid Analytic Space) . A rigid analytic space is a locally
ringed space ( X,OX ), with a Grothendieck topology in the above sense,
locally isomorphic to an aﬃnoid; more precisely, there exis ts a covering
{Xi}i∈I (possibly inﬁnite) of X by admissible open sets such that (Xi,OX|Xi)
is isomorphic to a certain aﬃnoid for each i.
Let us see some examples of rigid analytic spaces:
Example 2.6 (Projective Space) . The projective space Pn(K) has the nat-
ural rigid analytic structure. Here we limit ourselves to de monstrate it only
in the case n = 1, and leave the general case to the reader. Let ( X : Y ) be
the homogeneous coordinate in P1(K) and set z =X/Y . Set
U+ ={(X : Y )|| X|≤| Y|} and U− ={(X : Y )|| X|≥| Y|}.
Then U+ is isomorphic to the closed disk {z∈ K|| z|≤ 1} (the Southern
Hemisphere with the equator) , and U− to{z∈ K∪{∞}|| z|≥ 1} (the
Northern Hemisphere with the equator). The intersection U+∩ U− is thus
212 A. RAPID COURSE IN p-ADIC ANALYSIS.
isomorphic to the circle {z∈ K|| z| = 1}. Hence {U+, U−} gives the ad-
missible covering of P1(K) which induces, in the obvious way, the structure
of a rigid analytic space.
More generally, an algebraic variety, separated and of ﬁnit e type over
K, carries the canonical structure of a rigid analytic space.
Any open set (not necessarily admissible) U in a rigid analytic space X
will be again a rigid analytic space ( “open subanalytic space” ); more pre-
cisely,U has the induced analytic structure from that of X. The admissible
open sets of U , for example, are those of X contained in U .
3. Relation with F ormal Geometry .
In this section we need to consider the valuation ring R of K. Let
us denote by m the maximal ideal of R, and ﬁx a topological generator
0⁄=π∈ m. The residue ﬁeld R/m is denoted by k.
Let A be an aﬃnoid algebra over K. The spectral semi-norm on A is
the function|·| sup : A→ R≥0 deﬁned, for any f∈ A, by
|f|sup = sup
x∈Spm(A )
|f (x)|.
It is known that for any representation α : K{t1,... ,t n}/I ∼→ A, we have
|f|sup≤|f|α for every f∈ A (cf. [ BGR84, 6.2.1]).
Theorem 3.1 (Maximal modulus principle) . For an aﬃnoid algebra A and
an elementf∈ A, there exists a point x∈ Spm(A) such that|f (x)| =|f|sup.
We refer [ BGR84, 6.2.1] for the proof.
Given an aﬃnoid algebra A overK, we introduce the following notation:
A◦ = {f∈ A|| f|sup≤ 1},
A◦◦ = {f∈ A|| f|sup< 1},
A = A◦/A◦◦;
A◦ is a R-subalgebra of A, and A◦◦ is an ideal of it. For instance, K◦ =R,
K◦◦ = m, and K =k.
Example 3.2. We can immediately calculate:
T n
K
◦ = R{t1,... ,t n}
: =
{ ∑
ν1,... ,νn≥0aν1,... ,νntν1
1 ··· tνn
n |aν1,... ,νn|→ 0 for
∈R[[t1,... ,t n]] ν1 +··· +νn→∞
}
T n
K = k[t1,... ,t n].
Note that T n
K
◦ is the (π)-adic completion of the polynomial ring R[t1,... ,t n]
over R. It should be noticed that T n
K is a polynomial ring over k; indeed,
each element in R{t1,... ,t n} lies, by the convergence condition, in T n
K
◦◦
modulo ﬁnitely many terms.
Proposition 3.3. Let A be an aﬃnoid algebra over K. Then,
(i) A◦ is a model of A; i.e. A◦⊗RK∼
= A,
