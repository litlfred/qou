---
# qou-2g9j
title: 'Delta=2 Milnor residual: the mod-delta formula is HELD (Mellor-Melvin), so the residual is not blocked'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:58:08Z
updated_at: 2026-09-04T10:58:45Z
---

Successor to `qou-768r` route 3, which closed the `Delta = 0` (min-span) family and
left the `Delta = 2` triples as its **stated residual** — the ones touching a linked
pair, where `mubar` survives as ONE BIT. Owner opened the carrier tranche; PR #6560
merged as `01bc067cd5`.

## THE RESIDUAL IS NOT BLOCKED — the mod-delta formula is HELD

`qou-768r` records route 3's blocker as "computing a `mubar` needs the Magnus
expansion of a longitude in the free group, which is real work and is not done",
and my own ledger said *"none of the five core route-3 works supplies"* it.

**That was too pessimistic, and the source that supplies it is one I had already
listed.** Mellor & Melvin, *A geometric interpretation of Milnor's triple linking
numbers*, Alg. Geom. Topol. **3** (2003) 557-568 — held at `library/0110001v3/` —
gives the **general mod-delta** formula, not just the `Delta = 0` case:

    mubar_ijk  ==  m_ijk(F) - t_ijk(F)   (mod delta)

  * `t_ijk(F)` = signed count of TRIPLE POINTS of `F_i ∩ F_j ∩ F_k` for oriented
    Seifert surfaces in general position (an integer);
  * `m_ijk(F) = e_ijk + e_jki + e_kij` in `Z/delta`, where `e_pqr(F) = eps_pq(w_r)`
    is the coefficient of `h_p h_q` in the Magnus expansion of `w_r`, and `w_r` is
    read off by walking `L_r` and recording each intersection with `F_p`, `F_q`.

Source: `library/0110001v3/sections/sec-001-2-the-formula-for-µ-ijk.md` (the
displayed formula and the Borromean worked example, `m_ijk = 1`), with the proof
in `sec-002`.

**It is diagrammatic**, so it is computable from a braid word — which is exactly
what the derived carrier gives us.

**Contrast with the other held source, and this is why the ledger's "none supplies
it" reads plausible:** `arxiv-1101.3374v1` (DeTurck et al., Pontryagin invariants /
integral formulas) is stated **only when the pairwise linking numbers vanish** —
verified in the held text at lines 218, 332, 1003. That is the `Delta = 0` case,
which route 3 already closed by a structural argument. So the integral-formula
literature really is silent on the residual; Mellor-Melvin is not.

## A SKETCH, EXPLICITLY NOT A RESULT

Working the formula against the carrier's chain structure suggests it vanishes, but
this has NOT been verified and is recorded as a direction, not a finding:

  * for a triple `a - b - c` in the chain, `a` and `c` share no summand, so `F_a`
    and `F_c` can be made disjoint => `F_a ∩ F_b ∩ F_c = empty` => `t_ijk = 0`;
  * `w_a` and `w_c` then each read only ONE other surface, so their two-letter
    Magnus coefficients vanish, leaving `m_ijk = eps_ac(w_b)`;
  * the source's own line 88 gives `eps_ij(w_k) + eps_ji(w_k) = mu_ik mu_jk`, and
    `delta | mu_ik`, so that product is `0 (mod delta)`.

The gap: this bounds the SYMMETRISED sum, not `eps_ac(w_b)` itself. Closing it needs
either the antisymmetric part or an explicit `w_b`. **Do not report the sketch as a
vanishing result.**

## What a real attempt needs

1. Seifert surfaces for the components of the derived carrier — the components are
   `(2, odd)`-TORUS KNOTS, not unknots (measured on main by
   `atom_closure_milnor_indeterminacy_probe.py`, exact-integer Kauffman bracket,
   both branches), so their Seifert surfaces are not discs and `t_ijk` is not free.
2. The `w_r` words from the braid diagram.
3. `eps_pq` via Magnus expansion in the free group on two meridians — small, since
   the words are short.

## Scope note carried forward

This bean is about `Delta = 2` ONLY. `Delta = 0` is closed (`qou-768r`, merged:
min-span triples are defined exactly where they vanish). `Delta = 1` carries no
information by definition. Nothing here reopens route 2, which is blocked for an
unrelated reason (the complement-genus handle is Borromean-only).
