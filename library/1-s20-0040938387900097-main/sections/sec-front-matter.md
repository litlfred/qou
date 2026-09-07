---
doc_id: 1-s20-0040938387900097-main
doc_title: "STATE MODELS AND THE JONES POLYNOMIAL (f&riced in recisrdfirm I Srpremher 1986) $1. INTRODIJ’CTION IN THIS PAPER I construct a state model for the (original) Jones polynomial [5]. "
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-13
source_pdf: 1-s2.0-0040938387900097-main.pdf
source_sha256: dae76f3434834382
doc_brief: "STATE MODELS AND THE JONES POLYNOMIAL (f&riced in recisrdfirm I Srpremher 1986) $1. INTRODIJ’CTION IN THIS PAPER I construct a state model for the (original) Jones polynomial [5]. (In [6] a state — 2"
---
STATE MODELS AND THE JONES POLYNOMIAL 
(f&riced in recisrdfirm I Srpremher 1986) 
$1. INTRODIJ’CTION 
IN THIS PAPER I construct a state model for the (original) Jones polynomial [5]. (In [6] a state 
model was constructed for the Conway polynomial.) 
As we shall see, this model for the Jones polynomial arises as a normalization of a regular 
isotopy invariant of unoriented knots and links, called here the bracket polynomial, and 
denoted (K) for a link projection K. The concept of regular isotopy will be explained below. 
The bracket polynomial has a very simple state model. 
In $2 (Theorem 2.10) I use the bracket polynomial to prove (via Proposition 2.9 and an 
observation of Kunio Murasugi) that the number of crossings in a connected, reduced 
alternating projection of a link L is a topological invariant of L. iA projection is reduced if it 
has no isthmus in the sense of Fig. 5.) In other words, arty two connected, reduced alternating 
projections ofthe link L hnce the same nwnber of crossings. This is a remarkable application of 
our technique. It solves affirmatively a conjecture going back to the knot tabulations of Tait, 
Kirkman and Little over a century ago (see [16], [9], [lo]). 
Along with this application to alternating links, we also use the bracket polynomial to 
obtain a necessary condition for an alternating reduced link diagram to be ambient isotopic 
to its mirror image (Theorem 3.1). One consequence of this theorem is that a reduced 
alternating diagram with twist number greater than or equal to one-third the number of 
crossings is necessarily chiral. 
The paper is organized as follows. In 52 the bracket polynomial is developed, and its 
relationship with the Jones polynomial is explained. This provides a self-contained 
introduction to the Jones polynomial and to our techniques. The last part of $2 contains the 
applications to alternating knots, and to bounds on the minimal and maximal degrees of the 
polynomial. $3 contains the results about chiralit’y of alternating knots. $4 discusses the 
structure of our state model in the case of braids. Here the states have an algebraic structure 
related to Jones’s representation of the braid group into a Von Neumann Algebra. 
52. BRACKET ISVARIANT 
We first describe a general scheme ofcalculation from unoriented knot and link diagrams. 
This scheme associates a polynomial in three variables A, B and d to each diagram. It is well- 
defined on equivalence classes of diagrams. Two diagrams are equicalent if their underlying 
planar graphs are equivalent under orientation preserving homeomorphisms of the plane. 
Note that the Reidemeister moves change the graphical structure. 
We distinguish three relations on diagrams: equivalence (as above), ambient isotopy and 
regular isotopy. Two diagrams are ambient isotopic ifone can be obtained from the other by a 
sequence of Reidemeister moves of type I, type II and type III (see Fig. 1) plus equivalence as 
39.5 
396 
Ambient 
isotopy 
Louis H. Kauffman 
Reidemeister moves 
Fig. 1. 
Regular 
isotropy 
defined above. Two diagrams are regularly isotopic if they are ambient isotopic without the use 
of the type I move. Regular isotopy turns out to be a convenient concept for us. 
DEFIMTION 2.1. Let K be an unoriented knot or link diagram. Let (K) be the element of the 
ring Z [A, B, d] defined by means of the rules: 
(i) (O)=l 
(ii) (OuK)=d(K), K not empty 
(iii) ( /\‘)=A(=)+B( )(). 
Remark. A formula may involve the bracket and a few small diagrams. These smallfigures 
represent larger diagrams that difler only as indicated in the small diagrams. 
The bracket, (K), is well defined on diagrams, but it is not invariant under any of the 
Reidemeister moves. It is the purpose of this section to determine relations among A, B, d so 
that (K) becomes invariant under Reidemeister moves. We will obtain invariance under 
types II and III, hence the use of regular isotopy. 
Some comments are in order about the rules: Rule(i) says that (K) takes the value 1 on a 
single unknotted circle diagram. Rule (ii) says that (K) is multiplied by din the presence of a 
disjoint circular component. This component can surround other parts of the diagram. 
Rule(iii) applies to diagrams that differ locally at the site of a single crossing. We can use 
rule (iii) to keep expanding the formulas until we reach diagrams consisting of disjoint unions 
of circles (Jordan curves in the plane). Rules (ii) and (iii) then imply that the value of(K) on a 
disjoint collection of circles is d raised to one less than the cardinality of the collection. 
Note that rule (iii) entails the formula 
(x)=B(=)+A()(). 
In fact, we can create a mnemonic for this expansion by labelling the crossings as shown in 
Fig. 2. This label A marks the two local regions swept out by turning the overcrossing line 
counterclockwise until it coincides with the undercrossing line. 
For the expansion formula (iii) we can indicate which way a crossing is to be split by 
scoring a marker on it that connects the two regions that will be joined by the splitting. See 
Fig. 2. 
STATE MODELS AND THE JONES POLYNOMIALS 397 
B 
Y 5 5 
/ 
8 
Crossmq labels 
x v- -A split 
X Split >< 
State markers and splittmg 
Splitting a state S 
Fig. 2. 
If U is the underlying planar graph for K, then a state ofU is a choice of splitting marker 
for every vertex of U. Again see Fig. 2. I choose to call the underlying planar graph for a 
diagram K the universe for K (see [6]). This terminology distinguishes the underlying planar 
graph from the link projection and from other graphs that can arise. Thus we speak of the 
states of a universe. 
Since splitting all the vertices of a state results in a configuration of disjoint circles, we see 
that the states are in one-to-one correspondence with final configurations in the expansion of 
the bracket. Accordingly, we define (K 1 S) for a diagram K and a state S by the formula 
(K/S)=A’B’ 
where i is the number of state markers touching A labels, andj is the number ofstate markers 
touching B labels. The total contribution of a given state to the polynomial is then given by 
the formula. 
(KIS)d’s’-’ 
where ISI denotes the number of circles in the splitting of S. View Fig. 2. 
These observations are summarized in the statement of the following proposition, whose 
proof we omit. 
PROPOSITION 2.2. (K) is uniquely determined on diagrams by the rules (i), (ii), (iii). If is 
given by the formula 
(K)=~(KIS)d’S’-l 
s 
where this summation is ocer all states of the diagram, and S denotes the number of components 
in the splitting of a state S. 
We now see how (K) behaves under elementary diagram moves, and consequently 
determine how to adjust A, B, and d to obtain a topological invariant. 
398 Louis H. Kauffman 
LEWA 2.3. The follo\ving formula holds, bvhere the three diagrams represenr rhe Same 
projection except in the area indicated. 
(3: )=XB(x)+(ABd+A’+B’)(=). 
Hence ( 3: ) = (DC) for all diagrams if 
Proof 
AB=l and d=-A’--Ae2. 
(xz)=A<J-\)+B<~~_). 
Thus 
Hence 
<3:> =+<x>+-J<351>] 
+e [ ‘5<x> +A <3C> 1. 
<I<> = (AB~+A*+B*) <-_>+a?<~>. 
This completes the proof. 
LEMMA 2.4. Type II irlcariance for ( ) implies type III invariance. 
(by II-invariance) 
Hence (x)=(Yx ,). This is type III invariance. 
Thus we see that by choosing 
B=A-‘,d= -A*-A-* 
(K) becomes a Laurent polynomial in A, and it is an invariant of regular isotopy (i.e. 
invariant under moves of type II and III). It is not invariant under the type I moves, but 
behaves as follows: 
PROPOSITION 2.5. With 
then 
B=A-1, d= -A’--A-2 
(‘!)=(-A3) (-) 
Proof: This is a direct calculation, and is omitted. 
From now on, unless otherwise specified, we assume that A, B and d are chosen as indicated 
STATE MODELS AND THE JOSES POLYNOMIALS 399 
in Proposition 2.5. With these choices, the bracket polynomial is an invariant of regular 
isotopy for unoriented knots and links. 
The simplest invariant of regular isotopy for oriented diagrams is the ~r’ist number (or 
writhe) \L’(K). This is the sum of the signs of all the crossings where each crossing is given a sign 
of plus or minus 1 according to the conventions shown in Fig. 3. 
To obtain an invariant of ambient isotopy for oriented knots and links we define a 
Laurent polynomialf[K] by the formula 
f[K]=(-,4)-‘“‘“‘(K), 
where w(K) denotes the twist number of the diagram K. The bracket is defined on oriented 
diagrams by forgetting the orientation. 
THEOREM 2.6. The polynomial f[K] EZ[A,A-‘1 defined nboue is an ambient isotopy 
inrnriant for oriented links K. 
Proof By combining the behaviour of the twist number under type I Reidemeister moves 
with the behaviour of the bracket (Proposition 2.Q it follows that f [K] is invariant under 
type I moves. Thusf[K] is invariant under all three moves, and is therefore an invariant of 
ambient isotopy. 
Both the bracket and the polynomialf[K] behave as follows on taking mirror images: 
PROPOSITION 2.7. Let K! denote the mirror image of K (obtained by recersing all the 
crossings of K). Then 
(K!) (A)=(K) (A-‘) 
f[K!] (A)=f[K] (A-‘). 
Proof: Just note that switching all crossings results in the replacement of every 
appearance of A by its inverse in the expansion of the bracket. This proves the first part. Since 
the twist number of a mirror image is the negative of the twist number of the original. the 
second part follows as well. 
The Jones polynomial 
Now recall that the Jones polynomial [S] is defined by the identities: 
vo= 1 
t-‘vx -tV=/, = 4-1 v= ( > J’ 
The Jones polynomial is an ambient isotopy,invariant of oriented knots and links. 
Sign conventions 
Fig. 3. 
400 
THEOREM 2.8. 
Louis H. Kauffman 
V,(t)=f[K](t-“‘). 
Proof: <x> =a<=> +a-‘<)(> 
<x> =A-‘<=> +A <)(> 
Hence a<,‘<> -a-‘<x)=(&a-*)< x>. 
Multiplying this last formula by appropriate writhes, we have 
The result follows at once by substituting t raised to the negative one-quarter power for A. 
Figure 4 illustrates the calculation of the bracket for the Hopf link and for the trefoil knot. 
This calculation, in conjunction with Proposition 2.7, produces a short elementary proof of 
the distinction between the trefoil and its mirror image. 
Remark. Some formal results about the Jones polynomial (reversing formula [i 11, [12], 
Birman “infinity’‘-formula [21]) follow immediately and trivially from Theorem 2.5 and the 
definition of the bracket polynomial. We leave the verification of these relations as an exercise 
for the interested reader. 
Alternating links 
We now give applications to alternating links. The first result determines the highest and 
lowest degree terms in the bracket polynomial for an alternating diagram. 
PROPOSITION 2.9. Let K be an alternating knot or link diagram that is connected and 
reduced. Let K be shaded so that all the crossings are of shaded type A (the regions labelled “A” 
are shaded). Then the term in (K) of highest degree in A has degree V + 2W - 2, where V is the 
number of crossings in K, and W is the number of white regionsfor this shading. The co-efficient 
of this power of A in (K) is (- l)w-‘. 
With the same hypotheses, the lowest degree term has degree -V-Z(B- l), u.here B 
denotes the number of black (shaded) regions in the diagram. This term is manic with 
co-efficient ( - l)B- ‘. 
<@> = A-’ <a> +A <a> I A-’ (-A-3) + A (-A3) 
<@> = A <@> +A-’ <&> 
D A(-A4-A-4)+A-‘( -A3)-* 
-_ -/,5-A-3+ A-7 
Sample bracket calcutations 
Fig. 4. 
STATE MODELS AND THE JONES POLYNOMI.ALS 401 
Isthmus Simplest 
examples 
Fig. 5. 
Before proving this result, some commentary on terminology is needed. A reduced 
diagram is one that does not contain an isthmus as shown in Fig. 5. An isthmus is a crossing in 
the diagram so that two of the four local regions at the crossing are part of the same region in 
the larger diagram. 
Note that a connected alternating diagram, bvhen shaded in checkerboardfashion, has all of 
its crossings ofthe Same shaded type (see Fig. 6). By flipping the shading, if necessary, we may 
assume that it is the A-labelled regions that are shaded. 
We shall call a diagram satisfying these hypotheses (connected, reduced) a simple diagram. 
Thus Proposition2.9 says that if K is a simple diagram, then 
max deg (K) = V+ 2 W- 2 
min deg (K) = - V-2B+2. 
The idea behind our pinpointin g of the maxima1 degree is this: by choosing the state 
obtained by splitting every crossing in the A-direction, we obtain Wcomponents (where lVis 
the number of white regions), and hence a degree of V i 2( CV- 1) from the corresponding part 
of the summation for the bracket polynomial. 
Proojof 2.9. Let S be the state obtained by splitting every crossing in the diagram in the 
A-direction. Then (K 1 S) = AV, and /S/ = W, where W is the number of white regions in the 
shading. Thus this state contributes the term 
Fig. 6. 
402 Louis H. Kauffman 
to the state expansion of (S). Since 
d= -AZ-A-’ 
this means that the highest degree contribution of the state S is the degree V+2(E’-- 1). 
Now consider any other state S’. The state S’ can be obtained from S by switching some 
subset of state markers of S. Thus there is a sequence of states S(O), S(l), S(2), . , S(n) so 
that S = S(O), S’ = S(l), and S(i + 1) is obtained from S(i) by switching one state marker from 
type A to type A-‘. Since a state marker of type A-’ contributes (l/A), we see that 
(Kl S(i+l))=A-’ (K/S(i)). Also, IS(i+l)/ is within 1 of IS(i)/, since switching a single 
state marker can change the component count of the split state by at most one. It follows 
that the maximal degree contribution of S(i+ 1) is less than or equal to the maximal degree 
contribution of S(i). 
However, we assert that the maximal degree contribution actually falls from S(0) to S(1). 
This follows from the above assumption, if it is shown that switching any state marker in S will 
cause n decrease in the number ofcomponents of the corresponding split state. This follows from 
the assumption of diagram simplicity. (If the number of split components did not decrease 
from S = S(0) to S(l), then some white region would touch both sides of a crossing. This can 
only happen in the presence of an isthmus.) 
Thus we have shown that the term of maximal degree in the entire bracket polynomial is 
contributed by the state S, and is not cancelled by terms from any other state. This completes 
the proof. 
Finally we give the main application. 
THEOREM 2.10. The number of crossings in a simple alternating projection of a link L is a 
topological invariant of L. Hence any two simple alternating projections of a given link have the 
same number of crossings. 
Proof Let span (K) denote the difference 
span (K) = maxdeg (K) - mindeg (K). 
Then 
span (K)=[V+2W-2]-[- V-28+2] 
=2V+2(W+B)-4. 
Since W+ B equals the total number of regions in the diagram, and this exceeds the number 
of crossings by two, we have 
span (K)=2y+2(I’+2)-4=4V. 
This completes the proof. 
Remark. It is worth remarking that Proposition2.9 can be generalized to imply an 
inequality: 
span (K) < 4V, 
for an arbitrary (not necessarily alternating) diagram K. 
This result has been observed by Kunio Murasugi and (independently) Morwen 
Thistlethwaite (see [14] and [17]), each using the ideas of an early version of this paper. We 
give here our short proof via the: 
STATE MODELS AND THE JONES POLYNOMIALS 403 
DUAL STATE LEVY;\ 2.11. Let S he a statefor a connected unirerse U. Let .$ denote the state 
obtained from S by reversing all the state markers of S (call this the dual state of S). Then 
ISi+iSi <R 
where R denotes the number of regions in U. 
Proof: The proof is by induction on the number of vertices Vin U. It is easily seen to be 
true for V= 0, 1,2. Therefore suppose the result true for all universes with less than Vvertices. 
Let U be connected. with Yvertices. Let U’ and U” be the two universes obtained by splitting 
U at a given vertex P in the two possible ways. Then, by connectivity of U, one of U’ or U” is 
also connected. We may suppose that U’ is connected. Apply the induction hypothesis to U’. 
If S is a state of C, then either .S or 5 is split at the vertex P in the same direction that 
formed U’. We can assume that S is so split. Then, by ignoring the site at P, Scan be construed 
as a state S’ of U’. 
By induction, / S’l + 191 d R’ where R’ denotes the number of regions of U’. By 
construction, R’= R - 1 where R is the number of regions of U. And S’ and S have the same 
number ofsplit components: /SI = /S’I. On the other hand, it is possible that 9, being obtained 
from 9 by splicing at the site p, may have (at most) one less split component than s^‘. 
Thus Ipi+ 1 > 5. These facts imply the inequality jS( + Is^l ,< R, completing the inductive 
proof of the Lemma. 
The inequality mentioned prior to the proof of this lemma now follows by repeating the 
proof of 2.9, using the state S where all the markers are of type A. No relation with the 
checkerboard shading is required, nor do we need assume anything other than connectivity 
of the diagram. We then obtain: 
maxdeg (K) 6 V+2(1Sl--1) 
mindeg (K) 2 - V- 2( Is^l- 1). 
The lemma, in conjunction with the calculation of 2.10 then gives the inequality: 
span (K) < 4V. 
Finally we note that both Murasugi and Thistlethwaite prove the stronger inequality: 
span (K) < 4 V when K is a connected non-alternating diagram. Wu [IS] gives a proof of this 
inequality by strengthening our dual state Lemma. 
$3. CHIRALITY OF ALTERNATING LINKS 
Here we apply Proposition 2.9 to obtain a necessary condition for an oriented alternating 
link to be achiral (ambient isotopic to its mirror image). 
THEOREM 3.1. Let K be a simple alternating diagram shaded as in Proposition 2.9. Let W 
and B denote the number of white and black regions in this shading. Suppose that K has twist 
number w(K). If K is ambient isotopic to K! then 
3w(K) = W - B. 
It follows from this formula that 
W=(1/2) (V+3w(K))+ 1 
B=(1/2) (V-3w(K))+ 1 
where V denotes the number of crossings in the diagram. 
304 Louis H. Kauffman 
Proof: We use the Jones polynomial in the form of the ambient isotopy invariant 
.r‘[k’] (i-1) (see Theorem 2.8). It follows from 2.9 and the definition off[K] that f[K] has 
maximal and minimal A-degrees rnux (f) and min (f) given by the formulas 
max(f)= -3\v+ V+2(W- 1) 
min(f)= -3\t’- V-2(B- 1) 
where iv is the twist number ~t’=w(K). 
In order for K to be achiral it is necessary that -min (f)=ma.u (f) (by Proposition 2.6). 
Thus 
Hence 
3w+V+2(B-l)=-3w+V+2(W-1). 
3w = W-B. 
The remaining formulas follow by using the relation w+ B = V+ 2. This completes the proof. 
COROLLARY 3.2. Let K be a simple alternating diagram. Let T = 1 w(K) I. Assume K is not the 
unknotted circle diagram. Then, ifT > V/3 (V is the number of crossings in the diagram) then K 
is chirnl. 
This corollary is an easy consequence of Theorem 3.1. We omit the proof. It follows at 
once from Corollary 3.2 that special alternating (simple) links are chiral. This fact was first 
proved by Murasugi [13], using his signature invariant. 
Remark. There exist chiral alternating knots satisfying the condition 3w(K) = W-B of 
Theorem 3-l. Thus the condition of 3.1 is necessary but not sufficient for achirality. Figure 7 
depicts such an example. A signature calculation shows that this knot (10, in Rolfsen’s tables 
[ 151) is chiral. 
Note also that it is easy to produce an alternating prime knot ofzero twist number that is 
chiral (remove two crossings from the top line of Fig. 7). Erica Flapan has observed the non- 
alternating knot 101Z5 to have the same property (chiral, twist number zero, prime). 
Remark. It is entirely possible that the venerable conjecture (that the twist number is a 
topological invariant for reduced alternating diagrams) is true. This would generalize 3.1 
except for the case of twist number zero. In this case, 3.1 demands B = W for achirality. More 
may be true. We make the following conjecture. 
Fig. 7. 
STATE MODELS AND THE JONES POLYNOMIALS 305 
CONJECTURE. Let K be a prime reduced alternating diagram, and suppose that K is achiral 
bvith twist number zero. Then the two planar graphs B(K) and W(K) are isomorphic as abstract 
graphs. 
Here B(K) is the graph formed from the black shading: one vertex for each shaded region. 
one edge for each crossing shared by shaded regions. W(f<) is the planar dual to B(K) formed 
from the white regions. (See Note added in Proof.) 
$4. BRAID STATES AND THE DIAGR.4.M ALGEBRA 
The bracket also provides an entry into the representation theory associated vvith the 
Jones polynomial. In order to see this we define a diagram algebra, D[n], based on the 
patterns shown in Fig. 8. Here diagrams with free ends are multiplied as braids. while 
multiplication by the closed loop 6 denotes disjoint union. Addition is formal with no 
imposed relations. As the figure shows, the resulting (multiplicative) monoid has relations 
1 
h; = 6hi = hia 
hihi+,hi=hi 
hi+lhihi+I=hi+I 
hihj=hjhi, /i-j1 > 1. 
(We omit the proof here that it has exactly these relations. See [7], [8].) 
The original Jones polynomial was defined via a representation into an abstract algebra 
satisfying (essentially) these multiplicative relations. The diagram algebra forms the 
beginning of a direct geometric connection between these algebras and the theory of braids. 
In our terms the relation ( X) =A (E ) + A - ’ ( )( ) becomes the pattern for a 
representation of the braid group (see [5]) into the free additive algebra with the above 
multiplicative relations and 
a=d= -.A’-A-’ 
Generators of n-strand braid group 
h, h n-t 
Generators of n -strand diagram monotd 
__“o-_ h ,u n h,’ ’ 8 h, 
n 
U “, h,.,“, = 4 
n Diagram monoid relations 
Fig. 8. 
406 Louis H. Kauffman 
(specializing the loop variable). If Gi is the ith braid generator then the representation is given 
by the formula 
p(ai) = Ah, + rl - 1 1. 
Let B[n] denote the n-strand braid group. A braid is a product of the generators 
fl *1 crl , a2 , . . . , a,‘_‘,. 
(See Fig. 8.) For a braid b, let (b) denote the evaluation of the bracket polynomial on the 
closure of b. 
Since the states corresponding to a given braid b are obtained by eliminating crossings 
horizontally ( z ) or vertically ( )( ), we see that the generators for the diagram monoid 
correspond to horizontal splits on the generators of the braid group. (Vertical splits give 
identity braids.) 
The relations in the diagram monoid allow one to algebraically determine the number of 
components in the closure of h-hence the value of(h), for any product h in D[n]. This gives 
a diagrammatic interpretation to trace computations in the representation theory. 
Note how the bracket expansion and the form of the representation fit together. By 
representing each braid generator as a sum of two algebraic terms, the product correspon- 
ding to a braid word has a power-of-two number of terms. Each term is a power of A 
multiplied by a product of generators of the diagram algebra. Each such product corresponds 
to one of the states in the bracket expansion. 
Finally it is worth mentioning that a rich generalization of the braid group is obtained by 
allowing products of braid generators with elements of the diagram monoid. The resulting 
system, up to regular isotopy, can be defined so that it has relations corresponding to 
standard braiding relations, diagram monoid relations, plus extra relations of the type 
illustrated in Fig. 9. Call this structure the Braid Monoid. (See [7] and [8].) Yetter [ 191 has 
studied a version of the braid monoid, and Birman and Wenzel [4] use an algebra derived 
from it to study representations of the braid group and the Kauffman polynomial [S]. 
This section has been an introduction to braid states and the diagram algebra. For 
relations with chromatic polynomials and the Potts model (Cl], [S]), see [7]. (By associating 
an appropriate alternating link diagram to any planar graph, and by choosing A,B, d 
appropriately, dichromatic polynomials and partition functions (for the Potts model) can be 
computed using the bracket expansion. Thus our formalism provides a relat;onship among 
knot theory, graph theory and physics. In the case of braids, the simple topology of the 
diagram algebra underlies all three aspects.) 
A basic braid monoid relation 
Fig. 9. 
‘acknowledgements-The author would like to take this opportunity to thank a number ofpeople: Ken Millett, Ray 
Lickorish and Bob Brandt for sharing their work and ideas, Joan Birman for her continued intense support of this 
work, Vaughan Jones for helpful conversations, Massimo Ferri for extraordinary hospitality while this work was 
coming forth, Sostenes Lins for the right question at the right time, and for many conversations about combinatorics 
ST.ATE MODELS AND THE JONES POLYNOMIALS 401 
and three-dimensional topology, Mario Rasetti for insightful and patient conversations about knots and physics, 
Ivan Handler for clarification of Proposition 2.9, Murasugi for a conversation resulting in Theorem 2.10 and finally, 
M. Kervaire and the mathematics department at Geneva for a most stimulating visit. 
Work on this paper was partially supported by CNR (Italy) while the author was Visiting Professor at the 
Dipartimento Matematica, Universita di Bologona, by IS1 (Torino) while the author was visiting at Politecnico di 
Torino, and by ONR Grant No. NOOl-t-84-K-0099 (Stereochemical Topology Project-University of Iowa). 
-Vote added in Proof 
The invariance of the twist number for reduced alternating diagrams has been proved (in- 
dependently) by Murasugi and Thistlethwaite.
