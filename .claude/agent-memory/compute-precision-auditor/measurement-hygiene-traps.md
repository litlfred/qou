# compute-precision-auditor — detail file: measurement-hygiene traps

Read on demand. Summarised in `MEMORY.md`; this file carries worked cases.
Every trap below is one I actually fell into during bean `t7qv`
(2026-08-31/09-01) and caught before or shortly after publishing. Each cost a
wrong claim that had to be withdrawn.

## TRAP — `abs(x) > tol` on a quantity with a PROVEN sign

**Worked case.** The aggregation gap `free - atom` is `>= 0` structurally,
because aggregation is a relaxation and `x_p + x_n` is an explicit feasible point
of the aggregate with cost exactly `free`. I detected "gap opens" with
`abs(gap) > 1e-9`. What that caught was a run of **negative** gaps at
`-1.79e-11`, `-1.79e-10`, `-1.79e-9` — structurally impossible, i.e. LP solver
noise scaling with the perturbation. I reported a knife-edge radius of `3e-8`
off the back of it. There was no knife edge at that radius; along that direction
the gap never opened at all, even at a 63 % perturbation of the cost.

**Rule.** If you can prove a sign, assert the sign. `gap > tol`, never
`abs(gap) > tol`. And count the sign violations you see — if a "structurally
impossible" value shows up at all, that is your noise floor announcing itself,
and it is far above machine epsilon.

The corrected measurement (positive-only, relative threshold) found zero spurious
negatives and a real boundary established by **linear scaling over six decades**
(`gap/eps` constant to `< 5e-8` from `1e-1` down to `1e-6`) rather than by a
radius. A scaling law is a much stronger boundary claim than a threshold
crossing.

## TRAP — single-root bisection on a function that has 0 or 2 roots

**Worked case.** I located dual-vertex transitions by bisecting the margin over
`h in [0.02, 3]`, assuming one sign change. For one parameter choice the margin
has **no** root in that range and the bisection returned `h* = 2.0009` — a
number with no meaning, which I then tabulated alongside real ones and used to
claim a non-monotonicity.

**Rule.** Scan a grid for sign changes FIRST, bisect only inside a bracketed one,
and return `None` when there is no bracket. Report the bracket count. The
committed probes do this and the proton/neutron values were never affected — but
only because they happen to have a single crossing each, which I had not checked.

## TRAP — a linear solve that is not verified is not a solve

**Worked case.** Solving `v_n . W = v_p` for the weak transition operator, I built
the matrix of right-multiplications and used `lu_solve(M.T, ...)`. The relation
is `v_n . W = sum_k W_k (v_n . b_k)`, so the columns must be `v_n . b_k` — the
transpose was simply wrong. It produced a plausible-looking six-component `W`,
whose verification residual was `1.3e-1`. Corrected, it is `1.15e-41`.

**Rule.** Every solve gets a residual printed next to its answer, always. A
wrong answer to a linear system looks exactly like a right one.

## TRAP — assertion thresholds that encode your PROSE rather than your finding

Three separate probes failed on my own thresholds while the underlying
measurement was correct:

* asserted the saturation spread was `< 5e-4`; it is `5.9e-4`;
* asserted all-pairs is `4x` less ordering-sensitive; it is `3.4x` and `3.7x`;
* asserted `b_2` dominates by `> 3x` at both nucleons; it is `8.1x` at the proton
  and `1.9x` at the neutron.

Each time the sentence had been written before the number was read back.

**Rule.** Write the assertion from the printed value, not from the sentence you
intend to write about it. And when a threshold fails, check which of the two is
wrong before touching either — twice it was the prose, once (the monotonicity
check) it was a sort whose tie-break silently inverted the comparison.

## TRAP — a container reset can move you to a DIFFERENT BRANCH silently

**Worked case, and this one nearly produced two fabricated defect reports.** A
mid-session container reset dropped me from
`claude/mt7r-archimedean-eval-2026-08-24` onto
`claude/omegaorder-exponent-group-2026-08-16`. Same probe, same inputs, different
`pyhecke`: a transition I had measured at `0.477184636796` came back
`0.679319435`, and `atom_gen_chains` open-coded `-h/2` where my branch has
`D_PN`. I was one step from filing both as bugs.

**Rule.** After any reset — and the tell is `ModuleNotFoundError` on `mpmath`,
since the reset also wipes `pip install` — run `git branch --show-current` before
running anything else. If a previously-measured number changes, suspect the
checkout before suspecting the code.

## TRAP — `--depth=1` poisons `merge-base` and every ancestry count

Recovering the branch after that reset, I used `git fetch --depth=1`. The repo
stayed shallow (4 grafts) and afterwards `git merge-base HEAD origin/main`
returned **empty**, while `git rev-list --left-right --count` reported `7` vs
`33685` — both meaningless. Substituting an empty merge-base into
`git log -1 $(...)` silently reports `HEAD` instead, which is how the number
looked plausible.

**Rule.** `test -f .git/shallow` before trusting any ancestry command.
`git fetch --unshallow` first. The true counts here were `119` vs `1343`.

## NOTE — the `y_lambda` tables are stored f64, and that sets a floor

Agreement between anything routed through `nucleus_real_sdp.load_cost` and an
independent computation bottoms out around `1e-8`, not machine epsilon. Measured:
`6.1e-9` on the deuteron free trace against `tr_3(p) tr_3(n)`, and `5.6e-9`
between two determinations of `L_pn`. `h3a_frobenius_gram_offdiagonal_probe` sees
the same `1.1e-8` scale. Quote seven digits from that path, not fourteen, and do
not read a `1e-9` residual there as a defect.

By contrast, quantities computed entirely within one route reach machine
epsilon — the chain transfer scalar `F` is prefix-independent to `2.8e-16`, and
bond constants measured as `H_6`/`H_9` trace ratios agree with the closed form
`-log(z + d)` to `1.3e-13`. Knowing which floor applies to which number is the
difference between reporting a cross-check and reporting a discrepancy.

## TRAP — exact at both endpoints is not exact in between

**Worked case, and it caught two arcs independently.** The writhe exponent of a
`p-n` bond was in dispute: production said `e_pn = -delta/2`, `qou-brng` derived
`+delta/2` by interpolating from `e_pp = +1` and `e_nn = -1`, and I derived
`+delta/2` from the operator identity `sigma - beta h = (1-beta) sigma + beta
sigma^-1`. Two independent routes, same answer, opposite sign from production —
which reads like confirmation.

Both were wrong, and by a factor of `217`. The bond is a *sum* of two crossings,
the Markov trace is linear, and the writhe factor `(1-h)^(e/2)` is defined **per
diagram** — a formal sum of two diagrams is not a diagram and has no writhe. Done
correctly the effective exponent is `e_eff(beta_pn) = 0.149437`, not `0.000688`.
The averaged-exponent form and the per-diagram form agree **exactly** at
`beta = 0` and `beta = 1` and nowhere else, so `p-p` and `n-n` — the only two
bonds anyone had checked — could never have detected it. An interpolation
anchored on those two points reproduces itself and looks like a derivation.

**Rule.** When a formula is anchored on endpoints, the endpoints are not evidence
— they are the construction. Test it at an interior point against an
independently-derived value, and be most suspicious when the interior point is
the one you actually care about. Here `e_eff` is concave, so the interpolation
understated it at *every* interior point; the two candidate signs were both
"zero to three decimals" and the argument was over the noise.

**Corollary for averaging.** Before averaging a parameter that sits in an
exponent, check whether the operation the physics performs is a sum or a product.
`f(mean(x))` and `mean(f(x))` coincide only for affine `f`. The whole dispute was
`108x` smaller than the error that framing choice introduced.

## THE BIG ONE — you are probably computing blocks whose weight is ZERO

**Read this before optimising any Hecke trace.** Convention D puts the
three-strand q-antisymmetriser in the radical (`y_alt = 0`). That is the `N = 2`
specialisation, and it does **not** stop at `n = 3`: **every partition with
`>= 3` rows carries weight exactly zero, at every strand count.**

Measured against `load_cost`: `n = 6` has **4 nonzero blocks of 11**; `n = 9`
has **5 of 30**. At `n = 12` it is **7 of 77**, and the seven have dimensions
`1, 11, 54, 154, 275, 297, 132` — largest **297**, built in `0.04 s`.

For scale: `qou-sv7h` reports a Rust LP-accumulator kernel taking **278 s for a
single `A = 2` deuteron**, and `qou-w2vy` documents `binding_energy` as unable to
run for any `A >= 2`. Both are working on a computation whose cost is dominated
by blocks that contribute nothing. `A = 4` was believed to need `H_12` and to be
out of reach; it takes under a second.

The surviving weights have a closed form — for two-row `(n-k, k)`:

    y = [n - 2k + 1]_q / Z ,    Z fixed by  sum_lambda y . dim = 1

with `[m]_q` the balanced q-integer **at `q0`**, and
`dim(n-k,k) = C(n,k) - C(n,k-1)`. Verified against `load_cost`: **exact** at
`n = 9`, and `1.14e-8` at `n = 6` — which is that path's own stored-f64 floor,
so the closed form is the *more* precise of the two. There is no `y_lambda`
source for `n = 12`; this is how you get one.

**Reach, and note the largest block is NOT at the largest `k`** — at `n = 18` it
sits at `k = 7`, not `k = 9`, which is easy to get wrong by inspection:

    A=4  n=12  largest    297   dense, comfortable
    A=5  n=15  largest   2002   dense, comfortable
    A=6  n=18  largest  13260   needs sparse handling
    A=7  n=21  largest  90440   out of reach

**Cross-validate before believing it.** Reconstructed-weight `H_12` reproduces
`L_pp`/`L_pn`/`L_nn` to `1.3e-13`, band-routed bonds at separation 2 *and* 3 to
`3.4e-13`, and the `ppn` triangle to `3.69e-10` — each against an `H_6`/`H_9`
computation that does not share the weight source.

## TRAP — the bonds in an atom word DO NOT COMMUTE

Inserting the same set of bonds in a different order gives a different trace:
**`11.12 %` spread over the six orderings of one `A = 3` triangle, `38-40 %`
over `4He`'s six bonds** (`B` ranging `8.04 .. 12.43 MeV`). That is far larger
than the framed-vs-writhe-normalised question two probes were spent on.

Four of the six triangle orderings agree exactly; the two outliers are precisely
those with the band-routed bond sandwiched between the two adjacent ones — the
only pair that fails to commute. `atom_gen_chains` fixes an **interleaved**
order, `N0 . N1 . b01 . N2 . b02 . b12 . N3 . b03 . b13 . b23`, which had never
been lifted to the strand picture; a probe that appends all bonds after all
nucleon words is computing a different quantity (mine was, and it needed a
correction).

**Rule.** Quote a bond order with any atom trace, and take it from
`atom_gen_chains` rather than inventing one.

## TRAP — a re-run "MOVED" verdict is usually the comparison, not the computation

Measured across 99 producers in two sweeps (beans `qou-y98b`, PRs #6454 / #6493):
**every** apparent mover was the harness or the invocation. Zero were the
mpmath-version environment drift the sweep was built to detect. Five distinct
causes, in the order they cost me time:

1. **A field name the mask does not list.** `build_s`, `build_seconds`, `ms`.
   The mask cannot be a fixed list — a producer names its timing whatever it
   likes.
2. **A timing formatted into PROSE**, where no field-name mask can reach it:
   `assertions[1].source = "... built 0.04s; reach by A: {...}"`. Normalise
   timing-shaped substrings too — `\b\d+\.\d+\s*s\b` -> `<T>`. And note this is
   *not* a producer defect to fix: that assertion's own predicate is
   `build_s < 60`, so the measured time IS its evidence and belongs there.
3. **A CLI argument.** `qcollatz_vtwo_domain_stable_probe` takes
   `depth = sys.argv[1]`, default 14; the committed witness was made with 22.
   Run bare it reports nodes 52 -> 24, depth 22 -> 14, three descent violations
   -> two, nine histogram rows gone — and nothing drifted. **Read the invocation
   out of the witness** (`result.depth` records it) rather than assuming the
   default.
4. **A CWD-relative write.** Several producers `open('<stem>.witness.json','w')`
   with no path. Run from the repo root they create a stray witness AT THE ROOT
   and leave the real one untouched, which reads as "the producer did not
   stamp". Run each from its own directory.
5. **A genuinely stale consumer** — the one real finding, and the reason the
   sweep is worth running. `operator_selection_active_set_probe` does not solve;
   it READS `nucleus-real-sdp-*.witness.json` and republishes their duals. Its
   deuteron entry was `active_blocks [(2,1,1,1,1),(2,2,2),(3,3)]`,
   `y0_star -0.014433988` against a live upstream of `[(4,2),(5,1),(6,)]`,
   `y0_star +0.06426714876225478`. The upstream was regenerated by `393fec6bfa`,
   whose message claims "full propagation"; it did not reach this consumer.
   **Nothing detected it, because a stale consumer is self-consistent and its
   assertions still pass — 5/5 before and after.**

**Rule.** Before calling a re-run diff a defect, rule out 1-4. And a producer
that only *reads* other witnesses is the one worth re-running, because its
staleness is invisible to every check that looks at a witness in isolation.

## STABLE — the `independent` verdict needs a cone, and the cone must exclude the emitter

A file-local grep answers "does this source mention q0", which is not the
question. A transitive import cone answers it — but a naive one marks **every
witness-writing producer** as reading q0, because `qou_substrate/witness.py` is
imported by all of them and legitimately mentions `q_parameter`, `q_at`,
`q_muon_at`, `_q0_value_for_anchor`: it is the module that STAMPS the anchor.
Exclude `witness`, `witness_base`, `_precision` from the cone.

Measured on 10 producers a grep called clean: **3 of the 10 do read q0** —
`gs_filtration_jet_shape_magic_probe` (depth 2 via `hecke_core_symbolic`),
`shell_shadow_price_magic_contrast_probe` (depth 2 via `mass_endomorphism`,
plus `markov_peel`, `mass_at_3A_proper`, `_li_2_q_util`, ...), and
`milnor_a4_deficit_h_form`, which hardcodes the proton pin as
`sp.Rational(2584370278640139188197914756009, 2328306436538696289062500000000)`
= `1.1099785827513805166...` — 16 significant digits of agreement with the
canonical `1.1099785827513808075...`, rel dev `2.62e-16`, denominator
`2^8 * 5^40` (decimal-exact from a ~17-digit string, so not `Fraction(float64)`
but carrying its precision, under a field named `q0_pin_exact_rational`).
Declaring any of those three `independent` would have written a silent claim —
exactly what `build()`'s `require_declared` rule exists to prevent.

## TRAP — a q0-anchor manifest entry is INERT for a hand-rolled producer, and the count is not small

Measured 2026-09-03 on the anchor ratchet's 35-witness refill (`qou-y98b`):
**22 of the 27 proton producers were already declared `physical_proton` in
`computations/q0_anchor_manifest.json`, and their witnesses were unstamped
anyway.** 18 of those 22 hand-roll their witness — `json.dumps` +
`write_text` — and so never enter `WitnessBuilder.build()`, which is where the
manifest is read.

So: **"the stem is in the manifest" is not evidence the witness is stamped**,
and a triage pass that treats a manifest entry as done will skip the producers
that most need fixing. Check how the producer WRITES before believing a
declaration:

    grep -l 'WitnessBuilder' <producer>     # manifest route works
    grep -l 'write_text\|json.dump' <producer>   # manifest is inert

The fix for a hand-rolled producer is a producer-side `"q0Anchor"` key in the
witness dict. Leave the manifest entry in place — it states the pin correctly,
it is just not what stamps the file.

The ratchet's own header documents this mechanism; what was missing was the
measurement of how much of the live refill it accounts for. Two-thirds of it.

## TRAP — "a q0 value is in the source" does not mean "a pin is baked in"

`computations/audits/producer_baked_pin_audit.py` decides by VALUE (it parses
and evaluates literals and `Rational`/`Fraction`/`mpf`/`Decimal` calls), which
is what closes the import-cone trace's documented blind spot: a pin written as
`sp.Rational(num, den)` is invisible to a `1.1099785` prefix match.

But a `BAKED_PIN` verdict answers only "is a q0-valued literal present". Two
of the 27 proton producers flag, and **neither bakes a pin** —
`alpha_scale_is_outside_the_trace_probe` and
`extensive_carrier_scale_inversion_probe` carry `1.10997858` inside a
`Q_50_DIGIT_STR.startswith("1.10997858")` **guard** asserting the proton
anchor (added by a Copilot review on #6443). Read as a pin, they would have
been mislabelled — when in fact they self-assert the correct anchor, which is
stronger evidence than either audit gives.

Read the line before acting on the verdict.

## TRAP — one tolerance cannot serve anchor separations four orders apart

Writing that audit, my first draft used a single 1e-6 relative window. The
proton/muon gap is 1.16e-8, so the window was ~100x too wide — and it did NOT
blur the answer, it **silently returned the first candidate**: the retired
MUON pin was reported `proton` on 21 lines of one file.

There are FOUR anchors, not two — three different numbers are all called "the
muon q0" (retired self-certified pin; lepton-tower at CODATA 2018; at CODATA
2022), diverging at the 13th significant digit. The separations:

    proton vs any muon            1.16e-8
    muon-retired vs -codata2022   7.7e-11
    muon-retired vs -codata2018   2.8e-12

Hence three windows, and an explicit `ambiguous` verdict when a value matches
more than one. A pin truncated to 8 significant digits is `1.1099785...`,
which is a prefix of every anchor and is genuinely unattributable — say so
rather than assigning it to the nearest.

General form, worth more than the instance: **a tolerance looser than the
separation it is meant to resolve does not produce an uncertain answer, it
produces a confident wrong one.**

## BASELINE — baked q0 pins in `computations/`, 2026-09-03

    python3 computations/audits/producer_baked_pin_audit.py --all --quiet

    369 of 4387 files bake a q0 pin
      196 files  proton
      174 files  muon-retired      <- retired 2026-08-22
       46 files  muon-codata2018
       39 files  muon (vintage unresolvable from the digits present)
       29 files  ambiguous:truncated
        7 files  muon-codata2022   <- the LIVE canonical anchor

The `muon-retired` 174 is the **producer-source** surface and is a different
population from the ~40 witness FILES carrying the same string that AGENTS.md
records. Re-measure before quoting; run `--selftest` first (exits non-zero if
the matcher has stopped seeing a pin it provably used to see).

## TRAP — a "before" count taken from the tree your own branch is mutating is not a before count

AGENTS.md already records this for the witness-staleness sweep — *"baseline
from git (`git show origin/main:<witness>`), never from a tree your own sweep
writes to"* — and I broke it anyway, on 2026-09-03, in the same session where
I was quoting that rule.

**What happened.** Counting unstamped witnesses that carry a *near-miss* anchor
key (`q0_anchor` where the audits read `q0Anchor`), I measured the working
tree mid-session and got **14**, of which "4 are in this refill". Both numbers
reached a PR body, an audit doc and a commit message before being re-measured.

Against `origin/main`, a baseline the branch cannot write to: **17** — and this
branch fixed **11**, not 4. My own already-landed declarations had silently
removed their witnesses from the population I was counting.

**The tell was in the breakdown, not the total.** I recorded the sub-counts as
12 `q0_anchor` / 1 `anchor` / **1** `q0_pin`; the true split is 12 / 1 / **4**.
Three `q0_pin` witnesses were missing because I had already fixed them. A total
that is merely *low* looks like an honest count; a sub-count that has collapsed
to 1 is a fingerprint of self-contamination. **Always print the breakdown, and
look at the small buckets.**

**The rule, stated so it generalises:** any figure describing "the state before
this work" must be computed from a **revision**, not from a path. Concretely:

```python
blob = subprocess.run(['git','show',f'origin/main:{path}'], ...).stdout
```

and enumerate with `git ls-tree -r --name-only origin/main <dir>` rather than
`Path.rglob`, so the denominator is pinned to the revision too. Report both
ends (`before` at a named revision, `after` at `HEAD`) — a single number
without a revision attached cannot be checked by the next reader.

**Cost when it is not caught:** the wrong figure had already reached three
durable artifacts. Two were editable; the commit message was not.

**A second way to land in this trap, added 2026-09-05:** `git stash`. It
*looks* like it pins a revision — "put my changes aside and measure what was
there before" — and it does not: it reverts only the WORKING TREE, so any
change you have already committed on the branch stays in the measurement. See
"`git stash` is not a baseline" below; same rule, different mechanism, and the
stash form is more dangerous because it reads as revision-shaped.

## TRAP — a producer's ARGUMENT LIST is part of what its committed witness records

Hit **twice in one session** (2026-09-03/04), on two unrelated producers, in
both cases while re-running only to add a `q0Anchor` stamp. Re-running a
producer with different arguments than its committed witness was made with does
not produce a stamped witness — it produces a **different, smaller** witness,
and the diff reads as a stamp plus "some values moved".

**Case 1 — caught by an assertion.**
`wlambda_covariance_epic_M1_edge_ratio_decomposition` takes `nmax` and
**defaults to 40**; its committed witness records **46**. The default run
failed one assertion (*"needs nmax >= 46, got 40"*) and rewrote the witness
with a shorter table. The failing assertion is what saved it.

**Case 2 — nothing would have caught it.**
`bpp_higher_a_resumable_driver` reads
`A_LIST = [int(x) for x in args] or [5]`. Invoked as `driver.py 5` it computes
**A=5 only**, while both committed witnesses (`bpp-`/`bnn-higher-a-resumable`)
record `by_A = {2,3,4,5}`. It would have exited 0, written a valid witness, and
silently dropped three A values. It sat in my runner across **four launches**
before I read the arg handling. A downstream consumer would then have failed
for an unrelated-looking reason: `chain_binding_closed_form_probe` skips a
species on `if len(As) < 3: continue`.

**The check, before re-running anything:**

```python
# what was the witness actually built with?
d = json.load(open(witness))
d.get("invocation", {}).get("argv")      # often None — do not stop here
sorted(d.get("data", {}).get("by_A", {}))  # the SHAPE of the payload is the evidence
```

`invocation.argv` is frequently absent (it was `None` on both of these), so the
reliable signal is the **payload's own shape** — a range, a table length, an
`nmax`/`A_LIST`/`depth` field, the set of keys under a per-parameter dict.
Compare it to what your invocation will produce, *before* you run.

**And add it to the stamp-only gate.** A volatile-field mask compares values
that exist on both sides; it says nothing about keys that have **disappeared**.
Check the payload shape explicitly (`by_A == {2,3,4,5}`), or a truncation
passes as clean.

Related, same session: `qcollatz_vtwo_domain_stable_probe` takes `depth` as
`sys.argv[1]` defaulting to 14 against a committed 22 — nodes 52→24. Three
producers, one shape of mistake.

## TRAP — a "restore" that also reverts the thing you are testing WITH

Writing the q0 pin-flip test (`computations/audits/q0_pin_flip_test.py`,
2026-09-04): the harness patches `computations/q0_anchor_manifest.json` to force
a stem to the muon anchor, re-runs the producer, diffs, and restores the tree
between producers because **producers write sibling witnesses**. The restore was
`git checkout -- computations/`.

The manifest **lives under `computations/`**. So the restore after the first
producer reverted the pin patch, and every producer after it ran at the
UNFLIPPED pin — trivially showing "no move". The run reported *"0/7 subjects
moved, all verdicts hold"*, which was **vacuous**: six of the seven were never
actually tested.

**What caught it was the second positive control**, which read `no move` where
it had to move. A single control would not have: the first producer ran under a
correctly-patched manifest and moved, so `any(control_moved)` was True and the
run looked verified. The gate is now `all(controls moved)`, not `any`.

Two generalisations worth more than the instance:

1. **A restore step is part of the experiment, not scaffolding around it.** Ask
   what else lives under the path you are reverting. Anything the harness itself
   installed — a patched config, an env fixture, a stub — is inside the blast
   radius of a directory-level `git checkout`.
2. **Use MORE THAN ONE positive control, and require ALL of them.** One control
   verifies the harness at one moment; a harness that decays partway through a
   run (as this one did, after the first iteration) passes a single-control
   check and fails everything after it silently. This is the same shape as a
   detector whose first pass is sound and whose later passes are not.

The corrected run: 2/2 controls MOVED, 0/7 subjects moved. Only the second
number was ever in question, and only the fixed harness could answer it.

---

## TRAP — a new key shape in a shared checkpoint is an API change to every reader of it

**Established 2026-09-04, PR #6581, by breaking two probes with my own change.**

Making `bpp_higher_a_resumable_driver` resumable meant banking an in-flight row
cursor into the checkpoint it already used for completed terms, under a new key
suffix `|partial` whose value is a **dict** where every other value is a numeric
string. I excluded those keys in the driver and stopped there. Two sibling
probes read the **same file**, and both die:

    TypeError: cannot create mpf from
      {'next_row': 867, 'acc': '2069.9658...', 'dim': 1638}

Two things generalise:

- **`str.split(sep, maxsplit)` does not raise on an extra field.** The consumers
  do `a, w, lam = k.split("|", 2)`; the fourth field lands inside `lam`, the
  unpack succeeds, and the failure surfaces one line later as a type error that
  names neither the key nor the producer that wrote it. A malformed-key guard
  written as "the unpack will catch it" catches nothing.
- **Find the readers before writing the key, not after.** `grep -rln <basename
  of the state file>` is the whole audit and takes one command. Here it returns
  three files and the producer is one of them.

A shared checkpoint / cache / bank file is an interface. Adding a key namespace
to it is a breaking change to every consumer, exactly like adding a field to a
witness schema.

## TRAP — "has ≥ N points" is not a completeness guard, and a resumable producer is what exposes that

**Same PR, and this is the one that could have published a wrong number.**

`chain_binding_closed_form_probe` aggregates a two-species bank and guarded only
with `if len(As) < 3: continue`. That admits a state which is not merely
incomplete but *misleading*:

- **one species banked** — the `continue` skips it silently, and the probe then
  `KeyError`s at `params["nn"]`. Loud, but for the wrong reason, and only by
  luck: a probe that happened not to dereference the absent species would have
  written a witness.
- **both species banked at DIFFERENT A-sets** — both clear `len(As) >= 3`, the
  closed form is fitted on unequal ranges, and every pp-vs-nn comparison runs
  across A-sets that do not correspond. Nothing raises. The witness records a
  comparison that was never made.

**The point is that resumability turns the second case from a corner into the
default.** Before `--budget-seconds`, a bank was written by runs that either
finished a species or contributed nothing; afterwards, a bank mid-drain
routinely holds pp at `{2,3,4,5}` and nn at `[]` or `{2,3}`. Measured, while
fixing this: exactly that state.

So when you make a producer resumable, re-read every **consumer's** assumption
about the states its input can be in. The guard that was adequate against
"finished or absent" is not adequate against "partial", and the failure is
silent in exactly the case that matters.

The sibling `logratio_exactly_extensive_probe` had the species half of this from
a Copilot review; neither had the A-set-agreement half.

## STABLE — the strongest verification of a compute refactor is a stamp-only diff of the production run

Same PR. Two verification modes were written and both passed — `--verify-rowwise`
(9/9 partitions identical to 40 digits) and `--verify-cache` (140/140 entries
bit-exact by mpmath's internal `(sign, man, exp, bc)` tuple). Both are worth
having and neither is the real evidence.

The real evidence is that re-running the **whole** producer under the new code
path produced a witness whose diff against the committed one is **two lines**,
both of them the q0 stamp: every `B_tot`, every per-bond and marginal figure,
byte-identical. A spot-check says the new path agrees on the cases you chose;
the diff says it reproduces the original production arithmetic.

**Prefer this shape of check whenever a producer is cheap enough to re-run.** It
needs no tolerance, no sample, and no judgement about which cases were
representative — and it is the same instrument as the witness-staleness triage,
pointed at your own change.

Corollary for serialization: `mp.nstr` is lossy, so a cache persisted as decimal
strings would make a resumed run *disagree* with an uninterrupted one by a few
ulp — small enough to pass a tolerance check and large enough to break exactly
this diff. Persist the internal tuple.


---

# Session 2026-09-05 — the tr_M provenance arc (beans `qou-brkp`, `qou-49vn`, `qou-16yn`)

Six traps, every one of them mine, each caught by a measurement rather than
by review. Summarised as one line in `MEMORY.md`'s session log.

## TRAP — check the input's change date against the consumer's PREVIOUS run, not its new one

Asked why `option_e_multi_isotope_delta_lambda_probe_v3`'s
`tr_M` jumped +48.1 % on 2026-08-23, I checked whether its chi-* inputs changed
*at* that regeneration. They had not, and I wrote "stale inputs — REFUTED".
Wrong endpoint: the inputs changed on **08-10**, and the consumer had last run
on **08-09**. That test is *guaranteed* to report "unchanged" for exactly the
drift class being looked for, because a sweep re-runs the consumer without
touching its inputs. The window is `[consumer.computedAt_prev,
consumer.computedAt_new]`.
## TRAP — a commit timestamp is not a compute timestamp

In the same
investigation I argued from `2c68d7f34a` "landing 19:24:58Z" that the value was
"already computed from post-convention-D inputs". The witness *inside* that
commit has `computedAt 2026-08-09T00:41` — 42.7 h earlier, and a day and a half
*before* the commit I was ordering it against. Read `computedAt`, never `%ad`.
## TRAP — a data dependency through a witness JSON is invisible to every import-cone audit

`option_e…v3` imports only stdlib, mpmath, `_path_bridge`
and `_precision`, and takes its `tr_M` from `json.load` of a chi witness (its
line 129 copies `tr_M_at_q0` verbatim). `witness_import_cone_staleness_audit.py`
walks Python imports, so it sees none of this. Checking the *consumer's* imports
for a *data* dependency answers a question nobody asked — and the real drift was
one level up, in the chi producer's cone (`tr_m_wenzl_bridge_mpfr`).
## TRAP — a field named `convention` need not carry the convention you mean

The chi-* witnesses' `convention` reads `colour-weighted-averaged-crossing` —
the **p/n colour** axis, not Markov C-vs-D. I used it to "refute convention D";
the reading was empty, not exculpatory. Resolve the Markov question from the
y_λ table's `z` (`0.4993…` = C, `0.6126…` = D).
## TRAP — never read a truncated numeric string as a value

The ≥3-row weights
in `y-lambda-mpfr-proton-witness.json` print as `2.188243022053045885…` under a
40-char slice and are `2.188243…e-72`. I was one commit from filing a live "the
two y_λ tables disagree on support" defect off that slice. They agree; one
serialises a vanishing quantity as exact `0.0`, the other keeps the residue.
## BASELINE (2026-09-05) — the +48.1039 % `tr_M_atom` move is a y_λ WEIGHT-TABLE regeneration

`computations/probes/trm_provenance_chain_probe.py` (11/11).
Deuteron `0.38835714…` → `0.57517224…` in `7e4d1aa6d0`; every `chi_lambda` and
every provenance field (`scriptHash c36a8a393fcd`, `q0Anchor`, `q0Value`,
`dps 50`) byte-identical, every `y_lambda` changed. Trigger: `fcf629cf41`
switched `_Y_LAMBDA_DEFAULT` 33 s earlier — but the *size* is not the μ–p pin
(11.5 ppb, three orders too small); both y_λ tables had been regenerated that
day, moving weight mass onto the ≤2-row partitions ((3,3) ×1.071 → (6,) ×1.948,
≥3-row → ~1e-72). **`scriptHash`-keyed staleness structurally cannot see this.**

---

# Session 2026-09-05 — the seminormal-builder precision arc (bean `qou-sv7h`, PRs #6794 / #6807)

Seven traps, every one of them mine, each caught by a measurement rather than
by review.  The rebase that landed this section put the tr_M provenance arc
above it, so the header is explicit: these seven belong to `qou-sv7h`, not to
the arc immediately preceding them.

## TRAP — the AMBIENT `mp.dps` is 15, so exact inputs become a float64 computation

`_precision.py` deliberately does not set `mp.dps` as an import side effect, so
a bare `import hecke_core_legacy` leaves the ambient precision at mpmath's
default **15 dps = 53 bits = exactly float64's significand**. mpmath rounds
every operation to the ambient precision. So a producer can carry genuinely
exact `mpf` inputs and still be a float64 computation, with nothing in the
source to grep for: no `float(`, no `math.`, no literal.

Measured on one seminormal entry (qou-sv7h, PR #6807), after #6794 had made the
builder exact:

    builder entry, significand bits        167
    v*v at ambient dps 15                   53
    v*v inside workdps(COMPUTE_DPS=70)     234
    relative difference per operation   2.5722e-17

and compounded through the accumulator the published result moved 8.3e-15 /
4.1e-15 / 2.9e-15 at k = 5 / 6 / 7.

**Check `mp.dps` at the point of arithmetic, not at the point of construction.**
A `workdps` wrapper on the builder does not extend to its consumer; each entry
point needs its own.

## TRAP — the type fix and the context fix are each USELESS alone, and the type fix measures as ZERO

Same arc, and it is the part that would have ended the investigation early.
Switching `atom_character_raw`'s `math.log` to `mp.log` **first**, before
wrapping it in `workdps`, moved **0.00e+00 on four partitions** — because at
dps 15 `mp.log` and `math.log` agree to the bit. The obvious reading is "no
effect, revert it".

The correct reading is that the *other half* was missing: `mp.log` at ambient
precision is float64, and `workdps` around a `math.log` narrows anyway. Only
both together move anything.

**So a zero from half of a two-part precision fix is not evidence the half is
useless.** Land both, then measure. The same applies to `mpf` seeds vs the
arithmetic that consumes them.

## TRAP — measuring float64 loss AT float64 precision reads 0.0 by construction

I instrumented `_trace_dim` to report `abs(raw - mpf(float(raw))) / abs(raw)`
inside `mp.workdps(COMPUTE_DPS)` and got **max 0.0 over 129 traces** — an
apparently clean bill. The `raw` values had already been rounded to 53 bits by
the ambient-dps trap above, so `float(raw)` was lossless and the measurement
could not see what it was measuring. Opening the context *after* the value
exists does not restore the bits.

`mp.nstr(raw, 30)` on such a value prints 30 digits and looks like content —
that is the exact binary value's decimal expansion, not precision.

**Compare two RUNS, not a value against its own cast.** The honest instrument
is the whole producer at ambient dps against the whole producer inside
`workdps`, diffed.

## TRAP — `git stash` is not a baseline

**This is an instance of "a 'before' count taken from the tree your own branch
is mutating is not a before count" above**, which already states the general
rule: a before-figure must come from a REVISION, not a path. It is recorded
separately because the mechanism is different and worse — a path-based
enumeration at least *looks* like what it is, whereas `git stash` reads as
though it restores a prior state.

To A/B a change against `origin/main` I ran the harness, `git stash`ed, ran it
again, and reported the second as "main". `git stash` does not undo an
already-made **commit** — the first fix was committed by then, so the "main"
column was the post-fix tree and six of seven rows read `0.00e+00`. It looks
exactly like a clean no-op result.

**Use `git worktree add --detach /tmp/wt origin/main`** and run the harness
there, with the harness's repo root parameterised. Cheap, and it cannot lie
about which tree it ran in.

## TRAP — `x.context.prec` is the CONTEXT's precision, not the value's

`mpf.context.prec` reports the *current global* `mp.prec`, so it reads 53 for
every value while `mp.dps` is 15, including values carrying 167 bits. It looks
like a per-value attribute and is not.

The value's own significand length is `x._mpf_[3]` — the tuple is
`(sign, man, exp, bc)`. **`[2]` is the exponent**, and reading it as the
mantissa gave me "8 significand bits" for a value that has 167.

The cheap, tuple-free discriminator: `x == mpf(float(x))` is False iff the
value carries more than float64 can hold.

**And that discriminator is safe where the subtraction two sections up is
not.** mpmath compares `mpf` values *exactly*, independent of the ambient
precision — verified with `mp.dps = 15` and a 70-dps `mpf(1)/mpf(3)`
(236 bits): the equality returns False, while `abs(x - mpf(float(x)))`
computed at the same ambient dps rounds to 0. Control: `mpf(0.5)`, exactly
representable, returns True. So use the equality to *detect* excess precision
at any working precision; only ever use a subtraction to *quantify* it, and
then only inside a `workdps` opened before the values were built.

## TRAP — "object dtype has no BLAS" does NOT imply the numpy path is slower

Bean `qou-sv7h` finding 5 concluded that `_matmul_dim`'s `dim >= 8` numpy
branch was a 31 % pessimization and should be deleted, on the (correct) premise
that object-dtype arrays get no BLAS. Measured on the real inputs, the branch
is **~2.1x FASTER** at every dense partition with 8 <= dim <= 28 (ratios
0.47–0.50), and deleting it would roughly double the dense-path cost.

The premise is true and the inference is wrong: numpy's object path still runs
the k-loop in **C** rather than in the interpreter, and that alone beats a
triple-nested Python loop even with per-element `mpf` dispatch. "No BLAS" is
the difference between 1e-6 s and 1e-2 s at dim 16 — but the comparison that
matters is against the *alternative*, not against float64.

I tested the one mechanism that would have reconciled both figures — that the
old measurement was taken at ambient dps 15 — and it does not: 0.46x at dps 15,
0.48x at dps 70. The cause of the discrepancy is **undetermined**; the bean
records no harness.

## TRAP — measure CALL COUNTS before optimising a function

Same bean, step 2: export a Rust `dense_dense_mul_mpfr` and route `_matmul_dim`
through it, ">=24x, this is what makes higher isotopes reachable". Instrumented
with `pyhecke_native` present:

    unified_iterative_correction(1,1,k=7), kernel ON      0 calls
    unified_iterative_correction(1,1,k=7), kernel OFF  1025 calls
    atom_character_raw (4,2) dim 9,        kernel ON      0 calls
    _contrib_single_partition,             kernel ON     25 calls

Two of the three consumers short-circuit to a Rust path and never reach the
function at all. Worse, the 1025-call configuration is *by definition* the one
where `pyhecke_native` is absent — and the function to be exported lives in
that same extension, so the export cannot help the only path that calls it.

**A speedup factor is about the function; the payoff is about the call count.**
Ten lines of `sys.settrace`-free spy wrapper settles it before any porting.

## TRAP — a `nohup … &` long compute dies at TURN END; it is not harness-tracked

**Measured twice in one session, 2026-11-20 (bean `qou-oiz3`).** A 78-producer witness
refresh was launched as

```bash
nohup python3 -u /tmp/refresh.py > /tmp/refresh.log 2>&1 &
```

inside a Bash call made with `run_in_background: true`. It died **twice**, at 27/78 and
again at 6/52, and both times the diagnosis looked like a probe failure — the log's last
line was mid-producer (`gamma_gamma_isospin_composition_rule_probe`, then
`particle_gram_bond_locality_probe`), so the obvious reading is "that probe hung or OOMed".

**That reading is wrong, and the timestamps are what settle it.** Compare the log's last
write against the session's last tool call:

| death | log last written | my last tool call that turn |
|---|---|---|
| 1st, at 27/78 | 19:19:09 | ~19:19 |
| 2nd, at 6/52 | 19:59:27 | ~19:59 |

The job died **the moment the turn ended**, both times, on two different producers. It is
the turn boundary, not the probe.

**Mechanism.** The harness tracks the process it launches. `nohup … &` forks a child and
the launcher exits immediately, so the harness tracks the *launcher* and the real work is
orphaned. The giveaway is the completion notification: it arrives within seconds and says
`exit code 0` — that is the `nohup`+`sleep` wrapper succeeding, **not** the compute. An
orphan then has nothing holding it through container idle.

**So a notification saying "completed (exit code 0)" is evidence about the WRAPPER.**
Taking it as evidence the refresh finished is the second-order version of this trap, and it
is how "D is at 27/78" became "D finished at 27/78" in a session summary.

**The fix.** Pass the long compute to `run_in_background: true` **directly**, with no
`nohup` and no trailing `&`:

```bash
python3 -u /tmp/refresh.py 2>&1 | tee /tmp/refresh.log     # run_in_background: true
```

Then the harness owns the process, it survives turn boundaries, and the completion
notification is about the compute.

**Corollary for any resumable sweep: make the driver STATELESS.** This one baselines every
candidate against `git show HEAD:<file>` rather than against an in-memory snapshot, so a
resume re-derives verdicts instead of trusting the dead run's. That is the only reason two
deaths cost coverage and not correctness. A driver holding its baseline in memory would
have had to start over, or worse, would have committed verdicts computed against a
reference that no longer existed.

**And check for a death before reporting progress.** `pgrep -f <driver>` plus the log's
age (`stat -c %Y`) is two seconds of work; a tail alone cannot distinguish "running slowly"
from "dead six hours ago", and the last log line looks identical either way.
