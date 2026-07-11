# α-cluster geometry selection — contact-maximisation is a partial rule (²⁰Ne exception)

**Date:** 2026-07-11
**Branch:** `claude/bk-alpha-geometry-selection-2026-07-11`
**Compute:** [`computations/bk_alpha_geometry_selection.py`](../../computations/bk_alpha_geometry_selection.py)
**Witness:** [`computations/bk-alpha-geometry-selection.witness.json`](../../computations/bk-alpha-geometry-selection.witness.json)
**Follow-up to:** merged PR #3551, audit
[`2026-07-11-bk-coordination-degree-and-alpha-contact.md`](2026-07-11-bk-coordination-degree-and-alpha-contact.md).

## Question

The merged α-cluster result read binding beyond `n_α·B(⁴He)` as `N_contacts·b_αα`,
with `N_contacts` the edge count of a **hand-assigned** cluster geometry. Task 1
asks whether that geometry is **derived** by a selection rule: does the α-cluster
adopt the **contact-maximising** hard-sphere geometry (each α–α contact lowers
energy by `b_αα ≥ 0`)?

Test: compare `N_need = (B_AME − n_α·B(⁴He))/b_αα` to the maximal-contact number
`C_max(n_α)` of the optimal hard-sphere cluster (`b_αα ≈ 2.416 MeV` fixed from
¹²C/¹⁶O).

## Result

| nucleus | n_α | N_need | C_max | Δ | geometry |
|---|--:|--:|--:|--:|---|
| ¹²C | 3 | 3.0 | 3 | −0.0 | triangle (calib) |
| ¹⁶O | 4 | 6.0 | 6 | +0.0 | tetrahedron (calib) |
| **²⁰Ne** | 5 | **7.9** | **9** | **+1.1** | triangular bipyramid ← deviates |
| ²⁴Mg | 6 | 11.8 | 12 | +0.2 | octahedron ✓ |
| ²⁸Si | 7 | 15.9 | 16 | +0.1 | (lit.) ✓ |
| ³²S | 8 | 18.8 | 18 | −0.8 | (lit.) ← deviates |
| ³⁶Ar | 9 | 21.6 | 21 | −0.6 | (lit.) |
| ⁴⁰Ca | 10 | 24.5 | 25 | +0.5 | (lit.) ✓ |

`C_max` is exact for the n≤6 deltahedra (triangle, tetrahedron, triangular
bipyramid, octahedron); n≥7 uses Arkus–Manoharan–Brenner minimal-energy
hard-sphere cluster values (less certain, flagged).

## Reading (scope-limited (a))

1. **Contact-maximisation selects the geometry for the compact deltahedral
   nuclei.** ²⁴Mg = octahedron (Δ+0.2, *exact* `C_max`) is the firm case; ²⁸Si
   (+0.1) and ⁴⁰Ca (+0.5) agree with literature `C_max`. This is a *derivation*
   of the geometry (from a fit-free packing rule), not a per-nucleus fit.

2. **²⁰Ne is the exception.** It binds as **~8 contacts** (square pyramid), not
   the maximal **9** (triangular bipyramid). This is consistent with ²⁰Ne's
   well-known **prolate α+¹⁶O cluster structure** — it is not a maximal-contact
   blob. (³²S also deviates by ~1 contact, but its n=8 `C_max` is a less-certain
   literature value.)

3. **Caveat on the merged PR #3551 Part 2.** The ²⁰Ne geometry there
   (square-pyramid, 8 contacts) was **hand-assigned to fit** — so that one
   nucleus carried a one-bond DOF, and the merged "<0.5% forward" claim for ²⁰Ne
   was not fully fit-free. Recorded here per the critical-distance license rather
   than left implicit. ²⁴Mg/⁴⁰Ca remain genuinely forward (their geometries are
   the contact-maximising ones).

## Verdict

> Contact-maximisation is a **partial** geometry-selection rule: it *derives* the
> α-cluster geometry for the compact deltahedral nuclei (²⁴Mg exact; ²⁸Si, ⁴⁰Ca
> with literature `C_max`), but **fails at ²⁰Ne** (and possibly ³²S), which have
> non-compact cluster structures. Not a universal derivation. Scope-(a); `b_αα`
> empirical.

**Open:** a selection rule that reproduces ²⁰Ne's non-compact (α+¹⁶O) structure —
i.e. an energy functional beyond equal-weight contact counting, or a `𝓑_K`
link-topology criterion that penalises the maximal-contact blob for ²⁰Ne.
