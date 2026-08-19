---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-034-28-don-zagier
section_title: "Don Zagier"
section_number: 28
pages: 26-28
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
The derivative with respect to x of the right-hand side of (4) (or of (2)) has
the same value and both sides of (4) (or of (2)) vanish at x =0 .
(iii) Write the right-hand side of (4) as
∑
m, n≥1
xm
m
yn
n +
∞∑
k=1
( −x
1 − x
) k 1 − (1 − y)k
k2
=
∑
m, n≥1
xmyn
[ 1
mn −
∑
n≤k≤m
(−1)k−1
k2
( m − 1
k − 1
)( k
n
)]
and then verify as an elementary combinatorial exercise that the expre ssion
in square brackets, which clearly equals 1
mn if m<n , vanishes if m ≥ n.
It seems very surprising that the beautiful identities (2) and (4) are not
better known.
D. The quantum dilogarithm The “quantum dilogarithm,” studied by
Faddeev-Kashaev [15], Kirillov [22] and other authors, is the function of t wo
variables deﬁned by the series
Li2(x; q)=
∞∑
n=1
xn
n (1 − qn) . (5)
It is a q-deformation of the ordinary dilogarithm in the sense that
lim
ε→0
(
ε Li2(x; e−ε)
)
=L i 2(x)( |x| < 1) ; (6)
indeed, using the expansion 1
1−e−t = 1
t + 1
2 + t
12 − t3
720 + ··· we obtain a
complete asymptotic expansion
Li2(x; e−ε)=L i 2(x) ε−1 + 1
2 log
( 1
1 − x
)
+ x
1 − x
ε
12 − x + x2
(1 − x)3
ε3
720 + ···
as ε → 0 with x ﬁxed, |x| < 1.
The function (5) belongs to the world of “ q-series.” These series, about
which there is a very extensive literature—with the letter “ q” having been
the traditional choice long before it was realized that there was any conne c-
tion with the “ q” of “quantum”—are functions of a formal (or small complex)
variable q which are given by convergent inﬁnite series whose terms are ratio-
nal functions of q with rational coeﬃcients. For instance, the q-hypergeometric
functions, a very important subclass which includes some classical modular
forms and related functions like Ramanujan’s “mock theta functions” ( which
have occurred in connection with quantum invariants of 3-manifolds [24] ) are
given by series whose nth term has the form ∏ n
i=1 R(q, qi) for some rational
function R(x, y) of two variables. The classical aspects of q-series are those
having to do with the behavior as q tends to 0 and typically are concerned
The Dilogarithm Function 29
with proving identities F (q)= G(q) between two given q-series considered
as elements of Q[[q]]. This is usually done either by purely combinatorial ar-
guments (such as interpreting the coeﬃcients of qn in F (q)a n d G(q)a st h e
numbers of partitions of n of two diﬀerent types and then giving a bijection
between these) or else via algebraic tricks such as introducing an e xtra para-
meter x and showing that both F (x, q)a n d G(x, q) satisfy the same functional
equations under x ↦→qx (as in the proof of Proposition 2 below). The quan-
tum aspects, on the other hand, are the ones that emerge when one studies
the asymptotic behavior of the q-series as q tends to 1 (or more generally to
a root of unity) rather than to 0, an example being the asymptotic expansi on
of Li 2(x; e−ε)a s ε → 0 given above.
In the study of q-hypergeometric functions and other q-series, an important
role is played by the q-analogues
(q)n :=
n∏
m=1
(1 − qm) , (x; q)n :=
n−1∏
i=0
(1 − qix)
of the classical factorial function and Pochhammer symbol, respective ly. One
can also allow n = ∞ and set
(q)∞ :=
∞∏
m=1
(1 − qm) , (x; q)∞ :=
∞∏
i=0
(1 − qi x),
the q-analogues of the classical gamma function; the function ( q)∞ is up to a
factor q1/24 the modular form η(τ ) (Dedekind eta-function), where q = e2πiτ .
Observe that the ﬁnite products can be expressed in terms of the i nﬁnite
ones by ( q)n =( q)∞/(qn+1; q)∞ and ( x; q)n =( x; q)∞/(qnx; q)∞. Following a
much-practised abuse of notation we will consider q as given and omit it from
the notations, writing simply ( x)n and ( x)∞ instead of ( x; q)n and ( x; q)∞ .
This causes no confusion with the notations ( q)n and (q)∞ since (q)n =( q; q)n
and ( q)∞ =( q; q)∞ , but is an abuse of notation because, for instance, ( q)2
means (1 −q)(1−q2) but ( x)2 means (1 −x)(1−qx) rather than (1 −x)(1−x2).
The ﬁrst surprise is now that the quantum dilogarithm Li 2(x; q) is essen-
tially equivalent to the q-gamma function ( x)∞ ! This is the third part of the
following simple (and well-known) result which gives the expans ions of the
functions ( x)∞,1 /(x)∞ and log( x)∞ as power series in x . All three formulas
will play a role in §3 in connection with Nahm’s conjecture.
Proposition 2. For x, q ∈ C with |x| < 1, |q| < 1 we have the power series
expansions
(x; q)∞ =
∞∑
n=0
(−1)n q(
n
2)
(q)n
xn , (7)
1
(x; q)∞
=
∞∑
n=0
xn
(q)n
, (8)
− log(x; q)∞ =L i 2(x; q) . (9)
