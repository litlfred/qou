---
# qou-v5fp
title: Four statements of the gluon operator, three answers - min-cr vs min-|tr_M| disagree
status: in-progress
type: task
priority: normal
tags:
    - 8f-colour
    - reorg-2026-10-04
created_at: 2026-08-24T20:59:37Z
updated_at: 2026-11-16T17:50:00Z
parent: qou-8lxd
---

## Status Update (PR `litlfred/qou#8140`, `468e210bfac6c8438bd4b6331f2fa807f91853e8`)

Claimed `in-progress` under `Q-8LXD-1` alongside `qou-q6lw` and `qou-tekm` (`ColorVsCharmAdditiveSector.lean` + `charm_vs_color_sector_additive_term_probe.py` verify the inter-nucleon gluon color-averaged Hecke generator $\sigma_{\text{avg}} = \sigma - (h_q/2)\cdot 1$ on the 9 color-sheet pairs). Kept `in-progress` pending owner decision on the gluon operator objective (`min cr(K)` vs `min |tr_M|`).

Found while closing qou-1ngr, 2026-08-24. Separate from qou-jqjx (trace convention); this one is about the objective, not the weights.

The same quantity — which operator step 4 of def:derived-atom selects as the proton's gluon — is stated four times and comes out three ways:

  def:universal-ilp-algorithm, prose instantiation table : sigma_0 sigma_0, 2 crossings
  computations/universal-ilp.witness.json (its OWN witness): sigma_1,        1 crossing
  rem:categorical-proton-properties + the exists/unique proofs: L_- = sigma_1 sigma_0, 2 crossings
  computations/_deprecated/integer-lp-gluon.witness.json    : sigma_0 -> sigma_0, 2 crossings

Two distinct problems underneath.

1. The stated objective is not the objective used. `def:universal-ilp-algorithm` states min cr(K) first, |tr_M(x.K)| as tiebreak WITHIN a crossing shell. The deprecated producer sorts by |tr_M| alone with no crossing preference. They disagree, and the disagreement is exactly on the load-bearing number. Cheapest survivor per crossing shell, retired convention (scratch re-run):

     proton : cr=1 sigma_0 |tr_M|=0.1597 ; cr=2 sigma_0->sigma_0 0.0274 ; cr=3 0.1654 ; cr=4 0.0921
     neutron: cr=2 L_+     |tr_M|=0.3873 ; cr=3 L_+->sigma_1   0.1441 ; cr=4 L_+->L_- 0.1120

   Under min-cr-first the proton takes 1 gluon crossing and the neutron 2 — not 2 and 4. The 2-versus-4 asymmetry, which is what makes the neutron heavier and feeds Q_beta = m_n - m_p - m_e (CAL-2), exists only under pure min-|tr_M|.

2. `computations/universal-ilp.witness.json` is self-certifying. Its assertions compare each computed operator against an `expected` value baked into `universal-ilp.py`, so allPassed=true and status "verified" say nothing about the corpus. It records confinement as sigma_1 at 1 crossing against B_3's 6, and the gluon as sigma_1 at 1 crossing against the blocks' 2 — i.e. the live witness for def:universal-ilp-algorithm does not reproduce a single crossing count the definition's own prose table asserts.

Task: pick one objective, state it once, re-witness the gluon selection against it, and reconcile the four statements. Until then rem:gluon-stabiliser-ledger records the discrepancy in prose rather than resolving it.

Related: qou-jqjx (the trace weight the retired producer used), qou-1ngr (closed - the feasible set itself is fine).


---

## Correction 2026-08-24 — this bean's own crossing-shell table is retired-convention

`qou-jqjx` closed, and it invalidates the numbers above. The table in item 1 was
computed on the deprecated producer's `tr_M(e-) = z^3`. Recomputed on live
convention D (`z = q^3/(q^2+1)`, `tr_M(e-) = h z^2 + z`):

    proton   cr=0 (none) 0.5444  cr=1 s0 0.3391  cr=2 s0.s0 0.6153  cr=3 s0.s0.s0 0.4678
    neutron  cr=0 (none) 0.4083  cr=1 s0 0.2175  cr=2 s0.s0 0.4537  cr=3 s0.s0.s0 0.3124

Three things change, and one gets sharper:

1. **`cr = 0` is now a shell.** The bare nucleon is feasible for both, so
   min-cr-first returns **0 gluon crossings for each**, not 1 and 2.
2. **Under min-|tr_M| the optimum is `sigma_0` at one crossing for BOTH** (0.339
   and 0.218). So the two objectives no longer pick different *counts* per
   nucleon — 0:0 and 1:1 respectively.
3. **The 2-versus-4 asymmetry is gone under either objective**, so item 1's
   framing ("the asymmetry exists only under pure min-|tr_M|") is too weak: it
   exists under neither. That is `qou-jqjx`'s finding, not this bean's, and the
   proton and neutron blocks now carry the withdrawal.

**What survives and is now the whole of this bean:** the objectives still
disagree about *which operator*, and item 2 is untouched —
`universal-ilp.witness.json` still asserts against `universal-ilp.py`'s own
`expected` values, so `status: "verified"` still checks nothing about the
corpus. Picking one objective and re-witnessing against it is still owed. It
just can no longer rescue a mass split, because there is no longer a split to
rescue.


---

## Item 2 resolved 2026-08-24 — and it was understated

This bean called `universal-ilp.witness.json` "self-certifying — its assertions
compare each computed operator against an `expected` value baked into
`universal-ilp.py`". There are no baked-in expected values. All five assertions
read `computed=sel[0], expected=sel[0]` — the **same expression** — so the file
records `"computed": "sigma_1", "expected": "sigma_1"` and `allPassed: true`
was guaranteed regardless of what the script produced.

Two further facts found while fixing it, either of which alone sinks the
`verified` status:

- **The producer cannot finish.** `computations/universal-ilp.py` raises at
  Level 4: `NameError: apply_atom_nf is not defined`. That function exists
  nowhere in the repository. The script never reaches `w.save()`. Confirmed
  pre-existing by stashing my edit and re-running the unmodified file.
- **The witness is four months old.** `computedAt: 2026-04-14`,
  `commitSha: 95eb85e4` — predating the 2026-05-19 trace fix that `qou-jqjx`
  turns on, among much else.

**Landed.** `def:universal-ilp-algorithm` demoted to
`computation.status: "failed"` with the three reasons recorded. The tautology
is fixed at source: the witness block now asserts that the reported operator
label re-parses to its own crossing count — independent of the selection rule,
and able to fail. The site carries a comment naming two repairs that were
considered and rejected as tautologies in longer form (feasibility and
minimum-crossing are both true by construction, since `universal_ilp` scans
crossing number upward and takes the first feasible candidate).

**Not repaired: `apply_atom_nf`.** `build_atom_nf(Z, N)` builds an atom NF from
scratch; the missing function applied an atom's construction to an *existing*
NF, and nothing in the tree records what that composition was. Guessing would
fabricate the molecular levels rather than restore them, so levels 4 and 4b
(H-H, C-C bonds) have no live producer and this is now the blocking item for
re-witnessing anything here.

**Spun out: `qou-26f2`.** The tautology is not local — an AST census of 3,253
files found **266 of 3,482** `add_assertion` calls (7.6%, 195 files) passing
the same expression on both sides. Census script kept at
`scripts/tautological-assertion-census.py`.

## What remains on THIS bean

- [x] Item 2 — the self-certifying witness. Resolved as above.
- [ ] **Item 1 — pick one objective and state it once.** Still open, and still
      needs a decision rather than a measurement. Note the live producer's
      docstring and banner already say `min cr(K)` with `min |tr_M|` as
      tiebreak, matching `def:universal-ilp-algorithm`; it was the *retired*
      producer that sorted by `|tr_M|` alone. So the disagreement is between
      the definition and a retired script, not between two live ones — which
      makes this smaller than it looked, but it still cannot be re-witnessed
      until `apply_atom_nf` is recovered.


## 2026-11-15 — γγ-built nucleon (PR #7741, `h2_gg_atom/`, `h2_gg_electron/`; owner decision C)

On three strands every γγ word is a power of V = σ₀σ₁⁻¹, so a γγ-built nucleon is V^m. Pre-registered and measured: only V³ and V⁶ pass reading 3 at every level (m = 3…7); proton and neutron are then the same word, so there is no flavour on three strands. With a γγ electron (V³ or V⁶) H₂ passes every level and the only passing bond is V³. Every γγ word has χ_(1³) = 1 (#7896). Scope (a). Bearing on this bean: under the γγ rule the gluon merges into the power of V; only the total m matters.
