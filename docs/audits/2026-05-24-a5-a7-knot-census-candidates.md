# A ∈ {5, 6, 7} knot-census candidates — literature scan for ⁵Li, ⁶Li, ⁷Li target volumes

**Date:** 2026-05-24
**Branch:** `claude/post-1089-followups-2026-05-24`
**Parent gap audit:** [`2026-05-24-a5-a7-isotope-wiring-gap.md`](2026-05-24-a5-a7-isotope-wiring-gap.md)
**Status:** EXPLORATORY shape-probe. NOT a production assignment. Owner-direction required before any wiring lands.

## Purpose

The parent gap audit identifies that
[`mass_table_ppb.py`](../../computations/mass_table_ppb.py)
has no atom→knot rule for `A ∈ {5, 6, 7}`. This doc surveys the
hyperbolic knot/link census (from memory of SnapPy's
`HTLinkExteriors`, `OrientableCuspedCensus`, Rolfsen, Hoste–
Thistlethwaite, and standard link families) for objects whose
volumes sit near the Kashaev-law target windows.

Per CLAUDE.md production-vs-exploratory discipline, this is a
**shape-probe**: census matching is the CAL-4-equivalent path
already flagged in `mass_table_ppb.py:18–21`. Repeating it for
A ∈ {5, 6, 7} extends the hidden-fitting surface, so no assignment
recommended here should be wired without an independent
categorical justification.

## Targets

Kashaev law: `B_pred = ρ_F · m_e · Vol_hyp(K)`,
`m_e = 0.51099895 MeV`, `ρ_F ∈ {m_e, 2m_e}`.

| Atom | B_AME (MeV) | Vol (ρ=m_e) | Vol (ρ=2m_e) | Stability |
|------|-------------|-------------|--------------|-----------|
| ⁵Li  | 26.328      | 51.52       | 25.76        | resonance ~10⁻²² s |
| ⁶Li  | 31.99405    | 62.61       | 31.30        | stable, J^π = 1⁺ |
| ⁷Li  | 39.24453    | 76.80       | 38.40        | stable, J^π = 3/2⁻ |

The (ρ=m_e) targets (51.5 – 76.8) are **far above** the small-knot
census ceiling (most prime knots up to 16 crossings have Vol < 25).
The (ρ=2m_e) targets (25.8 – 38.4) sit at the **upper end** of
known prime-knot volumes and squarely inside the multi-component
link census.

## Census candidates by volume range

### Small reference anchors (canonical, already in `knot_volumes.py`)

| Object | Volume | Source |
|--------|--------|--------|
| Vol(4_1) figure-eight | 2.0299 | minimum cusped 3-mfd (Cao–Meyerhoff) |
| Vol(5_2) | 2.8281 | second-smallest |
| Vol(6_2) | 4.4008 | current ²H assignment |
| Vol(7²_1) | 4.7495 | α-α coupling constant |
| Vol(8_11) | 8.2863 | current ³H assignment |
| Vol(L6a4) Borromean = 8G | 7.3277 | Thurston/Catalan |

### ρ=2m_e targets (25.8 – 38.4) — prime-knot range

Prime knots in the Hoste–Thistlethwaite census reach Vol ≈ 20
around 14–15 crossings (e.g. `15n_*` saturated cables).
Genuine prime-knot volumes ≥ 25 are rare and most candidates
in this window are **multi-component hyperbolic links**:

- **⁵Li target 25.76** (ρ=2m_e):
  - Chain link `L8a*` family — needs SnapPy census verification.
  - Two-bridge link cables — Vol around 25 plausible but no
    specific name comes to mind with confidence > 0.5 in volume.
  - 🟡 No high-confidence small-name match. Needs census query.

- **⁶Li target 31.30** (ρ=2m_e):
  - **3-component chain links / Whitehead chains** — Vol scales
    roughly as `n_components · Vol(Whitehead)` ≈ n · 3.66, so a
    ~8-component Whitehead chain would land here, but the
    "magic-A topology" interpretation is unclear.
  - 🟡 Plausible but no specific named link recalled with
    sufficient confidence.

- **⁷Li target 38.40** (ρ=2m_e):
  - 5-cusp Borromean-like links — Vol ≈ 30–40 range.
  - 🟡 Same caveat — needs SnapPy `OrientableCuspedCensus`
    enumeration with volume filter `[37, 40]`.

### ρ=m_e targets (51.5 – 76.8) — multi-component / satellite range

All three (ρ=m_e) targets sit above the volumes of any prime knot
≤ 16 crossings. Candidates would be:

- **Iterated chain links** (Whitehead-chain length 12+),
- **Satellite knots** (cable of cable of …),
- **Augmented hyperbolic links** (volume scales with augmentation).

🟡 No specific named manifold recalled with confidence > 0.5
in volume for these targets. Census search required.

## Multiplicative-ratio pattern check

Testing target / canonical-anchor for clean integer ratios:

| Target (ρ=m_e) | / 8G (7.3277) | / Vol(7²_1) (4.7495) |
|----------------|---------------|----------------------|
| 51.52 (⁵Li)    | **7.030**     | 10.847               |
| 62.61 (⁶Li)    | 8.544         | 13.183               |
| 76.80 (⁷Li)    | 10.481        | 16.170               |

| Target (ρ=2m_e) | / 8G | / Vol(7²_1) |
|-----------------|------|-------------|
| 25.76 (⁵Li)     | 3.515 | 5.424      |
| 31.30 (⁶Li)     | 4.272 | 6.591      |
| 38.40 (⁷Li)     | 5.240 | **8.085**  |

**One striking near-integer ratio**: ⁵Li(ρ=m_e) / 8G ≈ **7.030**.
If interpreted as `B(⁵Li) ≈ m_e · 7·(8G)`, this is "seven
Borromean copies" — but the physical interpretation is opaque
(⁵Li has 5 nucleons, not 7). The 0.03 residual is ~0.4% which
is far from the 100×-experimental L2 target; likely coincidence.

⁷Li(ρ=2m_e) / Vol(7²_1) ≈ **8.085** is the next-closest integer
hit, again with no obvious physical reading.

No clean structural pattern emerges. The targets do **not** sit on
a simple `n_α · 8G + k · Vol(7²_1)` lattice, which is the
extension that would have made the existing α-cluster rule a
natural generalisation.

## Matter/topology mismatch flags

### ⁵Li — resonance, not bound state

⁵Li lifetime ≈ 10⁻²² s. The Kashaev volume law as currently
written produces a finite positive `B_pred`, which would predict
a **bound** state. Per CLAUDE.md §7b, unstable intermediaries
are properly modelled as **Demazure sub-crystals** of a larger
crystal — incomplete topological states whose Macdonald
evaluation reproduces broken-symmetry / short-lived behaviour.

🔴 **Assigning a stable hyperbolic knot to ⁵Li would
mis-categorise it as bound matter.** The canonical framing is a
Demazure sub-crystal of the A=5 sector. This is independent of
which volume target one picks: the topology assignment is wrong
in kind, not just in number. The Kashaev law itself does not
apply to resonances without further qualification.

### ⁷Li — spin 3/2 ground state

⁷Li has `J^π = 3/2⁻`. The current Kashaev-law assignments
(²H = 6_2, ³H = 8_11, ³He = L6a4) make no use of spin/parity —
they extract a single scalar `B` from the volume. If higher-spin
ground states require the closure topology to carry the
representation-theoretic data (e.g. selecting a partition
λ ⊢ n with `λ_1 − λ_2` matching `2J`), then the choice of
hyperbolic manifold for ⁷Li is constrained beyond volume
matching — only those whose Wedderburn-block decomposition
contains the `J = 3/2` sector would be admissible.

🟠 **The current single-knot model has no place to encode
J^π.** Both ⁶Li (J=1⁺) and ⁷Li (J=3/2⁻) should likely require
multi-cusp links whose link-group representations carry the
spin sector. Volume matching alone is insufficient.

### ⁶Li — α + d cluster

Empirically, `B(⁶Li) − B(⁴He) − B(²H) = 1.47 MeV` of α-d
binding (parent audit §Path 1). The natural categorical reading
is **not** a single knot of Vol ≈ 62.6 but a **link** of the
4He-knot and the d-knot (6_2) with a small additional coupling.
This points to Path 2 (multi-knot `VolDensity(K_1 ⊔ K_2)`) rather
than census search. Specifically, the framework already has a
canonical "two linked Borromean rings" → c_αα motif for α-α; the
α-d analogue would be a similar link of the 4He topology with
6_2 (deuteron), at a coupling needing independent derivation.

## Recommendation (EXPLORATORY)

🟡 **Do not wire any single-knot Kashaev assignment** for ⁵Li,
⁶Li, or ⁷Li from this census-scan output. The three flags above
each independently undermine the single-knot framing.

Preferred direction (per parent audit Path 2, reinforced by the
multiplicative-ratio negative result and the J^π / resonance
flags): **wait for PR #1081 Task 3** (S₅ ↔ SO(3) fibre action)
and develop **multi-knot `VolDensity(K_1 ⊔ K_2 ⊔ …)`** for
α + valence-nucleon configurations. Specifically:

1. ⁶Li → `VolDensity(L6a4_α ⊔ 6_2_d)` with α–d link coupling.
2. ⁷Li → `VolDensity(L6a4_α ⊔ 8_11_t)` with α–t link coupling.
3. ⁵Li → Demazure sub-crystal of the A=5 sector (not a knot).

Each requires its own categorical derivation of the link
coupling — none should be census-fit.

If the owner instead wants a **placeholder volume guess** for
interim mass-table rows (clearly labelled `origin: "shape-probe,
not canonical"`), the SnapPy `OrientableCuspedCensus` should be
queried with `volume_in_range(low, high)` for the (ρ=2m_e)
windows (25.5–26.0, 31.0–31.5, 38.0–38.6). The (ρ=m_e) windows
are too large for the standard census and would require
satellite or augmented-link enumeration.

🔴 **Any such interim probe must NOT be promoted to a
production assignment** without independent categorical
backing — that would repeat the existing D/T/³He
census-assignment pattern explicitly flagged as CAL-4-equivalent
in `mass_table_ppb.py:18–21`.

## Confidence statement

Volumes for objects beyond the canonical anchors listed in
[`knot_volumes.py`](../../computations/substrate/knot_volumes.py)
are **not** recalled with sufficient precision (better than 0.5)
from memory. The "🟡 needs SnapPy census verification" markers
above are honest gaps, not placeholders. Any next step in this
direction should run an actual census query in a SnapPy-enabled
environment rather than rely on this scan.

## Cross-references

- Parent gap audit: [`2026-05-24-a5-a7-isotope-wiring-gap.md`](2026-05-24-a5-a7-isotope-wiring-gap.md)
- Grandparent anatomy: [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
- Canonical knot-volume registry: [`computations/substrate/knot_volumes.py`](../../computations/substrate/knot_volumes.py)
- Mass-table gap surface: [`computations/mass_table_ppb.py`](../../computations/mass_table_ppb.py) lines 80–180
- CLAUDE.md §7b — Demazure sub-crystals for resonances (the ⁵Li reading)
- CLAUDE.md production-vs-exploratory discipline — why this is a shape-probe
- PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3 — supplier for multi-knot VolDensity path
