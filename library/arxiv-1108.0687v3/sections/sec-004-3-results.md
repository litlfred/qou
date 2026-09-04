---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-004-3-results
section_title: "Results"
section_number: 3
pages: 6-9
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
---
The chief consequence of the strong Rayleigh property that we us e to prove concentration inequalities
is the stochastic covering property. Although all of our examples s o far of measures with the SCP
are in fact strong Rayleigh, we note that this may not be the case in t he future, and with this in
mind, we state a result that uses only the SCP.
5
Theorem 3.1 (homogeneity and SCP implies Gaussian concentration) . Let P be a k-homogeneous
probability measure on Bn satisfying the SCP. Let f be a Lipschitz-1 function on Bn. Then
P(f − Ef ≥a) ≤ exp
(
−a2
8k
)
.
Remarks. (i) Replacing f with −f gives immediate two-sided bounds:
P(|f − Ef |>a ) ≤ 2 exp
( −a2
8k
)
. (3.8)
(ii) Replacing everyXi by 1−Xi if necessary, we may assume without loss of generality that k ≤n/2,
whence
P(f − Ef >a) ≤ exp
( −a2
4n
)
. (3.9)
For strong Rayleigh measures that are not necessarily homogeneo us, we have the following result.
Theorem 3.2 (Gauss-Poisson bounds for general strong Rayleigh measures) . Let P be strong
Rayleigh with mean µ = EN . Let f : Bn → R be Lipschitz-1. Then
P(f − Ef >a) ≤ 3 exp
(
− a2
16(a + 2µ)
)
;
P(|f − Ef |>a ) ≤ 5 exp
(
− a2
16(a + 2µ)
)
.
Remark. Because a,µ ≤n, the denominator in these inequalities may be replaced by 48 n.
Continuous versions
Continuous versions of these results may be stated in terms of poin t processes, which we now brieﬂy
review. Formally, a point process on a space S is a random counting measure on S. In other
words, a point process is a map Z deﬁned on a probability space (Ω , F, P) taking values in the space
of counting measures on S, a counting measure being one that takes only integer values or + ∞.
Intuitively, one envisions the sample counting measure Z(ω) as a set of points such that the sum of
delta functions at these points is the sample counting measure.
If the number k of points in the support of Z is deterministic, we may dispense with much of the
formalism by ordering the points in the support of Z uniformly at random and identifying the process
Z with the resulting exchangeable probability law on sequences of lengt hk inS. Notationally, if Z is
ak-homogeneous point process on Rd with law P, we denote by P↑ the corresponding exchangeable
law on ( Rd)k. For 1 ≤j ≤k, we use Xj to denote the “jth random point”, that is, the jth coordinate
function on ( Rd)k. The following sampling algorithm for any k-homogeneous point process is almost
trivial once one identiﬁes Z with P↑, and yet it is a generalization of an algorithm previously proved
only in the case of determinantal point process in [HKPV09, Proposit ion 4.4.3].
6
Lemma 3.3 (sampling in k steps). Let Z be a k-homogeneous point process on a standard Borel
spaceS and let P↑ be the corresponding exchangeable measure on Sk. Then for 0 ≤j <k there are
regular conditional distributions Qx1,...,xj for the law of Xj+1 given X1 =x1,...,X j =xj such that
the following procedure samples from P↑.
Sample X1 fromQ∅.
Recursively, conditional on X1 =x1,...,X j =xj, sample Xj+1 fromQx1,...,xj .
In the case where S is ﬁnite, let R denote the random set {X1,...,X n}. Then the law Qx1,...,xj is
equal to 1/(k −j) times the conditional intensity measure of R \ {x1,...,x j} given x1,...,x j ∈R.
Proof: Any standard Borel space admits regular conditional distributions [Dur04, Theorem 4.1.6].
The sampling algorithm essentially restates the deﬁnition of regular c onditional probabilities for
sequential sampling. Because P↑ is exchangeable, conditioning on Xi1 =x1,...,X ij =xj gives the
same exchangeable measure on the sequence of remaining elements of R for any i1,...,i j. Thus for
anyx other than x1,...,x j, we have
P(x ∈R |x1 ∈R,...,x j ∈R) = (k −j)P(Xj+1 =x |X1 =x1,...,X j =xj)
which is the ﬁnal conclusion. □
Remark. In the case of a measures on a ﬁnite set of size n, the main point of this sampling scheme
is to sample in k steps rather than n steps, so as better to control the Azuma martingale. But also,
sequential conditioning on x ∈ R can be easy to compute. For example, conditioning on an edge
being in a spanning tree replaces the original graph by a contraction along that edge.
Intuitively, there is a stochastic covering property for point proc esses deﬁned to hold when
conditioning on the presence of a point depresses the process eve rywhere else but by at most one
point. To make this deﬁnition precise begin by extending the notion of one measure stochastically
covering another to point processes. We say the point process Z stochastically covers the point
process W if there is a coupling of these two laws on counting measures support ed on pairs ( µ,ν )
such that µ =ν or µ =ν +δx for some x. Metrizing the space of ﬁnite counting measures on S by
the total variation distance, we see as before that if Z⊲ W then d∞(L(Z), L(W)) ≤ 1.
Next, given a k-homogeneous point process Z on a space S, we let Zx1,...,xj denote the (k −j)-
homogeneous point process whose law is the law of {Xj+1,...,X k} when sampling according to the
procedure in Lemma 3.3 conditional on X1 =x1,...,X j =xj. The k-homogeneous point process Z
is said to have the stochastic covering property if
Zx1,...,xj ⊲ Zx1,...,xj+1
for all choices of x1,...,x j+1. Note that the left-hand side is ( k −j)-homogeneous while the right-
hand side is ( k −j − 1)-homogeneous.
7
Theorem 3.4. Let Z be a k-homogeneous point process on a standard Borel space S and let f be
a Lipschitz-1 function (with respect to the total variation distance) on counting measures with total
mass k on Rd. If Z has the SCP, then
P(f − Ef ≥a) ≤ exp
(
−a2
8k
)
.
For point processes that are not homogeneous, as in the discrete case, we require more than the
SCP. Rather than deﬁning a notion of strong Rayleigh here, we will st ick to the case of determinantal
point processes, this being where all of our examples arise; see Sec tion 6 for deﬁnitions.
Theorem 3.5. Let Z be a determinantal point process with EN =µ <∞. Let f be a Lipschitz-1
function on ﬁnite counting measures. Then
P(f − Ef ≥a) ≤ 3 exp
(
− a2
16(a + 2µ)
)
;
P(|f − Ef ≥a) ≤ 5 exp
(
− a2
16(a + 2µ)
)
.
