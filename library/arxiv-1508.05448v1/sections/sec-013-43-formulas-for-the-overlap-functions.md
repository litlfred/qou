---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-013-43-formulas-for-the-overlap-functions
section_title: "Formulas for the Overlap Functions"
section_number: 4.3
pages: 67-89
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.992
doc_brief: "Concentration of Measure Techniques and Applications — 25 sections: Front matter; Biographical Sketch; Acknowledgments"
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

# Moments and Constraints on the Overlap Functions

An ideal situation would be to find an explict sum-formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$, just as Lemma [\[lem:G\]](#lem:G){reference-type="ref" reference="lem:G"} provides for $\mathcal{O}_N^{(1)}(z)$, but so far, this has not been discovered. In the next section, we will suggest a rigorous approach which may work to give the asymptotics, even when no explicit formula is known. For now, let us state the constraints imposed by the moment formula from before.

Recall from ([\[eq:mnpq\]](#eq:mnpq){reference-type="ref" reference="eq:mnpq"}) for any nonnegative integers $p$ and $q$, $$m_N((p);(q))\, =\, \int_{\mathbb{C}} z^p \overline{z}^q \mathcal{O}_N^{(1)}(z)\, d^2z 
+ \int_{\mathbb{C}} \int_{\mathbb{C}} z^p \overline{w}^q \mathcal{O}_N^{(2)}(z,w)\, d^2z\, d^2w\, .$$ Moreover, from the discussion at the end of Section [\[subsec:Argument\]](#subsec:Argument){reference-type="ref" reference="subsec:Argument"}, $m_N((p);(q))$ equals $0$ unless $p=q$, and as noted at the end of Section [\[sec:Expected\]](#sec:Expected){reference-type="ref" reference="sec:Expected"}, this is already reflected in the rotational invariance properties of $\mathcal{O}_N^{(1)}(z)$ and $\mathcal{O}_N^{(2)}(z_1,z_2)$. Therefore, specializing, we see that $$\label{eq:MoTot}
\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z 
+ \int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\, =\, 1\, ,$$ for each nonnegative integer $p$. This is the constraint formula. Let us now analyze this formula, starting with the leading order terms, and going down in order.

## Cancelling Divergences at Leading Order

For any fixed $z$ with $|z|<1$, we have $$\mathcal{O}_N^{(1)}(z)\, \sim\, N \pi^{-1} (1-|z|^2)\, ,$$ and the corrections are actually exponentially small in $N$ (since they arise as the deep part of the right tail of the series for the exponential). Therefore, integrating, we obtain the leading-order part of the contribution from $\mathcal{O}_N^{(1)}(z)$ from the formula above $$\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z\, \sim\, N \pi^{-1} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\, d^2z\, .$$ The corrections to this formula are not exponentially small, incidentally. This is because the formula for $\mathcal{O}_N^{(1)}(z)$ is not exponentially close to the exact formula for all $z$ in the complex plane. For a fixed $|z|>1$ it is easy to see that $\mathcal{O}_N^{(1)}(z)$ is exponentially small (hence exponentially close to the approximating function of $0$ there). That is because one only has the series for the exponential up to a small number of terms, deep in the left tail. Near the circle, there are algebraic corrections, not exponential ones.

Nevertheless, let us note that, by making a polar decomposition, $z=r e^{i\theta}$, we obtain $$N \pi^{-1} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\, d^2z\, 
=\, N \int_0^1 t^p (1-t)\, dt\, =\, \frac{N}{(p+1)(p+2)}\, .$$ Let us see how this cancels with the leading-order part of the $\mathcal{O}_N^{(2)}$ integral.

We will use Chalker and Mehlig's formula here for the leading-order part, even though we do not yet know the corrections for the lower-order part near the circle. Then we get $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\\
\sim\, - \int_{\mathbb{C}} \int_{\mathbb{C}} \left(z+\frac{\omega}{2N^{1/2}}\right)^p \left(\overline{z}-\frac{\overline{\omega}}{2N^{1/2}}\right)^p N^2 \pi^{-2} (1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\,\\ \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, N^{-1} d^2\omega\, d^2z\, ,
\end{gathered}$$ where the $N^{-1}$ associated to the volume-element $d^2\omega$-times-$d^2z$ is to account for the Jacobian of the transformation from $(z_1,z_2)$ to $(z,\omega)$. Now we will begin to separate this formula into even another decomposition into leading terms, and sub-leading terms. This is because, in the formulas $z_1^p = (z+\frac{1}{2}N^{-1/2}\omega)^p$ and $\overline{z}_2^p = (\overline{z}-\frac{1}{2}N^{-1/2}\overline{\omega})^p$, clearly the leading order arises by ignoring the contributions of $\omega$ which each are accompanied by negative powers of $N$. We really obtain, what we might call the "leading order, leading order" term: $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,
\sim\, \\ - N \pi^{-2} \int_{\mathbb{C}} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\, \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, N^{-1} d^2\omega\, d^2z\, .
\end{gathered}$$ Then it is easy to see that this splits. The integral over $\omega$ is $$\int_{\mathbb{C}} \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\, d^2\omega\,
=\, \pi \int_0^{\infty} \frac{1-(1+t)e^{-t}}{t^2}\, dt\,
=\, \pi \int_0^{\infty} \frac{1}{t^2} \left(\int_0^t s e^{-s}\, ds\right)\, dt\, .$$ Integrating-by-parts, it is easy to see that this gives $\pi$. Therefore, we end up with the exact negative of the leading order contribution by $\mathcal{O}_N^{(1)}$: $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,
\sim\, - N \pi^{-1} \int_{\mathbb{C}} |z|^{2p}(1-|z|^2) \mathbf{1}_{[0,1)}(|z|^2)\,  d^2z\, \\ =\, -\frac{N}{(p+1)(p+2)}\, .
\end{gathered}$$ The fact that these two terms cancel is good, because each diverges, separately; whereas, according to the formula, the exact answer is supposed to be $1$.

## The Sub-Leading Contribution from $\mathcal{O}_N^{(1)}$ {#subsec:sLO1}

For the first integral, we are fortunate that the exact correction is known near the circle. We will not attempt to keep track of the exponentially-small corrections which are present away from the circle. Near the circle, the exact corrections are relevant because they are not exponentially small.

Using Corollary 4.3, we know that $$\begin{gathered}
\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z
- \frac{N}{(p+1)(p+2)}\, =\,\\ \frac{N^{1/2}}{\pi}\, \int_{\mathbb{C}} \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2 u \Phi(-2u)\right]\Bigg|_{u = N^{1/2} (1-|z|)} |z|^{2p}\, d^2z
+ o(1)\, ,
\end{gathered}$$ where the small term $o(1)$ means that the remainder converges to $0$ as $N \to \infty$. This remainder includes exponentially small corrections to $\mathcal{O}_N^{(1)}(z)$ away from the circle, as well as the systematic correction terms to the leading-order behavior near the circle that arise from the Euler-Maclaurin series. The reason that these correction terms to the Euler-Maclaurin summation formula are $o(1)$ will arise momentarily: even the leading order term is only order-1, constant.

Making the polar decomposition of $z$ and then rewriting $r = 1-N^{-1/2}u$ so that $dr=N^{-1/2}\, du$ (and reversing orientation of the integral), we have $$\begin{split}
\int_{\mathbb{C}} |z|^{2p} \mathcal{O}_N^{(1)}(z)\, d^2z
- \frac{N}{(p+1)(p+2)}\, \\
=\, 2 \int_{-\infty}^{N^{1/2}} \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2 u \Phi(-2u)\right](1-N^{-1/2}u)^{2p+1}\, du+ o(1)\\
=\, 2 \int_{-\infty}^{\infty} \left[\frac{e^{-2u^2}}{\sqrt{2\pi}} - 2 u \Phi(-2u)\right]\, du+ o(1)\, .
\end{split}$$ In particular, this correction is independent of $p$, modulo vanishingly small remainder terms which are accumulated in the $o(1)$. Rewriting $u=x/2$ and integrating by parts gives a constant which is equal to $3/2$.

We will not be able to make it to the order-1, constant terms in the $N\to \infty$ asymptotics series (in decreasing powers of $N$). The reason is that for $\mathcal{O}_N^{(2)}$, we do not have sufficiently precise asymptotics to get to that level. Instead, what we will do next is to consider what constraints the formula for the moments imposes on $\mathcal{O}_N^{(2)}$.

## Sub-Leading Divergences in the $\mathcal{O}_N^{(2)}$ Term

We have now accounted for all the non-vanishing contributions from the $\mathcal{O}_N^{(1)}$ term. The leading-order divergence cancels with the leading-order divergence of the $\mathcal{O}_N^{(2)}$ term. The sub-leading order part of the $\mathcal{O}_N^{(1)}$ contribution to the moment is already order-1, constant, and it is independent of $p$. It equals $3/2$. Note that the moment itself is also independent of $p$, it is $1$.

Since we do not know the actual formula for $\mathcal{O}_N^{(2)}$, our plan for this section is to consider the proposed formula for $\mathcal{O}_N^{(2)}$ in the bulk. That still leads to one other divergent contribution, diverging logarithmically in $N$. What this must mean is that in the formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ for $z_1$ and $z_2$ close, and both near the circle, there must be an edge correction, which leads to a counter-balancing divergence. This is what we explain in some more detail, now. This subsection is detailed and technical.

We consider the proposed formula for $\mathcal{O}_N^{(2)}$ that Chalker and Mehlig derived. This is the correct formula in the bulk, following the argument of their paper, although there is a lower-order correction near the circle. We will not include the correction on the circle. Instead our calculations will show constraints that must be satisfied for this correction formula. We use $z_1 = z+\frac{1}{2}N^{-1/2}\omega$ and $z_2 = z-\frac{1}{2}N^{-1/2}\omega$ so that $$z_1 \overline{z}_2\,
=\, |z|^2 + \frac{i \mathrm{Im}[\omega \overline{z}]}{N^{1/2}} - \frac{|\omega|^2}{4N}\, .$$ Therefore, using the bulk formula we would have $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,\\
\approx\, -\frac{N^2}{\pi^2} \int_{\mathbb{C}} \int_{\mathbb{C}} \left[|z|^2 + \frac{i \mathrm{Im}[\omega \overline{z}]}{N^{1/2}} - \frac{|\omega|^2}{4N}\right]^p
\left(1 -  \left[|z|^2 + \frac{i \mathrm{Im}[\omega \overline{z}]}{N^{1/2}} - \frac{|\omega|^2}{4N}\right]\right)\\
\cdot \frac{1-(1+|\omega|^2)e^{-|\omega|^2}}{|\omega|^4}\,
\mathbf{1}_{[0,1]}\Big(\Big|z\pm\frac{1}{2}N^{-1/2}\omega\Big|^2\Big)\, 
N^{-1} d^2\omega\, d^2z\, ,
\end{gathered}$$ where we use the approximation symbol $\approx$ to remind ourselves that this is only one part of the eventual formula. Simplifying this, and writing $z = r e^{i\theta}$ and $\omega = \rho e^{i t}$, we have $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\, \\ \approx\, -\frac{N}{\pi^2} \int_{\mathbb{C}} \int_{\mathbb{C}} \left[r^2 + \frac{i r\rho \sin(\theta-t)}{N^{1/2}} - \frac{\rho^2}{4N}\right]^p
\left(1 -  \left[r^2 + \frac{i r\rho \sin(\theta-t)}{N^{1/2}} - \frac{\rho^2}{4N}\right]\right)\\
\cdot \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho^4}\,
\mathbf{1}_{[0,4N]}\Big(\Big|\rho \pm 2N^{1/2}re^{i(t-\theta)}\Big|^2\Big)\, 
r\rho\, dr\, d\rho\, d\theta\, dt\, .
\end{gathered}$$

Let us denote $\phi = t-\theta$. Integrating over the extra angular variable, simplifying the power of $\rho$ in the second line, and simplifying the indicator in the second line, we obtain$$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\,
 \\ \approx\, -\frac{2N}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\rho>0} \int\limits_{\phi \in [0,2\pi)} \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]^p
\left(1 -  \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]\right)\\
\cdot \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho^3}\,
\mathbf{1}_{[0,N^{1/2} R(r,\phi)]}(\rho)\, 
r dr\, d\rho\, d\phi\, ,
\end{gathered}$$ for $$R(r,\phi)\, =\, 2 \left(\sqrt{1-r^2\sin^2(\phi)}-r|\cos(\phi)|\right)\, ,$$ arising from the condition $|\rho \pm 2 N^{1/2} r e^{i\phi}| \leq 2N^{1/2} \Leftrightarrow \rho \leq R(r,\phi) N^{1/2}$

Let us rewrite this once again, this time isolating different functional terms that we wish to consider in more detail: $$\begin{gathered}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2\, \\ \approx\, -\frac{2N}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} \left(\int_0^{N^{1/2}R(r,\phi)} F_p(r,\phi,\rho) W(\rho)\, d\rho\right)\, r\, dr\, d\phi\, ,
\end{gathered}$$ where $$\label{eq:Fp}
F_p(r,\phi,\rho)\, =\, \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]^p
\left(1 -  \left[r^2 - \frac{i r\rho \sin(\phi)}{N^{1/2}} - \frac{\rho^2}{4N}\right]\right)\, ,$$ and $$W(\rho)\, =\,  \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho^3}\, .$$ Now we note that we can expand $$\label{eq:expand}
F_p(r,\phi,\rho)\, =\, \sum_{k=0}^{2p} f_p^{(k)}(r,\phi)\, \frac{\rho^k}{N^{k/2}}\, .$$ Odd powers of $k$ have $f_p^{(k)}(r,\phi)$ which is an odd function of $\sin(\phi)$. Since the rest of the integral will contribute even factors, this means all odd powers will integrate to zero, so we only keep track of even powers. We have already taken account of $f_p^{(0)}(r,\phi)$ which is just $f_p^{(0)}(r) = r^{2p} (1-r^2)$. This was what gave us the leading order divergence we considered in a past subsection.

Moreover, starting from the even power $k=4$, we have $$-\frac{2N}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} \left(\int_0^{N^{1/2}R(r,\phi)} f_p^{(k)}(r,\phi)\, \frac{\rho^k}{N^{k/2}} W(\rho)\, d\rho\right)\, r\, dr\, d\phi\, 
=\, O(1)\, .$$ The reason is that $N \cdot N^{-k/2} = N^{-(k-2)/2}$ which is vanishing. This means that the lower limit of integration is actually contributing a negligible correction, asymptotically for large $N$. Near the upper limit of integration, we may expand $W(\rho) \sim \rho^{-3}$. Therefore we obtain near the upper limit, for $k=4,6,\dots$, $$\begin{gathered}
\label{eq:largek}
-\frac{2}{\pi N^{(k-2)/2}} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(k)}(r,\phi)\,\left(\int_0^{N^{1/2}R(r,\phi)}  \rho^{k-3}\, d\rho\right)\, r\, dr\, d\phi\\
=\, -\frac{2}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(k)}(r,\phi)\, \frac{[R(r,\phi)]^{(k-2)/2}}{k-2}\, r\, dr\, d\phi
+o(1)\, =\, O(1)\, .
\end{gathered}$$

This only leaves the term with $k=2$ which might diverge. Indeed, for this, we just have $$-\frac{2}{\pi}\,
\int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(2)}(r,\phi)\,\left(\int_0^{N^{1/2}R(r,\phi)}  \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho}\, d\rho\right)\, r\, dr\, d\phi\, .$$ The only divergent part of this arises near the upper limit for the $\rho$ integral which gives $\ln(N^{1/2} R(r,\phi)) = \frac{1}{2} \ln(N) + \ln(R(r,\phi))$, so the logarithmic divergence is $$\begin{gathered}
-\frac{2}{\pi}\,
\int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} f_p^{(2)}(r,\phi)\,\left(\int_0^{N^{1/2}R(r,\phi)}  \frac{1-(1+\rho^2)e^{-\rho^2}}{\rho}\, d\rho\right)\, r\, dr\, d\phi\\
=\,
-\frac{\ln(N)}{\pi} \int\limits_{r \in [0,1]} \int\limits_{\phi \in [0,2\pi)} r f_p^{(2)}(r,\phi)\, dr\, d\phi
+ O(1)\, .
\end{gathered}$$ It is easy to see that $$f_p^{(2)}(r,\phi)\, =\,
\frac{1}{4}\, r^{2p} - \frac{p}{4}\, r^{2p-2} (1-r^2) - \frac{p(p-1)}{2}\, r^{2p-2}(1-r^2) \sin^2(\phi) + p r^{2p}\sin^2(\phi)\, .$$ Therefore, we have $$\begin{split}
\int_{\phi \in [0,2\pi]} f_p^{(2)}(r,\phi)\, d\phi\, 
&=\, 2\pi
\left(\frac{1}{4}\, r^{2p} - \frac{p}{4}\, r^{2p-2} (1-r^2) - \frac{p(p-1)}{4}\, r^{2p-2}(1-r^2) + \frac{p}{2}\, r^{2p}\right)\\
&=\, \frac{\pi}{2} \left[(p+1)^2 r^{2p} - p^2 r^{2p-2}\right]\, .
\end{split}$$ Therefore, the sub-leading order divergence is now $$\label{eq:sL}
\int_{\mathbb{C}} \int_{\mathbb{C}} z_1^p \overline{z}_2^p \mathcal{O}_N^{(2)}(z_1,z_2)\, d^2z_1\, d^2z_2
+ \frac{N}{(p+1)(p+2)}\,
=\, -\frac{1}{4}\, \ln(N) + O(1)\, .$$ We may consider this particular form. It is independent of $p$. Near the circle, and for $z_1$ near $z_2$, the form of $z_1^p \overline{z}_2^p$, to leading order is just $|z|^{2p}$ which is just $1$, because $z$ is near the circle. This is the same explanation for the reason that the order-1, constant term coming from $\mathcal{O}_N^{(1)}$ term is independent of $p$. We also know that the moment must be independent of $p$.

One could also try to calculate the order-1 contributions at this point, coming just from the bulk formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$. One could then check whether these combine to a constant independent of $p$. That would be yet another strong check that Chalker and Mehlig's formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ is true to very high accuracy in the bulk, and only needs an edge correction near the circle.

It would be best to have a sufficiently explict formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ to allow one to see the correction near the circle. Then we could have an answer to settle this. Next, we propose a method which we believe could potentially provide this.

# Proposal to Rigorously Approach Chalker and Mehlig's Result

There are various ways to try to prove Chalker and Mehlig's formula for the bulk behavior of $\mathcal{O}_N^{(2)}$. One way is to try to fill in the details to make Chalker and Mehlig's argument rigorous. Their idea is to express $\mathcal{O}_N^{(2)}$ in terms of the expectation of a function of the eigenvalues, and then use the known eigenvalue marginal for the complex Ginibre ensemble.

Here we want to propose a second method. The formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ is the determinant of a 5-diagonal matrix. One may express such a determinant through a recursion relation, although the recursion relation is significantly more complicated than in the tridiagonal case. It is higher order, and it is a vector valued recursion relation for a vector with dimension greater than $1$. We will not explicate this, here. It is well-known, it just follows from Cramer's rule, and it is widely used in numerical codes.

Instead, what we want to advocate here is solving recursion relations, at least asymptotically for large $N$, using adiabatic theory. We have not tried this yet for $\mathcal{O}_N^{(2)}(z_1,z_2)$. There may be formidable difficulties which obstruct this approach, but let us demonstrate the idea for an easier problem: re-deriving the formula for $\mathcal{R}_N^{(1)}(z)$. This leads to an easier problem. The key trick for this particular problem is to realize that $\mathcal{R}_N^{(1)}(z)$, at least for the leading-order asymptotic formula, is constant in $z$ for $|z|<1$.

## The Recurrence Relation for $\mathcal{R}_N^{(1)}(z)$ Using Matrices

We are treating the case of $\mathcal{R}_N^{(1)}(z)$ as a simpler toy model, in lieu of treating the real problem of interest which is $\mathcal{O}_N^{(2)}(z_1,z_2)$. We hope to be able to handle $\mathcal{O}_N^{(2)}(z_1,z_2)$ later, in another paper.

Recall from ([\[eq:RD\]](#eq:RD){reference-type="ref" reference="eq:RD"}) that $\mathcal{R}_N^{(1)}(z) = \pi^{-1} [(N-1)!]^{-1} \exp(-N |z|^2) D_{N-1}(z)$, which means from Stirling's formula that $$\mathcal{R}_N^{(1)}(z)\, \sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}}\, e^{-(N-1)\ln(N)+N(1-|z|^2)} D_{N-1}(z)\, .$$ Moreover, recall that there is a recursion relation in ([\[eq:Dr\]](#eq:Dr){reference-type="ref" reference="eq:Dr"}). Namely, defining $D_{N-1}(\sigma^{-2},z) = D_{N-1}(\sigma^{-1}N^{-1/2}z)$, it happens that $$D_{n+1}(\sigma^{-2},z)\, =\, (\sigma^{-2}|z|^2+n+1) D_n(\sigma^{-2},z)-\sigma^{-2}n|z|^2D_{n-1}(\sigma^{-2},z)\, .$$ Let us fix $\sigma^2=N^{-1}$ as Chalker and Mehlig do. Then $$D_{n+1}(N,z)\, =\, (N|z|^2+n+1) D_n(N,z)-Nn|z|^2D_{n-1}(N,z)\, .$$ Also, since the answer only depends on the magnitude of $z$, let us write $r=|z|$ so $$D_{n+1}(N,r)\, =\, (Nr^2+n+1) D_n(N,r)-Nnr^2D_{n-1}(N,r)\, .$$ We want to calculate $\mathcal{R}_N^{(1)}(r)$ which is asymptotically given by $$\mathcal{R}_N^{(1)}(r)\, \sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}}\, e^{-(N-1)\ln(N)+N(1-r^2)} D_{N-1}(N,r)\, .$$ Now since we have a second-order recursion relation, let us define a two-dimensional vector $v_n = [D_{n-1}(N,r),D_n(N,r)]^*$. (All our vectors and matrices will be real but we use the adjoint instead of the transpose because we want to keep the symbol $T$ for other purposes.) Then the recursion relation says that $$v_{n+1}\, =\, A_n v_n\, ,\qquad
A_n\, =\, 
\begin{bmatrix} 0 & 1 \\
-Nnr^2 & N r^2+n+1
\end{bmatrix}\, ,$$ and we want $D_{N-1}(N,r) = e_2^* v_{N-1}$, where $\{e_1,e_2\}$ is the standard basis for $\mathbb{R}^2$. In order to have a simpler formula, we note that we can write $v_1 = A_0 e_2$, for $A_0$ defined as above. In seeking $\mathcal{R}_N^{(1)}(r)$, we really have $$\mathcal{R}_N^{(1)}(r)\, \sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)} e_2^* A_{N-2} \cdots A_1 A_0 e_2\, .$$ The idea is to try to express this using the spectral decomposition of the matrices $A_n$, where we use the fact that the matrices $A_n$ are *varying slowly* in $n$, as much as possible. This is why we call this the *adiabatic approach.*

## Spectral Formulas and Summary of Main Contribution

We may summarize the spectral information as $$\begin{gathered}
\lambda_n^{\pm}\, =\, \frac{N}{2} \left(r^2+\frac{n+1}{N} \pm \sqrt{\left(\frac{n+1}{N}-r^2\right)^2+4r^2N^{-1}}\right)\, ,\quad \\
V_n^{\pm}\, =\, \begin{bmatrix} 1 \\ \lambda_n^{\pm} \end{bmatrix}\, ,\quad
W_n^{\pm}\, =\, \pm\frac{1}{\lambda_n^+ - \lambda_n^-} \begin{bmatrix} - \lambda_n^{\pm} \\ 1 \end{bmatrix}\, ;\\
A_n V_n^{\pm}\, =\, \lambda_n^{\pm} V_n^{\pm}\, ,\qquad
(W_n^{\pm})^* A_n\, =\, \lambda_n^{\pm} (W_n^{\pm})^*\, ,\qquad
(W_n^{\sigma})^* V_n^{\tau}\, =\, \delta_{\sigma,\tau}\, ,\ \text{ for $\sigma,\tau \in \{+1,-1\}$.}
\end{gathered}$$ In particular, $A_n = \lambda_n^+ V_n^+ (W_n^+)^* + \lambda_n^- V_n^- (W_n^-)^*$. Therefore, we can rewrite the conclusion of the recursion relation as $$\begin{split}
\mathcal{R}_N^{(1)}(r)\, 
\sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)} e_2^* A_{N-2} \cdots A_1 A_0  e_2\\
=\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)}
\sum_{\sigma \in \{+1,-1\}^{N-1}} \left(\prod_{n=0}^{N-2} \lambda_n^{\sigma(n)}\right)
([W_0^{\sigma(0)}]^* e_2) (e_2^* V_{N-2}^{\sigma(N-2)}) \\
&\hspace{9cm}
\cdot \left(\prod_{n=0}^{N-1} [W_{n+1}^{\sigma(n+1)}]^* V_n^{\sigma(n)}\right)\, .
\end{split}$$ Anticipating that the main contribution to this sum will be $\sigma(0)=\dots=\sigma(N-1)=+1$, we may rewrite this as $$\mathcal{R}_N^{(1)}(r)\, 
\sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)} \mathcal{M}_N(r) \mathcal{P}_N(r)\, ,$$ where $\mathcal{M}_N(r)$ is the "main term" $$\mathcal{M}_N(r)\,
=\,
\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)
([W_0^{+}]^* e_2) (e_2^* V_{N-2}^{+}) 
\cdot \left(\prod_{n=0}^{N-1} [W_{n+1}^{+}]^* V_n^{+}\right)\, ,$$ and $\mathcal{P}_N(r)$ will be a series of perturbations $$\mathcal{P}_N(r)\,
=\, 
\sum_{\sigma \in \{+1,-1\}^{N-1}} 
\left(\prod_{n=0}^{N-2} \frac{\lambda_n^{\sigma(n)}}{\lambda_n^+}\right)
\frac{([W_0^{\sigma(0)}]^* e_2) (e_2^* V_{N-2}^{\sigma(N-2)})}{([W_0^{+}]^* e_2) (e_2^* V_{N-2}^{+})}
\cdot \left(\prod_{n=0}^{N-1} \frac{[W_{n+1}^{\sigma(n+1)}]^* V_n^{\sigma(n)}}
{[W_{n+1}^{+}]^* V_n^{+}}\right)\, .$$ We know that we are trying to find that the leading order behavior of $\mathcal{R}_N^{(1)}(r)$ is as follows: it is constant, equal to $\pi^{-1}$, for $r<1$, and it is exponentially small for $r>1$. We will not try to recover the boundary behavior near $r=1$ in this note. (In fact, what we hope to be able to do in a later paper is to calculate $\mathcal{O}_N^{(2)}(z_1,z_2)$ in a similar way, and especially to determine the edge behavior when $z_1$ and $z_2$ are near the circle.) Let us quickly note how we may dispense with the $r>1$ case so that we may focus on $r<1$.

The largest contribution to $\mathcal{M}_N(r)$ comes from the product of eigenvalues $$\begin{gathered}
\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)
=\, \exp\left[\sum_{n=0}^{N-2} \ln( \lambda_n^{+})\right]\\
=\,e^{(N-1) \ln(N)} \exp\left(\sum_{n=0}^{N-2} \ln\left[ 
\frac{1}{2}\left(r^2+\frac{n+1}{N} + \sqrt{\left(\frac{n+1}{N}-r^2\right)^2+4r^2N^{-1}}\right)
\right]
\right)\, .
\end{gathered}$$ Moreover, defining $t_{n+1} = (n+1)/N$, the sum is $(N-1)$ times a Riemann sum approximation so that: $$\begin{split}
\frac{1}{N}\ln\left[e^{-(N-1)\ln(N)} \left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\right]\, 
&=\,
\int_0^1 \ln\left(\frac{1}{2}\left(r^2+t+\sqrt{(t-r^2)^2+4r^2N^{-1}}\right)\right)\, dt + o(1)\\
&=\, \int_0^1 \ln\left(\frac{1}{2}\left(r^2+t+\sqrt{(t-r^2)^2}\right)\right)\, dt + o(1)\\
&=\, \int_0^1 \ln(\max\{r^2,t\})\, dt + o(1)\, ,
\end{split}$$ where the remainder term $o(1)$ is a quantity which converges to $0$ as $N \to \infty$. Hence we may see, by integrating, that $$\lim_{N \to \infty} \frac{1}{N}\ln\left[e^{-(N-1)\ln(N)} \left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\right]\, 
=\, \begin{cases} \ln(r^2) & \text{ if $r\geq 1$,}\\
r^2-1 & \text{ if $r \in [0,1]$.}
\end{cases}$$ This means that, incorporating the exponential part of the prefactor for $\mathcal{R}_N^{(1)}(r)$, $$\lim_{N \to \infty} \frac{1}{N}\ln\left[e^{-(N-1)\ln(N)+N(1-r^2)} \left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\right]\, 
=\, \begin{cases} 0 & \text { if $r \in [0,1]$,}\\
\ln(r^2)-1+r^2 & \text{ if $r>1$,}
\end{cases}$$ and it is easy to see that $\ln(x) \leq x-1$ for all $x \in (0,\infty)$ by convexity of $-\ln(x)$. For $r>1$ this is exponentially small: to leading order $e^{N[\ln(r^2)-1+r^2]}$. We claim that no other factor is exponentially large, so that we obtain $$\lim_{N \to \infty} N^{-1} \ln(\mathcal{R}_N^{(1)}(r))\, 
=\, \begin{cases} 0 & \text { if $r \in [0,1]$,}\\
\ln(r^2)-1+r^2 & \text{ if $r>1$.}
\end{cases}$$ Therefore, we will henceforth assume $r<1$.

When $r<1$, we claim that we need to do a more careful analysis of the product. The time scale $t_n=n/N$ is too rough when $t_n$ is near $r^2$. The purely discrete scale $n$ is too fine. Therefore, we use the intermediate time scale $T_n = (t_n-r^2)N^{1/2}$, instead. Then we may rewrite $$\begin{gathered}
\lambda_n^{+}\,
=\, N \exp(\psi^{+}(T_{n+1}))\, ,\qquad \\
\psi^{+}(T_{n+1})\, =\, \ln\left(r^2 + \frac{1}{2}\, N^{-1/2} T_{n+1} + \frac{1}{2}\, N^{-1/2} \sqrt{T_{n+1}^2 + 4 r^2}\right)
\end{gathered}$$ so that $$\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\,
=\, N^{N-1} \exp\left(\sum_{n=0}^{N-1} \psi^+(T_{n+1})\right)\, .$$ Then we use the Euler-Maclaurin summation formula to obtain all other terms in the asymptotic series which are significant, including some boundary terms that come with the Euler-Maclaurin formula. (To do an integral such that $\int_{-r^2 N^{1/2}}^{(1-r^2)N^{1/2}} \psi^+(T)\, dT$, one may find it useful to define $T=2r\sinh(x)$ so that $dT = 2r \cosh(x)\, dx$ and $\sqrt{T^2+4r^2} = 2r \cosh(x)$, as well. Doing all this leads to $$\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\, \sim\, e \cdot r (1-r^2) e^{N\ln(N) - N(1-r^2)}\, .$$ It is also easy to use the definitions of $V_n^+$ and $W_n^+$ to show that $$^* e_2\,
\sim\, N^{-1} r^{-2}\quad \text{ and } \quad
e_2^* V_{N-2}^+\, \sim\, N\, .$$ Using the Euler-Maclaurin summation formula, one may also prove that $$\prod_{n=0}^{N-1} [W_{n+1}^{+}]^* V_n^{+}\,
\sim\,  \frac{r}{1-r^2}\, N^{-1/2}\, .$$ The details of the Euler-Maclaurin summation formula for this product as well as for the product of the eigenvalues are not trivial. (The product of the eigenvalues is harder than the product of the inner-products.) They may be done, in particular, by using the intermediate time-scale parameter $T_n$. Therefore, we obtain $$\mathcal{M}_N(r)\, =\, e \sqrt{N}\, e^{(N-1)\ln(N) - N(1-r^2)}\, .$$ Therefore, since $$\mathcal{R}_N^{(1)}(r) \sim \pi^{-1} (2\pi N)^{-1/2} \exp(-(N-1)\ln(N)+N(1-r^2)) \mathcal{M}_N(r) \mathcal{P}_N(r)$$ we see that $$\mathcal{R}_N^{(1)}(r)\, \sim\, \pi^{-1}\, \frac{e}{\sqrt{2\pi}}\,   \mathcal{P}_N(r)\, .$$ Now we will argue that $\mathcal{P}_N(r)$ is actually independent of $r$, to leading order.
