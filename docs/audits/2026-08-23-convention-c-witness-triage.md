# Convention-C witness triage (2026-08-23)

Answers *"any other uses of C convention that need to migrate to D?"*.
Bean `qou-z11r`; PR #5510.

**The source migration is essentially done; the committed outputs are not.**

| | count |
|---|---|
| `scripts/convention-c-producer-audit.py` actionable **source** sites | 1 |
| witnesses carrying `z_C = 0.4993203340...` | 58 |
| witnesses carrying `z_D = 0.6126880505...` | 4 |

Measured by the method AGENTS.md prescribes for this class — **test the answer,
not the source**. Thirteen source spellings are detector-blind
([detector-blindness taxonomy](2026-08-15-detector-blindness-taxonomy.md)); the
C *value* cannot hide in a committed witness.

## Classification

| class | n | meaning |
|---|---|---|
| `z-parameter-echo` | 40 | C appears **only** in `z`/`markov`-named fields — the witness recording which `z` it used |
| `payload-or-mixed` | 16 | C appears in a **computed** field (Gram entries, `tr_M`, traces) — convention C is baked into a mathematical result |
| `LIVE-C-PRODUCER` | 2 | the producer **computes** `√q/(q+1)` in current source |

Per-witness rows, with the exact JSON paths carrying the C value, are in the
[JSON twin](2026-08-23-convention-c-witness-triage.json).

## The two live-C producers

- `hecke-channel-binding.witness.json`  ←  `computations/probes/hecke_channel_binding_probe.py`
- `signed-crossing-feasibility.witness.json`  ←  `computations/probes/signed_crossing_feasibility_probe.py`

Both hardcode a **muon** `Q0` literal as well, and
`signed_crossing_feasibility_probe` additionally types `delta = 0.00137705`
instead of deriving it. So they are off-canon on three axes at once:
convention C, the muon pin, and a typed colour split.

### A durable refutation rests on this

`signed_crossing_feasibility_probe` emits
`"verdict": "signed-ILP-pure-chirality-refuted"`. That refutation was computed
with convention-C `z` at a muon-pinned `Q0`, and **has not been re-derived
under D**. Treat it as **C-conditional**, exactly as AGENTS.md requires of the
Q_β `c_k` ladder. It is not re-derived here, because
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` establishes that substituting
`z_D` into a C-frame result is not a valid move — a re-derivation is required,
not a swap. That is research, not cleanup.

## The 16 payload cases

These are the ones that carry mathematical weight — a Gram-matrix entry equal
to `z_C` means the Gram matrix was built in convention C:

- `producer-importability-audit.witness.json` — 1 field(s), e.g. `.description`
- `borromean-axial-coupling.witness.json` — 4 field(s), e.g. `.data.gram_matrix[0][1]`
- `chirality-topology-binding.witness.json` — 1 field(s), e.g. `.channel_values_at_q0.pp.std`
- `closed-form-tau-M-verification-phase5q.witness.json` — 1 field(s), e.g. `.data.per_atom_results[0].interface_ratio`
- `confinement-operator-selection.witness.json` — 5 field(s), e.g. `.parameters.z`
- `electron-m_e-derivation.witness.json` — 1 field(s), e.g. `.data.electron.t1_descended.value_50dps`
- `qbeta-h4-stagec-markov-infra.witness.json` — 1 field(s), e.g. `.data.trM_H4_generator`
- `inter-knot-decoupling.witness.json` — 2 field(s), e.g. `.data.z_markov_norm`
- `lepton-tower-probe-1-cinquefoil-muon.witness.json` — 5 field(s), e.g. `.constants.z_markov`
- `probe-9b-alphak-structure.witness.json` — 2 field(s), e.g. `.data.part_2a_numeric.trM_by_word.T1`
- `casimir-phi-q-markov-probe.witness.json` — 2 field(s), e.g. `.data.markov_parameters.z_M_v1`
- `frobenius-gram-matrix-probe.witness.json` — 5 field(s), e.g. `.parameters.z_at_q0`
- `q-hecke-seminormal-character-closure-probe.witness.json` — 2 field(s), e.g. `.data.per_test_results[1].lhs_partition_sum`
- `qbeta-klr-composite4-preflight-run.witness.json` — 2 field(s), e.g. `.data.anchors[0].tr_M_p2_JW_sym`
- `qbeta-symbolic-sdp-strict-complementarity.witness.json` — 2 field(s), e.g. `.data.t_at_q0[1]`
- `toffoli-lp-stability.witness.json` — 4 field(s), e.g. `.gram_matrix_at_q0[0][1]`

One of these, `producer-importability-audit`, is a **false positive**: its only
hit is in a `.description` string, not a value.

## Pin split

The C witnesses are split across **both** q₀ pins, so migrating convention is
not separable from the pin question:

- p50: 28
- muon: 23
- other: 3
- other+p50: 2
- muon+p50: 2

(`p50` = the 50-digit value `...40335612`; `muon` = `...40335982`.)

## What is NOT claimed

- **This is not a work order.** Nothing here is mass-regenerated. Only one
  witness in the corpus has been confirmed end-to-end as a stale output of an
  already-migrated producer (`terms-2-3-atom-per-gen-mpfr-50dps`, refreshed in
  PR #5510 and verified against unmodified `main`).
- **15 of 58 have no locatable producer** by output-filename
  reference, so they cannot be re-run to decide anything.
- **Re-running is the wrong instrument here**, and two of my own sweeps proved
  it. A file-level substring test cannot tell a flipped field from an untouched
  one when a witness legitimately holds both values; and a producer that exits 0
  in 0 s without rewriting its witness reads identically to one that re-emitted
  C. The classification above is therefore **static** — it reads what the
  witnesses and sources say, and does not infer from a re-run.

---

**Counts re-verified after rebasing onto `main` (148 commits).** `C = 58` is
unchanged; `D` moved `5 → 4` during that window, and the table above records
the post-rebase figure. Re-measure before acting on either number — this is the
same decay that makes a hand-kept count untrustworthy elsewhere in the corpus:

    grep -rl "0\.4993203340" --include=*.witness.json computations/ qou-mass/ | grep -v _deprecated | wc -l
