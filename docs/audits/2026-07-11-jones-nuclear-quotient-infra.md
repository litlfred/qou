# Jones nuclear-quotient infra — the RHS of the open Part-4 conjecture

**Date:** 2026-07-11 · **Axis:** `conj:jet-filtered-knot-factor` Part-4 (OPEN) ·
**Tier:** infra (RHS construction; symbolic-exact closed forms) ·
**No fit; nothing wired to production; does NOT close the conjecture.**

## What this builds (and what it does not)

`conj:jet-filtered-knot-factor` has Parts 1–3 established (the q-Plancherel
per-level invariant `a_k`) and **Part 4 open**: the Bethe–Weizsäcker knot factor
`a(Z,N)` is conjectured to equal the Jones polynomial `J_β̄(q)` of the **nuclear
quotient braid** `β̄` (each nucleon → one effective inter-nucleon crossing;
tracking the `A(A−1)/2` inter-nucleon crossings). The `.md` maps the quotient
knot type by shell structure: **odd `Z` → trefoil, even `Z` → Hopf, double-magic
→ unknot.**

This adds the Lean infrastructure for the **right-hand side** `jonesQuotient` —
the object the conjecture identifies with `a(Z,N)`:

- [`QOU/BraidKnot/JonesNuclearQuotient.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/JonesNuclearQuotient.lean):
  the three `(2,k)` torus-link Jones values (`jonesUnknot` = `z`, `jonesHopfLink`
  = `h·z+1`, `jonesTrefoil` = `(h²+1)·z+h`), the shell-structure classifier
  `nuclearCrossingPower : ℕ → ℕ → ℕ` (→ `{1,2,3}`), the assembled
  `nuclearQuotientJones`, and structural lemmas: `nuclearCrossingPower_mem`,
  the three selection lemmas (`_doubleMagic` / `_evenZ` / `_oddZ`), and
  positivity in the Wenzl regime (`nuclearQuotientJones_pos`).

Per AGENTS.md §"Axiomatization is NOT a Proof": **constructing the RHS is
infrastructure, not closure.** It does **not** prove `a(Z,N) = jonesQuotient`
(`jet_filtered_knot_factor.factor_is_jones` stays the open §3b conjecture) and
unlocks **no** downstream binding compute.

## The `(2,k)` torus-link Jones values (compute-verified)

In `H_2(q)` with `σ² = h·σ + 1` (`h = q − q⁻¹`, §7a), `σ^k = a_k·σ + b_k`
(`(a_0,b_0)=(0,1)`, `(a_{k+1},b_{k+1})=(h·a_k+b_k, a_k)`), and
`tr_M(σ^k) = a_k·z + b_k` with the canonical Markov parameter
`z = 1/(√q + 1/√q)`:

| link | `k` | `tr_M(σ₁^k)` | Lean def |
|------|-----|--------------|----------|
| unknot  `(2,1)` | 1 | `z` | `jonesUnknot` |
| Hopf    `(2,2)` | 2 | `h·z + 1` | `jonesHopfLink` |
| trefoil `(2,3)` | 3 | `(h²+1)·z + h` | `jonesTrefoil` |

**Cross-check** ([`nuclear_quotient_jones_torus_link_probe.py`](../../computations/deltalambda/nuclear_quotient_jones_torus_link_probe.py)
→ witness, 4/4 PASS): the `k=2` value `h·z + 1` **equals** the already-formalised
& verified `JonesViaMarkovTrace.jonesHopf` closed form
`(q^{5/2}−q^{1/2}+q²+q)/(q²+q)` — the difference simplifies to `0` in sympy. This
pins the recursion into the framework's Markov normalisation, so the unknot and
trefoil forms are in the same normalisation, **not** invented. Numeric sanity at
`q=4`: `0.4 / 2.5 / 9.775`.

The formal `rpow`-normalisation bridge lemma `jonesTorusLink 2 = jonesHopf` (the
Lean statement of the sympy `Δ=0` identity) is **deferred** — the
`Real.sqrt`↔`rpow` rewriting is fiddly and this session cannot run the LSP (see
below).

## Verification status (STRICT — not machine-validated this session)

The Lean is **hand-audited, not machine-checked**: the Lean toolchain
(`leanprover/lean4` v4.24.0) is firewalled this session — `release.lean-lang.org`
and the GitHub `releases/download/` path both return 403, and the toolchain
binary is not git-cloneable / not vendored in a qou branch (the olean cache
branch is fetchable, but inert without the compiler). `git clone` of github.com
*repos* works, but the compiler is a release asset, not a repo. The proofs use
only elementary tactics (`split`, `if_pos`/`if_neg`, `mul_pos`, `linarith`,
`positivity`, `simp` on literal-Nat `ite`), each hand-audited against Mathlib
v4.24.0. **CI `lean_ci.yml` is the confirming gate.** Unblock for machine
verification: whitelist `release.lean-lang.org` (or the github releases path), or
vendor the v4.24.0 linux toolchain into a `litlfred/qou` git branch (git-fetchable
like `lake-cache/qou-v4-24-0`).

## Next step

The open Part-4 test is now concrete: compare `nuclearQuotientJones q Z N`
(this RHS) against the Bethe–Weizsäcker `a(Z,N)` at the substrate `q₀`, per
nucleus — a compute task needing the full evaluation-at-`q₀` + scale machinery.
Note the 2026-07-05 Δ_λ gate-status finding that the Jones trace of `β_K` *alone*
is insufficient for binding *magnitude* (needs the `W_λ` knot-ideal projector);
whether that constrains the *bulk* `a(Z,N)` identification (a different object) is
the open question this infra lets a stack-equipped session probe.
