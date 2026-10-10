> **DEPRECATED on 2026-05-24.** Point-in-time status, intermediate workplan iteration, dead-end exploration, or earlier sublemma version superseded by a later "refined" iteration. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T2 for the deprecation rationale.

# N_v categorical-derivation impasse — verdict (2026-05-05)

**Branch:** `claude/w3-followup-term6-integration`
**Companion to:**
[`2026-05-02-nv-frob-filter-conjectures.md`](2026-05-02-nv-frob-filter-conjectures.md),
[`2026-05-03-nv1-candidate-a-doubleprime-test.md`](2026-05-03-nv1-candidate-a-doubleprime-test.md),
[`2026-05-05-refocused-1ppb-workplan.md`](2026-05-05-refocused-1ppb-workplan.md).

## Summary

The numerical search for a closed-form $N_v$ over $\{q^k, [k]_q,
\hbar_q^k, W(q)\}$ bases is **exhausted**. PSLQ-style probes can find
"hits" below CODATA-$G_F$ tolerance ($5\times 10^{-7}$), but the basis
combinatorics make the false-discovery rate $\approx 1$. The path
forward is **categorical content authoring**, not more compute.

This audit closes the W-2 (real) numerical-search line and identifies
the next-step content blocks that must be authored before any
derivation of $N_v$ is possible.

## 1. Reminder of the gap

$$
  v_{\rm weak} = N_v \cdot E_\times \cdot \mu_0,
  \qquad
  E_\times = \tfrac{q-q^{-1}}{2},
  \qquad
  \mu_0 = \frac{m_e}{3 E_\times}.
$$

At $q_0$: $v_{\rm weak}/m_e \approx 481{,}839.82$, hence
$N_v = 3\,v_{\rm weak}/m_e \approx 1{,}445{,}519.45$. This is
**back-solved** from CODATA $G_F = 1.1663788\times 10^{-11}\,\text{MeV}^{-2}$;
no categorical input currently derives it. Hence $N_v$ is functioning
as a **fourth external calibration**, in violation of the
[three-calibration discipline](../../content/quantum-observable-universe/observations/three-calibration-discipline.md).

## 2. What we tried in this audit

A focused PSLQ-style probe at 50-dps over the basis

$$
  v_{\rm weak} / m_e \;\stackrel{?}{=}\;
  \text{INT} \cdot [3]_q^{a_3} \cdot [5]_q^{a_5}
  \cdot [9]_q^{a_9} \cdot [10]_q^{a_{10}}
  \cdot h^b \cdot q^L,
$$

with $\text{INT} \in \{1, 2, 3, \ldots, 720\}$ (23 small integers
including $\binom{10}{2} = 45$, $|S_5| = 120$, $|S_6| = 720$),
exponents $a_k \in [-4, 4]$, $b \in [-2, 2]$, and $L$ chosen as the
nearest integer.

**Tolerance:** $5\times 10^{-7}$ relative (CODATA-$G_F$ floor — below
this, the target itself has measurement noise).

**Result:** 30 candidates with relative error $< 5 \times 10^{-6}$
(i.e. within an order of magnitude of the CODATA floor); 6 with
$< 5\times 10^{-7}$. Top three:

| INT | $[3]_q$ | $[5]_q$ | $[9]_q$ | $[10]_q$ | $h$ | $q^L$ | rel err |
|-----|--------:|--------:|--------:|---------:|----:|------:|--------:|
| 24  | $-1$ | $1$  | $-1$ | $3$  | $2$  | $q^{71}$  | $8.9\times 10^{-8}$ |
| 120 | $-1$ | $3$  | $1$  | $-1$ | $1$  | $q^{59}$  | $1.3\times 10^{-7}$ |
| 72  | $4$  | $4$  | $-1$ | $-3$ | $0$  | $q^{72}$  | $2.2\times 10^{-7}$ |

These hits **are not derivations**. The basis has $23 \times 9^4 \times 5
\approx 7.5 \times 10^{5}$ combinations searched; the expected number of
chance hits below tolerance $\tau$ over the integer-$L$ grid is roughly
$|\text{basis}| \cdot \tau$, which gives $\sim 0.4$ at $\tau =
5\times 10^{-7}$ and $\sim 4$ at $\tau = 5\times 10^{-6}$ — consistent
with what we observe.

**Multi-q test impossible.** $N_v$ is q-independent (it absorbs CODATA
$G_F$, not a substrate quantity), so we cannot disambiguate
candidates by varying $q$. This is the structural reason the search
is unable to converge.

## 3. Why this is the honest verdict

The successful $1/\alpha_{\rm EM}$ derivation (PR #543, AXKIA branch)
followed a **structural** pipeline:

1. **strand-count** at the relevant place (10 = Bring genus-4 torus knots);
2. **force-carrier sector** (`prop:force-carrier-bring-uniqueness`:
   $\{T_{2,9}, T_{3,5}\}$);
3. **Plancherel completeness** (`thm:em-spectral-completeness`:
   $w_+ + w_- = 1$);
4. **closed-form ansatz** built from upstream blocks ($45 \cdot [3]_q
   \cdot \hbar_q^4 [5]_q$);
5. **PSLQ as uniqueness witness** at 1000-dps — confirming no shorter
   form, *not* discovering the form.

For $N_v$, **steps 1–3 do not yet exist as content blocks.** No
authored block in the paper currently:

- identifies the weak-place strand count;
- identifies $W^\pm, Z$ as specific torus knots (the
  [unmapped-torus-knots.md](../../content/quantum-observable-universe/braids-and-knots/unmapped-torus-knots.md)
  remarks are speculation, not propositions);
- states the SU(2) idempotent decomposition of any candidate weak
  carrier.

Without these, step 4 (closed-form ansatz) has no upstream source,
and step 5 (PSLQ) collapses into the brute-force search done above —
which is what the false-positive rate predicts.

## 4. Required content-authoring blocks — competing paths

Per the source audit
([2026-05-02-nv-frob-filter-conjectures.md](2026-05-02-nv-frob-filter-conjectures.md))
two paths are on the table:

- **Path α (links):** force-carrier sector is $\{T(2,4), T(2,6),
  T(2,8)\}$ — torus *links* on three distinct hosts (genus 1, 2, 3).
  This path is **already authored** as
  [`conj:weak-spectral-completeness`](../../content/quantum-observable-universe/braids-and-knots/weak-spectral-completeness.md).
  Closure depends on three prerequisite conjectures
  (`conj:force-carrier-knot-vs-link-dichotomy`,
  `conj:electroweak-mass-eigenstate-count`, plus a Plancherel
  normalization $\mathcal{N}_{\rm sym}(q)$).
- **Path β (knots):** force-carrier is the $T_{3,5}$ torus *knot*
  acting as a unified weak/EM mediator. This path has paper-internal
  evidence (the [knot-particle-dictionary.md](../../content/quantum-observable-universe/braids-and-knots/knot-particle-dictionary.md)
  lists $T_{3,5}$ alongside $10_{124}$ as "weak force ($\beta$-decay)")
  but **is not yet authored** as a proposition.

The two paths are **mutually exclusive** as currently stated: path α
requires links (host-distinct), path β requires a single knot. A
choice between them is an architectural decision that touches
`conj:force-carrier-knot-vs-link-dichotomy` and is outside the
scope of this audit.

| Path | Status | Next-step authoring |
|------|--------|---------------------|
| α (links) | partially authored: `conj:weak-spectral-completeness` exists; gated on three prereq conjectures | discharge prereqs; author $\mathcal{N}_{\rm sym}(q)$ |
| β (knots) | not yet authored | (would conflict with path α) author `prop:t35-as-weak-mediator` |
| **PSLQ uniqueness witness** | gated on either path completing | 1000-dps probe on extended basis (path-specific) |

**No N_v derivation is possible without one of these paths
completing.** The numerical search closed in §2–3 was over the
*unextended* basis (no path-α $[2k]_q^2/[2]_q$ factors, no path-β
$T_{3,5}$ Markov trace as a structural input); that is why the
search did not converge.

The available T_{3,5} structural inputs (already computed):

- $W(q) := \mathrm{tr}_M((\sigma_1\sigma_2)^5) \approx 0.7035538$ in
  $H_3(q_0)$
  ([`t35-weak-vertex.witness.json`](../../computations/t35-weak-vertex.witness.json)).
- 10 crossings split as electron(3) + neutrino(0) + re-reduction(7).
- Trefoil and unknot Markov traces on the embedded sub-braids.

These supply *raw material* for the closed-form ansatz, but without
the upstream completeness/uniqueness propositions they cannot
constrain a closed form well enough to PSLQ at CODATA tolerance.

## 5. Coordination notes

- **PR #546 leading-coefficient discrepancy.** A new push
  (`claude/hoefsmit-2x2-fix` commit
  [`d3f04a9a2`](https://github.com/litlfred/qou/commit/d3f04a9a2))
  reports the **deuteron** symbolic Markov trace leading coefficient
  as $+1/128 = +2^{-7}$ (positive), in the
  $\mathrm{tr}_M / [6]_q!$ normalization
  ([`deuteron_tr_M_symbolic.witness.json`](https://github.com/litlfred/qou/blob/claude/hoefsmit-2x2-fix/computations/deuteron_tr_M_symbolic.witness.json)).
  This **further contradicts** PR #546's universal $-1/8$
  conjecture. The $A=2$ value is positive, not negative, and three
  orders of magnitude smaller than $-1/8$. The reconciliation is
  that the three values measure three different normalizations:
  - $-1/8$ (PR #546): claimed universal D(u) prefactor at A=1 in
    one convention.
  - $+2^A$ (mine, D(u) closed form): D(u) prefactor in canonical
    Markov-trace convention via Wenzl-bridge.
  - $+1/128$ (hoefsmit-2x2-fix): tr_M leading-low residue *with*
    [6]_q! normalization included.
  Each is internally consistent in its convention. The dispute
  reduces to which normalization the paper exposes, **not** a
  mathematical contradiction.

## 6. Verdict

- **Numerical $N_v$-derivation search closed.** The 50-dps probe
  over a 7.5×10⁵-element basis is unable to distinguish derivation
  from chance hit at CODATA tolerance.
- **Action shifts to content authoring.** The next concrete step
  is `prop:t35-as-weak-mediator` (path β, step 1). This is a
  collaborator-level skill task, not a numerical compute.
- **Without `prop:t35-as-weak-mediator`, $N_v$ remains the
  fourth de-facto calibration input** and the
  three-calibration-discipline gap stands.

## 7. Files

- This audit:
  [`docs/audits/2026-05-05-nv-categorical-impasse.md`](2026-05-05-nv-categorical-impasse.md)
- Predecessor audit:
  [`docs/audits/2026-05-02-nv-frob-filter-conjectures.md`](2026-05-02-nv-frob-filter-conjectures.md)
- Falsification of candidate (a″):
  [`docs/audits/2026-05-03-nv1-candidate-a-doubleprime-test.md`](2026-05-03-nv1-candidate-a-doubleprime-test.md)
- Existing T_{3,5} weak-vertex compute:
  [`computations/t35-weak-vertex.witness.json`](../../computations/t35-weak-vertex.witness.json)
- Existing N_v numerology probe:
  [`computations/probes/nv-categorical-derivation-probe.witness.json`](../../computations/probes/nv-categorical-derivation-probe.witness.json)
