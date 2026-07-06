# Aufbau ordering: the `λ₊^ℓ` reading needs a SCALAR-channel assumption — still open

**Date:** 2026-06-20 (corrected 2026-06-21 per owner: *"don't assume only scalar channels"*)
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Compute:** [`computations/aufbau_symmetric_block_channel.py`](../../computations/aufbau_symmetric_block_channel.py)
**Trigger:** owner picked "attempt the `λ₊^ℓ` derivation" (the open ordering gap).
**Method:** corpus-grep (STRICT) → found a relevant Lean result → then owner caught
an over-claim in how I used it. Both steps recorded below.

## TL;DR (honest, after the owner correction)

A corpus-grep found [`prop:symmetric-block-domain-weight`](../../content/quantum-observable-universe/molecular-construction/symmetric-block-domain-weight.md)
(`QOU.Molecular.symmetric_block_domain_weight`, **Lean sorry-free**): on the
**scalar** (trivial, 1-dim) Wedderburn block `σ_i ↦ q`, so a braid word of length
`L` weighs `q^L = λ₊^L`. I first read this as *"the `λ₊^ℓ` channel is derived."*
**That was an over-claim.** Angular momentum `ℓ` lives in the **non-scalar**
`(2ℓ+1)`-dim irrep `V_ℓ`, and on `V_ℓ` **every** natural object gives `q^{2ℓ}`
(a=+2 overshoot), **not** `q^ℓ`. Getting `q^ℓ` (a=+1, Madelung) requires
projecting onto the **scalar** block *and* equating word-length with `ℓ` — and
**assuming those IS assuming Madelung.** So the ordering is **still open**; the
scalar shortcut is load-bearing.

## What IS derived (survives)

1. **`λ₊ = q` on every block — exact eigenvalue identity.** `T_γe =
   [[q−q⁻¹,1],[1,0]]` has eigenvalues **exactly** `{q, −q⁻¹}` (sympy: discriminant
   `(q−q⁻¹)²+4 = (q+q⁻¹)²`; `det=−1`), identical to the Hecke eigenvalues
   `(σ−q)(σ+q⁻¹)=0`. Since `σ_i` obeys this quadratic in **every** representation,
   its eigenvalues are `{q, −q⁻¹}` on **every** block; `λ₊ = q` is the Perron one.
   `T_γe` is a Hecke generator. *(Rigorous.)*
2. **On the scalar block, weight `= q^L`** (`symmetric_block_domain_weight`, Lean
   sorry-free). *(Real, but it is about word-length on the trivial block.)*

## Why a=+1 is NOT derived (the owner's point, verified)

Angular momentum `ℓ` is the spin-`ℓ` irrep `V_ℓ` (dim `2ℓ+1`) — a **non-scalar**
block where `σ_i` is a **matrix**. On `V_ℓ` (compute, sympy):

| object on `V_ℓ` | value | `a` |
|---|---|--:|
| weights (q-Cartan) | `q^{2m}`, `m=−ℓ..ℓ` | — |
| **highest weight** | `q^{2ℓ}` | **+2** |
| **trace** (q-dimension) | `[2ℓ+1]_q ~ q^{2ℓ}` | **+2** |

**No** weight equals `q^ℓ` (would need a half-integer `m = ℓ/2`). So the genuine
non-scalar angular rep yields `q^{2ℓ}` (overshoot) by weights, highest weight, and
trace alike. The `q^ℓ` object exists **only** on the scalar (trivial) block, and
only after identifying word-length with `ℓ`. Two assumptions — and they are exactly
the content of "Madelung," so assuming them is circular.

Fill-order check (compute): scalar `q^ℓ` (a=+1) matches Aufbau; q-dim `q^{2ℓ}`
(a=+2) diverges at #2 (3s vs 2p); antisym `(λ₋/λ₊)^ℓ` (a=−2) diverges at #0. So
a=+1 is the unique survivor — but it is the **assumed** scalar channel, not a
derived one.

## The open problem, correctly framed (NOT accepted — owner STRICT)

> **Why would an atomic orbital's angular content be the SCALAR-block projection
> (`q^ℓ`, a=+1) rather than the genuine non-scalar `V_ℓ` action (`q^{2ℓ}`, a=+2)?**

That is the real gap. It is *not* answered by "use the symmetric block" — choosing
the symmetric block for a genuinely non-scalar (angular) object is the assumption
under scrutiny. The two corpus hooks that *might* bridge it:

- **`conj:palindromicity-orbital-type`** — `ℓ = ½·(palindromic defect)`. The `½` is
  the very factor between `q^ℓ` and `q^{2ℓ}`; if the palindromic-defect word truly
  carries the angular content on the *symmetric* block, the projection would be
  justified. Still a **conjecture**, not proved — and it must be proved on the
  non-scalar content, not assumed.
- **`hybridization-sp-gap-braid`** — uses the self-dual (palindromic, symmetric-
  block) `s` vs chiral (`p`) split; consistent with the symmetric-block picture
  for `s`, but does not establish the scalar projection for general `ℓ`.

Per owner STRICT: Madelung is a **derivation target**, not a semi-empirical input.
Madelung's fragility (Cr, Cu, Pd) is why it is hard, not a licence to accept it.

## Pattern recorded (two disciplines, one episode)

1. **corpus-grep (CLAUDE.md §"before declaring open")** correctly surfaced
   `symmetric-block-domain-weight` before I ran any wide search — good.
2. **critical-distance (CLAUDE.md §critical-distance license)** — the owner's
   *"don't assume only scalar channels"* caught me treating a scalar-block result
   as if it derived the non-scalar angular weight. The scalar projection was doing
   the work. Logged so the next agent does not re-make the over-claim: **a=+1 is
   not derived; assuming the scalar channel for angular `ℓ` is assuming Madelung.**

## Provenance

Compute: `aufbau_symmetric_block_channel.py` (eigenvalue identity; 3-channel order;
non-scalar `V_ℓ` weights/h.w./trace). Corpus: `prop:symmetric-block-domain-weight`
(Lean sorry-free), `conj:palindromicity-orbital-type`, `2026-06-09-hybridization-
sp-gap-shell-braid-derivation.md`. Refines (does not supersede the open status of)
`2026-06-20-aufbau-from-dominant-eigenvalue-duality.md` and synthesis §4.
