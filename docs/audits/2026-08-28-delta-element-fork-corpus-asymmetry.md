# The two-Δ fork is real, but the corpus is not symmetric between the two

Companion to [`2026-08-28-cds1-two-nucleon-word-models.md`](2026-08-28-cds1-two-nucleon-word-models.md)
(PR #5897, bean `qou-cds1`), which established that two elements of `H_3(q)`
both answer to `Δ = NF(n) − NF(p)` and priced each. It explicitly declined to
adjudicate which is canonical, correctly: picking one to make the ladder work
is the fit `qou-cds1` forbids.

This is the corpus archaeology that *does not* require picking. Scope-(a)
throughout — nothing here refutes either element, and the adjudication is
still an owner call. What it establishes is that the two sides are not
symmetrically supported, and that one prose site is internally inconsistent
with the corpus's own arithmetic.

## 1. The short element is derived identically in two independent blocks

[`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/nuclear-interactions/neutron-qvalue-symbolic.md)
§"Single-wrap normal-form computation" writes the two nucleons out:

```
proton  [u,u,d]:  L_+ − (h/2)·σ₀
neutron [u,d,d]:  L_+ − h·σ₀ − (h/2)·σ₁ + (h²/2)·γ
```

[`c5-involution-leibniz-decomposition-proof.md`](../../content/quantum-observable-universe/stochastic-mechanics/c5-involution-leibniz-decomposition-proof.md)
§Step 2 writes them as typed-operator products:

```
𝓑_p = σ₀ · (σ₁ − (h/2)·1)
𝓑_n = (σ₀ − (h/2)·1) · (σ₁ − h·1)
```

**These are the same element, verified by expansion rather than assumed.**
With `L₊ = σ₀σ₁` and `γ` the vacuum channel:

- `σ₀·(σ₁ − h/2) = σ₀σ₁ − (h/2)σ₀ = L₊ − (h/2)σ₀` ✓
- `(σ₀ − h/2)(σ₁ − h) = σ₀σ₁ − h·σ₀ − (h/2)σ₁ + (h²/2)·1` ✓ term for term

The check matters: the two blocks *look* like different accounts (one names
the averaged crossing at `σ₁`, the other produces a `σ₀` coefficient), and I
had them down as a conflicting third description until I expanded them. They
are one derivation stated two ways. Both give
`Δ(net) = h²/2 − h`, and `Δ` is supported on `{γ, σ₀, σ₁}` — which is
*why* (D1) is affine in the Markov parameter, a fact readable from the content
block and not only from the probe.

## 2. The 11-crossing count is asserted in three prose sites and derived in none

| site | what it says | derivation |
|---|---|---|
| [`q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.md):10 | "single-wrap construction (proton uud / neutron udd, both 11 typed crossings)" | none — a parenthetical scoping the proposition |
| [`q-beta-gamma-gamma-canonical-derivation.md`](../../content/quantum-observable-universe/stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md):33 | "`𝓑_p` and `𝓑_n` have 11 typed crossings each" | cites `def:categorical-proton` / `def:categorical-neutron` |
| [`c5-involution-leibniz-decomposition-interpretation.md`](../../content/quantum-observable-universe/stochastic-mechanics/c5-involution-leibniz-decomposition-interpretation.md):18 | "7 pure σ₀, 4 pure σ₁, 1 averaged σ₀, 1 averaged σ₁, 3 inverted σ₁⁻¹" | none |

**The one citation offered for the 11 terminates in a different number.**
`q-beta-gamma-gamma-canonical-derivation.md` sources it to
[`def:categorical-proton`](../../content/quantum-observable-universe/knots-particles-confinement/categorical-proton.md),
which states `𝓑₃ = (σ₀σ₁⁻¹)³` — a **six-letter** braid word — and never
mentions 11 anywhere. Typing a crossing may well add letters, but the
definition does not say so and does not give a count. So the citation chain
for the 11 is: parenthetical → parenthetical → a definition stating six.

The count is also what `pyhecke.atom.nucleon_gen_chains` builds, and the long
element **does** reproduce the committed
`qbeta-d-frame-trace-baseline.witness.json` χ^λ to `6.1e-50` (#5897's
calibration). So the compute is not confused about which element it traces.

**The asymmetry, stated exactly:** the short element is derived; the long
element is asserted in prose and realised in code. That is not by itself an
argument for the short one — a construction can be correct and stated without
a derivation, and the code is what the witnesses actually record. It does say
the two sides are not equally evidenced, which is what an adjudication needs.

## 3. One prose site contradicts the corpus's own arithmetic

The interpretation block gives the **proton** *"1 averaged σ₀, 1 averaged
σ₁"* — two averaged crossings. Its own proof sibling gives the proton
**ONE** averaged crossing, and reserves two for the neutron.

The arithmetic decides this without reference to either claim.
`c5-...-proof.md` §Step 3: *"The `h²/2` term is the product of TWO
averaged-crossing `h/2` contributions (the neutron has two such
positions)."* A proton with two averaged positions would therefore carry an
`h²/2` term. It does not: `net(p) = 1 − h/2`, first order in `h`, in both
deriving blocks and in every consumer.

**So the interpretation block's averaged-crossing count for the proton is
wrong**, independently of which element is canonical. It is a `remark`-tier
interpretation sibling, so nothing derives from it — but it is the single most
specific-looking statement of the 11-crossing decomposition in the corpus, and
it is the one a reader would most naturally take as authoritative.

## 4. A dead attribution, in passing

[`deuteron-binding-dressing-proton-net.md`](../../content/quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md):2
sources its net coefficients *"(from `conj:borromean-quark`)"*. The string
`net` occurs **zero** times in
[`borromean-quark.md`](../../content/quantum-observable-universe/observations/borromean-quark.md).
The coefficients are real and derived — in `neutron-qvalue-symbolic.md`, which
that block also cites — so this is a mis-aimed pointer, not a missing result.
Same class as the dead citation AGENTS.md records correcting on 2026-08-11.

## What this does and does not settle

- **Does not** adjudicate which element is canonical. `qou-bg3w` stays open.
- **Does not** touch #5897's pricing. Its 92.106× / 257.26× figures stand;
  I re-verified its two structural claims from source (the probe's mixed
  `eps`/`chi_all_lambda` sourcing at
  `qbeta_d_frame_trace_baseline_probe.py:130` vs `:104`, and 11 crossings
  counted by hand off `nucleon_gen_chains`).
- **Does** give the adjudicator an evidence asymmetry and one demonstrably
  wrong prose count to remove from the picture first.
- **Does** narrow what an adjudicator has to weigh: on the prose side the 11
  has no derivation and no citation that states it, so the live case for the
  long element rests on the code and on the witnesses it reproduces — which is
  a real case, and a different one from the prose.

## Method note

This is the fifth count in this arc to move on being read by hand, and the
first where the correction went *against* my own hypothesis mid-check. I
proposed that "single-wrap" separated the two models; the next grep found the
same qualifier attached to the 11-crossing construction, refuting it. The
habit that pattern argues for is not "distrust detectors" but "state the
hypothesis so the refuting grep is one command away".

## Addendum 2026-08-28 — the "possible third model" is real, is canonical, and is NOT an anchor artifact

#5897 flagged a third coordinate-sum value in `pyhecke` (`−0.188291`, 0.58 % from
`epsNPq`) as *"a pointer, not a measurement — stored float64, basis convention
unverified"*. Two things can now be said about it.

**It is not only in `pyhecke`.** The same value is
`transition.delta_net = -0.1882906200111204` in
[`computations/free-neutron-decay.witness.json`](../../computations/free-neutron-decay.witness.json),
which **20 Python consumers** read and which several of them call *"the canonical
free-neutron-decay witness"*. It is the source of `Δ(net)(q)` for the `c_k`
S-series work. So the third value is not a stray in a helper package — it is the
canonical one, and the two closed forms in `qbeta-counit-closed-form.md` disagree
with it.

**It is not the anchor.** The cheapest explanation would be that `h²/2 − h` is
being evaluated at a different q₀. Measured at 50 dps against all three:

| anchor | `h²/2 − h` | vs `delta_net` |
|---|---|---|
| proton `q_at()` | −0.187207194529378 | −0.5754 % |
| muon, frozen canonical | −0.187207212879143 | −0.5754 % |
| muon, superseded CODATA-2018 | −0.187207212874623 | −0.5754 % |

The three anchors differ from each other in the **8th** significant figure —
the 11.5 ppb μ–p tension, i.e. ~1.15e-6 %. The gap to `delta_net` is
**0.575 %**, five orders larger. **Anchor choice cannot produce it**, so
`delta_net` is a different quantity, not a re-evaluation. Scope-(a): this
excludes one explanation, it does not identify what `delta_net` is.

That is worth having because it is the explanation an adjudicator would try
first, and because this witness carries the superseded muon pin — which makes
"it is just the old q₀" look plausible until it is measured.

**Consequence for `qou-bg3w`.** The fork is not two elements plus a loose
pointer. It is two elements with published closed forms, and a third value
sitting in the witness that 20 producers actually consume.

