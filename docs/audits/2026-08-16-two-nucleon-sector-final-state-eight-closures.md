# The two-nucleon sector: final state — eight closures, and what is left

**Date:** 2026-08-16
**Branch:** `claude/l2-1ppq-mass-binding-mh643j` (PR #5256)
**Beans:** `qou-brg3` (closed), `qou-bid3` (closed), `qou-y0mc` (open)
**Status:** scope finding, consolidated. **Supersedes**
[`2026-08-16-two-nucleon-sector-scope-five-closed-routes.md`](2026-08-16-two-nucleon-sector-scope-five-closed-routes.md),
which is kept as the record of the five-route state and carries a forward pointer.

No repair is proposed. Nothing is fitted and nothing is wired.

---

## 1. What is wrong (unchanged)

`_bond_type_L` defines each per-bond suppression as the **isolated** two-nucleon
log-trace-ratio, so `L_pp` **is** the diproton and `L_nn` **is** the dineutron.

| system | framework | nature | |
|---|---:|---|---|
| pn (deuteron) | **+2.8328** MeV | `B = +2.2246` — BOUND | 27.3 % over |
| pp (diproton) | **+2.5416** MeV | `a^N_pp = −17.3 fm` — **UNBOUND** | **WRONG SIGN** |
| nn (dineutron) | **+3.3069** MeV | `a^N_nn = −18.9 fm` — **UNBOUND** | **WRONG SIGN** |

The framework predicts bound states that do not exist. Section 2 of the
predecessor proves this is structural (`μ ≤ z < 1`, unbinding needs
`q > 1.46557` against `q₀ = 1.10998`), not a bad parameter.

## 2. The closure table — eight, and how each closed

| # | route | why it fails | evidence |
|---|---|---|---|
| 1 | single crossing, any `d` | `μ ≤ z < 1` | **Lean**, scope-(b) |
| 2 | `T₃`-graded writhe | non-negative exponents on a base in `(0,1)` bind *harder* | **Lean**, scope-(b) |
| 3 | stacked powers `σ^m` | writhe factor common to both channels, cancels; surviving `q^{2m}` orders them backwards | measured + **Lean** |
| 4 | writhe-derived framing `f` | every candidate leaves `nn` at `f = 1–2` against a required `f ≥ 3` | measured, 3 candidates |
| 5 | operator-selection LP | Frobenius positivity — its core premise — **fails**: the form is indefinite, the program unbounded, the "active set" a box artifact | measured, both bases |
| 6 | drop the 2-dim subalgebra for full `H₆` | **retracted result.** With the production character routine three of four surviving blocks BIND; the weighted max is the trivial rep at `q ≈ 1.11`, forced | measured, corrected |
| 7 | **any T-odd rescaling, at any framing** | the total `B(T=1)+B(T=0) = −α·log(μ₊μ₋)` is **invariant** under `(μ₊,μ₋) → (μ₊t, μ₋/t)`, and `μ₊+μ₋ = 1` floors it at `α·log 4 = 5.8030` against nature's `2.1510` | **Lean**, scope-(b) |
| 8 | **rescale `α`** | the chain over-binds exactly one nucleus (²H, 1.27×) and under-binds every other by ~3×; `B_chain` is linear in `α`, so the two-nucleon floor (`α ≤ 1.5516`) and the many-body deficit (needs `α` larger) have an **empty** intersection | measured, whole chart |

Routes 7 and 8 are the new ones and they are the strongest, because neither
needs a candidate to be named. Route 7 closes an entire *class* without deriving
its parameter; route 8 closes the last free scalar in the law.

### Why route 7 supersedes route 4 rather than repeating it

Route 4 tried to derive the framing `f` and failed at `nn`. Route 7 shows there
was nothing to derive: the framing cancels identically in the total, verified at
`f = 0, 3, 10, −8.297` to 50 digits (spread `1.07e-50`). The predecessor's
honesty flag — *"`f = 3` is a fit"* — is superseded by something stronger.

### The sub-normalisation escape runs backwards

The intuitive repair is *"the colour-only fibre lacks a spin/spatial factor, so
the two channels carry only `s < 1` of the trace, and the floor drops."* It does
not. `μ₊μ₋ ≤ s²/4` **shrinks** with `s`, so a smaller normalisation binds
*harder*; reaching nature needs `s ≥ 1.547 > 1`, which a projector decomposition
of a normalised trace cannot supply. More channels is also wrong-way — the
`k`-channel floor is `α·k·log k`, rising. **This re-points the sibling question**
("can the colour-only fibre host `³S₁`/`¹S₀` at all"): a *smaller* fibre makes
the magnitude worse, so that question is about the sign only, not the magnitude.

Recorded because the wrong direction is the intuitive one and an earlier
revision of the companion probe asserted it.

## 3. The binding law was checked, and it is derived

Every closure above rests on `B = −α·log μ`, so the law itself was tested.
[`markov-trace-gibbs-free-energy.md`](../../content/quantum-observable-universe/mass-endomorphism/markov-trace-gibbs-free-energy.md)
gives `E_bind = E₀·ln(tr_M(W_free)/tr_M(W_atom))`, a Gibbs free-energy difference
with `kT = E₀`, on Markov traces as temperature states (Jones 1987). With
`tr_free/tr_atom = 1/μ` exactly, that **is** `−E₀·log μ`. The floor is therefore
not an artifact of a conventional choice.

**But the same block names a second, inequivalent object** two sentences later —
the entropy of the normalized channel measure. For a two-channel split:

| | | range | MeV | vs nature |
|---|---|---|---:|---:|
| implemented | `S = −log μ₊ − log μ₋` | **≥ 2 log 2** | 7.0377 | 3.27× |
| named | `H = −μ₊log μ₊ − μ₋log μ₋` | **≤ log 2** | 2.3414 | 1.09× |
| nature | | | 2.1510 | — |

Disjoint ranges. Nature sits outside `S`'s and inside `H`'s, which accounts for
the whole 3.27×.

**This is filed as an ambiguity (`qou-y0mc`), not a result**, and the fit-based
resolution is explicitly blocked. Four reasons, all applicable: it is *post-hoc*
(sought only after the floor failed); it **does not fix the sign**, which is the
primary defect (`−α·μ·log μ > 0` always, so both channels still bind); the ±10 %
window is **14.8 %** of the available `[0, log 2]` range, so an 8.85 % miss is not
a near-hit; and `S` is the block's headline equation while the channel-measure
line is a secondary remark. What would settle it is a derivation of *which object
confinement reweighting costs* — not a preference for whichever fits.

Independently of that: the block is **self-inconsistent as written** for any
2-channel split, and should be reconciled or scoped regardless of which wins.

## 4. What survives

* **Every Lean theorem.** The interface theorems of the predecessor's §4a, plus
  the seven in
  [`TwoChannelTotalBindingFloor.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/TwoChannelTotalBindingFloor.lean)
  (sorry-free, `lean`-direct exit 0, `[propext, Classical.choice, Quot.sound]`).
  None routes through `atom_character_raw`, so none is touched by the route-6
  retraction.
* **The chain's additivity**, verified to `1.78e-15` against the exact `p(3A)`
  trace.
* **The dimensionless ratios elsewhere** (`m_K/m_π` at 51 ppb, parameter-free) —
  they do not route through the binding chain.

## 5. What is left

Exactly two items, and neither is a two-nucleon item:

1. **The many-body collective term.** `R(A) := B_AME/A − B_chain/A`, with
   `R/α = 1.3240` per nucleon at plateau. Two screens constrain it: magnitude
   (1.90× the chain's own asymptote) and scaling (kills an unsuppressed
   all-pairs term). This is the many-body side's own open item, tracked as
   `qou-ls86`.

   > **The third screen — "mixed-sign in `A`" — is WITHDRAWN as stated
   > (2026-08-17).** It was measured on a 14-isotope convenience sample and used
   > to exclude "anything manifestly non-negative by construction — an entropy, a
   > KL divergence, a dimension count, a positive Plancherel weight". Over the
   > full AME2020 table (3554 nuclides) **7 rows have `R < 0`, and every one has
   > `B_AME/A < 1.73` MeV/nucleon** — six of them particle-unbound drip-line
   > exotics (⁵Be, ⁷H, ⁶H, ⁴Li, ⁵H, ⁴H), the seventh the deuteron. Among the
   > **3519 nuclides with `B_AME/A > 5` (99.0 % of the chart) there are zero
   > negatives**, and `R ∈ [+2.10, +5.89]`.
   >
   > Those negatives re-measure the *already-proved* interface defect rather than
   > the collective term: `B_sym` is positive for every `(Z,N)`, so wherever
   > nature has ~zero binding the chain must over-bind. **Replacement, scope-(a):**
   > on the well-bound regime `R` is strictly positive and bounded, and
   > non-negative candidates are **not** excluded there. Do not cite the old
   > screen against them.
2. **`qou-y0mc`** — the `S`-vs-`H` derivation above.

**The predecessor's §5 obstruction list is withdrawn.** Its item 1 ("7 of 11 `H₆`
blocks have `r_λ < 0`") cited the H₆ analysis that its own §4b retracts — an
internal inconsistency in that document. Its item 2 ("no selection principle")
is now moot: route 6 shows there is nothing worth selecting *from*. Its §6
"remaining candidates" list (an index, a positivity condition, a variational
criterion) is likewise withdrawn — all three route through the interface, and
route 7 closes the interface class as a whole rather than candidate-by-candidate.

## 6. Honest statement

The two-nucleon sector needs a **structural change**, not a correction, and the
space for corrections is now measured rather than guessed: six interface-side
routes, the entire T-odd class, and the last free scalar are all closed, six of
them with sorry-free Lean invariants. What remains is a change to the binding
law or to what the two-nucleon states are — both larger than a parameter.

This is a scope finding about one sector. It says nothing about the framework's
dimensionless-ratio results, which do not pass through this chain.

**On the reliability of this document.** The session that produced it recorded
five retractions, including one — route 6 — that reversed the only positive
structural result on the axis, and one caught pre-commit (the sub-normalisation
direction). The Lean theorems are the part to weight most heavily: they are
machine-checked and none of them depends on any retracted code. The probe-level
conclusions are weaker evidence and are labelled scope-(a) or scope-(b)
individually.
