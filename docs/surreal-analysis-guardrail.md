# Surreal-analysis guardrail — licensed vs forbidden analytic → surreal moves

**Read this before moving any analytic argument into the surreal
appendix or proposing new surreal machinery.** Pattern follows
[`docs/canonical-mass-formula-guardrail.md`](canonical-mass-formula-guardrail.md):
this page exists because the failure mode recurs — agents propose
surreal integration, surreal spectral theory, or surreal limits in
generality that published mathematics either does not support or
provably forbids.

Companion review: [`docs/audits/2026-07-13-alien-calculus-surreal-integration-review.md`](audits/2026-07-13-alien-calculus-surreal-integration-review.md).
Standing scope ruling: the 2026-06-08 transcendental-surreal narrowing
ledger resolved **all** surreal narrowings as Language-tier — the
corpus carries no surreal-necessary claim. New work must not silently
re-inflate that.

## Licensed moves (published support; cite it)

| Move | Basis | Where it lives in-corpus |
|---|---|---|
| Evaluate a transseries / Hardy-field germ at `ω` or at a positive infinitesimal | Berarducci–Mantova (JEMS 2018, arXiv:1503.00315); ADH universal H-field (arXiv:1512.02267); hyperserial exp/log `E_{ω^α}`, `L_{ω^α}` (Bagayoko–van der Hoeven, arXiv:2310.14873) | `conj:kashaev-surreal`, `conj:surreal-limit-transfer` |
| Take `st` of a finite surreal; use `st` as a ring hom + order-preserving map | Robinson; proved sorry-free in `QOU/AppendixSurreals/StandardPart.lean` | `def:standard-part-functor` |
| Read `st` on median-summable transseries values as Écalle median resummation | Écalle; Watson/Nevanlinna–Sokal uniqueness (hypothesis half Lean-proved in `QOU.Mathlib.Borel*`) | `rem:st-is-median-resummation` |
| Replace Big-O/o/Θ/∼ comparisons by `ord_ω` valuation statements | Conway normal form | `def:conway-normal-form`, blow-up calculus |
| Renormalise a divergent quantity as `st(X(ω) − C(ω))` | blow-up calculus, sorry-free `Blowup(Calculus).lean` | `def:surreal-blowup-calculus` |
| Integrate a **semi-algebraic / analytic / transserial** function | Costin–Ehrlich–Friedman positive theory (arXiv:1505.02478, arXiv:2208.14331 / Adv. Math. 2024) via Hardy-germ routing | cited in `rem:analytic-obstructions` |
| Record `X ≈ Y` optionally as `X = Y + δ` with `ord_ω(δ)` | bookkeeping only (AGENTS.md §7ab extension) | §7ab |

## Forbidden or open (do not propose without new published input)

| Move | Why blocked |
|---|---|
| General surreal integration (Lebesgue-like, or any translation-invariant σ-additive integral on `C(No)`) | **Provably impossible** — CEF set-theoretic obstruction (NBG⁻). Only the transserial/Hardy-germ class integrates. |
| General surreal limits / topology (net convergence on all of `No`) | No canonical topology does the job; the corpus replaces limits piecewise by `st ∘ ev`. The compatibility package on the abstract interface is exactly `conj:surreal-limit-transfer` — **open**, do not assume it. |
| Surreal exp/log as if formalized | Berarducci–Mantova exp is not in Mathlib and not in the QOU tree; only class-level use is licensed. |
| Surreal hyperbolic geometry / `Vol` of a manifold as a surreal-native object | Not native to `No` (see `rem:analytic-obstructions` §3.2); volume stays an external ℝ-anchor. |
| Surreal Hilbert spaces, spectral theorem, functional calculus | Dodged by design in the appendix ("spans the algebraic direct limit"); no published surreal counterpart. |
| Claiming a surreal reformulation *closes* a magnitude-refuted route (e.g. the deuteron 37× transseries undershoot) | Representation changes cannot fix magnitudes; scope-(a) negatives are representation-independent. |
| Presenting `q` as a nontrivial Hahn series with predictive higher coefficients | Retired (`_deprecated/.../hahn-substrate.*`): the α_k are free parameters, not predictions. Only the language-level `q = 1 + ε` survives. |
| Using surreals to assert transcendence/irrationality progress (e.g. of Vol(4₁)) | The corpus's physics depends only on volume *distinctness*; irrationality of `2Cl₂(π/3)` is open in the literature and a surreal rewrite does not move it. |

## Litmus questions before authoring

1. Which **licensed row** does the move instantiate? If none, stop.
2. Is the function class transserial/Hardy-germ? If not, CEF likely
   forbids the integral/limit you want.
3. Does the claim survive with surreals deleted (Language-tier)? If it
   would silently become Essential-tier, get an owner ruling first.
4. Are you re-opening a refuted route (deuteron transseries,
   hahn-substrate, full higher-instanton tower)? Check the refuted-class
   map before proposing.
