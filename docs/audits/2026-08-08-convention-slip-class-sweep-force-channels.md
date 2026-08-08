# Convention-slip defect class: sweep of the force / interaction channels

Branch `claude/convention-slip-class-sweep-2026-08-08`. 2026-08-08. Item 3a of
the trace-convention follow-up. No production value changed.

## Headline

> The class is **present, and it is not confined to traces.** Three confirmed
> instances in the EM and strong crossing-energy channels, all sharing one root
> cause: **the sign on the negative-crossing weight is dropped**, and a
> **balanced-variable (`q^{1/2}`) relation is transplanted into the unbalanced-`q`
> Hecke presentation** — the same `q^{1/2}` boundary where the seed defect lived.
> The weak channel and the colour channel come back **clean**, and the colour
> channel is clean *for a reason worth copying*: it names its normalisation's
> provenance, states its consistency check as falsifiable, and declines to wire.

The most reusable output is not the defect list. It is that **two of the three
diagnostic questions are mechanizable with no reference implementation to compare
against**, and are now implemented and running:
[`convention_slip_validate.py`](../coordination/convention_slip_validate.py).

## 1. The defect class, stated generally

> A **named constant stipulated inside a definition, inconsistent with the object
> the definition names**, propagating silently because nothing cross-checked the
> name against the value.

Three properties make it survive review, all present in the seed instance
([`markov-axioms-primitive.md:5`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md)
stipulating `z = 1/(q^{1/2}+q^{-1/2})` while naming the *Jones*–Markov trace):

1. **The value looks canonical.** `1/(q^{1/2}+q^{-1/2})` is exactly `1/δ`, the
   Temperley–Lieb loop reciprocal — a real object, just the wrong one for the
   Hecke generator `σ_n` it was applied to.
2. **The name and the value are never compared.** Nothing in the pipeline reads
   "Jones" and asks what `z` Jones requires (`q³/(q²+1)`).
3. **Production independently implements the *named* object**, so the numbers
   look fine and the stipulation is never exercised.

To that seed list this sweep adds a fourth, which is what actually let the EM
instances through:

4. **The wrong formula is correct on the one case that gets spot-checked.**
   `coulomb-charge.md`'s decomposition is exact for positive braids (`m = 0`).
   Every quoted numerical check in the corpus — the `tanh(ln q) ≈ 0.104`
   ratio — is a positive-braid check. The formula is wrong only where nobody
   looked.

The three diagnostic questions, and how mechanizable each is:

| Q | Question | Mechanizable? |
|---|---|---|
| 1 | Does the definition **name** an object whose standard value differs from the constant it stipulates? | **No** (needs an external notion of "standard"; this is the agent's judgement call) |
| 2 | Is there an **integrality / consistency invariant** the stipulated constant implies, and is it satisfied? | **Yes — fully.** Two independent forms, both implemented (R1, R3 below) |
| 3 | Do the **doc and the code** agree, and does any *third* place assert something incompatible? | **Partly.** The trace registry does this for traces; R2 below does the doc-vs-*algebra* case, which needs no code to compare against |

## 2. Verdict table

| # | Surface | Channel | Verdict | Evidence |
|---|---|---|---|---|
| 1 | [`coulomb-charge.md:9-15`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md) strong/Coulomb decomposition | **EM** | **confirmed-defect** | Reconstructs `pq + mq⁻¹`, not `pq − mq⁻¹`. Lean-refuted. §3 |
| 2 | [`q-energy-terms-and-limits.md:29,35`](../../content/quantum-observable-universe/climax-volume-mass/q-energy-terms-and-limits.md) `𝔈_×` | **strong** | **confirmed-defect** | Three incompatible values for one symbol, six lines apart; negative weight given as `+q⁻¹` against the chapter's own `def:crossing-energy`. §4 |
| 3 | [`feynman-eigenbasis.md:29`](../../content/quantum-observable-universe/braids-and-knots/feynman-eigenbasis.md) skein-as-characteristic-equation | **strong/EM** | **confirmed-defect** | Nonzero residual in a Hecke-satisfying rep; `qσ − q⁻¹σ⁻¹ = h(σ + q⁻¹)` is not scalar. §5 |
| 4 | [`crossing-energy.md:17-20`](../../content/quantum-observable-universe/climax-volume-mass/crossing-energy.md) cites balanced skein as its sign warrant | **strong/EM** | **needs-work** | Coherent *with* Form B, but Form B is a link-invariant relation, not a per-crossing rule. §5.2 |
| 5 | [`nitrogen-14-threading.md:13`](../../content/quantum-observable-universe/observations/nitrogen-14-threading.md) mixed-crossing weight | **strong** | **needs-work** | Same dropped sign; needs an eigenvalue-vs-energy-weight disambiguation I did not settle. §4.2 |
| 6 | `b = sqrt((q⁴+q²+1)/(q²+1)²)` ladder coupling | **weak** | **clean** | Not stipulated at all — *forced*, uniquely, by Hecke + braid. §6 |
| 7 | `Q_twist = T(t)/3` colour-tube charge quantum | **colour** | **clean** | Cites provenance, states a falsifiable consistency check, declines to wire. §7 |
| 8 | [`skein-mass-relation.lean`](../../content/quantum-observable-universe/observations/skein-mass-relation.lean) | strong | **clean** | Carries Form B as an *assumed* structure field, not a proved claim. §5.3 |
| 9 | Confinement SDP weights | **strong** | **clean (n/a)** | Solver outputs, not stipulated constants — no surface for this class |
| 10 | `α_EM = [2]_q·(1 − h²α)` | **EM** | **not reached** | Beaned. §9 |
| 11 | Gravity / information channels | — | **not reached** | Beaned. §9 |

Corpus-grep prior state: 20 audit docs mention "coulomb"; **none** names the
`coulomb-charge` ↔ `crossing-energy-decomposition` pair, and none names the
two-skein-form split. No prior agent flagged items 1–5.

## 3. Confirmed defect 1 — the EM/Coulomb decomposition (EM channel)

`def:crossing-energy`
([`crossing-energy.md:5-13`](../../content/quantum-observable-universe/climax-volume-mass/crossing-energy.md))
assigns `+q` to a positive crossing and `−q⁻¹` to a negative one, so for `p`
positive and `m` negative crossings

```
  𝔈_cross = p·q − m·q⁻¹ .
```

With `q = cosh λ + sinh λ` and `q⁻¹ = cosh λ − sinh λ` (`λ = ln q`):

```
  p·q − m·q⁻¹ = (p − m)·cosh λ  +  (p + m)·sinh λ .
```

**`(p − m)` on the `cosh` channel, `(p + m)` on the `sinh` channel.** The `sinh`
part is sign-blind: a negative crossing contributes `−cosh λ + sinh λ`, so its
`sinh` term *adds*.

- [`crossing-energy-decomposition.md:20-24`](../../content/quantum-observable-universe/observations/crossing-energy-decomposition.md)
  states exactly this: `E_sym = (p−m)cosh`, `E_asym = (p+m)sinh`. **Correct.**
- [`coulomb-charge.md:9-15`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md)
  states, with `Q = ½(n₊ − n₋)`:

  ```
    𝔈_cross = ½(n₊ + n₋)(q + q⁻¹)  +  Q·(q − q⁻¹)
              └── "baseline (strong)" ──┘   └ "Coulomb correction" ┘
  ```

  Expanding: `½(p+m)(q+q⁻¹) + ½(p−m)(q−q⁻¹) = ½[2pq + 2mq⁻¹] = p·q + m·q⁻¹`.

**The multiplicities are swapped between the two channels, which flips the sign
on every negative crossing.** The stated decomposition does not reconstruct the
object it decomposes.

Exact-rational check at the experimental pin `q₀ = 1.1099785827513808`:

| `(p,m)` | truth `pq − mq⁻¹` | `coulomb-charge.md` | `crossing-energy-decomposition.md` |
|---|---|---|---|
| (3,0) | +3.329936 | +3.329936 ✓ | +3.329936 ✓ |
| (2,1) | +1.319039 | **+3.120875 ✗** | +1.319039 ✓ |
| (1,2) | −0.691858 | **+2.911815 ✗** | −0.691858 ✓ |
| (3,3) | +0.627181 | **+6.032691 ✗ (9.6×)** | +0.627181 ✓ |
| (4,2) | +2.638078 | **+6.241751 ✗** | +2.638078 ✓ |

Agrees **iff `m = 0`** — property 4 of the class, exactly.

### 3.1 It is Lean-refuted, sorry-free

[`crossing-energy-decomposition.lean`](../../content/quantum-observable-universe/observations/crossing-energy-decomposition.lean)
machine-checks the opposite assignment:

| Declaration | Content |
|---|---|
| `symChannel p m q` | `(p − m) * symmetricWeight q` — docstring: *"The multiplicity is `p - m`"* |
| `asymChannel p m q` | `(p + m) * antisymmetricWeight q` — docstring: *"the `sinh` part is sign-blind"* |
| `crossingEnergy_split` | proves `p·q − m·q⁻¹ = symChannel + asymChannel` (by `ring`) |
| `ratio_general` | proves `asym/sym = ((p+m)/(p−m))·tanh(ln q)` |
| `ratio_two_one_ne_tanh` | proves the `(2,1)` ratio is **`3·tanh(ln q)`**, labelled *"Concrete witness that `ratio_general` is not vacuous"* |

The two docs' own ratio claims are **reciprocal**: `coulomb-charge.md:24` implies
`((p−m)/(p+m))·tanh(ln q)`; the Lean proves `((p+m)/(p−m))·tanh(ln q)`. At
`(2,1)` that is 0.03465 against 0.31189 — **off by 9×**. Both reduce to
`tanh(ln q) ≈ 0.104` at `m = 0`, which is the only value either doc quotes.

An independent third place lands on the Lean's side:
[`mass-energy-pair-creation.md:12`](../../content/quantum-observable-universe/information-theory/mass-energy-pair-creation.md)
gives the `e⁻e⁺` pair sum as `3(q − q⁻¹) ≈ 0.630`; Lean `pair_cancellation`
gives `(p+m)(q−q⁻¹)`, which for the trefoil `(3,0)` is `3(q−q⁻¹) = 0.62718`. So
the canonical convention is the Lean's, and `coulomb-charge.md` is the lone
outlier.

### 3.2 Propagation

Five further blocks carry the defective assignment:

- [`crossing-energy-intro.md:5`](../../content/quantum-observable-universe/climax-volume-mass/crossing-energy-intro.md) — restates `𝔈_cross = strong baseline + Q·(q − q⁻¹)`
- [`skein-crossing-asymmetry.md:23`](../../content/quantum-observable-universe/climax-volume-mass/skein-crossing-asymmetry.md)
- [`torus-hopf-stability-proof.md:4`](../../content/quantum-observable-universe/predicted-spectra/torus-hopf-stability-proof.md) — uses `½(n₊+n₋)(q+q⁻¹)` as the strong term
- [`stable-nucleus-valley.md:4`](../../content/quantum-observable-universe/predicted-spectra/stable-nucleus-valley.md) — **a downstream physics claim**: the stable `(Z,N)` valley is said to be selected by the balance of these two terms
- [`strangelet-crossing-energy-proof.md:1`](../../content/quantum-observable-universe/observations/strangelet-crossing-energy-proof.md)

**Not asserted here:** whether any *production compute* implements the defective
form. I did not find one, but I did not exhaustively sweep `computations/`, and
absence of a grep hit is not absence. The `stable-nucleus-valley` claim is the
one to check first, and it is beaned.

### 3.3 What is *not* wrong

`Q = ½(n₊ − n₋)` — the Coulomb **charge** itself (`coulomb-charge.md:1-7`) and
its Lean sibling `CoulombCharge.value` — is fine, as are the neutrality and
antisymmetry theorems. The defect is confined to the **decomposition** in the
same block. This matters downstream: `strand-twist-datum.md` (§7) pins its
falsification test to `Q`, i.e. to the *good* half, and is therefore
**unaffected**.

## 4. Confirmed defect 2 — `𝔈_×` carries three values (strong channel)

[`q-energy-terms-and-limits.md`](../../content/quantum-observable-universe/climax-volume-mass/q-energy-terms-and-limits.md),
six lines apart, for the same symbol:

- `:29` — *"Each crossing in the braid word contributes energy `𝔈_×(q) = ½(q − q⁻¹) = 0.1045`"*
- `:35` — *"For a positive crossing: `𝔈_×^{(+)} = q`. For a negative crossing: `𝔈_×^{(−)} = q⁻¹`."*

`½(q−q⁻¹) = 0.10453` against `q = 1.10998` against `q⁻¹ = 0.90092`. And `:35`
gives the negative weight as **`+q⁻¹`**, while the canonical `def:crossing-energy`
— **in the same chapter** — assigns **`−q⁻¹`**.

The same `½(q−q⁻¹)` per-crossing normalisation also appears in
[`knot-particle-dictionary.md:24`](../../content/quantum-observable-universe/knots-particles-confinement/knot-particle-dictionary.md),
[`binding-knots-visual-inventory.md:7,42`](../../content/quantum-observable-universe/knots-particles-confinement/binding-knots-visual-inventory.md)
and
[`trace-ratio-interpretation.md:26`](../../content/quantum-observable-universe/observations/trace-ratio-interpretation.md)
(where it feeds `v = N_v·𝔈_×·μ₀`, the weak scale). Under the Lean, `½(q−q⁻¹)` is
exactly `antisymmetricWeight` — the **Coulomb** channel's per-crossing weight,
sign-blind. Using it as *the* per-crossing energy silently drops the `cosh`
(strong) channel entirely.

**Scope: (a), scope-limited.** I am asserting an *internal inconsistency* — the
three values cannot all be `𝔈_×` — not that any particular one of them is the
wrong physics. Which is canonical is a question for the author; the dropped
sign at `:35` is unambiguous.

### 4.2 The related `needs-work`

[`nitrogen-14-threading.md:13`](../../content/quantum-observable-universe/observations/nitrogen-14-threading.md)
calls the negative crossing's weight `q⁻¹ = 0.901` (positive) and says the mixed
crossing *"does not incur the Coulomb penalty `(q − q⁻¹)/2 ≈ 0.105`"* — but the
average of `+q` and `−q⁻¹` **is** exactly `0.105`. Same dropped sign. I am
holding this at `needs-work` rather than `confirmed-defect` because resolving it
requires disambiguating the crossing **energy weight** (`−q⁻¹`, per
`def:crossing-energy`) from the Hecke **eigenvalue** of `σ⁻¹` (`q⁻¹`, or `−q`),
and I did not settle which the block intends.

## 5. Confirmed defect 3 — two incompatible Skein relations (strong/EM)

The corpus asserts both:

**Form A** — `L₊ − L₋ = (q − q⁻¹)·L₀`. AGENTS.md §7a, STRICT. **Forced**: right-
multiply the declared Hecke relation `σ² = (q−q⁻¹)σ + 1` by `σ⁻¹`. Carried by
[`skein-bar-antisymmetry.md:4`](../../content/quantum-observable-universe/climax-volume-mass/skein-bar-antisymmetry.md)
(with a Lean sibling, `prop:skein-bar-antisymmetry`), `definition-index.md:568`,
and `bar-involution-table3-data.md:3` ("*every* Hecke skein relation").

**Form B** — `q·L₊ − q⁻¹·L₋ = (q^{1/2} − q^{-1/2})·L₀`. Eleven blocks:
`crossing-energy.md:17`, `feynman-eigenbasis.md:29`,
`knot-particle-generation-consequences.md:24`,
`knot-particle-generation-interpretation.md:36`,
`embeddability-closure-spectral-filter.md:15`, `shell-threading-conjecture.md:10`,
`skein-mass-relation.md:4` + `.lean:11,36`, `skein-mass-relation-proof.md:16`,
`trace-ratio-observable.lean:34` + `-proof.md:29`,
`hadron-half-life-verification-table1-data.md:4`.

### 5.1 The machine test

In the Hoefsmit 2-dim representation of `H₃(q)` — first verified to satisfy
`σ² − (q−q⁻¹)σ − 1 = 0` exactly:

| Form | residual |
|---|---|
| A: `σ − σ⁻¹ − (q−q⁻¹)·1` | **exactly `[[0,0],[0,0]]`** |
| B: `qσ − q⁻¹σ⁻¹ − (q^{1/2}−q^{-1/2})·1` | **nonzero**; at `q₀` the off-diagonal is **0.18138** |

Symbolically, `q·σ − q⁻¹·σ⁻¹ = h·(σ + q⁻¹·1)` with `h = q − q⁻¹` — it carries a
genuine `σ` component, so it can **never** equal a scalar multiple of `1`.

Note the magnitude: the residual `0.18138` is *larger* than `½(q−q⁻¹) = 0.1045`,
the quantity the channel computes. This is not a small-parameter near-miss.

### 5.2 What is and is not being claimed — the scope that matters

**Form B is not false.** It is the correct Jones specialisation of the HOMFLY
skein relation (`a = t`, `z = t^{1/2} − t^{-1/2}`) — a relation among the
**invariants of three different links**, carrying a writhe normalisation. Read
that way, every block that states Form B as a property of a link invariant is
fine.

What is defective is the **role transplant**, and one block asserts it outright.
[`feynman-eigenbasis.md:29`](../../content/quantum-observable-universe/braids-and-knots/feynman-eigenbasis.md):

> *"The skein relation `q𝔪(L₊) − q⁻¹𝔪(L₋) = (q^{1/2} − q^{-1/2})𝔪(L₀)` is simply
> the characteristic equation of the braiding `c_{V,V}` evaluated under the
> categorical trace."*

The characteristic equation of `c_{V,V}` (eigenvalues `q`, `−q⁻¹`) is
`(σ−q)(σ+q⁻¹) = 0`, equivalently Form A. It is **not** Form B, per §5.1.

**Scope: (b), structural exclusion, invariant named.** The invariant is the
**Hecke quadratic relation** `σ² = (q−q⁻¹)σ + 1`, which the corpus declares
(AGENTS.md §7a) and which forces `σ − σ⁻¹ = (q−q⁻¹)·1`. Any purported *algebra*
identity in `H_n(q)` whose residual has a nonzero `σ` component is excluded, not
merely numerically disfavoured.

The **`needs-work`** sibling is `crossing-energy.md:17-20`, which cites Form B as
the warrant for its per-crossing sign convention: *"The sign convention follows
the Skein relation: [Form B]"*. Form B's `q` and `−q⁻¹` are normalisation
prefactors on whole-link invariants, not per-crossing energies. Reading them as
per-crossing weights is the transplant. The resulting *signs* happen to be the
ones `def:crossing-energy` wants, so the block is internally coherent — which is
precisely why this survived. I am holding it at `needs-work` because the fix is
a re-justification (cite the Hecke relation, i.e. Form A), not an arithmetic
correction, and that is an author call.

This is the **same balanced/unbalanced boundary** as the seed defect: `q^{1/2}`
standing in for Jones's `t^{1/2}`.

### 5.3 The Lean here is honest

[`skein-mass-relation.lean`](../../content/quantum-observable-universe/observations/skein-mass-relation.lean)
carries Form B as a **structure field**:

```lean
skein_mass : q * mass_plus - q⁻¹ * mass_minus =
  (q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))) * mass_zero
```

That is an *assumed hypothesis* on a hypothetical mass functional in a `rem:`
block, not a claimed proof. Satisfiable (one linear constraint), no vacuity
issue, no `sorry`. **Clean** as Lean hygiene. The false identification lives in
prose at `feynman-eigenbasis.md:29`, not here.

## 6. Clean — the weak channel's `b`, and *why* it is clean

[`mba-step09a-mass-identity.md:21`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09a-mass-identity.md)
stipulates `b = sqrt((q⁴+q²+1)/(q²+1)²)` for the `Q_β` ladder variable
`u = b·ℏ_q²`, naming it the Kashiwara/Hoefsmit `f̃₁` matrix element of `V_{(2,1)}`
of `H₃`.

Running question 1 as a **rigidity check** rather than a lookup: fix the
off-diagonal of the 2-dim rep to `b`, then impose `tr σ₂ = q − q⁻¹` and
`det σ₂ = −1` (the Hecke eigenvalues) *together with* the braid relation
`σ₁σ₂σ₁ = σ₂σ₁σ₂`. Result: **exactly one solution**, and it comes out
**symmetric** (`c = b` — the seminormal/orthogonal Hoefsmit form):

```
  σ₂ = (1/[2]_q) · [[ −q⁻²,  b·[2]_q ],
                    [ b·[2]_q,   q²  ]]        a = −1/(q³+q),  d = q³/(q²+1)
```

and `b = sqrt(q⁴+q²+1)/(q²+1) = sqrt([3]_q)/[2]_q` in the balanced convention
(`[3]_q = (q⁴+q²+1)/q²`, `[2]_q = (q²+1)/q`).

So **`b` is not a stipulated constant at all — it is forced.** There is no
convention freedom for a slip to occupy. This is the structural reason the weak
channel is immune where the EM channel was not: `b` is pinned by two relations,
whereas the crossing-energy channel decomposition is pinned by nothing that was
being checked.

## 7. Clean — the colour channel, and the exemplar worth copying

[`strand-twist-datum.md:11`](../../content/quantum-observable-universe/appendix-standard-model/strand-twist-datum.md)
introduces `Q_twist = T(t)/3` and does all three things the defective blocks omit:

1. **Names the normalisation's provenance, with a citation** — *"the colour-tube
   charge quantum of the quark picture, the helon-model normalisation
   `\cite{bilson-thompson2005}`"*. Name and value are explicitly tied, so
   question 1 is answerable by a reader.
2. **States the consistency invariant and calls it falsifiable** — *"the
   Gell-Mann–Nishijima relation hold[s] by construction if and only if the two
   independent charge routes agree, `Q_twist = Q` against [the crossing-derived
   Coulomb charge](#def:coulomb-charge) — a falsifiable consistency between
   framing and crossing data, not a definition."*
3. **Declines to wire it** — *"no numerical claim is made here."*

[`flavor-charge-assignments.md:34-36`](../../content/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md)
agrees. This is the discipline the class calls for, already practised in the
corpus. Per §3.3, its reference point (`Q = ½(n₊−n₋)`) is the *sound* half of
`coulomb-charge.md`, so it is unaffected by defect 1.

## 8. The mechanizable checker

[`convention_slip_validate.py`](../coordination/convention_slip_validate.py) +
[`convention-slip-registry.json`](../coordination/convention-slip-registry.json).
Generalises `trace_convention_registry_validate.py`, which implements **question
3** for traces. The insight is that **question 2 needs no reference
implementation** — a stipulated constant can be checked against an invariant it
implies, entirely self-contained — which is what makes it generalise across
channels.

| Rule | Check | Catches |
|---|---|---|
| **R1** reconstruction identity | A stated decomposition must sum to the object it decomposes. Symbolic, pin-independent. | Defect 1 — residual `−2m/q` |
| **R2** algebra-relation residual | A claimed `H_n(q)` identity must have zero residual in a Hecke-satisfying rep (Hoefsmit `H₃`, self-tested before judging). | Defect 3 |
| **R3** fibre-dimension integrality | `z(N) = q^N/[N]_q` is injective for `q > 1`, so a stipulated Ocneanu `z` implies `N_eff = −ln(1 − (q−q⁻¹)/z)/(2 ln q)`, which must be a positive integer. | The **seed** defect — `N_eff = 2.5995` |

R3's Lean backing is `QOU.BraidsAndKnots.ocneanu_param_eq_of_fibre_qdim`
(`FibreDimensionForcesTL.lean`, sorry-free), proving `z·[N]_q = q^N`.

Current run — 7 entries, **0 surprises**, exit 0:

```
[R1] DEFECT(known)  R1-em-coulomb-decomposition
     residual = -2*m/q  (reconstructs m/q + p*q)
[R1] ok             R1-em-coulomb-decomposition-corrected     residual 0
[R2] ok             R2-skein-form-A-hecke                     residual is the zero matrix
[R2] DEFECT(known)  R2-skein-form-B-as-characteristic-equation
     nonzero residual; at q0 = [[-0.00042434821, 0.18137738], [0.18137738, 0.21204693]]
[R3] ok             R3-trace-convention-D-jones-tl            N_eff = 2.00000000000 (integer, N = 2)
[R3] DEFECT(known)  R3-trace-convention-C-wenzl-z             N_eff = 2.59951553640 — NOT an integer
[R3] ok             R3-trace-N3                               N_eff = 3.00000000000 (integer, N = 3)
summary: 4 pass, 3 fail, 0 surprise(s)
```

`expect: "fail"` entries are **regression fixtures** pinning a confirmed defect,
so the validator is green today and stays informative. `--strict` exits 1 on a
surprise in **either** direction: a new defect, or a known defect quietly fixed
leaving the registry stale. Each rule ships with at least one positive control
(R3 has two, `N = 2` and `N = 3`, so it is not a two-point test).

**Honest limits.** The registry is hand-curated — R1/R2 cannot discover a
decomposition or a claimed identity in prose, only verify one that has been
transcribed. Automatic extraction of `$$...$$` decompositions from `.md` is the
obvious next step and is beaned. So this is a **guard against regression and a
drain-tracker**, not a corpus-wide detector.

`q₀` is the **experimental / proton** pin per the AGENTS.md owner directive of
2026-08-07. R1 and R2 are symbolic and pin-independent; only R3 evaluates at
`q₀`, and its verdict (0.5995 from an integer) is four orders of magnitude
clear of the tolerance, so it is not pin-sensitive either.

## 9. Not reached

Two candidate surfaces from the task were not reached and are beaned rather
than guessed at:

- **`α_EM = [2]_q·(1 − h²α)`**, the Coulomb charge's role in the EM self-energy
  sign work ([`2026-07-11-np-splitting-L2-em-sign-prune.md`](2026-07-11-np-splitting-L2-em-sign-prune.md)),
  and `ocneanu_12_em_correction_candidate.py`. The `[2]_q` factor sits on the
  balanced/unbalanced boundary and is a live candidate.
- **Gravity / spacetime and information channels** — not surveyed for stipulated
  normalisation constants at all.

Also open: whether any **production compute** implements the defective EM
decomposition (§3.2), with `stable-nucleus-valley` the first place to look.

## 10. What changed here

Nothing in production. This branch adds this audit, the validator, and the
registry. The three confirmed defects are **documentary** — but two of them
(defects 1 and 2) are arithmetic errors in blocks that downstream physics claims
cite, so they are not cosmetic. I have deliberately **not** edited the content
blocks: defect 1's fix is unambiguous (swap the multiplicities, or equivalently
cite `crossing-energy-decomposition.md`), but defects 2 and 3 require an author
decision about which normalisation and which relation is canonical, and fixing
1 alone would leave the chapter inconsistent in a new way.
