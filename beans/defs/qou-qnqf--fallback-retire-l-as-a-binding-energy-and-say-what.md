---
# qou-qnqf
title: 'Fallback: retire L as a binding energy and say what it is instead'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T06:48:04Z
updated_at: 2026-10-10T07:02:44Z
parent: qou-v2om
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

## ANSWERED (2026-09-05): the free-energy reading cannot supply the identification, and the reason is prior to every miss

Probe: `the_free_energy_reading_has_no_energy_spectrum_probe.py`, 6/6.
Lean: `QOU.Mass.FreeEnergyReadingIsSigned`, 11 theorems, sorry-free.

This bean asked "whether `L` is a binding channel at all", and the evidence so
far was three **misses** — the `A=2` ordering, no valley of stability, `31 %` at
`4He`. Misses are evidence about a formula. There is a prior fact about the
*reading*, and it is an identity in `q`, not a measurement at `q₀`.

### The state sum has a negative summand, always

A free energy is `-kT log Z` with `Z` a sum of **positive** Boltzmann factors.
That positivity is what makes `F` a Legendre transform, hence what gives it a `U`
and an `S` at all. Here the two `H₂` blocks carry eigenvalues `q` and `-q⁻¹`:

    bond    lambda_+ + d         lambda_- + d          z + d
    pp    1.10997858275138   **-0.90091828395574**   0.61268803714647
    pn    1.00552033498165   **-1.00537653172547**   0.50822978937674
    nn    0.90091828395574   **-1.10997858275138**   0.40362773835083

**Every `lambda_- + d` is negative.** Positivity would need `d > 1/q > 0`, and
the algebra's letters are `d ∈ {0, -h/2, d_pn, -h}`, all `≤ 0` — so the required
offset is not merely outside the range, it is **on the other side of zero from
all of it**, for every `q > 0`. Same shape as "no interface offset can close the
gap", and general in `q` rather than pinned at `q₀`.

Hence no real `E_-` has `exp(-E_-) = -q⁻¹ + d`: `exp` is positive and the factor
is not. **The `(1,1)` block has no energy.** So there is no `U` and no `S` for
`alpha L` to be or to differ from, and the step "this free energy is the binding
energy" has nothing to stand on. The three misses are downstream of this, not
independent of it.

### This bean's expensive option is not needed, exactly as it predicted

The bean already recorded "retiring the INTERPRETATION is not retiring the
QUANTITY", and the algebra makes that precise: the total `z + d` stays positive
because the `(2)` block outweighs the `(1,1)` block, so `L` is real, exact and
convention-D canonical in all 80 files. **No number moves.** The free-energy
*description* is also correct — the block already says "a signed observable over
a quasi-probability", which is a legitimate object. What goes is the sentence
after it.

### Scope, stated tightly

This does NOT show `alpha L` is not the binding energy by some other route. It
shows the reading that motivated the identification cannot supply it. The claim
stays open as a claim; what is settled is that this is not the reason for it.

### A conditional corollary I am NOT asserting

If one grants `kT = alpha` (the only temperature candidate, since `L` is
dimensionless "in units of `kT`" and `B = alpha L`) and applies Gibbs-Helmholtz
along the `q`-curve, the internal energy comes out ~0: `4He` gives `U = -0.0395`
against `F = 8.6817`, i.e. the whole thing is `-TS`. **My own objection: varying
`q` changes the block eigenvalues as well as the scale, so `q` is not a pure
temperature and this is not the textbook identity.** Recorded as indicative, kept
out of the probe's checks and the block. The finding needs no temperature.

### A detail the algebra hands over

For `pn` the two block factors nearly cancel:
`(λ₊+d) + (λ₋+d) = h + 2d_pn = h·δ/2 = 1.4380325618674e-4` exactly. The interface
the binding arc turns on is the near-null vector of the **unweighted** block sum
and survives in `z+d` only because `w₊ ≠ w₋`. The same letter is the near-null
vector of the `w̃` family the nuclear-jet level uses (`qou-gpb5`) — same algebra,
two different weight families, one distinguished letter.

- [x] Whether `L` is a binding channel at all — **the free-energy reading is not
      the channel, and cannot be.** `L` and every number from it stand.
- [ ] Decide the fate of `B_sym` and the `t7qv` / `qou-brng` arc's numbers.
      Unchanged by this: those numbers are `L`-derived and `L` is untouched; what
      needs revisiting is any prose calling them binding energies *because* `L`
      is a free energy.

## The prose sweep: DONE, and it found a defect en route (2026-09-05)

The remaining item was "decide the fate of `B_sym` and the `t7qv`/`qou-brng`
numbers". Scoped by finding every block that co-occurs "free energy" and
"binding", then reading each rather than bulk-editing.

### The sweep's actual finding: less to fix than expected

- **`QOU.BraidKnot.BsymLinearChain` needs nothing but a naming note.** `L : Bond
  → R` is an abstract parameter over a generic ring; every theorem is a statement
  about sums of whatever `L` is. Its line 8 already said `B_sym = α·ln(tr_free/
  tr_atom)` is "a definition + empirical claim". That hedge is now backed by a
  result. **No number recomputes** — the `t7qv`/`qou-brng` figures are `L`-derived
  and `L` stands.
- **`rem:markov-trace-gibbs-free-energy` is the one block that makes the
  inference**, and it makes it explicitly: the Markov trace "occupies the
  partition function slot", "energy and information appear Legendre-dual". It was
  already careful about ONE prerequisite — reading `E_0` as a finite temperature
  "requires naming the dynamics ... which the framework does not supply" — and
  silent about the second. Positivity is the second, and it fails. Caveat added.
- **`brunnian-binding-channel` deliberately left alone.** Its "free energy" is
  `log` of a multiplicative amplitude via the archimedean functor `τ = log`,
  separately proved (`QOU.Mass.ArchimedeanTraceBridge`, sorry-free). Different
  usage; my result does not bite there and asserting it would be the overreach
  this session has been correcting.
- `mba-step03-markov-trace` mentions only a witness filename. Nothing to do.

### A separate defect found while reading: a PUBLISHED WRONG READOUT

`thm:markov-trace-factorization` published

    Vhat_i(q) = z * (M_i)_11 + (M_i)_21

which is the readout of the **deprecated**
`computations/_deprecated/transfer_matrix_symbolic.py`, not the live one.
Measured against the Lean-proved `twoStrandTrace_eq` on a one-crossing matrix:

    bond      z + d        published        corrected (z*(M)_21 + (M)_22)
    pp    0.612688037146  1.128088744114   0.612688037146
    nn    0.403627738351  1.000000000000   0.403627738351
    pn    0.508229789377  1.064088425325   0.508229789377

The corrected readout reproduces `z + d` exactly; the published one misses every
bond and is not even monotone in `d`. The factorisation statement itself is
unaffected — what was wrong is the recipe for reading `(a_i, b_i)` off `M_i`.

**This is the same readout that produced `1.128089` in a retracted test earlier
in this arc**, already documented as a trap in
`no_within_generator_noncommutativity_probe.py`. The trap was recorded in a probe
and left standing in a theorem block. Fixed, and the block's correction table is
now witnessed by that probe (new §1b, 7/7) rather than resting on an ad-hoc run —
a published figure needs a check behind it.

- [x] Decide the fate of `B_sym` and the `t7qv`/`qou-brng` numbers. **Nothing
      recomputes; only the word "binding" was on loan, and it is now annotated.**

## 🛑 CORRECTION to my own note above: the pn near-cancellation is ONE fact, not two

The entry above says the `pn` letter is "the near-null vector of the `w̃` family
the nuclear-jet level uses (`qou-gpb5`) — same algebra, **two different weight
families, one distinguished letter**". The last clause is wrong, and measured
(probe §5, 8/8):

- **`w̃` is uniform on `H_2`** — both blocks there are the one-dimensional reps,
  `d_q = 1`, so `w̃ = 1/[2]_q!` on each. Hence "null vector of `w̃`" and "null
  vector of the *unweighted* block sum" are the **same statement** on two
  strands, not two families agreeing. `w̃` is not uniform at `H_3`
  (`0.1634, 0.6607, 0.1634`) or `H_4`, so nothing generalises.
- **`d_pn` is the average by construction**: `d_pn = -h/2 + h·δ/4`, verified
  `d_pn + h/2 = h·δ/4` exactly. So `h + 2·d_pn = h·δ/2` is *forced*, and would be
  exactly `0` at the colour-blind `-h/2`.

So the near-cancellation is **definitional** — the pn offset is defined as the
average of the other two, read through a measure that happens to be uniform only
at `H_2`. Not structure, not a coincidence between families, and not worth
chasing. I flagged it as "more interesting but more speculative"; it was neither.

The statement in `rem:bond-log-ratio-is-a-free-energy` is unaffected — it says
"near-null vector of the unweighted block sum ... survives in `z+d` only because
`w₊ ≠ w₋`", which is correct as written.


## 2026-10-10 — completed (survey for epic `qou-d8c7`, issue litlfred/qou#7547)

The question this bean held in reserve was answered on 2026-09-05 (section "ANSWERED": the free-energy reading cannot supply the binding identification), and the follow-on prose sweep is recorded as done the same day. Nothing in the body is still pending. The negative is listed under "Tried, failed (structural)" in the epic's catalogue; the kT question it touches stays open in `qou-892m`.


## 2026-10-10 (session_01ST9RpvTF7JHNdUNafrjf9J)
Core question judged resolved by the consolidation triage, but NOT closed: unchecked residual items / owner decision / rule-13a hold remain in the body.
