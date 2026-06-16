# Coordination ledger — Story B c_3/c_4/κ categorical derivation

**Goal:** establish whether Story B (categorical chain for Q_β
precision-ladder coefficients) is structurally forced or merely
preferred. Critical for the 1-ppb mass program's claim that the
0.0066 ppm Q_β residual is a *prediction* of QOU rather than a fit.

## Scope (as of 2026-05-17)

| PR | Title | State | Role |
|---|---|---|---|
| #670 | Crystal-bases shift_NF + ⁴He JSJ + ordering-invariance | merged | upstream — assumed Story B as user-direction selection |
| **#671** (this branch) | docs: Story B forced + m_p chain closure gap analysis | open | **walking back** the "structurally forced" framing after PR #664 critical review |
| #664 | prop:hopf-jones-c3-categorical (Story A falsified) | open | claims c_3 = -2 categorically; **critical-review-flagged** |
| #665 | N=4 + σ_1 eigenstructure + n-strand BraidGroup | open | downstream of c_4; same template question |
| #663 | isotope-mass-table honest no-cal regen + anti-staleness | open | parallel; not on Story B critical path |
| #661 | c_2 = b² categorical | merged | the TEMPLATE for a genuine categorical proof |

## Classification

- **Overlap (high)**: #671 ↔ #664 — my critical review and genuine
  Markov-trace probe directly address PR #664's claims.
- **Dependency**: #671's Story B audit was upgraded based on #664,
  then walked back after critical review of #664's probes.
- **Cherry-pick potential**: PR #664 author could integrate my
  genuine probe + critical-review audit doc to fix the gaps; in
  exchange, PR #664's structural framing of V_(2,2,2) → Hopf could
  be ported into #671's audit if rigorised.

## Critical-review findings (2026-05-17)

PR #664 ships three categorical claims:

1. **c_3 = J_Hopf(q=1) = -2** — probe is tautological (hardcodes -2
   in two places). Proof sketch hand-waves Step 2 (V_(2,2,2) → Hopf
   via Markov stabilisation) and Step 4 (order-h⁶ extraction).
2. **c_4 = b² + 1/2 = 3/2** — probe computes `c4 - c4 == 0` (same
   expression in both sides) with `b = 1` asserted.
3. **κ = -E_0·log(1/h)/([2]_q·[3]_q)** — formula was "identified
   empirically in PR #645", then interpreted; 0.035% numerical
   match is suggestive but not symbolic equality (cf. PR #661's exact
   c_2 = b² template).

Additional infrastructure finding:

- The codebase has TWO different tr_M implementations
  (`hoefsmit_symbolic.tr_M_symbolic` and
  `markov_weights_symbolic.tr_M_canonical`) that produce *different*
  symbolic answers for σ_1² in H_2 (both give +1 at q=1, but
  different rational functions). Neither equals the textbook Jones
  polynomial -(q+q⁻¹) directly. The Story B coefficient extraction
  needs an explicit convention choice the PR doesn't make.
- Writhe correction is required to go from Markov trace to Jones
  polynomial. tr_M_QOU(σ_1^odd)|_{q=1} = 0 always (Markov-parameter
  factor); J_knot(t=1) = 1 always — no single multiplicative
  normalization reconciles them.

## Actions taken on this branch (#671)

| Action | Commit |
|---|---|
| Audit doc: critical review of PR #664 | `26f677677` |
| Walk-back of "Story B structurally forced" in story-b-canonical-chain audit | `26f677677` |
| Genuine V_(2,1) seminormal Markov-trace probe for σ_1² in H_2 | `7f06e0bef` |
| Probe extended with tr_M_canonical comparison + dual-implementation finding | (this commit) |
| Coordination comment on PR #664 | (link below) |

## Coordination posts

- 2026-05-17 — comment on [PR #664](https://github.com/litlfred/qou/pull/664#issuecomment-4468992940) summarising critical-review findings and proposing the PR #661 template as the path forward.
- 2026-05-17 — follow-up coordination comment on PR #664 with dual-implementation finding (this round).

## What would close this

A genuine c_3 = -2 derivation needs:

1. Decide which tr_M is canonical (`tr_M_symbolic` or `tr_M_canonical`).
2. Compute the symbolic Markov trace of σ_1² (or the relevant
   V_(2,2,2)-projected object in H_6) via that canonical tr_M.
3. Verify it equals the textbook Jones value (or doesn't, with a
   stated writhe-correction factor).
4. Extract c_3 from the order-h⁶ Taylor expansion of Q_β around
   q=1 (not q=1 evaluation, which loses Taylor information).
5. Verify no other order-h⁶ contribution survives Frobenius selection.

The PR #661 template does steps 1–3 for c_2 = b². The analogous work
for c_3 is the proper closure of Story B at N=3.

## Next concrete task on the queue

Currently working PR #671. After this coordination cycle:

- (optional) implement the "tr_M_canonical contribution to σ_1²
  expanded around q=1+ε to order ε^6, with c_3 coefficient extracted"
  — this would be the genuine c_3 derivation, ~PR #661-scale work.
- Decide with the user whether to merge PR #671 now (audit-only,
  walk-back + critical review) or expand it with the genuine c_3
  computation.

## 2026-05-17 update — H_3 numerical comparison

User asked: "can we compare tr_M_canonical in mass scripts vs symbolic/production?"

Ran a side-by-side comparison on H_3 braids that production
mass-derivation chains evaluate. **The two implementations differ by
57–99% on the proton's intra-nucleon Hecke word.**

| Braid in H_3 | `tr_M_symbolic` | `tr_M_canonical` | rel |Δ| |
|---|---:|---:|---:|
| σ_1 | 0.1032 | 0.4993 | **79%** |
| σ_1·σ_2 | 0.00357 | 0.2493 | **99%** |
| σ_1³ (proton intra) | 0.3142 | 0.7302 | **57%** |
| σ_1³·σ_2³ (proton-like) | 0.09209 | 0.5332 | **83%** |

The 8% discrepancy on σ_1² in H_2 was the lower bound. On the
braids actually consumed by mass scripts, the discrepancy is 57-99%.

User asked: "is either proved to be derived from Cat Action?"

Answer (in dual-tr-m-discrepancy.md):
- `tr_M_canonical` (Wenzl y_λ) **YES** — Ocneanu/Wenzl categorical
  derivation, computes Jones polynomial of braid closure.
- `tr_M_symbolic` (dim_q²/[n]_q!/f^λ) **NO** documented Markov-trace
  derivation. Computes a different invariant (q-Plancherel expectation
  of normalized character), not the Jones polynomial.

So production scripts use a non-canonical tr_M whose categorical
derivation is undocumented, while the framework's `thm:jones-markov-trace`
cites the canonical one.

## §6 escalation candidates

This finding has cross-cutting implications beyond PR #664:

- PR #663 (m_p chain) uses `tr_M_symbolic` for the proton-mass
  derivation — the chain may be computing the wrong invariant for its
  own claimed identification.
- PR #661 (c_2 = b² categorical, merged) — needs cross-check: which
  tr_M did its symbolic derivation use? If `tr_M_symbolic`, its claim
  of "Markov trace of V_(2,1) Hoefsmit" is in the same non-canonical
  category.
- 1-ppb dashboard Layer 1/2 is internally consistent within
  `tr_M_symbolic` (Hoefsmit ↔ markov_peel both use it), but its claim
  of computing the Jones polynomial requires reframing.

Recommended owner adjudication:

1. Was the choice of `tr_M_symbolic` deliberate (e.g. a different
   well-defined invariant the framework wants to compute) or
   accidental (the name overloads with the literature-canonical
   Jones-Markov)?
2. If accidental: rename + audit + replace. ~15 scripts affected.
3. If deliberate: document the choice; update `thm:jones-markov-trace`
   in CLAUDE.md §7a to reflect the actual computed invariant.

## 2026-05-17 update — Dual tr_M FIX shipped + provenance traced

Followup investigation per user direction. Three new findings:

### Provenance (commit 58e78090e, 2026-05-05)

The dual-trace issue was **known at creation**. The introducing
commit's title is *"Resolve factor-of-2 mismatch: PR #546 uses
Plancherel trace, not Markov"* and its message documents:

> PR #546's tr_M = Σ (dim_q²/[n]_q!) · χ^λ / f^λ
>   → PLANCHEREL/REGULAR TRACE (Hopf-algebra integral)
>   → does NOT satisfy Markov axiom tr_M(1) = 1 except at q=1
>
> char_fast tr_M = Σ y_λ · χ^λ with y_λ from Markov axioms
>   → CANONICAL HOEFSMIT-WENZL MARKOV TRACE
>
> These are DIFFERENT categorical objects, not different normalizations.

The commit mandated a downstream Plancherel→Markov conversion via
y_λ re-weighting. **That conversion was never wired.** The function
was named `tr_M_symbolic` (M = Markov) anyway, and ~15 production
scripts call it as the Markov trace.

### Math validation

`tr_M_symbolic` is **correct as the q-Plancherel trace** (Hopf
integral), formula `Σ dim_q²(λ)/[n]_q!·χ^λ(β)/f^λ`. Verified.

It is **NOT the Markov trace** — violates tr_M(1) = 1 (gives ≈0.987
on H_3), fails the Markov property tr_M(α·σ_n) = z·tr_M(α).

`tr_M_canonical` (markov_weights_symbolic.py) IS the canonical
Markov trace via Wenzl's Schur principal specialization. **It is
the one cited by CLAUDE.md §7a `thm:jones-markov-trace`.**

### Categorical-action derivation

- `tr_M_canonical` (Wenzl y_λ): **YES** — Ocneanu 1985 + Wenzl 1988
  literature derivation, computes Jones polynomial of braid closure.
- `tr_M_symbolic` (dim_q²/[n]_q!/f^λ): **NO** documented Markov-trace
  derivation. Computes a different (well-defined) invariant.

### Fix shipped (commit 19ac57828 on this branch)

Added to `computations/hoefsmit_symbolic.py`:

| Name | Status | Function |
|---|---|---|
| `tr_q_plancherel_symbolic` | NEW canonical name | Σ dim_q²/[n]_q!·χ^λ/f^λ (regular trace) |
| `tr_Markov_symbolic` | NEW canonical name | thin wrapper of tr_M_canonical (Wenzl) |
| `tr_M_symbolic` | DEPRECATED alias | delegates to tr_q_plancherel_symbolic |

No consumer broken; every read-site now sees the disambiguating
docstring linking back to the audit doc.

### Implications for PR #664's c_3 = -2 claim

- `tr_q_plancherel_symbolic(σ_1²)` at q=1: **+1** (not -2)
- `tr_Markov_symbolic(σ_1²)` at q=1: **+1** (not -2)

The -2 value comes ONLY from the textbook Jones polynomial
$-(q+q^{-1})$ which is the **writhe-corrected** form (Kauffman/Jones
convention with framing α^w(β)). PR #664 must specify which object
the order-h⁶ coefficient of Q_β picks up; this is independent of
the dual-trace issue but the dual-trace finding sharpens the
question.

### Coordination posts (this round)

- Comment on [PR #664](https://github.com/litlfred/qou/pull/664#issuecomment-4469197220) — provenance + fix + implication
- Acknowledged sibling coordination from PRs #663, #665, #672 on
  [PR #671 comment thread](https://github.com/litlfred/qou/pull/671) (no separate post needed — they're already coordinating with us)

### Cross-link to shared ledger on main

The main-merged ledger `docs/coordination/1ppb-categorical-chain.md`
(commit `4cc7561fc`) tracks the same scope. This dual-tr_M finding
should be appended there too — will do in a follow-up commit once
merged or via cherry-pick coordination with the maintaining session.

## 2026-05-17 final — paper analysis confirms dual-tr_M finding

User questions answered after paper analysis:

### Q1: Why T2+T3 excluded at A=1?

Documented in scripts as "PR #533 finding: structurally empty under
current level-selection rule" (derive_m_p_hecke_path_a:138). But PR
#533 itself ("Phase A.3 unblocker: τ̂_0 proton-scale numerical
realisation") only ADDED an H_3 brane tower scaffold; it did NOT
derive an A=1 exclusion rule. The "structurally empty" framing is a
**quarantine workaround**, not a derived theorem.

Probe (probe_t2_t3_proton_neutron_a1.py) shows raw T2+T3 = 1.18e6
at A=1 (overshoots m_p target by ~10^3×). Three interpretations
remain open (see audit doc).

### Q2/Q3: Canonical T_i factors?

The PAPER's canonical mass formula is SINGLE-term:

    M(𝔥) := ρ · tr_M(T_w) = ρ · Σ y_λ(q) χ_λ(T_w)

(atom-knot-mass-derivation-proof.md:48-54). The 6-term formula
(T1+T2+T3+T4+T5+T6) is a PRODUCTION-SIDE engineering decomposition
in mass_formula_6term_mpfr_50dps.py — NOT canonical paper content.
The T_i terms do NOT have individual paper-side derivations.

### Q4: q-Plancherel as truncation of full mass tower?

NO. The paper's spectral sequence COLLAPSES at E_2 (atom-knot-mass-
derivation-proof.md:57-60): "Every quantity is finite-sum and exact;
no higher analytic content needed." The canonical mass is the
FULL Wenzl-Markov trace, NOT a series in jet-order/GB-filtration.

The q-Plancherel trace is NOT a truncation — it's a DIFFERENT
formula the production code uses by accident. The paper's
atom-knot-mass-derivation.md:42-44 tests BOTH conventions
empirically: single-term fails 87-100% under EITHER convention;
adding the brane tower reduces to 36-63%. Neither convention closes
the gap; the brane tower is the missing piece.

### Q5: Did sibling PR migrate to tr_M_canonical?

NO. git log --all --grep "tr_M_canonical|tr_Markov_symbolic" returns
ONLY commits on PR #671 (this branch). The deuteron script is the
only production script migrated. All other mass-prediction scripts
still compute the Plancherel trace under the misleading name
`tr_M_symbolic`.

### Owner-level decision matrix

The paper says the canonical mass = ρ · Σ y_λ(q) χ_λ(T_w) (Wenzl-
Markov). The production code computes ρ · Σ (dim_q²/[n]_q!) χ_λ/f^λ
(Plancherel). These differ by 57-99% on H_3 braids. Options:

  (A) Production code is WRONG: rerun all mass-prediction scripts
      with tr_Markov_symbolic; m_p / m_n / m_He predictions will
      change. The paper's claim is preserved.
  (B) Paper is WRONG: amend atom-knot-mass-derivation-proof.md to
      cite the Plancherel formula. CLAUDE.md §7a notation register
      also needs amendment (currently says y_λ is the canonical
      Markov-Wenzl weight).
  (C) BOTH are valid for DIFFERENT observables: mass = Plancherel,
      Jones polynomial = Wenzl-Markov. Need a paper block clarifying
      which observable is what.

Recommendation: investigate (C) first — if mass and Jones polynomial
are different observables in the framework, the dual-tr_M is
deliberate, just under-documented. If (C) is wrong, (A) is the
right path (paper is the source of truth).


## 2026-05-17 round 6 — F_n derivation analysis + new paper block

User direction: "do F_3, F_n categorical derivation" + "prove w/ lean
and write up in paper".

**Substantive new result on PR #671** (commits `f70ce8d6e`, `c11899aa4`):

  tr_M(σ_1²) = (q^{5/2} − q^{1/2} + q² + q) / (q² + q) = 1 + (q-1)·q^{−1/2}
  for all n ≥ 2, Markov-invariant.

  Taylor: ε^k coefficient = C(−1/2, k−1) for k ≥ 1 (exact binomials,
  verified through ε^10).

**Files shipped:**
- `content/quantum-observable-universe/braids-and-knots/trm-hopf-sigma1-sq-closed-form.{ts,md,lean}` — content block triple
- `lean/QOU/Braiding/TrMHopfSigma1SqClosedForm.lean` — 3 typed theorems w/ proof sketches + [jones1987]/[wenzl1988] refs
- `probe_F_n_categorical_derivation.py` + witness — verifies closed form + binomial pattern
- `docs/audits/2026-05-17-F-n-derivation-analysis.md` — analysis doc

**Critical implication for Story B:** The bare-Markov ε^{2n} coefficients
of tr_M(σ_1²) are NOT the framework's claimed F_n values:

  | n | framework F_n at q=1 | bare-Markov ε^{2n} |
  |---|---:|---:|
  | 2 | 0.7500 (b²)         | -0.3125 (-5/16)    |
  | 3 | -1.2990 (-2b³)      | -0.2461 (-63/256)  |
  | 4 | 1.2500 (b²+1/2)     | -0.2095 (-429/2048)|

PROVES the Q_β precision-ladder F_n are NOT bare-Markov Taylor
coefficients. Each F_n requires a SEPARATE Wedderburn-block projection.
PR #664's c_3 claim implicitly relies on V_(2,2,2) projection; bare-Markov
cannot recover -2·b³.

**Next-PR scope** (genuine F_3 derivation via V_(2,2,2) projection):
documented in audit doc §"Next-PR scope" — 6 steps, tractable on the
chi-deuteron-h6.witness.json cache.

**Coordination posts:**
- Round 6 on PR #664: https://github.com/litlfred/qou/pull/664#issuecomment-4469536436

## 2026-05-17 round 7 — cross-anchor falsification + framework alignment

### Δ_coupling cross-anchor falsification (probe_delta_coupling_cross_anchor.py)

User direction: "do as recommended" (recompute Δ_cat for p, n from
main's infra). Result: **falsifies the pp-nn correlation hypothesis**
shipped earlier on PR #671.

  Anchor     Predicted   Extracted    Gap        Verdict
  (2,2) DM   13.1945     13.1969      -0.018%    ★ confirmed
  (2,1) SM    6.5516      6.0252      +8.737%    ⚠ FALSIFIED
  (1,2) SM    6.5516      6.8211      -3.950%    ⚠ FALSIFIED

The doubly-magic 0.04% match was COINCIDENCE. 3-anchor system implies:
  pp_term ≈ -0.526 MeV, nn_term ≈ +0.270 MeV, corr ≈ +0.351 MeV.
The Z↔N asymmetry +0.796 MeV between (1,2) and (2,1) is real and
needs to be explained by channel-specific substrate primitives, not
the symmetric (A-2)·E_0·log(1/h) leading form.

### Habiro residue at A=1 (probe_habiro_residue_a1.py)

User direction: "3 y" (m_p chain Item C). Result: **CONFIRMS T6
small** — the cached tr_M(β_atomic, q_0) IS the Habiro-resummed
value; no separate "residue tail" to add. The T6 ~ 0.68·m_e quarantined
in derive_m_p_hecke_path_a refers to a small-q expansion tail, bounded
by ~0.3 MeV. Item C alone CANNOT close the 1571× m_p chain shortfall.

This narrows the remaining m_p gap to Items A (T2+T3 reformulation
at A=1) and B (T5 categorical attribution).

### MarkovTrace abstraction divergence — coordination needed

Posted on PR #664: my MarkovTraceTower class (HnMarkovTrace.lean)
diverges from PR #664's hecke-mass-trace.lean structure. Three
options laid out:
  (1) PR #664 canonical, mine wraps
  (2) PR #671 canonical, theirs instantiates
  (3) Both, different purposes (mass formula vs stabilisation-invariance)

Awaiting response from PR #664 author. Posted at:
  https://github.com/litlfred/qou/pull/664#issuecomment-4472407349

### Queued for after PR #671 merges

  Reformulate Δ_coupling per knot-fusion-step1-audit's operator-
  valued Wenzl branching framework (per user "1 see work on claude/
  knot-fusion-step1-audit"). The non-scalar A^λ_{μ,ν}(I) operators
  capture the Z↔N asymmetry my symmetric hypothesis missed.

  Genuine V_(2,2,2) projection probe for c_3 (Phase 2'). Closes PR
  #664's c_3 gap independently of mass-formula reformulation.


## 2026-05-17 round 8 — PR #681 review + combiner cross-link

User direction: "look at PR 681 - cherry pick if needed."

### Inspection result

PR #681 has 2 commits, both audit-doc only:
  413ae2835  Knot-fusion Step 1 audit: math + pipeline already on main
  a6a4af0e9  Address gemini on PR #681: fix block-count discrepancy

The corrected block count: 19/35 non-scalar (μ,ν) blocks in
sublemma-2-1-A-operator-extract.witness.json for H_6 deuteron
interface — NOT the 18/30 originally cited (Gemini caught the
conflation with H_9 partitions).

### Nothing to cherry-pick

Both commits are on the audit doc itself; cherry-picking would
conflict with PR #681's merge. My PR #671 ledger references the
operator-valued framework conceptually (no specific block-count
claims to correct).

### Coordination comment posted on PR #681

https://github.com/litlfred/qou/pull/681#issuecomment-4472570688

Cites my Step 2 combiner (canonical_tr_m_via_chi_cache.py, commit
e3a1b22ac) — verified to 1e-15 vs Habiro witness for the 3 complete-
coverage atoms. Notes the MarkovTrace abstraction divergence question
on PR #664 is independent (still awaiting response). Confirms PR
#671's empirical findings (cross-anchor falsification + T5 candidate
enumeration) align with PR #681's "operator-valued, not scalar"
diagnosis.

### Cross-PR scope map (current)

| PR | Author | State | Coord status |
|---|---|---|---|
| #671 (mine) | claude | open | Round 8 — Phase 2/3 work shipped |
| #664 (c_3/c_4/κ) | claude (other) | open | Awaits MarkovTrace abstraction answer |
| #681 (knot-fusion audit) | claude (other) | open | Round 8 cross-link posted |
| #663 (anti-staleness) | claude (other) | open | No conflict |

Next concrete actionable on PR #671: Phase 2' V_(2,2,2) projection
probe for c_3 (closes my own PR #664 critical-review gap).

