# Δ_λ gate is a *scale* gate: log|tr_M| is quadratic in A (2026-06-09)

**Status:** exploratory finding (no production wiring). Quantifies *why*
the six tabulated constant/structural Δ_λ ansätze fail, and pins what
Δ_λ must structurally be. This is a **refutation + characterization**,
not a seventh fit ansatz (cf. CLAUDE.md "Δ_λ gate (Track A blocker)").

> **⚠ Correction (2026-06-09, owner-confirmed).** The `tr_M` analysed below
> is the **H₃-local `build_atom_nf` NF** (gen 0/1 forced into the 6-dim
> H₃), whose coefficients blow up — the *mass-path projection*, **not** the
> object the binding formula uses. The **canonical binding `tr_M` is the
> H_{3A} matrix-M Markov trace**, which is **O(1)** (deuteron 1.332,
> tritium 1.086) and does **not** blow up. So the "scale gate" below is
> **route-specific to the H₃-local representation; it does NOT block the
> canonical Δ_λ binding closure.** On the canonical (matrix-M) object the
> required Δ is **mild** (O(1–10), per-nucleus), not 10^459 — see
> [`atom_vhyp_closure_matrix_m.py`](../../computations/atom_vhyp_closure_matrix_m.py)
> and its witness. The text below is retained as the (still-correct)
> characterization of the *H₃-local route's* failure.

## Setup

The per-isotope binding law is

$$ B(K) = m_e \sum_\lambda y_\lambda\, \chi^\lambda(\beta_K)\, \Delta_\lambda(K). $$

Using the overflow-free Wedderburn-block computation from the
[SDP-v2 probe](../../computations/all_nuclides_wedderburn_spectral_v2.py)
(40-dps mpmath block images of `build_atom_nf`, all 3558 AME nuclides),
this analysis
([`delta_lambda_feed_analysis.py`](../../computations/delta_lambda_feed_analysis.py),
witness
[`delta-lambda-feed-analysis.witness.json`](../../computations/delta-lambda-feed-analysis.witness.json))
characterizes the per-block χ_λ(a) against the AME binding B(A,Z) for the
N = 3554 nuclei with A ≥ 2 and B > 0.

## Finding

| quantity | law | fit |
|---|---|---|
| `log₁₀|tr_M(a)|` vs A | **quadratic** `0.0124 A² − 0.186 A + 1.29` | **R² = 0.99993** |
| `log₁₀|tr_M(a)|` vs A (linear only) | — | R² = 0.930 (much worse) |
| `log₁₀|tr_M(a)|` vs crossing count T | linear | R² = 0.999 |
| binding `B` vs A | linear | R² = 0.9915, B/A ∈ 0.02–8.79 MeV |

The Wedderburn characters `χ_λ(a)` grow **quadratically in A on the log
scale** — i.e. super-exponentially — because the atom crossing count is

$$ T(Z,N) = 11A + \tfrac{A(A-1)}{2} + Z \approx \tfrac{A^2}{2} $$

(proved + verified on all 3558 nuclides in the v2 probe, including the
closed form `sign(χ_alt) = (−1)^T`). `|tr_M|` reaches **~10^1025** at the
heavy end, while binding is **linear** (`log₁₀ B ≤ 3.3`). The scale
mismatch between χ_λ(a) and B is ~10^1000.

## Consequence — the gate is a scale gate

For the formula to hold, the required channel factor

$$ \Delta_\lambda(K) = \frac{B(K)}{m_e\, y_\lambda\, \chi_\lambda(a)} $$

must **absorb the exponential**. Measured on the dominant (alt) channel,
the required `Δ_alt(K)`:

- is **NOT constant** — it spans **~459 orders of magnitude** across the
  chart, and
- is **itself quadratic in A** (R² = 0.94, `log₁₀ Δ_alt ≈ −0.0068 A² …` —
  distinct from the `tr_M` coefficient 0.0124, since the alt block alone
  grows slower than the std-dominated `tr_M`).

So **no per-partition constant `Δ_λ` can close the formula** — this is
the structural reason the six prior ansätze (Frobenius co-Casimir,
Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented
Markov) fail, especially as A grows. `Δ_λ(K)` must be a **per-nucleus
~10^(−cA²) normalization** in the crossing count.

## Where this points (does not close)

A per-nucleus factor decaying like `10^(−c·A²)` in the crossing count is
exactly the shape of an **inverse hyperbolic-volume / packing-density**
term — consistent with the `ρ_F · V_hyp` binding law
(`rem:frobenius-packing-density`) and the canonical mass form
`m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`. The productive reading: `Δ_λ` is not
a Wedderburn-block constant to be discovered, but the **per-nucleus
volume/density normalization** that divides out the crossing-count
growth. This matches the GAP-A-3/GAP-A-4 directions
([`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md))
and does **not** reopen the fit-ansatz path.

## Caveat

Exploratory. The χ_λ(a) here are characters of the *full* `build_atom_nf`
crossing product; the binding β_K in the canonical formula may be a
reduced/normalized braid, which would change the prefactor but not the
A²-vs-A scale argument (the crossing count is intrinsic to the
construction). No production code consumes this analysis.
