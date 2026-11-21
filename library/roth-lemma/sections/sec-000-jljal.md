---
doc_id: roth-lemma
doc_title: "ROTH'S LEMMA"
section_id: sec-000-jljal
section_title: "JL^..+JaL"
section_number: null
pages: 11-21
source_pdf: roth_lemma.pdf
source_sha256: c2f2b49f25f35919
toc_source: inferred
doc_brief: "ROTH'S LEMMA — 2 sections: Front matter; JL^..+JaL"
---
Pi 
Pm
for all systems of suffixes ji ,..., jm for which
AJi— Jm^1'—'^ +°»
and put J(A)=« in the excluded case of the polynomial A = 0. The function
J(A) of A so defined is called the index of A at the point (/Ci,...,«m) relative
to pi,,">Pm-
This index may also be obtained as follows. By Taylor's formula,
88 
LECTURES ON DIOPHANTINE APPROXIMATIONS
ri 
r m 
+ _ + -
= E - Z Ajl...jm(/c1,...,Km)xpl 
Pmxijl...xm3m,
ji=0 
jm=0
where x is a further variable. Hence J(A), for A^O, is the exponent of the
lowest power of x in this development with a non-zero factor
A3i —Jm^1 »•••
From this, it follows at once that if B(xi,...,xm) is a second polynomial
of the same kind, then
(A): 
J(ATB) £ min{j(A), J(B)},
(B): 
J(AB) = J(A) + J(B),
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
m . 
m .A 
m
*
ji*=ji+U,...,Jm = im+lm and therefore 
Z 7^ = Z J| - Z ^-
h=lph h=lph 
h=lph
Since the index cannot be negative, we obtain then the inequality
(C): 
J(Ai ...i ) ^ max(0, J(A) - Z ^ )•
1 
m 
h=l ph
From now on the index J(A) will nearly always be taken relative to
. 
. («!,..., «m) =H1 )...(?m) A.* .*(Ki,..0Km)
Ji--0m 
\Ji/ 
\3m/ 
ji—Jm
2. Put w(A) a e"J<A) if A ^0, andW(O) = 0. The properties of J(A) just stated show
that w(A) is a non-archimedean valuation on the ring of polynomials.
ROTH'S LEMMA 
89
9. The upper bound a m(a; Hi,..., Hm; riM.., rm)
If Hi,...,Hm are m positive integers, we denote by Q(Hi,...,Hm) the
set of all systems of m rational numbers
Pi 
_ Pm"
written in their simplified forms,
(Pi,Qi) = (P2,Qa) = ... = (Pm>Qm) = 1,
of heights
Hh=max(|Phl,lQhl) 
(h = 1,2,..., m).
If further a^l is a real number and ri ,..., rm are positive integers, we de-
note by R(a; n ,..., rm) the set of all polynomials
ri 
rm 
.
A(Xl,...,xm)= E -. E ^..^...x^O
ii=0 
im=0
with integral coefficients which are of height
lAl ^ a.
Roth's lemma deals with a number 9m defined as follows.
Definition: Let a^l, and let ri,...,rm, Hi,...,Hm be 2m positive integers.
The symbol
denotes the least upper bound of J(A; ri ,..., rm;Ki ,..., Km) extended over
all polynomials AeR(A; ri ,..., rm) and over all systems of m rational
numbers (Ki,...,Km)eQ(Hi,...,Hm)-
Several simple properties of '8m follow at once from this definition.
First, both sets R(a;ri,...,rm) and Q(Hi,...,Hm) are finite. Hence the least
upper bound in the definition of 8m is attained, and there exist a polynomial
AeR and a set of fractions Ui ,...,/cm)eQ such that
6m(a> ri...,rm; Hi,...,Hm) = J(A; ri^.^rmj^i j.-.^m)-
Secondly, the set R(a;ri,...,rm) does not lose elements when a increases;
hence 6m is a non-decreasing Junction of a. Third, as we are considering
now indices relative to ri ,...,rm> J(A) is equal to a sum
m .
E -J* where 0 ^ ji ^ n ,..., 0 < jm < rm,
h=lrh
and it follows at once that 0 < J(A) ^ m and hence that
0 * ® * m-
90 
LECTURES ON DIOPHANTINE APPROXIMATIONS
10. An upper bound for 
@i (a; r; H).
We begin with the study of <9i . Let
A(x)= £ aixi*0
i=0
be a polynomial in one variable, with integral coefficients such that
[A! = max(|aol,|ail,..., |arl) < a.
Let the rational number K = -^ be written in its simplest form, thus (P,Q)=1,
and assume that
Hence /c*0 and P*0, Q*0.
Suppose J(A; r; K)> 0. Then K is a zero of A(x), say of the exact order
j>0, and A(x) is divisible by (x-/e)J. By Gauss's lemma from §6, A(x) can
then be written as
A(x) = (Qx-P)te(x)
where B(x) is a certain polynomial with integral coefficients. Hence the
lowest and the highest non-zero coefficients of A(x) are divisible by PJ and
Q3, respectively. It follows that
H3 ^ lAl ^ a,
hence that
a result valid also when J(A; r; K) = 0. Therefore always
(0i): 
0l(a'r'H)^Tlift 
if H* 2'
11. The property 
r^.
The induction proof of Roth's lemma in the next sections becomes sim-
pler if the following notation is used.
Denote by t a constant such that
0< t*s 1.
If b^l is a real number, and SI,...,SM> KI,...,KM are Positive integers, the
ordered system of numbers
b, si,...^]^, KI,...,KM
is said to have the property TM V either, (i)
M = l,
ROTH'S LEMMA 
91
or, (ii), simultaneously M**2 and
Kh > Si logKi 
(h = 1,2,..., M);
isit
b ^ KiM
Therefore the following inequalities also hold,
M
h=l
By way of application, let m^2; let the ordered system of numbers
a, ri ,..., rm, Hi ,..., Hm
have the property Fm; let n be an integer such that
1 ^ n ^ rm + 1;
and let
b = 2 
i— 
mn!an; Pi,= nri, P2= nr2,...,pm-i =
Then the new ordered system of numbers
b, pi,.-«»Pm-l> Hi,...,Hm_i
has the property rm_i.
Proof: The first inequalities
phlog Hh ^pilogH! 
(h = l,2,...,m-l
are for m^3 immediate consequences of the assumption that
(h = l,2,...,m).
Next, by hypothesis,
w ^oY-(m-l)m(2nn-l)
Hi ^2 
,
whence, trivially, also
92 
LECTURES ON DIOPHANTINE APPROXIMATIONS
Finally,
n « r m + l ^ r i + l « 2ri, hence n! ^ nn ^ 2nri = 2P1,
and, by assumption,
T f
a«Hi m 
, ri + r 2+•••+r m
Therefore,
92n-mri pi n 
(2m+l)p1
D ^ z 
-^ «a ^ &
because
1 , 1 . 
1
12. A recursive inequality for &m. I.
Let again t be a constant such that
0<t^l.
We assume that m^2 and that the ordered system of numbers
a, ri,...,rm, Hi,...,Hm
has the property rm.
It was shown in §9 that there exist a polynomial
A(X! ,..., xm) eR(a; TI ,..., rm)
and a set of fractions
(KI ,.-, Km) e Q(Hi ,..., Hm)
such that
^m(a>ri>-«-»rm>Hi,...,Hm) = J(A;ri,...,rm; Ki,...,/cm).
Denote by n the integer with Kn<rm+l> and by U(xi,...,xm-l),
and W(xi ,...,xm) the three polynomials that correspond to A by Lemmas 2
and 3, and put again
b =2 
' ' n ! a11; Pl= nn,...,pm-i = nrm_i, pm = nrm.
As has just been proved, the ordered system of numbers
b,pi,...,pm_i, Hi,...,Hm-i
has then the property rm-i.
From the construction and from Lemma 3,
1X1 < a; 
ful < a, 
IvI ^ a, 
(wl ^ a,
where
ROTH'S LEMMA 
93
Therefore the upper bounds for the degrees of U, V, and W imply that
U(xi,...,xm-i)eR(b;pi,...,pm-l), V(xm)eR(b;pm),
W(xi,.,.,xm)eR(b;pi,...,pm).
Hence, in particular, with the same fractions KI ,..., Km-l> Km as above,
J(V;pm;«m) * Si to Pm;Hm).
From the identity
W(xi,...,xm) = U(xi,...,xm-i)V(xm)
and from the multiplicative property (B) of the index, it follows that
J(W;pi,...,pm; i»...> ffm) = J(U;pil...,pm-i;«il,..,jem-l) + J(V*;pm;«m),
or
where, for shortness,
$m = ®m-lft>;pi v*Pm-i;Hi,...,Hm-i) H- 81 (b;pm;Hm).
Instead, we may also write
because ph = nrh for all h, and so, by the definition of the index,
J(W;ri ,..., rm; KI ,..., fm) = n J(W;pi ,...,pm; «i ,-•> «m)-
Since from now on only indices of polynomials at the fixed point (KI ,...,/tm)
relative to the fixed integers ri ,..., rm will occur, we shall write for these
indices simply J(W), J(A), etc.
13. A recursive Inequality for ®m. II.
In the inequality
J(W) ^ n$m
just proved, we can give a lower bound for J(W) in terms of J(A).
For, as in §7,
A A - . - A 
A ,
where the systems of suffixes /*!,..., jnn run over all n! permutations of
1,2,. ..,n, while the operators Ay are of the form
and the j's are non-negative integers such that
3Ml+...+j]Lim-l « M-l, 
3,/m = v-1 
(lJ>,v = 1,2,. ..,n).
94 
LECTURES ON DIOPHANTINE APPROXIMATIONS
Therefore
A^A = Aj/Jll...]1Lim_1jj;m,
so that property (C) of the index implies the inequality
J(A^A) > max(o, J(A) - *£ -j
\ 
h=l h
But
and so
\ 
m"1 h=l
^ maxfO, J(A) - **" - ^-
Therefore, finally, by the properties (A) and (B) of the index,
max(o, J(A)-t-^ ) .
\ 
rm/
This inequality can be simplified. For shortness put
N = [{ J(A)-t}rm] + 1,
where [x] denotes as usual the integral part of x. Hence
N-l«{j(A)-t}rm<N.
We shall now distinguish the two cases n< N and n>N.
The case n^ N. Evidently
n-KN-1 <{j(A)-t}rm
and hence
Therefore
n
v=l
whence
(1): 
j(A)«t+ 
J(W) 
i f n « N .
ROTH'S LEMMA 
95
The case n>N. Assume, for the moment, that
J(A)s*t and thus N £ 1.
Then
and
maxu),
it follows that
J(W)
J(A)-t-
N
rm/
0 
if
j(A)-t-^i =N{J(A)-1
>-t}-f{j(A)-t} = £
& 
&
On solving this inequality for J(A), we find that
(2): 
J(A) < t +t/— J(W) < t + 2 t/- J(W) if n > N,
?r m 
fn
because
« ^ 
, 1 rm ^ rm . n ^ 1 n n
In the case J(A)<t so far excluded this estimate is still valid.
The two inequalities (1) and (2) show that in both cases n^ N and n>N
the same estimate
J(A) < t + 2 max(j J(W),yi
holds. Since J(W)^n*m, it follows that always
In this inequality, A was chosen such that
J(A) = J(A;ri,...,rm;Ki,.'vKm) = ®m(a-;ri,..
and $m had the value
®m= ®m-l(b;pi,...,Pm-i;Hi,...,Hm-i)+ ®i(b;pm;Hm).
We apply now the inequality ( @i) of §10 which shows that
By definition, pi = nri and pm = nrm, and also
r m log Hm ^ r i log HI , hence pm log Hm ^ pi log Hi.
It was further shown in §11 that 
,
^TIT P^
96 
LECTURES ON DIOPHANTINE APPROXIMATIONS
Therefore
because
The long proof of the last sections has thus lead to the following recur-
sive inequality.
Lemma 4: Let m^2, and let
be any ordered system of numbers tuith the property Tm. Then there
exists an ordered system of numbers
b; pi ,...,pm-l> Hi ,..., Hm-1
with the property rm-i such that
0m(a; ri ,..., rm; Hx ,..., Hm) « t
where
14. Proof of Roth's Lemma.
It is now easy to prove
Roth's Lemma: Put cm=2m -3. If the ordered system of numbers
has the property rm, then
Cmt
Proof: We procede by induction for m. First let m=l, hence Hi ^ 2
and a^HF1*. The estimate ( 0i) of §10 implies then that
as asserted. Secondly assume that m^2, and that the assertion has already
been proved for all ordered systems of numbers
b, Pi v>Pm-l» HI ,..., Hm_i
with the property rm-i; it suffices to prove that it then is true also for all
ordered systems of numbers
a,n,...,rm,Hi,...,Hm
with the property rm. By this induction hypothesis, the expression ^m in
Lemma 4 satisfies the inequality
-l(b;Pi,—,Pm-i;H1,...,Hm-i) +t < cm-it2"(m"2)
ROTH'S LEMMA 
97
and therefore Lemma 4 implies that
0m(a;ri,...,rm;H1,...,Hm) ^ t
Now 0 <t ^ 1 and cm_i ^ 1. The expression
t H- 2 max(cm-it3-(m-2)
+ 1, 
A
of this inequality is therefore certainly not larger than
-2>+ l2-(">-2> )
whence the assertion.
We conclude this chapter by stating Roth's Lemma in a slightly weaker,
but more convenient explicit form, as follows.
Theorem 1: Let 0<t^l. Let a^l be a real number, and let ri,...,rm,
Hi,...,Hm, where m^2, be positive integers such that
(h = 1,2,..., m-1),
(h = 2,3, ...,m),
Let
be rational numbers such that
OPh»Qh) = 1» max(|Ph|,|Qh|) = Hh 
(h = 1,2,...,m).
Finally let A(xi,...,xm) be a polynomial of the form
ri 
rm 
1 
.
A(xi,...,xm)= ^ ... £ a^...! xi1..^^
ii=0 
im=0
which is not identically zero and has integral coefficients such that
laij...iml ^ a for all ii,..., im-
Then there exist non-negative integers ji,...Jm satisfying
V Jh.^2m+lt2-(m-D
" 
T»i^
h=l rh
such that
A!...!,...,^) =1=0.
