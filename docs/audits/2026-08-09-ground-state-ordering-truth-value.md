# `prop:ground-state-ordering` — per-clause truth value

**Bean** `qou-48is`. **Status: IN PROGRESS** (audit stub; verdict pending the exact sweep).

## Question

`prop:ground-state-ordering` asserts that the nuclear ground-state nucleon
ordering is the one **minimising** `Φ_q = Σ_i log|V̂_i|`, and that this
minimiser is

- **(A ≥ 4)** interleaved + tail-packed, and
- **(A ≤ 3)** sorted (all protons first).

The block is **stated, not proved**: the Lean is a `def … : Prop` with no
discharging instance, and `.ts` carries `validation: "not_checked"`.

## Method (planned)

Exhaustive sweep of `Φ_q` over **all** `C(A,Z)` arrangements, through the
corpus's own `_phi1_from_ordering_sym`, at the experimental (proton) `q₀`
pin, for both readouts:

- `Φ_nuc` — the bare nucleon chain, and
- `Φ₁` — the nucleon chain with the `["e"] * Z` tail appended
  (what `compute_phi1_full_sym` actually calls).

## Verdict

*(pending)*
