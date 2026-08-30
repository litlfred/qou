# Mining Molien: the correct q-analogue of `Σ (f^λ)² = n!`, and why `Z(n) ≠ 1`

**Date:** 2026-08-21
**Status:** RESULT — exact symbolic identity, verified `n = 2..7` in both conventions.
**Script:** [`scripts/molien_fake_degree_qanalogue.py`](scripts/molien_fake_degree_qanalogue.py)
(`ALL CHECKS PASS`, exit 0)
**Follows:** the Molien-series lead
[`2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md`](2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md)
— this closes that note's **open item 4** (which weight family the Molien weights land on).
**Companion to:** [`2026-06-20-keystone-wlambda-Z-defect-n-scaling.md`](2026-06-20-keystone-wlambda-Z-defect-n-scaling.md)
**Bean:** `qou-sf1t`

## Result

Mining the Molien-series machinery of Webster–Williamson §6 leads directly to the
coinvariant algebra, and from there to the identity the corpus was missing.

**In the corpus's own balanced convention** (`[m]_q = (q^m − q^{−m})/(q − q^{−1})`):

```text
  Σ_{λ ⊢ n}  f^λ · q^{−κ_λ} · d_q(λ)  =  [n]_q!
```

exact, verified symbolically for `n = 2..7`. Here `f^λ` is the **classical** number of
standard Young tableaux, `d_q(λ) = [n]_q!/∏_cells [h]_q` is the corpus's q-hook dimension,
and `κ_λ = Σ_{x ∈ λ} c(x) = n(λ′) − n(λ)` is the content statistic.

**In the standard convention** (`[m]_q = 1 + q + … + q^{m−1}`) the same statement is the
textbook one:

```text
  Σ_{λ ⊢ n}  f^λ · R_λ(q)  =  [n]_q!,        R_λ(q) = q^{n(λ)} · d_q(λ)
```

where `R_λ` is the **fake degree** — the graded multiplicity of `V_λ` in the coinvariant
algebra `ℂ[V]/(invariants)`, whose Poincaré polynomial is `∏_i [d_i]_q = [n]_q!` for
`W = S_n`. Verified alongside: `R_λ` has non-negative integer coefficients, `R_λ(1) = f^λ`,
and `κ_λ = n(λ′) − n(λ)`.

**And the corpus's object is not this.** `Σ_λ d_q(λ)² ≠ [n]_q!` in **both** conventions, at
every `n = 2..7`.

## What this explains

`Z(n) = Σ_λ d_q(λ)²/[n]_q!` was never going to be `1`, and now there is a reason rather
than an observation. The classical `Σ_λ (f^λ)² = n!` has **two** factors of `f^λ`. The
graded identity deforms exactly **one** of them — into the graded multiplicity `R_λ(q)` —
and leaves the other classical. The corpus's `Σ_λ d_q(λ)²` deforms **both** and squares,
with no content twist. That is a different object, and it agrees with the correct one only
at `q = 1`, where `R_λ(1) = f^λ` and `q^{−κ_λ} = 1`.

Which is exactly the observed behaviour: `Z(n) → 1` as `q → 1`, drifting away at `q ≠ 1`,
by a small amount, in **either** direction (the `n = 7` sign change) — because a
mis-specified deformation has no reason to err one way.

The script reproduces the companion note's table exactly at `q₀`
(`Z(3) = 0.987440`, `Z(4) = 0.982165`, `Z(5) = 0.982224`, `Z(7) = 1.012426`), confirming
the same object is under discussion.

## The twist is the `y_λ` / `w_λ(q)` separator

The balanced-convention twist is `q^{−κ_λ}`, and `κ_λ` is precisely the statistic the
notation register names when it says the Wenzl-bridge identity `y_λ = w_λ(q)` holds **on
the self-conjugate stratum only, where `κ_λ = 0`**. On that stratum `q^{−κ_λ} = 1` and the
twist is invisible; off it, it is exactly what the two families differ by.

So the content twist that repairs the normalisation identity and the content twist that
separates the two weight families are the same object. That is the substantive answer to
open item 4 of the lead note, and it did come out of the Molien route: the `q^{n(λ)}`
prefactor in the fake degree *is* the grading of the coinvariant algebra.

## Consistency with the 2026-08-16 owner ruling

This does **not** reopen the ruling; it sharpens it. The register holds that
`Σ_λ w_λ(q) ≠ 1` at `q ≠ 1` is by-design and that `w_λ(q)` is not a probability measure.
This note supplies the mechanism — `w_λ(q)` mis-deforms one factor — and, in the same
breath, the object that *does* normalise, so nothing is left dangling.

## Scope — what is and is not claimed

- **Not new mathematics.** The graded decomposition of the coinvariant algebra
  (Chevalley/Steinberg) and the fake degree are standard. The balanced-convention form is
  a transcription of it, derived here by chasing `[m]_q^{bal} = q^{1−m}[m]_{q²}^{std}` and
  `Σ_x h(x) = n(λ) + n(λ′) + n`, then verified.
- **What is new is the diagnosis** — that the corpus's `Σ d_q²` is the wrong q-analogue,
  and that this is the whole of the `Z(n)` defect.
- **Verification is `n = 2..7`.** The underlying identity is standard and holds for all
  `n`; the check here is finite and symbolic, not a proof in this corpus.
- **No physical claim, no fit, no wiring.** Nothing downstream is changed by this note. In
  particular it does **not** assert that any of `f^λ · q^{−κ_λ} · d_q(λ)`, `y_λ` or
  `w_λ(q)` is the right weight for a *physical* channel — only which one satisfies the
  normalisation identity.
- **The geometric-realization question stays open**, and stays owner-gated. Knowing the
  correct combinatorial identity does not supply the S¹-equivariant index; items 1–3 of
  the lead note (the `Tr_Γ` ↔ Jones–Ocneanu identification, the bigraded `(q,t)`
  specialisation, general type vs type A) are untouched.

## Next

The obvious Lean step, in the shape of the one already taken in
`QOU/MathlibExt/QPlancherel.lean`: state `Σ_λ f^λ · q^{−κ_λ} · d_q(λ) = [n]_q!` over a
`Finset` of partitions and prove it, which would give the module a **genuine**
normalisation theorem rather than the by-construction one it currently has. That is a
real theorem with real content, unlike `sum_measureOn_eq_one`, and it is the honest
successor to it.
