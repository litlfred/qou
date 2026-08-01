# (REP) Attack 2 — tightness of the balanced kernel family ⇒ archimedean (REP) without fibre uniqueness

**Date:** 2026-08-01 · **Bean:** qou-ry7x (REP attack 2), epic qou-q04o
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; the target conjecture
stays a conjecture. No content block touched. One NEW Lean file
(`BalancedKernelTightness.lean`); the sibling-owned files
(`BalancedMomentConfluence` / `BalancedKernelConfluence` / `QOU.lean` /
`FrechetShohat.lean`) are imported or referenced, never modified.

**Target.** The archimedean **(REP)** leg of
[`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
for the **constructed** balanced kernel family of Attack B §3
([`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md)):
the atomic Jackson $\circledast$ theta kernel $K^{\mathrm{at}}_q$ and the
a.c. Jackson $\circledast$ log-normal kernel $K^{\mathrm{ac}}_q$
($\sigma^2 = \tfrac{\ln q}{2}$, $\hat\mu = -\tfrac{\ln q}{4}$) are
explicit positive probability measures on $(0,\infty)$ with Stieltjes
moments exactly $N^{\mathrm{bal}}_q(k+1)$, and the per-$k$ moment
convergence $N^{\mathrm{bal}}_q(k+1) \to k!$ as $q \to 1^+$ is
Lean-proved (`BalancedMomentConfluence`). **Claim established here:**
the family is **tight**, so — by Prokhorov selection plus the
Lean-proved factorial-moment determinacy pin — every subsequential weak
limit is *the* Schwinger measure $e^{-s}\,ds$. Crucially this route
never uses fibre-level uniqueness, which is **false** at $q \ne 1$ (the
balanced moment problem is indeterminate, Attack B §3.1): determinacy
enters only for the archimedean limit sequence $\{k!\}$.

**Probe:** [`computations/probes/rep_tightness_probe.py`](../../computations/probes/rep_tightness_probe.py)
→ [`rep-tightness.witness.json`](../../computations/probes/rep-tightness.witness.json)
— 5/5 assertions, exit 0 (sympy exact + mpmath 60 dps, tol $10^{-30}$;
audit-only; both q₀ pins).
**Lean:** [`QOU/Archimedean/BalancedKernelTightness.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelTightness.lean)
— sorry-free, verified by `lean`-direct (exit 0) against the pinned
toolchain `leanprover/lean4:v4.24.0` olean cache.

## 1. The analytic argument (tightness is nearly free)

**Normalization consistency (the $dK$ vs $ds/s$ subtlety).** All
kernels are stated in Attack A's A2-shifted convention, identical to
`FrechetShohat.lean`'s `HasStieltjesMoments`: finite (probability)
measures $K$ on $[0,\infty)$ with

$$
\int_0^\infty s^k \, dK_q \;=\; N^{\mathrm{bal}}_q(k+1), \qquad k \ge 0,
$$

so the mass is $N^{\mathrm{bal}}(1) = 1$ and the limit object is
$e^{-s}ds$ with moments $k! = N(k+1)$. The conjecture's $ds/s$-moment
shape $\int s^n \, dK/s = N^{\mathrm{bal}}(n)$ is the same statement.
The "second moment" below is the $k = 2$ Stieltjes moment
$N^{\mathrm{bal}}(3)$, with $q \to 1$ limit $2! = 2$. All measures live
on the same space $\mathbb{R}$ (supported on $[0,\infty)$); no
renormalization varies along the family — the tightness question is
well-posed as stated.

**Step 1 — the second moment is exact and monotone.** For $m = 2$,

$$
\int s^2 \, dK_q \;=\; N^{\mathrm{bal}}_q(3)
\;=\; q^{-1/2}\,[2]_q! \;=\; \frac{1+q}{\sqrt{q}}
\;=\; 2 + \frac{(\sqrt{q}-1)^2}{\sqrt{q}},
\qquad
\frac{d}{dq} N^{\mathrm{bal}}_q(3) \;=\; \frac{q-1}{2\,q^{3/2}} \;>\; 0
\ \ (q > 1),
$$

both exact (sympy, probe T1). Hence on the whole family interval
$q \in (1, q_0]$ the second moment increases from $2$ to
$C_2 := N^{\mathrm{bal}}_{q_0}(3)$ — the uniform bound covers **every**
$q$ in the interval analytically, not merely sampled values (at the
proton pin $C_2 \approx 2.00272236$; at the Attack-B test value
$q = 1.2$, $C_2 \approx 2.00831604$). Equivalently: the second-moment
sequence *converges* (to $2! = 2$) along any ladder $q_n \to 1^+$, and a
convergent real sequence is bounded — the form the Lean file uses.

**Step 2 — Markov gives uniform tail control.** For any member and any
$R > 0$,

$$
K_q\bigl((R,\infty)\bigr)
\;\le\; \frac{1}{R^2} \int s^2 \, dK_q
\;=\; \frac{N^{\mathrm{bal}}_q(3)}{R^2}
\;\le\; \frac{C_2}{R^2},
$$

so for every $\varepsilon > 0$ the single compact window
$[0, \sqrt{C_2/\varepsilon}\,]$ catches mass $\ge 1 - \varepsilon$ of
**every** family member simultaneously: the family is tight, with the
$\varepsilon$-compact exhibited explicitly. No kernel-specific tail
estimate (theta decay, log-normal decay) is needed — the already-proved
moment convergence at $k = 2$ suffices. This is the sense in which
tightness is *nearly free*.

**Step 3 — the composition.** Tight ⇒ (Prokhorov selection, classical)
a weakly convergent subsequence exists. Along any convergent
subsequence the moments still converge to $\{k!\}$; (moment passage,
classical: uniform integrability of $s^k$ from the bounded
$s^{2k}$-moments) the limit measure realizes the moment data $\{k!\}$;
and the merged determinacy pin (Carleman divergence for $\{k!\}$,
Lean-proved + the classical Carleman theorem) forces the limit to be
$e^{-s}\,ds$. Since every subsequential limit is the same measure, the
archimedean (REP) statement holds for the constructed family — with the
fibre indeterminacy (two distinct positive kernels sharing all balanced
moments at $q \ne 1$) never contradicted: uniqueness is invoked only at
the archimedean boundary $q = 1$.

## 2. Lean status — proved vs class-carried

File: [`QOU/Archimedean/BalancedKernelTightness.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelTightness.lean)
(new; namespace `QOU.Archimedean.BalancedKernelTightness`; imports the
merged `FrechetShohat` + `BalancedKernelConfluence` infrastructure and
Mathlib's `MeasureTheory.Measure.Tight` / `TightNormed`).

| Declaration | Status | Content |
|---|---|---|
| `tail_measureReal_le` | **PROVED** | Markov: $\mu.\mathrm{real}\{s : R \le \lvert s\rvert\} \le C/R^2$ from $\int s^2 \le C$ (via Mathlib `mul_meas_ge_le_integral_of_nonneg`) |
| `measure_compl_closedBall_le` | **PROVED** | the same bound in $\mathbb{R}_{\ge 0}^\infty$ against $[-R,R]^\complement$ (the tightness-API shape) |
| `isTightMeasureSet_of_integral_sq_le` | **PROVED** | uniform second-moment bound ⇒ `IsTightMeasureSet` (Mathlib's tightness, via `isTightMeasureSet_of_tendsto_measure_compl_closedBall`; squeeze against $C/r^2 \to 0$) |
| `exists_forall_le_of_tendsto` | **PROVED** | convergent sequence ⇒ explicit uniform bound (`Filter.Tendsto.bddAbove_range`) |
| `isTightMeasureSet_of_tendsto_integral_sq` | **PROVED** | **the headline leg**: convergent second moments ⇒ tight — for the balanced family the hypothesis is the $k=2$ moment confluence, already Lean-proved upstream |
| `ProkhorovSelectionReal` | **class (Mathlib gap)** | tight sequence on $\mathbb{R}$ has a weakly convergent subsequence (Prokhorov 1956; Billingsley *Convergence*, Thm 5.1). Pinned-Mathlib survey re-confirmed: tightness *definitions* + Lévy–Prokhorov *metrizability* exist; the compactness theorem does not ([gap map](2026-07-25-kernel-convergence-mathlib-gap.md)) |
| `MomentPassageStieltjes` | **class (Mathlib gap)** | all-moments convergence + weak convergence ⇒ the limit realizes the moment data (Billingsley *P&M*, Thm 25.12 / proof of Thm 30.2) |
| `subseq_limit_eq_schwinger` | **PROVED conditional** on `[MomentPassageStieltjes]` + `[CarlemanDeterminacyStieltjes]` | every subsequential weak limit = `schwingerMeasure` — composes the merged determinacy pin `eq_schwingerMeasure_of_factorial_moments` (whose Carleman-divergence hypothesis is Lean-proved); **no fibre uniqueness used** |
| `exists_subseq_tendsto_schwinger` | **PROVED conditional** on the three classes | MAIN: tightness (proved) + selection (class) + passage (class) + determinacy (class, divergence proved) ⇒ a subsequence converges to the Schwinger measure, and all convergent subsequences share that limit |

Discipline notes:

- The two new classes are **content-bearing** (§3b-tax; quantified
  fields in the shape of the classical theorems), carry **no instance**,
  and name true classical theorems with citations — fabricating an
  instance would violate §Axiomatization-is-NOT-a-Proof.
- The gap surface is **strictly finer** than the merged
  `FrechetShohatStieltjes` wholesale class: the analytic core of
  Fréchet–Shohat (tightness) is now discharged in Lean; what remains is
  selection + moment passage (+ the Carleman step, unchanged).
- Verification: `lean`-direct (LEAN_PATH from the restored
  `lake-cache` oleans + the seeded QOU dependency oleans), exit 0,
  sorry-free, no diagnostics. The module is **not yet registered** in
  `QOU.lean` (file owned by a parallel verification agent this
  session) — registration is a one-line follow-up for the parent.
- Base ring (§7c): wall-side $\mathbb{R}$ throughout — tightness/weak
  convergence of Borel measures is archimedean content by construction.

## 3. Numerics (probe, exit 0, 60 dps)

- **T1 (exact, sympy).** The closed forms and the monotonicity
  factorization of §1 Step 1, all exact.
- **T2 (both kernels, 6 q-values).** $\int s^2\,dK = N^{\mathrm{bal}}(3)$
  for the atomic (separable Mellin factors $[2]_p! \cdot q^{1/2}$) and
  a.c. (Jackson × exact Gaussian moment) kernels, rel $< 10^{-30}$, at
  $q \in \{1.2,\ q_0^{\mathrm{proton}},\ q_0^{\mathrm{muon}},\ 1.1,\
  1.01,\ 1.001\}$; every value below the exact monotone bound. E.g.
  proton pin: $2.00272236386053329\ldots$ (both kernels, both variants
  identical to 25 digits).
- **T3 (Markov tails).** At $q \in \{1.2, q_0^{\mathrm{proton}}, 1.01,
  1.001\}$, $R \in \{2,4,8,16,32\}$: tails of both variants ≤ the
  Markov bound at every point — e.g. proton pin, $R = 8$: bound
  $3.13\times 10^{-2}$, actual tails $\approx 3.6\times 10^{-4}$;
  $R = 32$: bound $1.96\times 10^{-3}$, actual $\approx 10^{-13}$ (the
  true decay is exponential-type; Markov is lossy but sufficient —
  diagnostic only). Atomic tails are computed exactly as prefix sums
  over the separable Jackson-tail × theta-atom decomposition; a.c.
  tails as Jackson mixtures of log-normal $\mathrm{erfc}$ complementary
  CDFs.
- **T4 (the tightness certificate).** With $C_2$ from the max tested
  $q$: $\varepsilon = 10^{-2} \Rightarrow R(\varepsilon) \approx 14.17$,
  observed $\sup_q$ tail $1.7\times 10^{-6}$;
  $\varepsilon = 10^{-4} \Rightarrow R \approx 141.7$, sup tail
  $1.0\times 10^{-29}$; $\varepsilon = 10^{-6} \Rightarrow R \approx
  1417$, sup tail $7.4\times 10^{-78}$ — one compact window per
  $\varepsilon$ for the whole family, with enormous slack.
- **T5 (the $k=2$ confluence leg).** $N^{\mathrm{bal}}_q(3) - 2 =
  (\sqrt q - 1)^2/\sqrt q$ to rel $< 10^{-30}$, strictly decreasing
  down the ladder $q = 1 + 10^{-k}$: $2.27\times 10^{-3} \to
  2.50\times 10^{-13}$ ($k = 1..6$) — the exact $O(h^2)$ rate, matching
  Attack B's $c_2(3) = 1/8$ (since $(\sqrt q - 1)^2/\sqrt q =
  \tfrac{h^2}{4} + O(h^3) = 2\,c_2(3)\,h^2 + O(h^3)$ at $q = e^h$).

## 4. What this closes — and what it does not

**Closed (conditional on the two named classical gaps + Carleman):
archimedean (REP) for the CONSTRUCTED family.** The explicit positive
balanced kernels converge weakly (subsequentially, with all limits
equal) to $e^{-s}\,ds$ — positivity survives the limit for free, the
moments are the keystone-forced factorials, and the route is robust to
the fibre indeterminacy because it never needs the fibre moment problem
to be determinate. The *unconditional* Lean content added: the family
is tight (Markov from the proved moment convergence), i.e. the analytic
hypothesis Prokhorov needs is discharged, not assumed.

**NOT closed:**

1. **The (REP-1) identification** — that the *corpus's own* resummation
   kernel is a member of this family. The parallel REP-1 tranche
   ([`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md))
   found the corpus performs **no** binding-side integral at all —
   (REP) is a canonical-choice premise, and at $q \ne 1$ moments +
   symmetry do not pin the choice. Nothing here changes that: this
   tranche's result is about the constructed family's $q \to 1$
   behaviour, not about which kernel the substrate "uses".
2. **The two classical theorems** (Prokhorov selection; moment
   passage) and the Carleman determinacy step — Mathlib gaps, carried
   as content-bearing classes with no instance. Formalizing any of
   them is an upstream Mathlib contribution.
3. The conjecture itself — unchanged in kind: its open content is
   (REP-1)'s identification plus (for the full statement) the
   classical-analysis package above.

## 5. Discipline

- **Corpus-grep (all four paths).** `prokhorov|tightness|
  IsTightMeasureSet` over docs/audits, docs/coordination, content,
  computations: the only substantive prior statements are the gap map
  ([`2026-07-25-kernel-convergence-mathlib-gap.md`](2026-07-25-kernel-convergence-mathlib-gap.md):
  Prokhorov compactness MISSING from the pinned Mathlib — re-confirmed
  here against the pinned oleans) and the REP-1 sibling doc's scope
  note deferring tightness to this tranche. No prior tightness proof or
  claim exists; nothing is re-declared open that was closed.
- **NO FIT.** Every scored check is an exact symbolic identity or an
  exact-value cross-check at $10^{-30}$; the tail numbers are
  *inequality* verifications with no tuned quantity; the q₀ pin strings
  enter only as evaluation points; no CODATA read; nothing wired; no
  content block touched; no class instance created.
- **Scope-(a) throughout.** The verdict is "(REP) for the constructed
  family, conditional on named classical theorems" — not a proof of the
  conjecture, and explicitly not the substrate identification.
- **Formalize-first.** The Markov/monotonicity argument was derived
  and Lean-formalized (sorry-free) with the probe as numerical
  cross-check of displayed identities; the probe contains no search.
- **Sibling non-interference.** `BalancedMomentConfluence.lean`,
  `BalancedKernelConfluence.lean`, `QOU.lean`, `FrechetShohat.lean`
  untouched (verification agent); Jackson-identification files
  untouched (REP-1 agent). The new file only *imports* merged
  infrastructure.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening
  with `+`/`-`/`*` inside display math; no inline align-family
  environments; the pipeline render was not run in this sandbox —
  stated explicitly per the render-QA gate: this doc was **not
  machine-validated**).

## 6. Cross-references

- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- Attack B (the kernels + fibre indeterminacy): [`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md)
- REP-1 (parallel, the identification negative): [`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
- Mathlib gap map: [`2026-07-25-kernel-convergence-mathlib-gap.md`](2026-07-25-kernel-convergence-mathlib-gap.md)
- Merged Lean infrastructure: [`FrechetShohat.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/FrechetShohat.lean), [`BalancedKernelConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelConfluence.lean), [`BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)
- New Lean: [`BalancedKernelTightness.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelTightness.lean)
- Probe + witness: [`rep_tightness_probe.py`](../../computations/probes/rep_tightness_probe.py), [`rep-tightness.witness.json`](../../computations/probes/rep-tightness.witness.json)
- Classical references: Prokhorov, Theory Probab. Appl. 1 (1956);
  Billingsley, *Convergence of Probability Measures* 2nd ed. Thm 5.1;
  Billingsley, *Probability and Measure* 3rd ed. Thm 25.12, Thm 30.2;
  Fréchet–Shohat, Trans. AMS 33 (1931); Simon, Adv. Math. 137 (1998)
