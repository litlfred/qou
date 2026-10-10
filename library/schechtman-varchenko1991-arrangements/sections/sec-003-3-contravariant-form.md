---
doc_id: schechtman-varchenko1991-arrangements
doc_title: "Arrangements of hyperplanes and Lie algebra homology"
section_id: sec-003-3-contravariant-form
section_title: "Contravariant form"
section_number: "3"
pages: 13-19
source_pdf: schechtman-varchenko1991-arrangements.pdf
source_sha256: 0100fd32438740f0
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "Arrangements of hyperplanes and Lie algebra homology — 10 sections: Front matter; Introduction; Orlik-Solomon algebra (Part I. Coh"
---
3 Contravariant form
We save the assumptions of ss 1, 2
3.0 From now on up to the end of the paper we'll change slightly notations:
'(), g'() will be denoted by α'()z, g'()z, and α'(), g'() will denote
the complexifications α ()c =α ()z zC, g()c = g()z zC.
3.1 Let & be an arrangement. Suppose that a map a: & -→C is given. We'll
call such a map a collection of exponents for 6. For an edge L put
(3.1.1) a(L)=  a(H).
H- L,
3H
Put
(3.1.2) W=w(a)= Z a(H)Heα1().
Define differentials d = dp = dp(a): P() -→ p+ 1 () by the rule
(3.1.3) d(x) = w(a) x.
It is clear that d2  0
3.2 Define maps
(3.2.1) S= SP= SP(a): gP() -→αP()
as follows. For LeGi put
(3.2.2) S(L) = Z a(H)Heα();
H - L,
for a flag F =(L - LI  ...  LP)eF [P() put
(3.2.3) S(F) = S(L) . S(L2). ... - S(LP)
In other words.
(3.2.4) S(F) = Za(Hi)a(H2)... a(H) H ° ... · Hp
the sum is taken over all p-tuples (Hi, ..., H,) such that H;- Li, H;e%, 1 ≤i≤p.
One easily verifies that (3.2.4) correctly defines maps (3.2.1).
3.2.5 Lemma. s' defines the map of complexes S' S'(a): (g'(), d) -→(αl'(6),
d(a).
152 V.V. Schechtman and A.N. Varchenko
3.3 If we identify α() with '()* by means of isomorphisms (2.3.3) then
Sp may be regarded as bilinear forms on gp. Let us calculate their value on
a pair of flags (F, F').
Let us call a p-tuple H-(Hi, ..., Hp), H;e&, adjacent to a flag F if there
exists oe Z, such that F = F(H.(1), ..., Ho(p) (see (2.3.1). Note that such a permu-
tation is unique; denote it o☆(F).
Then for F, F'eF [P()
(3.3.1) SP(F, F')
the summing is taken over all H-(Hi, ..., Hp) which are adjacent to F and
F'.
3.3.2 Corollary. Forms S' are symmetric.
3.4 For a flag F =(L - Ll  ...  LP)e F [P() put
(3.4.1) a(F)= II a(L).
i=1
Suppose that a(L)+O for all edges L of codimension p. For a p-tuple
H =(Hi, ..., Hp), H;e%, in general position put
(3.4.2) RP(H)= Z (-1)lol a(F(αH)-1 F(αH)eP()
where H =(H.(1), ..., H.(p).
One easily verifies that this formula correctly defines the map
(3.4.3) RP= RP(a): P() →FP()
3.4.4 Lemma. Rp is inverse to Sp.
Proof. Since p and p are spaces of equal dimensions, it suffices to prove
that SpRP-id. Let Hi, ..., H, be in general position, L=Hi ...Hp. Note
that
(3.4.4.1) Z (-1)p-i H...H...H,). Z a(H)H=a(L) Hi... H,
i=1 HL
as follows from (1.2.3). Now let us prove that Sp Rp(Hi ... Hp) = Hi . .. H, by induc-
tion on p. We have
SP RP(H ... Hp)= Z (- 1)p Sp- 1 RP-1 (H....H,... Hp)
i=1 a(L)
(induction)
 a(H)H Z(-1)p H .. ....H,
H-L i=1 a(L)
(3.4.4.1)
a(H) H
H-L Hi... Hp.
Arrangements of hyperplanes and Lie algebra homology 153
3.4.5 Corollary. If a(L)+O for all edges L of codimension≤p then Sp(a) is iso.
(cf. Theorem 3.7).
3.5 Remark. Let us consider groups
gp() = gP()/ker SP(a)= SP(P(6) C&P(6).
Sp induces non-degenerate symmetric forms Sp on p; differentials d, d* on
A' induce differentials on g.= ④ p which are adjoint with respect to S. If
all a(H), He, are real then Sp are real and we have usual “Hodge" decomposi-
tion HP(g(%)={xEP()Id x =0 and d* x =0), etc. cf. 6.13, [Kos].
Determinant formula. All Sp(a) are linear operators between vector spaces of
equal dimension, depending polynomially on (a(H)He. So, det Sp(a) is a poly-
nomial in (a(H)) well defined up to a non-zero multiplicative constant. We'll
write down the formula for it.
3.6 Let  be a central arrangement in Cn with a unique vertex. Choose some
He&, and put
(3.6.1) (Hg)X=(9)a
where μ is as in 1.4 (cf. 1.7.4). From 4.1.5 follows that this number doesn't
depend on the choice of H.
Now let & be arbitrary. For an edge L of  put
(3.6.2) e(L) = e(%(L)
(We consider (L) as a central arrangement in the normal space to L in V).
') !         
Put
(3.6.3) dP(L)= dim P(CL)
3.7 Theorem. Let  be an arrangement in V=CN with exponents a:  -→. Then
for all p≥0
(3.7.1) (7)a-ip(7)(T) I I · Su0=(D)a- S 0p
(We put e(V) =- O; so det so - 1.)
Choose a framing of . This gives bases in lP(%), gp(), see 1.6, 2.9.2.
With respect to these bases, det sn-P(a) is equal to the r.h.s. of (3.7.1) with Const
= 1.
3.7.2 Example. Consider an arrangement  on the plane consisting of n lines
going through point, with exponents ai, ..., an. Then det $2
In- 2
-Const.a1 ... an ai
i=1
154 V.V. Schechtman and A.N. Varchenko
3.8 Corollary. Put
(3.8.1) det S(a)= II (det Sp(a)(- 1)N -P.
p=0
Then
(3.8.2) det S (a) = Const · II a(L)e(L) x(BL)
where the product is taken over all edges of &.
This formula should be compared with [V, Theorem 1.1]. The proof of
3.7 will occupy the rest of the section. It will consist of three steps.
3.9 Step I. S and Laplace operators
Let  be a central arrangement with a unique vertex v in V - CN.
Matrix elements of sn(a) are homogeneous degree N polynomials in a(H).
In this no we'll show that sn(a) may be decomposed into a product of N opera-
tors whose matrix elements are linear in a(H). (In fact, each framing of  induces
such a decomposition.) These last operators have remarkable form (Const -
Laplace operator).
Choose Hoe&
3.9.1 Lemma. The rectangle
SN
N-1 (
(2.5.2)
FN-1 (C; Ho) XN- 1 (; Ho)
(2.5.3) sn (%) (-1)-1
() N (%) n
commutes. Here the right vertical arrow is the restriction of (-1)N-1d:
αN - 1 (C) -→QIN() to &IN - 1 (; Ho)CαIN - 1 (C).
Proof. Follows immediately from (3.2.3).
Now consider the (non-central!) arrangement  -- H. in the (N -- 1)-dimen-
sional space. Let a, a* be differentials in αl'(C); Z- da* +d*a. In particular,
ZN-1=aN-2d*N-1.
3.9.2 Lemma. The diagram
dN- 1
QN -1 (C; Ho)
(1.4.2) (1.5.1)
a(V) -ZN- 1
commutes.
Arrangements of hyperplanes and Lie algebra homology 155
Proof. For Hi... Hn-1E&N-1(B; Ho) d(Hi ... Hn-1)= Z  a(H)H Hi...Hn-1
On the other hand, by (1.2.3)
N- 1
HHi...Hn-1=Ho Hi...Hn-1-Ho H Z (-1)i-1 Hi...H...Hn-1,
i=1
substituting this, we easily deduce the desired assertion.
3.10 Step II. Spectrum of Laplace operators
Let  be a central arrangement with exponents a in V=Cn with a unique
αl'(C), 4 = dd* +d* d. We'll identify & with @\{Ho}.
For every p put p= d*(p+1 (C)=ker(d*: P() -→αp-1()cαP().
For any edge L of  contained in Ho, define the subspace p(L)C&i p:
(3.10.1) αp(L)= (xe&i p]Supp xc L)
(see 1.8).
Suppose that L- H1 ...  HrHo, H,e&. Put
(3.10.2) αP(L)=(E - d*H1)(E -d* H2)...(E- d* H) p
where E denotes the identity operator.
3.10.3 Lemma. P(L) = P(L). In particular, αP(L) depend only on L.
Proof. Clearly, &P(L)&i P. By (1.8.2) P(L) &P(L). On the other hand, if
xEp, SuppxHHo, then Hx=O, whence (E-d*H)x=x, so p(L)
C&P(L). 
Clearly, if L' c L, then P(L)C P(L). Put
(3.10.4) GrP(L) =αP(L)/ Z αP(L)
T专,T
By 1.8.2 and (3.10.1) subspaces p(L) are stable under 4.
3.10.5 Lemma. Operator a(v) . E - 4 induces on grP(L) the multiplication by a(L).
Proof. 4lp= Z a(H) d*Hl p. If H- L then Hlp=O; if H→L then (E-d*H)
 p(L)& p(LH), so d*H acts as identity on rP(L), hence 4 acts as
Z a(H).
HL
Let Le&q+1, L Ho. Consider (L) as a central arrangement in the normal
space to L in V; let -@(L)H。 be the corresponding q-dimensional affine ar-
rangement (1.4). Put
(3.10.6) ()1 +b←(g)b :*p)=(T)
156 V.V. Schechtman and A.N. Varchenko
By 1.7.4
(3.10.7) e(L) = dim (L)
Let @, be the arrangement induced by @ on L.
Define maps (for i≥ 1)
(3.10.8) μui(L): (L)βαli(BL) →grq+i-1(L)
as follows. For xE(L)C&αq(@(L), y=(Hi O L)·(H2 L). ... (H; L)eα'(BL)
x ·d*(Hi .. H) lies in αq+i-1(L). By definition, μ'(L)(x @ y) is the image of this
element in gi9+i-1(L).
3.10.9 Lemma. Maps μu'(L) are epimorphic.
Proof. Put p=q+i-1. Consider z=H1...Hp+1E&p+1(C), z0, He&. Put zi
-Hi...Hi...Hp+1.
Set I =I(H)={ie[p+1]IHz;+O), J= J(H)=[p+1]\I(H). For every I'
[p+1] HnHo( H)H。 iff I'-I. If I={ii,..., i), i<iz<...<i;
iel'
J={ji, ..., js), ji <... <js, put zj=Hi,... Hjs; Zi=Hi,... Hi, (so z= ±z z). Put
d*(Hzi):=zi+ Z (-1)*HHi .. Hix.. H, (note that Hz-=O in &l(6)!). One can
k= 1
easily show that
(3.10.9.1) (E-d* H)d*z = ±d*(Hzi)d*(zj).
Analogously if we have t hyperplanes H(1), ..., H()e6 such that
I(H(1) I(H(2) ... C I(H(t), put Ki -I(H(i)\I(H(i-1), K1 = I(H(1). Then
(3.10.9.2) (E - d* H(t)(E- d* H(t - 1) ... (E - d* H(1) d* z
 ±d*(H(1) zk1) d*(H(2) zk2)...d*(H() zkt) d* z J(H().
The lemma follows from this and from Definition 3.10.2.
3.11 Step I11. End of the proof of Theorem 3.7 We'll prove (3.7.1) by induction
on N. Maps sp respect decompositions 1.3.2 and (2.1.2); hence we may, and
will, suppose that  is central with a unique vertex v, and p = O.
Choose Hoe%, and consider -BHo. By induction det sN-1() is equal
to
Const II II a(L)e(L)a(L)
1%3T 0!
So by 3.9.1 and 3.9.2 we have to show that
(3.11.1) det(a(u).E-ZN-1)~ II II a(L)e(L)di(L)
1%3T 01
LHo
Arrangements of hyperplanes and Lie algebra homology 157
Clearly, a(o).E-ZN-2 acts as multiplication by a(u)e(v) on the subgroup
AN - 1 - ker(d*: IN -1(G) → QN-2(C)CN -1(). So, it remains to show that
(3.11.2) det(a(v)· E- ZN -2)limd*~ II II a(L)e(L)d(L).
i≥1  Le%j
Lc Ho
By 3.10.5 and 3.10.9 the left hand side of (3.11.2) divides the right hand side.
On the other hand, because of independence of det sn on the choice of Ho.
and by induction on N, the r.h.s. divides the l.h.s., so they are proportional.
This completes the proof of Theorem 3.7.
3.12 Corollary. Maps μ'(L) (3.10.8) are isomorphisms.
