# Mirror-pair Coulomb sign-correction — general result + EM-linking invariant verdict

**Date:** 2026-06-19
**Branch:** `claude/he3-mirror-coulomb-sign-correction-2026-06-19`
**PR:** #2487
**Resolves:** the "open question for the branch" of the A=3 diagnosis
[`2026-06-18-he3-brane-tower-structural-gap.md`](2026-06-18-he3-brane-tower-structural-gap.md)
§"Where the fix must live" (lines 77–82).

## Summary (two sentences)

The per-generator brane-tower's **inverted Z-ordering** bug is closed
**generally** (all mirror pairs, no per-atom retuning) by a fit-free correction:
composite pair-knot replacement + an explicit `Z(Z−1)/2` Coulomb term built from
the *derived* per-pair reduction. The residual **magnitude** is the known-open,
forbidden-to-fit "EM-linking invariant"; a formalize-first attempt **prunes** the
simplest hypothesis class for it (a single q₀-constant) and scopes it to a
genuine A-dependent object — it does **not** close it.

## 1. General sign-correction (closed, fit-free)

Probe [`computations/probes/mirror_pair_coulomb_sign_correction.py`]
(witness `mirror-pair-coulomb-sign-correction.witness.json`, mpmath 50 dps).

Two structurally-motivated changes to the tower's operator content:

- **(a) Composite pair-knot replacement** removes the spurious additive
  per-generator over-count of the doubled proton near-pole pair
  (`E₀·Δtower ≈ 1.165 MeV`, **wrong sign** — it favoured ³He), restoring the
  exact Z↔N Markov-trace isospin symmetry `tr_M(σ_pp) = tr_M(σ_nn)`.
- **(b) Explicit `Z(Z−1)/2` Coulomb term.** Each of the `C(Z,2) = Z(Z−1)/2`
  proton pairs contributes the **derived** per-pair Coulomb reduction
  `ratio·B_pp` (`def:coulomb-charge`, `Q_pp=+1`,
  `ratio = tanh(ln q₀) = (q₀²−1)/(q₀²+1)` Lean-proved). The `Z(Z−1)/2` count is
  **pure combinatorics — no fit**; the per-pair magnitude is **cited** from the
  canonical `charge-coulomb-tn3he-derived.witness.json`.

The proton-richer member always carries more pairs ⇒ larger Coulomb reduction ⇒
less binding — the **correct ordering for every pair**:

| A | pair (poor / rich) | Δpairs | ΔCoulomb (MeV) | AME split (MeV) | covered | sign |
|---|---|---|---|---|---|---|
| 3 | ³H / ³He | 1 | 0.2377 | 0.7638 | 31.1% | ✓ |
| 7 | ⁷Li / ⁷Be | 3 | 0.7130 | 1.6441 | 43.4% | ✓ |
| 11 | ¹¹B / ¹¹C | 5 | 1.1884 | 2.7652 | 43.0% | ✓ |
| 13 | ¹³C / ¹³N | 6 | 1.4260 | 3.0028 | 47.5% | ✓ |

**Sign closed** (derived per-pair unit × combinatorial count, zero fit).
A=3 is fully within-model; A>3 use the A=3 H_6 diproton bond as a uniform
per-pair unit, so those rows are **right-sign predictions** (the per-pair bond's
A-dependence is the confound — see §2). **Magnitude open** (31–47%).

## 2. EM-linking invariant — formalize-first scoping (open, pruned)

Probe [`computations/probes/em_linking_invariant_scoping.py`]
(witness `em-linking-invariant-scoping.witness.json`).

Per the formalize-first discipline (narrow before searching), state the simplest
hypothesis class and find the structural constraint that prunes it:

> **H0:** the EM-linking invariant is a single q₀-derived constant `κ` with true
> per-pair Coulomb `= κ · (ratio·B_pp)` ⇒ the residual factor
> `κ = need_per_pair / derived_unit` is **constant across A**.

Result — the residual factor is **not** constant:

| A | need/pair (MeV) | κ = need/derived |
|---|---|---|
| 3 | 0.7638 | **3.214** |
| 7 | 0.5480 | 2.306 |
| 11 | 0.5530 | 2.327 |
| 13 | 0.5005 | 2.106 |

κ ranges 2.11→3.21 (**52.6% spread**) ⇒ **H0 REFUTED**: no single q₀-constant
times the derived unit supplies the invariant. The A=3 diproton (κ=3.21) is a
distinct regime — the ³He proton pair *is* the whole nucleus — vs the A≥7 mean
(κ≈2.25). The variation is **entangled with the unknown A-dependence of the
per-pair strong bond `B_pp`** (held at the A=3 H_6 value here); disentangling it
needs the `B_pp` bond at `H_{2A}` (intractable for A≥7) or a new categorical
construction. The LP-dual route is independently degenerate
(`he3-pairknot-composite-lp.witness.json`).

**This prunes the constant-invariant hypothesis class without any numerical
fit** — it does not PSLQ-match "3.21" or "2.25" to a constant (that would be the
numerology antipattern). It advances the open item by ruling out the simplest
class and identifying the confound.

## 3. Discipline status

- All compute **EXPLORATORY** (`computations/probes/`), discipline-bannered.
- Coulomb magnitude **cited**, never re-derived to close the gap.
- **No production script / dashboard / named constant touched.** The headline
  m_p/m_n/m_e dashboards use the Borromean vol-density form, not this tower; the
  binding-B / Hecke-path chains are the affected consumers, and they are not
  rewired here.
- The residual magnitude stays **open and forbidden-to-fit** until the
  A-dependent EM-linking object is derived from a 13-driver mechanism.

## 4. Falsifiable next step (not run — intractable)

Compute the per-pair strong bond `B_pp` at `H_{2A}` for A=7 to disentangle the
bond's A-dependence from the EM-linking invariant. At current basis sizes the
H_14 trace is intractable; flagged for the brane-tower compute backlog.

## Cross-references

- `computations/probes/mirror_pair_coulomb_sign_correction.py` + witness
- `computations/probes/em_linking_invariant_scoping.py` + witness
- `docs/audits/2026-06-18-he3-brane-tower-structural-gap.md` (diagnosis)
- `docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md` (#2478 synthesis)
- `docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md` (derived 31% Coulomb)
- `content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md` (def:coulomb-charge)
- `.claude/skills/local/production-vs-exploratory-discipline.md` (§Rule 14, 13-driver menu)
