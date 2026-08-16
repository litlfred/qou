---
# qou-2ixd
title: 'R9 is RED on main: gram.py moved to convention D, the registry still says C'
status: completed
type: task
priority: normal
created_at: 2026-08-15T12:46:10Z
updated_at: 2026-08-16T11:28:48Z
---


## What was red

`docs/coordination/trace_convention_registry_validate.py` on `origin/main`:

    ERROR : R9 pyhecke.gram.z: registry says convention C
            (z = 0.49932033418369445241...) but the CODE returns
            0.6126880371464652 (|d| = 0.1134 > 1.0e-15)
            -- it is actually convention D
    FAIL  (1 error(s), 22 warning(s))

`gram.py:175` reads `z = q0 ** 3 / (q0 ** 2 + 1)` and inverts `G` on the
quotient `H_3/rad`. That is the migration from bean `qou-w8zz` (in-progress,
sibling) — owner-approved and correct. The `blocked_migrations` row asserting
`stays: C` simply did not move with it.

**The gate worked.** The registry's own note said, in advance: *"If this ever
reports D without blocked_migrations being cleared, something switched it."*
It reported exactly that. R4/R5 compare a docstring to a registry field and
stay green whenever both sides go stale together; R9 evaluates the code.

## Fixed

1. `blocked_migrations: []`; the row moved to a new `resolved_migrations` with
   the resolution recorded. Moved rather than deleted — its `reason` is the
   clearest statement in the repo of why the full Wedderburn Gram cannot be
   inverted under D, and that is still true.
2. `evaluators/z[4]` `pyhecke.gram.z`: `convention` C → D.
3. The `.md` twin (`qou-ungx`: the twin drifts silently) and the
   `historical_c_sites` cross-reference, both of which still said "three
   places" and "BLOCKED".
4. R9 re-run: **PASS (0 errors, 22 warnings)** — the 22 are the pre-existing
   R5 "Borromean trace without a declared convention" warnings, unchanged.

## Two findings this exposed

### The detector trusted the record

`scripts/convention-c-producer-audit.py::scan_reexports` reads
`blocked_migrations` to decide what counts as a leak, so with a stale row it
reported **25 production sites "receiving convention C"** that were receiving
D. A detector that trusts a record inherits its staleness — the exact failure
the excision has been unpicking, arriving inside the tool built to find it.

Now verifies the premise: `_defines_convention_d(src, sym)` checks the named
file actually still defines the symbol as C before deriving anything from the
row, and prints `REGISTRY STALE` if not.

### `gram.py` has a live INTERNAL C/D split

Classification was `path.startswith("tools/pyhecke/") -> blocked by design`.
One registry row covered `gram.py::z`; three function-local C definitions
sheltered under the same blanket:

| site | |
|---|---|
| `tools/pyhecke/python/pyhecke/gram.py:650` | `z_ = 1 / (_mp.sqrt(q) + _mp.sqrt(qi_))` |
| `tools/pyhecke/python/pyhecke/gram.py:746` | same |
| `tools/pyhecke/python/pyhecke/atom.py:691` | `z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)` |

The `gram.py` docstring above line 650 says:

> **Convention C**, in lockstep with the module's `z` — see the blocking note
> at that definition.

The module's `z` is now **D**. They are no longer in lockstep, and the
docstring asserts they are. So the 50-dps mpmath trace path — the one you
reach for when precision matters — disagrees with the module's own declared
convention by 22%. R9 does not see it: it evaluates the module attribute
`pyhecke.gram.z`, not `_tr_m_mp`.

Classification is now registry-derived, so these three report as **"C with NO
registry row (unexplained)"** and count as actionable: `0 -> 3`.

## Next

- **Not fixing the three sites here.** `gram.py` is `qou-w8zz`'s active scope
  (sibling, in-progress, branch `claude/gram-convention-d-quotient-2026-08-15`,
  14 commits ahead of main and NOT carrying this registry fix). Changing the
  mpmath trace path underneath an in-flight migration is how the original
  block's "silently corrupts every consumer" warning comes true.
- Worth an R9-style evaluator for FUNCTION-level returns, not just module
  attributes — that is the hole these three sat in.

---

## Round 2: R9 could only see module attributes

The three unexplained `gram.py`/`atom.py` sites above sat in a hole R9 could
not reach: it evaluated **module attributes** only, so anything computed inside
a function was outside the gate. `pyhecke.gram.z` (module attr) was checked and
confirmed D; `z_mp()` and `tr_m_mp()` return C and were never looked at.

Measured:

    gram.z          (float64) = 0.6126880371464652        <- convention D
    gram.z_mp()     (50 dps)  = 0.4993203341836944524...  <- convention C
    gram.tr_m_mp()[1]         = 0.4993203341836944524...  <- convention C
    gram.tr_m_mp_strings()[1] = 0.49932033418369445241... <- convention C

18.5% divergence behind one import. **The float64 path is correct and the
NO-FLOAT64 path is not**, so the more precise answer is the wrong-convention
one — the opposite of where anyone would look.

### Two new evaluator kinds

`callable_no_arg` and `callable_index` in `_eval_z`. Registered
`pyhecke.gram.z_mp` and `pyhecke.gram.tr_m_mp[1]` as **C** — the truth, so R9
asserts it rather than leaving it invisible. Both now confirm at `|d| = 1.9e-51`.

### R10 — one module, one convention

R9 checks each entry against the registry *independently*, so a module whose
symbols disagree with **each other** passes entry by entry. `pyhecke.gram` does
exactly that: `z`=D, `z_mp`=C, `tr_m_mp[1]`=C, all three accurately recorded,
R9 confirms all three, nothing reported.

A caller imports a module, not a registry entry. R10 groups the `z` evaluators
by module and fails any module exporting more than one convention.

Waivable by name, because a module may legitimately export a preserved
historical constant beside its production one (`schur_principal_mpmath` does,
and says so in the symbol name). **A waiver downgrades to WARNING, never to a
note** — a note is read once and scrolled past; a warning is counted in the
summary line, so an open split stays visible until it is closed.

`pyhecke.gram` is waived as an OPEN DEFECT, not an approved design. Validator:
`PASS (0 errors, 23 warnings)` — the 23rd is R10's.

## The audit only ever looked at ASSIGNMENTS

`scan()` keyed off an assignment target, so a function computing the convention
straight into its `return` had nothing to match on:

    def z_mp(dps=...):
        return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))     # invisible

**"178 → 0 actionable" was never true.** With return-scanning added
(`ACTIONABLE 0 → 11`), seven sites appear that no sweep had ever counted, five
of them live producers in `computations/`:

| site | function |
|---|---|
| `computations/_habiro_coefficient_extract.py:136` | `_markov_z_q()` |
| `computations/_helium_habiro_coefficient_extract.py:80` | `_markov_z_q()` |
| `computations/inter_nucleon_linked_channel.py:116` | `z_factor()` |
| `computations/knot_operator_census_group_actions.py:79` | `z_factor()` |
| `computations/lepton_t2n_torus_tower.py:78` | `z_factor()` |
| `computations/qbeta/qbeta_ck_sseries_operator_match_probe.py:94` | `zf()` (probe) |
| `tools/sage-examples/scripts/hecke_surface.py:56` | `markov_z()` |

Each detector generation has found a class the previous one structurally could
not see: grep missed spellings; AST-on-assignments missed the half-argument
form; AST-on-assignments missed **returns**; witness fingerprints missed higher
`n`; and a registry-trusting detector missed a stale record. The pattern is
that the blind spot is always in the *shape* the detector keys on.

## Next

1. **Migrate the 5 live producers + 1 probe**, then regenerate their witnesses
   on the serial harness. Unclaimed — not started here, because it overlaps the
   witness arc siblings are running and wants the lock.
2. `tools/sage-examples/scripts/hecke_surface.py` misclassifies as
   "computations — live producers"; `classify()` has no sage-examples bucket.
3. The 3 `gram.py`/`atom.py` sites stay with `qou-w8zz`.

---

## Round 3: the six return-form producers, migrated and regenerated

All six moved to `z = q^3/(q^2+1)`. Audit **11 -> 5 actionable**; the 5 left are
the 4 pyhecke sites (`qou-w8zz`'s scope) and one sage example that misclassifies
as a live producer.

Witnesses regenerated serially, lock held, nothing else running:

| witness | result |
|---|---|
| `inter-nucleon-linked-channel` | 10 assertions, all passed |
| `knot-operator-census-group-actions` | regenerated |
| `lepton-t2n-torus-tower` | 21 assertions, all passed (after two fixes below) |

All three: **0 dead-block entries** structurally.

### A THIRD blind spot: C-specialised closed forms

Migrating `z` is not migrating the file. Four downstream quantities were
hardcoded to values that only hold at `z_C`, and the audit cannot see any of
them — it keys on a target name containing `z`, and these are named `W2`,
`W11`, `trM_sigma1_sq`, `census_hopf`:

| site | was | is |
|---|---|---|
| `knot_operator_census_group_actions.trM_sigma1_sq` | `1 + (q-1)/sqrt(q)` | `h*z + 1` |
| `lepton_t2n_torus_tower.wenzl_weights` | `(q^{3/2}+q+1)/(q^3+q^2+q+1)` | `(q*z+1)/(q^2+1)` |
| `lepton_t2n_torus_tower.trM_symbolic` | same weights, in sympy | solved from `z` |
| `inter_nucleon_linked_channel.census_hopf` | unlabelled "DIFFERENT normalisation" | named convention C, D value recorded beside it |

Verified symbolically before rewriting: `h*z+1` at `z_C` reproduces
`1+(q-1)/sqrt(q)` exactly, and `(q*z+1)/(q^2+1)` at `z_C` reproduces
`(q^{3/2}+q+1)/(q^3+q^2+q+1)` exactly. **The square roots were never
structural — they were `z_C`'s, showing through.** Under D both are rational,
which is the same "D never leaves Q(q)" property the migration keeps hitting.

### The symbolic path caught itself

`lepton_t2n_torus_tower` failed 2 of 21 assertions on first regeneration, and
both failures were informative:

- `trM_T2_3_symbolic_eq_numeric` — 0.7302 vs 0.8485. **A real miss of mine**:
  I migrated `wenzl_weights` (numeric) and left `trM_symbolic` (sympy) on C.
  The file's own symbolic-vs-numeric cross-check found it, which is exactly
  what that assertion is for.
- `trM_hopf_wenzl_eq_census` — this one was **correctly** failing. It asserted
  the Wenzl form equals the census Hopf form, which holds only while both are
  C. Asserting it now would be asserting C = D. Replaced with the
  convention-independent `trM_hopf_wenzl_eq_h_z_plus_1`, and the C/D gap
  recorded as data — the treatment `inter_nucleon_linked_channel` already gave
  the same pair.

### Pre-existing, not from this migration

`inter_nucleon_linked_channel` pins its own `Q0 = 1.109978595612202257...`,
against the canonical proton pin `1.109978582751380807...` and the muon pin
`1.109978595554180575...`. Close to muon, differing at digit 11 — a **third**
value. Not touched here; flagged.

## Next

1. **Detector gap:** nothing looks for C-specialised closed forms. The
   fingerprint is a half-integer power (`sqrt(q)`, `q**1.5`, `q**Rational(3,2)`)
   in a weight or trace expression, in a file that otherwise reads as D. That
   is a well-defined scan and would have found all four above.
2. `classify()` has no sage-examples bucket.

---

## Round 4: a detector for C-specialised closed forms

The blind spot round 3 found by hand is now scanned for. `scan_closed_forms`
flags a **half-integer power of `q` inside a trace or Wedderburn-weight
binding, in a file that has already migrated to D**. Under D those quantities
are rational in `q`, so a square root in one is `z_C` showing through.

### It was built too broad first, and the corpus said so

The first version matched any half-power of `q` in a D-migrated file: **50
sites**, nearly all legitimate. `q^{1/2}` is not a convention marker on its
own — `q^{1/2}+q^{-1/2}` is `[2]_{sqrt q}`, the Temperley–Lieb loop parameter
at half-argument, and it appears in Wenzl positivity, pair-skein formulas, and
the Jones change of variable `t = q^{-2}`, `A^2 = -q`.
`trace-convention-audit.ts` had already recorded exactly this: 58 content files
carry the expression, and flagging them *"would repeat the loose-grep error
that once reported 70 producers where the truth was 13."*

I repeated it anyway, in a new detector, and had to be told by the output. The
narrowing is to bindings whose NAME says trace or weight (`trM`, `W2`,
`y_lambda`, `wenzl`, `hopf`, `census`), which is the claim the detector
actually makes. **50 -> 4.**

### It rediscovers the site that was found by hand

`tools/pyhecke/python/pyhecke/gram.py:637  tr_m_mp <- sqrt(q)` — found
independently, having originally cost a manual read of the module. That is the
test that matters for a detector built after the fact.

### The four

| site | binding | status |
|---|---|---|
| `pyhecke/gram.py:637` | `tr_m_mp` | qou-w8zz's scope, registered in R9/R10 |
| `c_3_categorical_derivation_attempt.py:184` | `trM_hopf` | NEW, unverified |
| `from_scratch/wedderburn_markov.py:191` | `wenzl_y_lambda` | NEW, unverified |
| `probes/qbeta_5two_categorical_markov_volume_probe.py:132` | `ocneanu_weights` | NEW — but the Ocneanu trace is the FULL-Hecke trace with its own normalisation, so this one may be correct as written |

A fifth was `lepton_t2n_torus_tower.trM_hopf_census_form`, the C reference I
kept deliberately in round 3. Renamed `trM_hopf_census_form_C` so the label
lives in the NAME rather than only the docstring — which is what the audit's
`DELIBERATE` exemption keys on, and what the registry rule asks for. Producer
re-run: 21 assertions, all passed.

Selftest 30 -> 37. Six of the seven new fixtures pin the NARROWING rather than
the matching — over-breadth is this detector's whole risk.

## Next

1. Verify the three new candidates individually (as round 3 did: derive the
   general identity, check it reproduces the C closed form at `z_C`, then
   rewrite in terms of `z`). `ocneanu_weights` may be a true negative.
2. `classify()` still has no sage-examples bucket.

---

## Round 5: the three candidates verified, and a THIRD spelling of C

### `c_3_categorical_derivation_attempt.trM_hopf` — real, and the file was split

`1 + (q-1)/sqrt(q)`, while the SAME FILE already had `z = q**3/(q**2+1)` at
lines 231 and 243. Internally split exactly like `gram.py`: production `z` on
D, the Hopf closed form derived from it still on C, feeding a `c_3` candidate
at line 430. Migrated to `h*z + 1`; two stale annotations fixed with it.

Verdict checked before and after: **NEGATIVE both sides.** The numbers moved,
the scientific conclusion did not — worth confirming rather than assuming,
since the migration changes an input to that verdict.

### `qbeta_5two_categorical_markov_volume_probe.ocneanu_weights` — real, and a NEW BLIND SPOT

    t = sp.symbols("t", positive=True)
    q = t ** 2
    z = 1 / (t + 1 / t)          # convention C, invisible to both detectors

A **third spelling**. `is_c_form` needs a visible `sqrt` or `0.5`; there is
none. `is_c_form_halfarg` matches `t/(t**2+1)`; this is the reciprocal-sum
form. And it is *character-for-character* `1/(q + 1/q)` = `1/[2]_q`, the
Temperley–Lieb loop reciprocal, which the selftest explicitly requires NOT be
flagged. Shape cannot decide it.

What decides it is the file's own declaration `q = t ** 2`, which says `t` is
`sqrt(q)`. New `_half_argument_vars` reads that; `is_c_form_reciprocal` uses
it. The two fixtures that matter are the pair: flag `1/(t+1/t)` when
`q = t**2` is declared, clear `1/(q + 1/q)` when it is not.

Migrated to `t**6/(t**4+1)` — convention D in the half-argument variable.

**The independent confirmation.** This probe solves the H₃ Wedderburn weights
from three trace values, knowing nothing of Schur–Weyl or `live_channels`:

    W_(3)   = (q^4 + 1)/(q^2 + 1)^2      -> 0.505405 at q0
    W_(21)  = q^2/(q^2 + 1)^2            -> 0.247298 at q0
    W_(111) = 0

`W_(111) = 0` exactly, and the other two match the canonical convention-D
weights `y_(3) = 0.50540422650...`, `y_(2,1) = 0.24729788674...` to every
digit. The dead antisymmetric block, arrived at from a completely different
direction — a linear solve, not a representation-theoretic argument. Held-out
Ocneanu gate still True; 5 assertions passed.

### `from_scratch/wedderburn_markov.wenzl_y_lambda` — NOT a defect

`computations/from_scratch/README.md` declares the whole directory
**DEPRECATED for production** (2026-05-29, #1422 decision A'), kept "for
pedagogy / historical reference; not re-pursued". The file's own docstring
reads "Wait —", "Hmm but", "This is getting complicated. Let me just use the
SHORTCUT". No `WitnessBuilder`, no witnesses in the tree. A classifier gap, not
a producer defect.

### Two classifier gaps closed

- `from_scratch/` — bucketed as DEPRECATED and excused from the actionable
  count, matching what its README already says. Bucketed rather than skipped
  outright (as `_deprecated/` is) so it stays countable.
- `tools/sage-examples/` — bucketed, but **kept actionable**: nothing declares
  it dead, and an example teaching convention C is arguably worse than a
  producer using it, because examples get copied.

Selftest 37 -> 42.

## Next

1. `tools/sage-examples/scripts/hecke_surface.py:56 markov_z()` — still C, now
   correctly bucketed and still actionable.
2. The 4 pyhecke sites remain `qou-w8zz`'s.
3. `qbeta-5two-categorical-markov-volume` and `c-3-categorical-derivation-attempt`
   both carry raw float64 in their witnesses (15 and 67 fields). Pre-existing,
   the `qou-5lw7` arc.

---

## Round 6: the sage example was BROKEN on main, not merely stale

`tools/sage-examples/scripts/hecke_surface.py:56` kept a local
`markov_z(q) = 1/(q^{1/2} + q^{-1/2})` — a copy of a value the library also
exports. When `pyhecke.gram.z` moved to D the copy did not follow, and the
example's own guard fired:

    TR_M[1] = 0.612688037146  (== z above)
    AssertionError: TR_M disagrees with markov_z
    EXIT=1

So this was not a stale-convention nit: **the example exits 1 on `main`**, and
has since 2026-08-15. `assert abs(TR_M[1] - z) < 1e-9` exists precisely to
catch a local copy drifting from the library, and it did — nobody ran it.

Migrated to `q**3/(q**2+1)`. Now exits 0 with
`TR_M[1] == nf_tr(e_1) == 0.612688037146`.

**ACTIONABLE 5 -> 4.** The remaining four are all pyhecke (`qou-w8zz`).

### A non-finding, checked rather than assumed

The example prints `w_λ((1,1,1)) = 0.163383228` — nonzero on a three-row
partition, which is the structural signature of convention C. It is not:
`wedderburn_weight(λ) = d_q(λ)²/[n]_q!` is the Wedderburn–Artin/Plancherel
weight, has no `z` in it at all, and is conjugation-symmetric because
`d_q(λ) = d_q(λ')` — hence `w_(3) = w_(1³)`. It also sums to 1.648, not 1, so
it cannot be a normalised Markov weight. Recorded because the number *looks*
exactly like the defect the witness audit exists to find.

## Next

- The 4 pyhecke sites stay with `qou-w8zz`.
- Nothing else outside pyhecke is on convention C by the current detectors.

---

## Round 7: R11 — a derived quantity must match its own z

The last gate gap. R9 checks the Markov parameter; R11 checks everything
DERIVED from it — `tr_M(sigma_1^2) = h*z+1`, the H_2 weight
`(q*z+1)/(q^2+1)`, the entries of the TR_M vector.

`scan_closed_forms` already hunts these statically, but it keys on the
**binding name** (`trM`, `W2`, `y_lambda`, ...) — and a name-keyed detector is
precisely what went blind three times in this excision: the half-argument
spelling, the return form, the reciprocal form. A numeric identity cannot be
evaded by spelling.

### It has a track record

`TR_M[5]` was `z^3` rather than `h*z^2 + z` until
`docs/audits/2026-05-19-trm5-markov-bug.md`, and main carries the follow-on
commit *"flip trace_weights to h*z^2 + z — Rust and Python finally agree"*.
No static scanner can catch that: `z^3` and `h*z^2+z` are both perfectly
ordinary expressions in `z`, differing only in that one is right. **Only
evaluation distinguishes them** — the same argument R9 makes over R4/R5.

Registered `pyhecke.gram.tr_m_mp[3]` (identity `z^2`) and `[5]`
(`h*z^2+z`). Both CONFIRMED at `|d| ~ 2e-51`.

### Negative test

A gate that cannot fail is worse than none, so I injected the historical bug —
set `[5]`'s identity to `z^3` — and confirmed it fires:

    ERROR : R11 pyhecke.gram.tr_m_mp[5]: should equal z^3 = 0.1244909432...
            but the CODE returns 0.5514434143... (|d| = 0.427 > 1.0e-40).
            The derived form has drifted from the z it is derived from.
    FAIL (1 error(s), 23 warning(s))

Registry restored; `PASS (0 errors, 23 warnings)`.

Seven named identities are available (`z`, `z^2`, `z^3`, `h*z+1`, `h*z^2+z`,
`z+h*z^2`, `(q*z+1)/(q^2+1)`) — the closed forms this session had to verify by
hand in rounds 3 and 5.

## Next

- Extend R11 coverage to the producers migrated in rounds 3/5, so their closed
  forms are gated rather than merely correct-once.
- The 4 pyhecke sites remain `qou-w8zz`'s.

### R11 coverage of the producer layer is one entry, and that is a finding

Extending R11 to the four producers migrated in rounds 3/5 turned out to be
mostly impossible, for a reason worth recording:

| producer | `if __name__` guard | module-level `WitnessBuilder` |
|---|---|---|
| `c_3_categorical_derivation_attempt` | **yes** | no |
| `knot_operator_census_group_actions` | no | yes (line 109) |
| `lepton_t2n_torus_tower` | no | yes (line 178) |
| `inter_nucleon_linked_channel` | no | yes (line 120) |

Three of the four **run the whole producer at import and rewrite their own
witness**. A validator cannot import those without making validation a
side-effecting act — running `trace_convention_registry_validate.py` would
regenerate witnesses as a side effect, which is precisely the "regenerate from
the producer" attack surface the registry warns about elsewhere.

So R11 gates `c_3_categorical_derivation_attempt.trM_hopf` (verified
import-safe: 0.09 s, witness mtime unchanged) and cannot gate the other three.
`trM_hopf(q0) = 1.128088744114353785593152` matches `h*z+1` at `z_D` with
`|d| = 0`, and independently matches the `sigma_1^2` entry of
`markov-trace-recursive.witness.json` — two unrelated producers agreeing.

**The blocker is the missing `__main__` guard, not R11.** A producer that
cannot be imported without running cannot be gated by anything that imports it.

---

## Round 8: one definition, five copies, gated once

Rather than add `__main__` guards to three ~350-line producers (≈700 lines of
module-level restructuring for a gating benefit), fix the root cause: the
identities were **copy-pasted**, and local copies drifting is the defect class
this entire arc has been chasing.

`tr_M(sigma_1^2) = h*z + 1` existed in at least five places, each specialised
to convention C as `1 + (q-1)/q^{1/2}` — which IS that identity at `z_C`, the
square root being z_C's and not the identity's:

    knot_operator_census_group_actions.trM_sigma1_sq
    c_3_categorical_derivation_attempt.trM_hopf
    lepton_t2n_torus_tower.trM_hopf_census_form
    inter_nucleon_linked_channel.census_hopf
    tools/sage-examples/.../hecke_surface.trace_weights

That last one is why this matters concretely: its copy drifted from the
library and the example **exited 1 on main**.

### Canonical home

`computations/closed_form_tau_M.py` already owned `markov_z` (D) and
`hecke_h`, is a proper library module (no module-level `WitnessBuilder`,
imports in 0.07 s), and is already an R9 evaluator. Added there:

* `trM_sigma1_sq(q)` = `h*z + 1`
* `wenzl_weights_h2(q)` = `((q*z+1)/(q^2+1), 1 - that)`

Verified: `y_(2) + y_(1,1) = 1` and `y_(2)*q - y_(1,1)/q = z` both exact.
`y_(1,1) = 0.24729788674803459840...` = `1/[2]_q^2`, the same value as
`y_(2,1)` at n=3.

### Gated once, then repointed

R11 now carries 5 entries, all CONFIRMED:

    pyhecke.gram.tr_m_mp[3]                z^2               C   1.9e-51
    pyhecke.gram.tr_m_mp[5]                h*z^2+z           C   2.4e-51
    c_3_categorical_derivation_attempt     h*z+1             D   6.2e-52
    closed_form_tau_M.trM_sigma1_sq        h*z+1             D   6.2e-52
    closed_form_tau_M.wenzl_weights_h2[0]  (q*z+1)/(q^2+1)   D   1.5e-51

New evaluator kind `callable_q_index` for the tuple return.

All four producers repointed at the canonical definitions and re-run. Every
one exits 0, and **every witness is identical modulo timestamps** — only
`computedAt`, `commitSha`, `durationMs`, `scriptHash`, `scriptCommitSha`
moved. Zero numeric change, which is the test a behaviour-preserving refactor
has to pass.

The `__main__`-guard blocker is therefore routed around rather than removed:
those three producers still cannot be imported without running, but the values
R11 needs to gate now live in a module that can be.

## Next

- The 4 pyhecke sites remain `qou-w8zz`'s.
- `__main__` guards for the three producers are still worth doing on their own
  terms (a producer that runs at import is a hazard beyond gating), but no
  longer block R11.

---

## Round 9: producers that ran at import, and a q0 that is nobody's pin

### The side-effecting tail, guarded

Three producers ran their whole computation at module level, so `import
inter_nucleon_linked_channel` executed the producer and **rewrote its
witness**. Any tool that imports the module — a validator, a doc generator, a
test collector — regenerated a witness as a side effect. That is a hazard
beyond gating, and it is also why R11 could not reach them.

Fixed by moving **only the side-effecting tail** (from the `WitnessBuilder`
line to EOF) into `main()`, leaving constants and pure functions at module
level so they stay importable. Not a whole-file `main()` wrap — that would
have turned ~700 lines of module-level statements into locals and risked
`NameError` in any function reading a module global.

Verified both directions:

| producer | import side-effect free | witness after re-run |
|---|---|---|
| `inter_nucleon_linked_channel` | yes | identical modulo provenance |
| `knot_operator_census_group_actions` | yes | identical modulo provenance |
| `lepton_t2n_torus_tower` | yes | identical modulo provenance |

R11 now carries **8 entries**, all CONFIRMED — the three above plus the
canonical definitions and the two pyhecke vector entries.
`knot_operator_census_group_actions.trM_sigma1_sq` checks the *delegation*
rather than a second implementation: it fails if somebody re-adds a local
copy, which is exactly how that identity came to exist in five
specialised-to-C versions.

### A q0 that matches no documented pin — NOT changed, needs a decision

`inter_nucleon_linked_channel.py:57` pins

    Q0_STR = "1.10997859561220225731080831999100762523924148"
    # comment: "Substrate q0 (proton-anchored). FALSIFICATION reference only"

Measured against every candidate in the corpus:

| candidate | \|d\| | rel |
|---|---|---|
| proton (registry `Q_50_DIGIT_STR`) | 1.286e-8 | 1.16e-8 |
| muon-canonical (`Q_MUON`, many files) | 5.487e-11 | 4.94e-11 |
| muon variant (earlier note) | 5.802e-11 | 5.23e-11 |
| `a4_option_e` / `he4_binding_k` literals | 5.487e-11 | 4.94e-11 |

So it is **~230x closer to the muon family than to the proton pin, while its
comment says proton-anchored** — and it equals none of them. Introduced in
`e5dcd8f54`, an unrelated Lean commit, so copied rather than derived; it is
not a `Vol(4_1)`-ratio either.

**Deliberately not changed.** The two repairs differ by 230x in effect —
retarget to proton (moves every number ~1.16e-8 relative, matching the comment
and the AGENTS.md 2026-08-07 "default to the experimental (proton) pin"
directive) or to the exact muon-canonical (~4.94e-11, matching the magnitude).
This is a falsification-reference module, so the pin choice can change whether
a falsification passes. That is an authorial call, not a refactor.

## Next

- **Owner decision needed** on the q0 above: proton (per the comment and the
  directive) or muon-canonical (per the magnitude)? Either way the literal
  should become an import of a canonical constant rather than a hand-typed
  near-miss.
- The 4 pyhecke sites remain `qou-w8zz`'s.

---

## Round 10: the q0 resolved — proton, by owner ruling (2026-08-15)

Owner ruling: `inter_nucleon_linked_channel` is proton-anchored, per its own
comment and the AGENTS.md 2026-08-07 directive that new compute defaults to the
experimental (proton) pin.

Taken **by import**, not retyped:

    from q_parameter import Q_50_DIGIT_STR as _Q0_PROTON_STR

which closes the class rather than the instance — a literal cannot drift from a
source it does not have.

### The result confirms the ruling independently

All 10 assertions still pass, and two values that had been *nearly* right
snapped onto their canonical counterparts:

| field | before | after | canonical |
|---|---|---|---|
| `z(q0)` | `0.612688050606…` | `0.6126880371464652515958…` | registry `z_at_q0`, to 40 digits |
| `W_(1,1)` | `0.2472978861522…` | `0.2472978867480345984062` | `1/[2]_q^2 = 0.24729788674803459840622…`, to 22 digits |
| `tr_M(pp)` | `1.128088761203…` | `1.128088744114353785593151…` | `closed_form_tau_M.trM_sigma1_sq(q0)` exactly |

Before the change `W_(1,1)` was wrong at digit 9 against the registry's own
`y_(2,1)`; after it agrees to 22. `tr_M(pp)` now equals the canonical
`h*z + 1` **and** the `sigma_1^2` entry of `markov-trace-recursive.witness.json`
— three independent producers agreeing exactly where they previously did not.

That is the check that matters: the right pin makes the module's numbers
coincide with values derived elsewhere, and the wrong one made them miss by
1e-8 while still looking plausible.

Shift: `q0` 1.16e-8, `trM_pp - trM_nn` 1.15e-7, `W_(2)` 7.9e-10,
`W_(1,1)` 2.4e-9. R11 still CONFIRMS `z_factor` at 2.99e-51; validator
`PASS (0 errors, 23 warnings)`.

---

## Round 11: the precision-gates double-write (reported by the merge pipeline)

`scripts/precision-gates.sh` invokes `witness_raw_float64_audit.py` twice —
gating over the full corpus (line ~63), and advisory with
`--scan-root docs/audits/scripts` (line ~89). **Both wrote the same witness.**

Reproduced before fixing:

    committed dirty_witnesses = 1561
    after one advisory run    = 5        (57 lines of carve-outs dropped)

So the narrow advisory run silently replaced a corpus-wide audit with a
five-file one, and the result reads exactly like "a count moved, commit the
regenerated witness".

### The fix was already half-written

The script **already refuses `--rebaseline` with `--scan-root`**, with the right
reason attached: *"Rebaselining against a foreign root would write that root's
dirty files into a baseline keyed on computations/ paths — growing it.
Baselines drain, never grow."* The witness write is the same hazard and was not
guarded by the same rule. Now it is: a `--scan-root` run prints that it is
advisory and returns without writing.

Verified both directions — advisory leaves the witness untouched; the gating
run still writes.

### What the gating run then showed, and what I did NOT commit

Re-running the gating invocation gives `dirty_witnesses` 1561 → 1560,
`drained_files` 14 → 15, −30 fields. That is real progress, but it is **main's**:
`binding-k-enumerator.witness.json` drained 2210 → 0 in a sibling's work, and
main's committed audit witness simply has not been refreshed since.

Left it restored. Sweeping an unrelated corpus-count refresh into this PR is
how a reviewer loses the thread, and the drain belongs to whoever did it.

### Inherited red, not introduced

The gate exits 1 on one regression — `rho-k-co-casimir-extended.witness.json`,
3 → 4 raw float64. That file is **byte-identical to main** on this branch, so
the red is inherited. Worth flagging to whoever owns the co-Casimir refresh
(there is a `docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-needs-d-refresh.md`
on main now).

---

## Round 12: my precision-gates fix was superseded by a better one

Merged 94 commits from main. One conflict, on
`computations/witness_raw_float64_audit.py`: **main landed a fix for the same
double-write defect I had fixed an hour earlier**, and theirs is better.

| | |
|---|---|
| mine | a `--scan-root` run refuses to write the witness |
| theirs | `_output_name(scan_root)` derives a per-scan-root filename |

Theirs keeps the advisory run's record rather than suppressing it, and makes
the collision impossible for **any** future scan root instead of for the one
invocation `precision-gates.sh` happens to make today.

It also chases a consequence I had not: the derived name must still end in
`AUDIT_SUFFIX`, because `q0_anchor_consistency_audit.py` classifies audit
self-outputs by **suffix**, so a name ending in the scan slug gets filed as
`Q0_ANCHOR_MISSING` — measured 1889 -> 1890. I would have shipped a fix that
was correct in isolation and moved a count in a different audit.

Resolved `--theirs`; my guard is gone. Worth recording rather than quietly
dropping: two agents fixed the same defect within the hour, from the same
report, and the difference between the fixes was entirely in the second-order
consequence one of them checked.

Post-merge state: `blocked_migrations` still `[]`, `resolved_migrations` 1 row,
8 derived evaluators, `pyhecke.gram` waiver intact. Validator
`PASS (0 errors, 23 warnings)`; selftests 42/42, 16/16, 23/23.

---

## Round 13 (prepare-merge): two defects the gates caught, both mine

### `content_validate` rejected my `engine` value

`computation.engine` accepts `sympy | mpmath | python+mpmath | …`, and I had
written **`mpmath+sympy`** — on `prf:categorical-mass-markov` and in the
`WitnessBuilder` call when giving `markov_trace_canonical.py` its witness.

Set both to `sympy`, matching `markov-trace-recursive-reducer`, whose producer
has the same sympy-symbolic / mpmath-numeric shape. Witness regenerated, 6
assertions passing. **run-validate: 1 error -> 0.**

The remaining 5 issues are pre-existing warnings — three blocks with no Lean
declaration, one dangling remark, and the notice that no reference registry is
configured — not errors.

### The audit fired on a convention CONTROL

Main's 30 new commits brought `ACTIONABLE 4 -> 5`. The new site was
`qbeta_kc21_parity_convention_immunity_probe.py:141` (from the sibling's
#5123), and it is a **false positive of mine**:

    z_of(q, conv):
      C -> sqrt(q)/(1+q)
      D -> q**3/(q**2+1)
      X -> q/(1+q**2)     # "control, in no channel; genericity probe only"

`is_c_form_halfarg` matched the **X control** — `q/(1+q^2)` is exactly the
`r/(r^2+1)` shape — and a control deliberately chosen to sit in *no* channel is
the opposite of a convention-C leak.

`DELIBERATE` could not save it: that exemption keys on the target NAME, and
here the label lives in a docstring and a branch guard. The machine-checkable
signal is that **the same function also returns the D form** — a function
returning more than one convention is a dispatcher, and a dispatcher's C branch
is a labelled comparison by construction.

Bucketed as `convention dispatcher (returns C and D) — labelled comparison`
rather than silently skipped, so it stays countable. **ACTIONABLE 5 -> 4**, and
all four remaining are pyhecke (`qou-w8zz`).

Selftest 42 -> 44, with fixtures pinning both directions: a C+D function is a
dispatcher, a C-only function is not.


---

## Summary of Changes (completed 2026-08-16)

Opened because R9 was RED on `main` — the registry said `pyhecke.gram.z` was
convention C and the code returned D. That is fixed, and the arc it opened is
finished: **`convention-c-producer-audit.py` now reports ACTIONABLE: 0 sites**,
and this time it is a measured zero from a detector that scans return forms,
closed-form specialisations, half-argument reciprocals and registry-derived
buckets — not the 2026-08-09 "0 actionable" that took a week to retract.

**Three registry rules added**, each closing a hole the previous one revealed:
- **R9 function-level** — `callable_no_arg` / `callable_index` / `callable_q_index`.
  R9 reached only module attributes, which is exactly where `gram.py`'s
  high-precision path was not.
- **R10 — one module, one convention.** R9 checks entries independently, so a
  module whose symbols disagree passes entry by entry. A caller imports a module.
- **R11 — a derived quantity must match its own `z`.** Negative-tested against
  the historical `TR_M[5] = z³` bug; it fired on my own incomplete migration in
  `qou-cds2`, which is what it exists for.
- Plus **`agreed-migration-pending`** (`qou-cdh1`) and `RC8`/`RC9`/`RC10`.

**Detector-blindness taxonomy: eleven spellings**, three of which were found by
detectors written to catch the previous blind spot, plus the counter-move that
beats all eleven — check the algebraic form of the RESULT, not the source.

**The corrections matter as much as the fixes**, and most were mine: `qou-76a6`
retracted entirely (25 sites measured against a five-day-stale checkout); 53
orphans → 3; the closed-form detector's 50 false positives → 4; "151 coverable"
→ 13 → 2; "two mpmath consumers" → four; "~10 of 13 declarable" → wrong, killed
by checking semantics; and a verified 40-minute run destroyed by my own
`git checkout -- computations/*.witness.json` glob.

**Everything still open has its own bean** and none of it belongs here:
`qou-11wz` (the five-witness cascade from the atom.py migration), `qou-a28x`
(the 11 WEAK provenance candidates), `qou-cdh3`, `qou-cds1`, `qou-cds3`,
`qou-cds4`, `qou-cds5`, `qou-pvem`, and `prf:interface-knot-markov-z` left
deliberately red under `qou-cdh4`.
