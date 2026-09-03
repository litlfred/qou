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
