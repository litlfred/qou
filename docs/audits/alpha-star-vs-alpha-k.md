# Where α\* came from, what α_k is, and why they're different

A short note disambiguating two unrelated "α"s in the QOU
mass-derivation pipeline. Neither is fitted; both have explicit
algebraic / algorithmic origins.

## α_k — depth-k stratum prefactor (algebraic, exact, no fitting)

Defined in
[`prop:alpha-k-derivation-procedure`](../../content/quantum-observable-universe/braids-and-knots/alpha-k-derivation-procedure.md)
and made explicit at H_3 in
[`prop:explicit-alpha-k-h3`](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.md):

> α_k is the Markov-trace pairing of the trace functional with a
> chosen E_∞^{0,0}-page representative r_k of the depth-k class on
> the GB spectral sequence:  α_k = tr_M(r_k).

At H_3 the four explicit values are:

  α_0 = 1
  α_1 = 0
  α_2 = z²
  α_3 = h·z² + z = z·(1 + q^{1/2} − q^{−1/2})

where z = 1/(q^{1/2} + q^{−1/2}) and h = q − q^{−1}.

These are pure q-rational expressions in ℚ(q). **There is no
fitting.** They are computed by:
1. Solving the linear system Σ_λ χ_λ(w_μ) y_λ = z^{n−ℓ(μ)} for the
   y_λ Wenzl-bridge weights (alternatively via Wenzl-bridge closed
   form).
2. Pairing tr_M = Σ_λ y_λ χ_λ with each E_∞^{0,0}-page representative
   r_k (the Hecke-algebra basis class at depth k).
3. The result α_k(q) is exact rational in q for every k.

The α_k's enter Term 6 (residue-spectral-sum) of the unified mass
formula
([`thm:knot-mass-formula-unified`](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md))
and a prefactor in Terms 2 / 3 (single-generator and pair-generator
brane towers). They are **structural Wedderburn-decomposition
coefficients**, not numerical fudge factors.

## α\* — PSD-cone gap (single-number diagnostic, R5-minimal, presentation-dependent)

Defined in
[`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
§ "PSD-cone α\* ranking" (a recent addition from R5-minimal):

> α\*(𝔥) := max{α ∈ [0, 1] : α · ρ_λ(T_w) + (1−α) · I_{d_λ}  ⪰ 0  for all λ ⊢ n}

A single bisection variable. Implemented in
[`tools/hecke-engine/src/sdp_verifier.rs`](../../tools/hecke-engine/src/sdp_verifier.rs)
(commit
[`60d0ec2`](https://github.com/litlfred/qou/commit/60d0ec2)
"R5-minimal: PSD-cone α\* verifier (bisection; equivalent to SDP value function)").

### Origin

- The R5_FULL_PLAN.md roadmap called for an SDP-as-solver via
  Clarabel-rs, which requires system BLAS / LAPACK / gfortran.
- Awaiting BLAS, R5-minimal added a **bisection-based surrogate**
  for the SDP value function. The bisection on α tests whether the
  convex combination α·ρ + (1−α)·I has all-PSD blocks. The optimal
  α is the SDP value at q_0.
- **Not fitted.** The result is determined by the eigenvalues of
  the symmetric part of ρ_λ(T_w) at q_0 for each partition λ.
- **The point of the metric** was: for a candidate Hecke element
  T_w (e.g. the historical Borromean braid for proton, or 8_11 for
  ³H), if α\* = 1 then T_w is on the joint-tower SDP feasible set,
  and the historical T_w is a valid candidate for the canonical
  element. α\* < 1 was supposed to indicate "T_w is not on the
  feasible set, so the historical assignment is structurally
  inconsistent".

### Why the original interpretation was over-read

Per
[`docs/audits/h3-h2-h3-discrimination.md`](h3-h2-h3-discrimination.md):

- ρ_λ(T_w) is **non-symmetric** for d_λ ≥ 2 (Hoefsmit's seminormal
  matrices have upper-triangular plus 2×2-block form per σ_i;
  products are generically non-symmetric).
- The α\* test computes the symmetric *part* (M + M^T)/2, then
  checks PSD of that. The symmetric part of a generic non-symmetric
  matrix has both signs of eigenvalues.
- **α\* is not a Markov-class invariant.** Markov-equivalent braid
  words (same closure, same link, same tr_M) give different α\*.
  Empirically: proton's 6-letter Borromean at H_3 has α\* = 1,
  but the Markov-stabilized 8-letter version at H_5 has α\* < 1.
- "Natural" H_5 braids (e.g. σ_1 σ_2 σ_3 σ_4 σ_3 σ_2 σ_1, full
  half-twist Δ_5) all fail α\* < 1 at d_λ ≥ 4 — generically.

So **α\* < 1 doesn't refute the historical knot ID**. It records
that the specific braid representative has a non-PSD symmetric part
in some Wedderburn block — a generic property of multi-d
projections, not a structural anomaly.

### What α\* is good for

It is still a useful **per-representative consistency check**:
- α\* = 1 for proton/neutron/³He at H_3 confirms that the 6-letter
  Borromean is a "well-behaved" representative — its symmetric part
  is positive across all blocks at q_0. That's a non-trivial fact
  about that specific braid.
- α\* numbers are valid for comparing different braid-word
  representatives of the *same* link, e.g. asking which Markov
  representative of L_6a4 has the highest α\* for use in downstream
  numerical experiments.

What α\* is **not** good for: refuting historical knot IDs,
diagnosing which of the six terms in the unified mass formula
contributes the residual, or estimating how close a B_pred is to
B_AME.

## Summary table

| | α_k (stratum prefactor) | α\* (PSD-cone gap) |
|---|---|---|
| Defined in | prop:alpha-k-derivation-procedure | prop:atom-knot-mass-derivation §α\* ranking |
| Type | q-rational expression in ℚ(q) | real number ∈ [0, 1] at q = q_0 |
| Indexed by | depth k of GB spectral sequence | atom 𝔥 (one number per atom) |
| Computed how | Markov-trace pairing with E_∞-page representative r_k | bisection on α with eigenvalue check |
| Implementation | y_lambda_wenzl_bridge_extended.py + q_mn_recursive_memoized.py | tools/hecke-engine/src/sdp_verifier.rs |
| Fitted? | **No** — exact algebraic | **No** — bisection on a structural inequality |
| Markov-class invariant? | **Yes** (depends on link, not representative) | **No** (changes with representative) |
| Used in mass formula? | Yes — Terms 2, 3, 6 of the six-term formula | No — diagnostic only |
| 1 ppb relevance | High — drives the cyclotomic / Habiro expansion | Low — cannot be used to calibrate Bpred |

## Recommended action on the master prop

The "PSD-cone α\* ranking" subsection in
`prop:atom-knot-mass-derivation` should be reframed:

- **Before:** "α\* < 1 quantifies the gap from the PSD-cone
  boundary in the α-direction"; ³H listed with "5 of 7 blocks NOT
  PSD — *largest gap* in registry".
- **After:** Add a caveat that α\* is computed on a specific
  braid-word representative; that Markov-equivalent representatives
  give different α\*; and that α\* < 1 is generic for "natural"
  multi-strand braids and is not a structural refutation of the
  historical knot ID. The α\* ranking is a per-representative
  consistency check, useful for choosing well-behaved
  representatives, not a structural diagnostic.

The structural test for whether the historical knot ID K is
correct for atom 𝔥 is the **Markov-class-invariant** comparison:

  symbolic tr_M(T_w(𝔥), q)  ≟  J_K(q)  · q^k  for some integer k

(writhe normalisation factor q^k allowed). This test is implemented
in `atom_nf_symbolic_D.py` and the new `atomic_tr_m_mpfr_50dps.py`
(commit pending).
