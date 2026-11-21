---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-012-45-proof-of-1123-126-and-determination-of-its-mu
section_title: "Proof of 1[1.23, 1.26] and determination of its multiplicity"
section_number: 4.5
pages: 29-32
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.959
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
[]{#subsec:subinterval4 label="subsec:subinterval4"}

::: prop
[]{#prop:subinterval4 label="prop:subinterval4"} There is an eigenvalue in the interval $[1.23, 1.26]$.
:::

::: proof
*Proof.* Let $a = 1.23$ and $b = 1.26$. We define the test functions $h,g$ as in [\[eq:gh_hermite\]](#eq:gh_hermite){reference-type="eqref" reference="eq:gh_hermite"}. For this, we choose the sequence of rational numbers $\{s_n\}_{n=0}^{19}$ such that the two polynomials $$\begin{aligned}
u(y) &= \sum_{n=0}^{19} s_n L_n^{(-1/2)}(y),\\
v(y) &= \sum_{n=0}^{19} (-1)^n s_n L_n^{(-1/2)}(y),
\end{aligned}$$ meet the following conditions:

-   $u(y)$ has a double root at $4190$.

-   $v(y)$ possesses double roots at 1.87, 4.89, 9.46, 13.81, 19.97, 28.86, 39.99, 54.93 and additionally fulfills the conditions $v(0)=1$ and $v(b-1/4) = -1/10^5$.

There is a unique choice of $\{s_n\}_{n=0}^{17}$.

See the Sage notebook `subinterval4-1.ipynb` for the necessary numerical computations below. We can easily confirm that $u$ and $v$ have roots with the specified multiplicities at the designated locations.

We need to ensure that $h$ and $g$ satisfy the following conditions:

1.  $\ff(x)\geq 0$ for every $x \geq 0$.

2.  $\hatf(r(\la))\leq c=0.00141$ for every $\la \in [a, b]$.

3.  $\hatf(r(\la))\leq 0$ for every $\la \geq b$.

Again, we apply Sturm's theorem to count the number of roots of a polynomial over a given interval.

\(1\) We can check that $u(0)> 0$ and $u$ has a unique root at $4190$ in the interval $[0, \infty)$, which is a double root. By confirming that $u''(4190)$ is greater than zero, we can establish that both $u$ and $\ff$ maintain non-negativity throughout the interval $[0,\infty)$.

\(2\) We verify that $2v'-2v$ does not have a root in $[a-1/4, b-1/4]$. This implies that the maximum of $\hatf$ on the interval $[r(a),r(b)]$ is achieved at the endpoints. Using interval arithmetic, we can check that $\hatf(r(\la)) \leq  0.00141$ for $\la\in [a, b]$. Note that $\hatf(r(a)) \approx 0.00140988$ and $\hatf(r(b)) \approx -6.03506\times 10^{-6}$.

\(3\) We verify that $v$ has precisely $8$ distinct zeros, all of which are double zeros, in the interval $[b-1/4,\infty)$. We can confirm that $v''<0$ at all those roots, and $v(b-1/4)<0$. Consequently, we deduce that $v$ does not change sign over $[b-1/4,\infty)$ and, hence, $\hatf\leq 0$ over the interval $[r(b),\infty)$.

With the above test functions $h,g$, we will establish the following inequalities using interval arithmeti: $$\mathcal{I} \geq 1.08088, \quad \mathcal{G} \geq 1.25565, \quad -\hatf(r_0) \geq -2.33608.$$

To find a bound for $\calI$, we separate the integral into two parts $\calI = \calI_1+\calI_2$ : $$\begin{aligned}
\calI_1 & = 2(g(\X)-1) \int_0^{100} r \hatf(r) \tanh(\pi r) dr,\\
\calI_2 & = 2(g(\X)-1) \int_{100}^\infty r \hatf(r) \tanh(\pi r) dr.
\end{aligned}$$ Using interval arithmetic, we can find $$\calI_1 \geq 1.08088.$$ For the remaining part, we have $$\calI_2 = 2(g(\X)-1) \int_{100}^\infty r \hatf(r) \tanh(\pi r) dr\leq 2(g(\X)-1) \int_{100}^\infty r \hatf(r)dr,$$ which is negligible in comparison to $\calI_1$ as in the proof of .

Now we consider $\calG$. Because $\ff(x)\geq 0$ for every $x \geq 0$, $$\calG \geq \frac{1}{\sqrt{2\pi}}\sum_{\{\gamma\} \in P} \frac{\ell(\gamma)}{2\sinh(\ell(\gamma)/2)} \ff(\ell(\gamma)),$$ where $P$ is any subset of $\calC(\Gamma)$. By employing interval arithmetic to sum over conjugacy classes with the two shortest lengths described in , we obtain $$\calG \geq 1.25565.$$

Finally, we can check that $\hatf(r_0)\leq 2.33608$ using interval arithmetic.

Because $\hatf(r(\la))\leq 0$ for $\la \geq b$, the Selberg trace formula gives $$\calI+\calG = \calS = \sum_{n=1}^{\infty}\hatf(r_n)
\leq 
\hatf(r_0)+ \sum_{\substack{n=1 \\ \la_n\in [a,b]}}^{\infty}
\hatf(r_n).$$ Let $m(a,b)$ be the number of eigenvalues of the Laplacian in the interval $[a,b]$ counting multiplicity. From $\hatf(r(\la))\leq c$ for $\la\in [a,b]$, we obtain $$\calI+\calG - \hatf(r_0)  \leq  c m(a,b),$$ which implies $$m(a,b) \geq \frac{1}{c}\left(\calI+\calG - \hatf(r_0) \right) \geq 0.3237.$$ This proves the proposition. ◻
:::

::: prop
[]{#prop:subinterval4-2 label="prop:subinterval4-2"} The number of eigenvalues in the interval $[1.23,1.26]$ counting multiplicity is 7.
:::

::: proof
*Proof.* Let $a = 1.23$ and $b=1.26$. We define the test functions $h,g$ as in [\[eq:gh_hermite\]](#eq:gh_hermite){reference-type="eqref" reference="eq:gh_hermite"}. We choose the sequence of rational numbers $\{s_n\}_{n=0}^{17}$ such that the two polynomials $$\begin{aligned}
u(y) &= \sum_{n=0}^{17} s_n L_n^{(-1/2)}(y),\\
v(y) &= \sum_{n=0}^{17} (-1)^n s_n L_n^{(-1/2)}(y),
\end{aligned}$$ meet the following conditions:

-   $u(y)$ has a simple root at $33$ and a double root at $624$.

-   $v(y)$ possesses double roots at 1.91, 4.97, 9.92, 15.56, 22.31, 32.18, 46.81 and additionally fulfills the condition $v(a-1/4) = 1$.

Again, there is a unique choice of $\{s_n\}_{n=0}^{17}$.

See the Sage notebook `subinterval4-2.ipynb` for the necessary numerical computations below. We can easily confirm that $u$ and $v$ have roots with the specified multiplicities at the designated locations.

We need to ensure that they satisfy the following conditions:

1.  $\ff(x)\leq 0$ for every $x \geq \sys(\X)$.

2.  $\hatf(r(\la))\geq c=0.55299$ for every $\la \in [a, b]$.

3.  $\hatf(r(\la))\geq 0$ for every $\la \geq b$.

We can verify these statements similarly to the method described in the proof of . Also we have the following inequalities: $$\mathcal{I} \leq 16.242, \quad \mathcal{G} \leq -0.162, \quad -\hatf(r_0) \leq -11.826.$$

Because $\hatf(r(\la))\geq 0$ for $\la \geq b$, the Selberg trace formula gives $$\calI+\calG = \calS  =  \sum_{n=1}^{\infty}\hatf(r_n) \geq
\hatf(r_0) + \sum_{\substack{n=1 \\ \la_n\in [a,b]}}^{\infty}\hatf(r_n).$$ From $\hatf(r(\la))\geq c$ for $\la\in [a,b]$, we obtain $$\calI+\calG - \hatf(r_0)  \geq  c m(a,b)$$ where $m(a,b)$ denote the number of eigenvalues of the Laplacian in the interval $[a,b]$ counting multiplicity. Therefore, $m(a,b)$ is less than or equal to $$\frac{1}{c}\left(\calI+\calG - \hatf(r_0) \right) \leq \frac{1}{0.553}(16.242 - 0.162 - 11.826)< 7.70.$$ This implies that the multiplicity is less than 8. From , we know the multiplicity is positive. By Lemma [\[prop:mult7\]](#prop:mult7){reference-type="ref" reference="prop:mult7"}, it must be 7, which proves the proposition. ◻
:::
