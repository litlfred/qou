# Colour level (r = 2 vs r = 3), the `TL_n` compute move, and a production audit for experiment-inverted values

Three tasks. Task 0 (production audit for inverted-CODATA values) was
inserted ahead of the other two by owner directive mid-session.

---

## TASK 0 — audit production for experiment-inverted values

**Owner directive.** *"Δ_λ from inverted CODATA = NOT ALLOWED"* and *"it should
be excise from production"*.

### Verdict up front

**No experiment-inverted value was found wired to production as canonical.**
Every instance of the shape that I traced is either (a) confined to
exploratory probes, or (b) behind an *enforced, verified* tier gate. I found
**one** genuine bug and **three** labelling defects, none of which is a
production wiring.

This is a negative result, and I want to be explicit that it is a *measured*
negative rather than a failure to look: the corpus has evidently been through
prior anti-fit sweeps, and the fits that remain are labelled, firewalled, and
in several cases dead code. Where the owner's premise was that such values are
live in production, the measurement does not support it — for the paths I
covered. Coverage limits are stated at the end.

### Method

"Production" is taken from the repo's own definition
([`local/production-vs-exploratory-discipline`](../../.claude/skills/local/production-vs-exploratory-discipline.md)
§"Three categories of output"): the `canonical_*` family, `mass_table_ppb.py`,
the `*_50dps.py` family, `codata_constants.py`, named `LAMBDA_*` / `ALPHA_*` /
`Q_*` constants, `*-canonical.witness.json` / `*-50dps.witness.json`, the
cheat-sheet §5 "closed" rows, and the two dashboards
(`per-observable-100x-status`, `onepb-status-dashboard`).

The decisive per-site test is the owner's: *if the experimental value were
different, would this number change?* Yes ⇒ fit. I applied it by **consumption**
— a fit computed inside a probe is permitted as a shape-hint; a fit *read by* a
production consumer is not. So for each candidate I traced the readers, not
just the definition.

I deliberately did **not** rely on the `circ-anchor-inverted-roundtrip`
detector: bean `qou-yfsp` measured it at ~83% false positives (it matches
confirmation language inside docstrings and does not check direction), and its
one true positive is in `_deprecated`.

### Findings by bucket

#### Bucket 1 — wired to production as canonical

**Empty.** Nothing to excise. Details of the two sites that looked like
bucket 1 and are not:

**`qbeta-ck-cache.witness.json` → `per_observable_100x_status.py`** — the
strongest candidate, because `per_observable_100x_status.py` *is* the 100×
dashboard, explicitly named as production, and the cache it reads *is*
CODATA-inverted. `qbeta_utils.c3_target_at`
([`computations/qbeta/qbeta_utils.py:133-167`](../../computations/qbeta/qbeta_utils.py))
computes literally

```python
return (q_codata / Q_N2 - 1) / sub["u"] ** 3
```

which is a fit in every convention — it solves for whatever `c₃` reproduces the
experimental Q-value.

**But the dashboard does not consume it.**
[`per_observable_100x_status.py:463-475`](../../computations/per_observable_100x_status.py)
walks the cached rungs and `break`s at the first non-`derived` tier:

```python
for row in ck_data["rows"]:
    tier = row.get("tier") or (
        "derived" if row.get("label") == "lean-proved" else "cal-anchored")
    if tier == "derived":
        last_derived_row = row
    else:
        break  # stop at first non-derived (cal-anchored) rung
```

A tier gate is only as good as its data, so I checked the witness rather than
trusting the code:

| k | tier | label | q0_dependent |
|---|---|---|---|
| 2 | `derived` | `lean-proved` | `False` |
| 3 | `cal-anchored` | `cal-anchored` | `True` |

The loop therefore stops after `c₂` (Lean-proved Taylor-exact) and the inverted
`c₃` is never read. The dashboard's own row text names the reason: higher `c_k`
are *"extracted from CODATA Q_β, circular, q₀-dependent"*. **Correctly
firewalled.**

**The fitted Habiro tower** `(1+46u⁴)(1+4u⁵)(1−29u⁶)`, dropped 2026-07-04,
still has a live definition in a `*_50dps.py` file —
[`m_p_substrate_identity_50dps.py:194-205`](../../computations/m_p_substrate_identity_50dps.py),
`habiro_ratio_s5bb` — with `4` and `29` still hardcoded (only `46` was
parameterised to `c4`). That file is in the production family, so this looked
like a live bucket-1 hit. It is not: the function is **dead code** — grep for
`habiro_ratio_s5bb` returns only its own definition and two comments, no call
site — and its docstring reads *"NOT part of the raw proton pin and NO LONGER
applied to production m_p (owner ruling drop, #3280) … callers must not
multiply it into a production mass."* Same picture in
`deuteron_from_scratch_ledger.py:187-194`, where the headline is the bare
identity and the dressed variants are labelled comparison rows.

#### Bucket 2 — labelled diagnostics (legitimate; left in place)

| Site | Shape | Why legitimate |
|---|---|---|
| [`qbeta_utils.c3_target_at`](../../computations/qbeta/qbeta_utils.py) | `c₃ = (Q_codata/Q_N2 − 1)/u³` | 56 consumers, **all** `*_probe.py` / `*_sweep.py` / `*_scan.py` / `*_comparison.py`. The cross-anchor swing of this target *is* the intended discriminator. |
| [`delta_lambda_value_witness.py`](../../computations/delta_lambda_value_witness.py) | — | The production Δ_λ **value** path. Pure integer combinatorics: `(-1)^{n(λ)}·dim V_λ` via hook lengths. No CODATA anywhere. Tagged `value_only` and carries an explicit consumer warning not to read `Σ Δ_λ` as a binding energy. **Clean.** |
| [`binding_single_pipeline_comparison.py:255`](../../computations/binding_single_pipeline_comparison.py) | `alpha_D = deut["B_AME_MeV"] / ell_bond` | A deuteron-pinned binding scale — but run *side by side* with the derived `E_0 = m_e/(q₀(q₀−1))` as `scales = {"E0_derived": E0, "alpha_D_pinned": alpha_D}`, and the module docstring says the canonical α is `E_0`, "NOT a deuteron-pinned" scale. A two-scale comparison, correctly named. |
| [`unified_low_isotope_predictor.py`](../../computations/unified_low_isotope_predictor.py) | `B_AME` imported | Only as `AME_B_*_MEV_VALIDATION`, used solely in `err_pct` after `B_pred` is summed from derived terms. |
| `vol_density_per_block_wiring.py` | `codata` | Comparison only; docstring: "No tuning to m_p or B_AME." |
| `habiro_ratio_s5bb`, `deuteron_from_scratch_ledger.habiro_ratio` | fitted tower | Labelled FIT-TIER, dead / comparison-only (above). |

#### Bucket 3 — ambiguous, owner to rule

**`linking_weight_family_a` (λ_A) — AGENTS.md's description of it is wrong, and
the error runs in the direction that would cause a bad excision.**

AGENTS.md calls λ_A a *"CODATA-implied FIT"* and marks it deprecated for
absolute mass. Read literally, that plus the owner directive says: excise it.
It has ~13 non-probe consumers including `qou-mass`'s vendored
`_internal/_li_2_q_util.py`, so that would be a large blast radius.

The code does not support the literal reading.
[`_li_2_q_util.py:271-307`](../../computations/_li_2_q_util.py):

```python
qi = mpf(1) / q if q_inv is None else q_inv
h = q - qi
return mpf(5) / 2 + mpf(3) * h ** 2 / 4
```

`λ_A(q) = 5/2 + (3/4)h²` is **exact, closed-form, and parameter-free**. No
CODATA constant enters. Apply the self-test: if CODATA `m_p` changed tomorrow,
this number would not move. It is not an inverted value. It also does not
*hit* CODATA — at q₀ it gives ≈ 2.533 against the ≈ 2.46 that would round-trip
`m_p`, a 2.89 % miss, which is the documented `m_p` gap.

What is genuinely "CODATA-implied" is the **interpretation** — the H₄
Wedderburn-count reading, i.e. the *choice of index set* was motivated by
landing near 2.46. That is a selection-time fit and a real numerology exposure,
but it is a different defect from an inverted value, and it is not fixed by
excision.

**Ruling needed:** does the directive cover selection-time fitting of an
otherwise-derived form? I have not touched λ_A either way. Separately, the
AGENTS.md wording should be corrected regardless of the ruling — as written it
invites a future agent to excise a parameter-free algebraic identity.

**`delta_lambda_empirical_tabulation.py` — the owner's named shape does exist.**
[This script](../../computations/delta_lambda_empirical_tabulation.py) solves

```
Σ_{λ ⊢ 3A} c_λ(K) · Δ_λ(K) = ΔM(K) / m_e ,   ΔM(K) = M_codata − (Z·m_p + N·m_n)
```

i.e. Δ_λ inverted from CODATA, exactly as the owner described. It is heavily
self-labelled ("empirical-fit probe", "the Δ_λ values it emits are *targets*
fitted to CODATA, not predictions", "NOT consumed by any production prediction
pipeline"). **I verified the consumption claim rather than accepting it**: no
production consumer exists. Two caveats:

1. The claimed `auditOnly` tag is a **string field pointing at a doc path**
   (`"auditOnly": "docs/audits/2026-05-09-workplan-update-rho-k.md"`), not a
   boolean flag any tool enforces. The protection is documentation, not
   machinery.
2. Its one non-probe consumer,
   [`delta_lambda_two_factor_phase2.py`](../../computations/delta_lambda_two_factor_phase2.py),
   reads the CODATA-inverted Δ_λ table to test closure forms against it. By
   function and location that is exploratory, and it is not production by the
   skill's definition — but it carries **none** of its upstream's CLASS-A
   banner. An agent opening it cold would not know its inputs are fitted.
   Recommend a banner; I have not added one, to keep this audit read-only on
   the science.

#### The one genuine bug (adjacent, surfaced by Task 2)

[`qbeta_crossing_weight_hecke_probe.py:128`](../../computations/qbeta/qbeta_crossing_weight_hecke_probe.py)
runs `np.linalg.solve(gram.G, np.ones(6))` — an **unguarded** linear solve
against a form that is **identically singular** over ℚ(q) under convention D.
See Task 2 for why. It is a probe, so not a production defect, but it is a
wrong answer rather than a slow one.

### Coverage limits

- I traced by consumption from the production set inward, plus name-shape greps
  (`*_target`, `*_implied`, `*_resid`, `inverted`, `solve_for`, CODATA/AME
  identifiers on the right-hand side of an assignment). A fit that is spelled
  inline with no such token and no experimental identifier — e.g. a literal
  numeric constant that was *once* obtained by inversion and then hardcoded —
  is invisible to this pass. That class is real: the `4` and `29` in the Habiro
  tower are exactly it, and they were only findable because the audit trail
  named them.
- I did not audit `content/`, `docs/`, or Lean for inverted values; the
  directive said production code.
- `computations/` has ~2900 witnesses and I inspected the ones reachable from
  production readers, not all of them.

---

## TASK 1 — the 8-fold / colour question

### 1. Independent re-verification of PR #5234's measurement: **CONFIRMED**

Symbolically over ℚ(q), with `z_r = q^r/[r]_q` and
`[r]_q = (q^r − q^{-r})/(q − q^{-1})`:

```
r=1: q
r=2: q³/(q²+1)          ← exactly convention D
r=3: q⁵/(q⁴+q²+1)
r=4: q⁷/((q²+1)(q⁴+1))
```

`simplify(z_2 − q³/(q²+1)) == 0` exactly. So **convention D is level r = 2**,
confirmed independently.

At the proton pin q₀ = 1.1099785827513808:

| r | z_r |
|---|---|
| 1 | 1.10997858275138080 |
| **2** | **0.612688037146465244** ← z_D |
| 3 | 0.449304809090207852 |
| 4 | 0.369360232235604910 |

Solving `z_r = z_C = √q₀/(q₀+1) = 0.499320334183694453` for continuous `r`
gives **r = 2.5995155364**, no integer — consistent with the PR #5229
scope-(b) field-membership result (`√q ∉ ℚ(q)`).

### Per-file colour level, read from the code path

Every production colour/strong path resolves to **one** `z`, namely
`q³/(q²+1)`, i.e. **r = 2**. No production colour file defines its own `z`.

| Production file | `z` expression (verbatim) | r |
|---|---|---|
| `computations/closed_form_tau_M.py:165` (`markov_z`) | `return q ** 3 / (q ** 2 + 1)` | 2 |
| `computations/closed_form_tau_M.py:307-330` (`bring_color_weighted` branch) | `z = markov_z(q)` | 2 |
| `computations/hecke/hecke_symbolic.py:56` | `z_markov = q**3 / (q**2 + 1)   # convention D` | 2 |
| `qou-mass/src/qou_mass/_internal/hecke_symbolic.py:55` | same | 2 |
| `tools/pyhecke/python/pyhecke/gram.py:175` | `z = q0 ** 3 / (q0 ** 2 + 1)` | 2 |
| `tools/pyhecke/python/pyhecke/gram.py:437` (exact ℚ) | `_Z_FRAC = _Q_FRAC**3 / (_Q_FRAC**2 + 1)` | 2 |
| `tools/hecke-engine/src/gram.rs:125-127` (`markov_z`) | `q*q*q / (q*q + 1.0)` | 2 |
| `tools/hecke-engine/src/color_weight.rs` (Rust `bring_color_weighted`) | reuses `gram::markov_z` | 2 |
| `computations/mass_at_3A_proper.py:355-383` | defines no `z`; inherits from `hecke_symbolic` | 2 |
| `computations/markov/markov_peel.py` | defines no `z`; live path is `hecke_symbolic.z_markov` | 2 |
| `color_tube_*.py` family (8 files) | **no `z` at all** — these build the 9-element colour-pair weight tensor `W` | n/a |

Corroboration found *after* the computation, not used as input:
`schur_principal_mpmath.py:81-91` and `markov/markov_weights_symbolic.py:164-177`
both derive `Q^r = z_W/(1−Q+z_W) = q⁴ = Q²`, i.e. r = 2 exactly, in the
`Q = q²` Wenzl variables — the same statement.

**`z_3` appears nowhere outside a probe.** Only two sites: the comparison table
in `docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md:214`, and
its producer `computations/ocneanu_param_from_fibre_dimension.py`, which nothing
imports. *False-positive warning for future greps:* the literal
`0.44930482320583087` in many witnesses is **`h_q`**, not `z_3`
(`z_3 = 0.449304809090…`), differing at the 8th decimal.

### 3. What `bring_color_weighted` implies: **nothing about the level**

Canonical implementation `closed_form_tau_M.py:307-330`. It is a per-bond
scalar product over the A−1 nearest-neighbour bonds of the ordering `p^Z n^N`:

| bond | factor |
|---|---|
| p–p | `z` |
| n–n | `z − h` |
| p–n | `z − h·(1/2 − δ/4)` |

with `h = q − 1/q` and `δ = (q−1)²(1 − q⁻⁴)/3`. It takes the bar-symmetric
average `z − h/2` at a p–n interface and shifts it by `+h·δ/4`; `δ = 0` recovers
`strict_averaged`. That is the entire content.

It **consumes** `z` and never defines, derives, or constrains it. There is no
representation, no fibre object, and no row cap anywhere in the computation;
`δ/4` is a flavour-split magnitude, not a colour multiplicity. Even the one
genuinely colour-indexed object in the corpus — the 9-element weight tensor
`W_{c₁c₂}` in `InterNucleonChannelColorTube.lean`, normalised to
`Σ weight = 1` — is a convex average and so contributes a scalar of total
weight 1, which cannot change a level either.

**`bring_color_weighted` is fibre-agnostic.** Its canonicity under owner ruling
R3 therefore implies *nothing* about the level. This is a clean answer to task
item 3.

### 2. The code-vs-Lean tension: **they are about different objects, and the Lean claim is unformalized prose**

The cited Lean is
[`FibreDimensionForcesTL.lean:69-71`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/FibreDimensionForcesTL.lean):

> Colour antisymmetry, which genuinely needs a three-row block, therefore
> requires a *different* (3-dimensional) fibre and a *different* functor — it is
> not reachable by re-tuning this one.

Two things matter about this, and neither is visible from the line alone:

1. **It is a prose remark inside a module docstring, under a heading literally
   titled "What this does NOT establish".** Nothing below it formalizes the
   claim. The formalized content of the file is entirely about the mass
   channel: `qNumber_shift_identity`, `ocneanu_param_eq_of_fibre_qdim`
   (`dim_q V = [N]_q ⟹ z·[N]_q = q^N`), its `N = 2` instance, and
   `twoDimFibre_pins_h3_weights`. So "the Lean says colour needs three rows" is
   not accurate — a *comment* says it.
2. **Production has no colour fibre at all.** Per item 3 above,
   `bring_color_weighted` is a scalar reweighting of the p–n bond *inside* the
   level-2 mass channel. It is not a colour functor and does not claim to be.

**Verdict: there is no tension.** The Lean docstring describes a
not-yet-constructed object (a genuine colour functor with a 3-dimensional
fibre and a different functor); the code implements a colour-*motivated* scalar
correction within the mass channel. The two do not disagree because they are
not about the same thing. Neither "the code is wrong" nor "the Lean is
aspirational" is quite right: the Lean remark is a correct statement about an
object that does not exist yet, and the code is a correct implementation of a
different, weaker thing.

This confirms PR #5234's measurement **and** its conclusion, and supplies the
reason #5234 did not state: colour is a δ-perturbation rather than a fibre
change because production never had a colour fibre to change.

### 4. Is the eightfold line dead? **The numerological inference is dead. A precise structural test exists and is not dead.**

**Dead, and I mean it:** "level 3 is SU(3) and colour is SU(3), therefore
colour sits at level 3" is unsound and stays unsound. The Wenzl tower contains
every SU(r); the presence of an SU(3) in it is not evidence about colour's
SU(3). PR #5234 was right to say so. No measurement in this audit changes that,
and `z_3`'s total absence from production removes even the weak circumstantial
version of the argument.

**Numerology flag on my own output:** the observation below is *not* evidence
for the eightfold line either. It is a statement of what evidence *would* look
like. If it gets cited later as support, that citation is the error.

**What would count as evidence.** `ocneanu_param_eq_of_fibre_qdim` is proved
**general in N**, not just at N = 2:

```
dim_q V = [N]_q  ⟹  z · [N]_q = q^N
```

So if anyone constructs the colour functor the docstring describes — a
3-dimensional fibre with `dim_q V = [3]_q` — then the theorem *forces*
`z = q³/[3]_q = z_3`, with no freedom and no fitting. The test is therefore:

1. Construct a functor with a 3-dimensional fibre that actually realizes colour
   antisymmetry (the three-row block).
2. Its Markov parameter is then `z_3` **by the already-proved theorem**, not by
   coincidence.
3. Check whether that functor reproduces colour phenomenology.

Step 1 is the whole difficulty and nothing in the corpus does it. Until it is
done, the line has zero evidential support. But the route is precisely
specified and the deciding theorem is already sorry-free, which is a materially
different situation from "dead end". Scope-(a): the eightfold line is
unsupported as stated and its usual argument is invalid; it is **not**
structurally excluded, and I have no invariant that would exclude it.

---

## TASK 2 — the `TL_n` compute move

`dim TL_n = Catalan(n)` vs `dim H_n = n!`: 132 vs 720 at n = 6, 1430 vs 40320
at n = 8. Binding runs at `n = 3A`.

### The null-dimension claim is proved, not assumed

Cite [`docs/audits/2026-08-16-tl-all-n-weight-vanishing.md`](2026-08-16-tl-all-n-weight-vanishing.md):
`conventionD_weight_eq_zero_iff` in
`QOU/QBeta/WenzlWeightVanishing.lean` proves **`y_λ = 0 ⟺ λ has ≥ 3 rows`**,
sorry-free, all `n`, generic `[Field R]`. Cross-check:
`Σ (dim V_λ)² over ℓ(λ)≥3 = 1, 10, 78, 588, 4611, 38890 = n! − Catalan(n)` for
n = 3…8. One external input, cited not axiomatised: Wenzl (1988).

### Speed vs correctness, separated honestly

**Speed only** (the discarded blocks contribute exactly zero, so no value
moves) — this is the large majority:

| File | Object | n | Note |
|---|---|---|---|
| `wedderburn_jones_markov.py` | `Σ_{λ⊢3A} y_λ χ^λ` | 3A | **Fixed in this PR** (below) |
| `mass_at_3A_proper.py` (+ `qou-mass` mirror) | `M_λ = Π(c_kσ+d_kI)`, χ_λ per λ ⊢ 3A | 3A | Largest win available; the documented "3A ≳ 35 wall" is a p(n) wall TL removes |
| `tr_m_atom_via_transfer.py` | Bratteli transfer | 3A | Already d_λ-free; win is p(n) → ⌊n/2⌋+1 shapes |
| `hecke/hecke_3a_weights.py`, `binding_canonical.py`, `schur_principal_mpmath.py` | weights / traces | 3A | Enumeration-layer only |
| `gram_matrix_seminormal_{n,h6}.py` | Σ_λ dim_λ² | 3, 6 | 720 → 132 at n = 6 |
| `markov/markov_peel.py` | recursive peel | 3A | **No benefit** — already basis-free |

**Correctness genuinely differs** (rank-deficient solve / inversion / eigen of a
form that is identically singular over ℚ(q)):

| Site | Operation | Status |
|---|---|---|
| `qbeta/qbeta_crossing_weight_hecke_probe.py:128` | `np.linalg.solve(gram.G, ones(6))` | **Unguarded solve against a singular form — a wrong answer, not a slow one.** Clearest case in the corpus. |
| `confinement-operator-selection.py:195` | `_pg_safe_inverse(G, …)` | **Raises under convention D.** A hard blocker, not a speed issue. |
| `gram-matrix-dual.py:169-170,197` | `eigvals` + `pinv` | Conditioning-sensitive |
| `tools/pyhecke/.../gram.py:407` | `np.linalg.pinv` | Pseudo-inverts away exactly the 1-dim radical (`6 − 5` at n = 3) |
| `tools/hecke-engine/src/gram.rs:339` | Moore–Penrose via rank-one shift | Same |
| `qbeta/qbeta_markov_trace_norm_probe.py:219` | sympy `.inv()` | Same |

On `TL_3` the 5×5 form is genuinely non-singular, so these stop needing a
pseudo-inverse at all. That is the honest correctness case; everywhere else the
move is speed.

### Already-existing TL implementations (nothing needs writing from scratch)

- **Rust, production-grade:** `tools/hecke-engine/src/tl_cable.rs` and
  `tl_cable_mpfr.rs` (TL_n diagram basis as non-crossing matchings, `MAXP=30`,
  `assert_eq!(dim, catalan(n))`).
- **Python reference:** `computations/probes/qbeta_5two_n{3,5,6}_cable_*` and
  `computations/probes/tl_n6_discriminator.py` (verifies
  `corank = n! − Catalan(n)` at n = 3,4,5,6).
- **Lean:** `QOU/QBeta/TemperleyLiebTower.lean`, `QOU/Knots/KauffmanTL3.lean`,
  `QOU/MathlibExt/TLContentStratification.lean`.

**None is wired to the binding/Gram path.** `tl_cable*` serves the coloured-Jones
q\*-test; `KauffmanTL3` serves link-nontriviality.

### Implemented here (clean, low-risk)

`wedderburn_jones_markov.global_wedderburn_sum_jones_markov` looped over all
p(3A) partitions and skipped only on `χ == 0` — so the expensive
`specht_character_atomic` was evaluated even for blocks with `y_λ ≡ 0`. Moved
the `y == 0` test ahead of the character build.

Verified value-neutral by summing both ways symbolically:

| case | n | shapes | skipped | diff |
|---|---|---|---|---|
| p, n | 3 | 3 | 1 (33 %) | 0 |
| D | 6 | 11 | 7 (64 %) | 0 |
| T | 9 | 30 | 25 (83 %) | 0 |
| ³He | 9 | 30 | 25 (83 %) | 0 |

Every skipped partition confirmed to have ≥ 3 rows. The skipped fraction grows
with A, so this scales into the binding chain.

### Not implemented — listed with effort

| Item | Effort | Risk |
|---|---|---|
| Same `y == 0` guard at the enumeration layer (`y_lambda_at` / `y_lambda_at_q0_mpmath` return dicts keyed on all p(n) with zeros in them) | ~1 h | Low — but changes a public dict's keys, so check readers first |
| `mass_at_3A_proper.py` restrict λ-loop to ℓ(λ) ≤ 2 | ~half day | Low-moderate; biggest payoff |
| Route `pyhecke.gram` / `gram.rs` onto a genuine 5×5 `TL_3` form, retiring the pinv | ~2-3 days | **Moderate-high** — this is the correctness case and it touches the Rust engine, the Python wrapper, and `confinement-operator-selection`. Should be its own PR. |
| Fix the unguarded solve at `qbeta_crossing_weight_hecke_probe.py:128` | ~1 h | Low; independent of the TL move |

Deliberately **not** attempted: any wholesale rewrite of the binding chain.

### Two caveats surfaced en route

1. **`tools/pyhecke/python/pyhecke/gram.py` is internally convention-split.**
   The float64 `z` (L175) is convention **D**; `z_mp` / `tr_m_mp` (L622-652) and
   `gram_matrix_mp` (L746) are still convention **C** (`1/(√q + √q⁻¹)`), per
   their own docstrings. So the 50-dps path and the float64 path in the same
   module do not build the same form. Relevant to the convention-C excision
   tranche — and note this is exactly the "returned, not assigned" spelling
   that PR #5124 showed the C-detector is blind to.
2. Convention-C survivors on non-colour paths: `hecke/hecke_division.py:186`,
   `free-neutron-decay.py:54` (both r = 2.5995, i.e. no integer level);
   `schur_principal_mpmath.py:120-125` is explicitly quarantined.

---

## Beans

Extended rather than duplicated: `qou-8iru` (convention D is TL), `qou-d7h1`
(eightfold flavour SU(3) vs colour SU(3)), `qou-cds2` (pyhecke gram singularity).

Filed new: the unguarded singular solve; the Task 0 audit result + labelling
defects.

**Phantom bean IDs.** `qou-ondw` (cited in the task brief as the TL_n compute
move, PR #5230) **does not exist**, joining `qou-csdp` and `qou-rm47`. Three
bean IDs cited in PR bodies resolve to nothing. The live TL bean is `qou-8iru`.
