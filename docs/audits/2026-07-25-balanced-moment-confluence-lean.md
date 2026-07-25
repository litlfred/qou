# Per-n balanced moment confluence — Lean formalization (the `hmom` discharge)

**Date:** 2026-07-25 · **Bean:** qou-tzci · **PR:** #4250 (tranche home)
**Tier:** Lean formalization of already-probe-exact facts — NO FIT, nothing
wired to production compute; the target conjecture stays a conjecture.

**Target.** The explicit `hmom` hypothesis of the merged conditional theorem
[`balanced_kernel_tendsto_schwinger`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelConfluence.lean)
— per-$n$ moment convergence of the balanced q-Borel kernel to $(n-1)!$ as
$q \to 1$ — carried until now as a bare hypothesis because it was only
probe-exact (sympy; [`qborel_confluence_pos_probe.py`](../../computations/probes/qborel_confluence_pos_probe.py),
audit [`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md) §2).

**New file:**
[`QOU/Archimedean/BalancedMomentConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedMomentConfluence.lean)
(aggregator import added to `QOU.lean`). Verified `lean`-direct **exit 0,
sorry-free** against the restored `lake-cache` oleans; the edited
[`BalancedKernelConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelConfluence.lean)
(docstring-only residual-note update) re-verified exit 0.

## 1. The quarter-power formulation (the honest choice, and why)

The balanced normalizer $N^{\mathrm{bal}}_q(n) = q^{-(n-1)(n-2)/4}\,[n-1]_q!$
carries a quarter-power of $q$, which does not exist in a generic field.
Options considered:

1. **Half-variable $v = q^{1/2}$** (the probe's C4b convention
   $\tilde q = \sqrt q$): the exponent $(n-1)(n-2)/4$ in $q$ becomes
   $(n-1)(n-2)/2 = \binom{n-1}{2}$ in $v$ — an **integer**
   (`Nat.choose (n-1) 2`), since $(n-1)(n-2)$ is a product of consecutive
   integers. All fibre identities stay exact Laurent algebra over a generic
   `Field K`.
2. Squared-only form $N^{\mathrm{bal}}(n)^2$ (fully polynomial in $q$) —
   kept as a proved corollary, but insufficient alone: the un-squared
   bar-invariance (the Attack-E repair) and the $A(k)\cdot B(k)$ split live
   at the $v$-level.
3. `Real.rpow` throughout — rejected for the fibre side (§7c: archimedean
   construct on generic algebra).

**Chosen:** (1) for the generic fibre algebra; the archimedean object is
then literally `balancedNormalizerR q n := balancedNormalizer (Real.sqrt q) n`,
which for $q > 0$ equals $q^{-(n-1)(n-2)/4}[n-1]_q!$ with no `rpow`
anywhere. This also ties the archimedean object to the generic identities
by definition (no bridge lemma needed).

## 2. What is now PROVED (sorry-free, per declaration)

Generic fibre side (`{K : Type*} [Field K]`, §7c — no `ℝ`, no ordering):

| Declaration | Content | Probe leg |
|---|---|---|
| `pow_mul_qint_inv` | $q^k\,[k{+}1]_{q^{-1}} = [k{+}1]_q$ (reflection of the geometric sum) | C1b ingredient |
| `pow_choose_mul_qfact_inv` | $q^{\binom{m}{2}}\,[m]_{q^{-1}}! = [m]_q!$ | C1b |
| `balancedNormalizer_inv` | **bar-invariance** $N^{\mathrm{bal}}_{v^{-1}}(n) = N^{\mathrm{bal}}_v(n)$ — the Attack-E repair, previously probe-only | C1b / Attack E |
| `sq_balancedNormalizer` | $N^{\mathrm{bal}}(n)^2 = [n{-}1]_q!\,[n{-}1]_{q^{-1}}!$ at $q = v^2$ (geometric mean of the bar pair) | C1b |
| `balancedNormalizer_succ` | $N^{\mathrm{bal}}(k{+}1) = [k]_{q^{-1}}!\cdot v^{\binom{k}{2}}$ — the exact $A(k)\cdot B(k)$ positive-kernel split, with $q^{k(k-1)/4} = v^{k(k-1)/2}$ integer-exponent exact | C4d / audit (i) |
| `qint_one`, `qfact_one`, `balancedNormalizer_one` | evaluation at the confluence point: $[k]_1 = k$, $[m]_1! = m!$, $N^{\mathrm{bal}}_1(n) = (n-1)!$ | — |

Archimedean side (`ℝ`, wall-side by construction):

| Declaration | Content |
|---|---|
| `continuous_qint`, `continuous_qfact`, `continuousAt_balancedNormalizer` | continuity of the finite sum/product; the normalizer is continuous at every $v \ne 0$ |
| `tendsto_balancedNormalizerR` | **the per-$n$ confluence:** $N^{\mathrm{bal}}_q(n) \to (n-1)!$ as $q \to 1$ (full two-sided `𝓝 1`, subsuming $q \to 1^+$) |
| `tendsto_balancedNormalizerR_seq` | sequence form along any $q_j \to 1$ — exactly the `hmom` shape |
| `sum_c2_closed_form`, `sum_c2_closed_form_of_one_le` | **the $c_2(n)$ closed form** $\sum_{k=1}^{n-1}(k^2-1)/24 = (n-1)(n-2)(2n+3)/144$ as exact finite-sum algebra over `ℚ` (probe C2's `sympy.summation`, now Lean-proved by induction) |
| `balanced_kernel_tendsto_schwinger_of_confluence` | **the `hmom` discharge** (§3) |

## 3. What `hmom` shrank to

Before (merged `balanced_kernel_tendsto_schwinger`):

> `hmom : ∀ k, Tendsto (fun n => ∫ s^k ∂(K n)) atTop (𝓝 k!)` — bare
> moment-convergence hypothesis, probe-supported only.

After (`balanced_kernel_tendsto_schwinger_of_confluence`):

1. `hqs : qs → 1` — the fibre parameters approach the archimedean point
   (structural, trivially satisfiable);
2. `hrep : ∫ s^k ∂(K j) = N^bal_{qs j}(k+1)` — **balanced-moment
   representability**: the kernels' Stieltjes moments are the balanced
   normalizers. This is the conjecture's genuine open (REP) content
   (audit §4 gap 2) — and by the fibre-indeterminacy finding (audit §3.1)
   it cannot be reduced to moment data at $q \ne 1$, so this is the
   correct irreducible remainder on this leg.

The moment-*convergence* step is now a theorem
(`tendsto_balancedNormalizerR_seq` composed through `hrep`); the two
classical Mathlib-gap classes (`FrechetShohatStieltjes`,
`CarlemanDeterminacyStieltjes`) are inherited unchanged, per the merged
module — no instance exists or was fabricated
(§Axiomatization-is-NOT-a-Proof).

## 4. The quantitative h² layer — honest tiering

- **Proved:** the closed-form sum identity $c_2(n) = \sum_{k=1}^{n-1}
  (k^2-1)/24 = (n-1)(n-2)(2n+3)/144$ (pure algebra, `ℚ`).
- **NOT proved (stated, class-carried, NO instance):** the analytic
  expansion $\log\bigl(N^{\mathrm{bal}}_{e^h}(n)/(n-1)!\bigr) = c_2(n)h^2
  + O(h^4)$ with $h^1 = h^3 = 0$. Formalizing the remainder bound needs
  `Real.log`-series machinery out of scope this tranche; it is carried as
  the content-bearing hypothesis class `BalancedH2Expansion`
  (§3b-tax style, matching the `FrechetShohat` precedent: a true,
  probe-exact, unformalized statement worn in the type by any future
  consumer). Nothing in the corpus consumes it — the `hmom` discharge
  needs only the proved qualitative limit. No `[manuscript]`-cited `sorry`
  was used; the file stays sorry-free.

## 5. Verification + discipline

- **`lean`-direct, exit 0** (restored `lake-cache/qou-v4-24-0` oleans +
  root-workspace QOU oleans; `-D autoImplicit=false`):
  - `QOU/Archimedean/BalancedMomentConfluence.lean` — exit 0, sorry-free;
  - `QOU/Archimedean/BalancedKernelConfluence.lean` (docstring-only
    residual-note update) — exit 0, sorry-free.
  `lake build` deliberately avoided per the lean-environment-setup
  gotcha-#2 (wipes restored oleans).
- **Aggregator:** `import QOU.Archimedean.BalancedMomentConfluence` added
  to `QOU.lean` beside `BalancedKernelConfluence`.
- **§7c base-ring pass (by hand, per formalizer gate):** every fibre
  declaration is over generic `Field K` (inverses algebraic, no ordering,
  no `Real.*`); `ℝ` appears only where archimedean content demands it
  (continuity, `Real.sqrt`, the `exp`/`log` class statement). No
  gratuitous `ℝ`, no ordering hypotheses smuggled into generic
  statements.
- **Compose-don't-restate:** `qint`/`qfact` reused from
  `QOU.Mass.QDifferenceConfluentObstruction` (the corpus convention the
  probe cites); the wiring corollary calls the merged
  `balanced_kernel_tendsto_schwinger` rather than re-proving it.
- **No fit, nothing wired:** no numerics, no q₀ evaluation, no CODATA; the
  conjecture's (REP)/(POS) content remains open and is stated as such.
- **Render-QA (this doc):** preflight grep battery run by hand — balanced
  `$`/`$$`/braces, no `\operatorname`, no markdown-list lines opening
  with `+`/`-`/`*` inside display math, no inline align-family
  environments; the pipeline render was not run in this sandbox, so this
  doc was **not machine-validated** (stated per the render-QA gate).

## 6. Cross-references

- New Lean: [`BalancedMomentConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedMomentConfluence.lean)
- Discharged-into: [`BalancedKernelConfluence.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedKernelConfluence.lean); classes in [`FrechetShohat.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/FrechetShohat.lean)
- Probe + audit: [`qborel_confluence_pos_probe.py`](../../computations/probes/qborel_confluence_pos_probe.py), [`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md)
- Balanced-twist precedent (half-variable conventions): [`BalancedQuantumTwist.lean`](../../content/quantum-observable-universe/lean/QOU/Common/BalancedQuantumTwist.lean)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
