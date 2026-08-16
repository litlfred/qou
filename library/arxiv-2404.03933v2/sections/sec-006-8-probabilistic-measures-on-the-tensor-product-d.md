---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-006-8-probabilistic-measures-on-the-tensor-product-d
section_title: "Probabilistic measures on the tensor product decomposition"
section_number: 8
pages: 21-23
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
Here we introduce some natural probabilistic measures on indecomposable components of
T (1)⊗N for big and small quantum sl2 and we show that they are all induced by Markov
processes.
8.1. The character and the Plancherel measures forUq(sl2). LetX (l)
N be the set of tilting
modules of Uq(sl2) that occur in the decomposition of T (1)⊗N. It can be naturally identified
with the subset of dominant integral weights of sl2, i.e. with k ∈ Z≥0 such that k ≤ N,
k≡ N mod 2. Define the multiplicity function on Z≥0 as the multiplicity of T (k)⊂ T (1)⊗N
when k∈X (l)
N and zero otherwise.
Definition 8.1. The character measure on Z≥0 is given by
p(l)
N (k;t) = M (l)
k (N)chT (k)(et)
(chT (1)(et))N .
Here M (l)
k (N) is the multiplicity function, t is a real parameter and chT (k)(et) is the formal
character from Lemma 7.1 evaluated on et.
Multiplicativity and additivity of characters imply that the character measure a probability
measure, i.e. P
k∈X (l)
N
p(l)
N (k;t) = 1. Recall that the multiplicity function is computed explicitly.
Definition 8.2. When t = 0 the character measure becomes the Plancherel measure
p(l)
N (k) = M (l)
k (N) dimT (k)
(dimT (1))N .
22 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
Dimensions of tilting modules can be easily derived from their formal characters:
dimT (k0 +lk1) =



k0 + 1, if 0≤k0≤l− 2 and k1 = 0,
l(k1 + 1), if k0 =l− 1 and k1∈ Z>0,
2k1l, if 0≤k0≤l− 2 and k1∈ Z>0.
It is clear that the Plancherel measure for Uq(sl2) is the specialization of the character measure
att = 0. We distinguish it because as we will see that limit N→∞ is not interchangable with
the limit t→ 0.
8.2. The Plancherel measure for uq(sl2). Now let us define the Plancherel measure on
indecomposable components of T (1)⊗N foruq(sl2). Recall that in Section 6.2 to each node of a
graph in Figure 3 we assigned a tilting module. From now on we will use notation corresponding
to this assignment:
• T (k) =T+(k) when l− 1≤k≤ 2l− 2 and m(l)
k (N) =m(l)
k,+(N),
• T (k) =T−(k−l) when 2l− 1≤k≤ 3l− 2 and m(l)
k (N) =m(l)
k−l,−(N).
In this case, dimensions of indecomposable representations that occur in the decomposition
of the tensor product T (1)⊗N are written as follows
dimT (k) =



k + 1, if 0≤k≤l− 2,
l, if k =l− 1, 2l− 1,
2l, otherwise.
Definition 8.3. The Plancherel measure on indecomposable components ofuq-moduleT (1)⊗N
is
p(l)
N (k) = m(l)
k (N) dimT (k)
(dimT (1))N , 0≤k≤ 3l− 2
and is zero for k> 3l− 2.
8.3. The quantum Plancherel measure for uq(sl2). Quantum dimension [KR] of the irre-
ducible Uv(sl2)-module V (k) is
dimv(V (k)) = vk+1−v−k−1
v−v−1 .
For quantum dimensions of modules that T (k) which occur in the decomposition of T (1)⊗N
we have
dimq(T (k)) = qk+1−q−k−1
q−q−1
for 0≤k≤l− 2. For other modules T (k) quantum dimensions are zero.
Note that whenq =e
iπ
l we have dimq(T (k))∈ R≥0 for arbitrary values ofk and dimq(T (k))∈
R>0 for 0≤ k≤ l− 2.3. It is not difficult to show that this is the only root of degree l from
−1 with such property.
3This positivity is closely related to the unitarity of Wess-Zumino-Witten conformal field theory and of
quantum Chern-Simons topological quantum field theory.
TENSOR POWERS 23
Definition 8.4. Quantum Plancherel measure is defined as
p(l)
N (k) =
m(l)
T (k)(N)dimqT (k)
(dimqT (1))N , 0≤k≤l− 2
and is zero for k>l − 2.
