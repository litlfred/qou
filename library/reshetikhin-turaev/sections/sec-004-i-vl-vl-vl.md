---
doc_id: reshetikhin-turaev
doc_title: "Ribbon graphs and their invariants derived from quantum groups"
section_id: sec-004-i-vl-vl-vl
section_title: "I vl vl vl"
section_number: null
pages: 9-12
source_pdf: Reshetikhin_Turaev.pdf
source_sha256: 7ead97555a25d357
toc_source: inferred
doc_brief: "Ribbon graphs and their invariants derived from quantum groups — The generalization of Jones polynomial of links to the case of graphs in R 3 is presented."
---
9 
(d) S meets RZx {0,1} exactly in bases of certain type 2 bands and the 
collection of these bases is the collection of segments 
{[i_~ 
. 
1 
~,l+~] x0x0[i=l .... ,k}tu{[j-88188 
(4.2.1) 
(e) the remaining bases of type 2 bands are contained in the bases of type 1 
bands. 
The surface S is called the surface of the graph. The type 1 bands are called 
coupons, the type 2 bands are called ribbons. Those ribbons which are incident to 
the segments (4.2.1) are called border ribbons. Some examples of ribbon graphs are 
given in Figs. 1-3. 
Note that the choice of orientation for S is equivalent to a choice of one side of 
S. The chosen side will be depicted white, the opposite side will be shaded. Note 
that when we rotate an annulus around its core to the angle 180 ~ we get the same 
annulus with the opposite orientation. Thus, orientations of annuli are insignifi- 
cant when one considers ribbon graphs up to isotopy (see Sect. 4.3). 
Fig. 1 
Fig. 2 
Fig. 3 
v I 
Iv:l~, 
I v 
2% 
C',, v 
Xv,w = X~.w 
X~.w 
ft 
'r 
v 
k--:v 
~v 
vl~ 1 
vl~ I 
V1,~ I 
V~,s K 
I vl vl vl 
J~ 
K~ 
K~ 
10 
N. Yu. Reshetikhin and V. G. Turaev 
A ribbon graph is called homogeneous if in a neighbor hood of the segments 
(4.2.1) the white side of the graph surface is turned upwards (i.e. to the reader). For 
instance, the graphs in Figs. 1 and 2 are homogeneous, and those in Fig. 3 are not 
homogeneous. 
4.3. Directed Graphs. A ribbon graph is called directed if the cores of its bands and 
annuli are provided with directions. Note that the directed core of a band leads 
from one base to another one. The former base of the band is called initial, the 
latter one is called final. 
Two directed ribbon graphs F, F' are called isotopic if there exists a (smooth) 
isotopy h t : R z x [0, 1 ] ~ R2 x [0, 1 ] of the identity mapping h o = id so that each h t is 
a self-diffeomorphism of R2x [0, 1] fixing the boundary pointwise, and hi 
transforms F onto F' preserving the decomposition into coupons, ribbons and 
annuli, and preserving the directions of cores and the orientation of the graph 
surface. Isotopy is clearly an equivalence relation. 
With each directed ribbon (k,f)-graph F we associate two sequences 
~I(F),..., ek(C) and el(F),..., d(F) consisting of + 1. Here ei(F) = - 1 if the segment 
[i-(1/4), i+ (1/4)] x 0 x 0 is the initial base of the incident ribbon, and ~i(F)= + 1 
otherwise. Similarly, d(F)=-1 if the segment [j-(1/4), j+(1/4)] x0 x 1 is the 
final base of the incident ribbon and d(F) = 1 otherwise. 
Let Q be a coupon of a directed ribbon graph F. Denote by a=a(Q) 
(respectively by b = b(Q)) the number of ribbons of F incident to the initial 
(respectively final) base of Q. A small neighborhood of Q in R z x (0, 1) looks as in 
Fig. 4 where we assue that the white side of Q is turned upwards. Denote the 
ribbons of C incident to Q by BI(Q),..., Ba(Q) and BI(Q), ..., Bb(Q) in the order 
shown in Fig. 4. The directions of B ~, Bj are characterized by numbers e~(Q), 
ej(Q) e {1, -1}. Namely, ~i(Q)_= _ 1 if the base of B i depicted in Fig. 4 is its initial 
base; otherwise el(Q)- 1. Similarly, ej(Q) -- - 1 if the base of Bj depicted in Fig. 4 is 
its final base; otherwise ~j(Q)--1. 
B I 
B a 
Fig. 4 
B~ 
gb 
4.4. Colourings of Ribbon Graphs. Fix a Hopf algebra A. Denote by A = A(A) the 
class of A-modules of finite dimension over the ground field. Denote by N = N(A) 
the class of finite sequences (V1,~1), ...,(Vk, ek) where V 1, ..., VkeA and 51, "",~k 
= + 1. With such a sequence t/=((V1, ct) .... ,(Vk, ~k)) we associate the A-module 
V(q) = V~ ~ | 
| Vd k, where V 1 = V, V- 1 = VV, the tensor product is taken over the 
ground field, and the A-module structure in V(t/) is determined by the comulti- 
plication in A. 
A colouring (or an A-colouring) of a directed ribbon graph F is a mapping 2 
which associates with each ribbon B of F its "colour" 2(B) ~ A and associates with 
Ribbon Graphs Derived from Their Invariants 
It 
each coupon Q of r its "colour" 2(Q)e Homa(V(r/) , V(~/')), where 
t/= ((2(BI(Q)), el(Q)),... , (2(Bb(Q)), eb(Q))) e N, 
q' --- ((2(Bl(O)), e ~(Q)) .... , (2(B"(Q)), e"(Q))) e N. 
There is a natural isotopy relation in the class of coloured directed ribbon 
graphs, defined as in Sect. 4.3 with the additional condition of preservation of 
colouring. By a CDR-graph we shall mean a coloured directed ribbon graph 
considered up to isotopy. By a HCDR-graph we shall mean a homogeneous CDR- 
graph (see Sect. 4.2). 
Some examples of CDR-graphs and the notation for these graphs are presented 
in Figs. 2 and 3. The homogeneous (k, ~~ 
with one coupon of colour f 
presented in Fig. 2 will be denoted by F(f, q, q'); here q =((V~, el) .... , (Vk, ek))~ N, 
q'=((Vl, e 1) .... ,(V~,eO)~N, where V/, V j are the colours of the corresponding 
ribbons and ei, gJ are directions of their cores: + 1 means down, -1 means up. 
4.5. Category HCDR(A). Let A be a Hopf algebra. We define the category of 
homogeneous A-coloured directed ribbon graphs W--HCDR(A). Its objects are 
elements of N(A) (see Sect. 4.4). If q, q'e N(A) then a morphism t/~q' is a HCDR- 
graph such that the sequence of colours 2 and directions e of the top (respectively 
bottom) border ribbons is equal to ~/' (respectively ~). The composition F' o F of two 
such morphisms F :t/~/', F' :t/'~/" is defined as follows: shift F' by the vector 
(0,0, l) into R a x [1,2]; glue the bottom ends of F' with the top ends of F (this 
glueing preserves colours and directions of ribbons since they are determined by 
q'); reduce twice the size along the line 0 x 0 x R. This gives a well-defined 
composition law for morphisms. The identity morphism t/~t/is the HCDR-graph 
consisting of plane rectangular ribbons whose directions and colouring are 
determined by ~/. 
We provide ~ with the tensor product | : ~ x ~---,~4 ~ as follows. The tensor 
product of objects ((V1, e0,..., (Vk, ~k)) and ((W1, v0,..., (We, ve)) is their conjuction 
((v~, ~0,..., (v~, sk), (w~, v0 .... , (We, v~)). 
The tensor product of two morphisms (i.e. graphs) F, F' is obtained by positioning 
F' to the right off so that there is no mutual linking or intersection (see Fig. 5). It is 
obvious that Jt ~ is strict monoidal. [Here I e N(A) is the empty sequence, id, is the 
empty graph.] 
 ig.s 
: [] [] 
The category x4 ~ is provided with a natural braiding 
{%o : tl|174 
l rl, O e Ob(Jt~)= N(A)} 
(see Sect. 2.1). We take the HCDR-graphs representing id,, id0 and form the 
HCDR-graph % 0 as in Fig. 6. (This idea is borrowed from [JS].) It is a pleasant 
exercise for the reader to check that we do have a braiding. 
Finally, we provide ~ with a structure of a compact category. For an object 
q = ((V1, cO,..., (Vk, ek)) put q* = ((Vk, -- ek) , (Vk_ i, -- •k- 
1) .... 
, (V1, - el)). The con- 
struction of the homomorphisms % n~ should be clear from Fig. 7. 
12 
Fig. 6 
N. Yu. Reshetikhin and V. G. Turaev 
q 
0 
Fig. 7 
eq 
nq 
4.6. Theorem. ~ = HCDR(A) is a compact braided strict monoidal category. 
Proof Obvious. 
We may similarly introduce the category CDR(A) of CDR-graphs. In contrast 
to HCDR(A) the objects of CDR(A) are sequences (V1, ~1, vl) ..... (Vk, ek, Vk), where 
V1,..., Vk e A(A) and el, vi = + 1. The numbers {vi} are responsible for the up/down 
position of the white side of the border ribbons near the border segments. 
Theorem 4.6 may be easily extended to the case of CDR(A).
