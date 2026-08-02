# The q-Reeb eigenphase route is compact — it cannot supply the absolute binding scale `C_knot`

**Date:** 2026-08-02 · **Bean:** qou-0g4z (surviving lead of qou-3q7t) · **Axis:** Δ_λ / binding
magnitude · **Discipline:** formalize-first, 0-fit, scope-(a) negative; nothing wired.

## Context

After the single-universal-`C_knot` / single-scale route to the Δ_λ magnitude gate was refuted
(PR #4556: `C_knot = B_AME/(m_e·|Σ_λ y_λ χ^λ f^λ|)` is non-universal, spread 2.83× across D/T/³He/⁴He),
the one non-circular surviving lead was the **per-vertex q-Reeb eigenphase**

```
θ_λ  =  arccos(χ_λ / d_λ),        2 cos θ_λ  ~  (block-averaged) knot-operator eigenvalue phase,
```

the accumulated rotation angle of the knot operator on the Wedderburn block `V_λ`. This is already
formalized for the **figure-eight muon anchor** (`figure-eight-reeb-rotation`,
`figure-eight-reeb-theta-value`), where `2 cos θ = tr M_{4₁}(q)` and the perfect-square identity
`tr M_{4₁}(q) + 2 = (q² − 1 + q⁻²)²` gives `tr M_{4₁}(q) ≥ −2` for all real `q` — the block is
**provably compact** (the eigenvalue never leaves the unit circle on the real substrate axis; the
q-Reeb angle stays a bounded rotation).

The E₀-substrate-options audit (2026-06-01) had found the eigenphase route (its Candidate 3) closes
only **differences** (³H−³He to 2 %, B_D to −9 %); the v6 attempt to reach an absolute scale
re-introduced a free scale `γ` (a fit). The open question for qou-0g4z was whether that
difference-only limitation is **structural** or merely un-probed.

## What was measured (0-fit)

`computations/deltalambda/qreeb_eigenphase_compactness_probe.py` reads the committed per-partition χ
witnesses (`chi-{deuteron,tritium,helium-3}-*-at-q0-50dps.witness.json`) — the categorical characters
only; **`B_AME` is never read, `free_parameters = 0`** — and reports the block-by-block normalized
character `|χ_λ/d_λ|`:

| K | H_n | blocks | sole `|χ/d|>1` block | max `|χ/d|` among dim ≥ 2 (rotation) blocks |
|---|-----|--------|----------------------|---------------------------------------------|
| D | 6 | 11 | `(6,)` dim 1, `1.5599` | **0.8499** @ `(3,3)` — compact |
| T | 9 | 30 | `(9,)` dim 1, `1.5769` | **0.4676** @ `(8,1)` — compact |
| ³He | 9 | 30 | `(9,)` dim 1, `2.3937` | **0.8211** @ `(8,1)` — compact |

## Finding

**In every binding knot the only block with `|χ_λ/d_λ| > 1` is the trivial 1-dimensional
representation `(n,)`.** The trivial rep is the algebra map `σ_i ↦ q`, so its character on a
positive-writhe braid word is `q^{w}` — a **pure real scaling** by the writhe `w`. A 1-dimensional
block has no internal mixing, hence **no rotation angle at all**: the eigenphase `θ_λ` is simply not
defined there (`arccos` needs `|χ/d| ≤ 1`; when `|χ/d| > 1` there is no real `θ` with `cos θ = χ/d`,
since `|cos θ| ≤ 1` always).

**Every genuinely-rotational block (dim ≥ 2), where `θ_λ` is defined, is compact** (`|χ/d| ≤ 1`,
max 0.85 across all three knots). So the entire q-Reeb *rotation* content of a binding knot is a set
of **bounded, dimensionless angles** `θ_λ ∈ [0, π]`.

Consequences:

- A predictor assembled purely from the eigenphases `{θ_λ}` is bounded and scale-free: it fixes
  **ratios**, not the absolute MeV value. This is exactly the "closes only differences" behaviour the
  E₀ audit observed — now seen to be **structural**, not a probe artifact.
- The **sole unbounded channel** is the trivial-rep scaling `q^{w}`. But that term is **already a
  summand of the master binding formula** `B = m_e·|Σ_λ y_λ χ^λ f^λ|` (the `(n,)` contribution
  `y_{(n,)}·q^{w}·1`). It is not an un-probed radial handle: the master sum already includes it and
  still misses by `C_knot`.

**Therefore the q-Reeb eigenphase route cannot supply the missing absolute binding scale `C_knot`.**

## Scope discipline

- **scope-(a):** the eigenphase route, *alone*, does not close the Δ_λ magnitude gate. Confirms +
  sharpens the E₀-options "difference-only" finding into a structural statement about *where* the
  limitation comes from (compact rotation channels + a single already-summed scaling channel).
- **Not scope-(b) structural exclusion of Δ_λ closure in general.** This does **not** refute the Δ_λ
  magnitude derivation; it prunes one specific mechanism (the eigenphase as the absolute-scale
  carrier). The magnitude derivation stays **OPEN** (bean qou-0g4z / qou-3q7t).
- No fit; nothing wired; `B_AME` diagnostic-only (in fact unread); `free_parameters = 0`.

## Machine-checked (Lean, sorry-free, lean-direct exit 0)

`content/quantum-observable-universe/lean/QOU/MassTheory/QReebEigenphaseCompact.lean`:

- `no_rotation_angle_of_boost` — `1 < |x| → ¬ ∃ θ, cos θ = x` (general; the boost channel has no
  rotation angle).
- `trivial_char_is_scaling` — `1 < q → w ≠ 0 → 1 < q^w` (the trivial-rep character exceeds the
  trivial dimension 1: a growing scaling, not a bounded angle).
- `deuteron/triton/helium3_boost_is_one_dim_trivial` — the witnessed `ℝ` facts (sole boost `> 1`,
  rotation max `< 1`).
- `compact_eigenphase_bounded` — `arccos x ≤ π` (compact eigenphases are bounded).
- `eigenphase_route_is_compact` — capstone.

## Why the route was always doomed — information-equivalence (front 3, sharpened scope-(a))

The negative is stronger than "the numbers don't work": the compact eigenphase carries **no
information beyond the character it encodes**. `arccos` is a bijection `[-1,1] ↔ [0,π]`, so on every
block where `θ_λ = arccos(χ_λ/d_λ)` is defined,

```
χ_λ = d_λ · cos θ_λ            (char_from_eigenphase),
θ_λ = arccos(cos θ_λ)          (eigenphase_bijective_on_range),
```

i.e. `χ_λ ↦ θ_λ` is a **lossless reparametrization** of the compact-block characters. But those `χ_λ`
are exactly the terms already summed in `S(K) = Σ_λ y_λ χ_λ f^λ`. So an eigenphase-based predictor is
the *same data in angular coordinates* — it cannot introduce the missing scale. The one block the
eigenphase cannot encode (the trivial `q^w` boost, `no_rotation_angle_of_boost`) is itself already a
summand of `S(K)`. The scale must therefore come from **outside** the character data.

**Honest scope caveat (NOT scope-(b)).** This does **not** prove that *no* substrate function yields
`C_knot`: `C_knot` is dimensionless and bounded (3.3–9.3), so no dimensional or boundedness argument
excludes a substrate function in general (per AGENTS.md §"Before declaring refuted"). What is excluded
is the **eigenphase reparametrization**, by the bijection above. Labelling this a general impossibility
would be an over-claim; it is a precise scope-(a) statement about one construction.

## Surviving directions for qou-0g4z (unchanged by this negative)

The absolute scale must come from something the eigenphases structurally cannot carry — i.e. **not** a
bounded rotation angle. Candidates that remain open (each needs its own probe, none a fit):

1. A **dimensionful geometric input** (hyperbolic volume / cusp shape) already present in the muon
   anchor `Vol(4₁)` but not yet threaded into the per-isotope binding — i.e. the scale is *radial*
   (volume-like), consistent with the mass formula `m = m_e·Vol(K)·ρ/ℏ_q²`, and the binding closure
   needs a per-knot `Vol/ρ` handle, not an eigenphase.
2. The trivial-rep scaling `q^{w}` is present but *insufficient alone* — a genuine many-body closure
   would re-weight it against the compact channels (a cross-term structure), which the pairwise
   probes cannot see (§"compositional object is already many-body", AGENTS.md).

Neither is closed here; this audit only removes the eigenphase-as-scale hypothesis.
