---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-002-3-power-sums-of-eigenvalues
section_title: "Power sums of eigenvalues"
section_number: 3
pages: 5-7
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
We now develop some results relatingλ1 to the power sum of P ’s eigenvalues. We assume throughout this
section thatP is non-negative and trace-class (compact with summable eigenvalues). For any positive integer
k, let
sk =
κ∑
i=0
λk
i ,
and deﬁne s0 to be inﬁnity. The ﬁrst power sum, s1, is the trace norm of P (see e.g. Conway, 1990, 2000),
while√s2 is the Hilbert-Schmidt norm of P. ThatP is trace-class impliess1 <∞, and it’s clear thatsk is
decreasing ink.
The magnitude ofsk is directly related to the convergence behavior of the chain. For instance, suppose
that the chain starts at a point mass Φ0 =u, then the chi-square distance between the distribution of Φk and
the stationary distribution is given by (see e.g. Diaconis et al., 2008)
χ2
k(u) :=
∫
SU
(
p(k)(u,u′)−π(u′)
)2
π(u′) µ(du′) =
κ∑
i=1
λ2k
i |fi(u)|2,
wherefi :SU→ C is the normalized eigenfunction corresponding toλi. It follows that
s2k =
κ∑
i=1
λ2k
i =
∫
SU
χ2
k(u)π(u)µ(du),
5
which is the average ofχ2
k(u) underπ. More importantly, one can use functions ofsk to boundλ1, and thus
the spectral gap.
Observe that,
λ1≤uk := (sk− 1)1/k, ∀k∈ N.
Moreover, ifκ≥ 1, then it’s easy to show that
λ1≥lk := sk− 1
sk−1− 1, ∀k∈ N.
We now show that, in fact, these bounds are monotone ink and converge toλ1.
Proposition 1. Ask→∞ ,
uk↓λ1, (1)
and if furthermoreκ≥ 1,
lk↑λ1. (2)
Proof. We begin with (1). When κ = 0,s k≡ 1 and the conclusion follows. Suppose κ≥ 1, and that the
second largest eigenvalue is of multiplicitym, i.e.
1 =λ0>λ 1 =λ2 =··· =λm>λ m+1≥···≥ λκ> 0.
Ifκ = m, then sk− 1 = mλk
1 for all k≥ 1 and the proof is trivial. Suppose for the rest of the proof that
κ≥m + 1. For positive integerk, letrk =∑κ
i=m+1λk
i <∞. Thenrk > 0, and
rk+1
rk
≤λm+1<λ 1.
Hence,
lim
k→∞
rk
sk− 1−rk
= lim
k→∞
rk
mλk
1
≤ lim
k→∞
r1λk−1
m+1
mλk
1
= 0.
It follows that
loguk = logλ1 + 1
k logm + 1
k log(1 +o(1))→ logλ1.
Finally,
uk+1<λ 1/(k+1)
1
( κ∑
i=1
λk
i
)1/(k+1)
≤
( κ∑
i=1
λk
i
)1/[k(k+1)]( κ∑
i=1
λk
i
)1/(k+1)
=uk,
and (1) follows.
Now onto (2). We have already shown that
sk− 1 =mλk
1(1 +o(1)).
6
Thus,
lk = mλk
1(1 +o(1))
mλk−1
1 (1 +o(1))
→λ1.
To show thatlk is increasing ink, which would complete the proof, we only need note that
(sk+1− 1)(sk−1− 1) =
κ∑
i=1
λk+1
i
κ∑
j=1
λk−1
j
= 1
2
κ∑
i=1
κ∑
j=1
λk−1
i λk−1
j (λ2
i +λ2
j)
≥
κ∑
i=1
κ∑
j=1
λk
iλk
j
= (sk− 1)2.
Suppose now that we are interested in the convergence behavior of a particular Markov operator that
is known to be non-negative and trace-class. If it is possible to estimate sk, then Proposition 1 provides a
method of getting approximate bounds on λ1. When a DA Markov operator is trace-class, there is a nice
integral representation of sk that leads to a simple, classical Monte Carlo estimator of sk. In the following
section, we describe some theory for DA Markov operators, and in Section 5, we develop a classical Monte
Carlo estimator ofsk.
