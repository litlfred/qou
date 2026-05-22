# Agent brief — `λ_scale` from q-dilog tower direct parametrisation

> **Audience.** A future agent picking up the CAL-4 closure work
> for the Borromean baryon mass formula. The Bring-Bloch path has
> been exhausted (6-tier consistent negative); this brief sets up
> the **q-dilog tower direct parametrisation** as the alternative.
>
> **Status when this brief was written (2026-05-22).** `λ_scale` is
> a hardcoded literal in production. Migration Backlog #1 per
> [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md).

## TL;DR

Find a closed-form expression for `λ_scale ≈ 2.4599527869` (proton
closure target for the Borromean baryon mass formula) using the
q-dilog tower at `q = q_0` directly, **bypassing the Bring-Bloch
hyperbolic-volume search** which the 6-tier consistent negative has
ruled out for the proton's Bring-decomposition class.

## Background — what is `λ_scale` and why does it matter

The **Borromean baryon mass formula**
([`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)):

$$
\mathfrak{m}(B) = m_e \cdot \left[\frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \lambda_{\mathrm{scale}} + S(B)\right]
$$

- `m_e` (CAL-1) and `q_0` (CAL-2 via `m_μ/m_e`) are the only
  calibration inputs.
- `Vol(𝓑₃) = 8G ≈ 7.32772...` is a fixed topological invariant
  (Catalan's constant identity per
  [`prop:borromean-vol-8G`](../../content/quantum-observable-universe/braids-and-knots/)).
- `ℏ_q = (q-1)/q` is the q-deformed Planck constant; at `q_0`
  this gives `Vol(𝓑₃)/ℏ_q² ≈ 746.4`.
- `S(B)` is the Skein-orientation correction (different for proton
  vs neutron); structurally derivable.
- **`λ_scale` is currently hardcoded:** `LAMBDA_PROTON_DOC =
  mp.mpf("2.4599527869")` in
  [`folio-assistant/computations/m_p_borromean_verification_50dps.py:100`](../../folio-assistant/computations/m_p_borromean_verification_50dps.py).
  It was solved against CODATA `m_p` (a CAL-4 violation in
  disguise; see
  [`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](../audits/2026-05-18-210x-scale-gap-root-cause-v2.md)).
  Closing `λ_scale` in closed form would resolve the only known
  CAL-4 violation in the production mass pipeline.

## Why Bring-Bloch is exhausted

Per [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md),
the conjecture was `λ_scale = (1/8G) · D(Σ_i n_i^(p) [Z_K_i])` where
`D` is the Bloch-Wigner dilogarithm and `n_i^(p)` is an integer
multiset over hyperbolic-knot Bring-decomposition classes. The
search for this multiset via PSLQ has been run at 6 tiers:

| Tier | Basis | PSLQ tol | maxcoeff | Result |
|---|---:|---:|---:|---|
| 0 | 8 (Atlas) | — | 10³⁰ at 80 dps | NULL |
| 1 | 11 (Birman–Hilden 3-braid) | 1e-15 | 10⁸ at 100 dps | NULL |
| 2 | 16 (+ bridge-3) | 1e-12 | 10⁶ | NULL |
| 3 | 33 (+ 9-cross primes) | 1e-12 | 10⁵ | NULL |
| 4 | 40 (+ 10-cross primes) | 1e-12 | 10⁵ | NULL |
| 5 | 52 (+ 11-cross primes) | 1e-10 | 10⁵ | NULL |

52 hyperbolic-knot volumes searched, brackets the target `Vol(K_p^eff)
≈ 18.026` from below and above. The proton's Bring-decomposition is
**not** a ℤ-linear combination of prime hyperbolic-knot volumes
≤ 11 crossings.

Tier-search scripts:
[`folio-assistant/computations/bring_bloch_tier{1..5}_search_m_p.py`](../../folio-assistant/computations/).

## What "q-dilog tower direct parametrisation" means

Two q-dilogarithms are used in the framework
([`docs/canonical-derivation-cheat-sheet.md §4`](../canonical-derivation-cheat-sheet.md)):

| | Φ_q (Faddeev) | Li_2^q (Rogers) |
|---|---|---|
| Bar-symmetry | NOT (mass-anchor, asymmetric) | YES (binding, bar-symmetric) |
| Context | MASS | BINDING |
| Reference | [faddeev1996] | [kashaev1995] / [kirillov1995] |

**The hypothesis to test:** at the substrate point `q_0`, the
proton's `λ_scale` should be expressible as a **closed-form
combination of values of one of the two q-dilogarithms evaluated at
algebraic points in `ℚ(q_0)`** — bypassing the hyperbolic-volume
detour entirely. Candidate forms:

1. **Rogers-only** (bar-symmetric, binding-side): `λ_scale = α ·
   Li_2^q(z_1) + β · Li_2^q(z_2) + ...` for integer `α, β, ...`
   and `z_i ∈ ℚ(q_0)`.
2. **Faddeev-only** (bar-asymmetric, mass-side): `λ_scale = α ·
   Φ_q(w_1) + β · Φ_q(w_2) + ...` similar form.
3. **Mixed via the three-layer synthesis** (post-Phase 5b, PR #819):
   `Li_2^q ↔ cos_q(h) ↔ cosh(h)` — three avatars of the same
   bar-symmetric kernel at series / phase / closed-form levels.
   So `λ_scale` may admit a `cosh(h)` closed form via the
   `cosh ↔ Li_2^q` ladder.
4. **Kashaev-style integration identity** — Φ_q satisfies an
   integration identity that produces algebraic numbers when
   integrated against specific contours; check if the proton
   value emerges from such an integral at q_0.

## What's already known structurally

From [`prop:lambda-scale-bring-bloch-identity §Open work`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md):

> Three tasks remain:
> 1. Find K_p's explicit decomposition (Tier 1+ PSLQ search;
>    or derive from knot-operator LP/SDP).
> 2. Verify universe-level closure Σ_p D([Z]^(p)) = 2/(3π).
> 3. Categorically derive C2-inflection mechanism from
>    Bring-Bloch action.

Task #1 is the hard one. Task #3 hints at a **C2-inflection** at
the substrate point — `λ_scale` may emerge from where the q-dilog
tower has a curvature feature (inflection point) at q_0.

From the cheat sheet, the Phase 5b synthesis
`Li_2^q ↔ cos_q(h) ↔ cosh(h)` provides three avenues for the
same bar-symmetric kernel. The **mass-side equivalent**
(Faddeev tower, bar-anti-symmetric) is queued as the §7 #4
open frontier in
[`docs/audits/2026-05-20-compute-wiring-audit-pr-852.md`](../audits/2026-05-20-compute-wiring-audit-pr-852.md):
> "q-dilog tower direct λ_p_scale derivation (post-bar-anti-sym,
> given 6-tier negative Bring-Bloch)"

## Concrete search strategies

In approximate order of expected ROI:

### Strategy A — Rogers `Li_2^q` PSLQ at algebraic substrate points

Build a basis of `Li_2^q(z)` values for `z` in `ℚ(q_0)`'s natural
algebraic locus: `z ∈ {q_0, 1/q_0, q_0², 1-q_0, -q_0, q_0·(q_0-1),
1/(q_0(q_0-1)), q_0³, q_0/(q_0+1), ...}`. Run PSLQ against the
target `λ_scale = 2.4599527869...` at 80–100 dps.

**Compute kernel.** Use `folio-assistant/computations/li2q.py`
(or whichever script wraps Li_2^q in the framework — search via
`grep -l li2q folio-assistant/computations/*.py`). MPFR 50 dps,
PSLQ via `mpmath.pslq`.

**Estimated cost.** Hours, similar to Bring-Bloch tier searches.

### Strategy B — Faddeev `Φ_q` mass-side PSLQ

Same as Strategy A but with `Φ_q(w)` (bar-asymmetric). The
mass-anchor context is the right side for `λ_scale` which
multiplies the topological volume → mass scale.

**Compute kernel.** `folio-assistant/computations/phi_q.py` or
similar; CMP per `Φ_q` definition in
[`prop:mass-tower-operator-valued`](../../content/quantum-observable-universe/braids-and-knots/mass-tower-operator-valued.md).

### Strategy C — cosh / cos_q ladder

Via the Phase 5b synthesis, try `λ_scale = a · cosh(b·h) + c ·
cosh(d·h)` for small integers `a, b, c, d` and `h = q − q⁻¹`.
The closed-form `cosh` level is the easiest to PSLQ.

Already tried (negative): the "5/2 − h²·G ansatz" was an
empirical PSLQ coincidence at `h, h²` order;
[`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
notes this. Look for **higher-order combinations** (`h³`, `h⁵`)
or different basis functions (`sinh`, `cosh(h)^n`).

### Strategy D — Direct categorical derivation from `𝓑_p`

Compute `λ_scale` directly from the canonical proton Hecke
element `𝓑_p` (canonical braid construction;
[`folio-assistant/computations/canonical_braid_marshalling.py`](../../folio-assistant/computations/canonical_braid_marshalling.py))
via a knot-operator-LP/SDP problem. This bypasses PSLQ entirely:
solve for the canonical structural object whose evaluation at
q_0 yields `λ_scale`.

**Compute kernel.** Extend
[`folio-assistant/computations/lp_dual_solver.py`](../../folio-assistant/computations/lp_dual_solver.py)
with a `lambda_scale_from_braid_p` solver that takes 𝓑_p and the
Vol(𝓑₃) topological invariant and produces `λ_scale` as an LP/SDP
output.

### Strategy E — Universe-level closure

Per the `prop:lambda-scale-bring-bloch-identity` §Open work item #2:
verify `Σ_p D([Z]^(p)) = 2/(3π)`. This is a **constraint** the
correct `λ_scale` parametrisation must satisfy. If you find a
candidate via A/B/C, plug it into the closure identity and check.

## Verification criteria

A candidate parametrisation is acceptable iff it satisfies ALL:

1. **Numerical agreement** with the target at 50 dps:
   `|λ_scale^candidate − 2.4599527869...|/λ_scale < 1e-15`.
2. **Type discipline** — uses only `m_e, q_0, Vol(𝓑₃)` and rational
   numbers; no other calibration constants.
3. **q_0-locality** — the parametrisation must be well-defined as a
   function of q (not just a numerical accident at q_0). Verify by
   evaluating at q' = q_0 + ε for small ε and confirming smoothness
   + analytic continuation.
4. **Universe-level closure** — passes the
   `Σ_p D([Z]^(p)) = 2/(3π)` check (Task #2 in
   `prop:lambda-scale-bring-bloch-identity`).
5. **Falsifiability** — predicts a non-trivial `λ_scale` at a
   different substrate point (e.g., the C2-inflection point where
   `q = (1+√5)/2`-like algebraic neighbour), and that prediction
   agrees with the parallel computation done via Bring-Bloch's
   universal-volume integral.

Conditions 1+2+3 are mandatory; 4+5 are strong cross-checks that
distinguish a structural identity from a numerical coincidence.

## Anti-patterns (do NOT do)

1. **Do not introduce new calibration constants.** A 7th-ansatz fit
   for `λ_scale` against m_p is the same CAL-4 violation as the
   hardcoded literal. The strict 3-calibration rule is enforced
   per CLAUDE.md `Δ_λ gate`. Six closure ansätze have already
   failed on the deuteron, and a seventh fit-based attempt will be
   caught by the canonical-watcher.
2. **Do not lower precision.** PSLQ at < 50 dps will produce false
   positives. Use mpmath `mp.dps = 100` for the PSLQ runs and
   verify the candidate at `mp.dps = 200`.
3. **Do not silently switch q_0 conventions.** The substrate value
   is `Q_50_DIGIT_STR =
   "1.10997859555418057528159407960950937799328227995870"` in
   [`folio-assistant/computations/q_parameter.py`](../../folio-assistant/computations/q_parameter.py).
   Any candidate must be evaluated at exactly this q_0.

## Deliverables (when this work is done)

1. **Witness JSON** —
   `folio-assistant/computations/lambda-scale-qdilog-direct.witness.json`
   with the candidate expression, the numerical agreement at 50 dps,
   the q_0-locality check, and the universe-closure verification.
2. **Production wire-up** — replace `LAMBDA_PROTON_DOC` literal in
   `m_p_borromean_verification_50dps.py:100` with a call to the new
   derived expression. Same for `LAMBDA_NEUTRON_DOC` at line 101.
3. **Audit doc** — `docs/audits/2026-05-DD-lambda-scale-qdilog-direct.md`
   documenting which strategy (A–E) succeeded, what was tried and
   rejected, and the verification chain.
4. **Migration Backlog #1 closure** — update
   [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md)
   to remove the backlog item.
5. **Paper-side block update** — promote
   `prop:lambda-scale-bring-bloch-identity` either to a closed
   theorem (if Strategy A/B/C/D yields a proof) or to a falsified
   conjecture with the q-dilog-tower derivation as the canonical
   replacement.

## Cross-references

- [`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
  — the formula that uses `λ_scale`.
- [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
  — the now-incomplete Bring-Bloch hypothesis.
- [`prop:li2q-phiq-bar-symmetrization`](../../content/quantum-observable-universe/braids-and-knots/li2q-phiq-bar-symmetrization.md)
  — the Φ_q ↔ Li_2^q bar-symmetry identity.
- [`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](../audits/2026-05-18-210x-scale-gap-root-cause-v2.md)
  — diagnostic identifying `λ_scale` as the CAL-4 problem.
- [`docs/audits/2026-05-20-compute-wiring-audit-pr-852.md`](../audits/2026-05-20-compute-wiring-audit-pr-852.md)
  §7 — open frontier #4 (this work).
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §4 (Φ_q vs Li_2^q) and §5 #1 (Migration Backlog).
- [`folio-assistant/computations/q_parameter.py`](../../folio-assistant/computations/q_parameter.py)
  — substrate q_0 canonical pin.
- [`folio-assistant/computations/bring_bloch_tier{1..5}_search_m_p.py`](../../folio-assistant/computations/)
  — the exhausted Bring-Bloch path; use as PSLQ scaffolding template.
- [`folio-assistant/computations/lp_dual_solver.py`](../../folio-assistant/computations/lp_dual_solver.py)
  — LP/SDP infrastructure for Strategy D.

## Why this work matters

Closing CAL-4 in `λ_scale` is the **only** known path to
first-principles m_p, m_n, m_He absolute predictions in the QOU
framework. Without it, the production mass pipeline retains an
empirically-calibrated literal that the cheat sheet itself flags as
a 3-calibration discipline violation. The Bring-Bloch path is
exhausted; q-dilog-tower-direct is the next-best lead.

If successful, this resolves the headline "L2 100×" obstacle for
m_p, m_n absolute (currently at CAL-2 floor ~780 ppb; the
substrate-only derivation would push toward arbitrary 50-dps
precision). It also closes Migration Backlog #1.
