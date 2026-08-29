---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-028-84-third-cumulant-of-the-number-of-blocks-in-uni
section_title: "Third cumulant of the number of blocks in uniform set-partitions"
section_number: 8.4
pages: 68-69
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
Let Bn be the number of set-partitions of[n], known as then-th Bell number. Dobinski’s
formula states thatBn = e−1 ∑∞
k=0 kn/k!, which allows us to consider a random variable
M with the following distribution:
P[M = k] = 1
eBn
kn
k! .
An easy observation, useful below, is that E[Mr] = Bn+r/Bn. As above, we denote Xn
the number of blocks in a uniform set-partition of size [n]. We also consider a Poisson
variable P of parameter 1, independent from Xn. Stam [Sta83] proved the following
relation (with a very nice probabilistic explanation).
Lemma 8.4. [Sta83, Theorem 2] We have the following equality of random variables in law:
M law= Xn + P.
Therefore, κ(3)(M) = κ(3)(Xn) + κ(3)(P). But κ(3)(P) = 1 is a constant (independent
of n), whose value will not be relevant for the asymptotic of κ(3)(Xn). Let us consider
κ(3)(M). It is given by:
κ(3)(M) = E[M3]− 3 E[M2]E[M] + 2(E[M])3 = Bn+3
Bn
− 3 Bn+2 Bn+1
(Bn)2 + 2 (Bn+1)3
(Bn)3 .
In order to ﬁnd the asymptotic of the above formula, we use the following estimate
for Bell numbers. This is a variant of the Moser-Wyman formula [MW55], that can be
found in an unpublished note of Mohr [Moh95].
Lemma 8.5. Let αn be the positive real number deﬁned by the equation αn eαn = n; in partic-
ular αn = (log n) (1− o(1)). Then, one has, for any integer r,
Bn+r = (n + r)!
(αn)n+r
exp(eαn− 1)√
2πβ n
×
(
1 + P0 + rP1 + r2P2
eαn
+ Q0 + rQ1 + r2Q2 + r3Q3 + r4Q4
e2αn
+ O(e−3αn)
)
,
where βn = (( αn)2 + αn) eαn, and the Pi’s and Qi’s are explicit rational functions ofαn, with
Pi = O((αn)−i) and Qi = O((αn)−i).
MOD-φ CONVERGENCE, I 69
This lemma yields an estimate for quotients of Bell numbers (we substitute e αn by
n/αn):
(αn)r Bn+r
Bn
= (n + 1)··· (n + r)
(
1 + αn
rP1 + r2P2
n
+(αn)2−P0(rP1 + r2P2) + rQ1 + r2Q2 + r3Q3 + r4Q4
n2 + O(α3
n/n3)
)
Consider the expression
k3 := α3
n
( Bn+3
Bn
− 3 Bn+2 Bn+1
B2n
+ 2 (Bn+1)3
(Bn)3
)
.
With the help of a computer algebra program, we ﬁnd
k3 = n
(
(−6 P2 (P1 + P2) + 6 Q3 + 36 Q4)(αn)2 + 12P2 αn + 2
)
+ O((αn)3).
From the estimate Pi = O((αn)−i) and Qi = O((αn)−i), we see that the dominant term
in k3 comes from the constant 2 in the above equation. Namely,
k3 = 2n + O
( n
αn
)
, that is κ(3)(Xn) = 2n
(αn)3 + O
( n
(αn)4
)
,
as claimed in the previous subsection.
9. D EPENDENCY GRAPHS AND MOD -GAUSSIAN CONVERGENCE
Dependency graphs are a classical tool in the literature to prove convergence in dis-
tribution towards a Gaussian law of the sum of partly dependent random variables.
They are used in various domains, such as random graphs [JŁR00, pages 147-152],
random polytopes [IV07], patterns in random permutations [Bón10]. As dependency
graphs give a natural framework to deal in a uniform way with different kinds of ob-
jects, a natural question is the following: when we have a dependency graph with good
properties, can we obtain more precise or other results than convergence in distribu-
tion? Here is a brief presentation of the literature around this question.
• In [BR89], P . Baldi and Y. Rinott give precise estimates for the total variation
distance between the relevant sequence of random variables and the Gaussian
distribution.
• In [Jan04], S. Janson has established some large deviation result involving the
fractional chromatic number of the dependency graph.
• More recently, H. Döring and P . Eichelsbacher have shown how dependency
graphs can be used to obtain some moderate deviation principles [DE13b, Sec-
tion 2].
