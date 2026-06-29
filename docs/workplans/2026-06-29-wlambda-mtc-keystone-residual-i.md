# 2026-06-29 — W_λ keystone residual (i): owner-opened MTC-matching workplan

**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre kernel `R(q,x)`), parent keystone `s5bb`/`08a2`.
**Branch:** `claude/wlambda-mtc-keystone-residual-i-2026-06-29`
**Scope tag:** Subgoal-2, **owner-opened 2026-06-29** (explicit direction to work residual (i)).
**Status:** intent / mapping — no construction yet, no fit, nothing wired.

## Why this is open now

The owner directed (2026-06-29) opening the **single genuine remaining derivation**
of the lever-1 binding kernel. Per `.beans/z2bn` Stages 6–9 (concluded 2026-06-28)
and [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md):

- The kernel is `R(q,x) = x² − τx + 1` (depth-2, `det B = 1`; Lean sorry-free).
  The whole lever reduces to **one number** `τ = tr B = 2.6424` at q₀.
- **Algebraic / fibre side: CONCLUDED.** `τ = 3(3[2]²+2)/(4([2]+2))` is bar-even
  (`tau_quantum_integer_form`, sorry-free). The binding correction tower `D(m)`
  is fully characterized through m=11 as generic bar-symmetric residues — no finite
  q-special-function closed form (Stages 6–9). Further algebraic probing has
  diminishing returns; it has handed the geometric side a complete exact target.
- **Geometric `tr B` side: REDIRECTED to residual (i).** All three natural
  color-`E_q` elliptic candidates miss (loop monodromy integer-trace; path
  transport `θ_spec=0.0141`, ~55× small; intrinsic Tate period `5.847`, 6.5× large
  — [`2026-06-25-lever1-color-eq-lambda-sw-rapidity.md`](../audits/2026-06-25-lever1-color-eq-lambda-sw-rapidity.md)).
  So `θ_binding` is **not** a color-`E_q` period; its geometric origin is the
  **`W_λ`-side Plancherel/MTC localization** = keystone **residual (i)**.

## Residual (i) — the exact open statement

From the s5-so3 keystone ledger (residual (i), owner-gated until 2026-06-29):

> Pin the Beasley–Witten gauge datum on `S³/2I` to the Hecke `Rep U_q(sl_N)`
> blocks so the localization `W_λ = d_q²/D²` is provably **OUR** Hecke category's
> Plancherel measure, not "some MTC's".

What is already closed on this keystone (residual (ii), 2026-06-24):

- `restriction_intertwines_conjugation` (∀λ⊢5), `std_irrep_conjugation_fixed`,
  capstone `reeb_eq_restriction_scaffold [BringFiberAction]` — all `#print axioms`
  clean. These discharge the **algebraic** restriction-commutes-with-conjugation
  identity; the geometric fibre map (`BringFiberAction` class) stays open.

## Plan (formalize-first; smallest genuine increment first)

This is genuine multi-session DG; the discipline is to find the smallest
**formalizable structural claim** that advances residual (i), not to leap.
Candidate decomposition (to be refined by the in-flight corpus map):

1. **State the Plancherel/Verlinde target as a Lean structure.** `W_λ = d_q²/D²`
   for the Hecke category `Rep U_q(sl_N)` at the substrate `q₀` — quantum dims
   `d_q(λ)`, global dim `D² = Σ_λ d_q(λ)²`. Check whether the corpus already
   carries `d_q`, `D²`, and the Markov/Plancherel measure (much of the q-dim
   machinery exists; see `dim_q` / Wedderburn blocks).
2. **The MTC-matching obligation.** The open content is the identification of the
   Chern–Simons / WRT(`S³/2I`) localization weight with this categorical
   Plancherel measure — i.e. that the gauge-theory `W_λ` *is* `d_q²/D²` for *our*
   category. Isolate this as a single `[class]` field (§3b-cond) so downstream
   `tr B` results become rigorous-conditional, not unproved-flat.
3. **The bridge to `τ`.** Record (conditionally) how `W_λ = d_q²/D²` feeds
   `tr B → τ → R(q,x)`. Only assert what the map actually derives.

**Guardrails (STRICT).** No 7th fit-based ansatz (Δ_λ rule stands). No fit on
`τ`; the algebraic side already fixed `τ` exactly — the geometric side must
*derive* the same number, not tune to it. Scope every negative as (a) unless a
proved invariant licenses (b). Coordinate on #2722 / #2744 before constructing.

## Increment 1 (2026-06-29) — MTC-matching obligation formalized, sorry-free

[`QOU/BraidKnot/WLambdaMTCLocalizationObligation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaMTCLocalizationObligation.lean)
(lean-direct verified, exit 0, sorry-free; generic `{R : Type*} [Field R]` per §7c).

- `class BeasleyWittenLocalization R` carries residual (i)'s **matching obligation** as its single
  unproved field: `loc p = d_q(p)² / D²`, `D² = Σ_λ d_q(λ)²` — exactly what the owner-gated gauge
  datum on `S³/2I` must deliver. The gauge datum is **not** constructed; it is the hypothesis.
- Derived (non-tautological, §3b-cond):
  - **C1** `loc_isProbabilityMeasure : Σ_λ loc λ = 1` — the genuine Plancherel `D²` normaliser
    forces `Σ = 1` (the 2026-06-20 C1 normalization, now a theorem for any matching localization).
  - **C2** `loc_conj_eq : loc λ′ = loc λ` — transports the corpus-proved `qDim_conj`
    (`KeystoneC2QDimTranspose`, sorry-free) onto the gauge-theory weight via the matching.
- Non-vacuity: `instance localization_two : BeasleyWittenLocalization ℚ` (n=2 blocks, `d_q≡1`,
  `loc≡1/2`) — confirms the conditional theorems are not conditional-on-`False`.

**What this buys:** C1 + C2 are now **necessary conditions any gauge datum must satisfy** — a
falsifiable constraint on the owner-gated search (a localization whose weight is unnormalized or
chirality-asymmetric cannot be the Hecke Plancherel measure). It does **not** close residual (i).

**Coupling found (CORRECTED 2026-06-29):** I first wrote `D² = Σ d_q² = [n]_q!`. The `= [n]_q!` is
**false** — `Σ d_q² = [n]_q!` does not hold at generic q (disproved n=2..5; see
[`2026-06-29-wedderburn-trace-identity-false-at-generic-q.md`](../audits/2026-06-29-wedderburn-trace-identity-false-at-generic-q.md)).
`D² = Σ d_q²` is its own q-polynomial; `heckeLocalization` carries `D² ≠ 0` as a hypothesis (via
`globalDim_ne`) and never needs `[n]_q!`. For `1 < q` it is discharged directly from positivity
(`qBracket_pos`/`qFactorial_pos` ⇒ `d_q > 0`), independent of any Wedderburn identity — a clean
follow-up increment.

## Infrastructure (2026-06-29) — keystone Lean cone builds; `lake build` is unusable here

The keystone cone (`KeystoneC2QDimTranspose`, `IdentityIPlancherelConditional`,
`WLambdaDefectClosedForm`, + deps, + this increment) **builds sorry-free** against the restored
`lake-cache/qou-v4-24-0` oleans (mathlib 2951, QOU 208→209). Two hard env facts found:

1. **`lake build` is destructive + blocked here.** The git proxy is **repo-scoped to litlfred/qou**,
   so `lake` 403s on every dependency repo (mathlib/Qq/batteries) and, finding no `.git` in the
   restored package dirs, **deletes the 2951 mathlib oleans** and tries to re-clone. **Never run
   `lake build` in this sandbox** — it wipes the cache. Re-restore from `lake-cache/qou-v4-24-0` if
   it happens.
2. **Working verification = per-module `lean`-direct** against restored oleans, with the qou package
   option `-D autoImplicit=false` and `--root=$PKGROOT` (else spurious `Field ?m` / instance
   errors). Olean root suffix is `build/lib/lean` (extra `lean/`). Use the toolchain's own `lean`
   binary; only **`lake`** triggers the elan→`release.lean-lang.org` 403.

```bash
export PATH="$HOME/.elan/bin:$PATH"; ROOT=$(pwd)
LEANBIN=~/.elan/toolchains/lean-v4.24.0/bin/lean
PKGROOT="$ROOT/content/quantum-observable-universe/lean"; LIBOUT="$PKGROOT/.lake/build/lib/lean"
LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':'); LP="$LP$LIBOUT"
compile(){ local m="$1" s="$PKGROOT/${1//.//}.lean" o="$LIBOUT/${1//.//}.olean"; mkdir -p "$(dirname "$o")"
  env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 "$LEANBIN" -D autoImplicit=false --root="$PKGROOT" \
    -o "$o" -i "${o%.olean}.ilean" "$s"; }
compile QOU.BraidKnot.WLambdaMTCLocalizationObligation   # exit 0, sorry-free
```

(The `lake-cache/qou-v4-24-0` seed ships only the partial 202-olean QOU set; the keystone cone is
now built on disk. Re-seeding to capture it is owner-gated — a force-push to a load-bearing infra
orphan branch.)

## Increment 2 (2026-06-29) — real Hecke q-Plancherel wire-up

Strengthened Increment 1 (same file, now imports `KeystoneC2QDimTranspose`; compiles sorry-free
against the real cone via the lean-direct recipe below).

- `noncomputable def heckeLocalization (q P hsorted hconj hD) : BeasleyWittenLocalization ℝ` builds
  the obligation class on the **genuine** Hecke q-dimension `qDim` (`d_q = [n]_q!/∏[h_c]_q`), with
  `loc = d_q²/D²` (`loc_matches` = `rfl`) and the `qDim_conj` field **discharged by the
  corpus-proved `QOU.BraidKnot.IdentityI.qDim_conj`** — no longer carried abstractly.
- Consequence: C1 (`loc_isProbabilityMeasure`) + C2 (`loc_conj_eq`) now hold for the **actual** Hecke
  Plancherel measure of any conjugate-closed sorted block set `P`, modulo only `D² ≠ 0`.
- `D² ≠ 0` is the sole remaining structural input — `D² = Σ d_q²` is its own q-polynomial, **not**
  `[n]_q!` (that identity is false at generic q; audit
  [`2026-06-29-wedderburn-trace-identity-false-at-generic-q.md`](../audits/2026-06-29-wedderburn-trace-identity-false-at-generic-q.md)).
  Dischargeable from positivity for `1 < q`; carried as a hypothesis.

## Increment 3 (2026-06-29) — `D² ≠ 0` discharged from positivity (last input derived)

Same file, sorry-free, cone-verified. `qDim_pos` (`1 < q ⇒ 0 < d_q(λ)`, from `qFactorial_pos` +
`qBracket_pos` + `one_le_hookLength` + a `foldl_mul_pos` helper) ⇒ `sum_qDimSq_pos`
(`0 < Σ_λ d_q²` on nonempty `P`) ⇒ `heckeLocalizationOfPos` builds the obligation class with
`globalDim_ne` **derived** (no longer a hypothesis), for `1 < q` (the substrate regime) and
nonempty `P`. So residual (i)'s necessary conditions C1+C2 now hold for the actual Hecke Plancherel
measure with **zero** remaining structural inputs beyond `1 < q`, `P` sorted + conjugate-closed +
nonempty — none of them the false `Σ d_q² = [n]_q!`.

## Open log

- 2026-06-29: branch + intent; corpus map of residual (i) dispatched.
- 2026-06-29: Increment 1 — MTC-matching obligation class + C1/C2 derived, sorry-free (lean-direct).
- 2026-06-29: built the keystone Lean cone; recorded the `lean`-direct recipe (`lake build` is
  destructive + proxy-blocked here). Increment 1 re-verified against the real cone (exit 0).
- 2026-06-29: Increment 2 — `heckeLocalization` wires the real `qDim` + corpus-proved `qDim_conj`
  into the obligation (sorry-free, cone-verified); only `D² ≠ 0` remains as input.
- 2026-06-29: picking up "#2743" (`Σ d_q² = [n]_q!`) found the target is **false** at generic q
  (disproved n=2..5); wrote audit, corrected the conflation. The correct q-identity is the Poincaré
  `[n]_q! = Σ_λ f^λ·q^{b(λ)}·d_q(λ)`; the vector-space `Σ(f^λ)²=n!` is already proved (#2724).
- 2026-06-29: Increment 3 — discharged `D² ≠ 0` from positivity (`qDim_pos`, `1 < q`), so
  `heckeLocalizationOfPos` has no remaining structural input beyond the trivial block-set facts.
