# `conj:canonical-knot-id-sdp` — the assignments are an admitted fit, and the deuteron bridge is structurally impossible

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) ·
**Beans:** `qou-8ms1` (the lead this refutes), `qou-9ot5`

Owner asked: *"can we attack open `conj:canonical-knot-id-sdp`?"* — after I flagged
`m_e·Vol(6₂) = 2.2488 MeV` against `B_AME(²H) = 2.2246` (**+1.09 %**) as a lead worth
chasing, since the production Markov-closure route misses by +27.34 %.

## Verdict: the +1.09 % is not a result. Do not quote it.

**It is the residual of a search whose objective *was* `B_AME`.** Stated verbatim in
production source, [`computations/mass_table_ppb.py`](../computations/mass_table_ppb.py)
L11-22 — verified by reading the file:

> ```
>   D    ↔ 6_2            (handover hypothesis, not derived)
>   T    ↔ 8_11           (handover hypothesis, not derived)
>   3He  ↔ Borromean L6a4 (handover hypothesis, not derived)
> ```
> *"The atom→knot assignments for D, T, ³He were obtained by census search in
> `jsj_verification.py` — **that IS a form of AME-driven fitting (we picked the knot whose
> volume is closest to `B_AME/ρ`)**. Flagged here as `hyp: by-census` so the reader can
> distinguish."*

`jsj_verification.py` confirms it mechanically: it scans `snappy.LinkExteriors` keeping
`abs(v − tgt)/tgt < tol` with `tgt = B_AME/(ρ·m_e)`. **The selection criterion is
proximity to the experimental binding energy.**

The corpus was honest about this the whole time; **I did not read far enough before
calling it a lead.**

## The SDP does not select anything

- `binding-k-solver.witness.json`: *"Binding-K factorisation **EVALUATOR** … **NOT a
  search/optimisation step** — computed deterministically from the **presupposed** `T_w(𝔥)`
  **historical** braid."* Its `knot_name: "6_2"` is a hardcoded **input**.
- `joint_tower_sdp_solver_v2.py`: the program is `Find c_w s.t. ρ(T_w) ⪰ 0` — a
  **feasibility** check on an element already fixed. A feasibility check can reject a
  candidate; it cannot select one, and **uniqueness cannot be a property of a program with
  no objective**.
- `joint-tower-sdp-h6-h9.witness.json` emits **no** `y0_star` / `y_star` / `active_set` /
  `duality_gap`. Beyond the AGENTS.md first-class-dual rule, that matters here: the shadow
  prices are exactly the certificate of *which constraints bind* — the information a
  uniqueness argument needs. There is nothing to inspect because there is no optimisation.

## The "closure identifies as 6₂" check is circular

Verified this session: `snappy.Link('6_2').braid_word()` returns **exactly**
`[1,-2,1,1,1,-2]`, and `Link('8_11').braid_word()` **exactly** the registry's 14-letter
word. The registry words **are** SnapPy's stored braid words for the named knots, copied
verbatim — the source comments say so (`# 6_2 in B_3 (SnapPy)`, `# SnapPy canonical`).
Round-tripping them through SnapPy tests nothing physical.

## Census degeneracy — measured

Over `OrientableCuspedCensus`, 212,641 manifolds, targets `B_AME/(ρ·m_e)` with the
conjecture's own ρ = {1, 2, 2}:

| nucleus | named knot | its error | census manifolds **strictly closer** |
|---|---|---|---|
| ²H | 6₂ | 1.090 % | **796** |
| ³H | 8₁₁ | 0.156 % | **1,101** |
| ³He | L6a4 | 2.969 % | **26,671** |

Restricted to the tabulated `LinkExteriors` the producer actually searched (1,184
hyperbolic manifolds):

| nucleus | closer than the named knot |
|---|---|
| ²H | **0** — 6₂ is the unique best match; nothing lands within 1.0 % |
| ³H | **2** — `10_9` (+0.062 %) and `9_11` (+0.128 %) beat 8₁₁ (+0.156 %) |
| ³He | **24** — e.g. `8²_4` at +0.453 % vs L6a4's +2.969 % |

**Two findings:**

1. **All of the deuteron's apparent selectivity comes from the restriction to
   low-crossing tabulated links, not from the volume match.** Drop the restriction and
   796 alternatives do better. Nothing found derives the restriction.
2. **Two of the three assignments fail their own selection rule.** Under "closest
   volume" the argmin is `10_9` for ³H and `8²_4` for ³He. So they are not even the output
   of the procedure that produced them; a further unstated choice intervened.

## Scope-(b): 6₂ cannot be the closure of the canonical deuteron word

**Invariant cited:** the number of components of a braid closure equals the number of
cycles of the underlying permutation in `S_n`. Both `σ_g` and `σ_g⁻¹` project to the
**same** transposition `(g, g+1)`, so resolving a superposition letter `c·σ_g + d·1` into
either branch **cannot change the permutation**. Component count is constant across every
branch and every crossing-sign convention.

Measured two independent ways on `atom_braid_word_3A(1,1)` (23 letters in `H₆(q)`, 18
genuine braid letters, **5** superpositions ⇒ 32 branches):

- permutation alone: 6 strands → **3 cycles**;
- all 32 branch closures in SnapPy: **3 components in 32/32**, all non-hyperbolic.

**6₂ is a knot (1 component); Hopf is 2.** So neither the ²H `canonicalKnotId` (6₂) nor
its `bindingLinkName` (Hopf) can be the closure of the canonical deuteron word. An arity
mismatch fixed by a permutation invariant — not a numerical near-miss.

Independently reproduces [`2026-08-21-deuteron-knot-assignment-adjudication.md`](2026-08-21-deuteron-knot-assignment-adjudication.md)
(re-measured rather than cited, per the sibling-audit-is-not-a-primary-source rule), and
confirms the non-hyperbolicity result of
[`2026-08-25-atom-word-closures-are-not-hyperbolic.md`](2026-08-25-atom-word-closures-are-not-hyperbolic.md)
from a different direction — branch enumeration rather than `deconnect_sum`.

**Scope:** this excludes *the identification of 6₂ with the closure of the canonical mass
word*. It does **not** refute the conjecture, which may intend `K(²H)` as a different
object — the registry carries **both** `knot_name: "6_2"` and `binding_link_name: "L_H
(Hopf)"` as different fields. The registry is not self-contradictory; the consumer layer
that puts them in one slot is.

## The Lean proves structural hygiene, not the identification

`class CanonicalKnotIdSDP (n : LightNucleus)` — a **family**, three instances, no
universal closure.

- **`canonicalKnotId : String`** is a class field of type `String`, supplied per instance
  (`:= "6_2"`). Grepped every `.lean`: **never consumed** — declaration + 7 assignments,
  zero uses in any theorem. Replacing `"6_2"` with `"unknot"` breaks no proof.
- **All three instances carry the same `bindingKWord := [3,3]`** (σ₃², Hopf) while the
  `canonicalKnotId` strings differ. The only field with mathematical content does **not**
  distinguish the three nuclei.
- The four semantic `Prop` fields — including `bindingKMatchesHistoricalMarkovTrace` — are
  all discharged by the same decidable proxy `structurallyValidBinding [3,3] n₀`, i.e.
  *"the word is non-empty and its generator indices lie in [3, n₀)"*. A "Markov-trace
  match" satisfied by an index-range check is the §3b-tax `proof-claims-unencoded` pattern.
- The instance comments state the enumeration outcome outright: *"the 8_11-class
  3-component link is **NOT** min-length-selected at L=3"*, same for L6a4. **The search
  that ran contradicted two of the three names; the strings were kept.**

## Verdict and the one thing worth doing

**Ill-posed as stated**, with a well-posed core that needs a specific build. "The SDP
uniquely selects the canonical knot" describes a program that does not exist. This is not
a refutation — it is a finding that the conjecture **has no supporting evidence stream
independent of the AME data it predicts**.

**Do not attack it as posed.** The single highest-value next step:

> **Derive a complexity bound on `K(²H)` from the substrate — braid index and/or crossing
> number — with no reference to `B_AME`; then ask whether the volume match is unique
> inside that class.**

That is where all the discriminating power sits: **0** better matches inside the tabulated
low-crossing census, **796** without it. The registry already asserts `n_braid: 3`,
`n_0: 6` — **check whether that is derived or also handed over.** If the framework can
independently derive "3 strands, ≤ 6 crossings", then 6₂ being the unique match in that
class is a genuine parameter-free result and +1.09 % becomes quotable. If not, the
assignment carries no information and should be relabelled from `hyp: by-census` to a
plain fit.

Two secondary items, both cheap: the ³H and ³He rows fail their own criterion and want a
bean either way; and the Lean should stop carrying `canonicalKnotId` as an unconsumed
`String` while four `Prop` fields promise PSD-feasibility, minimal length and a
Markov-trace match and deliver an index-range check.

## What is NOT established

**That 6₂ is the wrong knot for the deuteron.** Nothing here shows that. What is shown is
that the *reason given* is a fit, the *bridge* from 6₂ to the canonical mass word is
structurally impossible by arity, and the *volume match* is 797-fold degenerate absent an
underived complexity restriction.
