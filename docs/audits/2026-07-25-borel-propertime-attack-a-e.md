# Binding Borel variable = loop proper time — Attack A (moment-determinacy reduction) + Attack E (bar-covariance falsifier)

**Date:** 2026-07-25 · **Beans:** qou-7gu9 (Attack A) + qou-zfl0 (Attack E), epic qou-q04o · **PR:** #4201
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; the target conjecture (its
content block is being authored in parallel by a sibling agent — no content
blocks touched here) stays a conjecture.

**Target.** The Borel-plane variable of the binding OGF resummation — the C1
carrier of [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
(forced normalizer $N(n) = (n-1)!$, recurrence $[m+2]_q\,b_{m+2} = b_{m+1} + b_m$;
the q-Borel/Gevrey-normalized kernel per the
[confluent-narrowing audit](2026-07-20-qdifference-kernel-confluent-narrowing.md))
— is conjecturally the SAME variable as the Schwinger proper time $s$ in the
ζ-regularized photon determinant $\int_0^\infty \frac{ds}{s}\,\mathrm{Tr}\,e^{-s\Delta}$
on Jac(Bring) (the $a_0 = 1/(4\pi)$ leg;
[`SchwingerMeasureShape.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean)).
Source lead: [`2026-07-25-r2core-schwinger-measure-exploration.md`](2026-07-25-r2core-schwinger-measure-exploration.md)
§2(d′)/§5.

**Probe:** [`computations/probes/borel_propertime_moment_attack_probe.py`](../../computations/probes/borel_propertime_moment_attack_probe.py)
→ [`borel-propertime-moment-attack.witness.json`](../../computations/probes/borel-propertime-moment-attack.witness.json)
— 9/9 assertions, exit 0 (sympy exact + mpmath 50 dps; audit-only).
**Lean:** [`QOU/Archimedean/BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)
— sorry-free, verified `lean`-direct exit 0 against the restored `v4-24-0`
olean cache (the missing dep olean `QDifferenceConfluentObstruction` was
compiled by hand with `lean --root -o` first); wired into `QOU.lean`.

## 1. Attack A — the moment-determinacy reduction

### 1.1 The exact statement

Both sides carry the same moment data:

- **Binding:** the keystone bridge PROVES $n \cdot N(n) = n!$, i.e.
  $N(n) = (n-1)!$, as the unique normalizer strip making the binding OGF the
  C1 carrier ([`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md)).
- **Loop:** the unit ($c = 1$) Schwinger kernel has
  $\int_0^\infty s^n\, e^{-s}\, \frac{ds}{s} = \Gamma(n) = (n-1)!$ for
  $n \ge 1$ (probe A1, exact $n = 1..8$; Lean `moment_eq_factorial`, stated
  index-shifted as $\int_0^\infty s^{n+1} e^{-s}\, ds/s = n!$).

**Index honesty (probe A2).** The kernel $e^{-s}\,ds/s$ has infinite mass at
$s = 0$ ($\int_0^\infty e^{-s}\,ds/s = \infty$, exact). The determinacy
statement therefore lives on the index-shifted FINITE measure $e^{-s}\,ds$
with Stieltjes moments $m_k = \int_0^\infty s^k e^{-s}\,ds = k! = N(k+1)$,
$k \ge 0$.

### 1.2 Carleman verdict: DETERMINATE

Carleman's condition for the Stieltjes problem of $\{k!\}$ holds, verified
exactly:

- Stirling asymptotics (exact sympy limit):
  $\lim_{k\to\infty} (k!)^{1/(2k)}/\sqrt{k} = e^{-1/2}$, so the Carleman
  terms behave as $(k!)^{-1/(2k)} \sim \sqrt{e/k}$.
- Exact minorant: $k! \le k^{2k}$ (verified $k = 1..200$; trivially from
  $k! \le k^k$) gives $(k!)^{-1/(2k)} \ge 1/k$, and $\sum 1/k = \infty$ —
  hence $\sum_k (k!)^{-1/(2k)} = \infty$.
- **Lean-carried:** `carleman_minorant` ($1/k \le (k!)^{-1/(2k)}$, sorry-free,
  via `Nat.factorial_le_pow` + rpow monotonicity) and `carleman_divergence`
  (non-summability, by comparison with `Real.not_summable_one_div_natCast`).
- Hankel consistency (probe A4): $\det[(i+j)!] > 0$ and $\det[(i+j+1)!] > 0$,
  sizes $1..6$, exact integers.

By the classical Carleman–Stieltjes determinacy theorem (Simon 1998, *The
classical moment problem*; **not formalized in Mathlib** — the Lean proves
its exact hypothesis, not the theorem), the moment problem for $\{k!\}$ is
**determinate**: $e^{-s}\,ds$ is the UNIQUE positive measure on $(0,\infty)$
with these moments.

### 1.3 The reduction (the deliverable)

Since the moment sequence is determinate, the conjecture reduces to exactly
two open hypotheses about the binding side:

1. **(POS)** the binding Borel resummation kernel — the weight $K_b(s)\,ds$
   realizing $B_n = b_n \int_0^\infty s^n K_b(s)\, ds/s$ — is a **positive
   measure** on $(0,\infty)$;
2. **(REP)** its $ds/s$-moments are the keystone-forced $(n-1)!$ (the
   keystone forces the normalizer *values*; that they arise as the moments
   of the substrate's own kernel is not proved).

Given (POS) + (REP), determinacy forces $K_b(s)\,ds = e^{-s}\,ds$: the
binding Borel variable and the loop proper time then carry the *same*
kernel — which is the identification, up to variable naming. This is a
genuine structural narrowing: the conjecture is no longer "two variables are
the same" but "the substrate resummation weight is a positive measure with
the already-forced moments".

**Lean carrier of the reduction:** the §3b-tax hypothesis class
`BindingKernelSchwingerRepresentation` (fields `positive`, `integrable`,
`moments` — content-bearing, **no instance**; creating one would launder the
conjecture) plus the PROVED conditional theorem
`kernel_moments_eq_schwinger`: any kernel satisfying the class is
moment-indistinguishable from the unit Schwinger kernel. The residual gap to
kernel equality is exactly the classical determinacy step of §1.2.

**Unit forcing (re-carried in Lean).** `unit_forced` / `half_unit_fails`:
with kernel $c \cdot e^{-s}\,ds/s$ the moments are $c\,(n-1)!$ and the proved
bridge identity forces $c = 1$; $c = \tfrac12$ gives $n!/2 \ne n!$ — the
r2core §5 distinguisher, now sorry-free Lean (conditional on the
identification, the Schwinger unit and the ρ-split-vs-E-Jacobian reading are
pinned as before; nothing new claimed unconditionally).

### 1.4 Binding-side positivity status: what is proved vs open

| item | status |
|---|---|
| coefficient positivity $I(n) > 0$ | **PROVED** (Lean `BindingGevreyHalf.involutionNumber_pos`; recomputed exactly to $n = 41$) |
| C1 carrier $b_n = I(n)/n!$ a Stieltjes moment sequence | **FALSE** — log-convexity fails exactly: $b_2^2 = 1 > b_1 b_3 = 2/3$ (violations at $m = 2..6,\dots$). So (POS) is a statement about the resummation KERNEL, not the carrier coefficients — the two must not be conflated. |
| raw periods $B_n = I(n)/n$ log-convex (necessary Stieltjes condition) | **PASSES** for $2 \le n \le 39$ (exact rationals) — consistent with, but far from proving, a positive-measure representation of the raw series (recorded as status, not evidence of (REP)) |
| (POS) kernel positivity | **OPEN** — corpus grep (docs/audits, content, computations, coordination) found no prior Stieltjes/positive-measure representability statement for the binding OGF |
| (REP) moment representability | **OPEN** — same |
| Frobenius-positivity SDP constraints | different object: they constrain Wedderburn-block pairings $\langle \pi_\lambda, \Phi\rangle \ge 0$ (`confinement-sdp`), not the Borel kernel; **no transfer established** (a future derivation of (POS) from the SDP feasibility would be the natural route — noted, not attempted) |

## 2. Attack E — the falsifier, and its verdict

**The computable consequence beyond the shared $\Gamma(n)$ moments:** if the
binding Borel variable IS the loop proper time, the bar involution
($q \mapsto q^{-1}$) must act compatibly — and loop proper time is **real**,
hence bar-invariant.

### 2.1 E1 — bar-covariance of the one-sided q-Borel normalizer (FAIL as stated)

Exact, symbolic ($n = 1..8$; Lean sorry-free `qint_reflect`,
`qfact_reflect`, `keystone_normalizer_not_bar_invariant`):

$$
[k]_{q^{-1}} = q^{1-k}[k]_q
\quad\Longrightarrow\quad
N_{q^{-1}}(n) = q^{-\binom{n-1}{2}} N_q(n),
\qquad \binom{n-1}{2} = \tfrac{(n-1)(n-2)}{2}.
$$

The weight is nontrivial for every $n \ge 3$ at generic $q \ne 1$: the
one-sided (corpus-convention) q-Borel normalizer is bar-**covariant** while
the loop proper time is bar-**invariant**.

> **Scope-(a) verdict: FAIL for the identification as stated with the
> one-sided normalizer $N_q(n) = [n-1]_q!$ at $q \ne 1$.** The exact
> discrepancy is the weight $q^{-(n-1)(n-2)/2}$. At $q = 1$ (the
> archimedean/classical shadow, where the loop actually lives) the weight is
> $1$ and nothing is refuted — the classical identification is untouched.
> This is a scope-limited negative on one stated carrier convention, not a
> structural exclusion of the identification.

### 2.2 E2 — the exact repair: the balanced kernel (the bar-projection caveat)

The **balanced** normalizer
$N^{\mathrm{bal}}_q(n) = q^{-(n-1)(n-2)/4}\,[n-1]_q!$ (equivalently built
from balanced integers $(q^{k/2}-q^{-k/2})/(q^{1/2}-q^{-1/2})$ — the
corpus's `BalancedQuantumTwist` convention) is **exactly bar-invariant**
(symbolic, $n = 1..8$; Lean `balanced_bar_invariance` in the doubled
variable $q_{\text{paper}} = Q^2$, where quarter powers become monomials).

So the falsifier's outcome is constructive: **the identification survives
iff the conjecture's kernel is read in the balanced convention** — the
bar-projection caveat has an exact, unique form, and it is the same balanced
convention the corpus already uses for quantum dimensions. This mirrors the
r2core (b′) finding (the ½'s bar-even home is per-channel/post-split): the
proper-time-compatible Borel variable is the bar-symmetrized one.

### 2.3 E3 — the subleading (q → 1) pattern falsifier (exact)

Per-moment relative corrections, exact series:

| side | first-order correction of the $n$-th moment | $n$-dependence |
|---|---|---|
| binding, one-sided $N_q(n)/(n-1)!$ | $1 + (q-1)\tfrac{(n-1)(n-2)}{4} + O((q-1)^2)$ | **quadratic** |
| binding, balanced $N^{\mathrm{bal}}_q(n)/(n-1)!$ | $1 + 0\cdot(q-1) + O((q-1)^2)$; at $q = e^h$ the $h^2$ coefficient is $\sum_{k=1}^{n-1}\tfrac{k^2-1}{24}$ (exact) | **zero** at first order |
| loop, heat-kernel $a_1$-correction | $(n-1)!\,(1 + \tfrac{a_1}{A}\,n + \dots)$ (exact: $\int s^{n+1}e^{-s}ds/s = n\,(n-1)!$) | **linear** |

The one-sided pattern (quadratic in $n$) matches **neither** the loop side's
q-independence at fixed geometry (zero) **nor** any $a_1$-type curvature
correction (linear in $n$) — E1's FAIL reproduced at the moment level with
the exact discrepancy. The balanced kernel's vanishing first-order
correction matches the loop side's q-independence at the archimedean level —
PASS (still unproved). The surviving balanced $q^2$-order coefficient
$\sum_{k=1}^{n-1}(k^2-1)/24$ is recorded as the **next-order falsifier
target** (any loop-side deformation the q-direction maps to would have to
reproduce it).

### 2.4 E4 — pin numerics (recorded, not scored)

At both q₀ pins (muon canonical-3-CAL witness string; proton
`Q_50_DIGIT_STR`), 50 dps: the one-sided defect at $n = 6$ is
$(q_0-1)\cdot 5 \approx 0.55$ relative — an $O(1)$ discrepancy at the
substrate value, not a small correction; the balanced ratio's pin shift is
at the known $\sim 10^{-8}$ pin-separation scale. Witness `pin_numerics`.

## 3. Honest gap list

1. **The identification stays a conjecture.** Attack A reduces it to
   (POS) + (REP) (§1.3); neither is proved, both are named as fields of a
   no-instance Lean class. The geometric leg of
   `conj:qdifference-kernel-prolongation-symbol` is untouched.
2. **Carleman *determinacy* is classical, not formalized.** The Lean proves
   the divergence hypothesis (`carleman_divergence`), not the
   Carleman–Stieltjes theorem itself (no Mathlib moment-problem theory).
   The reduction's last step is a cited classical theorem.
3. **The bar-projection caveat is forced but its physical reading is not
   derived.** E1/E2 show the identification needs the balanced kernel; that
   the substrate's resummation *is* balanced (rather than one-sided) is a
   convention-level claim of the same species as the r2core ½-adjudication
   — consistent with the (b′) bar-even channel story, not derived from it.
4. **The q-lift bridge's one-sided convention.** `KeystoneBridgeC1Binding`'s
   q-lift leg is stated (and proved) for the one-sided $[n-1]_q!$; E1 shows
   that convention cannot be the proper-time-identified one at $q \ne 1$. A
   balanced restatement of the bridge (replacing $[k]_q$ by balanced
   integers) is the natural follow-up Lean brick — queued, not landed;
   nothing in the proved bridge is wrong (it is a normalization identity,
   convention-agnostic at $q = 1$).
5. **(POS) route not attempted.** The Frobenius-positivity SDP constraints
   are the plausible derivation route for kernel positivity (§1.4); no
   transfer is established here.
6. **Whole-library Lean status.** Verification is `lean`-direct (exit 0) on
   the new file against the restored olean cache with a hand-compiled dep
   olean; `lake build QOU` was not run (per the lean-direct discipline — the
   whole-library build is red on pre-existing failures and is not the gate).

## 4. Discipline

- **Corpus-grep (all four paths).** `Stieltjes|Carleman|moment problem|
  log-convex` over docs/audits, content, computations, coordination: no
  prior statement of the determinacy reduction, no prior positivity/
  representability result for the binding kernel (nearest: the
  channel-rotation-askey block notes an *indeterminate* moment problem for
  the non-compact q-Hermite channel — a different object). The r2core
  exploration §5 states the moment identity and the $c$-forcing but not the
  determinacy reduction, the Hankel/Carleman verification, or the bar
  falsifier.
- **NO FIT.** Every check is an exact symbolic identity or an exact integer/
  rational computation; the two q₀ pin strings appear only in E4's recorded
  (unscored) numerics; no CODATA read; nothing wired; no content block
  touched; no instance of the conjecture class created.
- **Scope-(a) throughout.** The E1 refutation is classified scope-limited
  (one stated carrier convention, at $q \ne 1$), with the exact excluding
  identity displayed; the balanced repair is stated, not asserted as the
  substrate's convention.
- **Formalize-first.** The Lean core (moment identity, Carleman minorant,
  unit forcing, bar reflections) was proved before and alongside the probe;
  the probe verifies the same identities symbolically and adds the
  subleading/pin layers.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening with
  `+`/`-`/`*` inside display math; no inline align-family environments; the
  pipeline render was not run in this sandbox — stated explicitly per the
  render-QA gate: this doc was **not machine-validated**).

## 5. Cross-references

- Source lead: [`2026-07-25-r2core-schwinger-measure-exploration.md`](2026-07-25-r2core-schwinger-measure-exploration.md) (§2(d′), §5)
- Keystone bridge (the proved normalizer): [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md), [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
- Confluent narrowing (why the Borel plane): [`2026-07-20-qdifference-kernel-confluent-narrowing.md`](2026-07-20-qdifference-kernel-confluent-narrowing.md)
- Schwinger shell: [`SchwingerMeasureShape.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean); R2 owner ruling [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)
- Balanced convention: [`BalancedQuantumTwist.lean`](../../content/quantum-observable-universe/lean/QOU/Common/BalancedQuantumTwist.lean)
- New Lean: [`BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)
- Probe + witness: [`borel_propertime_moment_attack_probe.py`](../../computations/probes/borel_propertime_moment_attack_probe.py), [`borel-propertime-moment-attack.witness.json`](../../computations/probes/borel-propertime-moment-attack.witness.json)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
