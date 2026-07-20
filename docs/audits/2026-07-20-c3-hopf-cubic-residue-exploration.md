# Q_β `c_3` — Hopf-cubic analytic-residue exploration: DERIVED-MODULO-OPEN-NORMALIZATION

**Date:** 2026-07-20 · **Bean:** `qou-1dnr` (c_3 → Q_β 100× gap-closer) ·
**Branch:** `claude/argument-principle-residue-sum-2026-07-20`
**Axis:** c_3 / Q_β bar-odd decay face / 1ppQ · **Tier:** numerical scope-(a)
exploration + a sorry-free formalize-first structural narrowing ·
**Discipline:** no fit (nothing inverted from Q_β / CODATA to tune c_3), no c_k
wired, nothing to production, no tier change.

> **Read the registry, not this doc, for `c_3`'s tier.** The authoritative
> per-rung status is
> [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
> §3/§9 (KC20/KC21/KC22). This doc records the redirect the three 2026-07-20
> routes triangulated to, and how far it gets. It changes no tier.

## 0. The route (the redirect, not a fourth independent route)

The three 2026-07-20 routes all landed NEGATIVE and pointed to the **same** open
piece:

| route | verdict | redirect |
|---|---|---|
| DM-cubic / Berezinian ([audit](2026-07-20-c3-dm-cubic-derivation-attempt.md)) | scope-(a) NEG | genuine target is the SMOOTH bar-odd `S = h·D(ũ)`, not a swinging real-q c_3 |
| Habiro growth-dichotomy ([audit](2026-07-20-c3-habiro-route.md)) | scope-(b) class-REFUTED | the ladder is GEOMETRIC (simple pole at `u_sub`) ⇒ c_3 is the ANALYTIC RESIDUE, not a formal Habiro series |
| GGM-Stokes ([audit](2026-07-20-c3-stokes-route.md)) | scope-(a) NEG | a FLAT (anchor-invariant) datum is CORRECT; open piece = the NORMALIZED §4e bridge |

The corpus already gives the EXACT carrier (KC20, Lean-proved in
[`QBetaZeta4ResidueRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean)):

    Δ_net^odd = (h/4)·C(y),  h = q − q⁻¹,  y = q²+q⁻² = 2cosh 2λ,
    C(y) = y³ − 4y² + 3y − 2   (irreducible/ℚ, disc −152, S₃; Hopf double-crossing sector).

So the open piece is the **residue / normalization** from this exact carrier to
the c_3 rung. This exploration evaluates it and asks — brutally — whether the
normalization is corpus-principled or a fit.

## 1. Results (two-anchor, no fitting)

Probe
[`computations/probes/qbeta_c3_hopf_cubic_residue_probe.py`](../../computations/probes/qbeta_c3_hopf_cubic_residue_probe.py)
→ `qbeta-c3-hopf-cubic-residue.witness.json` (mpmath, audit_only). Anchors:
proton-pinned `q₀ = 1.10997858275…`, muon-pinned `q₀ = 1.10997859555…`
(Δq ≈ 1.3×10⁻⁸).

| quantity | proton | muon | swing |
|---|---|---|---|
| **EXACT carrier `(h/4)·C(y₀)`** | **−0.21114057** | **−0.21114059** | **−1.1×10⁻⁵ %** (FLAT) |
| — Hopf-sector piece `(h/4)·C_Hopf(y₀)` | −0.10909440 | — | — |
| empirical `c_3` (CODATA-anchored) | −2.0693426 | −2.0202002 | +2.4325 % |
| — bar-EVEN part ≈ `−Vol(4₁)` | −2.0298832 | −2.0298832 | 0 (exactly measured) |
| — bar-ODD part `S = c_3 + Vol(4₁)` | **−0.0394594** | **+0.0096830** | **sign-SWING** (KC21) |
| anchor-blind physical `|S|` scale (Φ_b state integral) | ≈ 0.0094 | ≈ 0.0094 | 0 |

Three clean facts:

1. **The EXACT carrier is anchor-INVARIANT (flat).** `(h/4)·C(y₀) ≈ −0.2111`,
   swing `1×10⁻⁵ %` — five orders below the empirical c_3 swing. Per route C /
   KC21 this is the **CORRECT** type for a derived object: the extracted-c_3
   "swing" is the `1/u³` ladder-inversion of a smooth zero, NOT the obstruction.
   The bar-EVEN part of c_3 is confirmed `= −Vol(4₁)` exactly.

2. **The bar-odd target `S` ITSELF swings SIGN** (p −0.0395 / μ +0.0097). So NO
   flat object equals `S` at both anchors (the same anchor-invariance wall the
   sibling routes hit; Lean `flatCarrier_cannot_match_swinging_S`). The fair,
   anchor-blind target is the physical `|S|` scale ≈ 0.0094 (the Φ_b
   state-integral volume deficit, capstone
   [2026-07-12](2026-07-12-c3-wall-resolution-capstone.md)).

3. **No corpus-named normalization maps the carrier onto `|S|` un-tuned.** The
   required `N_geom = |S|/|carrier| ≈ 0.0445`. Candidates tested at the proton
   anchor: `h² = 0.0437` (**1.8 % off** — closest, a near-coincidence, not a
   match), `ℏ_q² = 0.0098`, `u_sub = 0.0085`, `u_sub² = 7.3×10⁻⁵`,
   `u_sub³ = 6.2×10⁻⁷`, `u_sub⁴ = 5.3×10⁻⁹`, `1/(4q⁷) = 0.120`, `z = 0.499`.
   None hits `N_geom` within 1 %. A hand-picked `N` is a **fit**.

## 2. The sharp structural narrowing (the honest positive content)

Both the target `S = h·D(ũ)` (KC21) and the carrier `= (h/4)·C(y)` (KC20) are
**bar-odd**, so both factor as `h·(bar-even)`. The bar-odd carrier `h` cancels in
the ratio (Lean `carrier_to_S_normalization_is_barEven`, sorry-free):

    N = S / carrier = h·D / ((h/4)·C) = 4·D(ũ) / C(y)   (bar-even / bar-even).

**The shared `h` is AUTOMATIC bookkeeping, not a match** — *any* bar-odd Laurent
object factors as `h·(bar-even)`. So the exact cubic supplies only the automatic
bar-odd chirality carrier. The **genuine open content is exactly the bar-even
ratio `4D/C`**, and:

- `C(y)` is a **fixed degree-3 polynomial value** (the Hopf-sector cubic, KC20);
- `D(ũ)` is the **KC22 resurgent / non-holonomic ℚ(√3) ladder** (radius → 0,
  proved NOT low-order (q-)holonomic in any tested class).

Therefore `N = 4D/C` is **as transcendental as `D`**. The exact cubic does NOT
supply the bar-even normalization. Implied ladder values `D = S/h`: proton
−0.18875, muon +0.04632 (carrying the whole KC21 representation swing).

This is a real narrowing: it reduces the open normalization from "all of `S`" to
"the bar-even ratio `4D/C`", and identifies that ratio with the pre-existing
KC22 resurgent keystone — it does **not** produce a new closure.

## 3. Fibre-branch subtlety (route C)

The carrier is evaluated at the real substrate `q₀` (observable/archimedean
level). Per route C the unsuppressed contribution to the c_3 rung lives on the
fibre branch (`|q| = 1`, complex q). The carrier `(h/4)·C(y)` is a Laurent
polynomial and extends to the fibre trivially, but the **bar-even ladder `D(ũ)`
is the resurgent object** — the fibre-vs-observable distinction does not rescue
the normalization: `D` is transcendental on either level (KC22). The flat
real-`q₀` carrier value is the correct anchor-blind magnitude handle; the
normalization is where the fibre-level resurgence enters, and it stays open.

## 4. Verdict — DERIVED-MODULO-OPEN-NORMALIZATION (scope-(a))

- The exact Hopf-cubic carrier `(h/4)·C(y₀)` is the **correct flat object**
  (route C type test PASS) and supplies the automatic bar-odd factor `h` of
  `S = h·D`.
- The bar-odd **channel is NOT derived**: the normalization `N = 4·D(ũ)/C(y)` is
  the bar-even ratio, and `D(ũ)` is the KC22 resurgent ladder — no corpus-named
  quantity supplies it un-tuned (closest `h²`, 1.8 % off, a coincidence).
- **Q_β does NOT meet its 100× target (7.8 ppb) via this route** — no derived
  c_3 is produced; nothing is wired; the honest production state stays
  **c_2-only** (registry §6).

This is **scope-(a)**: "the exact cubic carrier, alone, does not reproduce the
bar-odd c_3 as-is." It is NOT a scope-(b) exclusion of the residue route — the
normalized bridge (a geometric determination of `D(ũ)` fixing the `|S|` scale)
remains the genuine open target (`conj:qdifference-kernel-prolongation-symbol`,
the §4e quantum-modularity / 3d-index bridge).

## 5. Formalize-first (sorry-free, lean-direct verified, Lean 4.24.0)

[`QOU/Mass/QbetaC3HopfResidue.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3HopfResidue.lean)
— generic `{R} [CommRing R]` (§7c; one `Field` restatement for the literal
`4D/C` ratio; no `ℝ`):

- `carrier_to_S_normalization_is_barEven` (sorry-free) — from `4·carrier = h·C`
  and `S = h·D`, the `h` cancels: `S·C = 4·D·carrier`. The normalization is the
  bar-even `4D/C`.
- `normalization_eq_four_D_over_C` (sorry-free, `Field`) — the literal
  `S/carrier = 4·D/C`.
- `flatCarrier_cannot_match_swinging_S` /
  `flatCarrier_misses_other_anchor_by_full_swing` (sorry-free) — a flat carrier
  matches the sign-swinging `S` at most one anchor.
- `HopfCubicResidueBridge` — content-bearing **primary conjecture class**
  (`carrier_factorization`, `smoothS_factorization`, `bridge_closes`,
  `bridge_nontrivial`, `smoothS_nonzero`), **no instance**: the honest open §4e
  geometric-normalization bridge.

## 6. Discipline (§Axiomatization is NOT a Proof, §3b, registry §8)

- [x] `c_3` NOT inverted from Q_β to claim a derivation. The CODATA-anchored
      c_3 / S are the comparison target ONLY; the carrier is CODATA-independent
      (KC20 categorical).
- [x] The irreducible-cubic fact (KC20) is respected as "no real-q **root**",
      not "no real-q **value**": the probe evaluates `C(y₀)` (a value) and does
      not seek a root.
- [x] Negative labelled **scope-(a)** (construction insufficient alone); the
      only structural EXCLUSIONS cited (KC20/KC22) are pre-existing, Lean-proved.
- [x] Lean file content-bearing, sorry-free, conjecture class instance-free.
- [x] No `c_k` wired; no production; no tier change; no
      appendix-mass-binding-algorithms change (negative probe). Bean `qou-1dnr`
      STAYS OPEN.

## References

- Probe: [`qbeta_c3_hopf_cubic_residue_probe.py`](../../computations/probes/qbeta_c3_hopf_cubic_residue_probe.py)
  + `qbeta-c3-hopf-cubic-residue.witness.json`.
- Lean: [`QOU.Mass.QbetaC3HopfResidue`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3HopfResidue.lean);
  carrier KC20 [`QOU.QBeta.Zeta4Residue`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean).
- Carrier narrative: [`rem:qbeta-odd-carrier-hopf-cubic`](../../content/quantum-observable-universe/mass-theory/qbeta-odd-carrier-hopf-cubic.md).
- Sibling routes: [DM-cubic](2026-07-20-c3-dm-cubic-derivation-attempt.md),
  [Habiro](2026-07-20-c3-habiro-route.md), [Stokes](2026-07-20-c3-stokes-route.md).
- Target / capstone: [`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md).
- Registry (authoritative tier): [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
  §9 KC20 (real-q root excluded), KC21 (`1/u³` smooth-zero), KC22
  (resurgent/non-holonomic `D`).
