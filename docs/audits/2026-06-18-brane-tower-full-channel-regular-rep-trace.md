# Brane-tower per-generator argument: `|V̂_i^full|` is the regular-rep trace — derived, with two residual conflations

**Date:** 2026-06-18
**Branch:** `claude/pensive-fermat-ja5fof` (PR #2481)
**Continues:** PR #2467 (physical-z pin) — which pinned `z_i = |V̂_i^full|` and
took it as given. This audit answers the channel-level *why*.
**Probe:** `computations/probes/brane_tower_full_channel_trace_audit.py`
+ `computations/brane-tower-full-channel-trace-audit.witness.json` (allPassed).

## Summary

The brane-tower per-generator argument `z_i = |V̂_i^full|` is the **trace on the
regular representation** of `H_3` (Wedderburn–Artin weights `w_λ = d_λ²/|S_3|`).
It is **derived, not a convergence-motivated fit** — it is forced by the mass
being the trace of a left-multiplication endomorphism (`def:hecke-mass-element`).
This audit records that derivation and **two genuine residual conflations** the
physical-z pin did not surface:

1. a **`tr_M`-vs-`tr_reg` conflation** in the descended term (~10%);
2. a **classical-vs-q-deformed weight-convention discrepancy** between the
   narrative block and the production code.

It also fixes a citation in `conj:brane-tower-z-habiro` (it cites the `std`
projection where it needs the regular-rep `full` object).

> **Retraction (intellectual honesty).** An earlier reading in this session
> called `full` a "convergence-motivated ansatz, no derivation found." The
> corpus-grep gate (CLAUDE.md §"Before declaring open") found the derivation
> (`atom-mass-full-hecke.md` + `hecke-mass-element.md`). That strong claim is
> **withdrawn**; the refined findings below are what stand.

## 1. The channel decomposition (proton, 50 dps)

Each generator carries three `H_3` irrep channels (`std` 2-dim, `sym` trivial,
`alt` sign), per the Hecke eigenvalues `(σ−q)(σ+q⁻¹)=0`:

| per-generator object | g0 | g1 | ∏ over gens | = `tr_M`? |
|---|---|---|---|---|
| `std` = `z·a+b` = localized **Jones–Markov** trace `Vol_q^({i})` | 1.14610 | 0.92950 | **1.06531** | **YES** (ratio 0.99999991) |
| `full` = `w_sym·sym + w_std·std + w_alt·alt` (**regular-rep**) | 0.98901 | 0.97107 | 0.96040 | NO (ratio 0.9015) |

(`Vol_q^({i})` computed independently via `canonical_brane_tower.vol_q_S`
equals the `std` value to 7 digits; `∏ std` equals the whole-word Jones–Markov
`tr_M` to 8 digits.)

## 2. `full` is derived: the regular-representation trace

`def:hecke-mass-element` defines the mass via the **left-multiplication
endomorphism** `L_{α_ϱ} ∈ End_C(A)`, with `Φ_mass := τ(L_{α_ϱ}) ∈ H_n(R,q)`.
Left-multiplication of an algebra on itself **is** the regular representation.
By Wedderburn–Artin, `A ≅ ⊕_λ M_{d_λ}(k)`, so the regular rep contains each
irrep `λ` with multiplicity `d_λ`, contributing `d_λ·d_λ = d_λ²` to the trace:

    tr_reg = Σ_λ (d_λ²/|S_3|) χ_λ   ⇒   w_λ = d_λ²/|S_3|.

This is exactly the `atom-mass-full-hecke.md` formula. So:

- **"Why the regular rep and not all channels?"** — the regular rep *is* all
  three channels; the question is the *weights*, and `d_λ²/|S_3|` is forced by
  the multiplicity structure of a left-mult endomorphism trace. "All channels
  equally" (`1/3`) or "all with Jones–Markov `y_λ`" are *different* traces,
  not the endomorphism trace.
- **"Why `full` and not the Jones–Markov trace?"** — the framework's canonical
  knot-invariant trace is Jones–Markov `tr_M = Σ_λ y_λ χ_λ` (Wenzl `y_λ`,
  sign-indefinite). For a single generator that trace = the `std` channel =
  `1.146 > q₀`, i.e. the *divergent* one. The mass is an endomorphism trace
  (regular rep), a genuinely distinct trace from the knot-invariant Markov
  trace; they need not — and here do not — agree.

So the regular-rep choice is principled. The remaining issues are about
**consistency**, not derivation.

## 3. Residual conflation 1 — `tr_M` vs `tr_reg` in the descended term

`∏ V̂_i^std = tr_M = 1.0653` (Jones–Markov) exactly. But the descended term of
`prop:mass-endomorphism-tower` is `|∏ V̂_i^full| = 0.9604` (regular-rep), while
the prose labels it *"the base-level Markov trace
([categorical mass as Markov trace](#prop:categorical-mass-markov))."* These
are two different traces differing by ~10% (ratio 0.9015 proton, 0.9026
neutron). Either the label should read "regular-representation trace" or the
descended term should use the Jones–Markov `∏ std`. This is a naming/convention
reconciliation, not a numerical error.

## 4. Residual conflation 2 — classical vs q-deformed weights

- `atom-mass-full-hecke.md` (line 29): **classical** `w_λ = d_λ²/|S_3|`
  → `(1/6, 4/6, 1/6) = (0.16667, 0.66667, 0.16667)`.
- `terms_2_3_atom_per_gen_mpfr_50dps.py` (lines 234–244): **q-deformed**
  `(dim_q λ)²/[3]_q!` → `(0.16546, 0.66908, 0.16546)` at q₀.

The notation register (`notation-register-table3-data.md`) explicitly
distinguishes `y_λ` (Jones–Markov / Wenzl) ≠ `w_λ` (classical Plancherel) ≠
`w̃_λ` (q-deformed Wedderburn), coinciding only at q=1. The narrative block and
the production code should cite the same one (the code's q-deformed form is the
substrate-correct choice; the `.md` should be updated to match, or vice-versa).

## 5. Dashboard impact

| consumer | uses this tower? | impact of the `full` choice |
|---|---|---|
| headline m_p / m_n / m_e (`m_p_borromean_verification_50dps`, per-observable-100x) | **no** (Borromean vol-density `m=m_e·Vol·ρ/ℏ_q²`) | **none** |
| binding B (triton, low-isotope B/A) + Hecke-path mass cross-checks | **yes** | load-bearing |

For the affected consumers: `full` vs `std` = **finite vs +∞** (proton T2 =
1.618 with `full`; +∞ with `std`, since `|V̂_0^std| = 1.146 > q₀`); T2 is
leading-order; `tr_full` drives B/A swings of ±1–6 MeV/A
(`atom-mass-full-hecke-table-data.md`). So the channel choice does not touch the
headline mass predictions, but it is structural for binding.

## 6. Citation fix (this PR)

`conj:brane-tower-z-habiro` writes "`z_i = |V̂_i|` … from
[algebraic quantum volume](#def:algebraic-quantum-volume)." But
`def:algebraic-quantum-volume` is the `std` projection `V̂_i = z·a_i + b_i`
(= 1.146, divergent), whereas the brane tower needs the **regular-rep**
`|V̂_i^full|` (`prop:mass-endomorphism-tower`). The conjecture text is updated
to cite the `full` object and note the std-vs-full distinction.

## Cross-references

- `content/quantum-observable-universe/mass-theory/hecke-mass-element.md` (`def:hecke-mass-element` — the left-mult endomorphism)
- `content/quantum-observable-universe/observations/atom-mass-full-hecke.md` (the regular-rep `tr_M^full` formula)
- `content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.md` (`def:algebraic-quantum-volume` — the `std` formula)
- `content/quantum-observable-universe/mass-theory/mass-endomorphism-tower.md` (`prop:mass-endomorphism-tower` — descended term)
- `content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md` (`conj:brane-tower-z-habiro` — citation fixed)
- `docs/audits/2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md` (PR #2467 — the pin this continues)
- witnesses: `brane-tower-full-channel-trace-audit`, `zhabiro-physical-z-pin`, `terms-2-3-atom-per-gen-mpfr-50dps`
