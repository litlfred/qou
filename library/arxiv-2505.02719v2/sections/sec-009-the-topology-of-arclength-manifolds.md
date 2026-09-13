---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais–Smale condition in geometric knot theory"
section_id: sec-009-the-topology-of-arclength-manifolds
section_title: "The topology of arclength manifolds"
section_number: null
pages: 20-23
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
doc_brief: "On the Palais–Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy"
---
Fix a pointz∈R 𝑛 and𝑠∈ (0,1]. The Hilbert spaceH=𝐻 1+𝑠(R/Z,R𝑛) with its inner
product8
⟨𝑓,ℎ⟩ H ≔⟨𝑓,ℎ⟩ 𝐻1+𝑠 =⟨𝑓,𝑔⟩ 𝐿2+⟨𝑓 ′,𝑔′⟩𝐿2
+
∫
R/Z
∫
R/Z
⟨𝑓(𝑢)−𝑓(𝑣),ℎ(𝑢)−ℎ(𝑣)⟩
|𝑢−𝑣| 1+2𝑠
R/Z
d𝑢d𝑣,for𝑓,ℎ∈H, (3.22)
8For𝑠=1simply replace the double integral in (3.22) by⟨𝛾′′,ℎ′′⟩𝐿2.
20
induces a Riemannian metric𝑔on the arclength submanifolds
N 1+𝑠
z ⊂N 1+𝑠⊂𝐻 1+𝑠
r (R/Z,R𝑛)⊂𝐻 1+𝑠(R/Z,R𝑛)and
A1+𝑠
z ⊂A 1+𝑠⊂𝐻 1+𝑠
ir (R/Z,R𝑛)⊂𝐻 1+𝑠(R/Z,R𝑛).
More precisely, letM ∈

N 1+𝑠,N 1+𝑠
z ,A 1+𝑠,A 1+𝑠
z
	
,𝑔 𝛾(𝑓,ℎ)≔⟨𝑓,ℎ⟩ H for𝛾∈Mand
𝑓,ℎ∈𝑇 𝛾M. So,Mis a smooth Riemannian submanifold of the open set𝐻1+𝑠
r (R/Z,R𝑛), or
𝐻1+𝑠
ir (R/Z,R𝑛), respectively; see [52, Theorem 3.6]. As in the abstract setting of Section 2.2
we have the path metric (cf. (2.5))
distM(𝛾,𝜂)≔inf
𝑐∈𝒫(𝛾,𝜂)
∫ 1
0
√︃
𝑔𝑐(𝑡)(⁄𝑐(𝑡),⁄𝑐(𝑡))d𝑡=inf
𝑐∈𝒫(𝛾,𝜂)
∫ 1
0
∥⁄𝑐(𝑡)∥H d𝑡(3.23)
measuringthedistanceoftwocurves𝛾,𝜂∈MinthesameconnectedcomponentofM,where
𝒫(𝛾,𝜂)≔

𝑐∈𝐶 1([0,1],M):𝑐(0)=𝛾,𝑐(1)=𝜂
	
.(3.24)
To investigate the topology ofMmore closely, we look at a mapping that transforms
an arbitrary regular closed curve𝛾∈𝐻 1+𝑠
r (R/Z,R𝑛)into an arclength parametrized curve.
The arclength𝜓𝛾 :[0,1]→[0,1](rescaled to the unit interval and then extended to all of
Rsuch that𝜓 𝛾(𝑡+1)=1+𝜓 𝛾(𝑡)for all𝑡∈R) is given by the strictly monotonic function
𝜓𝛾(𝑡)≔ 1
L(𝛾)L(𝛾|[0,𝑡])for𝑡∈[0,1]. Ithasastrictlymonotonicinverse𝜓 −1
𝛾 :[0,1]→[0,1].
We prove in Theorem A.1 in Appendix A that the reparametrization and rescaling mapping
arc :𝐻 1+𝑠
r (R/Z,R𝑛)→𝐻 1+𝑠
a (R/Z,R𝑛)given by
arc(𝛾)≔ 1
L(𝛾) 𝛾◦𝜓 −1
𝛾 for𝛾∈𝐻 1+𝑠
r (R/Z,R𝑛)(3.25)
is continuous with respect to the𝐻1+𝑠-topology for any𝑠∈( 1
2,1). For𝑠=1this was proven
by Reiter in [57, Theorem 1.13]. Notice that rescaling and reparametrization does not destroy
the injectivity of a curve so that we have the inclusionarc(𝐻1+𝑠
ir (R/Z,R𝑛)) ⊂A1+𝑠 for all
𝑠∈( 1
2,1].
Theorem 3.7 (Arclength manifolds are strong deformation retracts)The open set
𝐻1+𝑠
r (R/Z,R𝑛)⊂𝐻 1+𝑠(R/Z,R𝑛)strongly deformation retracts onto the submanifoldsN1+𝑠
andN 1+𝑠
z forany𝑠∈( 1
2,1]andz∈R 𝑛,whereas𝐻 1+𝑠
ir (R/Z,R𝑛)stronglydeformationretracts
ontoA 1+𝑠 andA 1+𝑠
z .
Proof.If𝛾∈N 1+𝑠 thenL(𝛾)=1and𝜓 𝛾(𝑡)=𝑡forany𝑡∈Rsothatarc(𝛾)=𝛾bydefinition
(3.25). Therefore, the mappingarc:𝐻 1+𝑠
r (R/Z,R𝑛)→𝐻 1+𝑠
a (R/Z,R𝑛)=N 1+𝑠 is continuous
witharc| N 1+𝑠 =IdN 1+𝑠, whence a retraction ontoN1+𝑠. For a given pointz∈R 𝑛 we simply
compose the maparcwith the smooth shift𝜏z :𝐻 1+𝑠(R/Z,R𝑛)→𝐻 1+𝑠(R/Z,R𝑛)defined as
𝜏z(ℎ)≔ℎ+z−ℎ(0)satisfying𝜏 z(𝛾)=𝛾for all𝛾∈A 1+𝑠
z so that we obtain the retraction
𝜏z◦arc :𝐻 1+𝑠
ir (R/Z,R𝑛)→N 1+𝑠
z .
Now,weneedtoconstructahomotopybetweentheidentitymaponthesetO≔𝐻 1+𝑠
r (R/Z,R𝑛)
andtheretractionontoN 1+𝑠,andN 1+𝑠
z ,respectively. Considerforanycurve𝜂∈Othefamily
of parameter transformations
𝜙𝜂(𝜎)≔(1−𝜎)Id R+𝜎𝜓−1
𝜂 :[0,1]→[0,1]for𝜎∈[0,1],(3.26)
21
where, as before,𝜓−1
𝜂 is the strictly monotonic inverse of the rescaled arclength𝜓𝜂(𝑡)=
1
L(𝜂)L(𝜂|[0,𝑡]). As before, we may extend𝜙𝜂 to all ofRwith𝜙 𝜂(𝑡+1)=1+𝜙 𝜂(𝑡)for all
𝑡∈R. Clearly,𝜙 𝜂(𝜎)(0)=0and𝜙 𝜂(𝜎)(1)=1, and𝜙 𝜂(𝜎)(·)is strictly increasing for all
𝜎∈[0,1], since𝜙 𝜂(𝜎)′(𝑡)=(1−𝜎)+𝜎(𝜓 −1
𝛾 )′(𝑡)>0for any𝑡∈[0,1]. We can interpret
thisfamily𝜙 𝜂(𝜎)asamapping𝜙 ·(·):O×[0,1]→𝐻 1+𝑠
r ([0,1]),whichclearlyiscontinuous
onO×[0,1]due to Corollary A.3 and Lemma A.5 in Appendix A. Next, we modify the
mappingarcin (3.25) to obtain a family of mappingsArc(𝜂,𝜎)for𝜎∈[0,1]defined as
Arc(𝜂,𝜎)≔ 1
1+𝜎(L(𝜂)−1) 𝜂◦𝜙 𝜂(𝜎)for𝜂∈O.(3.27)
Lemma A.4 in Appendix A implies that the mapArc(·,·):O×[0,1]→Ois continuous.
With𝜙𝜂(0)(𝑡)=𝑡forall𝑡∈RonehasArc(𝜂,0)=𝜂forall𝜂∈O,andArc(𝜂,1)∈N 1+𝑠 since
𝜙𝜂(1)=𝜓 −1
𝜂 so thatArc(𝜂,1)=arc(𝜂)by (3.25), and the original maparcwas shown to be a
retraction ontoN 1+𝑠. For𝛾∈N 1+𝑠 one hasL(𝛾)=1and𝜓 −1
𝛾 (𝑡)=𝑡whence𝜙 𝛾(𝜎)(𝑡)=𝑡
for all𝑡∈Rand𝜎∈[0,1], and thereforeArc(𝛾,𝜎)= 1
1+𝜎(1−1) 𝛾=𝛾.Hence,Arc(·,·)is a
strong deformation retraction ofOontoN 1+𝑠.
If we fix a pointz∈R 𝑛 to treat the arclength submanifoldN1+𝑠
z instead ofN 1+𝑠, then
we take the family of shifts𝑇z(ℎ,𝜎)≔ℎ+𝜎(z−ℎ(0))forℎ∈O. Then the composition
𝑇z(Arc(·,𝜎),𝜎)for𝜎∈[0,1]yieldsastrongdeformationretractionofOontoN 1+𝑠
z . Indeed,
we have𝑇 z(ℎ,0)=ℎ,𝑇 z(ℎ,1)=ℎ+z−ℎ(0)hence𝑇 z(ℎ,1)′ =ℎ ′, and𝑇 z(ℎ,1)(0)=z
for allℎ∈O. So,𝑇 z(Arc(𝜂,0),0)=Arc(𝜂,0)=𝜂, and𝑇 z(Arc(𝜂,1),1)=Arc(𝜂,1)+z−
Arc(𝜂,1)(0)∈N 1+𝑠
z for every𝜂∈O. In addition, for𝛾∈N 1+𝑠
z we have shown above that
𝑇z(Arc(𝛾,𝜎),𝜎)=𝑇 z(𝛾,𝜎),which equals𝛾since𝛾(0)=z.
ReplacingN 1+𝑠 and𝐻 1+𝑠
r byA 1+𝑠 and𝐻 1+𝑠
ir respectively, yields the desired statement for
the submanifolds of arclength parametrized knots.□
Remark 3.8Theorem 3.7 justifies restricting knot energies to the submanifold of arclength
parametrized curves topologically: As the knot space𝐻1+𝑠
ir (R/Z,R𝑛)strongly deformation
retracts ontoA 1+𝑠 and also ontoA1+𝑠
z , all three topological spaces are homotopy equivalent
and hence contain the same topological information.
The last result of this section gives a justification from the perspective of knot theory.
Theorem 3.9 (Connected components are knot classes)Let𝑠∈(1
2,1]. If two knots𝛾0 and
𝛾1lieinthesameconnectedcomponentofA 1+𝑠 thentheyare𝐶 1-ambientlyisotopic. If,onthe
otherhand,twoknots𝛾 0,𝛾 1∈A 1+𝑠 are𝐶 1-isotopicinR 𝑛,thentheylieinthesameconnected
component ofA 1+𝑠. All statements remain true if we replaceA1+𝑠 byA 1+𝑠
z for some fixed
pointz∈R 𝑛.
Proof.Fix𝑠∈ ( 1
2,1]. It suffices to treatA≔A 1+𝑠. If𝛾 0,𝛾 1 ∈ Aare contained in
the same connected component of the smooth submanifoldA⊂O≔𝐻 1+𝑠
ir (R/Z,R𝑛)then
there exists a path𝑐∈𝐶 ∞([0,1],A)such that𝑐(0)=𝛾 0 and𝑐(1)=𝛾 1; see, e.g., [52,
Lemma 3.1]. Set𝐽(𝑡,𝜎)≔𝑐(𝜎)(𝑡)for𝑡∈R/Zand𝜎∈ [0,1], to find that the curve
𝐽(·,𝜎) ∈ Ais a𝐶 1-embedding for any𝜎∈ [0,1]by means of the Morrey embedding
𝐻1+𝑠(R/Z,R𝑛)↩→𝐶 1(R/Z,R𝑛); see [37, Theorem A.2]. Moreover, one can show with this
22
embedding that𝐽is also of class𝐶1(R/Z×[0,1],R 𝑛)so that𝐽constitutes a𝐶 1-isotopy with
𝐽(·,0)=𝛾 0 and𝐽(·,1)=𝛾 1. According to [10, Theorem 1.2] the two knots𝛾0 and𝛾 1 are
therefore ambiently isotopic, i.e., in the same knot class.
Let𝐽∈𝐶 1(R/Z×[0,1],R 𝑛)be an isotopy satisfying𝐽(·,0)=𝛾 0 and𝐽(·,1)=𝛾 1. We
consider the metric space𝑋≔𝐶 1(R/Z,R𝑛)with the𝐶 1-norm. Define𝛤∈𝐶 0([0,1],𝑋)by
𝛤(𝑡)≔𝐽(·,𝑡). The set𝑈≔𝐶 1
ir(R/Z,R𝑛)is open in𝑋, and𝛤maps into it. Observe that the
distance function
dist(𝛾,𝑋\𝑈)≔inf
𝜂∈𝑋\𝑈
∥𝛾−𝜂∥ 𝐶1 for𝛾∈𝑈
is Lipschitz continuous. Thus, the function𝐹:[0,1] →R,𝐹(𝑡)≔dist(𝛤(𝑡),𝑋\𝑈)is
continuous. Theinterval[0,1]iscompact,so𝐹musthaveaminimizer𝑡 0∈[0,1]. Becauseof
𝛤(𝑡 0)∈𝑈andbecause𝑈isopen,theminimumvaluemustbepositive:2𝜀≔𝐹(𝑡 0)>0. Since
𝐶∞(R/Z×[0,1],R 𝑛)is dense in𝐶1(R/Z×[0,1],R 𝑛), there is an𝐻∈𝐶∞(R/Z×[0,1],R 𝑛)
so that∥𝐽−𝐻∥ 𝐶1(R/Z×[0,1],R𝑛) <𝜀. For the path𝐺defined by𝐺(𝑡)≔𝐻(𝑡,·)this means that

𝑡↦→∥𝛤(𝑡)−𝐺(𝑡)∥ 𝐶1

𝐿∞≤∥𝐽−𝐻∥ 𝐶1([0,1]×R/Z,R𝑛) <𝜀.
By construction, we have for every𝑡∈[0,1]that
𝐺(𝑡)∈𝐵 𝜀(𝛤(𝑡))∩𝐶 2(R/Z,R𝑛)⊂𝑈∩𝐶 2(R/Z,R𝑛)=𝐶 2
ir(R/Z,R𝑛).
Since the embedding𝐶2(R/Z,R𝑛)↩→𝐻 1+𝑠(R/Z,R𝑛)is linear and continuous, the path𝐺is
an element of𝐶∞([0,1],𝐻 1+𝑠
ir (R/Z,R𝑛)). Now we define the linear homotopies
𝛤1(𝑡)≔(1−𝑡)𝛾 0+𝑡𝐺(0)and𝛤 2(𝑡)≔(1−𝑡)𝐺(1)+𝑡𝛾 1,for𝑡∈[0,1].
Notice that𝐺(0)∈𝐵 𝜀(𝛾0),𝐺(1)∈𝐵 𝜀(𝛾1), that these balls contained in𝐶1
ir(R/Z,R𝑛)are
convex, and that knot classes are stable under small𝐶1-pertubations, see [10]. Thus, we
have𝛤 1,𝛤2∈𝐶 ∞([0,1],𝐻 1+𝑠
ir (R/Z,R𝑛)). Concatenation of the paths𝛤1,𝐺, and𝛤 2 yields a
continuous path from𝛾0 to𝛾 1 in𝐻 1+𝑠
ir (R/Z,R𝑛). Finally, we retract this path to a continuous
path inA, by means of Theorem 3.7.□
