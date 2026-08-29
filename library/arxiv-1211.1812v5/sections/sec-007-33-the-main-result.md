---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-007-33-the-main-result
section_title: "The main result."
section_number: 3.3
pages: 17-20
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
We now deﬁne a presheaf structure on the family Z 1
c (R)< := {Z 1
c (R)<a}a∈∆ , by means of the
restriction functors
raa′ :Z 1
c (R)<a′ →Z 1
c (R)<a , ( raa′z :=z|Σ 1(∆ a) , raa′ρ := {ρe}e∈∆ a ) , raa′t := {te}e∈∆ a ,
which obviously fulﬁll the presheaf relations raa′′ =raa′ ◦ra′a′′ , ∀a ⊆a′ ≤a′′ .
Lemma 3.2. The pair Z⊗ := (Z 1
c (R)<,r )∆ deﬁnes a simple tensor presheaf. Moreover we have
ǫ(zρ,wσ)e = ǫ( raa′zρ,raa′wσ )e , ∀e<a ⊆a′ , (3.11)
where zρ,wσ ∈ obj Z 1
c (R)<a′ .
Proof. We assume a ⊂ a′ , otherwise there is nothing to prove. Let zρ,wσ ∈ obj Z 1
c (R)<a′ and
t ∈ (zρ,wσ). Then for any path p :e′ →e such that e<a , e′<a ′ , |p| ⊆ ∆ a′
, we have
‖te‖2 = ‖z(p)te′w(p)∗‖2 = ‖w(p)t∗
e′te′w(p)∗‖ = ‖t∗
e′te′ ‖ = ‖te′ ‖2 ,
so raa′ is isometric and Z is a presheaf. In the following lines we prove that any raa′ , a ⊆ a′ ,
preserves tensor product and the families ǫ(·, ·). The fact that the tensor product is preserved is
evident by (3.8). Passing to the ”symmetry”, we consider a ⊆a′ , zρ,wσ ∈Z 1
c (R)<a′ and note that
the operators
ǫ(raa′zρ,raa′wσ )e , e ∈ ∆ a ,
should be deﬁned, according to (3.9), using paths poe , po′e in ∆ a with o ⊥o′ ; but since ∆ a ⊆ ∆ a′
and Σ 1(∆ a) ⊆ Σ 1(∆ a′
) we have that poe , po′e are paths also in ∆ a′
, so, since any ǫ(zρ,wσ)e ,
e ∈ ∆ a′
, is independent on the choice of poe , po′e , we obtain (3.11) as desired.
Lemma 3.3. Z 1(R) is the category of sections of Z⊗ .
Proof. If z ∈ obj Z 1(R) then we deﬁne the family za := z|Σ 1(∆ a) , ∀a ∈ ∆; to add a family of
charges, for any e<a we set
{ ∆( ⊥a,e ) := {p : ∂1p ⊥a,∂ 0p =e} ,
̺a
e (t) := {adz(p)}(t), ∀t ∈Ra , where p ∈ ∆( ⊥a,e ) .
By [9, Eq.4.5], ̺a
e does not depend on the choice of p ∈ ∆( ⊥a,e ), and [9, Lemma 5.1(i,iv)] 5 imply
that ̺a
e ∈ locRa . Using [9, Lemma 5.1(ii)] we ﬁnd
z(b) ·̺a
∂1b(t) = ̺a
∂0b(t) ·z(b) , ∀a ∈ ∆ , t ∈Ra , b ∈ Σ 1(∆ a) , (3.12)
so
za
̺ := ( za , ̺a := {̺a
e }e<a ) ∈ obj Z 1
c (R)<a .
Let now a ⊆a′ ; then ∆( ⊥a′,e ) ⊆ ∆( ⊥a,e ) so, by path-invariance of ̺a′
e ,
̺a′
e |Ra := ad z(p′)|Ra = ̺a
e , ∀p ∈ ∆( ⊥a′,e ) ⊆ ∆( ⊥a,e ),
5 In this reference an x ∈ M is chosen with a ⊥ {x} , and we have the notation ̺a
e ≡ yz
x(e)|Ra , ∀e ∈ ∆ a .
Moreover, it is proved that ̺a
e is independent of x .
17
and we conclude that {za
̺ }a is a section of Z. If t ∈ (z,w ) then deﬁning ta
e :=te , ∀e < a, yields
an arrow ta of Z 1
c (R)<a and a section ~t := {ta} , so Z 1(R) is a subcategory of ~Z. On the other
side, let us consider a section
(~z, ~̺) ∈ obj ~Z , (~z, ~̺) = {(~za, ~̺a) ∈ obj Z 1
c (R)<a}a∈∆ .
Since any a ∈ ∆ has proper closure in M , for any b ∈ Σ 1(∆) there is a ∈ ∆ such that |b| ∈ Σ 1(∆ a)
and we deﬁne z(b) := ~za(b). Since ~z is a section, the previous deﬁnition does not depend on the
choice of a > |b|; moreover given c ∈ Σ 2(∆) we have dz(c) = d~za(c) = 1 for any a > |c| so
z ∈ obj Z 1(R). If ~t := {~ta} is an arrow of ~Z then for any e ∈ ∆ there must be some a ∈ ∆ with
e<a and we set te := ~ta
e , so reasoning as above we have that t := {te} is an arrow of Z 1(R). We
conclude that Z 1(R) = ~Z as desired.
Lemma 3.4. The subpresheaf S := Z↓ , deﬁned as in Rem.2.1, is a simple, symmetric tensor
presheaf and ~S =Z 1(R).
Proof. By deﬁnition we have S = (S,r )∆ , where each Sa , a ∈ ∆, is the full subcategory of
Z 1
c (R)<a with objects
obj Sa := {za
̺ , z ∈ obj Z 1(R)} .
By Rem.2.1 we already know that ~S =Z 1(R). Moreover S is clearly simple and tensorial, so we
only have to check the symmetry property. To this end we note tha t we already know from §3.2
that, given o,o ′ <a , o ⊥o′ ,
ǫ(za
̺,wa
ς )e := wς (poe)∗ςa
o (z̺(po′e))∗ ·z̺(po′e)̺a
e (wς (poe)) , e<a ,
fulﬁls the symmetry relations, so we only have to prove that ǫ(za
̺,wa
ς )e ∈ Re for any e ∈ ∆ a .
Now, the point is that ǫ(za
̺,wa
ς ) is deﬁned exactly as in [9, Eq.5.10] and this time, due to the fact
that z,w are globally deﬁned , the charges ̺a
e,ςa
e extend to endomorphisms ̺x
e,ςx
e ∈ endR⊥
x , where
R⊥
x := ∪ω⊥{x}Rω for any x ∈M such that {x} ⊥ e (see [9, §5.1]). The property (3.7) now holds
in the form
ǫ(za
̺,wa
ς )e · {̺x
e ◦ςx
e }(t) = {ςx
e ◦̺x
e }(t) ·ǫ(za
̺,wa
ς )e , ∀t ∈R⊥
x ,
at varying of x ∈M with {x} ⊥ e (see [9, Lemma 5.1(iii)]). So, as remarked in §3.2,
ǫ(za
̺,wa
ς )e ·t′ = t′ ·ǫ(za
̺,wa
ς )e , ∀t′ ∈Rω ⊆R⊥
x , ω ⊥ {x} , ω ⊥e ,
and we conclude, by punctured Haag duality, that ǫ(za
̺,wa
ς )e ∈Re as desired.
Before to state our main result we select the sectors having a conj ugate. For any a ∈ ∆, we
denote the full subcategory of Sa with objects za
̺ , z ∈Z 1,•(R), by S•
a , and deﬁne
S• := ( S•,r )∆ .
By the previous Lemmata, and since by [9, §5.3] we have that Z 1,•(R) is a DR-category, we obtain:
Theorem 3.5. Let R = (R,j )∆ ⊆BH be a Haag-Kastler net where ∆ is the base of diamonds of
a globally hyperbolic spacetime M with spacetime dimension ≥ 3 . Then S := (S,r )∆ is a simple,
symmetric tensor presheaf such that Z 1(R) is the category of sections of S. In particular, S• is
a DR-presheaf with category of sections Z 1,•(R).
In the following points we list some consequences of the previous the orem.
18
Holonomy of sectors. Let z ∈ obj Z 1(R) and β ˆz the presheaf bundle of tensor powers of z
deﬁned in (2.15). By deﬁnition, the ﬁbre β ˆza , a ∈ ∆, has objects the tensor powers zn
a :=z ⊗... ⊗z ,
n ∈ N (note that a ∈ ∆ plays no role at the level of objects), and arrows
β(zn
a,zm
a ) = {t = (te ∈Re, e∈ ∪a′⊇a∆ a′
) : zm(b)t∂1b =t∂0bzn(b), ∀b ∈ Σ 1(∪a′⊇a∆ a′
)} .
A simpler way to describe β(zn
a,zm
a ) is the following: since any a has compact closure, we can ﬁnd
a′ ∈ ∆ such that a ∈ ∆ a′
; thus for any t ∈ β(zn
a,zm
a ) we can pick ta ∈ Ra , and this suﬃces to
determine t because of the relation
te = zm(p)tazn(p)∗ , ∀e ∈ ∪a′⊇a∆ a′
,
where p : a → e is a path made of 1-simplices in Σ 1(∪a′⊇a∆ a′
). In this way, on the arrows, the
restriction functors take the form rz
aa′ (ta′) = ta , a ⊆a′ , and have inverse
rz
a′a(ta) = ta′ = zm(ba′a)tazn(ba′a)∗ , ba′a := (a′,a ;a′) ∈ Σ 1(∆) .
Thus, reasoning as in (2.7), we compute the holonomy of β ˆz ,
χ′
z :π1(∆) → autβ ˆza , {χ′
z(p)}(ta) = zm(p)tazn(p)∗ , p :a →a , ta ∈ β(zn
a,zm
a ). (3.13)
Let now in particular z ∈ obj Z 1,•(R). By Theorem 2.3, the sector z deﬁnes a compact Lie group
Gz ⊆ U(d) and a holonomy representation χz : π1(∆) → QGz := NGz/Gz , which is a complete
invariant of the presheaf bundle β ˆz . In accord with the proof of [39, Theorem 5.3], the group
Gz is such that there is a symmetric tensor isomorphism F : β ˆza → ˆπGz . Regarding QGz as
an automorphism group of ˆπGz (see Ex.2.2), by the argument used to prove [39, Eq.5.5] we have
χz ◦F =F ◦χ′
z . It can be easily veriﬁed that d is the statistical dimension of z (see [9, §5.3]), but
we prefer to not discuss here the details.
Dual objects and topologically trivial sectors. By Theorem 2.2, any embedding I : S• → C
yields a full embedding of symmetric tensor C*-categories Z 1,•(R)֒→HilbG(∆), where G is a
compact group net bundle, and induces lifts ˆχz :π1(∆) →NGz , χz = ˆχz modGz , of the holonomies
deﬁned by sectors z ∈ obj Z 1,•(R). Let now Z 1
t (R) denote the subcategory of topologically
trivial sectors, that is, of those z ∈ obj Z 1(R) such that there is a family ψ = {ψa ∈ UH } with
z(b) = ψ∗
∂0bψ∂1b , b ∈ Σ 1(∆). Then zn(p) = 1 for any p :a →a and n ∈ N, and by (3.13) we have
that χ′
z(p) is the identity functor for any z ∈ obj Z 1
t (R). Thus when z ∈ obj Z 1,•
t (R) we have that
χ′
z and χz are trivial, and there is at least one lift ˆχz , the trivial one. We have a full embedding
Z 1,•
t (R)֒→HilbGt (∆), where Gt is the trivial net bundle with ﬁbre the Doplicher-Roberts dual Gt
of Z 1,•
t (R). But, by the results in [39], we may also have Z 1,•
t (R)֒→HilbG(∆) for some nontrivial
group net bundle G.
Cochains. By Theorem 2.4, any sector z ∈ obj Z 1,•(R) deﬁnes the 1–cochain uz : Σ 1(∆) →NGz
that classiﬁes lifts ˆχz :π1(∆) →NGz , q ◦ ˆχz =χz . The cochain uz deﬁnes a gerbe in the sense of
§5, see (5.2).
Characteristic classes. Let Pz →M denote the locally constant, principal QGz -bundle deﬁned
by χz . By (2.5), we have characteristic classes ζ↑(z) := [ ζ↑(Pz)] ∈ H 2k−1(M, R/K) that vanish
when χz is the trivial morphism, that is, when z is a topologically trivial sector. Thus we can
measure the obstruction of z being a topologically trivial sector in terms of the odd cohomology of
the given spacetime.
19
Chern classes of ﬁelds with ”trivial gauge group”. Let R be a Haag-Kastler net such that
Gz is trivial for any z ∈ obj Z 1,•(R). Then NGz =QGz = U(d) and χz takes values in U(d) . By
(2.6) we have Chern classes
{
ck(z) := c↑
k(χz) ∈H 2k−1(M, R/Z) , ∀k = 1,... ,d ,
ccs(z) := d + ∑ d
k=1
(−1)k−1
(k−1)! ck(z)modQ ∈ Z ⊕Hodd(M, R/Q) . (3.14)
This is the situation that we expect to hold for quantum ﬁelds with triv ial superselection structure
in the Minkowski spacetime, as, for example, the free electromagn etic ﬁeld. The classes (3.14) are
an interesting clue supporting the idea that Brunetti-Ruzzi secto rs describe Aharonov-Bohm-type
situations ([9, §7]): in fact, in the same way the monodromy phase of the quantum ele ctromagnetic
potential is described by a class in H 1(M, R/Z), the holonomy of z ∈ obj Z 1,•(R) is measured by
the ﬁrst Chern class c1(z) ∈H 1(M, R/Z). In this regard, we conjecture that the free electromagnetic
ﬁeld yields a net such that that Gz is trivial for any z ∈ obj Z 1,•(R).
