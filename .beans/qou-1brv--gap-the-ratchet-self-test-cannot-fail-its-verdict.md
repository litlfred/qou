---
# qou-1brv
title: 'GAP: the ratchet --self-test cannot fail — its verdict is a tautology'
status: todo
type: task
created_at: 2026-08-23T07:57:21Z
updated_at: 2026-08-23T07:57:21Z
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
