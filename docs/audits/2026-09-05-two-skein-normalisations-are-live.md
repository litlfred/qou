# Two Skein normalisations are live in this corpus, and they are not rescalings

**Date:** 2026-09-05 · **Bean:** `qou-8bxv` · **Producer:**
`computations/markov/skein_normalisation_two_conventions_audit.py` (8/8) ·
**Witness:** `computations/skein-normalisation-two-conventions.witness.json`
(proton pin) · **Lean:** `QOU/Braiding/SkeinNormalisation.lean`
(`lean`-direct exit 0, sorry-free, 7 declarations, only `propext` /
`Classical.choice` / `Quot.sound`)

## The claim

`AGENTS.md` §7a states the Skein relation as **STRICT**:

$$\textbf{(H)}\qquad L_+ - L_- \;=\; (q - q^{-1})\,L_0
\qquad\text{bridge } h_1 = q - q^{-1}$$

Eight live content blocks in five chapters state it differently:

$$\textbf{(J)}\qquad q[L_+] - q^{-1}[L_-] \;=\; (q^{1/2} - q^{-1/2})[L_0]
\qquad\text{bridge } s = q^{1/2} - q^{-1/2} = h_{1/2}$$

**These are not two normalisations of one relation.** The weight *ratio* on
$(L_+ : L_-)$ is $1$ in (H) and $q^2$ in (J). A rescaling $[L] \mapsto c[L]$
leaves that ratio fixed, so the only $q$ at which one constant reproduces both
weight pairs is $q^2 = 1$ — the classical point where both bridges vanish.
That is the load-bearing part of this audit, because the natural first reading
("same relation, bracket normalised differently") is measurably wrong.

Lean: `no_rescaling_of_skein_weights`.

## The exact relation between the two bridges

| identity | Lean |
|---|---|
| $h_1(u^2) = s(u)\,(u + u^{-1})$, in the square-root variable $q = u^2$ | `hOne_eq_sSqrt_mul_barEven` |
| $h_1^2 = [2]_q^2 - 4$ | `hOneSq_eq_twoQ_sq_sub_four` |
| $h_1^2 = s^2\,([2]_q + 2)$ | `hOneSq_eq_sSq_mul_twoQ_add_two` |
| $s^2 = [2]_q - 2$ | `WeakVertexT35.sSq_eq_twoQ_sub_two` (pre-existing) |

At the proton pin the conversion factor is

$$\frac{h_1^2}{s^2} \;=\; [2]_q + 2 \;=\; 4.0108968667071222998 .$$

The **squared** form is the one that matters downstream, because the
decay-coupling rate carries $s^2$ — not $s$ — exactly once.

**This identity is not new to the corpus, and the audit does not claim it is.**
`braids-and-knots/bar-involution-c5-algebraic-identities.md` already states the
factorisation $h_1 = s\,(q^{1/2} + q^{-1/2})$. What is new is that the two
*relations* are both live and are inequivalent, and that a single derivation
crosses between them (below). Recording this explicitly because a reader could
otherwise take the factorisation for the finding.

## Why the split survived undetected

The cofactor between the two bridges is **bar-even**: $[2]_{q^{-1}} + 2 =
[2]_q + 2$ (`twoQ_add_two_bar_invariant`, `barEven_bar_invariant`), while $s$
itself is **bar-odd** (`sJ_bar_antiinvariant`). Bar parity is this corpus's
usual separator for exactly this class of question, and it cannot see an even
factor. So the split is invisible to the tool most likely to be pointed at it.

## Consequence for the β-decay rate — a convention change hidden inside a substitution

The two conventions meet inside one derivation:

- **`prf:trace-ratio-observable`** (`observations/trace-ratio-observable-proof.md`
  lines 21 and 29) takes the vertex amplitude as
  $|\mathrm{skein\_amp}|^2$ with $\mathrm{skein\_amp} = q^{1/2} - q^{-1/2}$ —
  **convention (J)**, live, in a live block.
- **`prf:hadron-half-life`** item 1 replaces that $s^2$ by
  $|\mathcal{W}(q)|^2 = |\mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)|^2$,
  computed in $H_3(q)$ under the Hecke relation with $h = q - q^{-1}$ —
  **convention (H)**.

So the substitution changes the *convention* as well as the *coupling*, and
nothing in either block says so. The resulting figure differs by which bridge is
used:

| convention | quantity | value at $q_0$ |
|---|---|---|
| (J) — what the corpus computes | $\lvert\mathcal{W}\rvert^2/s^2$ | $129.40510740356669955$ |
| (H) — what §7a mandates | $\lvert\mathcal{W}\rvert^2/h_1^2$ | $32.263384401056933328$ |

**The `qou-ix74` scope-(a) negative survives under either.** Both $32\times$ and
$129\times$ are far too large to be the 10–17 % correction that negative is
about, so which convention is canonical does not move that verdict. **This is a
register defect, not a magnitude defect** — worth saying plainly, because the
two preceding corrections in this arc *were* magnitude defects (the $s^4$-vs-$s^2$
power, worth $91.77\times$, bean `qou-xql6`; and the withdrawn order argument,
`qou-q2l7`) and it would be easy to read this as a third of the same kind.

It also closes the open remainder of `qou-q2l7`: the $\{\tfrac12, \tfrac12\}$
exponent pair in the decay coupling is **forced by convention (J)**, not chosen.

## The surface: 8 blocks, 5 chapters

All eight verified present on this tree (8/8 live at the time of measurement):

| block | chapter |
|---|---|
| `predicted-spectra/beta-decay-skein-properties.md` | predicted spectra |
| `braids-and-knots/feynman-eigenbasis.md` | braids and knots |
| `brings-surface/embeddability-closure-spectral-filter.md` | Bring's surface |
| `climax-volume-mass/skein-crossing-asymmetry.md` | climax volume/mass |
| `climax-volume-mass/skein-crossing-asymmetry-prop.md` | climax volume/mass |
| `information-theory/skein-turing-machine.md` | information theory |
| `knots-particles-confinement/crossing-energy.md` | knots, particles, confinement |
| `appendix-transfer-matrices/tm-notation-table1-data.md` | appendix |

Consuming blocks recorded in the witness: `prf:hadron-half-life`,
`prop:trace-ratio-observable`, `prf:trace-ratio-observable`,
`def:beta-decay-skein`, `rem:bar-involution-c5-algebraic-identities`.

## A THIRD weighting — flagged here, RESOLVED by PR #6823

`prf:hadron-half-life` item 4 carries a pair Skein mass formula

$$\mathcal{S}_{ab}(q) \;=\; \frac{q\mu_a + q^{-1}\mu_b}{q^{1/2} + q^{-1/2}} .$$

The numerator has (J)'s asymmetric weights $(q, q^{-1})$, but the denominator is
the **bar-even** cofactor $q^{1/2} + q^{-1/2}$, **not** the bar-odd bridge
$s = q^{1/2} - q^{-1/2}$ that (J) would put there. So it is neither (H) nor (J)
as stated above.

**Flagged here; RESOLVED by PR #6823 the same day — reading (R3), and the
bar-even denominator is FORCED.** This audit offered three readings without
choosing (a third normalisation; a sign slip for $s$; or a deliberate
symmetrising normalisation because $\mathcal{S}_{ab}$ is a mass and not an
amplitude). The sibling branch answered it with two structural arguments,
neither numerical, and the third reading is the right one:

1. **Bar-covariance.** A mass must map to a mass under $q \mapsto q^{-1}$. With
   the **even** denominator, $\mathcal{S}_{ab}(1/q) = +\mathcal{S}_{ba}(q)$ —
   the bar involution *exchanges the constituents*, which is what a mirror
   should do. With the odd bridge $s$ it is
   $\mathcal{S}_{ab}(1/q) = -\mathcal{S}_{ba}(q)$: the mirror of a mass is a
   **negative** mass ($6.1844009 \to -6.1844009$ at the proton $q_0$, 60 dps).
2. **The classical limit, which is fatal to the sign-slip reading.** The even
   denominator gives $\mathcal{S}_{ab} \to (\mu_a + \mu_b)/2$ and the self-pair
   $\mathcal{S}_{aa} \to \mu_a$ exactly. The odd bridge puts a non-vanishing
   numerator over a vanishing denominator and **diverges** as
   $(\mu_a+\mu_b)/(q-1)$. That contradicts a statement the corpus already
   makes — `hadron-half-life-fermi.md` has beta decay *ceasing* at $q = 1$,
   whereas under the odd bridge $Q$ diverges and $f(Q) \propto Q^5$ blows up.
   So adopting the sign-slip reading would break an existing claim.
3. **Corroborating role split.** The corpus puts bar-**odd** $s$ in the
   *numerator* of amplitudes (correctly $\to 0$ at $q=1$) and the bar-**even**
   cofactor in the *denominator* of masses: bar-odd where vanishing is wanted,
   bar-even where finiteness is wanted.

**Scope (b)** — a structural exclusion of the odd bridge *in this formula*, on
two proved invariants (finiteness of the $q \to 1$ limit; sign-preservation of
a mass under the bar involution). It says **nothing** about which Skein
normalisation is canonical elsewhere, so the (H)/(J) split above and item 1's
silent substitution are untouched. Probe
`computations/qbeta/pair_skein_mass_bar_parity_probe.py` (5/5), landing on
PR #6823.

**What that changes for this audit:** the pair Skein mass formula is *not* a
third live convention. It is a mass-sector normalisation whose bar-even
denominator is forced, sitting alongside (H) and (J) rather than adding to the
split. So the two-convention framing above **is** exhaustive for skein
*amplitudes* — which is the opposite of what this section originally warned,
and is a stronger result than the flag it replaces.

## What is NOT decided

Whether the rate is restated in (H) to match §7a, or §7a is amended to record
(J) as the physics-sector convention, is an **author decision**. It touches a
STRICT rule and eight blocks in five chapters, and nothing measured here forces
either reading. No content block and no `AGENTS.md` line is edited on this
branch. The producer measures; it does not pick.

## Verification

- **Producer:** 8/8 assertions pass. `mpmath` end to end; no `float`
  arithmetic. Symbolic identities checked over exact rationals (`sympy`) before
  numerical evaluation, so the bridge identities do not rest on a floating
  agreement.
- **Lean:** `lean`-direct **exit 0** on `SkeinNormalisation.lean` against its
  real import cone; `#print axioms` on all seven declarations shows only
  `propext`, `Classical.choice`, `Quot.sound` — no `sorryAx`. Generic
  `{K : Type*} [Field K]` throughout, no `ℝ`, so no §7c straddle
  (`check-sidecars.sh`: *library Lean — no ℝ, generic OK*).
- **Precision gates:** `scripts/precision-gates.sh --changed` exit **0**.
- **No CI exists** (Actions are `workflow_dispatch`-only), so the above is the
  whole gate, not a supplement to one.
- **Known unrelated red:** `check-sidecars.sh` reports the authors-note
  Lean-coverage stats stale. Verified pre-existing — it fires identically with
  this branch's changes stashed — so it is not refreshed here; doing so rewrites
  a global note every sibling branch also touches.
