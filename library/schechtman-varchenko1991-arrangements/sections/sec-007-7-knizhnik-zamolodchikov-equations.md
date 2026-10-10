---
doc_id: schechtman-varchenko1991-arrangements
doc_title: "Arrangements of hyperplanes and Lie algebra homology"
section_id: sec-007-7-knizhnik-zamolodchikov-equations
section_title: "Knizhnik-Zamolodchikov equations"
section_number: "7"
pages: 44-55
source_pdf: schechtman-varchenko1991-arrangements.pdf
source_sha256: 0100fd32438740f0
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "Arrangements of hyperplanes and Lie algebra homology — 10 sections: Front matter; Introduction; Orlik-Solomon algebra (Part I. Coh"
---
7 Knizhnik-Zamolodchikov equations
In this section we calculate the Gauss-Manin connection in the top cohomology
of complexes studied in the previous section.
7.1 Let us save the assumptions and notations from 6.1. Fix A =(k1, ..., kr)eINr;
put N=la|= Z k; fix n weights A41, .., Aneh*, n≥2. Fix an epimorphism
i=1
Bn+N in Cn+N with coordinates (z1, ..., Zn; ti, ..., tn). Define the collection of
exponents
a=a(A41, .., An; K): Bn+N-→C
where keC, k + O is a complex parameter, by the rule
(7.1.1) a(zi- zj=0)=(4i, 4j)/k;
a(t; -zj=O)= -(α(i), A)/k;
a(t;  t;= O) =(α(i), α(i)/k
(cf. (6.5.1).
Denote by ,=- La(Ai, ..., An; k) the corresponding line bundle with an
integrable connection over U(%n+n), cf. (4.5), and J, the local system of its
horizontal sections.
Let p: U(n+ N) -→ U(n) be the projection on the first n coordinates. Abusing
the language, we'll denote by z=(zi, ..., zn) a generic point of U(n). Thus,
P(e) = U(Bn: N(z) (cf. 5.1), We put L(2)= Lulp-1(2):
Denote by 2() the direct image P* of the relative de Rham complex
of La. It is a complex of vector bundles over U(n), whose fiber at z is 2'(a)z
 2' (,(z) (cf. 4.5). Cohomology bundles
i(2(L)= Ri p()
are supplied with the Gauss-Manin integrable connection Vm.
Denote by 2os(a(z) (the complex of Orlik-Solomon forms) the image of
(4.5.4); put Hos((z) = Im(H(2os(,(z) -→ H(2'(,(z). This defines a sub-
complex of bundles2os()→2(). Put Ros P()= Im(H(2os()
→H(2(L)
Arrangements of hyperplanes and Lie algebra homology 183
It is convenient to represent local sections of Qi(a) in the form p(t, z)
ta(t, z) dti, ^ ... ^dti, where
(7.1.2) ta(t, z)= II (zm- Zm)(4m, 4m m/K
,u<u
. II(t; - zm)(-α(i), 4m)/r
i, m
. II (t; - t;,)(a(i),a(i)/k;
i>i
p(t, z) is a holomorphic function.
Let Za=Zk, × ... × Zkr act on [N] as follows: the i'th factor Zk, acts on
π- 1 (i) by permutations, where we identify π- 1 (i) with [k;] using the order π- 1 (i)
induced from [N]. This induces the fiberwise action an of E, on 2'() by
the rule
o[p(t, z)t,dti, ^... ^dti,J=op(t, z)ta dti, ^... ^dt
where  is obtained from  by permutation of t' s. This action respects 2os.
Evidently, the Gauss-Manin connection is Za-equivariant.
7.2 Put M; = M(4); M = M1 @ ... @ Mn:
For a vector space Vdenote by 2(V)e V V* the tautological element. For
TeNr put 2:=2(n)ena@n; 2±:=2(n*)en*@na; 20 =(2(b)
act on
M(A)*@ M(4')* by means of b @ b*-action introduced in 6.17. Note that on
(M(A)*@ M(M')*)a only 2表 with 2'≤a act non-trivially. (We say that "
=(ki, ..., k)≤a=(ki, ..., kr) iff k;≤k; for all i). So we may form an infinite
sum
(7.2.1) ++'=
which acts on M(A)* @ M(4')*.
Let us denote by 2i; the operator on M*= M*@.. @ M* acting as 2 on
M*@ M* and as the identity on other factors. These operators respect the
weight decomposition. By the same letter we'll denote the adjoint operators
acting on M.
Let 2ij act on spaces APn* M* as the identity on APn* and as above
on M*.
7.2.2 Lemma. The above action is respects the differential in C.(n*, M*).
Proof. This follows from the invariance of 2.
Clearly, this action respects the weight decomposition.
Denote by M, Ma, C.(n*, M*), etc. trivial bundles over U(Bn) with fibers
M, M a, C.(n*, M*), etc. respectively.
184 V.V. Schechtman and A.N. Varchenko
7.2.3 Definition. The Knizhnik-Zamolodchikov connection Vkz on C.(n*, M*) is
defined by
Ozi jti ZiZj
From the invariance of 2 follows that Vkz is integrable, cf. [Ko].
Note that Vkz respects the differential in C., so it induces the integrable
connection on cohomology bundles, which will be denoted by the same letter.
Theorem 6.16.2 defines canonical isomorphisms of complexes of vector bun-
dles
(7.2.4) n.: C.(n*, M*)a ~→20s(L)Fa
Put *= o(n*, M*); *=Ho(C.(n*, M*)a). Here is the main result of this
Section.
7.2.5 Theorem. The subsheaf Ros P*(a) RN p×(a) is stable with respect to VGM.
The isomorphism
o(n.): -→ Rs P()a
maps the Knizhnik-Zamolodchikov connection to the Gauss-Manin connection
(It is natural to suggest that the same is true for all (n.).) Let us formulate
a more exact assertion.
7.2.5' Theorem. There exist canonical maps of vector bundles
ni: M→QN-1()F
i= 1, ..., n such that for every xe M*
on(x) n(2ij x) + dni(x)
Ozi jti
where d is the differential in 2'(L).
Clearly, 7.2.5 follows from 7.2.5'. 7.2.5' will be proven in n°s 7.3--7.10.
7.2.6 Corollary. There exists a constant A such that for |kl> A the inclusion
Ros P(La) c RN p() becomes an equality.
Proof. Fix z°e U(6n). By Theorem 4.6 there exists A such that
(*) (z) (2)t_d) H=(z) (z) 1_ d)SH
for z = zo and Ikl> A. Since Ros P× is stable with respect to Vcm it follows that
it is a vector bundle; hence the (*) holds for every ze U(n).
Let us denote by S, the local system of horizontal sections of La; put Fa(z)
= Sal p- 1 (z), ze U(6n). Homology groups H n(p- 1 (z), Ja(z)*) form a vector bundle
H over U(n) with an integrable connection. In fact,  is dual to RN p*(a).
Arrangements of hyperplanes and Lie algebra homology 185
For △(z)eH~(p-1 (z), (z)*) put
(7.2.7) Xs(z)= f neVa.
4(z)
7.2.8 Corollary. If △ =(△(z) is a local horizontal section of n, then a Va-valued
function Xs(z) satisfies the KZ differential equations
(7.2.8.1) 0 xz(z) Zij Xe(2)
Ozi j 1
i1, ..., n.
There exists A>O such that for all k, Ikl> A, functions Xa for all △ form
a complete space of solutions of 7.2.8.1.
Now let us consider the Kac-Moody algebra g=g(B)/ker S (cf. 6.3); put
M(A) = M(A)/ker S, M; -= M(4) these are g-modules (Verma modules); let M(A)*
be contragradient modules. The Killing form K induces the non-degenerate
pairing between root spaces g. and g-α (cf. [K, Theorem 2.2 (d)].
Let 2.eg. @ g-α be the corresponding element. Let us form a (possibly infi-
nite) sum
(7.2.9)
as in (7.2.1). Put M= Mi @... @ Mn; define operators 2ii on M and M* as
after 7.2.1. Put
(7.2.10) V, = O ker(e;: M-→M).
i=1
The projection Ma → M, induces the map V, -→ V,
Let xz(z) be the image of xa(z) (7.2.7) in Va.
7.2.11 Corollary. In conditions of (7.2.8) Xz(z) satisfies the system of differential
equations
(7.2.11.1) 4(z).
Ozi iti
Proof. Follows from 7.2.8 and an easy assertion from linear algebra:
7.2.11.2 Lemma. For a(ki, ..., kr), α= -- Z k;α; the action of 2t on M(M)@
i 1
M(A') coincides with the action of 2..
7.2.12 Remark. Just Eqs. (7.2.11.1) were discovered by Knizhnik and Zamolod-
chikov in [KZ].
7.3 Let us review the definition of n = no from (7.2.4).
186 V.V. Schechtman and A.N. Varchenko
Let (a; n) denote the set of all pairs (, s), where y: [NJ-→[r] is a map
such that # -i(i)=k; for all i; ε: [N]→[n] is any non-decreasing map. To
every (y, s)e(a; n) we associate an element
(7.3.1) f(, 8) =fi, @... @fine(M1 @... @ Mn)a
where Im=((a), (a+1), ..., (b)) if ε-1(m)=[a, b]:={ila≤i≤b), a≤b; fr,
= f(a)Jy(a+ 1)...Jyb) Ume Mmi fim= Um (the vaccum vector of Mm) if c-1(m)=- (0.
The set (f(, ), (, )eg(a; n) forms a base of M. Denote by {o(y, )
= dr, @ ... @ oin) the dual base of M*.
Denote by  -- Rn; n the subring of the field of rational functions C(z1 , ..., Zn;
ti, .., tn) generated by all fractions (t;-tj)-1, (t;-zj)-1, (zi-zj)-1. To every
(y, c)e(a; n) we assign β(y, )eR as follows.
Choose a bijection p: [N] -→[N] such that (a)=(b) implies πp(a) =πp(b).
So, p maps -1 (i) isomorphically onto π-1 (i). Put
b-1
(7.3.2) Pm= (Pm(t, z) = II (tp() -tp(i+1)-1)(tp(b) -zm)- 1
if - 1 (m)=[a, b], a≤b; if ε- 1 (m)= 0, put βm= 1.
Set
(7.3.3) p(, 8) = Z a(P1 ... Pn)
the sum being taken over all ceZa, where Za acts on  by permutations of
t;'s as described above.
By definition.
(7.3.4) n(8(y, 8) (2元i)N P(y,8)-ta-dti ^... ^dtn.
The map just constructed coincides with (6.5.2) for p=O, and “standard"
π defined as after (6.5.1). This follows from 6.8.1. The case of arbitrary π is
reduced to this one after renumbering of t;'s.
7.4 Now we begin the proof of 7.2.5'. First let us introduce a diagram notation
(similar to that of  6) for some elements of the ring R = n;n (see 7.3). Consider
an element x of  which is a product of pairwise distinct factors (t;-ti)-1,
(t; -zi)-1, or (z;- z)-1. We'll depict as a directed graph: it has n + N coloured
and numbered vertices: n white ones which are in 1 -- 1 correspondence with
the set zi, .., zn, and N black ones which are in 1--1 correspondence with
ti, ..., t. The arrows are in 1-1 correspondence with inverse differences
belonging to x: the i-th black vertex is connected with the j-th black vertex
o iff there is a factor (t; -- t;)-1 in x, the same with →O, O -→ O. Sometimes
we'll omit the isolated vertices which are not a boundary of any arrow. If we
do not want to indicate the colour of a vertice, we'll depict it as a cross x.
Arrangements of hyperplanes and Lie algebra homology 187
Example. 3 =(t1 t3)-1(z1 t3)-1(z1  z2)-1(z2 -t2)-1
=(t1 - z1)-1+(t1 z1) -1(z1 z2)-1
10
Abusing the language, sometimes we'll denote by the same picture an element
(t, z)eR and differential form (t, z) ta(t, z).dti ^ ... ^ dtn.
Here is the key relation in R:
7.4.1 Lemma.
It implies
×2
7.4.2 Circle lemma. =0
i=1
i+1
(In i-th picture the arrow connecting i-th and (i+ 1)-th vertices is omitted.)
×i+1
7.4.3 Lemma.
IM
i1 i+1 j+1
7.4.4 Lemma. xi+p
×i+1
OMjp≤M...MjiMi jp i+1 jp+1 jp- i+p-1 jp-1+1
j1 i+1 ji+1
Proof. Follows from 7.4.3.
7.5 Suppose that ^=(1, 1, ..., 1), so N=r, Z, ={e]; suppose that π: [N]-→[r]
is identity. In notation of 7.3, let us consider a form n =n(y, s) corresponding
to some (y, e)e@(a; n). The diagram corresponding to n has the following shape:
188 V.V. Schechtman and A.N. Varchenko
(7.5.1)
Let us call connected components of it branches (they are similar to islands
of s 5). The m-th branch has the form
y(a) ）(a+1) (b)
if -i (m)-[a, b]. Sometimes we'll draw it without marking internal black ver-
tices:
(a)
For an arrow x- × let us call its weight the number w(a)=(w(s), w(t)/k,
where w(O)= - αi, w(O)= A;. For i, je[n], i+j let us introduce differential form
Vjn as follows. Its diagram is the sum of all diagrams obtained from (7.5.1)
by adding one arrow connecting a point in i-th branch with a point in j-th
branch, multiplied by the weight of an arrow:
(7.5.2) Vin=Z
7.5.3 Example.
一α1, A2)
(41, 42)
So we get linear operators
(7.5.4) j: 20s(LA) -→20s(LA).
For n=.ta dti ^ ... AdtneQN()put
Jn=(-1)i-1tadti ^... ^dt;^... ^dt.
Oti
Here is the first key point.
Arrangements of hyperplanes and Lie algebra homology 189
7.5.5 Lemma.
Ozi (, 8)  Z Vijn(, 8) -d(Za/otp)  n(y, 8)
jti
where the sum in the second summand is taken over all p lying in the i-th branch.
i.e. pe{(a), (a+1), ..., (b)), 8-1 (i)=[a, b].
Proof. By differentiation.
7.5.6 Now suppose that  is arbitrary. Then forms n(>, s) are sums of forms
of the type (7.5.1).
Operators V; defined by (7.5.2) are a-equivariant, and one has the same
formula as in 7.5.5, with the evident modification of the exact form summand.
Theorem 7.2.5' will follow from
7.5.7 Lemma. For every xe M*
n(2ij)
Zi-Zj
The proof will occupy next n's.
We may, and shall suppose that n =- 2. Put V =- V12 .
7.6 First we'll calculate the action of Q=212. We'll use notation: fi..in
-fi, ...Jin ; [fi...in] - [fi, [fi, [... fin - 1, fin]...], the same with e's.
7.6.1 Lemma. Let f=-fi...in, e =eij..jaeUg, x =f.ve M(M). Then ex =0 if q> N;
and
ex fi..Jip...ip.
1≤p1<... <Pq≤N
.... [e, Ji,,], fip,], ] ..., fip.J fipa +1..
if q≤N.
Proof. We have ex=efu=[e, f]v. By the Leibniz rule [a, bc]=[a, b]c + b[a, c],
we have
[e, f]u=- Z fi,...fip-,[e, fi,ifip+ ..
p=1
This proves 7.6.1 for q= 1. For q> 1 use induction on q: [e, fi,J is the sum
of products of q -- 1 e;'s, and we may use the induction hypothesis.
7.6.2 Lemma. We have an identity in U g:
[... [ei...in], fi,], Ji,], ...], fin] = K(Eei...in], fi...jn]) hin.
Proof. K(lei..in], [fi..in])-K(e, fin) where e-[...[ei..in], Jj,], Ji],...],
Jin- J-Za;ei. Hence, K(e, fin)=ain. On the other hand the left hand'side of
7.6.2 is [e, Jin] =ajin hjn·
190 V.V. Schechtman and A.N. Varchenko
In notations of 7.2, put 2g= Z 2., the sum is taken over all roots α of
lαl =q
length q, i.e. equal to a sum of q simple roots. Here is the key
7.6.3 Lemma. We have an equality in M, @ M2 :
Za(fi...in V @y)
j.i...in Ui @Efi..j.J y(αi.. A
1≤ji<...<jq≤N j= jq +1
Vie Mi the generator, ye M2.
Proof. Fix a root α, lαl = q. Choose a base {el' in g. consisting of simple commu-
tators [eji...j.]. Let ( fi"] be the dual base in g-a. We have
Z. (fi...i Ui @y) =(Zeli @fii) (fi...in Vi @ y)
7.6.1
1≤j1<...<jq≤N i
(]-[nd m =? a ".. 
7.6.2
1≤j1<...<jq≤N i
C K(e), fJ)f" y.
But Z K(e(i), [fi])f(i)-[fi] if [fi]eg-α, and zero otherwise. The lemma fol-
lows.
7.7 Suppose that K is non-degenerate on g. For a positive root α = Zk; α; consid-
er two operators: 2.eg.@g-α acting M,  M2, and 2*=2te(g-a)*@g-a,
2'=(ki, ..., k)) acting on M* @ M* as in 7.2.
7.7.1 Lemma. 2* is adjoint to 2..
Proof. For feg-α, βeM*, xeMi, <f-β, x>=<p, -f.x>. On the other hand,
if S= S(·, f)eg*, <S.Φ, x>=-<β, --tf.x>. This follows from the commutativity
of
n* M*→M*
S@id
M* *W-
id@s
M; - M;
If ,-Zei" @f(i), then 2*-Zl'fi) where sl)- S(., te(i). The lemma fol-
lows.
Arrangements of hyperplanes and Lie algebra homology 191
7.8 Insertions. Given two  sequences of distinct symbols (ai, ..., ak);
(bi, ..., bn-k), and 1≤m≤k, we'll denote by I(ai, .., ak; bi, ..., bn-k; m) the
set of all insertions of the second sequence into the first one, i.e. the set of
all sequences (c1, ..., Cn) such that
(i) {c1, ..., Cnf ={ai, ..., ak] U{bi, ..., bn-k);
(i) Cp,=a; for some 1≤pi<p2<... <pk= N; Cq,=b, for some 1≤qi<q2< ...
<qn-k<N;
(ii) q-k+1=pm.
m--1+N-k)
We have # I(ai,..., ak; b, .., bn-k; m) m-- 2 Put I(ai, ..., ak;
bi, ..., bn-k)= U I(ai,..., ak; bi, ..., bn-k; m).
m= 1
Let us identify elements of En with sequences (ii, ..., in)e[NjN by the rule
oE Zn←→(o(1), :.:, o(N). For 1 ≤k ≤ N denote by Ti(N) Z the subset consisting
of sequences (ii, ..., in) such that ii <i2 < ... <ik-1 <i = N>ik+1 > ... >in. Put
(N1)
T(N)= U T(N). We have # T(N)= ; # T(N)=2N-1
k=1
We have the identity in U n:
(7.8.1) [fi...]= Z (- 1)N- k
k= 1 (i1, ...,in)e Tk(N)
Set Sk(N)= I(1, 2, ..., k; N, N - 1, ..., k+1)
7.8.2 Example. N=3. T : ((3 2 1)); T2: ((1 3 2), (2 3 1)); T: ((1 2 3)). Si :
((3 2 1); S2 : (1 3 2), (3 1 2)); S3 : {1 2 3).
7.8.3 Lemma. St(N)= Ti(N)- 1, i.e. ceSt(N)>α-1 e Ti(N).
Proof. Left to the reader.
Note that if (i, ..., in)eSk(N) then in -- k.
7.9 Let us return to the assumptions of 7.7. The base of (M  M2)a constitute
all monomials (fi..,  @fi ..i 2 . Let (oi...i, @ Ooi ...in) be the dual base.
of (M+ @ M*)2:
b=[n]
p+1
7.9.1 Lemma. Z  Z Zoji.jp+.@o
m= 1 k= 1 aeTk(q)
dij where the internal summation is taken over all
j=m
i, .., jp+q)el(i, ..., ip; ip+.-I(1), ..., ip+g-(q); m).
Proof. This follows from 7.6.3 and 7.7.1.
192 V.V. Schechtman and A.N. Varchenko
7.10 End of the proof of 7.5.7
 ()   s s  ()  sods s
i..., @ Oi ...i . Diagrams (7.5.2) included in it have the shape
(7.10.1)
Using the Circle Lemma 7.4.2, we may present (7.10.1) as a sum (with ±1
coefficients) of diagrams of 3 types:
(7.10.2)
(a) (b) (c)
n(x)
A diagram of type (b) is equal to
Z1Z2
1 n(2° x)
of all diagrams of type (b) (with their coefficients) is equal to
Let us consider a diagram of type (c) K Z1Z2
+k
(7.10.3)
Z1— Z2
shape -
(the summation in the r.h.s. of 7.9.1
K Z1—Z2
corresponds to the twofold application to 7.4.4 to (7.10.3). Analogously, the
sum of diagrams of type (7.10.2) (a) is equal to 1 n(2= x) . This proves 7.5.7
K Z1-Z2
when K is non-degenerate and a -(1, 1, :.., 1). The case of an arbitrary a follows
by symmetrization.
Both sides of 7.5.7 are polynomial functions on matrix elements of B=(bij),
and by (3.4.5) they are equal for a Zarisky dense subset of matrices B, hence
they are equal for all B. This completes the proof of 7.5.7 and of Theorem
7.2.5'.
Arrangements of hyperplanes and Lie algebra homology 193
7.11 Remark. One can express Theorem 7.2.5' in a more simple way. The map
n defines the map
n: M* →QN(U(6n+n).
The proof of Theorem 7.2.5' shows that the following assertion holds
Theorem 7.2.5" For all xe M*
dn(x)=二 E i(Zij x)
i<j ZiZj
