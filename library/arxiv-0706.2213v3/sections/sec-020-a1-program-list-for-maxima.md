---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-020-a1-program-list-for-maxima
section_title: "A.1. Program list for Maxima"
section_number: null
pages: 31-32
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
Reidemeister torsion for a given twist knot. This program works on the free computer al-
gebra system Maxima [Sa06]. The function R(m) in the list computes the Riley polynomial
of J(2, 2m). The function T(m) computes the twisted Reidemeister torsion for J(2, 2m). It
gives a polynomial of s and u such that the top degree of u is lower than that in the Riley
polynomial φJ(2,2m)(s, u). Here we use Expressions (49) & (51) and the following remark
for computing the twisted Reidemeister torsion.
Remark 24. It follows from Equation (34) that the highest degree term of u in φJ(2,2m)(s, u)
is equal to −u2m−1 (resp. u2|m|) if m > 0 (resp. m < 0).
Program list
load("nchrpl");/*We need this package for using mattrace*/
R(m):=block(/*function for calculating the Riley polynomial of J(2,2m)*/
[/*w is the matrix of w=[y,xˆ{-1}]*/
w:matrix([1-s*u,1/s-u-1],[-u+s*u*(u+1),(-u)/s+(u+1)ˆ2]),
p],
w:wˆˆm,
p:w[1,1]+(1-s)*w[1,2],
p:expand(p),
return(p)
);
T(m):=if integerp(m) then
if m=0 then "J(2,0) is unknot." else
block(
[/*matrix for adjoint action of x*/
X:matrix([s,-2,(-1)/s],[0,1,1/s],[0,0,1/s]),
/*matrix for adjoint action of y*/
Y:matrix([s,0,0],[s*u,1,0],[(-s)*uˆ2,(-2)*u,1/s]),
IX,/*inverse matrix of X*/
IY,/*inverse matrix of Y*/
S:ident(3),/*marix for series of W or Wˆ{-1}*/
AS:ident(3),/*adjoint matrix of S*/
W,/*matrix W=[Y,IX] */
IW,/*matrix [IX,Y]*/
d:1,/*the highest degree of u in the numerator
of R-torsion*/
k:1,/*the highest degree of u in the Riley poly*/
p:0,
r:R(m),/*the Riley poly*/
r1 /*a polynomial removed the top term of u
from the Riley polynomial*/
],
IX:invert(X),
IY:invert(Y),
W:Y.IX.IY.X,
IW:IX.Y.X.IY,
/*calculating the numerator of R-torsion*/
if m>0 then
block(
/*calculation of S*/
for i:1 thru m-1 do(S:ident(3)+S.IW),
AS:adjoint(S),
/*the numerator of R-torsion*/
p:p+mattrace(IX.S),
p:p+3*mattrace(X.AS)+mattrace(IY.W.AS),
31
p:p-mattrace(IX.S)*mattrace((ident(3)+IX.Y).S),
p:p+mattrace(IX.S.(ident(3)+IX.Y).S),
p:p+(2-s+(-1)/s)ˆ2*determinant(S),
/*The top term of u in the Riley poly r
is given by -uˆ(2m-1).
We use the relation uˆ(2m-1) = r + uˆ(2m-1) later*/
k:2*m-1,/*the highets degree of u in the Riley poly*/
r1:r+uˆ(2*m-1)
)
else
block(
/*calculation of S*/
for i:1 thru -m-1 do(S:ident(3)+S.W),
AS:adjoint(S),
p:p-mattrace(IX.S.W),
p:p+3*mattrace(X.IW.AS)+mattrace(IY.AS),
p:p-mattrace(IX.S.W)*mattrace((ident(3)+IX.Y).S.W),
p:p+mattrace(IX.S.W.(ident(3)+IX.Y).S.W),
p:p-(2-s+(-1)/s)ˆ2*determinant(S),
/*The top term of u in the Riley poly r
is given by uˆ(2|m|).
We use the relation uˆ(2|m|) = -r + uˆ(2|m|) later*/
k:2*(-m),/*the highets degree of u in the Riley poly*/
r1:-r+uˆ(2*(-m))
),
p:expand(p),
/* simplify by using r (decreasing the degrees of u)*/
/* set the degree of u in p*/
d:hipow(p,u),
/*decreasing the degrees of u*/
for j:1 while d >= k do(
p:subst(r1*uˆ(d-k),uˆd,p),
p:expand(p),
d:hipow(p,u)
),
p:factor(p),
/*multiplying p
by the denominator of twisted Alexander*/
p:expand(p*(s/(sˆ2-2*s+1))),
p:factorout(p,s),
r:factorout(r,s),
print("The Riley polynomial of J(2,",2*m,"):",r),
print("The Reidemeister torsion for J(2,",2*m,"):"),
return(p)
)
else print(m,"is not an integer.");
