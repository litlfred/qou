# Per-braid q-Hecke normalization — analysis

**Pair**: [2026-05-01-math-framework-workplan.md](2026-05-01-math-framework-workplan.md) §P2.2c-norm
**Branch**: `claude/audit-math-framework-FXlp2`

## The puzzle

Two complementary per-braid mass-tower results, each correct in
one dimension but wrong in another:

| Variant | ³He vs ³H split? | cal/m_e spread vs AME |
|---------|:----------------:|----------------------:|
| **q=1 MN** ([per_braid_tower.py](../../computations/per_braid_tower.py)) | ❌ identical | ✅ 1.06% |
| **q-Hecke + (c, d)** ([per_braid_tower_q_hecke.py](../../computations/per_braid_tower_q_hecke.py)) | ✅ 47.5% relative | 🔴 65.5% |

Neither is physically right by itself.

## Root cause: Φ_q amplification of asymmetry

Per-nucleon sub-braid traces:

| Path | proton trace | neutron trace | ratio |
|------|-------------:|--------------:|------:|
| q=1 MN | 0.6715 | 0.6715 | 1.000 |
| q-Hecke | 0.8230 | 0.6013 | 1.369 |

When fed into Φ_q (which diverges as z → q ≈ 1.11):

- $\Phi_q(0.6715) \approx 1850$ — moderate
- $\Phi_q(0.8230) \approx \text{much larger}$ (closer to q)
- $\Phi_q(0.6013) \approx \text{much smaller}$

The single-tower term $\sum_i \Phi_q(|\text{tr}_M(\text{nucleon}_i)|)$
becomes dominated by $Z \cdot \Phi_q(\text{proton})$ for Z-rich
nuclei. For ³He (Z=2, N=1) vs ³H (Z=1, N=2):

$$\text{³He single} = 2\Phi_q(0.823) + 1\Phi_q(0.601)$$
$$\text{³H single} = 1\Phi_q(0.823) + 2\Phi_q(0.601)$$

Ratio ≈ 2:1 (since Φ_q(0.823) dominates), giving per-braid totals
of ≈ 41700 vs 21900 — a 2× difference NOT seen in the physical
mass (³He and ³H differ by 0.019%).

## Why q=1 MN "worked" — and why it was lucky

At q=1 MN, both nucleon traces are 0.6715 (S_n character cycle-type
trace, blind to the (c, d) Hecke distinction). This produces a
single-tower term proportional to A (Σ over A identical Φ_q values),
which scales linearly. Linear-in-A matches AME's mass-per-nucleon
≈ const → 1.06% spread.

But the q=1 MN trace is the q→1 LIMIT of the Hecke character.
The Φ_q tower uses q = q_0 = 1.11 ≠ 1. So feeding q=1 MN traces
into Φ_q at q=q_0 is **incoherent**: the trace and the Φ_q live
at different q.

The 1.06% spread was a numerical happy accident enabled by:
- nucleon trace ≈ 0.67 < q_0
- A copies summed → linear-in-A
- AME mass also linear-in-A
- ratio nearly constant

## Three structural options for the live formula

### Option A — Stay at q=1 MN per-braid (current default)

Pros: matches AME well (1.06%), simple.
Cons: physically incoherent (mixed q); cannot split isobars.
Limit: framework will plateau at ~1% accuracy.

### Option B — q-Hecke per-braid with **trace renormalization**

Replace $\Phi_q(|\text{tr}_M(\xi)|)$ with
$\Phi_q(|\text{tr}_M(\xi)| / D_\xi)$ for some
sub-braid-dependent renormalization $D_\xi$.

Candidate choices for $D_\xi$:
- $\dim_q^\xi$ — the q-dim of the smallest representation ξ acts on
- $\sum_\lambda w_\lambda \dim_q(\lambda)$ at the appropriate $H_n(q)$
- $|tr_M(\xi)|$ at q=1 MN (forcing tr_M / dim ≈ 1)

The third candidate would give ratios $0.823 / 0.6715 = 1.226$
for proton, $0.6013 / 0.6715 = 0.895$ for neutron — closer to 1
but still asymmetric.

### Option C — q-Hecke for the descended only; q=1 MN for the tower

Use q-Hecke per-braid only at the descended (level-0) term, where
the asymmetry is exponentially small (10⁻³ to 10⁻⁵ per atom).
Use q=1 MN per-nucleon for the Φ_q tower terms (preserves
linear-in-A scaling).

Splits ³He / ³H via the descended difference (small contribution)
while keeping AME accuracy.

## Status

The framework has **two complementary results** but **no single
formula** that simultaneously:
- Splits ³He from ³H (matches physical 0.53 MeV)
- Preserves linear-in-A scaling (matches A × ~939 MeV/nucleon)

Resolving this is the next research step (**P2.2c-norm**). The
three options above are starting points; the right answer
likely involves a careful re-derivation of the per-braid tower
formula with the q-deformation properly traced through.

## Reference data

| Atom | per-braid q=1 | per-braid q-Hecke | AME mass |
|------|--------------:|------------------:|----------:|
| D    | 3700.78  | 21211.78  | 1875.61 MeV |
| ³He  | 5551.57  | 41727.90  | 2808.39 MeV |
| ³H   | 5551.57  | 21908.72  | 2808.92 MeV |
| ⁴He  | 7402.67  | 42425.34  | 3727.38 MeV |

(q=1 totals from
[per-braid-tower.witness.json](2026-05-01-per-braid-tower.witness.json);
q-Hecke totals from
[per-braid-q-hecke-vs-ame.witness.json](2026-05-01-per-braid-q-hecke-vs-ame.witness.json).)
