---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-018-64-the-quantum-group-cqsl2
section_title: "The quantum group Cq[SL2]"
section_number: 6.4
pages: 37-40
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
[16] with q ∈C×and generators a,b,c,d obeying the relations
ba=qab, ca =qac, db =qbd, dc =qcd, da −ad= (q−q−1)bc, bc =cb, ad −q−1bc= 1.
We will focus on its 3D calculus with basis [25, 4]
e0 =dda−qbdc, e + =q−1adc−q−2cda, e −=ddb−qbdd
and relations e±f =q/divides.alt0f/divides.alt0fe±, e0f =q2/divides.alt0f/divides.alt0fe0, for f ∈Cq[SL2] an element of homogeneous degree
and /divides.alt0a/divides.alt0= /divides.alt0c/divides.alt0= 1, /divides.alt0b/divides.alt0= /divides.alt0d/divides.alt0=−1. Note that the above deﬁnitions imply that d acts on the generators
as
da=qbe++ae0, db=ae−−q−2be0, dc=qde++ce0, dd=ce−−q−2de0.
38 SHAHN MAJID AND FRANCISCO SIM ˜AO
This calculus in left-invariant in the sense that the coproduct ∆ induces a “left coaction”
∆L∶Ω1→Cq[SL2]⊗Ω1 via ∆Ld= (id⊗d)∆, and can be prolongated by setting
de0 =q3e+∧e−, de±=∓q±2[2]q−2e±∧e0,
e±∧e±=e0∧e0 = 0, q 2e+∧e−+e−∧e+ = 0, e 0∧e±+q±4e±∧e0 = 0,
where [n]q = (1−qn)/slash.left(1−q) denotes theq-integer. When discussing higher tensor powers of these
generators, we will use the notation ei1...in
n ∶=ei1⊗... ⊗ein ∈(Ω1
A)⊗An. for ij ∈{0,±}. To deﬁne
the jet bundle of Cq[SL2], we will restrict ourselves to left-invariant bimodule connections, i.e.
connections ∇satisfying ∆L∇= (id⊗∇)∆, where ∆ L here is the tensor product coaction on
Ω1⊗Ω1. Such connections where investigated in [4, Example 3.77]. We now build the jet bundle
for Cq[SL2] with q =±i.
Lemma 6.5. Left-invariant bimodule connections onΩ1 which are torsion-free, ﬂat,∧-compatibility,
extendable and Leibniz compatible exist only for q =±i, and in this case are characterised by ν ∈C
with
∇e0 =ν(e+−−e−+)−qe−+, ∇e±= 0, σ (er⊗es) = (−1)rses⊗er,
wherer,s ∈{0,±}.
Proof. A generic left-invariant connection is given by as [4, Example 3.77]
∇e0 =γe0⊗e0+νe+⊗e−+µe−⊗e+, ∇e±=α±e0⊗e±+β±e±⊗e0
on the generators, for parameters α±,β±,ν,µ,γ ∈C. Note that we can write this connection as
∇ei =−Γi
j⊗ej for the matrix with basis order e+,e 0,e−
Γ=−
/uni239B
/uni239C
/uni239D
α+e0 β+e+ 0
µe− γe0 νe+
0 β−e− α−e0
/uni239E
/uni239F
/uni23A0
.
The corresponding map σ is computed in [4, Example 3.77] as well as the torsion
T∇(e0) = (ν−q2µ−q3)e+∧e−, T ∇(e±) = (β±−q±4α±±q±2(1+q−2))e±∧e0.
The new part is to compute the curvature from R∇=−(dΓ+ Γ∧Γ) as
R∇=
/uni239B
/uni239C
/uni239D
(α+q3+β+µ)e+∧e− β+(−q2[2]q−2−q4α++γ)e+∧e0 0
µ(q−2[2]q−2+α+−q−4γ)e−∧e0 (γq3−q2µβ++νβ−)e+∧e− ν(−q2[2]q−2−q4γ+α−)e+∧e0
0 β−(q−2[2]q−2+γ−q−4α−)e−∧e0 α−q3−β−νq2e+∧e−
/uni239E
/uni239F
/uni23A0
.
We then use Mathematica to impose ﬂatness, torsion freeness and the YBE to ﬁnd the joint
solution as α±= β±= γ = 0, q = ±i and µ = −ν −q. This then gives the braiding σ(er⊗es) =
(−1)rses⊗er for r,s ∈{0,±}, meaning that σ is the ﬂip map whenever r = 0 or s = 0 and −ﬂip
otherwise. It is therefore clear the it is∧-compatible and extendable, so only Leibniz compatibility
needs to be checked, namelyσ2∇2 =∇2σ. Due to ∇e±= 0 this is immediate on er⊗es forr,s ∈±.
For the rest this is a matter of straight forward computation, we have for example
∇2σ(e0r) =∇2(er0) =σ1(νer+−+µer−+) =−νe+r−−µe−r+,
σ2∇2(e0r) =σ2(νe+−r+µe−+r) =−νe+r−−µe−r+
and similarly on er0,e 00. □
QUANTUM JET BUNDLES 39
Hence by our general results we have a jet bundle for these values of q. To compute the jet
bimodule note that the∧-relations reduce toe0∧e0 =e±∧e±= 0,e+∧e−=e−∧e+,e0∧e±=−e±∧e0 in
theq =±i case. This is very close to a Grassmann algebra, except for the commutation relations
for e+ and e−. The inﬁnite jet bimodule is then spanned by
J∞
Cq[SL2]= spanCq[SL2]/uni27E81,e 0,e±,e 0⊗e0,e±⊗e±,e+⊗e−−e−⊗e+,e 0⊗e±+e±⊗e0,... /uni27E9
up to degree 2. Higher degrees can be computed by starting with a basis element ei1...in
n and
adding terms to ensure that it is indeed in the kernel of ∧at every factor. To analyse the jet
prolongation maps jn let us introduce the following notation for n> 1
e{±0...0}
n =e±0...0
n +e0{±0...0}
n , e {±∓0...0}
n =e±{∓0...0}
n −e∓{±0...0}
n +e0{±∓0...0}
n ,
with e{±}
1 = e±and e{±∓}
2 = e±∓
2 −e∓±
2 . These are essentially all the permutations of the sets
{+0... 0} and {±∓0... 0}, where in the latter we take into account that when we swap signs,
the corresponding basis element gains a −1 factor. Note that in both cases we have e{±0...0}
n ∼
[n,σ]!e±0...0
n and e{±∓0...0}
n ∼[n,σ]!e±∓0...0
n , up to some normalisation constant.
Proposition 6.6. The jet prolongation map acts on the generators of Cq[SL2] as
jn(a) =a
n
/summation.disp
k=1
e0...0
n +qb
n
/summation.disp
k=1
e{+0...0}
n +νa
n
/summation.disp
k=2
e{+−0...0}
n ,
jn(b) =b
n
/summation.disp
k=1
e0...0
n +a
n
/summation.disp
k=1
e{−0...0}
n +νb
n
/summation.disp
k=2
e{−+0...0}
n ,
jn(c) =c
n
/summation.disp
k=1
e0...0
n +qd
n
/summation.disp
k=1
e{+0...0}
n +νc
n
/summation.disp
k=2
e{+−0...0}
n ,
jn(d) =d
n
/summation.disp
k=1
e0...0
n +c
n
/summation.disp
k=1
e{−0...0}
n +νd
n
/summation.disp
k=2
e{−+0...0}
n .
Proof. We will focus on the computation of jn(a), the rest of the jet prolongations can be
computed in a similar way. We will do this by induction. For n = 0, n = 1 this is clear due to
da=ae0+qbe+. For n= 2 we have j2(a) =a+ da+∇da and
∇da=∇(ae0+qbe+) =ae00+qbe+0+νa(e+−−e−+)−qae−++qbe0++qae−+=ae00+qbe{+0}+νae{+−}
showing that the formula indeed holds for n = 2. Before doing the computation for any n, we
need to show some identities, namely
∇ne0...0
n =
n−1
/summation.disp
k=0
σ1...σ ke0...0
k ⊗(∇e0)⊗e0...0
n−k−1
=νe+
n−1
/summation.disp
k=0
e0...0
k ⊗e−⊗e0...0
n−k−1+µe−
n−1
/summation.disp
k=0
e0...0
k e+e0
n−k−1 =νe+{−0...0}+µe−{+0...0}
which follows directly from the form of ∇e0 =νe+−+µe−+and Equation (5). The second identity
we will need is ∇ne{+0...0}
n =νe+{−+0...0}
n+1 , which we prove by induction. For n= 2 we have
∇2(e+0+e0+) =σ1(νe++−+µe+−+)+νe+−++µe−++=ν(e+−+−e++−)+µ(e−++−e−++) =νe+{−+}
the induction step then follows as
∇ne{+0...0}
n =∇n(e+0...0
n +e0{+0...0}
n ) =σ1e+∇n−1e0...0
n−1 +(∇e0)e{+0...0}
n−1 +σ1(e0∇n−1e{+0...0}
n−1 )
=−νe++{−0...0}
n+1 −µe−+{+0...0}
n+1 +νe+−{+0...0}
n+1 +µe−+{+0...0}
n+1 +νe+0{−+0...0}
n+1
=νe+{−+0...0}
n+1 .
40 SHAHN MAJID AND FRANCISCO SIM ˜AO
One can show that ∇ne{−0...0}
n =µe−{+−0...0}
n+1 in a similar manner. The third and last identity we
will need is ∇ne{+−0...0}
n = 0. This is clearly the case for n = 2 as ∇e±= 0. The induction step is
then
∇ne{+−0...0}
n =∇n(e+{−0...0}
n −e−{+0...0}
n +e0{+−0...0}
n ) =σ1e+∇n−1e{−0...0}
n−1 −σ1e−∇n−1e{+0...0}
n−1 +∇e0e{+−0...0}
n−1
=−µe−+{+−0...0}
n+1 +νe+−{−+0...0}
n+1 +νe+−{+−0...0}
n+1 +µe−+{+−0...0}
n+1 = 0.
With these 3 identities in hand, we can compute ∇na by induction as
∇na=∇n−1∇n−1a=∇n−1(ae0...0
n−1 +qbe{+0...0}
n−1 +νae{+−0...}
n−1 )
=ae0...0
n +qbe+0...0
n +νa(e+{−0...0}
n −e−{+0...0}
n )−qae−{+0...0}
n +qbe0{+0...0}
n +qae−{+0...0}
n
+qνbe+{−+0...0}
n +qνae0{+−0...0}
n +qνbe+{+−0...0}
n
=ae0...0
n +qbe{+0...0}
n +νae{+−0...0}
n .
□
In this example we again have im ∇n ⊂im[n,σ]! on the generators, which implies im ∇n ⊂
im[n,σ]! on the whole algebra. To see this take f,g ∈Cq[SL2] with ∇if = [i,σ]!dif ∈im[i,σ]!,
∇jg = [j,σ]!djg ∈im[j,σ]!, i,j ≤n, which in turn implies ∇n(fg) ∈im[n,σ]! for their product
∇n(fg) =
n
/summation.disp
k=0
/bracketleft.alt3n
k,σ/bracketright.alt3([n−k,σ ]!⊗[k,σ ]!)dn−kf⊗dkg = [n,σ]!
n
/summation.disp
k=0
dn−kf⊗dkg.
Thus, there is a reduced jet bundle J∞
σ =Sσ(Ω1) in this example as well, though it is smaller
than the original jet bundle, as one can already see in degree 2, since
im(id+σ) = spanCq[SL2]/uni27E8e0⊗e0,e+⊗e−−e−⊗e+,e 0⊗e±+e±⊗e0/uni27E9,
which is 4 dimensional, whereas Ω 2
S is 6 dimensional as shown above.
We remark that the inﬁnite jet bimoduleJ∞
Cq[SL2] in this example can also be cast as a braided
symmetric algebra S˜σ but for a diﬀerent braiding ˜σ obeying the braid relations and deﬁned on
the basis as the identity on the diagonal andσ otherwise. This is such that im[2, ˜σ]= ker∧= Ω2
S,
and similarly has Ωn
S = im[n, ˜σ]! at least up to n= 4 veriﬁed by hand.
