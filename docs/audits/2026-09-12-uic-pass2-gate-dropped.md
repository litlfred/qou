# The UIC Pass-2 sign gate is dropped — the numbers get worse, and that is the result

**Date:** 2026-09-12 · **Beans:** `qou-21oc` (the drop), `qou-xkjt` (the `K` comment),
`qou-ai7v` / `qou-px38` (two further carriers) · **Scope:** enacted owner ruling ·
**PR:** #7253

Asked *"only gate on lean proved — resolution options?"*, the owner chose two of four:
**drop the Pass-2 sign gate**, and **hunt the primal LP behind it**. The hunt is
[#7251](https://github.com/litlfred/qou/pull/7251) and it does **not** reverse the
drop. This document records the drop.

## 🛑 The headline, stated so it cannot be misread

**Dropping the gate does not fix the sign, does not improve accuracy, and moves
every measured atom further from AME.**

| tier | atom | returned BEFORE (gated) | returned AFTER (ungated) | factor | AME2020 | \|before − AME\| | \|after − AME\| |
|---|---|---|---|---|---|---|---|
| `k_exact = 4` | ²H | `−0.0895596830589507` | `−0.412212192245027` | 4.603× | `+2.2246` | 2.3142 | **2.6368** |
| `k_exact = 4` | ⁴He | `−0.0805867484776914` | `−0.2742397716174` | 3.403× | `+28.30` | — | — |
| `k_exact = 5` | ²H | `−0.7335499391634978` | `−1.2268740026260945` | 1.672× | `+2.2246` | 2.9581 | **3.4515** |
| **production default** `k_exact = k_max = 11` | ²H | `−9.14773623102088` | `−17.6908290020795` | 1.934× | `+2.2246` | 11.3723 | **19.9154** |

Both columns have the **wrong sign**. The gate was not the reason.

What the drop buys is that the producer now reports what its functional actually
gives, instead of a subset chosen by a rule nobody can derive. AGENTS.md
§"NO FITTING, EXCEPT CAL-1/2/3": *a documented honest miss is a result*, and
*a more accurate fitted route is worth LESS than a less accurate derived one*.

**Do not reinstate the gate. Do not look for a replacement selection that restores
the old numbers** — that is selection against the target, which the same section
forbids.

## Two figures that were not on the record

**1. The production-default factor is 1.93, not 3.4–4.6.** Every prior statement of
the gate's size — the code comment, #7251's table, #7237's content-block rewrite —
quotes `k_exact = 4`. Measured at the production default (193 partitions, one atom,
**425.5 s** wall):

```
²H   ungated −17.6908290020795   gated −9.14773623102088   94 of 193 admitted
```

So the gate's grip **loosens** as the partition set grows: it admitted 22 % of the
magnitude at `k_exact = 4` and 52 % at the default. A reader of the production path
needs this number and neither the comment nor the audits carried it.

**2. `k_exact` is not a small knob on this quantity.** ²H ungated runs
`−0.412 → −1.227 → −17.69` across `k_exact = 4 / 5 / 11`. Quote the tier with any
UIC number.

## Why the gate goes — refuted sorry-free, not merely doubted

`QOU.MassTheory.UICGateNotFromComplementarySlackness` (#7251; 8 declarations,
`lean -DautoImplicit=false -s 65536` exit 0, `#print axioms` clean, no `sorryAx`)
shows complementary slackness on `prop:operator-selection-lp` does **not** give this
gate, by four independent mismatches:

1. **Index set.** LP constraints run over NF basis elements (`d = n!`), the gate over
   partitions (`p(n)`) — 6 against 3 at `n = 3`.
2. **Argument.** CS constrains `(Gx*)_i`, a function of the operator being
   *selected*; the gate reads `t_λ = tr(M_λ(W_atom))`, an **input** entering the LP
   only as a cost coefficient.
3. **Direction.** `IsFeasible` demands `0 ≤ (Gx)_i`, so on any feasible point `≤ 0`
   and `= 0` are the same predicate: a sign gate there *is* the tightness gate,
   keeping only blocks at exactly zero — while the producer kept 4 of 10 at ²H.
4. **No unique optimum.** The minimiser set is a positive-dimensional face, so
   "the OPTIMAL primal-dual pair `(Φ*, y*)`" names no unique object.

A partition-indexed repair is excluded **scope (b)**. **Invariant:** primal
feasibility of the Frobenius constraints together with orthogonality of the
Wedderburn projectors. They are orthogonal idempotents, so
`G_{λμ} = tr_M(P_λ P_μ) = δ_{λμ} tr_M(P_λ)` is diagonal, CS decouples to
`s_λ · G_{λλ} · x_λ = 0`, and the atom's traces never appear in it. Independent of
`n`, `q` and trace convention.

Independently, #7237's `uicGated_cs_eq` reaches mismatch 3 from the functional's own
structure rather than from the LP's feasible set.

## One file asserted both sides for a week

`hecke_core_legacy.py:328-374` (`lp_shadow_price`) already carries an owner-ruled
correction of 2026-09-05 (PR #6752) stating that this module's `y_λ` are **not** LP
duals and that the net-constraint dual `y_0` is identically zero. **That correction
never reached the reasoning 1 800 lines down**, which derived the gate from LP
duality. The fix had landed at the site carrying the offending *name*, not the site
carrying the offending *reasoning*. Now cross-referenced at the Pass-2 site.

One refinement of that ruling, from #7251 and worth carrying: **`y_0* = 0` is
basis-dependent.** It holds for the NF-basis instance, whose cost vector *is* a Gram
row; the block-indexed instance measures `y_0* = 0.0346905` (²H) and `0.0129979`
(⁴He). The version that applies to `lp_shadow_price` is the NF one, so the ruling
stands as written for that site.

## A retraction the drop forced

[`2026-09-05-uic-sign-forced-by-gate.md`](2026-09-05-uic-sign-forced-by-gate.md)
concludes that the wrong sign is **forced by** the gate. Dropping the gate is the
experiment that claim could not survive: if the sign were forced by the gate,
removing the gate would have to be able to change it.

Re-measured over the same terms with no sign filter
(`uic_sign_forced_by_gate_probe`, 7/7 checks, two of them new):

| atom | gated sum | **ungated sum** | ratio |
|---|---|---|---|
| ²H | `−1.3656848` | **`−2.251132`** | 0.607 |
| ³H | `−0.97040895` | **`−1.8036172`** | 0.538 |
| ³He | `−0.80794043` | **`−1.7465929`** | 0.463 |
| ⁴He | `−0.80209171` | **`−1.3701187`** | 0.585 |
| ⁶Li | `−1.0769706` | **`−1.9696784`** | 0.547 |

Every ungated sum is negative and larger in magnitude.

**What survives, and it is most of it.** Step 1 (`C_λ ≥ 0` on all **682**
partitions) and step 3 (`|Tr| ≥ d` in **3.4 %** of `Tr ≤ 0` against **34.1 %** of
`Tr > 0`, because `Tr(I) = +d`) both re-measure unchanged and still pass. Together
they establish a **bias** — the gated subset is more negative than the slack one.
**Step 2's inference from that bias to "B < 0 is FORCED" does not follow** and is
withdrawn. This is a scope-(a) retraction of an over-claim; no measurement changes.

The same audit's **A-independence** explanation is downgraded to a correlation. The
gated-set size is near-constant across A — but `where_the_a_dependence_is_lost_probe`
Layer 3 already finds the **raw, pre-gate** ratio flat (1.25 / 1.16 / 1.09 at
k = 5 / 7 / 9), so the gate is not the cause there either.

That probe's own *"WHAT IS NOT CLAIMED"* paragraph explicitly declined to say the
gate was wrong, flagging the `tr ≤ 0`-vs-`tr = 0` tension as needing the primal LP.
#7251 supplied the primal LP; that tension is mismatch 3 of its four, and the
non-claim is now answered in the affirmative.

## What was kept, and why

- **`final_tr_sign` is still computed and reported** in `per_step`. It is a real
  property of the atom's final state; only its use as an admission filter is gone.
- **The gated sum is still computed and reported**, renamed `gated_total_MeV` →
  **`gated_total_DISPROVED_SELECTION_MeV`**. Measured: two consumers on `main`
  (`where_the_a_dependence_is_lost_probe.py:182`,
  `uic_per_block_log_valley_scan_probe.py:134`), both updated. A neutral name on a
  disproved selection is what let it be read as the answer; a consumer that wants it
  must now say so.
- The valley-scan probe's **S0.3 identity check is retargeted** from the gated to the
  ungated total. It would otherwise fail — and that failure *is* the change, so it is
  retargeted, not relaxed.

## Two further carriers of the same disproved argument — recorded, not changed

Both are deliberate non-changes. Neither is evidence the argument survives anywhere.

**`qou-ai7v` — the q-Gaussian fallback tier.** It zeroes `delta_g` on the identical
complementary-slackness reasoning, and its comment called that *"the categorically
correct outcome"*. Marked asserted-not-derived. **Not changed**: the tier is a
Perron–Frobenius asymptotic that supplies a `log_trace` and no matrix, so there is no
derived rule for what it should contribute, and inventing one to move a number would
be selection. It is also **unreachable on every default run** — `k_exact = k_max`
empties the window, measured 0 partitions at the default against 169 at `k_exact = 4`.

**`qou-px38` — `unified_iterative_correction_jet`.** Still gates on `tr_sign ≤ 0`, in
both its linear terms and its conjugate-pair cross terms. **Not changed**: zero code
callers tree-wide, and
[`2026-05-24-hecke-core-canonical-audit.md`](2026-05-24-hecke-core-canonical-audit.md)
row 63 classifies it EXPLORATORY with "no canonical caller". Changing it would move
no published number while costing a re-run nobody consumes.

## The second half of the tranche: the `K = 6` comment (`qou-xkjt`)

`hecke_core_legacy.py:389-404` named **three** values for one constant — `K = 6` at
`:390`, "capped at 8" at `:396` (a sentence truncated mid-clause, with no verb),
`K_PARTITION_MAX = 11` at `:404` — and its arithmetic was wrong in its own terms:
*"24 partitions in total: 2 + 3 + 5 + 7 + 11"*. That sum is **28**; at the live cap
it is `Σ_{k=2}^{11} p(k) = **193**`. Both verified by direct computation.

Worse, it read as an **endorsement of a fit the code does not implement**:
*"Empirical sweep … shows K = 6 is the OPTIMAL partition cutoff"*. Measured: **no
production caller truncates at 6.** The only live `k = 6` sites are
`uic_per_block_log_valley_scan_probe.py:167-168`, which pass 6 and 11 side by side
*to compare them*, and a different parameter in `_deprecated/heavy_atom_opts.py:280`.
The accuracy figures it cites (*"40Ca: 0.001 at K=6 → 0.012 at K=9"*) appear nowhere
else in the tree — no witness, no producer, no audit.

**So the sweep ran, recommended 6, and 6 was rejected.** AGENTS.md names *"sweeping a
discrete parameter for accuracy"* verbatim as fitting and says accuracy is not the
ranking criterion, so that rejection is the discipline working — written up as its
opposite. An agent running the anti-fit audit reported a live fit in the binding
compute on the strength of it. Rewritten to record the honest negative.

Comment-only; moves no number. **Exemption 2** of the ASK-OWNER gate — the file's own
live constant one line below decides it, and a reviewer checks by reading `:434`.

## What this does NOT close

- **`qou-brng`** (the extensive-term frontier) and **`qou-zlra`** (the graded-binding
  sign convention) stay **open**. Per AGENTS.md rule 13a, no bean whose subject is an
  open conjecture is closed here.
- **The sign is still wrong and unexplained.** The gate was a candidate explanation
  and it is now excluded. That is a narrowing, not an answer.
- **The functional itself is untouched.** `B_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*) ·
  (ln|tr M_λ| − ln d_λ)` is what it was; only the summation range changed.

## Verification

- **No Lean added here.** The Lean this rests on is #7251's, verified on that branch.
- `scripts/precision-gates.sh --changed` and `scripts/check-sidecars.sh` — results
  in the PR body, pre-existing reds named.
- Producer re-runs: `uic_sign_forced_by_gate_probe` 7/7,
  `uic_a1_vanishing_trace_probe` 9/9, `uic_word_level_locality_probe` 11/11,
  `uic_per_block_log_valley_scan_probe` (see PR).
