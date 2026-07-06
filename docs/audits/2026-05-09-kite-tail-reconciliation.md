# Kite-tail reconciliation — PR #546 round-3 vs PR #545 D(u)

**Branch.** `claude/kite-tail-reconciliation`
**Witness.** [`kite-tail-reconciliation.witness.json`](../../computations/kite-tail-reconciliation.witness.json)
**Script.** [`kite_tail_reconciliation.py`](../../computations/kite_tail_reconciliation.py)
**Continues.** [PR #546 round-3 audit](../../docs/audits/2026-05-05-r-and-kite-tails-exploration.md) (kite-tail status was `FALSIFIED-naive-form`).

## TL;DR

The "kite-tail FALSIFIED" claim from PR #546 round-3 has TWO causes,
not one. Reconciling them:

1. **Kite-power discrepancy IS a sympy-reduction artefact.** ✓
   PR #546 round-3 used `sp.cancel` (full reduction); PR #545's
   $D(u) = 2^{2A+1}\cdot u^{\text{shift}} \cdot (1+u^2)^{3A-1}$
   describes the un-reduced (`sp.together`) form. The two differ
   by one shared $(1+u^2)$ factor between numerator and
   denominator. **Round-3 kite-power falsification: RETRACTED.**

2. **Prefactor + neutron-shift discrepancies at A=1 remain.** ✗
   Even in the un-reduced form, proton/neutron at A=1 don't fully
   match PR #545's prediction:

| Atom | $D(u)$ predicted | Observed (un-reduced sp.together) | Match? |
|---|---|---|---|
| proton (A=1) | $2^3 \cdot u^{19} \cdot (1+u^2)^2$ | $2^2 \cdot u^{19} \cdot (1+u^2)^2$ | shift ✓, kite ✓, **prefactor ✗** |
| neutron (A=1) | $2^3 \cdot u^{22} \cdot (1+u^2)^2$ | $2^2 \cdot u^{19} \cdot (1+u^2)^2$ | kite ✓, **shift ✗ (19 vs 22)**, **prefactor ✗** |
| deuteron (A=2) | $2^5 \cdot u^{40} \cdot (1+u^2)^5$ | $2^5 \cdot u^{40} \cdot (1+u^2)^5$ | **all three ✓** |

**Deuteron A=2 verifies PR #545's D(u) exactly** (in un-reduced form).
The A=1 discrepancies are SEPARATE — likely a different braid
encoding between `markov_peel.atom_braid_word_3A` (used by
`term6_residues_at_roots` and PR #546 round-3) and PR #545's
canonical word.

## Diagnostic

Run [`kite_tail_reconciliation.py`](../../computations/kite_tail_reconciliation.py)
to reproduce the table.

The script computes the canonical Markov trace via
`term6_residues_at_roots.tr_M_atomic`, lifts to $u$ via
`lift_q_to_u`, then factorises in BOTH `sp.together` (un-reduced)
and `sp.cancel` (reduced) forms. The kite power drops by 1
between the two forms because the numerator and denominator
share a $(1+u^2)$ factor that cancels under reduction:

```
together (un-reduced):  N_T(u) / [4·u^19·(u²+1)^2]
cancel (reduced):       N_C(u) / [4·u^19·(u²+1)^1]
                        with N_T = (u²+1) · N_C
```

Both forms compute the same canonical $\mathrm{tr}_M$ (`difference = 0`
under sp.simplify).

## Outstanding work for the A=1 prefactor / neutron-shift mismatch

Three reconciliation paths to test:

1. **Different braid encoding** — PR #545's $D(u)$ was derived
   for a specific braid word (likely the dressed atomic word with
   gluon entries from `mass_endomorphism.proton_cross`), while
   `markov_peel` uses `atom_braid_word_3A` from `mass_at_3A_proper`
   (without gluon entries). Verify whether running PR #545's
   $D(u)$ derivation against the markov_peel word reproduces the
   observed $2^2 \cdot u^{19}$ prefactor for both proton and
   neutron.

2. **Plancherel vs Markov trace normalisation** — the commit
   `58e78090e` ("Resolve factor-of-2 mismatch: PR #546 uses
   Plancherel trace, not Markov") flagged a related factor-of-2
   issue. The 8 vs 4 prefactor mismatch may be the same
   Plancherel-vs-Markov normalisation question, with PR #545's
   $D(u)$ in one convention and `markov_peel` in the other.

3. **Symmetric vs asymmetric word** — neutron observed shift = 19
   = proton observed shift, both equal to $18Z+21N+1|_{Z=1,N=0}$.
   This suggests `markov_peel`'s neutron word has the same shift
   as proton, which contradicts the per-nucleon $18Z+21N+1$
   formula. Possibly markov_peel's neutron word is identical to
   proton's word up to relabelling — verify by direct comparison
   of `atom_braid_word_3A(0, 1)` vs `atom_braid_word_3A(1, 0)`.

## Coordination

- **PR #545 author** — please compare your `D(u)` derivation
  braid word against `markov_peel.atom_braid_word_3A(Z, N)`.
  If they differ, document which is canonical for the six-term
  mass formula.
- **PR #600 (Δ_λ derivation race)** — the deuteron A=2 D(u)
  match means PR #545's closed form is reliable for $A \ge 2$
  applications (which is what binding-energy work needs).
- **PR #547 author** — your "factor-of-2 Plancherel-vs-Markov"
  finding may directly explain the proton/neutron prefactor
  mismatch. Worth cross-checking.

## Update — A=1 prefactor RESOLVED

**Finding (2026-05-09 follow-up).** The A=1 prefactor mismatch
(observed $2^2 = 4$ vs predicted $2^{2A+1} = 8$) is explained by a
**convention issue in PR #545's $2^{2A+1}$ formula**, NOT the braid
encoding.

PR #545's commit message [`bcafe0d1d`](https://github.com/litlfred/qou/commit/bcafe0d1d) (also referenced in [`d_u_closed_form_proof.py`](../../computations/d_u_closed_form_proof.py)) derives the $2^{2A+1}$
prefactor by counting averaged crossings:

> "each averaged crossing = $(\sigma + \sigma^{-1})/2$, contributing
> a factor of $1/2$: each nucleon has 2 averaged ud-pair couplings →
> $2A$ factors; canonical pppnnn ordering has exactly one mixed
> $(p,n)$ inter-nucleon interface → $+1$ more, total $2A+1$."

The `+1` from the p-n interface only applies when **both proton and
neutron nucleons are present**. At A=1 (just p OR just n), there is
no p-n interface, so the formula should be $2A + 0 = 2A$, giving
$2^2 = 4$ — exactly the observed value.

**Corrected formula.**

$$
\text{prefactor} = 2^{2A + \delta_{Z\,N}}, \qquad
\delta_{Z\,N} = \begin{cases} 1 & Z > 0 \text{ and } N > 0 \\ 0 & \text{otherwise.} \end{cases}
$$

Verification across all atoms (PR #545 Dprime table values from the
`d_u_closed_form_proof.py` history):

| Atom | Z, N, A | Avg crossings | Predicted $2^k$ | Observed | Match? |
|---|---|---|---|---|---|
| proton | 1, 0, 1 | $2A = 2$ | $2^2 = 4$ | $4$ | ✓ |
| neutron | 0, 1, 1 | $2A = 2$ | $2^2 = 4$ | $4$ | ✓ |
| deuteron | 1, 1, 2 | $2A + 1 = 5$ | $2^5 = 32$ | $32$ | ✓ |
| tritium | 1, 2, 3 | $2A + 1 = 7$ | $2^7 = 128$ | $128$ | ✓ |
| ³He | 2, 1, 3 | $2A + 1 = 7$ | $2^7 = 128$ | $128$ | ✓ |
| ⁴He | 2, 2, 4 | $2A + 1 = 9$ | $2^9 = 512$ | $512$ | ✓ |

**The corrected formula matches all atoms exactly.** PR #545's
$2^{2A+1}$ formula was off by one factor of 2 at A=1; the corrected
$2^{2A + \delta_{Z\,N}}$ closes the prefactor mismatch entirely.

## Update — Neutron shift discrepancy (still open)

The shift formula `18Z + 21N + 1` predicts:
- proton (Z=1, N=0): $18·1 + 21·0 + 1 = 19$ ✓ matches observed
- neutron (Z=0, N=1): $18·0 + 21·1 + 1 = 22$ ✗ observed shift is $19$

Even with the `+1` interface term removed for A=1 (yielding
predicted $21$ for neutron), the prediction still doesn't match
the observed $19$. The 3-unit gap is not yet explained by
crossing-count arithmetic.

**Hypothesis.** `markov_peel`'s symbolic reduction may absorb a
$u^3$ factor from the numerator into the denominator-cancellation
phase, lowering the apparent shift by 3 for the neutron word.
Verification deferred — would need to inspect the `markov_peel`
intermediate state.

## Status (revised)

- **Round-3 kite-power FALSIFICATION**: ✓ RETRACTED (sympy artefact, explained).
- **PR #545 D(u) at A=2**: ✓ verified exactly in un-reduced form.
- **A=1 prefactor mismatch**: ✓ RESOLVED — corrected formula $2^{2A+\delta_{ZN}}$.
- **Neutron shift (19 vs 22)**: ⚠ open — likely a `markov_peel` numerator-absorption artefact, deferred.

## ρ_K^LO tautology — direct binding formulation

The ρ_K mass formula
$\mathcal{M}(K) = \rho_K \cdot m_e \cdot |\mathrm{tr}_M(K)|$
with leading-order
$\rho_K^{\mathrm{LO}} = (Z m_p + N m_n)/(m_e\,|\mathrm{tr}_M|)$
has the $|\mathrm{tr}_M|$ factor cancel against itself, reducing
the LO contribution to the constituent sum $Z m_p + N m_n$. The
only physical content is the second-order correction
$(\Sigma_\lambda y_\lambda \chi^\lambda \Delta_\lambda) / |\mathrm{tr}_M|$,
equivalently the binding energy
$$
\mathrm{Binding}(K) = m_e \cdot \sum_\lambda y_\lambda(q)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K).
$$

The new
[`computations/binding_K_direct.py`](../../computations/binding_K_direct.py)
script computes this binding directly, surfacing the physical
content rather than packaging it through the ρ_K · m_e · |tr_M|
intermediate.  The legacy
[`atomic_mass_via_rho_k.py`](../../computations/atomic_mass_via_rho_k.py)
is retained as the LO baseline reference; both scripts now flag
the LO tautology in their docstrings.  The content block
[`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md)
has been rewritten to lead with the direct-binding formula.

## V̂_i ↔ Δ_λ bridge — universal 1-dim closure (corrected formulation)

**Probe.** [`v_hat_to_delta_lambda_bridge.py`](../../computations/v_hat_to_delta_lambda_bridge.py)
([witness](../../computations/v-hat-to-delta-lambda-bridge.witness.json))
tests whether the q-character $\chi^\lambda(\beta_K)$ that appears
in Option G's $\Delta_\lambda^G = (\text{target}/S) \cdot \chi^\lambda / d_\lambda$
factors through the per-generator volumes $\hat V_i^\lambda$ from
`wedderburn_pair_volumes.atom_per_generator_full_matrices`.

**Universal formula (1-dim channels, any A).**

$$
\boxed{\;\chi^{1\text{-dim}}(\beta_K) \;=\; \prod_i \hat V_i^{1\text{-dim}}\;}
\qquad \text{for } \dim V_\lambda = 1, \text{ any } A.
$$

### Proof

Let $\varphi: H_n(q) \to R$ be a one-dimensional irrep (an algebra
homomorphism with one-dimensional image; the trace $\chi^\varphi$
on $V_\varphi \cong R$ coincides with $\varphi$ itself).

The atomic braid is a finite product of crossing operators:
$$
\beta_K \;=\; \prod_{k=1}^{m} \big(c_k\,\sigma_{i_k} + d_k\,\mathbf 1\big) \in H_n(q),
$$
where $i_k \in \{0, \ldots, n-2\}$ is the generator index of the
$k$-th crossing and $(c_k, d_k) \in \{(1,0),\,(1,-h),\,(1,-h/2)\}$
encodes the crossing type $\sigma$, $\sigma^{-1}$, or averaged.

Apply $\varphi$:
$$
\varphi(\beta_K) \;=\; \prod_{k=1}^{m}\big(c_k\,\lambda_\varphi(i_k) + d_k\big),
\qquad \lambda_\varphi(i) := \varphi(\sigma_i).
$$
The image is a product in the commutative target ring $R$, so the
factors commute and we may regroup by generator index:
$$
\varphi(\beta_K) \;=\; \prod_{i=0}^{n-2}\;\prod_{\substack{k=1 \\ i_k = i}}^{m}\big(c_k\,\lambda_\varphi(i) + d_k\big)
\;=\;\prod_{i=0}^{n-2} \hat V_i^\varphi,
$$
where $\hat V_i^\varphi := \prod_{k:\,i_k=i}(c_k\,\lambda_\varphi(i) + d_k)$
is the per-generator volume in the $\varphi$-channel as computed by
[`wedderburn_pair_volumes.atom_per_generator_full_matrices`](../../computations/wedderburn_pair_volumes.py).

Since $\chi^\varphi = \varphi$ on a 1-dim irrep, we conclude
$\chi^\varphi(\beta_K) = \prod_i \hat V_i^\varphi$.  $\square$

The proof is **independent of $A$, of $n$, and of the inter-nucleon
braid structure** — it uses only the homomorphism property of
$\varphi$ and the commutativity of the target ring.  The $H_3$
1-dim irreps are `sym` ($\varphi(\sigma_i) = q$) and `alt`
($\varphi(\sigma_i) = -q^{-1}$); at $H_n$ for any $n$ the same two
1-dim irreps exist (corresponding to partitions $(n)$ and $(1^n)$).

(An earlier draft of this section used a $\sum_{i<j}(\hat V_i \hat V_j)_\lambda$
form that coincides with the product only at $A=1$ — only 2
generators, so a single pair-product equals the two-factor
product.  The proof above shows the **product** is the universal
form.)

**Result (proton, neutron at $H_3$ + deuteron at $H_6$).**

| Atom | A | Channel | $d_\lambda$ | $\chi^\lambda(\beta_K)$ | $\prod_i \hat V_i^\lambda$ | rel. error |
|---|---|---|---|---|---|---|
| proton | 1 | sym=(3) | 1 | $1.3824945145464$ | $1.3824945145464$ | $5\!\times\!10^{-17}$ ✓ |
| proton | 1 | alt=(1³) | 1 | $-0.7392235469701$ | $-0.7392235469701$ | $5\!\times\!10^{-17}$ ✓ |
| neutron | 1 | sym=(3) | 1 | $1.1221068372363$ | $1.1221068372363$ | $1\!\times\!10^{-16}$ ✓ |
| neutron | 1 | alt=(1³) | 1 | $-0.9107622062324$ | $-0.9107622062324$ | $2\!\times\!10^{-16}$ ✓ |
| deuteron | 2 | sym=(6) | 1 | $1.5597587394181$ | $1.5597587394181$ | $3\!\times\!10^{-16}$ ✓ |
| deuteron | 2 | alt=(1⁶) | 1 | $-0.6769250645272$ | $-0.6769250645272$ | $2\!\times\!10^{-17}$ ✓ |
| **tritium** | **3** | **sym=(9)** | 1 | $1.5768015283810$ | $1.5768015283810$ | $3\!\times\!10^{-16}$ ✓ |
| **tritium** | **3** | **alt=(1⁹)** | 1 | $-0.6843215231762$ | $-0.6843215231762$ | $1\!\times\!10^{-16}$ ✓ |
| **³He** | **3** | **sym=(9)** | 1 | $2.3935111147542$ | $2.3935111147542$ | $4\!\times\!10^{-16}$ ✓ |
| **³He** | **3** | **alt=(1⁹)** | 1 | $-0.4508185556344$ | $-0.4508185556344$ | $5\!\times\!10^{-17}$ ✓ |
| **⁴He** | **4** | **sym=(12)** | 1 | $2.4196639445339$ | $2.4196639445339$ | $4\!\times\!10^{-16}$ ✓ |
| **⁴He** | **4** | **alt=(1¹²)** | 1 | $-0.4557444491781$ | $-0.4557444491781$ | $2\!\times\!10^{-16}$ ✓ |
| proton std=(2,1) | 1 | 2 | $1.8077033200982$ | matrix tr ✗ no scalar | — |
| neutron std=(2,1) | 1 | 2 | $1.7008888500892$ | matrix tr ✗ no scalar | — |

**12/12 one-dimensional channels match to ~$10^{-16}$ precision** across
A=1, 2, 3, 4 (all six low-A atoms × two 1-dim channels each).
Therefore $\Delta_\lambda^G$ for 1-dim partitions factors as

$$
\Delta_\lambda^G(K) \;=\; \frac{\text{target}_K}{S_K} \cdot \frac{\prod_i \hat V_i^\lambda}{d_\lambda},
\qquad d_\lambda = 1.
$$

**The multi-dim irreps DON'T factor as a scalar V̂_i product**
because the trace is intrinsically $\mathrm{tr}\big(\prod_i M_i\big)$
with non-commuting matrices.  More importantly, the connection
between single-particle $\hat V_i$ and the LR-decomposition that
defines $\Delta_\lambda$ for atomic braids is **operator-valued**,
not scalar.  Per the existing audit
[`docs/audits/2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md)
(refined Sub-lemma 2.1, PR #534's branch, 11/11 verified at $10^{-15}$):

> Under the LR decomposition
> $V_\lambda \big|_{H_{n_1}(q) \otimes H_{n_2}(q)} = \bigoplus_{(\mu, \nu)} c^\lambda_{\mu, \nu} \cdot V_\mu \otimes V_\nu$,
> the action of any element involves an **operator-valued
> interface coefficient $A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu, \nu}}$**.

So the bridge $\hat V_i \to \Delta_\lambda$ for **multi-dim
irreps** runs through this operator-valued $A^\lambda_{\mu\nu}(I)$,
not a scalar product.  The scalar product formula
$\chi^{1\text{-dim}} = \prod_i \hat V_i^\lambda$ is the
**1-dim specialisation** of the refined operator-valued sub-lemma
— which is consistent with the existing audit's framing that
the scalar form (categorical proof in PR #539) suffices for
the W-3 maximizer at $V_{(1^p)}$ (1-dim column irrep), while the
operator-valued form is needed for the general multi-dim case.

**Closing multi-dim sectors** requires:
1. Direct matrix evaluation: $\chi^\lambda(\beta_K) = \mathrm{tr}\big(\prod_i M_i\big)$ via Hoefsmit (always works, no factorisation).
2. Operator-valued sub-lemma application: extract $A^\lambda_{\mu\nu}(I)$ for the inter-nucleon interface and combine with single-nucleon $\hat V_i$ blocks.
   This is the path PR #534's `sublemma_2_1_A_operator_extract.py`
   already implements; integrating it into the V̂_i ↔ Δ_λ
   bridge is a concrete next step.

**Implication for 1ppb mass precision.** For atomic structure
where the std channel contribution is small or its ratio is
constrained by symmetry (e.g. saturated shells), the 1-dim
bridge alone may suffice to pin $\Delta_\lambda$ from
single-particle $\hat V_i$.  For shells where std dominates,
the matrix-trace reconciliation is the next concrete step.

**Status (2026-05-09):** bridge **closed on 1-dim Wedderburn
channels** (substantive new result); std channel reconciliation
queued as follow-up.  The deuteron at $H_6$ has additional
generator handling required in `chi_lambda_symbolic`; that test
is queued separately.
