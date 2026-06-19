# Keystone geometric realization — DG construction attack plan (formalize-first)

**Branch:** `claude/keystone-dg-construction-2026-06-19`.
**Gate status:** the owner **reversed** the subgoal-2 geometric-derivation decline
(2026-06-19; "1 2 3" + "reverse gate → start DG build"). This opens the
research-grade geometric-realization construction for the s5-so3 keystone.
**Binding discipline (STRICT, non-negotiable):** **no fabrication; every step
falsifiable.** The failure mode to avoid is the unfalsifiable correspondence-chain
the Habiro lead refused ([`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
z-Habiro note, 2026-06-17). A **finite-dimensional Sasakian is ruled out**
(PR #2500, `ColourArenaBlockCount` block-count theorem) — the construction is
**necessarily infinite-dimensional**. This is a multi-session tranche; this doc is
the plan, not a derivation.

## The open object

> Does the **full-Hecke principal-specialization Markov trace** `s_λ(1,q,q²,…)`
> admit a geometric realization whose `S¹`-equivariant index reproduces the
> canonical Markov weights `W_λ = d_q(λ)²/[n]_q!`, subject to the necessary
> conditions C1–C7
> ([`keystone-index-necessary-conditions.md`](../audits/2026-06-16-keystone-index-necessary-conditions.md),
> with C6 tightened by PR #2500)?

## The corpus lead (NOT my invention): WRT(S³/2I) = Lawrence–Zagier

The s5-so3 ledger (z-Habiro note, 2026-06-17) already identifies the **full-Hecke
Markov trace** with the **Witten–Reshetikhin–Turaev invariant of the Poincaré
homology sphere `S³/2I`** (binary icosahedral `2I`), = **Lawrence–Zagier**. This
is the natural infinite-dimensional geometric home: **Chern–Simons / RT TQFT** on
`S³/2I`. Corpus support already present:

- McKay `2I ↔ E₈` anchors (`Σdim²=120`, `|2I|=4h`, `dim E₈=8·31`; ledger #2424).
- `A₅ ≅ I` icosahedral structure, chirality `T₁/T₂` (the keystone backbone).

**Caveat (load-bearing).** The ledger flags that **forcing** the `(q,z)`-
bicompletion bridge is the unfalsifiable failure mode. So this plan does **not
assert** the WRT realization — it lays out a **falsifiable test** of it.

## Step 1 — the cheap, decisive, FALSIFIABLE gate (formalize-first)

Before constructing *any* geometric object, run the one check that can kill the
whole WRT line:

> **Does the WRT(S³/2I) / Lawrence–Zagier per-block weight numerically equal
> `W_λ = d_q²/[n]_q!` at `q₀`, for `n = 3,4,5`?**

- The RT surgery formula for `S³/2I` (Seifert-fibered; `(2,3,5)` exceptional
  fibers) gives per-irreducible weights colored by `H_n(q)` irreps `λ`.
- Compare to `W_λ` at `q₀` (computable now from `QPartitionCombinatorics.qDim` /
  `qFactorial`).
- **Decision:**
  - **WRT weights ≠ W_λ** ⇒ the WRT(S³/2I) realization is **REFUTED**; prune (do
    not build), and formalize the refutation (compute-author §3.4). The open
    object then needs a different geometric home.
  - **WRT weights = W_λ** ⇒ strong evidence; proceed to Step 2.

This is the right first move per formalize-first §3.3: a cheap, decisive check
that either **kills or constrains** the entire WRT line *before* any DG build.
**It is the deliverable of the next session.**

## Necessary-conditions cross-check (the constraint set, already pruned)

Any surviving construction must satisfy C1–C7. Two are *promising* for the WRT
line specifically (unlike the refuted Reeb-eigenvalue resonance):

- **C4 — block *dimensions* `d_q²`, not eigenvalues.** The WRT weight *is* a
  quantum-dimension-squared / `|S_{0λ}|²`-type object, so C4 is structurally
  aligned with WRT (the refuted Reeb resonance matched eigenvalues — the wrong
  invariant).
- **C6 — full support, all `p(n)` blocks (`= p(3A)` for a mass-`A` nucleus, since
  the nucleus braid is on `n = 3A` strands), no finite-`N`.** WRT colored by *all*
  `H_n(q)` irreps has full support by construction (PR #2500 gives this teeth).
- **C2 — chirality involution `λ↔λ'` (forced).** Geometric candidate:
  orientation reversal / complex conjugation on `S³/2I`. Facets formalized in
  `KeystoneChiralityInvolution.lean` (#2500).

## Multi-session roadmap (each step gated + falsifiable)

1. **[next session]** Falsifiable WRT(S³/2I)-weight vs `W_λ` numerical check (the
   gate). Refute or constrain.
2. *If survives:* identify the `S¹`-equivariant index as the WRT partition
   function's `λ`-decomposition; check C2/C4 geometrically.
3. *If survives:* the Chern–Simons action functional realizing the index — the
   actual DG construction.

## What NOT to do (failure modes, from the corpus)

- **Do NOT** build a finite-dimensional Sasakian (ruled out, #2500).
- **Do NOT** force the `(q,z)`-bicompletion bridge (unfalsifiable; Habiro lead
  refused it).
- **Do NOT** match eigenvalues (refuted Reeb-eigenvalue resonance; C4 demands
  dimensions).
- **Do NOT** introduce any fit / free parameter (three-calibration discipline).

## Net

The gate is reversed and the construction is **opened with a single cheap
falsifiable test** (Step 1). No geometry is built or asserted here. The next
session runs the WRT(S³/2I) vs `W_λ` check; its outcome (match or refutation)
determines whether the WRT line is the keystone's geometric home or is pruned.
