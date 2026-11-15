# Option I vs Option II: what differs, how they relate, and the full impact of II

Bean `qou-qs4c` (epic `qou-qs0e`), tracker #7735. Date 2026-11-15. Follows
`2026-11-15-quark-equals-strand-implications.md` §6, where the owner ruled **D1 = C (no change
for now)**. This document changes nothing and recommends no switch. It answers the owner's
question *"explain I vs II; does II throw away convention D? deep analysis of the impact of II"*.

## 1. The two options in one sentence each

- **I (the current corpus).** The q-deformed Hecke braiding acts on a **2-dimensional** strand
  space, read as **isospin** (u, d). Its Markov trace is convention D, `z_D = q³/(q²+1)`. Colour is
  a classical label.
- **II.** The same braiding acts on a **3-dimensional** strand space, read as **colour** (r, g, b).
  Its Markov trace is the Wenzl level-3 trace, `z₃ = q⁵/(q⁴+q²+1)`. Isospin is a classical label.

`QuarkStrandConsequences.tensor_crossing_not_hecke` proves one cannot have both in one Hecke
action: on colour ⊗ isospin the crossing has three eigenvalues, so no Hecke relation holds for
q > 1. Hence "I or II".

## 2. What is the SAME in I and II (most of the machinery)

The algebra, the words and the normal forms do not change. What changes is only **which trace
reads them**.

| object | I | II |
|---|---|---|
| algebra H_n(q), relation (σ−q)(σ+q⁻¹)=0 | same | same |
| braid words, GS normal forms, NF(γγ) | same | same |
| Wedderburn blocks λ ⊢ n and characters χ_λ(w) | same | same |
| Markov trace `tr = Σ_λ y_λ χ_λ` | weights y_λ at z_D | weights y_λ at z₃ |
| which blocks are seen | ℓ(λ) ≤ 2 | ℓ(λ) ≤ 3 |

`WenzlWeightLevelR.wenzlWeight_eq_zero_iff` (sorry-free, general r) states that the level-r weight
vanishes exactly on blocks with more than r rows. `wenzlWeight_two_eq_ocneanuWeight` states that
its r = 2 member **is** convention D. So **I and II are two members of one proved family**, r = 2
and r = 3, and they differ in one parameter.

**How they relate, structurally.** The 2-dim space sits inside the 3-dim one
(span{e₁, e₂} ⊂ span{e₁, e₂, e₃}). The Jimbo R-matrix of gl₃ preserves that subspace, and on it
the gl₃ quantum-trace weights (q², 1) are q·(q, q⁻¹), i.e. the gl₂ weights up to a scalar. So the
**level-2 trace is the level-3 trace conditioned on every strand using only two of the three
basis states**.

- *This is the standard Levi embedding U_q(gl₂) ⊂ U_q(gl₃), argued here from the K-weights. It is
  not formalised; gap G1 is that there is no N = 3 Jimbo action in Lean.*
- Under II's reading, convention D becomes **"colour restricted to two of the three colours"**.

## 3. Does II throw away convention D?

**No, and it does not throw away any theorem.** It changes what D *means* and stops using it as the
canonical observable. In detail:

**Kept (the mathematics, all true unchanged):**
- `JimboActionKernel`: N = 2 Schur–Weyl, kernel = blocks with three or more rows, Catalan image;
- `MarkovTraceTLUniqueness`: TL ⟺ D;
- `ocneanuWeight_conventionD_eq_zero_of_three_rows`;
- the TL tower;
- the Q_β augmentation / z_D identification probes.

These are statements about the level-2 member and remain theorems.

**Re-read.** Under II they describe the two-colour sector. That sector contains **no colour
singlet** (y_(1³) = 0 exactly there), so no physical baryon lives in it.

**Lost: D's status as the substrate's observable functional.** Every quantity currently evaluated
at z_D would be re-evaluated at z₃.

**Owner rulings II would need reversed, explicitly:**
1. 2026-08-15 R1, "convention D canonical";
2. 2026-09-08 / D7, "ε = Markov trace at z_D; convention D governs the decay channel";
3. it goes **beyond** 2026-11-15 G5(a), which adopted the SU(N) frame for colour observables
   **only** and states that "z, convention D and the writhe-normalised tr_M stay as ruled"
   (bean `qou-sl3f`; `eightfold-way/sl-n-color-frame-scope.md`).

**The corpus today (after G5(a)) is a hybrid, call it I′.** z_D serves every observable, while
colour factors are computed separately at level 3 in the SU(3) frame. That is consistent as **two
separate evaluations of the same word**. But by P3 it is **not one joint colour ⊗ isospin state at
q₀**, so joint statements (P1, Fermi colour × spin × flavour antisymmetry) hold only at q = 1.

## 4. Measured impact of II

All values were computed in exact rational arithmetic at the proton pin
q₀ = 1.1099785827513808. Floats are used only for display. The script is reproduced in §7.

### 4a. Block weights at n = 3

| | y_(3) | y_(2,1) | y_(1³) |
|---|---|---|---|
| I, z_D = 0.61268804 | 0.50540423 | 0.24729789 | **0** (exact) |
| II, z₃ = 0.44930481 | 0.37837069 | 0.29308249 | **0.03546433** |

- The corpus records that the **mass channel sees y_(3) + y_(1³)**
  (`2026-10-10-level3-su3-channel-test.md` l. 40). That weight moves **0.50540 → 0.41383 (−18.1 %)**.
- The nucleon-type (2,1) weight rises by 18.5 %.

### 4b. Q_β base (the 2026-09-08 ruled cell)

Formula: Q_β = m_e·|h²/2 − h z|·E₀, with E₀ = 1/(q(q−1)). This is exactly the producer's formula,
from `qbeta_augmentation_is_a_markov_trace_probe.py:214-219`, and it reproduces its cells.

| z | Q_β (MeV) | miss vs CODATA 0.78233 | F_required = Q_codata/Q_base |
|---|---|---|---|
| 1 (retired) | 0.78365 | +0.17 % | 0.998 |
| q (augmentation) | 0.87989 | +12.47 % | 0.889 |
| **z_D (ruled, I)** | **0.44470** | **−43.16 %** | **1.759** |
| **z₃ (II)** | **0.30172** | **−61.43 %** | **2.593** |

- **II makes the Q_β base worse, not better.**
- The `c_k` ladder's N = 2 factor is capped at 1 − u² < 1 for every phase (`LadderFactorBound`,
  AGENTS.md 2026-09-14 note). F_required > 1 is therefore unreachable under **both** I and II, and
  the Q_β blocker is not touched by the switch.

### 4c. Compute cost: the image of H_n(q), i.e. Σ_{ℓ(λ) ≤ r} (f^λ)²

| n (= 3A) | blocks r=2 | blocks r=3 | dim image r=2 (Catalan) | dim image r=3 | ratio |
|---|---|---|---|---|---|
| 3 | 2 | 3 | 5 | 6 = 3! (faithful) | 1.2× |
| 6 | 4 | 7 | 132 | 513 | 3.9× |
| 9 | 5 | 12 | 4 862 | 94 359 | 19× |
| 12 | 7 | 19 | 208 012 | 24 792 705 | **119×** |

- The corpus's cheap H₁₂ (bean `qou-38i9`: "the blocks that collapse are precisely the ones where
  colour would live") **is lost under II**. At n = 3, level 3 is faithful, so there is no quotient
  at all.
- Every A ≥ 3 binding computation grows by the ratio above; ⁴He at n = 12 grows ~119× in image
  dimension.

### 4d. The Borromean trace: a measured level-3 cost that framing cannot repair

`2026-10-10-level3-su3-channel-test.md` measured the Borromean trace near-match at 2.69e-4 at
level 3, ~1100× worse than at level 2.

**Correction to my own earlier recommendation.** In `…implications.md` §6 I proposed re-running it
"in the SU(3) frame". That is unnecessary. The frame multiplies an unnormalised trace by
q^{−wr(w)/N}, and the Borromean word has writhe 0 (`sl-n-color-frame-scope.md`: "Words of writhe
zero are unaffected"). So **the 1100× cost stands in both frames**, and the measurement I wanted is
already answered.

### 4e. Binding sign

`qou-v3u2` (μ = z + d ≤ z, so binding is forced when z < 1) is unchanged: z₃ = 0.449 < 1. The
binding *sign* structure survives II, but every binding magnitude moves with the weights in 4a.

### 4f. What II gains

- **Colour one-gluon ratio exactly 2, with both signs right**, in the SU(3) frame (#7830). This is
  exact for every q: the exponents −4/3 and +2/3 are in units of log q.
- **The colour singlet exists** with nonzero weight (0.0355 at q₀; 1/27 at q = 1).
- **The deformed factor is the gauged one**, which is the physically natural assignment.
- **The nucleon magnetic-moment ratio stays at the undeformed −2/3 (2.7 % off).** Under I, the
  Klein-Kreisler moment formula with isospin deformed at q₀ or √q₀ is 15–36 % off
  (`…implications.md` §6; one model, OCR transcription, q-normalisation unsettled).
- **Isospin undeformed matches the observed smallness of isospin breaking** (~10⁻³, against
  q₀ − 1 ≈ 0.11).

## 5. Ledger

| | I (current, z_D) | II (level 3, z₃) |
|---|---|---|
| colour ratio 3̄:6 | not a substrate observable (classical colour) | exactly 2 ✓ |
| colour singlet at q₀ | absent (y_(1³) = 0) | present (0.0355) |
| μ_n/μ_p, one model | 15–36 % off | 2.7 % off (classical) |
| Q_β base | −43.16 % | −61.43 % (worse) |
| Borromean near-match | baseline | ~1100× worse (frame-independent) |
| mass-channel weight y₃ + y₁³ | 0.5054 | 0.4138 (−18 %) |
| compute at n = 12 | 208 012 | 24.8 M (119×) |
| owner rulings | consistent | reverses R1 (08-15) and D7 (09-08); exceeds G5(a) |
| Lean | N = 2 Jimbo proved | needs N = 3 Jimbo action (G1); Wenzl weight already general |

**Reading (judgement, not a finding).**
- II wins every *colour* and *symmetry-pattern* comparison.
- I wins every *number the corpus currently scores* (Q_β, Borromean, mass) and the compute budget.
- That split is what one expects if the scored numbers were tuned around r = 2. **But** z_D was ruled
  on derivational grounds (TL/GNS), not by residual, so that is a suspicion, not a finding.
- A switch now would trade measured scores for structural fit. Under the NO-FITTING directive
  derivational cleanliness ranks first; II's case is structural, but it is not derived either.

## 6. What would decide it (measurements, not decisions)

1. **Formalise the N = 3 Jimbo action (G1)** and prove the Levi-restriction statement of §2. That
   turns "D = two-colour sector" from an argument into a theorem, and it is needed by II anyway.
2. **Settle the U_q-vs-Hecke q normalisation** for the moment test (§4f). Today it is the only
   comparison point that favours II quantitatively.
3. **Find one observable that I and II predict differently and that is not already scored at
   r = 2.** The colour-singlet weight 0.0355 has no experimental counterpart yet.

**Default (the owner's D1 = C ruling stands).** Nothing changes. The corpus stays I′: z_D
everywhere, with colour factors computed separately at level 3 in the SU(3) frame.

## 7. Reproduction

```python
from fractions import Fraction as F
q=F('1.1099785827513808'); me=F('0.51099895069'); tgt=F('0.78233309')
h=q-1/q; E0=1/(q*(q-1)); Qb=lambda z: me*abs(h*h/2-h*z)*E0
zD=q**3/(q**2+1); z3=q**5/(q**4+q**2+1)
# weights: solve sum_l y_l chi_l(w) = tr(w) for w in {1, s1, s1s2}, tr = 1, z, z^2
# chi: (3) 1,q,q^2 ; (2,1) 2,h,-1 ; (1^3) 1,-1/q,1/q^2  (Cramer's rule, exact)
# image dims: sum of (f^lambda)^2 over partitions with <= r rows (hook length formula)
```

At the r = 2 point, y_(1³) at z_D evaluates to exactly 0 in `Fraction` arithmetic, confirming the
convention-D vanishing.
