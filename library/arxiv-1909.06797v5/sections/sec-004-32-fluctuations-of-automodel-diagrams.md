---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-004-32-fluctuations-of-automodel-diagrams
section_title: "Fluctuations of automodel diagrams"
section_number: 3.2
pages: 12-13
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
Fluctuations of Young diagrams have been under investigation in the mathematics literature [9, 26–
36]. A rescaled Young diagram deﬁned in (3.11) in the k→∞ limit takes the form of limit shape
(denoted by Ω, as deﬁned in (3.12)). However there can be large k corrections to this result and
we call such corrections as ﬂuctuations of limit shape diagram Ω. Kerov studied the Gaussian
ﬂuctuations around the limit shape of Young diagrams Ω endowed with Plancherel measure in
[26]. In [9], Ivanov and Olshanki reconstructed a proof of Kerov’s result on ﬂuctuations around
the limit shape from his unpublished work notes, 1999. The central result pertains to large k
corrections to the limit shape which can be stated as
lim
k→∞
ˆνk(u)∼ Ω(u) + 2√
k
∆(u) (3.20)
The sub-leading piece ∆(u) is a Gaussian process deﬁned for|u|≤ 2. More precisely, ∆(u) is a
random trigonometric series given by
∆(u) = ∆(2 cosθ) = 1
π
∞∑
n=2
αn
√n sin(nθ) ; u = 2 cosθ (3.21)
whereαn are independent Gaussian random variables with mean 0 and variance 1. Further inves-
tigations has been done towards understanding the central limit theorem for Gaussian ﬂuctuations
around the limit shape [29, 30]. Fluctuations of random Gaussian and Wishart matrices have been
related to the notion of free probability and free cumulants in earlier works [34–36].
12
4. Partition Function for Y oung lattice
Following (3.2, 3.3) and eq. (3.5), the grand canonical partition function for Y can be written
as,
QY =
∞∑
k=0
zk
∑
λk
(dimλk)2
k! δ(k−|λk|), z> 0. (4.1)
This partition function is related to Poissonised Plancherel measure [37]. The above ensemble
sometimes is known as Meixner ensemble in literature [38, 39].
The above partition function does not capture the growth process of Young diagrams as it can
exactly be calculated using the normalization eq. (3.4)
QY = 1
1− z. (4.2)
However, to study the growth process through the partition function we regularise the sum by
imposing a cut-oﬀ on the Young diagrams in the summation over λk in eq. (4.1). We introduce
a large positive integer N and constrain that the Young diagrams in lattice Y can not have more
than N rows. In presence of such a cut-o ﬀ the summation overλk for k > N is not equal to unity
anymore. The regularised partition function is therefore given by
QN
Y =
∞∑
k=0
zk
∑
n1,···,nN≥0
(dimλk)2
k! δ
k−
N∑
i=1
ni
, with n1≥ n2≥···≥ nN≥ 0. (4.3)
This regularisation gives us a handle on the partition function to carry out a saddle point analysis
of the problem. In the large N limit, the partition function is dominated by a single Young diagram
for a given value of z. It turns out that the shape of this dominant diagram falls into the automodel
class of Kerov [5], paramatrised by z. For a particular value of the parameter z it becomes the
limit shape [3–5]. Before we present the calculation, we show that the partition function (4.3) is
equivalent to the partition function of S U(N) Gross-Witten-Wadia model and its cousins.
