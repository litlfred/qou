> **⚠ SUPERSEDED 2026-05-30** by [docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md](2026-05-30-qbeta-ck-mp-dk-deep-audit.md).
>
> This audit was at the WRONG c_3 form. Canonical c_3 = J_Hopf(q=1) − ℏ_q²
> (the q-deformed Hopf invariant from 2026-05-26 b2f9087315), NOT plain
> c_3 = −2. With canonical c_3, the Taylor match is **0.0038%**, not 0.49%.
> Discipline analysis in this audit is correct for what it tested; it tested
> the wrong target.

# Audit: μ–p tension sets the substrate accuracy floor (~240 ppb / 11.5 ppb in q₀)

**Date:** 2026-05-28

## TL;DR for other agents

The substrate has an **irreducible self-consistency tension** between the
muon and proton low-order mass formulas: no single `q₀` matches both to
CODATA simultaneously (each formula's residual cannot be zeroed at once).
The tension is **11.5 ppb in q₀ ≈ 240 ppb in m_p**. This is the substrate's
honest predictive floor. **Any fit that closes an observable below this
floor is modelling the tension = noise.** Do not re-introduce such fits to
production.

## The two independent q₀ pins

| Formula | q₀ that matches it to CODATA |
|---|---|
| `m_μ/m_e = Vol(4₁)/ℏ_q²` (muon, the canonical pin) | 1.10997859555… |
| `m_p/m_e = 2·Vol(4₁)/ℏ_q²·F_Bor(q) − 12` (proton) | 1.10997858275… |

The canonical repo `q₀` equals the **muon** pin to 0.00 ppb — i.e. the
substrate is calibrated on the muon. With that q₀:

| Pin q₀ from | Predict | Error | In experimental σ |
|---|---|---|---|
| muon (canonical) | m_p | −242 ppb | **4043 σ_exp(m_p)** |
| proton | m_μ | +210 ppb | **9.4 σ_exp(m_μ)** |

No choice of q₀ reconciles both within experiment. (`m_p/m_e` is measured
to 0.06 ppb; `m_μ/m_e` to ~22 ppb — the framework currently calibrates on
the *less* precise observable.)

## Consequence: the fitted towers are sub-floor noise

Several production/probe scripts "close" m_p or Q_β to ppb/ppQ via
multiplicative integer towers in `u = b·ℏ_q²`:

- m_p: `(1 + 46u⁴)(1 + 4u⁵)(1 − 29u⁶)(1 − 8u⁷)` — closes 242 ppb → 0.05 ppb
- Q_β: `c₃ = J, c₄ = J·b⁴, c₅ = 3J²+b` — closes 1247 ppb → 5.7 ppb

These close **~4800× below the 240 ppb floor**. They are not derivations:

1. **They target CODATA, not the categorical value.** The m_p tower closes
   the *formula→experiment* gap (242 ppb), not the *formula→exact-Habiro*
   gap (which is 6.7%, a different object — the exact proton Markov trace
   `tr_M_atomic(1,0)=1.0653` plugged into the formula gives **1960**, not
   1836). So the towers are fitting experiment.

   > **🛑 FIGURES CORRECTED 2026-09-05 — the conclusion survives, the
   > magnitudes do not.** The three numbers in this item are
   > **pre-migration**: `c1a3299434` (2026-08-16) migrated `markov_peel`'s
   > `word_to_element` path from convention C to convention D, eleven weeks
   > after this audit was written. Re-run today:
   >
   > | quantity | as published here | today |
   > |---|---|---|
   > | `tr_M_atomic(1,0)` | 1.0653 | **1.14575969245730086969** (+7.552 %) |
   > | implied `m_p/m_e` | 1960 | **2108.59** |
   > | gap vs the exact object | 6.7 % | **14.741 %** |
   >
   > **The argument is unaffected and is if anything strengthened** — the
   > formula→exact gap is now more than twice as large, so "the towers are
   > fitting experiment" holds with more room. Only the magnitudes move.
   >
   > Verified three independent ways, all agreeing: re-running
   > `computations/probe3qrv.py`; re-deriving this item's own formula
   > `m_p/m_e = 2·(Vol(4₁)/ℏ_q²·|tr_M|·[3]_q!/q³ − 6)` at 60 dps in mpmath,
   > which reproduces **1959.683** from the published trace and so validates
   > the reconstruction before applying it; and
   > `computations/probes/atom_intra_block_is_not_a_braid_probe.py`, whose
   > independently measured `rel 0.147409` against the Lean-proved closed form
   > `(4+h²−3h⁴−h⁶)/(h²+4)` is the same 14.741 %.
   >
   > **This figure has three carriers and this is the last of them.**
   > [`2026-08-08-borromean-trace-convention-forcing.md`](2026-08-08-borromean-trace-convention-forcing.md)
   > and `.beans/qou-3qrv` were corrected 2026-09-05; this one was found by
   > following `qou-3qrv`'s own cross-reference, which no mechanical scan
   > produced. Bean `qou-5pgl`.
2. **The integer coefficients have no categorical identity.** m_p's 46 is
   46.02 (not a clean invariant); the ℏ⁶ coefficient is 0.256, not 1/4.
3. **Q_β's apparent structure is a form artifact.** c₃'s "match" to −[2]_q
   (0.06%) collapses under a different (equally valid) c₂ form: with
   c₂ = cos(b·ℏ²), c₃_target swings from −2.01 to **−60.7**. c₃ is amplified
   ~100× (ℏ⁴/ℏ⁶) by any error in the unproven c₂, so it cannot be pinned.
4. **The probe that produces the Q_β value is in `_deprecated/probes/`** yet
   production reads its witness (`q-beta-operator-valued-N3.witness.json`).

## What IS genuinely derived (the honest floors)

| Observable | Derived to | Accuracy | Beyond = |
|---|---|---|---|
| m_p | N=0 (3-term formula) | 242 ppb (μ-p floor) | fit / noise |
| Q_β | N=1 (Kashiwara f̃₁, c₁=b) | 74 ppm | form-dependent / open |

- q₀ is pinned from m_p/m_e (2026-05-29; matched by construction via the
  substrate identity). m_μ/m_e = Vol/ℏ² is now a cross-check (9.5σ prediction).
- Q_β c₁ = b is the Kashiwara crystal edge weight — a real matrix element.
- Everything reaching ppb/ppQ is below the floor.

## The paper "proof" is a stub

`content/.../braids-and-knots/habiro-precision-ladder-equivalence.lean`
states three propositions all proved by `True := by trivial`. The narrative
asserts "the c_k are NOT empirical fits — they are integer polynomials
evaluated at the substrate," but (a) there is no proof, and (b) it is false
per the numerics above. The **true** part — `tr_M` has a finite expansion
with integer Habiro coefficients `a_m` — is verified computationally and
should be kept; the **bridge claim** (production c_k/d_i = those a_m) is what
fails.

## Recommendation

1. **De-fit production** (`per_observable_100x_status.py`,
   `mass_table_comprehensive.py`): report m_p at the 242 ppb floor and Q_β at
   the N=1/N=2 derived value; drop the integer towers. The dashboard should
   show m_p and Q_β do **not** beat 100× — that is the honest state.
2. **Reframe the paper blocks** (`habiro-precision-ladder-equivalence`,
   `proton-brane-tower-correction`): keep the derived structure (finite
   integer-a_m expansion; τ_M = Tr·exp(−½Σc_k ℏ²ᵏ); k=1 Kashiwara), delete
   the false "c_k are Habiro evaluations" + "1 ppQ" claims, relabel k≥3 as
   open R&D (matching `prop:tau-M-asymptotic-rep-theory`'s own honest Status).
3. **Banner the fit probes** as exploratory; stop production reading a
   `_deprecated/` witness.

## Relation to sibling work

The sibling Habiro-normalization audits (`2026-05-28-habiro-residual-319ppm`,
`2026-05-28-habiro-product-correction-7ppm`) close a **different** object —
the algebraic Habiro-vs-`tr_M` normalization identity, a math-to-math
comparison in the ppm range. Those `(1+ℏ²)`-type corrections are legitimate
*if* they compare two computed quantities (not experiment). This audit's
floor applies specifically to **observable→CODATA** fits: those below
~240 ppb on m_p are noise.
