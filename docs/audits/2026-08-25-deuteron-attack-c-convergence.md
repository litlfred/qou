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

> ### Added 2026-08-31 — a SECOND derivation, and it is not KVC-conditional
>
> The "posited" verdict in this section is retracted **by this document itself**,
> in the *RETRACTION + the real gap* section below, which derives the form via
> `Vol_alg(W) := tr_M(W)` → `τ_arch = ln|Vol_alg|` → `vol_through_tau` → evaluate
> at `q₀`. Nothing here disturbs that. This note adds a **second, independent**
> derivation that the retraction does not cite, and draws out what having two
> changes.
>
> [`2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`](2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md)
> **§10a** — *"The functional is DERIVED, not chosen — and it is the log form"* —
> argues from trace multiplicativity over bonds (`tr_atom = tr_free · ∏ μ_k`,
> measured there to 1.2e-31) plus energy extensivity that the trace-to-energy map
> obeys Cauchy's `f(xy) = f(x) + f(y)` on `(ℝ₊, ×)`, so the log form is forced.
> `ursell_alternation_sign_identity_probe.py` cites it as a derivation.
>
> **Why the second route matters.** Gap **(a)** below says every binding number is
> KVC-conditional, and gap **(b)** that the regime KVC licenses (`N → ∞`, `q` a
> root of unity) is not the regime the framework uses (fixed finite braid, real
> `q₀ > 1`). **§10a's route invokes neither the volume conjecture nor any
> asymptotic regime** — only multiplicativity and extensivity, both of which hold
> at fixed finite `n` and real `q`.
>
> So the two gaps do not bite equally: what is KVC-conditional is the
> **identification of `ln|tr_M|` with a hyperbolic volume**, not the **log form
> itself**. Gap (a) as stated — *"every binding number is therefore
> KVC-conditional"* — is too strong for the form, though it stands for the
> volume reading. Gaps (b) and (c) are untouched.
>
> **Now in Lean**, sorry-free, which the *Lean: nothing* row above correctly
> reported was missing:
> `QOU.QBeta.InterfaceScalar.{logForm_extensive, linearForm_extensivity_defect,
> linearForm_not_extensive, linearForm_ceiling}`. The defect of the linear rival
> has a closed form, `−α(1−x)(1−y)` — §10a gives only a measured number, and being
> an identity this holds at every `q` with no anchor. §10a's *uniqueness* step
> (only continuous solutions of Cauchy's equation are `c·ln x`) is classical and
> is **not** formalised, so "forced" still rests on it.
>
> **§10a's own figure is convention-C frame** — it predates the 2026-08-09
> convention-D excision by one day. At the proton pin: C gives **1.487498** (its
> quoted 1.4875, to 1.6e-6), D gives **0.966887**. Conclusion unaffected either
> way; the number needed the scope.
>
> Guard: `computations/probes/binding_functional_extensivity_probe.py` (4/4).


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

---

# Follow-up the same session — the braid-word freedom at A = 2 is now CLOSED

Owner: *"go"*. Continuing into the braid word, which is where the three lines pointed.

## The deuteron is topology-blind, so two of the freedoms are trivially absent

`atom_braid_word_3A` builds a **linear chain**: nucleon `k` occupies strands
`3k … 3k+2`; intra-nucleon crossings sit at generators `3k` and `3k+1`; the bond to
`k+1` is the **single bridge generator `σ_{3k+2}`**, joining nucleon `k`'s last quark to
`k+1`'s first.

| A | chain bonds `A−1` | complete graph `C(A,2)` |
|---|---|---|
| **2** | **1** | **1** ← identical |
| 3 | 2 | 3 |
| 4 | 3 | 6 |
| 7 | 6 | 21 |

**At A = 2 every topology is the same one bond.** So the two live topology positions —
`2026-06-20-chirality-forces-complete-graph-topology.md` ("chirality forces the complete
graph", RMS 6.19 vs the chain's 10.07) and bean `qou-v0yw` ("the graph itself is NOT
derivable; the ad-hoc chain undercounts coordination ~1 bond/nucleon vs data ~3") —
**cannot be adjudicated by the deuteron and cannot fix it either.** The chirality audit's
own table shows every model giving the *same* A = 2 value. Ordering is likewise vacuous
at A = 2: `['p']*Z + ['n']*N` has one arrangement.

## The bridge crossing count: no principled value lands (NEW)

Iterated the actual p-n element `(σ − h·t)` under the Hecke relation `σ² = hσ + 1`, so
`(σ − ht)^m = a_m σ + b_m` and `μ_m = a_m z + b_m`. Pre-specified sweep, convention D,
proton pin, 50 dps. Required `μ = 0.587715064111`.

| m | μ_m | B (MeV) | B_AME/B |
|---|---|---|---|
| **1 (production)** | 0.50822979 | 2.832825 | **0.7853** |
| 2 | 1.0109996 | −0.046131 | — |
| 3 | 0.51392837 | 2.786150 | 0.7984 |
| 4 | 1.0221203 | −0.091923 | — |
| 5 | 0.51969082 | 2.739476 | 0.8120 |
| 6 | 1.0333632 | −0.137716 | — |
| 7 | 0.52551784 | 2.692802 | 0.8261 |

**Two structural facts, neither of them a fit:**

1. **Parity decides bound vs unbound.** Even `m` gives `μ > 1` ⇒ `−ln μ < 0` ⇒ **negative
   binding**. This is `stacked_crossing_gt_one` (`qou-kj4v`) generalised: the convex
   decomposition `μ₊ + μ₋ = 1` is left only by stacking, and stacking to an even power
   overshoots past 1.
2. **Odd `m` creeps the wrong-slow way.** `μ` rises ≈ 0.0058 per step of 2, so reaching
   0.5877 needs **m ≈ 29**. A 29-crossing p–n bond is not a principled number, and tuning
   `m` is precisely what `qou-h7mh` forbids and `content_keyed_interface_refuted` closes.

And the parity handle **cannot** be repurposed to split ³S₁ from ¹S₀: `qou-kj4v` records
that the naive braid-topology argument **runs backwards** — identical nucleons ⇒ `π₁ = B_n`
so `σ` already closes, distinguishable ⇒ `P_n` so only `σ²` closes, predicting `σ²` for pn
and `σ` for pp/nn, i.e. **binding pp and unbinding the deuteron.**

## Where ²H stands: every braid-word freedom is eliminated

| candidate | status at A = 2 | established by |
|---|---|---|
| interface **element** | ✗ no principled element lands (closest 4.25 %, derived one 13.5 % off) | Line 1, this session |
| bridge **crossing count** | ✗ no small integer lands; even ⇒ unbound; odd needs m ≈ 29 | this section, new |
| **topology** (chain vs complete) | ✗ vacuous — one bond either way | this section, new |
| nucleon **ordering** | ✗ vacuous — one arrangement | this section, new |
| crossing **multiplicity** tuning | ✗ forbidden (content-keyed) | `qou-kj4v`, `qou-h7mh` |
| **α** | ✗ pinned by β-decay; per-channel α is a fit signature | 2026-08-09 audit |
| any **flavour-only μ** | ✗ `μ(³S₁) = μ(¹S₀)` exactly | Line 2 |

**Two things remain, and only two:**

1. **The functional form `B = −α·ln|tr_M|` — posited.** Five-path corpus-grep finds no
   derivation, **nothing in Lean**, and the only statement in `content/` is a row in a
   **notation table**; the dashboard's cited definition (`standard-part-functor.md`) does
   not contain it. Cheapest honest action in the whole ²H thread: derive it or mark it
   posited.
2. **A space index on the interface** (`qou-vbyi`) — the only route past the exact
   flavour-only degeneracy, and the only way ³S₁–³D₁ tensor mixing gets somewhere to live.

## What this is and is not

**Not a resolution of the deuteron.** It is an elimination: the 27 % over-bind is *not*
attributable to any remaining freedom in the braid word at A = 2, so the defect is in the
functional form or outside the word entirely.

**Scope.** The crossing-count result is scope **(a)** — a negative over `m = 1…7` plus a
linear extrapolation, at this q₀ under convention D; it does not exclude some large or
non-integer structure, it says no *principled small* one works. The topology-vacuity and
ordering-vacuity results are **combinatorial facts about A = 2**, not claims about A ≥ 3,
where the chain-vs-complete-graph question is live and contested. The parity fact is
structural (`μ₊ + μ₋ = 1`), the backwards-assignment is quoted from `qou-kj4v`.

---

# RETRACTION + the real gap — `B = −α·ln|tr_M|` IS derived, conditionally

Owner: *"Derive or retract the functional form."* The answer is **derive** — and that
means **retracting my own "posited" finding from earlier in this same document.**

## Retraction

Above I wrote that `B = −α·ln|tr_M|` is *"posited"*, on the strength of a five-path grep
that found no derivation, nothing in Lean, and only a notation-table row. **That grep was
looking for the wrong string.** The derivation exists; it is spelled in terms of `Vol`,
not in terms of `B_sym`, so a grep keyed on the binding symbol could not see it. Same
class of error as the arity conflation AGENTS.md warns about: I searched the topic and
not the claim.

## The chain, and it is complete

| step | statement | where |
|---|---|---|
| 1 | `Vol_alg(W) := tr_M(W)` — the **algebraic quantum volume IS the Markov trace** | [`algebraic-quantum-volume.md:6`](../content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.md) (a **definition**) |
| 2 | `τ_arch` *"projects categorical data into physical spacetime by **taking the absolute logarithm of the algebraic quantum volume**"* | [`archimedean-functor-uniqueness-context.md:45`](../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness-context.md) |
| 3 | `Vol(K_β) = τ_arch(Vol_q(β))`, *"there is no other archimedean route"* | [`vol-through-tau.md`](../content/quantum-observable-universe/mass-theory/vol-through-tau.md) — **Proposition conditional on `conj:kashaev-volume-conjecture`**, Lean `vol_through_tau_of_volumeConjecture` |
| 4 | *"Evaluate at `q = q₀` and take `ln|·|`"* | [`mass-table-z1-20.md:15`](../content/quantum-observable-universe/mass-theory/mass-table-z1-20.md) |

Compose 1–4: `Vol(K) = ln|tr_M(K)|`, so `−α·ln|tr_M|` is `−α·Vol`. **The form is
derived.** My "posited" verdict is withdrawn.

## But three things are wrong with it, and one is new and exact

### (a) It is conditional-proved, not established
Step 3 is *conditional on* `conj:kashaev-volume-conjecture`, which the corpus's own block
says is **"open in general (proved only for specific families: the figure-eight knot,
certain torus and pretzel knots)"**. Per AGENTS.md §"conditional-proved ≠
premise-established", every binding number is therefore **KVC-conditional** and should be
stated that way. The dashboard tags `B_sym` `DERIVED` with no conditionality marker.

### (b) The regime the conjecture licenses is not the regime the framework uses
KVC as the corpus states it ([`kashaev-volume-conjecture.md:8-18`](../content/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.md)):

$$\mathrm{Vol}_{\mathrm{hyp}}(S^3\setminus K) \;=\; 2\pi \lim_{N\to\infty} \frac{\log\lvert J_N(K)\rvert}{N}, \qquad J_N(K)\big\vert_{q=\exp(2\pi i/N)}$$

Three ingredients, none of which the framework supplies:

| KVC needs | framework has |
|---|---|
| `N → ∞` | a **fixed finite** braid, `n = 3A` strands |
| `q = exp(2πi/N)` — a **root of unity**, `\|q\| = 1` | `q₀ ≈ 1.10998` — **real and > 1** |
| prefactor `2π/N` | `α = E₀` |

And the real-`q₀` choice is not incidental — AGENTS.md's own §"Im(q) at fibre vs
observable level" records `Im(q₀) = 0` as an **archimedean requirement** for real masses.
So the framework evaluates precisely where the conjecture's asymptotics do not apply.
`vol-through-tau.md` bridges this by *asserting* that the realization functor's
computation rule "evaluates `τ_arch` … as exactly the Kashaev limit" — the regime bridge
is **inside the identification**, not derived from it.

### (c) The prefactor discrepancy — MEASURED AND EXACT, but I OVER-CLAIMED ITS SIGNIFICANCE

> **🛑 SELF-CORRECTION, same session.** I recorded this as *"the single most concrete
> unresolved item this session found on the binding leg."* **That was wrong, and the
> arithmetic below is not what deflates it — the provenance of one side does.**
>
> `m_e/ℏ_q²` is the prefactor of `m = m_e·Vol·ρ/ℏ_q²`, and **that shape is DEPRECATED for
> absolute mass.** Its own runtime warning says so verbatim:
>
> > *"`per_knot_density_borromean` is the **λ_A fit** (Vol(𝓑₃)·ρ_global/ℏ_q² → 966 MeV) —
> > **NOT the canonical absolute nucleon mass**. Use the `canonical_mass` facade."*
>
> That is the λ_A route AGENTS.md excised under the 2026-06-24 owner ruling (m_p ≈ 966,
> +2.96 %, a CODATA-implied fit). **The live mass route in the dashboard is the
> muon-anchored Hecke energy via `canonical_mass`, which does not use `vol_density` at
> all** — verified by reading the call site.
>
> So there are **not two live prefactors in conflict**. There is one live prefactor
> (`E₀`) and one belonging to an excised formula shape. And for *binding* the point is
> weaker still: AGENTS.md keeps `vol_density_per_block` valid **"for binding ratios only
> (scale cancels)"** — in a ratio the prefactor cancels outright.
>
> **What survives, unchanged:** the measurement itself (exact to 1e-49, `q₀³/(q₀−1)`),
> and the 2026-08-09 gap-4 finding it was reached from — *"the binding formula reuses
> `E₀` with a different dimensionless multiplier … and nothing validates `E₀` at that
> scale."* That gap is about `E₀`'s own justification and stands on its own; it does not
> depend on the deprecated shape. **What does not survive is my framing of this as a live
> two-prefactor contradiction.**

### The measurement, retained


The framework's mass shape is `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²` (AGENTS.md, the standing
purge banner). A binding is a difference of masses, so with a common `ρ` its prefactor
should be `m_e·ρ/ℏ_q²`. Measured at 50 dps, proton pin:

```
alpha = E0 = m_e/(q0*(q0-1))       =  4.18598136329 MeV   <- what every B_ form uses
mass-formula prefactor m_e/hbar_q^2 = 52.0514663819 MeV   <- what m = m_e*Vol*rho/hbar_q^2 implies

ratio                               = 12.4347104931
closed form q0^3/(q0-1)             = 12.4347104931
difference                          = -1.28e-49      (exact)
```

**The two prefactors differ by exactly `q₀³/(q₀−1) = 12.4347104931`.** Reconciling them
would require `ρ = (q₀−1)/q₀³ ≈ 0.0804` for every nucleus. **I am not claiming that is
`ρ`** — asserting it because it closes the gap is the CAL-4 antipattern. I am recording
that the binding forms and the mass formula use prefactors that differ by an exact,
q₀-only factor, and that nothing in the corpus reconciles them.

This is the quantitative content of the 2026-08-09 audit's gap 4 — *"the binding formula
reuses `E₀` with a different dimensionless multiplier … and nothing validates `E₀` at
that scale"* — reached from the opposite direction. That audit found α unvalidated; this
finds **what it is off by, exactly, and against what**.

## Consequences

1. **Do not call the binding forms "posited"** — that was my error. Call them
   **KVC-conditional**.
2. **Do tag them conditional.** `B_sym` / `B_qCLT_fac` are `DERIVED` in the dashboard's
   provenance table with no marker; they should carry one, as `E_C` now does for its own
   open `sorry`.
3. **The prefactor discrepancy is a live, exact, unexplained factor of 12.4347104931**
   between two forms the framework uses side by side. It is the single most concrete
   unresolved item this session found on the binding leg — `qou-2pnv`.
4. **The dead `standard-part-functor.md` citation stands as a defect** independently of
   all this: the dashboard cites it for the form definitions and it does not contain
   them. The right citation is `algebraic-quantum-volume.md` + `vol-through-tau.md`.

## Scope
(a)/(b) are readings of blocks quoted verbatim. (c) is a measurement, exact to 1e-49, and
is a statement that **two prefactors differ**, not a claim about which is right. Nothing
here is a refutation of the binding forms: a KVC-conditional derivation is a legitimate
object, and the framework is entitled to it — provided it says so.
