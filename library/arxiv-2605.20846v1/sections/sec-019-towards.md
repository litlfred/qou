---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-019-towards
section_title: "Towards"
section_number: null
pages: 92-99
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Towards ∞
Definition A.2.1. ((∞, 1)-category) An (∞, 1)-category is a complete Segal space X•.
That is, a simplicial object in topological spaces satisfying completeness and the Segal
condition.
See [Lur08] for details about completeness and Segal condition. See [Zha13, section
2] for a comparison between the different settings of complete Segal spaces.
Here
we specialize to the setting of topological spaces and retreat to compactly generated
Hausdorff spaces or CW spaces if pathologies arise.
Definition A.2.2. (Quasi-Category) A quasi-category is a simplicial set C such that
every map of simplicial sets f0 : Λn
i →C can be extended to an n-simplex f : ∆n →C
for 0 < i < n. We also call it an ∞-category.
Theorem A.2.3. (Joyal Tierney) There is a Quillen equivalence between the model
catgegory for quasi-categories and the model category for complete Segal spaces. In
particular, to each complete Segal space X• there is a quasi-category Q• given by Qn =
Sing(Xn)0.
Notations A.2.4. Let Cat∆be the category of simplicial categories, the objects are
simplicial categories and the morphisms are simplicial maps (i.e. maps of simplices that
are compatible with face and degeneracy maps). Let sSet be the category of simplicial
sets and simplicial maps. Let [n] = {0 < 1 < · · · < n} be the category whose objects
are 0, 1, . . . n and whose maps are orderings i < j.
Definition A.2.5. (Ordinary Nerve) The ordinary nerve of an ordinary category C is
a simplicial set defined as follows:
N(C)n = HomCat([n], C).
Specifically, N(C)n is the set of n-many composable arrows in C:
X0
f0
→X1 . . .
fn−1
→Xn.
with the face map given by
• d0 forgets the first object and the first arrow.
• dn forgets the last object and the last arrow.
• di for 0 < i < n forgets the object Xi and replaces fi−1 and fi with their
composition.
and the degeneracy maps given by inserting the identity morphisms.
To work in the setting of ∞-categories, one needs to define appropriate notions of
nerves for simplicial categories and for topological categories. We must introduce the
following notion
Definition A.2.6. (C[∆n]) is the simplicial category defined as
1. The objects are 0, 1, . . . , n
2. The mapping simplicial sets are given by
MapC[∆n](i, j) =
(
∅,
if j < i
N(Pi,j),
if i ≤j .
where Pi,j is the partially ordered set
Pi,j = {I ⊆{0, 1, . . . , n} |(i, j ∈I)
and
∀k ∈I, i ≤j ≤k} .
3. For i < j, k, the composition
MapC[∆n](i, j) × MapC[∆n](j, k) →MapC[∆n](i, k).
is induced by the map
Pi,j × Pj,k →Pi,k
(I1, I2) 7→I1 ∪I2
Example 13. Recall that the simplicial nerve N(C) of a simplicial category C is a
simplicial set N(C) ∈sSet, whose n-simplices are given by
N(C)n = HomCat∆(C[∆n], C).
Proposition A.2.7. [Lur09] Let C be a simplicial category such that MapC(X, Y ) is
a Kan complex for any X, Y ∈C. Then its simplicial nerve N(C) is an ∞-category.
Notations A.2.8. Let C be a topological category. Then there is an associated sim-
plicial category Sing(C) whose objects are those of C and whose homs are simplicial
spaces given by
MapSing(C)(x, y) = Sing(MapC(x, y)).
Remark A.2.9. A standard result is that Sing : tCat →Cat∆is the adjoint of the
geometric realization functor |.| : Cat∆→tCat, which sends a simplicial category C
to the topological category |C| whose objects are the same as those of C and whose
mapping spaces are given by
Map|C|(x, y) = | MapC(x, y)|.
Proposition A.2.10. The topological nerve N(C) of any topological category C is
defined as the simplicial nerve of Sing(C). It is an ∞-category.
Remark A.2.11. The First few levels contain the following data:
Remark A.2.12. Note that if C were an ordinary category, one may define a simplicial
category Cs and a topological category Ct. Their simplicial nerve and topological nerve
agrees with the ordinary nerve.
Definition A.2.13. (∞-operad) [Lur17a] An ∞-operad is a functor p : O⊗→N(Fin∗)
between ∞-categories satisfying
1. for every inert morphism f : ⟨m⟩→⟨n⟩in N(Fin∗) and every object C ∈O⊗
⟨m⟩=
p−1(⟨m⟩), there exists a p-coCartesian morphism f : C →C′ in O⊗lifting f. In
particular, f induces a functor f!O⊗
⟨m⟩→O⊗
⟨n⟩.
2. Let C ∈O⊗
⟨m⟩, C′ ∈O⊗
⟨n⟩, and f : ⟨m⟩→⟨n⟩a morphism in Fin∗.
Let
Mapf
O⊗(C, C′) be the union of the connected components of MapO⊗(C, C′) over f.
Choose p-coCartesian morphisms C′ →C′
i over the inert morphisms ρi : ⟨n⟩→⟨1⟩
for 1 ≤i ≤n. Then the induced map
Mapf
O⊗(C, C′) →
Y
1≤i≤n
Mapρi◦f
O⊗(C, C′
i)
is a homotopy equivalence.
3. For every collection of objects C1, . . . , Cn ∈O⊗
⟨1⟩, there exists an object C ∈O⊗
⟨n⟩
and a collection of p-coCartesian morphisms C →Ci covering ρi : ⟨n⟩→⟨1⟩.
We denote the fibre O⊗
⟨1⟩= p−1(⟨1⟩) as O and refer it as the “underlying ∞-category.”
Remark A.2.14. If condition (1) and (2) are satisfied, then condition (3) is equivalent
to
3. There is an equivalence of ∞-categories
ϕ : O⊗
⟨n⟩→O.
for all n ≥0 determined by the functors ρi
! : O⊗
⟨n⟩→O.
Definition A.2.15. (Algebra Object) Let O⊗, O′⊗be ∞-operads. An ∞-operad map
from O⊗to O′⊗is a map of simplicial sets f : O⊗→O′⊗such that
1. The following digram commutes
O⊗
O′⊗
N(Fin∗)
f
2. f carries inert morphisms to inert morphisms.
Denote by AlgO(O′⊗) the full subcategory of Fun(O⊗, O′⊗) spanned by ∞-operad
maps.
Acknowledgements The author would like to thank Ian Agol, Richard Bamler,
Ansuman Bardalai, Jacob Erlikman, Michael Hutchings, Theo Johnson-Freyd, David
Nadler, Qiuyu Ren, Luuk Stehouwer, and Jan Steinebrunner for the helpful discussions.
Bibliography
[Abr96]
Lowell Abrams. “Two-dimensional topological quantum field theories
and Frobenius algebras”. In: Journal of Knot theory and its ramifica-
tions 5.05 (1996), pp. 569–587.
[Ati88]
Michael F Atiyah. “Topological quantum field theory”. In: Publica-
tions Math´ematiques de l’IH´ES 68 (1988), pp. 175–186.
[BD95]
John C. Baez and James Dolan. “Higher-dimensional algebra and
topological quantum field theory”. en. In: Journal of Mathematical
Physics 36.11 (Nov. 1995), pp. 6073–6105. issn: 0022-2488, 1089-7658.
doi: 10 . 1063 / 1 . 531236. url: https : / / pubs . aip . org / jmp /
article/36/11/6073/394001/Higher- dimensional- algebra-
and-topological-quantum.
[Bar+14]
Bruce Bartlett et al. “Extended 3-dimensional bordism as the theory
of modular objects”. In: arXiv preprint arXiv:1411.0945 (2014).
[Bar+15]
Bruce Bartlett et al. “Modular categories as representations of the 3-
dimensional bordism 2-category”. In: arXiv preprint arXiv:1509.06811
(2015).
[BSV24]
David Ben-Zvi, Yiannis Sakellaridis, and Akshay Venkatesh. “Relative
langlands duality”. In: arXiv preprint arXiv:2409.04677 (2024).
[BBS26]
Rachael Boyd, Corey Bregman, and Jan Steinebrunner. The prime de-
composition fibre sequence for moduli spaces of reducible 3-manifolds.
2026. arXiv: 2604.02099 [math.GT]. url: https://arxiv.org/
abs/2604.02099.
[CS19]
Damien Calaque and Claudia Scheimbauer. “A note on the (∞, n)–category
of cobordisms”. In: Algebraic amp; Geometric Topology 19.2 (Mar.
2019), pp. 533–655. issn: 1472-2747. doi: 10.2140/agt.2019.19.
533. url: http://dx.doi.org/10.2140/agt.2019.19.533.
[CR18]
Nils Carqueville and Ingo Runkel. “Introductory lectures on topolog-
ical quantum field theory”. en. In: Banach Center Publications 114
(2018), pp. 9–47. issn: 0137-6934, 1730-6299. doi: 10.4064/bc114-1.
url: http://www.impan.pl/get/doi/10.4064/bc114-1.
[Cer70]
Jean Cerf. “La stratification naturelle des espaces de fonctions diff´erentiables
r´eelles et le th´eor`eme de la pseudo-isotopie”. en. In: Publications
Math´ematiques de l’IH´ES 39 (Jan. 1970), pp. 5–173. issn: 0073-8301,
1618-1913. doi: 10 . 1007 / BF02684687. url: https : / / pmihes .
centre-mersenne.org/articles/10.1007/BF02684687/ (visited
on 05/03/2026).
[Dij89]
Robertus Henricus Dijkgraaf. “A geometrical approach to two-dimensional
conformal field theory”. In: Ph. D. Thesis (1989).
[Fre09]
Daniel Freed. “Remarks on Chern-Simons theory”. en. In: Bulletin
of the American Mathematical Society 46.2 (Jan. 2009), pp. 221–254.
issn: 1088-9485, 0273-0979. doi: 10.1090/S0273-0979-09-01243-9.
url: https://www.ams.org/bull/2009-46-02/S0273-0979-09-
01243-9/.
[Fre12]
Daniel S. Freed. Lecture 23: An Application of Morse-Cerf Theory.
Lecture notes for Bordism: Old and New (M392C, Fall 2012). De-
cember 27, 2012. Accessed May 3, 2026. Dec. 2012. url: https://
people.math.harvard.edu/~dafr/M392C-2012/Notes/lecture23.
pdf.
[Hat08]
Allen Hatcher. “Diffeomorphism groups of reducible 3-manifolds”.
In: Available at pi. math. cornell. edu/hatcher/Papers/DR3M. pdf
(2008).
[Hir76]
Morris W. Hirsch. Differential Topology. Vol. 33. Graduate Texts
in Mathematics. New York, NY: Springer New York, 1976. isbn:
9781468494518 9781468494495. doi: 10.1007/978-1-4684-9449-5.
url: http://link.springer.com/10.1007/978-1-4684-9449-5
(visited on 05/01/2026).
[Jor16]
David Jordan. Topological Field Theories: Lecture Notes of the Work-
ing Seminar at The Hodge Institute. Lecture notes. Seminar organ-
iser: D. Jordan. Notes taken by Jenny August, Matt Booth, Juliet
Cooke, and Tim Weelinck. 2016. url: https://webhomes.maths.
ed.ac.uk/~djordan/lecture_notes_tft_seminar.pdf (visited on
05/04/2026).
[JT07]
Andr´e Joyal and Myles Tierney. “Quasi-categories vs Segal spaces”.
In: Contemporary Mathematics 431.277-326 (2007), p. 10.
[Juh18]
Andr´as Juh´asz. “Defining and classifying TQFTs via surgery”. In:
Quantum Topology 9.2 (2018), pp. 229–321.
[Kap10]
Anton Kapustin. “Topological field theory, higher categories, and their
applications”. In: Proceedings of the International Congress of Math-
ematicians 2010 (ICM 2010) (In 4 Volumes) Vol. I: Plenary Lectures
and Ceremonies Vols. II–IV: Invited Lectures. World Scientific. 2010,
pp. 2021–2043.
[KW07]
Anton Kapustin and Edward Witten. “Electric-magnetic duality and
the geometric Langlands program”. In: Communications in number
theory and physics 1.1 (2007), pp. 1–236.
[Kel64]
G.M Kelly. “On MacLane’s conditions for coherence of natural asso-
ciativities, commutativities, etc.” en. In: Journal of Algebra 1.4 (Dec.
1964), pp. 397–402. issn: 00218693. doi: 10.1016/0021-8693(64)
90018- 3. url: https://linkinghub.elsevier.com/retrieve/
pii/0021869364900183 (visited on 05/04/2026).
[Koc03]
Joachim Kock. Frobenius Algebras and 2D Topological Quantum Field
Theories. Cambridge: Cambridge University Press, 2003. isbn: 9780511615443.
doi: 10.1017/CBO9780511615443. url: https://www.cambridge.
org/core/books/frobenius- algebras- and- 2d- topological-
quantum - field - theories / A6438118DFADFD27175779F1FC0FF7CB
(visited on 05/01/2026).
[LV14]
Pascal Lambrechts and Ismar Voli´c. Formality of the little N-disks
operad. eng. Online-Ausg. Memoirs of the American Mathematical
Society. Providence, Rhode Island: American Mathematical Society,
2014. isbn: 9780821892121.
[Lur08]
Jacob Lurie. “On the Classification of Topological Field Theories”. en.
In: Current Developments in Mathematics 2008.1 (2008), pp. 129–280.
issn: 10896384, 21644829. doi: 10.4310/CDM.2008.v2008.n1.a3.
url: https://link.intlpress.com/JDetail/1806709566404542466
(visited on 05/01/2026).
[Lur09]
Jacob Lurie. Higher Topos Theory (AM-170): Princeton University
Press, Dec. 2009. isbn: 9781400830558. doi: 10.1515/9781400830558.
url: https : / / www . degruyter . com / document / doi / 10 . 1515 /
9781400830558/html (visited on 05/04/2026).
[Lur17a]
Jacob Lurie. Higher Algebra. Version dated September 2017. Sept.
2017. url: https://www.math.ias.edu/~lurie/papers/HA.pdf.
[Lur17b]
Jacob Lurie. Higher Algebra. Version dated September 18, 2017. Sept.
2017. url: https://people.math.harvard.edu/~lurie/papers/
HA.pdf.
[Mac94]
Saunders Mac Lane. Categories for the working mathematician. eng.
Corr. 6th print. Graduate texts in mathematics 5. New York: Springer,
1994.
[Mar16]
Bruno Martelli. “An introduction to geometric topology”. In: arXiv
preprint arXiv:1610.02592 (2016).
[May97]
J Peter May. “Operads, algebras, and modules”. In: Contemporary
Mathematics 202 (1997), pp. 15–32.
[Sch14]
Claudia Isabella Scheimbauer. “Factorization homology as a fully ex-
tended topological field theory”. PhD thesis. ETH-Z¨urich, 2014.
[Seg88]
Graeme B Segal. “The definition of conformal field theory”. In: Dif-
ferential geometrical methods in theoretical physics. Springer, 1988,
pp. 165–171.
[Ste26]
Jan Steinebrunner. The surface category and tropical curves. 2026.
arXiv: 2111.14757 [math.AT]. url: https://arxiv.org/abs/
2111.14757.
[Wit82]
Edward Witten. “Supersymmetry and Morse theory”. In: Journal of
differential geometry 17.4 (1982), pp. 661–692.
[Wit10]
Edward Witten. “Geometric Langlands from six dimensions”. In: A
Celebration of the Mathematical Legacy of Raoul Bott, in: CRM Proc.
Lecture Notes 50 (2010), pp. 281–310.
[Zha13]
Yan Zhao. “Extended topological field theories and the cobordism
hypothesis”. PhD thesis. Master’s thesis, Universit´e Paris XI (Paris-
Sud) and Universita degli studi . . ., 2013.
