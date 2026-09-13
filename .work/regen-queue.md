# Regeneration queue — rewritten 2026-09-13 after the 702-commit merge

The previous contents are obsolete. Main's `qou-sv7h` arc made the kernel
EXACT — the accumulator had been multiplying 167-bit inputs at ambient dps 15
and the log layer was float64 on top — so **everything downstream of
`hecke_core_legacy` computed before this merge is superseded by construction**,
not merely stale. That is a much wider statement than the old queue's, and it
replaces it.

## 1. The nuclide table — RUNNING

`hadron-knot-table.witness.json` completed 19/19 on 2026-09-07 and is committed
(`ee2c9c278f2`), but under the PRE-sv7h kernel. Re-running now from zero; the
old checkpoint was deleted rather than re-stamped.

**That is the opposite call from 2026-09-07, and deliberately so.** That merge
changed a key file by a pure RENAME, so the cached atoms were provably still
valid and re-stamping was right. This one changes the arithmetic, so the cache
is wrong and discarding is right. The key did its job both times; what differs
is what the diff said.

Early signal: proton / neutron / protium reproduce byte-identically
(0.629328 / 0.475134 / 1.146338), as expected — sv7h bites on the
accumulation, so divergence should appear at compounds, not at A=1.

Cheaper than the 7 h it took last time: main replaced the factorial SYT
enumeration with an exact closed form (`qou-r4w5`), and the witness now
checkpoints per atom, so a killed container publishes the rows it reached.

## 2. `qou-3uvs` — re-confirm, but the conclusion should hold

The si28 / ca40 / fe56 Frobenius verdicts (all FAIL) came from the old kernel.
They need re-confirming from this run. The conclusion is expected to survive:
the violations are **10 %–84 % of the scale** and ~1e9 x the tolerance, and
sv7h moves values at ~1e-15. Nothing at that size flips a verdict at that
margin — but it should be read off the new witness, not assumed.

## 3. The kernel memo — DELETED, re-port only with a wider key

38 MB discarded, not ported. `_memo_build_id()` hashed ONLY the compiled
native module, and sv7h is a **Python** change, so the old cache would have
been served unchanged against a numeric path that had moved — a stale-value
failure, which is worse than no cache.

Re-port it against a key that hashes the Python numeric path too. Main already
uses that idiom: `he4_magnus_omega2_sign_sparse_probe.py` stamps
`_ck_src = sha256(open(__file__,'rb').read())` into every cached row and drops
rows that do not match. Same fix as the `_ckpt_key` widening.

`scripts/hkt-resume.sh` still sets `QOU_KERNEL_MEMO`; it is inert and says so.

## 4. Everything else — RE-CHECK against the merged tree first

The old queue's entries were measured before 702 commits landed. Do not act on
them as written. In particular main independently fixed several things this
branch was carrying:

* the `mp.mpf(repr(<mpf>))` trap (`qou-gxsd`) in at least three more places,
  and better — dividing directly rather than round-tripping through a string;
* the witness truncation window, by building the payload BEFORE `open(...,"w")`
  rather than by writing to a sibling temp (`qou-m549`; this file had been
  committed to main at **0 bytes**);
* `scriptFile` in `stamp_staleness_metadata` (`qou-4383`).

Re-measure before re-doing.

## 5. `qou-qe81`'s two stale error-row witnesses — RE-RUN ONLY, no code owed

Re-measured 2026-09-13; neither needs a producer fix any more.

* `computations/sweeps/paper_six_term_isotope_sweep.py` — returns EMPTY rather
  than raising (fixed on this branch); its committed witness still carries 8
  `FileNotFoundError` rows.
* `computations/term6_residues_at_roots.py` — its 4 rows were
  `LaurentQ.from_sympy: non-Laurent factor`, on an expression that IS Laurent
  (`-q²/12 + q/6 + 5/12 + q⁻²/12 − q⁻³/6 + q⁻⁴/12`). **Main fixed the parser**
  under `qou-ls7l` with an expand-and-retry; verified here against the exact
  failing input.

Both still serialise `allPassed: true` over exception text because they
predate the error-row gate. Re-running is what makes that verdict visible.

## 6. `qou-85wn` leftovers — `probe_he4_canonical_tr_m_fingerprint.py` — RE-RUN ONLY

Producer prose fixed 2026-09-13; the witness still carries the old
`description` until it is re-run. **No code owed beyond the prose edit** — no
computed value, assertion or tolerance was touched.

`qou-85wn` (a sibling session's bean, still `todo`) regenerated the `.md`
table, the `.ts` title and docstring, `CITED_PCT`/`CITED_TR_M`, and the
producer's two `[cited …]` print literals against the 2026-09-06 chi
regeneration. It missed four prose sites **inside the producer**, which is why
the witness's own `description` still read `tr_M = 0.160974145442` against data
of `0.0112374176598` — a factor R_quark = 14.3248, with two blocks sign-flipped
and the trivial rep going 5.96 % → 85.398 %, i.e. from near-nothing to leading
the ranking.

Fixed: the module docstring's "Cited values" block and its "86.6 %" note,
`w.set_description(...)`, and the `source=` strings on the `tr_M_at_q0` and
`trivial_rep_pct` assertions. Superseded figures kept and dated, per 85wn's own
convention — the gap is the evidence, and overwriting it would have destroyed
the only record that the producer's prose and its pinned constants had parted.

Cheap: reads one upstream cache and sums 77 partitions of 12. Queued rather
than run only because the `qou-uiut` table holds the checkout and two producers
must never run concurrently here.

## 7. `h2o_bond_angle_magnitude_vsepr.py` — RE-RUN ONLY, prose fixed 2026-09-13

Producer said `θ ≈ 107.2°` / `narrows ≈ 2.3°` in both its docstring and its
`set_description`, while computing `theta_pred_coulomb_n1_deg = 106.70642` and
`narrowing_pred_n1_deg = 2.764776`. The witness's **own `finding` field** already
carried the right numbers (`≈106.71°`, `≈2.8°`), so the document contradicted
itself in two prose fields at once — the exact shape `qou-n62l` was opened on.
No computed value touched. Fast probe; queued only because the table holds the
checkout.

## 8. Two `--pairs` drifts — RE-RUN ONLY, prose fixed 2026-09-13

Both found by the new advisory `--pairs` detector (`qou-n62l`), which compares a
prose number only against the field its own sentence names.

* `computations/binding_via_interface_knot.py` — `q_0 ≈ 1.1097` in three places
  (docstring ×2, `set_description`) against q₀ = 1.1099785827513808. Wrong in
  its own 4th decimal: 1.10998 rounds to 1.1100, never 1.1097. Now 1.10998.
* `computations/probes/binding_lp_with_inter_nucleon_bonds_probe.py` —
  `L_nn = 0.907262271178` against data of `0.907262265533`, a 5.6e-9 gap which
  is exactly the y-table precision this probe's own docstring names; and the
  mirror ratio read `1.17022` against `1.170237`. **The description is now
  INTERPOLATED** from the same variables the matching `add_data` calls
  serialise, so it cannot drift again. Eight of its ten hardcoded figures were
  still correct roundings — which is the trap: a description that is mostly
  right reads as maintained.
