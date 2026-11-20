## Remark on the hypothesis

The hypothesis $|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$
— uniform boundedness of per-level binding across the brane tower —
is the named conjecture
[Uniform per-level binding bound $|\Delta^{(n)}(\varrho)| \le \Delta_{\max}(\varrho)$ for the brane tower](#conj:jet-tower-uniform-delta-max).
This proposition therefore
**reduces the convergence question to a single boundedness
statement**: once $\Delta^{(n)}$ is shown to be bounded (uniformly
or with growth slower than $\hbar_q^{-2n}$), the tail decays as a
geometric series.

Empirically (see
the canonical formalism
and the formal derivation) the per-level terms for $\mathrm{D}$,
$\mathrm{T}$, $\mathrm{^{3}He}$ satisfy
$|\hbar_q^{2n} \Delta^{(n)}| \leq |\hbar_q^{2(n-1)} \Delta^{(n-1)}|
\cdot \hbar_q^2$ to three significant figures, and the
`uniform_bound_pass` flag in
[`jet-tower-delta-max.witness.json`](../../../computations/jet-tower-delta-max.witness.json)
is **true** for D, T, ${}^{3}$He across $n = 1, \dots, 7$ — consistent
with $\Delta^{(n)}$ being bounded (in fact roughly constant).
Promoting that observation to a theorem closes the open
subconjecture
[Uniform per-level binding bound $|\Delta^{(n)}(\varrho)| \le \Delta_{\max}(\varrho)$ for the brane tower](#conj:jet-tower-uniform-delta-max).

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
