---
# qou-2ixd
title: 'R9 is RED on main: gram.py moved to convention D, the registry still says C'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T12:46:10Z
updated_at: 2026-08-15T12:51:32Z
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
