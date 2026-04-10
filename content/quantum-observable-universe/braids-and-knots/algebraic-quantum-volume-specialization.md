**Proposition.**
*The algebraic quantum volume
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}][z]$
specialises to three distinct invariants:*

1. ***The $q \to 1$ limit.**  As $q \to 1$:
   $H_A \to 0$, $z \to 1/2$, and each crossing matrix
   $c \cdot \sigma + d \cdot I$ degenerates to
   $(c + d) \cdot I$.  The traced volume
   $\hat{V}_i \to \tfrac{1}{2} \cdot 0 + (c+d)^k = (c+d)^k$
   for $k$ crossings.
   Hence $\mathrm{Vol}_q(\beta) \to 1$ (trivial) for the
   undeformed braid.*

2. ***Roots of unity (Volume Conjecture).**  At
   $q = e^{2\pi i/N}$, the colored Jones polynomial
   $J_N(K; e^{2\pi i/N})$ grows as
   $\exp(N \cdot \mathrm{Vol}(S^3 \setminus K) / 2\pi)$.
   The algebraic quantum volume $\mathrm{Vol}_q(\beta)$ embeds
   into the Habiro ring ([Habiro ring](#def:habiro-ring)), and
   its evaluations at all roots of unity collectively encode
   the hyperbolic volume.  The Borromean rings satisfy
   $\mathrm{Vol}(\mathcal{B}_3) = 8G$ via this route.*

3. ***The substrate evaluation $q = q_0$.**  At $q = q_0
   \approx 1.10998$ (not a root of unity):*

   $$
     \ln\lvert\mathrm{Vol}_{q_0}(\beta)\rvert
     = \Phi_1(\beta)
   $$

   *This is the quantum dilogarithm volume that enters the
   mass formula.  The binding scale is
   $\alpha = m_e \times 8G$ where $8G$ is the hyperbolic
   volume $\mathrm{Vol}(\mathcal{B}_3)$ obtained from the
   Habiro evaluation (route 2), not from the substrate
   evaluation (route 3).*

*The mass formula combines routes 2 and 3:*

$$
  \mathcal{M}(Z, N)
  = M_{\mathrm{free}}
  + \underbrace{m_e \times 8G}_{\text{route 2: hyperbolic}}
    \times
    \underbrace{\ln\lvert\mathrm{Vol}_{q_0}(\text{atom})\rvert}
      _{\text{route 3: substrate}}
$$

*Route 2 (the Habiro/root-of-unity path) provides the
overall energy scale $8G$.  Route 3 (the substrate evaluation)
provides the per-atom binding $\Phi_1$.  Both are shadows of
the single algebraic object $\mathrm{Vol}_q$.*

*Proof sketch.*
The algebraic volume $\mathrm{Vol}_q(\beta) = \prod \hat{V}_i(q)$
is a finite product of elements of
$\mathbb{Z}[q^{1/2}, q^{-1/2}][z]$.  Route 1 follows from
$H_A(1) = 0$.  Route 2 follows from the Habiro embedding and
the Kashaev–Murakami–Murakami theorem (the Volume Conjecture,
proved for hyperbolic knots with $\leq 7$ crossings).  Route 3
is direct evaluation.  $\square$
