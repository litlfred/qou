---
# qou-q2q7
title: 'Magnus Omega2 option A: adopt the Wenzl y_lambda as the pairing'
status: completed
type: task
priority: normal
created_at: 2026-09-07T11:44:22Z
updated_at: 2026-09-13T09:04:00Z
---

# RECOMMENDED (as headline, with option C kept as a guard)

Make the Wenzl-weighted value the reported `P_total` in all three sign probes.

## Why

- **Cross-A comparability, the decisive argument.** The programme's target claim
  is a *sign change in A*. Sign is scale-invariant so existing gates are safe,
  but any cross-A *magnitude* statement is meaningless under Plancherel, whose
  normalisation drifts 600× between A=2 and A=4. Wenzl fixes `tr(1)=1`.
- **The code would match its own derivation.** The docstrings already call the
  pairing `tr_M` and invoke "Markov trace of a commutator vanishes by
  cyclicity". Adopting Wenzl is a smaller repair than rewriting that derivation.
- **A nucleus is a link.** The Markov trace is the one invariant under
  stabilisation, so the answer depends on the nucleus rather than on the braid
  word chosen to present it.
- **Consistency.** Production `tr_M` uses this weight everywhere else.

## Against, and it is real

Discards the entire ≥3-row sector: 62 % of the A=2 contribution, 70 of 77 shapes
at A=4. Defensible only because the row cap is a corpus-wide commitment already —
if it is wrong it is wrong everywhere, which is `qou-fq0f`'s question, not this
probe's. ⁴He magnitude nearly doubles.

## Work

- [x] Add a Wenzl-weighted `P_total_wenzl` alongside the existing value in all
      three sign probes, and make it the headline.
- [x] Re-run; confirm every sign gate (including the he4→triton cross-atom
      assert) still passes. **2026-09-13.** deuteron 3 s (control 0, P −15.095
      / P_wenzl −6.921); triton a full 30/30 recompute, ~40 min (P +2.4701927,
      P_wenzl −13.930562, control 0); he4 `--gate` PASS — sparse reproduces the
      committed triton datum at rel diff **9.08e-60**, sign +1 both, so the
      cross-atom assert holds.
- [x] Update the docstrings' pairing line to the weight actually used.
      **2026-09-13**, 7 sites, plus 4 more the fix exposed (below).

Option from the decision analysis in [`docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md`](../docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md).
Parent question: `qou-za3q`. Sibling options: `qou-q2q7` (A), `qou-94yt` (B),
`qou-smvw` (C), `qou-ia4w` (D), `qou-gba1` (E).

**Shared measured context** (none of this is fitted):

- `tr(1) = Σ_λ w(λ)·d_λ` — Wenzl gives exactly **1.0** at n = 6, 9, 12;
  Plancherel gives **11.139 / 184.233 / 6751.541**. Plancherel is not a
  normalised trace and its scale grows ~600× from A=2 to A=4.
- Plancherel puts **81.8 %** of its H₆ mass on ≥3-row shapes; the Wenzl row cap
  (level r = 2, `qou-fq0f`) puts **0 %** there. **62.4 %** of the Plancherel
  |contribution| at A=2 comes from shapes Wenzl annihilates.
- 🛑 **CORRECTED 2026-09-13. This block said "the **sign is robust**: P_total
  < 0 under both, on all three atoms". THAT IS FALSE**, and it is the premise
  every option below was weighed against. It was measured on 2026-09-07 from a
  robustness run whose triton and ⁴He sources predated the 2026-09-05 ordering
  ruling (`qou-hu1f`). Regenerated on the canonical borromean word:

      atom      Plancherel      Wenzl (headline)     agree?
      deuteron   -15.095          -6.921              yes
      triton      +2.470         -13.931              NO
      ⁴He        +34.126         -20.466              NO

      Plancherel  -, +, +   one sign change, deuteron -> triton
      Wenzl       -, -, -   no sign change anywhere in A = 2,3,4

  So the two families do not merely disagree on a number: **they disagree on
  whether the programme's target A-dependent sign change is present at all.**
  Per-λ traces are mixed-sign at every A (+4/−5, +14/−14, +33/−42), so the sum
  is a genuine cancellation and the sign was free to move.
- **Magnitude is not robust** either, and not monotone. The figures that stood
  here (triton −108.1 → −60.0, ⁴He −57.8 → −100.8) were the same pre-ruling
  run; the canonical values are in the table above.
- The probes' stated control (`ρ=I ⇒ tr(Ω₂)=0`) holds **blockwise** — every
  per-λ control trace is exactly 0 — so it is weight-blind and provides no
  evidence either way.

🛑 **CORRECTED 2026-09-13.** This read *"No published conclusion depends on the
choice, so this is a correctness-of-object question, not an emergency."* Both
halves are now false. The choice of weight family decides whether the
A-dependent sign change — the programme's target — is exhibited, so a published
sign statement DOES depend on it. Choosing the family because it yields the
wanted sign would be selection against the target (AGENTS.md), which is why the
honest reading is that under the production Markov weight the sign change is
**not** exhibited in A = 2, 3, 4.


---

## 2026-09-07 — implemented

All three sign probes now accumulate `P_wenzl` via
`y_lambda_wenzl_bridge_numeric` alongside the Plancherel `P_total`, and emit
`headline_pairing: "P_total_wenzl"` with the value and its sign.

**`P_total` keeps its name and Plancherel meaning, deliberately.** Gate 2 of the
he4 sparse probe does a NUMERICAL dense-vs-sparse check against the committed
`P_total`, and `he4_magnus_mpfr_probe.py` reads it too — silently re-meaning the
field would compare a Wenzl-weighted sparse value against a Plancherel-weighted
committed one and break a real check. Adding the truth rather than re-meaning an
existing key is the same fix this arc used for the `y_lambda` column and the
missing `scriptFile`. A hard rename stays available, but must migrate those
numerical checks in lockstep.

Deuteron regenerated and verified: `P_total_wenzl = -6.9212506529727351`,
matching the independent offline re-weighting exactly; control assertion still
passes. Triton and he4 are slow (>10 min and worse) and pick up the fields on
their next run — no arithmetic changed, only what is additionally recorded.

Remaining on this bean: re-run triton and he4 so their witnesses carry the
headline fields, and confirm the cross-atom sign gate still passes end to end.

### Runtime reality for the remaining two

`triton_magnus_omega2_sign_probe.py` was given **2400 s and still timed out**
(exit 124); `he4_magnus_omega2_sign_sparse_probe.py` is slower again. Neither
wrote, so their witnesses still carry only the Plancherel arm while their
sources carry the implementation.

This is not a blocker for the result: the Wenzl values for all three atoms are
already committed, measured independently, in
`magnus-omega2-weight-family-robustness.witness.json` — deuteron −6.921, triton
−59.991, ⁴He −100.827. What is missing is only that those numbers travel inside
each probe's own witness.

Whoever picks this up should run the two with a multi-hour budget rather than a
session's tail — or, better, profile them first: a 40-minute H₉ probe is itself
worth a look, and `qou-4383` independently found `atomic_tr_m_helium4.py` and
`binding_combiner_markov_peel_fallback.py` exceeding 1200 s, so slow producers
in this tree are a pattern rather than a one-off.

## CLOSED 2026-09-13 — a948fb50789

Both remaining items done. The pairing line was the visible half; fixing it
turned up four more sites and one wrong gate.

### The seven sites, and the four the fix exposed

The 7 named in this bean now name both arms and the declared headline.
Correcting them surfaced:

- **`weight_family_note`, three copies**, all asserting the Wenzl re-weighting
  "leaves the sign of P_total unchanged". True at A=2, **false at A=3 and A=4**
  — written when the first robustness run reported all-atoms robustness off a
  pre-ruling triton source. Now ONE shared module,
  `computations/deltalambda/magnus_weight_family_note.py`, whose per-atom
  agree/disagree clause is **computed from the run**. Three copies of a claim
  is how two of them stay wrong.
- **The same sentence again** in the tail of `wedderburn_weight`'s docstring in
  all three probes ("what IS settled is that … the sign of P_total … does not
  depend on the choice").
- **The triton verdict**: *"SIGN FLIP CONFIRMED — the y-weighted 2nd-order
  Magnus pairing REVERSES sign"*. The whole headline finding, stated on the arm
  that is **not** the declared headline. It now says which arm and carries the
  other's answer beside it, both computed:

      P_total(A=3)       = +2.4701927   (+1)  [Plancherel]
      P_total_wenzl(A=3) = -13.930562   (-1)  [HEADLINE]
      sign_flip = True (Plancherel) / False (Wenzl)

- **The ⁴He sign-vs-A map** and the deuteron's *"(iii) the y_λ-weighted total"*,
  same treatment.

New witness keys: `sign_flip_vs_A2_wenzl`, `A2_P_total_wenzl_sign`,
`sign_vs_A_map_wenzl`, `sign_vs_A_maps_agree`. The legacy `P_total` and
`sign_flip_vs_A2` keep their Plancherel meaning **deliberately** —
`he4_magnus_mpfr_probe.py` and the sparse probe's gate 2 both do a numerical
cross-check against the committed `P_total`, so re-meaning it silently would
break a real check.

### The robustness probe asserted its own hypothesis

`sign_robust_to_weight_family` was `computed=0, expected=1` — permanently
failing, `allPassed: false`, while the file's own docstring recorded
non-robustness as **the finding**. A gate that fails identically whether the
science is fine or the inputs are stale carries no signal, and a standing red
is a gate someone eventually silences. It now asserts the preconditions (every
source post-ruling; all three atoms actually read — a missing source `continue`s
and would otherwise have left 2 disagreements looking clean) and **locks the
measured outcome** at 2 disagreeing atoms. Strictly more sensitive than what it
replaced, which could not tell 2 disagreeing atoms from 3. Exit 0, 3/3 passed.

### Three stale figures fixed in passing

- The deuteron scope line's *"Does NOT test the 'positive at A≥3' half (needs
  H₉)"* — H₉ and H₁₂ both exist now, and the answer is weight-dependent.
- §2.3 of the analysis doc: *"robust at A=2 and not at A=3"* → **"or A=4"**. The
  body's SETTLED banner already had it right; the heading is what a reader scans.
- `content/…/lean/QOU/MassTheory/MagnusPairingSignStructure.lean` cited the
  per-partition split as "2 positive, 7 negative" — the **pre-ruling** figure.
  Measures 4+/5-/2 zero on the canonical borromean word. Only the count moved:
  sign-indefiniteness holds under both words and under either weight family,
  since it is a statement about a commutator's trace pairing. Type-checks at
  0 errors.

### Runtime — the note in "Runtime reality for the remaining two" is now wrong

That section says triton timed out at 2400 s and he4 is "slower again". Both
were fixed by siblings before this session; triton completed **twice** here at
~40 min, and its witness now carries the headline arm. Two things worth knowing:

- **The cache stamp hashes the whole source file** (deliberately — `qou-z3q9`),
  so *every* edit to the triton probe, comment-only included, costs a full
  30/30 recompute. Batch edits before re-running.
- **The sparse route is ~87× faster on the same H₉ sweep**: `he4 --gate` does
  all 30 partitions in **27.5 s** against the dense probe's ~40 min, exact to
  9.08e-60. The dense triton probe is a slow producer with a drop-in
  replacement already in the tree. Worth a bean under `qou-4383`; not opened
  here because it is a performance change, not this bean's correctness one.

### ⁴He is NOT regenerated

Its source is corrected, so the next run emits the two-arm verdict. The
**committed** witness still carries the Plancherel-only one. Regenerating is an
8-hour run and was not attempted.
