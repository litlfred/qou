---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-000-11-jack-deformation-of-plancherel-measure-and-ra
section_title: "Jack deformation of Plancherel measure and random matrices"
section_number: 1.1
pages: 1-4
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
partitions occur in mathematics and physics in a wide variety of contexts, in partic-
ular in the Gromov-Witten and Seiberg-Witten theories, see [Oko03] for an intro-
duction to the subject. Another aspect which makes them attractive is the link with
random matrices. Namely, some classical models of random matrices have random
partition counterparts, which display the same kind of asymptotic behaviour.
In this paper, we consider the following probability measure on the set of parti-
tions (or equivalently, Young diagrams) of sizen:
(1) P(α)
n (λ) = αnn!
j(α)
λ
,
where j(α)
λ is a deformation of the square of the hook products:
j(α)
λ =
∏
□ ∈λ
(
αa(□ ) + ℓ(□ ) + 1
)(
αa(□ ) + ℓ(□ ) + α
)
.
Here, a(□ ) := λj − i and ℓ(□ ) := λ′
i − j are respectively the arm and leg length
of the box □ = (i, j) (the same deﬁnitions as in [Mac95, Chapter I]).
2010 Mathematics Subject Classiﬁcation. 60C05, 05E05 (secondary:60B20).
Key words and phrases. random partitions; Jack measure; bulk ﬂuctuations; Jack po lynomials;
polynomial functions on Young diagrams; Stein’s method.
MD has been supported by the grant of National Center of Scien ces 2011/03/N/ST1/00117 and
by ANR project CARTAPLUS ANR 12-JS02-001-01. VF has been par tially supported by ANR
project PSYCO ANR-11-JS02-001 and by SNSF grant “Dual combinatorics of Jack polynomials”.
1
2 M. DOŁ ˛ EGA AND V . FÉRAY
When α = 1 , the measure P(α)
n specializes to the well-known Plancherel mea-
sure for the symmetric groups. In general, it is calledJack deformation of Plancherel
measure (or Jack measure for short), because of its connection with the celebrated
Jack polynomials that we shall explain later. It has appeare d recently in several
research papers [BO05, Ful04, Mat08, Ols10, Mat10] and it is presented as an
important area of research in Okounkov’s survey on random pa rtitions [Oko03,
Section 3.3].
Recall that Plancherel measure has a combinatorial interpretation: it is the push-
forward of the uniform measure on permutations by Robinson-Schensted algorithm
(we keep only the common shape of the tableaux in the output ofRS algorithm). A
similar description holds for Jack measure for α = 2 (and α = 1/2 by symmetry):
it is the push-forward of the uniform measure on ﬁxed point free involutions by RS
algorithm (in this case, the resulting diagram has always even parts and we divide
each part by 2) – see [Mat08, Section 3].
Thus Jack measure can be considered as an interpolation betw een these two
combinatorially relevant models of random partitions.
1.1.1. α = 1 case: Plancherel measure and GUE ensemble. There is a strong
connection between Plancherel measure and theGaussian unitary ensemble(called
GUE) in random matrix theory. The Gaussian unitary ensemble is a random Her-
mitian matrix with independent normal entries. The probabi lity density function
for the eigenvalues of that matrix (of the size d × d) is proportional to the weight
(2) e−β/2 ∑ x2
i
∏
i<j≤d
(xi − xj)β
with β = 2 (see [AGZ10]). Consider the scaled spectral measure of the G UE
ensemble
µ(2)
d := 1
d (δx1 + · · · + δxd) ,
where x1 ≥ · · · ≥ xd are eigenvalues of our random matrix and δ is the notation
for Dirac operator. Then the famousWigner law states that, as d → ∞, the spectral
measure tends almost surely to a semicircular law, i.e. to a probability measure
µS−C :=
√
4−x2
2π 1[−2,2](x)dx supported on the interval[−2, 2] (see [AGZ10]). The
second order asymptotics is also known and one can observe Gaussian ﬂuctuations
around the limiting distribution (see [Joh98]). Informall y speaking, looking at the
scaled spectral measure of GUE as a generalized function
µ(2)
d (x) = 1
d (δx−x1 + · · · + δx−xd) ,
we have that
µ(2)
d (x) ∼ µS−C(x) + 1
d
~∆ (2)(x),
as d → ∞ , where ˜∆ (2)(x) is an explicit Gaussian process on the interval [−2, 2]
with values in the space of generalized functions (C∞(R))′.
It was also discovered that a similar phenomenon holds for the Plancherel mea-
sure. The ﬁrst order asymptotics for the Plancherel measure was found by Vershik
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 3
z
− 3− 2− 1
1
2
3
t
1
2
3
4
5
6
7
8
9
x
1 2 3 4 5
y
1
2
3
4
z
− 5 − 4 − 3 − 2 − 1 1 2 3 4 5
t
1
2
3
4
5
x
1
2
3
4
5
y
1
2
3
4
FIGURE 1. Young diagram λ = (4 , 3, 1) and the graph of the
associated function ω(λ).
and Kerov [KV77] and, independently, by Logan and Shepp [LS77]. They noticed
that a Young diagram λ can be encoded by a continuous piecewise-afﬁne function
ω(λ) from R to R: this encoding is represented in Figure 1 and formally deﬁne d
in Section 2.4. Then they proved that for appropriately scal ed Young diagrams
λ(n) of size n distributed according to the Plancherel measure (the bar encodes the
scaling), one has the convergence in probability
sup
x∈R
⏐
⏐ω(
λ(n))(x) − Ω( x)
⏐
⏐ (P )
− →0
where the limit shape Ω is given by
(3) Ω( x) =
{
|x| if |x| ≥ 2;
2
π
(
x · arcsin x
2 +
√
4 − x2
)
otherwise.
There is a strong connection between this limit shape and the semicircular law
µS−C, namely the so-called transition measure of Ω , seen as a continuous Young
diagram, is the semicircular law µS−C – see [Bia98, Section 1.2].
The problem of the second order asymptotics was stated as an o pen question
in late seventies and was solved by Kerov [Ker93a] who proved that, exactly as
in the GUE case, the ﬂuctuations around the limit shape are Ga ussian. Informally
Kerov’s result can be presented as follows
ω
(
λ(n)
)
(x) ∼ Ω( x) + 2√n ∆ (1)
∞ (x)
where ∆ (1)
∞ is the Gaussian process on [−2, 2] with values in (C∞(R))′ deﬁned by:
∆ (1)
∞ (2 cos(θ)) = 1
π
∞∑
k=2
ξk√
k
sin(kθ).
The detailed proof of this remarkable theorem can be found in [IO02]. Although
they are not equal, the Gaussian processes ∆ (1)
∞ (which describe bulk ﬂuctuations
4 M. DOŁ ˛ EGA AND V . FÉRAY
of Young diagram under Plancherel measure) and ~∆ (2) (which describe bulk ﬂuc-
tuations of the GUE) have quite similar deﬁnition.
Remarkably, the similarity between the Plancherel measureand the GUE ensem-
ble does not only take place at the level of bulk ﬂuctuations but also "at the edge".
To be more precise, it was proved that the distribution of ﬁni tely many (prop-
erly scaled) ﬁrst rows of random Young diagrams (with respec t to the Plancherel
measure) is the same as the distribution of the same number of (properly scaled)
largest eigenvalues of the GUE ensemble, asn → ∞ (see [BDJ99, Oko00, BOO00,
Joh01b, Joh01a, BDR01] for details).
1.1.2. General α-case and Gaussian β-ensembles. There are two famous ana-
logues of the GUE ensembles in random matrix theory: Gaussian orthogonal en-
sembles (GOE) and Gaussian symplectic ensembles (GSE) (see [Meh04]). The
GOE ensemble (GSE ensemble, respectively) is a random real s ymmetric matrix
(complex self-adjoint quaternion matrix, respectively) w ith independent normal
entries (with mean 0 and well-chosen variance). The density function for the dis -
tribution of eigenvalues of GOE (GSE, respectively) is, up t o normalization, the
function given by equation (2) with parameter β = 1 (β = 4, respectively). There-
fore, it is tempting to introduceGaussian β-ensemble (GβE, also called β-Hermite
ensemble) that has a distribution density function proportional to (2) for any posi-
tive real value of β.
The GβE ensembles are well-studied objects. For the ﬁrst order of a symptotic
behaviour of the spectral measure
µ(β)
d := 1
d
(
δ β
2 x1
+ · · · + δ β
2 xd
)
,
where x1 ≥ · · · ≥ xd are eigenvalues of the GβE of size d × d, Johansson [Joh98]
showed that the Wigner law holds, i.e., asd → ∞, one has the almost-sure conver-
gence
(4) µ(β)
d → µSC .
A central limit theorem for the GβE was proved by Dumitriu and Edelman [DE06].
Here, we can observe Gaussian ﬂuctuations around the limit s hape, similarly to
the GUE case. Additionally, a surprising phenomenon takes p lace: the Gaussian
process that describes the second order asymptotic is translated by a deterministic
shift, which disappears for β = 2 (see [DE06] for details).
A natural question is to ﬁnd a discrete counterpart for G βE. Some results of
Matsumoto [Mat08] suggest that a good candidate for such pro bability measure
on the set of Young diagrams is Jack measure given by (1), where the relation
between parameters α and β is β = 2
α. Matsumoto was studying a restriction of
Jack measure to the set of Young diagrams of size n with at most d rows. His
