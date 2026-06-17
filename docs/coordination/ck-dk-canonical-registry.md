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
  level), not a real-q formula (CLAUDE.md §"Im(q) at fibre vs observable level").
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
- **L2 100× dashboard: 3/7** beats-100× (`per-observable-100x-status.witness.json`,
  `summary.beats_100x_count = 3`). The deep audit's "4/7"/"6/7" are **stale**
  (pre proton-anchor re-pin).
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
- `CLAUDE.md` "c_3 SETTLED" note (the settle drifted again 2026-06-03/04)

---

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
