# Knot-fusion Step 1 audit — closed-form check (2026-05-17)

> **Question** (raised after PR #679's Wenzl-LR cross-check found
> ~80% divergence on D/T/³He): can the LR identity be lifted to
> work over the **canonical atomic braid** (which includes
> inter-nucleon arc crossings and is not a tensor product)?

## Headline finding

**Yes — and the math, the Rust/Python pipeline, and partial
witness caches already exist on main.** No new theory is required.
The remaining work is **finishing partial χ caches for T/³He/⁴He**
plus a small Σ_λ y_λ · χ^λ combiner.

## The identity (already documented)

[`hecke-branching-trace-decomposition.md`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md)
states the operator-valued Wenzl 1988 branching identity:

$$
\chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
  = \sum_{(\mu,\nu)} \operatorname{Tr}_{V_\mu \otimes V_\nu}\!\Bigl(
       A^\lambda_{\mu,\nu}(I) \cdot
       (\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2))
    \Bigr)
$$

where `I ∈ H_n(q)` is the **interface operator** supported on
boundary strands `{n_1, n_1+1}` — exactly the inter-nucleon arc
that broke my pure-LR consumer.

| Case | `A^λ_{μ,ν}(I)` |
|------|----------------|
| `I = identity` (no interface) | `c^λ_{μν} · 𝟙` — scalar, recovers pure Wenzl LR |
| `I = σ_{n_1}` or general braid interface | **operator-valued in general** (not a scalar multiple of identity) |
| `I = T_{p,k}` torus knot on `V_{(1^n)}` | scalar `α_shift(T_{p,k}) = k(p-1)` (proved in `prop:alpha-shift-torus-knot`) |

The manuscript explicitly notes: *"the original scalar formulation
`A^λ_{μ,ν}(I) = α_shift(I; λ, μ, ν) · 𝟙` is empirically falsified
for 9 of 11 partitions λ ⊢ 6 in the deuteron interface case."*
This is exactly what my pure-LR consumer assumed and why it
diverged.

## What already exists on main

### Math (Lean + manuscript)
- [`hecke-branching-trace-decomposition.md`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md) — full statement + 6-step proof sketch
- [`hecke-branching-trace-decomposition.lean`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.lean) — Lean formalisation
- [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md) — proved scalar case for torus knots

### Numerical witness (machine-precision verified)
- [`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json) — extracts `A^λ_{μ,ν}(I)` matrix entries via 144 `(β_1, β_2)` test pairs in `H_3(q_0) × H_3(q_0)` for the deuteron interface `I = σ_2 − ½(q − q⁻¹)·𝟙`. **All 11 partitions verify to ~10⁻¹⁵** (machine FP limit). Of the **35 `(μ, ν)` blocks** across these partitions, **16 are scalar (multiples of identity)** and **19 are non-scalar operators** (verified via `is_scalar_multiple_of_id` flag in the witness).

### Compute pipeline (parameterised by atom)
[`per_irrep_pole_atom.py`](../../computations/per_irrep_pole_atom.py) — generalised pipeline keyed on `(Z, N)`. Recipe:

1. Load cached symbolic `y_λ(q)` from `y-lambda-wenzl-bridge-symbolic-witness.json` (n=2-12 cached).
2. Load/compute symbolic `χ^λ_q(β_atomic(Z, N))` per partition λ ⊢ n. Cache: `chi-{atom}-h{n}.witness.json`. Multiprocessing across partitions.
3. Substitute `q = u²`, compute `ord_{u=0}(y_λ · χ^λ)`, take max → `shift_NF(β)`.

### Existing chi caches

| Atom | H_n | Cache status | partitions covered |
|------|-----|--------------|-------------------|
| proton | H_3 | **complete** | 3/3 |
| neutron | H_3 | **complete** | 3/3 |
| deuteron | H_6 | **complete** | 11/11 |
| tritium | H_9 | partial | 2/30 |
| ³He | H_9 | partial | 3/30 |
| ⁴He | H_12 | partial | (n/a) |

### Validated results

- `shift_NF(β_p) = 19` — exact match to `18·Z + 21·N + 1 = 19` for (Z=1, N=0)
- `shift_NF(β_D) = 40` — exact match to `18·1 + 21·1 + 1 = 40`
- Predicted: `T: 61, ³He: 58, ⁴He: 79, ⁶Li: 118` (chi-cache compute pending)

## Gap to canonical |tr_M| at 1 ppb

The pipeline computes `shift_NF` (pole-order via `q → u²` substitution), **not** `|tr_M(β_atomic)|` directly. What's missing is a **Σ_λ y_λ(q_0) · χ^λ(β)** combiner that:

1. Reads the same chi cache (`chi-{atom}-h{n}.witness.json`) for the symbolic χ^λ(β)
2. Substitutes `q = q_0` (not `q = u²`)
3. Multiplies by y_λ(q_0) from `wedderburn_jones_markov.y_lambda_at(n, q_0)`
4. Sums over λ
5. Returns absolute value

This combiner is **~50 lines of Python** that reuses both existing pieces (chi cache + y_λ table). No new math, no new infrastructure.

## Step 2 plan (next branch, on user direction)

1. **Finish chi caches** for tritium / ³He / ⁴He via `per_irrep_pole_atom.py`. Cost: tritium ~30 partitions × O(seconds), ⁴He = 77 × O(minutes) symbolic. May want Rust accelerator for ⁴He.
2. **Write `canonical_tr_m_via_chi_cache.py`** combiner (~50 lines).
3. **Extend `cross_check_trM_wenzl_lr_1ppb.py`** with a fourth path: `canonical_chi_cache`. Compare against Hoefsmit / markov_peel for D/T/³He at 1 ppb compute-precision target.
4. **Re-enable the ρ_K overlay layer 4** in `atomic_mass_via_rho_k.py`, this time reading the canonical chi-cache witness (not the broken tensor-product wenzl_lr witness).

## Open question for author

| # | Question |
|---|----------|
| Q5 | Should ⁴He's chi cache be computed in Python (~tens of minutes) or wired to the Rust `hecke-tr-m-wenzl-lr` binary (faster but currently produces the wrong tensor-product answer)? The Rust binary could be extended to compute non-tensor χ^λ via the `A^λ_{μν}(I)` operator-valued formula — that's a larger Rust addition. |

## Net step-1 conclusion

**The "knot-operator LR analog" question is answered:** the operator-valued Wenzl 1988 branching formula (with interface operator `I`) is the right structural identity. It already exists in QOU. The Step-2 work is purely consumer wiring (no new math) plus finishing chi caches for T/³He/⁴He.
