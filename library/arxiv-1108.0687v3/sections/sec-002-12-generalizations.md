---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-002-12-generalizations
section_title: "Generalizations"
section_number: 1.2
pages: 3-4
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
---
Our aim is to generalize (1.1) or its Poissonian version (1.3) in two ways. Instead of Sn we consider
arbitrary Lipschitz functions of X1,...,X n, and instead of independent Bernoullis we consider a
more general negatively dependent collection of binary random var iables. We will give a number of
applications, but before this, we brieﬂy discuss what is known about each of the two generalizations
separately.
For the ﬁrst generalization, let Bn denote the rank-n Boolean lattice {0, 1}n and let f : Bn → R
be Lipschitz with respect to the Hamming distance. Replacing f byf/c if necessary, we will lose no
generality in assuming our Lipschitz functions to have Lipschitz cons tant 1, and we do so hereafter;
thus |f (x) −f (x′)| ≤ 1 whenever x and x′ are two strings diﬀering in only one position. When P is
a product measure, a well known generalization of (1.1) [McD89] is
P(f − Ef ≥a) ≤e−2a2/n. (1.4)
For the second generalization, we say that a collection of random va riables {Xj} in {0, 1} is
negative cylinder dependent if
P(Xj = 1 for all j ∈S) ≤
∏
j∈S
pj (1.5)
and
P(Xj = 0 for all j ∈S) ≤
∏
j∈S
(1 −pj). (1.6)
Negative cylinder dependence implies the inequalities (1.1)–(1.2) (see , e.g., [PS97, Theorem 3.4]
with λ = 1). Lyons [Lyo03, Section 6] lists extensions and applications includ ing one to balls in
bins [DR98] and one to determinantal measures [Sos00].
It is not known whether these two generalizations can be combined. The random variables
{Xj : 1 ≤ j ≤ n} are said to be negatively associated if Efg ≤ (Ef )(Eg) for every pair f,g of
increasing functions on {0, 1}n such that f (X1,...,X n) depends only on the values {Xi : i ∈ S}
and g(X1,...,X n) depends only on the values {Xi : i /∈ S}, for some subset S ⊆ { 1,...,n }. By
induction, this implies the weaker property of negative cylinder depe ndence. E. Mossel (personal
communication, 2009) asked us whether the following holds.
Conjecture 1.2. Let X1,...,X n be negatively associated binary-valued random variables. Let f :
{0, 1}n → R be Lipschitz-1 and denote fn := f (X1,...,X n). Then (1.4) holds with the bound
exp(−2a2/n) replaced by c0 exp(−ca 2/n) for some positive constants c0 and c.
To see why the exponent must be weakened consider the example of Bernoulli random variables
X1,...,X n with n even, {X1,...,X n/2} independent with mean 1 /2, and Xn/2+j = 1 −Xj for
2
1 ≤ j ≤ n/2. These are negatively associated and yet the Lipschitz-1 functio n f := ∑ n/2
j=1Xj −∑ n
j=n/2+1Xj has tail probabilities on the order of e−a2/n. It is possible that this is the worst example
and that the conjecture holds with c = 1, but a resolution of the conjecture would be interesting
even without the optimal value of c. A recent paper [Far08] appears to settle this conjecture and
more, but the relevant result in that paper, Theorem 2, is not corr ect, the proof therein failing at
equation (6).
Recent investigations of negative dependence properties indicate that negative association may
not be suﬃciently robust to use as a hypothesis in this context. The problem was posed in [Pem00] to
ﬁnd a more useful negative dependence property; this was answe red in [BBL09], who showed that the
strong Rayleigh property implies negative association and many other desirable consequences ,
and is stable under probabilistic operations such as conditioning, sym metrizing and reweighting.
Our main result implies that Conjecture 1.2 holds with c = 1 /8 if one assumes the strong
Rayleigh property rather than just negative association. The str ong Rayleigh property is known
to hold for most standard examples in which negative association is kn own to hold, so this gives
up little generality, and moreover the strong Rayleigh property is us ually easier to check than is
negative association. Indeed for some of the measures described below, the only way we know they
are negatively associated is by establishing the strong Rayleigh prop erty. Several classes of measures
satisfying the strong Rayleigh property are:
• Determinantal measures and point processes;
• Bernoullis conditioned on the sum;
• Measures obtained by running exclusion dynamics from a determinist ic starting state (or more
generally, exclusion with birth and death).
An overview of the rest of the paper is as follows. In the next sectio n we introduce the strong
Rayleigh property and discuss its consequences. One important co nsequence for us will be the
stochastic covering property , which is all we use to derive our basic concentration inequality.
In Section 3 we state our results, and these are proved in Section 4 . Section 5 contains a number of
applications.
