# The dense Wedderburn-projector SDP lever is closed — 𝓑₃-selection ⟺ a fitted cost operator

**Date:** 2026-06-17
**Branch:** `claude/cooperative-cumulant-binding-2026-06-17`
**Picks up:** the Δ_λ-route arc after #2433 (`2026-06-17-delta-lambda-two-remaining-directions-closed.md`)
bounded every tractable lever **except one**: *"implement the genuine dense
per-block Wedderburn-projector SDP (`confinement-sdp.md`, the unbuilt object)."*
This audit **implements that object via its closed form** and shows the lever is
structurally bounded. Discipline: formalize-first, derive-or-refute; no fit,
nothing rewired.

## The one open lever (per #2433)

After the LP (#2417/#2426), the operator-cumulant route (#2430), and the
α-cluster sidestep were all closed, #2433 left a single non-refuted compute
lever: the genuine dense PSD program from
[`confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md),

```
min_Φ  ⟨T, Φ⟩   s.t.  Φ ⪰ 0,  ⟨π_λ, Φ⟩ ≥ 0 ∀λ,  2×2 pair-PSD,  tr Φ = n_target
```

which, *if* it selected the Borromean signature 𝓑₃, would unlock the
operator-cumulant binding scalar of #2430. It was "stated but not implemented".

## Formalize-first: the SDP has a closed form, so no solver is needed

Two structural facts collapse the program (and prune the multi-session build the
workplan feared):

1. **The "richer" constraints are redundant.** The central idempotents `π_λ` are
   PSD projectors, so for any `Φ ⪰ 0`, `⟨π_λ,Φ⟩ = tr(π_λΦ) ≥ 0` automatically;
   and a principal 2×2 submatrix of a PSD matrix is PSD. So the per-block
   Frobenius-positivity rows **and** the adjacent-pair rows add nothing — the
   program reduces to `min⟨T,Φ⟩ s.t. Φ⪰0, trΦ=n`.

2. **The reduced program is the classic eigenvalue SDP:**
   `Φ* = n_target · v vᵀ` with `v` = unit min-eigenvector of `T`,
   value `= n_target · λ_min(T)`.

**Therefore the dense Wedderburn-projector SDP selects exactly the
minimum-eigenvector of the cost operator `T`.** "Does it select 𝓑₃?" reduces to
"is 𝓑₃ the min-eigenvector of a *non-fitted* `T`?" — a 6×6 eigenproblem, run in
[`computations/probes/b3_dense_sdp_wedderburn_projector.py`](../../computations/probes/b3_dense_sdp_wedderburn_projector.py).

## Result — every non-fitted cost selects the mesonic channel, not 𝓑₃

| cost operator `T` (non-fitted) | min-eigvec | Markov cost `t` | full-cos → 𝓑₃ | is 𝓑₃? |
|---|---|--:|--:|:--:|
| `diag(t)`  (Markov-trace weighting) | `L₊` | 0.249 | 0.046 | no |
| `G`  (q-Laplacian / Gram) | `L₊` | 0.249 | 0.064 | no |
| `G⁻¹`  (Gram resolvent) | `L₊` | 0.249 | −0.064 | no |
| `−(G − λ_max·I)`  (resolvent inv.) | `e⁻` | 0.551 | 0.346 | no |
| **`−𝓑₃𝓑₃ᵀ`  (FITTED to the answer)** | `γ` | (n/a) | **1.000** | **YES (fit)** |

**The one-line reason (sharper than #2433's sig-cos control):** `NF(𝓑₃)` is
**99.8% γ**, the identity channel, which carries the **maximum** Markov-trace
cost `t_γ = 1.0 = max(t)`. A cost-**minimizing** PSD program selects the
**smallest**-cost channel — the mesonic `L±` (`t = 0.249`) — the structural
**antithesis** of 𝓑₃ (full-cos ≈ 0.05, essentially orthogonal). A minimizer can
never land on the max-cost identity direction that 𝓑₃ essentially is. The only
`T` whose ground state is 𝓑₃ is one built **from** 𝓑₃ (`−𝓑₃𝓑₃ᵀ`), i.e. a fit —
forbidden by the CAL-4 / three-calibration discipline.

> **Note on sig-cos.** Scored in the γ-orthogonal subspace, the `L±` selections
> have *high* sig-cos (0.71–0.98) — but that is a tiny-norm artifact: 𝓑₃'s
> norm-0.065 γ-orthogonal *tail* happens to lie along `L±`. The tail is not the
> operator; the operator is 99.8% γ, which the SDP misses entirely. **full-cos**
> is the honest "is it 𝓑₃" metric, and it is ≈ 0.

## Net — the Δ_λ gate is now closed on every compute lever

| lever | status |
|---|---|
| sign = chirality | **proved** (keystone, option-e #585ca846/#2416) |
| scalar magnitude / trace functional | **refuted** (#2417 — scalar trace factorizes exactly) |
| operator-cumulant scalar | **gated** on 𝓑₃-selection (#2430) |
| 𝓑₃-selection by any continuous principle | **refuted** (#2433 (1)) |
| dense Wedderburn-projector SDP (the last open lever) | **closed here — selection ⟺ a fitted `T`** |
| α-cluster sidestep | **fit-blocked** (#2433 (2)) |

The operator-cumulant route (#2430) was gated on 𝓑₃-selection; with the SDP
lever now closed, that gate is **structural, not pending**. The remaining
non-refuted directions are research-scale only (**GAP-A-3**: substrate-derived
`A(K)` × an open partition-projection `P_λ(K)`), or **promoting the discrete
topological criterion** (Borromean = no separable sub-link) *into* the selection
program rather than applying it as an after-the-fact tiebreak — a change of
selection principle, not a continuous optimization. Neither is a quick or
fitted closure.

## Companion finding — the ⁶Li chirality discriminator (falsifiable)

The chirality *sign* is the proved half of Δ_λ, but the production net-chirality
is a **hardcoded (Z,N) table** (`paper_six_term_isotope_sweep.py:1260`,
alternating, net = L mod 2), not derived (corpus audit on
`claude/chirality-shell-signs-2026-06-17`;
[`computations/chirality_shell_sign_probe.py`](../../computations/chirality_shell_sign_probe.py)).
The decisive, parameter-free test that distinguishes **structural** from
**hardcoded**:

> **⁶Li.** The hardcoded table gives net **0** (L = 6 even). But ⁶Li's ground
> state is **J = 1** (deuteron-like — an unpaired ³S₁ np pair), so a structural
> unpaired-spin-1-pair / Wigner-SU(4) rule predicts net **+1**, like the
> deuteron. Corroborating indicators both point to +1: `ZN mod 2 = 1`, and the
> trace-weighted option-e parity `⟨sgn⟩ = +0.0638` (positive). ⁶Li's
> experimental J = 1 favours the structural **+1** ⇒ the hardcoded table is
> likely **wrong** at ⁶Li.

This does **not** close binding (the magnitude gate above stands), but it
records the one cheap falsifiable prediction that would settle structural-vs-
hardcoded net chirality. Owned by the chirality sibling; cross-linked here.

## Cross-links
- [`b3_dense_sdp_wedderburn_projector.py`](../../computations/probes/b3_dense_sdp_wedderburn_projector.py) — this audit's closed-form SDP probe.
- [`b3_selection_signature_cos.py`](../../computations/probes/b3_selection_signature_cos.py) — #2433's continuous-principle control.
- `docs/audits/2026-06-17-delta-lambda-two-remaining-directions-closed.md` (#2433) — the audit that named this lever as the last open one.
- `docs/workplans/2026-06-17-operator-cumulant-cooperative-binding.md` (#2430) — the operator route gated on 𝓑₃-selection.
- `content/quantum-observable-universe/mass-theory/confinement-sdp.md` — the SDP spec implemented here in closed form.
- `computations/chirality_shell_sign_probe.py` — the ⁶Li discriminator (chirality sibling).
