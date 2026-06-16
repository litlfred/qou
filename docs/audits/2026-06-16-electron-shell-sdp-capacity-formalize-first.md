# Electron-shell SDP "capacity" — formalize-first correction

**Date:** 2026-06-16
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348)
**Compute:** [`computations/electron_shell_sdp_capacity.py`](../../computations/electron_shell_sdp_capacity.py)
**Class:** exploratory diagnostic — no fit, no witness.

## The idea, and the correction

The owner's idea (the Level-6 follow-up): *"put an electron on an isotope, keep
adding electrons until the confinement SDP won't solve — that's the capacity."*
A prior session built a scratch version and reported capacities like **H ≈ 5,
He ≈ 8, C ≈ 14** and called them shell counts.

**Formalize-first check (before trusting any number):** the canonical
mechanism, [`prop:shell-closure-stability`](../../content/quantum-observable-universe/particle-interactions/shell-closure-stability.md),
says the selection principle is the **dual objective** of the
[confinement SDP](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md):

$$
  \sigma_F(P^{(Z)}, q) \;=\; n_{\text{target}} \cdot u_0^*(P^{(Z)}, q)
  \qquad\text{(Frobenius stability index)},
$$

and **claim 1 proves σ_F is monotonically non-decreasing in Z** (SDP-relaxation
monotonicity). The SDP **never goes infeasible** as electrons are added — so
"add until it won't solve" has no terminal state. The proof contains the exact
warning:

> *the monotonicity here is SDP-relaxation, **not** Cauchy eigenvalue
> interlacing — the two would give **opposite conclusions on the raw Gram
> matrix**.*

The prior "capacity" used precisely the raw Frobenius Gram `Gx ≥ 0` feasibility
test — i.e. the eigenvalue-interlacing branch the proof excludes. Those numbers
are an artifact, not shell counts.

**The real shell-closure mechanism (claim 2):** σ_F has **local maxima** at
noble-gas `Z ∈ {2,10,18,36,54,86}` where the binding **multiplicity μ ≥ 2**
(≥ 2 tight dual blocks; `ElectronShell.bindingMultiplicity` = active dual
support). Equivalently the topological **full-of-curls** condition of
[`prop:noble-gas-characterization`](../../content/quantum-observable-universe/predicted-spectra/noble-gas-characterization.md):
`p·T_{2,3} = ⊔ closed sub-Hopf-links`. Closure is a *max of a monotone dual +
multiplicity* phenomenon — not a feasibility wall. Chemical inertness =
categorical terminality (leaving a closed shell needs breaking μ ≥ 2 tight
blocks, energetically forbidden at α).

## What the demo shows

**§1 — reproduces the artifact.** Adding alternating σ₀⁻¹/σ₁⁻¹ electrons and
stopping at the first raw-Gram `Gx ≥ 0` violation:

| atom | Z | "last-feasible e⁻" (raw-Gram) | chemical (neutral) |
|---|--:|--:|--:|
| H | 1 | 3 | 1 |
| He | 2 | 7 | 2 |
| Li | 3 | 10 | 3 |
| C | 6 | 18 | 6 |
| O | 8 | ≥20 | 8 |

Non-physical — confirms the raw-Gram threshold is the interlacing artifact.

**§2 — the canonical dual is feasible throughout.** Solving the confinement SDP
via the canonical `pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G,
n_target)` (cost `t` = Markov weights, `G` = Frobenius Gram) returns
`duality_gap ≈ 0` and `feasible = True` for every `n_target` — there is **no
infeasibility wall** where §1 claims one. (σ_F = 0 here is the single-level
degeneracy: the Markov-cost normalisation is non-binding on the 6-dim NF block.
The non-trivial σ_F(Z) growth + the noble-gas local maxima need the multi-level
cost operator, `multi_level_sdp.py` — see follow-up.)

## Finding

1. **"Add electrons until the SDP won't solve" is the wrong notion** — σ_F is a
   monotone non-decreasing dual objective; the confinement SDP does not become
   infeasible along the dressing chain.
2. **The prior H≈5 / He≈8 capacities are the raw-Gram interlacing artifact** the
   proof explicitly excludes.
3. **Shell closure = local max of σ_F + multiplicity μ ≥ 2** at noble-gas Z
   (= full-of-curls). This *is* the categorical "capacity," but it is a
   max/multiplicity signal, read from the **dual**, not an infeasibility
   threshold.

## Follow-up (not this PR)

- Build the per-Z **σ_F(Z) dressing chain** on the multi-level SDP
  (`multi_level_sdp.py`) and exhibit the noble-gas local maxima + μ ≥ 2 at
  Z = 2 (and 10, 18 where tractable) — the live, faithful version of the demo.
  This needs the multi-level cost operator + Wedderburn block extension, a
  separate infra tranche.
- The first-class LP/SDP **dual** is already emitted by the canonical solver
  (`y0_star`, `y_star`, `active_set`) — the `active_set` *is* the binding
  multiplicity μ, so the shell-closure read-out is one `solve_*` call away once
  the multi-level cost is wired.
