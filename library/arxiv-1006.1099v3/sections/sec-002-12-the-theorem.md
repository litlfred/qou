---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-002-12-the-theorem
section_title: "The theorem"
section_number: 1.2
pages: 1-3
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
1.3. Entropy 3
1.4. Representation varieties 3
1.5. Instanton Floer homology 4
1.6. Witten’s conjecture 5
1.7. Homological Mirror Symmetry 6
1.8. Another birational motivation 7
1.9. Outline of proof 7
2. The representation variety 9
2.1. Topology 9
2.2. Monodromy and degenerations 10
2.3. Fibred 3-manifolds 12
2.4. Faithfulness 13
2.5. A ﬁxed point theorem 15
3. The Fukaya category 17
3.1. Floer and quantum cohomology 17
3.2. Higher order products 19
3.3. Twisting and generation 21
3.4. Functors from quilts 23
3.5. Grading and deformations 26
3.6. Formality 26
3.7. The Fukaya category of a curve 29
4. From the base locus to the relative quadric 30
4.1. The Fukaya category of a quadric 30
4.2. Hyperelliptic curves and quadrics 33
4.3. Idempotents for functors 36
4.4. An illustrative example 37
4.5. Idempotents and blow-ups 41
4.6. Spinning 49
5. From the curve to the relative quadric 52
5.1. Matching Spheres 52
5.2. Thimbles 54
5.3. Exterior Algebra 56
5.4. The cubic term 59
5.5. Finite determinacy 62
References 67
Date: October 2011.
1
2 IV AN SMITH
1. Introduction
1.1. Two contexts. The main result of this paper, Theorem 1.1, belongs to categorical s ym-
plectic topology in the sense of Donaldson, Fukaya and Kontsevich. It relates the derived Fukaya
categories of a genus g surface Σ g and of the complete intersection Q0∩Q1 of two smooth quadric
hypersurfaces in P2g+1. The result is of interest in at least two diﬀerent contexts.
• The intersection of two quadric 4-folds in P5 is also a moduli space of solutions to the
anti-self-dual Yang-Mills equations on the product Σ 2×S1 [73, 72]. Theorem 1.1, in the
special case g = 2, can be seen as an instance of the “Seiberg-Witten equals Donald son”
philosophy for gauge-theory invariants of 3-manifolds.
• Theorem 1.1 can also be viewed as a symplectic analogue of a classical t heorem of Bondal
and Orlov [16] in algebraic geometry, concerned with derived catego ries of sheaves on the
same spaces. The passage here from algebraic to symplectic geome try ﬁts into the broader
program of Kontsevich’s Homological Mirror Symmetry conjecture .
After formulating a precise version of the main theorem, the rest o f the Introduction will ﬂesh
out these two contexts, and then indicate the basic strategy of t he proof, which is itself motivated
– via mirror symmetry – by several classical theorems on derived ca tegories of sheaves.
1.2. The theorem. Let Σ g be a closed surface of genus g≥ 2, equipped with a symplectic form.
This has a well-deﬁned balanced Fukaya category F(Σ g), linear over C. Let {Q2g
t }t∈P1⊂ P2g+1
denote a pencil of smooth 2 g-dimensional quadric hypersurfaces in P2g+1, with smooth base locus
Q2g
0 ∩Q2g
1 . By Moser’s theorem, the symplectic manifold underlying the complet e intersection
Q0∩Q1 is independent of the choice of generic pencil of quadrics. It is a simp ly-connected
Fano variety, in particular a monotone symplectic manifold with a well-d eﬁned monotone Fukaya
category F(Q0∩Q1), again deﬁned over C. The latter category actually splits into a collection of
mutually orthogonal A∞-subcategories, one for each eigenvalue of quantum multiplication b y the
ﬁrst Chern class on the quantum cohomology of Q0∩Q1. We denote by DπC the cohomological
category H(Tw πC) underlying the split-closure of the category of twisted complexes of an A∞-
category C. Our main result is:
Theorem 1.1. There is a C-linear equivalence of Z2-graded split-closed triangulated categories
DπF(Σ g)≃DπF(Q2g
0 ∩Q2g
1 ; 0)
where F(•; 0) denotes the summand corresponding to the 0-eigenvalue of qu antum cup-product by
the ﬁrst Chern class.
The proof of Theorem 1.1 given here relies essentially on the (typically non-geometric) passage
to idempotent completion.
If Σ g → P1 is a hyperelliptic curve, branched over {λ1,...,λ 2g+2} ⊂C, it determines a
(2, 2)-complete intersection
Q0∩Q1 =
(∑
z2
j = 0
)
∩
(∑
λjz2
j = 0
)
⊂ P2g+1.
Varying the λj in C, one obtains a natural action, by parallel transport, of the hype relliptic
mapping class group Γ hyp
g,1 of a once-pointed curve on each of Σ g and Q0∩Q1. (There is no
universal hyperelliptic curve over conﬁguration space Conf 2g+2(P1) [67]; we have constrained the
λj to lie in C⊂ P1, which accounts for the appearance of once-pointed curves.)
Addendum 1.2. The equivalence of Theorem 1.1 is compatible with the weak ac tion of Γ hyp
g,1 .
Considering the situation when branch points go to inﬁnity more care fully, there is a non-split
ﬁnite extension
1→ Z2g
2 −→ ˜Γ hyp
g −→ Γ hyp
g → 1
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 3
of the classical hyperelliptic mapping class group which acts, via para llel transport, by symplec-
tomorphisms of Q0∩Q1, cf. Remark 4.11. A fairly direct consequence of Theorem 1.1 is:
Corollary 1.3. The natural representation ˜Γ hyp
g →π0 Symp(Q0∩Q1) is faithful.
Classical surgery theory [99, Theorem 13.5] shows ˜Γ hyp
g →π0 Diﬀ(Q0∩Q1) has inﬁnite kernel.
More surprisingly, the Γ hyp
g,1 -action extends to a faithful weak action of the full mapping class g roup
Γ g by autoequivalences ofDπF(Q0∩Q1), which has no obvious direct geometric construction. The
construction of mapping class group actions on triangulated categ ories is a well-known problem
in that part of representation theory concerned with categoriﬁc ation.
