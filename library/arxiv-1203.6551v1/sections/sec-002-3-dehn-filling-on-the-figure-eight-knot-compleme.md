---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-002-3-dehn-filling-on-the-figure-eight-knot-compleme
section_title: "Dehn filling on the figure eight knot complement and its sister"
section_number: 3
pages: 8-10
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.969
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
In this section we study the closed hyperbolic manifolds obtained by Dehn filling on the figure eight knot complement and its sister, denoted $m004$ and $m003$ respectively in SnapPea notation. We will use the ideas described in the previous section to prove the following.

::: thm
[]{#closed_unique label="closed_unique"} There is an infinite sequence of hyperbolic Dehn fillings $M(a_i,b_i)$ on the figure eight knot complement $M=m004$ with $a_i^2+12b_i^2 \to  \infty$ such that if $N$ is any orientable hyperbolic 3-manifold with $\text{Vol} (N)=\text{Vol} (M(a_i,b_i))$ then $N$ is homeomorphic to $M(a_i,b_i)$. So the manifolds $M(a_i,b_i)$ are determined by their volumes, amongst all finite volume orientable hyperbolic 3-manifolds.
:::

For $m003$ and $m004$, the quadratic forms defined in equation ([\[eq1\]](#eq1){reference-type="ref" reference="eq1"}) are closely related to the quadratic form $$\label{eq10}Q_0(a,b) = a^2+ab+b^2 = |a+b \omega|^2$$ where $\omega = {1\over 2}(1-\sqrt{3} i )$ is a cube root of $-1$ satisfying $\omega^2-\omega+1=0$ and $\bar \omega = 1-\omega$. From the symmetries of the lattice $\mathbb{Z}+\mathbb{Z}\omega$, we have $$|a+b \omega| = | \omega^k(a+b \omega)| = | \omega^k(a+ b \bar \omega)| = | \omega^k(a+b-b \omega)|$$ for $k =0, 1, \ldots, 5$. Hence $Q_0$ has symmetry group $G_{Q_0} \cong D_6$ of order 12, and the orbit of $(a,b)$ under $G_{Q_0}$ is $$\label{eq11}\{ \pm(a,b), \pm(-b,a+b), \pm(-a-b,a), \pm (a+b,-b),\pm(b,a), \pm(-a,a+b) \}.$$

Now consider a maximal horospherical cusp torus for $m004$ and $m003$. In each case we choose the geometric basis for the peripheral homology used by SnapPea, consisting of two shortest simple closed geodesics. From Snap or SnapPy (or [@weeks_phd]) we have the following:

For $m004$, this torus has shortest closed geodesic of length 1, cusp shape $\tau = -2 \sqrt{3}i = 4 \omega -2$ and area $2 \sqrt{3}$. Hence, the $(a,b)$ geodesic has length squared $$\label{eq12}Q_1(a,b)= |a + b \tau|^2 = a^2 + 12 b^2 =Q_0(a-2b,4b) .$$ This quadratic form has symmetry group $G_{Q_1} = D_2$, given by $(a,b) \mapsto (\pm a, \pm b)$, and these all extend to symmetries of $m004$, so $G_{m004} = G_{Q_1}$.

For $m003$, the torus has shortest closed geodesic of length 2, cusp shape $\tau = \omega$ and area $2 \sqrt{3}$. Hence, the $(a,b)$ geodesic has length squared $$\label{eq13}Q_2(a,b)= |2a + 2b \omega|^2 = 4(a^2+ab+b^2) = 4Q_0(a,b) .$$ This quadratic form has symmetry group $G_{Q_2}=G_{Q_0} = D_6$ as described above. However, $G_{m003} = D_2$ is the subgroup given by $(a,b) \mapsto \pm(a,b), \pm(a+b,-b)$. (Note that any symmetry of $m003$ must preserve the homologically trivial longitude $(-1,2)$, hence must also preserve the orthogonal $(1,0)$ curve.)

::: prop
[]{#p_with_big_gap label="p_with_big_gap"} Given any integer $g >0$ there exist infinitely many primes $p$ such that

1.  $p$ can be written as $Q_1(a,b)$ where $a,b$ are relatively prime integers, and if $p=Q_1(a,b)=Q_1(a',b')$ then $(a',b') = (\pm a, \pm b)$ (with 4 possible choices of signs),

2.  $p+k$ has no primitive integer representation as $Q_0(a,b)$ for $0<|k|\le g$,

3.  $p$ has no primitive integer representation as $Q_2(a,b)$.
:::

This follows from some elementary number theory.

::: lem
[]{#p=1mod12 label="p=1mod12"} If $p$ is a prime congruent to $1$ modulo $12$, then $p$ can be written uniquely in the form $p= Q_1(a,b) = a^2 + 12 b^2$ where $a,b$ are relatively prime positive integers.
:::

::: proof
*Proof.* Euler showed that each prime $p \equiv 1 \bmod 3$ can be written uniquely in the form $p = x^2 + 3 y^2$ with $x,y$ positive integers (see for example [@cox Chapter 1]). If $p \equiv 1 \bmod 12$, then taking congruences $\bmod 4$ shows that $y$ is even. ◻
:::

::: lem
[]{#p=5mod6 label="p=5mod6"} If $p$ is a prime congruent to $5$ modulo $6$ and $p$ divides $n$, then $n$ has no representation $n = Q_0(a,b)=a^2 + ab + b^2$ with $a,b$ relatively prime integers.
:::

::: proof
*Proof.* Let $p$ be an odd prime dividing $n = a^2 + ab + b^2$ with $a,b$ relatively prime integers. Then by Lemma [\[discr_quad_res\]](#discr_quad_res){reference-type="ref" reference="discr_quad_res"}, $-3$ is a quadratic residue mod $p$. If $p \ne 3$, it follows that $p \equiv 1 \bmod 6$ by Quadratic Reciprocity (see e.g. [@HaWr Thm 96]). ◻
:::

::: proof
*Proof of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}.* We use the previous lemmas together with the Chinese remainder theorem and Dirichlet's theorem on primes in arithmetic progressions.

For $i=0,1,2$ let $$S_i = \{ Q_i(a,b) : a,b \text{ are relatively prime integers} \}.$$

Given any integer $g>0$, let $p_1, p_2, \ldots, p_{2g}$ be distinct primes congruent to $5$ modulo $6$. Consider the integers $n$ satisfying the congruences $$\begin{aligned}
 n-i &\equiv& 0 \bmod p_i   \qquad\text{ for }1 \le i \le g,\\
  n+i &\equiv& 0 \bmod p_{g+i} \quad\text{ for }1 \le i \le g, \text{ and }\\
 n &\equiv& 1 \bmod 12.
 
\end{aligned}$$ By the Chinese Remainder Theorem, these have a general solution of the form $$\label{eq14}
n \equiv n_0 \bmod 12 p_1 \ldots p_{2g}.$$ By Dirichlet's theorem on primes in arithmetic progressions, there are infinitely many solutions to ([\[eq14\]](#eq14){reference-type="ref" reference="eq14"}) such that $n$ is a prime, say $p$. For such $p$ we have $p \equiv 1 \bmod 12$ so $p \in S_1$ by Lemma [\[p=1mod12\]](#p=1mod12){reference-type="ref" reference="p=1mod12"}. Further $p+i$ is divisible by $p_i$ and $p-i$ is divisible by $p_{g+i}$ for $1 \le i \le g$. Hence $p+i \notin S_0, p-i \notin S_0$ for $1\le i \le g$ by Lemma [\[p=5mod6\]](#p=5mod6){reference-type="ref" reference="p=5mod6"}. Finally, $p \notin Q_2$ since $p$ is odd. Hence $p$ satisfies all the conditions (i)--(iii) of the proposition. ◻
:::

We now combine Proposition [\[few_with_symm\]](#few_with_symm){reference-type="ref" reference="few_with_symm"} and Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"} to prove the main theorem of this section.

::: proof
*Proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}.* The quadratic forms $Q_1$ and $Q_2$ for $m004$ and $m003$ considered above give the squares of geodesic lengths on a cusp torus with area $2 \sqrt{3}$. Hence the corresponding normalised quadratic forms, used in Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}, are $$\hat Q_1(a,b) =  {1 \over 2 \sqrt{3}} Q_1(a,b) \text{ and } \hat Q_2(a,b) =  {1 \over 2 \sqrt{3}} Q_2 (a,b).$$

We now apply Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"} with gap size $g = 4 \sqrt{3} C$, where $C$ is the maximum of the constants $C_2$ for $m004$ and $m003$ given by Proposition [\[error_bound\]](#error_bound){reference-type="ref" reference="error_bound"}. This gives a sequence of primes $p_i \equiv1 \bmod 12$ with $p_i \to \infty$ and pairs $(a_i,b_i)$ of relatively prime integers with $p_i =a_i^2+12b_i^2$ satisfying the conditions of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}.

Then $\text{Vol} (m004(a,b)) = \text{Vol} (m004(a_i,b_i))$ implies that $Q_1(a,b)=Q_1(a_i,b_i)$ by Proposition [\[few_with_symm\]](#few_with_symm){reference-type="ref" reference="few_with_symm"}, hence $(a,b) = (\pm a_i, \pm b_i)$ by condition (i) of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}. But these solutions differ by symmetries of $Q_1$ that extend to symmetries of $m004$, so $m004(a,b)$ is homeomorphic to $m004(a_i,b_i)$.

Further, $\text{Vol} (m004(a_i,b_i)) = \text{Vol} (m003(a,b))$ implies that $Q_1(a_i,b_i)=Q_2(a,b)$. But this has no solutions by condition (iii) of Proposition [\[p_with_big_gap\]](#p_with_big_gap){reference-type="ref" reference="p_with_big_gap"}. Hence $m004(a_i,b_i)$ is uniquely determined by its volume amongst Dehn fillings on $m004$ and $m003$.

Cao and Meyerhoff [@CM] showed that the figure eight knot complement $m004$ and its sister $m003$ are the unique orientable cusped hyperbolic 3-manifolds of smallest volume $v_\omega$. The work of Jørgensen and Thurston (see [@Th], [@Gr]) shows that any sequence of closed hyperbolic 3-manifolds with volume approaching $v_\omega$ from below has a subsequence whose geometric limit is a cusped hyperbolic 3-manifold $M_\infty$ with volume $v_\omega$, and that the manifolds in the subsequence are obtained by Dehn filling on $M_\infty$. It follows that there exists $\epsilon >0$ such that if $N$ is any closed orientable hyperbolic 3-manifold with $v_\omega - \epsilon < \text{Vol} (N) <v_\omega$ then $N$ can be obtained by Dehn filling on $m003$ or $m004$. Now the result follows from the previous observations. ◻
:::
