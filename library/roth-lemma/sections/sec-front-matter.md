---
doc_id: roth-lemma
doc_title: "ROTH'S LEMMA"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-11
source_pdf: roth_lemma.pdf
source_sha256: c2f2b49f25f35919
toc_source: inferred
doc_brief: "ROTH'S LEMMA — 2 sections: Front matter; JL^..+JaL"
---
Chapter 5
ROTH'S LEMMA
1. Introduction
Roth bases the proof of his theorem on a general property of polynomials
which is to be proved in this chapter. This property is roughly as follows.
Let
A(Xl,...,xm)= 
2
ii=0 
im=0
be a polynomial in m variables, with integral coefficients which are not "too
large" in absolute values. Assume that
is a "very small" positive number. Further let
_ PI 
Pm
Qi ' *"' 
Qm
be m rational numbers written in their simplified forms for which both the
maxima
Hi =max(|Pi|,|Qi|),..., Hm = max(|Pml, iQml)
and the quotients
logH2 logH3 
logHm
log Hi' logH2''"' logHm-1
are "very large". Then A(XI,..., xm) cannot vanish to a "very high" order
at xi = KI ,..., xm=Km. (An exact formulation of Roth's Lemma will be given at
the end of this chapter).
The main idea of the proof consists in an induction for m, the number of
variables, the case m=l being trivial. This induction uses a test for linear
independence of polynomials in terms of the so-called generalised Wronski
determinants.
2. Linear dependence and independence.
Let
fy = fj/(xi,..., xm) 
(v = 1,2,..., n)
be n rational functions of m variables, with coefficients in a field K. The
functions are said to be linearly dependent (or for short, dependent) over K
if there are elements ci,..., cn of K not all zero such that
77
78 
LECTURES ON DIOPHANTINE APPROXIMATIONS
Cifi+... + cnfn 5 0
identically in Xi ,,.., xm. If no such elements exist, then the functions are
called linearly independent (or for short, independent) over K. Evidently,
if fi ,..., fn are independent, none of these junctions can vanish identically.
Assume, in particular, that the coefficients of fi ,..., fn lie in the rational
field F , and that these functions are dependent over the real field P. Then
the functions are also dependent over r. For the identity cifi +...+cnfn = 0 is
equivalent to a finite system of linear equations
ci^ior + ... + cntoia = 0 
(a = 1,2,..., s)
for GI,..., cn with rational coefficients $va. By the hypothesis the rank of
the matrix of this system of equations is smaller than n. The system has
therefore also a solution ci,..., cn in rational numbers not all zero, whence
the assertion.
Conversely, if fi,..., fn have rational coefficients and are independent
over F, then they are also independent over P.
3. Generalised Wronski determinants.
The letter D, with or without suffixes, will be used to denote differential
operators of the form
8Ji + ... + Jm
where ]i,..., jm are non-negative integers. The sum ji+...+jm of these inte-
gers is called the order of D. Thus the unit operator 1 has the order 0 be-
cause ji=...=jm=0«
Let
i,-.., xm) 
(v = 1,2,..., n)
be n rational functions with real coefficients, and let Di,..., Dn* be n dif-
ferential operators such that
the order of Dv does not exceed v-l 
(v = 1,2,..., n).
The determinant
Difi Dif2 ... D^
/
\fi ...
D2fa ... D2fn
Dnfi Dnf2 ... Dnfn
is called a generalised Wronski determinant or a Wronskian.
This Wronskian evidently vanishes identically when the operators
Di,..., Dn are not all distinct. It also vanishes identically if fi,..., fn are
linearly dependent over the real field. For an identity
cifi +...+ cnfn = 0
implies the n identities
ROTH'S LEMMA 
79
... + cnDyfn E 0 
(v = 1,2,..., n).
.. 
,,..., .
If now ci ,..., en are not all zero, then the determinant of this system of linear
equations for Ci ,..., cn vanishes, and this determinant is the Wronskian we
considering.
Let these two trivial cases be excluded. It will then be proved that at
t one Wronskian of the given functions is not identically zero, at least
fi ,..., fn are polynomials.
least
when
4. The case of functions of one variable.
Let
fi, = Mx) 
(v = 1,2,..., n)
be n rational functions in one variable x which have real coefficients and
are independent over the real field; thus, in particular,
fn(x) * 0.
There is only one Wronskian of these functions that does not vanish trivially,
viz. that Wronskian which belongs to the operators
d 
d2 
dn-1
We show by induction for n that this Wronskian is in fact distinct from zero.
This is obvious for n=l since then
to.
Let therefore n ^ 2, and assume that the assertion has already been proved
for n-1 functions.
Put
These n-1 functions are still independent. For any equation
ClF1+...+Cn-lFn-l -
, with real coefficients implies, on integrating, that
cifi+...+cn-lfn-l B
where cn is a further real number, whence ci = ...=cn-l=Cn=0 because
fi ,..., fn are independent by hypothesis.
It follows then from the induction hypothesis that
(?;:::£:!) *0
Next one easily shows that, for any rational function g, identically
)•&*(
80 
LECTURES ON DIOPHANTINE APPROXIMATIONS
Here choose g=fn~1. Then in the Wronskian on the left-hand side all but the
first element of the n-th column vanish, and this determinant reduces to
* 0.
\jug... ins/ 
\*i-« An-i/
Hence, finally,
/^Di... Dm _ I DI ... DH-!\f~tt ± n
V fi ... fny 
\Fi... Fn-iy 
'
whence the assertion.
5. The general case.
From now on let
ri 
rm 
/ \
fp(xi,..., xm) = L ••• Li 
*ii—im Xll-« xm 
(^ = 1,2,..., n)
ii=0 
im=0
be n polynomials in xi,..., xm that have real coefficients and are independent
over the real field. We want to show that at lea'st one of the Wronskians in
these functions is not identically zero. In the special case m=l this asser-
tion has just been proved, even for the more general class of rational functions.
To reduce the general case to this special one, denote by x a new variable,
by g a positive integer exceeding all the degrees ri,..., rm, and put
YI 
ffn
U=0 
im=0 1
(v = 1,2,..., n).
The exponents ii+iag+i3g?+...+imgm""1.of x maybe considered as
representations to the basis g, with ii, i2,..., im as the digits; for by the
choice of g these numbers may assume only the values 0, 1, 2,..., g-1. Since
there is only one representation of any integer to the basis g, it follows that
no two terms in the multiple sum for ^(x) are constant multiples of the same
power of x.
This implies that <£i (x),..., <fri(x) likewise are independent over the real
field. For let ci,..., cm be real numbers such that Ci0i+...+cn0n= 0. By
what has just been shown, this identity requires that
But then cifi+...+cnfn E 0> whence ci=...=cn=0 by the assumed independence
of fi,..., fn«
The result of §4 may then be applied to fa,..., <fa, giving
d2
*n 
'*'•
ROTH'S LEMMA 
81
Denote now by 6 the linear operator
5 -
and by the sign ( ) * the operation of substituting
x, xS, xS*,..., xS111"1 for xi, X2, xs,..., xm, respectively.
In this notation, evidently
and
It follows that repeated differentiation of <£j,(x) leads to a relation
1, . . . ,xm)}*.
Here N^ is a positive integer depending on f-m/^1,..., i/'/zNn a1"6 polynomials
in x; and Dpii,..., d^Nn arp differential operators at most of order p in the
variables xi ,..., xm. The polynomials and the operators depend on ju, but
not on the functions fy or fo/.
Replace now in the determinant W(x) the terms -=-» ^(x) by their ex-
pressions in the derivatives of fj/(x). Then each term in the determinant
becomes a sum, and W(x) takes the form
Ni 
Nn-1
Since W(x)^ 0, at least one of the terms on the right-hand side likewise is not
identically zero, so that, say,
\
But then also
(J D^ ^ ... Dn lkn.A ^0
\ii 
i2 
is ... 
In 
/
We have thus the following result1
Lemma 1: Let fi,..., fn be n polynomials in m variables that have real
coefficients and are independent over the real field. Then there is at
least one Wronskian ( * *" - n ) that does not vanish identically. The
\ii... in /
same assertion holds if the polynomials have rational coefficients and
are independent over the rational field.
The second assertion of the lemma holds, of course, because, as we saw
in §2, the polynomials are also independent over the real field.
1. For a detailed study of the generalised Wronskian see, in particular, A. Ostrow-
ski, Math. Z. 4 (1919), 223-230.
82 
LECTURES ON DIOPHANTINE APPROXIMATIONS
6. An Identity.
By means of Lemma 1 we shall prove a general identity which is basic
for the later induction.
Assume that m ^2, and denote by
ri 
rm 
.
A(XI ,...,xm) = Z — S 
aii ...im xl1 — x^ * 0
ii=0 im=0
a polynomial with integral coefficient. Since
A(X1 ..... xm) =
im=0\ii=0 im_i=0
it is always possible to write the polynomial in at least one way as a sum
n
A(XI ,...,xm) = £ -Pi/xi i— >xm-i)Sj,(xm)
v=l
where Pi,...,Pn are polynomials in xi,...,xm-i and Si ,...,2^ are polynom-
ials in xm, all with rational coefficients. From now on choose one such
representation for which the number n of terms is a minimum; then
Let us call this the minimum representation of A.
In the minimum representation, both the n polynomials
Pi (xi ,...,xm-l),.-., Pn(xi ,...,
and the n polynomials
are independent over the rational and hence also over the real field (§2). For
assume, say, that there are rational numbers ci ,..., cn not all zero such that
ciPx +...+cnPns°J let e-g-> cn+0. On solving for Pn,
PnsyiPi+—+yn-lPn-l
where yi,...,yn-l are rational numbers. Hence we obtain a new representa-
tion of A,
n-1 
^ 
#
A(xl9...,xm) = 2) Pl/-l(x1,...,xm-i)S (xm) where S (xm) = 2v(xm) + rvZn(xm.
v=l 
,
with at most n-1 terms, contrary to the definition of the minimum representa-
tion. The independence of 1^ ,...,£n is proved in the same way.
By Lemma 1 there exist then two Wronskians
that do not vanish identically. Here, in the Wronskian U*,
ROTH'S LEMMA 
83
*
with certain non-negative integers jpi,..., Jym-l
On the other hand, in the Wronskian V**,
Ji/m
D* = 
i 
where km^-l 
G> = 1,2,..., n).
Denote by D^ and A^j, the new operators
* **
9 ll 
3
- xm-l m
and
Further put
D12A ... DmA
D2iA D22A ... D2nA
... DnnA
••• AmA
A21A A22A ... A2nA
An2A ... AnnA
Thus
W(xi ,...,xm) = C W*(xi ,...,xm)
where C=K) is a certain rational number.
On differentiating the minimum representation of A, we obtain the sys-
tem of identities
n
Therefore, by the multiplication law for determinants,
W*(xi,...,xm) = U*(xi,...,xm-i)V**(xm)
and hence also
= CU*(xi,...,xm_i)V**(xm).
It is obvious that all three determinants U*, V**, and W are polynomials
with rational coefficients in some or all of the variables xi,..., xm. Moreover,
the stronger result holds that W has integral coefficients. 
For if ji,..., jm
are arbitrary non-negative integers, the partial derivative
84 
LECTURES ON DIOPHANTINE APPROXIMATIONS
has the explicit form
ii -ji 
im-Jm
11 
... xm
and hence is a polynomial with integral coefficients. On the other hand, the
general element in the determinant W is exactly
hence is such a polynomial, and so the same is true for W.
Now a well-known theorem due to Gauss states that if f and g are poly-
nomials in any number of variables with rational coefficients such that the
product fg has integral coefficients, then there exists a rational number
c±0 such that both cf and c"1g have integral coefficients. On applying this
theorem to the two polynomials CU* and V**, we find that there are two
rational numbers jx+0 and w¥Q such that
U(xi,...,xm-i) = uU*(xi,...,xm-i) and V(xm) = vV**(xm)
have integral coefficients, and that further
W(xi,...,xm) = U(xi,...,xm-i)V(xm).
The following result has thus been obtained.
Lemma 2: Let
ri 
r5f
ii=0 
im=0
be a polynomial with integral coefficients. 
There exist a positive in-
teger n not greater than rm+1 and a system of n2 operators
A]LB/ =-
where j^i,..., jpim-l* Ji/m are non-negative integers such that
and that the following properties hold. The determinant
AH, A Ai2A ... Am A
A2iA A22A ... A 2n A
AmA ^A ... AnnA
does not vanish identically, is a polynomial with integral coefficients, and
can be written as a product
= U(xi,...,xm-i)V(xm)
where U and V are likewise polynomials with integral coefficients.
ROTH'S LEMMA 
85
7. Majorants for U,V and W.
If
^ 
1v?1
A(xi,...,xm) = E ... E ai
ii=0 
im=0
and
ri 
rm
B(Xl,...,xm)= E - E ^
ii=0 
im=0
are two polynomials with real coefficients such that
'aii ...im I * bii ...im 
for all suffixes ii ,..., im,
then B is said to be a majorant or majoriser of A, and we write
A«B.
It is obvious that this relation has the following properties.
// A « B and B «C, then A «C.
If A « 
Band C «D, then A*C «B +D and AC «BD.
If A < < B, and c is any real number, then cA« |c |B.
The relation A«B 
may be differentiated arbitrarily often with respect
to any of the variables.
We also use the notation,
and call [A] the height of A. This agrees with the definition of the height of
a polynomial in a single variable given in Chapter 3.
We consider now again the polynomial
ri 
rm 
.
A(xi,...,xm) = Z ••• E 
aii...im
Xl1— *r&
ii=0 im=0
of Lemma 2 and denote its height by
a= |Al.
By the binomial theorem,
Hence A has the majorant
A(xi ,...,
On differentiating this formula repeatedly, we find that
86 
LECTURES ON DIOPHANTINE APPROXIMATIONS
Here
so that
In particular, it follows that
AMy A<<2ri+"'+rma(l+xi)ri... (l+xm)rm 
(&v = 1,2,..., n).
Now, by its definition as a determinant,
where the summation extends over all n! systems of suffixes Mi>JU2,...
that are permutations of 1,2, ...,n. Therefore, on replacing the factors
AJUJ/A by their major ants,
)ri ... (l+xm)rm}n.
Since
U +x) n r=Z
k=0
this formula may be simplified to
W(x1,...,xm)«22n(ri+-+rm)ann
«2nr(l+x+...+xnr),
The majorant for W so obtained implies analogous majorants
,...,^.!) «22n(ri+-+rm)ann!
V(xm) «22n(ri+-+rm)ann!
for U and V. For, by construction, W=UV where U depends only on the
variables xi,...,xm_i and V only on the remaining variable xm; further-
more, all these polynomials have integral coefficients. Thus the product of
any coefficient of U with any coefficient of V is a coefficient of W. Since the
non- vanishing coefficients have at least the absolute value 1, it follows that
max(ITjl, [Vl) < Iwl,
whence the asserted majorants for U and V. In this way the following result
has been proved.
Lemma 3: Let A, U, V, W, and n be as in Lemma 2, and let
a=22n(n+...+rm)n, [^n. ^ nr1,...,pm.i=nrm-i,pm = nrm.
ROTH'S LEMMA 
87
Then
max([ul, [Vl, [W|)«a,
and the degrees of U in xi,...,xm_i do not exceed pi,...,pm-l> &&
degree of V in xm does not exceed pm, and the degrees of W in
xi,...,xm do not exceed pi,...,pm> respectively.
8. The index of a polynomial.
For any m£l, let
be m rational numbers written in their reduced forms so that
(P1,Q1) = ... = (Pm,Qm) = l.
The positive integers
Hi =max(|Pil,|Qi|),...,Hm = max(|Pm|,|Qm|)
are then called the heights of KI,..., Km, respectively. Let further pi,...,pm
be m arbitrary positive numbers, and let again
^ 
rm 
i 
i
A(xi,...,xm)= Jj — E ai 
imxi1...xn
m*0
ii=0 
im=0
be a polynomial in xi ,...,xm with integral coefficients which is not identically
zero. Hence the derivatives
x ) 3il+-+3mA(x1 ..... xm)
»-->xm' ~ 
* 
4
jil... Jm!9x3i1...3xm
m
cannot all vanish at the point Xi = KI ,...,xm= /cm. Denote by
J(A) = J(A; pi,...9pm;Kiy...9Km)
the smallest value of
