# Workplan: atom → V_hyp map → Δ_λ closure (2026-06-09)

**Goal.** Close the per-isotope binding `B(K) = m_e Σ_λ y_λ χ^λ(β_K) Δ_λ(K)`
by deriving the per-nucleus channel factor `Δ_λ(K)` as a volume/density
quantity, via the knot-convolution operator `⋈_K` on the active sets.

**Why now / status of the gate.** The
[SDP-v2 Wedderburn-spectral probe](../../folio-assistant/computations/all_nuclides_wedderburn_spectral_v2.py)
and the
[Δ_λ feed analysis](../audits/2026-06-09-delta-lambda-gate-quadratic-obstruction.md)
established (re-confirming known territory) that `Δ_λ` is **not** a
per-partition constant: `log|tr_M(a)|` is quadratic in A (R²=0.9999;
crossings `T ≈ A²/2`), binding is linear, and even `Δ ∝ q^(−T)` fails
(R²≈0 for A≤26). So `Δ_λ(K)` must be a **per-nucleus volume/density**
factor — the `ρ_F·V_hyp` / `m(K)=m_e·Vol·ρ/ℏ_q²` direction (GAP-A-3/4).

## The map (3 stages)

```
(Z,N) ──①──▶ atom knot index / χ^λ   ──②──▶ V_hyp(K)        ──③──▶ Δ_λ(K) ──▶ B(K)
        ⋈_K on active sets            depth-2 τ_arch          vol_density
        (matrix-M at A≥4)             (Li_2^q image OR SnapPy) (Vol·ρ/ℏ_q²)
```

### Stage ① — per-nucleus χ^λ via `⋈_K` on active sets — **HAVE (extend coverage)**
- `⋈_K` is the depth-0 knot-indexed Hecke convolution
  ([`knot-indexed-convolution-grid`](../../content/quantum-observable-universe/mass-theory/knot-indexed-convolution-grid.md));
  `build_atom_nf` already *is* such a convolution chain.
- **A≥4 χ infra EXISTS** (corrected 2026-06-09 — not a new-infra gap):
  - [`chi_at_q0_via_matrix_m_mpfr.py`](../../folio-assistant/computations/chi_at_q0_via_matrix_m_mpfr.py)
    — per-nucleus χ^λ(q₀) via the matrix-M reduced-block kernel at mpfr;
    witnesses for **deuteron** and **tritium (H₉, A=3)** at 50 dps.
  - [`derived_chi_catalogue_matrix_m_multi_a_benchmark.py`](../../folio-assistant/computations/derived_chi_catalogue_matrix_m_multi_a_benchmark.py)
    — multi-A χ catalogue; native `pyhecke_native.chi_via_matrix_m_mpfr`.
  - SDP-v2 supplies the **active sets** (Wedderburn blocks per nucleus).
- **Tractable next:** drive `chi_at_q0_via_matrix_m_mpfr` over the active
  sets to emit a per-nucleus χ^λ table feeding Stage ③. ~0.5 day for the
  A≤4 set already covered by matrix-M.

### Stage ② — χ^λ / knot index → V_hyp — **TWO ROUTES; algebraic one sidesteps the topology gap**
- **Route A (algebraic, tractable):** V_hyp is the **depth-2 archimedean
  image** of the depth-0 convolution (bi-filtration: "Markov trace +
  braid of a hyperbolic knot lands at depth 2 (volume)"). Compute it as
  the `Li_2^q` / Rogers-dilog image of the matrix-M χ — **no SnapPy, no
  link diagram**. This is exactly what `vol_density` already does for the
  Borromean nucleon; the task is to feed it the matrix-M χ at A≥4.
- **Route B (geometric, gated):** SnapPy on the atom link complement.
  Blocked by the atom→link-diagram realization (only 3 primitives
  tabulated: 4_1, 5_2, 6³_2; `snappy` not installed). For A≥4 the atom is
  a composite/satellite link (JSJ) — this is the genuine remaining gap.
- **Sharpening (do the tractable bits first):**
  1. A≤3 (²H, ³H, ³He): matrix-M χ exists → run Route A end-to-end now.
  2. A=4 (⁴He): matrix-M coverage being extended; the
     [A-8/9 path audit](../audits/2026-06-08-matrix-m-optimization-A-8-9-path.md)
     + [A5–A7 wiring-gap audit](../audits/2026-05-24-a5-a7-isotope-wiring-gap.md)
     are the frontier — extend matrix-M coverage A=4→9 first.
  3. Use Route A (Li_2^q image) as the V_hyp source for all A where
     matrix-M χ is available; reserve Route B (SnapPy) only to *validate*
     V_hyp on the 3 primitives + as the cross-check.

### Stage ③ — V_hyp → Δ_λ via depth-2 functor — **HAVE**
- [`_li_2_q_util.py`](../../folio-assistant/computations/_li_2_q_util.py)
  (`li_2_q`, `vol_density_borromean`, `vol_density_per_block`) +
  [`mass_vol_density.py`](../../folio-assistant/computations/mass_vol_density.py)
  (`vol_density_vd(vol_K, q) = Vol·ρ/ℏ_q²`) already implement the depth-2
  image / the canonical mass form. **Not a fit** — `vol_density` is
  canonical.
- **Tractable next:** wire `Δ_λ(K) = vol_density_per_block(V_hyp(K),
  tr_M(K), q₀)` and test `B_pred(K)` vs AME for the matrix-M-covered set.

## Critical path & sequencing
1. **① + ③ (build now):** matrix-M χ driver over active sets → `vol_density`
   → `B_pred`, on the A≤3 (+ A=4 as coverage lands) matrix-M set. Decisive
   closure test on the tractable subset.
2. **② Route A (build now):** Li_2^q depth-2 image as V_hyp from matrix-M χ
   — closes the loop algebraically without SnapPy.
3. **② coverage (narrow the gap):** extend matrix-M A=4→9 (existing
   A-8/9 path + A5–A7 wiring-gap audits) — this is the real remaining
   work, but it is *coverage extension of existing infra*, not new infra.
4. **② Route B (validation only):** SnapPy on the 3 primitives to
   cross-check Route A's V_hyp; the atom→satellite-link map (A≥4) stays a
   topology research item, needed only if Route A diverges from data.

## Discipline notes
- **Exploratory; no production wiring** until a closure passes the
  three-calibration review.
- `vol_density` / `Li_2^q` are **canonical** (not fits); the test is
  whether the *canonical* volume-density `Δ_λ` reproduces AME B — a
  forward prediction, not a parameter fit. Avoids the "seventh ansatz"
  trap (CLAUDE.md Δ_λ-gate note).
- Feeds: SDP-v2 active sets + matrix-M χ + `_li_2_q_util` are the inputs;
  the per-nucleus χ tables are the durable artifact.
