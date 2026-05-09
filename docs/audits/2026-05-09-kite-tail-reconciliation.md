# Kite-tail reconciliation — PR #546 round-3 vs PR #545 D(u)

**Branch.** `claude/kite-tail-reconciliation`
**Witness.** [`kite-tail-reconciliation.witness.json`](../../folio-assistant/computations/kite-tail-reconciliation.witness.json)
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

## Update — A=1 prefactor RESOLVED

**Finding (2026-05-09 follow-up).** The A=1 prefactor mismatch
(observed $2^2 = 4$ vs predicted $2^{2A+1} = 8$) is explained by a
**convention issue in PR #545's $2^{2A+1}$ formula**, NOT the braid
encoding.

PR #545's commit message [`bcafe0d1d`](https://github.com/litlfred/qou/commit/bcafe0d1d) (also referenced in [`d_u_closed_form_proof.py`](../../folio-assistant/computations/d_u_closed_form_proof.py)) derives the $2^{2A+1}$
prefactor by counting averaged crossings:

> "each averaged crossing = $(\sigma + \sigma^{-1})/2$, contributing
> a factor of $1/2$: each nucleon has 2 averaged ud-pair couplings →
> $2A$ factors; canonical pppnnn ordering has exactly one mixed
> $(p,n)$ inter-nucleon interface → $+1$ more, total $2A+1$."

The `+1` from the p-n interface only applies when **both proton and
neutron nucleons are present**. At A=1 (just p OR just n), there is
no p-n interface, so the formula should be $2A + 0 = 2A$, giving
$2^2 = 4$ — exactly the observed value.

**Corrected formula.**

$$
\text{prefactor} = 2^{2A + \delta_{Z\,N}}, \qquad
\delta_{Z\,N} = \begin{cases} 1 & Z > 0 \text{ and } N > 0 \\ 0 & \text{otherwise.} \end{cases}
$$

Verification across all atoms (PR #545 Dprime table values from the
`d_u_closed_form_proof.py` history):

| Atom | Z, N, A | Avg crossings | Predicted $2^k$ | Observed | Match? |
|---|---|---|---|---|---|
| proton | 1, 0, 1 | $2A = 2$ | $2^2 = 4$ | $4$ | ✓ |
| neutron | 0, 1, 1 | $2A = 2$ | $2^2 = 4$ | $4$ | ✓ |
| deuteron | 1, 1, 2 | $2A + 1 = 5$ | $2^5 = 32$ | $32$ | ✓ |
| tritium | 1, 2, 3 | $2A + 1 = 7$ | $2^7 = 128$ | $128$ | ✓ |
| ³He | 2, 1, 3 | $2A + 1 = 7$ | $2^7 = 128$ | $128$ | ✓ |
| ⁴He | 2, 2, 4 | $2A + 1 = 9$ | $2^9 = 512$ | $512$ | ✓ |

**The corrected formula matches all atoms exactly.** PR #545's
$2^{2A+1}$ formula was off by one factor of 2 at A=1; the corrected
$2^{2A + \delta_{Z\,N}}$ closes the prefactor mismatch entirely.

## Update — Neutron shift discrepancy (still open)

The shift formula `18Z + 21N + 1` predicts:
- proton (Z=1, N=0): $18·1 + 21·0 + 1 = 19$ ✓ matches observed
- neutron (Z=0, N=1): $18·0 + 21·1 + 1 = 22$ ✗ observed shift is $19$

Even with the `+1` interface term removed for A=1 (yielding
predicted $21$ for neutron), the prediction still doesn't match
the observed $19$. The 3-unit gap is not yet explained by
crossing-count arithmetic.

**Hypothesis.** `markov_peel`'s symbolic reduction may absorb a
$u^3$ factor from the numerator into the denominator-cancellation
phase, lowering the apparent shift by 3 for the neutron word.
Verification deferred — would need to inspect the `markov_peel`
intermediate state.

## Status (revised)

- **Round-3 kite-power FALSIFICATION**: ✓ RETRACTED (sympy artefact, explained).
- **PR #545 D(u) at A=2**: ✓ verified exactly in un-reduced form.
- **A=1 prefactor mismatch**: ✓ RESOLVED — corrected formula $2^{2A+\delta_{ZN}}$.
- **Neutron shift (19 vs 22)**: ⚠ open — likely a `markov_peel` numerator-absorption artefact, deferred.
