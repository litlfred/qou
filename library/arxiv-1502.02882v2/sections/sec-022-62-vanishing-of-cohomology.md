---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-022-62-vanishing-of-cohomology
section_title: "Vanishing of cohomology"
section_number: 6.2
pages: 32-36
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Vanishing of cohomology
We will need the following ‘handleslide’ identity.
32
Lemma 6.5. In the pairing convention for the graphical calculus associated to
a fusion category, we have
X
α,p
dp
=
X
k
dk
where dp are the fusion dimensions, X is an arbitrary object, and f : Xk ⊗X →
Xk ⊗X is an arbitrary morphism.
Proof.
LHS =
X
p,α
dp
= dk
X
p,α
(44)
where in the ﬁrst equality the pairing convention is being used, and in the second
equality we transformed the old basis vectors eα and ˆeα (which were written just
as α and ˆα in the diagrams) into new basis vectors fα ∈Hom(Xp∗, Xi ⊗Xk∗)
and ˆfβ ∈Hom(Xi ⊗Xk∗, Xp∗) by the formulas
:=
:= dp
dk
(45)
33
where the cup and cap maps are the same ones used in (44). Now we claim that
fα and ˆfβ form a dual basis. Indeed,
= dp
dk
= δαβ
as can be seen by closing the loop on the left and applying the deﬁnition of the
pairing convention. Hence the fα ˆfα term in the right hand side of (44) provides
a resolution of the identity, proving the lemma.
Theorem 6.6 (cf. [9, Thm 2.27]). Hn(C) = 0 for all n > 0.
Proof. We deﬁne an operator χn : Cn →Cn−1 by
= 1
D
X
p
dp
where on the right hand side we are using the pairing convention (else this
diagram would not be well-deﬁned), dp is the fusion dimension of Xp, and D is
the global dimension of C. We will show that
χn+1f n
k =
(
idCn
if k = 0
f n−1
k−1 χn
if k, n > 0
(46)
which will imply that dχ + χd = id, and hence the cohomology vanishes. The
case k = 0 of (46) is simply the relation D = P
p d2
p, which is the deﬁnition
of D. The cases k > 1 are tautologies. The nontrivial case is k = 1, which is
precisely the handleslide identity from Lemma 6.5.
Example 6.7. For a 2-cocycle A ∈Z2(C), that is, a collection of linear opera-
tors Ai
jk satisfying (43),the vanishing of H2(C) means that Ai
jk must take the
form
Ai
jk = (cj −ci + ck) id
(47)
for some scalars ci, cj, ck. This conclusion is perhaps not immediately evident
from (43). Even if we assume that the Ai
jk in (43) are diagonal (which is also
not immediately clear from dA = 0) i.e. (Ai
jk)αβ = δαβ ai
jk,α, then (43) becomes
the equation
at
jk,ω −as
it,θ + as
mk,γ −am
ij,δ = 0
whenever (F s
ijk)θtω
δmγ̸ = 0.
(48)
The vanishing of H2(C) means that the equations (48) must force the ai
jk, α to
all be equal for diﬀerent α and furthermore take the form (47). Thus Ocneanu
rigidity implies in particular that suﬃciently many associators must be nonzero.
34
References
[1] Bojko Bakalov and Alexander Kirillov. Lectures on Tensor Categories and
Modular Functors. American Mathematical Society, 2001.
[2] John W. Barrett and Bruce W. Westbury. Spherical categories. Advances
in Mathematics, 143(2):357–375, 1999.
[3] Bruce Bartlett. On unitary 2-representations of ﬁnite groups and topolog-
ical quantum ﬁeld theory. PhD thesis, Department of Pure Mathematics,
University of Sheﬃeld, 2009. arXiv:math/0512103.
[4] Alain Brugui´eres and Alexis Virelizier. On the center of fusion categories.
Paciﬁc Journal of Mathematics, 264:1–30, 2013. arXiv:1203.4180.
[5] Damien Calaque and Pavel Etingof. Lectures on tensor categories. 2004.
arXiv:math/0401246.
[6] Alexei Davydov. Twisting of monoidal structures. 1997. arXiv:q-alg/
9703001.
[7] Christopher L. Douglas, Christopher Schommer-Pries, and Noah Snyder.
Dualizable tensor categories. 2013. arXiv:1312.7188.
[8] Josep Elgueta. A strict totally coordinatized version of Kapranov and Vo-
evodsky’s 2-category 2Vect. Math. Proc. Camb. Phil. Soc., 142(407):407–
428, 2007. URL: http://arxiv.org/abs/math/0406475.
[9] Pavel Etingof, Dmitri Nikshych, and Viktor Ostrik. On fusion categories.
Annals of Mathematics, 162:581–642, 2005.
arXiv:math/0203060.
doi:
10.4007/annals.2005.162.581.
[10] Tobias Hagge and Seung-Moon Hong. Some non-braided fusion categories
of rank 3. Communications in Contemporary Mathematics, 11(4):615–637,
2009. arXiv:0704.0208.
[11] Seung-Moon Hong.
On symmetrization of 6j-symbols and Levin-Wen
hamiltonian. 2013. arXiv:0907.2204.
[12] I. Martin Isaacs. Character Theory of Finite Groups. Dover Publications,
1976.
[13] Andr´e Joyal and Ross Street. The geometry of tensor calculus II. Available
at web.science.mq.edu.au/ street/GTCII.pdf.
[14] Andr´e Joyal and Ross Street. The geometry of tensor calculus I. Advances
in Mathematics, 88:55–112, 1991. doi:10.1016/0001-8708(91)90003-p.
[15] Alexander Kirillov Jr. String-net model of Turaev-Viro invariants. 2011.
arXiv:1106.6033.
[16] Alexei Kitaev. Anyons in an exactly solved model and beyond. Annals of
Physics, 321:2–111, 2006. arXiv:cond-mat/0506438.
[17] Saunders Mac Lane. Categories for the Working Mathematician. Springer,
1997. 2nd edition.
35
[18] Michael M¨uger. From subfactors to categories and topology I. Frobenius
algebras in and morita equivalence of tensor categories. Journal of Pure
and Applied Algebra, 180:81–157, 2003.
[19] Michael M¨uger. From subfactors to categories and topology II: The quan-
tum double of tensor categories and subfactors. Journal of Pure and Applied
Algebra, 180(1):159–219, 2003. arXiv:0111205.
[20] Michael M¨uger. On the center of a compact group. International Mathe-
matics Research Notices, 2004(51):2751–2756, 2004.
[21] Michael M¨uger. Tensor categories: A selective guided tour. arXiv preprint
arXiv:0804.3587, 2008.
[22] Gregory L. Naber.
Topology, Geometry and Gauge ﬁelds: Interactions.
Springer, 2011.
[23] Siu-Hung Ng and Peter Schauenburg. Higher Frobenius-Schur indicators
for pivotal categories. 2005. arXiv:math/0503167.
[24] Dmitri Nikshych.
Non-group-theoretical semisimple Hopf algebras from
group actions on fusion categories. Selecta Mathematica, 14(1):145–161,
2008. arXiv:0712.0585.
[25] V. Ostrik. Pivotal fusion categories of rank 3 (with an Appendix written
jointly with Dmitri Nikshych). 2013. arXiv:1309.4822.
[26] Peter Selinger. New Structures for Physics, volume 813, chapter ”A survey
of graphical languages for monoidal categories”, pages 289–355. Springer,
2011. arXiv:arXiv:0908.3347.
[27] Zhenghan Wang. Topological Quantum Computation. Number 112 in Con-
ference Board of the Mathematical Sciences. Cambridge University Press,
2010.
[28] David N Yetter. Braided deformations of monoidal categories and Vassiliev
invariants. In Higher Category Theory, volume 230 of AMS Contemporary
Mathematics, pages 117–134, 1998.
[29] David N Yetter. Abelian categories of modules over a (lax) monoidal func-
tor. Advances in Mathematics, 174(2):266–309, 2003.
Mathematical Institute, University of Oxford and Mathematics Division, Stellenbosch
University
E-mail address, : brucehbartlett@gmail.com
36
