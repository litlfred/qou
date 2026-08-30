---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-004-0-which-as-a-reminder
section_title: "(which, as a reminder,"
section_number: 0
pages: 17-21
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — —A h y p e r i d e a l p o l y h e d r o n i s a n o n - c o m p a c t p o l y h e d r o n i n t h e h y p e r b o l i c 3-space 3 which, in the"
---
was deﬁned by subdividing the faces of P Proj
0 into triangles).
Consider now the unsubdivided polyhedron P Proj
0 ,a n dt r u n c a t ei tt oP Tru n
0 .
Each vertex v of P Tru n
0 is also a vertex of ˆP Tru n
0 ,a n di st h e r e f o r ea s s o c i a t e dt o
av e r t e xvt of P Tru n
xt .
For each edge e of P Tru n
0 ,l o o ka ti t se n dv e r t i c e sv1, v2,a n dc o n s i d e rt h e
hyperbolic distance d(vt
1,v t
2)b e t w e e nt h ec o r r e s p o n d i n gv e r t i c e svt
1, vt
2 of P Tru n
xt .
Label the edge e by the symbol +, 0 or − according to whether the derivative
of d(vt
1,v t
2)a t t =0i sp o s i t i v e ,z e r oo rn e g a t i v e .
Our goal is to show that all the edges are actually labelled by 0. This will
require a few preparatory lemmas.
If Q is a polygon with each of its edges labelled by a symbol +, 0 or −,d e ﬁ n e
the number of sign changes of ∂Q as the minimum number of vertices v1,...,v n
which one needs to remove from ∂Q so that the edges in each component
of ∂Q −{ v1,...,v n} have the same sign, namely are either all in {+, 0} or all
in {−, 0}.N o t et h a tt h en u m b e ro f s i g n c h a n g e s i sa l w a y s e v e n .
We will ﬁrst show that, for each face f of P Tru n
0 ,e i t h e ra l lt h ee d g e so ff
are labelled by 0, or it admits at least 4 sign changes in its boundary. In other
words, there cannot be 0 or 2 sign changes in the boundary of f ,u n l e s sa l lt h e
edges of f are labelled by 0.
We b egin with faces of Typ e (iii), contained in horospheres. The argument
uses the following euclidean geometry lemma, which is an inﬁnitesimal and
simpler version of Lemma M 3 of [15] (a result attributed there to A.D. Alek-
sandrov).
BULLETIN DE LA SOCI ´ET´EM A T H´EMATIQUE DE FRANCE
474 BAO (X.) & BONAHON (F.)
Lemma 13 .— In the euclidean plane R2,l e t Qt, t ∈ ]−ε, ε[,b ead i ﬀ e r e n t i a b l e
family of strictly convex polygons with straight sides. Suppose that, at t =0 ,
the derivative of the angle of Qt at each of its vertices is equal to 0,a n dt h a t
the derivative of the area of Qt is also equal to 0.L a b e l e a c h e d g e o fQ0 by the
symbol +, 0,o r − according to whether the derivative of its length at t =0 is
positive, zero or negative. Then, either al l edges are label led by 0,o rt h e r ea r e
at least 4 sign changes in ∂Q0.
Here, “strictly convex” means that the internal angle of Qt at each of its
vertices is strictly between 0 and π.
Proof.—( C o m p a r e[ 1 5 , L e m m aM3].) Suppose, in search of a contradic-
tion, that there are exactly 2 sign changes. We can then index the edges
of Qt as et
1,...,e t
q,e t
q+1,...,e t
r ,e t
r+1 = et
1,g o i n gc o u n t e r c l o c k w i s ei nt h i so r d e r
around ∂Qt,i ns u c haw a yt h a t et
i is labelled by + or 0 if 1 ≤ i ≤ q,a n d
by − or 0 if q +1 ≤ i ≤ r.L e t vt
i be the vertex intersection of et
i and et
i+1,a n d
set vt
0 = vt
r for consistency of the notation. Finally, let T t
i be the unit tangent
vector of the edge et
i,o r i e n t e db yt h ec o u n t e r c l o c k w i s eo r i e n t a t i o no f∂Qt,a n d
let 𝓁t
i be the length of et
i.T h e n , f o r 1≤ i<j ≤ r,
vt
j − vt
i =
j∑
k=i+1
𝓁t
kT t
k = −
i∑
k=1
𝓁t
kT t
k −
r∑
k=j+1
𝓁t
kT t
k.
Let αt
i ∈ ]0,π [b et h ea n g l ef r o m T t
i to T t
i+1,n a m e l yt h ee x t e r n a la n g l e
of Qt at the vertex vt
i .N o t e t h a t∑ r
i=1 α0
i =2 π.R e p l a c i n gt by −t if necessary
(which exchanges the labels + and −), we can assume without loss of generality
that ∑ r
i=q+1 α0
i ≤ π.P i c k a n i n d e xp with 1 ≤ p ≤ q such that ∑ p−1
i=1 α0
i <π
and ∑ q
i=p+1 α0
i <π .
Composing Qt by an isometry depending diﬀerentiably on t,w ec a na r r a n g e
that the vertex vt
p is ﬁxed, and that the tangent vector T t
p is constant. By
our hypothesis that the angles of Qt have derivative 0 at t =0 ,i tf o l l o w st h a t
dT t
i /dt|t=0 =0f o re v e r y i.A s a c o n s e q u e n c e , i f˙𝓁0
i =d 𝓁t
i/dt|t=0 denotes the
derivative of the length 𝓁t
i at t =0 ,t h ev e c t o r ˙v0
i =d vt
i /dt|t=0 is equal to
˙v0
i =
{
+ ∑ i
j=p+1
˙𝓁0
j T 0
j if p +1 ≤ i ≤ r,
− ∑ p
j=i+1 ˙𝓁0
j T 0
j if 1 ≤ i ≤ p − 1.
We will consider the direction in which the edges et
i move. We will say
that et
i weakly moves towards (resp. away from ) Q0 if either the vector ˙v0
i−1 =
dvt
i−1/dt|t=0 is equal to 0 or if the angle from ˙v0
i−1 to T 0
i is in the closed interval
[−π, 0] (resp. [0 ,π ]); note that we can consider the vector ˙ v0
i =˙v0
i−1 + ˙𝓁0
i T 0
i
instead of ˙v0
i−1 for this property. The edge et
i strictly moves towards (resp.
away from ) Q0 if ˙v0
i−1 =d vt
i−1/dt|t=0 is non-zero and the angle from ˙ v0
i−1
to T 0
i is in the open interval ] − π, 0[ (resp. ]0 ,π [).
tome 130 – 2002 – n o 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE 475
For p +1 ≤ j ≤ i − 1 ≤ q,t h ed e r i v a t i v e˙𝓁0
j is non-negative and the angle
from T 0
j to T 0
i is in the interval ]0 ,π [, by choice of the indexing. It follows
that the angle from ˙ v0
i−1 = ∑ i−1
j=p+1
˙𝓁0
j T 0
j to T 0
i is in [0 ,π ], unless ˙v0
i−1 =0 .
In other words, every edge et
i with p +2 ≤ i ≤ q +1 w e a k l y m o v e s a w a y
from Q0.I n a d d i t i o n ,et
i strictly moves away from Q0 if there is a j with
p +1 ≤ j ≤ i − 1 ≤ q − 1a n d ˙𝓁0
j > 0, namely such that e0
j is labelled by the
symbol +.
For 1 ≤ i ≤ p − 1, the same argument applied to ˙v0
i = − ∑ p
j=i+1
˙𝓁0
j T 0
j shows
that et
i moves away from Q0,a n dd o e ss os t r i c t l yi ft h e r ei saj with i+1 ≤ j ≤ p
such that e0
j is labelled by the symbol +.
In particular, for 1 ≤ i ≤ q +1, the edge et
i moves away from Q0.I n a d d i t i o n ,
since there is at least one edge labelled by the symbol +, at least one of the
two edges et
1 and et
q+1 strictly moves away from Q0.S i n c e t h e a r e a s o fQt
is inﬁnitesimally constant, we conclude that there must be an index i0,w i t h
q +2 ≤ i0 ≤ r,s u c ht h a tet
i0 strictly moves towards of Q0.W e c a n c h o o s e
this i0 so that et
i0+1 moves away from Q0 (using the convention that et
r+1 = et
1
when i0 = r).
Because et
i0 strictly moves towards Q0 and et
i0 +1 moves away from Q0,t h e
vector ˙v0
i0 is in the angular sector from T 0
i0 to T 0
i0 +1.S i n c e ∑ r
i=q+1 α0
i ≤ π,
we conclude that the angle from ˙ v0
i0 to Tq+1 is in ] − π, 0[. Remembering
that ˙𝓁0
j ≤ 0f o ra l l j with q +1 ≤ j ≤ r,w ec o n c l u d et h a tt h ea n g l ef r o m
˙v0
q+1 =˙v0
i0 − ∑ i0
j=q+2
˙𝓁0
j T 0
j to Tq+1 is in ] − π, 0[. However, this contradicts our
earlier conclusion that et
q+1 moves away from Q0.
This contradiction shows that there cannot be 2 sign changes around Q0.
As i m i l a rb u ts i m p l e ra r g u m e n ts h o w st h a tt h e r ec a n n o tb e0s i g nc h a n g e ,
unless all edges are labelled by 0. Therefore, either all edges are labelled by 0,
or there must be at least 4 sign changes around Q0.
Lemma 14 .— For every face Q of type (iii) of the truncated polyhedron P Tru n
0 ,
either all the edges of ∂Q are labelled by 0,o rt h e r ea r ea tl e a s t4 sign changes
in ∂Q.
Proof.—T h e r ei saf a c e ˆQt of the truncated polyhedron P Tru n
xt which is as-
sociated to Q and is contained in a horosphere ∂Ht.N o t e t h a t t h e v e r t i c e s
of ˆQt correspond to the edges of Pxt that are adjacent to the vertex of Pxt fac-
ing ˆQt.I n p a r t i c u l a r , s o m e v e r t i c e s o fˆQt are naturally associated to vertices of
Q and other vertices are not. In the horosphere ∂Ht endowed with its euclidean
metric, let Qt be the convex hull of those vertices of ˆQt which correspond to
vertices of Q.
For an edge e of Q,w i t he n dv e r t i c e sv1 and v2,t h eh y p e r b o l i cd i s t a n c e
d(vt
1,v t
2)b e t w e e nt h ec o r r e s p o n d i n gv e r t i c e svt
1, vt
2 of P Tru n
xt in H3 is a strictly
BULLETIN DE LA SOCI ´ET´EM A T H´EMATIQUE DE FRANCE
476 BAO (X.) & BONAHON (F.)
increasing function of the length of the edge et of Qt corresponding to e.I t f o l -
lows that, in our labelling of the edges of P Tru n
0 ,t h ee d g ee is labelled by +, 0,
or − exactly when the derivative of the length of et at t =0i sp o s i t i v e ,z e r o
or negative, respectively.
Because the vector ˙ x ∈ TΦ(P )(RP3)V tangent to t ↦→ xt is contained in
the kernel of the tangent map TΦ(P ) ~Θ, all the angles of ˆQt have derivative 0
at t =0 . I np a r t i c u l a r ,b e c a u s eˆQ0 = Q0,t h ed i s t a n c ef r o me a c hv e r t e xo fˆQt
to ∂Qt has derivative 0 at t =0 . T h i sp r o v i d e st w oi m p o r t a n tc o n c l u s i o n s :
First, the angles of Qt have derivative 0 at t =0 ;s e c o n d ,t h ea r e ao fQt has
the same derivative as the area of ˆQt at t =0 ,n a m e l y0s i n c et h ea r e ao fˆQt is
constant by choice of the truncated polyhedron P Tru n
xt .
We can therefore apply Lemma 13 to the p olyhedron Qt,w h i c hp r o v i d e st h e
conclusion of Lemma 14.
For faces of Typ e (i) of P Tru n
0 ,w eu s et h ef o l l o w i n gl e m m a .
Lemma 15 .— In the hyperbolic plane H2,l e t Qt, t ∈ ]−ε, ε[,b ead i ﬀ e r e n t i a b l e
family of convex hyperideal polygons such that, for every vertex v of QProj
t
which is on the circle at inﬁnity ∂∞ H2,t h ec o r r e s p o n d i n gv e r t e xvt is also on
∂∞ H2 for every t.L e t QTru n
t be obtained by truncating Qt,c h o s e nt od e p e n d
diﬀerentiably on t (remember that the truncation is not uniquely determined at
the ideal vertices of Qt).L a b e l e a c h e d g e o fQTru n
0 by the symbol +, 0,o r −
according to whether the derivative of its length at t =0 is positive, zero or
negative. Then, either all edges are labelled by 0,o rt h e r ea r ea tl e a s t4 sign
changes in QTru n
0 .
Proof.—I ft h e r ea r e f e w e rt h a n 4s i g n c h a n g e s , w ec a n t h e ni n d e xt h ee d g e s
of QTru n
t as et
1,. . . , et
p, et
p+1,. . . , et
q, et
q+1 = et
1,g o i n gc o u n t e r c l o c k w i s ei nt h i s
order around ∂QTru n
t ,i ns u c haw a yt h a te0
i is labelled by + or 0 if 2 ≤ i ≤ p−1,
and by − or 0 if p+1 ≤ i ≤ q.I n a d d i t i o n , r e p l a c i n g t h e m b y s u i t a b l e n e i g h b o r s
if necessary, we can arrange that et
1 and et
p are both contained in edges of the
original untruncated polyhedron Qt.
We use the pro jective mo del for the hyp erb olic plane H2 ⊂ R2 ⊂ RP2,
with isometry group PO(2 , 1). For each i,l e t T u
i ∈ PO(2, 1) be the hyperbolic
isometry which acts by translation of u ∈ R along the geodesic or horocycle that
contains e0
i ,f o rt h eo r i e n t a t i o nc o m i n gf r o mt h ec o u n t e r c l o c k w i s eo r i e n t a t i o n
of ∂QTru n
0 .L e t gt
i be the geodesic or horocycle of H2 that contains the edge et
i,
transversely oriented by the outer normal orientation of ∂QTru n
0 .F i n a l l y , l e tN t
1
and N t
p ∈ R3 be the unit normal vectors of the transversely oriented geodesics
gt
1 and gt
p,a sd e ﬁ n e d( f o rt h e3 - d i m e n s i o n a lc a s e )i n§ 1.
Composing Qt by an isometry depending diﬀerentiably on t if necessary, we
can arrange that et
1 stays in a ﬁxed geodesic of H2,a n dt h a tt h ev e r t e xs e p a -
rating et
1 from et
2 is constant. Since all the angles of QTru n
t remain equal to 1
2 π,
tome 130 – 2002 – n o 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE 477
we conclude that N t
