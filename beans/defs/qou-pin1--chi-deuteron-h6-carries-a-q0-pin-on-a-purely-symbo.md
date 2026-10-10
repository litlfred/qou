---
# qou-pin1
title: 'chi-deuteron-h6 carries a q0 pin on a purely SYMBOLIC artifact (declared muon, recorded proton)'
status: completed
type: task
priority: normal
created_at: 2026-08-08T19:00:00Z
updated_at: 2026-08-08T19:35:00Z
---

Surfaced by the new `computations/audits/q0_declared_vs_recorded_sweep.py`
(PR #4788) — the only DECL_MISMATCH among 310 checkable witnesses.

**The contradiction.** `computations/chi-deuteron-h6.witness.json` records
`q0Anchor: "proton"` (with the proton 50-digit value), while its producer
`per_irrep_pole_deuteron_h6.py` is listed under `ideal_muon` in
`computations/q0_anchor_manifest.json`.

**Why neither label is obviously right.** The producer appears to be purely
SYMBOLIC: its only `.subs()` calls are symbol→symbol (`other_q → q_sym`,
`q_var → u_var**2`), it does not import `q_parameter`, and the witness carries
`chi_lambda_symbolic` with an empty `data` block. If that reading holds there is
no numeric q₀ anywhere in the artifact, so **both** the `proton` stamp and the
`ideal_muon` declaration are asserting a pin that does not exist. The honest
classification would be `ambiguous` (or no pin at all), not a choice between the
two.

**Deliberately NOT resolved here.** Reclassifying another agent's producer in a
shared registry on the strength of a grep is exactly the kind of unilateral
edit the coordination rules discourage, and the sweep that found it was written
in the same session — an independent read is worth more than my own second look.

**Next step for whoever picks this up.** Confirm the producer never evaluates at
a numeric q₀ (check `hoefsmit_symbolic`, `canonical_braid_crossings`, and the
cached `y-lambda-wenzl-bridge-symbolic-witness.json` it loads). If confirmed:
move the stem to `ambiguous` in the manifest and drop the spurious `q0Anchor` /
`q0Value` from the witness. If it *does* evaluate somewhere, fix whichever of
the two labels is wrong and say which.

**Note on the detector.** This class is invisible to
`q0_anchor_consistency_audit.py`, which checks the stamp against ITSELF (label
must match value) and reports `Q0_FLIP: 0` corpus-wide. The same blind spot hid
a live 30.4 ppb mislabel on `qbeta-ck-cache` until 2026-08-08. See
`docs/audits/2026-08-08-q0-declared-vs-recorded-sweep.md`.


## RESOLVED 2026-08-08 (branch claude/q0-pin-coverage-2026-08-08)

Chain traced -- canonical_braid_crossings, hoefsmit_symbolic,
per_irrep_pole_proton_h3 -- and it IS purely symbolic. Module-level
`Q = sp.symbols('q', positive=True)`; the single numeric import
(`from q_parameter import Q as q_num`) sits inside hoefsmit_symbolic's
`if __name__ == "__main__"` self-test, unreachable from any import path.

So neither label was meaningful, as suspected. Stem moved ideal_muon ->
ambiguous; spurious q0Anchor/q0Value dropped from chi-deuteron-h6.witness.json.
DECL_MISMATCH is now 0.

Caveat worth carrying: removing a stem from ideal_muon is a LIVE RE-PIN
(q_parameter reads the manifest by stem), inert here only because this producer
never imports q_parameter outside its self-test. The check was the precondition,
not a formality. Audit: docs/audits/2026-08-08-q0-pin-coverage-and-the-manifest-
is-config.md
