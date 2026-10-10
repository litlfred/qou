---
# qou-pjfu
title: 'GAP: em-coupling-chern-simons uses undefined qInt (pre-existing red on main)'
status: completed
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


---

# RESOLVED (2026-08-08) — the convention was DECIDABLE, not a guess

This bean said choosing between the geometric and balanced q-integer "is a maths
convention call, not a mechanical one, so it is left open rather than guessed".
Correct caution -- but it IS decidable, because the file computes alpha_EM^-1, a
measured constant:

    geometric  -> 150.4821415   (9.8% off CODATA 137.035999177)
    balanced   -> 137.0359995   (2.6 ppb)

So the intended object is the BALANCED [k]_q.  The file now uses the existing
QOU.Mass.QHookDimensionBalanced.qIntBal (argument order flips: qIntBal is (q,n),
the old call sites were (k,q)) rather than adding a ninth q-integer.

lean-direct EXIT 0 on the file (one pre-existing unused-variable warning, not an
error).  The dep olean QHookDimensionBalanced had to be built first -- it is one
of 213 library modules with no olean in the lake-cache.

SCOPE: this fixes the IDENTIFICATION of a symbol, not the physics.  The 2.6 ppb
carries no evidential weight -- the file itself calls kappa = 8q empirical with
"no structural derivation linking su(3) gluon dimension to alpha_EM", so the form
was shaped against this target.  The number is a FINGERPRINT to recover which
function the author meant.  The conjecture stays a conjecture.

General derivation of WHY balanced is canonical (bar-parity, Hecke structure
constant, sl_2 weight-string symmetry):
docs/audits/2026-08-08-q-integer-convention-derived.md.  Corpus-wide reconcile
filed as qou-qint.
