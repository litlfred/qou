# The Plancherel-weight sweep: which of the 22 producers were actually wrong

**Date:** 2026-09-05
**Bean:** `qou-uk8o`
**Upstream finding:** [`2026-09-04-plancherel-convention-gap.md`](2026-09-04-plancherel-convention-gap.md) (bean `qou-7o7h`)
**Registry:** [`trace-convention-registry.md` §B-norm](../coordination/trace-convention-registry.md)

## 0. The one-line finding, and the correction to the triage rule

The upstream audit established that $w(\lambda) = d_q^2(\lambda)/[n]_q!$ is a
probability measure at $q = 1$ and nowhere else, summing instead to a constant
$c_n$ that varies with $n$. Because the weight enters linearly, any quantity
built from it is scaled by exactly $c_n$.

The sweep was framed on this triage rule:

> $c_n$ depends only on $n$, so it **cancels in any comparison made at fixed
> $n$**, and does not cancel across different $n$.

**That rule is right about the cross-$n$ case and wrong as a sufficient
condition, and two of the eight producers fixed here are fixed because of the
gap.** The correct statement is:

> $c_n$ cancels **iff the reported quantity is a ratio of two $w$-weighted sums
> at the same $n$.** It does not cancel when
> **(i)** $w$-weighted quantities at different $n$ are compared (the stated
> case), **or**
> **(ii)** a $w$-weighted quantity at one $n$ is compared against something
> that is *not* $w$-weighted — an experimental magnitude, a closed-form
> scalar, a $y_\lambda$-weighted object.

Category (ii) is the one a fixed-$n$ screen waves through.
`deuteron_fpn_wlambda_wiring` sits at $n = 3$ and compares $W_{(2,1)}$ against
the AME-required $f_{pn}$; `yekutieli_volume_join` sits at $k = 3$ and compares
a $w$-weighted $J$ against a closed-form production scalar. Both were exposed;
neither is cross-$n$.

Positive confirmation of the rule's *correct* half, measured rather than
argued: in `wlambda_jet_tower_connected_probe` the self-normalization moves
$w_{std}(k)$ by up to 10 % while the std **fraction** — a ratio at one $k$ — is
unchanged to 6 decimal places at every level.

## 1. Counts

| | |
|---|---|
| producers in the sweep set | **22** (the bean says ~23; the list is 22) |
| **AFFECTED and fixed** | **8** |
| **AFFECTED, deliberately not fixed** | **3** (reasons in §4) |
| **UNAFFECTED** | **10** |
| **excluded by design** | **1** |
| conclusions/verdicts that changed | **0 verdict strings; 1 substantive reading** (§3) |

## 2. Per-producer table

`cross-n?` is the stated triage question. `exposed?` is the corrected one —
does the producer report a quantity in which $c_n$ fails to cancel.

| producer | cross-n? | exposed? | verdict | old → new headline | conclusion changed? |
|---|---|---|---|---|---|
| [`log_delta_full_mass_subtract.py`](../../computations/log_delta_full_mass_subtract.py) | yes | **yes (i)** | FIXED | max/min 9.3468 → 17.8477 (self-norm), 21.1756 (q-Plancherel self-norm) | **reading reverses — see §3** |
| [`log_delta_per_depth_binding.py`](../../computations/log_delta_per_depth_binding.py) | yes | **yes (i)** | FIXED | same figures; `all B_pred > 0` **False → True** | **yes — sign defect disappears** |
| [`deltalambda/wlambda_jet_tower_connected_probe.py`](../../computations/deltalambda/wlambda_jet_tower_connected_probe.py) | yes | **yes (i)** | FIXED | $w_{std}(9)$ 62.193 → 55.984 | no (both assertions pass) |
| [`deltalambda/wlambda_level_selection_kA_probe.py`](../../computations/deltalambda/wlambda_level_selection_kA_probe.py) | yes | **yes (i)** | FIXED | $R^2(k\sim\log\text{bonds})$ 0.8912 → 0.8966 | no (ordering unchanged) |
| [`deltalambda/wlambda_wstd_growth_bound_probe.py`](../../computations/deltalambda/wlambda_wstd_growth_bound_probe.py) | yes | **partly (i)** | FIXED | $w_{std}(q_0,10)$ 193.92 → 161.48 | no — **strengthened**, see §3 |
| [`sweeps/light_isotope_sweep.py`](../../computations/sweeps/light_isotope_sweep.py) | yes | **yes (i)** | FIXED | ⁴He err −92.694 % → −95.245 % | no |
| [`probes/deuteron_fpn_wlambda_wiring.py`](../../computations/probes/deuteron_fpn_wlambda_wiring.py) | **no** | **yes (ii)** | FIXED | $W_{(2,1)}$ 0.66067377 → 0.66907723 | no (bracket survives) |
| [`yekutieli_volume_join.py`](../../computations/yekutieli_volume_join.py) | **no** | **yes (ii)** | FIXED | ratio $h^1$ −533/288 → −67/32 (proton); $h^{-1}$ unchanged | no |
| [`alpha/alpha_5_jucys_murphy_central.py`](../../computations/alpha/alpha_5_jucys_murphy_central.py) | yes | yes (i) | **not fixed** | spread 482 % vs a 10 % threshold | no — margin 48×; §4.1 |
| [`sigma_shell_characterization.py`](../../computations/sigma_shell_characterization.py) | yes | yes (i) | **not fixable** | — | §4.2 (normalizer needs $p(84)$) |
| [`atom_level_wedderburn_tower.py`](../../computations/atom_level_wedderburn_tower.py) | yes | yes (i) | **not fixed** | — | §4.3 (retired by owner ruling) |
| [`jet_knot_invariants.py`](../../computations/jet_knot_invariants.py) | tabulates | **no** | unaffected | — | $a_k$ is a ratio of two $w$-weighted sums at one $k$ |
| [`substrate/wlambda_identity_i_structure_probe.py`](../../computations/substrate/wlambda_identity_i_structure_probe.py) | no | **no** | prose fixed | no number moves | §5 — it *is* the corpus's detector |
| [`wedderburn_beta3_provenance_probe.py`](../../computations/wedderburn_beta3_provenance_probe.py) | no | no | **must not change** | — | §6.1 |
| [`q_pinning_50_digit.py`](../../computations/q_pinning_50_digit.py) | no | no | **protected** | — | §6.2 — anchor-defining |
| [`alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py`](../../computations/alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py) | no | no | unaffected | — | §6.3 — already carries the caveat |
| [`sweeps/paper_six_term_shadow_price_sweep.py`](../../computations/sweeps/paper_six_term_shadow_price_sweep.py) | tabulates | **no** | unaffected | — | its one comparison is T vs ³He, both $n=9$ |
| [`chirality_avg_content_atomic.py`](../../computations/chirality_avg_content_atomic.py) | tabulates | **no** | unaffected | — | $\langle c\rangle$ is num/den, both $w$-weighted at one $n$ |
| [`chirality_avg_content_chiral.py`](../../computations/chirality_avg_content_chiral.py) | no | no | unaffected | — | same ratio structure, $n=3$ |
| [`close_321_weinberg_gap.py`](../../computations/close_321_weinberg_gap.py) | no | **no** | unaffected | — | §6.4 — every CODATA candidate is a ratio |
| [`deltalambda/deltalambda_binding_cross_isotope_probe.py`](../../computations/deltalambda/deltalambda_binding_cross_isotope_probe.py) | yes | **no** | **not in class** | — | §6.5 — does not use this weight |
| [`probes/wenzl_bridge_self_conjugate_premise_is_false.py`](../../computations/probes/wenzl_bridge_self_conjugate_premise_is_false.py) | — | — | **excluded** | — | §7 |

## 3. The conclusions that moved

### 3.1 The log-delta pair — the reading reverses, and the sign defect goes away

**Measure the normalizer per producer; do not reuse $c_n$.** These two bind
`dim_q` to the χ witness's `dim` field, which is the **classical** Specht
dimension $f^\lambda$, not $d_q$ — so the weight is $(f^\lambda)^2/[n]_q!$, and
by Burnside $\sum_\lambda (f^\lambda)^2 = n!$ exactly, so it sums to
$n!/[n]_q!$:

| $n$ | 3 | 6 | 9 | 12 |
|---|---|---|---|---|
| $n!/[n]_q!$ (these producers) | 0.98029937 | 0.85832883 | 0.61193301 | 0.32612477 |
| $c_n = \sum d_q^2/[n]_q!$ (the audit's) | 0.98744023 | 0.99107952 | 1.11092313 | 1.51713321 |

A **3.0× spread, decreasing in $n$** — against the audit's 1.53×, increasing.
Neither the magnitude nor the direction carries over.

| weight form | max/min | T/³He/⁴He only | all $B_{pred} > 0$ |
|---|---|---|---|
| `f2_over_qfact` (as published) | 9.3468 | 2.1598 | **False** |
| `f2_selfnorm` | 17.8477 | 1.0991 | True |
| `dq2_selfnorm` | 21.1756 | 1.0990 | True |
| `identity` | 6.2562 | 1.7771 | True |

The naive reading is that the correction made things worse. It did not: the
9.35× was a **partial cancellation between two errors** — the shrinking
normalizer offset the growing $B_{pred}$. Corrected, T/³He/⁴He agree to
**1.10×** where the old form gave 2.16×, and the entire remaining spread is the
deuteron. "A tight three-atom cluster plus one outlier" is a different and much
sharper statement than "9.35× scatter". The deuteron's **sign** defect
($B_{pred} < 0$) also disappears under both self-normalized forms.

Verdict thresholds were deliberately **not** re-tuned. They are calibrated
against historical baselines, and re-tuning a threshold at the moment its
baseline moves is the trap recorded in
[`2026-09-04-plancherel-convention-gap.md` §7.4](2026-09-04-plancherel-convention-gap.md).
`max_over_min_heavy_three_no_deuteron` is recorded as a derived statistic
instead.

### 3.2 The growth-bound probe — the correction strengthens it

Checks 1 and 2 there carry the whole super-geometric claim and are computed at
$q = 1$, where $(f^\lambda)^2/k!$ **is** a measure exactly, so $c_k = 1$ and
nothing moves. Only check 3 (does $q_0$ track $q=1$?) was exposed. At $k = 10$
the $q_0$ column read 193.92 against 159.66 at $q=1$ — a 21 % gap;
self-normalized it is 161.48, a **1.1 %** gap. Most of the apparent
$q$-deformation of the tower weight was the missing normalization.

### 3.3 An independent cross-check that fell out

The self-normalized $W_{(2,1)}$ at $n=3$ is `0.66907723` in
`deuteron_fpn_wlambda_wiring` and byte-identical to the $k=3$ entry of the
self-normalized jet tower in `wlambda_jet_tower_connected_probe` — two
different code paths, one written in this session and one edited in it.

## 4. Affected, deliberately not changed

### 4.1 `alpha_5_jucys_murphy_central` — margin 48×, and it carries its own control

The verdict is a **refutation**: relative spread across $A = 2,3,4$ of the
$[3A]_q!$-normalized $\alpha_5$ is **482 %** against a 10 % refutation
threshold. The largest $c_n$ ratio available across $n = 6,9,12$ is 1.53×.
A ≤1.53× rescale cannot carry 482 % below 10 %.

More decisively, the probe **already computes a $c_n$-free control**: the
`alpha_5_at_A_partial_normalized` variant is
$\sum_{ht=6} d_q^2 c_5 / \sum_{ht=6} d_q^2$, self-normalized on the height-6
stratum, and its `naive_form_refuted_uniformly_in_q` assertion reports spreads
of 628 % to 279 730 % across the whole $q$ sweep. The refutation is established
on a quantity the defect cannot touch.

Not changed. Any edit here would move 66 fields for no epistemic gain.

### 4.2 `sigma_shell_characterization` — the normalizer is not computable at its own $k$

It tabulates $|y|$ across magic numbers $A = 2, 8, 20, 28$, i.e. $k = 3A =
6, 24, 60, 84$ — genuinely cross-$n$, and $y = w_\lambda/d_{cl} - 1/[k]_q!$ is
a difference of a $w$-weighted term and a non-$w$ term, so nothing cancels.

**But $c_k$ requires summing $d_q^2$ over every partition of $k$**, and
$p(60) = 966\,467$, $p(84) = 26\,543\,660$. The producer itself already avoids
$p(60)$ enumeration ("too slow for argmax here"). Self-normalizing it is not a
matter of will.

This is a real, unclosed exposure and it is recorded as such rather than
worked around. Options for whoever picks it up: an asymptotic $c_k$ (the
$C(n)h^2$ form in §8 is the obvious start, though its error is already 5 % at
$n = 12$), a generating-function evaluation of $\sum_\lambda d_q^2$ that avoids
enumeration, or restricting the tabulation to $A \le 8$.

### 4.3 `atom_level_wedderburn_tower` — retired, by owner ruling

Cross-isotope, and exposed. But its own witness carries
`"precision_tier": "float64"` and a `"deprecated"` block citing the owner ruling
of 2026-08-15: *"exploratory f64 shape-probe; retired rather than rewritten in
mpmath, which would be a rewrite of the numpy matrix core for a leaf nobody
reads"*. Its sole witness reader is itself and its sole importer is a
vocabulary test. Rewriting a producer the corpus has explicitly retired would
contradict a recorded disposition. Not changed.

## 5. `wlambda_identity_i_structure_probe` — the inverted defect

No number moves here, and it is the most interesting entry in the sweep.

The probe **tests** $\sum_\lambda d_q^2 = [n]_q!$ and has always recorded it as
**failing** (`computed: false, expected: true, passed: false`). Its docstring,
its witness `description` and its Lean-infra route verdict all said the
identity was *"verified here"*. The corpus held an assertion measuring the
defect and, three JSON fields away, a sentence asserting the opposite. The
prose is corrected; the assertion is deliberately left EXPECTED-TRUE and
measured-FALSE, with a source note saying so, because it is the corpus's own
detector and lowering `expected` would silence it.

**Re-measured independently while triaging, and this is stronger than the
upstream audit's evidence:** the identity is false **symbolically**, not merely
numerically. `sp.simplify(Σ_λ d_q² − [n]_q!) == 0` holds at $n=1$ and fails at
$n = 2 \ldots 6$; the $n=2$ ratio is exactly $2q/(q^2+1)$, which equals 1 only
at $q=1$. The upstream audit evaluated $c_n$ numerically in mpmath; this route
is sympy-symbolic → mpmath, and the two agree to 15 digits at $n = 3,4,5,6$
(0.987440229774 / 0.982165323836 / 0.982224148283 / 0.991079523637). So the
finding now rests on two independent code paths, one of them exact.

## 6. Unaffected — and why, individually

- **§6.1 `wedderburn_beta3_provenance_probe` — must not be changed.** It asks
  whether the literal `0.0499` in `next_partition_levels.py` is reachable from
  a pre-declared candidate set built out of the $n=3$ Wedderburn weights. That
  is a question about *what a past author computed*, and the sibling scripts
  compute the **unnormalized** weight. Self-normalizing would test a
  construction nobody performed and could flip a 1.27 % shift across a ±0.1 %
  acceptance window, changing a negative result for the wrong reason.
- **§6.2 `q_pinning_50_digit` — protected.** $n=3$ only. It is
  **anchor-defining**: `witness._q0_value_for_anchor` reads it, and AGENTS.md
  constraint 1 forbids re-pinning it. Worth noting that its
  `plancherel_weights_n3.sum` field has been publishing `0.98744023` — i.e.
  $c_3$ itself — all along, unlabelled.
- **§6.3 `alpha_em_b2_canonical_scale_ratio_probe` — already correct about
  this.** $n=5$ fixed; $w_{(4,1)}$ is one of three *declared distinct*
  intrinsic candidates and the source already says so in as many words: *"the
  canonical Markov trace: sum_lam y_lam \* f^lam = 1. (NOT sum_lam w_lam — that
  equals 1 only at q=1 …)"*. It knew.
- **§6.4 `close_321_weinberg_gap` — every comparison is a ratio.** $n=6$
  hardcoded. Path A's candidates against $\cot\theta_W$ are all ratios of two
  `pair_sum`s at $n=6$, so $c_6$ cancels exactly; Paths B and C use eigenvalue
  ratios and hook-length $q$-rationals and carry no Wedderburn weight at all.
- **§6.5 `deltalambda_binding_cross_isotope_probe` — not in the class.** It is
  cross-isotope, but its weight is $y_\lambda \cdot \chi \cdot \mathrm{sgn}
  \cdot d_q^2$ — the Jones–Markov $y_\lambda$ times $d_q^2$, with **no
  $[n]_q!$ division anywhere**. Its only `factorial` call is the classical
  `dim_ordinary`. The sweep list over-collected it.

## 7. Excluded by design

`wenzl_bridge_self_conjugate_premise_is_false` is a deliberate
normalization-variant comparison and its whole conclusion is that **no reading
of $\tilde w = d_q^2/[n]_q!$ satisfies the bridge**. Changing any variant would
destroy the enumeration. (One correction to the bean's wording: it is a
**six**-way comparison, not five — `dim_q^sym²/[n]!^sym`,
`dim_q^unb²/{n}!^unb`, `dim_q^sym²/{n}!^unb`, `dim_ord²/[n]!^sym`,
`dim_ord²/{n}!^unb`, `dim_q^sym/[n]!^sym`.)

## 8. Side finding — the corpus already holds a closed form for $c_n$'s $n$-dependence

The upstream audit says $c_n$ "grows with $n$" and that "simple
$q^{\pm 2n(\lambda)}$ prefactors do not close it". True of the *residual* — but
the leading $n$-dependence is already **proved** in this corpus and neither the
audit nor the registry entry cites it.

`deuteron_fpn_wlambda_wiring` prints, and
[`QOU/BraidKnot/WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean)
proves sorry-free:

$$1 - Z(n) = C(n)\,h^2 + O(h^4), \qquad C(n) = -\frac{n(n-1)(2n-13)}{144}$$

with $Z(n) = \sum_\lambda W_\lambda = c_n$ and $h = q - q^{-1}$. Checked
against the measured $c_n$ at the proton $q_0$ ($h^2 = 0.04370620853$):

| $n$ | $c_n$ measured | $1 - C(n)h^2$ | rel dev |
|---|---|---|---|
| 2 | 0.99458109 | 0.99453672 | −4.5e−5 |
| 3 | 0.98744023 | 0.98725236 | −1.9e−4 |
| 4 | 0.98216532 | 0.98178908 | −3.8e−4 |
| 5 | 0.98222415 | 0.98178908 | −4.4e−4 |
| 6 | 0.99107952 | 0.99089454 | −1.9e−4 |
| 7 | 1.01242609 | 1.01274764 | +3.2e−4 |
| 8 | 1.05056015 | 1.05099058 | +4.1e−4 |
| 9 | 1.11092313 | 1.10926552 | −1.5e−3 |

Four significant figures, and it **predicts the sign change**: $2n-13$ crosses
zero at $n = 6.5$, which is exactly where the measured $c_n$ crosses 1 (below
at $n \le 6$, above at $n \ge 7$). So $c_n$'s $n$-dependence — including the
feature the audit calls "the part that matters" — is not mysterious; it is a
proved $h^2$ coefficient plus an $O(h^4)$ residual that reaches ~5 % by
$n = 12$.

This does not change any verdict above. It is recorded because the audit and
the registry both describe $c_n$ as unexplained while a sorry-free Lean theorem
for its leading term sits in the tree, and because §4.2 needs exactly this if
$c_k$ at $k = 60, 84$ is ever to be estimated.

## 9. Precision, stated rather than dressed up

The five probes whose weight lines were rewritten now carry those weights as
`mpmath.mpf` through a local $q$-dimension, because the shared
`hecke_characters.dim_q` returns a builtin float. **That is hygiene, not a
correction:** $c_n$ departs from 1 by $10^{-2}$–$10^{-1}$, fourteen orders above
the float64 floor, so rounding was never what made these weights
non-normalized.

**`light_isotope_sweep` is the honest exception and is left float64.** The
`float(...)` the bean flagged on its weight line was a **no-op** —
`hecke_characters.dim_q` already returns a float, and the χ it multiplies comes
from a numpy matrix product built on `float(Q0)` (`chi_lambda_numeric`). That
producer is float64 end to end **by construction**; promoting the weight to
`mpf` would claim a precision the characters do not have. Rewriting the numpy
character kernel in mpmath is a separate and much larger job, is **not** done
here, and is not claimed. The comment on that line says so.

Raw-float64 fields actually drained, on lines already being touched:
`log-delta-full-mass-subtract` 16 → 0, `log-delta-per-depth-binding` 6 → 0.

## 10. What was NOT done

- No verdict threshold was re-tuned anywhere. Where a corrected baseline made a
  historical cut-off uninformative, a derived statistic was added beside it
  instead.
- No producer's historical weight form was deleted. Every fixed producer either
  reports both forms or names the old one explicitly (`f2_over_qfact`,
  `w`/`w_selfnorm`, the raw gate emission beside its normalized companion).
- `alpha_5_jucys_murphy_central`, `sigma_shell_characterization` and
  `atom_level_wedderburn_tower` are affected and unchanged, for the reasons in
  §4. `sigma_shell_characterization` is the only one of the three that is a
  live, unclosed exposure.
- The float64 character kernel behind `light_isotope_sweep`,
  `chirality_avg_content_atomic` and `atom_level_wedderburn_tower` is untouched.
- Nothing was changed in
  `q-plancherel-asymptotic-skeleton`, `plancherel-term-7-formulation`,
  `probe_plancherel_convention_gap.py` or the 2026-09-04 audit — a sibling
  session owns those.
