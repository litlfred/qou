# Holomorphicity endowment (`qou-2cvs`) — scope correction + the meromorphic wall

**Date:** 2026-07-18
**Bean:** `qou-2cvs` (FaddeevPhi holomorphicity endowment; parent `qou-89f9`)
**Branch:** `claude/alien-calculus-habiro-50257v` (restarted from `main` after #3966 merged)
**Status:** SCOPING — a correction to the endowment framing + an honest report of
two converging walls. **No Lean verified here** (the relevant Mathlib API is
unavailable in this sandbox — see §3); nothing axiomatized.

## 1. Correction — "divisor cancellation" is OFF the critical path of the scaffold

Bean `qou-2cvs` framed the endowment as `hratio` (ratio `Ψ/Φ` entire), decomposing
into (i) `Φ_b` holomorphic + (ii) **divisor cancellation** (two solutions share
zeros/poles ⇒ ratio entire). Re-reading the merged reduction shows (ii) is not on
the critical path of the scaffold as written:

- `FaddeevRigidityReduction.uniqueUpToScalar_of_entire`
  (`FaddeevRigidityReduction.lean:51-57`) takes `hΦe`/`hΨe` (Φ, Ψ **entire**) and
  `hΦ0` (Φ **nowhere zero**) — and **no separate `hratio`**.
- Upstream `ratio_const_of_doublyPeriodic` (`DoublyPeriodicLiouville.lean:125`)
  **derives** the entire ratio from those: `hΨ.div hΦ hΦ0`. Entire ÷
  nowhere-zero-entire is entire, a one-liner (`Differentiable.div`).

So in the nowhere-zero-entire regime the scaffold assumes, **the ratio-entire
input is already free** — there is nothing to prove by "divisor cancellation."
The rigidity leg reduces to just the two *entireness* hypotheses plus the
already-closed `hspan` (`qou-ce54`) and the reducible `hibinv` (`qou-q95i`).

## 2. …but the idealization is unphysical, and THAT is where divisor cancellation lives

The catch: **no nowhere-zero entire `FaddeevPhi` solution exists.** The true `Φ_b`
is *meromorphic*, with zeros on the `b`-lattice (`FaddeevQuantumDilogarithm.phi_b_zero`)
and poles on the dual `1/b`-lattice (the `shift_binv` guard, class docstring). So:

- **Idealized regime** (nowhere-zero + entire): `uniqueUpToScalar` is provable
  modulo an *entireness field* on the class — but that field is **false** for
  `Φ_b`, so this regime does not describe the physical object. Adding the field
  would be an honest *idealization marker*, not a proof about `Φ_b`.
- **Physical regime** (true meromorphic `Φ_b`): rigidity must be **restated
  meromorphically** — drop `nowhere zero`, replace "entire ratio" with "the two
  solutions have the **same divisor**, so `Ψ/Φ` extends to an entire nowhere-zero
  function." The divisor equality is forced because `Φ, Ψ` solve the *same*
  first-order q-difference equations (same prefactor `P`), so at each point
  `ord(Φ) = ord(Ψ)`. This — not (i) — is the genuine content of `qou-2cvs`, and
  it is a **multi-week meromorphic-geometry formalization**.

**Net correction:** `qou-2cvs` is not "add a holomorphicity field + a hard divisor
lemma." It is one of:
- **(A) idealization route** — add an entireness field, `uniqueUpToScalar` closes
  trivially, but the result is explicitly about an *idealized* `Φ_b` (honest, cheap,
  low physical value); or
- **(B) meromorphic route** — reformulate the whole rigidity statement over
  `MeromorphicOn`/divisors and prove same-divisor from the shared q-difference
  equation (honest, hard, the real target).

## 3. The environmental wall (this sandbox)

Route (B) needs Mathlib's meromorphic API (`MeromorphicOn`, `meromorphicOrderAt`,
`MeromorphicOn.divisor`). In this container:

- the restored `lake-cache` supplies Mathlib **oleans only** (2962), **no source
  tree** (`.lake/packages/mathlib/Mathlib` has 0 `.lean` files);
- the `Meromorphic` oleans are **not in the cache** (the QOU library never imports
  them), and they cannot be built from source (source absent; the release server /
  `cache get` are network-blocked).

So **no Lean using the meromorphic API can be compiled or verified here.** Route
(B) must be attempted in a full-build environment (or after seeding the cache with
the Meromorphic dep cone). Attempting it blind — writing meromorphic Lean I cannot
compile — would violate the QA-is-agent-owned discipline (unverified) and risks
the anti-laundering line; I am not doing that.

## 4. Honest outcome + recommendation

- **Done (verified, merged in #3966):** `hspan` (`exists_period_basis`), the
  `hibinv` dense-extension core (`periodic_of_continuous_of_eqOn_dense`), and the
  reduction itself. The rigidity leg's *closeable-now* pieces are closed.
- **`qou-2cvs` re-scoped** to routes (A)/(B) above; the divisor-cancellation is
  the route-(B) core, genuinely multi-week, and **blocked in this sandbox** on the
  absent meromorphic API.
- **Recommendation:** do route (B) in a full-build session (Mathlib source +
  `lake exe cache get` available), starting from `MeromorphicOn.divisor` and the
  shared-q-difference-equation same-order lemma. Route (A) is available anytime as
  an explicitly-labelled idealization if a placeholder is wanted — but it proves
  nothing about the physical `Φ_b` and should not be mistaken for closing G3.

Nothing here is wired, fitted, or axiomatized; the `uniqueUpToScalar` hypothesis
remains open with no instance, exactly as before.
