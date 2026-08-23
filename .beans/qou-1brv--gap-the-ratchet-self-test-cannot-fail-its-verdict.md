---
# qou-1brv
title: 'GAP: the ratchet --self-test cannot fail — its verdict is a tautology'
status: completed
type: task
priority: normal
created_at: 2026-08-23T07:57:21Z
updated_at: 2026-08-23T08:37:23Z
---

Found running `/prepare-merge-auto` on PR #5477, which is the PR that *added*
these self-tests. The self-tests do what the PR claims — they never construct a
`WitnessBuilder`, so they cannot pollute the witness, and that is verified. This
is a second, smaller defect in the same file, in the same spirit.

`_self_test()` in both audits computes its verdict from a tautology:

    fires = n > (n - 1)      # True for every int n
    holds = not (n > n)      # True for every int n
    ok    = fires and holds  # therefore always True
    return 0 if ok else 1    # therefore always 0

So `--self-test` **cannot report failure**. It exercises `scan()` and prints the
numbers, but it never touches the code path it claims to be testing — the strict
branch in `main()`, `grew = n > BASELINE; if args.strict and grew: return 1`. If
someone flipped that `>` to `>=` or `<`, or deleted the `--strict` guard, the
self-test would still print "ratchet FIRES ... True" and exit 0.

This was not theoretical during the merge run. On the rebased branch the live
divergent count was **72** against `BASELINE_DIVERGENT = 71` — the ratchet was
genuinely red — and `--self-test` printed

    BASELINE_DIVERGENT in source: 71  <-- DISAGREES with live 72
    ...
    EXIT=0

It exits 0 while the gate it is testing is failing. The disagreement is printed
for a human to read and has no effect on the exit code, which is the same shape
as the defect #5477 fixed: an artifact whose content contradicts the state it
reports.

AGENTS.md, on the bare root `lake build`: *a gate that can report success
without examining anything is not a gate.* Same class.

## Suggested fix (small, no semantic change)

Extract the ratchet predicate so `main()` and `_self_test()` share one function,
then have the self-test call it rather than re-spell it inline:

    def _grew(count: int, baseline: int) -> bool:
        return count > baseline

`main()` uses `grew = _grew(n_div, BASELINE_DIVERGENT)`; `_self_test()` uses
`fires = _grew(n, n - 1)` and `holds = not _grew(n, n)`. The expressions stay
always-True, but they now exercise the *shared* predicate, so a change to the
comparison operator is caught. That is the regression test the current code only
looks like.

Deliberately NOT proposed: making `--self-test` fail when `BASELINE` disagrees
with the live count. That would duplicate `--strict` and conflate two questions —
`--self-test` should assert the *mechanism* works, `--strict` asserts the *state*
is within baseline. Worth an owner opinion before implementing either way.

## Why it was not fixed in #5477

Editing the producer changes its `scriptHash`, which makes the committed witness
self-stale and requires a re-run plus another commit — during a merge run whose
explicit verification was that those witnesses stay byte-identical. Reported to
the owner in the merge report instead of expanded into the PR.

Affected:
  computations/audits/undeclared_muon_pin_flip_risk_audit.py   (_self_test)
  computations/audits/hardcoded_q0_literal_families_audit.py   (_self_test)


## FIXED 2026-08-23 — and the fix is mutation-verified

Extracted the ratchet's one predicate into `ratchet_fires(count, baseline)`
in both audits. `main()` and `_self_test()` now call the SAME function, so
the self-test exercises the predicate rather than a pair of literals.

**Proved it can now fail**, which is the property it lacked. Mutating the
shared predicate and re-running `--self-test` on both files:

    mutation            undeclared_muon...    hardcoded_q0...
    (unmutated)         exit 0  PASS  OK      exit 0  PASS  OK
    >  ->  >=           exit 1  FAIL  OK      exit 1  FAIL  OK
    >  ->  <            exit 1  FAIL  OK      exit 1  FAIL  OK

6/6. `>=` breaks the `holds` leg (`not (n >= n)` is False); `<` breaks
the `fires` leg. Files restored byte-identically after each mutation.

**Asserting the fix works was not enough here** — the defect being fixed was
precisely a test that passed without testing anything, so a fix verified by
'it still exits 0' would have reproduced the bug at one remove.

**Witnesses regenerated**, because editing the producers moved their
`scriptHash` (`68033e5348d3 -> c97056e5cad0`,
`361fa9700275 -> cea037bf5055`) and would otherwise self-stale them. This is
the reason the #5477 merge agent correctly declined to fix it in-flight.

**No count moved** — 0 of 5 numeric fields across the two witnesses, which is
the right outcome for a pure refactor. `hardcoded-q0-literal-families` stays
`allPassed: false` at 72 vs baseline 71: that ratchet is still deliberately
red and this change does not touch it. Baselines drain, never grow.

---

## 2026-08-23 (second agent) — defect 1 landed by a sibling and VERIFIED; a second defect found

I worked this bean in parallel and a sibling landed the same fix first
(`eadcb02e08` *"fix(qou-1brv): the ratchet self-test could not fail — one shared
predicate"*, `ratchet_fires`). Re-scoped to verify rather than re-derive, per
AGENTS.md §"Parallel exploration".

**Verified independently** with a mutation matrix against the landed code:

| mutation to `ratchet_fires` | `undeclared_muon_pin_flip_risk` | `hardcoded_q0_literal_families` |
|---|---|---|
| none | exit 0 ✓ | exit 0 ✓ |
| `>` → `<` | exit **1** ✓ (`FIRES … False`) | exit **1** ✓ |
| `>` → `>=` | exit **1** ✓ (`HOLDS … False`) | exit **1** ✓ |

The sibling's fix does what this bean asked. My duplicate implementation of it is
dropped.

### Second defect, NOT covered by that fix — the producer was nondeterministic

`scan()` iterated `set(_LITERAL.findall(src))` — a set of **strings**, whose
order is randomised per process by `PYTHONHASHSEED` — so
`hardcoded_q0_literal_families_audit.py` emitted a different witness on every
run. Three back-to-back runs in one container: identical as a set (72 entries
each), different as a list every time; confirmed directly against
`PYTHONHASHSEED=1` vs `=2`.

For a witness that matters: byte-identical reproducibility is impossible, every
diff shows meaningless churn, and a `scriptHash` staleness can never be cleared
by re-running because the re-run never reproduces. Fixed with
`sorted(set(...))` — the one unsorted iteration in a file that sorts everywhere
else. Deterministic across `PYTHONHASHSEED` 1 / 7 / 99; detected set unchanged
at 72; assertions unchanged (still genuinely red, 72 vs baseline 71 — no
baseline touched).

I first attributed the churn to the mpmath version, having seen the payload move
when I installed libraries to repair the environment record. Two runs under a
*fixed* mpmath disproved it; the unordered set was the cause throughout.
