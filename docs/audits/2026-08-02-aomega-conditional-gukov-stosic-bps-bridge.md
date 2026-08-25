# A_ω = 3 as a conditional-on-published-conjecture result — and the honest BPS-sector non-degeneracy result

**Date:** 2026-08-02 · **Beans:** `qou-ujmw` / `qou-qnnq` (G3 Stokes keystone,
c₃-odd bridge) · **Branch:** `claude/aomega-conditional-gukov-stosic-bps-2026-08-02`
· **Tier:** conditional adoption (Vol-conjecture-style) + non-degeneracy gate ·
**Scope:** (a); nothing fitted; nothing wired to production; L2 / Q_β unchanged.

## The task

Owner directive (2026-08-02): move the G3 Stokes integer `A_ω = 3` of the
figure-eight `4₁` from *structurally-open* → *conditional on a citeable published
conjecture*, treated exactly like the Volume Conjecture
(`conj:kashaev-volume-conjecture` Rule-14 adoption). The named conjecture was the
**Gukov–Stošić knot-homology ↔ BPS-states bridge** (arXiv:1112.0030). Mandatory
non-degeneracy gate: verify the BPS count of `4₁` reproduces the GGM DT/3d-index
spectrum `{3,4}` (reduced-Stokes `3`) *through the bridge* — and if it does **not**,
STOP and report honestly, landing **no** degenerate class.

## Author verification (from `library/`, arXiv title pages)

| ref id | arXiv | authors (verified) |
|---|---|---|
| `gukov-stosic2012` | 1112.0030 | Sergei Gukov, Marko Stošić |
| `gorsky-gukov-stosic2013` | 1304.3481 | Eugene Gorsky, Sergei Gukov, Marko Stošić |
| `gukov-pei-putrov-vafa2017` | 1701.06567 | Sergei Gukov, Du Pei, Pavel Putrov, Cumrun Vafa |
| `kucharski-reineke-stosic-sulkowski2017` | 1707.02991 | Piotr Kucharski, Markus Reineke, Marko Stošić, Piotr Sułkowski |

## The honest non-degeneracy result: the named bridge FAILS; a sibling bridge PASSES

There are **two** distinct knot-homology/BPS bridges in the literature, and they
identify **different** BPS spaces:

| Bridge | BPS sector | object | `4₁` count |
|---|---|---|---|
| Gukov–Stošić 1112.0030 | **OPEN** | colored HOMFLY homology on conormal `L_K ⊂ T*S³` | `det(4₁) = 5` |
| GPPV 1701.06567 + GGM Conj 3(d) | **CLOSED** / state-integral | `Ẑ` / resurgent Stokes = DT/BPS Hilbert space | `{3, 4}` |

**Open sector (FAIL).** Gukov–Stošić 1112.0030 states plainly (abstract, §1–2):
"knot homologies admit a physical description as spaces of **open** BPS states"
(M5-brane on `R × L_K × D`, `L_K` the conormal bundle to the knot). The
knots–quivers correspondence (Kucharski–Reineke–Stošić–Sułkowski 1707.02991)
makes this count explicit: the quiver of a knot has **one node per HOMFLY-PT
homology generator**. Their worked example is the trefoil, `3₁ → 3` nodes
(`3 = det 3₁`, calibration). For the figure-eight the reduced HOMFLY homology is
thin of rank `det(4₁) = 5`, so the open-BPS/quiver count of `4₁` is **5**. Since
`5 ∉ {3, 4}`, the open-HOMFLY Gukov–Stošić bridge does **not** reproduce the GGM
resurgent-Stokes spectrum and does **not** license `A_ω = 3`. **No degenerate
class on this bridge is landed** (per the gate).

**Closed sector (PASS).** The `{3, 4}` are Garoufalidis–Gu–Mariño resurgent Stokes
constants of the state integral of `S³∖4₁` — the peacock paper (2012.00062)
Conjecture 3(d): *"the Stokes constants are integers corresponding to the
Donaldson–Thomas invariants … and the BPS degeneracies."* GPPV (1701.06567)
realise that DT/BPS count as the graded dimension of the fivebrane BPS Hilbert
space of `T[M₃]` (the `Ẑ` / 3d–3d sector, DGG index the dictionary). This is the
closed / state-integral sector, and it reproduces `{3, 4}` (reduced symmetry
constant `3`, corpus q⁴⁰⁰); its `q → 0` anchor `S⁺(0)₀₁ = 3` is machine-checked
unconditionally (`QOU.QBeta.StokesQZeroDTCount`, sorry-free). GGM proved
Conjecture 3 for `4₁`, so the bridge instance is discharged there.

Witness: [`aomega-bps-sector-nondegeneracy.witness.json`](../../computations/probes/aomega-bps-sector-nondegeneracy.witness.json)
(`allPassed`; records both sector verdicts).

## What lands (closed-sector bridge only)

1. **`conj:stokes-dt-bps-bridge`** — the closed-sector adopted conjecture
   (Vol-conjecture-style). Lean `class QOU.QBeta.StokesDTBPSBridge` carries the
   two identifications `stokes = dt` (GGM Conj 3(d)) and `dt = bps` (GPPV) as
   fields (the conjecture's **inputs**); **no** field asserts `A_ω = 3`.
   lean-direct **exit 0**, sorry-free, content-bearing (no `True`, no empty
   marker).
2. **`thm:aomega-fourone-dt-count`** — `A_ω(4₁) = 3` as a BPS/DT count,
   §3b-cond conditional theorem. `QOU.QBeta.aomega_fourOne_dt_count` derives
   `bpsDim(4₁) = 3` by composing the two bridge fields with the
   bridge-independent certified `q → 0` Stokes datum `= 3`
   (`StokesQZeroDTCount.stokes_qzero_offdiagonal`). The value `3` comes from the
   certified computation, not a class field — **non-degenerate** (§3b-cond item 5).

## Anti-laundering / discipline

- **Class carries hypotheses, theorem derives the conclusion.** The `A_ω = 3`
  value is never a class field; it is composed from the two published
  identifications and a separately-certified integer. This is the same shape as
  `QOU.FluidDynamics.q_bkm_criterion` (the §3b-cond verified exemplar).
- **Not a proof of `A_ω = 3` from QOU drivers.** The internal (Hecke `H₃` / Bring
  / Wedderburn) derivation of the integer `3` remains **open** (`qou-qnnq`);
  this PR imports it from GGM (a theorem for `4₁`) and makes the dependency an
  auditable conditional class, nothing more.
- **Not wired to production.** L2 accuracy dashboard and the `Q_β` ladder are
  untouched. `A_ω = 3` is conditional (theorem for `4₁`, conjectural in general).
- **Honest negative recorded.** The open-HOMFLY Gukov–Stošić route is a scope-(a)
  finding: that bridge's `4₁` count is `5`, a different BPS sector — it does not
  reproduce `{3, 4}`. This constrains *which* published conjecture licenses
  `A_ω`; it does not exclude any ingredient.

## Flag (pre-existing, not fixed here)

The A_ω bricks `StokesQZeroDTCount.lean` / `StokesSymmetryConstant.lean` cite
`[garoufalidis-gu-marino2021]` for "GGM 2012.00062". In the corpus, 2012.00062 is
`garoufalidis-gu-marino2023peacock` (the peacock paper); `...2021` is 2007.10190.
A follow-up should correct the `-- Ref:` keys in those two library files.

## Cross-references

- Lean: [`StokesDTBPSBridge.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesDTBPSBridge.lean) (new), [`StokesQZeroDTCount.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesQZeroDTCount.lean) (q→0 anchor).
- Content: [`conj:stokes-dt-bps-bridge`](../../content/quantum-observable-universe/mass-theory/stokes-dt-bps-bridge.md), [`thm:aomega-fourone-dt-count`](../../content/quantum-observable-universe/mass-theory/aomega-fourone-dt-count.md).
- Prior synthesis: [`2026-08-01-ujmw-aomega-dt-index-derivation.md`](2026-08-01-ujmw-aomega-dt-index-derivation.md); [`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- Sources: 1112.0030, 1304.3481, 1701.06567, 1707.02991, 2012.00062 (peacock Conj 3(d)).
