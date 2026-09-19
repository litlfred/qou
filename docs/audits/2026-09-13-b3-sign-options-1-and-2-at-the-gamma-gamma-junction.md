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

**Option 1 is closed at the structure level.** **🛑 CORRECTED 2026-09-13, after a sibling flagged it on #7287 and I verified it at source.** This section
read: *"`PnBetweennessBlocksSignMixed` left two escapes — break averaging, or break affineness. The γγ family
breaks **both** … so the disjunction is not the binding constraint."* **Two things in that are wrong**, and the
correct version makes this PR's negative *more* interesting rather than less.

**(i) They are not two independent escapes.** `InterfaceMonotone.between_iff_combo` (PR #7255, on `main`):
over an ordered field, *"`d_pn` lies strictly between `d_pp` and `d_nn`"* and *"`d_pn` is a convex combination
of them"* are the **same condition**. Averaging is not separately breakable.

**(ii) Breaking affineness, on its own, buys nothing — the invariant is MONOTONICITY.**
`InterfaceMonotone.signMixed_impossible_of_monotone` holds for **any monotone interface law, affine or not**,
and its own docstring says so: *"abandoning affineness, on its own, buys nothing: the construction is dead
before any bond value is computed."* Verified against `origin/main`, not taken from the comment.

**What the γγ route actually is, and it IS in the live class.** `μ(x) = tr_M(W·x)/tr_M(W)` has a numerator
**linear in `x`**, so along an *affine path* `x(t) = x₀ + t·x₁` it is affine in `t`, hence monotone or antitone,
hence blocked either way. `G³ = (σ₂σ₃⁻¹)³` is a **power, not a sum** — not an affine path — so the affine block
does not reach it, and the power family is independently measured **non-monotone**. So the door this route
needs is genuinely open; §1 is a measurement of a **live candidate**, not a foregone conclusion.

**And §3a explains why the betweenness framework does not reach `G³` at all.** Both hypotheses are stated
about a *pair function* `f(d_pair)`. `secondOnly_eq_bondOf_iff` shows the γγ bond factor is **not a pair
function** — it reads one endpoint. It is outside the framework's domain, which is a different and cleaner
reason than "it breaks affineness".

**So the corrected statement of what §1 adds** is not "the disjunction is not the binding constraint". It is:
the γγ family occupies the one structurally-permitted door — non-monotone, non-pair-function — and **fails
there numerically**, because all four ordered bond factors land on the *same side* of 1. That is a measurement
the structure did not force.

**Option 2 is closed for this candidate.** The γγ assembly is affine, i.e. exactly on the concave boundary at
`b₃ = 0`. `qou-82mc`'s follow-up stands unchanged and now has one more ruled-out candidate.

**What is NOT claimed.** That no bond family exists; that no convex `Φ` exists; the magnitude of anything; that
the one-sidedness mechanism is understood. And the two chains' agreement in sign under `G³` is reported, not
required.

---

## 3a. Lean — what of this is provable, and one correction to my own framing

Most of the 13 probe assertions are **numeric measurements at `q₀`** and are not theorems. Of the ones with
structural content, the corpus already proves them (`b3corpus_chain_neg_of_same_sign`,
`b3_eq_zero_ofBondFunctional`) — cited, not re-proved. **Two were genuinely new**, and the first corrects §1c
above.

[`QOU/MassTheory/SecondArgBondNotPairFunction.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/SecondArgBondNotPairFunction.lean)
— 7 declarations, `lean`-direct **exit 0, zero errors, zero warnings**
(`-DautoImplicit=false -s 65536`), `#print axioms` clean.

**§1c understated the finding.** I wrote that the bond is *"order-dependent, and
`ChainBondOrderDependence.orderIndependent_iff` records that a nucleus has no arrangement"*. But `bondOf` is

    bondOf Lpp Lpn Lnn a b = if a = b then (if a then Lpp else Lnn) else Lpn

which is **symmetric in `a` and `b` by construction** (`bondOf_comm`). So a second-argument-only bond does not
merely *violate* arrangement-invariance:

    secondOnly_eq_bondOf_iff : (∃ Lpp Lpn Lnn, secondOnly f = bondOf …) ↔ f true = f false

it is **not of the `bondOf` form at all** unless constant. The corpus's whole chain calculus (`bondSum`,
`orderIndependent_iff`, `not_orderIndependent_of_ne`) is stated over `bondOf`, so a non-constant one falls
**outside its domain** rather than contradicting its conclusion. Measured `f true = 1.00105775`,
`f false = 1.00061119`, so the γγ bond factor is not any `bondOf`.

Two anti-vacuity guards, since an iff is cheap to satisfy vacuously: `secondOnly_const_is_bondOf` puts the
constant case inside the family; `bondOf_ne_secondOnly_witness` gives an explicit non-constant `Bool` witness
outside it.

**`weighted_diff_supported_on_multidim`** formalises §2's cross-arc reconciliation: if every 1-dimensional
block agrees on two words, the whole difference of a `y`-weighted character sum is carried by the blocks of
dimension `≠ 1`. That makes the reconciliation with `qou-99qc`/#7295 independent of `q₀`, where before it
rested on the numeric companion (1-dim `9.0e-62` vs ≥2-dim `1.729e-3`).

Axioms: six declarations on `[propext]` alone; `weighted_diff_supported_on_multidim` on
`[propext, Classical.choice, Quot.sound]` from `classical`. **No `sorryAx`.** Generic per §7c — `bondOf`
carries no typeclass and the decomposition asks only for `CommRing`.

## 4. Reproduce

```sh
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/gamma_gamma_bond_is_pair_independent_probe.py   # 11/11,  ~2 s
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/gamma_gamma_aggregator_convexity_probe.py       #  6/6,  ~56 s
```

Both emit witnesses alongside, carry the `engine`/`scriptFile`/`commitSha` provenance triple, are seeded from
`Q_50_DIGIT_STR` (never the float64 `q_parameter.Q`), and compute in `mpmath` end to end.
