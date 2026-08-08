---
# qou-pjfu
title: 'GAP: em-coupling-chern-simons uses undefined qInt (pre-existing red on main)'
status: todo
type: task
created_at: 2026-08-08T12:03:32Z
updated_at: 2026-08-08T12:03:32Z
---


## Finding

`content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.lean`
does not compile on `main`:

    :41:20 Unknown identifier `qInt`      ((1 - 1/q) ^ 4) * qInt 5 q
    :50:24 Unknown identifier `qInt`      let prefactor := 45 * qInt 3 q

`qInt` is neither defined in the file nor imported. **Pre-existing** — verified
by compiling the unmodified `HEAD` version, which fails identically.

## Not a simple missing import

There *is* a `qInt` in the corpus —
`QOU.FluidDynamics.surreal_enstrophy_finite_modes`:

```lean
def qInt (q : K) (k : ℕ) : K := ∑ j ∈ range k, q ^ j
```

but its argument order is `(q, k)` while the call sites here are `qInt 5 q` and
`qInt 3 q`, i.e. `(k, q)`. So importing it would not typecheck, and "fix the
import" is the wrong repair.

Someone has to decide which `q`-integer this file means — the geometric sum
`∑_{j<k} q^j` with arguments flipped, or the balanced `[k]_q = (q^k − q^{−k})/(q − q^{−1})`
convention used elsewhere in the Hecke work (AGENTS.md §7a). That is a maths
convention call, not a mechanical one, so it is left open rather than guessed.

## Context

Surfaced while removing axiom-discharged conjecture instances (§3b-tax). The
de-laundering change to this file — dropping
`axiom chern_simons_correction_identity_holds` and the global instance that
discharged `ChernSimonsCorrectionConjecture` with it — is correct and applies
cleanly; the file simply remains red for this unrelated, older reason.
