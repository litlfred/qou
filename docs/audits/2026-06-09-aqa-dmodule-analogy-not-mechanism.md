# AQA / D-module formalism — analogy, **not** mechanism

**Date:** 2026-06-09
**Status:** audit / standing-guard note (mirrors the §7b KLR-dialog audit
precedent, [`docs/audits/2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md))
**Trigger:** owner question — "how does substrate-as-adeles connect to surreals?
algebraic quantum analysis?" — plus a recollection of an "algebraic formalism of
analysis" thread that "should be in the paper somewhere."

---

## TL;DR

The paper **already has** an algebraic formalism of analysis. It is the
**surreal / ordered-field calculus**, not Sato–Kashiwara *algebraic analysis*
(D-modules, microlocal analysis, hyperfunctions). The two share a slogan
("replace analysis with algebra") and nothing load-bearing. Sato-school
algebraic analysis is a worthwhile **analogy** and citation target; it is **not
a wired mechanism** and should not be re-pitched as one (e.g. as a Δ_λ closure,
a compute speed-up, or a mass-formula ingredient). This matches the standing
surreal verdict: *keep surreals as the narrowing language — nothing
load-bearing*
([`docs/coordination/2026-06-08-transcendental-surreal-narrowing-ledger.md`](../coordination/2026-06-08-transcendental-surreal-narrowing-ledger.md)).

---

## Where the paper's "algebraic formalism of analysis" actually lives

All on `main` (PR #1995, `80ecc852`):

| Block / file | The claim |
|---|---|
| [`appendix-surreals/surreal-rate-calculus.md`](../../content/quantum-observable-universe/appendix-surreals/surreal-rate-calculus.md) | *"the algebraic content that replaces the informal '$O(\varepsilon^{-1})$ exceeds $O(\varepsilon^3)$ as $\varepsilon\to 0$': we do not need a limit, only an inequality inside $\mathbf{No}$."* |
| [`appendix-surreals/calculus-up-to-epsilon.md`](../../content/quantum-observable-universe/appendix-surreals/calculus-up-to-epsilon.md) | Which classical analysis survives the surreal substitution: Jackson $q$-derivative for $d/dx$, formal power series exactly, limits → evaluation + standard part; Hilbert completion / Lebesgue measure do **not** survive. |
| [`appendix-surreals-archimedean/algebraic-core-survives.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/algebraic-core-survives.md) | The mass-formula core (Hoefsmit → Markov trace → Jones) is **field-polymorphic** — runs identically over $\mathbf{No}$; analysis enters only at the final standard-part comparison to measured reals. |
| [`stochastic-mechanics/reeb-epsilon.md`](../../content/quantum-observable-universe/stochastic-mechanics/reeb-epsilon.md) / [`quantum-observable-universes/categorical-reeb-derivation.md`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-reeb-derivation.md) | $\varepsilon \in \mathrm{Der}(A)$ as the categorical primitive (derivation), $q = 1 + \varepsilon$ derived — the derivative is a **derivation-algebra**, not a limit of difference quotients. |

**One-line characterisation:** the paper's algebraic-analysis substitute is
**`standard-part ∘ evaluation-at-$q=1+\varepsilon$`**, with `Der(A)` for the
derivative and ordered-field inequalities in $\mathbf{No}$ for asymptotic
("squeeze") arguments. New this session: the *adelic* refinement
[`prop:adelic-reeb-restricted-product`](../../content/quantum-observable-universe/stochastic-mechanics/adelic-reeb-restricted-product.md)
(the $\omega$-order is additive over places; local squeezes lift to a global
squeeze — Tate-factorisation in the surreal register).

---

## AQA / D-module ↔ QOU surreal-$\varepsilon$ dictionary (analogy only)

| Sato–Kashiwara algebraic analysis | QOU surreal-$\varepsilon$ formalism | Load-bearing? |
|---|---|---|
| Replace functions/limits with algebraic objects (sheaves of solutions) | Replace limits with evaluation + standard part in $\mathbf{No}$ | **n/a** (parallel slogans) |
| Ring of differential operators $\mathcal{D}$; D-module = module over $\mathcal{D}$ | Derivation $\varepsilon \in \mathrm{Der}(A)$; substrate as $\varepsilon$-module | analogy |
| Microlocal / characteristic variety; order filtration on $\mathcal{D}$ | $\omega$-order `ordw` / birthday filtration on $\mathbf{No}$; per-place orders | analogy |
| Holonomic D-module; $b$-function (Bernstein–Sato) | (no current counterpart) | — |
| Riemann–Hilbert correspondence (regular holonomic ↔ perverse sheaves) | (no current counterpart) | — |
| Adelic / $p$-adic D-modules, arithmetic $\mathcal{D}$-modules | Adelic restricted product of local $\varepsilon_v$ (`prop:adelic-reeb-restricted-product`) | the QOU side is real; the *identification* with arithmetic $\mathcal{D}$-modules is **not** made |

The **right** column is real, formalised content. The **left** column is a
literature analogy: it suggests vocabulary (filtration, microlocal, derivation)
and possible citations, but no QOU result is proved *through* a D-module or a
holonomicity/Bernstein–Sato argument.

---

## Verdict (standing guard)

1. **Do not** re-pitch Sato-school algebraic analysis (D-modules, microlocal,
   hyperfunctions, $b$-functions, Riemann–Hilbert) as a *mechanism* — a Δ_λ
   closure, a compute speed-up, a mass/binding ingredient, or a substrate
   derivation of $q_0$. The paper's algebraic-analysis layer is already the
   surreal-$\varepsilon$ calculus; adding a D-module layer buys no proved result
   today.
2. **Do** treat it as an analogy / citation target if a future block genuinely
   needs the vocabulary (e.g. if the $\omega$-order filtration is ever compared
   to a characteristic-variety order, cite the analogy explicitly and keep it in
   a `remark`, not a `proposition`).
3. The honest status mirrors §7b's KLR/crystal verdict and the surreal
   narrowing ledger: **expressive language, not load-bearing.** Any agent
   arriving with "we can use D-modules / algebraic analysis to derive X" should
   read this note first and the surreal ledger second before spending compute.

**Cross-refs:** the corpus-grep / formalize-first disciplines (AGENTS.md) apply —
the productive home for any such idea is the existing surreal-calculus blocks
above, extended by `prop:adelic-reeb-restricted-product`, not a new mechanism.
