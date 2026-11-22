---
doc_id: reshetikhin-turaev
doc_title: "Ribbon graphs and their invariants derived from quantum groups"
section_id: sec-001-2-compact-braided-categories
section_title: "Compact Braided Categories"
section_number: 2
pages: 2-4
source_pdf: Reshetikhin_Turaev.pdf
source_sha256: 7ead97555a25d357
toc_source: inferred
doc_brief: "Ribbon graphs and their invariants derived from quantum groups — The generalization of Jones polynomial of links to the case of graphs in R 3 is presented."
---
2.1. Monoidal Categories (see [Ma, JS]). A monoidal category C = (C o, | 
I, a, r, •) 
consists of a category Co, a covariant functor (the tensor product) 
| : C o x Co-~C o, an object I of Co, and natural isomorphisms 
a = avvw : (U | V) | W--* U |174 
W), 
r=rv: V| 
E=dv:I| 
Ribbon Graphs Derived from Their Invariants 
3 
t~ 
(where U, V, W are arbitrary objects of Co) so that the following two diagrams 
commute: 
)/(u|174174 
((U| V)| W)| 
U|174174 
(2.1.1) 
J,| 
(u|174174 
~ > u|174174 
(U| 
V 
> U@(I| V) 
~| ~'-~. 
///~ | 
(2.1.2) 
U| 
The diagram (2.1.1) is called the pentagon for associativity and the diagram 
(2.1.2) is called the triangle for identities. C is called strift if each avvw, rv, Yv is an 
identity morphism in C. 
A braiding for C consists of a natural family of isomorphisms 
c=Cvv: U|174 
in C such that the following two diagrams commute: 
u|174 
~ , (v|174 
/ 
(u| v)| w 
v|174 u), 
(v|174 
~ v|174 
(2.1.3) 
(u|174 
~ , w|174 
o -j 
, 
UQ(V| w) 
(w| u)| v. 
1 | 
a 
/| 
u|174 
a-, (U|174 
(2.1.4) 
As noted in [JS] (2.1.4) amounts to (2.1.3) with Cvv replaced by Cvv 1. A monoidal 
category together with a braiding is called a braided monoidal category. Below (in 
Sects. 3 and 4) we give two fundamental examples of braided categories; for further 
examples see [JS]. 
We call a monoidal category C compact if for all objects V there exists an object 
V* and arrows ev: V| V*~I, nv:I---,V*| V such that the following composites 
are identity morphisms: 
V ~-', V@I ~+'+ V|174 
~-' 
---+(V|174 
~| 
I| 
+ , V, 
V* ~-~ 
V*-'| 
a 
------,I| 
(V*QV)| 
, V*| 
V*@l--~ V*. 
Remark that we do not require V**= V. 
4 
N. Yu. Reshetikhin and V. G. Turaev 
2.2. Functors of Monoidal Categories. Let C, C' be two compact braided strict 
monoidal categories. Recall that a covariant functor F: C ~ C' associates with each 
object (respectively morphism) X of C an object (respectively morphism) F(X) of C' 
so that F(idx)=idv(x) for any X ~ Ob(C) and F(f o g)=F(f)o F(g) for any two 
morphisms g: U--* V, f: V~ W of C. We say that F preserves the tensor product if 
F(Ic)=Ic. and for any two objects (respectively morphisms X, Y of C F(X| Y) 
=F(X)| 
We say that F preserves braiding if F(cvv)= cF(v)r(v) for any two 
objects U, V of C. We say that F commutes with the compact structures if one can 
associate with each object V of C an isomorphism Vv : (F(V))*---,F(V*) so that F(nv) 
= (Vv| 
o nF(V) and ev(v) = f(ev) o (idv(v) | Vv). 
2.3. Strict Extension of Monoidal Categories. Each monoidal category C is 
equivalent to a strict monoidal category C[] (cf. [Ma]). The objects of C[] are finite 
sequences V1 ..... Vk (including the empty sequence 0) of objects of C. The 
morphisms from (V1, ..., Vk) into (W1, ..., W~) are just C-morphisms 
(...(vl | v~.)| 
| v~_ j)| v~-,.(...(wl | w2)| 
| w,_ 1)| w,. 
(Here if k = 0 then V 1 | 
| Vk = I). The tensor product in C[] is defined for objects 
by the rule 
(171, ..., V~)| 
..., W~) = (V~ ..... V~, W,..., ~) 
and for morphisms by the evident application of the tensor product in C. It is easy 
to check that C D is a strict monoidal category with I G --0. 
There are two natural covariant functors relating C and C[]: the inclusion 
i: C~C D and the projection p : C D ~C. The inclusion i sends Ve Ob(C) into the 
1-term sequence V and sends f: V~ W into the same morphism f considered in the 
category C D. The projection p transforms each object (Vt ..... Vk) of CD into 
(...(V1 | V2) | 
| Vk - 1) | Vk and transforms each morphism of C [] in its obvious 
counterpart in C. Clearly, p o i = ido Both i and p are equivalences of categories. 
(Recall that a covariant functor G: C~C' is called an equivalence of categories C, 
C' if for any objects V, W of C, G maps Morf(V, W) bijectively onto Mor f(G(V), 
G(W)) and each object of C' is isomorphic to G(V) for someV~ Ob(C). 
Speaking non-formally one may say that C
9 has the same morphisms as C but 
more objects: each decomposition V = (...(V1 | V2)| 
| Vk- 1)| Vk of V ~ Ob(C) 
gives rise to an object (V1, ..., Vk) of Cry- 
It is not difficult to show that each braiding in C (respectively a compact 
structure in C) extends naturally to a braiding (respectively a compact structure) in 
C[]. In particular, (V, ..., Vk)* = (Vk*, ..., 1/1").
