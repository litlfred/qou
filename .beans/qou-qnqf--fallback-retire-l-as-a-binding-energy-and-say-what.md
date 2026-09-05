---
# qou-qnqf
title: 'Fallback: retire L as a binding energy and say what it is instead'
status: todo
type: task
created_at: 2026-09-04T06:48:04Z
updated_at: 2026-09-04T06:48:04Z
---


**FALLBACK / cleanup.** Opened 2026-09-04. Not a repair — a retraction, held in
reserve for when the repairs are exhausted.

`L = log(tr_free / tr_bonded)` reads naturally as a free-energy difference if the
Markov trace is a partition function, so `B = alpha L` is an interpretive
identification, not a derivation. `qou-mu1h` showed it produces the wrong
two-body ordering; the convexity result showed no monotone reinterpretation
rescues it, since `B` remains a sum of per-type constants and therefore convex in
`Z` with its maximum at an endpoint. Flipping the sign only moves the maximum
from `Z = 0` to `Z = A`.

So the live question is not what `L` should be rescaled to, but whether `L` is a
binding channel at all.

**The corpus's own numbers already point this way.** `magic-A-binding-formula`
gives `4He` at `29.956` against `28.296`, a miss of `+5.9%`. The bond chain gives
`8.68`, a miss of `-69%`. The exposition's binding predictions do not use `L`;
outside the two blocks written during the `qou-m3sh` arc, nothing in `content/`
references the bond constants at all.

- [x] **Answered: a free-energy difference.** Free energy of bond formation? A
      topological cost? It is a real, exactly-computable, convention-D-canonical
      quantity and it should be named correctly rather than quietly dropped.
- [x] **Inventoried:** 80 Python files, 61 probes, 31 witnesses, 6 exposition blocks.
- [ ] Decide the fate of `B_sym` and the `t7qv` / `qou-brng` arc's numbers.


## Worked 2026-09-04 — audit `docs/audits/2026-09-04-what-L-is-and-what-retiring-it-would-cost.md`

**What `L` is.** The Markov trace under convention D is a state sum: the Wenzl
weights `w+ = 0.752702113`, `w- = 0.247297887` sum to exactly 1 and are both
positive, so they are a genuine probability on the two `H_2` Wedderburn blocks,
and `tr_2(sigma + d) = E_w[lambda + d] = z + d` with `lambda` the block
eigenvalue of `sigma` (`q` on `(2)`, `-1/q` on `(1,1)`). Reproduces all three
bond constants exactly. Since `qou-m3sh` proved the chain trace is exactly the
product of these factors, `L = log(Z_free / Z_bonded)` is **a free-energy
difference in the standard sense**, dimensionless, per-interface additive, and
positive because every `z + d` lies in `(0,1)`.

Caveat recorded: the observable is SIGNED (the `(1,1)` eigenvalue is negative),
so it is a free energy over a quasi-probability. The sign is the
`sigma`/`sigma^-1` split, i.e. the p/n distinction itself — which is why the
Jensen intuitions in `qou-mu1h` needed checking rather than assuming.

**What retiring it would cost.** 80 Python files, 61 of them probes, 31 witness
JSONs, 6 exposition blocks. Not a small cleanup — this bean was proposed as the
honest option and the inventory says it is also the expensive one.

**But the expense is avoidable.** Retiring the INTERPRETATION is not retiring
the QUANTITY. `L` stays a correct free energy in all 80 files; only "and this is
the binding energy" is in question. Minimal honest action is a re-labelling:
keep every computation, mark the `B = alpha L` identification as an open
interpretation in the six exposition blocks and wherever a probe compares
`alpha L` to AME, and leave the numbers standing.

- [x] **Done (owner decision Q2, 2026-09-05).** One canonical block,
      `rem:bond-log-ratio-is-a-free-energy`, wired into
      `sec:canonical-closure-as-link`: states that `L` is a free-energy
      difference over the Markov state sum (with the signed-observable caveat
      and the three closed forms), and marks `B = alpha L` as an open
      interpretation with the evidence against it — the A=2 ordering, the
      no-valley result, and the 31 % of helium-4. The two blocks that present
      the bond constants (`rem:canonical-trace-factorises-over-chain`,
      `rem:pn-bond-cannot-be-extremal`) now point at it rather than each
      restating the caveat. Validation clean.

      Nothing retracted, no number moved: every `L` in the corpus stands as a
      correct free energy. The block also records that the corpus's working
      binding route is a different one — the Layer-1 canonical `|tr_M(q_0)|`
      table, reaching -0.16 % to +5.87 % on D, T, 3He and 4He.
