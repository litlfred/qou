# The ladder's phase term has no derivation to re-derive

**Bean:** `qou-cds1` (S1 — re-derive the Q_β `c_k` ladder under convention D).
**Probe:** [`computations/qbeta/qbeta_ladder_alpha_provenance_probe.py`](../../computations/qbeta/qbeta_ladder_alpha_provenance_probe.py) (5/5).
**Witness:** `computations/qbeta/qbeta-ladder-alpha-provenance.witness.json`.
**Scope: (a) throughout** — see the scope section at the end.

## The question nobody had asked

The prior arc worked *inside* the form. Given the ladder factor
`cos(α − u/2)` with `α = (z−1)h/2`, which `z` satisfies both the value and the
slope constraint? That search is exhausted — the two-row filter
([`qbeta_ladder_alpha_form_filter_probe.py`](../../computations/qbeta/qbeta_ladder_alpha_form_filter_probe.py),
[`2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md`](2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md))
found no admissible candidate, and its own scope note says the form "must
change".

The prior question is: **what derives the form?** The corpus answers with one
citation. [`q-beta-categorical-precision-ladder.md`](../../content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md)
says:

> `α = (z−1)h/2` is the single-wrap eigenphase on $V_{(2,1)}$
> (per [`prop:q-beta-spectral-bridge`](../../content/quantum-observable-universe/nuclear-interactions/q-beta-spectral-bridge.md))

So: read the source, and measure whether it supports the use.

## What the source actually says

**It names no eigenphase.** Across the proposition's `.md`, its `.lean`, and
its proof block, the strings `eigenphase`, `V_{(2,1)}`, `V_{2,1}`, `(2,1)` and
even `phase` occur **zero** times. The attribution names three things — an
eigenphase, a representation, and a phase role — and its cited source contains
none of them.

**What it does produce is a ratio coefficient.** The bridge relates two
presentations of the same observable, Form A (NF counit) and Form B
(transfer-matrix log-ratio):

```
Q_A / Q_B  =  (1 − h/2)/(1 − zh/2)  =  1 + (z−1)h/2 + O(h²)
```

`(z−1)h/2` is the **first-order term of a multiplicative ratio**. Verified
symbolically: the remainder is exactly `z(z−1)h²/4 / (1 − zh/2)`, which is the
source's own Lean theorem `bridge_first_order_remainder`.

The ladder then uses that same expression as an **angle**, inside a cosine. A
first-order ratio coefficient and an angle are different objects, and `1 + x`
and `cos(x − δ/2)` are different functions of `x`.

## Measured, the two roles are far apart

At the substrate anchor (`q₀ = 1.1099785827513808…`, proton pin, 50 dps):

| | convention C | convention D |
|---|---|---|
| `α = (z−1)h/2` | −0.0523361203 | −0.0404857773 |
| ladder factor `cos(α − u/2)` | 0.998398945 | 0.998999137 |
| the source's own factor `1 + α` | 0.947663880 | 0.959514223 |
| **relative difference** | **5.354 %** | **4.115 %** |

A 4–5 % gap, in a ladder whose later rungs are chasing ppb.

**And no small correction reconciles them.** The `δ` solving
`cos(α − δ) = 1 + α` is **−0.377** (C) / **−0.326** (D), against the ladder's
actual `u/2 = 0.004259` — off by **88.6×** / **76.6×**, and opposite in sign.

This closes the charitable reading. One could argue the bridge is cited only
for α's *value*, not for its role; but the same real number playing two
structurally different roles is not a derivation, and the δ table shows the two
roles are not bridged by any small correction either.

Three further weaknesses of the citation, for completeness: the proposition is
**conditional on the Borromean quark conjecture**; its Lean's two proved
theorems are free-variable `ring` / `field_simp` identities that hold for *any*
`h, z` and so say nothing about any convention; and its substantive analytic
step (`log(1+x)` to its Taylor truncation) is recorded as an open lemma.

## Incidental: a live doc-vs-body divergence

In [`q-beta-spectral-bridge.lean`](../../content/quantum-observable-universe/nuclear-interactions/q-beta-spectral-bridge.lean),
`markovZ` has body `q^3/(q^2+1)` — convention **D**, migrated 2026-08-26
(`2af189af1a`, `qou-cxjq`) — while its own docstring says
`z(q) = 1/(√q + 1/√q)` and the `.md` proposition *defines* z as C. The body
moved; the prose did not. It changes nothing about the proved theorems, since
both quantify over a free `z`, but it is the load-bearing definition and it
currently disagrees with itself.

## What this means for `qou-cds1`

**"Re-derive under D" cannot mean "recompute α at `z_D`."** α's provenance does
not survive inspection in *either* convention, so there is no C-frame phase
awaiting a D-frame twin. The D work has to **supply** a phase, not convert one.

It also explains the two-row filter's empty result rather than leaving it as a
brute fact: that search was looking for a `z` inside a form that has no
derivation behind it. A form chosen without a derivation has no reason to admit
a `z` that satisfies two independent constraints.

The standing position of this arc — recorded in
[`2026-08-31-cds1-block-bar-defect-and-conjugation.md`](2026-08-31-cds1-block-bar-defect-and-conjugation.md)
§Scope — is already that "α is **not** derived". This audit does not re-declare
that; it identifies the *mechanism*, which was not previously recorded: the
cited source derives a different object.

## Scope

**(a)**, per AGENTS.md §"Before declaring refuted". This is a statement about
whether the **cited attribution** supports the ladder's phase term, measured.
It is **not** a claim that no phase term is derivable, **not** a claim that the
bridge proposition is wrong (it is a bridge between two forms, and as such
untouched here), and **not** a statement about the ladder's numerical
performance. No invariant is offered that would forbid a phase term, so nothing
here is a structural exclusion.

## Which routes to "supply a phase" are already closed

Added after the fact. The section above says the D work must *supply* a phase
and stops there, which invites the reader to reach for the obvious candidate —
an eigenphase of a braid word on `V_(2,1)`, since the machinery is right there
and `hoefsmitB` already lives in that representation. **That candidate is
excluded**, scope-(b), with the invariant named, and a reader sent down it
would waste the pass. The closures, so the next agent inherits them:

- **No braid word on `V_(2,1)` supplies the phase** —
  [`qbeta_eigenphase_seminormal_exclusion_probe.py`](../../computations/qbeta/qbeta_eigenphase_seminormal_exclusion_probe.py)
  (bean `qou-pdix`). Every character of that representation lies in
  `ℤ[q, q⁻¹]` (`b` enters traces only through the rational `b·c`, so the square
  root never survives; verified on every word of length 2, 4, 6 — 17 traces, 0
  exceptions), while `2cos((z−1)h/2)` is not Laurent. Scalar normalisation does
  not rescue it: `det ρ(w) = (−1)^L` forces `L` even and `λ = ±1`, leaving the
  trace Laurent either way.
- **No braid-image transfer matrix carries it in *any* convention** —
  [`qbeta_braid_image_eigenphase_exclusion_probe.py`](../../computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py)
  gives an elementary boundedness argument that never reads `z`'s formula,
  replacing an earlier *unproved* transcendence assertion.

  **What closes branch 1 in full is neither of those, and the distinction is
  live** — `316c1dcc42` on main corrects three sites that named the
  transcendence route, and an earlier draft of this section made the adjacent
  misreading by writing that the result was "extended from Laurent to
  algebraic", as though algebraicity were what does the work. It is not.
  Branch 1 is closed — character case *and* eigenvalue-pair case — by
  **zero-counting**: `QOU.QBeta.BraidImageEigenphaseAlgebraic.coeffs_zero_of_surjective_nonpos`
  (sorry-free), "a polynomial with infinitely many roots is zero". Its
  load-bearing hypothesis must be carried with it:
  `hsurj : ∀ y ≤ 0, ∃ s ≥ 1, α s = y` — **surjectivity onto the non-positive
  reals**, which the unbounded `(z−1)h/2` family supplies and a bounded
  `arccos` does not. *"It is algebraic, therefore excluded"* is not what the
  theorem says. Companion probe:
  [`qbeta_eigenphase_algebraic_exclusion_probe.py`](../../computations/qbeta/qbeta_eigenphase_algebraic_exclusion_probe.py),
  whose own header states plainly that boundedness is the wrong invariant to
  push.
- **The Lean carrier is proved vacuous** —
  `QOU.QBeta.EigenphaseCarrier.carrier_is_trivial`. So the identification was
  never carried in Lean either, which is consistent with, and independent of,
  the citation defect measured above.
- **The convention-parameter class is pruned for D** —
  `qbeta_ladder_required_phase_probe.py`: the required phase sits in a window of
  half-width ≈ 1.09e-5 rad and `z_D` misses by ≈ 1.19e-2 rad, ~1000× the window.
- **The tail does not need re-deriving.**
  `QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common` (sorry-free): `z`
  reaches the ladder at exactly one place, the N=1 phase, so `c₂ … c₅` are
  phase-blind.

That last point is worth stating plainly, because it shrinks S1: **the D-frame
work is the phase and only the phase.**

What those exclusions explicitly leave open — quoting the seminormal probe's own
scope — is an `M_β` built from a **non-scalar** normalisation (divided by a
`q`-dependent, non-rational Markov-trace factor), or an `M_β` **outside the
braid image** (a general element of `H₃(q)`, or an operator on a larger space
restricted to `V_(2,1)`). Those are where a supplied phase could still come
from, and they are not excluded by anything above.

This does not change the finding of this audit — the attribution defect and the
4–5 % / 88× measurements stand independently — but it changes what the finding
should send someone to do next.

## The KZ / Kohno–Drinfeld route is closed too — and it meets this probe's own number

Checked after the section above named it as the route to look at first.
`9a8b09c661` on main (2026-09-04) corrects an earlier claim that branch 3 of the
eigenphase trichotomy was open: `QOU/QBeta/HolonomySpectrumSignObstruction.lean`
(landed 2026-08-31, `4471ee72ce`, 6 theorems, sorry-free) **excludes every
holonomy whose generator has real spectrum**, Kohno–Drinfeld included.

The argument is residue-independent, which is why it reaches the whole class
rather than one candidate: a real generator eigenvalue `a` gives character
`(eᵃ + e⁻ᵃ)/2 = cosh a ≥ 1` for every real `a`, so a `q`-dependent residue only
changes which `a` occurs. The required correction factor is **0.998399** — below
1, hence unreachable. The whole obstruction is `(x−1)² ≥ 0`; no analysis, no
transcendence.

**That 0.998399 is the number this probe computes independently.** Assertion 3
above reports `cos(α − u/2) = 0.9983989452530845` at convention C. And the
surviving condition's angle, `θ = 0.0565947`, is exactly `|α − u/2|` here
(`−0.052336120 − 0.004258617`). The two results are the same object approached
from opposite directions — one asking what the ladder's factor *is*, the other
asking what could *produce* it — which is a useful cross-check on both.

So the three routes left open by the seminormal exclusion now stand as:

| route | status |
|---|---|
| non-scalar normalisation (divided by a `q`-dependent non-rational Markov-trace factor) | **open** |
| `M_β` outside the braid image | **open in general**; the holonomy sub-case is closed for real spectrum |
| KZ / Kohno–Drinfeld holonomy | **closed** — real spectrum, `cosh a ≥ 1 > 0.998399` |

And the surviving condition is stated sharply rather than as "find a
connection": find one whose generator is **elliptic** at real `q` — `det A > 0`,
spectrum `±iθ` with `θ = 0.0565947`. **The imaginarity has to be sourced.** The
corpus names `conj:im-q-physical-role` for that, and it is Tier-0 condition D0
on beans `qou-pdix` / `qou-cds1`.

Worth noting where that lands: AGENTS.md's Im(q) banner separates the
**observable** level (`Im(q₀) = 0`, verified) from the **fibre** level (`Im(q)`
unconstrained). An elliptic generator at real `q₀` needs its imaginary part from
somewhere, and the fibre level is the only place the framework leaves for it.
That is a pointer to where the question lives, not a result — nothing here
derives such a generator or shows one exists.
