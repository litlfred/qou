# The 1 ppQ question, re-posed: what three weeks of `main` changed, and what is worth attacking

**Date:** 2026-09-07 · **Bean:** `qou-37j2` · **Branch:** `claude/drop-dihedral-hypotheses-2026-09-07`
**Tier:** reanalysis — measurement plus a ranked assessment. **No number is derived here and
nothing is wired.** Every figure is either read from a committed witness, re-run this session, or
computed from two committed witnesses and shown with its arithmetic.

Owner asked: *"back to original question of arc — how do we get to 1 ppQ. Lots of activity on main
in the last few weeks. A reanalysis is needed. What are the promising attack options … what's
needed from research and lit."*

Supersedes, as a status document,
[`2026-08-18-mass-binding-accuracy-what-is-closeable.md`](2026-08-18-mass-binding-accuracy-what-is-closeable.md)
— its §1 recount and §3 refutation both stand and are re-confirmed below; its §7 ranking is
superseded by §5 here, because two of its five items have since been settled and one route it did
not know about has arrived.

---

## 0. The four answers, flatly

1. **L1 is met and is not the question.** The compute leg (internal cross-method agreement
   ≤ 1 ppQ = 10⁻¹⁵) is met at 70 dps compute / 60 dps serialisation. "How do we get to 1 ppQ"
   is a question about **L2**, the per-observable accuracy leg `σ_pred ≤ σ_exp/100`.
2. **L2 has not moved: 1 / 5 scoreable, 0 / 5 unconditional.** Re-run today,
   `per_observable_100x_status.py` reproduces its committed witness **byte-identically**
   ("unchanged"). Not one of the five scoreable predictions improved in three weeks.
3. **But the ground under it moved twice, in opposite directions** (§2). One route the
   2026-08-18 audit ranked second is now *measurably worse* than it looked; one route nobody was
   scoring turns out to be the framework's second-best prediction; and one **new derived** result
   on the binding side improved a residual band 1300-fold.
4. **The single highest-value attack is not on any of the five.** It is the **`Q_β` chain's
   replacement**, and the reason is that three of the five *are one number*. §5.

---

## 1. Where L2 actually stands, measured today

Re-run this session, `PYTHONPATH=computations python3 -u computations/per_observable_100x_status.py`,
exit 0, witness unchanged:

| obs | role | err (ppb) | σ_exp (ppb) | 100× target (ppb) | miss |
|---|---|---:|---:|---:|---:|
| `m_p` | CAL-2 numerical anchor | 0.002852 | 0.3091 | 0.003091 | *not scored* |
| `m_e` | CAL-1 anchor | 0 | 0.3131 | 0.003131 | *not scored* |
| `m_μ` | validation | 211.2 | 21.77 | 0.2177 | **970.2×** |
| `Q_β` | derived (CAL-1+CAL-2) | 1279. | 779.7 | 7.797 | **164.0×** |
| `m_n` | validation | 0.9029 | 0.5109 | 0.005109 | **176.7×** |
| `Δ_pn` | validation (derived) | 658.0 | 433.6 | 4.336 | **151.7×** |
| `m_K/m_π` | validation (meson ratio) | 51.48 | 2.636e4 | 263.6 | **0.195×** ✓ |

`beats_100x_scoreable = 1`, `scoreable_total = 5`. And that one is
truncation-fitted plus `α_em`-`sorry`-conditional
([`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md)), so the count of
**unconditional parameter-free** sub-100× predictions is **0 / 5**.

Two structural facts about this table that the miss factors hide:

- **`Q_β`, `m_n`, `Δ_pn` are one number.** `m_n = m_p + Q_β + m_e` and `Δ_pn = m_n − m_p`, so the
  151–177× band is the same miss counted three times. **Three of the five scoreable predictions
  are one prediction.** The effective denominator is `{Q_β-chain, m_μ, m_K/m_π}` — three
  independent things.
- **`m_K/m_π` is the only ratio.** The other four are `m_e`-scaled absolutes or differences of
  them, and the 2026-08-11 absolute-mass excision already says an `m_e`-scaled MeV number carries
  no content beyond its dimensionless ratio. The one leg that passes is the one leg shaped the way
  the excision ruling says the physics lives.

---

## 2. What three weeks of `main` changed

**528 audit documents** landed under `docs/audits/` between 2026-08-18 and today; the tree took
~13,300 commits in six weeks. Four of those changes bear on L2. Three of the four are negatives,
which is the honest shape of a productive period.

### 2a. The `c_k` ladder does not converge in the canonical convention — the 164× floor is worse than C-frame, it may not exist

The 2026-08-18 audit ranked *"`c_k` re-derivation under convention D"* second and could not say
what the 164× floor becomes under D. **`qou-cds1` has now measured it**, and the answer is not a
shift:

| fact | convention C | convention D re-extraction |
|---|---|---|
| `c₃` (proton / muon) | −2.06934258 / −2.02020024 | **−974.43 / −974.38** |
| implied empirical `c₂` | −1.0176 | **−9.299** |
| N2/N1 residual ratio | 0.017 (58× rung gain) | **0.89 — no convergence** |
| bar parity of `z` | `bar(z_C) = z_C` | `bar(z_D) = q⁻⁴·z_D` |

Two consequences, and the second is the sharp one.

- **Every ≈ −2 value-level fact in the corpus is C-conditional**, including `c₂ = −1`,
  `c₃ = −2 = J_Hopf(q=1)`, `c₃^even = −Vol(4₁)` (H1), `[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S`.
  [`2026-09-06-resurgence-arc-convention-d-reanalysis.md`](2026-09-06-resurgence-arc-convention-d-reanalysis.md)
  measured the exposure: **45 of 73** resurgence-surface audits depend on the ladder and
  **zero** of them said so before that pass.
- **The rung convergence itself is C-frame only.** In D the residual ratio is 0.89, i.e. the
  second rung buys ~11 %, not 58×. So the "164× is the floor of the ladder's non-circular
  content" statement is not merely *C-conditional in its value* — under D there may be no ladder
  to have a floor. The dashboard's own witness records this without ambiguity:
  `convention_frame_qbeta.status = "INHERITED_C"`,
  `reproducible_under_canonical_convention: false`, and the D path
  **refuses to run** (`SystemExit(2)`, *"convention D has no derived `c_k` ladder"*).

  **So `Q_β`, and with it `m_n` and `Δ_pn` — three of five scoreable predictions — are not
  currently reproducible in the canonical convention at all.** That is a stronger statement than
  "they miss by 164×", and it is the most important single fact in this reanalysis.

### 2b. The binding functional changed, and it is derived, not fitted — a ~1300× residual gain

[`2026-09-05-binding-law-arc-synthesis.md`](2026-09-05-binding-law-arc-synthesis.md). The corpus
stated `B = Q_β·Δtr`; it is **refuted algebraically**, not empirically: `tr_M` is multiplicative
along the chain and binding is extensive, and `Δtr/tr_free = 1 − e^{−S}` is within `7.7e−4` of 1 by
`A = 11`, so above that `Δtr` *does not contain* the binding energy. p5–p95 residual spread 1592×;
²³⁸U over-bound 19.6-fold.

The replacement is forced rather than chosen — `log` is the unique multiplicative-to-additive map:

```
B = E₀ · log( tr_M(β_free) / tr_M(β_atom) )
```

p5–p95 **1.225×**, against 1592×. **A ~1300-fold gain from changing the functional, not a
constant**, on the same derived bond factors. And it is the framework's own object: the Markov
relation `tr_{n+1}(x·σ_n) = z·tr_n(x)` makes `ν(x) = log_z tr_M(x)` the tower's additive counter,
`b_pp = z` is a derived identity, so a p–p bond is exactly one Markov reduction, and
`rem:energy-scale-planck` reads `E₀` as the energy of one reduction step —
**`B = E₀ × (number of reduction steps)`**.

**This is the one unambiguously good thing in the window, and it is the shape the anti-fit rule
wants**: derivational cleanliness first, accuracy as a diagnostic. It does **not** touch any of the
five L2 rows (binding is not among them) — which is exactly why it must not be quoted as an L2
improvement.

What is left there is **shape, not scale**: total remaining scale freedom 0.99 %, residual band
22.5 %, so the shape residual is **22.7× the entire scale freedom**. Five rounds went into the
scale and it was never the dominant term.

### 2c. `α_EM` is the framework's second-best prediction and is not on the dashboard

Not one of the seven dashboard rows is `α_EM`, yet
[`alpha-em-schwinger-ladder.witness.json`](../../computations/alpha-em-schwinger-ladder.witness.json)
records the form-B ladder at the proton pin as **0.31343 ppb = 2.09 σ_α**. Computed here from
that witness and the two CODATA editions (arithmetic shown, `mp.dps = 40`):

| | vs CODATA-2018 | vs CODATA-2022 |
|---|---:|---:|
| form A (no Schwinger) | +1.6723 ppb, 11.15 σ, **1115×** | +0.9937 ppb, 6.48 σ, **648×** |
| form B (+Schwinger) | +0.3134 ppb, 2.09 σ, **209×** | **−0.3652 ppb**, 2.38 σ, **238×** |

So `α_EM` sits in the **209–238×** band — comparable to the `Q_β` trio (152–177×), four times
better than `m_μ` (970×), and it is the **only** L2-grade result in the corpus that is not one of
the three independent things in §1.

**🛑 With a caveat that must travel with the number.** The producer scores against **CODATA-2018**
deliberately (its own note: *"the live table carries 137.035999177; this producer scores against
the 2018 value on purpose"*). The **edition shift is 0.6787 ppb — 2.2× the form-B residual — and
it flips the residual's sign.** A result whose sign depends on which CODATA edition you compare to
is not yet a 2 σ agreement; it is a number of that size. Fixing this is cheap and is item 1 of §5.

The `α_EM` front also has a live `proof-statement-integrity` defect: the block's `.md` and `.lean`
state formulas **470 ppb apart**, and the construction the L2 dashboard actually imports
(`alpha_em_inv_derived`, −467.6 ppb) is neither the ladder above nor the `.lean` the paper cites
(`qou-aemx`,
[`2026-08-28`](2026-08-28-alpha-em-lean-vs-compute-divergence.md)).

### 2d. Infrastructure: the Matsumoto/Bruhat arc closed unconditionally

Not an L2 item, recorded because it removes a standing conditional from the Hecke layer everything
above sits on. As of PR #7027 (today) `matsumoto`, `exists_Tw`, the subword property, Bruhat
transitivity, lifting and both order equivalences (`BruhatLe ↔ ReflLe`, `↔ LeftReflLe`) hold for
**every** Coxeter system with no hypothesis — `DihedralExact` and the finite-bond condition are
both proved from the geometric representation (`CoxeterDihedralOrder`). Sorry-free,
`[propext, Classical.choice, Quot.sound]`.

---

## 3. The three independent walls, stated as walls

Stripping the triple-counting, L2 is blocked by exactly three things.

**W1 — `Q_β` has no derivation in the canonical convention.** The ladder's non-circular content is
exhausted *as algebra*: `QOU/QBeta/GreedyLadderTermination.lean` (sorry-free) proves the producer
extracts **one** rung by inverting the target, after which the residual is *identically* zero —
`greedy_later_rungs_vanish`: *"`c_4 … c_7` carry no information; they are not small, they are
`0`."* And the one extracted rung `c₃ = (Q_β^exp/Q_N2 − 1)/u³` comes **from** experimental `Q_β`,
so it is circular for predicting it. Add §2a and the position is: *the C-frame ladder is exhausted
and the D-frame ladder does not exist.* **Blocks 3 of 5.**

**W2 — the μ–p residual is a theory residual, not an anchor choice.** ~11.6 ppb must land
somewhere: proton pin ⇒ 970× on the muon; muon pin ⇒ 1.4e4 σ on the proton. Re-pinning **moves**
it. Closing it means shrinking the residual, which is a statement about the theory. It is also
**not** closeable by deriving `q₀` — permanently gated, owner ruling 2026-08-02. **Blocks 1 of 5.**

**W3 — `m_K/m_π` passes for the wrong reason.** Its derived core `√([3]_q[4]_q)` misses this
observable's own (unusually loose, 264 ppb) target by **385×** on its own; the sub-100× result is
manufactured by an EM correction whose **truncation order beats the untruncated series** — chosen
against the data — and whose `α_em` input is conditional on an open `sorry`. **The one pass is not
a pass.**

---

## 4. What this says about "1 ppQ" as a goal

Three observations the ranked list in §5 rests on.

**The targets are not comparable, and the loosest one is where the framework already lives.**
`m_K/m_π`'s 100× target is **263.6 ppb**; `m_n`'s is **0.005109 ppb** — a factor of **51,600**
between the two bars on the same scorecard. The framework clears the loose one and is ~150–1000×
from the tight ones. Both facts are about the *experiments*, not about the theory: `m_n`'s target
is tight because `m_n` is measured to 0.5 ppb.

**The ratios are the reachable class.** `m_K/m_π` is the only ratio and the only pass; `α_EM` is a
dimensionless coupling and is the second-best; the four misses are `m_e`-scaled absolutes and
differences. That ordering is not a coincidence — it is the 2026-08-11 excision ruling showing up
in the scorecard.

**Accuracy is not the ranking key, and here that has teeth.** Under §2a, the *more accurate*
`Q_β` route is the C-frame one and it is the **excised** convention. The *less* accurate answer —
"there is no D-frame derivation" — is the correct one to carry. Ranking by residual would
re-institute convention C.

---

## 5. The attack options, ranked by derivational cleanliness

Cost is my estimate; risk and blast radius are measured where stated. Ranked as the anti-fit rule
asks: what does each *derive*, not what does each *score*.

### 1. Re-score `α_EM` against CODATA-2022 and put it on the L2 dashboard — hours, not sessions

**What it means.** The framework's second-best prediction is unscored, and its recorded residual
is against a superseded reference whose edition shift is 2.2× the residual and flips its sign
(§2c). Re-score, add the row, and state the miss honestly (238× vs CODATA-2022).

**Cost.** One producer edit plus a dashboard row. The producer's own note says bumping the
reference alone would desynchronise the recorded residuals — so it is a re-run, not a constant
swap.

**Risk.** It makes the scorecard *look worse* in one sense (a sixth failing row) and better in
another (the failing row is at 238×, the second-best number the framework has). **This is the
correct direction under the anti-fit rule** — a scorecard that omits its own second-best result
because nobody added the row is not a scorecard.

**Commits to.** Nothing. Reversible in one commit.

**Recommendation (my judgement).** Do it first. It is the only item here whose cost is hours, and
it fixes a number that is currently sign-ambiguous.

### 2. A non-ladder derivation of `Q_β` — the only thing that can move 3 of 5

**What it means.** W1. Not a deeper `c_k` — that is proved empty — and not a `z`-swap into the
existing ladder, which `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) proves is invalid
because the C-frame ladder and the mass channel's three-row forcing are **mutually exclusive**.

**Cost.** Large, multi-session, genuinely open. This is research.

**Risk.** The honest outcome may be that `Q_β` has no D-frame derivation, in which case three
scoreable rows become *undefined* rather than *inaccurate*. That is a worse-looking scorecard and
a better-understood framework.

**Commits to.** Whatever functional form is chosen becomes the CAL-2 proxy's derivation.
`qou-cds1` has the live D-frame front (`cds1-*`, ~10 audits since 2026-08-21).

**Recommendation.** This is the highest-value item and the owner should expect it to take
sessions, not turns. It is also the one where the parallel-exploration relaxation applies — it is
open-outcome research, multiple routes are viable, and a second agent from a different direction
is a feature.

### 3. The binding shape residual — surface / Coulomb / symmetry as an edge-set question

**What it means.** §2b left a 22.5 % band against 0.99 % of scale freedom, and the synthesis
locates it: **Coulomb and surface are ONE defect, and it is the edge set.** The derived isospin
coefficient has the **wrong sign** (`κ = +2(q₀−1) = +0.2200`; data optimum `≈ −0.15`), and
layout-free bond counting (p5–p95 1.181) beats every isospin-resolved variant (1.225–1.232).

**Cost.** Medium. The four sorry-free negatives of 2026-08-29/30 have already pruned the space
from four directions — complete-graph coordination excluded by saturation, linear-chain excluded by
arrangement-dependence, body-order depth ≥ 3 forced, the connected 3-body Mayer cumulant sign
threshold-forced and wrong against AME.

**Risk.** Low blast radius — binding is not on the L2 scorecard, so nothing here moves a scored
number. That is also its weakness as an answer to *"how do we get to 1 ppQ"*.

**Commits to.** The log law as the binding functional.

**Recommendation.** Worth doing and **not** an answer to the 1 ppQ question. Do not let its 1300×
headline be quoted as L2 progress; it is a different leg.

### 4. The μ–p residual — structural, and the cheap move is to say so

**What it means.** W2. There is no anchor choice that closes it and the derivation route is
permanently gated.

**Cost / recommendation.** No attack. What is cheap is **stating it as structural on the
dashboard** so 970× stops reading as a tuning gap. My judgement: do not spend research time here
until W1 moves, because an 11.6 ppb theory residual is plausibly the same object as whatever
replaces the `Q_β` ladder.

### 5. Do NOT: extend the `c_k` ladder, or consolidate onto the most accurate `α_EM` form

Both are the fit signature pointing the wrong way. The ladder is proved empty (§3, W1). And of the
three rival `α_EM` constructions the **smallest residual (+2.59 ppb) belongs to the one whose own
docstring calls its coefficient post-hoc** and which `qou-aymm` has ruled out as PSLQ-empirical.
Choosing by residual selects it. Recorded here because it is the specific trap this arc is
standing next to.

---

## 6. What is needed from research and literature — named

Four gaps where the missing thing is a **citation or a theorem from outside**, not a computation we
have declined to run. Each is stated as the specific statement that is missing.

### 6a. An effective rate for the discrete-Bessel → sine-kernel convergence

The covariance-kernel epic (`qou-x631`, gap `qou-k5r5`, ~40 audits in three weeks) reduces
`M₁ = Cov_Planch(Σh, ω₃) > 0` for all `n` to a Cauchy–Schwarz margin `m(n) > 0`. Leading order is
closed (`m∞ = 0.3001861`, constants exact: `V_A = 8/(9π²)`, `P = 8/(15π)`, `ρ_P = 2√6/5`), exact
finite-`n` is verified for `4 ≤ n ≤ 40` (`m(4) = 0.20025`) — but the margin **oscillates** with
decreasing amplitude rather than approaching the limit monotonically, so small-`n` + leading-order
does not cover all `n`.

**Missing:** an effective variance bound
`|Var_n(Σ g·η)/n² − V_g| ≤ C_g·n^{−a}` for any `a > 0` with explicit `C_g`, `g ∈ {G_A, G_D, x²}`.
Equivalently: **an effective rate for the discrete Bessel kernel `J(x,y;θ)` converging to the
discrete sine kernel in the bulk.** A crude rate suffices — the deviation at `n = 40` is ~0.008
against a 0.30 budget.

**What we hold and why it is not enough:** Borodin–Okounkov–Olshanski is ingested
(`library/arxiv-math-9905032v2`); its Theorem 3 states bulk convergence as a **bare limit with no
error term**. Read at the source. So the held paper gives convergence, not speed.

**Ask:** the later determinantal-asymptotics literature with explicit error terms — the natural
places are the Riemann–Hilbert / Deift-school treatments of the discrete Bessel and Charlier
ensembles, and Baik–Deift–Johansson-lineage edge results that carry rates. Not currently in
`library/`.

### 6b. A non-commutative Penrose tree-graph identity

The Magnus / tr-decay arc (~30 audits) has reduced its theorem to a **non-commutative,
operator-valued matrix-element overlap decay**
`⟨⁅ρ_λ, A_a⁆, A_{a+1}⟩_F / dim_λ → 0`, and every audit named the proof route "the
cumulant / connected-diagram cancellation, tied to Procacci–Yuhjtman / Rebenko."

**Measured (`2026-08-31-cluster-route-literature-assessment.md`): those are a TEMPLATE, not a
plug-in theorem.** Procacci–Yuhjtman (`arxiv-1508.07379v2`), Rebenko (`arxiv-2205.07095v1`) and
Jansen–Kolesnikov (`s10955-022-02992-6`) are all ingested and all **classical and commutative** —
the Penrose tree-graph identity rewrites a sum over connected graphs of products of **scalar**
pairwise Mayer weights.

**Ask:** a tree-graph / cluster-expansion bound where the pair weight is an **operator** and the
product is non-commutative. Free-probability cumulants and the operator-valued
Boolean/free cumulant literature are the obvious neighbourhood;
[`2026-08-31-noncommutative-cumulant-structure-exists-colored-jones.md`](2026-08-31-noncommutative-cumulant-structure-exists-colored-jones.md)
found structure but not the bound. This is a real literature ask, and possibly a real gap in the
literature.

### 6c. The carrier-derivation routes — held, and the question has changed shape

[`2026-09-04-carrier-derivation-held-literature-ledger.md`](2026-09-04-carrier-derivation-held-literature-ledger.md)
measured both library tiers and settles a framing error worth repeating: **the census lookup was a
fit** (`jsj_verification.py` scanning `snappy.LinkExteriors` for volumes near `B_AME/(ρ·m_e)`,
797-fold degenerate, retired by owner ruling 2026-08-29) but **the carrier itself is derived** —
the closure of the canonical atom braid word, a connected sum `#_g T(2, e_g)`, verified against
SnapPy `deconnect_sum` on 32/32 branches with zero mismatches.

So the open question is **not which link but which invariant of that link carries binding.** The
link's structure is branch-independent: `μ = A + 1` components, linking graph the path `P_μ`,
`μ − 1 = A` nonzero linking pairs.

**Held primary:** Finkelstein, *Knots and preons* (`library/arxiv-0806.3105v3`), the SLq(2)
dictionary `(N, w, r) → D^{N/2}_{w/2,(r+1)/2}` — no volume, no census, nothing fitted.
**Ask:** invariants of connected sums of `(2,k)` torus links that are *additive over the connected
sum* — that is the shape an extensive binding term needs, and it is a classical knot-theory
question we have not yet posed to the literature as such.

### 6d. Two infrastructure gaps that are blocking research, not tracking it

- **`corpus_search` (MCP) has been unavailable for at least five consecutive sessions** —
  `paper-assistant` fails `ENOENT`, and `lean-lsp`, `openalex-paper-search` and `paper-search-mcp`
  all `CONNECT_TIMEOUT`. Path 0 of the corpus-grep checklist is the step that survives a change of
  vocabulary; without it **every absence any agent reports is lexical**. The measured spelling
  splits in that audit make the point: `hyperbolization`/`hyperbolisation` **8 / 1**,
  `uniformization`/`uniformisation` **10 / 1**, `Gauss-Bonnet`/`Gauss–Bonnet` **12 / 4** — and
  neither member of any pair is a superset of the other.
- **External egress is 403** (`api.crossref.org`, `export.arxiv.org`: *"CONNECT tunnel failed"*,
  `connect_rejected — policy denial`). So no bibliographic metadata can be verified against a
  publisher record, and **nothing new can be ingested into `library/` from a session.** Every
  literature ask in §6a–6c is therefore an ask *of the owner*, not something an agent can go and
  fetch.

---

## 7. What this reanalysis did NOT do

- **No physics compute was run** except re-running the L2 dashboard (which reproduced unchanged)
  and the four-cell `α_EM` residual arithmetic in §2c, which is shown in full.
- It did **not** re-derive the `c_k` ladder under D. The D-frame figures in §2a are quoted from
  `qou-cds1`'s recorded probe (`qbeta-c3-ladder-trace-convention-sensitivity`, 9/9), not
  re-measured here.
- It did **not** verify the binding log-law's 1.225× band independently; that is quoted from
  [`2026-09-05-binding-law-arc-synthesis.md`](2026-09-05-binding-law-arc-synthesis.md).
- It surveyed 528 audits **by title and by targeted reading of nine**, not by reading all of them.
  A route that landed in the window without a title naming its subject would be missed, and that
  is exactly the lexical blind spot §6d is about.

-- Ref: [manuscript] beans qou-37j2, qou-cds1, qou-aemx, qou-k5r5, qou-o6ov, qou-768r, qou-brng
