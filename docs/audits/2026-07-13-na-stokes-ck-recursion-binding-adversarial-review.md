# Adversarial review: the NA-Stokes / depth-2 CKRecursion binding closure

**Date:** 2026-07-13 · **Branch:** `claude/delta-lambda-gate-open-for-all-2026-07-13` ·
**Under review:**
[`content/…/mass-theory/universal-binding-architecture.md`](../../content/quantum-observable-universe/mass-theory/universal-binding-architecture.md)
(prose block) + [`strong-na-stokes-kernel.witness.json`](../../computations/strong-na-stokes-kernel.witness.json) ·
cheat-sheet step **9b** (marked 🟢 "derived … sub-1ppq") ·
**License:** critical-distance red-team. **Scope discipline:** findings are
scope-(a) ("as stated, not a parameter-free derivation"), **not** scope-(b)
("no such kernel can exist") — the volume/bond-count route is genuinely
part-derived (³H to −0.16%, zero fit), so this flags *laundering in the
presentation*, not an impossibility.

## The claim

`w_{n+1} = ½·w_n + r_res·w_{n-1}` (depth-2), with the coefficients from
"exact topological invariants" — the torus-knot trace ratios
`tr(T_{2,9})/tr(T_{2,3}) → 3` (gluonic), `tr(T_{2,5})/tr(T_{2,2}) → 5/2`
(residual), the ½ "from bar-even parity". Claimed to predict ⁴He binding to
**3.4 keV** and to give "exact mass closure across the fundamental light
isotopes … from geometric first principles."

## Findings (verified)

### F1 — the isospin "SU(4) differential 1.4947 m_e" IS the measured ³H–³He split (confirmed)

The block closes the A=3 doublet by "injecting the exact S₃/SU(4)
representation differential (1.4947 m_e)", which "precisely cancels the
remaining disparity, yielding exact mass closure." Arithmetic:

```
B(³H) − B(³He) = 8.48180 − 7.71804 = 0.76376 MeV = 1.4946 m_e.
```

The "1.4947 m_e" is the **measured** ³H–³He binding difference to 4 digits.
Unless `1.4947` is *independently* derived from S₃/SU(4) representation theory
**without reference to the measured split**, "exact mass closure" for A=3 is
circular — the answer is inserted. This is the single strongest red flag: it is
the anti-laundering pattern ("never launder empirical fits through categorical
language"). The burden is on
[`isospin-symmetry-breaking-su4-anomaly.lean`](../../content/quantum-observable-universe/mass-theory/isospin-symmetry-breaking-su4-anomaly.lean)
/ `verify_isospin_bar_anomaly.py` to *derive* 1.4947, not evaluate it.

### F2 — the recursion uses `r_res = 2.596`, NOT the advertised invariant `5/2 = 2.5`

Section 1 calls `5/2` an "exact topological invariant … not a phenomenological
fit." Section 2 then uses `r_res ≈ 2.596` ("the residual strong trace evaluated
at q₀") for the actual ⁴He prediction — **3.8 % above** the advertised 5/2. A
derivation cannot advertise an exact invariant and then substitute a 3.8%-shifted
q₀ number for the number that does the work. The ⁴He "3.4 keV" match rides on
2.596, not on 5/2.

### F3 — the "topological invariants" 3 and 5/2 are just the knot-index ratios; the knot choice is the hidden freedom

`3 = 9/3` and `5/2` are exactly the `n`-index ratios of the chosen `(2,n)` knots
(the witness confirms `tr(T_{2,n})|_{q=1} ∝ n`, so the q=1 ratio *is* `n₂/n₁`).
Nothing in the block derives **why** `T_{2,9}` vs `T_{2,3}` is "gluonic" or
`T_{2,5}` vs `T_{2,2}` is "residual". With the knots free to choose, a ratio in
`[2.5, 3]` is available by selection — that is where the freedom to seed the
recursion at ~2.5–3 lives. "Exact topological invariant" overstates a
post-hoc knot selection.

### F4 — `c_3 = 10/3` conflicts with the canonical c_3 framing

The weak-sector claim "seeding with `10/3` … recovers `c_3 = 10/3` required to
bound the Q_β anomaly" is at odds with the corpus's canonical c_3 (AGENTS.md
2026-05-31 banner; [truncation-order framing](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)):
`c_3 ≈ −2` (= `J_Hopf(q=1)`, near-match tier, cross-anchor swing ≤ 3.47 %).
`10/3 ≈ +3.33` differs in **magnitude and sign**. Either this is a *different*
`c_3` object (then it must be disambiguated — the glyph is overloaded) or it is
an internal inconsistency. This session's merged bar-odd-S work (#3691/#3716)
re-confirmed the `c_3 ≈ −2` near-match as representational; `10/3` does not
appear anywhere in that analysis.

### F5 — accuracy claims are over-stated; validation is effectively single-point

- The cheat-sheet "🟢 derived … T/³He **sub-1ppq**" is not supported: the block's
  own best is ⁴He to **3.4 keV** (`1.2×10⁻⁴` relative), and the parameter-free
  **bond-count** route (`M_n=(n−1)·Vol_n`, 2026-07-04) — the honest part —
  gets ³H to −0.16 % and ³He to −2.97 %. None of these is `1 ppq (10⁻¹⁵)`.
- The ⁴He chain `w_4 ≈ 15.6016 → 28.296 MeV` needs a ×1.81 scaling ("scaled by
  the constituent mass parameters") that the block does not pin. Combined with
  the 2 recursion coefficients (½, `r_res`) and the relabeled isospin term (F1),
  the number of tunable/advertised inputs is comparable to the handful of
  numbers "predicted" (⁴He, the A=3 pair). "Exact mass closure … from geometric
  first principles" is not earned by this ledger.

## Verdict (scope-(a))

As presented, the NA-Stokes / CKRecursion block is **not** the parameter-free
first-principles binding derivation it claims. Confirmed: (F1) the A=3 "closure"
inserts the measured ³H–³He split relabeled as an SU(4) differential; (F2) the
predictive `r_res` is a q₀ number 3.8 % off the advertised invariant; (F3) the
"invariants" are selectable knot-index ratios; (F4) `c_3 = 10/3` conflicts with
the canonical near-match `c_3 ≈ −2`; (F5) the accuracy and "exact closure"
language over-states a 3.4-keV / few-percent result plus a relabeled fit.

**What survives (not refuted):** the *bond-count* multiplicity `M_n(A) = (n−1)`
(linear-chain, zero fit) and the isospin-aware sub-link *volumes* `Vol_n` are a
genuine partial derivation (³H −0.16 %). The honest open items are unchanged: the
**deuteron Hopf-link `Vol=0` wall** (pure-resurgent case — the alien-calculus /
Gevrey-1/2 target), and a *derived* isospin split to replace the inserted
1.4947 m_e. Recommend: (i) demote the "Theorem 1 / exact closure / geometric
first principles" prose to match the evidence; (ii) reconcile or disambiguate
`c_3 = 10/3`; (iii) either derive `r_res` and the knot selection or label them
data; (iv) correct the cheat-sheet 9b "sub-1ppq / 🟢 derived" to the actual tier.

## Anti-laundering note

Per §"Axiomatization is NOT a Proof" and the anti-fit discipline: a fitted or
measured number relabeled in categorical language (F1) does not become a
derivation, and a q₀-substituted constant advertised as an exact invariant (F2)
is not "geometric first principles." Flagged in chat per the critical-distance
license; this doc records the verified arithmetic.
