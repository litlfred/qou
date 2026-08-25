---
# qou-bdkx
title: 4 witnesses declare one q0 anchor and carry another — declaration/payload contradiction
status: completed
type: bug
priority: normal
created_at: 2026-08-23T07:53:49Z
updated_at: 2026-08-24T00:00:20Z
---

Split out of qou-p8lx after re-measuring the `q0 constant staleness` gate on
main (2026-08-23). The gate flags 6 witnesses in the muon basin; they are NOT
one backlog.

CONSISTENT — valid as recorded, part of the GATED bulk migration (qou-1c4y,
needs scoped sign-off). Do not drain these here:

  lever1-binding-core-characterization        q0Anchor=muon,  .q0Value muon
  lever1-binding-habiro-single-element-test   q0Anchor=muon,  .params.q0 + .q0Value muon

CONTRADICTORY — declared anchor disagrees with the payload. Actionable WITHOUT
the gated migration, because the fix is to reconcile a declaration with a
value, not to re-pin the corpus:

  lever1-color-eq-intrinsic-tau-rapidity   declares 'proton'
      .results.substrate_q0.q = 1.10997859556        (muon basin)
  lever1-color-eq-lambda-sw-rapidity       declares 'proton'
      .results.q0 = 1.109978595557335                (muon basin)
  z2bn-tau-derivation-probe                declares 'independent'
      q0AnchorReason: "Reads no substrate value. PROVED by run..."
      .q0 = 1.1099785955573347199                    (records one anyway)
  knot-volumes                             declares NO anchor
      .assertions[9].computed = 1.1099785955541805

This is the "layer straddle" AGENTS.md calls a defect regardless of size: an
ideal-layer (muon) value inside an experimental-layer (proton) declaration.

## Per-witness triage still needed — do NOT batch-fix

Each has two possible resolutions and they are not interchangeable:
  (a) the declaration is right, the payload is stale  -> re-run the producer
      at the declared pin;
  (b) the payload is right, the declaration is wrong  -> fix the declaration.

Which applies needs the producer read. AGENTS.md is strict here: never
hand-edit a witness to match a table — fix the producer and re-run.

`z2bn-tau-derivation-probe` is the most interesting: 'independent' means
"reads no substrate value", so either the .q0 field is informational
provenance (declaration right, field misleading) or the probe does consume
q0 and the declaration is false. Those have opposite fixes.

## Measurement note

My first scan of these reported `knot-volumes: 0 muon-carrying fields` while
the gate reported one. My scan only walked STRING values; the value is a JSON
number. Anyone re-measuring must walk numbers too — repr() the float, do not
rely on the serialized text.


## knot-volumes RESOLVED — and two claims about it were wrong (2026-08-23)

Disposition, measured, with SnapPy 3.3.2 actually installed and the producer
actually re-run (`computations/knot-volumes.py`, exit 0 after the fix):

**1. It was never stale against a rename.** PR #5532's body says the witness is
"stale against a rename (`knot-volumes.py` -> `knot_volumes.py`)". There is no
rename. The producer `computations/knot-volumes.py` still exists under that
exact name and the witness's `scriptHash` `54201a9fe7aa` is its sha256 prefix
**byte-for-byte**. `computations/substrate/knot_volumes.py` is a *different
file* — a constants module (`VOL_4_1_MPF`, `vol_at`, `iter_provenance`), sha
`436b24a480fe`, no witness emitter, its `__main__` only prints. It happens to
sit next to the witness and differ by one hyphen. Hashing it is what produced
the false "stale" reading. `witness-provenance-audit` independently agrees:
`PROV_OK`.

**2. A re-run does NOT reproduce it unchanged.** The prior session reported
"the re-run reproduced the witness unchanged", which is what a run of the
*constants module* looks like — it writes nothing. A real run of the producer
changes three assertions and, before the fix, **exits 1**.

**3. The real defect: a CODATA edition straddle.** `MASS_ASSERTIONS` carried
the hand-typed literal `206.7682830` for m_mu/m_e with `tolerance: 1e-7`. That
is the CODATA-**2018** value. `qou_substrate.constants` moved to reading the
NIST table (`allascii.txt`) and now supplies the 2022 value `206.7682827` —
3.0e-7 away, three times the tolerance. So this producer has been **failing on
main** since that switch, while its committed witness still recorded
`allPassed: true` from the last run under the old literal. Exactly the straddle
`codata_table_vintage_audit.py` was written to catch, one file over.

  Fixed at the producer: `expected` is now read from the same NIST row the
  registry reads, so the assertion checks registry-vs-table instead of
  registry-vs-transcription. Re-run: 11/11 pass, exit 0.

**4. The anchor is `independent`, and this is the MIRROR of the z2bn case.**
The producer reads no substrate q0 — no `q_parameter.Q` / `Q_MP` / `q_at`, no
q0 literal; its only registry import is the CODATA mass ratio. Its q comes out
of `Vol(4_1)` and `m_mu/m_e`, i.e. the CAL-2 definition run forward as an
assertion's own subject. Checkable evidence that it derives rather than
transcribes: it carried `1.109978595554…` where all five other flagged
witnesses carry the literal `1.109978595573…`; the difference is precisely the
CODATA-2018 ratio it was computed from. z2bn declared `independent` falsely
because it *consumed* a hardcoded q0; knot-volumes emits one without consuming
any. The test is whether q0 is an INPUT, not whether a q0-shaped number appears.

  `q0Anchor: "independent"` + `q0AnchorReason` now declared at the producer.
  `q0-anchor-consistency-audit`: `Q0_INDEPENDENT` 37 -> 38, and knot-volumes
  leaves `Q0_ANCHOR_MISSING`. (That bucket still reads 1921 because
  `du-law-reparametrisation` entered it from main's `fbf64285` — not this
  change.)

**5. The staleness gate could not be drained at the producer, so the gate was
wrong, not the witness.** Its value is in the muon basin BY CONSTRUCTION — the
muon pin is *defined* by inverting this very relation — so no re-run can move
it toward the proton pin. `witness_constant_staleness.py` now exempts a basin
value only when BOTH (a) the witness declares `independent` with a reason, and
(b) EVERY basin value sits at `.assertions[i].computed|expected`, i.e. is a
measurement checked against its own expectation rather than a constant recorded
for downstream use. Condition (b) is load-bearing: z2bn declared `independent`
falsely and is **still caught**, because its value sat at top-level `.q0`.
Measured across all six, (b) alone separates the one structural case from the
five real ones. The exemption is printed, never silent, and `--selftest`
covers 11 cases including every z2bn-shaped negative.

Gate: 6 -> 5 stale. The five remaining are unchanged and still belong to this
bean (2) and to the gated bulk migration qou-1c4y (2, plus z2bn's own fix on
PR #5532's branch).


## aK_via_lp_dual_hecke_basis — RETRACTED as a straddle (2026-08-23, PR #5611)

I reported this as the fourth genuine straddle. It is not one.

Its q of its own is real — a file read of the muon anchor-defining witness
`q-pinning-50-digit.witness.json` (`Q_PIN`, line 76; `Q` line 81; `H` line 82).
But `Q` and `H` reach exactly two statements, both stamps:

    w.add_parameter("q0", repr(Q))    # line 237
    w.add_parameter("h",  repr(H))    # line 238

Every number in the witness comes from `pyhecke.gram`'s IMPORT-TIME float64
constants `TR_M` (gram.py:218) and `G = _build_gram()` (gram.py:394), built
from `q_parameter.Q` — the manifest pin, proton for this unlisted stem.

So the 39 moving fields are anchor-sensitive MATH, as they should be. No
computed quantity mixes two layers. The defect is a MISLABEL: the witness
advertises muon over numbers that are entirely proton — the direction that
misleads a reader who trusts the stamp.

Bounded: `a-K-via-lp-dual-hecke-basis.witness.json` is UNTRACKED, so nothing
wrong is on main. (`qou-fu8c` — degenerates under convention D — is likely why.)

Carrier is a THIRD shape, distinct from the other two found this session:
  1. defaulted function parameter  (`_cached_seminormal(shape)`, no q passed)
  2. import-time module constant   (`pyhecke.gram.TR_M` / `G`) — this one
     has no parameter to pass at all; q is fixed the instant the module loads
  3. (the earlier inline closed-form derivations)

Guard added: `anchor_flip_straddle_audit.stamp_only()` vetoes a straddle
verdict when the producer's q reaches only stamps. Vetoes 0 of 8 inline and
0 of 174 literal candidates — it changes no automated verdict, and fires only
on the producer I misread by hand. That is its whole value.


## mp_yekutieli_sign_block_discrimination — RESOLVED, and it was not a stamp (2026-08-23)

The contradiction (declares proton, carries the muon frozen literal in
`q_80dps`) was the visible edge of a bigger defect.

Committed: `sign_..._ppb_proton = 4807.83`, `..._ppb_muon = 4806.66`. Two pins
11.5 ppb apart cannot give residuals agreeing to the 4th digit. The producer
reads `q_at()`/`q_muon_at()` BY NAME (neither manifest-resolved), so the only
explanation is that `q_at()` itself was muon when the file was written — the
witness predates the 2026-05-28 proton re-pin. **Its cross-anchor comparison
compared one anchor against itself.**

Regenerated: 261.14 (proton) vs 5046.65 (muon) — properly separated.

Survives: the ASSERTION, which tests improvement-vs-bare, not absolute
residual, and passes at 32262.4 / 32262.6 within ±1 ppb. The code comment
already explained why that is the right metric (m_μ over-determination is a
substrate property, PR #1581 Probe A). Scientific claim unchanged.

Does not survive: the VERDICT string — hardcoded, emitted unconditionally,
claiming '54 ppb residual at both anchors'. 54 matches NEITHER the committed
values NOR the fresh ones. Stale inherited prose in both versions. A
`consistent` flag was computed nearby and never wired to it. Now derived.

Manifest: moved `ambiguous` -> `physical_proton` per AGENTS.md constraint 3
(comparison producers reading both accessors by name). Verified inert — 0
non-ephemeral fields move, since ambiguous already fell back to proton.

qou-bdkx triage is now complete: 49 flagged -> 5 REAL -> all 5 resolved
(3 re-bucketed, 1 retracted as stamp-only [aK], 1 regenerated [this]).
