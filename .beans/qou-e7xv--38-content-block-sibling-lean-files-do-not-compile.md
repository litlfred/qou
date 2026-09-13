---
# qou-e7xv
title: 38 content-block sibling .lean files do not compile — nothing in the corpus checks them
status: completed
type: task
priority: normal
created_at: 2026-09-03T22:46:23Z
updated_at: 2026-09-13T18:05:00Z
---

Audit: `docs/audits/2026-09-03-sibling-lean-compile-sweep.md`
Data:  `docs/audits/2026-09-03-sibling-lean-compile-sweep.tsv`

## Measured 2026-09-03

`lean`-direct on all 908 `.lean` under `content/quantum-observable-universe/`
outside `lean/`, then EVERY failure re-verified under a widened LEAN_PATH:

    raw failures                                        41
      harness: QOU-only LEAN_PATH, file imports UGB     -1
      harness: `import Mathlib` (aggregator olean absent) -2
    REAL                                                38   (4.2 %)

Both harness classes confirmed by re-running, not by inspection.
`vertex-algebra-relations.lean`: `unknown module prefix 'UGB'` under a
QOU-only path, exit 0 with all three paper packages. `Mathlib.olean` is
genuinely absent from the restore, so two files that `import Mathlib`
wholesale fail for a reason a real `lake build` would not have.

## Why nothing caught them

Siblings sit outside the Lake globs (`globs = ["QOU", "QOU.+"]`,
`srcDir = "."` = the `lean/` dir), so `lake build QOU` never sees them; CI is
`workflow_dispatch`-only; `lean-content-siblings.yml` gates content-block
siblings, not these.

## Largest shared causes

- `Inv GroundRing.R_q` fails to synthesise in **5 files** — ONE missing
  instance on the corpus's own ground ring, not five independent defects.
  Highest-leverage single fix in the list.
- 4 files fail at the PARSER.
- Mathlib drift: `Real.tendsto_log_mul_rpow_nhdsGT_zero`,
  `MonoidalCategory.whiskerRight_comp` -> `comp_whiskerRight`.
- `delta-max-uniform-bound.lean` imports `QOU.MassEndomorphism.JetTower`,
  which does not exist in source, and `QOU.BraidsAndKnots.MarkovTrace` where
  the tree spells the namespace `BraidKnot`. Absent olean AND absent source
  is what distinguishes this from a harness gap.
- Worst single file: `spin-involution-lp-dual-invariance.lean`, 24 errors.

## Scope

A sibling failing to compile is NOT automatically a false claim — most are
stale references and missing instances, not wrong mathematics. It means the
block's `lean.ref` points into a file that does not typecheck, so the
formalisation cannot be relied on as stated. Triage per file; do not read 38
as 38 refuted propositions.

## Already partly done on this branch

- `n-v-bring-action.lean` — was 8 parse errors (`Σ` used as a binder name);
  now exit 0, zero warnings, and its axiom + self-discharging instance removed.
- `braid-action-tensor.lean` — 5 errors -> 2 (bean `qou-8qby`).


## 🛑 CORRECTION (same day): the `Inv GroundRing.R_q` diagnosis above is WRONG

This bean and the audit first called the 5-file `Inv GroundRing.R_q` failure
"ONE missing instance on the corpus's own ground ring, not five independent
defects" and named it the highest-leverage single fix. **Retracted. Adding an
`Inv` instance is exactly what must not happen.**

`lean/QOU/GroundRingCore.lean` says so in its own docstring, on
`q_inv_param`:

  "Carried as its own declaration rather than written `q_param⁻¹`: `R_q` is a
   ring, not a field, so it has no `Inv` instance and `q⁻¹` cannot be written."

The absence is deliberate. An `Inv` instance on a non-field makes `x⁻¹`
elaborate to a junk value for every non-unit, so it would convert five
compile errors into five silently wrong formulas. Strictly worse than the
current state.

The real defect is at the five call sites, which write `(sp.field p)⁻¹` — the
inverse of an ARBITRARY ring element. In ℤ[q,q⁻¹] the indeterminate has an
inverse (`q_inv_param = T (-1)`); a general element does not. Each site needs
either `q_inv_param`, or an explicit inverse field carrying `q * q_inv = 1`
(the pattern used by `alternating_projection_weak_vertex`). That is a
per-site mathematical decision, not one-line infra.

Sites: information-theory/quantum-volume.lean,
quantum-observable-universes/{q-connection,q-ext-deriv,quantum-planck-constant,q-lie-bracket}.lean

Worth noting WHY the wrong fix was attractive: the "five files, one root
cause" framing. A shared error message is not a shared defect.


## UPDATE 2026-09-04: 38 -> 27, and the dominant cause is now clear

It is NOT Mathlib drift and NOT bad mathematics. **Migrations stop at the
sibling boundary.** A library object changes shape; every consumer inside the
Lake globs is updated because `lake build` forces it; the content-block
siblings are left behind because nothing builds them.

    SubstrateParameter split (categorical R_q / ArchimedeanSubstrateField ℝ)   6 files
    theorem specialised generic `Field R` -> ℝ, ascription left as `(q : R)`   1
    HeckeExpansion gained `(R : Type*) [Field R]` before `n`                   1
    HasPentagonRelation / HasBlochGroup given real fields instead of True-ish  1

That is 9 of the 11 repaired so far. The other two were a Lean-notation token
used as a binder name (`Σ`, `λ`) and orphaned docstrings.

CONSEQUENCE: a mechanically-enforced migration is NOT enforced here. Anyone
changing a library signature must grep `content/<paper>/**/*.lean` outside
`lean/` as a separate step — the compiler will not ask.

The Bloch-group case is the sharpest: the stranded sibling was WRONG, not
merely stale. It carried an instance with every field `:= trivial`, and the
library's strengthening (real `AddSubgroup` / `→+ ℝ` / torsion fields, its
docstrings saying "not a `True` placeholder") is exactly what stopped it
typechecking. The compile error was the guard working, and the fix was
deletion — supplying `⊥` and the zero hom would typecheck and assert nothing.

Fixed to ZERO errors and ZERO warnings so far (11):
  n-v-bring-action, quantum-volume, q-connection, q-ext-deriv,
  quantum-planck-constant, q-lie-bracket, substrate-parameter-exists,
  confinement-phase-stratification, gram-determinant-plancherel-ratio,
  flavor-mass-splitting-bound, bloch-group-quotient-construction,
  knot-factor-shell-closed

Improved but still failing (2): braid-action-tensor 5->2 (`qou-8qby`),
townsend-biot-savart-strain 9->7 (real-analysis proof drift, not names).

Re-verified against main after merging its 39 commits: those were library-side
and fixed none of the siblings.


## 2026-09-04 — 38 → 12

26 of the 38 now at **0 errors and 0 warnings**, re-measured lean-direct.

Fixed this pass (PR #6540): `delta-max-uniform-bound` (deleted — `: sorry
:= sorry` shadowing a proved library theorem), `localized-knot` (added
`BraidWord.writhe`, which the KnotTheory module header already promised),
`explicit-central-idempotent`, `bn-mtc-action`, `n-v-tower-depth-ninety`,
`pentagon-uv-commutation` (deleted — verbatim stale duplicate),
`typed-b3-sub-braid-extraction`, `borromean-h4-categorical-derivation`,
`h3-markov-wenzl-weights`, `he4-channel-active-set`,
`he4-two-row-dominance`, `hyperelliptic-z5-classification`,
`u-coordinate-discharges`.

Two new cause classes beyond the migration boundary, both cheap:

- **missing tactic import** — `unknown tactic` at `ring` / `linarith` /
  `interval_cases`, followed by an `unsolved goals` dump that reads as a
  broken proof. One import line each, no proof step changed.
- **`import Mathlib`** — the two authored files doing it (the other 21
  hits are vendored `MathlibTest/`). Unverifiable here and a §8 hygiene
  defect; narrowed to the real cones.

Triage rule learned: **verify the library declaration the `.ts` ref names
FIRST.** Three repairs were `git rm` — the sibling was a stale duplicate
of a complete library theorem and added nothing.

Remaining 12, by error count: `spin-involution-lp-dual-invariance` 22
(`qou-0xrn`), `townsend-biot-savart-strain` 7,
`vertex-algebra-jet-relations` 4, then `categorical-transfer-matrix` /
`gb-depth-period-correspondence` / `categorical-q-ext-deriv-unique` at 3,
`descent-cocycle-deviation` / `braid-action-tensor` (`qou-8qby`) /
`lagrange-resolvent-transform` at 2, `vertex-operator` (`qou-xdwp`) and
`chi-v21-hoefsmit-matrix-derivation` at 1.


**Correction:** the count is **38 → 11 (27 fixed)**, not 38 → 12. Off-by-one in
a hand-counted intermediate list (15 entries read as 16), which propagated
through the later subtractions. Re-measured after merging origin/main (151
commits) and re-running all 40 originally-failing paths lean-direct. The
per-file list is unaffected — it always had 11 rows.


## 2026-09-04, later — 38 → 8

30 of the 38 at 0 errors. Four more this pass: `descent-cocycle-deviation` (a
dropped structure parameter — `TwistedTwoCocycle R M`, not `… M`),
`lagrange-resolvent-transform` (**a completed proof**, not a repaired reference:
the `k = 4` case never held, because the enumerated ζ-power table was sized
against the products `k·j ≤ 16` while `ring_nf` produces exponents to 32;
replaced by a general conditional reduction lemma), and
`chi-v21-hoefsmit-matrix-derivation` (a forward reference, then a tactic script
whose failure was masked by a heartbeat timeout — now `sorry` + `-- Ref:`,
bean `qou-18b6`).

Two more traps for the list:
- **Raise `maxHeartbeats` before believing a timeout.** At 4 000 000 the
  chi-v21 declaration elaborates in 28 s and reports a real `rw` failure. A
  timeout makes a broken proof indistinguishable from a slow machine.
- **A forward reference reports `Unknown identifier`**, same as a missing
  declaration. Check the same file before concluding the name is gone.

Remaining 8: spin-involution-lp-dual-invariance 22 (`qou-0xrn`),
townsend-biot-savart-strain 7, vertex-algebra-jet-relations 4,
categorical-transfer-matrix (`qou-xdwp`) / gb-depth-period-correspondence /
categorical-q-ext-deriv-unique 3, braid-action-tensor (`qou-8qby`) 2,
vertex-operator (`qou-xdwp`) 1.


## 2026-09-04, third pass — 38 → 6

`vertex-operator` (a §7c straddle: `ReebBundle` is ℝ-indexed, this file is over
`R_q`; bundle now a type parameter — plus `axiom ope_is_skein` converted to a
theorem whose proof is record construction, so assuming it bought nothing) and
`braid-action-tensor` (both failures were `≫` right-association; `slice_lhs`
re-brackets — `qou-8qby` closed).

Remaining 6: spin-involution-lp-dual-invariance 22 (`qou-0xrn`),
townsend-biot-savart-strain 7, vertex-algebra-jet-relations 4,
categorical-transfer-matrix (`qou-xdwp`) / gb-depth-period-correspondence /
categorical-q-ext-deriv-unique 3.


## 2026-09-04, fourth pass — 38 → 4, plus a correction and a cost

`categorical-q-ext-deriv-unique` (the `qinv` field is DETERMINED by
`q * qinv = 1`, so the theorem needed a derivation, not the extra hypothesis
that would have weakened it) and `gb-depth-period-correspondence` (three
`opaque` constants were asserting `Nonempty (GroupLikeDepth q n)` — the
`sharpness` field of the file's own conjecture class — unconditionally; now
parameters, with the content derived as `depth_period_nonempty`, no axioms).

**CORRECTION to my own claim.** The audit doc said a stranded sibling is
"often a pure duplicate". That is a rate over a population I never measured;
I generalised from three repairs. A sibling session measured the adjacent
population (`02483c5457` on main): `sorry`-typed declarations = **exactly 1**
corpus-wide, siblings degenerate on a library name = **exactly 1**, both the
same file. Real shape, wrong rate.

**Corpus-grep miss.** `scripts/lean-sibling-library-divergence-audit.py`
existed from 2026-09-03 13:11, before this sweep, detecting the same
phenomenon from the other side. Its motivating incident is worse than any
found here (a `False` derivable from a stale sibling on 2026-09-03).

**Cost of the sweep, measured not assumed.** `lean.ref` resolves sibling-first
BY FILE, so making a sibling compile turns a visibly-broken shadow into a
silently-divergent one. Of the 38 files touched, 6 are in that script's 195
divergences and **4 verify as real**: `QOU.planck_classical_limit`,
`QOU.qExtDeriv_classical`, `QOU.qLieBracket_classical`,
`QOU.FlavorDressing.flavor_mass_splitting_bound`. All pre-existing; deciding
which declaration is canonical is a per-block judgement about what the `.md`
means, not a compile fix, so not done here.

The other **2 are false positives** from that script's documented
namespace-concatenation defect — it paired `descent_cocycle_deviation` with a
library file declaring no such name. Verify a reported pair against both files;
another agent's audit script is not a primary source.

Remaining 4: spin-involution-lp-dual-invariance 22 (`qou-0xrn`),
townsend-biot-savart-strain 7, vertex-algebra-jet-relations 4,
categorical-transfer-matrix 3 (`qou-xdwp`).


## 2026-09-04, final — 38 → 1

Only `spin-involution-lp-dual-invariance` (22, `qou-0xrn`) left; that is the
author's judgement call and stays untouched.

`categorical-transfer-matrix`, `vertex-algebra-jet-relations` and
`townsend-biot-savart-strain` all repaired, and each carried something larger
than its compile error.

**FOUR bare axioms across the sweep, wrong four different ways:**
`ope_is_skein` EMPTY (record construction); `transfer_matrix_level_independence`
FALSE (refutation now proved — a free `vertex_volume` field means two matrices
can share a base and carry any two values); `markov_level_compatible` provable
by `rfl` AND describing a different claim than its statement; and
`kappa_squared_tends_to_zero_axiom` **not an axiom at all** — a `theorem` with a
real filter proof, under a docstring announcing it as pending Mathlib
infrastructure.

`#print axioms` sees none of these. It reports what a proof term depends on, not
whether the statement is empty, false, docstring-mismatched, or already proved
under a misleading name.

**Two `lean.ref`s pointed at the wrong declaration.**
`categorical-transfer-matrix` named `QOU.Torsion.CategoricalTransferMatrix` —
live library code (a spectral mass-gap object with consumers in
`MassGapKeystone`/`MassGapFrontier`), not the braiding object its `.md`
describes. `vertex-algebra-jet-relations` named `euler_level_stable`, which was
a `norm_num` arithmetic identity; that WAS the block's formalisation.

`townsend`'s 7 errors were all Mathlib API drift (`Tendsto.pow` → `𝓝 (0^2)`,
rpow-vs-natural-power, `Pi.div`, an implicit `τ` passed explicitly) — the
opposite of what its docstring claimed.


## Fourth main merge, 2026-09-04

`7297f2f6d5 → d0d473550a` (21 commits), merged as `bf4f787890`. All **37**
repaired siblings re-verified `lean`-direct: **exit 0, zero errors, every one**.
No regressions. `pentagon-uv-commutation.lean` reports DELETED, which is this
sweep's own `git rm` of a verbatim stale duplicate, not a miss.

The single merge conflict was provenance-only (`commitSha` / `computedAt` in
`computations/witness-raw-float64-audit.witness.json`); both payloads hash
identically with the volatile keys masked, so the later run was taken and
nothing computed differently.

`QOU/Mathlib/LPDuality.lean` is the one library file main touched that is in
this branch's cone (+61 lines from a sibling, no deletions). Compiled anyway —
exit 0 — because "pure addition" is an argument, not a check.

Sweep stands at **38 → 1**; the remaining one is `qou-0xrn`.



## 2026-09-04 14:5xZ — independent confirmation from qou-n9j7, and four files outside this list
A second, independent pass (all 907 content-block siblings against a rebuilt library, PR #6649) confirms this sweep: every file in the 38 is green on main ceb526bc31 except qou-0xrn. FOUR reds are NOT in the 38 and remain red on main: knots-particles-confinement/confinement-level-exists (Unknown constant QOU.BraidKnot.ConfinementLevel.exists), lifting-and-descent/euler-char-stability (Failed to infer type of binder n), lifting-and-descent/localized-knot (no BraidWord.writhe in the environment), mass-theory/qz-bicompletion (Unknown identifier zPochhammer). Tracked on qou-isps; not touched by me. Note: my first sibling-fix commits collided with yours on rebase and were dropped for main's versions — same repairs, yours went further.


## 🟩 38 → 0 — the whole population is green (measured 2026-09-13, bean qou-g5sp)

This bean's last entry reads *"38 → 1. Only `spin-involution-lp-dual-invariance`
(22, `qou-0xrn`) left; that is the author's judgement call and stays untouched."*

**That one is green too.** `scripts/lean-content-sweep.sh` on `main`
`16ccc3f7e2`:

```
=== swept 938, RED 0 ===
```

`spin-involution-lp-dual-invariance.lean`: `exit 0`, 0 errors. So are all four
of the reds this bean's own 2026-09-04 addendum flagged as **outside** its list
and tracked on `qou-isps` — `confinement-level-exists`,
`euler-char-stability`, `localized-knot`, `qz-bicompletion` — and both files of
`qou-29pv` (whose prescribed one-line `import Mathlib.Data.Real.Basic` is in
place at line 1 of `knot-factor-borromean-composite.lean`; that bean said
*"verify, don't assume"*, so: verified).

**I cannot say WHEN or BY WHOM the survivor was fixed.** Agent clones here are
shallow, and `git log` on that file reaches exactly one commit in the fetched
window. The measurement is the evidence; the history is not available to me, and
guessing at it would be the error this bean's own corrections are about.

**Wider than this bean's population.** It counts 908 QOU siblings; the sweep
covers **938 across all three papers plus the visualizer** (QOU 902, UGB 22,
fred2005 12, visualizer 2). The UGB and fred2005 siblings are reachable by
neither this bean's method nor `lean-library-sweep.py`.

Per-file data:
[`docs/audits/2026-09-13-content-sibling-compile-sweep.tsv`](../docs/audits/2026-09-13-content-sibling-compile-sweep.tsv);
write-up + method + positive control:
[`2026-09-13-every-content-sibling-compiles-zero-red.md`](../docs/audits/2026-09-13-every-content-sibling-compiles-zero-red.md).

## The two durable findings in this bean outlive the count

**1. "Migrations stop at the sibling boundary."** The 2026-09-04 update's
diagnosis — a library object changes shape, every consumer inside the Lake globs
is updated because `lake build` forces it, and the siblings are left behind
because nothing builds them — is the reusable content here, and the count going
to zero does not retire it. It is a *recurring* condition, not a one-off
backlog: nothing forces a sibling to be rebuilt when a library signature moves,
so the population can go red again the next time one does, silently.

**What has changed is that the check now exists and is wired in.**
`scripts/lean-content-sweep.sh` is exactly this bean's own "Next" item from
`qou-29pv` — *"Consider a gate: compile every file named by a `lean.ref`"* — and
it runs in `/prepare-merge` §4 and `prepare-merge-auto` Phases 1 and 4. So the
consequence line *"anyone changing a library signature must grep
`content/<paper>/**/*.lean` outside `lean/` as a separate step"* is now served by
a script rather than by discipline.

**2. The cost note stands and is not closed by this.** *"`lean.ref` resolves
sibling-first BY FILE, so making a sibling compile turns a visibly-broken shadow
into a silently-divergent one."* Four of the divergences this bean measured
verify as real (`QOU.planck_classical_limit`, `QOU.qExtDeriv_classical`,
`QOU.qLieBracket_classical`, `QOU.FlavorDressing.flavor_mass_splitting_bound`),
and deciding which declaration is canonical is a per-block judgement about what
the `.md` means — **not** a compile question, and **not** settled by 938/0.
`scripts/lean-sibling-library-divergence-audit.py` is the detector; that work is
open and belongs elsewhere.

Status → completed **on the compile question only**. The divergence item above
is a different subject and should carry its own bean if it does not already.
