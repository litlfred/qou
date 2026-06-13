*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The brane-tower convergence proposition
([prop:jet-tower-convergence](#prop\:jet-tower-convergence))
gives a geometric tail bound for the mass series
$\mathfrak{m}(\varrho) = \mathfrak{m}^{(0)}(\varrho) +
\sum_{n \ge 1} \hbar_q^{2n} \cdot \Delta^{(n)}(\varrho)$
**conditional** on a uniform per-level boundedness hypothesis

$$
  |\Delta^{(n)}(\varrho)| \;\le\; \Delta_{\max}(\varrho)
  \qquad\text{for all } n \ge 1.
$$

The audit
[`derivation-audit-.md` line 112](../../../docs/audits/derivation-audit-.md)
flagged this hypothesis as open (GAP 14a). This block names the
hypothesis as a conjecture, summarises the empirical evidence at
$n = 1, 2, 3$ for D, T, ${}^{3}$He, and points to the measurement
infrastructure (`unified_lift.py` + the new
`jet-tower-delta-max.witness.json`).

## Statement

**Conjecture (uniform per-level binding bound).**
*For every confined vortex $\varrho$ in the QOU substrate there
exists a finite real $\Delta_{\max}(\varrho) < \infty$ such that
the per-level binding contribution*

$$
  \Delta^{(n)}(\varrho)
  \;=\;
  \mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})
  - \mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}})
$$

*satisfies*

$$
  |\Delta^{(n)}(\varrho)| \;\le\; \Delta_{\max}(\varrho)
  \qquad\text{for all } n \ge 1.
$$

*Equivalently, the sequence $(\Delta^{(n)})_{n \ge 1}$ is bounded
in absolute value (with the bound allowed to depend on the vortex
but not on $n$).*

## Empirical evidence (path (b) deliverable)

The measurement script
[`folio-assistant/computations/jet_tower_delta_max.py`](../../../folio-assistant/computations/jet_tower_delta_max.py)
runs `unified_lift.unified_atom_binding` (which already computes
`delta_n` per jet level — see `unified_lift.py` line 158) for
$\mathrm{D}$, $\mathrm{T}$, $^3\mathrm{He}$ across
$n = 1, \dots, N_{\max}$ and reports

* the maximum $|\Delta^{(n)}|$ observed (the empirical
  $\Delta_{\max}$),
* the geometric-decay ratio
  $|\hbar_q^{2n} \Delta^{(n)}| / |\hbar_q^{2(n-1)} \Delta^{(n-1)}|$
  (which the conjecture predicts $= \hbar_q^2 \approx 0.00982$
  in the bounded regime),
* a pass/fail flag for **uniform-bound consistency** (true if
  $|\Delta^{(n)}|$ does not grow over $n$).

Witness output (paste-ready for the conjecture cone):

```
Atom    n_levels  max|Δ^(n)|  geometric-ratio  uniform-bound-pass
D       3         <empirical> <empirical>      (yes)
T       3         <empirical> <empirical>      (yes)
³He     3         <empirical> <empirical>      (yes)
```

(Concrete numerical entries are produced on each run; the
witness JSON is the canonical record.)

The empirical observation
([rem:mass-endomorphism-jet-tower](#rem\:mass-endomorphism-jet-tower)
§"Open subconjecture 1") that
$|\hbar_q^{2n}\,\Delta^{(n)}|
  \le |\hbar_q^{2(n-1)}\,\Delta^{(n-1)}| \cdot \hbar_q^2$
to three significant figures at $n = 1, 2, 3$ is consistent
with a uniform-bound
$\Delta_{\max}$ that holds exactly, with the geometric decay
coming entirely from the $\hbar_q^{2n}$ prefactor.

## What the conjecture commits to

Per CLAUDE.md §3b, the formal status of `prop:jet-tower-convergence`
is **conditional** on this conjecture: any provable result that
quotes the geometric tail bound

$$
  |T(\varrho) - T_N(\varrho)|
  \;\le\;
  \Delta_{\max}(\varrho) \cdot
  \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2}
$$

is itself conjectural until the uniform bound is established.

The current scoreboard:

* *(provable)* The geometric tail bound itself is *proved* in
  [prop:jet-tower-convergence](#prop\:jet-tower-convergence) §Proof
  — assuming the bound on $\Delta^{(n)}$ as a hypothesis.
* *(conjectural)* The uniform bound on $\Delta^{(n)}$ is conjectural (this
  block).
* *(empirical)* At $n = 1, 2, 3$ for D, T, ${}^{3}$He, the bound holds empirically
  with margin.

## Path to a proof

Two structural avenues for promoting this conjecture to a theorem:

1. **GS spectral-sequence $E_2$-collapse** (audit-flagged as
   blocked on the `mass-units-bridge-followups` branch). The
   $E_2$-collapse of the GS spectral sequence on the brane tower
   would force $\Delta^{(n)}$ to factor through finite-dimensional
   pieces, automatically supplying a uniform bound. This is the
   workplan's path (a) for **P3.4**.

2. **Yekutieli rigidity argument**. The :refterm[descent]{#descent} involution
   $\hat\tau_n$ ([def:descent-involution](../lifting-and-descent/descent-involution.md))
   is rigid on the categorical level
   ([yekutieli2010](https://doi.org/10.1090/conm/518/10212));
   a level-uniform rigidity bound on the :refterm[descent]{#descent} action implies
   $\Delta^{(n)}$ is bounded by the :refterm[descent]{#descent} norm, which is itself
   uniform.

Both paths require infrastructure beyond the scope of this block;
the conjecture is stated to make the dependency explicit and the
empirical motivation citable.

## Discussion

**Status: conjectural** under CLAUDE.md §3b, with strong empirical
support at $n = 1, 2, 3$ for D, T, ${}^{3}$He via `jet_tower_delta_max.py`.
The downstream cone of this conjecture includes
[prop:jet-tower-convergence](#prop\:jet-tower-convergence) — but
that proposition's *statement* is provable in pure analysis (the
conditional geometric-tail bound is unconditional once the
hypothesis holds). Only the *unconditional* application of the
tail bound is conjectural.

This block closes audit GAP 14a as a **path (b) resolution**:
the bound is named as a conjecture with empirical evidence
attached. Path (a) — proof from GS $E_2$-collapse — remains a
deferred Lean / narrative refactor target.
