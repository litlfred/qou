---
# qou-59j5
title: 'GAP: the extensive term has no derived energy scale -- m_e vs E_0 moves it 8.19x'
status: completed
type: task
priority: high
created_at: 2026-08-31T04:13:26Z
updated_at: 2026-08-31T04:29:11Z
---


## The finding

The Markov normaliser `Z(n) = (1+q₀²)ⁿ` is a **dimensionless** partition
function. Turning `log Z` into MeV needs an energy, and **the framework does not
derive one**. Two different scales are in current corpus use and they differ by

    E₀ / m_e  =  1 / (q₀(q₀ − 1))  =  8.1917611722

| scale | value | used by |
|---|---|---|
| `m_e` | 0.51100 MeV | my three extensive-term probes, this session |
| `E₀ = m_e/(q₀(q₀−1))` | 4.18598 MeV | `computations/b_over_a_evaluator.py` ("Hadronic energy unit", the scale of every B/A prediction there); the `B_sym` linear chain, where `α = E₀` is CAL-1; the ROAST's own `E₀ log N` |

Every "the extensive term is short by ~7×" statement in this lane is **that
ratio**, not a measurement. `m_e` is the outlier and it is mine — I never gave a
reason for it. `E₀` is the corpus's, but it is CAL-1, a *calibration*, not a
derivation. So neither side is pinned, and until one is, no `N×` claim about the
extensive term means anything.

This is the ROAST's own §A1 complaint — "choosing the member that lands on the
target IS a fit" — one level up, applied to the units rather than to the
normalisation convention. I made exactly the error I was auditing.

⚠ **`E₀` is an overloaded name.** `computations/atom_mass_derived.py` defines
`E0_MEV = m_p / tr_M(proton) = 1662.7295 MeV`, a factor **397.21** away and a
different object entirely (it belongs to the absolute-mass chain excised
2026-08-11, bean `qou-exam`). Say which `E₀` you mean.

## The numbers, corrected

Probe: `computations/probes/extensive_term_energy_scale_reconciliation_probe.py`
(4 assertions, all passing).

At `E₀`, 3 strands/nucleon, over the normaliser convention family:

    8.722 … 11.597 MeV/nucleon      (at m_e it was 1.065 … 1.416)
    vs B/A plateau 8.5   →  1.03× … 1.36×  OVER      (was 6.0–8.0× short)
    vs a_V 15.8          →  1.36× … 1.81×  short     (was 11–15× short)
    family span          →  1.33×,  the SAME SIZE as the deficit

## Two verdicts this overturns

* **`qou-78pt` — WITHDRAWN.** "A1 REFUTED" rested on span 1.33× being two orders
  of magnitude smaller than a 6–15× deficit. Corrected, span ≈ deficit, which is
  exactly the condition that makes choosing a member a fit. **A1 reverts to
  "unfalsifiable as written"** and the ROAST was right the first time: pinning
  the convention from the axioms is the actual work. Probe docstring, witness
  and verdict all annotated in place; the original text is kept so the
  retraction has something to point at.
* **`extensive_counter_family_probe`** — its `no_family_member_reaches_plateau`
  assertion is renamed `..._AT_THE_m_e_SCALE` and is **false** at `E₀` (family
  max 46.39 MeV/nucleon). The conclusion "the missing factor is neither a
  normalisation nor a counter" is withdrawn.

**`qou-imcd` survives.** Its exponent test is scale-free — a constant multiplier
cannot change a log–log slope — so `log Z(3A)` is still exactly linear in `A`
and the braid→nucleus map is still not the defective step. Only its `6.906×`
residual figure is withdrawn.

## The unreconciled ROAST number, resolved

`markov_normalisation_convention_span_probe` logged an open discrepancy: the
ROAST's "~2.91 MeV/strand" against my 0.355–0.472, with "the ROAST does not show
its construction". It does, one sentence earlier — *"the extensive coefficient is
`E₀ log N`"* — and

    2.91 / E₀ = 0.695176   vs   ln 2 = 0.693147     (0.3 %)

while at `m_e` the figure is **unreachable**: it would need a normaliser with
`log = 5.695`, against a family whose logs span 0.694–0.923. Failing to
reproduce it was the tell, and I filed it as "unreconciled" instead of chasing
it. That is the lesson worth keeping from this bean.

*(Not fully determined: `E₀·ln 2 = 2.9015`, and the ROAST wrote `2.91`, which is
also exactly the `B_sym` chain's per-bond constant `b_pp = 2.91` — same `α = E₀`.
The documents do not distinguish the two, and it does not matter here: both are
`E₀`-scaled. If it was `b_pp`, the ROAST also mislabelled a **per-bond** constant
as **per-strand** and then multiplied by 3 strands/nucleon.)*

## What would actually close this

A derivation of the energy scale from the axioms, not a calibration. Candidates
to test, in order of how much structure they would need:

1. **Is `E₀ = m_e/(q₀(q₀−1))` derivable?** It is currently CAL-1. `q₀(q₀−1)` is
   not an obvious partition-function quantity; find out whether it is one.
2. **Does the scale cancel in a ratio?** Every L2 *ratio* observable (`m_μ/m_e`,
   `m_K/m_π`) is scale-free by construction, which is why they were never
   affected. If the extensive term can be phrased as a ratio to something else
   extensive, the question dissolves. `B/A` against `a_V` is not such a ratio —
   both carry MeV.
3. **The `B_sym` per-bond route as the cross-check.** `b_pp/b_pn/b_nn =
   2.91/3.89/5.18` (log form) and `2.38/2.49/2.53` (signed form) are two
   different functors of the same trace agreeing on the chain structure. They
   use the same `α = E₀`, so they do **not** independently pin the scale — but
   the ratio `b_nn/b_pp = 1.78` is scale-free and is a real prediction.

Do **not** report another "N× short" figure for the extensive term until (1) is
settled either way.

---

## 2026-08-31 — ANSWERED: **NO.** And the problem is bigger than this bean said.

Probe: `computations/probes/e0_convention_ladder_probe.py` (3 assertions, all
passing).

### 1. `E₀` is not derivable, and the corpus already established that

`computations/derivation_chain.py` carries an `E_0_CONVENTIONS` registry.
Convention A's own `derivation` field answers the question directly:

> "Closed-form algebraic substitution from CAL-1 m_e + CAL-2 q_0. … the existing
> direct LP-dual probe at H_3 reports y_0^* DIMENSIONLESS, far from 4.186 MeV —
> **so the MeV scale of E_0 still comes from CAL-1 + CAL-2 outside the LP**, not
> from the LP dual directly."

The single attempt to derive it — convention **D**, the operator-selection LP
dual, `derive_e_0_lp_dual_h3.py` — is a **recorded negative finding**. Read from
its committed witness: `y₀* = 0.375387` (dimensionless) for all four targets, so
`y₀*·m_e = 0.191822 MeV` against convention A's `4.185981` — **a factor of
21.8**. Its own `negative_finding` field: *"The LP-dual does NOT derive E_0 in
MeV; it gives a dimensionless action shadow price."*

So this bean's item 1 ("is `E₀ = m_e/(q₀(q₀−1))` derivable?") closes **NO**, and
it does not need another attempt — it has had one, and the failure is documented.

### 2. It is not two scales in tension. It is a four-convention registry, 256× wide

I framed this as `m_e` vs `E₀`. Wrong shape. The registry is indexed by
(`ℏ_q` power, Hecke level, operator class):

| convention | `E₀` | `ℏ_q` | level | operator class |
|---|---|---|---|---|
| `A_single_hecke_tick` | **4.18598 MeV** | ℏ_q¹ | H₃, 3 strands | `Δ_NF`, β-decay single wrap |
| `B_q_value_absorbed` | **0.78233 MeV** | ℏ_q⁰ | H_{3A}, 3A strands | `\|tr_M(W_free)\| − \|tr_M(W_atom)\|` |
| `C_proton_back_fit` | ~200 MeV | ? | H_{3A} | ⚠ DISCIPLINE VIOLATION, do not consume |
| `D_lp_dual` | N/A — dimensionless | — | — | not an `E₀` derivation |

and **`m_e = 0.511 MeV`, which my three probes used, is not in the registry at
all** — no entry, no operator class, no ℏ_q index.

**A and B are not two guesses at one number.** They are (scale) and
(scale × operator): `A·|Δ(net)| = 0.7836458` against CODATA `Q_β = 0.7823334`,
agreeing to **0.168 %**, with `Δ(net) = h(h−2)/2`, `h = q−1/q = ℏ_q(q+1)` so the
operator is exactly ℏ_q¹ and both routes total ℏ_q². Which convention a quantity
takes is decided by the ℏ_q power the quantity already carries — not by taste.

### 3. The rungs are 102× apart, and my 8.19× slip was a small step on that ladder

The registry warns that mixing convention A with a B-style operator "would miss
the `1/ℏ_q²` factor (≈ **102×** error)". Measured, `1/ℏ_q² = 101.862` — so the
stated 102 is exactly the ℏ_q bookkeeping, confirming the ladder's spacing
independently of the prose. **The uncertainty in the extensive term's scale is an
order of magnitude larger than the error I corrected earlier today.**

### 4. Why it stays open: `log Z(3A)` matches no registered operator class

* its **Hecke level** is H_{3A} → points at **B** (1.884 MeV/nucleon);
* its **ℏ_q content is zero** — `log(1+q₀²) = 0.803` is O(1), not small → points
  at **A** (10.083 MeV/nucleon);
* its **operator class** is none of the registered ones. It is neither `Δ_NF` nor
  a trace *difference* nor a mass assembly. It is the logarithm of a partition
  function.

The registry cannot adjudicate, and the two candidates differ by **5.35×**.

    at convention A   10.083 MeV/nucleon   →  1.57× short of a_V
    at convention B    1.884 MeV/nucleon   →  8.38× short of a_V
    at m_e (mine)      1.231 MeV/nucleon   → 12.84× short of a_V

### Verdict

**"The extensive term is short by N" has no determinate N.** Stop quoting
magnitude deficits for it. What survives is scale-free and should be what the
lane reports:

* the A-exponent of `log Z` is exactly 1, the SEMF volume exponent (`qou-imcd`);
* the four counters are exactly linear — `bonds A−1`, `averaged 2A+1`,
  `strands 3A`, `letters 12A−1` — and `letters = 4 × strands`;
* the framing factor `(1+q²)/(q+1/q) = q` exactly (`qou-78pt` assertion 1);
* `b_nn/b_pp = 1.78` in the `B_sym` chain.

### Successor question (do NOT reopen as "derive E₀")

The tractable question is not "what is `E₀`" but **"what ℏ_q power does `log Z`
carry, and does the framework assign an operator class to a bare partition
function at all?"** That is answerable from the Hecke side without any energy
scale, and it would select between A and B rather than inventing a fifth
convention. If the answer is "no operator class", then the extensive term is not
an energy in this framework and the whole comparison to `a_V` is category error —
which would itself be a result.

### Also fixed here

`derive_e_0_lp_dual_h3.py`'s docstring reported `y_0^* = 0.1245` and
`x^* = (0,…,0,1)`; its committed witness records `0.3753866` and a cone `x^*`
with two components at `0.49956`. The prose predates that file's own 2026-08-23
`scipy.linprog → clarabel-MPFR` change. Corrected in place; the conclusion is
unchanged (21.8× rather than 65×). The `negative_finding` **string emitted into
the witness** still carries the stale `≈ 0.124` — flagged in the docstring for
whoever next runs that script, since fixing it requires a clarabel-MPFR run.

## 2026-09-04 — the number, from the full table

With the additive law adopted as the working assumption, this gap is now ONE
dimensionless factor. Over 2548 measured AME nuclides the best single scale for
`B = scale . log(tr_free/tr_atom)` is **11.119 MeV**; the derived
`E_0 = m_e/(q0(q0-1)) = 4.18598 MeV` is **2.656x** below it
(`qbeta_binding_law_options_probe.py`).

Recorded as a target for a future derivation to be checked AGAINST, never a
criterion to search on. Two companions in the same category, also recorded not
searched: `E_0.|ln z| = 2.0507 MeV` is the per-p-p-bond energy in Markov-weight
units, and the residual ceiling sits at 3.00-3.01 across the iron peak with 4He
alone above at 3.259.

This is the surviving half of `qou-2pnv` (derive-or-retract): the DERIVE half
landed 2026-09-04, the SCALE did not.
