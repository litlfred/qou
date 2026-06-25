# SDP interface-operator selection — derivation or per-isotope fit?

**Date:** 2026-06-25
**Branch:** `claude/great-ramanujan-g5m05s`
**Probe:** [`computations/probe_sdp_interface_selection.py`](../../computations/probe_sdp_interface_selection.py)
**Witness:** [`computations/probe-sdp-interface-selection.witness.json`](../../computations/probe-sdp-interface-selection.witness.json) (audit-only, EXPLORATORY)
**Beans advanced:** `w5tg` (Lever 2 edge-set/occupancy), `z2bn` (Lever 1 fibre kernel; magic-A kill-switch), `thb7` (Lever 3 universal-ρ)

## The question

Canonical-chain step 10 specifies the inter-nucleon interface as the
confinement-SDP minimiser `T_w = argmin_{GB-NF} ‖tr_M(T_w)·𝔈₀ − B_tgt‖`
over the discrete, parameter-free Gröbner–Shirshov normal-form crossing
menu. The production word builder
[`mass_at_3A_proper.atom_braid_word_3A`](../../computations/mass_at_3A_proper.py)
instead **hardcodes** the p-n interface to the color-weighted averaged
crossing `σ − h·(½ − δ/4)·1` at generator `3k+2`.

**Owner's architectural point:** wire the actual SDP selection in rather
than hardcode. **The sharp guard:** an SDP that re-selects the interface
*per isotope* to minimise `‖B − B_AME‖` is a tautology — every
`B = B_AME`, zero predictive content. The only non-fitting version is a
**single** canonical interface selected **jointly** over the whole tower,
which must then **predict** each isotope. This probe decides which regime
we are in **before** mutating the canonical word builder (consumed by
~19 scripts).

## Structural leverage — why one knob is weak

The binding factorises over 2-nucleon bonds (audit
`2026-06-16-b-sym-linear-chain-closed-form`):

```
B_sym(Z,N) = α·[ (Z−1)·L_pp + L_pn + (N−1)·L_nn ],   α = E₀ ≈ 4.186 MeV
```

The interface operator enters **only through `L_pn`** — a single bond out
of the `(A−1)` adjacency bonds. p-p (`σ`) and n-n (`σ⁻¹`) are
isospin-fixed. So re-selecting the interface can move the deuteron freely
(it *is* the single p-n bond) but barely touches the heavy isotopes.

**Closed form (validated to colinearity resid 6.7e-52, this probe's
preflight).** The p-n crossing appears once as `(c·σ + d·1)`; χ^λ is
linear in that factor, so `tr_M^atom(1,1; c,d) = c·t_σ + d·t_I` with
`t_I = t_free` (inserting the identity at the bond = the free word, the
structural identity confirmed to 1.7e-16). Hence
`L_pn(c,d) = ln( t_free / (c·t_σ + d·t_I) )` — exact, sweeps any interface
(discrete menu or continuous fit) from two base traces.

## Results (q₀ = 1.10998, α = 4.186 MeV)

### Test A — discrete GB-NF menu, one interface for the whole tower

`err = B/B_AME`; each row is the *same* interface applied to every isotope.

| interface (c·σ+d·1) | L_pn | B_D | ²H | ³H | ³He | ⁴He | ⁶Li | ⁷Li |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| identity `1` (L₀) | 0.000 | 0.00 | 0.000 | 0.610 | 0.377 | 0.286 | 0.505 | 0.544 |
| `e₊` (q-sym proj) | 0.362 | 1.52 | 0.681 | 0.789 | 0.573 | 0.339 | 0.553 | 0.583 |
| `σ` (d=0) | 0.695 | 2.91 | 1.307 | 0.953 | 0.753 | 0.388 | 0.596 | 0.618 |
| `σ−h/2` (blind avg) | 0.929 | 3.89 | 1.749 | 1.069 | 0.881 | 0.423 | 0.627 | 0.643 |
| **`σ−h(½−δ/4)` CANON** | 0.929 | 3.89 | 1.749 | 1.069 | 0.881 | 0.423 | 0.627 | 0.643 |
| `σ⁻¹` (d=−h) | 1.237 | 5.18 | 2.328 | 1.221 | 1.048 | 0.469 | 0.667 | 0.676 |
| `e₋` (q-antisym proj) | 1.192 | 4.99 | 2.243 | 1.199 | 1.023 | 0.462 | 0.661 | 0.671 |

- **No single menu element gives `err ≈ 1` across the tower.** ²H swings
  0 → 2.33 (it is pure interface); **⁴He is pinned to 0.29–0.47 regardless
  of the interface** (1 p-n bond among its chain bonds); ⁶Li/⁷Li pinned to
  ~0.5–0.68.
- **The canonical `σ−h(½−δ/4)` is the joint-tower-optimal discrete element**
  (min `Σ(ln err)² = 1.485`). The hardcoded convention is *vindicated* as
  the best parameter-free choice — selecting jointly over the menu returns
  the value already in production.

### Test B — the mirage matrix (per-isotope fit ⇒ no prediction)

Fit the continuous interface to the **row** isotope (forcing `err = 1.000`,
the diagonal), then **predict** the **column** isotope with that same `d*`.

| fit-on / predict | ²H | ³H | ³He | ⁴He | ⁶Li | ⁷Li | d* |
|---|---:|---:|---:|---:|---:|---:|---:|
| ²H | **1.000** | 0.873 | 0.665 | 0.364 | 0.575 | 0.601 | +0.0884 |
| ³H | 1.485 | **1.000** | 0.805 | 0.402 | 0.609 | 0.628 | −0.0451 |
| ³He | 2.163 | 1.178 | **1.000** | 0.456 | 0.656 | 0.667 | −0.1825 |
| ⁴He | 9.085 | 2.993 | 2.995 | **1.000** | 1.137 | 1.059 | −0.4913 |
| ⁶Li | 7.113 | 2.476 | 2.427 | 0.845 | **1.000** | 0.947 | −0.4765 |
| ⁷Li | 8.045 | 2.721 | 2.696 | 0.918 | 1.065 | **1.000** | −0.4854 |

The diagonal is 1.000 **by construction** (the tautology). The
off-diagonal is wildly off — fitting ⁴He's interface mispredicts ²H by
**9.09×**; fitting ²H mispredicts ⁴He by 2.7×. **Per-isotope interface
fitting buys exactly zero predictive content.**

### Test C — joint best single continuous interface (leverage ceiling)

Best `d* = −0.0831` (close to canonical −0.1045), `L_pn = 0.877`:

| isotope | B | B_AME | err |
|---|---:|---:|---:|
| ²H | 3.669 | 2.225 | 1.649 |
| ³H | 8.847 | 8.482 | 1.043 |
| ³He | 6.577 | 7.718 | 0.852 |
| ⁴He | 11.754 | 28.296 | 0.415 |
| ⁶Li | 19.840 | 31.994 | 0.620 |
| ⁷Li | 25.018 | 39.245 | 0.637 |

Even the *optimal* single interface leaves an **irreducible 2.41× ceiling**
(²H wants weak binding, ⁴He wants strong; one knob cannot satisfy both).

## Verdict — scope-limited negative (a)

Per AGENTS.md §"Before declaring refuted / ruled out (STRICT)", classified
as **(a) a scope-limited negative**, *not* (b) a structural exclusion:

> **SDP-selecting the p-n interface operator, _alone_, does not reproduce
> the binding tower.** It can fit a single anchor isotope (tautology) but
> mispredicts the rest by 2–9× (Test B). The interface moves only `L_pn`
> (1 of the `A−1` chain bonds); the tower-wide under-binding (⁴He ≈ 0.42×,
> roughly uniform for A ≥ 4) is a collective / magic-A / operator-valued
> effect the per-bond linear chain omits — it cannot be repaired by
> re-selecting one bond's crossing.

This is **not** a claim that the interface operator is excluded from any
closure (no proved invariant forbids it). It constrains *what one knob can
do*, not *which ingredients may appear*. The interface remains a valid,
canonical building block; the probe measures the *size of the missing
collective term*, exactly as the multi-term-closure permanence principle
in AGENTS.md anticipates.

## Recommendation

1. **Do NOT wire per-isotope SDP selection into `atom_braid_word_3A`** — it
   would be fitting (Test B). The ~19 consumers are safe; no change.
2. **The hardcoded canonical interface `σ − h(½−δ/4)` stands** — it is the
   joint-tower-optimal discrete-menu element (Test A), so the principled
   "select jointly over the GB-NF menu" returns the production value. If a
   future agent *does* wire a selection step, it must be **joint-tower**,
   and it will reproduce the current hardcode (worth a one-line assertion
   in the word builder citing this audit, rather than a behavioural change).
3. **The productive direction is the collective binding factor**, not the
   interface: the magic-A / operator-valued / Δ_λ closure (beans `w5tg`,
   `z2bn`, `thb7`; Δ_λ gate in AGENTS.md). The 2.41× ceiling here is the
   same gap those levers target — this probe quantifies that the interface
   sub-problem is *closed* (canonical = optimal) and the open residual is
   entirely collective.

## Follow-up — structural form of the collective residual

Probe: [`computations/probe_collective_binding_residual.py`](../../computations/probe_collective_binding_residual.py)
(EXPLORATORY; witness `probe-collective-binding-residual.witness.json`).

Having established the residual is collective, this follow-up pins down its
**structural form** (formalize-first; **no** closed-form fit — Δ_λ gate
stands). Per-nucleon binding across ²H–¹⁶O (B_sym = the canonical-interface
linear chain):

| iso | A | B_sym | B_AME | F=AME/sym | B_sym/A | B_AME/A |
|---|--:|--:|--:|--:|--:|--:|
| ²H | 2 | 3.890 | 2.225 | 0.572 | 1.945 | 1.112 |
| ³H | 3 | 9.068 | 8.482 | 0.935 | 3.023 | 2.827 |
| ³He | 3 | 6.797 | 7.718 | 1.136 | 2.266 | 2.573 |
| ⁴He | 4 | 11.975 | 28.296 | 2.363 | 2.994 | **7.074** |
| ⁶Li | 6 | 20.060 | 31.994 | 1.595 | 3.343 | 5.332 |
| ⁷Li | 7 | 25.238 | 39.245 | 1.555 | 3.605 | 5.606 |
| ⁹Be | 9 | 33.323 | 58.164 | 1.745 | 3.703 | 6.463 |
| ¹²C | 12 | 44.315 | 92.162 | 2.080 | 3.693 | 7.680 |
| ¹⁶O | 16 | 60.486 | 127.619 | 2.110 | 3.780 | 7.976 |

Two honest signals (an initial "B_sym/A is globally monotone, B_AME/A peaks at
⁴He" hypothesis was **refuted** by the data — B_sym/A wiggles with isospin
composition and the *global* B/A peak is ¹⁶O; the real signal is the **local**
⁴He spike):

- **(A) General collective under-binding (grows with A).** `F = B_AME/B_sym`
  rises 0.94 (³H) → 2.11 (¹⁶O); `B_sym/A` saturates ~3.8 while `B_AME/A`
  climbs to ~8.0. The per-bond chain misses a non-additive term that grows
  with A — the tower-wide face of the 2.41× interface-probe ceiling.
- **(B) ⁴He α-magic local spike.** Over the linear A=3↔A=6 interpolation of
  `B/A`, ⁴He's excess is **+98% in AME** but only **+4% in B_sym** — the
  additive sum of fixed bond constants is smooth through A=4 and **cannot**
  produce a doubly-magic α-core singularity.

**Narrowing (scope-(a), no exclusion):** the missing physics is collective;
the ⁴He spike fingerprints a **4-body α-core (⁴He / Borromean)** term, **not**
a per-bond or pairwise correction. This is consistent with the magic-volume's
"exact-at-⁴He" construction and points the keystone (beans `w5tg`/`z2bn`/
`thb7`, A=4 interface operator [#2750](https://github.com/litlfred/qou/pull/2750),
s5-so3 4-body assembly) at the 4-body channel — away from any per-bond
collective ansatz.

## Reproduce

```bash
cd computations && python3 -u probe_sdp_interface_selection.py    # interface (A/B/C)
cd computations && python3 -u probe_collective_binding_residual.py # collective form
```

Pure-python (no `pyhecke_native`); runs in seconds — the whole tower comes
from three 6-strand traces (L_pp, L_pn, L_nn) plus the linear interface
model.
