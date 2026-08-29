---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-046-43-unbounded-random-variables-and-truncation-met
section_title: "Unbounded random variables and truncation methods"
section_number: 4.3
pages: 35-37
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
A possible generalization regards sums ofunbounded random variables. In the following, we develop a
truncation method that yields a criterion of asymptotic normality similar to Lyapunov’s condition (see
[Bil95, Chapter 27]). A small modiﬁcation of this method would similarly yield a Lindeberg type criterion.
Let Sn =∑Nn
i=1Ai,n be a sum of centered random variables, with
(
E[|Ai,n|2+δ]
) 1
2+δ
≤A
for some constantA independent ofi and n, and someδ >0. We suppose as before that the family of
random variables(Ai,n)i∈[ [1,Nn] ]has a (true) dependency graphGn of parametersNn and Dn. Note that
in this case,
Var(Sn) =
Nn∑
i,j=1
cov(Ai,n,Aj,n)≤
Nn∑
i=1
∑
j∼i
‖Ai,n‖2‖Aj,n‖2
≤
Nn∑
i=1
∑
j∼i
‖Ai,n‖2+δ‖Aj,n‖2+δ≤A2NnDn.
We set
A−
i,n =Ai,n 1|Ai,n|≤Ln ; A+
i,n =Ai,n 1|Ai,n|>Ln ;
S−
n =
Nn∑
i=1
A−
i,n ; S+
n =
Nn∑
i=1
A+
i,n ;
where Ln is a truncation level, to be chosen later. Notice thatGn is still a dependency graph for the
family of truncated random variables(A−
i,n)i∈[ [1,Nn] ]. Therefore, we can apply the previously developed
machinery (Theorem 34 and Corollary 30) to the scaled sumS−
n/Ln. On the other hand, by Markov’s
inequality,
dKol(Sn,S−
n ) = sup
s∈R
|P[Sn≥s]− P[S−
n ≥s]|≤ P[S+
n = 0]
≤
Nn∑
i=1
P[|Ai,n|≥ Ln]≤Nn
( A
Ln
)2+δ
.
Combining the two arguments leads to the following result (this replaces the previous assumption of
boundedness|Ai,n|≤ A).
Theorem 39.Let (Sn =∑Nn
i=1Ai,n)n∈N be a sum of centered random variables, with dependency graphs
of parametersNn→ +∞ and Dn, and with
36 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
‖Ai,n‖2+δ = (E[|Ai,n|2+δ])1/(2+δ)≤A
for alli,n and for someδ >0. We setYn =Sn/
√
Var(Sn). Recall that(~σn)2 = Var(Sn)
NnDn
.
(U1) Set
Vn = (~σn)2
(Nn
Dn
)1/3 1
(Nn)2/(2+δ)
and suppose thatlimn→∞Vn = +∞ (which is only possible forδ >4). Then, forn large enough,
dKol(Yn,NR(0, 1))≤ 78
(A2
Vn
)3(δ+2)
2(δ+5)
=o
( 1
Vn
)
.
(U2) More generally, forε∈ ( 2
2+δ, 1), set
Wn = (~σn)2
(Nn
Dn
)ε 1
(Nn)2/(2+δ)
and suppose thatlimn→∞Wn = +∞. Then,Yn ⇀NR(0, 1).
Remark 40.It should be noticed that ifδ→ +∞, then one essentially recovers the content of Corollary
30 (which can be applied because of Theorem 34). On the other hand, the inequalityδ > 4 amounts
to the existence of bounded moments of order strictly higher than6 for the random variablesAi,n. In
practice, one can for instance ask for bounded moments of order7 (i.e. δ = 5), in which case the ﬁrst
condition (U1) reads
lim
n→∞
Var(Sn)
DnNn
(Nn)1/9
(Dn)1/3 = +∞.
Moreover, we will see in the proof of Theorem 39 that in this setting (δ = 5), the constant 78 can be
improved to39, so that, forn large enough:
dKol(Yn,NR(0, 1))≤ 39
(A2
Vn
) 21
20
.
Proof. We write as usualYn = Sn√
Var(Sn)
, andY−
n = S−
n√
Var(S−
n )
. In all cases, we have
dKol(Yn,NR(0, 1))≤dKol(Sn,S−
n ) +dKol
(
Y−
n ,
√
Var(Sn)
Var(S−n )NR(0, 1)
)
≤Nn
( A
Ln
)2+δ
+dKol(Y−
n ,NR(0, 1)) +dKol
(
NR(0, 1),NR
(
0, Var(Sn)
Var(S−n )
))
by using the invariance of the Kolmogorov distance with respect to multiplication of random variables
by a positive constant. In the sequel, we denotea, b and c the three terms on the second line of the
inequality. The Kolmogorov distance between two Gaussian distributions is
dKol(NR(0, 1),NR(0,λ 2)) = 1√
2π sup
s∈R+
(∫ λs
s
e−u2
2 du
)
≤ λ− 1√
2π sup
s∈R+
(
s e−s2
2
)
=
√
1
2πe|λ− 1|
if λ≥ 1. One gets the same result ifλ≤ 1, hence,
Mod-φ convergence, II: Estimates on the speed of convergence 37
dKol
(
NR(0, 1),NR
(
0, Var(Sn)
Var(S−n )
))
=dKol
(
NR(0, 1),NR
(
0, Var(S−
n )
Var(Sn)
))
≤
√
1
2πe
⏐⏐⏐⏐⏐⏐
√
Var(S−n )
Var(Sn)− 1
⏐⏐⏐⏐⏐⏐
≤
√
1
2πe
|Var(S−
n )− Var(Sn)|
Var(Sn) .
To evaluate the diﬀerence between the variances, notice that
Var(S−
n ) = Var
(
Sn−
Nn∑
i=1
A+
i,n
)
= Var(Sn)− 2
Nn∑
i,j=1
Cov(A+
i,n,Aj,n) +
Nn∑
i,j=1
Cov(A+
i,n,A +
j,n)
Ifj is not connected toiinGn, or equal toi, thenAi,n andAj,n are independent, hence,Cov(A+
i,n,Aj,n) =
