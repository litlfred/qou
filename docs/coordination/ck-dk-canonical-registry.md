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
| **`c̃_k`** | **normalised-series** coefficients of the *same* ladder model: the `u^k` Taylor coefficients of `Φ(u)/Φ(0)`, i.e. of `cos(α−u/2)·∏(1+c_j u^j)` divided by its own value at `u = 0`. Distinct from `c_k` because the cosine factor contributes at every order. `c̃₂ = c₂ − 1/8` **exactly and independently of `α`** (Lean, sorry-free: `QOU.QBeta.normalisedQuadCoeff_eq`) ⇒ at the committed `c₂ = −1`, `c̃₂ = −9/8`. **Both numbers are right**; they are one model read at two normalisations, not a discrepancy — see §9i | **YES** (§9i) | [`LadderCoeffNormalisation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderCoeffNormalisation.lean); `qbeta_alpha_eff_ladder_reconciliation_probe.py` (which measured `−9/8`) |
| **`c₂^even`** | the **bar-even part** of the ladder's quadratic data, exact in `ℚ(√3)`, ≈ `−8.00641` | no — a third object; do **not** read it as either `c₂` or `c̃₂` | `qbeta_c3even_exact_sseries_probe.py`, bean `8we6` |
| `c_k(n)` | exponents in the cyclotomic expansion `F_n(z) = ∏_k(1 − q^{−k}z)^{−c_k(n)}` | no — different object | [`braids-and-knots/`](../../content/quantum-observable-universe/braids-and-knots/) |
| `(c_k, d_k)` | eigenvalue-factor **pair** in `χ_sym(β) = ∏_k(c_k q + d_k)` | no — different object | per-block character blocks |
| **`cl_k`** (was `c_k`) | **cluster / Ursell** coefficients of the many-body expansion, MeV-valued. `cl_3 = −E₀·Δ²g` is the μ₃-door three-body coefficient (`μ₃ > 0 ⟺ Δ²g < 0`); the Borromean H₉ magnitude lift is the same family. **Renamed off `c_k` 2026-08-07** — it sat within ~12 % of the ladder `c_3 = −2` with no signal they were unrelated objects | no — different object | [`2026-08-07-mu3-door-status-consolidated.md`](../audits/2026-08-07-mu3-door-status-consolidated.md), `computations/deltalambda/` |
| **d_k** | m_p mass **brane-tower** coefficients (mass-side analog of the Q_β ladder) | **YES** (§4) | [`2026-05-30-qbeta-ck-mp-dk-deep-audit.md`](../audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md), mass compute |
| `d_k` | chain-complex **differential** (`d_{k+1}∘d_k = 0`, d²=0) | no — unrelated homological `d` | [`confined-knot-binding.md`](../../content/quantum-observable-universe/mass-theory/confined-knot-binding.md) |
| **a₁ (kernel)** | c_k-recursion kernel **leading coefficient** `a₁ = −c₃ = √2·Φ₂ ≈ 2.07`; q=1 shadow `2 ≠ 0`; parity: nonzero bar-ODD **part** (NOT exactly odd — see §9 KC6) | **YES** (§9) | `QBetaCKRecursionKernelConstraints.lean` |
| `a₁` (heat-route) | per-mode heat coefficient `κ_{(2,1)}(q)·S` — **exactly** bar-odd, vanishes at q=1, magnitude ~1e-3 (Stage B refuted the per-mode identification; 2000× magnitude mismatch) | no — **distinct object**; do NOT transfer its attributes to the kernel a₁ (the 2026-07-07 tension was exactly this transfer) | [2026-06-13 heat audit](../audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md); [2026-07-07 investigation](../audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md) |
| `a_n` (z-Taylor) | ℏ-Taylor coefficients of `Δtr_M` / the `z(q)` 3-term recursion sequence (PR #2465 / #1739) | no — upstream z-side data, related by the **open f-map** | `qbeta-z-recursion-to-ck-recursion-bridge.md` |
| **Φ₂** | the #1887 phase's second coefficient, `Φ₂ = −c₃/√2` — same object as the kernel a₁ up to `√2` (conditional lemma `ck_a1_eq_sqrt2_phi2`) | **YES** (via a₁; §9) | PR #1887 / #1900 |

---

## 3. Q_β `c_k` precision ladder — per-rung registry

`Q_β = Q_base · ∏_k (1 + c_k·u^k)`, `u = b·ℏ_q² ≈ 0.00852`, at proton-pinned q₀.

> **Frame declaration (added 2026-08-16, bean `qou-cwin` T2).** Every rung in
> the table below is in the **`u` frame** (`u = b·ℏ_q²`) and is the **factor**
> coefficient `c_k`, not the normalised-series `c̃_k` of §2/§9i. A `c_k` number
> is meaningless without both labels, and the two axes are independent:
>
> | axis | this table | the other value you may meet |
> |---|---|---|
> | expansion variable | `u = b·ℏ_q²` | `h = q − 1/q` — and `u^k = (b/(q+1)²)^k·h^{2k}` **exactly**, so a `u`-rung of order `k` is an `h`-rung of order `2k` and odd `h`-orders are unreachable from any `u`-ladder ([`LadderFrameChange.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderFrameChange.lean), sorry-free) |
> | normalisation | explicit factor `(1 + c_k u^k)` | normalised series `Φ(u)/Φ(0)`, whose `c̃₂ = c₂ − 1/8` (§9i) |
>
> **A single declaration rather than a per-row column** because all rows are
> currently in the same frame at the same normalisation — a column repeating
> `u`/factor seven times carries no information. The discipline this replaces
> it with: **any row added in a different frame or normalisation must say so in
> its own cell.** The producer declares the frame mechanically at
> `qbeta_utils.LADDER_FRAME` (PR #5235), and no rung below has moved.

| rung | status | form / value | residual @ proton q₀ | anchor-stable? | authoritative producer |
|---|---|---|---|---|---|
| **c_2** | **CANONICAL** (proved, Taylor-exact) — **for the C-frame ladder object; frame named 2026-08-15, see §9g** (the implied empirical c₂ under convention D is ≈ −9.30 and the rung convergence is C-frame-only; no tier change — the proof stands, its object now carries its convention) | `−1` (Kashiwara f̃₁², bar-even) | exact | yes | `q-beta-c-2-eq-neg-one-structural.lean` (PR #1602) |
| **c_3** | **EMPIRICAL — near-match, REFUTED as real-q fibre element** | candidates `J−ℏ²`, `[3]_q/25` 3-rung; **q→1 shadow = G(0,1) = −2** (longitude norm form on 4₁ cusp, *exact*) | ~2.6–3% (J−ℏ²); 2.65 ppm (`[3]_q/25` at proton **only**); **−[2]_q = −(q+q⁻¹) at q₀: 0.54% off** | **NO** — swings −2.88% to muon; `dc_3/dq ≈ 4.6×10⁶` | falsification: [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](../audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md); **longitude provenance (2026-07-30):** cusp winding (m,ℓ)=(0,1) gives G=(2·0+1)²−3·1²=−2 at angle φ=π/3 (cusp shape); B1 re-run with canonical GGM V₃=−7.693: **0 assembly hits in 180 candidates** (old near-misses were artifacts of wrong V₃); **convention provenance (2026-08-15, §9g):** the extractor consumes the convention-C Markov parameter via `α=(z−1)h/2` (`qbeta_utils.py:124-125`) and the Q_β channel is **unregistered** in `trace-convention-registry.json` — every ≈−2 value-level fact on this row ((H1), `[3]_q/25`, `J−ℏ²`, `S_leak`, `q*_S`) is **C-conditional** (re-extraction under D shifts c₃ to ≈ −974); the REFUTED-as-real-q verdict itself is **convention-immune** (swing D/C = 1.0052, measured) — [validity audit](../audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md) |
| **c_4** | **EMPIRICAL — CODATA fit / artifact (mechanically confirmed 2026-07-11)** | `−0.97157` (CODATA residual); conjecture `c_3·b⁴` | fit (0 by construction) | n/a | `qbeta_1ppq_achieved.py` (flagged normalisation artifact, commit `c108fa38`); P4 entropy audit `computations/probes/qbeta-ck-basis-constrained-pslq.witness.json` (PR #3536) |
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
  flagged as a **normalisation artifact**. **Mechanically confirmed 2026-07-11
  (P4 entropy audit, PR #3536):** when c_3 is extracted exactly against the
  same Q reference, c_4 reproduces as *identically 0* — the quoted `−0.972` is
  purely the truncation residual of a *rounded* c_3, carrying zero independent
  empirical content. More broadly, the extraction chain
  `c_k = (Q_CODATA/Q_ladder − 1)/u^k` amplifies σ(Q_β) by `1/u^k`, leaving
  empirical c_3 with ≤ ~2.2 reliable digits per anchor and **zero** digits at
  k ≥ 4 — any "empirical c_k≥4" quoted from this chain is noise
  (`qbeta-ck-basis-constrained-pslq.witness.json`; corroborated by the P5
  q-holonomic probe's Y2 caveat). Kernel/recursion tests at k ≥ 4 need
  canonical rungs (the H₄ Hoefsmit c₄^even build, bean `8we6`), never
  extracted ones.
- The `[3]_q/25` building block is **shared** with the m_μ V9 closure (a real,
  clean proton-anchor structural coincidence) but is **NOT** a universal real-q
  element (same falsification).
- **(2026-07-12/13) The c₃ "wall" is RESOLVED as a representation artifact; the
  open odd channel is the exact D-ladder, now proved non-holonomic.** The
  [capstone](../audits/2026-07-12-c3-wall-resolution-capstone.md) (#3600/#3636/#3654):
  the `dc₃/dq ≈ 4.66×10⁶` hypersensitivity is the `1/u³` ladder inversion
  magnifying a **smooth** numerator zero (`S′(q*_S) = 2.37 × (1/u³)`) — there is
  no singular substrate→u map; do not re-open the "singular wall" search. The
  bar-odd part factors `S = h·D(ũ)` (KC21); its sign-flip is structural
  (bar-odd parity, Lean-proved), and the `S = 0` point `q*_S` ≈ 1.10998 (**not**
  KC22's `q*_ρ` ≈ 1.48989 — §9a) is **NOT** an independent third determination
  of q₀ (**§9f** — it is conditional on (H1), since `q*_S` is *defined* as the
  root of `c₃ + Vol(4₁)`; the μ–p–Q_β "three-way" reading is withdrawn). The bar-even ℚ(√3)
  ladder `D(ũ)` is exact through `d₂₁`, **convergent** (radius `ρ = ũ(q*_ρ)`,
  CORRECTED 2026-08-09), and **refuted as low-order (q-)holonomic in every
  tested class** (KC22) — so a genuine c₃ closure, if any, lies outside the
  low-order (q-)holonomic and q-difference classes that were tested. It is
  **not** thereby resurgent: the "transcendental/resurgent (Écalle class)"
  inference this bullet used to draw is **WITHDRAWN 2026-08-09** — it rested
  on a divergence the ladder does not have (`κ = 0`). What KC22 supplies
  instead is the closed form `D(w) = φ(w)log(1−w/ρ) + ψ(w)` with algebraic
  `φ`, `ψ` over a degree-12 field — itself an example of an element that is
  convergent yet not low-order P-finite. **No tier change**: c₃ stays
  EMPIRICAL/REFUTED-as-real-q; these rows narrow the search class, they do
  not produce a value.
- **`c_3 = −Vol(4₁) + u − (10/3)u²`** ([`2026-07-08-qbeta-keystone-derivation.md`](../audits/2026-07-08-qbeta-keystone-derivation.md),
  landed with an over-scoped "PROVEN/exact" tier) is a **muon-anchor near-match**,
  **re-scoped 2026-07-11**: it is anchor-blind (≈ −2.0216 at both anchors) while
  c_3 swings 2.43%, so it matches muon (0.07%) but misses proton (2.3%) and fails
  the §8 guard. `10/3 = lim_{q→1}[10]_q/[3]_q` is an exact writhe-ratio identity
  — real, and unaffected. The `−Vol(4₁)` piece was called "the solved bar-even
  part"; **re-scoped 2026-08-14 to *motivated, not solved*** — the bar-split is
  not determinable from anchor data at all, and its geometric backing is
  muon-only (**§9c**, the `qou-qb8f` pointer; **§9b**).
  c_3's status stays **EMPIRICAL/REFUTED as real-q** (this row). See
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
> conditional lemmas should carry `_of_` names; (R6) **twin-drift** — the
> JSON twin must not restate text this table has withdrawn (struck spans
> must not be asserted by a JSON `statement`, and an MD **WITHDRAWN** marker
> must reach the JSON; added 2026-08-15, bean `qou-ungx`, after KC22's JSON
> carried a withdrawn divergence claim for six days). Doc-lint mode
> (`--lint-docs`, warn-only; `--strict` fails) flags citations of
> conditional decls not marked "conditional" nearby.
>
> **Withdrawal idiom (standardised 2026-08-15).** When a row's claim is
> withdrawn, ~~strike the withdrawn text~~ **and** add a dated
> `**WITHDRAWN YYYY-MM-DD**` marker in the same row — both, not either
> (R6c warns on marker-without-strikethrough). The JSON twin keeps the
> withdrawn wording only inside double quotes ("previously read here as
> established: …"), which R6 treats as mention, not assertion.

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
| KC13 | `z` exactly bar-even; `κ_{(2,1)}` exactly bar-odd; no scalar z-functional sources the odd channel. **C-scoped (2026-08-15, §9g):** proved for the convention-C `z = √q/(1+q)` (`ZBarParity.lean:59-79`); under convention D `bar(z_D) = q⁻⁴·z_D` **exactly** (not bar-invariant), so the no-scalar-z-source prune does not transfer to D as stated — re-examination under D is open (bean `qou-cds1`; `qou-b3nk` closed 2026-08-23), not a result | proved-lean (`z_bar_invariant`, `kappa21_bar_odd`, ZBarParity) | even resp. odd / `1/2` resp. `0` | PR #3449 |
| KC14 | `f(z)·κ_{(2,1)}` order-blocked at q=1 (odd total order vs finite nonzero shadow) | symbolic-exact | — | PR #3449 (T3 witness) |
| KC20 | bar-ODD carrier is **not a root-of-unity object**: `num = (q²−1)·R₁₂` (cyclotomic content exactly `q²−1`; `Φ₄=q²+1 ∤ num`, remainder `−64`), and `R₁₂ = q⁶·C(q²+q⁻²)` with `C(y)=y³−4y²+3y−2` **irreducible** (no rational root among RRT candidates). Degree-3 field ⇒ no quadratic anchor (golden `y=3`, silver `y=6`, q=1 `y=2`) is a root ⇒ real-q/quadratic `c_3` closures structurally excluded. **proved-lean**: the factorisation, `Φ₄ ∤ num`, the trace-cubic reduction, `C = C_Hopf + C_unknot`, and no-rational-root of `C`/`C_Hopf`. **symbolic-exact** (witness, not Lean): the sector attribution (the cubic is the **Hopf (2-crossing)** sector `C_Hopf=y³−6y²+10y−6`; unknot adds `C_unknot=2y²−7y+4`; virtual+trefoil vanish). The discriminants (`C: −152=−2³·19`, `C_Hopf: −76=−2²·19`, shared prime 19) are **Lean-certified since 2026-07-13** (`cubicDisc` + `cubicC_disc`/`cubicC_Hopf_disc`/`disc_shared_prime_19`, generic `CommRing`) | proved-lean (`numOdd_factor`, `numOdd_at_phi4_root`, `R12_eq_cubic_trace`, `cubicC_sector_decomp`, `cubicC_rrt_candidates_all_nonzero`, `cubicC_Hopf_rrt_candidates_all_nonzero`, `cubicC_disc`, `cubicC_Hopf_disc`, `disc_shared_prime_19`) + symbolic-exact (sector attribution) | — / — | PR #3467 ([audit](../audits/2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md); refines [2026-07-04 ζ₄ refutation](../audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md); complements KC19 affine ladder, PR #3473) |
| KC21 | **the c₃ bar-odd part factors `S = h·D(ũ)`** — `h = q−q⁻¹` the anchor-blind bar-odd carrier, `D(ũ)` a bar-even ℚ(√3) ladder — and the "wall" is a representation artifact: the `dc₃/dq ≈ 4.66×10⁶` hypersensitivity is the `1/u³` ladder inversion over a **smooth** zero (`S′(q*_S) = 2.37×(1/u³)`); the sign-flip is **structural** (bar-odd: with `q = q₀+iε`, `S(−ε) = −S(ε)`, so no real q₀ produces it); the `S=0` point **`q*_S` ≈ 1.10998** (**NOT** KC22's `q*_ρ ≈ 1.48989` — see the glyph note under this table) is **NOT an independent determination of q₀** — it is the root of `c₃ + Vol(4₁)` and so presupposes (H1); the ~~"third, decay-sector determination"~~ reading is **WITHDRAWN 2026-08-15**, see **§9f**; the Φ_b state-integral saddle supplies the `\|S\|` scale from geometry (`Im 𝔙 = 0` at real substrate, volume deficit `0.0094 ≈ \|S(muon)\|`) — but that scale match is **muon-only and anchor-selective**, see the scale caveat below. **Convention note (2026-08-15, §9g):** the ladder behind `S`/`D(ũ)` consumes the convention-C `z` via `α=(z−1)h/2` (`qbeta_ck_sseries_exact_rational.py:20,248`), so the value-level `S`/`q*_S` facts are **C-conditional**; the structural parity statement and the `1/u³` result are convention-immune. **Parity immunity VERIFIED 2026-08-15 (§9h, bean `qou-kc21im`)** — it was *asserted* when added here, and is now measured (re-derived under D: holds to `1e-45` over eight decades of `ε` while the frame moves `c₃` by 470× its own magnitude) and *reduced*: the parity is Schwarz reflection, which reads only that `z` is **real-valued on the real q-axis** and never `z`'s formula, so it is immune to conventions beyond the two registered ones (`alphaPhase_im_odd_of_reflective_markov`, sorry-free, quantified over every reflective `z`). **Two corrections the verification forced.** (i) The statement is about **`Im S`**: the literal full-value reading `S(−ε)=−S(ε)` is **false**, since `Re S` is even and nonzero (`−0.0394593` at the proton pin). (ii) The operative hypothesis is **real coefficients, not bar-oddness** — the bar-**even** `Q_A` has the identical `ε`-parity — so this parity is **NOT evidence that the channel carrying it is bar-odd**, and the row's "bar-odd ⇒ odd in ε" reading of the Lean is superseded by "reflective ⇒ `Im` odd in ε" (`fig8TraceC_conj` is the operative lemma). Complex conjugation is **not** the bar involution `σ: q↦q⁻¹`; nothing here bears on `bar(z_D) = q⁻⁴·z_D` or the `z_C` full-bar-condition failure | proved-lean (`fig8Trace_im_odd`, `fig8Trace_im_real_zero`, `reflective_im_odd`, `alphaPhase_im_odd_of_reflective_markov`, `zD_reflective`) + symbolic-exact (`S = h·D` split, `1/u³` prefactor, Φ_b saddle) | odd / `0` | PRs #3600/#3636/#3654 ([capstone](../audits/2026-07-12-c3-wall-resolution-capstone.md); [1/u³ audit](../audits/2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md)) |
| KC22 | **`D(ũ)` is NOT low-order (q-)holonomic in any tested class** — exact `d_k = a_k + b_k√3 ∈ ℚ(√3)` through `k=21`, **convergent, radius `ρ = 0.142799996644689688905720885779` (CORRECTED 2026-08-09)** — `ρ = ũ(q*_ρ)`, **`q*_ρ` ≈ 1.48989** the unique real root > 1 of the irreducible degree-12 factor of the `Δ_net` numerator, a **`Q_b` zero** the 2026-07-12 singularity search omitted (**NOT** KC21's `q*_S` ≈ 1.10998 — see the glyph note under this table); the `≈0.143` ratio was the radius all along, not a `(k!)^C` shadow: no ℚ P-finite recurrence (separated `a_k`, `b_k`), no **coupled ℚ(√3)** matrix P-recurrence (`r≤2, D≤4`; `r=3, D≤3`; `r=4, D≤2` — exact, over-determined), no **q-holonomic** recurrence in base `3`, `1/3`, or classical `k` (`r≤3, E≤3`, prime-certified full rank) — even though the denominators are 3-smooth (`v₃(den d_k) ~ 1.5k`, Ohtsuki–Habiro). Denominator **2-adic valuation is parity-graded** (proved window `K=5`; conjecture class beyond; `p=3` ungraded ⇒ **2 is the unique graded prime**). Consequence: the (q-)holonomic search class is closed — that part stands, and is unaffected by the radius correction (a convergent series need not be holonomic; `φ(w)log(1−w/ρ) + ψ(w)` with algebraic `φ`, `ψ` over a degree-12 field is exactly the sort of element that is not low-order P-finite). ~~the odd-channel element is transcendental/**resurgent** (Écalle acceleration class), not a q-difference equation~~ — **the resurgent/Écalle inference is WITHDRAWN 2026-08-09**: it was drawn from the divergence, and the ladder is convergent (`k²Δ²log|d_k| → 1`, `kΔ² → 0`, so `κ = 0`). Closed form `D(w) = φ(w)log(1−w/ρ) + ψ(w)`, `φ(ρ) = 1/(2h*_ρ)`, `h*_ρ = q*_ρ − 1/q*_ρ = 0.818706471352` (**NOT** KC21's `h*_S = 0.2090603174197`), hence `d_k = −(1/(2h*_ρ))ρ^{−k}/k(1+O(1/k))` with no free parameters. The exact non-holonomicity, the 2-adic parity grading, and the Lean anchors are all untouched. **Log-closure loophole also closed (2026-07-14, owner-suggested):** `log D` and `ũD′/D` (exact `ℓ_k ∈ ℚ(√3)`, k≤20) are likewise not low-order coupled-ℚ(√3) P-finite nor q-holonomic in base `3`/`1/3`/`k` (same windows, prime-certified) — so `D` is not the exp of a low-order (q-)holonomic element either. **Convention note (2026-08-15, §9g):** the `d_k` are Taylor data of the **convention-C** ladder (`z_C` at `qbeta_ck_sseries_exact_rational.py:20,248`); the radius object `R₁₂`/`Δ_net` is itself z-free (even powers of q only, KC20) | symbolic-exact (exact rational linear algebra + prime-certified rank) + proved-lean 2-adic anchor (`DLadderTwoAdicGrading.bDen_two_adic_graded`; `three_not_parity_graded`; open `DLadderGradingConjecture`) | — / — | PR #3737 ([coupled-recurrence + 2-adic audit](../audits/2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md); [divergence correction](../audits/2026-07-12-dladder-divergence-correction.md); **[convergence correction 2026-08-09](../audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md)**) |

### 9a. Glyph note — `q*`, `h*`, `ũ(q*)` name TWO points (added 2026-08-14)

KC21 and KC22 are adjacent and both wrote `q*`, `h*` and `ũ(q*)` without
qualification. They are **different points**, off by 1.34× / 3.92× / 15.1×:

| glyph | **`q*_S`** — KC21, the `S = 0` point | **`q*_ρ`** — KC22, the `Q_b` zero |
|---|---|---|
| `q*` | `1.109978593031523288402…` | `1.489894799688365248225…` |
| `h* = q* − 1/q*` | `0.2090603174197` | `0.818706471352` |
| `ũ(q*)` | `0.0094539496177732` | `0.14279999664469` (`= ρ`) |
| what it is | the `S = 0` point — an **(H1)-conditional** determination of q₀, **NOT** an independent third one (**§9f**); independent of the two *mass* pins only | the D-ladder's **radius of convergence**; root of the degree-12 `Δ_net` factor |

**Always subscript.** Attributes do not transfer between them (AGENTS.md
§"Conditional-proved ≠ premise-established" rule 4): `q*_S` sits ~1e-8 from q₀
and carries anchor meaning; `q*_ρ` is a singularity of `log R` and carries
none. Verified in
[`kc21_kc22_glyph_and_anchor_robustness_check.py`](../../computations/qbeta/kc21_kc22_glyph_and_anchor_robustness_check.py)
(`q*_ρ` recomputed from the polynomial, not quoted).

### 9b. Scale caveat — the Φ_b deficit → `|S|` match is anchor-selective (added 2026-08-14)

> **⚠ SHARPENED + ATTRIBUTED 2026-08-15.** The original text here argued the
> match "can hold at at most one anchor" because `|S_leak|` swings `4.075×`, and
> called the gap a "26.3× disagreement". Two corrections, neither of which
> changes the verdict:
>
> 1. **Not new, and previously uncited.** The mechanism was already established
>    as **Route A** (2026-08-01) — the ratio is *anchor-offset arithmetic near
>    the S-zero*, not a period — and is **Lean-proved sorry-free** in
>    [`SLeakMagnitudeOffsetRatio.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakMagnitudeOffsetRatio.lean)
>    (`linear_ratio_slope_independent`, `smooth_ratio_near_one`,
>    `smooth_period_excluded_as_magnitude`). §9b restated it without the
>    citation. The citation is now here.
> 2. **The "26.3× disagreement" framing overstates what the proton value
>    tests.** It presents `|S_leak(proton)|` as a meaningful target. It is not —
>    see below. The correct objection is stronger than the one first given.

KC21 cites the Φ_b state-integral saddle as supplying the `|S|` scale "from
geometry … smooth + anchor-blind". The real defect is sharper: **`|S_leak|` at
either anchor carries no scale content at all.**

**`S_leak`'s zero lies BETWEEN the two anchors**, at `q*_S ≈ 1.109978593`, which
sits **80.28 %** of the way from the proton pin to the muon pin — hence the
opposite signs in the witness (`S_muon = +0.009683`, `S_proton = −0.039459`).
Across that interval `S_leak` is **linear through the zero**, so its magnitude at
an anchor is just `|slope| × |q_anchor − q*_S|`:

| | value |
|---|---|
| `\|q_proton − q*_S\| / \|q_muon − q*_S\|` (lever arm) | **4.0700** |
| measured `\|S_leak(proton)\| / \|S_leak(muon)\|` | **4.0751** |
| agreement | **0.12 %** |

**The "4.075× anchor swing" is that lever arm and nothing else** — Route A's
result, and the content of `linear_ratio_slope_independent` (the slope
*cancels*, so the ratio is pure offset arithmetic). It is set by where the
calibration happens to place the anchors relative to `q*_S`, not by any property
of `S_leak`. Consequently:

| | value | status |
|---|---|---|
| `vol_deficit` (both anchors) | `0.0094025…` | a genuine geometric constant |
| `\|S_leak(muon)\|` | `0.00968298` | `slope × 2.53e-9` — **no scale content** |
| `\|S_leak(proton)\|` | `0.03945936` | `slope × 1.03e-8` — **no scale content** |

The quoted 2.896 % agreement at the muon is therefore **not weak evidence for
(H1); it is not evidence at all** — it is a constant compared against a
near-zero residual whose size is a calibration accident. Equally, the 76.17 %
"miss" at the proton is **not counter-evidence**, and the "26.3× disagreement"
framing of the original text is withdrawn: it presented the proton number as a
meaningful test.

**Why the earlier "anchor-blind vs anchor-dependent" framing was circular.** Over
the same `Δq = 1.28e-8`, the carrier `h·D` moves by `1.23e-9` (slope ≈ **0.096**
— an ordinary smooth function) while `S_leak` moves by `0.0491` (slope ≈
**3.84e6**, within 17.7 % of the corpus value `dc₃/dq ≈ 4.66e6`). So
"anchor-blind" means *ordinary derivative* and "anchor-dependent" means *the
`1/u³` ladder inversion* — a result the 2026-07-12 capstone already closed
("the wall was never physical"). Casting it as an open obstruction re-imports a
settled finding as a gate.

**Calibration of the 2.9 %.** The deficit is **5.32× closer** to the ladder's own
expansion variable `ũ₀ = 0.0094539…` (0.544 %) than to `|S(muon)|` (2.896 %).
`ũ₀` carries no 4₁-volume content, so at that tolerance the match does not
discriminate a geometric reading from a numerological one.

The producing witness is honest — it records both anchors and says
`"deficit 0.0094 ~ |S(muon)|"` explicitly. It was the KC21 summary that
generalised a muon-only match into "the `|S|` scale".

#### What the carrier mismatch actually is — a ZERO, not a magnitude

The corpus note *"the carrier is anchor-blind (spread `1.23e-9`) and is NOT the
swinging empirical `S`, so `S = h·D(ũ)` is schematic, not a tight identity"*
(`qbeta-c3-qstar-k31-repin.witness.json`) is **right**, but not for the reason
the wording suggests. The mismatch is not that one swings and the other does
not — per the slope figures above, that comparison is just the `1/u³`
hypersensitivity restated.

The real mismatch: **`h·D(ũ₀) = −0.003486…` is a nonzero near-constant, while
`S_leak` passes through zero between the anchors.** A nonzero constant cannot
equal a function that crosses zero. That is a statement about the **location of
the zero**, and it is checkable.

**Consequence for any fibre-level attack.** The target is the zero location
`q*_S`, **not** a magnitude. This is why magnitude-matching attempts have failed
— they were matching a quantity (`|S_leak|` at an anchor) that carries no scale
information.

> **⚠ One sentence removed here, 2026-08-15.** This paragraph originally closed
> with *"It also fits `q*_S`'s independent standing as the third, decay-sector
> determination of q₀ (§3)."* That standing does not exist — `q*_S` is the root
> of `c₃ + Vol(4₁)` and so presupposes (H1). See **§9f**. The sentence was added
> in the same 2026-08-14 edit that corrected other errors in this section, which
> is how a withdrawn claim got re-asserted inside its own correction.

### 9c. `c₃^even = −Vol(4₁)` — the registry pointer (answers `qou-qb8f` (c))

Bean [`qou-qb8f`](../../.beans/qou-qb8f--is-c3-even-derived-to-be-vol41-two-inequivalent-splits.md)
asked whether the registry's c₃ row should carry a pointer on **(H1)**
`c₃^even = −Vol(4₁)`. It should, and this is it:

> **(H1) is NOT derived.** It is *geometrically motivated* — the Φ_b saddle gives
> `Im 𝔙 = 0` at the real substrate (amphichirality) and a volume deficit at the
> `|S|` scale — but per §9b that scale match is **muon-only** and no better than
> the substrate's own `ũ₀`. The bar-split is in any case **not determinable from
> anchor data** (it needs c₃ at `q ≈ 0.901`; both anchors sit at `q ≈ 1.10998`),
> so it must come from an assumed structural form. **Neither** named split is a
> derivation: `S_leak := c₃ + Vol(4₁)` and `S := −c₃/κ_(2,1)` are both
> *definitions*, and c₃ is recovered exactly from either — reparametrisations
> carrying no information (AGENTS.md §"Defined residual ≠ derived
> decomposition"). **c₃'s bar-parity is undetermined by the present corpus.**

Consequently the §3 phrase *"the `−Vol(4₁)` piece is the solved bar-even part"*
is **re-scoped**: motivated, not solved. The `10/3 = lim_{q→1}[10]_q/[3]_q`
writhe-ratio identity in that same bullet is exact and unaffected. c₃'s tier is
unchanged (**EMPIRICAL / REFUTED as real-q**).

Two objects are both called "the c₃ bar-odd `S`" and differ by ~5 orders
(`S_leak ≈ 0.0097` vs `S ≈ 886.79`); `SLeakZeroCrossing.lean` carries a collision
guard, but the 2026-07-12 capstone straddles them and KC21 inherits the
vocabulary. **Say which `S` you mean.**

### 9d. Resummation-witness re-tier — the owed item from `qou-qb8e`

The 2026-08-09 convergence correction enumerated 29 D-ladder witnesses and
recorded which had been rendered ill-posed, but explicitly deferred the re-tier:
*"That re-tiering is a registry edit and is **not made here**; it is tracked on
bean `qou-qb8e`."* This is that edit.

**Why it matters, and why a re-run would not have caught it.** No witness file
was wrong, and **all 29 still report `allPassed: true`** — each computes exactly
what it says it computes. What changed is that for one group the *question* is
ill-posed: they are divergent-series estimators applied to a series that
converges. Their recorded failures — *"gate fails at every `s`"*,
*"length-blocked at k=41"*, *"UNDECIDABLE at k=21"* — read as obstructions to be
overcome with more terms. They are not. They are the estimators detecting that
**there is nothing to estimate**.

| tier | count | reading |
|---|---|---|
| **A — UNAFFECTED** | 6 | arithmetic / holonomicity / 2-adic; independent of growth class |
| **B — scope-(b) CLOSED / ILL-POSED** | **12** | divergent-series estimators on a convergent series |
| **C — PARTIALLY superseded** | 1 | exact k=31 data stands; its "divergence-class C" reading is the spurious `1/log k` decay |
| **D — NOT ASSESSED** | **3** | genuinely different object (deformed meridian); radius result does not transfer |

**Group B is re-tiered from scope-(a) NEGATIVE to scope-(b) CLOSED/ILL-POSED.**
None is deleted — they are the evidence the resummation arm was pursued properly
and exhausted, and their input (the exact `ℚ(√3)` ladder) is live. What changes
is that **none of them is an open lever**: do not re-run them for more terms, and
do not read their failures as a gate.

#### Correction to the 2026-08-09 group assignment (B is 12, D is 3)

That note put `qbeta-odd-channel-stokes-borel` in group **D** ("different
object … concerns the deformed meridian and the odd-channel Stokes structure,
**not `D(ũ)`**"). **That is wrong, and it is checkable in one line.** The probe
imports the D-ladder producer and calls it directly:

```python
import qbeta_dladder_generating_function_structure_probe as P   # line 87
dk, KMAX, valid_top, odd_ok = P.build_d_ladder()                # line 136
```

It operates on **exactly the same `d_k`**, so the radius result *does* transfer
and it belongs in **B**. Verified by reference count: the three genuine group-D
probes (`…deformed-meridian`, `…deformed-rungs`, `…borel-pade-resummation`) have
**0** references to `build_d_ladder`; this one has **4**.

This is also why its re-scope in PR #5050 was correct rather than an over-reach:
its own data corroborates convergence (Gevrey order drifts **down**, `0.08→0.05`;
Borel–Leroy pole `0.147` at `s = 0.02`, ≈3 % from `ρ` and trending toward it as
`s → 0`). Scope-(a): that is *consistency with* the radius, **not** a derivation
of `ρ` from Borel–Leroy.

Its method negative — plain-Borel (Vol/π) does **not** transfer to the odd
channel, so G3 (#3805) needs the true q-Borel/alien chain — is a statement about
the *method* and survives the re-tier intact.

#### Group B — the twelve

    qbeta-dladder-ecalle-acceleration                 Leroy gate fails at every s
    qbeta-dladder-ecalle-phib-resummation
    qbeta-dladder-single-instanton-extraction         "length-blocked at k=41"
    qbeta-dladder-fibre-branch-stokes-ambiguity       r* = 0.147 IS the ratio estimate of ρ
    qbeta-dladder-fibre-two-action
    qbeta-dladder-jackson-qborel-acceleration
    qbeta-dladder-qborel-leroy-resummation
    qbeta-dladder-parity-split-resummation
    qbeta-dladder-parity-odd-singularity-even-order
    qbeta-dladder-barodd-borel-pade-laplace
    qbeta-dladder-parity-adjudication                 "UNDECIDABLE at k=21"
    qbeta-odd-channel-stokes-borel                    ← moved from D (see above)

`…fibre-branch-stokes-ambiguity` is the sharpest of them: its `r* = 0.147` was
recorded as an ambiguity scale and is in fact a ratio estimate of `ρ = 0.1428`
— the arm measuring the radius while reporting a Stokes datum.

#### The reusable falsifier

Any future claim of Gevrey growth, a nonzero instanton action, or a Stokes
ambiguity **in this ladder** must first exhibit a singularity of
`log R(q) − log R(1/q)` strictly inside `|ũ| < ρ`. The complete singular set is
enumerated in the 2026-08-09 audit; none is. Do not open another
Borel/Leroy/Stokes/Écalle probe on `D(ũ)` without clearing that bar first.

**Scope.** Scope-(b) here is the *proved-invariant* kind and is justified by the
enumerated singular set plus `κ = 0` (`k²Δ²log|d_k| → 1`, `kΔ² → 0`), not by a
numerical near-miss. It closes the resummation arm on **this** ladder only. The
Ohtsuki κ-tower is genuinely Gevrey-1 divergent and its resurgence programme is
untouched, as are the three group-D probes.

### 9e. The swing is resolved but circular; individual `S` values are not resolved (added 2026-08-15, `qou-9jem`)

Two pins so no future session re-targets either object:

1. **Individual `S_leak` values are not robustly defined.** Each carries a
   ±1.262 CAL-3 propagated uncertainty (the `1/u³` amplification of the Q_β
   input error) — 130× the muon and 32× the proton central value. The
   canonical witness (`qbeta-c3-barodd-sleak.witness.json`) states the
   anchor sign flip "must not be cited as an established sign flip" (O2
   negative, [`2026-08-14-aomega-to-S-bridge-refuted-O2-negative.md`](../audits/2026-08-14-aomega-to-S-bridge-refuted-O2-negative.md)).
   This does **not** touch KC21's *structural* parity statement
   (`S(−ε) = −S(ε)` in complex `ε`, Lean `fig8Trace_im_odd`) — that is an
   odd-function fact, not a claim that the real-anchor data exhibit a flip.
2. **The swing `S(μ) − S(p) = c₃(μ) − c₃(p) = 0.0491423421` IS resolved**
   (±7.6×10⁻⁷; the CAL-3 error is common-mode and cancels) — but it is
   **not an independent derivation target**: it factors exactly as
   (11.54 ppb μ–p substrate tension) × `dc₃/dq`, i.e. the known open
   tension amplified by the circular cal-anchored `c₃` extraction
   (probe [`aomega_6y1p_swing_reframe_not_tractable.py`](../../computations/probes/aomega_6y1p_swing_reframe_not_tractable.py),
   exit 0; bean `qou-6y1p`, scrapped). Deriving it requires **both** a
   first-principles `c₃` (the fixed theory ladder has `[u³] ≡ 0`) **and**
   the μ–p tension. It remains valid as a *filter* on candidate `u(q₀)`
   maps (the A3 swing-difference gate), not as a target.

### 9f. `q*_S` is NOT an independent determination of q₀ (added 2026-08-15, `qou-kh7e`)

> **Companion to §9e.** That section and this one were written independently,
> hours apart, and reach the same root from opposite ends: §9e from the
> *swing* ("the circular cal-anchored `c₃` extraction"), this one from the
> *zero* (`q*_S` presupposes (H1)). Read together they say the anchor-level
> `S` data supports neither a magnitude nor a determination.
>
> **§9e sharpens this section.** Its finding that each individual `S_leak`
> value carries **±1.262** propagated CAL-3 uncertainty — **130×** the muon
> central value `0.00968` — is stronger than the argument below. If the
> value is not resolved at all, the quoted "2.896 % agreement" between the
> Φ_b deficit and `|S(muon)|` is not a weak match; it is a comparison
> against a number with no resolved central value. §9b's conclusion stands
> on either ground.

Author-found. `c₃` is **extracted from experimental Q_β**, and `q*_S` is
root-found on `c₃ + Vol(4₁)` — so locating `q*_S` presupposes the very
hypothesis (H1) it was cited as evidence for.

    c₃(q)  = (Q_β^exp / Q_N2(q) − 1) / u(q)³      ← qbeta_utils.c3_target_at
    q*_S   = root of  S(q) = c₃(q) + Vol(4₁)       ← qstar_k31_repin_probe.py:164

`q*_S` is therefore a determination of q₀ **conditional on (H1)**. It *is*
independent of the two **mass** pins (it uses neither `m_p` nor `m_μ`) — that is
a weaker and different statement, and conflating the two is the defect.

#### The placement carries no information beyond Vol(4₁)'s value

[`sleak_offset_genericity_check.py`](../../computations/qbeta/sleak_offset_genericity_check.py)
(committed well before this note) shows **every** constant in

    window (−c₃(μ), −c₃(p)) = (2.02020024, 2.06934258),  width 0.0491423

puts a zero between the anchors — 7/7 unrelated constants tested (`2+1/36`,
`63/31`, `e^0.708`, …). As `V` sweeps that window, `q*_V` sweeps the **entire**
anchor interval. Vol(4₁)'s position in it:

| | |
|---|---|
| `(V − lo)/(hi − lo)` from the muon end | 0.197039 |
| from the proton end | **0.802961** |
| figure published for `q*_S` | **"≈ 80.3 % muon-ward"** |

**80.2961 % computed against "≈80.3 %" published.** The headline placement *is*
Vol(4₁)'s position in the genericity window — a restatement of
`c₃(q₀) ≈ −Vol(4₁)`, not a decay-sector preference. (That restatement is itself
worth only **0.031 σ** against `σ(c₃) = ±1.262`; the "0.48 %" this sentence
originally quoted is the **muon** figure — proton is 1.907 % — see the re-scope
box at the end of this section.) The supporting
argument that `q*_S` "is not the precision-weighted mean" (0.0007 % muon-ward)
is true and irrelevant: no in-window `V` gives a reconciliation either.

Consistent with this, [`SLeakMagnitudeOffsetRatio.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakMagnitudeOffsetRatio.lean)
already states the same thing from the magnitude side — *"the magnitude fixes
only **where the anchors fall** relative to `q*`"*. The anchor offsets and the
`80.3 %` are one datum, not two.

#### Sites corrected

| site | was |
|---|---|
| `observations/epistemic-status-of-calibrations.md` | *"a third, decay-sector determination … μ–p–Q_β three-way consistency test"* — **the calibration authority**, worst affected |
| `mass-theory/rem-qstar-decay-sector-q0.md` | *"a third determination of q₀, independent of both mass-sector pins"* |
| §3 above, KC21 row, and §9b | the same phrase; **§9b's was added 2026-08-14 by the same edit that corrected other errors in that section** |

**The Lean is clean.** `BarOddLadderShape.lean` uses "the decay-sector
determination `q*`" only as a *name* for the point where the numerator vanishes;
its content (`A(q*) = 0`) is unaffected. The other `decay-sector` hits
(`MassComputationChainRoadmap`, `BraneTowerNStar`) are an unrelated `n_⋆ = 2`
sector.

#### Scope, and what survives

Scope-(a). This does **not** refute (H1) — §9c already has it as *motivated, not
derived* — and does not show Vol(4₁) is absent from c₃. What falls is the **use
of `q*_S` as independent evidence**, and with it the "three-way" reading: the
substrate rests on **two** pins, and μ–p is a **two-way** tension.

Untouched and still correct: the `1/u³` smoothness result (`S′(q*_S) = 2.37 ×
(1/u³)`), `dq*/dQ_β ≈ −0.539`, and the bar-odd structural sign-flip.

> **🛑 The "surviving empirical fact" is RE-SCOPED 2026-08-15** (same day, same
> author, PR #5093; probe
> [`qbeta_h1_significance_against_cal3_band.py`](../../computations/qbeta/qbeta_h1_significance_against_cal3_band.py)).
> It previously read: *"the surviving empirical fact, stated without the
> machinery: **c₃ at the substrate anchor agrees with −Vol(4₁) to ≈ 0.48 %**
> (0.07 % at the muon for the full keystone form …; 2.3 % at the proton …)."*
> Two defects, both mine:
>
> 1. **The percentage omits the error bar on the quantity being compared.**
>    `σ(c₃) = ±1.262` per anchor, CAL-3 propagated — **61 %** of `|c₃|`. Derived
>    in the probe as `σ(Q_β)/(Q_N2·u³)`, reproducing the corpus's quoted 1.262 to
>    `4.1e-5` rather than assuming it. In σ the agreements are **0.031 σ**
>    (proton) and **0.008 σ** (muon). That is not strong evidence — it is *no*
>    evidence, and by the same standard §9e's O2 verdict already applied to the
>    `A_ω → S` bridge ("neither confirmed nor excluded … the signature of a fit").
>    That test had never been turned on **(H1) itself**, the hypothesis that
>    *defines* `S`.
> 2. **The 0.48 % is the MUON figure**, quoted under the label "the substrate
>    anchor". Measured: muon **0.479 %**, proton **1.907 %** — 4.0× worse. Since
>    the 2026-08-07 owner directive makes the proton pin the default, "substrate
>    anchor" now reads as proton, so the headline attaches the muon's number to
>    it and flatters (H1) fourfold.
>
> **This makes the genericity result above understate the problem by ~51×**: the
> 1σ acceptance for `V` is `[0.807, 3.331]`, width **2.524**, against the
> **0.0491** window the 7/7-constants check was computed over.
>
> **Scope-(a), and it cuts both ways.** (H1) is **not** refuted — no invariant
> forbids a `4₁`-volume ingredient in `c₃`'s bar-even part, and 0.031 σ is not
> evidence *against* it either. Nothing is being measured. Testability needs
> **32×** (proton) or **130×** (muon) sharper `Q_β`, bracketing the **25.68×**
> the zero-location test needs (#5084) — all three are the same lever.

Tracked: beans `qou-kh7e`, `qou-qb8g`.

### 9g. Convention provenance — the Q_β ladder is a convention-C object end-to-end (added 2026-08-15, owner redirect)

> **🛑 SUPERSEDED IN PART — owner ruling 2026-08-15** ([audit](../audits/2026-08-15-owner-ruling-convention-d-proton-color.md),
> bean `qou-cdh1`). Two things below are now settled and one sentence is stale.
>
> 1. **The decay channel's convention is adjudicated: it is D.** The ruling
>    (*"convention D is convention. excise convention C."*) settles what
>    scope-(a) below explicitly declined to settle. `channels.qbeta-decay` in
>    [`trace-convention-registry.json`](trace-convention-registry.json) is now
>    `definitional_convention: "D"`, `status: "agreed-migration-pending"`.
> 2. **"The Q_β channel is not registered there" is stale.** It *is* registered
>    — as `disputed` on 2026-08-15 (bean `qou-b3nk`), settled 2026-08-16.
>
> **What is NOT superseded — do not re-derive it.** Every number in the measured
> table below is a correct measurement of the C→D *sensitivity* and stays. In
> particular `c₃ ≈ −974` is **what the current extractor returns when fed `z_D`
> — a sensitivity measurement, not a proposed new value of `c₃`.** The ladder
> must be **re-derived** under D, not re-evaluated, and this is proved rather
> than assumed: `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes
> *"keep the C-frame ladder"* and *"the two-row forcing applies here"* mutually
> exclusive. That re-derivation is bean `qou-cds1`; until it lands, the
> C-conditional labels on rows `c_2`, `c_3`, KC13, KC21, KC22 above remain
> correct as written.

The 2026-08-09 owner ruling excised Markov-trace **convention C**
(`z = √q/(1+q)`) in favour of **D** (`z = q³/(q²+1)`) for the `mass`,
`binding`, and `borromean` channels of
[`trace-convention-registry.json`](trace-convention-registry.json). **The Q_β
channel is not registered there**, and its ladder consumes `z` in the N=1
rung phase `α = (z−1)h/2`
([`qbeta_utils.py:124-125`](../../computations/qbeta/qbeta_utils.py); same
`z_C` in the KC21/KC22 `D(ũ)`-ladder core and in `ZBarParity.lean` — note
that the `D` in "`D(ũ)`-ladder" is KC21's bar-even ℚ(√3) function `D`, **not**
convention D; that core evaluates at `z_C`). Measured
(probe [`qbeta-c3-ladder-trace-convention-sensitivity`](../../computations/qbeta/qbeta_c3_ladder_trace_convention_sensitivity_probe.py),
9/9 assertions; full pillar table:
[validity audit](../audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md)):

| fact | C frame | D re-extraction | consequence |
|---|---|---|---|
| extracted c₃ (proton / muon) | −2.06934258 / −2.02020024 | **−974.43 / −974.38** | every ≈−2 value-level fact ((H1), `[3]_q/25`, `J−ℏ²`, `S_leak`, `q*_S`) is **C-conditional** |
| anchor swing | 0.0491423 | 0.0493990 (**ratio 1.0052**) | the **REFUTED-as-real-q verdict is convention-immune** — it stands in both frames |
| implied empirical c₂ | −1.0176 (= −1 + c₃u) | **−9.299** | **c₂ = −1 (proved Taylor-exact) is a C-frame statement**; the proof stands, its object now carries its convention |
| N2/N1 residual ratio | 0.017 (58× rung improvement) | 0.89 (no convergence) | the ladder's rung convergence exists in the C frame only — the C→D excision does **not** transfer by a z-swap |
| bar parity of z | `bar(z_C) = z_C` exact | `bar(z_D) = q⁻⁴·z_D` exact | KC13's no-scalar-z-source prune is **C-scoped** |

**Scope-(a), both directions.** This adjudicates **no** convention for the
decay channel: the mass-channel forcing (two-row cap ⇒ `y_(1³) = 0` ⇒ D) has
not been examined for the β channel, whose explicit weight instance
(`y = (z, 1/2−z, z)`) has `y_(1³) ≠ 0`. Settling it — derive C, derive D (and
re-derive the ladder), or register `disputed` — is bean **`qou-b3nk`**.

> **Partly overtaken, 2026-08-16 (`qou-cdh1`).** Of the three options above, the
> third happened (registered `disputed`, 2026-08-15) and then the **owner ruling
> of 2026-08-15 settled the convention: D.** The registry channel is now
> `agreed-migration-pending`. What is **not** done is the part this paragraph
> lists first — a *derivation*. The ladder must be **re-derived** under D, which
> is bean **`qou-cds1`**, and `decayLadder_zC_threeRow_ne_zero` proves that is
> not a z-swap. `qou-b3nk` remains open on its own terms and is untouched here.

Until then: **any quote of a c₃/S/q*_S value must name the convention** (the
trace-convention registry's own rule: convention-silent trace values are not
comparable) — and after the ruling, naming it "C" also means naming it
**excised**.

**Registration addendum (2026-08-15, bean `qou-b3nk` worked).** The channel is
now **registered `disputed`** in `trace-convention-registry.json`
(`channels.qbeta-decay`: definitional `null` — the decay blocks write the
excised-C value while naming it "the Markov–Jones parameter", whose referent
has read D since 2026-08-09 — production `C`; an R9 evaluator on
`qbeta_utils.markov_parameter` asserts the C-state mechanically). Two upgrades
to the paragraph above:

1. **The escape is now proved, and unconditional in the parameter** — Lean
   `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free): *any* faithful
   normalised Markov trace at the ladder's `z_C` carries `y_(1³) ≠ 0` for every
   substrate `s = √q > 1`, so the two-row forcing and the C-frame ladder are
   **mutually exclusive** — the forcing cannot transfer by a z-swap. (The
   explicit instance `y = (z, 1/2−z, z)` cited above was the *wrong witness*
   for this: its `σ₀` functional value is `h/2` exactly, z-independently — it
   is a class inhabitant, not an Ocneanu `z_C`-trace. Conclusion unchanged,
   witness corrected.)
2. **The full-bar condition is now in Lean**: `bar(z) = z − h` holds for `z_D`
   exactly (`zD_full_bar_covariant`) and fails for any bar-even `z` — hence
   for `z_C` — away from `q² = 1` (`barEven_fullBar_forces_classical`,
   `zC_fails_fullBar`); premise (trace bar-compatibility) named, not proved.

Neither C nor D is *derived* for the decay channel; the full analysis and the
two honest settlement routes:
[`2026-08-15-qbeta-decay-channel-convention-disputed-registration.md`](../audits/2026-08-15-qbeta-decay-channel-convention-disputed-registration.md).

**One branch of the re-derivation is now CLOSED — in every convention, not only
in C (added 2026-08-23, `qou-cds1`, PR #5536).** `z` reaches the ladder at
exactly one place, the N=1 eigenphase `α = (z−1)h/2`
(`QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common`, sorry-free), and
`QOU.QBeta.EigenphaseCarrier` shows the carrier meant to hold that spectral
identification is **vacuous** — so `α` is asserted in C and derived in neither
frame. That file leaves a trichotomy for the transfer matrix: (1) braid image,
(2) arbitrary — circular, (3) a holonomy of an independently-defined connection
(KZ / Kohno–Drinfeld). It calls (1) excluded *by transcendence of
`2cos((z−1)h/2)` over `ℚ(q,z)`* — an **unproved docstring assertion**, scoped
to C.

Branch (1) is now **proved**, by an elementary boundedness argument instead:
`QOU.QBeta.BraidImageEigenphase.no_braid_character_C` / `_D`
([`BraidImageEigenphaseExclusion.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BraidImageEigenphaseExclusion.lean),
sorry-free, axioms `[propext, Classical.choice, Quot.sound]`). A braid word's
character is a Laurent polynomial and `|2cos α| ≤ 2` always; a Laurent
polynomial bounded on `(0,∞)` is constant; and `α_C`, `α_D` are both
non-constant — indeed unbounded, C below (`α_C(s) ≤ −(s−1)/4`) and D above
(`α_D(s) ≥ s−3`). **The argument never reads `z`'s formula**, so the exclusion
is a property of the whole class: *re-picking `z` cannot repair the D-frame
ladder inside the braid picture.* Scope-(b), citing a proved invariant.

Exact companion, 12/12, no float64:
[`qbeta_braid_image_eigenphase_exclusion_probe.py`](../../computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py)
— `det ρ(σ_i) = −1` identically in `q`; `tr ρ(w) ∈ ℤ[q,q⁻¹]` over all 1364
words of length ≤ 5; and the concrete failure: `ρ(σ₁σ₂)` has `det = 1`,
`tr = −1` **identically in `q`** (eigenphase `2π/3` at every substrate value)
against `2cos(α_C(q₀)) = 1.99726`. The rational-normalisation escape is closed
by `det M = 1`, which forces `c = ±1` (`−c² = 1` has no real solution).

**Three limits.** (i) ~~It closes the **character** case … not the
*eigenvalue-pair* case … that sub-case still needs the transcendence
argument.~~ **SUPERSEDED 2026-08-23 — the eigenvalue-pair case is now closed
too, and not by a transcendence argument.** The diagnosis was right (an
algebraic function *can* be bounded on `(0,∞)` and non-constant, e.g.
`q/(q+1)` — verified, A1 of the probe below), but boundedness was simply the
wrong invariant to push. The hypothesis already proved in that file is far
stronger than boundedness: `α` attains **every** non-positive real on `[1,∞)`,
so each level set `{s : 2cos α(s) = c}`, `c ∈ [−2,2]`, is **infinite** — and
infinitely many solutions kill a polynomial relation of **any** degree, Laurent
or algebraic. `QOU.QBeta.BraidImageEigenphase.coeffs_zero_of_surjective_nonpos`
([`BraidImageEigenphaseAlgebraic.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BraidImageEigenphaseAlgebraic.lean),
sorry-free, axioms `[propext, Classical.choice, Quot.sound]`): if
`∑_{j≤d} p_j(s)·(2cos α s)^j = 0` on `[1,∞)` then **every** `p_j = 0`. Three
applications of "a polynomial with infinitely many roots is zero" — freeze `Y`
at `c`, freeze `X` at `x`, then read off coefficients. The subsumption of the
Laurent statement is **machine-checked, not asserted** (`no_laurent_of_algebraic`
re-derives the predecessor as the `d = 1` case). Applies to a *sum of two
eigenvalues* because that is algebraic over `ℝ(s)` — the pairwise-sum resolvent
has coefficients in the base field, verified exactly at `3×3` and `4×4` (A2). (ii) It excludes a *functional*
identification on the substrate branch, not a numerical coincidence at `q₀`.
(iii) The Laurent shape of `tr ρ(w)` is imported from Geck–Pfeiffer as the
shape of the hypothesis.

**Still open, and unchanged by either pass:** no D-frame ladder is stated, and
`α` is derived in neither convention. With branch (1) now closed **in full**
(character *and* eigenvalue-pair) and branch (2) circular, branch (3) — a
holonomy of an independently-defined KZ / Kohno–Drinfeld connection — is the
only branch where a derivation of `α` can still live. `c₃ ≈ −974` remains a
sensitivity measurement, wired nowhere.

> **🛑 CORRECTION 2026-08-23 — "branch (3) is untouched" is FALSE, and this
> section said it.** The 2026-08-15 pass wrote *"branch (3) is untouched"* and
> the 2026-08-23 pass repeated it. Both are wrong, and the first was already
> wrong when written: `.beans/qou-pdix` and
> [`qbeta_eigenphase_holonomy_consistency_probe.py`](../../computations/qbeta/qbeta_eigenphase_holonomy_consistency_probe.py)
> (16 assertions) landed on `main` at **08:11 UTC**, the claim at **09:56 UTC**.
> Branch (3) carries ~a dozen dated bean entries and **four refuted sub-routes**:
> `α = c·ln q` (fails at `t³`); `α` as a quarter of `σ₁`'s half-monodromy
> log-gap (ratio not constant, `iπ` dominates ~15×); unitary holonomy
> (structurally blocked — `σ₁`'s phase content is `{0, π}`, `q`-independent);
> modular/`cosh` resummation (required factor `< 1`, `cosh ≥ 1`).
>
> **Un-attempted is narrower than "branch 3":** construct a KZ connection on
> `Conf_n` whose monodromy is the `H₃(q)` braiding on `V_(2,1)` and compute its
> holonomy angle. Kohno–Drinfeld fixes `ħ = 2 ln q`, so the scale is not free.
> A gating question sits ahead of it (`qou-pdix`, unresolved): the
> single-wrap-vs-typed NF ambiguity is **0.579 %** while the factor branch 3
> must derive is a **0.160 %** correction — 3.6× smaller than the convention
> ambiguity in the object it corrects.
>
> **A tension worth naming.** `α = (z−1)h/2` at `q = 1+t` has `t¹` coefficient
> `z(1)−1` and `t²` coefficient `1/4 + z′(1)` (re-verified independently). So
> `α` is holonomy-shaped through `t²` exactly when `z′(1) = 0` — **true for
> `z_C` (`1/4`), false for `z_D` (`5/4`)**. An independent structural signal
> pointing at C, alongside a field-membership argument excluding C. The two are
> about different things (`q → 1` jet vs membership in `ℚ(q)`) and do not
> contradict, but branch 3 has to face both.

Exact companion to the 2026-08-23 pass, 4/4, sympy-exact over `ℚ(s)` plus
mpmath at 60 dps, no float64:
[`qbeta_eigenphase_algebraic_exclusion_probe.py`](../../computations/qbeta/qbeta_eigenphase_algebraic_exclusion_probe.py).

### 9h. The KC21 parity immunity is VERIFIED — and its stated mechanism was wrong (added 2026-08-15, `qou-kc21im`)

§9g above closed with the sentence *"the structural parity statement
(`S(−ε)=−S(ε)`) and the `1/u³` result are convention-immune."* The `1/u³` half
carried a measurement (swing ratio D/C = 1.0052). **The parity half carried
none** — it was asserted, and the assertion is not obvious: `c₃(q)` is not a
convention-free object but is *defined by* an extractor whose N=1 rung consumes
the convention-C `z`, and under D that extractor is a different function
(`c₃ ≈ −974`). Parity of `f_C` does not transfer to `f_D` because both are
spelled `c₃`.

Probe [`qbeta-kc21-parity-convention-immunity`](../../computations/qbeta/qbeta_kc21_parity_convention_immunity_probe.py)
(12/12, exit 0, 60 dps, proton pin) settles it by **both** available routes.

| route | result |
|---|---|
| **re-derive under D** | parity holds to `1e-45` relative over `ε ∈ [10⁻³⁰, 10⁻²]`, non-vacuously (`Im c₃^D(q₀+10⁻⁸i) = 0.0386 ≠ 0`) — while the C→D shift moves the value by 972, i.e. **470× \|c₃^C\|** |
| **the reduction** | every ingredient (`h`, `ℏ_q`, `b`, `u`, `Q_A`, `z_C`, `z_D`, `cos`) is **Schwarz-reflective**, `f(conj q) = conj f(q)`; the class is closed under the field operations and composition, so the composite inherits it |

**Why it is immune, stated exactly.** The parity is Schwarz reflection. Its
only hypothesis on the Markov parameter is that `z` be **real-valued on the
real q-axis** near `q₀` (equivalently: holomorphic on a conjugate-symmetric
neighbourhood, real on the interval). It never reads `z`'s *formula*. So the
immunity is not a C-vs-D coincidence but a property of the whole class — a
control convention `z_X = q/(1+q²)`, present in no channel, has the parity too.
Formalized sorry-free in
[`LadderParityReflection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderParityReflection.lean):
`alphaPhase_im_odd_of_reflective_markov` is quantified over *every* reflective
`z`, with `zD_reflective` the concrete D instance. Only a convention whose `z`
carries an explicit `i`, or introduces a branch point/pole inside the disc used,
could break it; neither C nor D does (`z_C`'s branch point sits at `q = 0`,
`z_D`'s poles at `q = ±i`, both far from `q₀ ≈ 1.11`).

**Correction 1 — the statement is about `Im S`, and the literal reading is
false.** `Re S` is even in `ε` and nonzero (`−0.0394593` at the proton pin), so
the full complex value is *not* an odd function of `ε`; `S(−ε) = −S(ε)` written
of the value is wrong. The true statement, and the one the Lean proves, is
`Im S(q₀−iε) = −Im S(q₀+iε)` — the decay projection. The KC21 row is corrected
accordingly.

**Correction 2 — the parity is not evidence for bar-oddness.** KC21 derives it
as *"bar-odd ⇒ odd in ε."* That is not what the Lean chain proves. The operative
lemma is `fig8TraceC_conj`: **real coefficients ⇒ conjugation commutes ⇒ `Im`
odd in `ε`** — a hypothesis about real-analyticity that says nothing about
`σ: q↦q⁻¹`. Measured consequence: the manifestly bar-**even** `Q_A` has the
identical `ε`-parity. So every real-analytic ingredient of the ladder has this
property, bar-odd or not, and observing it in `S` does **not** discriminate the
bar-odd channel. The conclusion (immunity) stands; the reason given for it was
the wrong one, and it was doing evidential work it cannot do.

**Scope-(a), and three things this does NOT do.** It adjudicates **no**
convention for the Q_β channel (`qou-b3nk` is untouched by this section: the
addendum to §9g above registers the channel `disputed`, which records the
disagreement rather than settling it — neither C nor D is derived, and nothing
here changes that). *[Still true of **this section**, whose scope is the parity
immunity only — but the channel itself was settled the same day by the owner
ruling of 2026-08-15 (D); see the banner on §9g. What that ruling did **not**
supply is a derivation, so "neither C nor D is derived" stands as written: the
convention is now decided, the ladder is not yet re-derived (bean `qou-cds1`).]*
It
revives **no** C-conditional value — `c₃`, (H1), `[3]_q/25`, `J−ℏ²`, `S_leak`,
`q*_S` stay C-conditional per §9g. And it does **not** touch the **bar
involution**, which is a *different* involution from complex conjugation:
`bar(z_D) = q⁻⁴·z_D` (§9g) and the `z_C` full-bar-condition failure both stand
exactly as stated, so the bean's companion question — whether trace-derived
quantities still carry clean *bar* parity — is untouched here and stays open.
Per §"Defined residual ≠ derived decomposition", `S = c₃ + Vol(4₁)` remains a
residual of a C-frame extraction; the `h·D(ũ)` bar-split is a separate claim
from the `ε`-parity verified above and inherits none of its immunity.

Audit: [2026-08-15 KC21 parity convention-immunity](../audits/2026-08-15-kc21-parity-convention-immunity-audit.md).

### 9i. `c₂` vs `c̃₂` — one model, two normalisations, exact offset `1/8` (added 2026-08-16, `qou-f09n` + `qou-cwin` T2)

Three live quantities in this channel were all written `c₂`. Two of them come
from the **same model read two ways**, and the difference between them was
reported (by me, on PR #5210) as *"two different ladders … a live
contradiction"*. **That framing is withdrawn.** Nothing computes wrongly; it
is a naming defect. Owner ruling (2026-08-16): short distinct names, with the
tilde marking a different **normalisation of the same object**. (Note this is
*not* an appeal to the old `w_λ` / `w̃_λ` pairing — the notation register
retired that one on the same day, because the bare symbol's referent moved.
The tilde device is fine; the precedent is not available.)

| name | value | what it is | provenance |
|---|---|---|---|
| **`c₂`** | `−1` | coefficient of the **explicit factor** `(1 + c₂u²)` | **hardcoded** at [`qbeta_utils.py`](../../computations/qbeta/qbeta_utils.py) `c3_target_at` — definitional, not extracted |
| **`c̃₂`** | `−9/8` | `u²` coefficient of the **normalised series** `Φ(u)/Φ(0)` | measured by `qbeta_alpha_eff_ladder_reconciliation_probe.py` |
| **`c₂^even`** | ≈ `−8.00641` | the **bar-even part**, exact in `ℚ(√3)` | `qbeta_c3even_exact_sseries_probe.py`, bean `8we6` |

**The relation is proved, not measured.**
[`LadderCoeffNormalisation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderCoeffNormalisation.lean)
(sorry-free, `#print axioms` clean, base ring `ℝ` per §7c since `Real.cos` is
genuinely archimedean):

    c̃₂ = c₂ − 1/8        (`normalisedQuadCoeff_eq`)
    c₂ = −1  ⇒  c̃₂ = −9/8  (`normalisedQuadCoeff_at_neg_one`)

The `−1/8` is contributed **entirely by the model's cosine factor**, and comes
from the **half-argument** in `cos(α − u/2)`: the second derivative at `0` is
`−cos α/4`, so the quadratic Taylor coefficient is `−cos α/8`. The
`α`-dependence cancels in the normalisation — which is why the offset is a
clean rational rather than an anchor-dependent quantity, and why this is worth
a theorem instead of a measurement at one `q`.

**The `c₁` discrepancy is the same defect, not a second one.** The normalised
series has `c̃₁ = tan(α)/2 ≠ 0` while the #1887 reframe has `c₁ = 0`. The two
parameterisations do not share a base point (`Φ(0) = cos α ≠ 1`), so their
coefficients are not the same coefficients.

**Scope.** No number changes and nothing is wired. This gives **no** `c₂`
value (`−1` remains fixed by construction, not derived), **no** derivation of
`α` (un-derived in both Markov conventions — §9g), and **no** accuracy claim.

**The owed AGENTS.md item — done 2026-08-16 (owner-authorised), and half my
diagnosis was wrong.** The `c_k` truncation-order banner said *"`c_2 = −1` is
PROVED Taylor-exact"*. Bean `qou-f09n` claimed that was wrong on **both**
halves. Measured, only one half is:

- **"Taylor" is UNDER-SPECIFIED, not false — RETRACTED.** The `u²` coefficient
  of the **explicit-factor product** `Π_{k≥2}(1 + c_k u^k)` is exactly `c₂`,
  trivially, since there is no `k = 1` factor. So `c₂ = −1` **is** a Taylor
  coefficient — of *that* series. The bean called the normalised-series reading
  *"the natural reading"*; that was a reading presented as **the** reading. The
  rule is therefore **say which series**, never delete the word.
- **"PROVED" is wrong, and stands.** `N2_factor` is a bare `def` in
  `QBetaCategoricalPrecisionLadder.lean` with **no** theorem deriving it —
  every use `unfold`s it, and the Kashiwara provenance is a docstring. The Lean
  identity proves only the re-reading. The banner now says **"structural"**,
  which is what the source block itself claims and is defensible (no fit, no
  CODATA, no q₀); the over-compression happened in AGENTS.md, not in the block.

A third banner claim was checked and **left alone**: the `c_3 = −2` gap quoted
as `3.47 %` is `|−2 − c₃|/2`, while the ladder witness reports `3.3509 %` for
the same gap normalised by the extracted `c₃`. Neither is stale; neither should
be "fixed" into the other. That this normalisation trap sits in the same banner
as the `c₂`/`c̃₂` one is the whole lesson.
