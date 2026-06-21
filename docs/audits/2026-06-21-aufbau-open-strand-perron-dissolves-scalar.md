# Aufbau ordering — the open-strand Perron lever dissolves "why scalar", reduces `H_scalar` to one topology choice

**Date:** 2026-06-21
**Branch:** `claude/h-scalar-open-strand-perron-2026-06-21`
**Bean:** e2nf (electron-shell program — Aufbau ordering gap)
**Type:** structural reframing + sorry-free Lean anchor — *not* a closure, *not* a fit.
**Lean:** [`aufbau-open-strand-perron.lean`](../../content/quantum-observable-universe/molecular-construction/aufbau-open-strand-perron.lean)
(`QOU.Molecular`, sorry-free).

## The gap as left by the synthesis

The electron-shell synthesis ([`2026-06-20-electron-shell-program-synthesis.md`](2026-06-20-electron-shell-program-synthesis.md))
and the dominant-eigenvalue audit ([`2026-06-20-aufbau-from-dominant-eigenvalue-duality.md`](2026-06-20-aufbau-from-dominant-eigenvalue-duality.md))
isolate the Aufbau ordering to **one** hypothesis:

> **H_scalar** — an orbital's energy is the **symmetric-block (scalar) component**
> of its angular braid word (`q^ℓ`, a=+1, Madelung `n+ℓ`), not the non-scalar
> `V_ℓ` action (`q^{2ℓ}`, a=+2).

The puzzle in that framing: *why* would the genuinely non-scalar angular content
`V_ℓ` project to the **scalar** block? The merged
[`prop:symmetric-block-domain-weight`](../../content/quantum-observable-universe/molecular-construction/symmetric-block-domain-weight.md)
gives `q^ℓ` **only on the scalar (trivial) block** — so as stated, `H_scalar`
*assumes* the scalar projection.

## The lever — Perron dominance holds on **every** block, so no scalar projection is needed

The Hecke generator `σ_i` satisfies its defining quadratic
`σ² − (q−q⁻¹)σ − 1 = 0` in **every** representation. Hence (Lean
`hecke_eigenvalue_mem`) its eigenvalues are `{q, −q⁻¹}` in every block, and for
the substrate `q > 1` the eigenvalue `q` **strictly dominates** in modulus
(Lean `perron_eigenvalue_is_q`: `|−q⁻¹| = q⁻¹ < q`). This is the merged
eigenvalue identity (the `T_γe` Perron `λ₊ = q`), now stated
representation-independently.

**Consequence.** An **open** strand — a transfer-matrix *matrix element*
`(T^L)_{ij}`, Perron-dominated — weighs `λ₊^L = q^L` **on every block**, not just
the scalar one. The "scalar projection" was never required: the `q`-per-step
weight is the *dominant eigenvalue*, which is `q` in every representation. So the
puzzling step in `H_scalar` ("project the angular content to the scalar block")
**dissolves** — Perron dominance already gives `q^L` everywhere.

## Where the `a=+2` overshoot actually comes from — closed-loop q-dimension, not a "non-scalar block"

The overshoot `q^{2ℓ}` is **not** "`σ_i` acting on a non-scalar block" (that still
has dominant eigenvalue `q`). It is the **q-dimension / top weight** of the
**packaged** `(2ℓ+1)`-dim irrep `V_ℓ`: `[2ℓ+1]_q ~ q^{2ℓ}`, top weight `q^{2ℓ}`.
That is a **closed-loop** object — the quantum trace closing the strand into a
loop, summing the whole weight diagram `q^{-2ℓ}, …, q^{2ℓ}`.

The Lean anchor makes the relationship exact:

$$
  q^{2\ell} \;=\; (q^{\ell})^2
  \qquad(\texttt{closed\_loop\_is\_open\_squared}),
$$

i.e. **the `a=+2` closed-loop weight is the *square* of the `a=+1` open-strand
weight.** Equivalently the total keys differ by exactly one extra angular factor
(Lean `closed_key_exceeds_open`):

$$
  \underbrace{q^{\,n+2\ell}}_{\text{closed, key }n+2\ell}
  \;=\;
  \underbrace{q^{\,n+\ell}}_{\text{open, Madelung }n+\ell}\;\cdot\;q^{\ell}.
$$

## The residual open item — one topology choice, stated honestly

So the Aufbau `a=+1` vs `a=+2` ambiguity is **not** "scalar vs non-scalar block"
(both blocks are Perron-`q`) and **not** a free magnitude. It is a single
**open-vs-closed topology** choice for the bound electron's angular content:

| reading | object | weight | `a` | order |
|---|---|---|--:|---|
| **open strand** (on-shell worldline / propagator) | Perron transfer element `(T^ℓ)_{ij}` | `q^ℓ` | **+1** | **Madelung `n+ℓ` ✓** |
| **closed loop** (q-dim of packaged `V_ℓ`) | quantum trace / top weight `[2ℓ+1]_q` | `q^{2ℓ}=(q^ℓ)²` | +2 | overshoot |

The reframed (sharper, more physical) hypothesis that replaces `H_scalar`:

> **H_open** — the bound atomic electron is a single **open** strand (an on-shell
> worldline carrying the fundamental rep), so its angular content enters as `ℓ`
> open Perron-transfer curls, weight `q^ℓ` (a=+1) — *not* the **closed-loop**
> q-dimension `q^{2ℓ}` of the packaged irrep `V_ℓ` (a=+2). Radial `n` and angular
> `ℓ` are then both open-transfer curl-counts weighted by the same Perron `λ₊=q`,
> entering the key symmetrically → Madelung `n+ℓ`.

**What is gained over `H_scalar`:**
1. **Dissolves "why scalar".** Perron `λ₊=q` on *every* block (Lean) — the open
   strand needs no scalar projection.
2. **Names the overshoot's true origin.** `q^{2ℓ}` is the **closed-loop
   q-dimension** of `V_ℓ`, exactly `(q^ℓ)²` — not a non-scalar-block eigenvalue.
3. **Localizes the open item** to one physically-meaningful binary: is the bound
   electron's angular content an **open** propagator strand or a **closed**
   q-dim loop? The electron is on-shell/observed (an open worldline, not a
   vacuum bubble) — which *motivates* `open`, but the framework does not yet
   **derive** that the angular fusion is `ℓ` open steps rather than the `V_ℓ`
   packaging.

**What is NOT gained (honest caveat, owner-STRICT).** This is **not** a closure.
`H_open` is a sharper, more falsifiable hypothesis than `H_scalar`, but the
residual identification — *"angular momentum `ℓ` = `ℓ` open fundamental-fusion
transfer curls"* vs *"angular content packaged as the single irrep `V_ℓ`"* — is
still a structural **choice**, motivated by the open-worldline physics but not
forced by a categorical identity. Per the repeated-overshoot pattern (eigensplit
a=−2; q-dim a=+2; `√`-q-dim refuted at `q₀`), and per owner directive, the
ordering remains an **open derivation target**, not a semi-empirical input. The
contribution here is to make the target precise and to remove the spurious
"scalar projection" framing.

## Lean anchor (sorry-free)

[`aufbau-open-strand-perron.lean`](../../content/quantum-observable-universe/molecular-construction/aufbau-open-strand-perron.lean):

- `hecke_quadratic_factor` — `x²−(q−q⁻¹)x−1 = (x−q)(x+q⁻¹)`.
- `hecke_eigenvalue_mem` — eigenvalues `∈ {q, −q⁻¹}` in every representation.
- `inv_lt_self_of_one_lt` / `perron_eigenvalue_is_q` — `|−q⁻¹| < |q|` for `q>1`
  (Perron dominance, representation-independent).
- `closed_loop_is_open_squared` — `q^{2ℓ} = (q^ℓ)²` (overshoot = open²).
- `closed_key_exceeds_open` — `q^{n+2ℓ} = q^{n+ℓ}·q^ℓ` (keys differ by `q^ℓ`).

No `sorry`; elementary-real arithmetic; nothing wired; no fit.

## Provenance

Builds on (merged): `symmetric_block_domain_weight` (scalar-block `q^ℓ`),
the `T_γe` Perron eigenvalue identity, `2026-06-20-aufbau-from-dominant-
eigenvalue-duality.md` (the open-vs-loop-trace reframing — caveat 2),
`2026-06-21-palindromicity-does-not-justify-scalar-projection.md` (defect `=2ℓ`
parallels the non-scalar size). No new compute — corpus + structural reading +
Lean (formalize-first).
