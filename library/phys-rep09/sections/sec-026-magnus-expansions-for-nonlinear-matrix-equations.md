---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-026-magnus-expansions-for-nonlinear-matrix-equations
section_title: "Magnus expansions for nonlinear matrix equations"
section_number: null
pages: 30-32
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
It is possible to extend the procedure leading to the Magnus expansion for the linear equation (30), and obtain
approximate solutions for the nonlinear matrix equation

Y'=A(t,Y)Y, YO)=Y% 4%, (139)

where ¢ is a matrix Lie group, A : R, x % —~> g and g denotes the corresponding Lie algebra. Eq. (139) appears in
relevant physical fields such as rigid body mechanics, in the calculation of Lyapunov exponents (¢ = SO(n)) and other
problems arising in Hamiltonian dynamics (9 = Sp(n)). In fact, it can be shown that every differential equation evolving on
a matrix Lie group 9, can be written in the form (139) [59]. Moreover, the analysis of generic differential equations defined
in homogeneous spaces can be reduced to the Lie-group Eq. (139) [98].
S. Blanes et al. / Physics Reports 470 (2009) 151-238 181

In [99] a general procedure for devising Magnus expansions for the nonlinear equation (139) is introduced. It is based on
applying Picard’s iteration on the associated differential equation in the Lie algebra and retaining in each iteration the terms
necessary to increase the order, while maintaining the explicit character of the expansion. The resulting methods are thus
explicit by design and are expressed in terms of integrals.

As usual, the starting point in the formalism is to represent the solution of (139) in the form

Y(t) = exp(2(t, Yo))Yo. (140)
Then one obtains the differential equation satisfied by 2:
Q' = dexpg' (A(t, e7 Yo), 2(0) =0, (141)

where d exp! is given by (38). Now, as in the linear case, one can apply Picard’s iteration to Eq. (141), giving instead

C
alm) = | AeEXP ani AG: e2'™Oyy)ds
0

t 00
By (mm)
-/ Fp ttoime A 8 Sy)ds, m>0.
0 ko“

The next step in getting explicit approximations is to truncate appropriately the d exp~! operator in the above expansion.
Roughly speaking, when the whole series for dexp~' is considered, the power series expansion of the iterate function
Q(t), k > 1, only reproduces the expansion of the solution $2(t) up to a certain order, say m. In consequence, the
(infinite) power series of 2!I(t) and Q!**+"(t) differ in terms @(t™*'), The idea is then to discard in 2'*\(t) all terms of
order greater than m. This of course requires careful analysis of each term in the expansion. For instance, 2!°! = O implies
that (2!"l)’ = A(t, Yo) and therefore

t
Q(t) = | A(s, Yo)ds = Q(t, Yo) + O(t?).
0

Since
A(s, €2"' Yo) = ACO, Yo) + O(5)

it follows at once that
1 t
3 [ [2"(s), As, e?"" Yoy]ds = O°).
0

When this second term in 2!!(t) is included and 2"! is computed, it turns out that 2! reproduces correctly the expression
of 2'7! up to O(t?). Therefore we truncate d exp! at the k = 0 term and take

t
22l(e) -|/ Als, e2'"Yp)ds.
0

With greater generality, we let

t
att) -|/ A(s, Yo)ds (142)
0

m—2 t
By {m—1]
amo=y al, adiin-iigA(S 07” "Yo)ds, m > 2
k=0 ~

and take the approximation Q(t) ~ !™(t). This results in an explicit approximate solution that involves a linear
combination of multiple integrals of nested commutators, so that 2!"!(t) € g for all m > 1. It can also be proved that
2'"\(t), once inserted in (140), provides an explicit approximation Y!!(t) for the solution of (139) that is correct up to
terms 9(t"*+') [99]. In addition, 2!"!(t) reproduces exactly the sum of the first m terms in the 2 series of the usual Magnus
expansion for the linear equation Y’ = A(t)Y. It makes sense, then, to regard the scheme (142) as an explicit Magnus
expansion for the nonlinear equation (139).

This procedure can be easily adapted to construct an exponential representation of the solution for the differential system

Y’=[A(t,Y),Y],  Y(@) = Yo € Sym(n). (143)

Here Sym(n) stands for the set of n x n symmetric real matrices and the (sufficiently smooth) function A maps R; x Sym(n)
into so(n), the Lie algebra of n x n real skew-symmetric matrices. It is well known that the solution itself remains in Sym(n)
for allt > 0. Furthermore, the eigenvalues of Y(t) are independent of time, i.e., Y(t) has the same eigenvalues as Yo.
This remarkable qualitative feature of the system (143) is the reason why it is called an isospectral flow. Such flows have
182 S. Blanes et al. / Physics Reports 470 (2009) 151-238

several interesting applications in physics and applied mathematics, from molecular dynamics to micromagnetics to linear
algebra [100].

Since Y(t) and Y (0) share the same spectrum, there exists a matrix function Q(t) € SO(n) such that Y(t)Q(t) = Q(t)Y(0)
or, equivalently,

Y(t) = Q(t)¥Q"(t). (144)
Then, by inserting (144) into (143), it is clear that the time evolution of Q(t) is described by
Q' =Alt, WQ)Q, Q(0) =I, (145)

ie., an equation of type (139). Yet there is another possibility: if we seek the orthogonal matrix solution of (145) as
Q(t) = exp(2(t)) with 2 skew-symmetric,

Y(t) =e®@Ype"2,  t > 0, A(t) € son), (146)
then the corresponding equation for 2 reads
2! = dexpy' (A(t, e*Yoe™@)), 20) =O. (147)

In a similar way as for Eq. (141), we apply Picard’s iteration to (147) and truncate the dexp~! series at k = m — 2. Now we
can also consistently truncate the operator

AdgYp = e? Yoe? = e42 Yq

and the outcome still lies in so(n). By doing so, we replace the computation of one matrix exponential by several
commutators.
In the end, the scheme reads

t
amet) = il A(s, Yo)ds
0

m—1

1
Om-1() = P| Fadigim-niey Yo (148)
l=0 ~

m—2 t
By
alm) = ») al adi int, Om_1(s))ds, m>2
k=0 ~"

and, as before, one has 2(t) = 2!\(t) + (t'"*!). Thus
Ox(t) = Yo + [2"(t), Yo]

t
Q(t) = il A(s, @1(s))ds
0
@2(t) = Yo + [21(t), Yo] + sla, (21(t), Yol]

t t
aro= f ACs, exsyas— > [ [21(s), As, O2(s))Ids
0 0

and so on. Observe that this procedure preserves the isospectrality of the flow, since the approximation 2!"!(t) lies in so(n)
for allm > 1 and t > 0. It is also equally possible to develop a formalism based on rooted trees in this case, in a similar way
as for the standard Magnus expansion.

Example. The double bracket equation
Y’=[[Y,N],Y], | Y() = Yo € Sym(n) (149)

was introduced by Brockett [101] and Chu & Driessel [102] to solve certain standard problems in applied mathematics,
although similar equations also appear in the formulation of physical theories such as micromagnetics [103]. Here N is a
constant n x n symmetric matrix. It clearly constitutes an example of an isospectral flow with A(t, Y) = [Y, N]. When the
procedure (148) is applied to (149), one reproduces exactly the expansion obtained in [104] with the convergence domain
established in[105]. O
