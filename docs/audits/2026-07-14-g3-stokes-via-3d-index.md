# G3 keystone attack via the GGM 3d-index of 4₁ — RESOLVED (derivation, with a structural wall)

**Started:** 2026-07-14 (PR #3805 stub) · **Resolved / consolidated:** 2026-07-25
(branch `claude/argument-principle-residue-sum-2026-07-20`) · **Bean:** `qou-1dnr`
(stays OPEN — c₃ not closed) · **Tier:** scope-(a) — a genuine integer
*derivation* plus a structural (parity) exclusion of the naive c₃ identification ·
**Discipline:** no fit; no `c_k` wired; no A_ω wired to production.

> **Attribution.** This audit began as the PR #3805 stub (branch
> `claude/alien-calculus-surreal-integration-2t823z`), whose I_Δ scaffold
> [`computations/probes/tetrahedron_index.py`](../../computations/probes/tetrahedron_index.py)
> **correctly flagged its own gate**: the naive transcription failed the
> literature triality on negative-e cases and #3805 refused to glue the 4₁
> index on an unvalidated I_Δ. That gate was the right call. It has since been
> *cleared* on the sibling lineage that merged to `main`, and the full pipeline
> assembled and read out; this doc consolidates that completed work and records
> the honest verdict. The #3805 scaffold is retained (superseded header) because
> the canonical probe credits its path.

## 0. Verdict (read first)

- **A_ω IS a genuine derived INTEGER, not a fit.** The Garoufalidis–Gu–Mariño
  resurgent structure of 4₁ gives the Stokes constants as the Donaldson–Thomas /
  BPS spectrum **{3, 4}** of `T[4₁]` (GGM 2012.00062 Eq 96/98), read exactly from
  the 3d-index — an integer *count*, never inverted from the anchors. The
  load-bearing constant is **3**, on the singularity `ι = Vol(4₁)/π ≈ 0.6461`.
- **It does NOT derive the bar-odd c₃ — for a STRUCTURAL (parity) reason, not
  merely a numerical miss.** 4₁ is amphichiral ⇒ the u=0 complete-structure
  Chern–Simons vanishes (`V(σ₁) = i·Vol`, purely imaginary; GGM Eq 41), so the
  u=0 Stokes datum (the integer 3, the rotated 3d-index) is **bar-EVEN / real**.
  The c₃ anchor-dependence lives in the **bar-ODD** channel
  (`S(muon) = +0.00968`, `S(proton) = −0.03946`). Even + odd are different parity
  sectors: the derived bar-even A_ω cannot be the bar-odd c₃ datum.
- **The wall:** the bar-odd A_ω requires the **deformed (u≠0) state-integral
  median resummation** of the 4₁ Φ_b block — which is **not in the repo** — or a
  **non-amphichiral knot**. That is the honest open frontier; no integer is
  fabricated for it.

Net: this is a scope-(a) result on both sides — *positive* for "A_ω is a derived
integer" and *negative* for "A_ω (bare, u=0) = c₃". Bean `qou-1dnr` stays open;
c₃ stays EMPIRICAL (open in magnitude and sign, per
[`2026-07-24-c3-barodd-fork-correction.md`](2026-07-24-c3-barodd-fork-correction.md)).
L2 count unchanged (2/7).

## 1. The pipeline (all built, certified exact, merged to `main`)

| step | probe | witness assertion | status |
|---|---|---|---|
| I_Δ triality pin | [`tetrahedron_index_triality_pin.py`](../../computations/probes/tetrahedron_index_triality_pin.py) | full S₃ greens on `(m,e)∈[−3,3]²` incl. negative e, two q | ✅ |
| exact I_Δ engine | [`qbeta_g3_tetrahedron_index_exact.py`](../../computations/probes/qbeta_g3_tetrahedron_index_exact.py) | exact `ℤ[[x]]` series, `x=q^½`; triality as exact monomial identity | ✅ |
| 4₁ total index | [`qbeta_g3_fourone_index_assembly_corrected.py`](../../computations/probes/qbeta_g3_fourone_index_assembly_corrected.py) | matches DGG 1112.5179 **Eq (4.20)** exactly; amphichiral Eq (4.19) | ✅ |
| GGM Stokes data | [`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py) | `det W_m=2`, q-diff Eq (49), (59a) sandwich vs printed (61)–(64) | ✅ |
| A_ω amplitude | [`qbeta_g3_aomega_residue_first_number.py`](../../computations/probes/qbeta_g3_aomega_residue_first_number.py), [`qbeta_g3_aomega_sharpened_amplitude.py`](../../computations/probes/qbeta_g3_aomega_sharpened_amplitude.py) | Borel–Padé leading pole at `Vol/π`; `|2πi·res|` within ×2 of the proved integer 3 | ✅ |
| c₃ identification | [`qbeta_c3_stokes_ggm_order3_probe.py`](../../computations/probes/qbeta_c3_stokes_ggm_order3_probe.py) | bare integer −3 in Q_β ladder ⇒ 576 ppb (74× target); **NEGATIVE** | ✅ (negative) |

## 2. The triality gate that stalled #3805 — cleared

#3805's self-test tried `I_Δ(m,e) =? (±q^?)^e · I_Δ(−e−m, m)` and found it red on
negative e. The fix is that the S₃ **cyclic** prefactor depends on **m, not e**.
Independently reproduced here (mpmath, 40 dps, q=0.13, tol 1e-25, 49 pairs):

```
CORRECT  (-q^½)^m · I(-e-m,m):  mismatches / 49 = 0
#3805    (-q^½)^e · I(-e-m,m):  mismatches / 49 = 42
```

Pinned S₃ (empirically, no guessed convention):
`I_Δ(m,e) = (−q^½)^m · I_Δ(−e−m, m)` (ℤ/3 generator, order-3, prefactors→1) and
`I_Δ(m,e) = I_Δ(−e, −m)` (ℤ/2 reflection, no prefactor).

## 3. The assembled 4₁ 3d-index (low orders, literature-validated)

The 4₁ (m004) total index `I_{4₁}(1,1)(q)` via DGG Eq (4.18) on the exact I_Δ
engine reproduces DGG 1112.5179 **Eq (4.20)** to exact integer coefficients:

```
I_{4₁}(1,1)(q) = −q − q² + 2q³ + 7q⁴ + 11q⁵ + 11q⁶ + 3q⁷ + …
```

and is amphichiral, `I_{4₁}(m,e) = I_{4₁}(−m,−e)` (Eq 4.19). The GGM descendant
Stokes tower on the `ι = Vol(4₁)/π` ray is
`S⁺_{σ₁σ₁}(q) = 1 − 8q − 9q² + …` (substrate value 0.258436267261), certified
against the printed GGM series.

## 4. The A_ω extraction and the cross-check vs Vol(4₁)/π

The Borel–Padé leading pole of the exact κ-rung series sits within 5% of
`Vol(4₁)/π ≈ 0.6461` — the **same object** as the corpus's independently measured
Borel action A ≈ 0.62–0.65 (#3692/#3819) — and `|2πi·res|` sits within a factor 2
of the proved integer **3**. So the singularity *position* (even-face action) and
the integer Stokes *count* both check out. But the exact pole phase is purely
**kinematic** (`arg(ι̃·2πi/ξ) = arctan(t/π)` to 1e-12): there is **no intrinsic
odd phase in the singularity position** — consistent with §0's parity finding.

Two tempting numerological identifications were tested and refuted (scope-(a)):
- `−3 = disc(ℚ(√−3))` (the 4₁ trace-field discriminant) — refuted because the
  Stokes spectrum is `{3,4}` and the co-occurring **4** has no discriminant
  meaning; the integers are the DT/BPS spectrum (GGM Conjecture 4), not a field
  discriminant ([`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md)).
- `c₃ = −3` (bare integer in the Q_β ladder) — refuted: 576 ppb residual, 74×
  the 7.8 ppb 100× target, worse than even the crude −2 near-match (43 ppb).

## 5. Formalize-first honesty check (STRICT)

- **Derivation, not a fit.** A_ω = {3, 4} is an integer count read from the
  3d-index (DT/BPS spectrum, GGM Conjecture 4); nothing was inverted from Q_β or
  the anchors. This satisfies the anti-fit / formalize-first discipline.
- **Scope-(a) NEGATIVE on the c₃ identification**, with the invariant cited: the
  refutation is *parity-structural* (bar-even u=0 Stokes datum vs bar-odd c₃
  anchor), reinforced by the amphichiral CS=0 fact (GGM Eq 41) and the two
  numerical refutations of §4. Per the "before declaring refuted" rule this is a
  scope-(a) *scope-limited* negative, not a scope-(b) structural exclusion of the
  3d-index route as such — the **deformed (u≠0)** median resummation remains the
  live, un-refuted handle for the bar-odd A_ω.
- **Nothing wired.** No A_ω value and no `c_k` enters any dashboard or production
  script. Registry untouched.

## 6. Lean rigidity leg (companion, sorry-free reduction)

The "A_ω carries no fitting freedom" leg is formalized down to named open inputs
(see [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md) §6–§10):
`FaddeevRigidityReduction.uniqueUpToScalar_of_entire_of_sq_not_real` (lean-direct
exit 0) consumes upstream `ratio_const_of_doublyPeriodic` (elliptic-Liouville) and
`PeriodLatticeBasis.exists_period_basis` (`hspan` **closed**). Two open inputs
remain: `hibinv` (identity theorem off the dual pole lattice, bean `qou-q95i`) and
`hratio`/entireness (the Φ_b holomorphicity + divisor-cancellation endowment, bean
`qou-2cvs`). None axiomatized; the reduction is a proved implication. This proves
A_ω is *forced*, not *what it is* — it does not touch the §0 parity wall.

## 7. What would move the bar-odd frontier (for the next agent)

1. **Deformed (u≠0) state-integral median resummation** of the 4₁ Φ_b block —
   the missing in-repo object; the bar-odd A_ω lives here, unsuppressed (the
   substrate-meridian real-q Stokes jump is 10⁻²⁷-suppressed, so it is NOT here —
   [`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)).
2. **A non-amphichiral knot** whose u=0 Stokes data already carries a bar-odd
   (CS≠0) part — sidesteps the amphichiral CS=0 obstruction entirely.
3. **The quantum-modularity normalization** bridging the integer Stokes datum to
   the c₃ rung (phib audit §4e) — the algebraic factor that the bare integer
   lacks.

## Cross-references
- DGG tetrahedron / 4₁ index: `dimofte-gaiotto-gukov2013`, arXiv:1208.1663,
  1112.5179 Eq (4.18)/(4.19)/(4.20)
- GGM Stokes = DT invariants: `garoufalidis-gu-marino2021` (2012.00062 Eq 96/98,
  Conjecture 4)
- Fork correction (c₃ open, magnitude+sign): [`2026-07-24-c3-barodd-fork-correction.md`](2026-07-24-c3-barodd-fork-correction.md)
- Evidence base + Lean rigidity target: [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
- Trace-field refutation: [`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md)
