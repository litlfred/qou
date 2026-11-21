---
doc_id: 04010141
doc_title: "Cellular algebras and diagram algebras in representation theory"
section_id: sec-001-cellular-algebras-and-temperley-lieb-algebras
section_title: "Cellular algebras and Temperley-Lieb algebras"
section_number: null
pages: 3-11
source_pdf: 04010141.pdf
source_sha256: b86b204b05453a5d
toc_source: inferred
doc_brief: "Cellular algebras and diagram algebras in representation theory — We discuss a circle of ideas for addressing problems in repre- sentation theory using the philosophy of cellular algebras, applied to"
---
Cellular algebras were first defined in [15] in terms of the existence 
of a basis with specified multiplicative properties. Subsequently, there 
has been a significant literature (cf. [25], [26], [27], [28] and [13]) in 
which structural definitions have been given, in terms of the existence 
of certain filtrations, and in which cellular algebras have been compared 
with quasi-hereditary algebras; in particular much is now known about 
their characterisation in terms of global dimension, Cartan matrix and 
representation type. The main point of a cellular structure is that it 
is preserved under specialisation, so that cellularity is a particularly 
effective way of studying algebras which are not semisimple, but are 
deformations of semisimple algebras. 
In this work, we shall use the original definition. Let R be a commu-
tative ring with 1, and let A be an R-algebra which is free over R, and 
which we assume for the moment to be of finite rank (although many 
of the concepts will be applied when A has infinite rank). To specify 
a cellular structure for A, we require a "cell datum" , which consists of: 
(i) a poset T, (ii) for each t E T, a set M(t), and (iii) an injection 
IltETM(t) x M(t) -SA, whose image is an R-basis {C1r} of A which 
satisfies 
' 
aC1,r = L ra(S', S)C1',T + lower terms 
(2.1) 
S'EM{t) 
(a E A,ra(S',S) E R), 
where "lower terms" indicates a linear combination of basis elements 
c%1/ T" with t' < t. In addition, one requires that the map C1 T I-+ C} S> 
exte~ded R-linearly, be an anti-automorphism a~---+ a* of A. ' 
' 
We shall review briefly the representation theory of cellular algebras. 
To start with, for each t E T, one has the cell module W(t); this has 
R-basis {Cs I S E M(t)}, and A acts on the left by the rule 
(2.2) 
a.Cs = L ra(S', S)Cs' for a E A, S E M(t). 
It follows from 2.1 that 2.2 defines an action. 
The cell module W(t) has a natural R-bilinear form <Pt 
W(t) X 
W ( t) --+ R, defined by 
(2.3) 
(C1,r) 2 = <Pt(Cs,Cr)C1,r + lower terms. 
It is easily shown ([15]) that the form <Pt is symmetric and invariant 
under the action of A, i.e. that for any two elements x, y E W(t) and 
144 
J.J. Graham and G.I. Lehrer 
a E A, we have cf>t(x,y) = cf>t(y,x) and cf>t(a.x,y) = cf>t(x,a*.y). An 
immediate consequence is that the radical Rad(t) = Radcf>t = {x E 
W(t) I cf>t(x, y) = 0 for all y E W(t)} of cf>t is an A-submodule of W(t). 
Write L(t) := W(t)j Rad(t); clearly L(t) is zero if and only if the form 
cf>t = 0. 
The next statement summarises the representation theory of A when 
R is a field. 
Proposition 2.4 ([15]). 
Maintain the above notation, and in ad-
dition assume that R is a field. Let T 0 be the set of t E T such that 
L(t) -=/- 0 {or equivalently cf>t-=/- 0}. Then (i) The modules L(t) {t E ro} 
are absolutely irreducible and form a complete set of representatives of 
the distinct isomorphism classes of irreducible A-modules. 
(ii) For s E T, t E ro let dst be the multiplicity of L(t) in W(s). 
Then the decomposition matrix D = (dst) is upper unitriangular. In 
particular Hom(W(tl), W(t2 )) = 0 unless t1 ;?: t 2 . 
(iii) For s1, s2 E T 0 , let C81 ,82 be the multiplicity if the irreducible 
module L(s2) in the projective cover P(s1) of W(s 1). If C is the (Car-
tan) matrix ( Cs, ,s2) then c = Dt D' where nt denotes the transpose of 
D. 
(iv) The cell module W(t) is irreducible if and only if, for all t' E 
T, t' -=1- t, Hom(W(t'), W(t)) = 0. Equivalently, the form cf>t is non-
degenerate on W ( t) . 
(v) The following assertions are equivalent. 
The algebra A is 
semisimple. Each cell module is absolutely irreducible. The forms cf>t 
are all non-degenerate. There are no non-trivial homomorphisms be-
tween distinct cell modules. 
We shall now see how these concepts apply to the Temperley-Lieb 
algebras of type A and B. Let R be a commutative ring with 1; write 
Rx for the group of invertible elements of R and let q, Q E Rx. For 
any invertible element x E R, write Dx = -(x + x-1 ). Our notation 
for parameters, which may appear arbitrary, is chosen with a view to 
the links with Heeke algebras described below. The usual Temperley-
Lieb algebra TLn(q) may be described in terms of planar diagrams (see 
[20], [10] or [15]) in a way which is well known. The Temperley-Lieb 
algebra T LBn(q, Q) of type Bn has a corresponding description in terms 
of "marked diagrams" (cf. [42], [36], [37]). When the base ring is an 
algebraically closed field, TLBn(q, Q) is sometimes known as the "blob 
algebra" (see [6]). The algebra TLn(q) is realised as the subalgebra of 
TLBn(q, Q) which is spanned by unmarked diagrams. We describe now 
T LBn(q, Q) as a cellular algebra, using the language of [16] for diagrams. 
Cellular algebras and diagmm algebras 
145 
If t, n are positive integers of the same parity, a finite (planar) dia-
gram J1. : t -----+ n is represented by a set of non-intersecting arcs which 
are contained in the "fundamental rectangle" (see below). These arcs 
divide the fundamental rectangle into regions, among which there is a 
unique "left region" as shown below. 
n 
t 
A marked diagram is a (finite planar) diagram, where the interior 
of the boundary arcs of the leftmost region may be marked with one or 
more • symbols ("marks") (see below). 
n 
t 
The R-linear combinations of unmarked diagrams from t to n constitute 
the morpbisms in the Temperley-Lieb category T, where the objects are 
the non negative integers Z;:::0 . If t, n respectively denote the number of 
bottom and top nodes in a diagram D, then D is a morphism from t 
ton in T. Composition of morphisms corresponds to concatenation of 
diagrams, with closed loops being deleted and replaced by the scalar 8q. 
In the composition D 1D2 of diagrams D 1 and D2, D 1 is placed above 
I 
I 
I 
I 
I 
I 
I 
146 
J.J. Graham and G.I. Lehrer 
D 2 . This is consistent with morphisms being composed from right to left. 
The endomorphisms of nET form an algebra Homr(n,n) ~ TLn(q). 
Marked diagrams may be similarly concatenated according to rules we 
shall now state; this produces a new category, 'll'lffi, the Temperley-Lieb 
category of type B. The composition rules are as follows. 
A marked diagram is proper if it has no loops and each arc has at 
most one mark. The following rules reduce the concatenation of any two 
diagrams to an R linear combination of proper diagrams: 
2.5. 
(i) If J-L is a diagram and L is a loop with no marks, J-L II L = 
8q/-L· 
(ii) If, in {i}, L has one mark, J-L II L = KJ-L, where K = !J + ~. 
(iii) If some arc of J-L has more than one mark and J-L1 is the diagram 
obtained by removing a mark from the arc concerned, then J-L = 8QJ-L1 • 
Now consider the following marked diagrams from n ton. 
1 
2 
n-1 n 
i 
i + 1 
I 
I 
I 
I 
I 
I 
I 
1 
2 
n-1 n 
i 
i + 1 
co : n ___, n 
e;, : n ___, n, 1 :::; i :::; n - 1 
The next result describes TLBn(q, Q) algebraically. 
Proposition 2.6 (cf. [18, 5.8]). 
(i) The Temperley-Lieb algebra 
TLBn(q,Q) is generated as R-algebra by {c0,c1, ... ,cn-d subject to 
the relations 
(2.7) 
c6 = 8QCo 
c; = 8qci for 1 :::; i :::; n - 1 
CiCiH Ci = e;, for 1 :::; i :::; n- 2 
CiCi-1 Ci = C;, for 2 :::; i :::; n- 1 
C;,Cj = CjC;, ifli- Jl > 1, Q:::; i,j:::; n -1 
where K = !J + ~ and 8x = -(x + x- 1 ) for x E Rx. 
(ii) The elements c1, ... ,cn-1 generate a subalgebra ofTLBn(q,Q) 
isomorphic to the usual Temperley-Lieb algebra TLn(q) of type An_ 1 . 
Cellular algebras and diagmm algebras 
147 
The stated relations are easily seen to hold by 2.5. The fact that all 
relations are consequences of these depends on the connection between 
the Heeke algebra description of TLBn(q, Q) (§4 below) and the dia-
grammatic description here. The proof may be found in [42, Satz (4.5) 
p. 77]. 
We now specify the various elements of a cellular structure (see 
above) for TLBn(q, Q). Take T = {t E Z I ltl ~ n, t = n (mod 2)}, 
partially ordered as follows: t ~ s if ltl < lsi or ltl = lsi and t ~ s. 
To define the sets M(t), first take t E T, t ;::: 0. Then M(t) is 
the set of monic diagrams D : t ---+ n with no marked through strings, 
where "monic" means that there are t through strings, as in [GL2], 
where it is shown that this is equivalent to D being a monic morphism 
in the category-theoretic sense. In general, let M(t) = M(ltl). Then 
C: M(t) x M(t)---+ TLBn(q, Q) is defined as follows. LetS, T E M(t). 
Fort;::: 0, define C1 T =SoT*, where* denotes reflection in a horizontal 
axis. Fort< 0, defi'ne C1 T = s 0 Co 0 T*' where Co = eo(t) : t---+ tis the 
generator shown below 2.5. This is the diagram SoT*, with the leftmost 
through string marked. The cellular axioms above, in particular 2.1 are 
easily checked. 
The cell modules Wt(n) are now defined in complete analogy with 
the Wt,z(n) of [GL2]. For any t E T, Wt(n) has basis M(t). If t ;::: 
0, TLBn(q, Q) acts via composition in the category 'lm; explicitly, if 
DE M(t) and wE TLBn(q,Q), then w.D = wD (composition in 'lm) if 
w o D E M(t), and w.D = 0 otherwise. 
For t < 0, one may think of Wt(n) as having basis the set {Do 
co(t) I D E M(ltl)} of monic diagrams : t---+ n in 1m with the leftmost 
through string marked. Then the action of TLBn(q, Q) is essentially 
multiplication in 'lm, as in the case t ;::: 0. Thus if t < 0, then w.(D o 
eo(t)) = 0 if w o D is not monic, while w.(D o eo) = wDeo (composition 
in 'lm) if w o D is monic. 
It is easily seen ( cf. [42]) that the dimension (i.e. rank over R) of 
Wt(n) is( .. ~.,). 
2 
For each integer i with 1 ~ i ~ n-1, the diagrams {eo, c1o ... , Ci-d 
generate an algebra isomorphic to T LBi ( q, Q), and we shall require infor-
mation concerning the restriction of the cell modules Wt ( n) to the sub-
algebras TLBi(q, Q). Let us first consider the restriction of Wt(n) from 
TLBn(q,Q) to TLBn-l(q,Q) when t E T,t;::: 0. Now TLBn-l(q,Q) 
is spanned by those diagrams in TLBn(q, Q) with a string joining the 
rightmost dots in the top and bottom rows. The basis elements of Wt ( n) 
divide naturally into those which have a through string to the right-
most top dot, and those which do not. The former evidently span a 
148 
J.J. Graham and G.l. Lehrer 
TLBn_1(q,Q)- submodule isomorphic to Wt_1(n-1). A diagram in 
the latter set may be identified with a monic diagram t + 1 ---+ n - 1 by 
"pulling down" the rightmost dot from the top to the bottom row. In this 
way, the quotient of the TLBn-l(q, Q)-module Wt(n) by Wt-l(n- 1) is 
easily identified as Wt+ 1(n- 1). Using a similar argument for the case 
t ~ 0 we obtain 
Proposition 2.8. 
Let t E Z, 0 ~ ltl ~ n, n + t E 2Z. Assume 
8q =1- 0. 
(i) If t ~ 0, we have a short exact sequence 
(ii) If t < 0, we have a short exact sequence 
Here we adopt the convention that W;(k) = 0 if Iii > k. 
Repeated application of 2.8 yields 
Corollary 2.11. 
Lett E Z, 0 ~ ltl ~ n, n + t E 2Z and suppose 
t ~ 0. There is a filtration of Wt(n) by R-submodules W(i), i = n, n-
1, n- 2, ... , 1 as in 2.12 below. 
(2.12) 
Wt(n) ::::> Wt-I(n -1) ::::> • • • ::::> Wo(n- t) ::::> W-1(n- t -1) ::::> 
Wo(n- t- 2) ::::> W-1(n- t- 3) ::::> • • • ::::> Wo(2) ::::> W_l(1). 
Thus 
(2.13) 
. 
{Wt-n+i(i) ifn- t ~ i ~ n 
W(i) ~ W 0(i) ifi is even andO ~ i ~ n- t 
W_l(i) ifi is odd andO ~ i ~ n- t. 
For each i = 1, 2, 3, ... , n, W(i) is a TLBi(q, Q)-submodule of Wt(n). 
To illustrate the construction in 2.11, we note that the diagram 
Et = Et n below lies in each of the submodules W(i). 
, 
Cellular algebras and diagram algebras 
149 
n 
t 
Given the details of the cellular structure of TLBn(q, Q), all the 
results of Proposition 2.4 are available. However we turn next to the 
affine Temperley-Lieb algebra. 
§3. 
The diagram version of the affine Temperley-Lieb algebra 
There are several algebras which could be (and have been) called the 
"affine Temperley-Lieb algebra". In this section we discuss the diagram-
matic version T,::(q), which was introduced in [16, 2.7] as the algebra of 
endomorphisms of an object of the affine Temperley-Lieb category 'Jl'a 
(see [GL2, (2.5)]), and whose representation theory was completely anal-
ysed in loc. cit. using cellular theory, although the algebras are infinite 
dimensional. It also occurs independently in the work of Green [12] and 
Fan-Green (8]. We maintain the notation of the last section for R, q, etc. 
Details may be found in [GL2], but a good approximation to the picture 
is obtained if one thinks of affine diagrams as arcs drawn on the surface 
of a cylinder joining 2n marked points, n on each circle component of 
the boundary, in pairs. The arcs must not intersect, and diagrams are 
multiplied by concatenation in the usual way. These diagrams are rep-
resented by periodic diagrams drawn between two horizontal lines, each 
diagram being determined by the "fundamental rectangle", from which 
the cylinder is obtained by identifying vertical edges. In this interpre-
tation, the generators {h, ... , fn, Tn} of T:t(q) are represented by the 
diagrams shown below. 
150 
J.J. Graham and G.l. Lehrer 
1 
2 
n-1 n 
i 
i + 1 
R I I 2 
1 
2 
n-1 n 
i 
i + 1 
fn: n-> n 
fi : n -> n, 1 :=:; i :=:; n - 1 
1 
2 
3 
t 
1 
2 
t- 1 t 
To: 0-> 0 
The elements {!1, ... , fn} of the algebra T;:(q) satisfy the relations 3.1 
below. 
fl = 8q/i 
(3.1) 
lili±di = li 
fifJ = !Jfi if li- Jl ~ 2 and {i,j} =I= {1, n}, 
Further, Tn/iT;; 1 = fi+b where the index is taken mod n. We shall 
sometimes omit the subscript from the "twist" Tn when there is no am-
biguity. 
The reduction of a concatenation of affine diagrams to a linear com-
bination of diagrams is simpler that in the case of T LEn ( q, Q): circles 
which circumnavigate the cylinder (these are called infinite in [16]) re-
main; they are simply powers of To. If Dis an affine diagram and Cis a 
finite or contractible closed loop, then in the category ']['a, D II C = DqD. 
In [16], we defined cell modules Wt,z(n) for the algebra T;:(q), (where 
t E Z, 0 :=:; t :=:; n, t+n E 2Z, and z E Rx) and when R is an algebraically 
closed field of characteristic zero, completely determined their composi-
tion factors and multiplicities. We briefly review this material now. 
Recall [16] that an affine diagram from t to n is monic if it has t 
through strings. It follows that t :=:; n and t = n(mod 2). For such a 
positive integer t, let Xt be the T;:(q)-module with basis all monic affine 
Cellular algebras and diagram algebras 
151 
diagrams:t-+ n, with T;:(q) action given by composition in the category 
'II'a, modulo diagrams with fewer than t through strings. Thus Xt may 
be thought of as a quotient of the left T;:(q)-module Homya (t, n) by the 
submodule spanned by diagrams with fewer than t through strings. Let 
z E Rx. The T;:(q) module Wt,z(n) is defined as the quotient of Xt by 
the ideal generated by the set 
(3.2) 
over all affine diagrams 1 EXt, where Xz(t) = z if t-/=: 0 and Xz(O) = 
z + z- 1 . 
While the module Xt is evidently of infinite rank over R, Wt,z(n) is 
shown in [16, §2] to be free of rank ( nr:_,) over R. A basis of Wt,z(n) is 
2 
provided by the standard diagrams (see [16, 1.7, 2.7]) from t ton in 'll'a. 
The R-linear map w ~---> w*, where d* denotes the reflection of a 
diagram d E ']['a in a horizontal line defines an involution on the category 
']['a (i.e. an involutory functor from ']['a to ('ll'a)oPP), which induces an anti-
automorphism of T;:(q) for each n. Suppose p,, v are standard diagrams 
from t ton. Let cPt,z : Wt,z(n) X wt,z-1 (n)----+R be the R-linear extension 
of the map (p,,v) ~---> cf>t,z(J-L,v) = Xz(v*p,), where Xz: Tt(q)-+ R is the 
R-linear map which annihilates non-monic diagrams and takes Tf to x~ 
(see 3.2). Then cf>t,z is bilinear and ([16, (2.7)]) invariant in the sense 
that cf>t,z(wp,,v) = cf>t,z(J-L,w*v), (p,,v E Wt,z(n),w E T;:(q)). We now 
have all the ingredients of a cellular structure and can state the analogue 
of 2.4 for T;:(q). 
Definition 3.3.
