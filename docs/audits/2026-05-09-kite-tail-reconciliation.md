# Kite-tail reconciliation — PR #546 round-3 vs PR #545 D(u)

**Branch.** `claude/kite-tail-reconciliation`
**Witness.** [`kite_tail_reconciliation.witness.json`](../../folio-assistant/computations/kite_tail_reconciliation.witness.json)
**Script.** [`kite_tail_reconciliation.py`](../../folio-assistant/computations/kite_tail_reconciliation.py)
**Continues.** [PR #546 round-3 audit](../../docs/audits/2026-05-05-r-and-kite-tails-exploration.md) (kite-tail status was `FALSIFIED-naive-form`).

## TL;DR

The "kite-tail FALSIFIED" claim from PR #546 round-3 has TWO causes,
not one. Reconciling them:

1. **Kite-power discrepancy IS a sympy-reduction artefact.** ✓
   PR #546 round-3 used `sp.cancel` (full reduction); PR #545's
   $D(u) = 2^{2A+1}\cdot u^{\text{shift}} \cdot (1+u^2)^{3A-1}$
   describes the un-reduced (`sp.together`) form. The two differ
   by one shared $(1+u^2)$ factor between numerator and
   denominator. **Round-3 kite-power falsification: RETRACTED.**

2. **Prefactor + neutron-shift discrepancies at A=1 remain.** ✗
   Even in the un-reduced form, proton/neutron at A=1 don't fully
   match PR #545's prediction:

| Atom | $D(u)$ predicted | Observed (un-reduced sp.together) | Match? |
|---|---|---|---|
| proton (A=1) | $2^3 \cdot u^{19} \cdot (1+u^2)^2$ | $2^2 \cdot u^{19} \cdot (1+u^2)^2$ | shift ✓, kite ✓, **prefactor ✗** |
| neutron (A=1) | $2^3 \cdot u^{22} \cdot (1+u^2)^2$ | $2^2 \cdot u^{19} \cdot (1+u^2)^2$ | kite ✓, **shift ✗ (19 vs 22)**, **prefactor ✗** |
| deuteron (A=2) | $2^5 \cdot u^{40} \cdot (1+u^2)^5$ | $2^5 \cdot u^{40} \cdot (1+u^2)^5$ | **all three ✓** |

**Deuteron A=2 verifies PR #545's D(u) exactly** (in un-reduced form).
The A=1 discrepancies are SEPARATE — likely a different braid
encoding between `markov_peel.atom_braid_word_3A` (used by
`term6_residues_at_roots` and PR #546 round-3) and PR #545's
canonical word.

## Diagnostic

Run [`kite_tail_reconciliation.py`](../../folio-assistant/computations/kite_tail_reconciliation.py)
to reproduce the table.

The script computes the canonical Markov trace via
`term6_residues_at_roots.tr_M_atomic`, lifts to $u$ via
`lift_q_to_u`, then factorises in BOTH `sp.together` (un-reduced)
and `sp.cancel` (reduced) forms. The kite power drops by 1
between the two forms because the numerator and denominator
share a $(1+u^2)$ factor that cancels under reduction:

```
together (un-reduced):  N_T(u) / [4·u^19·(u²+1)^2]
cancel (reduced):       N_C(u) / [4·u^19·(u²+1)^1]
                        with N_T = (u²+1) · N_C
```

Both forms compute the same canonical $\mathrm{tr}_M$ (`difference = 0`
under sp.simplify).

## Outstanding work for the A=1 prefactor / neutron-shift mismatch

Three reconciliation paths to test:

1. **Different braid encoding** — PR #545's $D(u)$ was derived
   for a specific braid word (likely the dressed atomic word with
   gluon entries from `mass_endomorphism.proton_cross`), while
   `markov_peel` uses `atom_braid_word_3A` from `mass_at_3A_proper`
   (without gluon entries). Verify whether running PR #545's
   $D(u)$ derivation against the markov_peel word reproduces the
   observed $2^2 \cdot u^{19}$ prefactor for both proton and
   neutron.

2. **Plancherel vs Markov trace normalisation** — the commit
   `58e78090e` ("Resolve factor-of-2 mismatch: PR #546 uses
   Plancherel trace, not Markov") flagged a related factor-of-2
   issue. The 8 vs 4 prefactor mismatch may be the same
   Plancherel-vs-Markov normalisation question, with PR #545's
   $D(u)$ in one convention and `markov_peel` in the other.

3. **Symmetric vs asymmetric word** — neutron observed shift = 19
   = proton observed shift, both equal to $18Z+21N+1|_{Z=1,N=0}$.
   This suggests `markov_peel`'s neutron word has the same shift
   as proton, which contradicts the per-nucleon $18Z+21N+1$
   formula. Possibly markov_peel's neutron word is identical to
   proton's word up to relabelling — verify by direct comparison
   of `atom_braid_word_3A(0, 1)` vs `atom_braid_word_3A(1, 0)`.

## Coordination

- **PR #545 author** — please compare your `D(u)` derivation
  braid word against `markov_peel.atom_braid_word_3A(Z, N)`.
  If they differ, document which is canonical for the six-term
  mass formula.
- **PR #600 (Δ_λ derivation race)** — the deuteron A=2 D(u)
  match means PR #545's closed form is reliable for $A \ge 2$
  applications (which is what binding-energy work needs).
- **PR #547 author** — your "factor-of-2 Plancherel-vs-Markov"
  finding may directly explain the proton/neutron prefactor
  mismatch. Worth cross-checking.

## Status

- **Round-3 kite-power FALSIFICATION**: ✓ RETRACTED (sympy artefact).
- **PR #545 D(u) at A=2**: ✓ verified exactly in un-reduced form.
- **PR #545 D(u) at A=1**: ⚠ partial — kite ✓, shift partial, prefactor ✗.
- **Reconciliation roadmap**: three concrete paths above; each is
  a 1-2 hour follow-up that needs cross-PR coordination.
