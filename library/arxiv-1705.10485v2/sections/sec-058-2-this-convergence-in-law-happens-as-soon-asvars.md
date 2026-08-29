---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-058-2-this-convergence-in-law-happens-as-soon-asvars
section_title: "This convergence in law happens as soon asVar(Sn)"
section_number: 2
pages: 49-49
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
nε →∞ for someε> 0.
Proof. Combining Propositions 54 and 44, the sumSn admits uniform bounds on cumulants with pa-
rameters
Dn =
(
1 + 2
∞∑
t=1
(θP )t
)
= 1 +θP
1−θP
,
Nn = n and A = K
√
M. Observe thatDn is here independent ofn. We can apply Corollary 30 to get
the ﬁrst part of the theorem. The second follows from Theorem 32. ⊓ ⊔
Remark 56.A bound similar to Eq. (12) is given in [SS91, Theorem 4.19]. We believe however that the
proof given there is not correct. Indeed, the proof associates with each partitionπ such thatN(π)⁄= 0 a
sequence of numberqj; the authors then claim that “obviouslyqj≤qj+1” (p. 93, after eq. (4.53)). This
is unfortunately not the case as can be seen on the example of partitions given p. 81 inloc. cit.: for this
partition q3 = 3, whileq4 = 2. As a consequence of this mistake, the authors forget many partitionsπ
when expressing classical cumulants in terms of Boolean cumulants (since they encode partitions with
only non-decreasing sequencesqi), which make the resulting bound on classical cumulants too sharp. We
have not found a simpler way around this error than the use of uniform weighted dependency graphs
presented here. Note nevertheless that our proof still uses several ingredients from [SS91]: the use of
Boolean cumulants and the relation between Boolean and classical cumulants.
Remark 57.If the functionsft are indicatorsft(x) = 1x=st, then one can remove the size(
√
M)3 in the
bound on the Kolmogorov distance. Indeed, in this case, we have
B(r)(Yt1,...,Y tr) =π(s1)Qt2−t1(s1,s 2)Qt3−t2(s2,s 3)··· Qtr−tr−1(sr−1,sr).
On the other hand, the individual terms of the matrixQt(x,y ) can be bounded by
|Qt(x,y )|≤
√
π(y)
π(x) (θP )t,
by adapting the proof of Theorem 53. Therefore,
⏐⏐⏐B(r)(Yt1,...,Y tr)
⏐⏐⏐≤ (θP )tr−t1π(s1)
√
π(s2)
π(s1)···
√
π(sr)
π(sr−1)
≤ (θP )tr−t1
√
π(s1)π(sr)≤ (θP )tr−t1.
Thus, in this case, one has the bound of Theorem 55 without the factor(
√
M)3.
