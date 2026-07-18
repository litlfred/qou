# α_EM per-loop `2` unification: the Hecke channel-swap is a *holomorphic* modular involution `τ↦½−τ`, not anti-holomorphic conjugation — a holo-vs-anti-holo obstruction

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure (the single load-bearing wall) ·
**Tier:** exact modular algebra (scope-(a) — sharpens the unification to a precise
obstruction; does NOT close it) · **Discipline:** no fit, nothing wired, `1/(8π)`
stays a phase-4 identification.

## The remaining wall, and this attack

After #3936 established that the involution swapping the Hecke channels
`e₊ ↔ e₋` is the eigenvalue-exchange `q ↦ −q⁻¹` (the bar involution `q ↦ q⁻¹`
FIXES the channels), the per-loop wall reduces to one correspondence: does the
τ-functor identify `q ↦ −q⁻¹` with the Hodge conjugation `H^{1,0} ↔ H^{0,1}`
(#3920) — the sibling conjecture-statement audit's "as complex conjugation
swaps `H^{1,0} ⊕ H^{0,1}`"? This is the hard open attack; this probe takes it to
an honest obstruction.

## Result (exact, verified to 1e−20)

Mapping each `q`-involution through the standard nome `q = e^{2πiτ}` (τ the
modular parameter of the Bring Jacobian's elliptic factor `E`,
`Jac(Bring) ~ E⁴`):

| `q`-involution | modular involution | analytic type |
|---|---|---|
| bar `q ↦ q⁻¹` | `τ ↦ −τ` | holomorphic |
| **channel-swap `q ↦ −q⁻¹`** (#3936) | **`τ ↦ ½ − τ`** | **holomorphic** |
| Hodge conjugation `H^{1,0} ↔ H^{0,1}` | `τ ↦ −τ̄` | **anti-holomorphic** |

`τ ↦ ½ − τ` is a half-period shift composed with `τ ↦ −τ` (an Atkin–Lehner-type
holomorphic involution), and it is an involution (`½ − (½ − τ) = τ`).

**The obstruction.** The channel-swap corresponds to a **holomorphic** modular
involution; Hodge conjugation is **anti-holomorphic** (`τ ↦ −τ̄` depends on `τ̄`).
At any point with `Re τ ≠ ¼` the two images differ, so **a holomorphic τ-functor
cannot identify the Hecke channel-swap with Hodge conjugation directly** — they
are of different analytic type.

## Consequence — the unification is necessarily fibre-level

The identification can hold only where the reality structure differs from the
archimedean `q₀ ∈ ℝ`: at the **fibre level**, where `q` is a formal/complex
variable with `Im q` unconstrained (AGENTS.md Im(q) fibre-vs-observable banner).
The anti-holomorphic (conjugation) ingredient must enter through the fibre's
complex structure, **not** through the holomorphic nome map `q = e^{2πiτ}`. This
is consistent with #3936's finding that `q ↦ −q⁻¹` sends the real `q₀` to a
real-negative value (not a conjugation of a real). The open input is thereby
localized: it is the categorical→archimedean τ-functor's `q₀ ↔ period`
dictionary, which must supply the anti-holomorphic piece.

## Caveat (STRICT)

The correspondence is computed under the **standard** nome `q = e^{2πiτ}`. The
framework's *actual* τ-functor `q₀ ↔ period` dictionary is the unproved input;
under a different identification the modular involution could differ. This probe
establishes the obstruction **for the standard nome** and names the dictionary as
the open degree of freedom — it does **not** close the correspondence, and does
**not** claim the unification is impossible (only that a *holomorphic* direct
identification is obstructed).

## What this does and does NOT establish

- **DOES (exact):** matches each `q`-involution to its modular involution; shows
  the channel-swap `q↦−q⁻¹` is holomorphic `τ↦½−τ`, distinct in analytic type
  from anti-holomorphic conjugation `τ↦−τ̄`; localizes the unification to the
  fibre-level reality structure.
- **DOES NOT:** derive the unification or close the wall. It converts "the
  τ-functor maps conjugation to the channel-swap" into a precise obstruction
  (holo vs anti-holo, under the standard nome) and names the open input.

## Scope discipline (anti-laundering)

Exact modular algebra, verified numerically; no CODATA read; no convention tuned
toward `8π`; the nome map is the textbook `q = e^{2πiτ}`, stated as a caveated
choice; the unification is left OPEN. No `α_k` wired; no fit; no tier change.

## Cross-references

- Channel-swap involution `q↦−q⁻¹` (the input this maps to τ): [`2026-07-18-alpha-em-channel-swap-involution.md`](2026-07-18-alpha-em-channel-swap-involution.md) (#3936)
- Hodge doubling (`H^{1,0}↔H^{0,1}`, the conjugation side): [`2026-07-18-alpha-em-multiplicity2-realcomplex-count.md`](2026-07-18-alpha-em-multiplicity2-realcomplex-count.md) (#3920)
- Two-clause conjecture + named unification hypothesis: [`2026-07-18-alpha-em-perloop-conjecture-statement.md`](2026-07-18-alpha-em-perloop-conjecture-statement.md)
- Cluster status consolidation: [`2026-07-18-alpha-em-perloop-measure-status-consolidation.md`](2026-07-18-alpha-em-perloop-measure-status-consolidation.md)
- Bring elliptic factor `E` (`Jac(Bring) ~ E⁴`, genus-1 Lean-locked): [`2026-07-17-alpha-em-kronecker-elliptic-determinant.md`](2026-07-17-alpha-em-kronecker-elliptic-determinant.md)
- Probe + witness: [`../../computations/alpha_em/alpha_em_tau_correspondence_probe.py`](../../computations/alpha_em/alpha_em_tau_correspondence_probe.py), `computations/alpha_em/alpha-em-tau-correspondence.witness.json`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
