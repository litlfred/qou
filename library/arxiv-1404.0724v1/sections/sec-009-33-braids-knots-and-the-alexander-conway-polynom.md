---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-009-33-braids-knots-and-the-alexander-conway-polynom
section_title: "Braids, knots and the Alexander Conway polynomial"
section_number: 3.3
pages: 10-13
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
Braids, knots and the Alexander Conway polynomial
A knot is an isotopy class of an embedding of a circle in three dimensional euclidian space. More
generally, a link with k components is an isotopy class of an embedding of k circles in R3. The
fundamental problem of knot theory is the classiﬁcation of knots and links. The following is a
typical example of a knot:
......................................................................
........................................................................
........................................................................
.......................................................................
....................................................................
The relationship between links and braids is given by the operation of closure of a braid, which
produces a link by connecting the strands of the braid, as explained in the following diagram:
7→
A link obtained as the closure of a braid comes with a natural orientation, given by declaring
the strands of the braid to be ﬂowing downwards.
Theorem 3.7 (Alexander [1]). Any oriented link can be obtained as the closure of a braid.
Proof. For a proof of this theorem the reader may consult [18] Theorem 2.3.
□
The theorem above immediately raises the question of deciding when two braids produce the
same oriented link upon closure.
This question is answered by Markov’s theorem.
We say
that two braids β, β′ ∈Bn are related by the Markov move M1 if their are conjugate, i.e. if
there exists a γ ∈Bn such that γβγ−1 = β′. The following picture describes the action of the
operation M1.
7→
Let ιn : Bn →Bn+1 be the natural inclusion of groups characterized by ι(σi) = σi. Two braids
β ∈Bn, β′ ∈Bn+1 are related by the second Markov move M2 if σ±
n ι(β) = β′. The following
picture describes the action of the second Markov move on a braid:
7→
Deﬁnition 3.8. The Markov equivalence relation M is the smallest equivalence relation on the
set of all braids such that two braids are equivalent if they are related by the Markov moves M1
and M2. We say that two braids are Markov equivalent if they are equivalent with respect to M.
Theorem 3.9 (Markov [24]). Two braids are Markov equivalent if and only if their closures
represent the same oriented link.
Proof. The interested reader may consult [18] Theorem 2.8.
□
Deﬁnition 3.10. A Markov function f with values in a set X is a sequence of functions fn :
Bn →X with the property that:
• fn(γ−1βγ) = fn(β).
• fn(β) = fn+1(σnιn(β)) = fn+1(σ−1
n ιn(β)).
Clearly, Markov’s theorem implies that any Markov function produces a link invariant with
values in the set X. Let us now describe a Markov function provided by the Burau representation.
Let g : Λ = Z[t, t−1] →Z[s, s−1] be the ring homomorphism characterized by t 7→s2. We deﬁne
the group homomorphsim
⟨⟩: Bn →Z,
by setting ⟨σi⟩= 1.
For n ≥2 we deﬁne the function fn : Bn →X = Z[s, s−1] by the formula:
fn(β) = (−1)n+1 s−⟨β⟩(s −s−1)
sn −s−n
g (det (ψr
n(β) −id)) .
Theorem 3.11. The sequence of functions fn deﬁned above is a Markov function with values
in the set X = Z[s, s−1].
Proof. The interested reader may consult [18] Lemma 3.12.
□
The Markov function fn deﬁned above in terms of the Burau representation deﬁnes an invariant
of oriented links known as the Alexander-Conway polynomial.
Deﬁnition 3.12. The Alexander-Conway polynomial of an oriented link L, denoted ∇(L), is
the polynomial fn(β) ∈Z[s, s−1], where β is any braid whose closure is L.
For the purpose of computation it is often useful to describe the skein relations for the Alexan-
der Conway polynomials. These relations express the change in the value of the polynomial that
occurs when modifying the crossing of a link diagram. A Conway triple L+, L−, L0 is a triple of
link diagrams that diﬀer only locally at one crossing, which looks, respectively, as follows:
_
?
L+
?
_
L−
\
B
L0
Theorem 3.13. The Alexander-Conway polynomial is the unique invariant of oriented links ∇
with values in Z[s, s−1] which satisﬁes the following properties:
• ∇(L) = 1 if L is the unknot.
• For any Conway triple L+, L−, L0:
∇(L+) −∇(L−) = (s−1 −s)∇(L0).
Proof. The proof can be found in [18] Theorem 3.13.
□
It is fairly easy to show that there is at most one invariant satisfying the skein relations
above. The existence is the more interesting part of the theorem, and that is where the explicit
construction of the invariants, provided by the Burau representations, is needed.
