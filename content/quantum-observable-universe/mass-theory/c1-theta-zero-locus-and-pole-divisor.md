**Proposition (the $q$-theta of the ramified binding module vanishes on the orbit $-p^{\mathbb{Z}}$; the connection matrix's poles are theta zeros).**

Let $p>1$ and let
$$
\theta_p(w) \;=\; \sum_{n\in\mathbb{Z}} p^{-n(n+1)/2}\,w^{n},
$$
the $q$-theta attached to the ramified binding operator
$$
L \;=\; (p^{4}z^{2}-1)\,\tau^{2} \;-\; (p^{2}-1)\,\tau \;-\; (p^{2}-1),
\qquad \tau F(z)=F(pz),\qquad q=p^{2}.
$$
Then:

1. **Vanishing on the orbit.** $\theta_p(w)=0$ for every $w\in -p^{\mathbb{Z}}$.
   The proof is an involution and uses no analysis: the map $n\mapsto 2k-1-n$
   on $\mathbb{Z}$ leaves the exponent invariant and flips $(-1)^n$, so the
   series is its own negative. No summability hypothesis is required.
2. **Analytic foundation.** $\theta_p$ is holomorphic on $\mathbb{C}^{*}$, and
   satisfies $\theta_p(pw)=w\,\theta_p(w)$; differentiating and dividing gives
   $$
   p\,\frac{\theta_p'(pw)}{\theta_p(pw)} \;=\; \frac{1}{w} \;+\; \frac{\theta_p'(w)}{\theta_p(w)},
   $$
   and hence, for any $\rho>0$ on whose circle $\theta_p$ does not vanish,
   $$
   \oint_{|z|=p\rho}\frac{\theta_p'}{\theta_p}\,dz
     \;=\; 2\pi i \;+\; \oint_{|z|=\rho}\frac{\theta_p'}{\theta_p}\,dz .
   $$
   The winding number rises by **exactly one per period**.
3. **Series solutions.** With $T=\sqrt{(p^{2}-1)/p^{3}}$, the $0$-side series
   $\sum_k g_k z^{k}$ converges for $\lVert z\rVert<1$ and the $\infty$-side
   series $\sum_k h_k z^{-k}$ is entire, both recursions being consequences of
   $L$ rather than stipulations.
4. **Pole loci (inclusion only).** Every pole of the connection matrix
   $P=Y_0^{-1}Y_\infty$ found in the computation lies on one of the three
   $p$-orbits $-p^{\mathbb{Z}}$, $-T\!\cdot\!p^{\mathbb{Z}}$,
   $+T\!\cdot\!p^{\mathbb{Z}}$, each a single orbit of the zero set of a
   $\theta_p$; the first is a normalisation artifact of the $0$-side character's
   common numerator and is not connection data.

**Scope — the converse is not proved.** Claim (1) gives $-p^{\mathbb{Z}}\subseteq
Z(\theta_p)$, hence $\supseteq$ for the pole loci in (4), *not* equality. The
missing step is a single named lemma — the **argument principle on an annulus**,
which would read the winding difference in (2) as a zero count and force exactly
one zero per fundamental annulus. Mathlib has no argument principle, winding
number, or complex residue. Everything that lemma would consume is proved. This
is *not* the Jacobi triple product, which additionally needs Liouville on
$\mathbb{C}^{*}/p^{\mathbb{Z}}$ and is strictly more work.

**The remaining claims are computational, not derived.** The pole divisor and its
residue-theorem completeness check, the connection invariant $\chi$ having order
$2$, the identification $\alpha=t_2/T$, and the closed form for $\chi$ verified
to $5.3\times10^{-63}$ over twelve points, rest on numerical witnesses. That
$Y_0$ and $Y_\infty$ are the canonical solutions, that $P=Y_0^{-1}Y_\infty$ is
meromorphic, and that the divisor is complete, are open.
