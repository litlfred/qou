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

## 4-bis. Bean `c4qz` — pre-statement (identifications + kill criteria, BEFORE any run)

The 4₁ order-2 qZeilberger operator (P-C15 survivor) is a recurrence in the
color `N` with coefficients rational in `x = q^N`; the c_k ladder is indexed by
the rung `k`. Candidate identifications:

- **I-A (color↔rung, direct):** slot the operator's normalized homogeneous
  coefficients `α₁ = −a₁/a₂`, `α₂ = −a₀/a₂` into the depth-2 kernel slots of
  `QBetaCKRecursionKernelConstraints` (`α₂ ↔ c₂ = −1`, `α₁ ↔ −c₃`), with `x`
  a free evaluation point (the classical `M = q^N` held fixed as `q → 1`).
- **I-B (cyclotomic re-basing):** push the `N`-recurrence through the Habiro
  `(q;q)_n` expansion to an induced recurrence on the cyclotomic coefficients,
  then the `(u;u)_m → u^k` basis change (the 2026-06-13 audit §2-bis bridge).
  Genuinely hard; NOT attempted in this probe.
- Caveat recorded up front: the 4₁ operator is **inhomogeneous** (`… = b`);
  the `CKRecursion` engine is homogeneous. I-A tests the homogeneous part
  only.

**Kill criteria for I-A's q=1 shadow (decidable, no anchors, no fit):**

1. **K1a:** `α₂(q=1, x) ≡ −1` identically in `x` (the `a₂ = c₂ = −1`
   constraint). If not identically `−1` → I-A killed.
2. **K1b:** `α₁(q=1, x) = 2` (the `a₁ = −c₃ → 2` shadow, `c₃ → −2 = J_Hopf(1)`)
   must have a solution `x* ∈ ℝ_{>0}`. Two constraints, one unknown `x` —
   overdetermined unless K1a is identical; no solution → I-A killed.
3. **K2:** the `α₁` slot must be bar-ODD (up to monomial twist) and `α₂`
   bar-EVEN under `q ↦ 1/q, x ↦ 1/x` — slot-parity match with
   `ck_a1_bar_odd_of_c3_odd` + the ea56 exclusion. Wrong parity → I-A killed.

Outcome semantics: PASS = I-A's shadow is *not excluded* (scope-(a) positive;
no c_k value, nothing wired); any KILL → record scope-(a) refutation row and
fall back to I-B / Z3 carriers.

### Outcome (2026-07-06, run after pre-statement commit `c9b873b6`)

**I-A KILLED on K2 (scope-(a)); K1a/K1b structure SURVIVES and transfers.**
Probe [`qbeta_c4qz_fourone_operator_q1_shadow_probe.py`](../../computations/qbeta/qbeta_c4qz_fourone_operator_q1_shadow_probe.py)
→ [witness](../../computations/qbeta/qbeta-c4qz-fourone-operator-q1-shadow.witness.json)
(sympy exact; exit 1 = candidate-excluded convention):

- **K1a PASS — identically:** `α₂(q=1, x) ≡ −1` for ALL `x` — the 4₁
  operator's trailing slot reproduces the proved `a₂ = c₂ = −1` constraint
  with no tuning. (Equivalent to P-C15's `R(q→1) = 1`.)
- **K1b PASS — golden bar-pair locus:** `α₁(q=1, x) = x² − 3x + 3 = 2` exactly
  on `x² − 3x + 1 = 0`, i.e. `x* = (3±√5)/2 = φ^{±2}` — a **bar-conjugate
  pair** (`x*·x*′ = 1`, `x + x⁻¹ = 3` — classical `M + M⁻¹ = 3` locus).
  Recorded as structure, not wired.
- **K2 FAIL — the kill:** `bar(α₁)/α₁` is **not** a Laurent monomial: it
  carries the factor `P₊/(q²x²·P₋)` with
  `P₋ = q²x²−q²x+q²−qx²−qx+q+x²−x+1` (the operator's middle quintic factor)
  and `P₊ ≠ ±P₋` (`P₊ − P₋ = 2q(x²−1)`). Cross-checked against the committed
  P-C15 witness `coeff_bar_ratios.a1` — identical; P-C15's asserted
  monomiality was only ever for the `a₀/a₂` Casoratian ratio.

**Scope-(a) statement:** the *raw pointwise* slot identification — `a₁-slot :=
−a₁/a₂` evaluated at a fixed `x` — cannot supply the required bar-ODD kernel
coefficient. NOT excluded: (i) evaluation symmetrized over the bar-pair locus
`{x*, 1/x*}` (where bar-transport permutes the pair — exactly the K1b golden
pair); (ii) the I-B cyclotomic re-basing; (iii) Z3 factorizations where a
bar-odd carrier absorbs the non-monomial factor. The K1a identity + K1b
bar-pair locus transfer to any refined identification.

## 4-ter. Beans `7vfu` (T1) + `pxvo` (T3) — pre-statement (BEFORE any run)

**T1 — bar-pair symmetrized evaluation (`7vfu`).** On the golden locus pair
`{x*, 1/x*}`, `x* = (3+√5)/2`, define `D(q) = α₁(q,x*) − α₁(q,1/x*)` and
`S(q) = α₁(q,x*) + α₁(q,1/x*)`. Since the full bar involution
`(q,x) ↦ (1/q,1/x)` permutes the pair, the symmetrized objects are the
canonical candidates for clean parity. Decidable checks (exact, radicals):

- **T1-K1:** is `D(1/q) = −D(q)` (bar-ODD), exactly or up to Laurent-monomial
  twist? Note `D(1) = 0` automatically (both evaluations equal 2 at q=1) —
  consistent with odd.
- **T1-K2:** is `S(1/q) = +S(q)` (bar-EVEN), exactly or up to monomial twist?
- Outcome semantics: T1-K1 pass → a canonical bar-odd scalar built from the
  4₁ operator on its own c₃-shadow locus survives (feeds Z3/Z4); both fail →
  pair-symmetrization at the raw level killed, escalate to I-B.

**T3 — Z3 carrier preflight (`pxvo`).** Decidable q=1-order bookkeeping:

- **T3-1:** `κ_{(2,1)}` vanishes at q=1 to order exactly **3**; `z − 1/2`
  vanishes to order exactly **2** (z is critical at q=1). Consequently
  rational functions of `z` realize only **even** vanishing/pole orders at
  q=1, so `(rational-in-z) × κ_{(2,1)}` has odd total order and **cannot**
  equal the finite nonzero shadow `a₁(1) = 2` — killing the naive
  `f(z)·κ_{(2,1)}` sub-class of Z3 (scope-(a): as the *sole* source, at
  q=1-regular f).
- **T3-2 (tension flag, 🟡 owner):** any exactly-bar-odd function regular at
  q=1 vanishes there (`f(1) = −f(1)`); but `a₁ = −c₃ → 2 ≠ 0` at q=1. So
  "a₁ exactly bar-odd" (ck_a1_bar_odd_of_c3_odd's hypothesis, from #1887) and
  "a₁ q=1-regular with shadow 2" are **jointly impossible** — the corpus
  constraint set must mean odd-PART dominance of the anchor swing, or a₁
  singular at q=1. To be verified symbolically and flagged, not resolved.

### 4-ter outcomes (2026-07-06, runs after pre-statement commit `44b0b82c`)

- **T1 (`7vfu`) KILLED (scope-(a)).** Neither `D(q)` nor `S(q)` on the golden
  pair has clean bar-parity — the twist ratios remain non-monomial
  ([probe](../../computations/qbeta/qbeta_t1_barpair_symmetrization_probe.py) →
  [witness](../../computations/qbeta/qbeta-t1-barpair-symmetrization.witness.json),
  exit 1 = candidate-excluded). Reading: the middle coefficient's non-monomial
  bar-covariance is **intrinsic** — no evaluation choice (pointwise or
  pair-symmetrized) repairs it; the defect must be addressed in the function
  space (I-B) or absorbed by a carrier with matching covariance.
- **T3 (`pxvo`) 7/7 EXACT** ([probe](../../computations/qbeta/qbeta_t3_carrier_q1_order_preflight_probe.py) →
  [witness](../../computations/qbeta/qbeta-t3-carrier-q1-order-preflight.witness.json)):
  `κ_{(2,1)}` q=1-order exactly 3 (leading coeff 2); `z − 1/2` order exactly
  2 (leading `−1/16`; z critical at q=1) ⇒ z-functionals realize even orders
  only ⇒ **`f(z)·κ_{(2,1)}` excluded as the sole `a₁` source** (odd total
  order vs finite nonzero shadow). **T3-2 tension CONFIRMED, 🟡 owner:**
  "a₁ exactly bar-odd" + "a₁ q=1-regular with shadow 2" jointly impossible —
  ruling needed (odd-part/swing reading of #1887 vs q=1-singular a₁);
  affects every parity gate in the program.
- **T3-2 INVESTIGATED on the merits (2026-07-07; owner declined fiat ruling,
  asked to investigate).** Verdict in
  [`docs/audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md`](../audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md):
  **no corpus source establishes exact bar-oddness of kernel `a₁ = −c₃`** —
  #1887's Lean is component-level (`sinh` odd; bar-antisymmetric *part*);
  #1866 is rung/phase parity (`c₃ = 0` on the even slice); `ck_a1_bar_odd_of_c3_odd`
  is conditional; pointwise real η-parity of c₃ is ill-posed by the corpus's
  own #1821 smooth-real refutation. Plus a **symbol-overloading finding**:
  the heat-route `a₁ = κ_{(2,1)}·S` (exactly odd, vanishes at q=1, ~1e-3) and
  the kernel `a₁ = −c₃` (shadow 2, ≈2.07) are distinct objects (Stage B's
  2000× magnitude mismatch, ledger cont. 19). Evidence-based reading: **`a₁`
  has a nonzero bar-odd part (swing channel); its bar-even part carries the
  shadow** (`shadow_carried_by_even_part`, sorry-free, ZBarParity §5).
  Docstring of `ck_a1_bar_odd_of_c3_odd` clarified (conditional scope; no math change;
  file still compiles, lean-direct exit 0). The c4qz/T1 kills survive
  re-examination. 🟡 Owner sign-off requested on making this the standing
  reading (prose/gate re-scope only).
- **T2 (`ciei`) scoped, not started:**
  [`docs/scope/2026-07-06-z-ck-fmap-ib-rebasing-scope.md`](../scope/2026-07-06-z-ck-fmap-ib-rebasing-scope.md)
  — I-B is now the load-bearing route (B1 induced recurrence → B2 re-based
  parity → B3 shadow + basis composition); 4₁ is the cleanest test knot
  (`C_n ≡ 1`); reuses the n920 Habiro machinery landed on main.

## 4-quater. Prevention tranche (bean `f2pz`, owner "do 1 2 3 4 5", 2026-07-07)

So the a₁ incident class cannot recur:

1. **Kernel/f-map constraint registry** — [`ck-dk-canonical-registry.md` §9](ck-dk-canonical-registry.md)
   (14 rows KC1–KC14, per-row epistemic tier) + JSON twin
   [`kernel-constraints-registry.json`](kernel-constraints-registry.json) +
   validator [`kernel_constraints_registry_validate.py`](kernel_constraints_registry_validate.py)
   (R1–R5 incl. the machine rule **exactly-bar-odd ⇒ zero q=1 shadow**;
   0 errors, 9 standing warnings: R5 on three pre-existing decl names +
   the historical 2026-06-05 scope doc, warn-only by design).
2. **`_of_` naming rule** — `ck_a1_bar_odd` renamed
   `ck_a1_bar_odd_of_c3_odd` (compiles, exit 0; on-branch citations
   updated, historical docs untouched); rule codified in
   `local/formalizer.md` §Conditional-lemma naming. The three older
   conditional decls (KC2–KC4) kept their names — visible as standing R5
   warnings rather than a wider rename.
3. **Registry §2 disambiguation rows** for `a₁` (kernel vs heat-route),
   `a_n` (z-Taylor), `Φ₂`.
4. **Doc-citation lint** — `--lint-docs` mode of the validator (warn-only;
   `--strict` for CI).
5. **AGENTS.md STRICT rule** "Conditional-proved ≠ premise-established"
   (owner-visible file; wordsmith at will).

## 4-quinquies. Bean `ciei` step B1+B2 — pre-statement (BEFORE any run)

4₁'s cyclotomic (Habiro) expansion is `J_N = Σ_{k=0}^{N−1} ω_k(x)`,
`ω_k = ∏_{j=1}^k (x + x⁻¹ − q^j − q^{−j})`, `x = q^N` — coefficients
`C_k ≡ 1` (termwise equal to the certificate's Habiro–Le summand
`q^{Nk}(q^{−N−1};q^{−1})_k(q^{−N+1};q)_k`, per `aj_figure_eight_certificate.py`).
Checks (exact symbolic, no anchors, no c_k values):

- **B1-K1 (transcription gate):** the ω-sum must satisfy the verified
  inhomogeneous order-2 operator `a₂J_{N+2} + a₁J_{N+1} + a₀J_N = b`
  exactly for N = 1..8. Mismatch → transcription wrong, stop.
- **B1 structural readout:** with `C_k ≡ 1`, the induced coefficient
  recurrence in the cyclotomic basis is the trivial depth-1 constant
  `C_{k+1} = C_k` — the basis change absorbs the operator's complexity; the
  basis elements carry it via the clean first-order factor recurrence
  `ω_{k+1}/ω_k = (x + x⁻¹ − q^{k+1} − q^{−(k+1)})`.
- **B2-K2 (parity gate, the load-bearing check):** bar-parity of the factor
  `x + x⁻¹ − q^j − q^{−j}` and of `ω_k` under `(q,x) ↦ (1/q,1/x)` must be
  clean (exact or monomial twist). Non-monomial → cyclotomic re-basing
  ALSO fails to repair the parity defect ⇒ strong scope-(a) verdict against
  Z4-via-4₁ at every basis tested; fall back to Z3 carriers/other knots.
- **B3 partial (shadow orders):** record q=1/x=1 vanishing structure of
  `ω_k` (expected `((x−1)²/x)^k` at q=1 — even orders, echoing T3).

## 5. Session log

| date | event |
|---|---|
| 2026-07-06 | Tranche opened; beans `uz9i`/`3iwu`/`ea56`/`c4qz`/`iw8o`; this ledger landed as first commit. PR [#3449](https://github.com/litlfred/qou/pull/3449). |
| 2026-07-06 | Intent posted on overlapping siblings [#3429](https://github.com/litlfred/qou/pull/3429) (f-map power-class pincer — same axis; C15 row/probe-id collision flagged) and [#3447](https://github.com/litlfred/qou/pull/3447) (c₃-not-exact verdict — framing here confirmed consistent). Gemini reviewer at daily quota; Copilot reviewer check failed (bot-side) — docs-only PR, no code CI. |
| 2026-07-06 | **Bean `c4qz` DONE — I-A raw-slot identification KILLED on slot bar-parity (scope-(a)); `α₂ ≡ −1` identity + golden bar-pair locus `x* = φ^{±2}` survive** (§4-bis outcome). Next open moves: bar-pair-symmetrized evaluation, I-B re-basing, Z3 carrier factorization. |
| 2026-07-06 | **Bean `ea56` DONE — the z-alone exclusion (scope-(a)).** `z(q)=√q/(1+q)` proved **exactly bar-EVEN** (twist 1) and `κ_{(2,1)}` exactly bar-ODD, sorry-free Lean [`QOU/QBeta/ZBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean) (`lean`-direct exit 0) + sympy-exact 7/7 witness. Since the bar-fixed locus is a subring and `a₁ = −c₃` is bar-ODD nonzero, **no scalar rational function of z alone can source `a₁`** — class Z2 excluded; survivors are Z3 (bar-even z-functional × bar-odd carrier) and Z4 (operator-level / P-C15). Hypothesis-class lattice: [`docs/scope/2026-07-06-z-ck-fmap-hypothesis-class.md`](../scope/2026-07-06-z-ck-fmap-hypothesis-class.md). Bean `c4qz` unblocked. |
