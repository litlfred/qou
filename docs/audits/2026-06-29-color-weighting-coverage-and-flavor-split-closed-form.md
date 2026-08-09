# Color-weighting coverage audit + flavor-split closed-form probe (2026-06-29)

**Branch:** `claude/color-weighting-flavor-split-audit-2026-06-29`
**Follows:** the L1 peel float64 fix (PR #3084) — the cross-check now certifies
the color-weighted trace at 1 ppQ, which motivated verifying the
color-weighting is applied *consistently* everywhere it should be.

## Part A — color-weighting `h(½ − δ/4)` coverage (option 2)

**Question.** Is the canonical color-weighted p-n crossing
`σ − h·(½ − δ/4)·𝟙`, with δ = `flavor_split_subleading(q)`, applied
consistently across compute — same δ, same coefficient — everywhere the p-n
bridge appears?

**Method.** Grep + per-consumer inspection of the ~23 non-deprecated files
that reference `flavor_split_subleading` / the `½ − δ/4` crossing weight.

**Result — CONSISTENT. No gaps found.**

| Check | Finding |
|---|---|
| δ source | `flavor_split_subleading(q)` in every consumer — `closed_form_tau_M.py:281`, `chi_cd_mpfr.py:70`, `chi_monotone_transfer.py`, `markov_peel.py` (symbolic mirror), the binding probes. |
| `flavor_split_leading` usage | ONLY inside `_li_2_q_util.py`, to *build* `subleading = leading·(1+ℏ_q³)`. No consumer uses leading-only as the color-weighting. |
| crossing coefficient | `½ − δ/4` uniform across production + probes (`z − h(½−δ/4)` for the binding factor; `σ − h(½−δ/4)·𝟙` for the Hecke crossing). |
| L1 cross-check | markov_peel and chi-cache (the two independent color-weighted implementations) agree at ~1e-50 post-#3084 — direct proof they use the *same* δ to 50 dps. |
| apparent sign anomaly | `derived_bond_graph_binding.py:104` `f_bar["pn"] = z + h(½−δ/4)` is the **intentional bar-conjugate** `f̄` of `f["pn"] = z − h(½−δ/4)` (archimedean bar-norm `tr_M·tr̄_M`, per the line-98 comment) — NOT a sign bug. |

The color-blind legs (Hoefsmit, Habiro) correctly *omit* the weighting and
diverge ~1.8e-4 at A≥2 by construction (handled as informational in both
`cross_check_trM_1ppb.py` and, post-#3084, the peel producer's bridge check).

## Part B — is `(1+ℏ_q³)` a series? does inverting close Δm_pn? (option 3)

**Question.** `(1+ℏ_q³)` is exactly the first two terms of the geometric
series `1/(1−ℏ_q³) = 1 + ℏ_q³ + ℏ_q⁶ + …`. Is the denominator a series, and
does the closed form `leading/(1−ℏ_q³)` close the Δm_pn gap?

**Probe:** `computations/probes/flavor_split_geometric_closure_probe.py`
(witness `flavor-split-geometric-closure-probe.witness.json`).

| form | δ = Δm_pn/M_N | err vs CODATA |
|---|---|---|
| `leading` = (q−1)²(1−q⁻⁴)/3 | 0.0013757112 | 0.128% |
| `leading·(1+ℏ_q³)` (canonical) | 0.0013770494 | **0.0305%** |
| `leading/(1−ℏ_q³)` (closed-form hypothesis) | 0.0013770507 | 0.0304% |
| CODATA Δm_pn/M_N | 0.0013774699 | — |

**Findings (scope-(a) — numerical, not a structural exclusion):**

1. **The subleading correction is real and material:** `(1+ℏ_q³)` cuts the
   error ~4× (0.128% → 0.0305%) vs leading-only.
2. **The geometric closed form does NOT close Δm_pn.** `1/(1−ℏ_q³)` differs
   from `(1+ℏ_q³)` only at O(ℏ_q⁶) ≈ 9.5e-7 (rel 9.5e-7), a sub-ppm nudge —
   the residual to CODATA stays ~0.03%, ~300× larger. The missing physics is
   not in the denominator's higher geometric terms.
3. **The closed form is a HYPOTHESIS, not a derived identity.** The
   derivation frames `(1+ℏ_q³)` as a specific *"3-loop substrate-Planck"*
   correction (`flavor_split_subleading` docstring), not as a geometric
   series. Treating it as `1/(1−ℏ_q³)` without an independent derivation that
   the correction is geometric is exactly the clean-looking-formula move the
   three-calibration discipline flags. **NOT wired to production δ.**

## Part C — `(1 + ℏ_q³)` is an UNPROVEN production factor (flag)

The L1 fix (#3084) made this visible: peel and chi-cache now agree at ~1e-50
on a color-weighting δ that *includes* the `(1 + ℏ_q³)` subleading factor. So
the factor is now baked, to 50 dps, into every production color-weighting
consumer (`closed_form_tau_M`, `markov_peel`, `chi_cd_mpfr`, the binding
probes — all via `flavor_split_subleading`). **Yet it has no derivation.**

Corpus-grep status (per AGENTS.md "Before declaring open/unproved"):

| where a derivation would live | found? |
|---|---|
| compute docstring | only a **label** — `_li_2_q_util.py:165`: *"(1+ℏ_q³) 3-loop substrate-Planck correction"* |
| content block (`flavor-split-substrate.md`) | **no** — documents only the *leading* `(q−1)²(1−q⁻⁴)/3` |
| Lean | **no** proof of the subleading factor |
| witness | **no** witness derives `(1+ℏ_q³)`; they only *consume* `flavor_split_subleading` |

**Assessment.** The leading term `(q−1)²(1−q⁻⁴)/3` is derived (physical
accounting in the content block). The `(1 + ℏ_q³)` multiplier is **posited**,
not derived — its sole justification is the docstring phrase "3-loop
substrate-Planck." It improves the Δm_pn match ~4× (0.128% → 0.0305%), which
is suggestive but is also exactly the signature of an underived `h^k`
shape-fix that the production-vs-exploratory discipline exists to catch
(cf. AGENTS.md §production-vs-exploratory: "where does this h^k come from").

**Stronger finding — `(1+ℏ_q³)` is not even the right number.** The exact
correction CODATA demands is `C_true = (Δm_pn/M_N)_CODATA / leading =
1.0012784`, i.e. `C_true − 1 = 1.278e-3`. But `(1+ℏ_q³)` supplies only
`ℏ_q³ = 0.973e-3` — the ratio `(C_true−1)/ℏ_q³ = 1.314`, so **`(1+ℏ_q³)`
delivers just 76% of the needed correction** (it cuts the residual from
0.128% to 0.0305%, not to 0). No clean single `ℏ_q`-power reproduces
`C_true−1` (tested `ℏ_q³`, `ℏ_q³·[2]_q/2`, `ℏ_q²·h_q`, `ℏ_q⁴·[3]_q`, `h_q³`,
`ℏ_q³(1+ℏ_q)` — closest 0.84×). So `(1+ℏ_q³)` is a **partial, posited
shape-fix**, not merely an unproven-but-correct factor.

**Consequence for "derive `(1+ℏ_q³)`":** it is the *wrong derivation target*.
There is no principle that *should* yield exactly `(1+ℏ_q³)`, because that
factor does not close the gap. The genuine open problem is the **full**
subleading correction to the derived leading `ℏ_q²·h_q·[2]_q/3`. Chasing a
clean closed form for `C_true−1` directly is the c_k-flip-flop trap
(`docs/coordination/1ppq-qbeta.md`) and is explicitly **not** the path.

**The disciplined direction (formalize-first).** The leading term is a
*2-strand* object — the `u↔d` swap is `σ` on a 2-strand sub-braid, giving
`[2]_q` and two action quanta `ℏ_q²` (content-block accounting). The
baryon is a *3-quark / 3-strand* state, so the missing correction should be
**derived from the third (spectator) strand's substrate coupling** — a
3-strand categorical extension of the 2-strand leading object — not fit as
an `ℏ_q`-power. That extension is part of the open Archimedean-mass-functor
per-block action (the same R&D gating Δ_λ), and is not closed here.

**Required disposition (one of):**

1. **Derive the full correction** — a 3-strand categorical extension of the
   leading 2-strand object that yields `C_true ≈ 1.00128` from the spectator
   strand's coupling. (NOT "derive `(1+ℏ_q³)`" — that factor is wrong by 24%.)
   This is open Archimedean-mass-functor R&D.
2. **Label it** — until (1) lands, mark `flavor_split_subleading` as
   `posited` (not `canonical`) per the production-vs-exploratory tiering, and
   consider reporting Δm_pn at the **derived leading** residual (−0.13%)
   rather than the posited-factor residual (0.0305%), since shipping the
   76%-fix improves the apparent number without justification (the
   "fitting below σ_theory" anti-pattern).

Until one of these is done, `(1 + ℏ_q³)` must not be cited as a derived
result, and its 0.0305% Δm_pn residual must not be cited as the framework's
achieved accuracy on the splitting.

## Part D — 3-strand derivation attempt: the second-order self-interaction form

Probe: `computations/probes/flavor_split_3strand_derivation_probe.py` (+ witness).
Built the flavor split as an H₃ Markov-trace object with the spectator strand
*braiding* (the passive spectator factor is exactly 1.0 — confirmed — so the
correction must come from braiding). Findings:

- **Raw 3-strand trace ratios badly overshoot** (10–85% corrections; the
  per-nucleon H₃ traces differ by 2.1% — 15× too large and *opposite sign*).
  So the split is **not** a raw trace ratio; the bulk cancels (a self-energy /
  difference structure).
- **The working parameter-free object is the second-order self-interaction
  form** `full = leading·(1 + leading)` (⟺ `leading/(1−leading)` ⟺
  `[2]_q → [2]_q·(1+leading)`):

  | form | err vs CODATA | derivable? |
  |---|---|---|
  | leading (proven) | 0.128% | ✓ proven |
  | leading·(1+ℏ_q³) (posited, production-old) | 0.0305% | ✗ posited, 76% |
  | **leading·(1+leading)** (3-strand 2nd-order) | **0.0097%** | **parameter-free** |

  - **13× better than leading**, 3× better than the posited factor.
  - **Parameter-free**: the correction scale *is* the derived leading split,
    NOT a posited `ℏ_q`-power. Anchor-stable to ~1e-13.
  - Categorical reading: a 3-quark baryon has 3 quark *pairs* — leading
    accounts for the swapped `u↔d` pair; the `leading²` term is the
    spectator-pair (self-interaction) contribution.

- **Honest caveat (why this is scope-(a), not a closure):** the *exact*
  factor is `(C_true−1)/leading = 0.929`, not 1.000 — `leading·(1+leading)`
  over-supplies by ~7.6%. The second-order **structure** is strongly
  indicated and is the right direction, but the exact 0.929 coefficient is
  **not** closed. Per the anti-flip-flop discipline the probe did **not** fit
  0.929 to a clean form.

**Verdict.** `leading·(1+leading)` **supersedes `(1+ℏ_q³)`** on every axis
(accuracy, parameter-freeness, anchor-stability, a structural story) — it is
the right derivation target. It is **not yet a rigorous derivation** (the
0.929 coefficient is open). So the production de-wire to the *proven leading*
stands as the honest baseline; `leading·(1+leading)` is the leading candidate
to wire **once the second-order coefficient is closed** (3-strand
self-interaction normalisation — open Archimedean-mass-functor work).

## Recommendations (follow-ups, not done here)

- **Doc-currency gap (owner-review):** the content block
  [`observations/flavor-split-substrate.md`](../../content/quantum-observable-universe/observations/flavor-split-substrate.md)
  documents only the *leading* `(q−1)²(1−q⁻⁴)/3`; the `(1+ℏ_q³)` subleading —
  which is what every compute consumer actually uses and which is 4× more
  accurate — is undocumented in the canonical content. Documenting it (with
  the honest "3-loop substrate-Planck, not yet a rigorous derivation"
  framing) is a content change to a calibration-sensitive block and is left
  for owner review rather than edited unilaterally here.
- **If the geometric closed form is ever pursued:** formalize-first — derive
  that the substrate-Planck correction is geometric *before* swapping
  `(1+ℏ_q³)` → `1/(1−ℏ_q³)`; the ℏ_q⁶ payoff is sub-ppm and does not justify
  a calibration-sensitive change on its own.

## Reproduce

```bash
python3 computations/probes/flavor_split_geometric_closure_probe.py
```

---

## CORRECTION 2026-08-09 — Part A's "CONSISTENT. No gaps found." is no longer true as written

Part A certified that `δ = flavor_split_subleading(q)` was used "in every
consumer". The **de-wire happened the same day** (`mass_at_3A_proper.py`:
"DE-WIRED 2026-06-29: proven leading δ, not posited subleading"), moving the
canonical path onto `flavor_split_leading`. The code moved; this audit and the
docstrings did not.

**The code is right and the prose was wrong.** `flavor_split_subleading` is
explicitly POSITED — its own docstring says the `(1+ℏ_q³)` multiplier "has no
derivation" and supplies only 76% of the gap — while `flavor_split_leading` is
what `prop:flavor-split-substrate` actually proves. So the de-wire was correct
and this is a documentation defect, not a numerical one.

### Docstrings corrected 2026-08-09 (prose only, no numerical change)

Every one of these named `flavor_split_subleading` while the code beside it
called `flavor_split_leading`; **none of them had a real subleading call site**:

```
chi_cd_mpfr.py:20              closed_form_tau_M.py:64, 173, 273
canonical_braid_crossings.py:45   mass_at_3A_proper.py:284
markov/markov_peel.py:78       chi_monotone_transfer.py:40, 91
tr_m_atom_via_transfer.py:90
```

### STILL SPLIT AT THE CODE LEVEL — not corrected here, needs an owner call

These do call `flavor_split_subleading` at runtime, so they compute a p-n
interface `d` that differs from the canonical path's:

```
tr_m_algebraic_q.py:162
binding_bring_enhancement_compare.py:61
probes/binding_color_vs_charge_tn3he_perknot_rerun.py:94, 119
probes/interface_factor_enhancing_check_probe.py:36
probes/bring_color_weighted_base_scale_probe.py:58
```

Measured size of the disagreement:

```
δ_leading     = 0.0013757108070271
δ_subleading  = 0.0013770489659926
d_leading     = -0.1044582477697263
d_subleading  = -0.1044581778307480
separation    = 6.9939e-08        effect on B(²H) = 7.4e-07 MeV
```

Left alone deliberately: several of these are *comparison* probes where using
the other convention may be the point. Each needs reading before changing.

### The whitelist tolerates both — and can tell them apart

`chi_monotone_transfer.word_to_mpfr` re-identifies a crossing against **all**
live δ conventions (`_color_weight_deltas`) and rebuilds `d` from whichever
matches, with `_TOL = 1e-9`. The two candidates are separated by 6.99e-8 =
**69.9 × _TOL**, so the match is unambiguous and no silent mis-identification is
possible. That is why the split has not produced a visible failure.

### Two further alignment findings, on the same question

1. **Only the p-n bond is averaged at all.** `_X_PP = (1, 0)` is pure σ and
   `_X_NN = (1, −h)` is pure σ⁻¹ — unaveraged. If averaging over an internal
   degree of freedom is physically warranted it should apply to all three bonds.
   Applying the averaged template uniformly makes `L_pp = L_pn = L_nn`, which
   **satisfies charge independence and sends the ³H/³He mirror splitting to
   exactly 0** (removing the 2.2708 MeV artifact, against nature's 0.7638 —
   mostly Coulomb). It does not move the magnitude: `B(²H) = 3.890455`, +74.9%.
2. **"Colour-weighted" is a misnomer.** δ is `Δm/M_N`, the neutron–proton mass
   splitting — a **flavour** (isospin) quantity. No SU(3) colour averaging
   appears anywhere in the trace. The `½` is a plain σ/σ⁻¹ midpoint and `δ/4` a
   small isospin tilt on it. (This bullet originally called the trace "the
   N = 2 (SU(2)/Temperley–Lieb) Ocneanu member". **CORRECTED 2026-08-09** — see bean `qou-qlma` and `computations/y_lambda_su_n.py`: this is convention **C** (full-Hecke Ocneanu), NOT Temperley–Lieb. TL/SU(2) is convention **D** at `z = q³/(q²+1) = 0.6126880`; `D ≠ C` is Lean-proved and they differ by 195.8 ppm on `β_Bor`. C has `y_(1³) = 0.0227 ≠ 0`, so it does not carry the N=2 row cap, and it matches **no integer N** (effective N = 2.5995).)

### 2026-08-09 follow-up: the split is REAL and PRINCIPLED, not just drift

The "STILL SPLIT AT THE CODE LEVEL" list above was worked through. Eight files
were switched to `flavor_split_leading` and each verified to exit 0 afterwards:

```
tr_m_algebraic_q.py                                binding_bring_enhancement_compare.py
binding_color_vs_charge_tn3he.py                   binding_combiner_markov_peel_fallback.py
sweeps/mass_table_bring_phi_q_h4_sweep.py          probes/interface_factor_enhancing_check_probe.py
probes/bring_color_weighted_base_scale_probe.py    probes/binding_color_vs_charge_tn3he_perknot_rerun.py
```

**Two files were deliberately NOT switched, and this is the substantive finding.**
Both hid behind an aliased import (`from _li_2_q_util import
flavor_split_subleading as _flavor_split`), which is why the first pass missed
them — the same rename-evasion `f64_into_mpmath_audit` exists to catch.

* `m_p_borromean_verification_50dps.py:347` carries a **regression gate**:
  `substrate_flavor_split_ratio_within_1000ppm_of_codata`, `tolerance = 1000.0`
  ppm, comment "current value ~305 ppm". Subleading gives 0.0305 % = 305 ppm and
  passes; leading gives 0.128 % = **1280 ppm and would FAIL the gate**.
* `atomic_mass_via_rho_k.py:121` derives `m_n = m_p·(1 + δ)` and says so
  explicitly ("with (1+ℏ_q³) sub-leading correction"). Switching would move m_n
  by ~0.1 %, i.e. ~1 MeV.

**So the corpus is split for a reason, and the two halves are each right for
their purpose:**

| path | δ | why |
|---|---|---|
| trace / binding | `leading` | PROVENANCE — `prop:flavor-split-substrate` proves only the leading form; the subleading `(1+ℏ_q³)` is admittedly posited |
| nucleon mass / flavour-split gate | `subleading` | ACCURACY — only it lands inside the 1000 ppm CODATA gate (305 vs 1280 ppm) |

That is a genuine tension, not drift: the framework currently trades provenance
against accuracy depending on which consumer is asking, and **nothing in the
corpus states this**. It is also the sharpest available statement of what the
posited `(1+ℏ_q³)` is buying — 4× on Δm/M_N, and a passing gate.

Resolving it means deriving the subleading correction (the open
Archimedean-mass-functor R&D that `flavor_split_subleading`'s own docstring
already points to: "should be DERIVED from the 3-strand / 3-quark (spectator)
categorical structure, not as an ℏ_q-power fit"). Until then the split should be
DOCUMENTED where each side is used, not silently unified in either direction.
