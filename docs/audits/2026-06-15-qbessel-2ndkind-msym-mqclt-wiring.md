# q-Bessel-2nd-kind corrections to m_sym / m_qCLT — what wired, what stayed gated (2026-06-15)

**Branch:** `claude/vigilant-brown-x0tzat` (PR #2325)
**Scope:** wire the gate-respecting (derived, no-fit) pieces; record the blockers.
**Discipline:** [`production-vs-exploratory-discipline`](../../.claude/skills/local/production-vs-exploratory-discipline.md)
+ CLAUDE.md §"Δ_λ gate" (no 7th ansatz).

## The owner question, answered

*"Recent q-Bessel-2nd-kind work might provide needed corrections to `m_sym` and
`m_qCLT` — wire all we can; what are blockers?"*

The 2nd-kind q-Lommel **order** recurrence supplies a `b = q₀¹⁰+q₀⁻¹⁰ =
2cosh(10η₀)` (Lean `QOU.QBeta.two_root_geometric`). Tracing it to the two binding
channels gives an asymmetric answer:

| channel | binding form | does the 2nd-kind correction apply? |
|---|---|---|
| `m_qCLT` | linear `B_lin = α·s` (the JSJ-additive estimator) | **YES** — the `Δ_λ^lin` ladder carries the geometric `r = q₀¹⁰` signature (item 3) |
| `m_sym` | exact log-trace `B_sym = α·ln(tr_free/tr_atom)` | **NO** — `B_sym` (Kashaev `tr ~ exp(Vol)`) **already realizes** the exponential; `Δ_λ^sym ≈ 1` on A=3 |

So the "correction to m_sym and m_qCLT" is really **one** correction (the 2nd-kind
exponential) that the m_sym channel **already contains** and the m_qCLT (linear)
channel still needs. Applying it on top of `B_sym` would double-count.

## What wired (item 1 — canonical infrastructure, derived inputs)

[`m_qclt_approx.py`](../../computations/m_qclt_approx.py) now
carries a **self-contained derived binding** — the factorized q-CLT

  `B_qCLT_fac(Z,N) = E₀·(A−1)·(Σ_type n_type·L_type)/C(A,2)`,
  `E₀ = m_e/(q₀(q₀−1))` derived (q₀, m_e only — no fit),
  `L_type` = 2-nucleon sub-braid log-traces (p-p 0.6945 / p-n 0.9292 / n-n 1.2370,
  recorded canonical, source `scriptCommitSha` pinned).

It **resolves the T/³He isospin split** (L_nn > L_pp ⇒ T more bound; B_fac
T=8.638 / ³He=7.124 vs B_AME 8.48/7.72) within **1.08×**, no fit — which the
isospin-blind leading term `Z·m_p+N·m_n` cannot. Witness
`m-qclt-approx.witness.json`, **6 assertions green** (2 new: split-resolution +
within-1.25×). This is canonical infrastructure (derived), **not** a production
observable promotion.

## What it disambiguated (item 3 — exploratory probe)

[`qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py`](../../computations/qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py)
(witness `qlommel-delta-lambda-lin-vs-sym-ladder.witness.json`, 3 green) tests
which ladder the 2nd-kind `b` governs, on the recorded `Δ_λ^lin` / `Δ_λ^sym`:

| ladder | `Δ(T)/Δ(D)` vs `r=q₀¹⁰=2.839` | verdict |
|---|---|---|
| `Δ_λ^lin` (linear binding) | 2.607 (**−8.2%**) | geometric — carries the first-kind branch |
| `Δ_λ^sym` (log-trace binding) | 1.635 (**−42.4%**) | **flat / non-geometric** — B_sym spent it |

Log-trace absorption `Δ_λ^lin/Δ_λ^sym` at A=3: T 2.45×, ³He 2.02× — i.e. `B_sym`
already absorbs ~2–2.5× of the exp-vs-linear gap. **Honesty note:** the
single-interior-point recurrence-`b` test is data-limited and ⁴He-magic-
contaminated (it gives sym `b_emp`=3.139 vs lin 3.516, misleadingly favouring
sym), so it is **reported, not used as the discriminator** — the clean
A=2→3 geometric ratio is.

## Blockers (production observable layer stays gated)

1. **Nucleon-mass gap +2.89 %** (Subgoal-2, owner-declined 2026-05-08) — caps
   absolute accuracy of any mass channel; the derived spectral θ/(8ℏ²) closes it
   ~35× but is itself a vacuous-`True` Lean stub (workplan P1).
2. **Δ_λ exponent keystone open** — `10A−5 = 5(2A−1)` not yet derived from Bring
   crossings (#2316 merged with the keystone *explicitly open*); a closed Δ_λ now
   would be the forbidden 7th fit-ansatz.
3. **Bond-graph modeling choice** — chain-(A−1) vs all-pairs-C(A,2) not derived;
   A≥4 undershoots ~1.6×.
4. **Lean env down in sandbox** (`release.lean-lang.org` firewalled) — did not
   block items 1/3 (Python + recorded-witness only).

## Net

The 2nd-kind correction is **needed for m_qCLT (linear)** and **already realized
by m_sym (log-trace)**. The derived factorized binding is wired into the m_qCLT
*infrastructure* channel (resolving T/³He). Nothing reaches the production
observable dashboards — blockers 1–2 are the gate, and they are framework-level,
not session-sized.
