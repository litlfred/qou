# z → c_k f-map keystone — coordination ledger

**Branch:** `claude/z-c-k-f-map-keystone-ub5yix`
**Opened:** 2026-07-06 (owner instruction: "open z→c_k f-map keystone")
**Beans:** milestone `uz9i`; tasks `3iwu` (this ledger), `ea56` (formalize-first
hypothesis class), `c4qz` (gated P-C15 probe, blocked by `ea56`), `iw8o`
(sibling coordination).
**Master ledgers:** [`1ppq-qbeta.md`](1ppq-qbeta.md) (Q_β authority) ·
[`ck-dk-canonical-registry.md`](ck-dk-canonical-registry.md) (tiers — flip-flop
guard) · [refuted-class map](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
(methods C1–C15).

## 1. The keystone, precisely

Exhibit the **f-map**: the assembly that takes the proved pre-archimedean
$z$-side data — the Markov parameter $z(q) = \sqrt q/(1+q)$ with its exact
3-term recursion, equivalently the exact anchor-independent $\hbar_q$-Taylor
sequence $a_n$ of $\Delta\mathrm{tr}_M$ — into the Q_β precision-ladder rungs
$c_k$ (equivalently: construct the fibre-level Habiro element $F(q)$ / kernel
$R(q,\xi)$ whose $(u;u)_m \to u^k$ coefficients are the $c_k$, with the
$z$-data as its upstream structural input).

Named as "the open f-map" in
[`prop:qbeta-z-recursion-to-ck-recursion-bridge`](../../content/quantum-observable-universe/mass-theory/qbeta-z-recursion-to-ck-recursion-bridge.md)
(§"Claims not established by this block": no concrete `CKRecursion ℝ`
instance, no formula for $c_k$ in terms of $a_n$ — both contingent on the
f-map). This ledger opens that item as a work tranche; it does **not**
change any registry tier.

## 2. Proved inputs (do not re-derive)

| input | status | where |
|---|---|---|
| $z$-recursion backbone $4(n{+}1)a_{n+1} + 6n\,a_n + (2n{-}1)a_{n-1} = 0$ | sorry-free | `MarkovParameterRecursion.lean` / `ZRecursionCoeffs` (PR #1739); bridge triple `qbeta-z-recursion-to-ck-recursion-bridge.*` |
| Exact anchor-independent $\hbar$-Taylor of $\Delta\mathrm{tr}_M$: $a_n = -5/4, -13/8, -33/16, -77/32, \dots$ | exact, executed | PR #2465 (`habiro_mode_to_ladder_bridge.py`); refuted-class map §3 forward constraint |
| Conditional recursion engine (`CKRecursion`) | sorry-free (conditional — no values) | `prop:q-beta-c-k-recursion-from-habiro-q-difference`; registry §5 |
| Non-constant-coefficient engine | sorry-free | `QOU/QBeta/RationalCoeffRecurrence.lean` |
| Kernel constraints: non-constant, $a_2 = c_2 = -1$, $a_1$ bar-ODD, constant depth-2 refuted | sorry-free | `QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean` |
| Phase reframe: $Q_\beta/Q_A = \cos\Phi(u)$, $\Phi_1 = \sqrt2$ anchor-exact; $\Phi_2 \approx 1.46324616887618$ (p) / $1.42849728553818$ (μ) is the open object | Lean + probe | PR #1887; synthesis §2.4 |
| f-map is mode-selective onto the (2,1) standard block (bar-odd carrier $\kappa_{(2,1)} = (q-1)^3(q+1)/q^2$); scalar f-maps excluded | symbolic-exact | [2026-06-13 heat f-map audit](../audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md) |
| f-map must re-mix bar-parity across levels ($L_0$ odd / $L_1$ even / $L_2$ odd / $L_3$ mixed) | probe, 7/7 asserts | Hoefsmit Stage B (PR #2106 arc) |
| P-C15: 4₁ order-2 qZeilberger operator survives the bar-parity gate — **live $R(q,\xi)$ candidate** | sorry-free Lean + symbolic witness | [2026-07-03 P-C15](../audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md); `QOU/QBeta/QCasoratianBarParity.lean` |

## 3. Standing exclusions binding this tranche (do not re-run)

- **C13** — a $\Delta\mathrm{tr}_M$-seeded **linear / bar-even** $f$ is
  REFUTED (gives constant $c_3 \approx -1.4\ldots-1.5$, not $-2$). The
  surviving f-map is **non-linear** in $\Delta\mathrm{tr}_M$. (PR #2465.)
- **C1–C4** real-q scalar forms (1309-candidate saturated sweep); **C5**
  constant kernels through depth 4 + constant depth-2 (PR #1900); **C12**
  trace-level $\mathrm{Ind}_{H_3}^{H_4}$ Markov-stabilization; **C14** forced
  root-of-unity scalars.
- **Integer brane-tower level** in the $1/u^k$ amplification: refuted
  (swing-locked, PR #1887 update).
- **Precision floor** (σ(c_k) = σ_R/u^k): only $c_2, c_3$ are
  data-determined. Any f-map candidate is validated by **structural gates +
  exact $c_2 = -1$ + $c_3 \to -2$ shadow + cross-anchor stability** — never
  by fitting $c_{k\ge4}$.
- **Flip-flop guard** (registry §8): nothing wires to production here; any
  future wiring needs owner approval + passing proton+muon cross-anchor.
- 2026-07-04 ledger note "do not open a separate Q_β probe" is superseded
  **for this tranche only** by the explicit owner instruction opening the
  z→c_k f-map keystone (2026-07-06). The s5-so3 keystone (`W_λ`) remains a
  distinct, parallel item.
- **Live sibling inputs (2026-07-06):**
  [PR #3429](https://github.com/litlfred/qou/pull/3429) is pruning the
  pure-power non-linear class `f = A\cdot(\Delta\mathrm{tr}_M)^m` (odd $m$
  → half-integer rung; $m=2$ → forbidden $c_1$; $m=4,6$ generically killed)
  — if it lands, the `ea56` hypothesis class starts from
  {compositional / operator-level} only; cite, do not re-derive.
  [PR #3447](https://github.com/litlfred/qou/pull/3447) falsifies the
  main-landed "c₃ = −2 exact for all q" claim (2.375% cross-anchor swing;
  registry near-match tier stands) — this ledger uses c₃ only as the q=1
  shadow gate, consistent with that verdict.

## 4. Plan of attack

1. **Formalize-first (bean `ea56`).** Before any probe: state the surviving
   hypothesis class as a formal object. The $z$-side kernel is depth-2 with
   $n$-dependent rational coefficients; the $c_k$-side engine admits
   non-constant q-rational kernels (`RationalCoeffRecurrence`). Task: pin
   which kernel classes on the $c_k$ side are *reachable* from a
   $z$-generated $F$ under the $(u;u)_m \to u^k$ change of basis, given
   (i) $u_L = b\hbar_q^2$ is quadratic in $\hbar$ (even-order pairing),
   (ii) C13 non-linearity, (iii) bar-parity re-mix, (iv) the (2,1)
   projection. Output: a Lean-stated compatibility lemma (or a documented
   structural exclusion narrowing the class), per compute-author §3.3.
2. **Gated probe (bean `c4qz`, blocked by 1).** Run the P-C15 4₁ operator
   against the exact $a_n$ data through the
   [7-step preflight](../audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md):
   does the qZeilberger operator, seeded by the $z$-backbone, reproduce
   $c_2 = -1$ exactly and the $c_3 \to -2$ q=1 shadow with the bar-odd
   $a_1$? Kill criteria pre-stated before the run; scope-(a)/(b) phrasing
   per AGENTS.md on any negative.
3. **Coordinate (bean `iw8o`).** Intent on overlapping Q_β siblings
   (the #3273 / #3294 lineage; any active `qbeta-*` branches).

## 5. Session log

| date | event |
|---|---|
| 2026-07-06 | Tranche opened; beans `uz9i`/`3iwu`/`ea56`/`c4qz`/`iw8o`; this ledger landed as first commit. PR [#3449](https://github.com/litlfred/qou/pull/3449). |
| 2026-07-06 | Intent posted on overlapping siblings [#3429](https://github.com/litlfred/qou/pull/3429) (f-map power-class pincer — same axis; C15 row/probe-id collision flagged) and [#3447](https://github.com/litlfred/qou/pull/3447) (c₃-not-exact verdict — framing here confirmed consistent). Gemini reviewer at daily quota; Copilot reviewer check failed (bot-side) — docs-only PR, no code CI. |
| 2026-07-06 | **Bean `ea56` DONE — the z-alone exclusion (scope-(a)).** `z(q)=√q/(1+q)` proved **exactly bar-EVEN** (twist 1) and `κ_{(2,1)}` exactly bar-ODD, sorry-free Lean [`QOU/QBeta/ZBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean) (`lean`-direct exit 0) + sympy-exact 7/7 witness. Since the bar-fixed locus is a subring and `a₁ = −c₃` is bar-ODD nonzero, **no scalar rational function of z alone can source `a₁`** — class Z2 excluded; survivors are Z3 (bar-even z-functional × bar-odd carrier) and Z4 (operator-level / P-C15). Hypothesis-class lattice: [`docs/scope/2026-07-06-z-ck-fmap-hypothesis-class.md`](../scope/2026-07-06-z-ck-fmap-hypothesis-class.md). Bean `c4qz` unblocked. |
