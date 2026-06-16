# HOMFLY / Markov-trace convention discipline (KEEP THE WRITHE)

**Status:** authoritative convention reference. Cited by
`docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md`
and `computations/homflypt_reference_qa.py`.

This doc exists because the HOMFLY / Markov-trace normalisation has tripped
**multiple agents repeatedly**. The failure is always the same shape: three
different variable conventions coexist in the compute, an agent assumes one,
and the absolute values silently disagree with a knot invariant while passing
internal self-consistency checks. Read this before touching any HOMFLY,
Jones, Markov-trace, or `tr_M` normalisation.

## 0. The one-paragraph summary

There is **no one-line normalisation multiplier** that turns the current
`Σ_λ y_λ χ^λ` machinery into a correct HOMFLY polynomial, because (a) the
character is evaluated at the wrong variable, (b) the binding pipeline uses
`|χ^λ|` (modulus) which has already destroyed the sign a knot invariant
needs, and (c) **the writhe must be KEPT, not divided out** — in QOU the
framing carries physical content (the EM phase / chirality), so the target is
the *framed* invariant, not the textbook ambient-isotopy invariant.

## 1. The three coexisting conventions (the trap)

| Code path | σ eigenvalues | skein `z` | character evaluated at |
|---|---|---|---|
| `_homflypt_2strand_numerical` (n=2) | `(q, −1)` Jones-asymmetric | `q − 1` | `q₀` |
| `chi_lambda_braid`·`y_λ` (n≥3) | `(s, −s⁻¹)` symmetric | `s − s⁻¹` | **`q₀`** ← wrong |
| `(v, z)` declared by `homflypt_at_su_n` | — | `q₀^{1/2} − q₀^{-1/2}` | implies `s = √q₀` |

The n≥3 path calls `chi_lambda_braid(q_value=q₀)`, giving skein `q₀ − q₀⁻¹`,
while the engine *declares* `z = q₀^{1/2} − q₀^{-1/2}`. For consistency the
character **must be evaluated at `s = √q₀`** so that `s − s⁻¹ =
q₀^{1/2} − q₀^{-1/2} = z`. Evaluating at `q₀` is a concrete bug.

## 2. Principle A — KEEP THE WRITHE (the framing is physical)

Standard knot theory multiplies the Markov trace by `a^{−w}` (w = writhe =
braid exponent sum) to cancel the Reidemeister-I framing anomaly and obtain
an **ambient-isotopy** invariant — the textbook HOMFLY `P(K)`.

**QOU does the opposite on purpose.** The framing anomaly is the U(1) framing
phase `q^{w·c}` (writhe × colour) — it is the **electromagnetic phase /
chirality** degree of freedom (the Im part that lives at `|q| = 1`; purged by
`|·|` only when computing the strong-binding modulus). Dividing it out
discards the physics.

Consequence for any HOMFLY-like compute in this repo:

- The production object is the **framed** invariant
  `P_framed(β) = a^{w(β)} · P_unframed(β̂)`, which depends on the braid
  word's writhe — **this is a feature**.
- The raw Markov trace `tr_M(β)` already carries this writhe-dependence
  (before any `a^{−w}` correction). **Do not strip it.**
- The **correctness gate** still uses the unframed textbook value: validate
  `P_framed(β) · a^{−w(β)}` against the rigorous skein reference
  (`homflypt_reference_qa._torus_homfly`). The writhe stays in the production
  output; the gate just divides the *known* framing back out to check the
  knot-type part. Correctness is gated; physics is kept.

## 3. Principle B — signed `χ` (HOMFLY) vs `|χ|` (binding) are different objects

The mass/binding pipeline computes `Σ_λ y_λ · |χ^λ|` (modulus per partition;
see `per_bond_growth_a3.py:59`, `closed_form_tau_M.py`) because strong binding
is `|tr_M|` (CLAUDE.md: *"Strong binding = modulus"*). A **sum of absolute
values has already destroyed the sign** that a signed knot invariant needs.

> You cannot recover a signed HOMFLY/Jones value from `Σ y_λ |χ^λ|` by any
> normalisation. The HOMFLY engine needs **signed** `χ^λ`; it must be a
> **separate code path** from the binding `|tr_M|`. Never share the core.

## 4. The fix recipe (thread ONE convention end-to-end)

1. **Variable:** symmetric HOMFLY — eigenvalues `(s, −s⁻¹)`, `z = s − s⁻¹`,
   framing base `a = s^N` (SU(N)); `s = √q₀`.
2. **Character:** evaluate `χ^λ` at `s` (not `q₀`), **signed** (no `abs`).
3. **Trace:** `tr_M(β) = Σ_λ y_λ χ^λ(β)` with `y_λ` the genuine **Ocneanu
   weights for that `a`** — NOT the SU(2)-mass-specialised Wenzl weights.
   (Empirically the current `y_lambda_at` weights do **not** make
   `tr_M`/skein factor as a clean monomial, so they are not the right
   Ocneanu weights — this is the core of the rework.)
4. **Framed output (KEEP writhe):** production value is
   `δ^{n−1} · tr_M(β)` with `δ = (a⁻¹ − a)/z`. Do **not** apply `a^{−w}`.
5. **Gate (correctness):** `homflypt_reference_qa.py` checks
   `output · a^{−w} == _torus_homfly` (and held-out fig-8 / Borromean) to
   ~1e-6. Validate against the skein reference, never internal consistency.
6. **Separation:** binding `|tr_M|` and HOMFLY signed `tr_M` stay in
   different functions.

## 5. Why internal self-consistency never caught this

`cross_check_trM_1ppb.py` compares four methods that all compute the **same**
`Σ_λ y_λ χ^λ` definition. They agree → "1 ppb" green, but a shared convention
error is invisible. The skein reference in `homflypt_reference_qa.py` is the
first **external** anchor. Any future normalisation change must move that gate
toward 5/5, not just keep the four internal methods agreeing.

## 6. Empirical status

- **2026-06-04** SU(2) exponent fixed: `v = q^{N/2}` (was `q^{(N-1)/2}` →
  degenerate `δ≡−1`). Reference gate built. Rework engine
  `homfly_ocneanu_trace.py` landed (signed Ocneanu trace at `s`, writhe kept):
  gate **5/5** (PR #1792, merged).
- **2026-06-07** the engine independently confirms the merged GAP-A-4 Borromean
  result (§7).

## 7. Reconciliation with the GAP-A-4 Markov-trace thread (2026-06-07)

Main's `prop:borromean-markov-trace-closed-form` (PR #1933 T17 R-matrix, content
PR #1942) derives, via a *different* route (Schur-Weyl R-matrix on V^⊗3 → Jones
polynomial of 𝓑₃):

```
χ^{(3)}(β_Bor) = χ^{(1³)}(β_Bor) = 1
χ^{(2,1)}(β_Bor) = (−q¹²+3q¹⁰−3q⁸+4q⁶−3q⁴+3q²−1)/q⁶ = 2 − 3h⁴ − h⁶
tr_M(β_Bor)      = (4 + h² − 3h⁴ − h⁶)/(h² + 4)
```

`borromean_chi_independent_crosscheck.py` confirms the three **χ^λ** forms from
the skein-validated seminormal engine to **≤ 4e-50** at every tested q.

**Proof-status (do not overclaim).** This is *not* two independent proofs, and
the layers differ:
- The Borromean **tr_M closed form** IS Lean-proved (sorry-free) in
  `QOU/BraidsAndKnots/BorromeanMarkovTrace.lean` (`field_simp; ring` on the
  algebraic core, modulo the *cited* topological inputs `V(𝓑₃)`=Murasugi Jones
  poly and `tr_M=V/[2]²`).
- The **per-rep `χ^λ` forms** this cross-check verifies (`χ^{(3)}=χ^{(1³)}=1`,
  `χ^{(2,1)}=2−3h⁴−h⁶`) are **narrative-only** (content `.md`), *not* in that
  `.lean` — so the numerical confirmation here anchors a layer the Lean does
  not cover (corroboration, not a theorem of equivalence). Full status:
  `docs/audits/2026-06-07-borromean-chi-crossmethod-proof-status.md`.

**Do NOT equate the two weight families.** They share `χ^λ(β)` but use different
normalisations, and are *not* a constant multiple of each other:

| aspect | main's `y_λ` (Wenzl/Markov) | this engine's `w_λ` (Ocneanu/HOMFLY) |
|---|---|---|
| normalisation | `Σ_λ y_λ d_λ = tr_M(id) = 1` | unknot closure = 1, writhe kept |
| `tr_M(β_Bor)` form | `Σ y_λ χ^λ = (4+h²−3h⁴−h⁶)/(h²+4) ≈ 1` | `Σ w_λ χ^λ ≈ 4.0` (HOMFLY-closure norm) |
| `(3)` weight | `y_{(3)}(q=1) = 1/4` (universal H₃, T18) | `w_{(3)} = 0` |
| ratio engine/`tr_M` | — | q-dependent (4.0→6.6), **not constant** |

The interchange object between the two threads is **`χ^λ(β)`**, not the weights.
Equating `w_λ` with `y_λ` (or assuming a constant `[2]_q²` bridge) would
manufacture the very "third convention" this doc warns about (§1). When porting
results across the threads, port `χ^λ` and re-apply the destination's weight
normalisation.
