Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Planck-$q$ constant
$\hbar_q = (q-1)/q$.  For a vortex $\varrho$ with braid
representative $\beta \in B_n$, the brane-tower refinement of the
mass endomorphism
([mass tower](#prop:mass-endomorphism-tower),
[jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
takes the form

$$
  \mathfrak{m}(\varrho)
  = \mathfrak{m}^{(0)}(\varrho)
  + \sum_{n=1}^{\infty} \hbar_q^{2n} \cdot \Delta^{(n)}(\varrho),
$$

where $\mathfrak{m}^{(0)}$ is the canonical Markov-trace term at
brane level zero and $\Delta^{(n)}(\varrho) = \mathfrak{m}^{(n)}
(\varrho_\mathrm{free}) - \mathfrak{m}^{(n)}(\varrho_\mathrm{atom})$
is the per-level binding contribution at brane level $n$.  The
$\hbar_q^{2n}$ weight comes from the recursive brane tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$: each jet-up step pairs a
Kähler form with its Frobenius dual, contributing $\hbar_q^2$ to
the weight.

**Proposition.**
*Assume there exists $\Delta_{\max}(\varrho) < \infty$ with
$|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$ for all
$n \geq 1$.  Then the brane-tower sum
$T(\varrho) := \sum_{n \geq 1} \hbar_q^{2n} \Delta^{(n)}(\varrho)$
converges absolutely, and the $N$-term truncation error is
bounded by*

$$
  \bigl\lvert T(\varrho)
    - \sum_{n=1}^{N} \hbar_q^{2n}\,\Delta^{(n)}(\varrho) \bigr\rvert
  \;\leq\; \Delta_{\max}(\varrho) \cdot
  \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

*In particular, to achieve binding-energy precision
$\varepsilon_B$ (in MeV) at archimedean calibration $E_0$, it
suffices to take*

$$
  N \;\geq\;
  \left\lceil \frac{\log\bigl( \tfrac{\varepsilon_B \,(1 - \hbar_q^{2})}
                                {E_0 \,\Delta_{\max}(\varrho)} \bigr)}
                 {\log(\hbar_q^{2})} \right\rceil.
$$

*Proof.*  The geometric series $\sum_{k \geq 0} \hbar_q^{2k}$
converges with sum $(1 - \hbar_q^{2})^{-1}$ because
$\hbar_q^2 \in (0, 1)$ (indeed $\hbar_q^2 \approx 0.00982$ at
$q_0 \approx 1.11$).  Absolute convergence follows from the
comparison
$\sum_{n \geq 1} \hbar_q^{2n} |\Delta^{(n)}|
\leq \Delta_{\max} \sum_{n \geq 1} \hbar_q^{2n}
= \Delta_{\max} \cdot \hbar_q^2 / (1 - \hbar_q^2)$.  The tail
bound factors the first skipped term:

$$
  \bigl\lvert \sum_{n > N} \hbar_q^{2n}\,\Delta^{(n)} \bigr\rvert
  \leq \Delta_{\max} \cdot \hbar_q^{2(N+1)}
   \sum_{k \geq 0} \hbar_q^{2k}
  = \Delta_{\max} \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

Multiplying by $E_0$ and solving $E_0 \cdot \Delta_{\max} \cdot
\hbar_q^{2(N+1)} / (1 - \hbar_q^2) \leq \varepsilon_B$ for $N$
gives the stated count.  $\square$

## Remark on the hypothesis

The hypothesis $|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$
— uniform boundedness of per-level binding across the brane tower —
is the named conjecture
[`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max)
(workplan **P3.4** path (b)). This proposition therefore
**reduces the convergence question to a single boundedness
statement**: once $\Delta^{(n)}$ is shown to be bounded (uniformly
or with growth slower than $\hbar_q^{-2n}$), the tail decays as a
geometric series.

Empirically (see
[`computations/jet_tower_delta_max.py`](../../../computations/jet_tower_delta_max.py)
and `unified_lift.py`) the per-level terms for $\mathrm{D}$,
$\mathrm{T}$, $\mathrm{^{3}He}$ satisfy
$|\hbar_q^{2n} \Delta^{(n)}| \leq |\hbar_q^{2(n-1)} \Delta^{(n-1)}|
\cdot \hbar_q^2$ to three significant figures, and the
`uniform_bound_pass` flag in
[`jet-tower-delta-max.witness.json`](../../../computations/jet-tower-delta-max.witness.json)
is **true** for D, T, ${}^{3}$He across $n = 1, \dots, 7$ — consistent
with $\Delta^{(n)}$ being bounded (in fact roughly constant).
Promoting that observation to a theorem closes the open
subconjecture
[`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max).

## Engineering consequence

Combined with the empirical level-1 residual $\varepsilon^{(1)} =
|\Delta^{(1)}|$ reported by the engine, the proposition gives a
constructive error budget: once the within-level $\hat{V}$ model is
improved so $\varepsilon^{(1)}$ is at the target precision, a single
extra jet level gives $O(\hbar_q^2)$ further reduction.  The jet
loop is therefore **not the bottleneck for sub-ppm precision** —
the level-1 $\hat{V}$ model is.

## Relation to confinement SDP

The level-1 $\hat V^{(1)}$ baseline entering this proposition is
produced by the SDP-feasible confinement operator of
[prop:confinement-sdp](#prop:confinement-sdp).  When the confinement
SDP is at a rank-1 solution (scalar LP regime) the baseline $\hat V$
is a real braid-word product and the boundedness hypothesis
$|\Delta^{(n)}| \le \Delta_{\max}$ holds empirically (cf.
`sdp-lift-audit.witness.json`: every real Hecke word has $x^T G x
\ge 0$).  At higher ranks the hypothesis is open, and the jet-tail
bound above remains conditional on the multi-operator binding
supporting a uniform $\Delta_{\max}$.  Closing that conditional is
the main outstanding piece of open subconjecture 1 on
[rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower).

*Formal asymptotic content. The geometric tail is the native
Jackson $d_q$-difference of the brane tower;
$\ordw(\text{tail}) = 2(N+1)\,\ordw(\hbar_q)$, and the recursive
jet prolongation is the
[surreal blow-up calculus](#def:surreal-blowup-calculus).
See [Big-O via $\ordw$](#rem:conway-normal-form),
[calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon),
and the [body asymptotics catalog](#rem:body-asymptotics-catalog).*