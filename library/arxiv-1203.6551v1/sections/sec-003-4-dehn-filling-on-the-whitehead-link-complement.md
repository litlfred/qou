---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-003-4-dehn-filling-on-the-whitehead-link-complement
section_title: "Dehn filling on the Whitehead link complement and its sister"
section_number: 4
pages: 10-13
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.99
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
We now study the 1-cusped hyperbolic 3-manifolds obtained by Dehn filling on the Whitehead link complement and its sister, the complement of the $(-2,3,8)$-pretzel link, denoted $m129$ and $m125$ respectively in SnapPea notation. Note that each of these manifolds has a symmetry interchanging the cusps, so it suffices to consider Dehn fillings on cusp 0. See also [@HMW; @NR] and [@AD] for detailed discussions of the geometry and topology of these manifolds and their Dehn fillings.

The main result of this section is the following:

::: thm
[]{#cusped_unique label="cusped_unique"} There is an infinite sequence of hyperbolic Dehn fillings $M(a_i,b_i)$ on one cusp of the $(-2,3,8)$-pretzel link complement $M=m125$ with $a_i^2+b_i^2 \to  \infty$ such that if $N$ is any orientable cusped hyperbolic 3-manifold with $\text{Vol} (N)=\text{Vol} (M(a_i,b_i))$ then $N$ is homeomorphic to $M(a_i,b_i)$. So the manifolds $M(a_i,b_i)$ are determined by their volumes, amongst all orientable cusped hyperbolic 3-manifolds.
:::

The proof is similar to the proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}. However there is an extra difficulty because not every symmetry of the cusp torus extends to a symmetry of the manifold $m125$. To deal with this, we look at the next terms in the Neumann-Zagier asymptotic expansion for volume change during Dehn filling.

The quadratic forms for $m125$ and $m129$ given by ([\[eq1\]](#eq1){reference-type="ref" reference="eq1"}) are closely related to the quadratic form $$\label{eq15}
Q_0(a,b) = a^2+ b^2 = |a+b i|^2 .$$ From the symmetries of the lattice $\mathbb{Z}+\mathbb{Z}i$, we have $$|a+b i | = | i^k(a+b i)| = | i^k(a- b i)|$$ for $k =0, 1, \ldots, 3$, and $Q_0$ has symmetry group $G_{Q_0} \cong D_4$ of order 8, with the orbit of $(a,b)$ under $G_{Q_0}$ given by $$\label{eq16}
\{  \pm(a, b), \pm(-b,a), \pm(a,-b), \pm(b,a) \}.$$

Consider a maximal horospherical cusp torus for $m129$ and $m125$. In each case we choose the geometric basis for peripheral homology used by SnapPea. From SnapPea (or [@HMW; @NR; @AD]) we have the following:

For $m125$, the torus has cusp shape $\tau = i$. If we normalise so that the torus has area $2$ then the $(a,b)$ geodesic has length squared $$\label{eq17}
Q_1(a,b)= 2 |a + b i |^2 = 2(a^2 + b^2) = 2 Q_0(a,b).$$ This quadratic form has symmetry group $G_{Q_1}=G_{Q_0} = D_4$ as described above. The subgroup of symmetries of $Q_1$ extending to symmetries of $m125$ is the subgroup of orientation preserving symmetries $G_{m125} = C_4$, given by $(a,b) \mapsto  \pm(a, b), \pm(-b,a)$.

For $m129$, the torus has cusp shape $\tau = 2 i$. If we normalise so that the torus has area $2$ then the $(a,b)$ geodesic has length squared $$\label{eq18}
Q_2(a,b)={ |a+ 2bi|^2 } = (a^2+ 4b^2) = Q_0(a,2b).$$ This quadratic form has symmetry group $G_{Q_2} = D_2$ consisting of $(a,b) \mapsto (\pm a, \pm b)$, but $G_{m129} = C_2$ is the subgroup $(a,b) \mapsto \pm(a,b)$.

::: prop
[]{#2p_with_big_gap label="2p_with_big_gap"} For each $g >0$ there exist infinitely many integers $m=2p$, with $p$ prime, such that

1.  $m$ can be written as $Q_1(a,b)$ where $a,b$ are relatively prime integers, and if $Q_1(a,b)=Q_1(a',b')$ then $(a',b') = (\pm a, \pm b)$ or $(a',b') = (\pm b, \pm a)$.

2.  $m+k$ has no primitive integer representation as $Q_0(a,b)$ for $0<|k|\le g$,

3.  $m$ has no primitive integer representation as $Q_2(a,b)$.
:::

This again follows from some elementary number theory.

::: lem
[]{#p=1mod4 label="p=1mod4"} If $p$ is a prime congruent to $1$ modulo $4$, then $p$ can be written in the form $p= a^2 + b^2$ where $a,b$ are relatively prime positive integers. Further, if $p=(a')^2+(b')^2$ where $a',b'$ are positive integers then $(a',b')=(a,b)$ or $(b,a)$.
:::

::: proof
*Proof.* This is a result of Euler (see, for example, [@HaWr Chapter 15]). ◻
:::

::: lem
[]{#p=3mod4 label="p=3mod4"} If $p$ is a prime congruent to $3$ modulo $4$ and $p$ divides $n$, then $n$ has no representation $n = Q_0(a,b)=a^2 + b^2$ with $a,b$ relatively prime integers.
:::

::: proof
*Proof.* Let $p$ be an odd prime dividing $n = a^2 + b^2$ with $a,b$ relatively prime integers. Then by Lemma [\[discr_quad_res\]](#discr_quad_res){reference-type="ref" reference="discr_quad_res"}, $-1$ is a quadratic residue mod $p$. It follows that $p \equiv 1 \bmod 4$ (see e.g. [@HaWr Thm 82]). ◻
:::

::: lem
If $n \equiv 2 \mod 4$ then $n = Q_2(a,b) = a^2 + 4 b^2$ has no solution with $a,b$ integers.
:::

::: proof
*Proof.* Reduce modulo $4$. ◻
:::

::: proof
*Proof of Proposition [\[2p_with_big_gap\]](#2p_with_big_gap){reference-type="ref" reference="2p_with_big_gap"}.* This follows from the previous lemmas together with the Chinese remainder theorem and Dirichlet's theorem on primes in arithmetic progressions, as in the proof of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}. ◻
:::

::: proof
*Proof of Theorem [\[cusped_unique\]](#cusped_unique){reference-type="ref" reference="cusped_unique"}.* The quadratic forms $Q_1$ and $Q_2$ for $m125$ and $m129$ considered above give the squares of geodesic lengths on a cusp torus with area $2$. Hence the corresponding normalised quadratic forms are given by $$\hat Q_1(a,b) =  {1 \over 2 } Q_1(a,b) \text{ and } \hat Q_2(a,b) =  {1 \over 2 } Q_2 (a,b).$$ We now apply Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"} with gap size $g = 4 C$, where $C$ is the maximum of the constants $C_2$ for $m125$ and $m129$ given by Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}.

This gives a sequence of primes $p_i \equiv 1 \bmod 4$ with $p_i \to \infty$ and pairs $(a_i,b_i)$ of relatively prime integers with $p_i =a_i^2+b_i^2$ satisfying the conditions of Proposition [\[2p_with_big_gap\]](#2p_with_big_gap){reference-type="ref" reference="2p_with_big_gap"}. Then $\text{Vol} (m125(a,b)) = \text{Vol} (m125(a_i,b_i)$ implies that $Q_1(a,b)=Q_1(a_i,b_i)$, hence $(a,b) = \pm(a_i,b_i), \pm(-b_i,a_i), \pm(a_i,-b_i)  \text{ or} \pm(b_i,a_i)$. For any such $(a,b)=(a_i,b_i)$, $\text{Vol} (m125(a,b)) = \text{Vol} (m125(a',b'))$ implies that $Q_1(a,b)=Q_1(a',b')$ hence $(a',b') = \pm(a, b), \pm(-b,a), \pm(a,-b)  \text{ or} \pm(b,a)$.

Now the surgeries $\pm(a, b), \pm(-b,a)$ give manifolds which are homeomorphic, hence have the same volume. Similarly, the surgeries $\pm(a,-b),   \pm(b,a)$ give homeomorphic manifolds of the same volume. Next, we use the degree 4 terms in the Neumann-Zagier asymptotic formula to show that $\text{Vol} (m125(a,b)) \ne  \text{Vol} (m125(b,a))$ for all sufficiently large $(a,b)$.

In [@AD], Aaber and Dunfield study the Neumann-Zagier asymptotic expansion of volume for Dehn fillings on the Whitehead link sister $m125$. Using their calculations we obtain the following asymptotic formula for decrease in volume for surgeries on cusp 0 of $m125$ (see Example [\[m125_NZ4\]](#m125_NZ4){reference-type="ref" reference="m125_NZ4"} and equation ([\[eq31\]](#eq31){reference-type="ref" reference="eq31"}) below): $$\Delta V_{m125} (a,b)=  
{ \pi^2 \over a^2+b^2} -
\frac{\pi^4(a^4-12 a^3 b-6 a^2 b^2+12 a b^3+b^4)}{ 24\left(a^2+b^2\right)^4}
+ O \left({1 \over (a^2+b^2)^3}\right).$$ Hence, we have $$\label{eq20}\Delta V_{m125} (a,b) - \Delta V_{m125} (b,a)
=  \frac{\pi ^4 a b \left(a^2-b^2\right)}{\left(a^2+b^2\right)^4} +
O \left({1 \over (a^2+b^2)^3}\right).$$

::: lem
[]{#lower_bound label="lower_bound"} If $a$ and $b$ are integers with $a > b > 0$, then $a b (a^2-b^2) \ge  {r^3/4},$ where $r^2 = a^2+b^2$.
:::

::: proof
*Proof.* Consider the function $$f(a,b)=    a b (a^2-b^2) = a b ( a + b ) ( a - b ).$$ Now we have

1.  If $b \le a/2$ then $b(a-b) \ge b (a - a/2)=  b a/2  \ge a/2,$ since $b \ge 1$.

2.  If $b  \ge a/2$ then $b (a-b) \ge  a/2 \cdot (a-b)  \ge  a/2,$ since $a-b  \ge 1$.

Further, $a^2+b^2 = r^2$ and $a > b > 0$ imply that $a^2 \ge r^2/2$ and $a+b \ge r$. Hence $$f(a,b)=  a(a+b) b(a-b) \ge a(a+b) \cdot a/2  = a^2 (a+b)/2 \ge r^3/4,$$ as desired. ◻
:::

Equation ([\[eq20\]](#eq20){reference-type="ref" reference="eq20"}) shows that, whenever $a^2+b^2$ is sufficiently large, $$\Delta V_{m125} (a,b) - \Delta V_{m125} (b,a)
\ge  \frac{\pi ^4 a b \left(a^2-b^2\right) - C(a^2+b^2)}{\left(a^2+b^2\right)^4},$$ where $C$ is a positive constant. Hence, by Lemma [\[lower_bound\]](#lower_bound){reference-type="ref" reference="lower_bound"}, there exists a constant $R>0$ such that if $(a,b)$ are relatively prime integers with $a >b >0$ and $a^2+b^2 \ge R^2$ , then $\Delta V_{m125} (a,b) > \Delta V_{m125} (b,a)$.

This completes the proof that for all sufficiently large $(a_i,b_i)$, the Dehn fillings $m125(a_i,b_i)$ are determined by their volumes amongst Dehn fillings on $m125$.

Further, $\text{Vol} (m125(a_i,b_i)) = \text{Vol} (m129(a,b))$ implies that $Q_1(a_i,b_i)=Q_2(a,b)$, which has no solutions by condition (iii) of Proposition [\[2p_with_big_gap\]](#2p_with_big_gap){reference-type="ref" reference="2p_with_big_gap"}. Hence, for all sufficiently large $(a_i,b_i)$, the manifolds $m125(a_i,b_i)$ are determined by their volumes amongst Dehn fillings on $m129$ and $m125$.

The result now follows as in the proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"} since $m129$ and $m125$ are the unique 2-cusped manifolds of volume $v_{\omega^2}$ by the work of Agol [@agol_2cusp]. So any 1-cusped manifold with volume less than $v_{\omega^2}$ but sufficiently close to $v_{\omega^2}$ comes from Dehn filling on $m129$ or $m125$. ◻
:::
