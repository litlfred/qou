---
doc_id: arxiv-1105.0091v1
doc_title: "E-mail: meliot@phare.normalesup.org"
section_id: sec-004-6-pitman-operators-and-a-link-with-conditioned-r
section_title: "Pitman operators and a link with conditioned random walks and brownian matrices"
section_number: 6
pages: 42-57
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
doc_brief: "E-mail: meliot@phare.normalesup.org — In this paper, we review the representation theory of the inﬁnite symmetric group, and we extend the works of Kerov and Vershik by proving that the irreducible"
---
brownian matrices
In the previous paragraphs, we have shown that the rows and columns
of a partitionλ of law Pn,ω have limit frequenciesαi and βj, and gaussian
ﬂuctuations when gathered for equal coordinates of the pointω of the Thoma
simplex. To treat the case of equal parameters, we shall use O’Connell’s theory
([O’C03]) that relates the Robinson-Schensted algorithm to an operation on
multidimensionalpaths,andthereforerandomtableauxcomingfrom ω-shuﬄes
to random walks conditioned to stay in a Weyl chamber. These random walks
are also related to the processes of eigenvalues of brownian traceless Hermitian
matrices. Thus, the ﬂuctuations of a block ofd rows or columns corresponding
to equal coordinates ofω are the same as those of the eigenvalues of a gaussian
matrix in su(d, C), up to the additional gaussian term described by Theorem
19; see Theorem 25 for a precise statement. We shall prove this progressively,
starting from the toy model of2-shuﬄes, then introducingPitman operators
in order to treat the case ofd-shuﬄes, and ﬁnally studying the general case.
6.1 The case of2-shuﬄes
To begin with, let us treat minutely the case when
ω =
(( 1
2, 1
2, 0, 0,...
)
, (0, 0,... )
)
.
The correspondingω-shuﬄes (which we shall call2-shuﬄes) are easy to de-
scribe. Indeed, for anyn, a random permutation of lawQn,ω can be obtained
by shuﬄing together two blocks of sizen1 andn2 =n−n1 withn1∼B (n, 1
2 ),
that is to say that
P[n1 =k] = 1
2n
(n
k
)
.
Werecallthatallthe
(n
k
)
shuﬄesoftwoblocksofsizes k andn−k areequiprob-
able. Thus, ifb1,...,b n are independent identically distributed variables with
P[bi = 1] = P[bi = 2] = 1/2, then one can produce a permutation of lawQn,ω
by:
–setting n1 = card{i| bi = 1}, n2 = card{i| bi = 2}.
–sending the integers of [ [1,n 1] ]in this order to the positionsi such that
bi = 1, and then sending the integers of[ [n1 + 1,n 1 +n2] ]in this order to
the positionsi such thatbi = 2.
For instance, if the sequence of Bernoulli variables is 121121221, then the
corresponding permutation7 will be 162374895. This explicit construction of
2-shuﬄes will enable us to relate them to random walks — here, the random
walk that we shall consider is:
7 With the vocabulary of §2,σ is the standardization of the word whose letters are the
Bernoulli variables.
A central limit theorem for the characters ofS∞ and H (S∞) 43
5
Fig. 5 Random walk associated to the2-shuﬄe 162374895 = Std(121121221).
Given a permutation σ obtained by standardization from a word w in
{1, 2}∗, the shape of the tableauP (σ) is the same as the shape of the tableau
P (w). Actually, for anyk≤ n, ifPk(σ) (respectively, Pk(w)) is the tableau
obtained after Schensted insertion of thek ﬁrst letters ofσ (resp., of thek ﬁrst
letters ofw), thenPk(σ) has the same shape asPk(w). Hence, we will study
the random process (P (wk))k≥0, wherewk = b1b2...b k is a random word in
{1, 2}k with independent Bernoulli letters. This process takes its values in
SST{1, 2} ={semi-standard tableaux with entries in{1, 2}}.
A semi-standard tableau with entries in{1, 2} has at most two rows, and the
entries in the second row are all equal to2. Thus, if one knows the sizen of
the tableau, then it is entirely determined by the numberm11 of entries 1 on
the ﬁrst row, and by the numberm12 of entries 2 on the ﬁrst row:
m11 “1” m12 “2”
m22 “2”
6
with m22 = n−m11−m12. So, let us study in detail the random process
(m11(k),m 12(k)). For this purpose, we introduce the random walkXk = 3k−
2(b1 +b2 +··· +bk); this is a standard random walk onZ, starting from0.
Lemma 20. For any k, m11(k) = k+Xk
2 and m12(k) = Sk− Xk, where
Sk = supj≤kXj.
Proof. Thequantity m11(k)isjustthenumberof“ 1” inthesequenceb1,...,b k.
Hence,
m11(k) =
k∑
i=1
2−bi = 2k− (b1 +b2 +··· +bk) = k +Xk
2 .
As form12(k), let us prove the result by induction onk. Supposingm12(k) =
Sk−Xk, let us computem12(k + 1):
44 Pierre-Loïc Méliot
1. Ifbk+1 = 1, one inserts a letter1 in the ﬁrst row. Suppose thatm12(k) = 0.
Then, m12(k + 1) is also equal to 0, so Sk = Xk, and Xk+1 = Xk + 1,
because bk+1 = 1 means that we go up. This implies thatSk+1 =Xk+1, so
m12(k + 1) = 0 = Sk+1−Xk+1. On the contrary, suppose thatm12(k)≥ 1.
Then, the letter1 will replace a letter2, so
m12(k + 1) = m12(k)− 1 = Sk−Xk− 1.
On the other hand, sinceXk =Sk−m12(k)≤Sk−1,Xk+1 =Xk +1≤Sk,
so Sk = Sk+1. But then,m12(k + 1) = Sk− (Xk + 1) = Sk+1−Xk+1, so
the identity holds again at rankk + 1.
2. If bk+1 = 2, one inserts a letter2 at the end of the ﬁrst row, so
m12(k + 1) = m12(k) + 1 = Sk−Xk + 1.
On the other hand,bk+1 = 2 means that the random walk goes down, so
Xk+1 = Xk− 1 and Sk = Sk+1. Then, m12(k + 1) = Sk− (Xk− 1) =
Sk+1−Xk+1.
Hence, if𝓁k(σ) is the length of the longest increasing subword ofσ(1)··· σ(k),
then
𝓁k(σ) = m11(k) +m12(k) = k
2 + 2Sk−Xk
2 ,
and this for anyk≤n.
It is known since Pitman’s works (see [Pit75]) that if(Xk)k∈N is a standard
random walk onZ, then(2Sk−Xk)k∈N is a markovian random process on the
non-negative integers, with
p(k,k + 1) = k + 2
2(k + 1) ; p(k,k− 1) = k
2(k + 1).
After scaling byn on thex-axis and√n on they-axis, the random process
(2Sk−Xk)k∈[ [0,n] ]converges in law inC ([0, 1]) to a 3-dimensional Bessel
process (BES3
t )t∈[0,1], whose trajectorial laws are the same as(2St−Bt)t∈[0,1],
with (Bt)t∈[0,1] standard brownian motion andSt = sups≤tBs. Alternatively,
(BES3
t )t∈[0,1] can be deﬁned as the solution of the stochastic diﬀerential equa-
tion
dYt =dBt + dt
Yt
,
see [RY91, Chapter 6, §3]. For this reason, and using Itô’s calculus, one can
show that (BES3
t )t∈[0,1] has the same trajectorial laws as the euclidian norm
(
√
X 2
t +Y 2
t +Z 2
t )t∈[0,1] of a 3-dimensional brownian motion. In particular,
this allows to compute the density of the law ofBES3
t:
BES3
t∼ 1y≥0
√
2
πt 3 y2 e−y2
2t dy.
A central limit theorem for the characters ofS∞ and H (S∞) 45
With these classical results from probability, Lemma 20 can be reinterpreted
as follows:
Proposition 21. Letσ be a random permutation obtained by a2-shuﬄe. We
denote
L(n)
t∈[0,1[ = 2√n
([
(⌊nt + 1⌋− nt)𝓁⌊nt⌋(σ) + (nt−⌊nt⌋)𝓁⌊nt⌋+1(σ)
]
− nt
2
)
the random process obtained by renormalization and interpolation of the pro-
cess (𝓁k(σ)− k
2 )k∈[ [0,n] ]. Asn goes to inﬁnity,(L(n)
t )t∈[0,1] converges in law8 in
C ([0, 1]) to a 3-dimensional Bessel process(BES3
t )t∈[0,1] (see Figure 6).
t
BES3
t
7
Fig. 6 A trajectory of the3-dimensional Bessel process.
In particular,
𝓁(σ) = λ1 = n
2 +
√n
2 Y +o
(√n
)
, with Y ∼ BES3
1∼ 1y≥0
√
2
πy2 e−y2
2 dy.
To conclude this paragraph, let us give yet another representation of the
3-dimensional Bessel process. We denote by su(2, C) the space of traceless
hermitian matrices of size2× 2. An element ofsu(2, C) can be written as
M =
( m1 m2 + im3
m2− im3 −m1
)
,
8 As usual, the interpolation is only needed in order to work inC ([0, 1]); if one uses instead
step càdlàg functions, one has the same result of convergence, but this time in Skorohod’s
space D([0, 1]), see [Bil69, Chapter 3, §14].
46 Pierre-Loïc Méliot
and su(2, C) is an euclidian space for the scalar product⟨A|B⟩ = trAB∗ =
2(a1b1 +a2b2 +a3b3). A brownian motion insu(2, C) is a continuous gaussian
process (Mt)t∈R+ starting from the null matrix, and with covariances
E[tr((AMs)(BMt)∗)] = K (s∧t) tr(AB∗).
For instance, ifX,Y,Z are three independent brownian motions inR, then
( Xt Yt + iZt
Yt− iZt −Xt
)
is a brownian motion insu(2, C), withK = 3. Now, the eigenvalues of such
a matrix brownian motion are±
√
X 2
t +Y 2
t +Z 2
t, so they are described by a
3-dimensional Bessel process. Hence, Proposition 21 can be restated as follows:
if λ = (λ1,λ 2) is a random partition of lawPn,ω with ω = ((1/2, 1/2), (0)),
then
2√n
(
λ1− n
2,λ 2− n
2
)
≃n→∞ (x1,x 2),
where x1≥x2 are the two eigenvalues of a brownian matrix insu(2) at time
t = 1. This is the good formulation of Proposition 21 for a generalization to
the case ofd-shuﬄes.
6.2 The case ofd-shuﬄes
Withasimilarframeworkasbefore,wewanttounderstandtheasymptotics
of d-shuﬄes, meaning that we consider the case when
ω =
(( 1
d, 1
d,..., 1
d, 0, 0,...
)
, (0)
)
,
with d coordinates equal to 1
d in α. A generalization of the arguments of the
previous paragraph to the case ofd-shuﬄes has been proposed by N. O’Connell
in [O’C03], in connection with previous results from [OY02]. Let us denote by
Πd the set of pathsW : N→ Nd, such thatW (0) = (0, 0,..., 0) and
W (k + 1)−W (k)∈{ 0,e 1,e 2,...,e d}
for anyk, whereei = (0 1, 02,..., 1i,..., 0d). Ifw is a word in{1, 2,...,d }∗ of
length n, we associate to it a path(W (k))k≤n in Πd, with
W (k + 1)−W (k) = ei if wk =i.
Now, for any pair of sequences(x(k))k∈N and (y(k))k∈N in Π1, we deﬁne two
new sequences
(xy)(k) = min{x(j)−y(j) +y(k)}j≤k;
(xy)(k) = max{x(j)−y(j) +y(k)}j≤k.
A central limit theorem for the characters ofS∞ and H (S∞) 47
Notice that the rules and  are not associative. In the following, we will use
the following convention:xyz = (xy)z and xyz = (xy)z. We
then deﬁne operatorsDd :Πd→Πd and Td :Πd→Πd−1:
Dd(x1,...,x d) = (x1,x 1x2,x 1x2x3,...,x 1x2··· xd);
Td(x1,...,x d) = (x2x1,x 3 (x1x2),...,x d (x1x2··· xd−1)).
Finally, from a path W in Πd, we deﬁne new pathsDiW ∈ Πd−i+1 and
TiW∈Πd−i by the recursive rule
D1W =Dd(W1,W 2,...,W d) ; T 1W =Td(W1,...,W d)
Di+1W =Dd−i(TiW ) ; Ti+1W =Td−i(TiW ).
For any pathW, the family(D1W,D 2W,...,D dW ) is a sequence of triangular
arrays. The link between this construction and the RSK algorithm is given by
the following result of O’Connell:
Theorem 22. For any wordw∈{ 1, 2,...,d }n, the semi-standard tableau of
size n obtained fromw by Schensted insertion is
m11 “1” m12 “2” ··· m1d “d”
m22 “2” m23 “3” m2d “d”···
... ...
8
where9 mij = (Dj−i+1W )i(n)− (Dj−iW )i(n) for any 1≤i≤j≤d, W being
the path associated to the wordw. In particular, for anyk ≤ n, the shape
(λ1,λ 2,...,λ d) of Pk(w) is
(
(DdW )1(k), (Dd−1W )2(k),..., (D1W )d(k)
)
.
We refer to [O’C03, Theorem 3.1] for a proof of this important result. Now,
we have to understand the transformation
Gd :Πd→Πd
W↦→
(
(DdW )1, (Dd−1W )2,..., (D1W )d
)
,
and what is the law ofGd(W ) when W is a random path inNd associated
to a random word in{1, 2,...,d }∗. To begin with, we shall notice that the
operators  and  also make sense for any continuous or càdlàg functionsx(t)
and y(t). Thus, we can deﬁne operators
Dd : C0(R+, Rd)→ C0(R+, Rd)
Td : C0(R+, Rd)→ C0(R+, Rd−1)
Gd : C0(R+, Rd)→ C0(R+, Rd)
9 By convention,D0W = (0, 0,..., 0) for any pathW, somii = (D1W )i(n) for anyi.
48 Pierre-Loïc Méliot
where C0(R+, Rd) denotes the set of continuous functionsw(t) from R+ to Rd,
withw(0) = (0, 0,..., 0). Moreover,Gd has the following property, see [O’C03,
Lemma 2.2]: for any pathw∈ C0(R+, Rd) and any timet∈ R+,
w1(t) +w2(t) +··· +wd(t) = (Gdw)1(t) + (Gdw)2(t) +··· + (Gdw)d(t).
In particular,Gd stabilizes the subspaceC0(R+,H )⊂ C0(R+, Rd) of functions
taking their values in the hyperplane
H ={(x1,x 2,...,x d)| x1 +x2 +··· +xd = 0}.
On the other hand, for anyx,y,f functions in C0(R+, R), one has
(x +f ) (y +f ) = (xy) +f ; ( x +f ) (y +f ) = (xy) +f.
This implies immediately that:
Gd(x1 +f,x 2 +f,...,x d +f ) = Gd(x1,x 2,...,x d) + (f,f,...,f ).
In particular, setf = x1+x2+···+xd
d . Then,
Gd(x1,x 2,...,x d) = (f,f,...,f ) +Gd(x1−f,x 2−f,...,x d−f ),
and the last term is a function inC0(R+,H ); hence, it suﬃces to study the
restriction ofGd to the subspaceC0(R+,H ).
The operatorsGd are better understood in terms of thePitman trans-
forms attached to a root system (cf. [BBO05]). The hyperplane H ⊂ Rd
contains a root system of typeAd−1, whose simple roots are e1−e2,e 2−
e3,...,e d−1−ed. To each simple rootδi = ei−ei+1, we attach an operator
Pi : C0(R+, Rd)→ C0(R+, Rd), deﬁned by the following formula:
(Piw)(t) = w(t)− (min{⟨δi|w(s)⟩}s≤t) δi.
Notice that eachPi stabilizes the subspaceC0(R+,H ). In [BBO05], it is shown
that the operatorsPi satisfy the braid relations of the generatorssi = (i,i− 1)
of the Coxeter groupSd:
∀i≤d− 2, PiPi+1Pi =Pi+1PiPi+1;
∀i,j ≤d− 1, |i−j|≥ 2⇒PiPj =PjPi.
It enables us to deﬁnePσ for any σ ∈ Sd, and it is not hard to see that
Pσ|C0(R+,H) takes its values in
C0
(
R+,
⋂
si∈Lσ
H +
i
)
,
where Lσ ={si| 𝓁(siσ) < 𝓁(σ)}, and H +
i ={x∈ H| ⟨δi|x⟩≥ 0} — cf.
[BBO05, Proposition 2.8]. In particular, ifω0 is the permutation of maximal
A central limit theorem for the characters ofS∞ and H (S∞) 49
length inSd, that is to say(d,d−1,..., 1), thenPω0|C0(R+,H) is an idempotent
operator taking its values in C0(R+,C ), where C = ⋂d−1
i=1 H +
i is the closed
Weyl chamber inH corresponding to the simple roots. In terms of coordinates,
notice thatx = (x1,...,x d) is inC if and only if
x1 +··· +xd = 0 and x1≥x2≥···≥ xd.
Now, ifφd
k is the projection (x1,...,x d)∈ Rd↦→ (x1,...,x k)∈ Rk, then it is
easily seen that
Td(W ) = φd
d−1Pd−1Pd−2··· P2P1(W );
TiW =φd
d−i (Pd−i··· P1) (Pd−i+1··· P1)··· (Pd−1··· P1)(W ).
From this, one sees thatGd =P1(P2P1)··· (Pd−1··· P1) = Pω0. In particular,
Gd|C0(R+,H) takes its values inC0(R+,C ), which was not clear from the ﬁrst
deﬁnition.
Then, let us consider the path W associated to a random word w ∈
{1, 2,...,d }∗, where each letter ofw is independent of the other letters, and
uniformly distributed on[ [1,d ] ]. If
~W (k) = W (k)−
(k
d,k
d,..., k
d
)
,
then~W lives in the hyperplaneH, and by (multi-dimensional) Donsker’s the-
orem (cf. [Bil69, Chapter 2]), after time-space scaling,~W converges to a brow-
nian motion (wt)t∈R in H, that is to say a continuous gaussian process inH
with covariances
E[⟨a|ws⟩⟨ b|wt⟩] = 1
d (s∧t)⟨a|b⟩.
Indeed, ifX is a random step~W (n+1)−~W (n), then⟨δi|X⟩equals 1ifX =ei,
−1 if X =ei+1, and 0 otherwise. From this, one sees thatE[⟨δi|X⟩⟨ δj|X⟩]
equals 2
d if i =j,− 1
d if i =j± 1, and 0 otherwise. But this is exactly⟨δi|δj⟩
d ,
whence the result after applying Donsker’s theorem.
Let us forget for the moment the factor1
d, and consider a standard brown-
ian motionw in H. Then, it can be shown thatPω0 (w) is a brownian motion
conditioned in Doob’s sense to stay in the Weyl chamberC, cf. [BBO05, The-
orem 5.6] or [Bia09]. We have drawn on Figure 7 a random walk inH⊂ R3
corresponding to a random word (in blue), and its image by Pitman’s trans-
formPω0 =P1P2P1 (inviolet);itapproximatesabrownianmotionconditioned
to stay in a Weyl chamber10.
10 On the drawing, it appears that an important part of the trajectory of the initial brow-
nian motion is simply translated by Pitman’s transformPω0. This observation can be made
precise, and one obtains a generalization of Williams’ decomposition of the trajectories of
the BES3 process, cf. [RY91, Chapter 6, Theorem 3.11].
50 Pierre-Loïc Méliot
9
Fig. 7 Action of Pitman’s transform on a brownian motion whend = 3.
This conditioned brownian motion is the Markov process onC with tran-
sition probabilities
qt(x,y ) = ∆(y)
∆(x)
∑
σ∈Sd
ε(σ)pt(x,σ (y))
wherept(x,y ) = (2πt)−d−1
2 exp
(
−‖x−y‖2
2t
)
is the transition kernel of the stan-
dard brownian motion inH, and
∆(x) =
∏
α positive root
⟨α|x⟩ =
∏
1≤i<j≤d
xi−xj
A central limit theorem for the characters ofS∞ and H (S∞) 51
is (up to a multiplicative constant) the unique positive function onC that
is harmonic with respect to the symmetrized kernel and that vanishes at the
boundary ofC. The singularity of the transition kernel atx = (0, 0,..., 0) is
solvable11, with
qt(0,y ) = ∆(y)2
1! 2!··· d− 1!t
d(d−1)
2
pt(0,y ).
This Markov process corresponds to the process of the eigenvalues
(xt,1≥xt,2≥···≥ xt,d)
of a brownian matrix insu(d, C) with covariances
E[tr((AMs)(BMt)∗)] = d2− 1
d (s∧t) tr(AB∗),
see [Dys62,Bia09], and [AGZ09, Theorem 2.5.2] for checking that the multi-
plicative constant is indeed d2−1
d . Taking account of the factor 1
d put aside
before, we get:
Theorem 23. In the following, (Mt)t∈R+ is a brownian matrix in su(d, C)
starting from the null matrix and with normalized covariances
E[tr((AMs)(BMt)∗)] = d2− 1
d2 (s∧t) tr(AB∗);
and (x1,t≥ x2,t≥···≥ xd,t) is the set of eigenvalues ofMt. On the other
hand, we consider a random permutationσ obtained by ad-shuﬄe, and we
denote
L(n)
i,t = 1√n
([
(⌊nt + 1⌋− nt)Λi,⌊nt⌋(σ) + (nt−⌊nt⌋)Λi,⌊nt⌋+1(σ)
]
− nt
d
)
,
where (Λ1,k(σ),...,Λ d,k(σ)) is the shape of the tableau Pk(σ) obtained by
Schensted insertion from thek ﬁrst letters ofσ. Asn goes to inﬁnity,
(
L(n)
1,t,L (n)
2,t,...,L (n)
d,t
)
t∈[0,1]
→ (x1,t,x 2,t,...,x d,t)t∈[0,1],
where the convergence is in law and takes place inC ([0, 1], Rd). In particular,
if λ∼ Pn,ω with ω = ((1/d, 1/d,..., 1/d), (0)), then12
λi = n
d +
√n
d Yi +o
(√n
)
with
(Y1,...,Y d)∼ 1y1≥y2≥···≥yd
y1+y2+···+yd=0
∆(y1,y 2,...,y d)2
1! 2!··· d− 1! (2π)
d−1
2
e−‖y‖2
2 dy.
11 This is easily seen by expanding termsexp(−‖ηi−xσ(i)‖2/2t) withη→ 0, and by using
the theory of antisymmetric polynomials, see [Mac95, §1.3].
12 Here, notice thatdy denotes the (d− 1)-dimensional Lebesgue measure onH.
52 Pierre-Loïc Méliot
6.3 The general case of equal coordinates
We pursue the study of the ﬂuctuations of rows of a tableau obtained by
Schensted insertion from a generalized shuﬄe, and we consider now the case
when ω = ((pd1
1 ,pd2
2 ,...,p dr
r ), (0)) with
p1 >p 2 >··· >p r > 0 and d1p1 +d2p2 +··· +drpr = 1.
Here, by pdi
i , we mean thatpi appears di times in α. It will be clear from
our reasoning that one could even consider an inﬁnite sequence ofpi’s with
the same property. So, if one understands the behaviour of rows with a ﬁnite
number of parameters, the study of the general case whenω = (α, 0) andγ = 0
will be completed. In the following, we setd =d1 +d2 +··· +dr.
As before, anω-shuﬄe of sizen corresponding to parameterspd1
1 ,...,p dr
r
can be obtained by standardizing a random wordw = b1b2...b n in [ [1,d ] ]n,
where the lettersbk are independent and of law
P[bk =i] = pj if d1 +··· +dj−1 + 1≤i≤d1 +··· +dj.
To such a (random) word, we attach as before a random walkW∈ Zd, with
W (k + 1)−W (k) = ei if bk = i. O’Connell’s Theorem 22 holds again, so
Gd(W )(k) is the form Λk(σ) of the tableau Pk(σ) (or Pk(w)) obtained by
Schensted insertion from thek ﬁrst letters ofσ. Now, we shall use the following
technical lemma:
Lemma 24. If W = (x1,...,x d) is a random walk obtained from a shuﬄe
of parameterpd1
1 ,...,p dr
r , we introduce random functionsf1,...,f d such that
(f1,...,f d) is the vector
Gd(x1,...,x d)− (Gd1 (x1,...,x d1 ),...,G dr (xd1+···+dr−1+1,...,x d1+···+dr )).
These functions are almost surely bounded (as functions ofN).
Example. Before proving Lemma 24, let us see study the simplest example
where it applies, namely, whenω = ((a, 1−a), (0)) witha> 1/2. The random
walk to consider is two dimensional and will be denotedwn = (xn,yn)n∈N;
moreover,
(G2w)n = (xn− min{xk−yk}k≤n,yn + min{xk−yk}k≤n).
However, (zn =xn−yn)n∈N is a random walk onZ with P[zn+1 =zn + 1] =a,
P[zn+1 =zn− 1] = 1−a, andz0 = 0 almost surely. It is well-known that such
a random walk is transient, with
P
[
inf
n∈N
zn≤−m
]
=
( 1−a
a
)m
P
[
min
n∈N
zn =−m
]
=
( 1−a
a
)m
−
( 1−a
a
)m+1
= 2a− 1
a
( 1−a
a
)m
.
Thus, (G2(x,y ))− (x,y ) = (−z,z ), with|z| almost surely bounded by a (ran-
dom) constant of expectation 1−a
2a−1.
A central limit theorem for the characters ofS∞ and H (S∞) 53
Proof of Lemma 24.The example above can be generalized by using the lan-
guage of Pitman operators: ifPi acts on the random walk withi =d1 +··· +dj
for somej∈ [ [1,r− 1] ], thenPiw diﬀers fromw by almost surely bounded func-
tions on the coordinates of indexd1 +··· +dj and d1 +··· +dj + 1. This is
exactly for the same reason: the diﬀerence of the two random walksxd1+···+dj
and xd1+···+dj +1 is almost surely bounded from below. Quite obviously, this
is also true if one replacesw by w +δ with δ almost surely bounded vector,
so one can use this argument several times. More generally, this works also
if w is replaced byPσ(w), whereσ is a permutation in the Young subgroup
Sd1× Sd2×···× Sdr⊂ Sd; indeed, such an operator won’t change the fact
that the coordinatesxd1+···+dj andxd1+···+dj +1 have diﬀerent rates of growth
to inﬁnity.
In the operatorGd = Pω0 = P1(P2P1)(P3P2P1)··· (Pd−1··· P1), it allows
to neglict all the factorsPi withi =d1 +··· +dj: they will simply modify the
random path by almost surely bounded functions. So,Gdw≃Jdw, whereJd
is obtained fromGd by deleting in the reduced decomposition ofω0 all thesi’s
with i =d1 +··· +dj, j∈ [ [1,r− 1] ]. Then,Jd acts separately on each block
of coordinatesxd1+···+dj−1+1,...,x d1+···+dj, and the action corresponding to
the block of sizedj is given by the operator
Gdj (Pdj−1··· P2P1)k,
where k = d−dj. Now, eachPi is an idempotent operator (this is almost
obvious from the deﬁnition given on page 48), and on the other hand, for any
i, there is a reduced decomposition ofω0 in Sdj that ends bysi. Hence,
Gdj (Pdj−1··· P2P1)k =Gdj,
whence the result.
Now, for each blockxd1+···+dj−1+1,...,x d1+···+dj, one can follow the same
reasoning as in the case ofd-shuﬄes, with some precaution. First, notice that
if gj = 1
dj
∑dj
i=1xd1+···+dj−1+i, then:
1. In Nr, (d1g1,...,d rgr) is a random walk of parameterd1p1,...,d rpr.
2. The vectors
~Wj = (xd1+···+dj−1+1−gj,...,x d1+···+dj−1+dj−gj)
withj∈ [ [1,r ] ]are random walks inH⊂ Rdj, and they are all independent,
and independent from the vector(d1g1,...,d rgr).
54 Pierre-Loïc Méliot
One takes account of the ﬁrst vector by the standard central limit theorem:
digi =n(dipi) +√nXi +o
(√n
)
where (X1,...,X r) is a gaussian vector of covariance matrix k(Xi,Xj) =
δijdipi−didjpipj. More precisely, one can describe asymptotically
(d1g1(k)−kd 1p1,...,d rgr(k)−kdrpr)k≤n
by using the multidimensional Donsker theorem. As for the vectors~Wj, they
can be studied with the framework of the previous paragraph ond-shuﬄles.
The only diﬀerence is the multiplicative constant in the covariances of the
brownian motion that is the limit of ~Wj after time-space scaling: it is pj
instead of 1
dj
. In the end, one obtains the following:
Theorem 25. With the same notations as before, we ﬁx independent brow-
nian motions (Mt,j)t∈R+,1≤j≤r taking values in the spacessu(dj, C), with co-
variances
E[tr((AMs,j)(BMt,j)∗)] = d2
j− 1
dj
pj (s∧t) tr(AB∗);
(x1,j,t ≥ x2,j,t ≥ ··· ≥xdj,j,t) will denote the set of eigenvalues of Mt,j.
We also consider an independent brownian motion(B1,t,...,B r,t) in Rd, with
covariances
E[⟨X|Bs⟩⟨ Y|Bt⟩] = (s∧t)XtQY, whereQ =
(
δij
pi
di
−pipj
)
1≤i,j≤r
.
On the other hand, we consider a random permutation obtained by a shuﬄe
of parameterspd1
1 ,...,p mr
r , and we denote as beforeΛk(σ) the shape of the
standard tableauPk(σ), and
L(n)
i,t = 1√n
([
(⌊nt + 1⌋− nt)Λi,⌊nt⌋(σ) + (nt−⌊nt⌋)Λi,⌊nt⌋+1(σ)
]
−pjnt
)
,
assuming thatd1 +··· +dj−1 + 1≤ i≤ d1 +··· +dj. Asn goes to inﬁnity,(
L(n)
1,t,...,L (n)
i,t ,...,L (n)
d,t
)
t∈[0,1]
converges in law to
(B1,t +x1,1,t,...,B j,t +xi,j,t,...,B r,t +xdr,r,t)t∈[0,1],
in C ([0, 1], Rd). In particular, ifλ = Λn(σ) = Λ(σ) with σ chosen randomly
as before, then
λi =npj +√npj (Xj +Yi,j) +o
(√n
)
,
with
(Y1,j,...,Y dj,j)∼ 1y1,j≥y2,j≥···≥ydj,j
y1,j +y2,j +···+ydj,j =0
∆(y1,j,y 2,j,...,y dj,j)2
1! 2!··· dj− 1! (2π)
dj−1
2
e−
‖yj‖2
2 dyj
and (X1,...,X r) gaussian vector of covariance matrix
Q′ =
(δij
di
−√pipj
)
1≤i,j≤r
.
A central limit theorem for the characters ofS∞ and H (S∞) 55
Remark. At the end of Section 4, we have seen that the law of large numbers
can be informally restated by saying that the longest increasing subsequences
in aα-shuﬄe are not bigger at ordern than the lengths of the blocks shuﬄed
together. Theorem 25 ensures that it is also true at order√n, unless some
blocks have the same frequencypj = αi = αi′. Then, some of the increasing
subwords become (stochastically) bigger than the sizes of the blocks to be
shuﬄed, because of the terms√npjYi,j.
Theorem 25 seems to remain true whenβ⁄= 0,γ ⁄= 0, and in this case,
the ﬂuctuations of the ﬁrst renormalized columns seem to be given by anal-
ogous formulas as those given above, with ﬂuctuations “of typeX” described
by Theorem 19, and ﬂuctuations “of typeY” (for equal coordinates) indepen-
dent of the ﬂuctuations of the rows. We don’t know how to prove this, but we
can give arguments in favor of this conjecture. These arguments can be made
rigorous in some cases, for instance whenγ = 0 and β has only a ﬁnite num-
ber of non-zero coordinates. When performing the Schensted insertion from a
permutation σ obtained by anω-shuﬄe, let us mark by a point• the boxes
containing a number coming from a block of sizemj, and by a star⋆ the boxes
containing a number coming from the block of sizel.
Example. Suppose n = 16, n1 =n2 = 3, m1 =m2 = 3, l = 4. We denote the
“cards” to be shuﬄed by0,1,...,9,A,B,...,F. After cutting the deck, the
ﬁve blocks to be shuﬄed are
012, 345, 678, 9AB, CDEF .
The blocks678 and 9AB are reversed, andCDEF is randomized, becoming from
instance DFCE. Then, all the blocks are shuﬄed together, and one can for
instance obtain
8B0D3A97FC41E562.
Now, the partitions appearing in the RSK algorithm are:
• • •
•
•
•
• ⋆
• •
⋆
• • ⋆
•
•
• • ⋆
•
•
•
• • ⋆
•
•
•
• • ⋆
• ⋆
•
•
• • ⋆ ⋆
• ⋆
•
•
•
• • ⋆ ⋆
⋆
•
•
•
•
• ⋆ ⋆
⋆
•
•
•
•
• ⋆ ⋆
⋆ ⋆
56 Pierre-Loïc Méliot
•
•
•
• ⋆
• ⋆ ⋆
⋆
•
•
•
• ⋆ ⋆
• ⋆ ⋆
•
•
•
• ⋆
• • ⋆
⋆ ⋆
•
Notice that the partition of unmarked boxes
is the one corresponding to034152; more generally, during the Schensted in-
sertion, the partition of unmarked boxes evolves as the partition obtainedvia
RSK from the subword containing only the letters coming from the blocks
of sizesni. Thus, to prove that Theorem 25 holds again whenβ⁄= 0,γ ⁄= 0
amounts to control the number of marked boxes appearing at the right of the
ﬁrst rows, and to show that it is ao(√n) — then, by symmetry of the prob-
lem, we would obtain the ﬂuctuations of the columns, and see that they are
analogous to those of the rows.
One should notice that each time a unmarked box appears in a row, it
pushes a marked box
• or ⋆
to the next row. Moreover, marked boxes push themselves to upper rows: for
instance, ifγ = 0 and β = (β1,...,β d), then one can not ﬁnd more thand
marked boxes on the same row. So the idea would be to show that marked
boxes are “suﬃciently pushed up”. Unfortunately, to do this rigorously, it seems
that we would need precise estimates on the probabilities of creating a “long”
increasing subword in a shuﬄe of parameterα = 0; and we don’t have for the
moment such estimates.
To conclude this section, let us look again at the partition-valued random
process (Λk(σ))k∈[ [0,n] ], where σ is obtained from anω-shuﬄe, andΛk(σ) is
the shape of the tableau obtained by Robinson-Schensted insertion from thek
ﬁrst letters ofσ. We have shown previously that after time-space scaling, and
at least whenβ = γ = 0, the coordinates of this process converge jointly to
a markovian process that can be written in terms of (conditioned) brownian
motions. It raises the following question: is(Λk(σ))k∈[ [0,n] ]itself a markovian
process in Y =⨆
n∈N Yn? The answer is yes, and more precisely:
Theorem 26. The random process(Λk(σ))k∈[ [0,n] ]is markovian, with transi-
tion probabilities equal to
p(λ,Λ ) = 1λ↗Λ
sΛ(ω)
sλ(ω).
A central limit theorem for the characters ofS∞ and H (S∞) 57
Proof. This is a generalization of [O’C03, Theorem 6.1], and the proof is ex-
actly the same. The statement of Theorem 26 amounts to ask that for any
sequence of partitionsλ(1)↗···↗ λ(k),
P[Λ1(σ) = λ(1),··· ,Λk(σ) = λ(k)] = sλ(k) (ω).
However, one can expandsλ(k) (ω) by using the structure of Hopf algebra of
Sym:
sλ(k) (ω) =
(
(1⊗υ⊗ 1)◦∆3)
sλ(k) (α,β,γE )
=
∑
ν⊂µ⊂λ(k)
sν(α)sµ′\ν′(β)sλ(k)\µ(γE ).
Then, the arguments are exactly the same as in [O’C03].
