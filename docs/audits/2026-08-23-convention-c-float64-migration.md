# Migrating off convention C and float64 — four sites, and a refutation that does not survive

**Date:** 2026-08-23
**Beans:** `qou-z11r` (the C triage), `qou-iph3` (the mass-table regeneration that preceded this)
**Follows:** the 25-atom regeneration (#5526, `cde2fbcd89`) and the two-triage reconciliation (#5543)

## What moved

| site | was | now |
|---|---|---|
| `mass-from-q-symbolic.py:314,424` | `1.0/(Q0**0.5 + Q_INV0**0.5)` — C **and** float64, serialised into a witness | `markov_z(Q_MP)` |
| `probes/hecke_channel_binding_probe.py:56` | `mp.sqrt(Q0)/(Q0+1)` — C, muon literal pin | `markov_z(Q0)`, proton pin |
| `probes/signed_crossing_feasibility_probe.py:59` | same, plus a durable `refuted` verdict | same |
| `q_pinning_50_digit.py:115` | `mpf(1)/(sqrt(Q) + sqrt(Q_INV))` — C, **anchor-witness producer** | `Q**3/(Q**2+1)` |

Every fix calls the canonical helper `closed_form_tau_M.markov_z` rather than
re-spelling `z` inline. That is the point, not a stylistic preference: every
convention detector in this repo keys on **how `z` is written**, so a private
inline spelling is exactly how a site goes blind — which is how three of these
four survived two independent sweeps.

Live-C producers found by the triage detector afterwards: **0**.

## The fourth blind spelling

`q_pinning_50_digit.py` writes `1/(√q + √(1/q))` as

```python
Z_MARKOV = mpf(1) / (sqrt(Q) + sqrt(Q_INV))
```

Both detectors keyed on `sqrt(x) + 1/sqrt(x)`. This binds the reciprocal to a
separate `Q_INV` name and takes its square root, so neither pattern matched.
Found by reading, not by scanning. The detector now carries a pattern for it.

**Its witness is deliberately NOT regenerated.** `q-pinning-50-digit.witness.json`
is anchor-*defining* — AGENTS.md rule 1, it is what `_q0_value_for_anchor` reads,
and re-pinning it redefines what "muon" means corpus-wide (262 `Q0_FLIP`s,
measured). `Z_MARKOV` there is a leaf: one print, one witness field, nothing
computes with it, and grep for `["z_markov"]` / `.get("z_markov"` across live
`.py` returns **zero reads**. So the committed field stays C until someone
regenerates that witness with the anchor context intact. Source is canon; the
field is a known-inert provenance defect.

## The finding that matters: a durable refutation does not survive canon

`signed_crossing_feasibility_probe` emitted
`"verdict": "signed-ILP-pure-chirality-refuted"`, and
[`2026-06-17-signed-crossing-binding-refutation.md`](2026-06-17-signed-crossing-binding-refutation.md)
recorded it as a refutation. Its kernel line says `z=√q/(q+1)` outright — the
whole result was **convention C**.

Re-run under canonical D at the proton pin, it flips:

| atom | miss under C | miss under D | ≤5 % under D |
|---|---|---|---|
| D | 74.9 % | 27.4 % | ✗ |
| T | 39.0 % | 11.6 % | ✗ |
| ³He | 36.9 % | **0.013 %** | **✓** |
| ⁴He | 16.4 % | 39.3 % | ✗ |

`n_close_pure_chirality_of_4`: **0 → 1**. The verdict field itself changes to
`signed-ILP-pure-chirality-partial`.

The landed `qou-z11r` triage was right to flag this as C-conditional. It is
stronger than conditional: **as stated, it is false under the canonical
convention.**

### What is and is not claimed

- **Retracted:** the word *refuted*, and the 0/4 that carried it. The C-frame
  table is kept as a record of what C gives.
- **Still holds, scope-(a):** the construction *alone* does not reproduce the
  binding — three of four still miss by 12–39 %, which is not a closure.
- **NOT claimed:** that ³He at 0.013 % shows the construction works. One
  near-match among four, with the others missing by an order of magnitude more,
  is the shape a coincidence takes. It is a lead to probe, not a result. Do not
  wire it.

This is the mirror of the AGENTS.md refutation discipline: a scope-(b)-sounding
"refuted" that rested on a non-canonical convention has to be re-scoped when the
convention is corrected, not quietly carried forward.

## A pre-existing crash, found by trying to verify

`mass-from-q-symbolic.py` **could not run to completion on `main`**:

```
File "computations/mass-from-q-symbolic.py", line 366
    print(f"    m_n/m_p CODATA ≈ {codata_ratio_n_p:.10f}")
TypeError: unsupported format string passed to mpf.__format__
```

Both CODATA masses are `mpmath.mpf`, so the ratio is `mpf`, and `mpf.__format__`
rejects a float format spec. It aborted **before the witness write**, which is
why that witness was stale. Verified pre-existing by running `main`'s unmodified
copy — same line, same error.

Fixed with `mp.nstr` (display-only). The producer now exits 0 and reaches its
witness for the first time in however long. Noted because it is the reason the
convention fix here could not have been verified end-to-end without it — and
because a producer that crashes before writing looks identical, from the
witness, to one that was simply never re-run.

## A false positive of my own, and the fix

After migrating `mass-from-q-symbolic.py`, the triage detector reported it as a
**live-C producer** — matching the C spelling inside the comment that documents
what the line used to be. That is the most confusing possible false positive: it
sends the next agent to re-migrate code that is already correct.

The detector now blanks `COMMENT` tokens before scanning (`_strip_comments`,
tokenise rather than regex-strip, so a `#` inside a string literal is not
mistaken for a comment). Quarantine-marker detection still reads the original
text, since those markers live in comments by design.

## Verification

- `scripts/precision-gates.sh --changed` → **all blocking gates green, EXIT=0**.
- raw-float64 ratchet: `dirty_witnesses` 1406 → **1395**, `total_fields`
  487450 → **487396**. 0 NEW, 0 REGRESSED.
- `q0-anchor-consistency-audit`: `Q0_ANCHOR_MISSING` 1897 → **1881**,
  `Q0_OK` 698 → **701** — the three migrated witnesses now declare their anchor.
- Triage detector: **0** live-C producers remaining.
- All three producers re-run to exit 0; `clarabel`, `numpy` and `scipy` were
  installed at the recorded versions first, so no environment block was
  weakened.

## A fifth site that must NOT be migrated — and a third class the triage lacked

Walking the import cones of the 28 `unresolved` witnesses turned up one
C-supplying dependency: `computations/qbeta/qbeta_utils.py:173`.

**Do not fix it.** It is the Q_β `c_k` ladder, and it is convention C *on
purpose*: the registry records `channels.qbeta-decay` as
`agreed-migration-pending` — convention settled to D, code deliberately not
moved, because `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` makes the C-frame
ladder and the mass channel's three-row forcing mutually exclusive. Substituting
`z_D` is not a valid move; the ladder must be **re-derived** (`qou-cds1`), which
is research, not cleanup.

Two real hazards were sitting there anyway:

**1. The protective docstring did not cover the site.** `markov_parameter` (line
47) carries the full "deliberately still C / deliberately not migrated" note.
Line 173 is a **second, independent inline spelling** of the same value inside
`substrate_ladder_quantities`, with no such note — so a reader arriving at that
function alone sees a bare C `z` and a standing instruction to migrate C to D.
The note is now restated at the site.

**2. The obvious tidy-up would have changed the number.** Replacing the inline
spelling with a call to `markov_parameter(q)` looks like pure hygiene — one
documented site instead of two. It is not: the two spellings are algebraically
equal but **not bit-equal**.

```
1/(√q + 1/√q)  vs  √q/(1+q)      relative difference 1.6e-61 at 60 dps
```

Tiny, and irrelevant almost anywhere else — but this is the one ladder that must
not be perturbed by a substitution, so the refactor was **declined** and the
reason recorded at the site. Verified afterwards that `substrate_ladder_quantities`
returns the identical `z`.

**The triage detector lacked this class entirely.** It knew "historical" and
"comparison-only"; it did not know *"settled to D, deliberately not yet moved,
because moving it needs a re-derivation."* Without that, it reports the ladder as
a live-C producer and the next agent migrates the one thing that must not be
z-swapped. `agreed-migration-pending` / `deliberately not migrated` /
`must be re-derived` are now quarantine markers.

## Still open

- **28 `unresolved` C witnesses.** The import-cone walk (depth 2, local modules
  only) found exactly **one** C-supplying dependency across all of them —
  `qbeta_utils`, the deliberate ladder above — and it accounts for only 1 of the
  28. So the import-cone hypothesis is **not** the whole explanation, and the
  other 27 remain genuinely unexplained: byte-identical producer, no C spelling
  in it, no C-supplying local import within two hops. Candidates not yet
  eliminated: a deeper cone, a non-local dependency (`pyhecke`, `qou_substrate`),
  or a committed witness older than a producer edit that left the hash
  coincidentally unchanged. Stating this as open rather than closing it on the
  one hit that fit.
- **15 `stale-output`** witnesses: mechanical re-runs, individually.
- **The typed `delta`** in `signed_crossing_feasibility_probe`
  (`mp.mpf("0.00137705")`) is still hand-entered rather than derived, and both
  probes still hardcode the bond shifts inline instead of calling
  `d_for_ctype` — whose own docstring names such private lookups as how the
  colour-weighted interface got lost. Separate axis (`qou-cds4`), not touched.
