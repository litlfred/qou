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
| `Vol_B3` | `7.327724753417752` | `8G = Vol(𝓑₃)` | matches to 1.6e-17 — **correctly labelled**, see the correction below |
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

**A field was called mislabelled. It is not — CORRECTED 2026-08-25.** This
section read *"`Vol_B3` … holds `8·Catalan` to sixteen digits … an agent reading
the witness for a volume gets a Catalan constant."* That is wrong, and it
inverts the fact: the Borromean rings complement is two ideal octahedra, and
`V_oct = 4G`, so

$$\mathrm{Vol}(\mathcal{B}_3) \;=\; 2\,V_{\mathrm{oct}} \;=\; 8G \;=\; 7.3277247534177521\ldots$$

is an identity, not a coincidence. The corpus says so in its own canonical
link-volume module: [`computations/binding_link_volumes.py:112`](../../computations/binding_link_volumes.py)
sets `VOL_B3 = 8 * catalan` under the comment *"Vol(L6a4) = 8G =
Vol(Borromean)"*. An agent reading this witness for a volume gets **the
volume**. `Vol_B3` is the one recorded parameter that needed no comment at all.

Recorded rather than silently deleted because the failure mode generalises: a
closed-form value was read as a *substitution for* the quantity it is the closed
form *of*. The check that would have caught it — grep the corpus for the
constant before calling a field mislabelled — is the same corpus-grep discipline
this document's §1 invokes for the file itself.

## 3. What this does and does not settle

- It **does** settle that the table has a real producer and a recoverable
  artifact, and that the "never existed" claim must be withdrawn wherever it
  appears.
- It **does** establish that the published formula and the producing
  computation disagree in their third coefficient by 14.2 %.
- It **does not** license reconstructing `beta3`, fitting it, or adjusting
  the published formula to match. **But which of the two is *derivable* is a
  measurement, and it has now been made — see §3a.**
- It **does not** revive the witness as a certificate. Restoring the file
  verbatim into `computations/` would imply it certifies the current formula,
  which it demonstrably does not. It is recorded here, with its commit, so
  anyone can retrieve it.

## 3a. Which coefficient is derivable — MEASURED 2026-08-25

§3 left the choice open on the ground that *"the artifact cannot distinguish the
two"*. The artifact is not the only evidence: **derivability** distinguishes
them, and it needs no artifact at all.

**`h_A²` is derived, and it is a q-integer.** The identity

$$h_A^2 \;=\; (q - q^{-1})^2 \;=\; q^2 + q^{-2} - 2 \;=\; [3]_q - 3$$

is exact — verified symbolically to 3e-51, and **proved in Lean**, sorry-free
over a generic `Field R` with no archimedean construct and no substrate value of
`q`:
[`QOU/Mass/WedderburnMassFormulaCoefficients.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/WedderburnMassFormulaCoefficients.lean).

That makes the finding sharper than "the recorded `beta3` disagrees with the
published `h_A²`". Because `β₂ = −2[3]_q` and `β₃ = [3]_q − 3`, the two
coefficients satisfy **one linear relation with no `q` in it**:

$$2\beta_3 + \beta_2 + 6 \;=\; 0 .$$

The recorded pair `(−6.087415, 0.0499)` evaluates it to `+0.012385`, not `0`. So
the witness's two numbers are **mutually inconsistent as a pair** — for *any*
`q`, under *any* pin, in *either* trace convention, and regardless of which one a
reader prefers. The same `β₂` forces `β₃ = 0.0437073`.

**`0.0499` has no construction.** Its one surviving producer,
`fsh-guts/deprecated/computations/next_partition_levels.py`, hardcodes it as
`BETA3 = 0.0499` under the comment *"(from Wedderburn weights)"* — while the
sibling coefficients in the same block, `BETA4` and `BETA5`, are genuinely
computed from `wedderburn_weight()`. That comment is therefore checkable, and it
fails: of **16 pre-declared candidates** (exactly the forms `BETA4`/`BETA5` use,
applied at `n = 3`), the closest misses by **63.7 %** against the **0.1 %**
window a 3-significant-figure literal allows.
[`computations/wedderburn_beta3_provenance_probe.py`](../../computations/wedderburn_beta3_provenance_probe.py).

**A precision defect is not a fit — keep them apart.** The published *digits*
`0.043707282` are `(q − q⁻¹)²` at a **five-decimal-rounded** `q = 1.10998`,
agreeing to 2.05e-9. At either real pin the value is `0.04370621`, which is
2.4e-5 away; the μ–p gap is 1.2e-8 in `q` and cannot account for that. So the
published number carries a 2.4e-5 rounding defect while the published
*construction* is exact. Re-publishing it at an unrounded `q₀` is an authoring
change and is left to the author.

**Verdict.** One coefficient has an exact construction and a Lean proof; the
other has three significant figures, a comment its own file contradicts, and
`"fitted": 0` beside it. The published formula is the derivable one, and the
table was not its output.

**Scope (a), not (b):** the pre-declared set does not reach `0.0499`; some other
construction might. Nothing is excluded. What is established is the asymmetry —
and, independently of it, the q-free inconsistency of the recorded pair.

**Still not done, deliberately:** no reconstruction of `beta3`, no adjustment of
the published formula, no re-derivation of the table. Owner directive
2026-08-25 (*"no fitting!!!"*) forbids the fit; it does not license a
replacement invented here.

The separate measurement that `Φ_n` in
`observations/neutron-proton-mass-splitting-proof.md` is not reproducible
from the reading its `Φ_p` pins ([`computations/pn_splitting_proof_provenance_probe.py`](../../computations/pn_splitting_proof_provenance_probe.py))
is **unaffected** — that block's numbers are quark-level and do not appear in
this atomic-mass witness at all, which is the same wrong-artifact mismatch
noted when its citation was corrected.

---

## 4. It is a systematic class, not one file — two more recovered

The two remaining `REMOVED` citations from
[`computations/audits/content_witness_citation_audit.py`](../../computations/audits/content_witness_citation_audit.py)
recover from **the same place and the same cause**: added under
`folio-assistant/computations/`, lost when the platform moved out in miga.

| witness | added | commit |
|:---|:---|:---|
| `atom-mass-complete-wedderburn` | 2026-04-10 | `1359fe23ac` |
| `co-molecular-binding` | 2026-04-13 | `a3e8c2c82d` |
| `mass-qvalue-by-level` | 2026-04-15 | `e2814e577f` |

So "the witness is missing" is not a per-block accident; it is a migration
that left live content citing artifacts on the other side of a repo split.
All three are recoverable with `git show <commit>:folio-assistant/computations/<name>`.

### 4a. `mass-qvalue-by-level` — good numbers beside assertions that cannot fail

The file is better than a first look suggests, and worse in one specific way.

**Good.** It carries `data.mass_by_level` with **19 rows, H through ²⁰⁸Pb**, so
the citing block's range claim in
`mass-theory/unified-iterative-correction-proof.md` is fair. Its
`data.qvalues` computes each decay **two ways**, and the BW(k=5) column is
accurate — `³H → ³He` gives `Q_bw5 = 0.018228` against `Q_exp = 0.01861`,
about 2 %. `allPassed` is honestly `false`.

**The problem is the assertion tolerances.** Six assertions test the *NF
trace* column, which is the inaccurate one, against experiment — and each
tolerance is set just above its own discrepancy:

| assertion | computed | expected | tolerance | error | tol as % of expected | passed |
|:---|---:|---:|---:|---:|---:|:---|
| `Q(³H → ³He) NF trace` | 2.4412 | 0.0186 | 2.6648 | **13017 %** | 14319 % | ✅ |
| `Q(¹⁴C → ¹⁴N) NF trace` | 3.0678 | 0.1565 | 3.2024 | 1861 % | 2047 % | ✅ |
| `Q(⁶⁰Co → ⁶⁰Ni) NF trace` | 1.9329 | 0.3182 | 1.7762 | 508 % | 558 % | ✅ |
| `Q(¹³⁷Cs → ¹³⁷Ba) NF trace` | 1.9544 | 0.5140 | 1.5845 | 280 % | 308 % | ✅ |
| `Q(⁹⁰Sr → ⁹⁰Y) NF trace` | 1.9552 | 0.5459 | 1.5502 | 258 % | 284 % | ✅ |
| `Q(²¹⁰Bi → ²¹⁰Po) NF trace` | 1.9544 | 1.1627 | 0.8709 | 68 % | 75 % | ✅ |
| `B(D) at k=5` | 2.8435 | 2.2242 | 1.5551 | 28 % | 70 % | ✅ |

A tolerance ~10 % wider than the miss it covers is the signature of a bound
chosen *after* seeing the result. The contrast inside the same file makes the
point: `B(T)` and `B(³He)` carry tolerances of `0.0004` and `0.0001` and are
recorded as **failing** at 0.0 % error. Tight bounds that fail sit beside
loose bounds that cannot.

### 4b. `co-molecular-binding` — a fitted scale, a wrong constant, and a contradiction

**The scale is fitted, on H₂.** The witness records
`calibration_factor = 0.23879110765149733`, and

```
delta_Phi1_per_bond x E_hartree_eV x calibration_factor
  = 0.687012518457808 x 27.296143240836667 x 0.23879110765149733
  = 4.478000 eV
```

which is H₂'s measured bond energy. Its own `H2_cross_check` records the
**uncalibrated** value as `18.75279 eV` — a factor 4.19 too large — and
`0.23879 = 4.478 / 18.753` is exactly the ratio that closes that gap. This is
a **fourth calibration**, fitted on a molecular observable, outside CAL-1/2/3.

**The constant named "Hartree" is not the Hartree.** `E_hartree_eV =
27.296143240836667` against CODATA `27.211386245988` — **+0.31 %**. Whatever
that number is, it is not what its key says.

**The witness contradicts its own block's prose.** `co-triple-bond-energy.md`
states that "the σ bond contributes the largest |V̂| … the π bonds contribute
smaller |V̂|". In the witness all three bonds carry the **identical**
`delta_Phi1_per_bond = 0.687012518457808`; σ and both π bonds are the same
number, and the k=3 total is exactly 3× the k=1 value. The differentiated
picture in the prose is not in the artifact.

The block also says the witness records "the LP dual shadow prices
`y₁, y₂, y₃`". It records none: `y0_star`, `y_star`, `active_set`,
`primal_obj`, `dual_obj` and `duality_gap` are all absent — the fields
AGENTS.md requires of every LP/SDP witness.

Finally, the surviving assertion is `"CO triple bond within 25% of observed"`
against `D₀(CO) = 11.09 eV`. The computed `13.434 eV` is **+21.1 %** — inside
a 25 % bar, reached by a factor fitted on a different molecule.

### 4c. What to do with these

Nothing here proposes restoring any of the three, re-fitting anything, or
editing the two citing blocks. The recoveries establish that the missing
witnesses are **recoverable and worth reading**, and that reading them
changes what their blocks can claim. Each needs an authoring decision, and
`co-molecular-binding`'s calibration needs one from the owner specifically,
since a fitted molecular scale sits outside the three-calibration discipline.

---

## 5. 🟧 OWNER DIRECTIVE (2026-08-25): **no fitting**

Put to the owner as the one item in §4 that was not mine to decide — whether
`co-molecular-binding`'s H₂-fitted `calibration_factor` is admissible. The
answer, verbatim: **"no fitting!!!"**

It settles that item and, read straight, the other two of the same kind that
this audit turned up. All three recovered witnesses carry a fitted quantity,
and none of them is admissible:

| witness | the fit | evidence |
|:---|:---|:---|
| `co-molecular-binding` | `calibration_factor = 0.23879110765149733` | `= 4.478 / 18.753` exactly — the ratio that makes the uncalibrated result equal H₂'s **measured** bond energy. A fourth calibration, on a molecular observable, outside CAL-1/2/3. |
| `mass-qvalue-by-level` | seven assertion **tolerances** | each set ~10 % above its own discrepancy, so it cannot fail — `Q(³H → ³He)` passes at **13 017 %** error. A bound fitted to a miss is a fit. |
| `atom-mass-complete-wedderburn` | `beta3 = 0.0499` | against the published `h_A² = 0.043707282`, a **14.2 %** departure with no stated derivation, recorded beside `"fitted": 0`. |

**What follows, and what does not.**

- These three are **not live**: all were lost in the miga migration and none
  is in the tree. So the directive requires no un-wiring — there is nothing
  wired.
- What it does mean is that **recovering them cannot rehabilitate the claims
  that cite them.** A block whose provenance is a fitted artifact is not
  better off for the artifact being findable. `co-triple-bond-energy.md`'s
  CO number, and the NF-trace Q-values in
  `unified-iterative-correction-proof.md`, both rest on fits and must not be
  cited as parameter-free.
- It does **not** authorise reconstructing `beta3`, re-deriving the CO scale
  from CAL-1/2/3, or widening/narrowing any tolerance. "No fitting" forbids
  the fit; it does not license a replacement invented here.
- The `atom-mass-complete-wedderburn` case keeps a second, independent
  problem the directive does not touch: the published formula and the
  computation that produced the table **disagree**, `h_A²` against `beta3`.
  Which of the two is wrong is still an authoring question.

The honest summary of §1–§5 together: the missing witnesses are recoverable,
and recovering them makes the situation **worse rather than better** — each
one, read, contains a fit that the owner has now ruled out.
