---
doc_id: arxiv-2301.02038v1
doc_title: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Diﬀerential Equations"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a"
---
Systems of algebraic equations can be encoded geometricall y in an algebraic
variety. This apparently harmless observation is the start ing point for the develop-
ment of such a successful branch of modern Mathematics as Alg ebraic Geometry.
One of the leading principles behind most of the mathematica l work of Alexandre
M. Vinogradov is that Partial Diﬀerential Equations (PDEs) should be treated in
a similar way. Namely, let x = (x1,...,x n) be some independent variables, let
u = (u1,...,u m) be some dependent variables, and let
(0.1) E0 :Fa(x,...,u I,... ) = 0,
a = 1 ,...,r , be a system of possibly non-linear PDEs, where a multi-inde x I
denotes multiple partial derivatives with respect to the x’s. Adding to (0.1) all its
2020 Mathematics Subject Classiﬁcation. Primary 58A15, 58A20; Secondary 17B56, 55T25,
58A12, 70S05.
Key words and phrases. Partial diﬀerential equations, jet spaces, horizontal coh omology,
C -spectral sequence, secondary calculus.
1
2 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIANO
total derivatives results in a new but equivalent system of i nﬁnitely many PDEs
(0.2) DJFa(x,...,u I,... ) = 0.
Here DJ denotes multiple total derivatives of arbitrarily high ord er with respect
to the x’s. Now, interpret (x,...,u I,... ) as independent coordinates on an ∞-
dimensional manifold J ∞. Then (0.2) can be interpreted as deﬁning a (generically
∞-dimensional) submanifold E ⊆ J ∞, the ∞-prolongation of E0. This submani-
fold is canonically equipped with an involutive distributi on C , called the Cartan
distribution, spanned by the total derivatives Di|E , i = 1,...,n . The pair (E, C )
is, in the terminology of Vinogradov and his school, a diﬃety 1 (from the words
diﬀ erential equation and var iety) and contains most of the relevant information
about the original system E0 (see, e.g., the extensive monographs [ 2, 11, 27 ] on
the subject). According to Vinogradov, the diﬃety (E, C ) should be considered as
the ultimate geometric portrait of E0. In other words, diﬃeties are to PDEs what
algebraic varieties are to algebraic equations. However th e geometry of a diﬃety
is much more intricate than that of an algebraic variety. Nam ely, while solutions
of a system of algebraic equations are points of an algebraic variety and they do
not possess any internal structure, solutions of a system of PDEs E0 are integral
submanifolds of the Cartan distribution on the diﬃety (E, C ) and they do possess
internal structure. As a consequence the space of solutions of a PDE share some
features of the leaf space of a foliation (and it is the leaf space of a foliation when
dim E <∞) and should be treated as a stack rather than as an ordinary sp ace
[17, 1, 4 ]. This is exactly where homological and homotopical algebr a come into
play when trying to develop a general theory of PDEs. A fundam ental achievement
of Vinogradov is that there is a cohomological replacement f or diﬀerential calculus
on the space of solutions of a PDEs . Vinogradov used to call such formal calculus
Secondary Calculus, because of an analogy with secondary quantization in physi cal
ﬁeld theory [ 26, 2, 27 ]. The main building blocks of Secondary Calculus are the
leaf-wise cohomologies of the Cartan distribution, often c alled horizontal De Rham
cohomologies. Most of the coordinate free properties of a PDE can be expres sed in
terms of horizontal cohomologies: symmetries, conservati on laws, variational prin-
ciples, etc., to name a few. Additionally, horizontal cohom ologies can be interpreted
as smooth functions, vector ﬁelds, diﬀerential forms on the space of solutions of the
PDE. One of the main features of horizontal cohomologies sup porting this interpre-
tation is that they possess the correct algebraic structures (those that we expect
from functions, vector ﬁelds, diﬀerential forms). In summa ry, Secondary Calculus
is the collection of all these algebraic structures.
In the ultimate idea of Vinogradov this fascinating constru ctions should be
studied in their homotopy aspects. More precisely, Vinogra dov conjectured that
what is important is not really horizontal cohomology but ra ther the homotopy
type of the horizontal De Rham algebra, and the homotopy cate gory (or even the
derived category) of diﬀerential graded modules over it [ 27, Chapter 5]. Notice that
this conjecture (together with the interpretation of the sp ace of solutions of a PDE
as a stack), is somehow complementary to the interpretation of a PDE as a derived
zero locus and, in the particular case of an Euler-Lagrange P DE, as a derived
critical locus (see, e.g., [ 23], and references therein), and suggests a relationship
to Homotopical and Derived Geometry [ 20, 21, 19 ] that, unfortunately, to the
1To the best of our knowledge, the term diﬃety appeared for the ﬁrst time in [ 24].
