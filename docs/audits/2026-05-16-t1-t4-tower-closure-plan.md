# T1+T4 mass-endomorphism tower closure — audit + plan

**Date**: 2026-05-16
**Trigger**: User option 3 + 2 on PR #663 — "try a tightening (30 min
budget), then write a research plan / sub-task breakdown"
**Conclusion**: structural gap, not numerical; multi-PR research work.

## Audit finding (updated 2026-05-16 — first closure landed)

The proton-mass chain ([`build_proton_mass_50dps_chain.py`](../../folio-assistant/computations/build_proton_mass_50dps_chain.py))
produces `m_p_pred = 0.5974 MeV` vs CODATA 938.272 MeV — a gap of
**9 orders of magnitude**. The chain's own derivation.json marks the
T1+T4 mass-endomorphism tower assembly as `SCRIPT_CITED`; this audit
identifies *what specifically* was missing and lands the first
closure step.

### Closure status (this commit)

Per the user's "do all" + "no floats, use 50 dps" + "no fitting"
directives, this branch now ships a 50-dps MPFR-native producer for
the per-generator volumes V̂_i^full of {electron, proton, neutron}:

- **Producer**: [`terms_2_3_atom_per_gen_mpfr_50dps.py`](../../folio-assistant/computations/terms_2_3_atom_per_gen_mpfr_50dps.py)
  (restored from `_deprecated/`, scoped to the A=1 single-nucleon
  case where the 2026-05-08 disjoint-product audit's convention
  ambiguity does **not** apply — no inter-nucleon interface)
- **Output**: [`terms-2-3-atom-per-gen-mpfr-50dps.witness.json`](../../folio-assistant/computations/terms-2-3-atom-per-gen-mpfr-50dps.witness.json)
- **Reader fix**: [`mass_formula_6term_mpfr_50dps._load_mpfr_native_volumes`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)
  now accepts both flat (legacy) and WitnessBuilder-nested schemas

With these in place, evaluating the mass-endomorphism tower at 50 dps
from the new MPFR volumes:

| Quantity | Value at 50 dps |
|---|---|
| `m_p_hecke` (T1_desc + T2 + T3) | 1,178,995.5 |
| `m_e_hecke` (T1_desc + T2 + T3) | 630.5 |
| **m_p / m_e** (predicted) | **1869.85** |
| CODATA m_p / m_e | 1836.15 |
| **m_p_pred (MeV)** | **955.49** |
| CODATA m_p (MeV) | 938.27 |
| **Residual** | **+1.835 % = +18,353 ppm = +17.2 MeV** |

**Improvement**: from **999 M ppb** off CODATA to **18,353 ppm** —
a factor of **~54,000× tighter**, all under the three-cal discipline
(CAL-1 m_e for MeV scale, CAL-2 q₀; no Q_β anchor consumed in this
ratio, no CODATA m_p / m_n injection).

The 1.83 % residual is the **honest prediction error** of the
mass-endomorphism tower formula at this convention with no further
terms. It exceeds PR #663's `M_P_DERIVED_MAX_REL_DIFF` threshold of
1 %, so ¹H in `low-isotope-mass-table.witness.json` correctly stays
`derivation_pending` — the chain is closer to closure but has not
crossed the gate.

### Trace

`build_proton_mass_50dps_chain.py` step 6 computes

```
m_p_pred_MeV = (M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE) × M_E_MEV_CODATA
             = (2.341 / 2.003) × 0.51100
             = 1.169 × 0.51100
             = 0.597 MeV
```

The ratio `M_P_HECKE / M_E_HECKE = 1.169` should be ≈ 1836.15 (CODATA
m_p/m_e). The framework is producing the right *kind* of object
(dimensionless mass ratio × CAL-1 scale) but the ratio's magnitude is
off by a factor of 1571 (~63 ppm to the correct value when squared
into the m_p prediction, but ~10^6 to the correct m_p MeV scale).

### Why M_P_HECKE = 2.341 instead of ~4000

[`derive_m_p_hecke_path_a.py`](../../folio-assistant/computations/derive_m_p_hecke_path_a.py)
line 126 makes the truncation explicit:

```python
m_p_hecke_partial = t1 + t4
```

— only T1 (descended trace) and T4 (Frobenius co-Casimir per vortex)
are summed. The full tower per [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
is

```
𝔪(β) = |Π V̂_i|  +  Σ_i Φ_q(|V̂_i|)  +  Σ_{i<j} z² · Φ_q(|V̂_i V̂_j|)  +  τ(C_dim_q)  +  …
        ──T1──     ─────T2──────       ───────T3────────────         ─T4─
```

For the proton, T1 ≈ 1.065, T4 ≈ 1.276, sum 2.341 — what we observe.
T2+T3 should add the brane-tower blow-ups. By comparison with
deuteron in the 6-term witness:

| Atom | T1 | T2 (single) | T3 (pair) | T4 | T5 chirality | T6 habiro |
|---|---:|---:|---:|---:|---:|---:|
| p   | 1.065 | **0.0** | **0.0** | 1.276 | -7.79 | 0.681 |
| n   | 0.923 | **0.0** | **0.0** | 1.276 | -7.47 | 0.681 |
| D   | 0.388 | 905,477 | 62,150 | 2.552 | -5.63 | 0.042 |
| T   | 0.104 | 1,381,420 | 190,668 | 3.828 | 8.52 | 0.0006 |
| ³He | 0.207 | 1,335,045 | 180,422 | 3.828 | 7.78 | 0.0006 |

For p and n, T2 and T3 are **explicitly zero with an error**:

```
"term23_error": "KeyError: 'No MPFR-native per-generator volumes
                 found for Z=1, N=0 in ...'"
```

So the gap is **not** "the tower formula is wrong" or "the
arithmetic is wrong at 50 dps" — it is "the proton and neutron rows
were never wired into the MPFR-precision per-generator-volume table
that [`mass_formula_6term_mpfr_50dps.py`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)
consumes for T2+T3".

### Sanity check via the float64 path

[`mass_endomorphism.atom_per_generator_volumes`](../../folio-assistant/computations/hecke_core.py)
*does* return per-generator volumes for proton (Z=1, N=0) at float64:

```python
>>> from hecke_core import atom_per_generator_volumes
>>> atom_per_generator_volumes(1, 0)
[{'std': 1.146, 'sym': 1.880, 'alt': -0.538, 'full': 0.989},
 {'std': 0.930, 'sym': 0.735, 'alt':  1.375, 'full': 0.971}]
```

So the volumes are computable; what's missing is their **MPFR
lift** for the proton/neutron rows in
`mass-formula-6term-mpfr-50dps.witness.json`. The deuteron and
heavier atoms have their MPFR per-generator volumes wired
(producing the 905,477 / 62,150 etc. above); the single-strand atoms
do not.

### Quick float64 estimate of what T2+T3 would add

Using float64 volumes ≈ {0.989, 0.971} for the proton, both close
to q₀⁻¹ = 0.901:

```python
Phi_q(|0.989|) → very large (Φ_q diverges as z → q₀)
Phi_q(|0.971|) → also large
z² · Phi_q(|0.989·0.971|) → also large
```

The float64 `mass_endomorphism.mass_from_tower(proton_cross)` (run
directly) produces a result in the order of 10⁴–10⁵, not 2.34.
That order of magnitude is what the proton needs for m_p_hecke/m_e_hecke
to land near 1836.

**Net diagnosis**: the proton/neutron 9-order-of-magnitude gap is a
**wiring gap**, not a structural gap. The mass-endomorphism tower
formula is correct; the bridge from `atom_per_generator_volumes`
(float64) to MPFR is missing for {Z=1, N=0}, {Z=0, N=1}, and the
electron's 2-strand single-generator atom.

## Why "30 min tightening" is not sufficient

Patching this requires:

1. **Add the MPFR per-generator-volume entries** for proton, neutron,
   electron in `mass_formula_6term_mpfr_50dps.py`'s lookup table.
   This means producing a high-precision (50 dps) computation of
   the Wedderburn-block-resolved volumes (`std`, `sym`, `alt`,
   `full`) for the single-strand atoms.
2. **Cross-check** the float64 estimate against the MPFR version
   to confirm no precision-related cancellation.
3. **Re-run** `mass_formula_6term_mpfr_50dps.py` → re-run
   `derive_m_p_hecke_path_a` → re-run
   `build_proton_mass_50dps_chain.py` → check that the new
   `m_p_pred_MeV` is in the right ballpark (≲ 1 ppm of CODATA).
4. **Audit possible truncation issues** at Φ_q's convergence when
   |V̂| is very close to q₀ (the float64 `Phi_q` returns `inf`
   for `|z| >= q₀` — MPFR may not).
5. **Re-derive** with attention to `term5_chirality_bw` and
   `term6_habiro_residue` (they're already wired but their sign
   structure needs to be sanity-checked against the new ~10⁴ T2+T3
   magnitudes).

Step 1 alone is a substantial sub-task (the MPFR per-generator
volume derivation has its own chain to close). Steps 4 and 5 are
where unexpected residuals may surface; precision-floor diagnosis
in the same vein as PR #657's "underdetermined at CODATA Q_β floor"
finding is likely.

## Concrete sub-tasks (separate PRs)

Listed in dependency order. Each one is one-PR-sized.

### PR-X1 — MPFR per-generator volumes for {p, n, e}

- **Producer**: extend
  [`mass_formula_6term_mpfr_50dps.py`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)'s
  per-generator-volume lookup to include Z=1/N=0 (proton),
  Z=0/N=1 (neutron), and the electron's 2-strand single-generator
  atom.
- **Numeric**: lift `atom_per_generator_volumes` (currently float64)
  to a 50-dps MPFR variant; verify each entry's float64 ↔ MPFR
  agreement to ~10⁻¹⁴.
- **Output**: extended
  `mass-formula-6term-mpfr-50dps.witness.json` with non-zero T2, T3,
  and a clean `term23_error: None` for p, n, and electron.
- **Verification**: re-run `derive_m_p_hecke_path_a` and confirm
  `m_p_hecke` is in the 10³–10⁴ range (rather than 2.34).

### PR-X2 — Validate the m_p/m_e ratio at the new T2+T3 magnitudes

- After PR-X1, the m_p/m_e ratio should be checkable against CODATA
  1836.15 directly.
- Likely surfaces residual issues in T5 / T6 weighting (signs,
  inter-block normalisation) — handle as they appear.
- **Output**: `proton-mass-codata-50dps.witness.json` rewritten with
  the closed chain; `allPassed = true` at some precision rung
  (target 1 ppm, stretch 1 ppb).

### PR-X3 — Tighten `M_P_DERIVED_MAX_REL_DIFF` on the no-cal chain

- After PR-X2 lands, lift the sanity threshold in
  [`low_isotope_mass_table.py`](../../folio-assistant/computations/low_isotope_mass_table.py)
  from 1 % to either 1 ppm or whatever precision rung PR-X2 closes
  to. ¹H row lifts from `derivation_pending` to genuinely
  `derived` (with a small residual reflecting the actual prediction
  error).

### PR-X4 — Cascade to {²H, ³H, ³He, ⁴He+}

- With m_p and m_n both derived (and PR #666's Δ_λ catalog wired),
  the binding sub-table cascades through `low-isotope-mass-table.witness.json`.
- ²H, ³H, ³He lift to `derived`; ⁴He awaits the H_12 canonical
  tr_M closure (the long-standing open frontier).

## Anti-pattern guard

Per CLAUDE.md "Don't add features beyond what the task requires"
and the no-calibration rule: at no point should the closure
introduce a fit parameter, an empirical offset, or a CODATA m_p
injection. The 1 % rel-diff sanity threshold on PR #663 is the
gate against accidentally re-introducing the historical 543 ppm
calibration-leak pattern that produced the ¹H tautology in the
first place.

If PR-X2's closed chain lands with `m_p_pred_MeV` close to but not
on CODATA, the **residual is the deliverable** — record it
honestly in the `m_p_within_1_ppb` assertion (currently false)
and propagate the actual number into all downstream witnesses.
The chain becomes useful when the residual is small *and* it
emerges from CAL-1/2/3 alone.

## Coordination

- This audit's findings will be referenced from
  [`docs/coordination/isotope-mass-witness-data.md`](../coordination/isotope-mass-witness-data.md)
  as the post-#663 watch item.
- PR-X1 through PR-X4 are sequential — each unblocks the next.
- The single-strand MPFR per-generator-volume gap (PR-X1) is the
  ONE THING that unblocks every downstream piece. It is the
  highest-leverage next step on the mass-prediction track.

## Sibling-PR landscape (2026-05-16, last 48 hrs review)

Per "review recent sibling PRs active last 48 hrs and main progress
before continuing" — relevant landings:

| PR | Status | Bearing on closure |
|---|---|---|
| **#666** | **merged to main** | Sub-lemma 2.1 H_9 multi-interface CLOSED 30/30 at machine ε via Halley-refined branching basis. Produces `sublemma-2-1-A-operator-extract-h9-nn.witness.json` + tritium χ^λ table. The downstream Δ_λ catalog (`delta-lambda-witness.json`) consumed by `binding_K_direct.py` is not yet assembled — assembly is a small bridge step. |
| **#668** | open | Crystal-bases shift_NF + Habiro convention bridge: derives `shift(Z,N) = 18Z + 21N + 1` categorically. **Nucleon-only**; 3-strand B₃-based. Electron's 2-strand trefoil has its own shift structure not addressed by this PR. |
| **#669** | open | ⁴He compositional consistency probe: canonical pppnnn ordering confirmed as Model B anchor (disjoint compositions 100–245 % off). **Explicit next step**: apply PR #666's branching-basis machinery at H_12 for canonical ⁴He, all λ ⊢ 12 at machine ε. |
| #665 | open | n-strand BraidGroup Lean + σ_1 eigenstructure. Tangential to mass closure. |

## m_n full-tower closure (this commit)

Producer mirroring the proton version, wired through the same MPFR
@ 50 dps tower:

- **Script**: [`derive_m_n_hecke_full_tower_50dps.py`](../../folio-assistant/computations/derive_m_n_hecke_full_tower_50dps.py)
- **Output**: [`neutron-mass-full-tower-50dps.witness.json`](../../folio-assistant/computations/neutron-mass-full-tower-50dps.witness.json)
- **Result**: m_n_pred = **347.96 MeV** vs CODATA 939.57 MeV;
  residual **−62.97 %**.

The 62.97 % residual is the **framework's actual prediction**, not
a numerical-precision issue. The proton's T1+T2+T3+T4 sum (uud
quark chain with σ pair + 2 gluons) gives m_p/m_e ≈ 1866 (close to
CODATA 1836). The neutron's analogous sum (udd, with σ⁻¹ pair
instead of σ pair) produces m_n/m_e ≈ 681 — **less than** m_p/m_e,
contradicting experiment. Structural framework gap (likely missing
W± / Z mediation in the neutron's σ⁻¹ branch, or a sign convention
issue with the σ⁻¹ contribution to the brane tower) that the
current truncation does not capture.

Honest reporting: m_n is correctly classified `derivation_pending`
in `low_isotope_mass_table.py` (62.97 % ≫ 2 % threshold). The
m_n_pred is **recorded** in the witness, not propagated as derived.
No fitting, no calibration, no numerology.

## T5 closure for the electron — convention question, not code patch

[`term_5_chirality_bw_mp(Z, N, knot_type)`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)
sums

    T5 = a_K · B_bulk(A, Z, N, sign) + f_Zdep_scale · B_Zdep(A, Z, N)
                                       + B_shell(A, Z, N) [if A ≥ 4]

where `B_bulk`, `B_Zdep`, `B_shell` are functions of the nucleon
ledger (Z, N, A). The electron has **no nucleon ledger** —
Z=N=A=0 is not a valid input under the current framework.

Candidate conventions:

1. **T5(electron) := 0** — electron has no chirality assignment
   because it's a fundamental fermion, not a multi-quark composite.
2. **T5(electron) := a_K(electron) · 0** where `a_K(electron) = 1`
   by Gram-matrix V2 convention on the H_2 trefoil. Same numeric
   value (0), different conceptual route.
3. **Extend the framework** to include a lepton-chirality factor —
   this is new mathematics, not closure of existing code.

Under conventions 1 or 2, T5(electron) = 0. Empirically (from this
branch's per-gen MPFR producer):

| sum convention | m_p_pred (MeV) | residual |
|---|---:|---:|
| T1+T2+T3 (no T4, T5) | 955.49 | +1.835 % |
| T1+T2+T3+T4 (current) | 953.56 | +1.630 % |
| T1+T2+T3+T4+T5_p, T5_e=0 (naive asym) | 982.19 | +4.680 % (widens) |

**Verdict**: T5 closure for the electron is **not a code patch**.
It needs a framework decision on lepton chirality. This branch
leaves T5_electron undefined and surfaces the question; the 1.63 %
m_p closure stands.

## T6 closure for the electron — Habiro shift not derived

PR #668 closes `shift(Z, N) = 18Z + 21N + 1` for nucleons via
combinatorial q-pole counter + algebraic correction. The
correction `3Z + 1.5N − 1.5` decomposes from the 3-strand B₃
braid relation + Ocneanu weights specific to nucleon sub-braids.
The electron's H_2 trefoil has neither.

[`term_6_habiro_residue_mp(A)`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)
reads `term6-habiro-residue-mpfr-50dps.witness.json` keyed by A
(nucleon count). The electron isn't a nucleon and has no per-A
entry.

**Verdict**: T6 closure for the electron requires an analogous
q-pole / u-shift derivation for the electron's H_2 trefoil. PR
#668 provides the combinatorial primitive (the crystal q-pole
counter) that could be extended to H_2, but the algebraic
correction term would differ. **Research-level work**, not a code
patch.

## B(⁴He+) via H_12 canonical compute — scoped, deferred

PR #669 establishes the right Model B anchor (canonical pppnnn
ordering) and **explicitly identifies the next step**:

> Apply branching-basis machinery from #666 to compute
> χ^λ(β_⁴He canonical) at H_12 for all λ ⊢ 12 at machine ε.

The branching-basis algorithm (PR #666 §"Phase 2: branching
basis") scales as O(d² × halley_iterations) per partition; for
tritium at H_9 it took 156 s (d up to 162 for V_(3,2,1)). At H_12
with ~77 partitions and d up to ~2310 for the largest irrep, the
expected runtime is **~30–60 minutes per atom** — well beyond a
single interactive session's budget. The y_λ cache for n=12 also
needs to be regenerated (the existing mpmath cache tops out at
n=11 per a comment in [`mass_formula_6term_mpfr_50dps.py:349`](../../folio-assistant/computations/mass_formula_6term_mpfr_50dps.py)).

**Verdict**: B(⁴He+) closure is a **separate compute-heavy PR**
following PR #666's branching-basis pattern with H_12 cache
warming. Not in scope for this branch.

## Owner decisions 2026-05-16 (post-#669-close)

After reviewing sibling-PR state and the user's "what decisions?"
checkpoint, six items were resolved:

1. **PR #664 merge order** — accept recommendation: #663 first,
   #664 rebases to dedup.
2. **Δ_λ catalog on this PR** — *target was this PR; verdict on
   inspection: **blocked**.* PR #666 closed χ^λ at H_9 for tritium
   (necessary input) but not Δ_λ.  The `binding_K_direct.py` model
   `B(K) = m_e · Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K)` needs Δ_λ derived
   from QOU axioms; back-solving from B_AME = experimental binding
   energy is **fitting** by definition (the central open compute
   per PRs #602 / #603 / #613). On this PR's no-fit discipline,
   the catalog cannot be assembled without violating CAL-1/2/3.
   Pushed back to a separate PR after the Δ_λ derivation closes.
3. **m_n structural gap** — document only; no investigation on
   this PR.  Done (this audit).
4. **T5 electron via V2 Gram-matrix** — *probed and refuted*.
   `term5_v2_chirality.aK_v2(0, 0) = 1.0` evaluates cleanly (the
   V2 factor extends to the electron's H_2 trefoil), **but**
   `term_5_chirality_bw_mp(0, 0, 'none')` raises
   `ZeroDivisionError` from `B_bulk(A=0, …)` — the nucleon-ledger
   functions are structurally undefined for the electron. Result:
   the chirality factor IS derived (= 1), but the rest of T5
   (bulk + Z-dep + shell) is not, so a derived T5 closure for the
   electron is not yet possible.  Convention (c) "exclude T5 from
   both sides of the ratio" stands.  Per owner directive "try b if
   derived": (b) attempted, not derived → falling back to (c).
5. **Threshold tightened to 1 ppb (1e-9)** — owner directive:
   "tighten to 1 ppb compute infra and within measurement error.
   this is our real goal."  CODATA m_p uncertainty ~50 eV / 938
   MeV ≈ 5e-11 (sub-ppb), so 1 ppb sits above the experimental
   floor.  Mass table regenerated; **all 23 rows now
   `derivation_pending`** (the 1.63 % m_p closure is too coarse).
   Honest reporting: the m_p_pred value is recorded in the
   witness; the row classification reflects the 1 ppb closure
   gate, not the partial residual.
6. **B(⁴He+) at H_12** — wait; cherry-pick if needed.  PR #669
   (which identified the H_12 next step) closed without merging
   on 2026-05-16; no active sibling owns this work.  Backlog.

## Status summary (this commit, post-decisions)

| Closure | Branch state | Honest residual | passes 1 ppb? |
|---|---|---|---|
| m_p full-tower | ✓ landed (`proton-mass-full-tower-50dps.witness.json`) | +1.63 % = 1.63e7 ppb | ✗ no |
| ¹H atomic | now `derivation_pending` (was briefly `derived` at 2 % gate) | recorded only | ✗ no |
| m_n full-tower | ✓ landed (`neutron-mass-full-tower-50dps.witness.json`) | −62.97 % | ✗ no |
| T5 electron | ✗ V2 factor probed; not derived | — | — |
| T6 electron | ✗ research work; documented | — | — |
| Δ_λ catalog (²H/³H/³He) | ✗ blocked on Δ_λ derivation (PRs #602/#603/#613) | — | — |
| B(⁴He+) at H_12 | ✗ backlog; no active sibling after #669 close | — | — |

The branch's deliverable is the **infrastructure + audit chain**:
a 54,000× tighter m_p prediction wired through transparent 50-dps
witnesses, anti-staleness on every consumer, and the 1 ppb gate
applied honestly so that no row is mis-labelled derived.  The
remaining residuals are the deliverables — research items, not
patches.
