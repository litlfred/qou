---
# qou-cwin
title: 'MIGRATION: express the Q_beta c_k ladder in h = q - 1/q instead of u = b*hbar_q^2'
status: in-progress
type: task
priority: high
created_at: 2026-08-16T12:45:00Z
updated_at: 2026-08-17T01:53:02Z
---

Owner-authorised 2026-08-16: *"bean up and start = express the ladder in h"*.
Parent: `qou-cds1` (S1 of the convention ruling). Evidence for the decision is
on PR #5210.

## Why (the reasons that survived measurement)

- **Analyticity.** `u ~ h^2`, so reverting `u -> h` needs `sqrt(u)` and the
  ladder is non-analytic at `u = 0` (corpus:
  `qbeta_ck_from_operator_markov_trace_probe`). In `h` the same function is a
  genuine power series: measured, `cos(alpha - u/2) = 1 + 0*s - s^2/8 +
  ((1-sqrt3)/8)s^3 + ...` with `s = q-1`, integer powers throughout.
- **Expressiveness.** Odd-order content is half-integer in `u` and therefore
  structurally unrepresentable there. In `h` it is an ordinary rung. Note
  `s^1 = 0` exactly, so the h-frame has no linear rung -- the `u^1` rung
  (`a_1 = -sqrt(3)/12`) is an artifact of expanding in a squared variable.
- **Literature alignment.** The Ohtsuki series is a power series in `q - 1`
  with integral coefficients (Lawrence conj., Rozansky proof); the Habiro ring
  is described as analytic functions at roots of unity.
- **Channel consistency.** alpha_EM's Habiro element is ALREADY written in h:
  `[2]_q * (1 - h^2 * a)`. Q_beta is the odd channel out.

## Why NOT (measured, and it must not be over-sold)

**The reframe does not fix anchor-instability.** Tested at matched
magnification (`h^k` chosen so `h^k ~ u^3`) in
`qbeta_h_vs_u_frame_stability_probe`:

    frame       proton         muon      rel swing
      u^3    -2.069343    -2.020200      2.3748%
      h^9    -1.676039    -1.636236      2.3748%
    residual R                           2.3747%

Identical to five significant figures; the variables' own swings are ~1e-6.
The instability is in the RESIDUAL, not the coordinate. This refuted a
hypothesis I had put in writing (that half-integer leakage drives the drift) --
scope-(a), as the explanation of THIS drift at THESE anchors.

**Cost: ~3x the rungs** for equal precision (7.2 -> 22.1 for 1e-15). It is
3.045x rather than 2x because `u = 0.195 h^2`, and that prefactor costs about
as much as an extra power at these magnitudes.

So this migration is **hygiene and expressiveness, not a fix.** Do not
describe it as one in any PR, witness, or content block.

## Blast radius

Every `c_k`-derived statement is u-frame and becomes a different number:
`c_2`, `c_3`, `c_4...`, `S_leak = c_3 + Vol(4_1)`, `q*_S`,
`c_3^even = -Vol(4_1)`, `[3]_q/25`, `J - hbar^2`. Plus AGENTS.md's truncation
rule `N >= log10(1/eps)/2.07 - 1`, whose `2.07` is `-log10(u)`.

## Ordered plan

**T0 (FIRST, before any number moves) -- make the frame DECLARABLE.**
Add a `ladder_frame: "u" | "h"` field to every c_k-bearing witness and require
it. This is the lesson from the convention C->D campaign, learned the hard
way: PR #5210's own `--impact-vs-main` had to report *"0 of 12 declare
`markov_convention`, so the count is a lower bound."* A migration whose
artifacts do not declare their frame cannot be measured, only guessed at. Do
NOT skip this step to get to the interesting part.

**T1** -- extract the h-frame rungs at both anchors; establish the h-ladder as
a computed object with a witness, alongside (not replacing) the u-ladder.

**T2** -- registry: record the frame on every c_k row; pair with `qou-f09n`'s
`c_2` / `\tilde c_2` naming so a reader can tell which coefficient in which
frame.

**T3** -- re-derive the truncation-order rule in h and correct AGENTS.md
line 1062. Owner sign-off required (STRICT banner, contested channel).

**T4** -- downstream content blocks. NOT started without owner sign-off:
changes published statements.

## Discipline

The anti-fit rules are unchanged. A rung obtained by matching a target is a
fit regardless of which variable it is written in. `alpha` remains un-derived
in both frames and this migration does not change that.

---

## T0.5 VERIFIED (2026-08-16) — and it re-scopes this migration substantially

#5187's claim was flagged by the coordination sweep as "worth reconciling
before T1". Checked. **It is confirmed, and it is stronger than stated.**

### `c_4..c_7` are not zero — they are never computed

`qbeta_ck_cache.py:139-146` extracts recursively:

    for k in range(3, 8):
        ratio_m1 = Q_codata / Q_prev - 1
        if abs(ratio_m1) < EPS_RESIDUAL: break
        ck_extracted = ratio_m1 / u ** k
        Q_next = Q_prev * (1 + ck_extracted * u ** k)

`Q_next = Q_prev * (1 + ratio_m1) = Q_prev * (Q_codata/Q_prev) = Q_codata`
**exactly**. So `c_3` absorbs the entire residual by construction and the
guard fires immediately. Run output, verbatim:

    c_3 (extracted) =   -974.4318877
    c_4: residual below compute precision (0.00e+00) — ladder converged

Residual **exactly** `0.00e+00`. The `structural_candidates` entries for
k = 4,5,6,7 (`c_3*b^4`, `-(b^2+1/2)`, `c_3^2*b^2`, `c_3^3 = -8`) are
**unreachable dead code** — nothing is ever compared against them.

### So the "ladder" has ONE extracted rung

`c_2 = -1` is hardcoded and `c_3` is defined to make the product exact. That
is a two-parameter model fitted through one point, not a convergent series.

**This contradicts AGENTS.md line 1062**, which describes the ladder as *"a
convergent series; N is the truncation order chosen by target precision
(N >= log10(1/eps)/2.07 - 1)"*. There is no truncation order to choose: the
ladder terminates at k=3 by construction, at every anchor, always.

To its credit the producer is honest in its own output — it labels `c_3+` as
*"extracted from Q_codata, CIRCULAR & q0-dependent ... NOT a prediction.
Never counts toward a 100x/1x pass."* The defect is that the AGENTS.md
framing does not match the producer.

### Second finding: the producer is ALREADY convention D

`qbeta_ck_cache.py:85` is `z = q**3 / (q**2 + 1)` — convention D. So its
committed `c_3 = -974.43` is a D-frame value already on main, while
AGENTS.md and the registry still carry the C-frame `c_3 ~ -2.07`. Those are
not competing measurements; they are the same quantity in two frames, and
only one of them is what the producer now emits.

## Consequence: RE-SCOPE

| justification | status after T0.5 |
|---|---|
| Analyticity in h | **stands** |
| Ohtsuki / Habiro literature alignment | **stands** |
| alpha_EM channel consistency | **stands** |
| **Odd rungs become representable** | **VOID** — there are no higher rungs to represent |
| Churn across `c_4...` | **VOID** — those values do not exist |

The migration is now materially smaller than advertised: it touches `c_2`,
`c_3`, and the framing, not a tower. **The siblings told to expect `c_4...`
churn must be re-briefed** — that list was wrong, and it was my broadcast.

The strongest remaining reason to do it is no longer expressiveness. It is
that the h-frame makes the ladder's actual shape legible: a one-rung exact
interpolation is easier to recognise as such when it is not dressed as a
truncated series in a variable chosen to make it converge fast.

## New follow-ups this surfaced

- **AGENTS.md line 1062 is wrong on a second count** (beyond `qou-f09n`'s
  "PROVED Taylor-exact"): the convergent-series / truncation-order framing
  does not describe the producer. Owner sign-off needed — STRICT banner.
- **`qbeta_ck_cache.py` emits 11 raw float64 fields** (the run warns:
  `.assertions[0].computed/expected/tolerance`,
  `.data.rows[*].err_ppb_after_this_rung`, `structural_candidates[*].err_pct`).
  Pre-existing, not mine, worth its own bean.

## Reconciled with main's red-team (e83e83ac9) — two extractors, both findings right

Main landed an adversarial audit of the same ladder (bean `qou-cds1`) while
this branch was working. It says *"c_6/c_7 imposed in extraction
(self-consistency); c_8 pattern breaks"*, which appears to contradict T0.5's
"c_4..c_7 are never computed". Both are correct; there are **two** extractors:

| producer | form | c_4+ |
|---|---|---|
| `qbeta_ck_cache.py` | greedy sequential, `Q_next = Q_prev(1 + c_k u^k)` | **never computed** — the loop breaks (T0.5; Lean-proved in `GreedyLadderTermination.lean`) |
| `qbeta_ck_extraction_precision_floor.py` | product `R(u) = prod_k (1 + c_k u^k)` | **computed, but pure noise** |

The second carries a good bound worth citing rather than re-deriving:
`sigma(c_k) = sigma_R / u^k` with `sigma_R ~ 6e-7` the AME relative precision
on Q_beta. Since `u^3 ~ 6.2e-7 ~ sigma_R`, `c_3` sits exactly AT the noise
floor and `c_4` (`u^4 ~ 5.3e-9`) is far below it. Only `c_2` (~0.8%) and
`c_3` (~48%, marginal) are data-determined.

So the two findings are complementary, not competing: **structurally** the
greedy ladder cannot have a c_4 (proved), and **statistically** a product-form
c_4 could not be measured even if it did.

### An over-claim NOT made here, recorded so nobody makes it later

`sigma(c_k) = sigma_R / h^k` with `h > u` gives every h-rung a bigger lever and
a smaller sigma than its u-index counterpart. It is tempting to read that as
"more rungs clear the noise floor in h", i.e. the h frame extracting more
information. **That is wrong.** There is ONE measured scalar (Q_beta), so one
combination is determined no matter the coordinate. Changing variables
re-conditions the coefficients; it does not create information. The correct
statement is only that the h rungs are better *conditioned* per index.

This matters because it would have been the strongest-sounding argument for
the migration, and it is unsound.


## T2 DONE (2026-08-16, PR #5258) — Lean first, then the registry

Per the owner's 'go carefully. lean formalize and prove first', the theorem was
written BEFORE the registry rows it justifies, so the naming rests on a proof
rather than on a symbolic run.

Lean (both sorry-free, lean-direct exit 0, #print axioms clean on all 12 decls):
  LadderFrameChange.lean          T1, generic Field  (4 theorems)
  LadderCoeffNormalisation.lean   T2, R per §7c      (8 declarations)

Registry:
  §2   c-tilde_k and c_2^even rows added
  §9i  new subsection: theorem + three-way table + withdrawn contradiction
  §3   FRAME DECLARATION, not a frame column -- every rung is u-frame and
       factor-normalised, so a column repeating that 7x carries no information.
       Replaced by the discipline: any row in a different frame or
       normalisation must say so in its own cell.
  notation-collisions.md   c_k / c-tilde_k / c_k^even split at the lookup point

Verification: ck_dk_registry_validate.py OK (wired rungs ['2'], flip-flop guard
satisfied).  Content validate exit 0, 4 pre-existing warnings, none on the
touched block -- and the block IS in the chapter manifest (notation.ts:37), so
the render/AST gate genuinely covered it.

RETRACTED mid-task: I briefly cited 'bun run render-latex.ts <block>' as a
pipeline render.  It validated nothing -- that module exits 0 on no arguments
AND on a nonexistent path.  Caught by testing the negative controls before
recording the pass.  The real gate is scripts/run-validate.ts.

## Remaining

T3 (AGENTS.md line 1062) and T4 (downstream content blocks in F/h coordinate)
both need OWNER SIGN-OFF and are deliberately not started.


## T3 + T4 DONE (2026-08-16, owner-authorised 'go t3 t4')

T3 -- AGENTS.md line 1062 banner corrected.  Three claims examined; the
detailed record and the retraction are in qou-f09n.  Headline: only ONE of the
two halves the bean named was actually wrong ('PROVED'), 'Taylor-exact' is
under-specified rather than false, and a third figure I expected to be stale
turned out to be a normalisation difference and was LEFT ALONE.

T4 -- downstream content blocks.  Scope was measured, not assumed: 13 sites
across 10 files carry 'Taylor-exact' on c_2.  The T4 shape CHANGED as a result
of the T3 finding: it is NOT 'replace Taylor-exact everywhere' (that would have
deleted a correct claim from 12 published statements).  It is:

  * 8 sites carrying 'proved/PROVED' -> reworded to 'structural' (real defect)
  * 2 bare-'Taylor-exact' seed sites -> which-series pointer added
  * 3 sites LEFT deliberately:
      - phi-b-bar-parity-interpretation.md:32 is correct as written, and its
        2.375% swing matches my own measurement exactly
      - complex-volume-ladder-intro.md:3 names a DIFFERENT series (the
        fibre-level complex V(q)); I cannot verify its normalisation, so I did
        not touch it
      - q-beta-q-eq-one-shadow-gate-proof.md:25 'a Taylor-exact constant' --
        referent not confirmed

Also FIXED two artifacts I had landed earlier the same session which carried
the now-retracted framing: notation-collisions.md and registry §9i both said
'Taylor-exact is wrong'.  Both now say it is under-specified.

FLAGGED, not fixed: qbeta-ck-truncation-canonical.ts says 'cross-anchor 2.98%'
where the registry §9g anchor pair gives 2.3748% (proton-normalised).  Dated
2026-05-31, so plausibly pre-re-pin -- but NOT verified, and I had just been
wrong about a 'stale' percentage, so it is recorded as a named open item rather
than silently corrected.


## The flagged 2.98% is RESOLVED (2026-08-16)

It was the one loose thread I named at the end of T4.  Answer: STALE, not
mis-normalised -- and my first sharper theory about it was wrong.

  extracted c_3 proton  -2.06934258
  extracted c_3 muon    -2.02020024   <- current
  superseded muon value -2.0097       <- what 2.98% was computed against

  swing                        /|c_p|      /2
  CURRENT                     2.3748%   2.4571%
  STALE (pre-#1422 muon)      2.8803%   2.9801%   <- the corpus's 2.88% and 2.98%

So 2.88% and 2.98% are ONE stale gap under two normalisations, exactly like the
3.47%/3.35% pair for the proton gap and exactly like c_2 vs c-tilde_2.  Third
instance of the same trap in this bean.

WRONG TURN, recorded: I first identified -2.0097 as the candidate model
J_Hopf - hbar_q^2 = -2.00981718, because all three published percentages
reproduced from it to 3 s.f.  A corpus grep killed it -- the corpus value is
-2.00973976, a DIFFERENT object that agrees to four decimals (differs at
7.7e-5), and one doc explicitly labels it 'muon-pin (stale, pre-#1422)'.  My
ORIGINAL 'plausibly pre-re-pin' flag was right and I talked myself out of it.
The coincidence is now an explicit assertion in the probe so the next reader
does not repeat it.

VERDICT UNCHANGED (scope-(a)): 2.3748% is smaller than 2.98% but still vast
beside 1e-50 compute precision, so c_3 stays a q0-dependent NEAR-MATCH.  No
tier moves.

Landed: new probe + witness (3/3), the canonical framing audit (correction
banner + the FACT B rule list), the red-team doc dated today (which had the
CORRECT anchor pair but the STALE percentage), the truncation-canonical
authorNote and its block title, and the AGENTS.md clause.

## Also fixed: a float64-padding regression I committed in T1

The precision preflight went RED on my OWN T1 witness.  qbeta_h_frame_rungs_probe
did float(c) on the exact Q(sqrt 3) coefficients and then re-promoted with
mp.mpf, serializing 50 digits of a float64.  Same regression class I had fixed
in charge_symmetric_coulomb_binding earlier this session, committed again three
commits later.  Fixed at the producer with sp.N(c, 60); padding 18 -> 13
(= baseline), NEW 0.  The h^3 digits now diverge from the old ones at digit 17,
confirming the old tail was fabricated.
