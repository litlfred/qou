---
doc_id: 1-s20-0040938385900047-main
doc_title: "ToporoPy Vol. 24, No. 3, pp. 307-332. 1985. 0040-9383185 s3.00+ .OO Printed III Great Britain. C 1985. Pcrgamon Press Ltd. VOLUMES OF HYPERBOLIC THREE-MANIFOLDS"
section_id: sec-005-6-examples
section_title: "Examples"
section_number: 6
pages: 21-25
source_pdf: 1-s2.0-0040938385900047-main.pdf
source_sha256: f0db9d97f2ae83c6
doc_brief: "ToporoPy Vol. 24, No. 3, pp. 307-332. 1985. 0040-9383185 s3.00+ .OO Printed III Great Britain. C 1985. Pcrgamon Press Ltd. VOLUMES OF HYPERBOLIC THREE-MANIFOLDS — 7 sections: Introduction; Combinatori"
---
We shall illustrate our results on the example of the figure eight knot complement. We 
first describe more explicitly what our results say in the case of one cusp. 
As described in $1, if the expansion of u = vi as a power series in u = u1 is 
0= 2 c,lA” (c, = 0 for n even), (52) n=1 
then the volume formula is 
Vol (M,) = Vol (M) + i Im (UC) + Im (J(u)) (53) 
= vol(M)-i 8 Im(c,u”ii)-i 
II 1 
4 z *m(~c.u”+i). 
I 1 
We can also invert series (52): 
u = C a,~” (a, = 0 for n even), 
a=1 
1 a, =-) *,=-C3 3c: cs 
Cl C:’ 
a, = 7-7, 
Cl Cl 
12c; 8~3~ a, = - -iT-- cl Cl 
and write the volume as 
Vol (M,) = Vol (M) - f z Im 
( 
n-l 
a,u”C+ -a u n+l . 
I) 1 n+l ” 1 
On the other hand the Dehn surgery coefficients (p, q) are determined by 
pu + qu = 2ni. 
By (52) we can write this as 
2ni A -_= --u + c$ + c$ + . . . 
4 4 
with 
A = p+c,q 
and applying the inversion formula (c.f. equation (54)) to solve for u gives 
(54) 
(55) 
(56) 
(57) 
(58) 
328 Walter D. Neumann and Don Zagier 
Inserting into (56) and solving for u gives 
_ (59) 
2 
lZc+8c~c,~+c,$ 2xi ’ 
+ A3 )( ) 
A + . . . . 
It is now a simple matter to express the ingredients of the volume formula (53) in terms of the 
Dehn surgery coefficients. Since, by (56), we have Im (uU) = Im 
we obtain from (59): 
iIm(nV)= -Im(c,) ~+aIm[c,(~~+(3c~~-c~)(~)” (60) 
+(1zc:~-8c,c,~+c,)(~)s + . . .]. 
A similar calculation yields 
+- 12c3d-8c c z+c 
3 
4 ( ‘A2 35A ,)($)“+ . ..I 
(61) 
n-l . 
where the term of degree 2n is always - n+l times the corresponding term in (60). Thus the 
volume formula becomes 
12~~42-8~ c g+c 3~2 35A . . .]. 
To illustrate this for the figure eight knot complement (shown in Fig. 15 in white on black) 
we shall use the ideal triangulation described by Thurston [7]. This triangulation uses two 
1-simplices, four 2-simplices, and two 3-simplices, identified as in Fig. 16. 
Let z and w denote the parameters of these tetrahedra with respect to the labelled edges and 
Fig. 15. 
Fig. 16. 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 329 
for any x E C* denote x’ = 1 - i and x” = (x’)‘. By inspection of the same identifications on 
the truncated tetrahedra (Fig. 17) one sees the triangulation of the torus at infinity. It is shown 
in Fig. 18; the pictured fundamental domain is bounded by our choice of basis m, G (this is the 
knot-theoretic meridian and longitude). One can read off the consistency relations 
z2z’wZw’ = 1, Z’(Z”)2W’(W”)2 = 1 
which simplify to 
zw(z-l)(w-1)= 1 
z-lw-l (z- l)-‘(w-l)-’ = 1, (63) 
so the matrix R of $2 is 
1 
R= 
1 1 1 
-1 -1 -1 -1 > . 
The holonomy of / and M can also be read off; they simplify to 
e: z2(1 - z)2 
m: w(l-z), 
so the matrix C of $2 is 
The matrix X of Proposition 2.5 is X = (2,2), and the various lemmas of $2 are easily verified. 
Now by (64) and by equations (28) and (29) we have 
u=log(w(l-z)) (65) 
0 = 2log(z(l -z)) = -2log(w(l -w)) (66) 
where the branches are chosen so u = u = 0 near the initial value z = w = l+ifi 
2 . Because 
Fig. 17. 
Fig. 18. 
330 Walter D. Neumann and Don Zagier 
of relation (63) there is only one degree of freedom (corresponding to the one cusp of our 
manifold). Computations are easier in this case if we take u as our local parameter and expand 
u as a power series in u, 
u = U(U) = f a,o”. 
!I=1 
Thus to compute the volume of M, as a power series in u (Equation (55)) we must know the 
coefficients a,. 
From (66) we get 
z(1 -z) = fP, w(1 -w) = e-“I’, 
or, solving the quadratic equations, 
where in each case the branch of the square root is chosen which is + ia at u = 0. Hence 
from (65) 
du 1 d(l-z), 1 dw 
dv=-- l-z do w do 
This is an even function of u, as desired. Also 
J& = h ( 1 +~Ce.” - 1) 
) -112 
where the Yim) are the Stirling numbers of the second kind, defined by (e’- l)m/m! 
=~Y~m)~n/n!orbyx”=~Y~m)x(x-l)...( x -m + 1) (the latter expression makes it 
clez that LY,$~)E Z ; in fact ‘9’ n (m) is the number of partitions of (1, . . . , n> into m non- 
empty subsets). Hence 
du 1 _=- fQ_ (- l)m(2m)! YArn, 
du 2amzo 2”n! m=O 3m m! 
n even 
and 
a, = 
“@!! yie), @ odd) 
m! 
(n even). 
VOLUMES OF HYPERBOLIC THREE-MANIFOLDS 331 
Numerically, this gives 
V 
u=- *+g+g(yy+&(q+...). 2fl ( 
(67) 
We could also have proceeded by solving (63) and (65) to get z and w as algebraic functions of 
e”, substituting into (66), and differentiating. The computation, similar to the one above but 
somewhat longer, gives: 
dv 2 1-2e”-2e-” 
du= Je2U+e-2y-2ey-2e-U+l 
1 23 89 u+ju3+180uS+- lo80u’+ . . . (68) 
which is the inverse expansion of (67) and gives the coefficients c, of equations (52) to (62). In 
particular, equation (53) gives 
U4 
Vol (M,) = Vol (M) - L(u) + - li4 23u6 23G6 - - 
4,./j +q+ ISO&+ 180$ 
and equation (62) becomes: 
89u* 89iP ___ - 
+960$+960$+ “’ 
2&? Vol (Mt,,q,) = Vol (M) - - 1 &?(A4 + 24) (2n)4 
IAl2 +fi 3lAl* 
+ 4q (A’ - A’) (27~)~ + - 23n(A6 + J6)(2@ 
31A114 270 IAl” 
+ -8,,‘=?q2(A10+A10)(2~)8 + -46q(A9-J9)(2n)* 
31A12’ 45 IAl’* 
+ 89G(As + 2*)(2n)’ 
2160 IAll 1 1 + . . . 
= Vol (M) - 2&? 
p2 + 12q2 
+4&P4 - 72p2q2 + 144q4)# + 
3@2 + 12q2)4 . . . . 
The computation of this expansion up to 2nd order originally led us to conjecture Theorem 
1 A, while it was an experimental computation of the above expansion in terms of u up to 6th 
order which first suggested Theorem 2 to us. 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9.
