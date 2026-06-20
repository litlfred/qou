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
  [`prop:binding-scale-catalan`](../../content/quantum-observable-universe/braids-and-knots/binding-scale-catalan.md);
  see also the 100-dps witness chain referenced from
  [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)).
- `ℏ_q = (q-1)/q` is the q-deformed Planck constant; at `q_0`
  this gives `Vol(𝓑₃)/ℏ_q² ≈ 746.4`.
- `S(B)` is the Skein-orientation correction (different for proton
  vs neutron); structurally derivable.
- **`λ_scale` is currently hardcoded:** `LAMBDA_PROTON_DOC =
  mp.mpf("2.4599527869")` in
  [`computations/m_p_borromean_verification_50dps.py:100`](../../computations/m_p_borromean_verification_50dps.py).
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
[`computations/bring_bloch_tier{1..5}_search_m_p.py`](../../computations/).

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

**Compute kernel.** Use `computations/li2q.py`
(or whichever script wraps Li_2^q in the framework — search via
`grep -l li2q computations/*.py`). MPFR 50 dps,
PSLQ via `mpmath.pslq`.

**Estimated cost.** Hours, similar to Bring-Bloch tier searches.

### Strategy B — Faddeev `Φ_q` mass-side PSLQ

Same as Strategy A but with `Φ_q(w)` (bar-asymmetric). The
mass-anchor context is the right side for `λ_scale` which
multiplies the topological volume → mass scale.

**Compute kernel.** `computations/phi_q.py` or
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
[`computations/canonical_braid_marshalling.py`](../../computations/canonical_braid_marshalling.py))
via a knot-operator-LP/SDP problem. This bypasses PSLQ entirely:
solve for the canonical structural object whose evaluation at
q_0 yields `λ_scale`.

**Compute kernel.** Extend
[`computations/lp_dual_solver.py`](../../computations/lp_dual_solver.py)
with a `lambda_scale_from_braid_p` solver that takes 𝓑_p and the
Vol(𝓑₃) topological invariant and produces `λ_scale` as an LP/SDP
output.

### Strategy E — Universe-level closure

Per the `prop:lambda-scale-bring-bloch-identity` §Open work item #2:
verify `Σ_p D([Z]^(p)) = 2/(3π)`. This is a **constraint** the
correct `λ_scale` parametrisation must satisfy. If you find a
candidate via A/B/C, plug it into the closure identity and check.

## Alternatives to Strategy D (added 2026-05-22, post-#895 framing)

**Framing note.** This section is written in the post-PR #895
framing: `λ_scale := λ_A(q) = 5/2 + (3/4)·h²` (the Family A
theorem, proved in `lambda_scale_all_c_i_family_a.py` + Lean) IS
the framework-derived substrate value. The production
`m_p_borromean_verification_50dps.py` was rewritten in
[PR #895](https://github.com/litlfred/qou/pull/895) (commits
`19bbcbdd` + `61923f2c`) to use Family A in place of the
CAL-4-fitted literal `LAMBDA_PROTON_DOC = 2.4599527869`. The
framework's honest m_p prediction is now 966 MeV (~3 % off
CODATA's 938.27 MeV); the CODATA value was a fitted closure
target, not a substrate derivation
([PR #917](https://github.com/litlfred/qou/pull/917) dashboard
refresh quantifies this).

The strategies below ask whether **structural refinements of
Family A** — alternative substrate-pure functionals on the same
H_n Wedderburn / Hecke-trace / Skein-polynomial data — close the
3 % gap to CODATA. They do **not** claim Family A is wrong; they
search for the next-order substrate term that combines with
Family A's leading 5/2 to land closer to 938.27 MeV.

Strategy D requires extending `lp_dual_solver.py` with a
`lambda_scale_from_braid_p` solver — substantial infrastructure
work. The alternatives below either bypass LP/SDP or use existing
infrastructure with smaller incremental cost, and should be
exhausted before committing to D's infrastructure lift.

**Two reference values appear in the result tables below:**

- **Family A prediction** — `λ_A(q_0) = 5/2 + (3/4)·h²(q_0) ≈
  2.5327796637` (the substrate-derived value; the framework's
  honest λ_scale per #895).
- **CODATA-derived target** — `(m_p^CODATA / m_e) · ℏ_q² /
  Vol(𝓑_3) ≈ 2.4599527876` (the value λ_scale would have if the
  m_p Borromean formula closed exactly to CODATA; this is the
  CAL-4-anchored quantity that #895 explicitly retired from
  production).

Refinements compatible with Framing A should land near
**2.5328** (the framework's actual prediction); refinements that
hit **2.4600** identify the residual mechanism that would close
the 3 % gap — useful for future precision work but **not** a
sign that Family A is wrong.

Empirical results from the 2026-05-22 first-pass execution are
recorded inline.

### Strategy F — Markov-trace identity test on β_Bor

Test whether the two formalisms (Markov-trace on H_3,
Vol-form on 𝓑_3) coincide on the bare 6-crossing Borromean braid:

  `λ_scale  ?=  |tr_M(β_Bor, q_0)| · ℏ_q² / Vol(𝓑_3)`

where `β_Bor = (σ_1^{-1} σ_2)^3 ∈ B_3 ⊆ H_3(q)`. If the naive
identity holds, λ_scale would be over-determined: Markov-trace
alone produces it, and Family A's prediction would need to equal
the Markov-trace expression for consistency.

**Compute kernel.** `lambda_scale_alt_f_markov_trace_beta_bor.py`
(this brief; uses existing `hecke_character_symbolic` and
`y_lambda_wenzl_bridge` infrastructure). Single 5-min compute.

**Estimated cost.** ~5 min single compute; instant verdict.

**Result (2026-05-22, witness
`lambda-scale-alt-f-markov-trace-beta-bor.witness.json`):**
**naive identity DOES NOT HOLD.**

  | quantity | value at q_0 |
  |---|---:|
  | `tr_M(β_Bor, q_0)` | 0.998366621839... |
  | `ℏ_q² / Vol(𝓑_3)` | 1.339903... × 10⁻³ |
  | candidate (above product) | 0.001337543870979 |
  | Family A prediction λ_A(q_0) | 2.5327796637 |
  | CODATA-derived target | 2.4599527876 |
  | rel diff vs Family A | −99.95 % (three orders of magnitude off) |

The naive product `|tr_M|·ℏ_q²/Vol` ≈ 0.00134 differs from
both Family A (2.5328) and the CODATA target (2.4600) by ~1836×
— exactly the m_p/m_e ratio. Consistent with the 2026-05-11
brief's PR #487 agent finding #6: the Markov-trace formalism
produces `O(1)` numbers (binding-energy decomposition,
cheat-sheet step 9); the Vol-form produces `O(1836)` numbers
(absolute rest mass). They do not coincide on β_Bor under this
naive ratio.

**Implication.** The Markov-trace formalism and the Vol-form
formalism measure different invariants of the Borromean
substrate. λ_scale lives on the Vol-form side; testing it via a
direct ratio against Markov-trace was a category error. Strategy
F closed-negative; **no consequence for Family A**, which is
derived from H_4 Wedderburn data (not from β_Bor's H_3
Markov-trace).

### Strategy G — Skein-family polynomial direct evaluation at q_0

The Borromean Jones, Kauffman bracket, and HOMFLYPT polynomials
all have closed forms (Murasugi, Lickorish-Millett). Evaluate
each at standard substrate substitutions and check whether any
single polynomial value, or natural ratio/root thereof, equals
λ_p. No PSLQ — these are categorical invariants with known
closed forms; the test is just whether one matches.

**Compute kernel.** `lambda_scale_alt_g_skein_polynomial_direct.py`
(this brief). Standard Skein-family polynomial evaluators in
`mpmath`. Single 5-min compute.

**Result (2026-05-22, witness
`lambda-scale-alt-g-skein-polynomial-direct.witness.json`):**
**no single-polynomial Skein form matches Family A.** All direct
Jones / HOMFLYPT evaluations are far from both Family A's
2.5328 and the CODATA target 2.4600. Distances quoted relative
to the CODATA target (the more demanding reference):

  | candidate | value at q_0 | |rel diff vs CODATA tgt| |
  |---|---:|---:|
  | V(𝓑_3, q_0) | 4.0105 | 63 % |
  | V(𝓑_3, q_0²) | 4.0379 | 64 % |
  | √V(𝓑_3, q_0²) | 2.0094 | 18 % |
  | V(𝓑_3, q_0)^{1/3} | 1.5888 | 35 % |
  | P_HOMFLYPT(𝓑_3, q_0^−1, q_0−q_0^−1) | 14.397 | 485 % |
  | `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})` | **2.4604** | **165 ppm vs CODATA**, +2.86 % vs Family A |

The best match `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})` lands close to
the CODATA target (165 ppm) but ~2.86 % away from the
framework-derived Family A value. Per PR #701's exhaustive
falsification of the `5/2 − h²·G` form (5 independent
structural routes), forms of shape `5/2 − topological·h²`
that produce the CODATA value are **numerical coincidences**,
not derivations. The form here parallels that pattern with
different structural ingredients (`ℏ_q² ≠ h²`, `⟨𝓑_3⟩ ≠ G`)
but lands in the same coincidence basin.

**Implication.** Strategy G is closed for the single-polynomial
identity. No Skein-family polynomial of 𝓑_3 at q_0, including
the ratio-form variants, provides a substrate-pure refinement
of Family A; the candidates either disagree with Family A by
%-level (so they are not refinements at all) or coincide
numerically with the retired CODATA-anchored target (so they
are coincidences in the sense of PR #701).

### Strategy H — Wedderburn linear-functional scan (Family A = V_1; V_2-V_8 alternatives)

The Family A theorem (PR #701, on main via #888 / #895) proves
that
`λ_A(q) := (1/4) · Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4)·h²` exactly
([`lambda_scale_all_c_i_family_a.py`](../../computations/lambda_scale_all_c_i_family_a.py))
across the framework's substrate window. Per #895 this IS the
framework-derived λ_scale; m_p prediction = 966 MeV, ~3 % off
CODATA.

The companion probe `probe_family_a_variants.py` scans seven
other natural linear functionals V_2 — V_8 on the H_4 character
table — all SUMS (positive-coefficient combinations); none
matches Family A. PR #701 used this scan + 32-variant
sign-flipped Wedderburn enumeration + Hecke level scan H_2-H_7
to falsify the empirical `5/2 − h²·G` form.

This Strategy H tranche extends the search to **quotient**
forms, which PR #701's sum-based enumeration did not consider.
Both reference values are quoted below: rel diff vs Family A
(the framework's substrate value, what a refinement should land
near) and rel diff vs the retired CODATA target (informational
only — a candidate hitting 2.4600 is a coincidence in the sense
of PR #701, not a derivation):

  | variant | h² coeff | at q_0 | rel vs Family A (2.5328) | rel vs CODATA tgt (2.4600) |
  |---|---:|---:|---:|---:|
  | V_1 = (1/4) Σ dim_q V_λ (**Family A**) | +3/4 | 2.5328 | 0 | +2.89 % |
  | V_2 = (1/(48·5)) Σ dim_q² V_λ (Plancherel) | +5/3 | 2.5734 | +1.60 % | +4.54 % |
  | V_3 = (1/(48·5)) Σ dim_q · dim_cl | +5/6 | 2.5364 | +0.14 % | +3.04 % |
  | V_4 = (1/48) Σ hook_cl · dim_q | +7/12 | 2.5255 | −0.29 % | +2.59 % |
  | V_6 = (1/(4·5)) · dim_q V_(2,2) only | +5/4 | 2.5546 | +0.86 % | +3.78 % |
  | V_7 = Σ dim_q V_λ / [4]_q (quotient) | −13/16 | 2.4652 | −2.67 % | +0.144 % |
  | V_8 = harmonic of dim_q V_λ | +85/361 | 1.5891 | −37.3 % | −35.4 % |

**V_3 and V_4 are ALSO fits, not refinements (closed-negative
2026-05-22 post-/coordinate user challenge).** Among the
Wedderburn sums tested, V_3 and V_4 land within ±0.3 % of
Family A — but the follow-up probe
[`lambda_scale_alt_h_v3_v4_substrate_probe.py`](../../computations/lambda_scale_alt_h_v3_v4_substrate_probe.py)
documents that their normalisations 5/48 and 1/48 are PINNED by
the desired classical limit (5/2 at q = 1), not derived from a
natural category-theoretic measure on H_4. They are
**fit-siblings** of Family A in the same sense that
`LAMBDA_PROTON_FITTED_FROM_CODATA` was a fit before PR #895
rescued the production chain with the proved Family A theorem
— same antipattern, just normalised against a different target
constant. V_3 and V_4 should NOT be presented as substrate-pure
refinement candidates.

**V_3/V_4 verdict.** Closed-negative. Witness:
[`lambda-scale-alt-h-v3-v4-substrate-probe.witness.json`](../../computations/lambda-scale-alt-h-v3-v4-substrate-probe.witness.json).

**V_7 is a separate observation.** The quotient form
`Σ dim_q V_λ / [4]_q` lands close to the retired CODATA target
(2.4652 vs 2.4600 — within 0.144 %), but disagrees with Family
A by 2.67 %. Under the post-#895 framing, V_7 is **not** a
substrate-pure candidate for λ_scale — it instead identifies
the same coincidence basin that the falsified `5/2 − h²·G` form
landed in (PR #701). The negative h² coefficient (−13/16) arises
from the q-correction of the denominator `[4]_q ≈ 4 + (5/2)h²`
over-cancelling the numerator's positive h² — a structural
mechanism, but PR #701's exhaustive search rules out the family
of forms that land at the CODATA target as substrate-derived.

**Status.** WEAK-POSITIVE for Family A refinement: V_3, V_4 are
plausible substrate-pure variants within ±0.3 % of Family A,
worth probing for categorical justification. NEGATIVE for
hitting CODATA: V_7's quotient form is in the
falsified-coincidence basin, not a new substrate-pure
derivation. The 3 % framework-vs-CODATA gap remains open
research; the q-dilog tower (Strategies A/B/C in the original
brief) is the unchanged primary direction.

**Anti-pattern to avoid (per
[`AGENTS.md §Δ_λ gate`](../../AGENTS.md)):** do not fit a
seven-parameter `α · V_3 + β · V_4 + γ · V_7 + ...` ansatz
against m_p. Find the categorical justification for the
specific variant first, then verify the numerical match.

### Strategy J — HOMFLYPT cross-orientation closure

The Borromean rings is a **3-component link**, so its HOMFLYPT
polynomial admits orientation refinements per component. For the
proton-vs-neutron quark partition `(2,1)` vs `(1,2)`, evaluate

  `P(𝓑_3; (2,1)) (a = q_0^{-1}, z = q_0 − q_0^{-1})`
  `P(𝓑_3; (1,2)) (a = q_0^{-1}, z = q_0 − q_0^{-1})`

and check whether the ratio matches the empirical `m_p / m_n`
ratio at q_0. If yes, the Skein orientation correction `S(p) /
S(n)` is **structurally pinned**, leaving `λ_scale` as a
single-unknown observable — over-determinable from a 2-equation
system instead of a 1-equation fit.

This was **Lead #1 from the PR #487 agent** in the 2026-05-11
brief; never executed. Existing infra:
[`skein_proton_canonical.py`](../../computations/skein_proton_canonical.py)
computes the Kauffman bracket for the canonical proton braid,
but does not yet emit a per-orientation HOMFLYPT.

**Compute kernel (to write).** Extend
`lambda_scale_alt_g_skein_polynomial_direct.py` to use
orientation-dependent multi-variable HOMFLYPT (or use SnapPy /
SnapPyHP for explicit closed-form polynomial). ~1 day.

**Estimated cost.** 1 day if HOMFLYPT closed form is available;
2-3 days if it requires symbolic Skein-reduction from scratch.

**Status.** Deferred (out of this tranche's scope).

### Strategy I — Yekutieli holonomy with per-cell curvature

Categorical derivation of `Σ_geom(q)` such that
`λ_scale = π_alg(q) − Σ_geom(q)`, where `π_alg` is Family A
(`5/2 + (3/4)h²`) and `Σ_geom` is the per-cell hyperbolic
curvature 2-form integrated over the Borromean ribbon surface
via Yekutieli non-abelian Stokes (cheat-sheet step 2).

Already partially explored in
[`lambda_scale_rd1_geometric.py`](../../computations/lambda_scale_rd1_geometric.py)
with the ansatz `Σ_geom = (3/4 + G)·h²`. The categorical
derivation of the `(3/4 + G)` coefficient is the gap. If
Yekutieli integration is computed structurally (not fit), it
should produce the empirical match WITHOUT introducing a 4th
calibration constant.

**Compute kernel.** New script under
`computations/lambda_scale_alt_i_yekutieli_curvature.py`
that integrates the per-cell curvature 2-form on `𝓑_3`'s 8
ideal octahedral cells. Each cell contributes
`Λ(π/4) = G/2`; the total of 8 cells gives `8 · G/2 = 4G`
naturally — needs to be related to the empirical `3/4 + G`
coefficient.

**Estimated cost.** 2-3 days (deriving the 2-form is the work,
not the integration).

**Status.** Deferred; Strategy H's V_7 finding may obsolete this
direction.

### Strategy K — Bloch class via explicit triangulation

INVERT the failed 6-tier Bring-Bloch PSLQ search. The 52-knot
search ruled out `[Z_p] = Σ_i n_i [Z_K_i]` as a ℤ-linear
combination of prime hyperbolic-knot Bloch classes ≤ 11
crossings. But the **decomposition basis** was the wrong
formalism; the Bloch class itself can be constructed directly.

Procedure:
1. Take the canonical 11-crossing proton braid
   ([`canonical_braid_marshalling.py`](../../computations/canonical_braid_marshalling.py),
   `atomic-braid-recipe-p`).
2. Compute its braid closure as a knot or link in S³.
3. Triangulate that closure via SnapPy.
4. Extract ideal-tetrahedron z-parameters.
5. Compute `D([Z_K_p]) = Σ_i D(z_i)` where `D` is the
   Bloch-Wigner dilogarithm.
6. Check if `λ_scale = (1/8G) · D([Z_K_p])`.

This is the categorical identity from
[`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
with the **integer multi-set** replaced by the **explicit
triangulation**. The 6-tier negative ruled out the existence of
the multi-set decomposition; it did NOT rule out the underlying
Bloch class.

**Compute kernel.** New SnapPy-bridge script.

**Estimated cost.** 2-3 days; needs SnapPy (separate Python env;
may not work in the production mpmath environment).

**Status.** Deferred; highest theoretical payoff if it lands,
but also the largest implementation lift.

### Strategy M — Cross-isotope over-determination

The common-scale conjecture asserts ONE `λ_scale` applies to
EVERY Borromean baryon (proton, neutron, and any Σ, Λ, Δ
extension). Use the mass table as additional constraints: a
candidate λ_scale that matches proton might still fail on the
2nd or 3rd Borromean baryon.

Procedure:
1. For each known Borromean baryon `B_i` with mass `m_{B_i}`
   from CODATA/AME and orientation partition `(p_i, n_i)`,
   compute its empirical λ_scale closure target.
2. A correct substrate parametrisation gives a single λ_scale;
   if the closure targets disagree by more than the Skein-
   contribution refinement, the conjecture is **falsified** at
   the second observable.
3. Use this to filter candidates from Strategies A/B/C/G/H.

**Compute kernel.** Extend
[`lambda_scale_proof_step5_skein_anchor.py`](../../computations/lambda_scale_proof_step5_skein_anchor.py)
to emit per-baryon closure targets.

**Estimated cost.** 1 day, once Strategies F-H produce
candidates worth filtering.

**Status.** Verification scaffold; runs against any candidate
from F/G/H/I/K.

### Recommended ordering (revised 2026-05-22 evening, after q-dilog Tier 0 spike + V_3/V_4 closure)

**Current empirical state of the substrate-pure search:**

- **Bring-Bloch leg:** REFUTED at Tier 5 (52 prime hyperbolic
  knots ≤ 11 crossings; PR #888 + #904).
- **q-dilog tower direct leg:** REFUTED at Tier 0 (23-element
  substrate-natural Li_2^q + Φ_q basis, coeff ≤ 10²⁰; commit
  `af2d27ee` "spike(q-dilog): no λ_scale closure in
  substrate-natural q-dilog basis", audit
  [`docs/audits/2026-05-22-q-dilog-tower-spike-lambda-scale.md`](../audits/2026-05-22-q-dilog-tower-spike-lambda-scale.md)).
- **Wedderburn-sum leg (Strategy H):** V_1 (Family A) is the
  framework's substrate λ_scale per #895; V_3, V_4 confirmed as
  fits, not refinements (this PR's `lambda_scale_alt_h_v3_v4_substrate_probe`).
- **Single-polynomial Skein leg:** CLOSED-NEGATIVE (this PR's
  Strategy G).
- **Markov-trace identity on β_Bor:** CLOSED-NEGATIVE (this
  PR's Strategy F).
- **q-locality test on all four prior near-matches**
  (commit `c18e562b9` on main, 2026-05-23): **0 / 4 survive.**
  Slope of residual vs q at substrate-window q_0 ± ε:

  | candidate | slope (ppm/q) | smooth? | substrate-q_0 coincidence? |
  |---|---:|---|---|
  | `1/(1 − h_q · q_0^{10})` (PR #943) | −1.5×10⁷ | no | YES |
  | `5/2 − h_q²·G` (numerology) | −1.7×10⁷ | no | YES |
  | **V_7 = (Σ dim_q V_λ) / [4]_q** (this PR Strategy H) | **−1.86×10⁷** | **no** | **YES** |
  | **5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})** (this PR Strategy G) | **−1.69×10⁷** | **no** | **YES** |

  All four are zero-crossings of curves with slopes ~10⁷ ppm/q
  across the substrate window. Per the standing discipline that
  "q_0 is not special, just where we happen to be", **none is a
  categorical identity** — all four are substrate-q_0 coincidences.
  The cluster has added an "Empirical-exhaustion update 2026-05-23"
  banner to
  [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
  documenting six independent searches all returning negative.
- **Updated reclassification for this PR's findings:**
  - Strategy G's `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})` at 165 ppm:
    confirmed coincidence-basin (slope test fails).
  - Strategy H V_7 = Σ dim_q V_λ / [4]_q at 0.144 %: confirmed
    coincidence-basin (slope test fails).
  - The d348ad8c "Bring color-tube backing for n=10" elevation
    (earlier sections of this brief, commit `dccf0f75`): the
    q^10 selectivity has been re-verified as a substrate-q_0
    coincidence by commit `c1dca4d73` (q-locality slope
    −1.5×10⁷ ppm/q). The Bring-color-tube-categorical-backing
    framing has been retired by the cluster; the n=10 specific
    power is now a zero-crossing structural artifact.

**Implication.** The 3 % CODATA gap on m_p is **not** closeable
by any substrate-natural basis tested through 2026-05-23. **All
four known near-matches fail the q-locality discipline.** The
remaining open directions all require ENLARGING the search basis
beyond what's been tried — AND the candidates must pass q-locality
(smooth slope across q_0 ± ε), not just match at the substrate
point:

  1. **q-dilog Tier 1+ extensions** (per `af2d27ee` audit
     §Recommendation): the operator-valued spectral coordinates
     `|V̂_S|` from
     [`prop:mass-tower-operator-valued`](../../content/quantum-observable-universe/braids-and-knots/mass-tower-operator-valued.md);
     2-variable Bloch-Wigner regulators
     `L_2(x,y) := D[x] + D[y] + D[xy/((1−x)(1−y))]`; the
     `Q(ζ_60)` trace-field rank-8 basis. These are bigger
     bases; the Tier 0 negative does not rule them out.
  2. **Strategy I (Yekutieli curvature)** — derive a per-cell
     curvature term that, ADDED to Family A's 5/2 + (3/4)h²,
     accounts for the residual 3 %. Per-cell octahedral
     volume G/2 from `Λ(π/4) = G/2` is the natural ingredient.
     Independent of basis-extension PSLQ.
  3. **Strategy K (Bloch class explicit construction via
     triangulation)** — bypass PSLQ entirely; construct
     `[Z_K_p]` from K_p's actual SnapPy triangulation. Note:
     `prop:lambda-scale-bring-bloch-identity` was demoted to
     `conj:` by PR #904 (now merged); the Bloch-class route is
     conjectural, not theorem.
  4. **Strategy J (HOMFLYPT cross-orientation)** — secondary
     check of the Skein term `S(p) / S(n)`; doesn't directly
     change λ_scale but pins the orientation correction.
  5. **Strategy D (LP/SDP on 𝓑_p)** — PR #909 stage-1 found
     that the naive LP setups (D1/D2/D3/D6) do NOT yield
     λ_scale; the formulation needs more structure than the
     brief sketch. Large infrastructure lift; lower priority
     than #1-#3 above.
  6. **Accept the 3 % gap as the framework's honest accuracy.**
     Per PR #895 + #917, this is already the production state.
     If #1-#5 all exhaust, the cluster's standing decision is
     that Family A IS the framework-derived λ_scale; the gap
     is what the framework knows, and tighter closures await
     either a substrate-derivation of q_0 (out of scope per
     AGENTS.md §Precision goals Subgoal-2) or a fundamentally
     new structural ingredient.

### Strategies closed-negative by 2026-05-22 sweep

  - **Strategy F (Markov-trace identity on β_Bor).** The naive
    identity `λ_scale ?= |tr_M(β_Bor)|·ℏ_q²/Vol(𝓑_3)` does not
    hold: candidate 0.00134 vs Family A 2.5328 (and vs CODATA
    target 2.4600), three orders of magnitude off. The H_3
    Markov trace of the 6-crossing braid is an `O(1)` number;
    λ_scale lives on the Vol-form side at `O(m_p/m_e)`. Direct
    identity between the two formalisms was a category error.
    No consequence for Family A (which is H_4-derived, not
    H_3-β_Bor-derived).
  - **Strategy G (single-polynomial Skein identity).** No
    direct Jones / Kauffman / HOMFLYPT value at q_0 equals
    Family A. The best ratio-form `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})`
    at +165 ppm vs the CODATA target lands in the same
    coincidence basin as PR #701's falsified `5/2 − h²·G` form
    — different structural ingredients (`ℏ_q² ≠ h²`, `⟨𝓑_3⟩ ≠ G`),
    same numerical-coincidence basin. Closed for single-polynomial;
    Strategy J's multi-orientation HOMFLYPT is the remaining
    Skein direction.
  - **Strategy H V_7 quotient form.** `Σ dim_q V_λ / [4]_q` is
    the first Wedderburn-quotient functional in the search;
    lands at +0.144 % from the CODATA target but −2.67 % from
    Family A. Per PR #701, hitting the CODATA target is
    coincidence (not derivation) — V_7 is not a new substrate
    candidate. V_7's negative h² coefficient is a real
    structural feature (denominator over-cancellation), but it
    does not survive PR #701's exhaustive falsification of the
    `5/2 - ε·h²` family for the CODATA value.
  - **Strategy H V_3 / V_4 sum-form siblings.** Per the
    follow-up probe `lambda_scale_alt_h_v3_v4_substrate_probe.py`
    (this PR, post-/coordinate user challenge): V_3 and V_4
    normalisations 5/48 and 1/48 are PINNED by the desired
    classical limit 5/2-at-q=1, not derived from any natural
    category-theoretic measure on H_4. They are
    fit-siblings of Family A — same antipattern that
    LAMBDA_*_FITTED_FROM_CODATA was before #895 — and should
    NOT be presented as substrate-pure refinement candidates.
  - **Original brief Strategies A / B (Rogers / Faddeev PSLQ
    direct).** Refuted at Tier 0 by commit `af2d27ee` on main:
    23-element substrate-natural Li_2^q + Φ_q basis at
    `{1/φ, 1/φ², 3/7, 1/[2]_q, ±h_q, ±h_q²}` with classical
    anchors `{1, G, [n]_q, φ, h_q}`, PSLQ coeff ≤ 10²⁰, dps 60
    — no relation to λ_scale or to `Vol_eff_p = λ_scale·8G`.
    Sweep B with pentagon-identity 1−z arguments at dps 80,
    coeff ≤ 10³⁰: only trivial Rogers identity, target coeff 0.
    Audit:
    [`docs/audits/2026-05-22-q-dilog-tower-spike-lambda-scale.md`](../audits/2026-05-22-q-dilog-tower-spike-lambda-scale.md).
  - **Tier 1+ q-dilog basis extensions (3 paths).** Refuted by
    [PR #928](https://github.com/litlfred/qou/pull/928) (|V̂_S| at
    H_3 + Q(ζ_60) D-values + tier-0 hyperbolic-knot vols,
    PSLQ coeff ≤ 10³⁰) AND [this PR's c94c2c0c commit](https://github.com/litlfred/qou/commit/c94c2c0c)
    (2-variable L_2(x,y) at root-of-unity pairs + Q(ζ_n) D-values
    for n | 60, PSLQ coeff ≤ 10²⁰). Combined: substrate-natural
    q-dilog + |V̂_S|-extended + Q(ζ_60)-D + 2-var-L_2 + tier-0-
    knot bases all NEGATIVE for λ_p, Vol_eff_p, and the residual
    (λ_p − Family A). The empirical case that the framework's 3 %
    CODATA gap is honest (per #895 + #917) is strengthened by
    every additional negative basis extension.
  - **Φ_q functional-equation route.** Refuted by commit
    [`7711f48d`](https://github.com/litlfred/qou/commit/7711f48d)
    on main: tested whether `λ_p = Φ_q(qz)/Φ_q(z) = 1/(1−z)` for
    substrate-natural `z` (back-solve z_* ≈ 0.5935; closest of 11
    substrate candidates is 1/φ at 4.14 % relative error). The
    structurally-distinct non-linear Φ_q route is now also closed
    in its tested form. 4th independent negative search in the
    cluster (Bring-Bloch tier 0-5 + q-dilog Tier 0 + q-dilog Tier
    1+ + Φ_q functional-equation).
  - **Faddeev-pentagon operator-theoretic route — categorically
    conditional on Bring color-tube weighted averaging (Phase 5q).**
    Commit [`d348ad8c`](https://github.com/litlfred/qou/commit/d348ad8c)
    on main: tested operator-theoretic Φ_q pentagon `Φ_q(U)·Φ_q(V)
    = Φ_q(V)·Φ_q(U·V)·Φ_q(U)` on a truncated 16-dim Heisenberg
    representation. Surfaces a **19 ppm near-match**

    ```
    λ_p  ≈  1/(1 − h_q · q_0^10)  =  2.45999923...
         =  Φ_q(h_q · q_0^11) / Φ_q(h_q · q_0^10)   (Faddeev functional eq)
    ```

    The integer power n=10 (n=8, 9, 11, 12 give 13–51 % error) is
    NOT an unexplained selectivity — it plausibly traces to the
    **Bring color-tube weighted averaging** Phase 5q open audit
    finding (per [cheat-sheet §"Bring color-tube weighted
    averaging"](../canonical-derivation-cheat-sheet.md)): the
    owner-intuition canonical p-n boundary averaging weights over
    9 color-pair assignments (3 × 3 quark-color sheets;
    `proton uud → (μ_u, μ_u, μ_d)`, `neutron udd → (μ_u, μ_d, μ_d)`),
    plausibly + diagonal averaging direction = **10**. Scheme 4
    (per-sheet PL integration on Bring's surface, recorded in
    [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py)
    and [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py))
    empirically reproduces `Δm_{n-p}` to ~0.14 % of CODATA, an
    independent confirmation of the 10-fold color-pair structure.

    **Status.** Categorically-conditional **alongside Strategy I**
    (Yekutieli per-cell), not in the coincidence basin. Both
    Reading B (Yekutieli) and `1/(1 − h_q · q_0^10)` (Faddeev
    pentagon × Bring color-tube) have explicit load-bearing
    Phase 5q open work items. The Faddeev form is **3.4× closer
    to CODATA** (19 ppm) than the prior `5/2 − h²·G` numerology
    coincidence (5.6 ppm — wait, 19 vs 5.6 means 5/2−h²·G is
    *3.4× closer*, not the Faddeev form). Actually:
    - `5/2 − h²·G`: 5.6 ppm (smaller error)
    - `1/(1 − h_q · q_0^10)`: 19 ppm
    The numerology-coincidence form is still closer; the
    Faddeev/Bring form has structural backing the coincidence
    lacks.

    Audit:
    [`docs/audits/2026-05-22-faddeev-pentagon-operator-spike.md`](../audits/2026-05-22-faddeev-pentagon-operator-spike.md).
    5th independent negative search in the cluster — but with
    structurally-elevated near-match.
  - **Strategy I (Yekutieli per-cell curvature) — Yekutieli
    quadratic added to canonical Wedderburn.** Per 2026-05-23
    user direction "we need yekutieli quadratic as added", the
    framework's substrate-pure prediction is the **CATEGORICAL
    SUM** of the canonical Wedderburn theorem and the Yekutieli
    per-cell curvature contribution:

    ```
    λ_scale^framework  =  λ_canonical  +  λ_Yekutieli quadratic
                       =  (5/2 + (3/4)·h²)  +  (−G · h²)
                       =  5/2 + (3/4 − G) · h²    +  O(h⁴)
                       ≈  2.49266                  at q_0
                       →  1.4 % framework gap from CODATA
    ```

    Both contributing terms are derived from independent
    substrate-natural principles:
    - **Canonical Wedderburn:** `(1/4) · Σ_{λ ⊢ 4} dim_q V_λ =
      5/2 + (3/4)h²`. Proved theorem in
      [`lambda_scale_all_c_i_family_a.py`](../../computations/lambda_scale_all_c_i_family_a.py)
      + Lean; on production via PR #895.
    - **Yekutieli quadratic:** `−G = −Vol(𝓑_3)/8 =
      −(per-cell hyperbolic volume)`. Comes from non-abelian-Stokes
      curvature integration over 𝓑_3's 8-fold ideal-octahedral
      tessellation; per the audit
      [`docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`](../audits/2026-05-18-conjecture-proof-step3-yekutieli.md),
      the load-bearing step is the cell-↔-half-sym-projection
      bijection at H_4.

    The framework's m_p prediction under this formula is
    **~951 MeV** vs CODATA 938.27 MeV — gap **halved** from the
    canonical-Wedderburn-alone ~3 % to ~1.4 %.

    **The audit's "Reading A" formula `5/2 − G·h²` (Yekutieli
    REPLACING the canonical Wedderburn h²) is NOT the framework's
    prediction.** Per the 2026-05-23 user direction, the Yekutieli
    quadratic is ADDED to the canonical Wedderburn theorem, not a
    substitute for it. The two mechanisms contribute INDEPENDENTLY
    at h² order:
    - canonical Wedderburn = (1/4) Σ dim_q V_λ enumerated sum over
      H_4 partitions
    - Yekutieli per-cell = curvature 2-form integrated over the
      ribbon surface

    These are different categorical objects measuring different
    things; both contribute. The earlier "Reading A" framing (one
    REPLACES the other) was incorrect per the additive direction.

    **Load-bearing conjecture** (audit's own flagging,
    §"Concrete next R&D" item 1): the explicit
    cell-↔-half-sym-projection bijection at H_4. The audit
    sketches the bijection (vertex / edge / center octahedra ↔
    conjugate-pair / self-conjugate partitions) but the explicit
    construction + sign-convention verification is open. With the
    proof, the additive Yekutieli quadratic above becomes the
    framework's substrate-pure theorem.

    > **Terminology (per 2026-05-23 user direction).** Going forward
    > the brief refers to the proved Wedderburn-sum λ_scale as the
    > **canonical λ_scale** (not "Family A"). Where "Family A"
    > appears in cross-references to prior PRs / audits / scripts
    > (e.g. `LAMBDA_PROTON_FAMILY_A` constant,
    > `lambda_scale_all_c_i_family_a.py`), the name is retained for
    > traceability, but the content concept is "canonical".

    Production-update options (canonical-only per 2026-05-23
    user direction "no empirical fitting, canonical only"):

    | option | dependency | m_p pred | CODATA gap |
    |---|---|---:|---:|
    | hold canonical Wedderburn | none (proved theorem) | 966 MeV | ~3 % |
    | adopt canonical + Yekutieli quadratic added | cell-↔-projection bijection at H_4 | 951 MeV | ~1.4 % |
    | adopt Bring color-tube `1/(1−h·q₀¹⁰)` | color-sheet ↔ quark-flavor mapping (Phase 5q) | 938 MeV | **−670 ppm** |

    All three are conjecture-conditional but FITTING-FREE. The +α·h⁴
    refinement probe (`lambda_scale_refinement_h4_correction_bring.py`)
    surfaced an empirical α = (3/4 + 1 − G) ≈ 0.834 that gives m_p
    to 22 ppm, but the "+1" leading h⁴ coefficient lacks categorical
    derivation. **RETIRED** per user direction "no empirical fitting,
    canonical only". The canonical refinement direction is the audit
    Step 4 R&D: derive the second-order Yekutieli per-cell h⁴
    coefficient FROM the partition algebra at H_4 — not by fitting
    against CODATA.

    Witness:
    [`lambda-scale-alt-i-yekutieli-percell-numerical.witness.json`](../../computations/lambda-scale-alt-i-yekutieli-percell-numerical.witness.json).

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
   per AGENTS.md `Δ_λ gate`. Six closure ansätze have already
   failed on the deuteron, and a seventh fit-based attempt will be
   caught by the canonical-watcher.
2. **Do not lower precision.** PSLQ at < 50 dps will produce false
   positives. Use mpmath `mp.dps = 100` for the PSLQ runs and
   verify the candidate at `mp.dps = 200`.
3. **Do not silently switch q_0 conventions.** The substrate value
   is `Q_50_DIGIT_STR =
   "1.10997859555418057528159407960950937799328227995870"` in
   [`computations/substrate/q_parameter.py`](../../computations/substrate/q_parameter.py).
   Any candidate must be evaluated at exactly this q_0.

## Deliverables (when this work is done)

1. **Witness JSON** —
   `computations/lambda-scale-qdilog-direct.witness.json`
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
- [`computations/substrate/q_parameter.py`](../../computations/substrate/q_parameter.py)
  — substrate q_0 canonical pin.
- [`computations/bring_bloch_tier{1..5}_search_m_p.py`](../../computations/)
  — the exhausted Bring-Bloch path; use as PSLQ scaffolding template.
- [`computations/lp_dual_solver.py`](../../computations/lp_dual_solver.py)
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
