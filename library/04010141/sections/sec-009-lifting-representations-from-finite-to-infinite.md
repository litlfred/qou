---
doc_id: 04010141
doc_title: "Cellular algebras and diagram algebras in representation theory"
section_id: sec-009-lifting-representations-from-finite-to-infinite
section_title: "Lifting representations from finite to infinite dimensional algebras"
section_number: null
pages: 19-31
source_pdf: 04010141.pdf
source_sha256: b86b204b05453a5d
toc_source: inferred
doc_brief: "Cellular algebras and diagram algebras in representation theory — We discuss a circle of ideas for addressing problems in repre- sentation theory using the philosophy of cellular algebras, applied to"
---
algebras 
5.1. 
Commutative diagrams and lifting representations 
Let A and B be R-algebras and 'ljJ : A -+ B be an R-algebra homo-
morphism. If p: B-+ EndR(M) is a representation of B (where M is a 
free R-module) one may lift p to a representation 'lj;* p of A by composing 
with 'lj;. This is called the inflation of p via 'ljJ We shall discuss in this 
section the lifting of representations in the diagram 4.19. Note that by 
4.14(v), if R is an algebraically closed field of characteristic not dividing 
n, then every finite dimensional irreducible representation of 'fi{(q) is 
the lift via ¢a of an irreducible represetation of T~(q), for some a E Rx. 
It follows that the inflations to f&(q) of irreducible representations 
of T~(q) are precisely those irreducible representations of J&(q) which 
factor through 'fi{ (q). Our next result describes the lifting of cell mod-
ules from TLBn(q, Q) to T~(q). 
Theorem 5.1 ([18], Corollary (6.15)). 
Suppose R is any commu-
tative ring and suppose that q, Q are elements of Rx. Let f3 E Rx satisfy 
(32 = -qn-2 and let gf3 : T~(q) -+ TLBn(q, Q) be the surjection defined 
in 4.18. Fort E Z such that It I ::; n and t = n {mod 2), define f.t := 1!1 
fort=/= 0, and Et = 1 if t = 0. 
160 
J.J. Graham and G.I. Lehrer 
Then the inflation g~Wt(n) of the cell module Wt(n) ofTLBn(q, Q) 
is isomorphic to the cell module Wjtl,z;t (n) of T::_(q), where 
(5.2) 
( 1)t{3Q-1 -l(n+t-2) 
Zt=-
q2 
. 
It follows from 5.1 that the inflation g~Lt(n) of the irreducible quo-
tient Lt(n) (cf. 2.4(i)) of Wt(n) is the irreducible T::_(q)-module Lltl,z;t. 
This is because of the implied description of the irreducible quotients 
of cell modules in terms of homomorphisms between cell modules (see 
2.4(ii)). It therefore follows (see 3.7) that 
Corollary 5.3. 
Fix q E Rx and assume R is a field. Then ev-
ery irreducible T::_(q)-module is the inflation via g{j of an irreducible 
TLBn(q, Q)-module for some Q E Rx. 
To see this, one need only observe that given t, (3, q and z E Rx, the 
equation zt = z (see 5.2) has the solution Q = ( -1)t(3z-1q-!Cn+t-2). 
Our objective is to study the inflations of T::_(q)-modules to ~(q), 
and to apply our knowledge of decomposition numbers for T::_( q) (see 
3.11) to the representations of ~(q). For this purpose we focus on the 
part of the diagram 4.19 below. 
(5.4) 
~(q) 
1 
~Q,,. 
TLBn(q,Q) ~ 
TLBn(q,Q) 
where 1/Jo. =<Po. o 1"/3 and €Q,p. = 774 o 1"/Q,w 
By the commutativity of the diagram 5.4, we have 
(5.5) 
where z = Zt as above, and a, (3 and f..t are related by (32 = -qn-2 and 
t-ta- 1 = (3. We wish to interpret the inflations 1/J~Wt,z(n) of the cell 
modules of T::_(q) in terms of the "standard modules" of ~(q), and we 
therefore give a brief description of these. 
5.2. 
Standard modules for ~(q) 
We assume henceforth that the ground ring R is C, although many 
of our results apply more generally (see [18]). The standard modules for 
~(q) may be defined cohomologically ([5, 24, 43]) or as induced modules 
([41, 4, 44, 45]). The various definitions agree only up to equivalence in 
the Grothendieck group r(~(q)) of finite dimensional ~(q)-modules, 
Cellular algebras and diagram algebras 
161 
which suffices for our purpose, since we shall be discussing composition 
factors. Let G = GLn(C) and~= Lie(G). The standard modules are 
parametrised by the set P of equivalence classes of pairs ( s, N) modulo 
G, where s E G is semisimple, N E ~ is nilpotent and s.N = q2 N 
(where G acts on ~ through the adjoint representation). 
Let us explain a key property of this correspondence. The algebra 
~(q) has a subalgebra (4.6(iv)) U(n) = qxf=l, ... , x,:;=1J, which may 
be thought of as the group algebra C(zn), where zn = (X 1, ... , Xn). 
Any one-dimensional representation x of U ( n) therefore corresponds to 
a character of zn and hence to the sequence (x(X1 ), ... , x(Xn)). Let 
(s, N) E P, so that N corresponds to a partition A = (A1 ::::; A2 ::::; 
· · · ::::; A£), where I: Ai =nand s = diag(s1, ... , sn) where Si+l = q-2si 
whenever i, i + 1 lie in the same "block" of N. Thus the sequence of 
eigenvalues of s consists of£ subsequences of size AI, A2, ... , A£, which 
we call blocks, and each block is of the form a, aq-2 , aq-4 , . • . for some 
a E ex. If Ms,N is the corresponding standard module, its dimension is 
K = 
,x 11~\t! and there is a filtration 
(5.6) 
0 C M1 C M2 C · · · C MK = Ms,N 
where dimMi = i, each term Mi is a U(n)-submodule of Ms,N, and 
the characters of U ( n) on the K quotients Md Mi-l ( i = 1, 2, ... , K) 
are given by the K sequences (x1, ... , Xn) obtained by permuting the 
sequence (s1, ... , sn) while keeping each block in its original order. 
5.3. 
Lifting cell modules to standard modules 
To state our main result, it is convenient to note that that there is an 
involution L: H;:(q) ---+ H;:(q) which takes Ti to -Ti-l (i = 1, ... , n- 1) 
and x1 to Xj1 (j = 1, ... , n); this follows by noting that the images of 
the Ti and X 1 under L satisfy the the relations 4.6(iv). The surjection 
Oa: ~(q)---+ T;:(q) is defined by (cf. 5.4) 
(5.7) 
Theorem 5.8 ([18], (9.9)). 
Let H;:(q) be the affine Heeke algebra 
of GLn(C) and let f(~(q)) be the Grothendieck group of finite dimen-
sional ~(q)-modules. Let Wt,z(n) be a cell module for the diagram 
algebra T;:(q). Then, with ()a as in 5. 7, we have 
(5.9) 
where [V] denotes the class in r(~(q)) of an ~(q)-module v and 
Ms,N is the Kazhdan-Lusztig standard module of ~(q) corresponding 
162 
J.J. Graham and G.l. Lehrer 
to the pair (s, N) E P where N = Nk is the nilpotent Jordan matrix 
corresponding to the 2-step partition (n- k, k) and s is the diagonal 
t · d" 
( 
-2 
-(n+t-2) b b -2 
b -(n-t-2)) 
h 
th 
ma nx 1ag a, aq 
, ... , aq 
, , q 
, ... , q 
, w ere 
e 
parameters a, b and k are given by 
(5.10) 
n- t 
k=--
2 
a=( _ 1)n+lo:zq!(n+t-2) 
b =( _ 1)n+lo:z-1q!(n-t-2) 
Some remarks concerning the proof. 
We begin by noting (see [1, 
Theorem 3.2, p.798]) that Ms,N is equivalent in f(H~(q)) to an induced 
module, which has an easy characterisation [18, (9.3)] in terms of a gen-
erating vector. One then shows that when the pair (q, z) is generic (see 
[18, (8.1)] for a definition; it suffices that there be no non-trivial polyno-
mial F such that F(q,z) = 0) then O~Wt,z(n) is actually isomorphic to 
the induced module. Finally a number-theoretic specialisation argument 
is used to prove the result in general. 
The key to the proof is the treatment of the generic case. The 
heart of the proof in this case is the determination of the characters 
of the algebra U(n), i.e. the simultaneous eigenvalues of the elements 
Xi, on O~Wt,z(n), or equivalently, on '¢~Wt,z(n). For this, we use the 
identification '¢~Wt,z(n) ~ ~Q,J.LWt(n) as in (5.5), where the parameters 
are as stated there. Now to analyse the action of the Xi on ~Q,J.L Wt(n), 
we start by observing that X 1X 2 ... Xn = vn is in the centre of H::_(q) 
(4.2(v)), and acts on '¢~Wt,z(n) as a scalar (since r:;: acts on Wt,z(n) as 
a scalar), which may be easily computed. We now use the filtration 2.12 
of Wt(n) to obtain one for '¢~Wt,z(n) ~ ~Q,J.LWt(n), noting that by the 
above argument, xlx2 ... xi acts via a (known) scalar on the ith term of 
the filtration. By this means one finds a simultaneous eigenvector for the 
Xi, and using the fact that Xi = (X1X2 ... Xi)(X1X2 ... Xi-1)- 1 one 
knows the corresponding character of U(n). Proceeding by induction, 
one obtains a filtration of '¢~ Wt,z ( n) like that described in 5.6. 
Assuming genericity, the characters of U(n) arising in this filtration 
are all distinct, so that '¢~Wt,z(n) is semisimple as U(n)-module. This 
permits the determination of the action of the Tj on a certain summand, 
completing the proof for the generic case. The passage from the generic 
case to the general case involves a number-theoretic argument (cf. [3]). 
We refer the reader to [18, §§6,7,8 and 9] for all details. 
D 
We denote the pairs, N in the statement 5.8 above by s(a, b), Nk. 
Cellular algebras and diagram algebras 
163 
§6. 
On the decomposition numbers of standard modules 
It is clear from Theorem 5.8 and the remark preceding 5.1 that 
the standard modules of ~(q) which factor through representations of 
f[{(q) are precisely the Ms,N where N = Nk is a two-step nilpotent 
element of (!5 as above. Since the relations 5.10 may be inverted to 
give a, z and t in terms of s, k, these modules are all realised, up to 
Grothendieck equivalence, as inflations of cell modules of T;:(q). Hence 
the results of Theorems 3.11 and 3.14 may be applied to analyse their 
composition factors. 
After working through the details of the correspondence provided 
by Theorem 5.8 and the properties of the cell modules Wt,z ( n), the 
following precise statement results. 
Proposition 6.1 ([18], 9.12). 
Let P be the set equivalence classes 
of pairs (s, N) E P where N E (!5 is two-step nilpotent, i.e. N"' Nk for 
some k with 0 ~ 2k ~ n. Let fi be the set of triples (t, a, z) (t E Z, 0 ~ 
t ~ n, n-t E 2Z; a, z E C x) and let n be the set of equivalence classes of 
triples in n under the equivalence generated by the relations (t, a, z) "' 
(t,-a,-z), (n,a,z)"' (n,y- 1za,y) and(O,a,z)"' (O,a,z-1). Then 
(with the obvious abuse of notation} we have well defined ~(q)-modules 
Ms,N, ( s, N) E P and 0~ Wt,z( n), ( t, a, z) E n, and there is a bijection 
f: P-+ 0 such that if(s,N) E P corresponds to (t,a,z) E 0, [Ms,N] = 
[O~Wt,z(n)]. 
This correspondence permits us to define the irreducible ''top quo-
tients" Ls,N for (s, N) E P as the pullback of the corresponding top 
quotient of Wt,z(n), which is either zero or irreducible. Translating the 
statement 3. 7(i) into the language of pairs, we obtain 
Proposition 6.2. 
The module Ls(a,b),Nk is zero if and only if 
{6.3) 
q2 = -1, n is even, k = ~' a= a, b =-a, for some a E Cx. 
We therefore denote by Po the set of (equivalence classes of) pairs 
in P which do not satisfy the condition 6.3. By Theorem 3.7{i), Po 
parametrises the irreducible ~(q)-modules which factor through f[{(q). 
The partial order ~ on Aa(n)0+ induces one on P using the corre-
spondence 6.1. Specifically we have 
Proposition 6.4. 
Suppose that under the correspondence 6.1 above, 
the triples (h,a,zl), (t2,a,z2) correspond to the pairs (s(al.bl),NkJ, 
0 
(s(a2, b2), Nk2 ) respectively. Then (t1, z1) -< (t2, z2) if and only if there 
164 
J.J. Graham and G.l. Lehrer 
exists f > 0 and E = ±1 such that if we write 2ki = n- ti fori = 1, 2, 
then 
(6.5) 
k2 =kl- f ~ 0 
a1 b!l =qtt +•t2 
(a2,b2) =(al>bl) ifE= 1 
(b1,a1) ifE = -1 
Now Theorems 3.11 and 3.14 yield immediately 
Theorem 6.6. 
Let P and Po be the sets of semisimple-nilpotent 
pairs defined above, and let ::::5 be the partial order on P generated by 
the relation 6.5. Then in the Grothendieck group of finite-dimensional 
H!(;(q)-modules, 
(6.7) 
[Ms,N]= 
(s' ,N')E'Po 
(s,N):5(s',N') 
[Ls',N'] 
for any pair (s,N) E P, 
and for (s, N) E Po, 
(6.8) 
s' N' 
where ns,N = 0 or ±1. 
(s' ,N')E'P 
(s,N)~(s' ,N') 
We conclude this section by giving some applications to the structure 
of the standard modules which are easy consequences of Theorem 6.6 
Corollary 6.9. 
(i) The standard modules Ms,N ((s, N) E P) are 
multiplicity free. 
(ii) If q is not a root of unity, the standard modules have at most 2 
composition factors. 
(iii) In all cases, Ms,N has composition length bounded by [ ¥ ]. 
(iv) The maximum composition length of Ms,N is [¥], and therefore 
is unbounded as n--> oo. 
§7. 
Connection with representation varieties of quivers 
In this section we continue to consider the representations of .iif:_(q), 
where the underlying ring is C. In this case, we explain an interpreta-
tion of6.7,6.9 in terms of the intersection cohomology of certain varieties. 
Cellular algebras and diagram algebras 
165 
Specifically, we show how (6.9)(i) is equivalent to the rational smooth-
ness of certain varieties which we define below. This interpretation of 
decomposition numbers in terms of intersection cohomology is due to 
Chriss-Ginzburg [5], Kazhdan-Lusztig [24] and Lusztig [33, 34, 35], (see 
also [11]) and the exposition here owes much to A. Henderson, who 
has given an alternative direct geometric proof of our (6.9)(i) starting 
from the geometric point of view (see [19]). Write G = GLn(C) and 
0 =Lie( G). The multiplicities of the irreducible f&(q)-modules in the 
standard modules Ms,N are given in terms of the intersection cohomol-
ogy of certain complexes on the closures of the orbits of the group Zc ( s) 
acting on the variety 
(7.1) 
Ns,q = {N E 0nil IS· N = q2 N}. 
Specifically, for N E Ns,q, let ON be its orbit under Zc(s). Let :<:; be 
the partial order on the (finite) set of orbits of Zc(s) on Ns,q which is 
defined by orbit closure. Let J'f'k(JC(ON)) denote the kth cohomology 
sheaf of the perverse extension of the constant sheaf on 0 N to the closure 
ON. It is known (see below) that £k(JC(ON)) = 0 if k is odd. For 
N' E Ns,q such that ON':<:; ON, write J"t'}J,(IC(ON)) = 0 for the stalk 
at any point of 0 N' of this sheaf, and define 
(7.2) 
kN,N'(t) = Ldim £J~(IC(ON))tk 
j~O 
Now the modules Ms,N generally have a top quotient Ls,N, which is 
irreducible or zero, and the non-zero modules among the Ls,N form a 
complete set of irreducible f&(q)-modules (see [5, Chapter 8] or [43]). 
Theorem 7.3 (Ginzburg [5], 8.6.23) (see also [1] and [11]). 
We 
have the following multiplicity formula for the standard modules Ms,N. 
Assume Ls,N =/= 0. Then 
(7.4) 
(M,',N' 'L,,N] ~ { 
0 unless s' rvc s 
kN,N'(1) ifs = s' and ON':<:; ON 
0 ifs = s' and ON' 1:. ON 
Here rvc denotes conjugacy in G = GLn(C). 
Let V = en, on which both G = GLn(C) and 0 act via matrix 
multiplication. For any linear transformation A of V and element~ E C, 
write V(A, ~) for the ~-eigenspace of A in V. For any pair (s, N) as 
above, write V = V1 EB V2 EB · · · EB Vk for the s-eigenspace decomposition 
166 
J.J. Graham and G.l. Lehrer 
of V, where Vi = V(s, ~i) and the ~i are distinct. The relation (7.1) 
shows that 
(7.5) 
Multiplication by q2 partitions ex into orbits which are infinite if q2 is 
not a root of unity and have cardinality e if q2 has finite multiplicative 
order e (say). These orbits are linearly (resp. cyclically) ordered if the 
order of q2 is infinite (resp. finite). We may assume that the ~i are 
ordered so that each orbit occurs as a sequence of successive elements 
in (6, · · · , ~k) in the specified linear or cyclic order, and that the ~j in 
a given orbit occur as a "block", which we denote by si (i = 1,··· ,r), 
in the matrix s. Let kt, · · · , kr be the sizes of these blocks, so that 
k1 + · · · + kr = n. The nilpotent element N correspondingly decomposes 
into blocks: N = N 1 E9 · · · E9 Nr, where Ni is of size ki and Si · Ni = q2 Ni 
fori= 1, · · · , r. The following facts may be found in [4, 41, 1]. 
Proposition 7.6. 
(i) The standard module Ms,N is Grothendieck 
equivalent to the induced module 
(7.7) 
where Ms,,N, is the standard module of Jiff: (q), >. = (kt, · · · , kr) and 
<2fi=l Ms,,N, is the lift from ®Jif. (q) to "Jif. (q) of ®";=1 Ms,,N,. 
(ii} If Pi is a composition factor of Ms,,N, (i = 1, · · · , r ), then 
Ind!!.E_(q) ~p· is irreducible. 
H):(q) 
•=1 ' 
(iii} The standard module Ms,N is multiplicity free if and only if 
each component Ms,,N, is multiplicity free. 
Thus the decomposition of Ms,N may be discussed in terms of that of 
the Ms,,N,i in this way one reduces to the case where all the eigenvalues 
~j of s are in the same q2-orbit in C. This may also be seen from the 
geometric description of the decomposition numbers given above (see 
(7.3)) as follows. 
The centraliser Za(s) ~ Il~=l GLn, (C), where ni is the size of the 
block Si (or Ni)· It is clear that the orbit ON C Ns,q is isomorphic to 
the product rr~=l ON" where ON, := ZaLn,(q(si) 0 Ni. It follows from 
the Kunneth theorem for intersection cohomology, that in the above 
notation, 
(7.8) 
Cellular algebras and diagram algebras 
167 
where Nf is the i-block of N', regarded as an element of <!5i =Lie GLn, (C). 
Thus for the decomposition of Ms,N, it suffices to consider the case 
when all eigenvalues of s are in the same q2-orbit, and hence after mul-
tiplication by a scalar, one may assume that they are powers of q2. The 
relation (7.5) then shows that the pair (s, N) defines a representation 
of the cyclic or linear quiver, and this is a convenient context for an 
explicit discussion of the combinatorial geometric interpretation of our 
result (6.9)(i). 
We shall therefore formulate our result in the language of quiver 
representations. We start by recalling some elementary facts concerning 
quiver representations, most of which may be found in [40]. 
Fix an element e E Z~ 0 , and let Qe be the cyclic quiver of type 
Ae-l· For e = 0, this is interpreted as the linear quiver A00 • If we 
write I = Z/eZ, Qe has vertex set I and an arrow from i to i - 1 
for each i E J. A representation of Qe is a pair (V, E), where V = 
EElieiVi is an /-graded C.vector space, and E = EElieiEi E Ev, where 
Ev = EElierHomiEI(Vi, Vi-I) C End(V). The dimension vector of (V, E) 
is denoted d = (db ... , de), where di =dim Vi, and its total dimension is 
written n = I:~= I di. We have a notion of equivalence for representations 
of Qe, which is defined in the obvious way. For a fixed graded vector 
space V, the set of all representations (V, E) is identified with the affine 
space Ev in the obvious way, and the group Gv := niEI GL(Vi) acts 
on this space by conjugation. The representation E E Ev (and its Gv-
orbit) is said to be nilpotent if E is nilpotent as an endomorphism of V; 
the set of nilpotent representations of Qe on V is clearly (Zariski)-closed 
in Ev, and we denote this variety by .Nv. 
Suppose henceforth that q2 has multiplicative order e, where e = 0 if 
q is not a root of unity. Let (s, N) be a pair with N E .Ns,q, and suppose 
all eigenvalues of s are powers of q2, and hence are parametrised by 
I (we have seen that the general case may be reduced to this one). 
Then by (7.5), the s-eigenspace decomposition V = EElierVi of V =en 
defines, together with N, a nilpotent representation of the quiver Qe. 
Conversely, given such a representation, V = EElierVi, with a nilpotent 
endomorphism E : Vj --+ Vj_ 1 (j E J), define s E GL(V) as the linear 
transformation which acts on Vi as multiplication by q- 2i. Then E E 
.Ns,q· The following statement is now clear. 
Proposition 7.9. 
(i) There is a bijection between GLn(C)-
conjugacy classes of pairs ( s, N) such that the eigenvalues of s are powers 
of q and s · N = q2 N, and isomorphism classes of nilpotent representa-
tions (V, E) of the quiver Qe, with total dimension n. 
168 
J.J. Graham and G.l. Lehrer 
{ii) If (s, N) and (V, E) correspond under this bijection (recall that 
V comes with its grading), the variety ON above is isomorphic to the 
Gv-orbit of E in Nv. 
We next give a parametrisation of the Gv-orbits on Nv. By (7.9)(i), 
as the pair (V, E) varies, v being an [-grading of en and E E Nv, these 
orbits will index the standard modules of ~(q) in (7.9), and by (7.3) 
and (7.9)(ii), the geometry of any orbit determines the decomposition 
of the corresponding standard module. Take E E Nv. Since E is a 
nilpotent endomorphism of V, it corresponds to a partition ), = >.1 ~ 
>.2 ~ · · · ~ Ap(>.) > 0 of n (we refer to p(>.) as the number of parts 
of the partition ), and to n as its size). Of course in general ), does 
not determine the Gv-class of E. To describe the latter, we require the 
following description of the indecomposable nilpotent representations of 
Qe; an arbitrary nilpotent representation is uniquely (up to order of 
the summands) expessible a sum of nilpotent indecomposables. The 
nilpotent indecomposables are parametrised by pairs (i,€), i E I,€ E 
Z>oi denote the corresponding representation of Qe by M(i; €). Iff= 
ae + b, (a, b E Z?:o, 0 ~ b < e), the graded vector space V = EBjEJ Vj has 
(7.10) 
a+ 1 for j = i, i + 1, · · · , i + b- 1 
a otherwise. 
If Vj has basis { v1,1 , · · · , v1,d1 }, the homomorphisms E1 : VJ+l ---> Vj are 
described by 
(7.11) 
Vj,c if j =/:- i 
Vj,c+l if j = i 
where Vj,c is defined to be 0 if c > dj. 
The pair ( i; f) may be identified with the sequence ( i, i + 1, · · · , i + f- 1) 
of elements of I, and so is sometimes referred to as a segment. Note that 
the total dimension of M(i; €) is €. Any nilpotent representation M of Qe 
of total degree n is equivalent to a sum M ~ M ( i 1 ; f 1) EB · · · EB M ( ip; fp), 
where L_1 £1 = n. The multiset {(i1,£1) I j = 1, .. · ,p} is uniquely 
determined by the isomorphism class of M and conversely; hence the 
isomorphism classes are often referred to as "multisegments". If the 
segments are ordered so that the £1 are in weakly decreasing order, the 
sequences corresponding to the ( i1, £1) may be written in an array, which 
may be thought of as a Young diagram whose boxes are labelled with 
elements of I, which increase by one across the rows. The dimension 
vector of the representation M is d = (d0 , · · · , de_ I), where di is the 
Cellular algebras and diagram algebras 
169 
number of entries of the array which are equal to i. If the partition of 
n which corresponds to the Young diagram is >., we call the array an 
I- labelling of>., or simply an /-partition (of n). Clearly>. describes 
the GL(V)-orbit of the nilpotent transformation E. 
Remark 7.12. 
The distinct /-partitions of n parametrise the nilpo-
tent representations of Qe of total dimension n, with two /-partitions 
deemed to be the same if one is obtained from the other by permuting 
rows (necessarily of the same length). We denote an /-labelling of>. by 
a symbol(>., l), where l refers to the labelling. In view of (7.9)(i), corre-
sponding to each /-partition(>., l), we have a standard module for ~(q), 
which we denote by M(>.,z), which is uniquely defined up to isomorphism; 
similarly for the top quotient L(>.,l) mentioned above. Further, in view of 
(7.9)(ii), we also have associated to(>., l) a corresponding variety, which 
we denote O(>.,!)i the closure relation among these varieties defines a 
partial order among /-partitions, which we denote~. 
Lusztig (see [30, §5 and Appendix]) has given a necessary and suf-
ficient criterion for L(>.,l) to be non-zero. Say that (>., l) is aperiodic if 
for each m E Z>o there exists an element i E I such that (>., l) does not 
have a row of length m starting with i. Then L(>.,l) =f. 0 if and only if 
(>., l) is aperiodic. 
We may now express (7.3) in the language of /-partitions as follows. 
Note that the dimension vector d of an /-partition determines the "s" 
in the corresponding pair ( s, N). 
Corollary 7 .13. 
Let ( >., l) and ( >.', l') be two I -partitions with the 
same dimension vector such that ( >.', l') ~ ( >., l) in the sense above, and 
suppose that (>., l) is aperiodic. Define 
(7.14) 
-
~ . 
2k 
k 
K(>.,l),(>.',l')(t) = L...J dzm Yr(y,l')(IC(O(>.,l)))t . 
j~O 
Then 
(7.15) 
If(>., l) and (>.', l') do not have the same dimension vector, [M(>.,l) 
: 
L(>.',l')] =0. 
Our result (6.9) pertains to /-partitions with at most 2 parts (rows). 
Note that in this case, the criterion (6.3) given in our result (6.2) for 
L(>.,l) to be non-zero coincides with Lusztig's aperiodicity. Denote the set 
of /-partitions with dimension vector d by P(d), and the set of elements 
of P(d) with at most 2 parts by P~ 2 (d). The subsets corresponding 
170 
J.J. Graham and G.I. Lehrer 
to /-partitions (.X, l) with L(:> .. ,l) =/: 0 will be denoted respectively by 
'Po(d) and 'Pt2(d). Clearly if (J-t,m) E p9(d), ((.X,l)) E 'P(d) and 
(J-t,m) ~ (.X,l), then (.X,l) E p9(d). Our (6.9) may now be stated as 
follows 
Theorem 7.16. 
Let d be a fixed dimension vector and suppose 
that (.X,l), (.X',l') E p9(d), and (.x',l') ~ (.X,l). Then 
(7.17) 
k(> .. ,l),(>..',l')(t) = 1. 
For (.X, l) E Ptf2(d), (7.16) follows immediately from (6.9) and 
(7.17), because K(>..,I),(N,1')(1) = 1 implies that K(>..,l),(>..',l')(t) = 1, since 
K(>..,l),(>..',l')(t) E Z~o[t]. But if (.X, l) is not aperiodic, then as observed 
above .X= (m, m) for some m, and so (.X, l) is minimal in 'P~2 (d), whence 
(.X, l) = (A', l') and (7.17) holds trivially. 
This means that the variety O(>..,l) is rationally smooth (but not 
generally smooth) at the points of O(>..',l')· A. Henderson has given 
((19]) a geometric proof of Theorem (7.16) using an explicit resolution 
of 0(>..,1) 
Note that in the case e = 1 (i.e. q2 = 1), (.X, l) =.X (i.e. the label is 
irrelevant) and Lusztig has shown ((34]) that 
K>..,>..'(t) = tn(>..')-n(>..) K>..,>..'(t- 1 ), 
where n(.X) = Lj(j- 1).Xj, and K>..,>..'(t) is the Kostka-Foulkes poly-
nomial. In general, Lusztig (35, §11] has shown that for any (.X, l) E 
P(d), the variety O(>..,l) may be embedded as an open subvariety of 
an affine Schubert variety of type An-1 • 
It follows from this that 
Jek(JC(O(>..,l))) = 0 fork odd. Furthermore, there is is an order preserv-
ing injective map 'P(d) <......+ wa (notation as in §2 above) such that ifw, w' 
are the respective images of (.X, l), (.X', l'), then K(>..,l),(>..',l')(t) = Pw,w•(t), 
the usual Kazhdan-Lusztig polynomial associated with the coxeter sys-
tem of type An_1 . Thus our result also implies the triviality of certain 
special affine Kazhdan-Lusztig polynomials. 
We remark finally is that the results of (18] may be used to discuss 
aspects of the representation theory of the affine Heeke algebra m(q) 
over any algebraically closed field of positive characteristic, i.e. the 
"modular case". This is carried out for the algebras TLBn(q, Q) in (6]. 
Cellular algebras and diagram algebras
