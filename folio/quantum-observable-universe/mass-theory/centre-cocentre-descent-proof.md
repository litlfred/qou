**Items 1–2.** Existence is the direct-sum decomposition. For uniqueness, apply $\pi_Z$ to $x = z + c$ with $z\in Z(A)$, $c\in[A,A]$: since $\pi_Z(z)=z$ and $\pi_Z(c)=0$, $\pi_Z(x)=z$ and then $c = x-z$. Idempotence holds because $\pi_Z(x)\in Z(A)$ is fixed by $\pi_Z$. For $z\in Z(A)$, $zx = z\,x^{\mathrm{desc}} + z\,x^{\mathrm{trans}}$; the first term is central, and $z[a,b]=[za,b]$, so $z[A,A]\subseteq[A,A]$. Uniqueness gives $\pi_Z(zx)=z\,\pi_Z(x)$.

**Item 3.** A trace vanishes on each $ab-ba$, hence on their span $[A,A]$; apply it to $x^{\mathrm{trans}}$.

**Item 4.** An automorphism or anti-automorphism $\theta$ maps $Z(A)$ onto $Z(A)$. It maps commutators to commutators: $\theta(ab-ba) = \theta a\,\theta b-\theta b\,\theta a$, or its negative for an anti-automorphism. So $\theta[A,A]\subseteq[A,A]$, and uniqueness applied to $\theta x = \theta x^{\mathrm{desc}}+\theta x^{\mathrm{trans}}$ gives $\pi_Z(\theta x)=\theta(\pi_Z x)$.

**Item 5.** $\pi_Z(\theta_Z x) = 2\pi_Z x-\pi_Z x = \pi_Z x$, so $\theta_Z(\theta_Z x) = 2\pi_Z x-(2\pi_Z x - x) = x$. On $Z(A)$, $\theta_Z=\mathrm{id}$; on $[A,A]$, $\theta_Z=-\mathrm{id}$.

**Item 6.** It suffices to treat one block $M_d(K)$ with $d\in K^\times$. Its centre is $K\cdot1$. Its commutator span is $\mathfrak{sl}_d$: commutators are traceless, and $E_{ij}=[E_{ii},E_{ij}]$ for $i\ne j$ and $E_{ii}-E_{jj}=[E_{ij},E_{ji}]$ span $\mathfrak{sl}_d$. The intersection is $0$ because $c\cdot 1$ traceless means $cd=0$. The sum is everything: $x = \frac{\mathrm{tr}\,x}{d}\cdot 1+(x-\frac{\mathrm{tr}\,x}{d}\cdot1)$. Summing over blocks gives the formula. For $H_n(q)$ over $\mathbb{Q}(q)$ the Wedderburn decomposition is [Dipper–James 1986] and [Geck–Pfeiffer 2000, Ch. 8–9], with $d_\lambda$ the number of standard tableaux, a positive integer. The Markov-trace line is item 3.

**Item 7.** Since $\mathfrak d\circ\ell=\mathrm{id}$, $\hat\tau_n\circ\ell=\ell$, so $g_1=\ell(g_1)$ lies in the image. Over any nontrivial commutative ring with $q$ invertible, the matrices
$$
G_1=\begin{pmatrix}q&1\\0&-q^{-1}\end{pmatrix},\qquad G_2=\begin{pmatrix}-q^{-1}&0\\1&q\end{pmatrix}
$$
satisfy $G_i^2=(q-q^{-1})G_i+1$ and $G_1G_2G_1=G_2G_1G_2$, so they define a representation of $H_3(q)$. The $(1,1)$ entry of $G_1G_2-G_2G_1$ is $1$. So $g_1g_2\ne g_2g_1$ in $H_3(q)\subseteq H_{n+1}(q)$, and $g_1$ is not central. $\blacksquare$
