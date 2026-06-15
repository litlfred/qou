# Δ_λ: toward the q₀^5-per-chain-site mechanism (starting notes, 2026-06-15)

**Status:** started, NOT landed — the deep keystone. Follow-on to the merged
crossing/second-kind derivation (PR #2311; audit
`2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md`). Bean: `qb5s`
(record the quintic/EW interpretation) + this (the mechanism).

## The well-posed question

The Δ_λ q₀-exponent is `5·(2A−1) = 5 × (A nucleons + A−1 bonds)` = **5 per
chain-site**, with `5 =` the Bring-quintic degree (`𝒳₅`). The lone remaining
keystone: **why does each chain-site contribute exactly `q₀^5`?**

## The mechanism it must come from (identified)

`Δ_λ(K) = B_AME / B_pred`, and (`binding_canonical.py`)

    B_pred(Z,N) = E_0 · ( tr_M(W_free) − tr_M(W_atom) )

is the **linear** trace difference. Per the linear-truncation diagnosis
(`docs/audits/2026-05-28-binding-endomorphism-analogy.md` §"linear-truncation
diagnosis"; `kashaev-as-archimedean-realization.md`): `tr_M ~ exp(Vol)`
(Kashaev), so the scalar `Δtr` is the **linearization**, and `Δ_λ` is the
**exp-vs-linear gap**. So `q₀^(5·sites)` is the *per-site* exp/linear correction.

The carrier is the **q-Reeb phase** `θ = arccos(χ_(2,1)/2)` — the same forced
eigenphase as `QOU.BraidKnot.eigenphase_forced` (proved in
`HoefsmitV21CosSymmetrization.lean`, this session). For `|tr_M| < 2` (elliptic),
real-q gives `Vol ≈ 0`; a genuine hyperbolic volume — hence a nonzero exp/linear
gap — requires **complex-q** (Kashaev rotation, `binding_reeb_phase_decomposition.py`).

## Working hypothesis + why it's hard

Per chain-site, the full (exp) binding exceeds the linear `Δtr` by `q₀^5`. Two
sub-questions, both genuinely open:
1. **Why exponential in the site count** (`q₀^(5·sites)`) rather than polynomial?
   — the Kashaev `exp(Vol)` structure must promote the per-site `Δθ` (q-Reeb
   phase shift, polynomial `~ η₀²`) into an exponential `exp(c·η₀)` gap. Needs
   the complex-q volume, not the real-q `Vol ≈ 0` degenerate case.
2. **Why the coefficient is exactly 5 (= quintic degree)** per site — the
   per-site q-power must equal the Bring quintic degree; candidate routes: the
   quintic's `g² = 5` Gauss sum, or `|χ(Bring)| − 1 = 6 − 1 = 5`, or the
   degree-5 cover. Same `5,7` odd integers as the EW Weinberg `cosh(5η₀)/cosh(7η₀)`.

This is the framework's standing **complex-q / Kashaev** open item; it is not a
session-sized chip. Recorded so the next pass starts from the mechanism, not the
observation.
