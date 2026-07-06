# lw(2) c=2 prediction — independent-test ATTEMPT (Hopf link), honest negative (2026-06-24)

**Direction:** lever-1, direction C. **Discipline:** corpus-grep + no-fit +
the AGENTS.md (a)/(b) refutation-scope rule. **Disposition:** the test was
*attempted* against a genuinely independent c=2 object and the result is a clean
**scope-limited (a) negative** — no fabricated match, no built-to-fit.

**Follows:** [`2026-06-24-lw2-c2-prediction-untested-status.md`](2026-06-24-lw2-c2-prediction-untested-status.md)
(established lw(2) is derivation-tight but structurally untestable). This audit
**executes the attempt** that the prior status doc deferred, and confirms its
conclusion with an explicit independent compute.

## The question (restated, sharpened)

Can the selection rule's c=2 value

$$
  \mathrm{lw}(2)(q) \;=\; \tfrac{1}{3}\!\sum_{\lambda \vdash 3} \dim_q V_\lambda
  \;=\; \frac{1 + [2]_q + 1}{3} \;=\; \frac{(q+1)^2}{3q}
  \;\approx\; 1.3370 \ \text{at } q_0,
$$

be **tested** against an *independent* c=2 (2-component-link) object — one
computed **without** reference to the selection rule — so that the comparison is
non-circular?

## Corpus-grep — what independent c=2 / Hopf objects already exist

| object | value at $q_0$ | source (independent of the selection rule) |
|---|---|---|
| Hopf-link Markov trace $\mathrm{tr}_M(\sigma_1^2)$ (Wenzl & q-Schur agree at $H_2$) | $1+\tfrac{q-1}{\sqrt q} \approx 1.1044$ | [`trm-hopf-sigma1-sq-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/trm-hopf-sigma1-sq-closed-form.md) — proved over $\mathbb{Q}(q^{1/2})$ |
| Hopf q-Schur-Plancherel trace $y_2 q^2 + y_{11}q^{-2}$ | $\approx 1.0437$ | [`torus_knot_markov_trace_closed_form.py`](../../computations/torus_knot_markov_trace_closed_form.py), [`markov_trace_for_knot.py`](../../computations/markov/markov_trace_for_knot.py) |
| Hopf linking number $\mathrm{lk}(L_H)$ | $+1 = Q_{pp}$ | [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md), [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md) |
| Hopf Hoefsmit-(2,1) eigenvalues of $\sigma^2$ | $(q^2,q^{-2})=(1.232,0.812)$ | [`HopfBindingLinkEigenvalueIdentity.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/HopfBindingLinkEigenvalueIdentity.lean) (sorry-free) |
| U(1) framing factor $q^{w\cdot c}$ ($w{=}2,c{=}1$) | $q^2 \approx 1.232$ | [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md) |

So independent c=2 Hopf data **does** exist (a Markov trace, a linking number, an
eigenvalue pair, a framing factor). The Hopf diquark
([`hopf-diquark.md`](../../content/quantum-observable-universe/observations/hopf-diquark.md))
is the natural physical c=2 object but carries **no** mass / VolDensity / linking-
weight number to compare. **No production `linking_weight` exists at c=2** — only
the c=3 `linking_weight_family_a` in `_li_2_q_util.py`.

## The compute — independent Hopf trace vs the lw(2) target

Script: [`lw2_c2_independent_hopf_test_attempt.py`](../../computations/lw2_c2_independent_hopf_test_attempt.py)
· witness `lw2-c2-independent-hopf-test-attempt.witness.json` (4/4 assertions
pass, 60-dps compute / 50-dps serialise, canonical $q_0$ from
`qou_substrate.constants.q_at`). The Hopf trace is derived from the Hecke
quadratic relation $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$ and the Markov axioms
$\mathrm{tr}(1)=1,\ \mathrm{tr}(\sigma_1)=z$ — **zero selection-rule input**.

| quantity | value at $q_0$ | rel-miss vs lw(2) |
|---|---:|---:|
| **TARGET** lw(2) $=(q+1)^2/(3q)$ | **1.336966** | — |
| INDEP Hopf $\mathrm{tr}_M(\sigma_1^2)=1+(q-1)/\sqrt q$ | 1.104388 | **17.40 %** |
| INDEP Hopf q-Schur-Plancherel $y_2q^2+y_{11}q^{-2}$ | 1.043706 | 21.93 % |

**The independent c=2 object does NOT equal 1.337** (best miss 17.4 %, gate 1 %).

## Why this is a clean negative, not a near-miss to be closed

The mismatch is **structural**, not a small residual to be patched:

1. **They are different q-functions.** Symbolically (sympy),
   $\mathrm{lw}(2)(q) \not\equiv \mathrm{tr}_M(\sigma_1^2)(q)$; they coincide only
   at two *isolated* algebraic values $q \in \{1.4618\ldots,\ 8.7397\ldots\}$,
   **neither equal to $q_0$**. Forcing agreement at $q_0$ would be a coincidence-
   fit (PSLQ-coincidence antipattern), not a test.

2. **They disagree even in the classical limit $q\to1$:** lw(2) $\to 4/3$ (the
   *mean dimension* of $S_3$), whereas $\mathrm{tr}_M(\mathrm{Hopf}) \to 1$. A
   genuine "same object" would agree at $q=1$.

3. **lw(c) is the wrong KIND of object to be a single-link trace.** The decisive
   identification:
   $$
     \mathrm{lw}(c) \;=\; \frac{1}{c+1}\sum_{\lambda\vdash c+1}\dim_q V_\lambda
     \;=\; \frac{I_q(c+1)}{c+1},
   $$
   the **q-deformed involution number** $I_q(n)=\sum_{\lambda\vdash n}\dim_q V_\lambda$
   divided by $n$ (at $q=1$, $I(n)=$ #involutions in $S_n$ by Frobenius–Schur:
   $I(2,3,4,5)=2,4,10,26$, matching $1{+}1,\ 1{+}2{+}1,\ 1{+}3{+}2{+}3{+}1,\ldots$).
   It is a **mean quantum dimension** — a representation *count* averaged over all
   irreps of $H_{c+1}$. A Markov trace $\mathrm{tr}_M(\beta)=\sum_\lambda y_\lambda\chi_\lambda(\beta)$
   is a *single braid word's* weighted character. **There is no braid word whose
   Markov trace equals the mean dim$_q$.** So no independent single-link trace can
   ever equal lw(2): the comparison is a category mismatch, not a tuning target.

## The circularity gate — confirmed

The c=3 anchor was **not** validated by an independent Markov trace either: lw(3)
$=(1/4)\sum_{\lambda\vdash4}\dim_q$ is *literally the same formula* re-used as the
production proton VolDensity multiplier `linking_weight_family_a` — it is the same
mean-dimension object, not an independent trace. (And that c=3 value $\approx2.533$
is itself flagged in `_li_2_q_util.py` as "a CODATA-implied near-match … not a
derived categorical count.") The c=1 anchor is lw(1)$=1$, trivially the muon knot.

Therefore the **only** object equal to $1.337$ at $q_0$ is the lw(2) formula
itself. Any "test" that reaches $1.337$ must route through the selection rule ⇒
**circular**. The independent Hopf trace, which does *not* route through the rule,
lands at $1.104$ — a clean 17 % away. There is no non-circular path to $1.337$
with the objects currently in the corpus.

## Verdict (AGENTS.md (a)/(b) scope rule)

- **Class (a) — scope-limited negative.** *The natural independent c=2 object (the
  Hopf-link Markov trace), alone, does not reproduce the selection-rule c=2 value*
  (1.104 vs 1.337). This constrains the **identification** ("the Hopf trace is the
  wrong independent object"), not lw(2)'s magnitude or validity.
- **NOT class (b) — no structural exclusion of lw(2).** lw(2) $=(q+1)^2/(3q)$
  **remains derivation-tight** (Lean-proved, `selection-rule-c2-prediction`).
  Nothing here refutes the selection rule. The negative is that
  $\mathrm{tr}_M(\mathrm{Hopf})$ is a *trace*, while lw(2) is a *mean dimension* —
  different objects, so the trace is not a valid test of the rule.
- **Is lw(2) now testable?** **No — still circularity-gated / structurally
  untestable.** A genuine non-circular test needs a c=2 **mass-CONSUMER**: a
  production mass (or binding) model for a 2-component-link object that
  *independently requires* a linking weight, derived from c=2 structure without
  citing the selection rule. None exists; building one is the research-grade,
  circularity-gated path the prior audit named — out of scope for a quick compute,
  and not attempted here (it would risk a built-to-match result). The honest
  disposition is unchanged: **lw(2) is the selection rule's standing falsification
  target, awaiting a c=2 mass-consumer.**

## Discipline statement

- **Does** confirm independent c=2 Hopf data exists (Markov trace, linking number,
  eigenvalues, framing) and **does** compute the Hopf Markov trace from first
  principles (Hecke + Markov axioms), independent of the selection rule.
- **Does** show the independent object ($1.104$/$1.043$) does NOT equal the lw(2)
  target ($1.337$); 17–22 % miss; assert-the-refutation witness (4/4 green).
- **Does** identify lw(c) as a mean quantum dimension (q-involution-number/(c+1)),
  structurally distinct from any single-link Markov trace, and proves
  lw(2)$\not\equiv$tr$_M$(Hopf) as q-functions (isolated coincidences, none at $q_0$).
- **Does NOT** fit, tune, or force any q-form to $1.337$; does NOT modify any
  production file; does NOT wire to production; does NOT advance L2; does NOT
  discharge any Lean `sorry`. No LP/SDP solve (no dual required).

## Cross-references

- Prior status (deferred the attempt): [`2026-06-24-lw2-c2-prediction-untested-status.md`](2026-06-24-lw2-c2-prediction-untested-status.md).
- The c=2 closed form (Lean-proved): [`selection-rule-c2-prediction.md`](../../content/quantum-observable-universe/climax-volume-mass/selection-rule-c2-prediction.md).
- The c=1/c=3 anchors: [`selection-rule-anchors-c1-c3.md`](../../content/quantum-observable-universe/climax-volume-mass/selection-rule-anchors-c1-c3.md).
- The lw(c) unification: [`binding_selection_rule_tau_closure.py`](../../computations/binding_selection_rule_tau_closure.py).
- Independent Hopf trace closed form: [`trm-hopf-sigma1-sq-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/trm-hopf-sigma1-sq-closed-form.md).
- Independent c=2 EM-linking data: [`2026-06-03-em-linking-invariant.md`](2026-06-03-em-linking-invariant.md).
- Hopf diquark (physical c=2 object, no mass): [`hopf-diquark.md`](../../content/quantum-observable-universe/observations/hopf-diquark.md).
- This compute + witness: [`lw2_c2_independent_hopf_test_attempt.py`](../../computations/lw2_c2_independent_hopf_test_attempt.py).
