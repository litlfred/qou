---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-017-71-weak-real-stability-preservation
section_title: "Weak Real Stability Preservation"
section_number: 7.1
pages: 23-24
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
---
real stability of the associated symbol Symb BB (T ). We have to say “almost equivalent” here because there
are certain weak real stability preserving operators for which the corresponding symbol is not real stable. As
before, this implies a certain dimension restriction: such operators must have image of dimension at most
two.
We will now characterize all strong real stability preserving linear op erators. As above, strong real
stability preservation will serve to eliminate the degeneracy conditio n of the Borcea-Br¨ and´ en characterization.
In this section, we duplicate the outline of our previous discussion on complex operators, making use of
arguments similar to those found in [ BB09a] to ﬁll in the gaps.
Further, we also obtain a characterization of a certain class of ope rators which preserve ray- and interval-
rootedness. The question of a full characterization of such oper ators is as of yet still an open problem (see
[BB09c]). Here, we answer this question for operators which preserve bo th strong ray- or interval-rootedness
as well as weak real-rootedness.
23
7.1 Weak Real Stability Preservation
Borcea and Br¨ and´ en obtain the following characterization of weak real stability preserving linear operators.
Recall the notion of proper position (denoted by ≪) given in Deﬁnition 4.8.
Theorem 1.2 (Borcea-Br¨ and´ en). Fix λ ∈ Nm
0 and any linear operator T : Rλ[x1,...,x m] → R[x1,...,x m].
The following are equivalent.
(i) T maps real stable polynomials to weakly real stable polynomi als.
(ii) One of the following holds:
(a) SymbBB (T ) is H2m
+ -stable.
(b) SymbBB (T ) is (Hm
− × Hm
+ )-stable.
(c) T has image of dimension at most two, and is of the form
T :p ↦→q ·ψ1(p) +r ·ψ2(p)
where q,r ∈ R[x1,...,x m] are weakly real stable such that q ≪ r, and ψ1,ψ 2 are real linear
functionals.
As in the case of complex operators, the degeneracy condition ( ii)(c) is the result of allowing weak real
stability preserving operators. We now give an example which demons trates its necessity.
Example 7.1. Deﬁne T : Rn[x] → R[x] via:
T :
n∑
k=0
( n
k
)
akxk ↦→anxn +an−2xn−1 = (anx +an−2)xn−1
This operator obviously preserves weak real stability. We then hav e that Symb BB (T ) = (z2 +x)xn−1, which
is not H2
+-stable nor ( H− × H+)-stable.
Again, the degeneracy condition is required for the characterizat ion but obscures the connection between
an operator and its symbol. To remove it, we now turn to our charac terization of strong real stability
preserving operators.
