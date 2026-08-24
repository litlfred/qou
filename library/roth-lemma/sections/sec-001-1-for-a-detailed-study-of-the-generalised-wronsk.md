---
doc_id: roth-lemma
doc_title: "Chapter 5 ROTH'S LEMMA 1. Introduction Roth bases the proof of his theorem on a general property of polynomials which is to be proved in this chapter. This property is roughly as f"
section_id: sec-001-1-for-a-detailed-study-of-the-generalised-wronsk
section_title: "For a detailed study of the generalised Wronskian see, in particular, A. Ostrow-"
section_number: 1
pages: 5-12
source_pdf: roth_lemma.pdf
source_sha256: c2f2b49f25f35919
doc_brief: "ROTH’S LEMMA — 4 sections: Introduction; For a detailed study of the genera; Put w(A) a e'J<A) if A ^0, andW(O)"
---
ski, Math. Z. 4 (1919), 223-230.
82 LECTURES ON DIOPHANTINE APPROXIMATIONS
6. An Identity.
By means of Lemma 1 we shall prove a general identity which is basic
for the later induction.
Assume that m ^2, and denote by
ri rm .
A(XI ,...,xm) = Z — S aii ...im xl1 — x^ * 0
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
n-1 ^ #
A(xl9...,xm) = 2) Pl/-l(x1,...,xm-i)S (xm) where S (xm) = 2v(xm) + rvZn(xm.
v=l ,
with at most n-1 terms, contrary to the definition of the minimum representa-
tion. The independence of 1^ ,...,£n is proved in the same way.
By Lemma 1 there exist then two Wronskians
that do not vanish identically. Here, in the Wronskian U*,
ROTH'S LEMMA 83
*
with certain non-negative integers jpi,..., Jym-l
On the other hand, in the Wronskian V**,
Ji/m
D* = i where km^-l G> = 1,2,..., n).
Denote by D^ and A^j, the new operators
* **
9 ll 3
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
the stronger result holds that W has integral coefficients. For if ji,..., jm
are arbitrary non-negative integers, the partial derivative
84 LECTURES ON DIOPHANTINE APPROXIMATIONS
has the explicit form
ii -ji im-Jm11 ... xm
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
ri r5f
ii=0 im=0
be a polynomial with integral coefficients. There exist a positive in-
teger n not greater than rm+1 and a system of n2 operators
A]LB/=-
where j^i,..., jpim-l* Ji/m are non-negative integers such that
and that the following properties hold. The determinant
AH, A Ai2A ... Am A
A2iA A22A ... A 2n A
AmA ^A ... AnnA
does not vanish identically, is a polynomial with integral coefficients, and
can be written as a product
= U(xi,...,xm-i)V(xm)
where U and V are likewise polynomials with integral coefficients.
ROTH'S LEMMA 85
7. Majorants for U,V and W.
If
^ 1v?1
A(xi,...,xm) = E ... E ai
ii=0 im=0
and
ri rm
B(Xl,...,xm)= E - E ^
ii=0 im=0
are two polynomials with real coefficients such that
'aii ...im I * bii ...im for all suffixes ii ,..., im,
then B is said to be a majorant or majoriser of A, and we write
A«B.
It is obvious that this relation has the following properties.
// A « B and B «C, then A «C.
If A « Band C «D, then A*C «B +D and AC «BD.
If A < < B, and c is any real number, then cA« |c |B.
The relation A«B may be differentiated arbitrarily often with respect
to any of the variables.
We also use the notation,
and call [A] the height of A. This agrees with the definition of the height of
a polynomial in a single variable given in Chapter 3.
We consider now again the polynomial
ri rm .
A(xi,...,xm) = Z ••• E aii...imXl1— *r&ii=0 im=0
of Lemma 2 and denote its height by
a= |Al.
By the binomial theorem,
Hence A has the majorant
A(xi ,...,
On differentiating this formula repeatedly, we find that
86 LECTURES ON DIOPHANTINE APPROXIMATIONS
Here
so that
In particular, it follows that
AMy A<<2ri+"'+rma(l+xi)ri... (l+xm)rm (&v = 1,2,..., n).
Now, by its definition as a determinant,
where the summation extends over all n! systems of suffixes Mi>JU2,...
that are permutations of 1,2, ...,n. Therefore, on replacing the factors
AJUJ/A by their major ants,
)ri ... (l+xm)rm}n.
Since
U+x)nr=Z
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
ROTH'S LEMMA 87
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
^ rm i iA(xi,...,xm)= Jj — E ai imxi1...xnm*0
ii=0 im=0
be a polynomial in xi ,...,xm with integral coefficients which is not identically
zero. Hence the derivatives
x ) 3il+-+3mA(x1 ..... xm)»-->xm' ~ * 4jil... Jm!9x3i1...3xmm
cannot all vanish at the point Xi = KI ,...,xm= /cm. Denote by
J(A) = J(A; pi,...9pm;Kiy...9Km)
the smallest value of
JL^..+JaLPi Pm
for all systems of suffixes ji ,..., jm for which
AJi— Jm^1'—'^ +°»
and put J(A)=« in the excluded case of the polynomial A = 0. The function
J(A) of A so defined is called the index of A at the point (/Ci,...,«m) relative
to pi,,">Pm-
This index may also be obtained as follows. By Taylor's formula,
88 LECTURES ON DIOPHANTINE APPROXIMATIONS
ri rm +_+-
= E - Z Ajl...jm(/c1,...,Km)xpl Pmxijl...xm3m,
ji=0 jm=0
where x is a further variable. Hence J(A), for A^O, is the exponent of the
lowest power of x in this development with a non-zero factor
A3i —Jm^1 »•••
From this, it follows at once that if B(xi,...,xm) is a second polynomial
of the same kind, then
(A): J(ATB) £ min{j(A), J(B)},
(B): J(AB) = J(A) + J(B),
where the indices are taken at (KI ,..., /cm) relative to pi ,...,pm< K is further
obvious that
either J(A) £ 0 or J(A) = «>,
and thai?
J(A) = 0 if and only if A(/d ,...,Km) * 0.
We need one further simple property of the index. Let li ,..., 1m be
arbitrary non-negative integers, and let
Evidently
B.
where
m . m .A m
*ji*=ji+U,...,Jm = im+lm and therefore Z 7^ = Z J| - Z ^-
h=lph h=lph h=lph
Since the index cannot be negative, we obtain then the inequality
(C): J(Ai ...i ) ^ max(0, J(A) - Z ^ )•
1 m h=l ph
From now on the index J(A) will nearly always be taken relative to
. . («!,..., «m) =H1 )...(?m) A.* .*(Ki,..0Km)Ji--0m \Ji/ \3m/ ji—Jm
