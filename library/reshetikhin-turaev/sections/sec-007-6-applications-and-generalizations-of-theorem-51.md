---
doc_id: reshetikhin-turaev
doc_title: "Ribbon graphs and their invariants derived from quantum groups"
section_id: sec-007-6-applications-and-generalizations-of-theorem-51
section_title: "Applications and Generalizations of Theorem 5.1"
section_number: 6
pages: 17-20
source_pdf: Reshetikhin_Turaev.pdf
source_sha256: 7ead97555a25d357
toc_source: inferred
doc_brief: "Ribbon graphs and their invariants derived from quantum groups — The generalization of Jones polynomial of links to the case of graphs in R 3 is presented."
---
6. Applications and Generalizations of Theorem 5.1 
6.1. Isotopy lnvariants of Coloured Links. A link in R 3 is a finite set of disjoint 
oriented smooth circles imbedded in R 3. The circles are called the components of 
the link. Fix a ribbon Hopf algebra A. An A-colouring of the link is a function 
associating with each component an A-module of finite dimension over the ground 
field. A link is called framed if each component is provided with an integer. As 
usual, one introduces the isotopy relation for coloured framed links [Re2]. 
Each framed link L determines a ribbon (0, 0)-graph FL, consisting of several 
annuli. Namely, let L~ ..... L k be the components of L and let rex, ...,mk be the 
associated integers. Let A i be the.annulus in R 3 with the oriented core L~ and such 
that the linking number of two circles making 0Ai is equal to m~. Assume that the 
annuli A1,..., A~ are disjoint. Compressing ? A~ into R 2 x (0, 1) we get the desired 
ribbon (0, 0)-graph F L. Each colouring of L gives rise to a colouring of F L in the 
obvious fashion. The formula L~--~F L defines a bijective correspondence between 
the isotopy types of coloured framed links and the isotopy types of HCDR-graphs 
which consist of annuli. 
Note that for an arbitrary HCDR-graph F which has zero number of border 
ribbons the operator F(F) is a linear endomorphism of the ground field, i.e. the 
multiplication by an element of this field. This element is an isotopy invariant of F. 
In particular, with each framed coloured link L we may associate its isotopy 
invariant F(FL) which is an element of the ground field. For instance, if 
A = Uh(SI,(~) ), (cf. Sect. 7), if all integers which determine the framing of L are 
chosen to be zero, and if the colours of all components of L are chosen to be the 
vector representation of A in C" then the invariant F(FL) depends on q = e h as a 
polynomial. Up to a reparametrization this polynomial equals PL(q",q--q-1), 
where PL is the 2-variable Jones-Conway polynomial of L. In the case n --2 we get 
the Jones polynomial of L. For A = UhG, G = so(n), sp(2k) a similar construction 
gives an infinite set of l-variable reductions of the 2-variable Kauffman 
polynomial of L (see [Tu~]). The invariants corresponding to the exceptional Lie 
algebras and to the spinor representation of UhSO(n) seem to be new (see IRe1] ). 
6.2. Even Graphs. A HCDR-graph is called even if it may be obtained from graphs 
_+ 
~v, r-~v, Xv, w, F(f q, tf) and the graphs Z~, w shown in Fig. 9 by applications of 
the operations | 
and o. 
There is a simple necessary and sufficient criteria which enables one to decide if 
a given HCDR-graph is even. Draw a picture of this graph so that all coupons are 
represented by rectangles with horizontal bases (as in Figs. 1, 2 and 4). The bases of 
ribbons will be automatically horizontal. Assume also that white sides of the 
coupons are turned up and that all ribbons lie "parallel" to the plane of the picture, 
i.e. have no twists (cf. Fig. 1). Now, moving along the directed core of a ribbon or an 
annulus one meets a certain number of local extremums ,'-,~, r 
~_~, ~ of the height 
function. Compute the number of left oriented extremums ~..J, r 
lying on the 
Fig. 9 
Z,~,w 
Zv.w 
Y~.w 
Yv,w 
18 
N. Yu. Reshetikhin and V. G. Turaev 
ribbon (respectively the annulus). It is a simple topological exercise to show that a 
HCDR-graph is even if and only if these numbers are even for all ribbons and 
annuli of the graph. For example, the 1-ribbon graphs r 
~_J do not satisfy this 
criteria and therefore they are not even. The HCDR-graph F L corresponding to a 
framed coloured link L is even if and only if all framing numbers of L are odd. 
Let (A,R,v) and (A,R,v') be two ribbon Hopf algebras with the same 
underlying quasitriangular Hopf algebras. Let F, F' be the corresponding functors 
HCDR(A)-*RepD A. It follows directly from definitions that the values ofF, F' on 
+ 
~-.~v, r-'~v, Xf. w, F(f, rl, tl') are the same. Using the assumption that v, v' lie in the 
centre of A one easily shows that 
-+ 
' 
+ 
' 
F(Zv, w) = F (Zv, w). This implies that on the set of 
even graphs we have F = F'. In other words, for even graphs the functor F does not 
depend on the choice of v. 
Moreover, for even A-coloured HCDR-graphs we can define operators F 
without any use of v, i.e. for such graphs we may use an arbitrary quasitriangular 
Hopf algebra (A, R). Here is a sketch of the construction. First, extent the ground 
field to an algebraically closed field. Note that each representation of A may be 
extended to a representation of A (see Sect. 3.3); we use that for any finite- 
dimensional operator N over an algebraically closed field there exists an operator 
d acting in the same vector space such that d2= N and d commutes with all 
operators commuting with 9). Thus A-colouring giver rise (non-uniquely) to an 
~-colouring. Apply now the functor F = Fa and the reduction homomorphism 
RepD .4--,RepD A. The composition restricted to even graphs does not depend on 
the choice of square roots. 
6.3. Theorem. (An extension of Theorem 5.1). Let (A,R,v) be a ribbon I-Iopf 
algebra. Assume that for each A-module V we have fixed two invertible A-linear 
operators 0~, 0 v : V--,V. There exists a unique eovariant functor Fo:CDR(A) 
~Rep[] A which has the following properties: (i) on the subcategory HCDR(A) of 
CDR(A) Fo equals F; (ii) Fo preserves the tensor product; (iii) for any A-module V 
Vo(J~)=O ~ 
and 
Fo(Jv)=Ov. 
We give here a construction of F o. Note that an arbitrary CDR-graph T with k 
bottom ends and E top ends may be uniquely represented in the form 
(11@... | 
~) o ig o (It | 
Q/k), where iF is a homogeneous CDR-graph and each 11 
is either 19 or J), ~ = +_ 1, each 1i is either I} or K}, e-- + 1 (see Figs. 2 and 3). Put 
F0(J~) = 0}z, Fo(K~) = (0~)- 1, Fo(i~) = idw, where V + = V, V- = V ~. Put 
F(/') = (F0(I 1) | 
| Fo(i~)) o F(F) o (F o(11) @... @ F o(&)) . 
All the properties of Fo easily follows. 
6.4. Remarks. 1. It is obvious that the operator invariant F(F, 2) of a directed 
ribbon graph F with a colouring 2 is additive with respect to the colours of the 
coupons of F. This invariant is also additive with respect to the colours of those 
ribbons which connect 2 distinct coupons. More exactly, if the colour of such a 
ribbon B is a direct sum of A-modules, V, W then we split the colours of the 
coupons incident to B and obtain thus two A-colourings, say, 2' and 2" of F. Here, 
)7 and 2" coincide outside B and the incident coupons and )J(B)---V, ,V'(B)= W. 
Ribbon Graphs Derived from Their Invariants 
19 
Then F(F, 2)=F(F,2')+F(F, 2"). This follows from the isotopy invariance of 
F(F, ~), since B is isotopic to a standard plane vertical ribbon for which the 
assertion is obvious. Similarly, the invariant F(F, 2) is additive with respect to the 
colours of annuli and of those ribbons which connect a coupon with one of the 
border segments (4.2.1). Note also that each annulus of F may be replaced by two 
coupons and two ribbons without changing F(F, 2) (see Fig. 10). 
2. Let F be a HCDR-graph and let the colour of a ribbon B of F is the tensor 
product V| Woftwo A-modules, V, W. Cutting out B alongits core we get two new 
ribbons which make together with F\B another DR-graph, say, F'. The colouring 
off obviously induces a colouring of F'. Note that looking on B from its white side 
we see one of the new ribbons to lie to the left of the directed core orB, the other one 
lying to the right; we colour them respectively by V and W. It turns out that F(F') 
=F(F). This follows from 3.1.2, 3.1.3; these equalities directly imply equalities 
presented in Fig. 11. A similar assertion holds for each annulus coloured by a 
tensor product V| 
We may replace such an annulus by two subannuli, 
obtained by cutting along the core, and coloured V and W. Such a replacement 
does not change F(F). 
3. The functor F:HCDR(A)~Repc~A is surjective since each morphism 
f" ~--~ t/' of RepD A is the image of the graph F(f, t/, t/'). Moreover, f may be always 
presented by a 3-valent HCDR-graph, i.e. a graph whose coupons are all incident 
to =< 3 ribbons. This follows from the fact that the local operation on the HCDR- 
graphs depicted in Fig. 12 preserves the image of the graph in Rep[]A and 
decreases the valence of the coupon by I by virtue of introducing an additional 
coupon of valence 3. Note that in Fig. 12d is the identical endomorphism of 
Vk-1@ Vk and the colours f, f' are equal. 
Fig. 10 
Fig. 11 
V 
V 
W 
V 
VeW 
V 
W 
V 
V~W 
V 
Fig. 12 
VK 
VK-2 
VK- 1 
V K 
20 
N. Yu. Reshetikhin and V. G. Turaev 
4. To colour a directed ribbon graph is a problem in itself. It is natural to 
colour such a graph F in two steps: first ribbons and then coupons. The second 
step is somewhat more complicated as it is not easy to describe the 
A-homomorphisms in a combinatorial language. The following construction gives 
a useful method of colouring coupons. 
Assume that the ribbons of F are coloured. Assume that with each coupon Q of 
F we have associated a DR-graph F e with coloured ribbons so that the border 
ribbons of F a have the same directions, colours, and orientations (white/black) as 
the ribbons of F incident to Q. Gluing F e instead of Q we get a "simpler" directed 
ribbon graph with coloured ribbons. This in principle enables us to reduce the 
problem of colouring coupons of F to the same problem for simpler graphs {Fo}. 
For instance, in many cases we may take FQ without any coupons at all. (Ribbon 
graphs without coupons are called ribbon tangles.) This construction suggests a 
specific point of view on coupons: one may think that coupons are black boxes 
hiding inside some blocks {Fo}.
