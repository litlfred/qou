---
# qou-n9qf
title: 'Delta_tr IS extensive and at A<=4 that is the failure: flat 0.29/nucleon vs B/A moving 6.4x, and two corpus scales for it differ 5.5x'
status: in-progress
type: task
created_at: 2026-09-03T10:37:26Z
updated_at: 2026-09-03T10:37:26Z
---

Probe: computations/qbeta/qbeta_extensivity_is_the_failure_probe.py (5/5). Refines qou-imcd / qou-78pt rather than disputing them.


## Measured (four atoms, from the committed deciding-test witness)

| atom | A | `Delta_tr` | `Delta_tr/A` | B (MeV) | B/A | deficit/nucleon |
|---|---|---|---|---|---|---|
| ²H | 2 | 0.55654466 | 0.27827233 | 2.2246 | 1.112 | 5.11 |
| ³H | 3 | 0.88853613 | 0.29617871 | 8.4818 | 2.827 | 12.20 |
| ³He | 3 | 0.89290858 | 0.29763619 | 7.7180 | 2.573 | 11.05 |
| ⁴He | 4 | 1.11980901 | 0.27995225 | 28.2957 | 7.074 | **32.30** |

- relative spread of `Delta_tr/A`: **0.0672**
- relative spread of `B/A`: **1.7552** — *26x larger*
- `B/A` max/min: **6.36**
- deficit per nucleon: **5.11 … 32.30**, i.e. **not a constant**

## What this says

`Delta_tr` — the quantity `B = Q_beta(n) . (tr_M(W_free) - tr_M(W_atom))`
actually evaluates — **is extensive**: flat to 6.7 % per nucleon across
A = 2..4. And that is precisely the obstruction, not the achievement. `B/A`
moves 6.4x over the same four atoms, so the falling "fraction supplied"
(19.6 %, 8.2 %, 9.1 %, 3.1 %) is not four separate disappointments: it is one
flat number divided by a rising one.

**Consequence for every add-a-term attack.** The per-nucleon deficit runs
5.1 → 32.3. A missing term that is any fixed multiple of an extensive quantity
cannot close that, whatever the multiple. This is also the structural reason the
interface deciding test (`qou-bmz8`) returned every candidate near spread 2: it
asked for one constant `c` with `R_X = c . S_X(w)` while `R_X` is dominated by a
term varying 6.4x and the candidates supply flat ones. That test was fair; the
answer was structural rather than unlucky.

**The calibration atoms are the wrong place to check extensivity.** `B/A`
reaches its ~8.5 MeV/nucleon plateau only well above A = 4; at A = 2 it is 1.11.
All four atoms sit where the semi-empirical surface, Coulomb and pairing terms
dominate. "The extensive term has the right shape" is a claim about the
asymptotic regime being tested against non-asymptotic data — it can be true and
useless at the same time.

## Relation to prior work — refining, not disputing

`qou-imcd` measured the A-exponent of `log Z(3A)` as exactly 1.0 and concluded
the residual is "a pure multiplicative constant, not a shape error";
`qou-78pt` calls it "a pure convention choice". **Neither is disputed.** Both
measure the **normaliser**. What is added here is the same measurement on the
**binding law's own quantity**, which is extensive too — plus the observation
that at A <= 4 extensivity is the problem.

## 🛑 Two corpus figures for the same quantity differ by 5.5x — for the owner

Both are presented as the framework's extensive energy per nucleon:

```
qou-imcd, via the normaliser :  3 . log(1 + q0^2) . m_e  = 1.2309 MeV/nucleon
the binding law, via the trace:  Q_beta . <Delta_tr/A>    = 0.2253 MeV/nucleon
                                                    ratio = 5.46
```

with correspondingly different deficits against the 8.5 plateau: **6.91x**
(normaliser) versus **37.72x** (binding law). They are different objects with
different energy scales, so this need not be an error — but the corpus offers
both as "how far off the extensive term is", and they cannot both be that.
Which is the prediction changes what "a pure multiplicative constant" is a
constant *of*.

## Todo

- [ ] **Owner:** which of the two scales is the framework's prediction for
      energy per nucleon? The 6.91x and 37.72x deficits are quoted in different
      places for what reads as the same claim.
- [ ] Test the prediction this makes: if `Delta_tr` is extensive and the data
      is not, the framework should track `B` *better* at larger A, where `B/A`
      flattens. A = 6..16 would show it. Cheap on the character route, which
      reaches n = 12 already and is the validated path (see the Case C trap in
      `.claude/agent-memory/compute-precision-auditor/MEMORY.md`).
- [ ] The missing term must be **strongly A-dependent in the light region** —
      surface-like — not a constant multiple of anything flat. That is a real
      negative constraint on candidates and it is derived, not guessed.
