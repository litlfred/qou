---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-008-2-zz1-on-the-unit-circle-see-sz1
section_title: "(z+z−1) on the unit circle (see [Sz1],"
section_number: 2
pages: 18-19
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
[DKMVZ1]).
Similar problem on the real line is analyzed in [DKMVZ1] with-
out double scaling limit (γ is kept ﬁxed). Our goal is to ﬁnd the large q behavior
of Y21(0; q) for all γ > 0.
e
iθ
-1
0
θ
1
Figure 7. branch cut of log(z −eiθ)
LONGEST INCREASING SUBSEQUENCE
19
Let dµ(s) be a probability measure on the unit circle. Deﬁne
g(z) ≡
Z
Σ
log(z −s)dµ(s)
(4.5)
where for each θ, the branch is chosen such that log(z −eiθ) is analytic in C −
(−∞, −1] ∪{eit : −π ≤t ≤θ} (see Figure 7) and log(z −eiθ) ∼log z for real
z →∞. The following Lemma is based on related calculations in [DKM].
Lemma 4.2. Suppose dµ(z) = u(θ)dθ is an absolutely continuous probability mea-
sure on the unit circle and u(θ) = u(−θ). Then g(z) has the following properties
:
1. g is analytic in C −Σ ∪(−∞, −1).
2. On (−∞, −1), g+(z) −g−(z) = 2πi.
3. g(z) = log z + O( 1
z) as z →∞.
4. eqg(z) is analytic in C −Σ.
5. eqg(z) = zq(1 + O( 1
z)) as z →∞.
6. g(0) = πi.
7. g+(z) + g−(z) = 2
R π
−π log |z −s|dµ(s) + i(φ + π) on z ∈Σ where φ = arg(z).
8. g+(z) −g−(z) = 2πi
R π
φ dµ(s) on z∈Σ.
Proof. (i)-(v) are trivial. For (vi),
g(0) =
Z π
−π
log (0 −eiθ)u(θ)dθ =
Z π
−π
i(θ + π)u(θ)dθ = πi
using the evenness of u(θ).
For (vii), ﬁx z = eiφ ∈Σ. Then arg(z −eiθ) is analytic if −π < θ < φ and
g+(z) =
Z π
−π
log |z −eiθ|dµ(z) + i
Z φ
−π
arg(z −eiθ)dµ(z) + i
Z π
φ
arg+(z −eiθ)dµ(z),
g−(z) =
Z π
−π
log |z −eiθ|dµ(z) + i
Z φ
−π
arg(z −eiθ)dµ(z) + i
Z π
φ
arg−(z −eiθ)dµ(z).
Note that for φ < θ < π,
arg+(eiφ −eiθ) −arg−(eiφ −eiθ) = 2π.
This yields
g+(z)+g−(z) = 2
Z π
−π
log |z−eiθ|dµ(z)+2i
Z π
−π
arg+(eiφ−eiθ)dµ(z)−i
Z π
φ
2πdµ(z).
Set
F(φ) = 2
Z φ
−π
arg(eiφ −eiθ)dµ(z) + 2
Z π
φ
arg+(eiφ −eiθ)dµ(z) −2π
Z π
φ
dµ(z) −φ
If we show F(φ) ≡π, then (vii) is proved. Note that (a) arg(eiφ −eiφ−) = φ + π
2 ,
(b) arg+(eiφ −eiφ+) = φ + 3π
2 and (c)
d
dφarg(eiφ −eiθ) ≡1
