# Saturating shared-channel closure for the mixed multi-bond interface — derive-or-refute

> **⚠ ERRATUM (2026-07-14, R10 — the "resonance at k=A_light" reading is
> FALSIFIED).** The falsifiable prediction stated in §6 item 3 below (the
> deuteron ladder, A_light=2, should peak at k=2) was tested in
> [R10](2026-07-14-deuteron-ladder-falsification.md) and **fails**: the
> deuteron ladder (⁶Li/¹⁰B/¹⁴N/¹⁸F) miss is `[−0.090, 2.807, 5.818, 1.632]`
> at k=[1,2,3,4] — a strict interior maximum at **k=3 (¹⁴N)**, NOT k=2 (¹⁰B).
> The peak sits at the **same k=3** as the triton ladder, and the neutron
> ladder (A_light=1) ALSO peaks at k=3 (¹³C) where the resonance shape is
> degenerate. Three ladders, three A_light values (1,2,3), one peak location
> k=3. **The peak does NOT track A_light — it is a FIXED-k=3 effect (the 3-α
> Brunnian onset / k≥3 α·α gate turn-on).** So candidate (c) below reproduces
> the peak location on the t-ladder *only because A_light=3 coincides with the
> fixed onset k=3* — a coincidence, not a resonance. What A_light actually
> controls is the peak **amplitude** (k=3 heights ≈ 2.8/5.8/8.0 MeV for
> A_light=1/2/3), not its location. **What still STANDS:** the interior-maximum
> invariant (§2) and the two structural prunes it powers — **(P1)** the additive
> non-negative cone and **(P2)** the monotone-saturating 1−∏ idempotent class —
> are unaffected (the invariant holds, indeed is strengthened, on all three
> ladders); only the *mechanistic label* "resonance at k=A_light" is wrong. The
> closure seed sharpens to **(fixed 3-α-onset envelope in k) × (A_light-scaled
> amplitude) × (bar-parity fall)**. Full test:
> [R10 deuteron-ladder falsification](2026-07-14-deuteron-ladder-falsification.md).

**Date:** 2026-07-14 · **Task:** R9 (follows R8) · **Branch:** `claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/saturating_shared_channel_probe.py`](../../computations/deltalambda/saturating_shared_channel_probe.py)
· **Witness:** [`saturating-shared-channel.witness.json`](../../computations/deltalambda/saturating-shared-channel.witness.json)
(allPassed: true, 9/9; witness-fed — misses reproduced from the committed
R8/Model-G witnesses to `1.8e-15` MeV, `b` reused from the committed R5-a
witness, only the 15N deficit read from vendored AME2020; nothing recomputed,
one **fitted** scale, all candidates + thresholds pre-registered)
**Discipline:** formalize-first (`compute-author.md` §3.3) — the
interior-maximum invariant in §2 was stated *before* the candidate
evaluations and prunes two whole classes; the three candidates and the
closed-six regression were pre-registered in the task.

## 1. The clean test — the t-ladder

R8 ([mixed multi-bond](2026-07-14-mixed-multibond-interface-derive-or-refute.md))
proved by a cone/monotonicity invariant that every **additive non-negative**
graph-counting extension of Model G is excluded, and identified the surviving
class as **saturating / sub-additive / sign-changing**. The right object to
attack is the **t-ladder**: fixed light cluster (triton, $A_{light}=3$),
varying $k$ = number of α's, so $A_{light}$ and the triton's internal
structure are held constant and only $k$ moves.

| $k$ | iso | pieces | Model-G miss (MeV) | status |
|--:|---|---|--:|---|
| 1 | ⁷Li | α+t | 0.122 | **closed** (Model-G resid −0.31% of $B$) |
| 2 | ¹¹B | 2α+t | 6.440 | open |
| 3 | ¹⁵N | 3α+t | 8.049 | open |
| 4 | ¹⁹F | 4α+t | 2.679 | open |

The miss **rises then falls** with a strict interior maximum at $k=3$. (⁷Li's
0.122 MeV is scatter, $\approx 0$ against the 6–8 MeV misses; the ladder
misses reproduce the committed R8 values to `1.8e-15` MeV.)

## 2. Formalize-first — the interior-maximum invariant prunes two classes

**Invariant.** The t-ladder miss satisfies
$$
0 \approx M(1) \;<\; M(2)=6.440 \;<\; M(3)=8.049 \;>\; M(4)=2.679,
$$
a **strict interior maximum at $k=3=A_{light}$**. Two consequences, stated
before any fit:

- **(P1) — the additive cone [R8, re-derived].** Any additive non-negative
  counting $V(k)$ is non-decreasing in $k$, so $V(4)\ge V(3)$; the target has
  $M(4)<M(3)$. **Excluded.**
- **(P2) — the monotone-saturating class [NEW].** The canonical
  shared-channel shape $1-\prod_{\text{bonds}}(1-f) = 1-(1-f)^{P(k)}$, with
  $P(k)$ any non-decreasing bond/pair count, is **non-decreasing in $k$** and
  asymptotes *upward* to $V_{max}$. It cannot turn over, so it cannot
  reproduce $M(4)<M(3)$ for **any** $f$ or $V_{max}$. The pure $1-\prod$
  idempotent form (task candidate (a)) is **excluded by the same interior
  maximum** — a structural exclusion, not a bad fit.

Hence the surviving class is genuinely **non-monotone**: a resonant magnitude
peaking at an interior $k$, and/or a parity/sign-graded term. The peak sits
exactly at $k=A_{light}=3$ — the triton's nucleon count — which is the
structural seed for the resonance candidate (c).

**Scope.** (P1)/(P2) exclude the additive-non-negative and monotone-saturating
*classes*, conditional on the committed AME deficits and the all-α
decompositions; they exclude no *ingredient* (permanence) — a saturating
factor may still appear as one piece of a non-monotone closure.

## 3. Candidate table (fit ≤1 constant on ⁷Li+¹¹B, predict ¹⁵N/¹⁹F out-of-sample)

| cand | form | 15N (k=3) OOS | 19F (k=4) OOS | verdict |
|---|---|--:|--:|---|
| **(a)** 1-∏ idempotent | $V\,[1-(1-f)^{C(k,2)}]$ | over (monotone) | over (monotone) | **excluded by (P2)** — non-decreasing, 19F pred > 15N pred for every $f$; the fall never appears |
| **(c)** resonance at $k{=}A_{light}$ | $V\,(k-1)(2A_{light}-1-k)$ | 8.587 (**+6.7%**) | 6.440 (**+140%**) | **partial** — peak location + rising branch reproduced parameter-free; asymmetric fall missed |
| **(b)** parity / bar-graded | even-$k$ decay + odd-$k$ enhancement | — | — | **indicated** — supplies the asymmetric fall (c) misses; not closed with one constant |

**(a) 1-∏ idempotent.** With $P(k)=C(k,2)$ (pairs bridged by the shared
triton; 0 at $k=1$ so ⁷Li is untouched) and $f$ fixed structurally
($\tfrac12,\tfrac13,\tfrac1{A_{light}}$), fitting $V$ on ¹¹B gives a monotone
non-decreasing curve: ¹⁹F is always over-predicted (pred $>$ 15N pred). This
is (P2) in action — the idempotent shared channel saturates *up* and cannot
produce the ¹⁵N→¹⁹F drop.

**(c) resonance at $k=A_{light}$.** The parameter-free symmetric shape
$S(k)=(k-1)(2A_{light}-1-k)$ has zeros at $k=1$ (⁷Li, closed) and
$k=2A_{light}-1=5$, and peaks at $k=A_{light}=3$. With only the scale $V$
fitted on ¹¹B ($V=2.147$ MeV):

- ¹⁵N (k=3) out-of-sample: 8.587 vs 8.049 — **+6.7%**;
- ¹⁹F (k=4) out-of-sample: 6.440 vs 2.679 — **+140%**.

The peak **location** (at $k=A_{light}=3$, the triton's nucleon count) and the
$k{=}2\to k{=}3$ **rise** are reproduced with no shape parameter. The ¹⁹F
overshoot is honest: a *symmetric* parabola is too shallow on the descending
($k>A_{light}$) side.

**(b) parity / bar-graded.** Split the ladder by parity. The **even**
sublattice decays: ¹¹B ($k{=}2$) 6.440 → ¹⁹F ($k{=}4$) 2.679 (ratio 0.416) — a
genuine sub-additive fall. The **odd** $k=3$ (¹⁵N) sits **+3.49 MeV above** the
even-neighbour mean (4.560). So the real curve is even-sublattice decay *plus*
an odd-$k$ enhancement — a bar-parity grading (even → Vol/mass, odd → decay,
the Ohtsuki-tower pattern) is **indicated** as exactly the asymmetric term the
symmetric resonance (c) lacks. This connects to the R8 "odd-Z pairing physics"
next-step. It is not closed here with a single constant.

## 4. Closed-six regression (disjoint support — the strongest outcome)

The shared channel is gated on $\{A_{light}\ge 2 \text{ AND } k\ge 2\}$ (the
exact R8 trio selector). The closed six all **fail** the gate — ⁶Li/⁷Li have
$m=1$; ⁸Be/⁹Be/¹²C/¹⁶O have $A_{light}\le 1$ (pure-α or single-$n$) — so the
term is **identically 0** on them. Their committed Model-G residuals are
therefore **unchanged**: ⁶Li +0.28%, ⁷Li −0.31%, ⁸Be +0.16%, ⁹Be −0.02%,
¹²C −0.26%, ¹⁶O −0.28% of $B$ (all $<0.5\%$). Disjoint support is the
strongest possible regression result — no tuning could break the closed six
because the channel is zero there by construction.

## 5. Honest classification

**PARTIAL / NEGATIVE (scope-(a) for ingredients; structural exclusion of two
classes, invariant cited).**

- **Structural exclusions (invariant cited).** The interior-maximum invariant
  excludes both the additive non-negative cone (P1, R8 re-derived on the
  t-ladder) and — new here — the entire **monotone-saturating $1-\prod$
  idempotent class** (P2): task candidate (a) cannot turn over for any $f$,
  so its failure at ¹⁹F is structural, not a fit miss. Conditional on the
  committed AME deficits and the all-α decompositions; no ingredient excluded.
- **Partial (scope-(a)).** The resonance-at-$k{=}A_{light}$ shape (c)
  reproduces the peak location and the rising branch parameter-free and lands
  ¹⁵N out-of-sample to +6.7% with one fitted scale, but over-predicts ¹⁹F by
  +140% — the descending side is asymmetric.
- **Indicated missing term.** The even sublattice is itself a decaying
  sub-additive channel; the odd $k{=}3$ peak is an enhancement above it. A
  **bar-parity grading** is the identified missing piece supplying the
  asymmetric fall — the odd-Z pairing route, not an invented constant.
- **Nothing derived.** The resonance scale $V$ and the parity split are
  **fitted / indicated**, not derived; $b$ and all deficits reused from
  committed witnesses. Nothing wired; no tier change.

**Net.** The saturating/sub-additive **class survives** the interior-maximum
prune (unlike the additive and the monotone-saturating classes), and the
turnover is now localized structurally: a resonance at $k=A_{light}$ (peak +
rise, reproduced) times a bar-parity even-$k$ suppression (the fall,
indicated). This is a genuine narrowing — the missing object is a
**resonant, parity-graded** shared channel, not any monotone saturation.

## 6. Next steps (named, not run)

1. **Two-piece closure.** Compose the resonance envelope (peak at
   $k=A_{light}$) with the even-$k$ bar-parity suppression and test whether a
   *single* structurally-motivated constant closes all four ladder members
   out-of-sample. The even-sublattice decay ratio (0.416) is the first datum
   to derive.
2. **Derive the bar-parity grading.** Check the corpus's Ohtsuki-tower /
   `mirror_split_*` machinery (even → Vol/mass, odd → decay) supplies the
   odd-$k$ enhancement before inventing a term — the R8 odd-Z pairing route.
3. **Second light cluster. ✗ DONE / FALSIFIED (R10).** The deuteron ladder
   ($A_{light}=2$; ⁶Li/¹⁰B/¹⁴N/¹⁸F) was tested in
   [R10](2026-07-14-deuteron-ladder-falsification.md): it peaks at **k=3**
   (¹⁴N), not the predicted k=2 (¹⁰B). Together with the neutron ladder
   ($A_{light}=1$, peak k=3) and the triton ladder ($A_{light}=3$, peak k=3),
   the peak is **fixed at k=3** and does not track $A_{light}$ — the resonance
   reading is refuted (see the erratum at the top). $A_{light}$ controls the
   peak *amplitude*, not its location. The invariant and the P1/P2 prunes
   stand.
4. **R5-full SDP knot-ID (#604)** remains the principled route to the
   composite interface (unchanged).

## Provenance

Inputs: committed
[`alpha-activation-brunnian.witness.json`](../../computations/deltalambda/alpha-activation-brunnian.witness.json)
(Model-G rows, $b$; misses reproduced), committed
[`mixed-multibond-interface.witness.json`](../../computations/deltalambda/mixed-multibond-interface.witness.json)
(t-ladder misses cross-checked to `1.8e-15` MeV), vendored AME2020
(`_ame_binding_mev`, ¹⁵N deficit only). Companions:
[R8 mixed multi-bond](2026-07-14-mixed-multibond-interface-derive-or-refute.md),
[Model G consolidated record](2026-07-14-model-g-consolidated-record.md),
[R6-a Brunnian gate](2026-07-13-alpha-activation-brunnian-derive-or-refute.md).
The canonical shared-channel $1-\prod$ shape is the corpus's
[`binding_block_multiplicative.py`](../../computations/binding_block_multiplicative.py)
convention. EXPLORATORY — audit + witness only; no production wiring; scale
$V$ fitted (stated as such); nothing tuned beyond the one declared constant.
Render-QA: pipeline render unavailable in this sandbox; the manual grep
battery (balanced `$`/`$$`/`{}`/`\begin`-`\end`; no `\operatorname`; no
list-hijack lines in display math; align-family fenced) was run by hand — not
machine-validated.
