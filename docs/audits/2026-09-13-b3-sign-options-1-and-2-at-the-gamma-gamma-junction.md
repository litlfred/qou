# The `b₃` sign: Options 1 and 2 pushed at the γγ junction — both close, and two of my own predictions were refuted

**Date** 2026-09-13 · **Bean** `qou-ix0x` · **Branch** `claude/b3-affineness-is-the-last-hypothesis-2026-09-13` · **PR** #7287

Owner instruction: *"work qou-ix0x — push option 1 as far as possible. then option 2"*, against the
`qou-brng` framing of 2026-09-13:

- **Option 1** — keep the count/bond channel, find a further *derived* source of per-pair variation.
- **Option 2** — accept the channel is not where `b₃` lives; a different object supplies the extensive term.

Both are pushed here to a structural stop. **Neither closes the gap**, and the useful content is *why*.

---

## 0. The bean was aimed at the wrong thing, and said so itself

`qou-ix0x` sat at `todo` since 2026-09-11 asking for *"the FORM of `w3`"* and naming the Habiro/cyclotomic
summation as its route. That question was answered on `main` while it sat. Three results it does not record:

| result | what it fixes |
|---|---|
| `MassTheory.B3SignOneRoot.b3corpus_chain` | `b3corpus f01 1 f12 = −((f01−1)(f12−1))` **exactly** ⇒ `b₃ > 0` iff **exactly one** chain bond exceeds 1 |
| `MassTheory.PnBetweennessBlocksSignMixed` | the escape reduces to **two hypotheses**: pn **averaging**, and **affineness** of `μ = z + d` |
| `Mass.ProductionChainBondProduct.tr_productionChain_braided` (landed 2026-09-13) | `tr_M(W_atom)/tr_M(W_free) = ∏_bonds (z + d_b)`, from `BraidedTower` alone |

The AGENTS.md extensive-term bullet and the Ursell audit §4 both say a positive term *"needs a bond factor
above 1"*. That is **necessary and not sufficient** — a chain's `φᵀ₃` is a *product*, so flipping **both**
bonds leaves `b₃` byte-identical.

---

## 1. Option 1 — the γγ bond is pair-dependent, and still cannot sign-mix

The owner ruled on 2026-09-08 (`qou-ales`) that every canonical braid word is selected by **γγ pair-production
+ the confinement SDP**. Step 3 measured the selected bond `G³ = (σ₂σ₃⁻¹)³` **unbinding the diproton**
(`tr_atom/tr_free = 1.001058 > 1`). `GammaGammaEscapesSingleCrossing` proves why that does not collide with
the single-crossing obstruction. Step 8's own not-claimed list names *"the dineutron side"*.

So `μ_pp > 1` was derived and `μ_pn`, `μ_nn` were **unmeasured**. That is the junction: `qou-q8vl`'s open item
is literally *"a THIRD bond family that supplies the sign-mixed pattern by derivation"*, and neither arc had
connected to the other.

**Probe** [`gamma_gamma_bond_is_pair_independent_probe.py`](../../computations/probes/gamma_gamma_bond_is_pair_independent_probe.py)
— 11/11, 60 dps, proton pin, convention D.

| ordered pair | `μ` (template `σ₂`) | `μ` (`G³`) | `> 1`? |
|---|---|---|---|
| pp | 0.612688037146465252 | **1.00105775254515984** | yes |
| pn | 0.612688037146465252 | **1.00061119140688078** | yes |
| np | 0.612688037146465252 | **1.00105775254515984** | yes |
| nn | 0.612688037146465252 | **1.00061119140688078** | yes |

### 1a. My stated expectation was refuted

The bean recorded, **before the probe ran**, that the likely outcome was pair-*independence* — which would have
given three equal bond factors and closed Option 1 immediately. Measured: `G³` **is** pair-dependent, spread
`4.47e-4` against the template's `1.6e-61`. The prediction was falsifiable and it was wrong.

### 1b. Option 1 closes anyway, for a sharper reason

**All four ordered pair types exceed 1.** So every `A = 3` chain gets **two** bonds above 1, not exactly one,
and `b3corpus_chain` gives `b₃ < 0` on both atoms — ³He `−6.46e-7`, ³H `−3.74e-7`.

### 1c. And the pair-dependence that exists is ONE-SIDED

The `np` row is an order-reversal control: same unordered pair as `pn`, nucleons swapped.

    |μ_pn − μ_np| = 4.47e-4        →  μ is NOT a function of the pair
    μ_np = μ_pp,  μ_pn = μ_nn  to 1.6e-61   →  μ IS a function of the SECOND nucleon

A bond factor that changes when you swap the two nucleons it joins is **order-dependent**, and
`MassTheory.ChainBondOrderDependence.orderIndependent_iff` records that a nucleus has no arrangement.

**The mechanism is MEASURED, NOT PROVED, and the probe says so.** `G³`'s only block-interior generator is
`σ₃`, which `StrandLayoutForcesChain.crossesBlocks_iff` places inside block 1 (`3 % 3 = 0` does not cross).
That is a *candidate* explanation and no more: `G³` also carries `σ₂`, which is **adjacent** to block 0's `σ₁`
and therefore does **not** far-commute past it, so no commutation argument closes it.

**Controls.** Template `σ₂` reproduces `z_D` on every pair to `5.4e-61` (connected-sum multiplicativity);
`μ_pp(G³)` reproduces step 3's recorded `1.001058` to `2.5e-7`.

---

## 2. Option 2 — the γγ assembly is EXACTLY AFFINE, which is the wrong side

`qou-82mc` (completed, sorry-free `AggregatorConvexityDichotomy`) reduces the `b₃` sign to a **secant
comparison on the ray through the origin**: with `B = Φ(m_A·g)`,

    Φ concave through 0  ⇒  b₃ ≤ 0        Φ convex through 0  ⇒  b₃ ≥ 0

Both machine-checked assemblies are on the concave side — multiplicative/Mayer is strictly concave (`b₃ < 0`);
the additive bond-functional sum is **affine**, the concave *boundary*, `b₃ = 0` exactly. AME2020 needs
`+1.4262225 > 0`, and `qou-82mc` measures AME's own `Φ` strictly convex on `A = 2,3,4`. Its follow-up:
*"identify a candidate `Φ` from Hecke-side quantities that is convex at small argument"*. `qou-q8vl` records
the same route as **"the convexity route, which is unanalysed here"**.

Option 1 handed me a candidate: the corpus's derived assembly is affine *precisely because* the bond product
holds, and `G³` provably violates that theorem's strand-window hypothesis. So the γγ assembly **need not** be
affine.

**Probe** [`gamma_gamma_aggregator_convexity_probe.py`](../../computations/probes/gamma_gamma_aggregator_convexity_probe.py)
— `A = 3` in `H₉`, 60 dps, restricted to the `y_λ > 0` blocks (under SU(2) exactly the ≤2-row partitions;
the 25 dropped blocks carry `y = 0` **exactly**, verified, so this is a restriction and not an approximation).

    δ := μ_both − μ_0·μ_1        δ = 0 is exactly the bond product

| atom | bond | `μ_both` | `μ_0·μ_1` | `δ` |
|---|---|---|---|---|
| ppn | `G³` | 1.00166959044130683 | 1.00166959044130683 | `−1.6e-61` |
| pnn | `G³` | 1.0012227563686974 | 1.0012227563686974 | `+1.6e-61` |
| ppp | `G³` | 1.00211662393076648 | 1.00211662393076648 | `0.0` |
| nnn | `G³` | 1.0012227563686974 | 1.0012227563686974 | `0.0` |

**`δ = 0` to the 60-dps floor — the same floor as the template control.** The γγ assembly is **exactly
affine**, so its log-assembly is additive in bond count and `qou-82mc`'s `b₃` is **0, not positive**. Option 2's
convexity requirement is not met by it.

### 2a. My second prediction was refuted too, and this one is worth keeping

I wrote *"the assembly is NON-AFFINE"* as an assertion — my hypothesis — and the measurement refuted it. The
probe now asserts what is **true** (`the assembly is EXACTLY AFFINE`) so the statement stays falsifiable: a
future bond word that breaks the product will fire it.

### 2b. A scope correction to a theorem that landed the same day

The bond product holds for `G³` **despite** `G³` violating `ProductionChainBondProduct`'s `hlow`/`hup`
strand-window hypothesis. So **those hypotheses are sufficient but not necessary**, and the theorem's reach is
wider than its statement. That is a note for `qou-qqm4`, not a defect.

### 2c. Do not read the per-content `δ` signs as structure

They are `−, +, 0, 0` — and every `|δ|` sits at the **same `1e-61` floor as the control**. Agreement at the
floor of the arithmetic is not evidence about the mathematics (AGENTS.md, probes rule 4). The probe asserts
this so "MIXED" is never quoted as a finding.

---

## 3. Where this leaves the front

**Option 1 is closed at the structure level.** `PnBetweennessBlocksSignMixed` left two escapes — break
averaging, or break affineness. The γγ family breaks **both** (it is not an average of anything, and it is a
length-6 word rather than `σ + d·1`) and still fails, because every bond factor lands on the *same* side of 1.
So the disjunction is not the binding constraint; **being on the same side of 1 is**, and that is a sharper
statement than the two hypotheses it replaces.

**Option 2 is closed for this candidate.** The γγ assembly is affine, i.e. exactly on the concave boundary at
`b₃ = 0`. `qou-82mc`'s follow-up stands unchanged and now has one more ruled-out candidate.

**What is NOT claimed.** That no bond family exists; that no convex `Φ` exists; the magnitude of anything; that
the one-sidedness mechanism is understood. And the two chains' agreement in sign under `G³` is reported, not
required.

---

## 4. Reproduce

```sh
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/gamma_gamma_bond_is_pair_independent_probe.py   # 11/11,  ~2 s
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/gamma_gamma_aggregator_convexity_probe.py       #  6/6,  ~56 s
```

Both emit witnesses alongside, carry the `engine`/`scriptFile`/`commitSha` provenance triple, are seeded from
`Q_50_DIGIT_STR` (never the float64 `q_parameter.Q`), and compute in `mpmath` end to end.
