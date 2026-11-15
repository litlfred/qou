---
doc_id: ram1991-frobenius-formula
doc_title: "A Frobenius formula for the characters of the Hecke algebras"
section_id: sec-004-4-the-frobenius-formula-for-the-characters-o
section_title: "The Frobenius formula for the characters of H_f"
section_number: "4"
pages: 10-16
source_pdf: ram1991-frobenius-formula.pdf
source_sha256: 26b2fc85338d9150
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "A Frobenius formula for the characters of the Hecke algebras — This paper uses the theory of quantum groups and the quantum Yang-Baxter equation as a guide in order to produce a method of computing"
---
4 The Frobenius formula for the characters of H ,
The crucial step in this development is to evaluate the left hand side of the
expression in Theorem 3.8 by another means.
(4.1) Theorem. For 1 ≤ r ≤f the trace of the operator DTyr on V@r is given by
tr(DT,) = Z qe()(q - 1)()xi, Xiz . . . Xir 
where the sum is over all sequences I = (ii, i2,. . ., ir) such that 1 ≤ii ≤. . . ≤ir:
e(I) denotes the number ofi; = ij+ 1 in I and l(I) denotes the number ofi; < ij+1 in I.
Proof. The proof is by induction on r.
Case 1 ir-1 > ir:
Dwgr-1 . . . 91 lw = q1/2 D(w"viVir-1)gr-2 .. . 91 lv. Di, :
Since gr-2 . . . g1 acts only on the letters in w"vi, and Vir-1 + Vir, DwT,lw = 0.
Case 2 ir-1 < ir:
DwT,lw = (q - 1)DwTr-1 Iw + q1/2 w"Vi,Vir-1 Tr-1 Iw
= (q - 1)xir(Dw' Tr-1)lw + 0 .
Case 3 ir-1 = ir:
DwT,Iw = qDwTyr-1 /w = qxi(Dw' Tyr-1)lw, 
So, by induction,
tr(DT,)=  DwTy,/w
[wl = r
DVit Vi2 . . . Vi, Tyrlvit Viz .. . Vi.
1≤i,i2,...,i≤n
i≤iz≤...≤ir
A Frobenius formula for the characters of the Hecke algebras 471
(4.2) Proposition. For any composition c F f,
tr(DT) = I tr(DT.)
Proof. It is sufficient to prove that for permutations pe Sr, and oe Sr2, ri + r2 -- f,
tr(DTp×c) = tr(DT,)tr(DT) .
By direct computation, since T, acts only on the first ri letters of a word w and T
acts only on the remaining letters of w,
Z DwTp×alw = DwW1 W2 Tp ×a/ w1 w2
W1W2-W
[wil = r1, [w2l = r2
Dw1 T,lw1 Dw2 T.lw2
W1 W2
[wil = ri [w2l = r2
Remark. The above proposition is just a proof of the fact that the trace of the
action of Ha, @ Ha2 @... on the tensor product representation y@ai @
V@ 2  . . . is the product of the traces of the actions of the Ha, on V@ in.
-ring notation and Hall-Littlewood symmetric functions
In order to simplify the derivation of formulas for the irreducible characters of the
Hecke algebras we shall use α-ring notation for symmetric functions. The following
is a short exposition of 2-ring notation. The identities (4.3-4.10) are all well known
and can be found in [Mac].
An alphabet is a sum of commuting variables so that, for example,
X = xi + x2 + . . . + xn is the alphabet of commuting variables x1, . . :, Xn. In this
notation, if X = xi +...+ xn and Y- yi +...+ yn then XY represents the
alphabet of variables {xiyif1 ≤ i,j≤ n.
pr(0) = 0 ,
pr(x) = x" ,
pr(X + Y) = pr(X) + pr(Y) , (4.3)
pr(X Y) = pr(X)pr(Y) ,
where x is any single variable and X and Y are any two alphabets. For each
partition μ= (μi, μ2,. . ., μk) define
Pu(X) = pui(X)puz(X). . . Puk(X) 
For an alphabet X, we define
2(X) = exp
472 A. Ram
For each r ≥ O define the homogeneous symmetric function hr(X) to be the
coefficient of tr in 2(Xt), i.e.
2(Xt) = Z  hr(X)tr. (4.4)
r≥0
For a partition μ = (μ1, μ2, . . ., μk) define
hu(X) = hui(X)hμz2(X). . . huk(X) 
For any partition a  (a1, 22, : : . ), the Schur function Sa(X)in the alphabet X can
be given by
Sa(X) = det(hat-i+j(X)1≤i,j≤n 
where n ≥ t(), and hr(X) = 0 for any r < 0.
Let X, Y be two alphabets. The addition formula for Schur functions is
Sa(X + Y) = Z Su(X)sa/u(Y) . (4.5)
The duality formula for Schur functions is
sa(- X) =(- 1)lalsα(X) (4.6)
where a' denotes the conjugate partition to a.
For a brief moment let Sa, Su, S, denote the irreducible representations of the
symmetric group S, corresponding to the partitions a, μ, v f respectively. Set
Caμv to be the multiplicity of the representation Sa in the Kronecker product of
symmetric group representations Su  S,. The numbers cauv are symmetric with
functions is
sa(XY) = Z cauvsu(X)ss(Y) . (4.7)
u,y
Let ma(X) be the monomial symmetric function in the alphabet X. For any
alphabet X,
hu(X) = sa(X)Kau, 8 and
Sa(X) = Z Kaumμ(X) , (4.8)
where Kau is the Kostka number, the number of column strict fillings of the shape
 with weight u.
For alphabets X = xi +. . . + xn, Y= y1 +... + yn and a variable t,
2(XY(1 - t))  1 - txiyj (4.9)
1≤ij≤n 1 - xiyj
A Frobenius formula for the characters of the Hecke algebras 473
The following expansions of 2(X Y(1 -- t)) follow from the expansions in [Mac
Chapter I, $4].
2(X Y(1 - t)) = Z sa(X)sa(Y(1 -- t))
= Z ha(X(1 - t)ma(Y) (4.10)
pa(1
pa(X)pa(Y) ,
where a? is given by (1.1).
Chapter III of [MacJ is devoted to the study of Hall-Littlewood symmetric
functions. In particular the Hall-Littlewood symmetric function qr(x1, : . : , Xn; t) is
defined by
qo(x; t) = 1 ,
qr(x; t) = (1 - t)  x II Xi txj (r ≥ 1) .
i=1 ji Xi— Xj
For a partition μ,
t(μ)
qμ(x; t) = II qu(x; t) .
i=1
The generating function for the qr(x; t) is ([Mac, Chapter III (2.10)J)
 txiy
Z qr(x; t)y" = II (4.11)
r=0   Xiy
Expressions for tr(DTyr)
(4.12) Lemma. Let t be a variable and a  f. Then, in 2-ring notation,
[(1 - t)(- t)s-m, if α = (1}-mm) for some m ≥ 1 ;
Sa(1
otherwise .
Proof. By the addition formula
(1-)ns()"s  = (μ- l)"s
Su(1) = O unless μ = (k) for some k. Using duality,
S(- t)-k, if a/(k) is a vertical strip,
Sa/(k)(- t) = (- 1) -ks(a/(k)(t)  if a/(k) is not a vertical strip .
474 A. Ram
There are only two cases when 2/(k) is a vertical strip: either a = (1f-kk) or
 = (1}-k-1(k + 1). So if sa(1 - t) + 0,  = (1f -mm) for some m.
S1f-mm(1 - t) = S(k)(1)S(1 f - mm)/(k)( -- t)
(k) = (15-mm)
= S(1f-mm)/(m)(- t) + S(1f-mm)/(m-1)(- t)
=(- t)s-m +(- t)-m+1 (1 - t)(一 t)s-m. 
(4.13) Theorem. Let X = x1 + x2 + . . . + Xn. Then, in 2-ring notation, for r ≥ 1,
(a) tr(DTr) = - Z q"-t(M(q - 1)(μ - 1mu(X),
μr
(b) tr(DTr) = qr(X; q -1)
(c) tr(DTr)  hr(X(1 - q-1) ,
(d) tr(DTr) = I(qui - 1) pu(X) ,
u?
(e) tr(DTr) =
k=1
Injb
Proof. (a) follows immediately from Theorem 4.1. Let qr(X; q) = tr(DTyr) and
rewrite qr(x; q) in the form
t(μ)
gr(x; q) = - mu(X) .
q  1
If qo(x; q) =- 1/(q -- 1) then the generating function for the qr(x, q) is
It(μ)
Z qi(x; q)y" = q'y" Z mμ(X)
r≥0 ≥0 μr
q-1
+1
 qyxi
- 1/q + (1/q)(1 - qyxi)
1 - yxi
- (1/q)qyxi
1 - qyxi
giving (b).
-- (1/q)qyxi
= 2(Xqy(1 - q-1) ,
1 -- qyxi
A Frobenius formula for the characters of the Hecke algebras 475
and the expansions in (4.10) give
Z qi(x; q)y"  2(Xqy(1 - q-1)
r≥0
E su(X)su(qy(1 - q-1))
hr(X(1 - q-1))q"yr
≥0
I:(1 - q-μi)
Pu(X)q"y".
q-1 r≥0μｒ u?
(c) and (d) follow from the last two expressions respectively by comparing coeffic-
ients of yr with the left hand side. Using Lemma 4.12,
Zsu(X)su(qy(1 - q-1)) = Z Z su(X)qlulylulsu(1 -q-1)
≥0μr
q'y"  s u--(_b-)(_b- I)(x)(uu-)s
r≥0 m= 1
- Z y"(q - 1) Z (- 1)-mqm-1s(1r-mm)(X),
r≥0 m=1
giving (e). (f) follows immediately from (c). 
The Frobenius formula
Let mμu(x) and sa(x) denote the monomial 1 symmetric function and the
Schur 'function respectively, in the variables Xi,X2,..., Xn. Recall that
T,= gr-19r-2...91 and that for any partition Iμ=(μi,...,μk),
 T.X...×T..
For each r ≥ i, and each partition μ define
gr(x; q) = Z q" - t()(q - 1)t(v) - 1m,(x) ,
μr
t(μ)
qu(X1,. . ., Xn; q) = II qu(x; q),
i=1
respectively.
We have the following Frobenius type formula for the characters of Hf.
(4.14) Theorem. For each μ  f,
qu(x; q) = Z x^(T,)sa(x) ,
where x~ denotes the irreducible character of H corresponding to a and sa(x) denotes
the Schur function in the variables Xi, . . . , Xn.
476 A. Ram
Proof. The theorem follows immediately from Theorem 3.8 and Theorem
4.13(a).
