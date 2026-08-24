---
doc_id: 04010141
doc_title: "Cellular algebras and diagram algebras in representation theory"
section_id: sec-000-25-i-if-j-l-is-a-diagram-and-l-is-a-loop-with-no
section_title: "(i) If J-L is a diagram and L is a loop with no marks, J-L II L ="
section_number: 2.5
pages: 6-13
source_pdf: 04010141.pdf
source_sha256: b86b204b05453a5d
doc_brief: "Cellular algebras and diagram algebras in representation theory — We discuss a circle of ideas for addressing problems in repre­ sentation theory using the philosophy of cellular algebras, applied to"
---
8q/-L· 
(ii) If, in {i}, L has one mark, J-L II L = KJ-L, where K = !J + ~. 
(iii) If some arc of J-L has more than one mark and J-L1 is the diagram 
obtained by removing a mark from the arc concerned, then J-L = 8QJ-L1 • 
Now consider the following marked diagrams from n ton. 
1 2 n-1 n i i + 1 
I 
I 
I 
I 
I 
I 
I 
1 2 n-1 n i i + 1 
co : n ___, n e;, : n ___, n, 1 :::; i :::; n - 1 
The next result describes TLBn(q, Q) algebraically. 
Proposition 2.6 (cf. [18, 5.8]). (i) The Temperley-Lieb algebra 
TLBn(q,Q) is generated as R-algebra by {c0 ,c1, ... ,cn-d subject to 
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
Cellular algebras and diagmm algebras 147 
The stated relations are easily seen to hold by 2.5. The fact that all 
relations are consequences of these depends on the connection between 
the Heeke algebra description of TLBn(q, Q) (§4 below) and the dia­
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
generate an algebra isomorphic to T LBi ( q, Q), and we shall require infor­
mation concerning the restriction of the cell modules Wt ( n) to the sub­
algebras TLBi(q, Q). Let us first consider the restriction of Wt(n) from 
TLBn(q,Q) to TLBn-l(q,Q) when t E T,t;::: 0. Now TLBn-l(q,Q) 
is spanned by those diagrams in TLBn(q, Q) with a string joining the 
rightmost dots in the top and bottom rows. The basis elements of Wt ( n) 
divide naturally into those which have a through string to the right­
most top dot, and those which do not. The former evidently span a 
148 J.J. Graham and G.l. Lehrer 
TLBn_ 1(q,Q)- submodule isomorphic to Wt_1 (n-1). A diagram in 
the latter set may be identified with a monic diagram t + 1 ---+ n - 1 by 
"pulling down" the rightmost dot from the top to the bottom row. In this 
way, the quotient of the TLBn-l(q, Q)-module Wt(n) by Wt-l(n- 1) is 
easily identified as Wt+1 (n- 1). Using a similar argument for the case 
t ~ 0 we obtain 
Proposition 2.8. Let t E Z, 0 ~ ltl ~ n, n + t E 2Z. Assume 
8q =1- 0. 
(i) If t ~ 0, we have a short exact sequence 
(ii) If t < 0, we have a short exact sequence 
Here we adopt the convention that W;(k) = 0 if Iii > k. 
Repeated application of 2.8 yields 
Corollary 2.11. Lett E Z, 0 ~ ltl ~ n, n + t E 2Z and suppose 
t ~ 0. There is a filtration of Wt(n) by R-submodules W(i), i = n, n-
1, n- 2, ... , 1 as in 2.12 below. 
(2.12) 
Wt(n) ::::> Wt-I(n -1) ::::> • • • ::::> Wo(n- t) ::::> W-1(n- t -1) ::::> 
Wo(n- t- 2) ::::> W-1(n- t- 3) ::::> • • • ::::> Wo(2) ::::> W_l(1). 
Thus 
(2.13) 
. {Wt-n+i(i) ifn- t ~ i ~ n 
W(i) ~ W0 (i) ifi is even andO ~ i ~ n- t 
W_l(i) ifi is odd andO ~ i ~ n- t. 
For each i = 1, 2, 3, ... , n, W(i) is a TLBi(q, Q)-submodule of Wt(n). 
To illustrate the construction in 2.11, we note that the diagram 
Et = Et n below lies in each of the submodules W(i). , 
Cellular algebras and diagram algebras 149 
n 
t 
Given the details of the cellular structure of TLBn(q, Q), all the 
results of Proposition 2.4 are available. However we turn next to the 
affine Temperley-Lieb algebra. 
§3. The diagram version of the affine Temperley-Lieb algebra 
There are several algebras which could be (and have been) called the 
"affine Temperley-Lieb algebra". In this section we discuss the diagram­
matic version T,::(q), which was introduced in [16, 2.7] as the algebra of 
endomorphisms of an object of the affine Temperley-Lieb category 'Jl'a 
(see [GL2, (2.5)]), and whose representation theory was completely anal­
ysed in loc. cit. using cellular theory, although the algebras are infinite 
dimensional. It also occurs independently in the work of Green [12] and 
Fan-Green (8]. We maintain the notation of the last section for R, q, etc. 
Details may be found in [GL2], but a good approximation to the picture 
is obtained if one thinks of affine diagrams as arcs drawn on the surface 
of a cylinder joining 2n marked points, n on each circle component of 
the boundary, in pairs. The arcs must not intersect, and diagrams are 
multiplied by concatenation in the usual way. These diagrams are rep­
resented by periodic diagrams drawn between two horizontal lines, each 
diagram being determined by the "fundamental rectangle", from which 
the cylinder is obtained by identifying vertical edges. In this interpre­
tation, the generators {h, ... , fn, Tn} of T:t(q) are represented by the 
diagrams shown below. 
150 J.J. Graham and G.l. Lehrer 
1 2 n-1 n i i + 1 
R I I 2 
1 2 n-1 n i i + 1 
fn: n-> n fi : n -> n, 1 :=:; i :=:; n - 1 
1 2 3 t 
1 2 t- 1 t 
To: 0-> 0 
The elements {!1, ... , fn} of the algebra T;:(q) satisfy the relations 3.1 
below. 
fl = 8q/i 
(3.1) lili±di = li 
fifJ = !Jfi if li- Jl ~ 2 and {i,j} =I= {1, n}, 
Further, Tn/iT;; 1 = fi+b where the index is taken mod n. We shall 
sometimes omit the subscript from the "twist" Tn when there is no am­
biguity. 
The reduction of a concatenation of affine diagrams to a linear com­
bination of diagrams is simpler that in the case of T LEn ( q, Q): circles 
which circumnavigate the cylinder (these are called infinite in [16]) re­
main; they are simply powers of To. If Dis an affine diagram and Cis a 
finite or contractible closed loop, then in the category ']['a, D II C = DqD. 
In [16], we defined cell modules Wt,z(n) for the algebra T;:(q), (where 
t E Z, 0 :=:; t :=:; n, t+n E 2Z, and z E Rx) and when R is an algebraically 
closed field of characteristic zero, completely determined their composi­
tion factors and multiplicities. We briefly review this material now. 
Recall [16] that an affine diagram from t to n is monic if it has t 
through strings. It follows that t :=:; n and t = n(mod 2). For such a 
positive integer t, let Xt be the T;:(q)-module with basis all monic affine 
Cellular algebras and diagram algebras 151 
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
']['a (i.e. an involutory functor from ']['a to ('ll'a)oPP), which induces an anti­
automorphism of T;:(q) for each n. Suppose p,, v are standard diagrams 
from t ton. Let cPt,z : Wt,z(n) X wt,z-1 (n)----+R be the R-linear extension 
of the map (p,,v) ~---> cf>t,z(J-L,v) = Xz(v*p,), where Xz: Tt(q)-+ R is the 
R-linear map which annihilates non-monic diagrams and takes Tf to x~ 
(see 3.2). Then cf>t,z is bilinear and ([16, (2.7)]) invariant in the sense 
that cf>t,z(wp,,v) = cf>t,z(J-L,w*v), (p,,v E Wt,z(n),w E T;:(q)). We now 
have all the ingredients of a cellular structure and can state the analogue 
of 2.4 for T;:(q). 
Definition 3.3. Let Aa(n)+ be the set 
(3.4) Aa(n)+ = {(t,z) It E Z~o, 0::::; t::::; n, n-t E 2Z; z E Rx}. 
Define Aa(n) by 
(3.5) 
Define the equivalence relation ~ on A a ( n) + as that which identifies 
(0, z) and (0, z- 1) for all z E Rx, and write 
(3.6) 
Aa(n) 0 = Aa(n)/ ~ 
Aa(n)O+ = Aa(n)+ / ~ 
If (t1, zl), (t2, z2) E Aa(n)+, then Wt1 ,z1 (n) ~ Wt2 ,z2 (n) if (tb z1) ~ 
(t2 , z2 ). Thus Aa(n) 0+ plays the role ofT in §2. We write Radcf>t,z for 
152 J.J. Graham and G.I. Lehrer 
the submodule {x E Wt,z(n) I l/Jt,z(x, y) = 0 for ally E Wt,z-1 (n)} of 
Wt,z(n). 
Theorem 3. 7 ([16, (2.8)]). Let R be an algebraically closed field 
and maintain the above notation. 
(i) For (t, z) E Aa(n)+, Lt,z(n) := Wt,z(n)/Radl/Jt,z is either an 
{absolutely) irreducible T:;(q) module or zero, and Lt,z(n) =1- 0 if and 
only if (t, z) E Aa(n). 
(ii) All irreducible T:;(q) modules are realised thus, and if (t1, zi) -::f. 
(t2,z2), then Lt,,z 1(n) '1- Lt2 ,z2 (n). 
(iii) The cell module Wt,z ( n) is irreducible if and only if for any 
(t',z') E Aa(n) 0 , (t',z') =1- (t,z) we have 
Equivalently, the form l/Jt,z is a perfect pairing. 
It follows that the distinct irreducible T:;(q)-modules are 
parametrised by A a ( n) 0 , while the distinct cell modules are parametrised 
by A a ( n) O+. These two sets therefore play the roles of T 0 and T re­
spectively in §2. Where there is little danger of confusion, we abuse 
notation by denoting the elements of Aa(n) 0+ as pairs (t, z), rather than 
equivalence classes of pairs. Thus we speak of Wt,z(n) and Lt,z(n) for 
(t, z) E Aa(n) 0+. It follows from (3.7) that to understand the com­
position factors of the T:;(q)-module Wt,z(n), it suffices to understand 
the spaces Homr;:(q)(Ws,y(n), Wt,z(n)) for all pairs (t, z), (s, y). This 
analysis is caried out in [16], and leads to the following results. 
Let ~ be the partial order on Aa(n)+ which is generated by the 
0 0 
preorder-< which stipulates that (t,z)-< (s,y) if 
(3.8) 
0 ::; t ::; s ::; n, s =t + 2£ (£ E Z, £ > 0) and 
z2 = q•(s,z)s and y = zq-<(s,z)f. for E(s, z) = ±1. 
Note that 3.8 implies that 
(3.9) 
and 
(3.10) (t, z) ~ (t', z') ==} zt = (z'/. 
0 
It suffices to verify 3.10 when (t, z) -< (t', z'), in which case it follows 
easily from 3.8. 
Cellular algebras and diagram algebras 153 
It is easily verified that [ 17, 4.1] the partial order j on A a ( n) + in­
duces a partial order, also denoted j, on the set A0 (n) 0+ = A0 (n)+ J ~. 
The following result is proved in [16, Theorem 5.1]. 
Theorem 3.11. Let R be a field of characteristic 0 or p > 0, 
where pe > n and e is the multiplicative order of q2 • Then (i) We have 
(3.12) . {1if(t,z)j(s,y) dlmHomT"(q)(Ws,y(n), Wt,z(n)) = . 
n 0 otherwzse 
(ii) In the Grothendieck group r(T;(q)), we have for any (t, z) E A0 (n)0 +, 
(3.13) Wt,z(n) = 
(s,y)EA"(n)O 
(t,z)j(s,y) 
Thus the matrix expressing the cell modules in terms of the irre­
ducibles in r(T;(q)) is upper unitriangular, and has entries 0 or 1. Now 
if (t,z) is confined to A0 (n) 0 , the relation 3.13 can clearly be inverted. 
The result is (cf. [17, Theorem (4.5)]) 
Theorem 3.14. In the notation above, if(t,z) E A0 (n) 0 , 
(3.15) Lt,z(n) = 
(s,y)EA"(n)O 
(t,z)j(s,y) 
where nts,y = 0 or ±1. ,z 
§4. Interrelationships among various Heeke and Temperley­
Lieb algebras 
Our purpose in this section is to give a concise statement of the var­
ious connections among several Heeke algebras and Temperley-Lieb al­
gebras. Behind these connections are facts concerning generalised Artin 
groups and their interpretation in terms of braids and ribbons. The topo­
logical background may be found in [7] and [39], and a more leisurely 
exposition may be found in [18, §2].
