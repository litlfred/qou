# Atom → knot rule for A ≥ 5 — constraint set, rule-class verdicts, and the alpha-cluster additivity test

**Date:** 2026-07-13 · **Queue item:** `research-atom-to-knot-rule-A5plus`
(no assignment for ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F) · **Branch:**
`claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/alpha_cluster_volume_additivity_probe.py`](../../computations/deltalambda/alpha_cluster_volume_additivity_probe.py)
· **Witness:** [`alpha-cluster-volume-additivity.witness.json`](../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json)
(allPassed: true, 7/7 assertions; symbolic-exact arithmetic, no census scan, nothing tuned)
**Design discipline:** formalize-first (`compute-author.md` §3.3) — this is a
constraint-analysis + one cheap decisive probe, not a wide search.

## 1. Context

The only derived binding structure is the bond-count tower
(`prop:linear-chain-bond-count`; multiplicity `M_n = (n−1)` Lean-proved
sorry-free in `QOU/Mass/LinearChainBondCount.lean`):

`B(K) = m_e · Σ_{n=2}^{A} Σ_{consecutive n-clusters c} (n−1) · Vol(c)`,

with 3-carriers `ppn → L6a4` (7.3277), `pnn → 8₁₁` (8.2863), 2-chains → Hopf
(`Vol = 0`). Its single-link `n = 4` reading was executed **negative** at ⁴He
([`2026-07-13-he4-vol4-prediction-test.md`](2026-07-13-he4-vol4-prediction-test.md)):
the AME-implied `Vol₄ = 8.0484` is carried by **no** ≤14-crossing 4-component
link (0 of 7463 within ±0.05 — a census-spectrum gap), and the linear 4-chain
closures (L8a21/L8a20) overshoot by +26%. The A≤3 IDs themselves are
deprecated volume-search matches, trace-unconfirmed
([`2026-07-04-he4-vol4-gated-on-r5full.md`](2026-07-04-he4-vol4-gated-on-r5full.md);
deprecation recorded in `2h-markov-trace-zero-audit.md`, tags
`manual-historical-volume-match` / `deprecated-volume-match`; the knot *names*
were re-adjudicated correct at the volume-matching level in
[`2026-06-12-knot-id-volume-match-adjudication.md`](2026-06-12-knot-id-volume-match-adjudication.md)).
Any A ≥ 5 rule must clear this record.

## 2. Constraint table (what any A ≥ 5 assignment rule must satisfy)

| # | constraint | source | epistemic tier |
|---|---|---|---|
| C1 | Tower form `B = m_e·Σ (n−1)·Vol(c)` over consecutive sub-chains of the `p^Z n^N` nucleon chain; `M_n = (n−1)` and `Σ_{n}(A−n+1)(n−1) = C(A+1,3)` | `QOU/Mass/LinearChainBondCount.lean`; [`2026-07-04-theta-mn-bondcount-derived-linearchain.md`](2026-07-04-theta-mn-bondcount-derived-linearchain.md) | proved-lean (combinatorics only; the `Vol`-as-scale identity is conditional per the [volume ledger](../coordination/binding-scale-is-hyperbolic-volume.md)) |
| C2 | Isospin carriers exist only for **mixed** 3-chains (`ppn`, `pnn`); the IDs are deprecated volume-search matches that the Markov-trace test does not confirm — **by the producer's ratio test, not by the raw `0.388` vs `1.027` gap, which is not evidence** (§5-bis) | r5full-gate audit | empirical / deprecated |
| C3 | **Vol₄ census gap:** implied 8.0484 lies in a gap of the ≤14-crossing 4-component spectrum; the linear-chain closure family's *minimum* (L8a21, 8 crossings) is 10.149, +26% — so either the n=4 carrier has ≥15 crossings (outside the whole HT census) or the n≥4 term is **not a single volume** | Vol₄ test audit | executed negative, scope-(a) |
| C4 | **Supra-linearity:** cluster measure `C(A+1,3) ~ A³` vs `B_AME ~ 8·A` forces the AME-required *average* per-cluster volume to collapse: 5.54 (A=4) → 1.79 (⁶Li) → 1.37 (⁷Li) → 0.63 (¹²C) → 0.37 (¹⁶O), against 7.3–8.3 corpus 3-carriers. An untruncated tower with O(8) volumes at every level over-predicts B by ~4× already at A=6 | this probe §[2] | symbolic-exact |
| C5 | **Brunnian non-extension:** the Borromean A=3 pattern (L6a4, Brunnian, pairwise linking 0) does not extend as a volume carrier — the 4-component Brunnian analogue L8n8 is **non-hyperbolic** (`Vol ~ 0`). Consistent with n≥4 truncation, but a pure n≤3 truncation fails at ⁴He (n≤3 = 15.96 MeV = 56% of AME) | Vol₄ test probe | executed |
| C6 | **Ordering gap:** the canonical `p^Z n^N` ordering (`atom_braid_word_3A`, `ordering = ['p']*Z + ['n']*N`) makes the ⁶Li chain `pppnnn`, whose 3-sub-chains include `ppp` and `nnn` — species-pure carriers with **no corpus assignment**. The linear-chain rule is underdetermined at A ≥ 5 even at the n=3 level. (An alternating `pnpnpn` ordering would avoid this but is itself a new, underived model choice.) | this probe §[3] | structural |
| C7 | **n≤3 bracket:** with every 3-carrier bracketed in [Vol(L6a4), Vol(8₁₁)], the n≤3 layer alone spans AME at A=6 (29.96–33.87 vs 31.99 MeV) and A=7 (37.44–42.34 vs 39.25) — the n≥4 terms must be near zero there, sharpening C4/C5 | this probe §[3] | symbolic-exact (bracket, conditional on C2 carriers) |
| C8 | **Carrier-saturation / flat B/A** (A≈4 sibling work, this branch): known links must reproduce the flat ≈7–8 MeV/nucleon plateau — the composite/large-A limit of C4 | sibling `carrier_saturation_*` / `packing_*` (owned by sibling agents; cited only) | in progress (sibling) |
| C9 | **SDP route requirements:** the principled ID is the R5-full categorical SDP (`conj:canonical-knot-id-sdp`, #604): GS normal form + Markov trace of the atom Hecke element in `H_{3A}` — H₁₅ (A=5), H₁₈ (A=6; 385 Wedderburn blocks; a cached canonical ⁶Li χ witness already exists per `li6-h18-amplification-discriminator.witness.json`, so H₁₈ trace data is feasible). The interface superposition is `2^k` pure braids (k=7 at A=3, k=9 at A=4, growing ~2 per nucleon). Blocking issue: the method currently **fails to confirm its own A≤3 anchors** (C2) | r5full-gate audit; ⁶Li H₁₈ witness | open (gate #604) |

## 3. Rule-class verdicts

### (i) Linear-chain closures (the current implicit rule) — does not extend as-is

The Vol₄ test already showed the n=4 single-volume reading fails at ⁴He.
Quantification of "what crossing number would be needed": none within the
family — the linear 4-chain closure family's *minimal* member (L8a21, 8
crossings) sits at 10.149 (+26% above the required 8.0484), and adding
crossings/twist regions to the chain family adds hyperbolic content, moving
volumes further up, not down. The required 8.0484 is below the family minimum
and inside a gap of the entire ≤14-crossing 4-component census; a carrier
would have to be a ≥15-crossing 4-component link found post hoc — a CAL-4 fit,
out of bounds. At A ≥ 5 the rule is additionally **underdetermined** (C6:
`ppp`/`nnn` carriers unassigned) and **arithmetically excluded** untruncated
(C4). **Scope-(a):** the tower form and the Lean-proved multiplicity survive;
what fails is the *single-volume-per-level, non-decaying* carrier assignment.

### (ii) Alpha-cluster composites — the testable interim (probe executed)

Read the A ≥ 5 link as a composite (connected sum / split union) of A ≤ 4
cluster units. Hyperbolic volume is **additive** under both operations, so
under the tower the composite's binding is the sum of cluster bindings —
zero-fit predictions from A ≤ 4 values alone. AME-level cluster values
(vendored AME2020; probe §[4]):

| iso | decomposition | B_add (MeV) | B_AME (MeV) | err | deficit (MeV) | implied Vol/bond (GUARDED) |
|---|---|--:|--:|--:|--:|--:|
| ⁶Li | α + d | 30.520 | 31.994 | **−4.61%** | +1.474 | 2.884 |
| ⁷Li | α + t | 36.777 | 39.245 | **−6.29%** | +2.468 | 4.829 |
| ⁸Be | α + α | 56.591 | 56.499 | **+0.16%** | −0.092 | −0.180 |
| ⁹Be | α + α + n | 56.591 | 58.164 | −2.70% | +1.573 | 1.539 |
| ¹¹B | 2α + t | 65.073 | 76.205 | −14.61% | +11.132 | 10.892 |
| ¹²C | 3α | 84.887 | 92.162 | −7.89% | +7.275 | 7.118 |
| ¹⁴N | 3α + d | 87.112 | 104.659 | −16.77% | +17.547 | 11.446 |
| ¹⁶O | 4α | 113.183 | 127.619 | −11.31% | +14.437 | 9.417 |
| ¹⁹F | 4α + t | 121.664 | 147.801 | −17.68% | +26.137 | 12.787 |

Findings (honest classification):

- **⁸Be validates the α unit to +0.16%** — additivity's own anchor (⁸Be is
  barely unbound against 2α; the −0.092 MeV deficit is the known threshold).
- **Additivity is a consistent lower bound**: every deficit is positive
  except ⁸Be's (asserted in the witness). The deficit *is* the cluster
  separation energy — in tower language, the missing inter-cluster bond term.
- **One-bond composites land within 3–6.3%** (⁶Li −4.61%, ⁷Li −6.29%,
  ⁹Be −2.70%) — comparable to the ³He −2.97% anchor residual, with zero fit.
- **Multi-bond composites degrade to −15…−18%** (¹¹B, ¹⁴N, ¹⁹F): the
  inter-cluster bonds accumulate and are not captured.
- **The implied per-bond volumes are non-constant** (2.9 → 12.8, guarded,
  non-evidential): the missing inter-cluster term is **not one universal
  volume**. Matching links to these numbers post hoc would be CAL-4 fits.
- **Tower-level (conditional) variant** (probe §[5]): with the tower's own
  cluster values (α conditional on the AME-implied Vol₄ — tautologically
  `B_AME(α)`; d = 0 via Hopf; t = `m_e·2·Vol(8₁₁)`, −0.16%), ⁶Li lands at
  −11.56% (the Hopf-zero deuteron costs ~7 points) and ⁷Li at −6.32%. The
  derived Borromean-route deuteron (+0.19%,
  [volume ledger](../coordination/binding-scale-is-hyperbolic-volume.md) item 2)
  restores the AME-level −4.6%.

**Scope-(a).** This constrains the *bare-additivity* composite rule; it does
not exclude the composite ingredient — the cluster pieces are structurally
exact lower-bound contributions (permanence principle), and the deficit is
the measured size of the missing inter-cluster term.

### (iii) SDP canonical knot-ID — the only principled route

`conj:canonical-knot-id-sdp` (#604, R5-full) is the route that *derives*
the link rather than assigning it: GS normal form of the atom Hecke element
in `H_{3A}`, Markov trace, census match under SDP uniqueness. Requirements
at A ≥ 5: H₁₅ (A=5) / H₁₈ (A=6) symbolic reduction — **feasible** (a cached
canonical ⁶Li χ witness at H₁₈ with 385 Wedderburn blocks already exists) —
plus handling the `2^k` interface superposition (k = 9 at A=4, ~2 more per
nucleon). The blocking issue is not scale but **validity**: the method does
not confirm its own A≤3 anchors (established by the producer's **ratio
test**, not by the raw `tr_M` vs `J_{6₂}` gap — see §5-bis),
so running it at H₁₈ before resolving the A≤3 non-confirmation would produce
IDs with no more standing than the deprecated volume matches.

## 4. Recommended route

1. **Principled path: R5-full SDP knot-ID (#604), gated on resolving its A≤3
   anchor non-confirmation first.** Until the trace test confirms (or
   replaces) 6₂/8₁₁/L6a4, no A ≥ 5 ID derived by the same machinery is
   trustworthy. This remains the queue item's real blocker (matching its
   existing `blocked_by: research-multi-nucleon-interface-operator`).
2. **Testable interim: alpha-cluster additivity as a zero-fit lower bound**
   for the six gap isotopes — exact for ⁸Be-type thresholds, −3…−6% for
   one-bond composites, degrading with bond count. Suitable for dashboard
   *bracketing* (clearly labeled lower bound), **not** for wiring as a
   canonical assignment.
3. **The open derivational object is the inter-cluster bond term** — non-
   universal (2.9 → 12.8 implied volume units per bond), so not a single new
   link volume. Its A-dependence is the same object as the sibling
   carrier-saturation/packing work (C8) and the ⁴He non-single-volume n=4
   reading (C3): one missing composite-interface theory, seen three ways.
   Formalize-first note: before any census search for inter-cluster
   carriers, a structural invariant (e.g. additivity-monotonicity + the C4
   collapse rate) should prune the class — no such search is run or
   recommended here.

## 5. Provenance / discipline

Inputs: `m_e` (CODATA 2022, CAL-1), vendored AME2020 (`_ame_binding_mev`,
validation-only), corpus volumes from `binding-link-volumes.witness.json`
(deprecated volume-search IDs, stated as such), the AME-implied
`Vol₄ = 8.0484` used **only** as a guarded conditional input. No fitted
constant; no census scan; no production wiring; no tier changes. Files owned
by sibling agents (`packing_*`, `carrier_saturation_*`) untouched — cited
only. Queue item `research-atom-to-knot-rule-A5plus` advances from "no
constraint set" to "constraint table + executed interim test + gated
principled route"; it stays **open** (the assignment itself is not made —
making one today would be a fit).

## 5-bis. What actually supports the A≤3 anchor non-confirmation (2026-08-31)

**Corrected twice on the same day; read the second correction.**

### The raw-value comparison is not evidence

**C2** and §4 item 1 above cite `tr_M(²H) ≈ 0.388` against
`J_{6₂}(q₀) ≈ 1.027`. The producer behind that pair,
`computations/atom_nf_symbolic_D.py`, converts trace to Jones via
`markov_trace_to_jones` — which **is the identity function**. Its own docstring
names the normalisation factor `((-1/√q)^{n-1} · (q/(1−q²))^{n-1})` and then
states *"for ease, we return `tr` as-is"*. `main()` calls it and compares the
result directly against a normalised `J(6_2)` from Kawauchi/KnotInfo.

So the two sides are an **unnormalised** 6-strand Markov trace and a
**normalised** Jones polynomial. They must differ, and by how much says nothing
about the identification. **Do not quote the pair or any percentage from it.**

### The gate is sound anyway — the producer supplies the right test

`main()` knows the normalisation is missing and computes the
convention-independent discriminator: *"even if they differ by a
writhe/normalization factor, the ratio should be a pure power of `−q^{1/2}`."*
That ratio is recorded as `symbolic_ratio` in the witness.

Measured: a rational function with **83 terms over 11**, in half-integer powers
of `q` running past `q^{2713/2}`. **Not a monomial.** The ratio test fails, so
the anchor non-confirmation is real and **C9 stands as written** — on this
evidence rather than on the two floats.

### The convention scoping, and why it does not rescue the comparison

`tr_M(²H) ≈ 0.388` is the **convention-C** value; convention D is canonical
(owner ruling 2026-08-15) and PR #6318 regenerated the table at the proton pin
to `0.5751722439177719` (**+48.13 %**), re-verified live via
`binding_canonical(1, 1)` → `0.575172243917772`. That correction is right about
the `tr_M` value and **irrelevant to this comparison**: correcting an input to a
test that was never evidential does not make it evidential. An earlier version
of this section reported the gap as "62.19 % / 43.99 % low"; both figures are
withdrawn.

### For whoever attacks `conj:canonical-knot-id-sdp`

Aim at the **ratio being a pure power of `−q^{1/2}`**. Do not read the raw gap
as "how far off" the identification is — that distance is dominated by an
omitted normalisation factor, which at `n = 6` strands is large.

Measured by `computations/probes/r5full_anchor_gate_evidence_probe.py` (3/3,
exit 0). Scope **(a)**: about the evidence for the gate, not about the knot —
nothing here shows `6₂` is right or wrong for the deuteron.
