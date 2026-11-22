---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-021-43-formulas-for-the-overlap-functions
section_title: "Formulas for the Overlap Functions"
section_number: 4.3
pages: 67-74
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.994
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Chalker and Mehlig were able to relate the overlap functions to expectations of functions involving all the eigenvalues. The eigenvalue distribution for the complex Ginibre ensemble is well-known. In fact it is one of the simplest of the various Gaussian ensembles. For example, as Chalker and Mehlig also point out in their paper, $$\label{eq:RD}
\mathcal{R}_N^{(1)}(z)\, =\, \frac{N}{\pi N!}\, e^{-N |z|^2} D_{N-1}(z)\, ,$$ where $D_{N-1}(z)$ equals the determinant of the $(N-1)$-dimensional square matrix $\mathcal{D}_N(z)$ where the matrix entries are best indexed for $j,k \in \{0,\dots,N-2\}$ as $$_{jk}\, =\, \left(\frac{N^{j+k+4}}{\pi^2 (j!) (k!)}\right)^{1/2} \int_{\mathbb{C}} \overline{\lambda}^j \lambda^k
|z-\lambda|^2 \exp(-N|\lambda|^2)\, 
d^2\lambda\, .$$ By rotational invariance of all the terms in the integrand other than $|z-\lambda|^2$, which is only quadratic, it happens that $\mathcal{D}_N(z)$ is a tridiagonal matrix. Hence, Chalker and Mehlig point out that it is easy to derive a recursion relation for $D_{N-1}(z)$. It is easier to define a new quantity $D_{N-1}(\sigma^{-2},z) = D_{N-1}(\sigma^{-1} N^{-1/2} z)$. Then they show $$\label{eq:Dr}
D_{n+1}(\sigma^{-2},z)\, =\, (\sigma^{-2}|z|^2+n+1) D_n(\sigma^{-2},z) - \sigma^{-2} n |z|^2 D_{n-1}(\sigma^{-2},z)\, ,$$ and $D_0(\sigma^{-2},z)=1$, $D_1(\sigma^{-2},z) = 1+\sigma^{-2}|z|^2$. It turns out to be easy to solve this recurrence relation, and Chalker and Mehlig give the formula $$\label{eq:D}
D_{N-1}(\sigma^{-2},z)\, =\, (N-1)! \sum_{n=0}^{N-1} \frac{(\sigma^{-2}|z|^2)^n}{n!}\, ,$$ which is the partial sum for the series for $(N-1)! \exp(\sigma^{-2}|z|^2)$. In order to obtain $D_{N-1}(z)$ one must take $\sigma^{-2}=N$. One sees that the dividing line is $|z|<1$ versus $|z|>1$, as to whether enough terms have been included in the partial sum to get essentially $\exp(N|z|^2)$ or not. From this it follows that the measure $\mathcal{R}_N^{(1)}(z)\, d^2z$ converges weakly to $\pi^{-1} \mathbf{1}_{[0,1]}(|z|^2)\, d^2z$, as $N \to \infty$. The reason for going into so much detail in this example is that the other examples are similar, but harder. In fact, some of the formulas are so complicated that so far they have eluded any explicit, exact formula (at least as far as we have been able to find in the literature).

Another easy result which follows from these explicit formulas, but which does not appear in the paper of Chalker and Mehlig, is the scaling formula near the unit circle. Let us record this for later reference.

::: lemma
[]{#lem:circle label="lem:circle"} For any $u \in \mathbb{R}$, $$\mathcal{R}_N^{(1)}(1-N^{-1/2}u)\, \stackrel{N\to\infty}{\longrightarrow}\, \pi^{-1} \Phi(2u)\quad 
\text{ where }\quad
\Phi(x)\, =\, \frac{1}{\sqrt{2\pi}}\, \int_{-\infty}^{x} e^{-z^2/2}\, dz\, .$$
:::

::: proof
*Proof.* Given the exact formula, $$\mathcal{R}_N^{(1)}(1-N^{-1/2}u)\, =\, \pi^{-1} \exp(-N+N^{1/2}u) \sum_{n=0}^{N-1} \frac{(N-N^{1/2}u)^n}{n!}\, ,$$ make the substitution $n=N-N^{1/2}x$ for $x \in \{N^{-1/2},2N^{-1/2},\dots,N^{1/2}\}$ and use Stirling's formula. Then replace the sum by an appropriate integral in $x$ (of which it is a Riemann sum approximation with $\Delta x=N^{-1/2}$) by using the rigorous Euler-Maclaurin summation formula. ◻
:::

We may note that using the Euler-Maclaurin summation formula, one may obtain more terms as corrections of the leading-order term, just as one does for the asymptotic series in Stirling's formula. Additionally, one may obtain formulas that are valid for more values of $u$: one may obtain an asymptotic formula for $\mathcal{R}_N^{(1)}(z)-\pi^{-1}$ assuming that $|z|-1<CN^{-1/2}$ for some $C$, and another formula for $\mathcal{R}_N^{(1)}(z)$ assuming that $|z|-1>-CN^{-1/2}$ for some $C$: the difference in being whether one chooses to asymptotically evaluate the terms which are present in the partial sum for $\exp(N|z|^2)$ or whether one chooses to asymptotically evaluate the terms which are absent in that partial sum.

## More Involved Formulas:

The formula for $\mathcal{O}_N^{(1)}$ is not much more complicated than the formula for $\mathcal{R}_N^{(1)}$, and Chalker and Mehlig gave the explicit answer. It turns out that one may write $\mathcal{O}_N^{(1)}$ similarly to $\mathcal{R}_N^{(1)}$ as $$\begin{gathered}
\mathcal{O}_N^{(1)}(z)\, 
=\, \frac{N}{\pi N!}\, \exp(-N|z|^2) G_{N-1}(z)\quad 
\text{ where }\quad
G_{N-1}(z)\, =\, \det[\mathcal{G}_{N-1}(z)]\, ,\\
\forall j,k \in \{0,\dots,N-2\}\, ,\quad \\
[\mathcal{G}_{N-1}(z)]_{jk}\, =\,  \left(\frac{N^{j+k+4}}{\pi^2 (j!) (k!) }\right)^{1/2} \int_{\mathbb{C}} \overline{\lambda}^j \lambda^k
(N^{-1}+|z-\lambda|^2) \exp(-N|\lambda|^2)\, 
d^2\lambda\, .
\end{gathered}$$ The matrix $\mathcal{G}_{N-1}(z)$ is also tridiagonal for the same reason as $\mathcal{D}_{N-1}(z)$. In particular, there is again a recursion relation for $G_{N-1}(z)$. Defining $G_{N-1}(\sigma^{-2},z) = G_{N-1}(\sigma^{-1}N^{-1/2}z)$, one may see the recursion formula $$\begin{split}
G_{n+1}(\sigma^{-2},z)\, \\
&=\, [\mathcal{G}_n(\sigma^{-2},z)]_{nn} G_{n}(\sigma^{-2},z) - [\mathcal{G}_n(\sigma^{-2},z)]_{n,n-1} [\mathcal{G}_n(\sigma^{-2},z)]_{n-1,n} G_{n-1}(\sigma^{-2},z)\\
&=\, (\sigma^{-2}+n+2) G_{n}(\sigma^{-2},z)  - \sigma^{-2} n |z|^2 G_{n-1}(\sigma^{-2},z)\, ,
\end{split}$$ with $G_0(\sigma^{-2},z) = 1$ and $G_1(\sigma^{-2},z) = 2 + \sigma^{-2}|z|^2$.

::: lemma
[]{#lem:G label="lem:G"} The exact solution to the recursion relation when $\sigma^{-2}=N$ is $$\label{eq:lemG}
G_N(z)\, =\, (N-1)!\, \sum_{n=0}^{N-1} (N-n) \, \frac{(N|z|^2)^n}{n!}\, .$$
:::

Using this formula, it is easy to see that $N^{-1} \mathcal{O}_N(z)\, d^2z$ converges weakly to $\pi^{-1} (1-|z|^2) \mathbf{1}_{[0,1]}(|z|^2)\, d^2z$, which is precisely the behavior that Chalker and Mehlig found by other techniques. We will return to their approach, shortly. For now, let us state the analogue of Lemma [\[lem:circle\]](#lem:circle){reference-type="ref" reference="lem:circle"}.

::: corollary
For any $u \in \mathbb{R}$, $$\label{eq:Ocirc}
\mathcal{O}_N^{(1)}(1-N^{-1/2}u)\, \sim\, \frac{N^{1/2}}{\pi}\, \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2u\Phi(-2u)\right]\, ,\quad \text{ as $N \to \infty$.}$$
:::

::: proof
*Proof.* The proof is perfectly analogous to the proof of Lemma [\[lem:circle\]](#lem:circle){reference-type="ref" reference="lem:circle"}, except we start with Lemma [\[lem:G\]](#lem:G){reference-type="ref" reference="lem:G"} instead of equation ([\[eq:D\]](#eq:D){reference-type="ref" reference="eq:D"}). ◻
:::

One also needs the two point function $\mathcal{O}_N^{(2)}$ in order to obtain any interesting moments. The two-point function for the eigenvalues is easier to start with since its distribution is known exactly. Using ideas related to the theory of orthogonal polynomials, one may see that $\mathcal{R}_N^{(2)}(z_1,z_2)$ is determinantal. The canonical general reference for this is [@Mehta]. One may write the formula as $$\mathcal{R}_N^{(2)}(z_1,z_2)\, =\, \pi^{-2} e^{-N|z_1|^2} e^{-N|z_2|^2}
\det\left(K_N(z_j \overline{z}_k)\right)_{j,k=1}^{2}\quad \text{ for }\quad
K_N(z)\, =\, \sum_{n=0}^{N-1} \frac{(Nz)^n}{n!}\, .$$ From this one may determine the following asymptotics, proved in the same way as before.

::: lemma
Define $\mathcal{C}_N^{(2)}(z_1,z_2) = \mathcal{R}_N^{(2)}(z_1,z_2) - \mathcal{R}_N^{(1)}(z_1) \mathcal{R}_N^{(1)}(z_2)$, the corrected correlation function for the eigenvalues. Then for any fixed $u_1,u_2 \in \mathbb{C}$ $$\mathcal{C}_N^{(2)}(1-N^{-1/2}u_1,1-N^{-1/2}u_2)\, 
\sim\, \pi^{-2} e^{-|u_1-u_2|^2} |\Phi(-u_1-\overline{u}_2)|\, ,$$ where the definition of $\Phi$ is extended to the complex plane as $$\Phi(-u)\, =\, (2\pi)^{-1/2} e^{-u^2/2} \int_{0}^{\infty} e^{-x^2/2} e^{-ux}\, dx$$
:::

We have stated a somewhat precise limit for $\mathcal{R}_N^{(2)}$, but we do not know how to get a precise limit for $\mathcal{O}_N^{(2)}$. Let us state one of Chalker and Mehlig's main results as a conjecture. In other words, they give a good argument for the calculation of $\mathcal{O}_N^{(2)}$ which is highly plausible on the basis of mathematical reasoning, but to the best of our knowledge their result has not yet been fully rigorously proved.

::: conj
\(i\) For any two points $z_1,z_2$ such that $|z_1|<1$, $|z_2|<1$ and $|z_1-z_2|>0$, $$\mathcal{O}_N^{(2)}(z_1,z_2)\, \stackrel{N\to\infty}{\longrightarrow}\,
-\frac{1}{\pi^2}\cdot \frac{1-z_1\overline{z}_2}{|z_1-z_2|^4}\, .$$ (ii) For any $\omega \in \mathbb{C}$ and $z$ such that $|z|<1$, $$\begin{gathered}
\label{eq:CM2}
N^{-2} \mathcal{O}_N^{(2)}\Big(z+\frac{1}{2}N^{-1/2}\omega,z-\frac{1}{2}N^{-1/2}\omega\Big)\,
\sim\, -\pi^{-2} (1-|z|^2)\, \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, ,\qquad \\ \text{ as $N \to \infty$.}
\end{gathered}$$
:::

Importantly, there is no asymptotic formula for $z_1$ and $z_2$ near the boundary of the circle. For all the other cases, this regime gives lower-order corrections, beyond the leading order.

Chalker and Mehlig's approach is beautiful and compelling. They calculated an explicit formula for $\mathcal{O}_N^{(2)}(0,z)$. Note, for instance, that $\mathcal{R}_N^{(2)}(0,z) = \pi^{-1} (\mathcal{R}_N^{(1)}(z)-\pi^{-1}e^{-|z|^2})$, so the formula simplifies when one of the arguments is $0$. A similar fact holds for $\mathcal{O}_N^{(2)}(z_1,z_2)$, even though it seems that it is not determinantal like $\mathcal{R}_N^{(2)}(z_1,z_2)$. Then, Chalker and Mehlig considered a universality-type argument to see how the functional form should behave under transformations of the point $0$ to other places on the circle. Their argument is also a universal argument, applying to more ensembles than just the complex Ginibre ensemble, but we will continue to consider just the complex Ginibre ensemble, here.

The second part of their argument is the key to their formula. The function $\mathcal{O}_N^{(2)}(z_1,z_2)$ may be expressed as the expectation of a non-local function of all the eigenvalues of $A_n$. Chalker and Mehlig observe that the function depends mainly on the eigenvalues in a core small area around $z_1$ and $z_2$. For this core, the distribution of the eigenvalues should be universal, not depending on the proximity of $z_1$ and $z_2$ to the boundary of the disk, as long as they are not near the boundary. Then outside the core there is a self-averaging contribution of all the other eigenvalues, which may be reduced to a Riemann integral approximation, and calculated. That part does depend on the geometry of the point configuration in the disk, but it is easily calculated. Putting these two parts together with their formula for $\mathcal{O}_N^{(2)}(0,z)$, they were able to arrive at ([\[eq:CM2\]](#eq:CM2){reference-type="ref" reference="eq:CM2"}).

The reader is advised most strongly to consult their beautiful paper.

Now we want to explain briefly the first part of their argument since it is a basis for a different proposal we have for how to prove their conjecture. Chalker and Mehlig point out that $\mathcal{O}_N^{(2)}(z_1,z_2)$ may be calculated as the determinant of a 5-diagonal matrix. In fact, it is easier to start with $\mathcal{R}_N^{(2)}(z_1,z_2)$: $$\mathcal{R}_N^{(2)}(z_1,z_2)\, 
=\, \frac{N^3}{\pi^2 N!}\, |z_1-z_2|^2 e^{-N|z_1|^2} e^{-N|z_2|^2} F_{N-2}(z_1,z_2)\, ,$$ where $F_{N-2}(z_1,z_2)$ equals the determinant of the $(N-2)$-dimensional square matrix $\mathcal{F}_{N-2}(z_1,z_2)$, where $$_{jk}\, =\, \left(\frac{N^{j+k+6}}{\pi^2 (j+1)! (k+1)! }\right)^{1/2} \int_{\mathbb{C}} \overline{\lambda}^j \lambda^k |z_1-\lambda|^2 |z_2-\lambda|^2 
\exp(-N|\lambda|^2)\, d^2\lambda\, ,$$ for $j,k=0,\dots,N-3$. Then the formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ is $$\mathcal{O}_N^{(2)}(z_1,z_2)\, 
=\, -\frac{N^2}{\pi^2 N!}\, e^{-N|z_1|^2} e^{-N|z_2|^2} H_{N-2}(z_1,z_2)\, ,$$ where $H_{N-2}(z_1,z_2)$ equals the determinant of the $(N-2)$-dimensional square matrix $\mathcal{H}_{N-2}(z_1,z_2)$, where $$\begin{gathered}
_{jk}\, =  \, \left(\frac{N^{j+k+6}}{\pi^2 (j+1)! (k+1)! }\right)^{1/2} \\  \int_{\mathbb{C}} \overline{\lambda}^j \lambda^k \Big[|z_1-\lambda|^2 |z_2-\lambda|^2 
+ N^{-1} \left(\overline{z}_1 - \overline{\lambda}\right)(z_2-\lambda)\Big]
\exp(-N|\lambda|^2)\, d^2\lambda\, ,
\end{gathered}$$ for $j,k=0,\dots,N-3$. These are naturally 5-diagonal because of rotational invariance. However, notice that if $z_1=0$ or $z_2=0$ then they become tri-diagonal again. Hence, they are more easily calculable in that case. That is why $\mathcal{O}_N^{(2)}(0,z)$ is calculable.

In a later section, we are going to propose another method to proceed. We will write down the recursion relation for the 5-diagonal matrix, which is harder than for a tridiagonal matrix. Then, even if the formula is not exactly solvable, we argue that it should be asymptotically solvable. We give more details in a later section, in particular carrying out the asymptotic approach for the easier problem of calculating $\mathcal{R}_N^{(2)}(z)$ (which we may check against the exact solution).
