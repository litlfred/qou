---
doc_id: agt-v3-n1-p17-p
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-003-2-a-proof-using-orthogonal-polynomials
section_title: "A proof using orthogonal polynomials"
section_number: 2
pages: 5-9
source_pdf: agt-v3-n1-p17-p.pdf
source_sha256: df196f0a732ad6b9
doc_brief: "Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of"
---
Habiro’s proof of Theorem 1.1 uses the relationship with the quantum group
Uqsl2 . Here is another proof, using the method of orthogonal polynomials as in
[BHMV1].
Testing with the Sn -basis, we see that (8) holds if and only if
cn;−= ht−1Sni
hRn;Sni :
Thus, it is clear that an!−satisfying (8) exists, and to compute its coecients,
we just need to compute ht−1Sni.
As in [BHMV1], de
ne another bilinear form h ;i1 by
hx;yi1 =ht(x);t (y)i :
De
ne polynomials R
n and S
n by
t(R
n)= nRn;t (S
n)= 2nSn :
(The factors n and 2n are included so that R
n and S
n are monic, i.e. have
leading coecient equal to one.)
Again, the R
n form a basis ofB,a n dt h eS
n form a basis of the even partBev
ofB, since the twist map t preservesBev .W eh a v ehR
n; S
mi1 =0f o r n6=m,
and
hR
n; S
ni1 =n2nhRn;Sni : (10)
Note thatht−1Sni =−1
2nhS
ni. Thus, we just need to compute hS
ni.
Proposition 2.1 The polynomials S
n satisfy a four-term recursion formula
S
n+1 =(z2−
n)S
n−
n−1
S
n−1−γn−2
S
n−2 (11)
for certain 
n;
n−1;γn−22Z[A]:
Algebraic &GeometricTopology, Volume 3 (2003)
542 Gregor Masbaum
Proof Since S
n is monic of degree 2n,w eh a v et h a tz2
S
n−S
n+1 is a linear
combination of the S
k with kn. The coecients can be computed by taking
the scalar product with R
k . So we just need to show that hz2
S
n; R
ki1 =0i f
k<n −2.
The point is that multiplication by z is a self-adjoint operator with respect to
the bilinear form h ; i1 . In other words, one has
hzx;yi1 =hx;zyi1
for all x;y2B . (This is because hx;yi1 =ht(xy)i.) It follows that
hz2
S
n; R
ki1 =hS
n;z 2
R
ki1 =0 i f k<n −2;
since R
k has degree k,a n d S
n annihilates all polynomials of degree <n .
Note that the coecients in the recursion formula (11) are given by

n =hz2
S
n; R
ni1
hS
n; R
ni1
;
 n−1 =hz2
S
n; R
n−1i1
hS
n−1; R
n−1i1
;γn−2 =hz2
S
n; R
n−2i1
hS
n−2; R
n−2i1
: (12)
By convention, if n< 0t h e nR
n; S
n;
n;
n;γn are all zero.
Proposition 2.2 One has

n =2 + a6n+4[3]−a2n (13)

n−1 =( a4n+1 +a8n+1[3])f2ngf2n +1g (14)
γn−2 = a10n−4f2n−2gf2n−1gf2ngf2n +1g (15)
Proof The formula for γn−2 is the easiest. Let us use the notation on for
terms of degree n.S i n c ez2
R
n−2 = R
n +on−1 ,w eh a v e
hz2
S
n; R
n−2i1 =hS
n;z 2
R
n−2i1 =hS
n; R
ni1 ;
and hence formula (15) follows from (12), (10), and (5).
For
n−1 , we need to compute
hz2
S
n; R
n−1i1 =hS
n;z 2
R
n−1i1 =2nn−1hSn;tz 2t−1Rn−1i : (16)
This amounts to computing the coecient ofRn in the expression oftz2t−1Rn−1
in the Rk -basis. This coecient can be computed as follows.
Forn 1, one has
zn =en +(n−1)en−2 +on−4 :
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 543
(This follows by induction from (2).) Thus, for " =1, one has
t"zn ="
nzn +(n−1)("
n−2−"
n)zn−2 +on−4 :
It follows that
tz2t−1zn = n+2
n
zn+2 +( 2−(n +1 )n+2
n
+(n−1) n
n−2
)zn +on−2 : (17)
Now write
Rn =
n−1Y
i=0
(z−2i)= zn−xn−1zn−1 +on−2 ;
where xn−1 =Pn−1
i=0 2i . Then (17) gives
tz2t−1Rn−1 = n+1
n−1
Rn+1 +(xn
n+1
n−1
−xn−2
n
n−2
)Rn +on−1 (18)
and hence
hSn;tz 2t−1Rn−1i =(xn
n+1
n−1
−xn−2
n
n−2
)hSn;Rni :
Plugging this into (16), we have
hz2
S
n; R
n−1i1 =2nn−1hSn;tz 2t−1Rn−1i
=(xn
n+1
n
−xn−2
n−1
n−2
)hS
n; R
ni1
=(A6n+1[3] +A−2n+1)hS
n; R
ni1 :
Using (12), (10), and (5) as before, this implies formula (14) for 
n−1 .
Finally, for 
n , let us compute
hz2
S
n; R
ni1 =2nnhtz2t−1Sn;Rni : (19)
This amounts to computing the coecient of Sn in the expression of tz2t−1Sn
in the Sk -basis.1
The computation is similar to the one above. We write
Sn =
n−1Y
i=0
(z2−2
i )= z2n−yn−1z2n−2 +o2n−4 ;
1This is easier than computing hSn;tz 2t−1Rni by expanding tz2t−1Rn in the Rk -
basis, because the latter would require computing the 
rst three terms, and not just
the 
rst two terms as in (18) above and also in (20) below.
Algebraic &GeometricTopology, Volume 3 (2003)
544 Gregor Masbaum
where yn−1 =Pn−1
i=0 2
i . Then (17) gives
tz2t−1Sn = (20)
2n+2
2n
Sn+1+

2+( yn−2n−1)2n+2
2n
−(yn−1−2n +1 ) 2n
2n−2

Sn +o2n−2
and hence
htz2t−1Sn;Rni =

2+( yn−2n−1)2n+2
2n
−(yn−1−2n +1 ) 2n
2n−2

hSn;Rni
=( 2+ a6n+4[3]−a2n)hSn;Rni :
Plugging this into (19), we get
hz2
S
n; R
ni1 =( 2+ a6n+4[3]−a2n)hS
n; R
ni1 ;
proving formula (13) for 
n .
Proof of Habiro’s Theorem 1.1 As already observed, we have
cn;−= ht−1Sni
hRn;Sni =−1
2n
hS
ni
hRn;Sni :
ButhS
ni satis
es the recursion relation
hS
n+1i =(2
0−
n)hS
ni−
n−1hS
n−1i−γn−2hS
n−2i (21)
(sincehzi =0 ). It follows that
hS
ni =(−1)na(3n2+n)=2fn +1gfn +2gf 2n +1g
f1g ; (22)
since one can check that (22) is true for n =0 ; 1; 2 and that it solves the
recursion (21). This implies Habiro’s formula (9) for cn;−. Taking conjugates,
one then also obtains formula (7) for cn;+ .
Remark 2.3 Although it might be hard to guess formula (22), once one knows
it the recursion relation (21) is easily checked. Observe that 2
0 =a2 +a−2−2.
Put q(n)=( 3n2 +n)=2. Then (21) is equivalent to
(a2 +a−2−a6n+4[3] +a2n)aq(n) +(a4n+1 +a8n+1[3])fngaq(n−1)
−a10n−4fn−1gfngaq(n−2) =−f2n +2gf2n +3g
fn +1g aq(n+1)
which is a straightforward computation.
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 545
