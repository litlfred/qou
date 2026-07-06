# Markov-stabilization trace-level axis — formalize-first scope

**Date:** 2026-06-04
**Trigger:** PR #1841 (Option B) REFUTED the box-adding Bratteli induction
axis at the **algebra-tower** level for the H₃→H₄ jump. PR #1808's Option E
literature-import audit named **Markov stabilization at the trace level**
(Jones 1987; Orellana; Geck–Lambropoulou 1997) as the orthogonal lead.
This doc applies the **formalize-first probe discipline** (PR #1826) — state
the hypothesis class, find the structural invariant, let it narrow/kill the
probe **before** running a wide numerical scan.
**Sibling chain:** #1762 (roadmap) → #1816 (Option A data) → #1841 (Option B
refutation) → this (the next axis the refutation points to).
**Scope:** read-only scope + one cheap symbolic probe. No production change.

---

## §1. The hypothesis class

Production's `linking_weight_family_a(q) = (1/4)·Σ_{λ⊢4} dim_q(V_λ)
= (3q²+4+3q⁻²)/4 ≈ 2.53` is applied as a **global geometric multiplier**
for every atom (Option A confirmed: uniform 2.53 across A=1..4, vs the
per-block tr_M ≈ 1.065 for the proton). The open question: **what
trace-level structure forces the H₄ (partitions-of-4) count** when the
proton braid `𝓑₃` lives in H₃?

The Markov-stabilization hypothesis: the H₃→H₄ promotion is a **Markov
move** β ↦ β·σ₃^{±1} (B₃ ↪ B₄), under which the link closure — hence
its Jones invariant — is **unchanged**, and the Markov/Ocneanu trace
scales by the **stabilization parameter**.

The trace lives on the **Hecke algebra** H_n, so the scaling law is
stated in terms of the Hecke generator `g_n` (the image of the braid
generator under the quotient map `B_n → H_n`, `σ_i ↦ g_i`, where the
`g_i` satisfy the Hecke relation `(g_i − q)(g_i + q⁻¹) = 0`). For
`x ∈ H_n` embedded in H_{n+1}:

  tr_M(x·g_n)    = z   · tr_M(x)
  tr_M(x·g_n⁻¹)  = z'  · tr_M(x)

with (canonical, from
[`hecke/hecke_symbolic.py:46`](../../computations/hecke/hecke_symbolic.py)):

  z = 1 / (q^½ + q^{-½}) = 1 / [2]_{√q}.

Here `z'` is the stabilization parameter for the inverse generator;
at the substrate q₀ the parameter q is **real**, so `g_n⁻¹` is a real
linear combination of `g_n` and `1` (via the Hecke relation
`g_n⁻¹ = g_n − (q − q⁻¹)`) and `z'` is likewise real — there is no
complex conjugation involved at the archimedean evaluation. (`z' ≠ z`
in general; only the forward `z` is needed below, since the H₃→H₄
promotion adds one strand with a single positive generator.)

## §2. The structural invariant (formalize-first narrowing)

**Cheap structural fact, no scan needed:** evaluate z at the substrate q₀.

  q₀ ≈ 1.10998   ⇒   √q₀ ≈ 1.05356,   z = 1/(1.05356 + 0.94917) ≈ **0.4993**.

(Matches the cached `z_markov = 0.4993203…` in
[`inductive-atom-witness.json`](../../computations/inductive-atom-witness.json).)

**Direction obstruction.** z ≈ 0.4993 < 1, whereas the linking_weight
≈ 2.53 > 1. A single Markov stabilization β ↦ β·σ₃ **decreases** the trace
by ≈ ½. So:

> **No single Markov stabilization can produce the >1 linking_weight
> multiplier.** The naive "stabilization explains the jump" reading is
> structurally dead before any probe runs.

This is exactly the kind of cheap structural kill that the
formalize-first discipline targets: a one-parameter z-scaling with
z < 1 cannot be a >1 factor. **What survives** is a sharper question:

  Is `(1/4)·Σ_{λ⊢4} dim_q` a trace-level Markov object at all — e.g. the
  trace of a **central idempotent** / the **stabilized identity** 1_{H₄},
  rather than a stabilization of the proton braid?

Two refined candidates remain (and only these — the probe tests exactly
these, not a wide scan):

- **M1 — stabilized identity.** tr_M(1_{H₄}) = Σ_λ y_λ·χ^λ(1) = Σ_λ y_λ·f^λ
  (f^λ = ordinary dimension). Is this equal to, or a clean multiple of,
  `(1/4)Σ_{λ⊢4} dim_q`? Tests whether the linking_weight is the H₄
  trace of the identity rather than of any braid.
- **M2 — z-renormalised dimension sum.** Is `(1/4)Σ_{λ⊢4} dim_q` =
  `z^{-k}·(something H₃)` for a small integer k (the number of strands
  added, k=1)? I.e. does dividing out the stabilization factor land on
  an H₃ quantity? (z⁻¹ ≈ 2.003 — suggestively close to 2; tested exactly.)

## §3. The cheap probe (`markov_stab_trace_axis_probe.py`)

Pure `sympy`+`mpmath`, no Hecke construction beyond the symbolic z:

1. Confirm z(q₀) ≈ 0.4993 and the **direction obstruction** (z < 1 <
   linking_weight) — records the formalize-first kill as a witness fact.
2. **M1**: compute tr_M(1_{H₄}) = Σ_{λ⊢4} y_λ·f^λ at q₀ (y_λ from the
   canonical `y-lambda-at-q0.witness.json`, f^λ = hook-length dimension),
   compare to `(1/4)Σ_{λ⊢4} dim_q`. Verdict EXACT/NEAR/REFUTED.
3. **M2**: test `(1/4)Σ_{λ⊢4} dim_q · z^k` and `· z^{-k}` for k ∈ {1,2}
   against clean H₃ quantities (`(1/4)Σ_{λ⊢3} dim_q`, `[4]_q`, `[3]_q`,
   etc.); report any exact rational/`[n]_q` coincidence symbolically.
4. Emit `markov-stab-trace-axis-probe.witness.json` with the
   direction-obstruction fact + M1/M2 verdicts + `discipline: EXPLORATORY`,
   `production_wired: false`.

**Honest expected outcome.** The direction obstruction already kills the
naive form; M1 is the live candidate (the linking_weight as the H₄
identity-trace). If M1 lands, the H₃→H₄ jump is **derived** as "evaluate
the identity in H₄, not the proton braid in H₃". If M1 and M2 both refute,
the trace-level Markov axis is also dead, and the jump's origin is neither
tower-induction (#1841) nor trace-stabilization — pointing back to the
production code's own provenance (the linking_weight may be a CODATA-implied
near-match, per `_li_2_q_util.py:298-313`, not a derived categorical count).

## §4. Discipline

- **EXPLORATORY** — no production code, content blocks, or witnesses touched.
- **Formalize-first** (PR #1826): the z<1 obstruction is the structural
  invariant that pre-narrows the probe from "scan all trace constructions"
  to "test exactly M1 + M2".
- **No Δ_λ-gate ansatz** — M1/M2 are structural identities (trace of a
  known element), not per-partition fits.
- **No 7th ansatz** — this is a derivation attempt for an existing
  production constant, not a new binding-energy closure.
