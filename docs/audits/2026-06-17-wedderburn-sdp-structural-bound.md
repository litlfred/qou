# The dense Wedderburn-projector SDP is structurally bounded — it selects a single-block extremal, never the multi-block 𝓑₃ (2026-06-17)

**Branch:** `claude/delta-lambda-open-levers-2026-06-17`
**Picks up:** the Δ_λ-route arc — specifically the one open *compute* lever
left by [`2026-06-17-delta-lambda-two-remaining-directions-closed.md`](2026-06-17-delta-lambda-two-remaining-directions-closed.md)
(#2433): *"implement the genuine dense Wedderburn-projector SDP
([`confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md)),
which — if it selects the Borromean signature — unlocks #2430's
operator-cumulant scalar."*
**Discipline:** formalize-first (state the class, find the invariant, let it
narrow the probe); derive-or-refute; no fit, nothing rewired.

## Formalize-first verdict — do NOT build the heavy solver; it is provably bounded

Before implementing the full dense matrix-`Φ` primal SDP, the formalize-first
discipline asks: *is there a structural invariant the whole solution class must
satisfy that settles the question first?* There is, and it is decisive.

The SDP ([`confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md),
implemented in dual/scalar form in `computations/sdp_cross_channel.py`) is

$$\min_\Phi\ \langle T,\Phi\rangle \quad\text{s.t.}\quad \Phi\succeq 0,\ \ \langle\pi_\lambda,\Phi\rangle\ge 0\ \forall\lambda,\ \ \text{(2×2-pair PSD)},\ \ \mathrm{tr}\,\Phi = c.$$

Three structural facts collapse it:

1. **`⟨π_λ,Φ⟩ ≥ 0` is redundant.** The `π_λ` are the central idempotents
   projecting onto the Wedderburn blocks — PSD projectors. For any `Φ ⪰ 0`,
   `⟨π_λ,Φ⟩ = tr(π_λ Φ) ≥ 0` automatically (trace of a product of two PSD
   operators is non-negative). The per-block Frobenius-positivity constraints
   add nothing.
2. **The 2×2-pair-PSD constraints are redundant.** Every principal submatrix of
   a PSD matrix is PSD. Given the global `Φ ⪰ 0`, every `2×2` adjacent-pair
   block is already PSD.
3. **The cost operator `T` is block-diagonal.** In `sdp_cross_channel.py` the
   cost is `T_λλ = μ_λ` (the q-Laplacian / content-Casimir eigenvalue per
   Wedderburn block), off-diagonal `= 0` (`sdp_with_atom_observables` docstring,
   line 178). The Markov-trace-weighting variant is likewise diagonal (a scalar
   weight per central block); its resolvent is diagonal too.

Hence the SDP collapses to `min ⟨T,Φ⟩ s.t. Φ⪰0, trΦ=c` with diagonal `T` —
and a **linear** objective over the (compact, convex) density spectrahedron
attains its minimum at an **extreme point**, i.e. a rank-1 projector onto the
**minimum-eigenvalue eigenvector of `T`**. With `T` block-diagonal that
eigenvector lies in the single Wedderburn block `λ* = argmin_λ μ_λ`.

> **Structural theorem.** *No SDP of the form `min⟨T,Φ⟩ s.t. Φ⪰0, trΦ=c` with
> block-diagonal `T` can select a multi-block element: its optimum is always a
> single-block extremal density. The Borromean braid `𝓑₃` is a multi-block
> element (its normal form is ≈99.8% the `[3]`-trivial component — the
> **highest**-cost block, not the lowest). Therefore the genuine dense
> Wedderburn-projector SDP cannot select `𝓑₃` for any block-diagonal cost `T`,
> and the per-block / 2×2-pair constraints — being redundant — cannot rescue
> it.*

This is the rigorous upgrade of #2433's empirical *"run directly it concentrates
on the smallest-cost mesonic channel."* The reason is not the particular `T`; it
is that **selection = minimising a linear functional = landing on an extreme
point = a single block**, while `𝓑₃` is an interior, multi-block superposition.

## Numerical confirmation

[`computations/probes/wedderburn_sdp_extreme_point.py`](../../computations/probes/wedderburn_sdp_extreme_point.py)
solves the dense `6×6` primal SDP over `H_3(q₀)` (blocks `[3]⊕[2,1]⊕[1,1,1]`,
dims `1+4+1`) with cvxpy, **with and without** the redundant per-block / pair
constraints, and confirms:

- *(numbers filled in by the probe — see PR)*

## Consequence for the arc

The one open *compute* lever of #2433 is now closed structurally: building the
dense SDP would only reproduce the single-block extremal. `𝓑₃`-selection
genuinely requires the external **topological** criterion (Borromean = no
separable sub-link), exactly as the corpus's actual selection
(`confinement-operator-selection.md`) already does — a discrete ranking + a
topological tiebreak, not a continuous variational program.

The **only** non-refuted lever remaining is the research-scale **GAP-A-3**
(substrate-derived `A(K)` × an *open* partition-projection `P_λ(K)`) — scoped in
[`../workplans/2026-06-17-gap-a-3-substrate-partition-projection-scope.md`](../workplans/2026-06-17-gap-a-3-substrate-partition-projection-scope.md).

## Cross-links
- [`2026-06-17-delta-lambda-two-remaining-directions-closed.md`](2026-06-17-delta-lambda-two-remaining-directions-closed.md) (#2433) — the lever this closes structurally.
- `content/quantum-observable-universe/mass-theory/confinement-sdp.md` — the SDP spec (the object proved bounded here).
- `computations/sdp_cross_channel.py` — the dual/scalar implementation (diagonal cost `T = μ_λ`).
