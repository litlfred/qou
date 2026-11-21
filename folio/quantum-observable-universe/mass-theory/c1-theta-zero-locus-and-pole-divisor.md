**Proposition (the $q$-theta of the ramified binding module vanishes exactly on the orbit $-p^{\mathbb{Z}}$; the connection matrix's poles are theta zeros).**

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
3. **The zero locus is exactly that orbit, and every zero is simple.** For
   $w\neq 0$,
   $$
   \theta_p(w)=0 \iff w\in -p^{\mathbb{Z}},
   $$
   and $\mathrm{ord}_{w}\theta_p = 1$ at each such $w$. The argument
   principle on the annulus $\rho<|z|<p\rho$ reads the winding difference of
   (2) as the number of zeros there counted with multiplicity, so that number
   is $1$; claim (1) supplies a zero at $-p^{k}$ whenever the annulus meets the
   orbit, and $\lfloor\log_p|w|\rfloor$ places any given $w$ in such an
   annulus. The hypothesis in (2) — no zero on the contour — is not a
   restriction: only finitely many radii carry a zero, so a clean contour can
   be placed on either side of any point. The origin is excluded because it is
   an essential singularity, where $\theta_p$ is not an analytic object at all.

   This is not the Jacobi triple product, which additionally identifies the
   product expansion and needs Liouville on $\mathbb{C}^{*}/p^{\mathbb{Z}}$.
4. **Series solutions.** With $T=\sqrt{(p^{2}-1)/p^{3}}$, the $0$-side series
   $\sum_k g_k z^{k}$ converges for $\lVert z\rVert<1$ and the $\infty$-side
   series $\sum_k h_k z^{-k}$ is entire, both recursions being consequences of
   $L$ rather than stipulations.
5. **Pole loci.** Every pole of the connection matrix $P=Y_0^{-1}Y_\infty$
   found in the computation lies on one of the three $p$-orbits
   $-p^{\mathbb{Z}}$, $-T\!\cdot\!p^{\mathbb{Z}}$, $+T\!\cdot\!p^{\mathbb{Z}}$,
   each of which is by (3) the *full* zero set of a $\theta_p$, reduced; the
   first is a normalisation artifact of the $0$-side character's common
   numerator and is not connection data.

For a $q$-difference system that is regular singular at $0$ and at $\infty$, the general framework is Sauloy's: canonical solutions at the two points are built from theta-quotient characters, their connection matrix has elliptic coefficients, and that matrix together with the two local data classifies the system \cite[\S0.1--0.2]{sauloy2000}.

**Scope.** (3) determines the zero divisor of $\theta_p$, so the three loci in
(5) are exact rather than containments and carry multiplicity one. What (5)
does not settle is completeness in the other direction — whether $P$ has poles
off those orbits. That, together with the identification of $Y_0$ and
$Y_\infty$ as the canonical solutions, the meromorphy of $P=Y_0^{-1}Y_\infty$,
and the closed form for the connection invariant $\chi$, remains open.

**The remaining claims are computational, not derived.** The pole divisor and
its residue-theorem completeness check, the connection invariant $\chi$ having
order $2$, the identification $\alpha=t_2/T$, and the closed form for $\chi$
verified to $5.3\times10^{-63}$ over twelve points, rest on numerical
witnesses.
