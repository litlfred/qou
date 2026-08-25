# The "phantom witness" is not a phantom — and what it shows

**Date:** 2026-08-25 · **Bean:** `qou-1jw9` · **Status:** correction + finding

## 1. The correction

`atom-mass-complete-wedderburn.witness.json` has been described in this
corpus as a **phantom witness** — cited by content blocks but never present
in repository history:

> "Phantom witness: cited by the Wedderburn mass proof but exists nowhere in
> repo history."
> — [`docs/audits/2026-07-12-exposition-drain-needs-owner-ledger.md:49`](2026-07-12-exposition-drain-needs-owner-ledger.md)

**That is false, and I repeated it.** The witness was added on **2026-04-10**
in commit **`1359fe23ac`** ("Complete Wedderburn mass: 0.074% mean, all 3
invariants, no truncation") at

```
folio-assistant/computations/atom-mass-complete-wedderburn.witness.json
```

It is retrievable today:

```sh
git show 1359fe23ac:folio-assistant/computations/atom-mass-complete-wedderburn.witness.json
```

### Why the earlier searches missed it

Every search that concluded "never existed" looked under **`computations/`**.
The file lived under **`folio-assistant/computations/`** and left the tree
with the platform code in the **miga** migration, when folio-assistant moved
to its own repository. A basename search finds it; a path search does not.

I asserted the phantom claim in three pull requests — **#5743** and **#5753**
(both merged) and **#5758** — before checking it. The sites are corrected in
the same change that carries this document.

**The general lesson, worth more than this instance:** a negative existence
claim about repository history is only as good as the *paths* it searched,
and this repository has moved whole subtrees between repos. Search by
**basename across all refs** (`git log --all --diff-filter=A -- "*/<name>"`),
never by the path the file is expected at today. And note the clone here is
**shallow**, which can only manufacture *false* "never existed" verdicts —
never false "exists" ones — so a negative from a shallow clone is
particularly weak evidence.

## 2. The finding, which is stronger than the phantom claim was

The recovered witness reproduces the published table exactly — all 20 rows,
`1H` at `938.910`, `4He` at `3734.624`, `7Li` at `6534.188`, summary
`mean 0.074%`, `max 0.1917%`. So the table *is* backed by a real computation.

But the witness's own `parameters` block shows the producer **did not compute
the formula as published**. `thm:wedderburn-mass-formula` states

```
m(Z,N) = Z·m_p + N·m_n + Z·m_e + α·( Φ₁ − 2[3]_q·Φ₂ + h_A²·Φ₃ )
```

against which the recorded parameters check as follows:

| recorded | value | published counterpart | verdict |
|:---|:---|:---|:---|
| `alpha` | `3.74446` | `m_e · 8G = 3.74446` | matches |
| `beta2` | `−6.087415` | `−2[3]_q = −6.0874146` | matches |
| `beta3` | `0.0499` | `h_A² = 0.043707282` | **mismatch, ratio 1.1417 — a 14.2 % departure** |
| `Vol_B3` | `7.327724753417752` | — | **mislabelled: this is exactly `8G`, not a volume** |
| `m_p` | `938.230457` | CODATA `938.27208816` | **−0.0416 MeV (−44 ppm)** |
| `m_n` | `939.532005` | CODATA `939.56542052` | **−0.0334 MeV (−36 ppm)** |
| `fitted` | `0` | — | asserts zero fitted parameters |

Three things follow.

**`beta3` has no stated derivation.** The published third coefficient is
`h_A² = 0.0437073` at the witness's own `q₀ = 1.10998`. The producer used
`0.0499`. Nothing in the formula, the notation register, or the surrounding
blocks yields that number, and the witness carries `"fitted": 0` immediately
beside it. Either the published `h_A²` is wrong, or `beta3` is an
undocumented parameter; the artifact cannot distinguish the two, but it does
establish that the published formula is **not** what produced the table.

**The base masses are not CODATA.** The errors, −0.042 and −0.033 MeV, are
not negligible against what the table reports: `1H`'s entire quoted
`Δ = 0.127 MeV`, so roughly a third of the light-atom discrepancy is already
present in the inputs before any Φ is computed.

**A field is mislabelled.** `Vol_B3` reads as the Borromean volume and holds
`8·Catalan` to sixteen digits. This matters beyond tidiness: an agent reading
the witness for a volume gets a Catalan constant.

## 3. What this does and does not settle

- It **does** settle that the table has a real producer and a recoverable
  artifact, and that the "never existed" claim must be withdrawn wherever it
  appears.
- It **does** establish that the published formula and the producing
  computation disagree in their third coefficient by 14.2 %.
- It **does not** license reconstructing `beta3`, fitting it, or adjusting
  the published formula to match. Which of the two is correct is an authoring
  question about published content.
- It **does not** revive the witness as a certificate. Restoring the file
  verbatim into `computations/` would imply it certifies the current formula,
  which it demonstrably does not. It is recorded here, with its commit, so
  anyone can retrieve it.

The separate measurement that `Φ_n` in
`observations/neutron-proton-mass-splitting-proof.md` is not reproducible
from the reading its `Φ_p` pins ([`computations/pn_splitting_proof_provenance_probe.py`](../../computations/pn_splitting_proof_provenance_probe.py))
is **unaffected** — that block's numbers are quark-level and do not appear in
this atomic-mass witness at all, which is the same wrong-artifact mismatch
noted when its citation was corrected.
