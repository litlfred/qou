---
doc_id: roth-lemma
doc_title: "Chapter 5 ROTH'S LEMMA 1. Introduction Roth bases the proof of his theorem on a general property of polynomials which is to be proved in this chapter. This property is roughly as f"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: roth_lemma.pdf
source_sha256: c2f2b49f25f35919
doc_brief: "ROTH’S LEMMA — 4 sections: Introduction; For a detailed study of the genera; Put w(A) a e'J<A) if A ^0, andW(O)"
---
Roth bases the proof of his theorem on a general property of polynomials
which is to be proved in this chapter. This property is roughly as follows.
Let
A(Xl,...,xm)= 2
ii=0 im=0
be a polynomial in m variables, with integral coefficients which are not "too
large" in absolute values. Assume that
is a "very small" positive number. Further let
_ PI Pm
Qi ' *"' Qm
be m rational numbers written in their simplified forms for which both the
maxima
Hi =max(|Pi|,|Qi|),..., Hm = max(|Pml, iQml)
and the quotients
logH2 logH3 logHm
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
fy = fj/(xi,..., xm) (v = 1,2,..., n)
be n rational functions of m variables, with coefficients in a field K. The
functions are said to be linearly dependent (or for short, dependent) over K
if there are elements ci,..., cn of K not all zero such that
77
78 LECTURES ON DIOPHANTINE APPROXIMATIONS
Cifi+... + cnfn 5 0
identically in Xi ,,.., xm. If no such elements exist, then the functions are
called linearly independent (or for short, independent) over K. Evidently,
if fi ,..., fn are independent, none of these junctions can vanish identically.
Assume, in particular, that the coefficients of fi ,..., fn lie in the rational
field F , and that these functions are dependent over the real field P. Then
the functions are also dependent over r. For the identity cifi +...+cnfn = 0 is
equivalent to a finite system of linear equations
ci^ior + ... + cntoia = 0 (a = 1,2,..., s)
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
i,-.., xm) (v = 1,2,..., n)
be n rational functions with real coefficients, and let Di,..., Dn* be n dif-
ferential operators such that
the order of Dv does not exceed v-l (v = 1,2,..., n).
The determinant
Difi Dif2 ... D^
/
\ fi ... D2fa ... D2fn
Dnfi Dnf2 ... Dnfn
is called a generalised Wronski determinant or a Wronskian.
This Wronskian evidently vanishes identically when the operators
Di,..., Dn are not all distinct. It also vanishes identically if fi,..., fn are
linearly dependent over the real field. For an identity
cifi +...+ cnfn = 0
implies the n identities
ROTH'S LEMMA 79
... + cnDyfn E 0 (v = 1,2,..., n)... ,,..., .
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
fi, = Mx) (v = 1,2,..., n)
be n rational functions in one variable x which have real coefficients and
are independent over the real field; thus, in particular,
fn(x) * 0.
There is only one Wronskian of these functions that does not vanish trivially,
viz. that Wronskian which belongs to the operators
d d2 dn-1
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
(?;:::£:!)*0
Next one easily shows that, for any rational function g, identically
)•&*(
80 LECTURES ON DIOPHANTINE APPROXIMATIONS
Here choose g=fn~1. Then in the Wronskian on the left-hand side all but the
first element of the n-th column vanish, and this determinant reduces to
* 0.\jug... ins/ \*i-« An-i/
Hence, finally,
/^Di... Dm _ I DI ... DH-!\f~tt ± n
V fi ... fny \Fi... Fn-iy '
whence the assertion.
5. The general case.
From now on let
ri rm / \
fp(xi,..., xm) = L ••• Li *ii—im Xll-« xm (^ = 1,2,..., n)
ii=0 im=0
be n polynomials in xi,..., xm that have real coefficients and are independent
over the real field. We want to show that at lea'st one of the Wronskians in
these functions is not identically zero. In the special case m=l this asser-
tion has just been proved, even for the more general class of rational functions.
To reduce the general case to this special one, denote by x a new variable,
by g a positive integer exceeding all the degrees ri,..., rm, and put
YI ffn
U=0 im=0 1
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
*n '*'•
ROTH'S LEMMA 81
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
Ni Nn-1
Since W(x)^ 0, at least one of the terms on the right-hand side likewise is not
identically zero, so that, say,
\
But then also
(J D^ ^ ... Dn lkn.A ^0
\ii i2 is ... In /
We have thus the following result1
Lemma 1: Let fi,..., fn be n polynomials in m variables that have real
coefficients and are independent over the real field. Then there is at
least one Wronskian ( * *" - n ) that does not vanish identically. The\ii... in /
same assertion holds if the polynomials have rational coefficients and
are independent over the rational field.
The second assertion of the lemma holds, of course, because, as we saw
in §2, the polynomials are also independent over the real field.
