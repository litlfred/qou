---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-075-32-index-theorems-and-irregularity-33
section_title: "INDEX THEOREMS AND IRREGULARITY 33"
section_number: 3.2
pages: 39-40
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
Proof. — Conjugating the C-linear endomorphism σq−u of K by w∈ K ∗
(undestood as the automorphism ×w), one ﬁnds:
w◦ (σq−u)◦w−1 = w
σq(w)◦ (σq−u′), with u′ =uσq(w)
w ,
whence the ﬁrst statement. Then, qkv = σq(w)
w , where w = zk∏
i≥1
σ−i
q (v)∈ K
(also well deﬁned in the convergent case), whence the second statement.
So we now set u :=dzν.
Fact. — The kernel of σq−u :K→K has dimension 1 if (ν,d ) = (0, 1), and
0 otherwise.
Proof. — The series f = ∑ fnzn belongs to the kernel if, and only if
∀n , qnfn = dfn−ν. Since we deal with Laurent series having poles, this
implies f = 0 except maybe if ν = 0. In the latter case, it implies f = 0,
except maybe if d∈ qZ. From the condition on |d|, this is only possible if
d = 1, thus u = 1. In that case, the kernel is plainly C.
Fact. — The map σq−u :K→K is onto if ν >0 and also if ν = 0, d⁄= 1.
Proof. — Let g∈K. We look for f solving the equationσqf−dzνf =g inK.
This is equivalent to: ∀n, qnfn−dfn−ν =gn, that is, ∀n, fn =q−n(dfn−ν +
gn). If ν ≥ 1, one computes the coeﬃcients by induction from the ν ﬁrst
among them. Moreover, in the convergent case, inspection ofthe denominators
show that f converges if g does; and then, the functional equation ensures
meromorphy. If ν = 0 and d⁄= 1 (so that d /∈ qZ), one gets rightaway fn =
gn
qn−d. Convergence (resp. meromorphy) is then immediate in the co nvergent
case. (When ν≥ 1, one can also consider the ﬁxpoint equation F(f) = f,
where F(f) := σ−1
q (g +dzνf): it is easy to see that this is a contracting
operator as well for the formal topology, i.e. forz-adic convergence, as for the
transcendant topology, i.e. for usual convergence.)
Fact. — If (ν,d ) = (0, 1), the cokernel of σq−u :K→K has dimension 1.
Proof. — One checks that σq−u vanishes on C and induces an automorphism
of the subspace K • of K made up of series without constant term.
Fact. — Assume ν <0. Then σq−u :K→K is onto in the formal case.
Proof. — Put F ′(f) = d−1z−ν(σq(f)−g). Since ν > 0, this is a z-adically
contracting operator, whence the existence (and unicity) o f a ﬁxed point.
34 CHAPTER 3. THE AFFINE SPACE OF ISOFORMAL ANALYTIC CLASSES
Remark 3.2.1 . — This is the ﬁrst place where the formal and convergent
cases diﬀer. The operator is (rather strongly) expanding for the transcendant
topology, it produces Stokes phenomena! So this is where we need an argument
from analysis in the convergent case.
Fact. — Assume ν =−r,r∈ N∗. Then, in the convergent case, the cokernel
of σq−u :K→K has dimension r.
Proof. — This is a consequence of lemma 3.1.2 (and therefore relies on the
use of the q-Borel transformation).
We now summarize our results:
Proposition 3.2.2. — Let u =dzνv, v∈K, v(0) = 1, with d∈ C∗. Write
d the class of d moduloqZ. The following table shows the ranks of the kernel
and cokernel, as well as the index χ(P ) := dim Ker P− dim Coker P of the
C-linear operator P :=σq−u :K→K:
(ν,d) Kernel Cokernel Index
(0, 1) 1 1 0
(0,⁄= 1) 0 0 0
(> 0,−) 0 0 0
(< 0,−) 0
{
