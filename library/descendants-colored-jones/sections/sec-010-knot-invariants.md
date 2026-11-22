---
doc_id: descendants-colored-jones
doc_title: "The descendant colored Jones polynomials"
section_id: sec-010-knot-invariants
section_title: "Knot invariants"
section_number: null
pages: 19-23
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
toc_source: outline
doc_brief: "The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the second author in 1994 on quantum"
---
We can use the r-matrix given in Equation (28) to construct knot invariants
from their planar projections. This is a standard construction explained in
several places that include [Jon89, RT90, Tur88, Tur94]. We will follow the
presentation of [Kas] which does not require neither the theory of Hopf alge-
bras nor the existence of ribbon elements, and uses as a combinatorial input a
generic planar projection of a long knot with no local extrema oriented from
left to right and equal numbers of positive and negative crossings. Locally,
such a planar projection has eight types of crossings (four positive and four
negative ones)
(47)
to which one assigns the suitably “rotated” r-matrices shown in Equations
(16)–(19) of [Kas], two types of vertical segments, and two types of local
extrema
(48)
2326 Stavros Garoufalidis and Rinat Kashaev

to which ones assigns respectively the identity operators and ¢ and 7 maps
of Equation (7) of [Kas]. In our case, we fix a primitive root of unity ¢ of
order N, a (discrete spectral parameter) n € Z/NZ and a planar projection
D of a long knot K’. We color each arc of D by an element of Z/NZ, place r-
matrices at the crossings (using the fixed spectral parameter at all crossings),
according to the rules described below, and sum over all indices. The result
of this contraction is a complex number that depends on the colors i and 7
of the outgoing and incoming arcs of the diagram of the long knot. These
complex numbers arrange in a matrix

(49) (Dy nn € Matn(Z[N*, ¢])

The r-matrices given below are rigid, i.e., satisfy the Yang-Baxter equation
(9) and the inverse matrix equation (10) of [Kas]. The next theorem follows
from the results of [Kas].

Theorem 3.1. The state-sum (D) yn» depends on the long knot K and not
on the planar projection D used.

It remains to explain the rules for the r-matrices.
Starting with the case with m = n = 0, we get the following rules for the
four types of positive crossings

(50)

x = x = < =Vige(Q)er, ~x< =Vieig (OC *
and for the four types of esate crossings

(51)

<< = ~< = x< =Vignu(Qe*, < =Viniga(QQer em.

Note that the weights of the negative crossings are the complex conjugates of
the corresponding weights of the positive crossings.
The descendant colored Jones polynomials 2327

Switching in now the general colors m and n, we get the rules for the
positive crossings

<->? mR PL Vigna Gerri eienn,
52
(52) Do
Le = Vieti-mg—n—1(G)G2 Bom
k L

and the negative crossings

i

dj a L L k
~< = >< = OX = Vig-ne—mi(O)C +( jtltn)m
CN EN OES

j i

=Vpti ni m—1(C) CRS (ken) |

“a Ny

k L

Note that for general m,n, the weights of the negative crossings are not the
complex conjugates of the corresponding weights of the positive crossings.
Note also that the eight r-matrices needed in Equations (16)—(19) of [Kas],
up to powers of ¢, are all expressed in terms of the symbols Vj,,4(¢) and
their complex conjugates Vj 5.41(0).

Additionally, we have relations between colored and uncolored weights

J a jm
s-b- dd Xe

(54) ran ran fas i n) mm
k » NO k-n
J a jrn i—m

7 = ~< CG-len)m
ad

k L k L
2328 Stavros Garoufalidis and Rinat Kashaev

in the case of positive crossings, and

j a i L L k jrn a
Sf Se SS SS crim
PX = FN = FN= 7 |
k L J k i J k—m L
(55)
i i j-m i-n
SS gtism
EQ SN
k L k L

in the case of negative crossings.
We complement the rules by the weights on the four types of segments
a Jj j
56 = |=O N= DS = big.
( ) I} { i j ——s a

j

With our rules, one can calculate weights of few simplest composed dia-
grams in the colored case

j i j i

(57) ret = Oi et1}y rot = 65,641} 6"

and

(58) Qe = 01.541 N> 2: = 6i{j+1no
J a Jj a

which imply that

(59) — . 1 = 0450", 2

. ¥ oA at ta

It is interesting to note, that the continuous spectral parameter can be
used in an alternative formulation of knot and link invariants along the idea
of Jones [Jon89] of considering a “statistical mechanics” model on piecewise
linear diagrams with straight segments where the multiplicative angles are
encoded in the continuous spectral parameters. In our case, such an approach
might be applicable only in the case with color n = —1 (mod N) but not for
The descendant colored Jones polynomials
2329
other values of n. In the case n ≡−1 (mod N), the starting graphical rules
would look like
(60)
k
l
j
i
x
= ⟨i, j|r(x; −1, −1)|k, l⟩,
j
i
x
= ⟨i|h(−1/x, 0)|j⟩,
where the continuous variables x’s are thought of as exponentiated angles eiα,
whose product around each vertex is 1.
