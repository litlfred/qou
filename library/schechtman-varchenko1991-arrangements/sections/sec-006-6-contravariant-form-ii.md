---
doc_id: schechtman-varchenko1991-arrangements
doc_title: "Arrangements of hyperplanes and Lie algebra homology"
section_id: sec-006-6-contravariant-form-ii
section_title: "Contravariant form, II"
section_number: "6"
pages: 32-44
source_pdf: schechtman-varchenko1991-arrangements.pdf
source_sha256: 0100fd32438740f0
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
---
6 Contravariant form, II
6.1 Fix a finite dimensional complex vector space h together with a non-degener-
ate symmetric bilinear form (,) on it. Denote by b: * -→h the isomorphism
induced by (,). By means of b we transfer the form (,) to h*; we'll denote
it also by (,)
Fix a finite set of linear independent covectors ({αi, .., αr} h*. We'll call
α; simple roots. Put h;-b(αi); bij=-(αi, αj)=<hi, αj>; B=(bijli,j=1 .
Arrangements of hyperplanes and Lie algebra homology 171
Denote by g=g(B) the Lie algebra with generators ei, fi, i=1, ..., r, and
heh; subject to the relations
[ei,J] - Oi, hi ;
(6.1.1) [h, e] =<h, αi>ei; ;[h, f]=-<h,αi>fi
[h, h']  0
for all i, j= 1, ..., r, h, h'eh.
We'll denote by n=n- (resp., by n+) the Lie subalgebra of g generated
by fi (resp., ei), i -- 1, ..., r. These subalgebras are free [K, Theorem 9.2(b)]. We'll
identify n with the Lie algebra studied in s 5. In particular, the decomposition
n= ① na is defined as in loc. cit. We have the natural decomposition g-
AeNr
n. @ h @ n+ . Put b = n④ h; it is a Lie subalgebra of g.
6.2 Bilinear forms
6.2.1 Lemma-definition. There is a unique bilinear form K(,) on g such that
(i) K coincides with (,) on h; K is zero on n- and n+; h and n_ n+ are
orthogonal;
(ii) K(fi, ej)- K(ej, f)=Oij, i, j=1, ..., r;
(ii) K is g-invariant, i.e.
K([x, y], z) = K(x, [y, z])
for all x, y, zeg.
This form is symmetric.
Proof. The same as in [K, $ 2.2].
Denote by t: g-→g the Lie algebra automorphism which is (-- 1) on h, and
maps fi to --ei, e; to -fi ("the Chevalley involution"). We have
(6.2.2) K(tx, ty)=K(x, y)
for all x, yeg.
Define the bilinear form S on g by the rule
(6.2.3) S(x, y) = K(t x, y).
From (6.2.2) follows that S is symmetric. We have
(6.2.4) S([x, yl, z) = S(x, [t y, z]).
This follows from the invariance of K and (6.2.2).
The subspaces n.-, h, n+ are pairwise orthogonal with respect to S. The
restriction of S to n is uniquely determined by the properties
(6.2.5) S(fi, J)= -Oij
(6.2.6) S (Lfi, x], y)= S(x, [ei, y])
The subspaces na C n, ae INr are pairwise orthogonal with respect to S.
172 V.V. Schechtman and A.N. Varchenko
bii
in [K, $ 1.2]; the isomorphism maps generators é;eg(A) to e;; Ji to fi, and
is identity on h. This isomorphism maps the form K to the form (.J-) defined
in [K, Ch. 2].
We have Ker K=Ker Scg. The quotient g(B)=g(B)/Ker S is the Kac-
Moody Lie algebra associated with A. Suppose that A is a generalized Cartan
matrix, that is, aijeZ, aij≤O for i+j. Then the Gabber-Kac theorem [K, Theo-
(ade;)nij(ej), nij= -aij+ 1, ij.
6.4 Verma modules. Let Aeh*. Denote by M(4) ("a Verma module") the g-
<h, A>v, heh. M(A) is isomorphic to Un as the n-module. We'll use the
notations of $5 for M(M)a. If a=(ki,..., kr) then M(4)a=^xeM(M)lhx=
h, A- Z k; αi).x for all heh.
i=1
The contragradient module M(A)* is by definition the dual space to M(M)
with the g-module structure defined by the rule <x, gβ>= < - t(g)x, β>, xe M(4)
Pe M(M)*, geg.
6.4.1 Lemma-definition. There is a unigue bilinear form S on M(A) such that
S(v, v)= 1; S(fix, y)= S(x, eiy);
S(e;x, y)= S(x, fiy) for all x, ye M(A); ie[r]. S is symmetric. Subspaces M(A),
are pairwise orthogonal with respect to S.
Proof is left to the reader.
The form S induces the map of g-modules S: M(A)-→ M(4)*. ker S is the
maximal proper submodule of M(A), [K, 9.2]. We put L(A):=M(4)/ker S. It
is the irreducible g-module with the highest weight A.
More generally,definethe symmetric form on spaces
APn M(A1)@ ... @ M(An), A;eh*, by the rule
(6.4.2) S(gi ^... ^g,@x1@... @xn, gi ^... ^g,@xi @... @xn)
= det(S(gi, g). II S(xi, x)
i=1
So we get the map of graded spaces
(6.4.3) S: C.(n, M(41)? ... @ M(4n) -→(C.(n, M(41)@ ... β M(4n)*.
Below we'll introduce the differential on the r.h.s. of (6.4.3) so that S will be
map of complexes.
We'll call the form S the contravariant or the Shapovalov form.
Arrangements of hyperplanes and Lie algebra homology 173
6.5 Fix a non-zero complex parameter k. For a=(ki, ..., k,)eINr, Ial= N, and
A1, ..., Aneh*, define the set of exponents a= a(B, A1, ..., An): Bn;N -→C:
(6.5.1) a(Hij)=(-αn(i), αn()/
a(Hm)=(-α(i), Am)/K.
i-1
Here π: [N]-→[r] is defined by the rule π()=iif Z k,<j≤ Z kp.
p= 1 p=1
Note that a is Za-invariant, i.e. a(oH)=a(H) for all He&n;N, oeZa. It follows
that S: g'(Cn; N) -→ l'(Bn; N) is Ea-equivariant.
Put for brevity M = M(A1)@ ... @ M(An).
Let us denote by
(6.5.2) n =N(a,p,n): C,(n, M) →&IN-P(Bn; N)Fa
the isomorphism, which is the composition of the inverse to the conjugate to
Y(a,p.n) (5.5.2), and β -1 (2.3.3).
Consider the square
C.(n, M)a C.(n, M)*
(6.5.3)
n:N
where the upper S is (6.4.5), and the lower S is (3.2.1)
The main result of this section is
6.6 Theorem. One has for all p
n,S=(-1)NNSp.
This Theorem will be proven below in several steps.
6.7 First, let us introduce certain diagram notation for elements of groups
p(n; n), similar to that of  5.
Namely, we'll draw a monomial Hi : ... · H,ep(&n;n) as the following non-
n crosses enumerated from 1 to n. It has p edges enumerated from 1 to p:
the i-th edge connects circles α and β if H;= Haβ, and the α-th circle with
the β-th cross if H,=He. So, if we forget the numbers of edges, we obtain
the picture of an edge H,  ...  H,eBn,n, cf. 5.6.
Example. N = 4; n = 2.
= H34H2H13
6.8 Suppose that a=(1, 1, ..., 1), N=-aj=-r, and n=1. The aim of this n° is
to prove 6.6 for this case and for p=0. Put 4= 41, M = M(4). The space M,
has as a base the set of monomials fo =fo(N) Jo(N - 1) ..fa(1) V, oe Zn.
174 V.V. Schechtman and A.N. Varchenko
Denote by S.e M the functional equal to 1 on fo(1)Jo(2)..fa(n)u and O on
other monomials. (NB! Pay attention to the inverse order!).
6.8.1 Lemma. n: M* -→αN(61;N) maps S. to
N-1
(-1)ial  (1) (2) (3) a(N-1) (N) X1
Proof. Since n is En-equivariant, it suffices to prove it for - 1. This case is
easily deduced from the definitions.
For any subset Ic[N], put a, ={ki, ..., kn}, where k; =- 1 if ieI, and O other-
wise. Set M,:=- Mar. For example, M(nj=- Ma.
Let 6,c61;n be the subarrangement, consisting of all hyperplanes Hi; and
Hl with i, jeI. Put F,=p(C), &r=&p(Ci), where p= # I. We have Fr
= gP(61;N); , =P(61;N). Define maps
(6.8.2) =:M→
by the following rule. Let I =- {ii, ..., ip), ii < ... <ip.
Let J =[N]\I; J= {ji, .., jn-p),ji<j2< ... <jn-p. Denote by o, the permu-
tation (ii,.., ip,, ji, j2, ...,jn-p)eEn. For put f。=fic(p)
fic(p- )*.. ...fio)*veM,. Set
(6.8.3) Y(f.)=(- 1)o +Iorl F(Hlc(1 Hi. Hi..
In other words,
(6.8.4) Y(f.)= Ya(Jin-p^fin-p-1 ^... ^fi, @fo)
(cf. 5.8.10). From 5.9 follows that Y are isomorphisms
Let
(6.8.5) n=nr: M*-→αI
be the composition M*-- *→&r. Denote by .EM* the -functional
equal to 1 on fig(nfic(2):. fic(n) v and to O on other monomials.
From 6.8.1 follows that
(6.8.6) n1 (60) =(— 1)lol +lol
1c(1) tg(2) ic(p-1) io(p)
Let je J. Put I' = I U ( j}. Define the operator
(6.8.7) Wj: Q+→Q1
by the formula
(6.8.8) W;(x)=x·[ a(Hi) Hij+a(H)) H)]
iel
Arrangements of hyperplanes and Lie algebra homology 175
Let us consider the square
M*
(6.8.9)
where e′ is the conjugate to the multiplication by ej.
6.8.10 Lemma. If j =jg then
ni. e =(- 1)g+ 1 k; n1.
Proof. This follows easily from the relation in A.:
6.8.11 Lemma.
p+1
q+1 q+2 p+1
=  (-1)p-q
q=0 12 iq+1 ip
Proof of 6.8.11 Induction by p, using the Orlik-Solomon relation
=0
.= o or ×). 
Now let us consider the Shapovalov form S: Ma-→ M*. For eZn S(f.)
is the image of the canonical generator of M under the composition
e(1) e(2) M* (N) M*.
(c(1)) (o(1), a(2))
From this remark and from 6.8.10 follows 6.6 for a =(1, 1, ..., 1) and p = 0.
6.8.12 Remark. In assumptions of 6.8.11 identify spaces 41, r. with the corre-
sponding spaces of differential forms. Define operators resHi, (resp., reshj): lr
-→r as follows. For a form w =w(ti)ier take its residue along the hyperplane
t, = t; (resp., t;= zi) and then put tj t (resp., tj= zi).
reSHij
corresponds (up to a sign) to f* (cf. 6.8.10). iel
6.9 Proof of 6.6 for a=(1, 1, ..., 1), n=0 and p=1. Well reduce to the case
n = 1, p = O, using the following trick.
176 V.V. Schechtman and A.N. Varchenko
We have the isomorphism of graded algebras
(6.9.1) α ( 0;N)~→α ( 1; N - 1)
which maps Hi; to H;- 1, j-1 if i, j>1, and Hi; to Hi-1 . It induces the isomorph-
ism of flag groups. On the other hand, consider the algebra g = g(B) correspond-
ing to the (r-1)×(r-1) matrix B=(bij):=bi+1, j+1)j=1. Let M = M(M) be the
  (...)   m sa   n
commutative square of isomorphisms r- 1 times
N:09)
(6.9.2) (6.9.1)*
N- (C1; N)
.. Ji -·D.
One easily verifies' by induction on N that the isomorphism × maps the
form S on na to (-1) times the form S on Mz. The isomorphism (6.9.1) is
compatible with the form S. Hence, the case n=O, p= 1 follows from the case
n = 1, p = 0 proven in 6.8.
6.10 Proof of 6.6 for  =(1, ..., 1), n= 1 and arbitrary p. For a subset Ic[N]
put n,=nar where ar is defined as in 6.8. We have the natural S-orthogonal
decomposition
(APnβM)a=④(nj, @... βnj,@M)
J...J,  I.
Analogously, we have the S-orthogonal decomposition
(see 5.6.3). By definition,  respects these decompositions, and 6.6 follows from
the particular cases proven in 6.8, 6.9.
The case of a=(1, ..., 1), arbitrary p and arbitrary n is proven similarly
and we leave it to the reader.
Thus, we have proven 6.6 for a =(1, ..., 1).
6.11 Proof of 6.6 for an arbitrary 2. Let A=(k1, ..., k,), N=12]. Fix some map
π: [N]→ [r] with # π-1 (i)- k, for all j. Introduce the new N × N matrix B-(b,j),
where b=ba(i) n(). Let g=g(B) be the corresponding Lie algebra with generators
éi,Ji, heh.
Let Meh* be a weight. Choose a weight Meb* such that <hi, M>=<ha();
A> for all ie[N]. Put M -- M(M); M = M(M). Put T-(1, 1, ..., 1). For any subset
Ntimes
I c[NJ define Mr as in 6.8. Set a(I)=(ki, ..., k’) where k';= # (I π-1 (i)
Arrangements of hyperplanes and Lie algebra homology 177
Define maps
(6.11.1) nr: M,→Ma()
be the formula r(Ji. ..Jip)-fu(in)...Jr(ip). On the other hand, define averaging
maps
(6.11.2) Sr: Ma() →M
by the formula
(6.11.3) Sr(Ji, ...Jip) = pr(s(fi) s(fi2) ... s(fip)
where s(i)= Z Ji ; pr: M-→M, is the projection to the homogeneous compo-
ieπ-1(j)
nent (cf. 5.11.2).
In other words.
(6.11.4) Si(i....Ji)-EJi...J
the sum being taken over all p-tuples of pairwise distinct integers (i, ..., ip)
such that π(in) =jk for all k.
Maps S, induce isomorphisms
(6.11.5) Ma(I)-→ Ma(m)
where Z a) acts on M, in the evident way (cf. 5.11).
6.11.6 Lemma (" The projection formula"). Let I [N], ie I; put I' -- I -- {i).
The sguare
Ma(1)
er(i)
SI
Ma(1)
commutes.
Proof. Direct verification.
6.11.7 Lemma. Squares
Ma
SM SM
M*
commute.
Proof. Follows from the previous lemma by induction of N (cf. the end of
6.8).
178 V.V. Schechtman and A.N. Varchenko
This Lemma proves 6.6 for p=O, n=1 and any a. The case of general p, n
follows from the commutativity of squares
C.(n, M)a s→C.(n, M)
(6.11.8)
C.(n, M)* →C.(n, M)
which in turn follows from 6.11.7 (cf. 6.9 and 6.10).
The proof of 6.6 is complete.
6.12 Remark. In view of 6.6, the determinant formula 3.7 applied to arrange-
ments n;N appears to be a variant of the Shapovalov determinant formula
[Sh].
6.13 In conditions of 6.6, put g=g/ker S; it is the Kac-Moody Lie algebra
associated with the matrix A defined in 6.3. Put n=n/ker Scg; L(A;)
= M(4)/ker S - these are irreducible g-modules; L- Li @...  Ln. As in $3,
denote by  the image S()&:.
Corollary. The maps : induce isomorphisms of complexes
C.(n, L)a-→ FN-(Cn;n)2a
for any Ae Nr.
In the rest of this section we'll introduce a structure of a Lie bialgebra
on b[DJ and a structure of a b-comodule on M = M(4i)@ ... @ M(4n). Com-
plexes N -'(6n;n) are identified with homogeneous parts of the standard com-
plex C.(n*, M*).
6.14 Cobracket. 6.14.1 Lemma-definition. There exists a unique map v: b -→ b ^ b
such that
(i) v(h) =O; v(f)-fi^h; for all heh; i= 1, ..., r;
(ii) v([x, y])=xv(y)-yv(x) for all x, yeb, where the action of b on b^b is
the adjoint one: a(b^c)=[a, b] ^c+a^[b, c] (i.e. v is a 1-cocycle of b with
values in b ^ b).
Proof. Left to the reader (cf. [D, Example 3.2]).
Let us define the map μ: Nr -→h by the formula μ(ki, ..., k,)= Z k; hi.
i=1
Note that v([h, x])=h.v(x) for heh, xeb. Hence the cobracket v preserves
the weight decomposition (with respect to the h-action).
6.14.2 Lemma. For every xEna
(i) v(x)= -μ(a) ^x+v(x)_ where v(x)- En^ncb^b.
(ii) For every i
v(Efi, x])-  fi.v(x)-- -(hi, μ(2)fi^x= fi.v(x)- +fi^ [hi, x].
Arrangements of hyperplanes and Lie algebra homology 179
Proof. For x = fi (i) is 6.14.1 (i). Suppose that we know (i) for x. We have v(Lfi,
x])= fi.v(x)- x.(fi ^ hi)=[fi, x] ^(μ(2)+hi) -(hi, μ(2)fi ^x+ fi.v(x)- .
This implies (i) for Lfi, x] and (ii). 
6.14.3 Lemma. For every xEn
[ S(x, [a, b]) if aen, beh
S(v(x), a^b) :
(S(x, [a, b]) if a, ben.
S is defined on b ^ b by the rule
(S(a, c) S(a, d)
S(a ^ b, c ^ d)=det (cf. (6.4.2)
(S(b, c)S(b, d)
Proof. The first equality is the direct consequence of 6.14.2(i). Let us prove
the second one. For x =fi the both sides are zero. Note that the form S on
b ^ b has the property
(6.14.4) S(x· y, z) = S(y, -t(x)·z)
if t(x)·zeb. Suppose that we know 6.14.3 for xena. We have
S(v([fi, xJ), a^ b) = S(fi. v(x) - x· v(f), a ^b)
= S(v(x), e;(a ^b) - S( fi^[x, hil, a^b) if a, ben.
Put 2 =(0, ..., O, 1, O, ..., O), so μ(20) = hi.
1st case. aena?, bena. If a= a? then both sides of 6.14.3 for fi, x are zero.
If ^+ a?, we have
S(v([fi, x]), a ^b) = S(v(x), [ei, a] ^ b +a ^[ei, b]) -(hi, μ(2) S(fi, a) S(x, b)
= S(x, [[ei, a], b])+S(x, [a, [ei, b]])+ S(x, [ei, [a, b]])
= S(x, [ei, [a, b]])= S(Lfi, x], [a, b]).
2nd case. aena", bena", 2', a" +a?. Then
S(v([fi, xJ), a ^ b)= S(v(x), e;·(a ^b)
= S(x, [ei, [a, b]])
= S(Lfi, x], [a, b])
So, the second equality 6.14.3 is proven for [fi, x].
6.15 Comultiplication. Suppose that n weights A1, .., Aneh* are given. Put M;
= M(Mi) with the generator vi; M=- Mi @...@ Mn, U=vi @... @un, 4= Z Ai.
i= 1
Let b act on b@ M by the rule a.(bm) = [a, b] @m+a@ b.m.
For 1≤i≤n, c, beg, m=xi @...βxneM, put bli)m=xi ... @xi-1βbx;
@ xi+ 1 @ ... β xn; b(i)(c?m) =[b, c] @m+c@ bli) m.
6.15.1 Lemma-definition. There exists a unique C-linear map Vm: M -→b @ M
such that
180 V.V. Schechtman and A.N. Varchenko
(i) Vm(h.x)= h.Vm(x) for any heh, xeM;
(ii) Vm(x)=(b(A)-μ(a)@x+Vm(x), Vm(x)en M, for any xeM, where b:
h* -~→ h is defined in 6.1 ;
(ii) Vm(f() x)=f().Vm(x)- -fiβ h}) x for 1≤i≤r, 1 ≤j≤n.
Proof. Left to the reader.
6.15.2 Lemma. For any x, ye M, aeb
(S(x, ay) if aeh,
S(vm(x), a@y):
(S(x, ay) if aen.
Here S is defined on b  M by the rule S(a @ x, b @ y)= S(a, b) S(x, y) (cf. (6.4.2)
Proof. The first equality follows from 6.15.1(i). Suppose that aen, xeMa,
@... Man, and we have proven 6.15.2 for a, x and any y. Let us prove it
for f) x. We have
S(vm(f() . x), a@ y)= S(vm(f() . x)- , a@ y)
= S(f() . Vm(x)- , aβy) -(hi, b(4) -μ(a) S(fi@x, a@y)
1st case. aena?. We may suppose that a = fi. We have
S(f() vm(x)-, fi@ y)= S(vm(x)- , eg) .(fi@y)
= S(vm(x)- , fi@el y)= S(x, Jie" y)
= S(x, [-hg) +e f(i y).
We may have two non-trivial possibilities
1st subcase. ye Ma, @ ... @ Man. Then
S(fi) vm(x)-, fi@y) = -(hi, b(A) -μ(aj) S(x, y)
+ S(x, el fi y),
S(fi x, a@y)= - S(x, y).
Hence,
S(vm(f() x), fi@y) = S(x, e( fi y) = S(f() x, fi y).
2nd subcase. yeMa: @... @ Mar where ',= a,+ a?; 2- 2k- a? for some k+j,
and a, = a, for all p丰k, j. Then S(fi x, fi@y) = O,
S(x, fie y) = S(x, f(k) e y) = S(x, ed" f(k) y)
= S(f() x, f(k) y) = S(f() x, fi y),
hence S(vm(f}) x), fi@ y) = S(f() x, fi y).
2nd case. aena', ' + a?. This case is treated similarly, and we leave to the reader.
Lemma is proven.
Arrangements of hyperplanes and Lie algebra homology 181
6.15.3 Remark. Let us give a pair of more explicit formulas for vm. First, for
any xeM
(6.15.3.1) Vm(x)-=- Z fi@ei x+Vm(x)--,
i=1
where Vm(x)-- - En- - @ M, n-- =
[>1
For a N-tuple of pairwise distinct integers (i(1), ..., i(N), 1≤i(i)≤r; and
(a(1), ... , a(N)E[n]N
(6.15.3.2) Ji(N- 1)
p=1 1≤j1<...<jp≤N
. [frag", fa]... ? ein flas..Jiag Jip)
Both formulas are proved by induction on Iaj.
6.16 From 3.4.5 follows that for general matrices B (i.e. for matrices B belonging
to a Zarisky dense subset of the set of all r × r-matrices) the map S: b -→b*
is an isomorphism. Analogously, for general B and A1, .., An S: M -→ M* are
isomorphisms. In this case properties 6.14.3 (resp., 6.15.2) uniquely determine
v: b -+b ^ b (resp., Vm: b -→b@ M).
It follows easily that for general B, A;v is a Lie cobracket (i.e. satisfies the
dual of the Jacobi identity), hence b is a Lie bialgebra, and M is a b-comodule.
Hence, the same is true for any B, A;. So, we get
6.16.1 Proposition. The map v: b -→ b ^ b 6.14.1 defines a structure of a Lie bialge-
bra on b. The map ym: M -→ b @ M defines a structure of a b-comodule on M.
Alternatively, one can say that v, Vm define the structures of a Lie algebra
on b* and of a b*-module on M*.
Consider n* as a subspace of b* by means of the projection b -→n. n* is
a Lie subalgebra of b*.
Warning. n with its bracket and a cobracket induced by the above bracket
is not a Lie bialgebra!
Consider the standard complex C.(n*, M*)= C.(n, M)*. From 6.6 follows
6.16.2 Theorem. The map n. induces isomorphisms of complexes
C.(n*, M*)a -~
for all 2.
6.17 Let D(b) be the double of b. Recall [D, n° 13] that this is a Lie algebra
equal to b@b* as a space, with the bracket on b and b* defined by the Lie
algebra structure on b and b*, and for beb, teb* [t, b]=+b, Teb*, beb
are defined by the rules T(c)= t([b, c]), ceb; t'(b)=[t', t] (b), t'eb*.
182 V.V. Schechtman and A.N. Varchenko
Consider the space M* as in 6.16 and define the action of bb* on it.
Namely, for beb, teM*, put bt(x)=t(-bx); the action of b* is defined as in
6.16.
6.17.1 Proposition. The above rule defines on M* the structure of a D(b)-module
Proof. We have to verify that [t, b] t=tbt-btt for all teb*, beb, teM*
As in 6.16 we have to prove this for general B, Ai. Suppose that t(.)= S(:
c), ceb, t()=S(·, n), neM. Then [t, b]=7+b where b=[tc, b] if [tc, b]eb
and O otherwise, t()=S(·, [c, tb]) if [c, tb]eb and O otherwise. Hence, [b,
tJ t()= S(, [tb, c n). On the other hand, (bt - t b) t()= S(, (tbc - ctb) n)= S(.
,[tb, c] n).
