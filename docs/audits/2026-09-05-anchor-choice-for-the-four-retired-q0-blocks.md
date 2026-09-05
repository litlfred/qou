# The anchor choice for the four retired-`q₀` blocks: pros, cons, downstream

**Bean:** `qou-i229`. **Probe:** `published_figures_carry_a_retired_q0_probe.py` (5/5).
**Date:** 2026-09-05.

## Summary

I framed this as an owner-gated **proton-vs-muon** decision. That framing was
wrong, and correcting it collapses most of the choice.

The six figures do not carry a *retired anchor*. They carry the **CODATA-2018
vintage of the muon anchor** — the same anchor the corpus's own two-layer
convention says canonical blocks should use. Verified by inverting the CAL-2 pin
`m_μ/m_e = Vol(4₁)/ℏ_q²`:

| `m_μ/m_e` | vintage | `q₀` it yields |
|---|---|---|
| `206.7682830` | **CODATA 2018** | `1.1099785955541805753` |
| `206.7682827` | **CODATA 2022** | `1.1099785956427390467` |

The first is the published constant **to twenty digits**; the second is the live
muon anchor, exactly. So the real question is not *which anchor* but *which
vintage*, and the answer to that is not a matter of taste.

## This is collateral of a known, already-fixed defect

`qou_substrate/codata.py` records that `206.7682830` was carried under a
"CODATA 2022" comment **across 138 sites**, against a second registry holding the
correct `206.7682827`, and that "nothing could detect the disagreement, because
there was nothing authoritative to compare against". It was fixed on 2026-08-15
by reading the NIST table instead of transcribing it.

**That fix reached `computations/` and `tools/`. It did not reach `content/`.**
The six figures are the residue. This is the same shape as the transfer-matrix
readout corrected earlier today: the correction landed in the compute and the
published block kept the old value, because nothing walks from one to the other.

The discrepancy is `1.451 ppb` in `m_μ/m_e`, i.e. `0.065σ` — physically nothing,
which is exactly why it survived.

## What the corpus's own rule already decides

The two-layer convention (AGENTS.md §"q₀ anchor convention", owner-clarified
2026-06-16):

- **Ideal / canonical** — `q₀ ← CAL-2 (𝔇_β)`, pinned via the lepton ratio.
  **Muon.**
- **Physical-Observations** — may anchor on a derived quantity with smaller
  experimental error: `m_p/m_e` at `0.017 ppb` against the muon ratio's
  `22 ppb`. **Proton.** Explicitly "*not* a change to the canonical CAL-2 and
  *not* a fourth calibration".

`q0_anchor_manifest.json` then tags producers, and **six of its nineteen
`ideal_muon` entries are `qbeta_*`**. Two of the four blocks are Q_β blocks. The
corpus has already ruled on those.

There is a sharper reason for the Q_β pair specifically: **Q_β *is* the CAL-2
proxy.** `Q_β = ℏ/𝔇_β`, and `𝔇_β` is what the muon pin pins. Anchoring a Q_β
table on the proton ratio makes it a prediction derived from a prediction, and
folds the μ–p tension into a quantity whose job is to express CAL-2.

## The options, with magnitudes

`q₀` moves by `7.98e-11` under A and `1.15e-8` under B — **B is 145× larger.**

| figure | published | A: muon 2022 | B: proton | A shift | B shift |
|---|---|---|---|---|---|
| `1 + q₀` | `2.10997859556` | `2.109978595642739` | `2.109978582751381` | `3.9e-11` | `6.1e-9` |
| `log(1+q₀)` | `0.74667780313` | `0.7466778031913746` | `0.7466777970816641` | `8.2e-11` | `8.1e-9` |
| `log(1/ℏ_q)` | `2.31181024982` | `2.311810249123439` | `2.311810354726361` | `3.0e-10` | `4.5e-8` |
| `q[9]_q[10]_q` | `136.823219654` | `136.8232197292729` | `136.8232088535826` | `5.5e-10` | `7.9e-8` |
| `1 + ℏ_q²` | `1.009817188513479` | `1.009817188527722` | `1.009817186454275` | `1.4e-11` | `2.0e-9` |
| `h²` | `0.04370621823290131` | `0.04370621829759422` | `0.04370620853252199` | `1.5e-9` | `2.2e-7` |

Roughly **11 published significant digits survive option A; about 8 survive B.**

### Option A — refresh the vintage, keep the muon anchor  ✅ recommended

**For.** It is not a convention change at all; it is the 2026-08-15 CODATA fix
finally reaching `content/`. It agrees with the two-layer rule for canonical
blocks and with the manifest's own `qbeta_*` tagging. It is the smallest move, so
the most published digits survive. It removes a documented stale vintage that the
repo already knows about and warns against.

**Against.** It requires holding that all four blocks are canonical-layer — three
clearly are; the fourth is argued below. And it leaves them muon-anchored while
906 of 940 tagged producers are proton, so they remain in the minority
convention. That is a *consistency* cost, not a correctness one: the convention
is deliberately mixed and a blanket flip is explicitly forbidden.

### Option B — switch to the proton anchor

**For.** It aligns with the overwhelming majority of producers (906 vs 19), and
the proton ratio is ~1300× more precise (`0.017` vs `22 ppb`). One anchor
everywhere is simpler to reason about.

**Against, and these are strong.** It contradicts the two-layer rule for
canonical blocks. For the two Q_β blocks it is close to self-undermining, for the
CAL-2-proxy reason above. It is a 145× larger perturbation than the defect being
fixed — using a vintage refresh as the occasion for a convention change is how
conventions drift unnoticed, which this arc has spent its time undoing. It
destroys ~3 more published digits than necessary. And it would require retagging
the manifest's `qbeta_*` entries, or content and compute diverge on the same
quantities.

### Option C — leave as published

Defensible only as a hold pending the ruling. It is now a *knowing* choice: the
stale vintage is documented in the repo and flagged in the blocks.

## The one block I would not decide without you

`em-coupling-bring-zero-mode` lives under `predicted-spectra/`, and under the
two-layer rule "predicted spectra" reads as Physical-Observations → **proton**.
But the quantity is `q·[9]_q·[10]_q`, the *bare* coupling — a derivation input to
`α_EM`, not an observation. Its section placement and its content point opposite
ways, and no manifest entry covers it. **This is the one genuine ambiguity of the
four**, and it is a question about what that block is for rather than about `q₀`.

The other three I would refresh under option A without further consultation:
`hecke-log-decomposition-table-data` (a Hecke derivation table) and the two Q_β
tables (covered by the manifest's own tagging).

## Downstream implications

- **Nothing physical moves under A.** `1.451 ppb` on `m_μ/m_e` is `0.065σ`; no
  claim, comparison or agreement figure in the corpus changes sign, order or
  verdict.
- **Under B the μ–p tension enters four blocks that currently do not carry it.**
  The proton re-pin makes `m_μ/m_e` a `9.5σ` cross-check prediction. Blocks
  anchored on muon express CAL-2; blocks anchored on proton inherit that tension.
  Moving these four across that line changes what they *mean*, not just what they
  print.
- **A closes a class; B opens one.** Under A the four blocks join the substrate's
  already-corrected state and the CODATA-vintage question is finished. Under B
  they become the only content blocks on proton while their `qbeta_*` producers
  stay muon-tagged, which is a new divergence to maintain.
- **Either way, the walk from compute-fix to published-figure is still missing.**
  Both defects found today — this and the transfer-matrix readout — are a
  correction landing in code while a block keeps the old value. Neither gate in
  the repo looks across that boundary. `scripts/unsourced-published-figures.py`
  is the first thing that does, and it found this only because the figures had no
  provenance at all; a stale figure that *does* match some producer would still
  be invisible.

## A stale comment found en route

`computations/substrate/q_parameter.py` states the corpus is "genuinely MIXED
(sweep 2026-07-06: 279 proton + 455 muon)". The manifest now reads **906 proton,
19 muon, 15 ambiguous**. The comment is stale by a large factor and would mislead
anyone reasoning about corpus-wide balance from it — including the argument in
option B above, which I checked against the manifest rather than the comment.
Not changed here: `q_parameter.py` is anchor-selection machinery and the owner
ruling on it is explicit ("do NOT change this default"). Filed in `qou-i229`.

## Recommendation

**Option A for the three canonical blocks; ask on `em-coupling-bring-zero-mode`.**
It is the smallest change, it is the corpus's own already-made decision reaching
content, and it treats a data refresh as a data refresh rather than as an
opening to re-decide a convention.
