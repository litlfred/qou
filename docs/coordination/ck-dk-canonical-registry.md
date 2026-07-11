# c_k / d_k canonical registry — the ONE source of truth

**Status:** AUTHORITATIVE (2026-06-04). This registry **supersedes** every
prior scattered c_k / d_k status note (see [§7 Supersession](#7-supersession)).
When any paper block, compute script, audit doc, or chat reply states a
c_k / d_k status, it must agree with **this file** or update it.

> **Machine-readable twin.** [`ck-dk-registry.json`](ck-dk-registry.json) mirrors
> §3/§4/§6 for dashboards; [`ck_dk_registry_validate.py`](ck_dk_registry_validate.py)
> enforces the §8 flip-flop guard (a wired rung MUST be `canonical`). Keep the
> JSON in sync with this markdown when a tier changes.

> **Why this exists.** The author has asked 3–4 times to stop the c_k / d_k
> flip-flop (wired ↔ de-fit ↔ reverted, ≥4 times on c_3 alone) and to track
> **canonical vs empirical** in one place. The disagreement had two root
> causes — **symbol overloading** (§2) and **drifted status across ≥5 audit
> docs** (§7) — both resolved here.

---

## 1. The one distinction that resolves most of the confusion

**Machinery-proved ≠ values-derived.**

A Lean file can be **sorry-free** yet prove only a **conditional** ("if a
kernel/element exists, then …"). A sorry-free *recursion engine* does **not**
mean the c_k *values* are derived. Read every "c_k proved" claim through this
lens:

| Claim you may have seen | What is actually true |
|---|---|
| "the c_k recursion is proved (sorry-free Lean)" | The **machinery** is proved + the **conditional** "IF F(q) satisfies a depth-d q-difference equation with kernel R, THEN c_k satisfy a linear recursion" is proved. The **kernel R and the element F(q) are NOT constructed** — so it produces **no c_k values**. It is *scaffolding* (the block's own title + Status). See §5. |
| "the c_k are the Taylor/Habiro expansion" | Correct **framing**: c_k are the ladder coefficients of a fibre-level Habiro element F(q). But the **specific F(q) is the open keystone** — unconstructed. So this framing does not make any c_k≥3 *derived*. |
| "c_2/c_3/c_4… are canonical" | **Only c_2 = −1 is canonical** (Taylor-exact, proved, anchor-stable). c_3 is a falsified near-match; c_4 is a CODATA fit; c_5+ are open. See §3. |

**Canonical** in this registry = derived to compute precision (Taylor-exact)
**and** anchor-stable. Everything else is **empirical** (and labelled with its
tier: near-match / conjecture / fit / artifact / refuted / TBD).

---

## 2. Symbol disambiguation (c_k and d_k are overloaded)

`c_k` and `d_k` each denote several **distinct** objects. Only the first row
of each is the "precision-ladder" sense this registry governs; the others are
cross-referenced so they are never conflated again.

| symbol | meaning | governed here? | where |
|---|---|---|---|
| **c_k** | Q_β β-decay **precision-ladder** coefficients: `Q_β = Q_base·∏_k(1 + c_k·u^k)`, `u = b·ℏ_q²` | **YES** (§3) | [`q-beta-c-k-recursion-from-habiro-q-difference.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md), [`appendix-mass-binding-algorithms/`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/) |
| `c_k(n)` | exponents in the cyclotomic expansion `F_n(z) = ∏_k(1 − q^{−k}z)^{−c_k(n)}` | no — different object | [`braids-and-knots/`](../../content/quantum-observable-universe/braids-and-knots/) |
| `(c_k, d_k)` | eigenvalue-factor **pair** in `χ_sym(β) = ∏_k(c_k q + d_k)` | no — different object | per-block character blocks |
| **d_k** | m_p mass **brane-tower** coefficients (mass-side analog of the Q_β ladder) | **YES** (§4) | [`2026-05-30-qbeta-ck-mp-dk-deep-audit.md`](../audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md), mass compute |
| `d_k` | chain-complex **differential** (`d_{k+1}∘d_k = 0`, d²=0) | no — unrelated homological `d` | [`confined-knot-binding.md`](../../content/quantum-observable-universe/mass-theory/confined-knot-binding.md) |
| **a₁ (kernel)** | c_k-recursion kernel **leading coefficient** `a₁ = −c₃ = √2·Φ₂ ≈ 2.07`; q=1 shadow `2 ≠ 0`; parity: nonzero bar-ODD **part** (NOT exactly odd — see §9 KC6) | **YES** (§9) | `QBetaCKRecursionKernelConstraints.lean` |
| `a₁` (heat-route) | per-mode heat coefficient `κ_{(2,1)}(q)·S` — **exactly** bar-odd, vanishes at q=1, magnitude ~1e-3 (Stage B refuted the per-mode identification; 2000× magnitude mismatch) | no — **distinct object**; do NOT transfer its attributes to the kernel a₁ (the 2026-07-07 tension was exactly this transfer) | [2026-06-13 heat audit](../audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md); [2026-07-07 investigation](../audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md) |
| `a_n` (z-Taylor) | ℏ-Taylor coefficients of `Δtr_M` / the `z(q)` 3-term recursion sequence (PR #2465 / #1739) | no — upstream z-side data, related by the **open f-map** | `qbeta-z-recursion-to-ck-recursion-bridge.md` |
| **Φ₂** | the #1887 phase's second coefficient, `Φ₂ = −c₃/√2` — same object as the kernel a₁ up to `√2` (conditional lemma `ck_a1_eq_sqrt2_phi2`) | **YES** (via a₁; §9) | PR #1887 / #1900 |

---

## 3. Q_β `c_k` precision ladder — per-rung registry

`Q_β = Q_base · ∏_k (1 + c_k·u^k)`, `u = b·ℏ_q² ≈ 0.00852`, at proton-pinned q₀.

| rung | status | form / value | residual @ proton q₀ | anchor-stable? | authoritative producer |
|---|---|---|---|---|---|
| **c_2** | **CANONICAL** (proved, Taylor-exact) | `−1` (Kashiwara f̃₁², bar-even) | exact | yes | `q-beta-c-2-eq-neg-one-structural.lean` (PR #1602) |
| **c_3** | **EMPIRICAL — near-match, REFUTED as real-q fibre element** | candidates `J−ℏ²`, `[3]_q/25` 3-rung | ~2.6–3% (J−ℏ²); 2.65 ppm (`[3]_q/25` at proton **only**) | **NO** — swings −2.88% to muon; `dc_3/dq ≈ 4.6×10⁶` | falsification: [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](../audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md) |
| **c_4** | **EMPIRICAL — CODATA fit / artifact** | `−0.97157` (CODATA residual); conjecture `c_3·b⁴` | fit (0 by construction) | n/a | `qbeta_1ppq_achieved.py` (flagged normalisation artifact, commit `c108fa38`) |
| **c_5** | **EMPIRICAL — outlier** | `−(b² + ½)` (averaging-resonance ½ fingerprint) | proton-anchor only | NO | `qbeta_decay_sdp_extended_ck.py` (Pell-Lucas NON-clean — structural outlier per the §averaging-resonance-rule) |
| **c_6, c_7** | **EMPIRICAL — APPLIED in extraction (self-consistent)** | `c_3²·b² = 4·b²`, `c_3³ = −8` (Pell-Lucas-clean) | bias-corrected q₀ recovers them: **0.005% / 0.26%** | **cross-anchor tested 2026-06-04: recovered by #1824 bias-correction — but these forms are IMPOSED in the extraction, so this is self-consistency, not independent validation** | applied in `qbeta_decay_sdp_extended_ck.py`; probe `qbeta_c6_c10_crossanchor_falsification.py` (PR #1842) |
| **c_8, c_9, c_10** | **EMPIRICAL — silver-anchored, PROVED at q = 1+√2; pattern BREAKS at c_8** | `4·b⁴ = 49/16`, `−8·b² = −7`, `4·b⁶ = 343/128` (Pell-Lucas-clean σ-action) | c_8 first FREE rung: closed +2.27 vs **bias-corrected −0.215 (wrong sign)**; c_9 −297, c_10 1.05×10⁸ | **cross-anchor tested 2026-06-04 (#1842, vs #1824 bias-corrected): anchor-stable (swing 2.4×10⁻⁷%) but the Pell-Lucas pattern does NOT survive into the free rungs → stays empirical** | sibling triple `qbeta-c8-c10-silver-rationals.{ts,md,lean}` (PR #1793), Lake mirror `QBetaCnAtSilver.lean`; probe `qbeta_c6_c10_crossanchor_falsification.py` |
| **kernel R(q,ξ)** / **element F(q)** | **OPEN keystone** | structurally constrained, not pinned | — | — | `habiro_ladder_bridge.py` |

**Key facts:**
- Only **c_2** is canonical. c_3's best forms reproduce the empirical value at
  the **proton anchor only** and are **rigid** (swing 4.7M× less than empirical
  c_3) → **falsified** as universal real-q fibre elements. A genuine c_3 Habiro
  element, if it exists, must be **complex-analytic / root-of-unity** (fibre
  level), not a real-q formula (AGENTS.md §"Im(q) at fibre vs observable level").
- **c_8 / c_9 / c_10** are PROVED rational identities at the silver ratio
  (`norm_num`-trivial in `qbeta-c8-c10-silver-rationals.lean`), but per §8 a
  silver-anchored exact rational is **not canonical** without a passing
  proton+muon cross-anchor swing test. Such a test is **not yet run**; the
  upstream SDP-extraction docstring already records q₀ leverage as
  noise-dominated for k ≥ 8 (ratios 10³–10⁷×). The closed forms are the
  STRUCTURAL signal at the silver ratio, not a q₀ precision claim.
- **(2026-06-17) The silver anchor is now Lean-grounded**
  (`QOU.QBeta.SilverAnchorGrounding`, sorry-free, PR #2445): `b² = 7/8` is
  *derived* from the silver relation `q² − 2q − 1 = 0` (it was a **premise** in
  `Cn_at_silver`), via `8(q⁴+q²+1) = 7(q²+1)²` with cofactor `(q²+2q−1)`; and the
  same locus is proved to be the **`Q_A` decay-prefactor zero** (`2q+1−q² =
  −(q²−2q−1)`).
- **(2026-06-17, correction — PR #2445 dominance claim) the silver/`Q_A` pole
  is GENUINE but SUBDOMINANT.** PR #2445 originally called it "the F-pole fixing
  the *dominant* `1/u_substrate ≈ 117.4` root." Re-checked: the *true*
  `Q_β = |Δ(net)|·E₀` uses the GB-reduced trefoil coefficient, and
  `Δ(net)(1+√2) = 82216 + 58136√2 ≠ 0` while `Q_A(1+√2) = 0`, so `F` has a
  **genuine** pole at silver (an earlier check that used the cheat-sheet
  closed-form `Q_β ≈ Q_A` was *circular* — it gave `F = 1/cos`, trivially
  regular). **But** `u_silver = u(1+√2) ≈ 0.321 → char root ≈ 3.12`, which is
  **subdominant**: the dominant tail root `117.4 = 1/u_substrate`
  (`u_substrate ≈ 0.0085 < u_silver`; `prop:q-beta-radius-of-convergence-gate`,
  PR #1727) comes from a **non-`Q_A`** source. So the silver/`Q_A` zero pins one
  *subdominant* root of the kernel's minimal denominator and prunes the dominant
  root search (it is not the `Q_A` zero). Evidence:
  `computations/qbeta/qbeta-silver-pole-subdominant.witness.json`. This grounds
  the "categorical derivation of `Q_A·cos α_eff`'s zero" direction
  (`RationalCoeffRecurrence`); it does **not** change any rung's empirical tier.
- c_4 in the 1ppQ-achieved witness is a **CODATA-residual fit**, and separately
  flagged as a **normalisation artifact**.
- The `[3]_q/25` building block is **shared** with the m_μ V9 closure (a real,
  clean proton-anchor structural coincidence) but is **NOT** a universal real-q
  element (same falsification).
- **`c_3 = −Vol(4₁) + u − (10/3)u²`** ([`2026-07-08-qbeta-keystone-derivation.md`](../audits/2026-07-08-qbeta-keystone-derivation.md),
  landed with an over-scoped "PROVEN/exact" tier) is a **muon-anchor near-match**,
  **re-scoped 2026-07-11**: it is anchor-blind (≈ −2.0216 at both anchors) while
  c_3 swings 2.43%, so it matches muon (0.07%) but misses proton (2.3%) and fails
  the §8 guard. The `−Vol(4₁)` piece is the solved bar-even part and `10/3 =
  lim[10]_q/[3]_q` is an exact writhe-ratio identity — both real; only the tier is
  corrected. c_3's status stays **EMPIRICAL/REFUTED as real-q** (this row). See
  [`2026-07-11-qbeta-c3-keystone-rescope-anchor-blind.md`](../audits/2026-07-11-qbeta-c3-keystone-rescope-anchor-blind.md).

---

## 4. m_p `d_k` brane-tower — per-rung registry

Mass-side analog. All rungs **de-fit** in #1416; **none currently wired**
(honest production = bare, see §6).

| rung | status | form / value | residual | wired? |
|---|---|---|---|---|
| **d_4** | **EMPIRICAL — near-match** | `J²·n_crossings + n_gluon = 4·11+2 = 46` | ~0.05% | NO |
| **d_5** | **EMPIRICAL — near-match** | `J² = 4` (Jones squared) | — | NO |
| **d_6** | **TBD** (no derived form) | `−29` (closest-integer extraction) | — | NO |

The d_k are categorically *suggestive* (crossing counts, Jones²) but each is an
empirical integer extraction, not a derivation. The current categorical
`VolDensity(𝓑₃)` leaves the documented **~2.89% m_p gap** with no d_k wired.

---

## 5. The c_k recursion — what is actually proved

Block: [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
(kind `proposition`, title **"Proposition (scaffolding)"**, Lean **sorry-free**).

**Proved (sorry-free):**
- The recursion **engine** — Lean `CKRecursion R` structure + `applyRecursion`.
- The **conditional**: *IF* `F(qξ) = R(q,ξ)·F(ξ)` (depth-d q-difference eq), *THEN*
  `c_{k+1} = Σ_{j=1}^d a_j(q₀)·c_{k+1−j}` with `a_j` read off R via the Habiro
  `(u;u)_m → u^k` change of basis.

**NOT proved / open:**
- The **kernel** `R(q,ξ)` — structurally constrained (bar-even, ζ₄ residue,
  √u→u² lift), not pinned.
- The **Habiro element** `F(q)` — "the open keystone" (needs symbolic α(q)).
- A **constant-kernel** recursion was explicitly **REFUTED through depth 4**
  (commit `eca145ca`, 2026-06-04) — so the kernel, if any, is non-constant
  q-rational.

**Therefore:** the recursion does **not** currently produce c_3, c_4, …. It
would collapse c_3…c_8 to `seed (c_2=−1) + kernel` **once F(q) is constructed**
— that construction is the open keystone, not a completed proof. (The separate
sorry-free `MarkovParameterRecursion.lean` — 2 sorries remain — is a different,
per-block-χ recursion; do not conflate it with the c_k ladder recursion.)

---

## 6. Production wiring — the ONE authoritative statement (verified 2026-06-04)

- **Q_β: c_2 only** (`Q_N2`-level). `q_beta_predicted.py` wires **no** c_3+
  ladder rung; the ~0.17% truncation residual is the c_2-level gap.
- **m_p: bare.** No d_k wired; ~2.89% categorical `VolDensity` gap stands.
- **L2 100× dashboard: 2/7** beats-100× (`per-observable-100x-status.witness.json`,
  `summary.beats_100x_count = 2`; m_e and m_K/m_π). The "3/7" recorded here
  earlier — and the deep audit's "4/7"/"6/7" — are **stale**: m_p dropped from
  the count on 2026-07-04 when its fitted Habiro tower was removed (de-fitted
  round-trip +1.35 ppb, ~437× miss; see AGENTS.md §Precision goals and
  `docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`).
- The c_3 structural form is locked behind the §3b-cond conditional class
  `QbetaC3StructuralFormClass` — **conditional, not a derivation**, not wired.

**Nothing in this registry changes production.** It is a consolidation of
*status*, not a re-wire (re-wiring is the flip-flop trap).

---

## 7. Supersession

The following are **historical record only** for c_k / d_k status; this
registry is authoritative. Each should carry a one-line banner → this file.

- [`2026-05-30-qbeta-ck-mp-dk-deep-audit.md`](../audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md) (body + addendum)
- [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- [`2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`](../audits/2026-06-03-l2-closure-habiro-3-q-25-universal-template.md)
- [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](../audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)
- the flip-flop history table in [`1ppq-qbeta.md`](1ppq-qbeta.md)
- `AGENTS.md` "c_3 SETTLED" note (the settle drifted again 2026-06-03/04)

---


> **Standing reading (owner-granted 2026-07-07).** For every kernel/f-map constraint: **parity gates test the bar-ODD part** of a coefficient; **shadow gates test the bar-EVEN part** (`shadow_carried_by_even_part`). "a₁ exactly bar-odd" is the never-proved antecedent of the *conditional* KC6 lemma — do not restate it as fact. Ref: [investigation audit](../audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md) §4.

## 8. Flip-flop guard (standing rule)

1. **Do not re-wire** any c_k≥3 or d_k≥4 to production without (a) explicit
   owner approval AND (b) a **passing cross-anchor test** (proton + muon swing
   < 1%). c_3's best forms FAIL this test today.
2. **Canonical requires anchor-stability.** A proton-anchor near-match is
   `empirical`, never `canonical`, no matter how small the proton residual.
3. **Sorry-free ≠ derived.** A conditional/scaffolding Lean proposition does
   not promote a coefficient's tier.
4. **Update this registry** (not a new audit doc) when a rung's status changes —
   that is what keeps "one approach" true.

---

## 9. Kernel / f-map structural-constraint registry (added 2026-07-07)

One authoritative table of every structural constraint on the open kernel
`R(q,ξ)` / element `F(q)` / kernel coefficients `a_j`, with a per-row
**epistemic tier** — added after the a₁ parity-shadow incident
([investigation audit](../audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md)),
in which a *conditional* lemma's hypothesis was propagated as established
fact by prose shorthand. Same discipline as §3/§4: when any doc states a
kernel constraint, it must agree with this table or update it.

> **Machine-readable twin + validator.**
> [`kernel-constraints-registry.json`](kernel-constraints-registry.json) mirrors
> this table; [`kernel_constraints_registry_validate.py`](kernel_constraints_registry_validate.py)
> enforces: (R2) every `conditional` row names its hypothesis; (R3)
> **`parity: exactly-odd` ⇒ `q1_shadow: 0`** (the fixed-point rule
> `QOU.QBeta.fixed_eval_two_mul_kills_bar_odd` — the machine form of the
> incident); (R4) every `proved-lean` row names its decl; (R5, warn)
> conditional lemmas should carry `_of_` names. Doc-lint mode
> (`--lint-docs`, warn-only; `--strict` fails) flags citations of
> conditional decls not marked "conditional" nearby.

Tiers: `proved-lean` (unconditional Lean) · `symbolic-exact` (sympy-exact
witness) · `conditional` (Lean implication; hypothesis named, NOT established)
· `empirical` (data-derived) · `gate` (adopted screening requirement).

| id | constraint | tier | parity / q=1 shadow | source |
|---|---|---|---|---|
| KC1 | kernel depth ≥ 2 | proved-lean (`ck_recursion_depth_one_refuted`) | — | PR #1900 |
| KC2 | depth-2 slot `a₂ = c₂ = −1` | conditional (hyp: depth-2 recursion at n=2, seeds `f₀=1, f₁=0`; `ck_a2_eq_c2_depth_two`) | even / `−1` | PR #1900 |
| KC3 | depth-2 slot `a₁ = −c₃` | conditional (hyp: depth-2 recursion at n=3; `ck_a1_eq_neg_c3_depth_two`) | see KC6 / `2` | PR #1900 |
| KC4 | `a₁ = √2·Φ₂` | conditional (hyp: phase relation + `Φ₁=√2`; `ck_a1_eq_sqrt2_phi2`) | see KC6 | PR #1887/#1900 |
| KC5 | constant kernels refuted (depth-2 over-determines `c₄ = 1−c₃²`, 3.4× miss; constants refuted through depth 4) | empirical | — | PR #1900; commit `eca145ca` |
| KC6 | `a₁` parity: **nonzero bar-ODD part** (anchor-swing channel); bar-even part carries the `→2` shadow. NOT exactly odd — exactly-odd ⇒ zero q=1 shadow (`fixed_eval_two_mul_kills_bar_odd`) | conditional (hyp: c₃ exactly η-odd — modelling hypothesis, NOT established; `ck_a1_bar_odd_of_c3_odd`) + proved-lean fixed-point rule | odd-part-nonzero / `2` | [2026-07-07 investigation](../audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md) |
| KC7 | overall `F` bar-even | gate §4(b) | even / — | PR #1875 (`prop:q-beta-bar-even-kernel-invariant`) |
| KC8 | simple pole of `g(u)` at `u_substrate` (radius/ratio test) | gate §4(a), empirical basis | — | PR #1727; `prop:q-beta-radius-of-convergence-gate` |
| KC9 | ζ₄ residue; period-3 (ζ₃/ζ₆) resonance | empirical | — | 2026-06-01 audits |
| KC10 | q=1 shadows: `c₂ → −1`, `c₃ → −2`; per KC6 the shadow gate tests the **bar-even part** (`shadow_carried_by_even_part`) | gate §4(c) | — / even-part | 2026-06-05 gates; ZBarParity §5 |
| KC11 | 4₁ operator slot ratios are **exactly bar-invariant** (twist 1, incl. `α₁` — corrected 2026-07-07; the earlier "non-monomial" row was a transcription-error artifact): raw pointwise slots are bar-EVEN with zero odd part and cannot source the bar-odd channel | symbolic-exact | even / — | PR #3449 ([correction audit](../audits/2026-07-07-pc15-a1-transcription-error-correction.md)) |
| KC15 | pair-difference `D(q) = α₁(q,φ²) − α₁(q,φ⁻²)` on the golden bar-pair is **exactly bar-ODD**, `D(1) = 0` — canonical odd-channel candidate from the 4₁ operator; Habiro basis `ω_k` exactly bar-even (`cycFactor_bar_invariant`), `C_k ≡ 1` | symbolic-exact + proved-lean (`QOU.QBeta.cycFactor_bar_invariant`) | odd / `0` | PR #3449 (T1 + B1 witnesses) |
| KC16 | one-sided Habiro basis `(q;q)_k` has **index-alternating bar-parity**: `bar((q;q)_k) = (−1)^k q^{−k(k+1)/2} (q;q)_k` — parity re-mix supplied by the **basis**; x=1 shadow of the 4₁ cyclotomic basis = Kashaev double; u-side transfer open | proved-lean (`pochNum_bar_twist`, induction, generic `CommRing`) | mixed / — | PR #3449 (B3 witness) |
| KC17 | **u-side transfer OBSTRUCTION**: `bar(u) = q²·u` (scaling, not KC16 inversion) ⇒ `(u;u)_m` has no clean monomial twist, the per-rung twist `q^(−2k)` is contradicted by `c_2 = −1`, and `u ~ (q−1)²` is even-order vs bar-odd odd-order. Naive re-expansion in `u` does NOT carry fibre parity (KC15/KC16) to the `c_k`; odd channel enters via the archimedean Markov-pairing evaluation | symbolic-exact + proved-lean (`uPow_bar_twist`) | — | PR (B3-U); [obstruction audit](../audits/2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md) |
| KC18 | **archimedean evaluation map bar-decomposition**: the counit `ε`/Markov trace `tr_M` on the nucleon NF diff splits EXACTLY into a bar-even identity term `h²/2` (shadow) + a bar-odd crossing/loop term (`−h` / `−h·z`; the odd channel), since `h=q−q⁻¹` is bar-odd and `z` bar-even (KC13). Realizes the standing reading on the actual map; `D(q)` (KC15) feeds the observable via the Markov crossing term | proved-lean (`epsNP_decomp`, `trMNP_bar_image`) | mixed / — | PR (eval-map); [decomposition audit](../audits/2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md) |
| KC19 | evaluation map `E(w) = h²/2 − h·w` is **affine** in the crossing weight (`∂E/∂w = −h`) ⇒ ladder factor `L(w) = E(w)/E(w₀)` Möbius; bar-**odd** part `= 2h(w−w₀)/(4w₀²−h²)` (**linear** in the departure `(w−w₀)` × the **fixed anchor-free** bar-odd kernel `K(q) = 2h/(4w₀²−h²)`); bar-even part `(4ww₀−h²)/(4w₀²−h²)`. Keystone ⇒ single scalar `(w−w₀)`; `K(q)` anchor-rigid ⇒ c₃ swing lives in `w(q)`. Sharpens KC18 | proved-lean (`CrossingWeightAffine.evalMap_affine` / `ladder_odd_part` / `ladder_even_part`) | mixed / — | PR #3473 ([affine narrowing audit](../audits/2026-07-07-qbeta-crossing-weight-affine-narrowing.md)) |
| KC12 | 4₁ Casoratian ratio `a₀/a₂` bar-invariant (twist 1) | proved-lean (`casoratian_ratio_bar_invariant`) | even / `1` | P-C15 |
| KC13 | `z` exactly bar-even; `κ_{(2,1)}` exactly bar-odd; no scalar z-functional sources the odd channel | proved-lean (`z_bar_invariant`, `kappa21_bar_odd`, ZBarParity) | even resp. odd / `1/2` resp. `0` | PR #3449 |
| KC14 | `f(z)·κ_{(2,1)}` order-blocked at q=1 (odd total order vs finite nonzero shadow) | symbolic-exact | — | PR #3449 (T3 witness) |
| KC20 | bar-ODD carrier is **not a root-of-unity object**: `num = (q²−1)·R₁₂` (cyclotomic content exactly `q²−1`; `Φ₄=q²+1 ∤ num`, remainder `−64`), and `R₁₂ = q⁶·C(q²+q⁻²)` with `C(y)=y³−4y²+3y−2` **irreducible** (no rational root among RRT candidates). Degree-3 field ⇒ no quadratic anchor (golden `y=3`, silver `y=6`, q=1 `y=2`) is a root ⇒ real-q/quadratic `c_3` closures structurally excluded. **proved-lean**: the factorisation, `Φ₄ ∤ num`, the trace-cubic reduction, `C = C_Hopf + C_unknot`, and no-rational-root of `C`/`C_Hopf`. **symbolic-exact** (witness, not Lean): the sector attribution (the cubic is the **Hopf (2-crossing)** sector `C_Hopf=y³−6y²+10y−6`; unknot adds `C_unknot=2y²−7y+4`; virtual+trefoil vanish) and the discriminants (`C: −152=−2³·19`, `C_Hopf: −76=−2²·19`) | proved-lean (`numOdd_factor`, `numOdd_at_phi4_root`, `R12_eq_cubic_trace`, `cubicC_sector_decomp`, `cubicC_rrt_candidates_all_nonzero`, `cubicC_Hopf_rrt_candidates_all_nonzero`) + symbolic-exact (sector attribution + discriminants) | — / — | PR #3467 ([audit](../audits/2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md); refines [2026-07-04 ζ₄ refutation](../audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md); complements KC19 affine ladder, PR #3473) |
