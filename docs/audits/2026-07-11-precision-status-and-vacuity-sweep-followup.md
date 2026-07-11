# Precision status (m_p / Q_β) + Lean vacuity-sweep triage — follow-up to PR #3511/#3513

**Date:** 2026-07-11
**Branch:** `claude/dashboard-low-ejlwg3`
**Context:** follow-up to the de-laundering PRs #3511 (removed fabricated
trivial instances from 6 open conjecture carriers) and #3513 (A>40 atlas
relabel + `Archimedean.BorromeanQuark` self-assuming-field removal). This doc
pins two things so they are not re-claimed: (1) the honest ppb-level accuracy
status of the nucleon masses and Q_β, and (2) the state of the machine
vacuity sweep across the Lean tree.

---

## Part 1 — ppb-level precision status (the "1 ppb" masses)

Source: `computations/per-observable-100x-status.witness.json` (compute 70 dps,
output 60 dps). Ranked by the framework's L2 goal (σ_pred ≤ σ_exp/100).

| Observable | predicted (MeV) | err vs CODATA (ppb) | 100× target (ppb) | meets L2? |
|---|---|---|---|---|
| m_e | 0.510998951 | 0 (anchor) | 0.0029 | yes |
| m_K/m_π | 3.53711852 | 23.4 | 263.6 | yes |
| m_p | 938.272089 | 1.35 | 0.0031 | no (≈ 437×) |
| m_n | 939.565423 | 2.39 | 0.0057 | no (≈ 416×) |
| Δ_pn | 1.293333 | 755.6 | 4.74 | no |
| m_μ | 105.658398 | 209.8 | 0.218 | no (≈ 964×) |
| Q_β | 0.782334 | 1248 | 7.80 | no (≈ 160×) |

**Canonical L2 count = 2/7** (m_e, m_K/m_π), per `beats_100x_count`. The
"1 ppb masses" seen in built LaTeX are m_p (1.35 ppb) and m_n (2.39 ppb) —
genuinely at the 1–2 ppb level in absolute accuracy, from the muon-anchored
Borromean Hecke energy (`canonical_mass.py`), unchanged by the recent binding
commits — but they do **not** meet the framework's own 100× goal.

### 1a — The sub-ppb m_p was a fit (dropped 2026-07-04)

Through 2026-07-04 the built tables showed m_p on CODATA to 0.0004 ppb. That
came from a multiplicative **Habiro precision tower** bolted onto the
parameter-free base m_p = 2·m_μ·F_Bor − 12·m_e:

$$
\text{tower}(q) = (1 + c_4 u^4)(1 + 4 u^5)(1 - 29 u^6), \quad u = b\,\hbar_q^2 \approx 0.00852, \quad c_4 = 4143/90 \approx 46.033.
$$

The three integers (c₄ ≈ 46, +4, −29) are the fitted part. Three
facts show it is a fit, not a derivation (see
[`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md)):

1. **c₄ is the q₀ pin offset, not a constant.** The exact c₄ that lands
   m_p on CODATA runs linearly from 0 at the proton pin to 46.04 at the
   muon pin across the 11.5 ppb window between the two legitimate calibrations
   (affine fit matched to < 9×10⁻⁶). "46" just encodes "calibrate on
   the muon" — it *is* the μ–p tension rewritten at order u⁴.
2. **No derivation trail.** `4143` appears on one line in the corpus; `git log -S`
   finds nothing computing it; the cited "s5bb colour Reeb index" route was
   independently refuted.
3. **Entropy bound.** c₄ is a 2–3 significant-figure quantity, so `46`,
   `4143/90`, `45.74` are all equally consistent and equally content-free.

The tower was dropped (it was also a live +242 ppb bug once q₀ re-pinned to
the proton). The honest de-fitted m_p is the **1.35 ppb** above.

### 1b — Q_β is anchor-insensitive (the refresh moves it ≈ 28 ppb)

The committed canonical Q_β = 0.782334 MeV (1248 ppb) is **muon-anchored**
(its witnesses carry q₀ = 1.10997859556…). Evaluating the production
Form-A closed form at both pins:

| anchor | q₀ | Q_β (Form A, N=1) |
|---|---|---|
| proton | 1.10997858275 | 0.79133902 |
| muon | 1.10997859556 | 0.79133900 |

The proton-vs-muon shift is only **≈ 28 ppb** (from the 11.5 ppb q₀
change). So refreshing the anchor leaves Q_β at ≈ 1250 ppb — the
anchor was never the lever. The historical "5.7 ppb Habiro-exact" Q_β came
from a fuller c_k / Habiro tower against the muon pin, which is a **tiered
near-match** per the c_k truncation-order framing
([`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)),
not a robust proton-anchored prediction.

**Do not re-claim** a sub-ppb m_p or a sub-10-ppb Q_β as "met": the
former was a dropped fit, the latter a stale-anchor near-match.

---

## Part 2 — Lean vacuity sweep (machine scan state)

`content/pipeline/lean-vacuity-axiom-audit.ts` was run across the QOU Lean tree
(1956 `.lean` files). Result: **42 non-exempt candidates across 107 files** (92
entries already exempt), by criterion:

| criterion | count | severity |
|---|---|---|
| `proof-no-false-premise` | 23 | critical |
| `proof-no-trivial-true` | 8 | critical (some exempt as shadow-stub / §3b placeholder) |
| `proof-no-self-assuming-projection` | 4 | critical (some exempt) |
| `proof-claims-unencoded` | 4 | major |
| `proof-no-provable-axiom` | 2 | critical |
| `proof-no-decide-masking` | 1 | critical |

**These are high-recall candidates, not confirmed defects.** The
genuine-vs-legit verdict is a per-candidate agent call recorded in
[`lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json); this sweep
does not adjudicate them. Two observations from spot-checking:

- **`categorical-reeb-derivation.lean:62` (claims-unencoded) is a false
  positive.** Its docstring transparently encodes 2 of 3 conditions as fields
  (`reeb_normalizes`, `reeb_periodic`) and honestly defers the 3rd (the Leibniz
  rule, which needs a preadditive ambient) with a stated reason. Not laundering.
- **The `q-beta-c3-continuum-geometry.lean` candidates** (`axiom f_integrable`;
  `c3_continuum_limit_is_hyperbolic_volume : True`) overlap the **active sibling
  branch** `claude/qbeta-c3-continuum-vol41-rescope`, which is already naming the
  vacuous capstone in that file. Left to that branch — not touched here.

The concentrated laundering batch (`25ef4f4b`, the fabricated "closed primary
conjecture" instances) was fully unwound in #3511/#3513. The remaining 42 are a
mixed population (false positives, sibling-owned, and some needing genuine math
analysis of "false premise" theorems) and belong in the ledger workflow
(`--review-ledger` to seed, `--check-ledger` to gate), adjudicated per-candidate
rather than mass-edited.
