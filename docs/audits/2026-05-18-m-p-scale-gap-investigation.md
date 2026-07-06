# m_p mass-prediction scale gap — 1700× residual investigation

**Date:** 2026-05-18
**Branch:** `claude/canonical-chi-rust` (PR #683)
**Status:** Open R&D — structural hypothesis surfaced; numerical verification deferred.

## The gap

| Quantity | Value | Source |
|----------|-------|--------|
| m_p (CODATA) | 938.27208816 MeV | `codata_constants.M_P_MEV_VALIDATION` |
| m_p (current categorical chain) | 0.597 MeV | `proton-mass-codata-50dps.witness.json` |
| Residual | 99.94% (~1572× factor) | |
| m_p / m_e (chain) | 1.169 | `derive_m_p_hecke_path_a` at q_0 |
| m_p / m_e (CODATA) | 1836.15 | |
| Scale factor needed | **1572** | 1836.15 / 1.169 |

The current categorical chain consumes only T1 + T4 from the
six-term formula — single-level Markov-trace × m_e plus the
Frobenius co-Casimir correction. Per `prop:categorical-mass-markov`:

> "single-level Markov trace does NOT produce mass ratios like
> m_μ/m_e ≈ 206.8; those require the full tower sum, which evaluates
> to Vol(K)/ℏ_q² in the archimedean realisation."

## Tower-formula sanity check (muon)

| Particle | Knot K | Vol(K) | Vol(K)/ℏ_q² | CODATA m/m_e |
|----------|--------|--------|--------------|--------------|
| Muon | 4_1 (figure-8) | 2.0299 | **206.77** | 206.768 ✓ |

The tower formula `m_lepton / m_e = Vol(K) / ℏ_q²` recovers
m_μ/m_e to better than 1 ppm.

## Proton-knot hypothesis

For m_p / m_e = 1836.15 the tower formula needs **Vol(K_p) = 18.026**.
Comparing to standard hyperbolic-knot volumes:

| Candidate knot complex | Vol | Vol/ℏ_q² | Residual to 1836.15 |
|------------------------|-----|----------|---------------------|
| 8 × Vol(4_1) | 16.239 | 1654 | -9.9% |
| **9 × Vol(4_1)** | **18.269** | **1861** | **+1.35%** |
| 10 × Vol(4_1) | 20.299 | 2068 | +12.6% |

**9 × Vol(4_1) ≈ 1.35% off** — suggestive but not exact.

### Why 9?

The proton has 3 quarks × 3 colors = 9 internal degrees of freedom
in the Hecke-algebra braid picture. Per the existing block
`q-integer-mass-formula.md`:

> "$[7]_q$: related to the proton's internal crossing count
> (7 crossings on generator 0: 3 B₃ + 1 uu + 2 gluon + 1 ud)."

The mid-strand crossing count is 7, but the TOTAL braid strand
count for a 3-quark proton at the H_9 level (3 nucleons-as-3-strands
times A=1 nucleon for ¹H, doesn't quite arithmetic out — but
the 9 = 3 × 3 (color × flavor) structure is documented).

### Refining the 1.35% residual

The residual of +1.35% suggests an O(h) correction (where h = q - q⁻¹ ≈ 0.21). Candidate forms:

- 9·Vol(4_1) · (1 - ξ) where ξ ≈ 0.0135
- A 9-component link with volume ≠ exactly 9·Vol(4_1) (additivity
  fails for hyperbolic volumes under connected sum without specific
  conditions; the Gromov norm IS additive but volume is not)
- Higher-order tower contribution adding a partial Vol

## Concrete next steps

1. **Identify the canonical proton knot complement K_p.**
   The 3-quark × 3-strand structure suggests a specific 9-component
   link. Inspect `prop:nuclear-knot-classification` for the
   classification table.

2. **Compute Vol(K_p) explicitly via SnapPy.**
   `computations` has snappy/snappea integrations
   (`engine='snappea'` per `witness_base.py`). A targeted compute
   on the canonical proton braid closure.

3. **Verify against m_p/m_e at 50 dps.**
   If Vol(K_p) / ℏ_q² matches CODATA m_p/m_e to better than 1 ppm
   (the muon's accuracy), the tower formula is structurally complete
   and m_p chain closes — the 1700× scale gap dissolves.

4. **Wire the tower formula into the m_p chain.**
   Currently `build_proton_mass_50dps_chain.py` consumes only the
   single-level Markov trace. The tower extension would prepend
   the `Vol(K_p) / ℏ_q²` factor (or equivalently, recognize the
   chain output as a ratio to m_e and multiply through).

## Why this matters for B.4 (¹H lift to `derived`)

The Item B audit identified five steps for closing the m_p chain
(`docs/audits/2026-05-18-m-p-item-b-t5-categorical-attribution.md`):

- B.1 (canonical a_K via closed-form C) — ✅ done this session
- B.2 (Items A+B+C audit closures) — ✅ done
- B.3 (¹H re-derivation at MPFR-50dps under canonical formula) — ❌ blocked
- B.4 (lift to `derived`) — ❌ blocked
- B.5 (narrative update) — ✅ done this session

B.3/B.4 are blocked by the 1700× scale-gap documented here. T5
chirality is structurally correct; the issue is upstream of T5 —
specifically, the TOWER SUM (multi-level mass-endomorphism)
isn't wired into the chain.

## Sibling-PR connection

PR #691 (`claude/post-682-followups-860f40`) extends the y_λ cache
to n=15, unblocking ⁵Li canonical |tr_M|. The y_λ extension is
INDEPENDENT of the tower-formula gap documented here — y_λ is the
Wedderburn-block weight at single level, while the tower sum is
the multi-level extension. Both threads need to land for full
m_p closure.

## §11 RESOLUTION (added 2026-05-18 after numerical verification)

**The scale gap is structurally explained by the Borromean baryon
mass formula** — already in the paper as
[`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md).
The naïve "9 × Vol(4_1)" hypothesis was WRONG. The correct
identification uses Vol(B_3) (Borromean rings) with a multiplicative
λ_scale, **not** a sum of figure-8 volumes.

Verification at MPFR 50 dps via
[`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py):

| Particle | Formula | Pred MeV | CODATA MeV | Residual |
|----------|---------|----------|------------|----------|
| Muon | m_e · Vol(4_1) / ℏ_q² | 105.65837565 | 105.65837550 | +0.001 ppm |
| Proton | m_e · [Vol(B_3)/ℏ_q² · λ_p_doc + S(p)≈0] | 938.27185264 | 938.27208816 | **−0.251 ppm** |
| Neutron | m_e · [Vol(B_3)/ℏ_q² · λ_n_doc + S(n)≈0] | 939.56518467 | 939.56542052 | **−0.251 ppm** |

The Borromean tower factor `Vol(B_3)/ℏ_q² · λ_scale ≈ 1836.15`
IS the missing 1700× multiplier from the single-level chain.

### Why this is NOT yet a closed prediction

The λ_scale values (λ_p = 2.4599527869, λ_n = 2.4633436333) were
SOLVED FROM CODATA per `borromean-baryon-mass-formula.md`
§"Empirical closure targets at q_0". Using them to "predict" m_p
is therefore circular at this stage.

**The open conjecture (Status #2 of the Borromean baryon formula):**
derive λ_scale from substrate via the Skein polynomial Q(q_0) of
B_3, the graded-Hecke-energy weight, or the canonical 11-crossing
Borromean braid. Closing that conjecture would make m_p a fully
derived quantity.

### Updated B.4 status

B.4 (lift ¹H to `derived`) is **conditionally unlocked**. The
Borromean tower formula gives 0.25 ppm under closure-target
λ_scale. Wiring this into `build_proton_mass_50dps_chain.py`
would drop `rel_diff` from 99.94% to 0.25 ppm — well below the
1% threshold. But the witness fails the "no fit-free derivation
chain" criterion: λ_scale was solved from CODATA. Until λ_scale
derives from substrate, ¹H legitimately remains `derivation_pending`.

### Concrete remaining R&D (for full m_p closure)

1. **Compute the Skein polynomial Q(q_0) of B_3** via the canonical
   11-crossing Borromean braid (per `prop:nuclear-knot-classification`
   and the GS-confinement filtration cohomology).
2. **Test whether Q(q_0) ≈ 2.46 = λ_scale** at the substrate point.
3. **Compute the graded-Hecke-energy weight** of B_3 at the canonical
   level — alternative candidate derivation for λ_scale.
4. **Once any of (1)-(3) closes**, wire the substrate-derived λ_scale
   into the m_p/m_n chains.

Both proton AND neutron use the SAME λ_scale (common-scale
hypothesis); their split comes from S(B) Skein differences,
covered separately by `prop:flavor-split-substrate`.
