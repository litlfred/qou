# ²H ATTACK C — three independent lines converge on the braid word

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) ·
**Beans:** `qou-d5e8` (this), `qou-19jc` (the Hecke-element negative), `qou-vbyi`, `qou-5d6k`

Owner ask: *"let's dig in and try and resolve mass and binding issues for ²H first"* +
*"what are attack options?"*

## Result

**The interface scalar is not the defect, and neither is α. All three lines land on the
braid word.** One of the three is a 2026-08-09 audit that got there first; this session
adds two independent confirmations and closes the "maybe it is just the wrong element"
escape.

## Line 1 — no principled Hecke element gives the required deuteron offset (NEW)

Tested `d_req/h = -0.11945345` against a **pre-specified** list of Hecke-admissible
elements `a·σ + b·I` (μ = a·z + b under Markov). Convention D, proton pin, 50 dps. Full
table in `qou-19jc`; the shape of it:

| element | μ | d/h | vs required |
|---|---|---|---|
| `σ` | 0.6126880371 | 0.0 | 4.249 % |
| `σ⁻¹` | 0.4036277384 | −1.0 | 31.323 % |
| `σ²` | 1.128088744 | 2.465 | 91.945 % |
| `P₊` | 0.7527021133 | 0.670 | 28.073 % |
| `P₋` | 0.2472978867 | −1.748 | 57.922 % |
| **`(σ+σ⁻¹)/2` — the DERIVED choice** | 0.5081578877 | −0.5 | **13.537 %** |

**Nothing lands.** And the failure has a specific shape:

- the framework's derived element **is** principled — `σ_avg = σ − (h/2)·1`, the
  flavour-blind colour-average that
  [`inter-nucleon-channel-color-tube.md`](../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)
  argues for on the grounds that *"gluons couple colour, not flavour"* — and it is
  13.5 % wrong in μ, 27 % in B;
- the required value corresponds to **no** element on the list and sits between two.

So it is **not** "the right element has not been found yet". A principled element gives
the wrong number and the right number is not principled. Tuning `d` is fitting with
nothing to point at.

## Line 2 — a flavour-only interface cannot split the channels at all (qou-kj4v, re-verified)

Verified independently at 50 dps. In S-wave, Pauli locks spin to isospin, so a
Pauli-consistent interface carries a projector in **each** SU(2):

```
mu(3S1) = mu+^spin * mu-^iso = 0.18614164195799085217
mu(1S0) = mu-^spin * mu+^iso = 0.18614164195799085217
difference                   = 0.0   EXACTLY
```

because multiplication commutes. **No flavour-only μ splits ³S₁ from ¹S₀, whatever the
functional.** In the SM that split is the tensor force — a spin-*space* coupling. And
`mu+ + mu- = 1` exactly, so projection only removes trace weight ⇒ both channels
necessarily bind; unbinding needs `mu > 1`.

## Line 3 — α is pinned elsewhere, so the multiplier is the free part (2026-08-09, PRIOR)

[`2026-08-09-canonical-chain-walk-gaps-marked.md`](2026-08-09-canonical-chain-walk-gaps-marked.md)
§gap-4 already established this and reached the same destination:

> The binding formula reuses `E₀` with a *different* dimensionless multiplier
> (`ln(tr_free/tr_atom) ≈ 0.929` instead of `0.188`), and nothing validates `E₀` at that
> scale. "One α" is therefore an assumption.

and rules out the escape route:

> The 2026-06-04 handover rules that **a per-channel E₀ is a fit signature** … So
> resolving gap 4 by introducing a separate *nuclear* α would be, by the framework's own
> standard, a fit.

leaving three admissible resolutions, of which its own same-day supersession picks one:

> Route (2) said "the dimensionless multiplier is wrong … which lands on `z_m`". The
> Step 4 correction shows `z_m` **is** derived, so route (2) survives but **relocates:
> the multiplier is wrong because the BRAID WORD is wrong, not because `z` is.**
> … *"Everything that is not the braid word has now been eliminated."*

## What the ²H braid word actually is

Measured this session — `atom_braid_word_3A(1, 1)` is **23 crossings** over 6 strands
(3 quarks × 2 nucleons, generators 0–4). Of those 23, **exactly one** carries the
interface offset: index 2, `d = −0.10445824776972629 = −0.4997·h`. The other 22 are
intra-nucleon quark structure and **cancel in the free/atom ratio**.

**So the entire deuteron binding rides on a single σ-type crossing.** That is the object
all three lines indict, and it is a modelling choice with no derivation in the corpus.

## The functional form has no derivation and a DEAD citation (NEW)

`mass_binding_dashboard.py` cites the binding forms twice (lines 9 and 1116) as
*"Defn: standard-part-functor.md"*. **That block does not define them.** Read in full
(2500 bytes): it defines the standard-part map `st : No_fin → ℝ`, the induced iso
`No_fin/No_inf ≅ ℝ`, and the functor `St` with four properties. It contains no `B_sym`,
no `α`, no binding, no trace-to-energy step. Same defect class as
`prop:hecke-spectral-sequence` — a citation that resolves to a real file which does not
contain the claim.

Corpus-grep for a derivation of `B = −α·ln|tr_M|`, all five paths:

| path | result |
|---|---|
| `docs/audits/` | files that **use** the form; none derives it |
| `content/` | **`notation-collisions.md:112`** — a **notation table** row, i.e. registered as notation; plus a mermaid node in an audit probe and a use in the colour-tube block |
| `computations/` | 5 consumers, no derivation |
| `docs/coordination/` | 3 ledgers, uses only |
| **Lean** | **nothing** — no `logTrace` / `log_trace` / `bindingLog` declaration anywhere |
| appendix `alg:` blocks | the form does not appear |

**So `B = −α·ln|tr_M|` is posited.** Scope **(a)** — it is not derived *in this corpus*;
this does not exclude a derivation existing or being found.

## Attack options, re-ranked by what the convergence implies

1. **The deuteron braid word itself** (cheapest, newly indicated). One crossing carries
   all of it. Ask what fixes the interface crossing count and type from the categorical
   action rather than from convention — the 2026-08-09 audit's own surviving route.
2. **`qou-vbyi` — a space index on the interface.** The only route past Line 2, and the
   principled way to make the word carry L (so ³S₁–³D₁ mixing has somewhere to live).
   Substantial construction.
3. **Derive or retract the functional form.** Independent of ²H and cheap to state
   honestly: either derive `B = −α·ln(tr ratio)` or mark it posited in the dashboard and
   the notation register, and fix the dead `standard-part-functor.md` citation.
4. **~~Tune `d`~~** — closed by Line 1 + `content_keyed_interface_refuted`. Not available.
5. **~~A nuclear-sector α~~** — closed by Line 3 as a fit signature by the framework's own
   standard.

## Scope discipline

Line 1 is scope **(a)**: a negative over a finite pre-specified list (10 entries, not the
algebra) at this q₀ under convention D. A space-indexed construction would supply a **new**
candidate, not one of these — do not cite Line 1 as a structural exclusion. Line 2 is
scope **(b)** with the invariant cited (commutativity of the two projector scalars).
Line 3 is quoted from a prior audit, not re-derived here. The dead-citation and
no-derivation findings are corpus-state facts, each with the grep that establishes them.

**Not claimed:** that the braid word IS wrong — only that it is what remains after the
interface scalar and α are eliminated, and that it carries an undocumented convention
(the hard-coded `['p']*Z + ['n']*N` ordering, worth 3–6 % of `B_sym`; `qou-h7mh`).
