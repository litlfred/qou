---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-008-33-resurgent-structure
section_title: "Resurgent structure"
section_number: 3.3
pages: 21-24
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41,S 3\52 with generic"
---
We collect the trans-series associated to the geometric and conjugate ﬂat connections in a
vector
Φ(k)
41 (x;τ) =
(
Φ(k,σ1)
41
Φ(k,σ2)
41
)
(x;τ). (3.35)
The singularities of the Borel transform of each component trans-series are located in Λ (k)
i
given in (2.63). In the case of level k = 1, we superimpose the Borel singularities of the
components of Φ(1)
41 (x;τ) and plot them in Fig. 2. At a generic level k≥ 1, the distrubtion
of the Borel plane singularities is the same and their actual locations are reduced by a
factor of 1/k according to (2.63).
As explained in Section 2, Stokes constants of individual Borel plane singularities
can be extracted from global Stokes automorphisms. The entire Borel plane is divided
by Stokes rays of components of Φ (k)
41 (x;τ) into inﬁnitely many cones. We label the four
cones above and below the positive and negative real axes by I,II,III,IV , ordered in
counter-clockwise direction, as illustrated in Fig. 2. We choose to calculate the global
Stokes automorphism S(k)
+ (˜x; ˜q) = S(k)
IV→II (˜x; ˜q) and S(k)
− (˜x; ˜q) = S(k)
II→IV (˜x; ˜q), both in
the anti-clockwise direction, which encode all the Stokes constants.
In order to derive the Stokes automorphisms, we ﬁrst calculate the Borel resummation
of the trans-series. Following [31] and with numerical evidence presented shortly after,
We claim that they can be written as bilinear products of holomorphic blocks in q and ˜q.
Concretely,
sI(Φ(k)
41 )(x;τ) =
(
−˜x 1 + ˜x−1
0 1
)
W−1(˜x; ˜q−1)∆(k)(τ)B(x;q), |˜q|< 1, (3.36a)
sII (Φ(k)
41 )(x;τ) =
(
0 −˜x
1−˜x− ˜x2
)
W−1(˜x−1; ˜q−1)
(
1 0
0−1
)
∆(k)(τ)B(x;q), |˜q|< 1,
(3.36b)
– 20 –
sIII (Φ(k)
41 )(x;τ) =
(
0−˜x
1 1
)
W−1(˜x−1; ˜q−1)
(
1 0
0−1
)
∆(k)(τ)B(x;q), |˜q|> 1, (3.36c)
sIV (Φ(k)
41 )(x;τ) =
(
−˜x−˜x
0 1
)
W−1(˜x; ˜q−1)∆(k)(τ)B(x;q), |˜q|< 1. (3.36d)
Here W−1(x,q ) is the Wronskian of holomorphic blocks deﬁned in (3.32), and
B(x;q) =
(
A0(x;q)
B0(x;q)
)
(3.37)
∆(k)(τ) is the diagonal matrix deﬁned by
∆(k)(τ) = diag(e−πik
4 −πi
2k−πi
4k (τ+τ−1), e
πik
4 +πi
2k +πi
4k (τ+τ−1)). (3.38)
From (3.36a) and (3.36b), we can derive the Stokes automorphism S(k)
I→II (˜q) which encom-
passes all the Stokes constants in the upper half plane. This step involves only multipli-
cation of ˜q-series. On the other hand, from (3.36a) and (3.36d) we can derive the Stokes
constants associated to the three Borel plane singularities on the positive real axis, and
this step involves analytic continuation of the Wronskian W−1(˜x−1; ˜q−1) from inside to
outside the unit circle with the help of (3.34). We can combine the two results to write
down the global Stokes automorphism S(k)
+ (˜x; ˜q) from the ray ρ0− to ρπ+0−. Likewise, we
can compute the global Stokes automorphism S(k)
− (˜x; ˜q) from the ray ρπ+0− to ρ2π+0−.
Together they encompass the Stokes constants of all the Borel plane singularities.
S(k)
+ (˜x; ˜q) =
(
0 −1
˜x−1−1− ˜x
)
W−1(˜x−1; ˜q−1)W−1(˜x; ˜q)T
(
0 ˜ x
−1−1− ˜x−1
)
, |˜q|< 1 (3.39)
S(k)
− (˜x; ˜q) =
(
˜x ˜x
0−1
)
W−1(˜x; ˜q)W−1(˜x−1; ˜q−1)T
(
˜x−1 0
˜x−1−1
)
, |˜q|< 1. (3.40)
In particular, we notice that the Stokes automorphisms and therefore the Stokes constants
do not depend on the level k.
At level k = 1 numerical evidences for the position of Borel plane singularities as well
as (3.36a),(3.36b),(3.36c),(3.36d) were given in detail in [31].
For higher levels, the computation is similar, although the expression becomes more
complicated. At level k = 2, we ﬁrst choose x = 6/5, corresponding to u = 2 log(6/5) and
n = 0. We truncate the power series toN = 100 terms. The poles of the Pad´ e approximant
for Φ(2)
41 (x,τ ) are shown in Fig. 3. Notice that the accumulating poles on the real axis hint
at a branch cut on the corresponding exact Borel plane.
Clearly, if we consider the vector Φ(x,τ ), the Borel plane is divided into four regions as
promised. It remains to check (3.36a),(3.36b),(3.36c),(3.36d). The comparison is tabulated
in Table 1.
We consider next x =−5/4, corresponding to u = 2 log(5/4) and n = 1, and we
truncate the power series up to N = 200 terms. The positions of poles for the Pad´ e
approximant Φ(k=2)
41 (x,τ ) are shown in Fig. 4. Again one observes the emergent branch cut
– 21 –
-2 -1 1 2
Re(t)
-4
-2
2
4
Im(t)
(a)
-2 -1 1 2
Re(t)
-4
-2
2
4
Im(t) (b)
Figure 3: The distribution of poles of the Pad´ e approximant for (a) : ϕ(k=2,σ1)
41 (x,τ ) and
(b) :ϕ(k=2,σ2)
41 (x,τ ) with x = 6/5 and N = 100 terms.
on the real axis. We then present the numerical evidence of (3.36a),(3.36b),(3.36c),(3.36d)
for each region in Tab. 2. As we can see, the relative errors between two sides of (3.36a),
(3.36b), (3.36c), (3.36d) (the ﬁrst column) are always within the precision of the Borel
resummation (the second column), and are always far smaller than a potential ˜ q (or 1/˜q
in the lower half plane) or a ˜x±1 correction (the third and the fourth columns).
-2 -1 1 2
Re(t)
-4
-2
2
4
Im(t)
(a)
-2 -1 1 2
Re(t)
-4
-2
2
4
Im(t) (b)
Figure 4: The distribution of poles of the Pad´ e approximant for (a) : ϕ(k=2,σ1)
41 (x,τ ) and
(b) :ϕ(k=2,σ2)
41 (x,τ ) with x =−5/4 and N = 200 terms.
We also perform numerical analysis at levelk = 3. We choose x = 6
5e2πni/3 (n = 0, 1, 2)
corresponding tou = 3 log(6/5) andn = 0, 1, 2 respectively. The power series are truncated
up to N = 220 terms. The poles of the Pad´ e approximant have a similar structure to the
cases k = 1, 2, so we omit them here. The numerical evidence for the Borel resummation
of the trans-series (3.36a),(3.36b),(3.36c),(3.36d) in each region are given in Tabs. 3, 4 and
5 respectively.
– 22 –
|sI(Φ)(x;τ)
FI(x;τ) − 1| |sI(Φ)(x;τ)
s′
I(Φ)(x;τ)− 1| | ˜q(τ)| Min(|˜x(x,τ )|,|˜x(x,τ )−1|)
σ1 8.6× 10−16 3.5× 10−15
1.9× 10−8 0.36σ2 3.7× 10−23 2.4× 10−22
(a) Region I: τ = 1
8e
πi
4
|sII (Φ)(x;τ)
FII (x;τ) − 1| |sII (Φ)(x;τ)
s′
II (Φ)(x;τ)− 1| | ˜q(τ)| Min(|˜x(x,τ )|,|˜x(x,τ )−1|)
σ1 3.7× 10−23 2.4× 10−22
1.9× 10−8 0.36σ2 8.6× 10−16 3.5× 10−15
(b) Region II : τ = 1
8e
3πi
4
|sIII (Φ)(x;τ)
FIII (x;τ) − 1| |sIII (Φ)(x;τ)
s′
III (Φ)(x;τ)− 1| | ˜q(τ)−1| Min(|˜x(x,τ )|,|˜x(x,τ )−1|)
σ1 3.7× 10−23 2.4× 10−22
1.9× 10−8 0.36σ2 8.6× 10−16 3.5× 10−15
(c) Region III : τ = 1
8e− 3πi
4
|sIV (Φ)(x;τ)
FIV (x;τ) − 1| |sIV (Φ)(x;τ)
s′
IV (Φ)(x;τ)− 1| | ˜q(τ)−1| Min(|˜x(x,τ )|,|˜x(x,τ )−1|)
σ1 8.6× 10−16 3.5× 10−15
1.9× 10−8 0.36σ2 3.7× 10−23 2.4× 10−22
(d) Region IV : τ = 1
8e− πi
4
Table 1 : We perform the numerical Borel resummation for Φ (k=2)
41 (x;τ) at x = 6/5
(u = 2 log 6/5,n = 0) with 100 terms, after choosing suitable τ in four diﬀerent regions.
We compare them with equations (3.36a),(3.36b),(3.36c),(3.36d) whose right hand side is
denoted as FR(x;τ). Meanwhile, we estimate the contribution of higher order terms by
resumming Φ(k=2)
41 (x;τ) with 95 terms. The values of |˜q(˜q−1)| and|˜x±1| are also provided
for comparison.
