# PR #664 critical review — c_3 / c_4 categorical claims

**Date:** 2026-05-17
**Branch:** `claude/post-670-story-b-mp-c5-c6`
**Status:** Critical review of [PR #664](https://github.com/litlfred/qou/pull/664)
("prop:hopf-jones-c3-categorical — c_3 = J_Hopf(q=1) = -2 from V_(2,1)
self-fusion (Story A falsified)") and its companion c_4 claim.
**Verdict:** The probes are **tautological**; the proof sketches in the
`.md` files hand-wave the critical steps; **Story A is not falsified**
by this PR. The categorical derivation is plausible but not done.

## What PR #664 claims

> Derives `c_3 = J_Hopf(q=1) = -2` from QOU axioms with no empirical fit,
> mirroring PR #661's `c_2 = b²` categorical proof.
>
> Combined with #661, this **falsifies Story A** (PR #657's "all c_k
> beyond c_2 are CODATA noise"): the categorical derivation matches the
> empirical PR #655 value of c_3 = -2 *exactly*. The 0.0066 ppm Q_β
> residual closure is now a *prediction* of QOU, not a curve-fit.

The PR ships:

- `prop:hopf-jones-c3-categorical` (`.ts/.md/.lean`) — proposition + 4-step proof sketch + Lean class `HasC3HopfJonesIdentity`
- `prop:kashiwara-jones-c4-categorical` (`.ts/.md/.lean`) — same pattern for c_4 = b² + 1/2
- `probe_hopf_jones_c3_categorical.py` — claims 3/3 assertions pass at 50 dps
- `probe_kashiwara_jones_c4_categorical.py` — same

## Finding 1 — both probes are tautological

### `probe_hopf_jones_c3_categorical.py`

```python
def j_hopf(q):
    """Jones polynomial of the positive Hopf link at q."""
    return -(q + 1 / q)          # HARDCODED textbook formula

c3_categorical = j_hopf(mp.mpf(1))           # = -2 by arithmetic
c3_empirical_pr655 = mp.mpf(-2)              # HARDCODED literal
delta = c3_categorical - c3_empirical_pr655  # = 0 by construction
```

The 3 "passing" assertions are:

1. `c3_categorical == -2` — true because `-(1 + 1/1) == -2` (arithmetic).
2. `c3_categorical matches c3_empirical_pr655` — true because **both are
   hardcoded as -2 in the same script**.
3. `|c_3| == 2` ("Story A falsified") — restates #1.

The probe asserts `c_3 = -2` by writing `-2` in two places and verifying
they're equal. It does **not** compute the Markov trace of $\sigma_1^2$
via the V_(2,1) Hoefsmit seminormal representation, despite the
docstring claiming "Computing J_Hopf(q) = -[2]_q via the V_(2,1)
Hoefsmit seminormal Markov trace of $\sigma_1^2$ in $H_2(q)$."

### `probe_kashiwara_jones_c4_categorical.py`

Worse:

```python
b_at_one = mp.mpf(1)                                  # ASSUMED b = 1 at q = 1
b_squared_at_one = b_at_one ** 2                      # = 1
half_shift = mp.mpf(1) / 2                            # ASSUMED 1/2

c4_categorical = b_squared_at_one + half_shift        # = 3/2
c4_empirical_pr655 = b_squared_at_one + half_shift    # SAME EXPRESSION

delta = c4_categorical - c4_empirical_pr655           # = 0, identically
```

This is literally `c4 - c4 == 0`, presented as a proof that c_4 = 3/2 is
categorically derived. The "b at q=1" value is not computed from the
Hoefsmit representation (which is the cited source); it's just
`mp.mpf(1)`.

## Finding 2 — the proof sketches hand-wave the critical step

The `.md` body of `prop:hopf-jones-c3-categorical` has a 4-step sketch:

| Step | Content | Rigour |
|---|---|---|
| 1. Self-fusion decomposition | $V_{(2,1)} \otimes V_{(2,1)}$ Littlewood-Richardson decomposition | OK — standard L-R, correct |
| 2. Frobenius selection picks Hopf channel | Claims $V_{(2,2,2)}$ is the "Hopf-mediated" self-conjugate channel that "admits a 2-strand Hopf reduction via Markov stabilisation" | gap — asserted, not derived |
| 3. Hopf trace at $q = 1$ | $J_\mathrm{Hopf}(q) = -[2]_q \Rightarrow J(1) = -2$ | OK — textbook Jones polynomial, but cited as fact rather than derived from V_(2,1) trace |
| 4. Coefficient identification | $c_3 = J_\mathrm{Hopf}(1) = -2$ at order $h^6$ | gap — asserted, no order-$h^6$ expansion of $Q_\beta$ shown |

**Step 2 is where the work has to be done.** The claim is that the
order-$h^6$ contribution to $Q_\beta$ in the Story B expansion comes
specifically from the $V_{(2,2,2)}$ channel under Markov stabilisation
of the $\sigma_1^2$ closure into the 6-strand decomposition. That
requires:

- An explicit Markov-stabilisation map $V_{(2,1)}^{\otimes 2} \to H_6 / \text{ideal}$
- A projection onto the $V_{(2,2,2)}$ irreducible
- A calculation that this projection equals the closure of $\sigma_1^2$
  modulo the trace
- An order-$h^6$ expansion of $Q_\beta$ showing the coefficient is the
  Jones value at $q = 1$

None of this is in the proof sketch.

**Step 4 is similarly hand-waved.** The Q_β precision ladder is
$Q_\beta = Q_A \prod_k (1 + c_k \hbar_q^{2k})$. To get from "Hopf-trace
at $q=1$ is $-2$" to "$c_3 = -2$" requires showing the $\hbar_q^6$
coefficient in the Q_β expansion picks up exactly the Hopf-trace
contribution (and not other order-$h^6$ terms from the other irreps).
The proof sketch claims the non-self-conjugate channels "cancel in
pairs" but doesn't verify this.

## Finding 3 — the textbook Jones polynomial is not a categorical derivation

$J_\mathrm{Hopf}(q) = -(q + q^{-1})$ is the standard Kauffman/Jones
formula for the positive Hopf link, derivable from the skein relation
or from the Kauffman bracket directly. **Citing this textbook value
does not constitute "derivation from V_(2,1) self-fusion."**

For the claim "c_3 = J_Hopf(q=1)" to be a *categorical derivation*
specific to QOU, the V_(2,1) Hoefsmit seminormal Markov trace must
*produce* the polynomial $-(q + q^{-1})$ symbolically, not be cited as
giving it. PR #661 (c_2 = b²) did this for its own claim — the
seminormal Hoefsmit matrices were constructed and the order-$h^4$
coefficient extracted from the actual trace. PR #664 does not do the
analogous calculation for c_3.

## Finding 4 — Story A is not falsified

To falsify Story A's "c_3 = 0 within CODATA noise" claim, PR #664 would
need to show **from QOU axioms that c_3 must be -2** (excluding all
other values). What PR #664 actually shows is:

- The textbook Hopf-Jones polynomial at q=1 happens to be -2.
- The PR #655 empirical extraction of c_3 from the residual is -2.
- These match.

This is **consistency**, not derivation. Story A's position is that the
ladder coefficients beyond c_2 are CODATA noise; consistency with -2
is not exclusion of "c_3 = 0 within ~400 ppb."

A genuine falsification of Story A would need either:

1. **A first-principles derivation** that the V_(2,1) Hoefsmit Markov
   trace of $\sigma_1^2$ symbolically equals $-(q + q^{-1})$, plus the
   order-$h^6$ extraction in step 4 above, with all order-$h^6$
   contributions accounted for.
2. **A consistency-with-bounded-uncertainty argument**: at 50-dps
   precision the empirical c_3 is closer to -2 than to any other
   simple-Jones-at-q=1 value (-2, +1, +2, ±4), and the only
   structurally-admissible channel is the Hopf. PR #655's residual
   chain *does* close to -0.0066 ppm using c_3 = -2; this is suggestive
   but not exclusive.

## Finding 5 — c_4 is even thinner

Where c_3 at least has a textbook Jones value to point at, c_4's
"b² + 1/2 = 3/2" has:

- `b = 1` at q=1 asserted (not computed from Hoefsmit; PR #661 derived
  $b^2 = (q^4 + q^2 + 1)/(q^2 + 1)^2$ which gives $b^2 = 1$ at $q = 1$
  identically, so $b^2$ — but the c_4 probe uses `b = 1` directly, not
  $b^2$ from that formula).
- "GB-jet half-shift" of +1/2 from "Markov-symmetrization step at h^8"
  — asserted as "exact, independent of q" with no derivation.

The c_4 = 3/2 claim is even less substantiated than c_3 = -2.

## What this means for my PR #671 audit upgrade

The PR #670 audit doc
[`2026-05-16-story-b-canonical-chain.md`](2026-05-16-story-b-canonical-chain.md)
was upgraded in PR #671 to say "Story B is **structurally forced** by
PR #664's categorical c_3 proof." Per the findings above, this
**overstates** what PR #664 demonstrates. PR #664 shows Story B is
*consistent with* the textbook Jones polynomial and PR #655's empirical
chain. It does not *force* Story B.

**Correction**: Story B remains a strong candidate, supported by:

1. PR #661's genuinely categorical c_2 = b² proof
2. PR #664's *consistency* check (textbook J_Hopf(1) = -2 matches PR #655's empirical -2)
3. The natural categorical reading of the Q_β precision ladder

But "Story A falsified" is too strong — Story A is *empirically
disfavoured by ~60×* (Story B's 0.0066 ppm residual vs Story A's c_3 = 0
floor of ~400 ppb) but not categorically excluded by what's in PR #664.

PR #671 should be amended to walk back the "structurally forced" wording.

## Summary verdict

| Question | Answer |
|---|---|
| Is PR #664 on a wild goose chase? | No — the categorical reading is *plausible* and consistent with what's known. |
| Has it found a gap? | Yes — but inverted: the gap is that the probes don't deliver the proofs they claim to. The probes are tautologies. |
| Does it falsify Story A? | No. It demonstrates consistency, not exclusion. |
| What would close the gap? | (a) Symbolically compute the V_(2,1) seminormal Markov trace of σ_1² and verify it equals -(q + q⁻¹); (b) extract the c_3 coefficient from an order-h^6 expansion of the full V_(2,1) tower, not from the bare Hopf textbook value. PR #661's c_2 proof is the template. |

## Finding 6 — the κ magic-shell formula is fit-then-interpret

PR #664 also ships `prop:magic-shell-coupling-kappa` (`magic-shell-coupling-kappa.{ts,md,lean}`) claiming a categorical closed
form for the per-(n_pp − n_nn) excess slope κ at single-magic anchors:

$$
  \kappa \;=\; -\frac{E_0 \cdot \log(1/h)}{[2]_q \cdot [3]_q}
$$

The numerical match against PR #656 v6's empirical κ is 0.035%
(κ_cat ≈ -1.0704 MeV vs κ_emp ≈ -1.0708 MeV). The proposition `.md` and
the probe `probe_kappa_categorical_h7a_closed.py` present this as
categorical. Problems:

1. **The formula was discovered empirically.** The `.md` explicitly
   admits: "*identified empirically in PR #645 at the doubly-magic
   anchor (2, 2) and structurally as the logarithm of the Hecke
   deformation*". This is the fit-then-interpret pattern, not
   derive-then-verify.

2. **`log(1/h)` is transcendental.** Logarithm is not a standard
   categorical operation in the QOU substrate. Its appearance as the
   "natural magic-shell energy unit" is interpretation, not derivation.
   No chain links the categorical axioms to a log.

3. **The q-bracket product `[2]_q · [3]_q` is asserted as "V_2 ⊗ V_3
   Schur-Weyl tensor product"** — but V_2 and V_3 are notation-ambiguous
   (partition $(2)$ vs $(1,1)$? $(3)$ vs $(2,1)$ vs $(1,1,1)$?), and the
   claim that the q-bracket product is the right LR normalization is
   asserted, not derived.

4. **One specific `E_0` convention** is chosen out of three documented in
   `derivation_chain.py`. The choice is not justified beyond making the
   numerics work.

5. **0.035% is not exact.** PR #661 (the genuine template) gave
   *symbolic* equality for $c_2 = b^2$, not a 0.035% match. With several
   tunable structural choices ($E_0$ convention, which q-bracket product,
   sign convention), a 0.035% match could be coincidence.

The probe at least *computes* κ from substrate inputs (unlike the c_3/c_4
probes which hardcode the answer twice). But "computes from substrate
inputs" $\neq$ "categorical derivation" when the formula itself was
empirically discovered.

The companion m4 probe `probe_m4_magic_shell_correction.py` is more
honest — it explicitly acknowledges "κ is empirical from the v6 probe
(not yet categorically derived)" and "The H7a piece $[A-2]_q \cdot E_0 \cdot
\log(1/h)$ was refuted as a UNIVERSAL closure by PR #654's F2 probe."

## Finding 7 — the codebase has TWO disagreeing tr_M implementations (q^{1/2} vs q coordinates)

Running `probe_hopf_markov_trace_genuine.py` (companion replacement
for PR #664's tautological probe) on σ_1² in H_2 surfaced a deeper
infrastructure issue:

| Implementation | Formula | Result on σ_1² (H_2) | Value at q=1 |
|---|---|---|---|
| `hoefsmit_symbolic.tr_M_symbolic` | $\sum_\lambda w_\lambda \chi^\lambda(\beta) / f^\lambda$ | $(q^4+1)/(q^3+q)$ | +1 |
| `markov_weights_symbolic.tr_M_canonical` | $\sum_\lambda y_\lambda \chi^\lambda(\beta)$ (Wenzl y_λ) | (huge half-power expression) | +1 |
| Textbook Jones $-(q+q^{-1})$ | (Kauffman/skein) | $-(q+q^{-1})$ | −2 |

The first two are symbolically different rational functions even
though they agree at $q=1$. **Neither equals the textbook Jones
polynomial** at any $q$. An equivalence script
[`y_lambda_equivalence_proof.py`](../../computations/y_lambda_equivalence_proof.py)
exists on main but its claimed equivalence does **not** hold
symbolically on H_2.

Most production mass-derivation scripts (proton, neutron, deuteron,
axiomatic Markov, recursive Markov) call `tr_M_symbolic` (the
hoefsmit_symbolic variant); the Q_β precision-ladder framework
cites the Jones-Markov weight $y_\lambda$ via
`thm:jones-markov-trace`, which corresponds to `tr_M_canonical`.
**These are not interchangeable.**

### Where exactly they differ

**Numerical check at q_0** (the substrate parameter, q_0 ≈ 1.10998):

| Implementation | $\text{tr}_M(\sigma_1^2)$ at $q_0$ |
|---|---:|
| `tr_M_symbolic` (Hoefsmit) | 1.0163158... |
| `tr_M_canonical` (Wenzl y_λ) | 1.1043881... |
| **$\|\Delta\|$** | **0.0881 (~8% relative)** |

They are genuinely different functions, **not** the same math in
different coordinates. Both give +1 at q=1 (coincidence, because
several rational functions interpolate +1 → +1 around q=1 with
different slopes), but everywhere else they disagree.

**Difference 1 (formula):**

- `tr_M_symbolic`: $\text{tr}_M(\beta) = \sum_\lambda \frac{\dim_q^2(\lambda)}{[n]_q!} \cdot \frac{\chi^\lambda(\beta)}{f^\lambda}$ — divides by SYT count $f^\lambda$
- `tr_M_canonical`: $\text{tr}_M(\beta) = \sum_\lambda y_\lambda(q) \cdot \chi^\lambda(\beta)$ — uses Wenzl's principal-specialisation $y_\lambda = s_\lambda(1, Q, Q^2, \ldots, Q^{r-1}) / Z$ with the normalisation $Z = \sum_\mu s_\mu \cdot f^\mu$ to enforce $\text{tr}_M(1_{H_1}) = 1$, no $f^\lambda$ division at the per-irrep step.

These weights are NOT equal in general. For $n = 2$:

- Hoefsmit: $w_{(2)} = w_{(1,1)} = \frac{1}{[2]_q}$ (since $\dim_q = 1$ for both partitions of 2). After the $/f^\lambda = /1$ division, the formula gives $(q^4+1)/(q^3+q)$ on $\sigma_1^2$.
- Wenzl: $y_{(2)}$ and $y_{(1,1)}$ are Schur-principal-specialization values that absorb the $q^{1/2}$ coordinate (see Difference 2). They give the huge half-power rational function reported above.

**Difference 2 (coordinate system, the bigger issue):**

`markov_weights_symbolic` uses `SQ = sp.sqrt(Q)` to define the
**Wenzl Markov parameter** $z_W = 1 / (q^{1/2} + q^{-1/2})$. The
$q^{1/2}$ remains unevaluated symbolically because sympy treats
`Q_W = Q**2` (and hence `SQ`) as algebraically independent
symbols — sympy will not auto-simplify $\sqrt{Q^2}$ to $|Q|$ without
explicit assumption that $Q > 0$. As a result the output is
expressed in **$(q, q^{1/2})$ coordinates** with surviving
half-integer powers.

By contrast `hoefsmit_symbolic` uses `Q = q` directly and never
introduces $q^{1/2}$, so its output is in **pure $q$ coordinates**.

This **is** a coordinate-change issue. The two outputs may evaluate to
the same numerical value at any specific $q$ (and indeed both give $+1$
at $q = 1$ for $\sigma_1^2$), but the *symbolic representations* are
in different coordinate systems and cannot be directly subtracted.

The "Jones $q^{1/2}$ convention" (Jones 1985, Wenzl 1988) and the
"straight-$q$ convention" used by the rest of the QOU framework are
both standard; the literature is split. CLAUDE.md §7a does not
specify which one is canonical for the framework.

### Comparison to derivation documents

CLAUDE.md §7a notation register says:

> Jones polynomial: Always $J_K(q)$, never $V_K(t)$ or bracket with variable $A$.
> ...
> Markov parameter: plain italic, $z = 1/(q^{1/2} + q^{-1/2})$.

So the canonical Markov parameter is in $q^{1/2}$ coordinates — that's the
`tr_M_canonical` convention. But CLAUDE.md also says:

> $H_n(q)$ — always with subscript $n$; standard knot-theory convention.

— $q$, not $q^{1/2}$, is the Hecke deformation parameter. So Hecke
relations use $q$ while the Markov parameter uses $q^{1/2}$. This is
internally consistent in the *notation register* but it means
`tr_M_symbolic` (pure $q$, no $q^{1/2}$) is using a different
convention than CLAUDE.md prescribes.

The `y_lambda_equivalence_proof.py` script on main may bridge the two
conventions, but the *symbolic outputs* of the two `tr_M` engines do
not agree directly — and that's what most production scripts call.

Implication for PR #664's c_3 claim:

- Neither tr_M implementation gives $-2$ at $q=1$ for σ_1² (both give +1).
- The textbook Jones polynomial value $-2$ that PR #664 hardcodes
  arises from a *third* convention (Kauffman bracket with writhe
  correction, not from a Markov trace at all).
- Going from any of these to a Q_β precision-ladder coefficient $c_3$
  requires both an identified convention AND an order-$h^6$ expansion
  around $q=1$.

Resolution: ratify one tr_M implementation as canonical (likely
`tr_M_canonical` since CLAUDE.md's `thm:jones-markov-trace` and the
$y_\lambda$ weight is the literature-standard Jones-Markov form) and
audit downstream consumers. Until that happens, claims of the form
"c_k = some-textbook-value" are not derivable from the framework
without specifying which tr_M is meant.

## Finding 8 — writhe correction (or equivalent) IS needed

Empirical check on σ_1^k braids in H_2:

| Braid | Closure | Writhe | tr_M_QOU at q=1 | Textbook J at q=1 |
|---|---|---:|---:|---:|
| σ_1 | unknot | 1 | 0 | 1 |
| σ_1² | Hopf+ (2-comp) | 2 | +1 | −2 |
| σ_1³ | trefoil (1-comp) | 3 | 0 | 1 |
| σ_1⁴ | Solomon's seal (2-comp) | 4 | +1 | … |

Pattern: $\text{tr}_M^{\text{QOU}}(\sigma_1^k)|_{q=1}$ depends only on
parity of $k$ (even → +1, odd → 0, because of a Markov-parameter
factor $z = (q^2-1)/(q^2+1)$ that vanishes at $q=1$). The textbook
Jones values $(-2)^{c-1}$ depend on component count $c$, not parity.

There is **no single multiplicative factor** $N(q)$ depending only
on $n$ that satisfies $J = N \cdot \text{tr}_M$ across all braids:
the relationship between Markov trace and Jones polynomial requires
a writhe-and-stabilization-dependent correction. PR #664's claim
"$c_3 = J_\text{Hopf}(q=1) = -2$ from V_(2,1) Hoefsmit Markov trace"
elides this; the seminormal trace gives +1 at $q=1$, not −2.

## Summary of what is NOT canonically derived in PR #664

| Object | Status in PR #664 | Truly categorical? |
|---|---|---|
| c_3 = -2 | Tautological probe; hand-waved proof sketch | **No** — textbook Jones, asserted not derived |
| c_4 = 3/2 | Tautological probe (`c4 - c4 == 0`); `b = 1` asserted | **No** — even thinner than c_3 |
| κ closed form | Numerical match 0.035%; "identified empirically" then interpreted | **No** — fit-then-interpret |
| H7a quantum $E_0 \cdot \log(1/h)$ | Empirically anchored, refuted as universal by PR #654 | **No** — partial empirical structure |

| Object | Genuinely categorical? |
|---|---|
| c_2 = b² (PR #661, referenced) | **Yes** — symbolic Hoefsmit Markov trace, the template |

## Recommended next steps

1. **Walk back the "Story B structurally forced" wording in PR #671** —
   either un-merge or amend with a follow-up commit clarifying that
   PR #664's claim is consistency, not exclusion.
2. **Comment on PR #664** flagging the tautological c_3/c_4 probes and
   the fit-then-interpret κ formula (or close the PR pending genuine
   derivations).
3. **Write the genuine c_3 categorical probe** — port PR #661's c_2
   methodology to c_3:
   - Build the 2-strand Hoefsmit matrices for V_(2,1)
   - Compute the symbolic Markov trace of $\sigma_1^2$
   - Verify it equals $-(q + q^{-1})$ as a polynomial
   - Evaluate at $q = 1$
4. **Same for c_4** — port the methodology, extracting the order-h^8
   coefficient from the V_(2,1) tower.
5. **Defer κ closure** — first either (a) derive `log(1/h)` from
   categorical axioms or (b) replace it with an exact q-algebraic
   factor that gives κ to ~0 ppm (not 0.035%). Until then, κ should
   be labelled "empirical, structurally suggestive."

## CAL discipline

This review uses only CAL-1/CAL-2 framework knowledge. The c_3 = -2
empirical value (PR #655) and the textbook J_Hopf polynomial are public
facts; the review does not re-fit anything.

## Cross-references

- [PR #664](https://github.com/litlfred/qou/pull/664) — the PR under review
- [PR #661](https://github.com/litlfred/qou/pull/661) — c_2 = b² genuine categorical proof (template)
- [PR #655](https://github.com/litlfred/qou/pull/655) — empirical c_3 extraction
- [PR #657](https://github.com/litlfred/qou/pull/657) — Story A vs Story B framing
- [PR #670](https://github.com/litlfred/qou/pull/670) — Story B canonical-chain audit (now merged)
- [PR #671](https://github.com/litlfred/qou/pull/671) — Story B "forced not preferred" upgrade (this branch's PR; needs walk-back)
