# Red-team: is the Q_β `c_k` truncation ladder physics or numerology?

**Date:** 2026-08-16 · **Kind:** adversarial audit (read-only; no production
code, no wiring change) · **Bean:** `qou-cds1` · **License:** standing
Critical-distance red-team (AGENTS.md).

**Scope.** This is a merits challenge of the Q_β categorical precision ladder

$$Q_\beta(q) = Q_{\text{base}}\cdot\prod_{k\ge 2}\bigl(1 + c_k\,u^k\bigr),
\qquad u = b\,\hbar_q^2 \approx 0.00852$$

against the anti-fit discipline (AGENTS.md §"Before declaring refuted",
§"Defined residual ≠ derived decomposition", §"Formalize-first probe
discipline", the PSLQ entropy bound). It re-adjudicates each claim from
scratch and states the C→D status. **It changes no tier and wires nothing** —
that is `qou-cds1`'s job, not this audit's.

Corpus-grep discipline satisfied: `ck-dk-canonical-registry.md` (the ONE source
of truth), `2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`,
`1ppq-qbeta.md` flip-flop table, `2026-08-15-owner-ruling-convention-d-proton-color.md`
§S1, `qbeta_utils.py`, and the QBeta Lean tree all read.

---

## (a) Per-claim verdict table

Tiers: **proved-lean** (unconditional Lean derives the value) · **symbolic-exact**
(exact algebra, but the *identification* it rests on is asserted) · **near-match**
(reproduces the anchor, swings across anchors) · **fitted** (extracted by
inverting the experimental anchor; carries ≤ the data's digit budget).

| # | claim | verdict | evidence (file:line / decl) |
|---|---|---|---|
| 1 | `c_2 = −1` is Taylor-exact | **symbolic-exact, identification ASSERTED, C-frame** | Lean is a `ring` tautology `1 − b²ℏ⁴ = 1 − (bℏ²)²` (`q-beta-c-2-eq-neg-one-structural.lean:50-53`). The load-bearing step — "the operator-valued N=2 correction factor *is* `(1 − b²ℏ_q⁴)`" — is in the **docstring, not the Lean** (`:2-12`). Anchor-stable to 10⁻⁵⁰ (real evidence). Under D the *implied empirical* c₂ = **−9.299** (registry §9g:713) ⇒ even c₂ is a C-frame object. |
| 2 | `c_3 = −2 = J_Hopf(q=1)` is a derivation | **fitted / near-match — REFUTED as real-q, extracted from the anchor** | Swings −2.0202 (muon) → −2.0693 (proton), **2.3748 % cross-anchor** (proton-normalised; 2.4571 % normalised by the candidate −2). *Corrected 2026-08-16: the `2.98 %` that stood here does not follow from this row's own anchor pair — it is the gap to the superseded muon `c_3 = −2.0097`. See `qbeta_c3_crossanchor_swing_provenance_probe.py`. The verdict is unaffected.* (framing §"FACT B":40-42). A true Taylor coeff is anchor-independent. Rigidity of any real form is 4.7 M× tighter than the empirical swing (registry §3:78-82). Extracted, not derived: `c_k = (Q_exp/Q_ladder − 1)/u^k` (registry §3:117). The `= −2 = J_Hopf(q=1)` is a **q→1 shadow 5 ε-orders from the ladder order** — "accidental cross-order coincidence" (`1ppq-qbeta.md` order audit, PR #1593). |
| 3 | higher `c_k` (k≥4) are derived | **fitted / noise** | c_4 reproduces as **identically 0** when c_3 is extracted exactly ⇒ the quoted −0.972 is "purely the truncation residual of a rounded c_3, zero independent content" (registry §3:112-124, P4 entropy audit PR #3536). Extraction amplifies σ(Q_β) by 1/u^k ⇒ **zero reliable digits at k≥4**. c_6/c_7 forms are **imposed in the extraction** — "self-consistency, not independent validation" (registry §3:73). c_8–c_10 are proved *rationals at the silver ratio* but **not cross-anchor validated**, and the pattern **breaks at c_8** (wrong sign, registry §3:74). |
| 4 | ladder is a convergent series with a *derived* truncation order N (not a post-hoc fit) | **series-convergence is REAL; the coefficients it truncates are fitted** — see §(a-4) | The ladder **is** convergent, radius = u_substrate, `κ = 0` proved (KC22, registry §9:318). But N(ε) = log₁₀(1/ε)/2.07 − 1 (framing Rule 1:59) only "derives" N *given* O(1) coefficients — and c_k≥3 are not derived. The **N=4→N=5 non-monotonicity** (+0.055 → +0.63 ppb) is a **fit tell the framing itself flags**: "a convergent series with *exact* c_k would be monotone" (framing Rule 3:94). |
| 5 | the ladder survives C→D (D now canonical) | **NO — unmoored; honest status is UNKNOWN pending D re-derivation** | The whole ladder consumes `z_C = 1/(√q+1/√q)` at `qbeta_utils.py:124`, feeding `α=(z−1)h/2:125`. Under D: c₃ → **−974** (470×|c₃|), rung convergence **vanishes** (N2/N1: 0.017 → 0.89), c₂ implied → −9.299 (registry §9g table:709-715). **Proved not a z-swap**: `decayLadder_zC_threeRow_ne_zero` (sorry-free) — the C-frame ladder trace and the D-forced two-row trace are **mutually exclusive** (`MarkovZFullBarCondition.lean:168-181`). |
| 5b | `c₃^even = −Vol(4₁)` (the (H1) hypothesis) is derived | **NOT derived — a defined residual, no evidence** | `S_leak := c₃ + Vol(4₁)` is a **definition**, c₃ recovered exactly from it (registry §9c:436-451, AGENTS.md §"Defined residual ≠ derived decomposition"). The bar-split is **not determinable from anchor data at all** (needs c₃ at q≈0.901; both anchors at q≈1.110). The "0.48 % agreement" is the **muon** figure; against σ(c₃)=±1.262 it is **0.031σ (proton) / 0.008σ (muon) — no evidence** (registry §9f re-scope:658-690). |

---

## (a-4) The key question, answered directly

**Is N a derived truncation order, or is it chosen post-hoc to beat the target?**

Both readings are partly right, and separating them is the whole game:

- **The convergence is a genuine structural fact.** KC22 proves the ladder
  `D(ũ)` is convergent with radius `ρ = ũ(q*_ρ)` and `κ = 0` (no divergence),
  exact through `d₂₁` over `ℚ(√3)` (registry §9:318). This is real mathematics,
  Lean-anchored on the 2-adic grading. The step size `u ≈ 0.00852` giving
  ~2.07 digits/rung is arithmetic, not a fit.

- **But "derive N from u" only works for a ladder whose coefficients you have
  already fitted.** The N(ε) formula assumes the `c_k` are O(1). c_2 is O(1) by
  the asserted structural identification; **every c_k≥3 is obtained by inverting
  the single experimental number Q_β^exp** at the single anchor q₀. So the
  "series" is a residual expansion of *one measured scalar*: c_3 absorbs the
  residual after c_2, c_4 absorbs the residual after c_3, and so on. That is the
  textbook shape of an over-parametrised fit — N coefficients reproducing 1
  target — not N independent predictions.

- **The N=4→N=5 non-monotonicity is the tell, and the framing is honest about
  it.** A convergent series with *exact* coefficients truncates monotonically.
  The residual going +0.055 → +0.63 ppb from N=4 to N=5 is the ladder telling you
  its c_4, c_5 are near-matches, not Taylor coefficients. The canonical framing
  **states this explicitly** (Rule 3) and refuses to call the higher rungs
  proved. That is the discipline working — the framing is *not* itself
  numerology; it is a tiered, honest accounting that declines to wire the fit.

**Net on claim 4:** the framing document is physics-grade discipline. The
*object it describes* — the higher `c_k` — is a fit. Production wires **c_2
only** (registry §6:211-213); the ~0.17 % Q_β residual is the honest c_2-level
gap. Nothing beyond c_2 reaches a dashboard. This is a case where the anti-fit
machinery **succeeded**: the fit was caught and never shipped.

---

## (b) DOF-vs-precision accounting (the PSLQ / entropy argument)

The extraction inverts **one** experimental input per anchor:

    c_k = (Q_β^exp / Q_ladder(q₀) − 1) / u(q₀)^k          [registry §3:117]

Consequences, stated as a degrees-of-freedom budget:

1. **The ladder fits a single number with unboundedly many coefficients.**
   Q_β^exp is one scalar (per anchor). c_3, c_4, … are not independent
   observations — each is a residual-absorber. A model with ≥1 free coefficient
   per target datum is under-determined by construction; "matching" is
   guaranteed, not evidential.

2. **The digit budget is ~2 at c_3 and 0 beyond.** Because `1/u ≈ 117`, the
   inversion multiplies σ(Q_β) by `1/u^k`: ≤ ~2.2 reliable digits at k=3, **zero
   at k≥4** (registry §3:120, `qbeta-ck-basis-constrained-pslq.witness.json`).
   So the honest information content of "c_3" is `−2.0` — two digits. Identifying
   that with `J_Hopf(q=1) = −2` is a **1–2 digit coincidence at the noise floor**;
   it is exactly the resolution PSLQ would refuse to certify (the entropy bound
   `precision > n_terms·log₁₀(2·height)` that killed the 12-constant basis,
   AGENTS.md §Formalize-first).

3. **The cross-anchor swing is the falsifier, and it fires.** A real Taylor
   coefficient is anchor-independent. c_3 swings 2.3748 % (corrected from a
   stale 2.98 %, 2026-08-16); the rigidity of any
   candidate real-q form is 4.7 M× tighter than that swing (`dc₃/dq ≈ 4.66×10⁶`,
   registry §3). Therefore c_3 is **not** a real-q fibre constant — REFUTED, and
   this verdict is **convention-immune** (swing ratio D/C = 1.0052, registry
   §9g:712).

4. **σ(c_3) = ±1.262 — 61 % of |c_3|.** The CAL-3-propagated error on a single
   extracted c_3 is 130× the muon and 32× the proton central value (registry
   §9f:668). Any "structural identification" of c_3 to a named constant is a
   comparison against a quantity with no resolved central value.

**Bottom line of the accounting:** the ladder has as many free parameters as it
has rungs and one datum to fit. The only rung carrying more signal than noise is
c_3 (~2 digits), and those 2 digits swing across anchors by 15 000× their own
error-free rigidity. There is no high-precision identification to be had — a fact
the corpus reached independently three times.

---

## (c) C → D status: does it survive?

**No. Under the now-canonical convention D the entire ladder is unmoored, and
this is not repairable by substitution.**

- The ladder is a convention-C object **end to end**: `z_C` at
  `qbeta_utils.py:124`, and again in the KC21/KC22 `D(ũ)`-core and `ZBarParity`
  (registry §9g:693-704).
- Feeding the *current extractor* `z_D` returns c₃ ≈ **−974** and destroys rung
  convergence (registry §9g table). That −974 is a **sensitivity measurement, not
  a proposed new c₃** (owner ruling §S1:294).
- **Proved that it is not a z-swap.** `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
  (sorry-free, `MarkovZFullBarCondition.lean:168-181`): any faithful normalised
  Markov trace at the ladder's `z_C` carries `y_(1³) ≠ 0` for every `s = √q > 1`,
  so "keep the C-frame ladder" and "apply the two-row (D) forcing" are **mutually
  exclusive**. The ladder must be **re-derived under D, not re-evaluated**.

**What survives C→D (proved, do not re-derive):**

1. The **REFUTED-as-real-q** verdict — swing ratio D/C = 1.0052; stands in both
   frames.
2. The KC21 **ε-parity** (Schwarz reflection), Lean `alphaPhase_im_odd_of_reflective_markov`
   — but note its originally-stated bar-odd *mechanism was wrong* (registry §9h:752-800):
   it is real-analyticity, not bar-oddness, and is therefore **not** evidence the
   channel is bar-odd. The bar-even `Q_A` has the identical parity.
3. `c_2 = −1` as a *proof* — untouched — but its *object* is now known to be
   C-frame (implied empirical c₂ under D = −9.299).

**Honest status of the ladder as a whole under D: UNKNOWN pending re-derivation.**
Every value-level `c_k` fact, plus (H1), `[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S`,
is **C-conditional** (registry §9g:711). Do not quote a c_k number without naming
the convention.

---

## (d) Bottom line — physics or numerology?

**Both, cleanly separated — and the corpus already knows which is which, which is
the most important finding here.** The *convergence framework* is physics: the
ladder is a genuinely convergent series (radius = u_substrate, κ = 0, KC22,
Lean-anchored), and `c_2 = −1` is an exact algebraic identity resting on one
asserted (not proved) operator identification. The *higher coefficients* are
numerology-adjacent fits: c_3 is extracted by inverting the single experimental
Q_β, carries ~2 digits that swing 3 % across anchors (15 000× their rigidity),
and is REFUTED as a real-q constant; c_4 is a normalisation artifact that
vanishes when c_3 is extracted exactly; c_k≥5 are noise (zero reliable digits).
"c_3 = −2 = J_Hopf(q=1)" is a 1–2 digit shadow coincidence 5 ε-orders from the
ladder order — the exact object that flip-flopped into and out of production four
times. **The discipline held: production wires c_2 only, nothing beyond it ever
shipped, and the framing document tiers the fit honestly rather than laundering
it as a derivation.** And under the now-canonical convention D the whole ladder
is a C-frame object that is *proved* (not merely suspected) to be unrecoverable
by z-substitution — so its honest current status is **not "derived," not
"refuted," but UNKNOWN pending the D re-derivation tracked as `qou-cds1`.** The
one thing no agent should do is re-quote any C-frame c_k number as a D result, or
resurrect "c_3 = −2 = J_Hopf" as a derivation — that is the fifth flip-flop
waiting to happen.

---

## Cross-references

- Canonical framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- The ONE registry: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) §3, §6, §9c/§9f/§9g/§9h
- C→D ruling: [`2026-08-15-owner-ruling-convention-d-proton-color.md`](2026-08-15-owner-ruling-convention-d-proton-color.md) §S1
- Flip-flop table: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Load-bearing Lean: [`MarkovZFullBarCondition.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean), [`q-beta-c-2-eq-neg-one-structural.lean`](../../content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.lean)
- z-consumption: [`qbeta_utils.py:124-125`](../../computations/qbeta/qbeta_utils.py)
