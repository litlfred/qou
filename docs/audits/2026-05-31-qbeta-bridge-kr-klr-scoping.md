# Q_β bridge — KR/KLR route scoping (2026-05-31)

> **Purpose.** Scope what closing the open Q_β bridge `f` would actually
> require if attempted via the **Khovanov–Rozansky (KR) / KLR-canonical-
> basis** route. Companion to
> [`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md)
> (which ruled out 6 other mechanisms). This doc does **not** attempt
> the derivation — it maps what an attempt would have to produce, why
> the priors are skeptical, and what (if any) cheap intermediate
> experiments are worth running before committing to multi-week work.

## The open target (recap)

Find a substrate-canonical `f` such that

    Q_β = m_e · f( Δtr_M(q), q )   is Taylor-exact at canonical q₀.

`Δtr_M(q) = tr_M(β_n) − tr_M(β_p)` is the exact Habiro multi-block
Markov-trace difference; it's a rational function of `q` with leading
Taylor order `−5/4 · ε` (where `ε = q − 1`). Form A's net-winding slot
`Δ(net)_A = h(h−2)/2` has leading Taylor order `−2 · ε`. **The two are
structurally distinct** (item-1 finding); the bridge is not "Δ(net)_A →
Δtr_M" substitution. It is something else.

## What the KR/KLR route would produce

The Khovanov–Rozansky homology `KR(L, q)` of a link `L` decategorifies
to the HOMFLY-PT polynomial; the Markov trace `tr_M(β, q)` of a closed
braid `β` is its q=1 specialisation along the HOMFLY-PT chain. The KLR
canonical basis of `H_n(q)` gives a per-Wedderburn-block decomposition
of `tr_M(β)` that's **finer** than the dim_q² weighting (which was
falsified at c_3, mechanism #5 of the narrowing doc).

For Q_β specifically, KR/KLR would have to produce a closed-form
expression `f(Δtr_M, q)` such that:

1. **At Taylor order ε¹:** `(∂f/∂Δtr_M)|_{q=1} · (−5/4) +
   (∂f/∂q)|_{q=1} = c_1^Q_β`, the leading Q_β-ladder coefficient.
   (`c_1 = b` is already known, Kashiwara f̃₁.)
2. **At Taylor order ε^k for k ≥ 2:** the chain
   `c_k^Q_β = polynomial in {Taylor coeffs of f, Δtr_M, b, ℏ_q, …}` reproduces
   the empirically-extracted c_k at every order (currently c_3 ≈ −2.0693,
   then convergent below compute precision).
3. **q₀-independence:** the same `f` works at the muon-pin q₀ and the
   m_p-pin q₀; the q₀-sensitivity that killed mechanisms 1–6 must not
   resurface here.

Requirement 3 is the discriminating test. Any candidate `f` whose
Taylor coefficients drift with q₀ is the same failure mode the
narrowing-doc mechanisms hit.

## Why the prior is skeptical (AGENTS.md §7b precedent)

The 2026-05-30 audit
[`2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md)
assessed six candidate proofs against a KLR layer and found **0/6
would meaningfully shorten** with KLR machinery added. Recurrent
failure modes flagged there:

- **Mass-formula mis-framing** — re-introducing the purged `λ_scale`.
  Do NOT.
- **Bloch–Wigner / dilog-transcendence on the trefoil** — non-hyperbolic
  knot, `D(z) = 0`, the argument fails algebraically.
- **Positivity-by-construction over-claim** — KLR gives `dim Hom ≥ 0`
  for graded modules; Q_β's residuals are archimedean bounds on real
  `q > 0`, not categorical positivity.

A KR/KLR Q_β attempt would have to evade all three. Per §7b ("authoring
guidance, not proof-restructure triggers") the standing repo policy is
to use KLR techniques as algorithmic shortcuts where the categorical
content is already aligned, **not** as a structural-derivation
generator. The audit precedent says: don't expect KLR to produce
`f` from first principles.

## Cheap intermediate experiments (before any multi-week commitment)

If the bridge is going to be attempted, the following 1–2 day
experiments would either rule the KR/KLR route OUT (saving 2–4 weeks
of work) or give it enough traction to commit:

| # | experiment | cost | what passing means | what failing means |
|---|------------|------|---------------------|---------------------|
| 1 | Compute `tr_M(β_n) − tr_M(β_p)` per Wedderburn block (already done in `qbeta_per_block_paper_closed_forms.py`); check whether the **per-block ratio** `χ_λ(β_n − β_p) / Δtr_M` has a `λ`-independent leading-order asymptotic at `q = 1` | ½ day | weak signal a `f(Δtr_M, q)` exists at all in a per-block-friendly form | per-block weights deviate at LO ⟹ no per-block path; reinforces narrowing-doc verdict |
| 2 | Test whether the **Habiro element** of the closed-form fundamental-rep `tr_M(β_n − β_p)` (treating the difference as a virtual link) admits a KR-homological decategorification matching the c_k Taylor coefficients | 1–2 days | candidate `f` identified; commit to multi-week refinement | empirical c_k don't match → KR route ruled out the way mechanisms 1–6 were |
| 3 | Test the `c_3 → trivial + sign block` LO hypothesis (per [`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md) "established structural fact #4": c_3 ≈ −2 matches the (3) & (1,1,1) blocks' LO −2, NOT the (2,1) block's LO −1) — does a multi-block eigenphase `cos(Σ_λ α_λ)` with `α_λ` drawn from KLR-canonical-basis weights close the gap? | 1 day | the multi-block eigenphase is the bridge | drift between q₀ pins → form-fitting again |

Experiment 3 is the cheapest decisive test and is the most direct
follow-on from item-1 (the eigenphase has the right direction; the
question is whether multi-block weights make it Taylor-exact).

## What this doc is NOT

- Not an attempted derivation. The KR/KLR commit is multi-week; this is
  scoping only.
- Not a recommendation to proceed. Per §7b precedent, the priors are
  unfavourable. Experiment #3 is cheap enough to run pre-commitment.
- Not a hidden re-pitch of `λ_scale`, Bloch–Wigner on the trefoil, or
  positivity-by-construction. Those are recurrent failure modes the §7b
  audit catches; this scope explicitly does NOT touch them.

## Recommendation

**Don't commit to the multi-week route.** Run experiment #3
(multi-block eigenphase, ~1 day) as the decisive cheap test. If it
fails (q₀-drift between pins), the KR/KLR route is ruled out by the
same q₀-sensitivity criterion that killed mechanisms 1–6. If it passes
(stable across pins, Taylor-exact at canonical q₀), commit to the
multi-week formalisation.

Honest production stays at Q_N2 = 1277 ppb (the μ-p substrate floor)
either way. The bridge is the genuine open derivation target; this doc
maps what closing would require, not a closure.
