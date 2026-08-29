---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-017-93-tasep-coulomb-gas-and-random-matrices
section_title: "TASEP, Coulomb gas, and random matrices"
section_number: 9.3
pages: 13-13
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
In proving Theorem 3.2, Johansson also proved an unexpected connection of TASEP to Coulomb gas and
random matrices [53]. Consider the probability density function on Rn
+ given by
p(x1, · · · , xn) = cn,me2 P
1≤i<j≤n log |xj−xi|−Pn
i=1 V (xi),
V (x) = x −(m −n) log x,
(9.1)
where cm,n is the normalization constant. Let xmax = max{x1, · · · , xn}. Johansson proved that for m ≥n,
the last passage time L(m, n) of the exponential DLPP has the same distribution as xmax. The density
function (9.1) is said to deﬁne a Coulomb gas with potential V on R+ since the term log |xi −xj| is the 2d
Coulomb potential of two equal charges at xi and xj. The function V (x) represents the conﬁning potential.
Let X be an n × m random matrix with entries that are independent complex normal variables of mean
zero and variance 1/2.
The random matrix W = XX∗is called the complex Wishart matrix, and its
eigenvalue density function is precisely (9.1) [44]. Thus, L(m, n) has the same distribution as the largest
eigenvalue of a complex Wishart matrix. See also [33]. The connection of the exponential DLPP to Coulomb
gas and the random matrix is special, and we do not expect to hold for general random variables ws.
There are universality results for both Coulomb gas and random matrices.
The Tracy-Widom limit
theorem is proved for the Coulomb gases with a general potential V .
The paper [38] showed the limit
theorem for generic analytic potentials, and [8] proved for discrete Coulomb gases in which particles are
restricted to be only on a discrete set.
Universality is a central question in random matrix theory, and there have been remarkable successes.
The largest eigenvalue of a large class of random Hermitian matrices with independent entries converges to
the Tracy-Widom distribution [41,60,81,85].
9.4
