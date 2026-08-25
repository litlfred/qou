# The two-nucleon interface is selected by isospin, not by a crossing count

**Date:** 2026-08-09
**Branch:** `claude/anchor-followups-2026-08-08`
**Beans:** `qou-h7mh` (bond count), `qou-c6gx` (interface scalar), `qou-8pl3` /
`qou-8p1x` (N=3 routes)
**Lean:** `QOU/QBeta/InterfaceScalar.lean` §`IsospinOrdering`, §`ChannelSelection`

Answers three questions put to this session:

1. derive why identical nucleons take two crossings — **not** a fit;
2. is the unbound two-nucleon channel aligned to the eightfold way or to the
   Standard Model;
3. does the corpus already force `N = 3` via `S₃` / SU(3) / a knot complement.

The answer to (1) is that **the question is mis-posed**, and that is provable
rather than a matter of taste. (2) is: isospin SU(2), which sits *inside* the
eightfold way but does not need it — and the residual mismatch is a
Standard-Model fine-tuning the framework has no channel for. (3) is: **no.**

---

## 1. The premise is refuted before any number is computed

The proposal was `m_pp = m_nn = 2`, `m_pn = 1` in
`atom_braid_word_3A(Z, N, *, m_pp, m_pn, m_nn)`. Bean `qou-h7mh` already warns
against exactly this — *"DO NOT JUST FIT m_\*. Tuning them to reproduce 2.15
buys a good table and costs the parameter-free claim"* — so it needed a
derivation or nothing.

It gets nothing, for a reason that is stronger than "no derivation was found".
**Nature has four two-nucleon channels, not three:**

| channel | S | T | B (MeV) | state |
|---|---|---|---|---|
| pn ³S₁ (deuteron) | 1 | 0 | +2.224566 | **bound** |
| pn ¹S₀ (virtual)  | 0 | 1 | −0.066 | unbound |
| pp ¹S₀            | 0 | 1 | ≈ −0.1 | unbound |
| nn ¹S₀            | 0 | 1 | ≈ −0.1 | unbound |

The two pn rows have **identical nucleon content** and **opposite boundness**.
Any interface assigned from the unordered pair of species — which is precisely
what a multiplicity `m_pp / m_pn / m_nn` is — is a function of that content, so
it must give the two pn rows the same energy. No choice of the three integers
can succeed, because the defect is in what they are *allowed to depend on*.

Formalised as `content_keyed_interface_refuted` (`InterfaceScalar.lean`): if the
interface factors through `content : Channel → Content` and the two pn channels
share content, then `0 < B` and `B ≤ 0` for them is `False`. Trivial as a proof;
it is the load-bearing step, so it is on the record as a theorem rather than as
prose.

Two further notes, recorded because they were the obvious routes and both fail:

* **The naive braid-topology argument runs backwards.** For identical particles
  the configuration space is `(Mⁿ − Δ)/Sₙ` with `π₁ = Bₙ`, so `σ` itself is a
  loop; for distinguishable particles `π₁ = Pₙ` and only `σ²` closes. That
  predicts `σ²` for **pn** and `σ` for pp/nn — the opposite assignment, and it
  binds pp while unbinding the deuteron.
* **Identity is the wrong variable anyway.** pp and nn are identical-nucleon
  channels, pn ¹S₀ is not, and all three behave the same. What they share is
  `T = 1`.

## 2. The variable that works is already in the algebra — free

`T` is not a new parameter. The Hecke quadratic `σ² = h·σ + 1` has eigenvalues
`q` and `−q⁻¹`, and its spectral projectors

    P₊ = (σ + q⁻¹)/(q + q⁻¹)        P₋ = (q − σ)/(q + q⁻¹)

are the isospin-symmetric (`T = 1`) and antisymmetric (`T = 0`) channels. Both
were already proved complementary and orthogonal (`proj_add_eq_one`,
`proj_mul_eq_zero`). Their interface scalars are

    μ₊ = (z + q⁻¹)/(q + q⁻¹) = 0.75270211325196540159
    μ₋ = (q − z)/(q + q⁻¹)   = 0.24729788674803459841        μ₊ + μ₋ = 1

**These are not new objects.** They equal the `n = 2` Wedderburn/Markov weights
`y_(2)` and `y_(1,1)` from `y_lambda_su_n(2, q₀, 2)` to `3.3e-52`, i.e. to
round-off at 50 dps — the identification `markov_param_determined` +
`weight_eq_proj_scalar` already asserted, now measured. So selecting the channel
costs no parameter: it is a choice of Young diagram, and the diagram is fixed by
`T`.

`μ₊ + μ₋ = 1` (`mu_sum_eq_one`) is the statement that the two channels
**partition the free trace**. It also explains a structural limit: projection can
only remove weight, so `μ_T < 1` and `B_T > 0` for both `T`. **The projector
decomposition can never produce an unbound channel.** Unbinding needs `μ > 1`,
which requires leaving the convex decomposition of `1` — e.g.
`stacked_crossing_gt_one`, where `σ²` gives `μ = h·z + 1 = 1.12809 > 1`.

## 3. The one thing that IS derived, for every q, with no fit

Under convention D (`z = q³/(q²+1)`),

    2z − h = (q⁴ + 1) / (q(q² + 1))          (an identity; residual 0.0 at 50 dps)

Every factor on the right is positive for `q > 0`, so `h < 2z` always
(`two_z_sub_h_conventionD`, `h_lt_two_z_conventionD`). Since
`μ₊ − μ₋ = (2z − h)/(q + q⁻¹)`, this gives

> **`μ₋ < μ₊` for every `q > 0`** (`mu_singlet_lt_mu_triplet`), hence
> `B₊ < B₋` (`singlet_binds_more`): **the isospin singlet is always the more
> strongly bound channel.**

That is the deuteron-versus-pp/nn ordering, forced by the algebra, with no
crossing count, no multiplicity, and no numerical input. It is the first
structural result in this line that gets the sign right without tuning.

It is also convention-robust: `2z − h > 0` holds under C too (0.7896), though
there it is `q`-dependent rather than a closed-form positive. D gives the clean
identity — one more point in D's favour after the excision.

## 4. Where it stops, quantitatively — and the reason is Standard-Model side

Honest accounting of the miss:

| reading | T=1 | T=0 | splitting |
|---|---|---|---|
| absolute `B = −α·ln μ` | +1.1892 | +5.8485 | 4.6593 |
| nature | ≈ −0.07 | +2.2246 | 2.2906 |

> **RETRACTION 2026-08-09 — the `+5.8485` column is NOT a deuteron prediction,
> and tabulating it against nature's `+2.2246` was wrong.** It is *identically*
> the pp+nn two-bond energy. Exact algebraic identity under D, residual `1.0e-51`
> at 50 dps:
>
>     z     = q³/(q²+1)  = μ_pp        z − h = q⁻¹/(q²+1) = μ_nn
>     μ₋    = 1/(q+q⁻¹)² = μ_pp · μ_nn        μ₊ = 1 − μ_pp·μ_nn
>
> so `B(T=0) = −α·ln μ₋ = B_pp + B_nn` exactly — and it is *writhe-invariant*,
> the `±0.4908765` shifts on pp and nn cancelling in the sum. Equivalently
> `μ₋ = [1]/[2]²` and `μ₊ = [3]/[2]²`, relative quantum dimensions with the
> `q^{±2}` framing factors cancelled. So (a) the colour-weighted p–n bond and
> (b) the `T = 0` projector are **different objects**, not competing predictions
> — there was never a conflict to reconcile.
>
> Moreover `+5.8485` can **never** be the deuteron, for any `q`: `q + q⁻¹ ≥ 2`
> by AM-GM (already proved in-file as `two_le_add_inv`) gives `μ₋ ≤ 1/4`, hence
>
>     B(T=0) ≥ α·ln 4 = 5.803002359688 MeV     for every q,
>
> and `B_AME(²H) = 2.2245662` is **61.7 % below that universal floor**
> (symmetrically `B(T=1) ≤ α·ln(4/3) = 1.204232`). A two-line Lean proof from
> lemmas already present.
>
> What the projectors legitimately supply is the **ordering**
> (`mu_singlet_lt_mu_triplet`, `singlet_binds_more`) and the channel-selection
> refutation (`content_keyed_interface_refuted`) — none of which is a magnitude
> claim. Those stand. The magnitude framing below does not.
>
> Structural note worth keeping: (a) and (b) are the **diagonal and off-diagonal
> data of one 2×2 Hoefsmit `V_{(2,1)}` block** of `H₃`. The bond family has no
> access to the off-diagonal, which is exactly *why* `t` is confined to
> `[z−h, z]` and the projectors sit outside it on both sides. That same `M₂`
> block is what carries the Lorentzian signature in `GramSignature.lean`.

The **sign pattern is right and the magnitude is 2.034× too large**. Both model
channels bind, where nature binds only one.

The reason is not a missing crossing. In S-wave, Pauli **locks spin to isospin**:
space is symmetric, so spin and isospin symmetry must be opposite —
`S = 1 ⟺ T = 0` and `S = 0 ⟺ T = 1`. A Pauli-consistent interface therefore
carries a projector in *each* SU(2), and

    μ(³S₁) = μ₊^spin · μ₋^iso = μ₋^spin · μ₊^iso = μ(¹S₀) = 0.186142

**exactly degenerate**, because multiplication commutes. A flavour-only interface
cannot split ³S₁ from ¹S₀ *at all*.

In the Standard Model that splitting is the **tensor force** (³S₁–³D₁ mixing) —
a spin–space coupling. The Hecke interface has one index (the strand) and no
space index to carry it. Separately, nature's `T = 1` channel sits at −0.066 MeV
because the ¹S₀ scattering length is unnaturally large (`a_s ≈ −23.7 fm`), i.e.
a near-critical fixed point — fine-tuning, not symmetry. The framework produces
`O(α) ≈ 4.7 MeV` symmetric splittings and has no mechanism to tune one to
threshold. Both halves of the residual are dynamical, not representational.

## 5. Eightfold way: not needed here, and not available anywhere

The two-nucleon channel structure is `2 ⊗ 2 = 3 ⊕ 1` in isospin SU(2) — the
`n = 2` Hecke decomposition into `(2) ⊕ (1,1)`. It lives entirely at `N = 2` and
requires only two-row partitions. **It does not need the eightfold way.** What
needs `N = 3` is the baryon octet and the three-row partition `(1³)`, which
`RowCapObstruction.lean` kills at `N < 3`.

A corpus-wide sweep for a forcing argument (`S₃`/`B₃`, SU(3) directly, knot
complements, Borromean/eightfold) found **none**, and the corpus says so itself:

* `RowCapObstruction.lean:66` — the obstruction "says nothing about whether some
  other construction supplies `N = 3`, **which is the open half**."
* `.beans/qou-8pl3:78` — "**No proved invariant forbids `N = 3`; it is simply not
  constructed.**"
* `eightfold-open-problems.md:18` — "**The *obstruction* is proved; the
  *construction* is missing.**"

Route by route: `a2-from-three-strands.md:5` flags its own `A₂` as true *by
construction* and "**not** the `A₂ = 𝔰𝔩₃` of flavour SU(3)";
`2026-08-04-pgl3-higher-teichmuller-assessment.md` §2a answers the knot-complement
route "**NO** — the holonomy is rank 1, it **reinforces** the `dim V = 2` cap";
`borromean-decuplet-derivation.md:61` withdraws its own Brunnian→Young-symmetriser
step "as a non-sequitur". `decuplet_forces_three` / `singlet_forces_three` run in
the direction the framework does not need — they infer `N = 3` from *observing* a
decuplet.

And there are **anti**-forcing results: `ocneanu-N-lockin.witness.json:63` shows
the `N = 2` and `N = 3` Ocneanu traces on `H₃(q)` are not proportional, so
"`N = 2` is locked in for the mass pipeline"; `.beans/qou-8p1x:215` shows `N` is
the quantum dimension of the fibre, so choosing `N` *is* choosing `V`, and
Descartes fixes `dim V = 2`. Even `N = 2` is posited, not derived
(`su2-emergence.lean:58`, `fund_dim_two` is a hypothesis field).

**Conclusion for the eightfold question: the unbound channel aligns to isospin
SU(2), a subgroup of the eightfold way that the framework already has in full.
Nothing here motivates or supplies `N = 3`.**

## 6. What changed in the tree

* `InterfaceScalar.lean` — new sections `IsospinOrdering` (5 theorems) and
  `ChannelSelection` (1), sorry-free.
* `computations/y_lambda_su_n.py` — **stale-docstring fix.** It still asserted
  "the production trace is convention **C**" and led with `N = 2.5995155…`;
  C was excised on this branch (`73311b57`, `33a6c7aa`). Three self-tests were
  asserting the pre-excision state and were **failing (30/33)**; they now pin the
  live convention (production **is** D, `y_(1³) = 0`, production **is** SU(2)
  exactly) and act as the regression guard against a slide back to C. Back to
  33/33. The C measurement is retained as history — it is *why* C was excised.

## 6b. Where a space index would have to come from

§4's degeneracy is an obstruction with an address: the interface needs an index
carrying `L`. The corpus has an `ℓ` in exactly two places, and **neither is
connected to the NN interface**:

* `knots-particles-confinement/shell-transition-knot.md:20` — harmonic-oscillator
  levels with `ℓ = N, N−2, …` and the `j = ℓ ± ½` split. This is the shell model
  imported as structure, not derived from the trace.
* `predicted-spectra/skein-coulomb-enhancement.md:41` — a partial-wave sum over
  `ℓ` inside a scattering amplitude.

Wiring either to the interface is not attempted here and should not be assumed
cheap: the Hecke generator `σᵢ` is indexed by strand position, and there is no
existing map from strand position to orbital angular momentum. Recording the
address so the next reader does not re-derive the obstruction from scratch.

## 7. Not claimed

* No claim that the isospin reading fixes the ²H magnitude. It does not; it is
  2.034× high, and §4 says why.
* No claim that `B = −α·ln μ` is the right functional. §4's degeneracy result is
  an argument that *no* flavour-only `μ` can be, whatever the functional.
* The Markov property remains an `axiom` with a `sorry` in this corpus
  (`jones-markov-trace.lean`), so everything downstream of `interface_scalar` is
  conditional on Jones (1987).
* `m_pp`/`m_pn`/`m_nn` are left at 1. Nothing here licenses changing them, and
  §1 is the argument that nothing ever will.

---

## 8. Claims EXCISED from the paper on 2026-08-09, preserved here

Owner directive: excise the false claims from the paper, keep them in the audit.
These were the module docstring of
`content/quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean`, which
is paper content. All were **convention-C specific** and became false when C was
excised. The THEOREMS are untouched — they are true conditionals; what was wrong
was the claim that they bind at the deuteron.

Verbatim, as removed:

1. Title / subtitle —
   "# The nucleon–nucleon interface is a single scalar, **and it has a floor**"
   "**Why no crossing convention can bind the deuteron.**"

2. The band paragraph —
   "Numerically that is `[2.907195, 5.177967]` MeV, while `B_AME(²H) =
   2.2245662`: **below the floor by 30.69 %** … no crossing sign, colour weight,
   or multiplicity reaches the deuteron."

3. The floor billing —
   "**the stronger, q-independent form, which supersedes `mu_unreachable` as the
   headline.** The production Markov parameter is `z = 1/(q^{1/2} + q^{-1/2})`"
   — `z = 1/(√q+1/√q)` is convention C and is NOT the production parameter.

4. `mu_unreachable`'s own docstring —
   "so the deuteron is unreachable, and the ²H miss cannot be localised in the
   interface."

5. The scope note —
   "This is an impossibility result about the *interface*" … "Since no
   admissible `μ` reaches AME, and since the per-bond deficit changes sign
   across `A` (audit §4), the defect is in the *form* of `B = −α·ln μ`".

6. The mirror-split number — "Measured, `α(L_nn − L_pp) = 2.27077 MeV`" (C-era;
   under D with the derived writhe term it is 0.76532 MeV).

### Why they are false

Under production convention D, `z = q³/(q²+1) = 0.6126880 > 1/2`, so the AM-GM
step behind the floor never bites. Measured:

    admissible band under C   [2.907195, 5.177967] MeV   AME 2.224566 BELOW it
    admissible band under D   [2.0507,   3.7978  ] MeV   AME 2.224566 INSIDE it

    required offset under C   d = +0.088442 = +0.42305 h   OUTSIDE [-h, 0]
    required offset under D   d = -0.024973 = -0.11945 h   INSIDE  [-h, 0]

So the deuteron is reachable. What replaces the impossibility is a narrower and
better-posed gap: the derived colour weight `t = ½ − δ/4 = 0.499656` does not
equal the required `t = 0.119453`, a factor 4.183. Reachable, not derived.

Also flagged: the A-scaling refutations in bean `qou-c6gx` ("per-bond deficit
changes sign, spread 7.105 MeV/bond") were computed under C and must be re-run
before being cited.
