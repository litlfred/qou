---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-008-33-main-result
section_title: "Main Result"
section_number: 3.3
pages: 41-47
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
Using these results, along with the method of Chatterjee and Ledoux, we are able to
prove the following result:
Theorem 3.3.1. Take any 1≤ k≤ n and an n-dimensional Hermitian matrix G.
LetA be the k×k matrix consisting of the ﬁrst k rows and k columns of the matrix
obtained by conjugating G by a rotation matrix Rθ
ij ∈ SO(n) chosen uniformly at
random. If we let F be the expected spectral distribution of A, then for each r >0,
P
(
‖FA−F‖∞≥ 1√
k
+r
)
≤ 12
√
k exp
(
−r
√
k
32
)
Proof. The proof of this theorem uses the method introduced by Chatterjee and
Ledoux [Chatterjee and Ledoux, 2009] with appropriate changes made to apply to
the situation we are considering.
LetRij(θ)∈ SO(n) and let A be as stated above. Note that since A is a compression
of a Hermitian operator, it will also be Hermitian. Fix x∈ R. Let f(A) := FA(x),
whereFA(x) is the empirical spectral distribution of A. Let Q be the transition oper-
ator as deﬁned in (1) and let |||.|||∞ be as in (2). Using Lemma 2.2 from [Bai, 1999],
33
we know that for any two Hermitian matrices A and B of order k,
‖FA−FB‖∞≤ rank(A−B)
k
In our case, taking one step in Kac’s walk is equivalent to rotation in a random
plane by a random angle. Hence A and Rθ
ijA will diﬀer in at most two rows and two
columns, bounding the diﬀerence in rank by 2, so
‖f(A)−f(Rθ
ijA)‖∞≤ 2
k
Using (2),
|||f|||2
∞ = 1
2
(n
2
) sup
A∈SO(n)
∑
1≤i<j≤n
E[f(A)−f(Rθ
ijA)]2
≤ 1
2
(2
k
)2(2k
n
)
= 4
kn
where the 2k
n comes from the probability that both i and j are greater than k, in
which case, A and Rθ
ijA will be the same. From Theorems 2.1 and 2.2, we have that
P(|FA(x)−F (x)|≥ r)≤ 6 exp

−r
2
√
1
2
n+2
(n−1)n
√
4
kn


= 6 exp
(
−r/2
√
1
8
k(n + 2)
n− 1
)
≤ 6 exp
(
−r/2
√
k
8
)
This is true for any x. Now, if we let FA(x−) := lim y↑xFA(y), then we have
EFA(x−) = limy↑xF (y) =F (x−). Hence, for r >0,
P(|FA(x−)− EFA(x−)|>r )≤ lim
y↑x
P(|FA(y)−F (y)|>r )
≤ 6 exp
(
−r/2
√
k
8
)
34
This holds for allr, so we can replace> by≥. Next we will ﬁx𝓁∈ Z≥2. For 1≤i<𝓁 ,
let
ti := inf{x :F (x)≥i/𝓁}
and t0 =−∞, t𝓁 =∞. Then for each i, F (ti+1)−F (ti)≤ 1/𝓁. Let
∆ = (max
1≤i<𝓁
|FA(ti)−F (ti)|)∧ (max
1≤i<𝓁
|FA(ti−)−F (ti−)|)
Take anyx∈ R. Let i be an index where ti≤x<t i+1. Then
FA(x)≤FA(ti+1−)≤F (ti+1−) +∆≤ F (x) + 1/𝓁 +∆
and
FA(x)≥FA(ti)≥F (ti)−∆≥ F (x)− 1/𝓁−∆
Using these two facts, we get that
‖FA−F‖∞≤ 1/𝓁 +∆
Then for any r >0, we have
P(‖FA−F‖∞≥ 1/𝓁 +r)≤ 12(𝓁− 1) exp
(
−r
√
k
32
)
Letting 𝓁 =k1/2 + 1, we have
P(‖FA−F‖∞≥ 1√
k
+r)≤ 12
√
k exp
(
−r
√
k
32
)
which concludes the proof of our theorem.
35
3.4 Kac’s Model Coupled to a Thermostat
Using a spectral gap result from [Bonetto et al., 2014], we are able to demonstrate the
application of this method to a more complicated Markov chain. In this system, the
particles from Kac’s system interact amongst themselves with a rate λ and interact
with a particle from a thermostat with rate µ. The particles in the thermostat are
Gaussian with variance 1
β, so they have already reached equilibrium. The Markov
transition operator for Kac’s walk is deﬁned as in (1) and the Markov transition
operator for the thermostat is given by
Rf(G) = 1
n
n∑
j=1
1
2π
∫ 2π
0
∫
Rn
√
β
2π
n
e−β
2ω∗2
ij (θ)f(Vj(θ,ω )G)dθdω (3.3)
whereω = (ω1,ω 2,...,ω n),Vj(θ,ω ) sends each elementgij in column j togijcos(θ) +
ωi sin(θ) fori = 1 ton andω∗
ij =−gij sin(θ)+ωi cos(θ). In [Bonetto et al., 2014], they
consider the Markov chain acting on a vector. We consider the Markov chain acting
on a matrix by treating the matrix as n independent vectors. Using this adaption,
the following theorem follows immediately from the results proved in [Bonetto et al.,
2014].
Theorem 3.4.1. Kac’s walk coupled to a thermostat has unique invariant measure
given by
νn =
∏
i,j
√
β
2πe−β
2v2
ij
and has spectral gap µ
2n
For the thermostat alone (lettingλ = 0), we can again prove a theorem analogous
to Chatterjee and Ledoux’s theorem 3.3. Let G be the set of n×n matrices with
independent and identically distributedN (0, 1/β) entries. We can deﬁne the Dirichlet
36
form and the triple norm for the thermostat as
Q(f,f ) = 1
2n
n∑
j=1
1
2π
∫ 2π
0
∫
Rn
∫
G∈G
( β
2π
)n/2
e−β
2w∗2
ij (f(Vj(θ,w ))G−f(G))dνndwdθ
|||f|||2
∞ = sup
G∈G
1
2n
n∑
j=1
1
2π
∫ 2π
0
∫
Rn
( β
2π
)n/2
e−β
2w∗2
j|f(Vj(θ,w ))G−f(G)|2dwdθ
(3.4)
Using these, we can prove a concentration of measure result for the thermostat anal-
ogous to Theorem 3.2.2
Theorem 3.4.2. Consider the Gaussian thermostat and let F :G→ R be such that
|||F|||∞≤ 1. Then F is integrable with respect to νn and for every r≥ 0,
νn(F≥Fdνn +r)≤ 3e−r√λ1/2
whereλ1 = µ
2n is the spectral gap of the thermostat process.
We omit the proof here as it is similar to the proof of Theorem 3.2.2.
Using this result and Theorem 3.4.1, we can prove the following concentration of
measure inequality.
Theorem 3.4.3. Take any 1≤ k≤ n and an n-dimensional Hermitian matrix G.
LetS be an n×k matrix whose k columns are the ﬁrst k columns of a random matrix
with distribution νn. Let A be the k×k matrix obtained by conjugating G by S.
LettingF denote the expected spectral distribution of A, then for each r >0,
P(‖FA−F‖∞≥ 1√
k
+r)≤ 12
√
k exp
(
−r
√
kµ
108
)
whereµ is the rate of the interaction with the thermostat.
37
Proof. The proof of this theorem closely follows the proof of Theorem 3.3.1, with
appropriate changes made. Let A be stated as above, and let A′ be A after one
step of the Markov chain. Fix x∈ R and let f(x) = FA(x), where where FA is the
empirical spectral distribution of A. Notice that rank( A−A′)≤ 3, since after one
step of the chain, at most 3 columns of A will be changed (two from Kac’s Walk, and
one from the thermostat). Again using the inequality from [Bai, 1999], we know that
‖f(A)−f(A′)‖∞≤ 3
k
|||f|||2
∞ = 1
2
(n
2
)
n sup
A
∑
1≤i<j≤n
n∑
k=1
E|f(A)−f(A′)|2
where the ﬁrst sum is over possible interactions in Kac’s process and the second is
over possible particle interactions with the thermostat. The above is
≤ 1
2
(3
k
)2(3k
n
)
= 27
2kn
Using theorems 3.4.1 and 3.4.2, we have that
P(|FA(x)−F (x)|≥ r)≤ 6 exp
(
−r
2
√
µ
2n
27
2kn
)
= 6 exp
(
−r
2
√
kµ
27
)
Following the rest of the proof in 3.2.1 (with the appropriate numbers changed), we
get
P(‖FA−F‖∞≥ 1√
k
+r)≤ 12
√
k exp
(
−r
√
kµ
108
)
38
