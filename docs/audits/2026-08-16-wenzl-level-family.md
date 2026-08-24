# The Wenzl level family — what sits above `r = 2`

**Verdict on the owner's question — "is something missing that we are not
capturing?" — in one line: the *lemma* is not missing anything (it was already
proved for every `r`); what is missing is that only `r = 2` is ever
instantiated, and the corpus has no map of the rest.** This is that map.

Follow-on to
[`2026-08-16-tl-all-n-weight-vanishing.md`](2026-08-16-tl-all-n-weight-vanishing.md),
which proved `s_λ = 0 ⟺ ℓ(λ) > r` for every `n`, every `λ` and **every** level
`r` (`QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff`, sorry-free), and
identified convention D as `r = 2` exactly.

Probe: [`wenzl_level_family.py`](../../computations/probes/wenzl_level_family.py)
· output [`wenzl-level-family.json`](../../computations/probes/wenzl-level-family.json)
· 10/10 checks pass, sympy-exact over `ℚ(q)` plus mpmath at 50 dps, no float64.

## Read this first: most of the machinery is prior art

Three of the four deliverables land partly on ground the corpus already holds.
Naming that up front, because the difference between *re-deriving* and
*discovering* is the whole epistemic content here.

| Already in the corpus | Where |
|---|---|
| The level family `z = q^N/[N]_q`, `N = 1…8` | [`markov_z_fibre_rank_bar_covariance_probe.py:75`](../../computations/markov_z_fibre_rank_bar_covariance_probe.py) + witness; [`markov_z_full_bar_condition_probe.py:128`](../../computations/markov_z_full_bar_condition_probe.py) |
| `z·[N]_q = q^N` proved in Lean, division-free, general `N` | [`FibreDimensionForcesTL.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/FibreDimensionForcesTL.lean) `ocneanu_param_eq_of_fibre_qdim`, sorry-free |
| `N_eff(z_C) = 2.5995…`, "not an integer" | [`ocneanu_param_from_fibre_dimension.py:190`](../../computations/ocneanu_param_from_fibre_dimension.py) + witness C5 |
| `Q^r ≈ 1.72025` under C, `r = 2` under D | [`schur_principal_mpmath.py`](../../computations/schur_principal_mpmath.py) `_wenzl_constants` docstring |
| Colour needs a three-row block, so a *different* 3-dimensional fibre | `FibreDimensionForcesTL.lean:68-71`, quoted in full in §4 |

What is **new** here is marked **[N1]**–**[N5]** below.

## 0. The normalisation is forced, not chosen

Wenzl and Orellana use `g² = (Q−1)g + Q`, eigenvalues `{Q, −1}`. This repo uses
`σ² = (q − q⁻¹)σ + 1`, eigenvalues `{q, −q⁻¹}` (AGENTS.md §7a). Writing
`σ = g/c` and matching eigenvalues gives `−1/c = −q⁻¹` and `Q/c = q`, whose
**unique** solution is `c = q`, `Q = q²`, hence `z_W = q·z` (W0, solved rather
than asserted). Nothing downstream of this is convention-optional; every level
statement below is stated in that one normalisation.

Wenzl's parameter relation `z_W = Q^r(1−Q)/(1−Q^r)` inverts to
`Q^r = z_W/(1 − Q + z_W)`.

## 1. Is `z_C` any Wenzl level at all?

**No — and not merely "not an integer one". `z_C` is not `z_r` for any `r`,
integer or real, identically in `q`.** This is a **scope-(b) structural
exclusion**; the invariant is named below, per the AGENTS.md refutation rule.

### The three outcomes the question allowed, and which one happened

The owner named three possible answers. The result is the third — the strongest
one — but arrived at through the second, which is worth separating because the
corpus's existing result is the second and *only* the second.

`z_C = √q/(1+q) = 1/[2]_{√q}`. Substituting into the inversion:

```
z_W    = q·z_C = q^{3/2}/(q+1)
Q^r    = q^{3/2} / ( q^{3/2} − (q−1)(q+1)² )
```

This is not `q^{2r}` for any constant `r`, because `q^{2r}` is a **monomial**
in `q` and the right-hand side is not. Two independent invariants close it:

- **Field membership.** Every `z_r = q^{2r−1}/(1 + q² + … + q^{2r−2})` lies in
  `ℚ(q)`. `z_C` does not: `x² − q` is irreducible over `ℚ(q)` (Eisenstein at
  the prime `q` of `ℚ[q]`), so `√q ∉ ℚ(q)`, and `z_C ∈ ℚ(q)` would give
  `√q = z_C·(q+1) ∈ ℚ(q)`. **[N3]**
- **Non-constancy.** The formal level `r_C(q) := log(Q^r)/log(Q)` takes
  different values at different `q` — `2.2267…` at `q = 1.05`,
  `2.9553…` at `q = 1.15` — so no constant `r` can work either. **[N2]**

### What the corpus had, and why it is weaker

`ocneanu_param_from_fibre_dimension.py` check C5 records
`N_eff(z_C) = 2.5995155364…` at the proton pin and concludes "not an integer".
That is a **pointwise** statement at one `q` — scope-(a) grade. It leaves open
the reading "C is a different level, we just evaluated at an awkward anchor",
which is exactly the reading the owner asked to rule out. The field-membership
argument rules it out at every `q` simultaneously.

### `N_eff` and the Wenzl level are the same quantity — identically **[N1]**

The prompt asked whether they are. They are, as **maps**, not merely as numbers
at `q₀`. The corpus's extractor is

```
N_of(z) = −log( 1 − (q − q⁻¹)/z ) / (2 log q)
```

and the Wenzl inversion is `r = log( q·z/(1 − Q + q·z) ) / log Q` with `Q = q²`.
Their arguments are reciprocal identically in `ℚ(q, z)`:

```
(1 − q² + q·z)/(q·z)  =  1 + (1 − q²)/(q·z)  =  1 − (q − q⁻¹)/z
```

so the two logs differ by a sign and the two denominators are both `2 log q`
(W3, sympy-exact; round-trip `N_of(z_r) = r` for `r = 1…5`). At the proton pin
both give `2.59951553640017695890186155174`, agreeing to every digit the
committed witness records. **So the 2.5995 already in the corpus *is* the Wenzl
level. That half was indeed already measured** — as the prompt suspected.

### The C curve is transverse to the family, and `q₀` is not special **[N2]**

`r_C(q)` is not a constant but a curve, and the corpus's single number is one
point on it:

| `q` | `r_C(q)` |
|---|---|
| `→ 1` | `2` exactly (limit; `r_C = 2 + 4(q−1) + (37/4)(q−1)² + …`) |
| `1.05` | `2.2267` |
| `1.1099785827513808` (proton pin) | `2.5995` |
| `1.154160652264486` | `3` exactly |
| `1.215893600279658` | `4` exactly |
| `1.278449576579693` | `+∞` (pole: `q^{3/2} = (q−1)(q+1)²`) |
| `> 1.2784…` | complex |

So `z_C` passes through **every** integer level at some isolated `q` before
diverging. "C is level `k`" is therefore a statement about a *point in `q`*,
never about a convention — and `q₀` is not any of the crossings. This is the
genericity check the AGENTS.md "defined residual" rule asks for: the interesting
feature (a near-integer level) is produced by a whole interval of `q`, so
locating one is not evidence for anything.

### Scope discipline — what is *not* claimed

`z_C` **is** a perfectly good Markov/Ocneanu parameter: the Ocneanu trace on the
Hecke tower exists for any `z`. What is excluded is membership in the
**SU(N)/Wenzl sub-family** — the parameters that arise from a fibre of quantum
dimension `[N]_q` and carry a row cap with a semisimple quotient. A trace at
`z_C` has no row cap, hence no Temperley–Lieb-type radical, hence none of the
structure the `r = 2` results rest on. That, and not a bad number, is the
structural justification the convention-D ruling has.

## 2. The level family **[N4]**

`z_r = q^r/[r]_q` with balanced `[r]_q = (q^r − q^{−r})/(q − q^{−1})`,
equivalently `z_r = q^{2r−1}/(1 + q² + … + q^{2r−2})` (W1, exact, `r = 1…8`).
The `r = 2` member is `q³/(q²+1) = z_D` on the nose (W2).

The quotient at level `r` is `H_n(q)/⟨E^{(r+1)}⟩`, `E^{(r+1)}` the `(r+1)`-strand
`q`-antisymmetriser, whose blocks are the `λ` with at most `r` rows —
**classical Jones/Wenzl structure theory, cited, not derived here.** Only the
dimension arithmetic below is computed.

| `r` | `z_r` | `z_r(q₀)` | row cap | quotient | gauge label | `dim` quotient, `n = 1…8` |
|---|---|---|---|---|---|---|
| 1 | `q` | `1.1099785827…` | `ℓ(λ) ≤ 1` | `H_n/⟨E^{(2)}⟩`, one-dimensional | SU(1), degenerate | `1,1,1,1,1,1,1,1` |
| 2 | `q³/(q²+1)` | `0.6126880371…` | `ℓ(λ) ≤ 2` | `TL_n = H_n/⟨E^{(3)}⟩` | SU(2) | `1,2,5,14,42,132,429,1430` (Catalan) |
| 3 | `q⁵/(q⁴+q²+1)` | `0.4493048091…` | `ℓ(λ) ≤ 3` | `H_n/⟨E^{(4)}⟩` | SU(3) | `1,2,6,23,103,513,2761,15767` |
| 4 | `q⁷/((q²+1)(q⁴+1))` | `0.3693602322…` | `ℓ(λ) ≤ 4` | `H_n/⟨E^{(5)}⟩` | SU(4) | `1,2,6,24,119,694,4582,33324` |

`dim = Σ_{ℓ(λ) ≤ r} (f^λ)²`, which by RSK counts the permutations of `S_n` with
no decreasing subsequence of length `r+1`.

The corank `n! − dim` is the dimension of the trace radical — the part of `H_n`
the level-`r` Markov–Gram form annihilates:

| `r` | corank, `n = 1…8` | first `n` with a radical |
|---|---|---|
| 1 | `0,1,5,23,119,719,5039,40319` (`= n!−1`) | 2 |
| 2 | `0,0,1,10,78,588,4611,38890` | 3 |
| 3 | `0,0,0,1,17,207,2279,24553` | 4 |
| 4 | `0,0,0,0,1,26,458,6996` | 5 |

**This table is the direct answer to "is something missing at `r > 2`".** PR
#5207's measured coranks `1, 10, 78, 588` are the `r = 2` row (reproduced here
as a self-check on the machinery, W6). The ladder above it is the *same*
statement at higher level: at level `r` the radical is `⟨E^{(r+1)}⟩`, it first
appears at `n = r+1` with corank exactly `1`, and it is generated by the
one-column diagram `(1^{r+1})`. Nothing about the `r = 2` result is special —
it is the second row of a table, and the proved vanishing lemma already covers
every row.

## 3. Where the QOU channels actually sit **[N5]**

The registry
([`trace-convention-registry.json`](../coordination/trace-convention-registry.json),
schema `trace-convention-registry/v1`, updated 2026-08-15) carries **four**
channels. Reading the `z` each one's production code actually evaluates:

| channel | convention | `z` in production | level | registry status |
|---|---|---|---|---|
| `mass` | D | `q³/(q²+1)` via `m_p_substrate_identity_50dps::trM_borromean` → `canonical_mass` | **2** | agreed |
| `binding` | D | `closed_form_tau_M::markov_z`, `wedderburn_jones_markov::y_lambda_at` | **2** | agreed |
| `borromean-binding-single-pipeline` | D | `borromean_binding_recompute.py:110` | **2** | agreed |
| `qbeta-decay` | C | `qbeta/qbeta_utils::markov_parameter` | **none** (formal `2.5995` at `q₀`) | agreed-migration-pending (bean `qou-cds1`) |

**Finding: every channel that is in the family at all is at `r = 2`. No QOU
channel sits at `r = 3` or above.** The one channel that is not at `r = 2` is
not at another level either — it is off the family entirely, which is the §1
result read per-channel. So the honest answer to the owner's payoff question is
the second of the two he named: *they are all `r = 2`* — and that is a finding,
because it says the framework currently has exactly one gauge sector's worth of
Hecke structure wired.

### Two things found on the way

**(a) A third `z` spelling, live in code, at no level.** `z = 1/(q + q⁻¹) =
q/(q²+1)`, numerically `0.4972905456…`, formal level `2.6136…`. It is *not*
`z_C` (`0.4993203342…`) and not `z_D`. It appears in
[`meson_lepton_knot_dictionary_probe.py:104`](../../computations/probes/meson_lepton_knot_dictionary_probe.py)
inside a function named `markov_trace_h2` whose docstring self-labels it
*"Wenzl Jones-Markov"* — i.e. it names the referent of C/D while computing
neither — and as `z_M_v3` in
[`casimir_phi_q_markov_probe.py:126`](../../computations/probes/casimir_phi_q_markov_probe.py).
Neither file is a production file, and the registry's discovery pattern cannot
see them (its R4/R5 rule requires the function name to contain `borromean`).

This one is excluded from the family by a **different** invariant than `z_C`:
`q/(q²+1)` *is* in `ℚ(q)`, so the field argument does not apply. Instead, `z_r`
has numerator `q^{2r−1}`, so numerator degree `1` forces `r = 1`, and
`z_1 = q ≠ q/(q²+1)`. Also scope-(b), also non-numerical. The registry logs the
`1/δ`-vs-`z_C` confusion as a *prose* conflation (bean `qou-98g5`); it is also
executable.

**(b) The registry is stale on `pyhecke.gram.z`.**
[`tools/pyhecke/python/pyhecke/gram.py:175`](../../tools/pyhecke/python/pyhecke/gram.py)
now reads `z = q0 ** 3 / (q0 ** 2 + 1)` — convention D, migrated 2026-08-15 per
its own banner at `:15`/`:52` — while `trace-convention-registry.json` still
carries it as C in both `evaluators.z` (`:426`) and `blocked_migrations`
(`:360-371`, `owner_decision_required: true`). The registry's own note at `:435`
says a D reading there means "something switched it and `G_INV` is now silently
wrong", so this needs an owner eye rather than an agent edit — **not fixed on
this branch.** Related: `z_mp` (`:622`), `tr_m_mp` (`:637`) and `:746` in the
same module are still C, and their docstrings assert a lockstep with the
module's float64 `z` that no longer holds.

Both verified by direct read, not taken on report.

## 4. SU(3) and colour — did the idea survive?

**Partly, and not as a discovery: the corpus already states the structural
half, and it is not numerology.** But it is still a hypothesis, and the
quantitative support is thin.

### What survives

`FibreDimensionForcesTL.lean:68-71` already says, verbatim:

> Colour antisymmetry, which genuinely needs a three-row block, therefore
> requires a *different* (3-dimensional) fibre and a *different* functor — it
> is not reachable by re-tuning this one.

Read against the level map, that sentence acquires a specific object. "Needs a
three-row block" plus the proved vanishing lemma (`s_λ = 0 ⟺ ℓ(λ) > r`) forces
`r ≥ 3`; "a 3-dimensional fibre" is `dim_q V = [3]_q`, which by
`ocneanu_param_eq_of_fibre_qdim` (`z·[N]_q = q^N`, sorry-free) forces

```
z_3 = q⁵/(q⁴ + q² + 1)   ( ≈ 0.4493048091 at the proton pin )
```

So the correspondence is **not** a numerical coincidence between two unrelated
`3`s. It is a chain of proved implications: three-row block ⇒ `r ≥ 3` ⇒ fibre
`[3]_q` ⇒ a *determined* `z`. The minimal case `r = 3` is SU(3), and the gauge
group of colour is SU(3).

### What does not survive, and the honest state

- **No QOU channel is at `r = 3`** (§3). There is no measurement supporting the
  correspondence — only a consistency of shape.
- **The "SU(N) ↔ gauge group" label is a naming convention**, not a derivation.
  Calling `r = 3` "SU(3)" is standard quantum-group nomenclature for the fibre
  `[3]_q`; it does not by itself connect to the colour SU(3) of QCD. Treating
  the shared name as evidence would be exactly the error the corpus's own
  history warns about.
- **The owner's R3 (`bring_color_weighted` canonical) is not evidence either.**
  That ruling is about a p/n weighting convention in the mass channel, which
  sits at `r = 2`. It does not place anything at `r = 3`.

### Self-flagged numerology risk

Per the critical-distance license, flagging the trap in my own output: `r_C(q₀)
= 2.5995 ≈ 2.6` and the third spelling's `2.6136 ≈ 2.6` are **not** a
meaningful coincidence, and neither is "2.6 is close to 3". Measured: the band
of `z` giving `r ∈ (2.5, 2.7)` is `0.0290` wide at `q₀`, while the two
off-family spellings differ by only `0.0020` — 7 % of the window. Both are just
"`z ≈ 1/2`", and every `z ≈ 1/2` has `r ≈ 2.6`. For comparison the genuine gap
`z_2 − z_3 = 0.1634` is 80× the separation. **No inference should be drawn from
either number's proximity to 2.6 or to 3.**

### The named test

The hypothesis is falsifiable and cheap to test, which is the only reason it is
worth recording:

> **Test.** Build the level-3 channel explicitly — Markov trace at
> `z_3 = q⁵/(q⁴+q²+1)`, weights `s_λ(1, Q, Q²)` at `Q = q²`, quotient
> `H_n/⟨E^{(4)}⟩` — and check whether the three-row blocks it *keeps* (the ones
> `r = 2` annihilates) reproduce a known colour observable without a new
> calibration. **Pass** = a colour quantity comes out of the `ℓ(λ) = 3` sector
> at the existing three calibrations. **Fail** = it needs a fourth input, in
> which case the SU(3) correspondence is a name and nothing else.

Until that runs, this is a **hypothesis**, tier `hypothesis`, wired to nothing.

## Tiering

| Claim | Tier |
|---|---|
| `s_λ = 0 ⟺ ℓ(λ) > r`, all `n`, `λ`, `r` | **proved-lean** (`schurPrincipal_eq_zero_iff`) |
| `z·[N]_q = q^N` from a fibre of `q`-dimension `[N]_q` | **proved-lean** (`ocneanu_param_eq_of_fibre_qdim`) |
| `z_D` is level 2 | **proved-lean** (`wenzlLevel_conventionD`) |
| `z_r = q^r/[r]_q`; eigenvalue matching forced | **symbolic-exact** (W0, W1) |
| `N_eff` ≡ Wenzl `r` as maps | **symbolic-exact** (W3) |
| `z_C` is no level, any `r`, identically in `q` | **symbolic-exact**, scope-(b), invariant named (W4) |
| `z_TL = 1/[2]_q` is no level | **symbolic-exact**, scope-(b), degree invariant (W9) |
| `r_C(q₀) = 2.5995…`; crossings; pole at `1.27845` | **measured**, 50 dps (W5, W7) |
| Quotient dims and coranks, `r = 1…4` | **measured** (exact integer combinatorics, W6) |
| Quotient is `H_n/⟨E^{(r+1)}⟩` with `≤ r`-row blocks | **cited** (Jones/Wenzl) |
| Every registered channel is at `r = 2` | **measured** (W10, registry + call sites) |
| Level 3 ↔ colour SU(3) | **hypothesis** — named test above, wired to nothing |

## References

`wenzl1988`, Wenzl, *Hecke algebras of type `A_n` and subfactors*, Invent.
Math. **92** (1988) 349–383, [doi:10.1007/BF01404457](https://doi.org/10.1007/BF01404457)
— the weight formula and the parameter relation `z_W = Q^r(1−Q)/(1−Q^r)`.

`orellana1998`, Orellana, *Weights of Markov Traces on Hecke Algebras*,
[arXiv:math/9806163](https://arxiv.org/abs/math/9806163), p. 17 — restates the
type-A result in this form. **Its "type D" is the Coxeter type `D_n`** and has
nothing to do with this repo's trace convention D.

Both are already registered in `content/schema/references.ts`; neither is
re-added.

## What this does not establish

- **No Lean was written.** Everything new here is symbolic/numeric. The two
  scope-(b) exclusions (§1, §3a) are one-line field- and degree-theoretic
  arguments that would formalise cheaply, but they are not formalised, and this
  document does not claim they are.
- **The `r > 2` quotients are not constructed.** The table gives their
  dimensions and their radicals' coranks; no level-3 Markov trace, weight
  vector, or Gram matrix was built. The named test in §4 is the build.
- **Nothing here re-derives the convention-D ruling** or bears on the proton
  pin or the colour weighting. It supplies the structural reason C is excluded
  that the ruling did not previously have written down, and nothing more.
