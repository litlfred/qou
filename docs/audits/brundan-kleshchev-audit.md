# Brundan–Kleshchev isomorphism — empirical-evidence dossier

**Status.** Tracking audit. **Witness:**
[`brundan-kleshchev-audit.witness.json`](https://github.com/litlfred/qou/blob/main/computations/audits/brundan-kleshchev-audit.witness.json).

**Script.** [`brundan_kleshchev_audit.py`](https://github.com/litlfred/qou/blob/main/computations/audits/brundan_kleshchev_audit.py).

The Brundan–Kleshchev theorem
[brundankleshchev2009] states that the cyclotomic Hecke algebra
$H_n(R, q)$ at level 1 is isomorphic, as a graded algebra, to a
cyclotomic Khovanov–Lauda–Rouquier algebra $R_\alpha^\Lambda$.
This isomorphism is the upstream conjectural input axiomatised
by `class CrystalGraphRealization` in
[`thm:confinement-grading-correspondence-conditional`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/confinement-grading-correspondence-conditional.md).

A full Lean-level instance of the BK isomorphism is out-of-scope
for this audit. This dossier instead collects **necessary
structural consequences** of the isomorphism that we can verify
combinatorially as empirical evidence:

| # | Consequence | Verification |
|---|---|---|
| 1 | $\dim H_n(R, q) = n!$ | $\sum_\lambda f_\lambda^2 = n!$ (Burnside) |
| 2 | $\dim Z(H_n) = p(n)$ | partition count |
| 3 | Jucys–Murphy content multisets pairwise distinct | content-multiset check |
| 4 | $\sum_\lambda \dim_q(V_\lambda)^2 / [n]_q!$ bar-invariant | numerical at $q_0$ to 50 dps |

All four tests pass for $n \in \{2, 3, 4, 5, 6\}$ — 20 assertions
total, all green. None of these is a proof of BK; they are
necessary conditions whose failure would falsify the upstream
conjecture.

## How this feeds the conditional theorem

The Lean class `CrystalGraphRealization n q` carries a single
`sorry`-instance for the BK isomorphism's content (the
`confinement_eq_klr_top_degree` field). Any future progress on
discharging that instance — e.g.

1. Constructing the explicit graded isomorphism for small $n$.
2. Finding a constructive proof in Mathlib that the cyclotomic
   quotient $R_\alpha^{\Lambda_0}$ realises $H_n(R, q)$.
3. Identifying the LP shadow-price ordering with the KLR
   $\mathbb{Z}$-grading explicitly.

— should be cross-referenced in this audit and cited from
`thm:confinement-grading-correspondence-conditional`. When the
class instance is fully discharged, the conditional theorem
becomes unconditional.

## How to update

Re-run after any upstream change to partition combinatorics,
$q$-integer / Plancherel-weight definitions, or the CrystalGraph
class fields:

```bash
cd computations
python3 brundan_kleshchev_audit.py
```

The CI witness pipeline (`witness-pipeline.yml`) runs this
script on every PR that touches the relevant computation files.
