# Rule 14 escalation — Kashaev density rule `ρ_F ∈ {m_e, 2m_e}`

**Date:** 2026-05-24
**Branch:** `claude/post-1089-followups-2026-05-24` → PR [#1111](https://github.com/litlfred/qou/pull/1111)
**Status:** ✅ **RESOLVED 2026-05-24** — owner authorised the conjecture-conditional adoption. New content block authored: [`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/braids-and-knots/kashaev-density-equals-sdp-multiplicity.md). Compute field `rho_factor` renamed to `nu_sdp` in `mass_table_ppb.py`. R&D follow-up to confirm $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$ via R5-full SDP solver still open.

## Statement of the rule under escalation

The script
[`computations/mass_table_ppb.py`](../../computations/mass_table_ppb.py)
adopts in production the **Kashaev binding-energy formula**

```
B_pred(K)  =  ρ_F · m_e · Vol_hyp(K)            (mass_table_ppb.py:10, 165)
```

with the **density rule** `ρ_F ∈ {1, 2}` (in units of `m_e`).
The script's docstring at `mass_table_ppb.py:23-24` explicitly
self-declares this as

> "Truly derived pieces: (1) the density rule `ρ_F ∈ {m_e, 2m_e}` —
> **pending formal justification**".

The current assignment table at `mass_table_ppb.py:86-132` is:

| Atom | Knot | `ρ_F` | Origin tag |
|------|------|-------|------------|
| ²H (D) | `6_2` | **1** | `hyp: census-assigned` |
| ³H (T) | `8_11` | **2** | `hyp: census-assigned` |
| ³He | `L6a4` (Borromean) | **2** | `hyp: census-assigned` |
| ⁴He | `4·Borromean` (magic) | **2** | `framework: A·8G magic rule` |
| α-cluster atoms (≥⁸Be) | recursion on ⁴He + `c_αα` | **2** (inherited) | `framework: α-cluster` |

The Kashaev volume formula itself (the right-hand `m_e · Vol_hyp(K)`
factor) is canonical — derived as the `τ_arch` realisation of the
algebraic quantum volume, per
[`rem:kashaev-as-archimedean-realization`](../../content/quantum-observable-universe/braids-and-knots/kashaev-as-archimedean-realization.md)
and the open conjecture
[`conj:kashaev-volume-conjecture`](../../content/quantum-observable-universe/braids-and-knots/kashaev-volume-conjecture.md).
What is **NOT** canonical is the multiplicative `ρ_F ∈ {1, 2}`
prefactor — it does not appear in either content block. It is
introduced solely in the compute script (`mass_table_ppb.py:10, 23-26,
87-95, 165, 176, 187`), with no narrative or Lean block deriving it.

## Why this is a Rule-14 escalation

Per
[`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](2026-05-23-lambda-scale-canonical-unification.md)
§Rule 14, any production coefficient that cannot be derived from one
of the 13 categorical drivers (i)-(xiii) requires explicit owner
authorisation before remaining in a production-mass-chain script.
`mass_table_ppb.py` is the AME-comparison production driver
(`mass_table_ppb.py:1-4, 219-282`); the `ρ_F` factor multiplies every
predicted binding energy. It is therefore in scope.

## Walk through the 13 categorical drivers

Candidate substrate-derived readings of `ρ_F ∈ {1, 2}`, against each
driver from the canonical-menu doc:

- **(i) Faddeev recursion / (ii) Φ_q power series / (iii) Rogers
  pentagon / (iv) Yang-Baxter / (v) hexagon / (vi) Frobenius
  reciprocity / (xi) Lobachevsky / Cl_2 / Catalan-G.** All produce
  q-deformed continuous prefactors; none naturally produce the
  **integer doubling** `{1, 2}`. Negative.
- **(vii) Quantum 6j-symbols (Racah-Wigner).** Quantum 6j matrix
  elements have integer multiplicities controlled by the
  decomposition `V_a ⊗ V_b = ⊕_c V_c`. Doubling `{1, 2}` is
  consistent with the multiplicity of the spin-½ summand in
  `V_½ ⊗ V_½ = V_0 ⊕ V_1`, but **needs a definite map** from atom-
  knot data to a 6j cell. **Plausible, not yet derived.** Needs read
  of any `prop:quantum-6j*` block.
- **(viii) Modular S-transform.** S = symmetry of the partition
  function under `q ↔ q̃`. No integer-doubling content for a knot
  prefactor. Negative.
- **(ix) KLR positivity.** KLR canonical-basis coefficients are
  non-negative integers; `{1, 2}` could in principle be canonical-
  basis multiplicities. **Hint**, but no concrete map at present.
- **(x) MacMahon-style partition-algebra identities.** Per
  [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
  §Algorithm step 3, the **SDP multiplicity** `ν_SDP ∈ ℤ_{>0}` is
  the multiplicity of `T_w`'s SDP solution in the Wedderburn
  decomposition. The audited values are `ν_SDP,D = 1`,
  `ν_SDP,T = 2`, `ν_SDP,³He = 2` (`atom-knot-mass-derivation.md`
  line 265). **These exactly match the `ρ_F` assignments** in
  `mass_table_ppb.py:87, 89, 91`. This is the **strongest single
  hint** — `ρ_F` may literally be `ν_SDP`, the Wedderburn
  multiplicity of the canonical Hecke element. See §Strongest
  hypothesis below.
- **(xii) Chern-Simons perturbative (Ohtsuki).** The WRT TQFT
  density of states scales with level `k`; for a fixed `k` an
  individual knot's contribution carries no integer doubling beyond
  multiplicity counts already captured by (vii) and (x). Negative
  for `{1, 2}` specifically.
- **(xiii) Crystal-graph (Kashiwara q→0).** Crystal multiplicities
  are non-negative integers; `{1, 2}` is admissible as a crystal-
  basis count, but **no concrete crystal-graph reading** of the
  atom-to-knot map is on file.

**Net:** no driver currently *derives* `ρ_F`; driver (x) provides
the strongest hint (numerical agreement with `ν_SDP`), with (vii)
and (ix) consistent but unmapped.

## Strongest hypothesis: `ρ_F = ν_SDP`

The numerical coincidence is exact on the three census-assigned
hyperbolic atoms:

| Atom | `ρ_F` (mass_table_ppb.py:87-91) | `ν_SDP` (atom-knot-mass-derivation.md:265) |
|------|------|------|
| D | 1 | 1 |
| T | 2 | 2 |
| ³He | 2 | 2 |

If `ρ_F = ν_SDP`, then the Kashaev formula in `mass_table_ppb.py`
is the **post-Archimedean instance** of the QOU multi-term mass
identity collapsed onto its `|tr_M(T_w)|` term, with
`|tr_M(T_w)|_{q_0}` replaced by `m_e · Vol_hyp(K)` under the volume
conjecture (per
[`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
§Post-Archimedean interpretation, lines 204-216, 298-307). That
is structurally consistent with the QOU pipeline and would land
`ρ_F` squarely under driver (x).

**Caveats** (be honest — these are guesses):

- ⁴He uses `ρ_F = 2` under the **magic A·8G rule**
  (`mass_table_ppb.py:94`), not census. The structural prefactor
  rule for ⁴He's `ν_SDP` is not yet derived
  (`atom-knot-mass-derivation.md:260-272` notes `ν_SDP` is *open
  in general*). The `ρ_F = ν_SDP` reading therefore extrapolates
  beyond the three confirmed values. **Needs read of**
  `r5_full_canonical_knot_solver.py` and the
  `joint-tower-sdp-certificate` witnesses to confirm whether ⁴He's
  Wedderburn multiplicity is genuinely 2.
- The agent-suggested alternative readings ("number of spinor
  degrees of freedom per cusp" or "links-per-component" or
  "highest-weight Wedderburn block degeneracy") are also consistent
  with `{1, 2}` on three data points but lack a candidate driver in
  the 13-source menu. They look like reverse-engineered just-so
  stories without the SDP-multiplicity bridge.

## Empirical pattern check (be careful — three data points)

| Atom | Strands `n_0` | # components of K | # cusps | spin (atom) | `ρ_F` |
|------|---------------|------|------|--------|-------|
| D | 2 | 1 (knot `6_2`) | 1 | 1 | 1 |
| T | 3 | 1 (knot `8_11`) | 1 | ½ | 2 |
| ³He | 3 | 3 (link `L6a4`) | 3 | ½ | 2 |
| ⁴He | 4 | 12 (4·Borromean → 12 cusps) | 12 | 0 | 2 |

- **"Spin doubling"** (`ρ_F = 2·spin + 1`?): D has spin 1 → would
  give `ρ_F = 3` (wrong, observed 1); T has spin ½ → `ρ_F = 2` ✓;
  ³He spin ½ → `ρ_F = 2` ✓; ⁴He spin 0 → `ρ_F = 1` (wrong,
  observed 2). **Negative.**
- **"Components-per-knot"** (`ρ_F = #components`?): D 1 ✓, T 1
  (wrong, observed 2). **Negative.**
- **"Cusps per knot"**: D 1 ✓, T 1 (wrong), ⁴He 12 (wrong).
  **Negative.**
- **"Fermion / boson"**: D is boson, T+³He+⁴He are fermion (or
  spin-0 even-A). Not a clean `{1, 2}` partition either —
  boson ⁴He gets `ρ_F = 2`.
- **`ν_SDP` (Wedderburn multiplicity)**: D 1, T 2, ³He 2 ✓✓✓;
  ⁴He extrapolated, unverified. **Best fit.**

The structural reading "`ρ_F` = number of saturating Wedderburn
blocks under the joint-tower SDP" cleanly explains why D's simpler
Hecke element saturates only one block while T/³He saturate two,
and is the only reading on the 13-driver menu. The `spin` and
`cusp` ansätze fail.

## Recommendation

**(a) Escalate as conjecture-conditional (Rule 14) with the
`ρ_F = ν_SDP` interpretation.** Specifically:

1. **Author a `prop:` block** named
   `prop:kashaev-density-equals-sdp-multiplicity` in
   `content/quantum-observable-universe/braids-and-knots/`, stating
   the identity `ρ_F = ν_SDP` and citing
   [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
   §Algorithm step 3 as the categorical mechanism (driver (x)
   MacMahon-partition-algebra multiplicity).
2. **Conjecture-conditional Lean class** axiomatising
   `KashaevDensityIsSDPMultiplicity` per `AGENTS.md` §3b. The
   conjecture is open until R5-full lands per
   [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
   §"Where the gaps actually are".
3. **Update `mass_table_ppb.py:23-26`** to cite the new `prop:`
   block instead of the bare "pending formal justification"
   admission. The `rho_factor` field in `ATOM_ASSIGN`
   (`mass_table_ppb.py:87-95`) should be renamed `nu_sdp` for
   notational consistency with the QOU pipeline.
4. **R&D follow-up**: extend the joint-tower SDP solver to
   produce `ν_SDP` for ⁴He, ⁶Li, ⁷Li, α-cluster atoms; verify the
   `ν_SDP = 2` extrapolation to ⁴He and document `ν_SDP` for the
   A-gap isotopes per
   [`docs/audits/2026-05-24-a5-a7-isotope-wiring-gap.md`](2026-05-24-a5-a7-isotope-wiring-gap.md).
5. **Cross-link with the atom-knot-census Rule-14 doc**
   ([`docs/audits/2026-05-24-rule14-atom-knot-census.md`](2026-05-24-rule14-atom-knot-census.md)) —
   the `ρ_F` derivation and the atom-to-knot assignment are the
   two halves of the same canonical-derivation gap.

This is the cheapest path that brings `ρ_F` onto the 13-driver
menu (under (x)) and replaces the bare "pending formal
justification" string with an auditable conjecture-conditional
class.

## Cross-references

- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](2026-05-23-lambda-scale-canonical-unification.md)
  §13-driver menu + Rule 14
- [`docs/audits/2026-05-24-rule14-atom-knot-census.md`](2026-05-24-rule14-atom-knot-census.md)
  (sibling) — atom→knot assignment census escalation
- [`computations/mass_table_ppb.py`](../../computations/mass_table_ppb.py)
  — production script under escalation
- [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
  §Algorithm step 3 — `ν_SDP` definition
- [`kashaev-volume-conjecture.md`](../../content/quantum-observable-universe/braids-and-knots/kashaev-volume-conjecture.md)
  — KVC class axiomatisation precedent (re-use pattern)
- [`kashaev-volume-density.md`](../../content/quantum-observable-universe/braids-and-knots/kashaev-volume-density.md)
  — `m = Vol · ρ_q` substrate density (note: this is a DIFFERENT
  ρ — substrate quantum-Planck `ρ_q = 1/ħ_q²` — not the
  Kashaev-formula prefactor `ρ_F`; the symbol collision is a
  notation hazard flagged here)
- [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
  §Notation (lines 1-13) — `ρ` already disambiguated into
  `ν_SDP` (integer Wedderburn multiplicity) vs `ρ_K` (CODATA-fit
  density); `ρ_F` is currently a **third** unnamed ρ in compute
  scripts only. The rename to `ν_SDP` in §Recommendation step 3
  also resolves this notation drift.
